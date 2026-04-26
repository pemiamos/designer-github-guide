#!/usr/bin/env python3
"""
HCI Encyclopedia → Obsidian Exporter
=====================================
将 Notion 里的《人机交互百科全书》(2nd Ed.) 全部导出为 Markdown，
保存到 Obsidian vault 的 HCI百科 文件夹。

使用方法：
    python3 export_hci_to_obsidian.py

运行前请填写下方的 NOTION_TOKEN。
"""

import os
import re
import time
import json
import requests
from pathlib import Path

# ─── 配置 ────────────────────────────────────────────────────────────────────

NOTION_TOKEN = "NOTION_TOKEN_REMOVED"   # ← 填入你的 Notion Integration Token（secret_xxx）

# 输出目录：Obsidian vault 里的 HCI百科 文件夹
OUTPUT_DIR = Path.home() / "Library/Mobile Documents/iCloud~md~obsidian/Documents/HCI百科"

# ─── 章节列表（page_id → 文件名前缀）────────────────────────────────────────

CHAPTERS = [
    ("ba4b1c08acae41fa9b6b34782876a321", "CH01 - Interaction Design"),
    ("32ec3638cbb240d299e73747f78b179e", "CH02 - Human Computer Interaction"),
    ("b0f7a8af7afe405a9dcc4a7ee33c9604", "CH03 - User Experience and Experience Design"),
    ("056210a1bd114f1f98bb7d87b6db29fd", "CH04 - Social Computing"),
    ("22f5c8186c7c4da08b24ad31744856a4", "CH05 - Visual Representation"),
    ("bc7e2361f52a40d1b046f810b553de7a", "CH06 - Industrial Design"),
    ("c91ce21fa61b4d6389f8f4bdfde97cfb", "CH07 - Bifocal Display"),
    ("574ffbe339f049c0abc64d5b08b6ace3", "CH08 - Contextual Design"),
    ("7c35528e0d474429b4610399df597fc6", "CH09 - Mobile Computing"),
    ("3017ab97cb3c4e0f9cc931a2b2cc86ba", "CH10 - End-User Development"),
    ("332fa03e3aad40688dfd46ec236a6a98", "CH11 - Philosophy of Interaction"),
    ("0b9e35a5bf5e497183f151a351ce5b48", "CH12 - Affective Computing"),
    ("97d4de22f8a84c349b3d6c1c04ff9613", "CH13 - Requirements Engineering"),
    ("6840a26311fa49f2ab10c6ccc401d5e1", "CH14 - Context-Aware Computing"),
    ("d405fe40837c439ca0765ac27c108ae7", "CH15a - Usability Evaluation"),
    ("c8ed924207fb4571919f943f9fdd341f", "CH15b - Usability Evaluation (2)"),
    ("d0fed14320a44f0aaf6cb5d58fcd6d56", "CH16 - Activity Theory"),
    ("a6a404967a7a4331b124018c988ddfc2", "CH17 - Disruptive Innovation"),
    ("800f9e2fb85748af83f47a698cc6ad63", "CH18 - Open User Innovation"),
    ("a9fb8ab8718041b9af2f2c49823c78c3", "CH19a - Visual Aesthetics"),
    ("5b61edd1c31e485c96fbcb435477e929", "CH19b - Visual Aesthetics (2)"),
    ("69119776b5b1481f8d18f32d5061a56e", "CH20 - Tactile Interaction"),
    ("49a5290afdfe4e01a01169640a610ca4", "CH21 - Somaesthetics"),
    ("7710eb7fef8a4bd0a856d0e169ce57be", "CH22 - Card Sorting"),
    ("a1506241eef04f949b22653ea86cb38d", "CH23 - Wearable Computing"),
    ("3ae5a0c607fc4f11ad2494ac0a911cdb", "CH24a - Socio-Technical System Design"),
    ("9576f84653a142da89b38251a7067154", "CH24b - Socio-Technical System Design (2)"),
    ("c0b0dc5308c142ca95fafa659036e731", "CH24c - Socio-Technical System Design (3)"),
    ("b6cc841f2fc64cfaa8c9cecf75b6665d", "CH25 - Semiotics"),
    ("5262b51c208b4516a41904c9a39f035e", "CH26 - Aesthetic Computing"),
    ("8c2f3fc7c19a4892b6e9aac64cfa6ff4", "CH27 - Computer Supported Cooperative Work"),
    ("41d90b1cd61d428e8abdac95e26fbdc1", "CH28 - Phenomenology"),
    ("c70a4787fb7a4636991677b9533890d9", "CH29 - Formal Methods"),
    ("7caaf54970ab4bec8de0a656622bb349", "CH30 - Personas"),
    ("fd37ec966b72427f833db8dd049829ae", "CH31 - Ethnography"),
    ("be2ba0263ae7404183fede7ce0e9d876", "CH32 - 3D User Interfaces"),
    ("c9f22a06e9bd484fa0ee40fd3e8d11f9", "CH33 - Action Research"),
    ("e662fea1a5864df7bca1b4b7be4c95d3", "CH34 - Experimental Methods in HCI"),
    ("fed37581f3af40bf83c800ad0924c3ca", "CH35 - Data Visualization for Human Perception"),
    ("17859438d87e419abca84c8ab3d1fa24", "CH38a - Human-Robot Interaction"),
    ("189442856f2a45bf8ef75c34bd7af4c8", "CH38b - Human-Robot Interaction (2)"),
    ("e805d3b5cca944ddb4030727ca105397", "CH39 - User Interface Design Adaptation"),
    ("ddc1f6314cff4c2086e742d369c289b4", "CH40 - Emotion and Website Design"),
    ("c230f13c8f4a41078ee1afa2c6bd93b6", "CH41 - Human-Data Interaction"),
    ("05ca9616d00e45ada16e3198bb1fc907", "CH42 - Design for All"),
    ("4126e95ab3364b3782d98251af06d8c1", "CH43 - Research through Design"),
    ("2cebd50516e54ce5a00858b313b6b6ca", "CH44 - Affordances"),
    ("c4ec7cf5af024f7d906df8f954472eca", "CH52 - Semi-Structured Qualitative Studies"),
    ("448baae89fa04d30b2cdbf272acab381", "CH53 - Service Design"),
]

