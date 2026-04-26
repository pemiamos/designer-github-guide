#!/usr/bin/env python3
"""
HCI百科图片下载脚本
用法：python3 download_images.py
图片会下载到脚本所在目录，按章节前缀命名。
"""

import re
import os
import ssl
import time
import urllib.request
from pathlib import Path

# 跳过 SSL 证书验证（Mac 上 Python 3 常见问题）
SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

# ── 路径配置 ──────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent                          # 图片存放目录（脚本所在文件夹）
HCI_DIR    = SCRIPT_DIR.parent                              # HCI百科目录

# ── 图片 URL 提取正则 ────────────────────────────────────
# 排除 ] 和空白，防止 Markdown 链接格式把多余内容带入 URL
IMG_PATTERN = re.compile(
    r'https://public-media\.interaction-design\.org'
    r'/images/encyclopedia/[^\s)\]"\']+\.(?:jpg|jpeg|png|gif|webp)',
    re.IGNORECASE
)

# ── 章节前缀提取（从文件名）───────────────────────────────
def get_prefix(filename: str) -> str:
    """从文件名提取章节前缀，如 'CH03'、'CH15a'"""
    m = re.match(r'^(CH\w+)', filename)
    return m.group(1) if m else "UNKNOWN"

# ── 下载单张图片 ─────────────────────────────────────────
def download(url: str, dest: Path) -> bool:
    if dest.exists():
        print(f"  ⊙ 已存在，跳过：{dest.name}")
        return True
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30, context=SSL_CTX) as resp:
            data = resp.read()
        dest.write_bytes(data)
        print(f"  ✓ {dest.name}  ({len(data)//1024} KB)")
        return True
    except Exception as e:
        print(f"  ✗ 失败：{url}\n    原因：{e}")
        return False

# ── 主流程 ───────────────────────────────────────────────
def main():
    md_files = sorted([
        f for f in HCI_DIR.glob("CH*.md")
        if "翻译" not in f.name and "目录" not in f.name
    ])

    if not md_files:
        print("❌ 找不到章节 .md 文件，请确认脚本位置正确。")
        return

    total_ok = total_fail = total_skip = 0

    for md_file in md_files:
        prefix = get_prefix(md_file.name)
        content = md_file.read_text(encoding="utf-8")
        urls = list(dict.fromkeys(IMG_PATTERN.findall(content)))  # 去重，保持顺序

        if not urls:
            continue

        print(f"\n📂 {md_file.name}  →  {len(urls)} 张图片")

        for i, url in enumerate(urls, 1):
            # 从 URL 提取原始文件名
            raw_name = url.split("/")[-1].split("?")[0]
            ext = Path(raw_name).suffix or ".jpg"
            dest_name = f"{prefix}_{i:02d}_{raw_name}"
            dest_path = SCRIPT_DIR / dest_name

            if dest_path.exists():
                total_skip += 1
                print(f"  ⊙ [{i}/{len(urls)}] 已存在，跳过")
                continue

            ok = download(url, dest_path)
            if ok:
                total_ok += 1
            else:
                total_fail += 1

            time.sleep(0.3)  # 礼貌延迟，避免请求过快

    print(f"\n{'─'*50}")
    print(f"完成！成功 {total_ok} 张 · 跳过 {total_skip} 张 · 失败 {total_fail} 张")
    print(f"图片保存在：{SCRIPT_DIR}")

if __name__ == "__main__":
    main()
