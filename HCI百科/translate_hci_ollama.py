#!/usr/bin/env python3
"""
HCI 百科 Ollama 翻译脚本 (智能跳过参考文献版)
===========================================
功能：
1. 自动检测并跳过 References / 参考文献 章节。
2. 强制粉碎长文本，解决 48000+ 字符导致的超时。
3. 绕过系统代理，直连本地 Ollama。
4. 支持 --repair 模式只翻译未完成部分。
"""

import re
import sys
import time
import argparse
import requests
from pathlib import Path

# ─── 配置 ─────────────────────────────────────────────────────────────────────

OLLAMA_BASE   = "http://localhost:11434"
DEFAULT_MODEL = "gemma4:31b"
HCI_DIR       = Path(__file__).parent
CHUNK_CHARS   = 1500        # 每次送给模型的字符上限
SUFFIX        = " 翻译"     # 译文文件名后缀

# ─── 翻译提示词 ───────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """\
你是一位专业的学术翻译，擅长人机交互、设计研究、认知科学领域。
将以下英文学术 Markdown 翻译为简体中文，要求：
1. 保留所有 Markdown 格式（标题、加粗、斜体、代码块、链接、表格）
2. 专业术语首次出现时附英文原文，如「可供性（Affordance）」
3. 人名、书名、期刊名保留原文
4. 语言自然流畅，符合中文学术习惯
5. 只输出翻译结果，不要解释或说明
"""

# ─── Ollama 调用 ──────────────────────────────────────────────────────────────

def list_models():
    r = requests.get(f"{OLLAMA_BASE}/api/tags", timeout=10)
    r.raise_for_status()
    return [m["name"] for m in r.json().get("models", [])]


def translate_chunk(text: str, model: str) -> str:
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": text},
        ],
        "stream": False,
        "options": {"temperature": 0.2},
    }
    # 强制绕过代理，超时设为 1200 秒
    r = requests.post(
        f"{OLLAMA_BASE}/api/chat", 
        json=payload, 
        timeout=1200, 
        proxies={"http": "", "https": ""} 
    )
    r.raise_for_status()
    return r.json()["message"]["content"].strip()


# ─── 辅助判断：是否需要翻译 ───────────────────────────────────────────────────

def needs_translation(text: str) -> bool:
    """通过统计中文字符数量判断"""
    chinese_chars = re.findall(r'[\u4e00-\u9fff]', text)
    return len(chinese_chars) < 15


# ─── Markdown 分块（暴力防御版）───────────────────────────────────────────

def split_markdown(text: str, max_chars: int = CHUNK_CHARS) -> list[str]:
    # 按标题切分
    heading_pattern = re.compile(r'^(#{1,3} .+)$', re.MULTILINE)
    positions = [m.start() for m in heading_pattern.finditer(text)]
    if not positions or positions[0] != 0:
        positions.insert(0, 0)
    positions.append(len(text))

    chunks, buf = [], ""
    for i in range(len(positions) - 1):
        section = text[positions[i]:positions[i+1]]
        
        # 如果单块过长（如参考文献列表），按行强制切碎
        if len(section) > max_chars:
            if buf.strip():
                chunks.append(buf.rstrip())
                buf = ""
            lines = section.split('\n')
            temp = ""
            for line in lines:
                if len(temp) + len(line) > max_chars and temp:
                    chunks.append(temp.rstrip())
                    temp = line + '\n'
                else:
                    temp += line + '\n'
            if temp.strip():
                chunks.append(temp.rstrip())
        else:
            if len(buf) + len(section) > max_chars and buf:
                chunks.append(buf.rstrip())
                buf = section
            else:
                buf += section
                
    if buf.strip():
        chunks.append(buf.rstrip())
    return chunks


# ─── 文件翻译 ────────────────────────────────────────────────────────────────

def translated_path(src: Path) -> Path:
    return src.parent / f"{src.stem}{SUFFIX}{src.suffix}"


def translate_file(src: Path, model: str, force: bool = False, repair: bool = False) -> bool:
    dest = translated_path(src)

    if repair:
        if not dest.exists():
            return True
        print(f"  🔧 修复模式：{dest.name}")
        text = dest.read_text(encoding="utf-8")
    else:
        if dest.exists() and not force:
            print(f"  ⏭  跳过已存在文件：{dest.name}")
            return True
        text = src.read_text(encoding="utf-8")

    chunks = split_markdown(text)
    total  = len(chunks)
    parts  = []
    
    # 核心状态机：是否处于参考文献区域
    is_skipping_refs = False

    print(f"  📄 {src.name}（共 {total} 块）")
    for idx, chunk in enumerate(chunks, 1):
        # 1. 检查标题，判断是否进入或退出参考文献区域
        header_match = re.match(r'^(#{1,3})\s+(.+)', chunk)
        if header_match:
            title = header_match.group(2).lower()
            if "reference" in title or "参考文献" in title:
                is_skipping_refs = True
            else:
                # 如果遇到了新的非参考文献标题，恢复翻译
                is_skipping_refs = False

        # 2. 如果正在跳过参考文献
        if is_skipping_refs:
            print(f"     [{idx}/{total}] {len(chunk)} 字符... ⏩ [参考文献区域] 直接保留")
            parts.append(chunk)
            continue

        # 3. 修复模式下的中文检测
        if repair and not needs_translation(chunk):
            print(f"     [{idx}/{total}] {len(chunk)} 字符... ⏭ 已是中文，跳过")
            parts.append(chunk)
            continue

        # 4. 执行翻译
        print(f"     [{idx}/{total}] {len(chunk)} 字符...", end=" ", flush=True)
        t0 = time.time()
        try:
            result = translate_chunk(chunk, model)
            parts.append(result)
            print(f"✅ {time.time()-t0:.1f}s")
        except Exception as e:
            print(f"❌ 失败保留原文: {e}")
            parts.append(chunk)   
        time.sleep(0.2)

    dest.write_text("\n\n".join(parts) + "\n", encoding="utf-8")
    return True


# ─── 主流程 ──────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model",  default=DEFAULT_MODEL)
    parser.add_argument("--force",  action="store_true")
    parser.add_argument("--repair", action="store_true")
    parser.add_argument("--file",   nargs="+")
    args = parser.parse_args()

    try:
        models = list_models()
    except Exception as e:
        print(f"❌ 无法连接 Ollama：{e}")
        sys.exit(1)

    if args.file:
        files = [HCI_DIR / f for f in args.file]
    else:
        files = sorted(f for f in HCI_DIR.glob("CH*.md") if SUFFIX not in f.stem)

    print(f"📚 任务启动 | 模型：{args.model} | 模式：{'修复' if args.repair else '常规'}\n")

    for f in files:
        if not f.exists(): continue
        translate_file(f, model=args.model, force=args.force, repair=args.repair)

    print(f"\n{'='*50}\n✅ 处理完成！")


if __name__ == "__main__":
    main()