# ─── Notion API 工具函数 ──────────────────────────────────────────────────────

HEADERS = {}

def setup_headers():
    global HEADERS
    HEADERS = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    }

def get_page(page_id: str) -> dict:
    url = f"https://api.notion.com/v1/pages/{page_id}"
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return resp.json()

def get_blocks(block_id: str) -> list:
    """获取一个 block 的所有子 block（自动分页）。"""
    blocks = []
    url = f"https://api.notion.com/v1/blocks/{block_id}/children"
    cursor = None
    while True:
        params = {"page_size": 100}
        if cursor:
            params["start_cursor"] = cursor
        resp = requests.get(url, headers=HEADERS, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        blocks.extend(data.get("results", []))
        if not data.get("has_more"):
            break
        cursor = data.get("next_cursor")
        time.sleep(0.3)  # 避免触发 rate limit
    return blocks

# ─── Block → Markdown 转换 ────────────────────────────────────────────────────

def rich_text_to_md(rich_texts: list) -> str:
    """将 Notion rich_text 数组转换为 Markdown 字符串。"""
    result = []
    for rt in rich_texts:
        text = rt.get("plain_text", "")
        ann = rt.get("annotations", {})
        href = rt.get("href")

        # 处理格式
        if ann.get("code"):
            text = f"`{text}`"
        if ann.get("bold"):
            text = f"**{text}**"
        if ann.get("italic"):
            text = f"*{text}*"
        if ann.get("strikethrough"):
            text = f"~~{text}~~"
        if href:
            text = f"[{text}]({href})"
        result.append(text)
    return "".join(result)

def blocks_to_md(blocks: list, depth: int = 0) -> str:
    """将 block 列表递归转换为 Markdown。"""
    lines = []
    indent = "  " * depth

    for block in blocks:
        btype = block.get("type", "")
        bdata = block.get(btype, {})
        rt = bdata.get("rich_text", [])
        text = rich_text_to_md(rt)

        if btype == "paragraph":
            lines.append(f"{indent}{text}" if text else "")
        elif btype == "heading_1":
            lines.append(f"\n# {text}\n")
        elif btype == "heading_2":
            lines.append(f"\n## {text}\n")
        elif btype == "heading_3":
            lines.append(f"\n### {text}\n")
        elif btype == "bulleted_list_item":
            lines.append(f"{indent}- {text}")
        elif btype == "numbered_list_item":
            lines.append(f"{indent}1. {text}")
        elif btype == "quote":
            lines.append(f"{indent}> {text}")
        elif btype == "code":
            lang = bdata.get("language", "")
            code_text = "".join(rt_item.get("plain_text", "") for rt_item in rt)
            lines.append(f"```{lang}\n{code_text}\n```")
        elif btype == "divider":
            lines.append("---")
        elif btype == "callout":
            emoji = bdata.get("icon", {}).get("emoji", "💡")
            lines.append(f"> {emoji} {text}")
        elif btype == "toggle":
            lines.append(f"**{text}**")
        elif btype == "image":
            url = bdata.get("file", {}).get("url") or bdata.get("external", {}).get("url", "")
            caption = rich_text_to_md(bdata.get("caption", []))
            lines.append(f"![{caption}]({url})")
        elif btype == "synced_block":
            # synced_block 分两种：
            # 1. synced_from == null → 这是原始块，内容在其子块里（has_children 处理）
            # 2. synced_from.block_id → 这是复制块，需去原始块 ID 拉子块
            synced_from = bdata.get("synced_from")
            if synced_from and synced_from.get("block_id"):
                original_id = synced_from["block_id"]
                try:
                    original_children = get_blocks(original_id)
                    child_md = blocks_to_md(original_children, depth)
                    if child_md.strip():
                        lines.append(child_md)
                    time.sleep(0.2)
                except Exception as e:
                    lines.append(f"<!-- synced 原始块加载失败：{e} -->")
                continue  # 跳过下面的 has_children 处理，避免重复
        elif btype == "child_page":
            title = bdata.get("title", "")
            lines.append(f"- 📄 {title}")
        elif btype == "table":
            # 表格在下面递归处理
            pass
        elif btype == "table_row":
            cells = bdata.get("cells", [])
            row_texts = [rich_text_to_md(cell) for cell in cells]
            lines.append("| " + " | ".join(row_texts) + " |")
        elif btype == "column_list":
            # 分栏布局：把各栏内容顺序输出
            pass  # 子块是 column，column 的子块才是内容，由 has_children 递归处理
        elif btype == "column":
            pass  # 内容在子块里，由 has_children 处理

        # 递归处理子块
        if block.get("has_children"):
            try:
                child_blocks = get_blocks(block["id"])
                if btype == "table":
                    # 表格：第一行后插入分隔线
                    child_lines = []
                    for i, cb in enumerate(child_blocks):
                        cells = cb.get("table_row", {}).get("cells", [])
                        row_texts = [rich_text_to_md(cell) for cell in cells]
                        child_lines.append("| " + " | ".join(row_texts) + " |")
                        if i == 0:
                            child_lines.append("|" + "|".join(["---"] * len(cells)) + "|")
                    lines.extend(child_lines)
                else:
                    child_md = blocks_to_md(child_blocks, depth + 1)
                    if child_md.strip():
                        lines.append(child_md)
                time.sleep(0.2)
            except Exception as e:
                lines.append(f"<!-- 子块加载失败：{e} -->")

    return "\n".join(lines)

# ─── 主流程 ───────────────────────────────────────────────────────────────────

def export_chapter(page_id: str, filename: str, output_dir: Path, force: bool = False) -> bool:
    """导出单章到 Markdown 文件。"""
    out_path = output_dir / f"{filename}.md"
    if out_path.exists() and not force:
        print(f"  ⏭  已存在，跳过：{filename}")
        return True

    try:
        # 获取页面标题
        page = get_page(page_id)
        title_prop = page.get("properties", {}).get("title", {})
        title_texts = title_prop.get("title", [])
        title = "".join(t.get("plain_text", "") for t in title_texts).strip()
        title = re.sub(r"^\*+|\*+$", "", title).strip()  # 去掉加粗符号

        print(f"  📥 正在导出：{filename} ({title})")

        # 获取所有 blocks
        blocks = get_blocks(page_id)

        # 转换为 Markdown
        content = blocks_to_md(blocks)

        # 加文件头
        header = f"""# {title}

**来源**：The Encyclopedia of Human-Computer Interaction, 2nd Ed.
**Notion 原页面**：https://www.notion.so/{page_id.replace('-', '')}

---

"""
        full_content = header + content

        # 写入文件
        out_path.write_text(full_content, encoding="utf-8")
        print(f"  ✅ 完成：{out_path.name}")
        return True

    except requests.HTTPError as e:
        print(f"  ❌ HTTP 错误：{filename} → {e}")
        return False
    except Exception as e:
        print(f"  ❌ 导出失败：{filename} → {e}")
        return False


def create_index(output_dir: Path):
    """创建目录索引文件。"""
    lines = [
        "# 🧠 HCI 百科全书 - 目录索引",
        "",
        "**The Encyclopedia of Human-Computer Interaction, 2nd Ed.**",
        "",
        "来源：[Interaction Design Foundation](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed)",
        "",
        "---",
        "",
        "| 章节 | 主题 | 文件 |",
        "|------|------|------|",
    ]
    for page_id, filename in CHAPTERS:
        chapter_num = filename.split(" - ")[0]
        topic = filename.split(" - ", 1)[1] if " - " in filename else filename
        lines.append(f"| {chapter_num} | {topic} | [[{filename}]] |")

    lines += ["", "---", "", f"共 {len(CHAPTERS)} 个章节", ""]
    index_path = output_dir / "📚 HCI百科 - 目录索引.md"
    index_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"✅ 索引文件已生成：{index_path.name}")


def main():
    import sys
    force = "--force" in sys.argv  # 传入 --force 则覆盖已有文件

    if not NOTION_TOKEN:
        print("❌ 请先填写脚本顶部的 NOTION_TOKEN！")
        return

    setup_headers()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"📂 输出目录：{OUTPUT_DIR}")
    print(f"📋 共 {len(CHAPTERS)} 个章节待导出{'（强制覆盖模式）' if force else ''}\n")

    success, failed = 0, []
    for i, (page_id, filename) in enumerate(CHAPTERS, 1):
        print(f"[{i}/{len(CHAPTERS)}]", end=" ")
        ok = export_chapter(page_id, filename, OUTPUT_DIR, force=force)
        if ok:
            success += 1
        else:
            failed.append(filename)
        time.sleep(0.5)  # 避免 rate limit

    # 生成索引
    create_index(OUTPUT_DIR)

    print(f"\n{'='*50}")
    print(f"✅ 成功导出：{success} 章")
    if failed:
        print(f"❌ 失败：{len(failed)} 章")
        for f in failed:
            print(f"   - {f}")
    print(f"📂 文件已保存到：{OUTPUT_DIR}")


if __name__ == "__main__":
    main()
