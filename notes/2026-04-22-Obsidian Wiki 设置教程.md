# Obsidian Wiki 设置教程

> **写给 Claude 的操作说明**
>
> 本文档是一份可执行的安装向导。你（Claude）负责引导用户完成从零到可用的完整设置。
> 配合《Wiki自动化处理设置教程.md》一起使用，两份文档覆盖全部步骤。
>
> **执行前请先问用户以下三个问题：**
> 1. 操作系统是 macOS 还是 Windows？（本教程针对 macOS，Windows 需调整部分路径）
> 2. Obsidian vault 打算放在哪里？（iCloud / 本地 Documents / 其他）
> 3. 打算用哪个 Ollama 模型？（运行 `ollama list` 查看已有模型）

---

## 一、系统概述

这套系统由三部分组成：

```
Obsidian（笔记库）
  └── Clippings/      ← Web Clipper 保存文章到这里
  └── RAW/            ← 处理完的文章移到这里归档
  └── Claude/         ← Wiki 知识库（你的第二大脑）
        ├── 学习日志   ← 所有文章的时间线索引
        ├── 提示词模板库
        ├── Skills库
        └── 知识库-xxx  ← 按主题分类的深度笔记

clipping_watcher.py（自动处理脚本）
  └── 监控 Clippings/ → 调用 Ollama → 写入 Wiki → 存入 RAW/

Ollama（本地大模型）
  └── 负责分类判断和内容生成，完全本地运行，无隐私风险
```

**工作流：** 在浏览器里点一下 Web Clipper → 等几分钟 → 打开 Obsidian 看到文章已整理进 Wiki。

---

## 二、前置软件清单

| 软件 | 用途 | 下载地址 |
|------|------|---------|
| Obsidian | 笔记库主体 | [obsidian.md](https://obsidian.md) |
| Obsidian Web Clipper | 浏览器保存文章 | Chrome 应用商店搜索 "Obsidian Web Clipper" |
| Ollama | 本地运行大模型 | [ollama.com](https://ollama.com) |
| Python 3.9+ | 运行自动化脚本 | macOS 自带，或 [python.org](https://python.org) |

---

## 三、步骤一：安装软件

### 3.1 安装 Obsidian

1. 下载并安装 Obsidian
2. 打开后选择「Create new vault」
3. Vault 名称建议：`Obsidian`
4. 存放位置根据用户选择：

**iCloud 同步（推荐，多设备可用）：**
- 选择路径：`iCloud 云盘` → 新建文件夹 `Obsidian`
- 实际磁盘路径：`~/Library/Mobile Documents/iCloud~md~obsidian/Documents/`

**本地存储：**
- 选择路径：`~/Documents/Obsidian/`
- 实际磁盘路径：`~/Documents/Obsidian/`

> **请让用户确认 vault 实际路径。** 在终端运行以下命令找到确切路径：
> ```bash
> find ~/Library/Mobile\ Documents -name "*.md" -maxdepth 4 2>/dev/null | head -3
> # 如果看到 iCloud~md~obsidian 开头的路径，说明用的是 iCloud 存储
> ```

### 3.2 安装 Ollama 并下载模型

```bash
# 安装 Ollama（访问 ollama.com 下载安装包，或用 brew）
brew install ollama

# 启动 Ollama 服务
ollama serve &

# 下载推荐模型（选一个，取决于电脑配置）
ollama pull gemma4:26b    # 推荐：质量最好，需要 16GB+ 内存
ollama pull qwen2.5:14b   # 备选：中文支持好，需要 8GB+ 内存
ollama pull llama3.2:3b   # 轻量：低配电脑用，速度快但质量一般

# 确认模型已下载
ollama list
```

### 3.3 安装 Python 依赖

```bash
pip3 install watchdog requests python-frontmatter
```

### 3.4 安装 Web Clipper

1. 在 Chrome / Edge 应用商店搜索「Obsidian Web Clipper」
2. 安装后点击扩展图标 → 进入设置
3. 填入 vault 路径和保存文件夹（见步骤四）

---

## 四、步骤二：创建 Wiki 文件夹结构

> **让 Claude 执行：** 根据用户确认的 vault 路径，在终端创建以下目录结构。

### 4.1 创建必要文件夹

将 `VAULT_ROOT` 替换为用户的实际 vault 根目录路径：

```bash
# 以 iCloud 存储为例（根据用户实际情况替换路径）
VAULT_ROOT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents"

mkdir -p "$VAULT_ROOT/Clippings"
mkdir -p "$VAULT_ROOT/RAW"
mkdir -p "$VAULT_ROOT/Claude"

echo "文件夹创建完成："
ls "$VAULT_ROOT"
```

### 4.2 创建 Wiki 核心文件

**让 Claude 依次创建以下文件，内容见附录。**

需要创建的文件列表：

| 文件名 | 说明 |
|--------|------|
| `Claude/📅 学习日志.md` | 时间线索引，所有文章必记 |
| `Claude/📚 Wiki 主页.md` | 总导航 |
| `Claude/Wiki操作指南.md` | Claude 的工作规则（每次会话先读） |
| `Claude/提示词模板库.md` | 提示词收藏 |
| `Claude/🛠 Skills库.md` | AI 工具技能包 |
| `Claude/知识库-AI工具评估.md` | AI 工具深度整理 |
| `Claude/知识库-AI与教育.md` | AI 与认知/教育反思 |
| `Claude/知识库-编程与工具.md` | 编程/开发工具 |
| `Claude/知识库-设计系统.md` | UI/UX 设计 |
| `Claude/知识库-GitHub×设计师.md` | GitHub 与设计师 |

---

## 五、步骤三：配置 Web Clipper

1. 点击浏览器里的 Obsidian Web Clipper 图标
2. 进入 Settings（设置）
3. 填写配置：

| 设置项 | 填写内容 |
|--------|---------|
| Vault | 你的 vault 名称（如 `Obsidian`） |
| Default folder | `Clippings` |
| Default template | 保持默认或选 Clippings 模板 |
| File name | 建议用 `{{title}}` |

4. 保存后测试：在任意网页点击 Web Clipper → 保存到 Clippings

---

## 六、步骤四：配置自动化处理

> 详细说明见《Wiki自动化处理设置教程.md》，这里只列关键步骤。

### 6.1 下载脚本

将 `clipping_watcher.py` 放入 Claude 文件夹（见附录，内含完整脚本代码）。

### 6.2 修改配置

打开 `clipping_watcher.py`，找到顶部配置区，按实际路径修改：

```python
# 根据 vault 位置修改
VAULT_ROOT = Path.home() / "Library" / "Mobile Documents" / "iCloud~md~obsidian" / "Documents"
# 本地存储改为：
# VAULT_ROOT = Path.home() / "Documents" / "Obsidian"

MODEL = "gemma4:26b"   # 改成 ollama list 里的实际模型名
TIMEOUT = 180          # 如果模型很慢，可以改为 300
```

### 6.3 测试运行

```bash
python3 "$VAULT_ROOT/Claude/clipping_watcher.py"
```

看到 `✅ 监控已启动` 即为成功。用 Web Clipper 保存一篇文章，观察终端输出。

### 6.4 设置开机自启动

**将路径中的 `amos` 替换为用户实际用户名（`echo $HOME` 查看）：**

```bash
cat > ~/Library/LaunchAgents/com.username.clipping-watcher.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.username.clipping-watcher</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/Users/你的用户名/Library/Mobile Documents/iCloud~md~obsidian/Documents/Claude/clipping_watcher.py</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/Users/你的用户名/clipping_watcher.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/你的用户名/clipping_watcher.log</string>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/usr/local/bin:/usr/bin:/bin:/opt/homebrew/bin</string>
    </dict>
</dict>
</plist>
EOF

launchctl load ~/Library/LaunchAgents/com.username.clipping-watcher.plist
launchctl list | grep clipping
```

---

## 七、步骤五：在 Cowork 中使用 Wiki

每次打开 Cowork 和 Claude 协作时：

1. 把 `Wiki操作指南.md` 发给 Claude（或让 Claude 读取该文件）
2. Claude 会立即理解 Wiki 结构，可以直接处理任何 Clipping 或对话摘要
3. 不需要每次重新解释规则

**日常工作流：**

```
浏览文章 → Web Clipper 一键保存
    ↓
自动处理（2～5分钟）
    ↓
打开 Obsidian 查看学习日志和知识库
    ↓
想深入某篇？打开 Cowork 让 Claude 继续分析
```

---

## 附录 A：Wiki 文件模板

> **给 Claude 的指令：** 请用下方模板逐一创建这些文件。创建前先确认 vault 根目录路径。

---

### A1：📅 学习日志.md

```markdown
# 📅 学习日志

每条记录一行。完整内容在对应知识库或独立文件里。

← [返回 Wiki 主页](./📚%20Wiki%20主页.md)

---

## 快速导航

| 去哪 | 链接 |
|------|------|
| 提示词（即取即用） | [📋 提示词模板库](./提示词模板库.md) |
| Skills（工具扩展） | [🛠 Skills库](./🛠%20Skills库.md) |
| AI 工具评估 | [知识库](./知识库-AI工具评估.md) |
| AI 与教育 | [知识库](./知识库-AI与教育.md) |
| 编程与工具 | [知识库](./知识库-编程与工具.md) |
| 设计系统 | [知识库](./知识库-设计系统.md) |

---

## 日志（倒序）

| 日期 | 内容 | 标签 | 位置 |
|------|------|------|------|

---

_新条目加在日志表格第一行 ↑_
```

---

### A2：📚 Wiki 主页.md

```markdown
# 📚 Wiki 主页

我的个人知识库导航。

---

## 知识库

| 主题 | 文件 | 说明 |
|------|------|------|
| AI 工具评估 | [→ 打开](./知识库-AI工具评估.md) | AI 工具、插件深度整理 |
| AI 与教育 | [→ 打开](./知识库-AI与教育.md) | AI 对认知、学习的影响 |
| 编程与工具 | [→ 打开](./知识库-编程与工具.md) | 编程、vibe-coding、开发工具 |
| 设计系统 | [→ 打开](./知识库-设计系统.md) | UI/UX 设计系统 |
| GitHub × 设计师 | [→ 打开](./知识库-GitHub×设计师.md) | GitHub 与设计相关 |

---

## 工具库

| 工具 | 文件 |
|------|------|
| 提示词模板库 | [→ 打开](./提示词模板库.md) |
| Skills 库 | [→ 打开](./🛠%20Skills库.md) |

---

## 日志

[📅 学习日志](./📅%20学习日志.md) · 时间线索引，所有文章的入口
```

---

### A3：Wiki操作指南.md

```markdown
# Wiki 操作指南（CLAUDE.md）

> 这是给 Claude 看的系统说明。每次新会话开始时，先把这个文件发给 Claude，它就能立刻理解结构、直接干活，不需要重新解释。

**Wiki 主人：** [填入你的名字]
**用途：** 记录与 Claude 协作的日常学习，兼顾归档和查询
**平台：** Obsidian（本地）+ Cowork（Claude 桌面端）双轨

---

## 一、文件结构

```
Claude/
├── Wiki操作指南.md        ← 本文件，每次会话开始先读
├── 📚 Wiki 主页.md        ← 总导航
├── 📅 学习日志.md         ← 时间线索引，每条一行
├── 提示词模板库.md        ← 即取即用的提示词
├── 🛠 Skills库.md         ← 技能包，按「我要做什么」查找
│
├── 知识库-AI工具评估.md
├── 知识库-AI与教育.md
├── 知识库-编程与工具.md
├── 知识库-设计系统.md
└── 知识库-GitHub×设计师.md
```

**Obsidian Clippings 文件夹**（在 Claude 文件夹之外）：
- 原始收藏，未处理状态
- 自动化脚本处理后，加 `processed: true` frontmatter 并移入 RAW/

---

## 二、如何处理 Clippings

每次用户发来 Clipping 文件，按以下流程判断：

### 第一步：判断价值等级

| 等级 | 标准 | 处理方式 |
|------|------|---------|
| A 级 | 有独特洞察，值得深度整理 | 进对应知识库 + 学习日志加一行 |
| B 级 | 有用信息，无需展开 | 学习日志加一行，记录要点 |
| C 级 | 重复或价值低 | 只在学习日志加一行「已存档」 |

### 第二步：判断归宿

| 内容类型 | 归入 |
|---------|------|
| 提示词 / Claude 使用技巧 | 提示词模板库 |
| AI 工具、插件、技能包 | Skills库 或 知识库-AI工具评估 |
| 设计相关 | 知识库-设计系统 或 知识库-GitHub×设计师 |
| AI 与教育、认知、反思 | 知识库-AI与教育 |
| 编程、vibe-coding、开发工具 | 知识库-编程与工具 |
| 不属于以上任何类别 | 新建对应知识库文件 |

### 第三步：写入学习日志

无论 A/B/C 级，**必须在学习日志加一行**：
```
| 日期 | 内容描述（一句话） | #标签 | 位置链接或「已存档」 |
```

### 第四步：标记 Clipping 为已处理

在原 Clipping 文件 frontmatter 加：
```yaml
processed: true
processed_date: YYYY-MM-DD
destination: 知识库-XX / 提示词模板库 / 已存档
```

---

## 三、学习日志格式

**每行格式：**
```
| 日期 | 内容一句话描述 | #标签 | 链接（可选） |
```

**标签体系：**
`#知识学习` · `#技术编程` · `#提示词` · `#工作效率` · `#写作创作` · `#设计` · `#AI工具`

---

## 四、知识库条目格式

每个知识库文件顶部有索引表，新增条目：

**索引表加一行：**
```
| 条目标题 | 类型 | 链接或说明 |
```

**正文条目结构：**
```markdown
## 条目标题 <a id="anchor-id"></a>

> 日期 · 来源（可选）

**一句话：** 这个东西是什么 / 解决什么问题

**核心内容：**
（要点、表格、代码块等，保持精简）

**我的判断：**
（值得用吗？什么场景？局限是什么？）
```

---

## 五、新建知识库文件

当内容不属于任何现有知识库时，新建文件：

**命名格式：** `知识库-主题名.md`

**文件结构：**
```markdown
# 知识库 · 主题名

← [返回 Wiki 主页](./📚%20Wiki%20主页.md)

---

## 文章索引

| 主题 | 类型 | 链接 |
|------|------|------|

---
```

新建后，在 `📚 Wiki 主页.md` 的知识库表格里加一行。

---

*最后更新：[创建日期]*
```

---

### A4：知识库文件通用模板

以下模板适用于所有 `知识库-xxx.md` 文件。创建时替换「主题名」：

```markdown
# 知识库 · 主题名

← [返回 Wiki 主页](./📚%20Wiki%20主页.md)

---

## 文章索引

| 主题 | 类型 | 链接 |
|------|------|------|

---
```

按此模板创建以下文件（主题名替换）：
- `知识库-AI工具评估.md` → 主题名：AI工具评估
- `知识库-AI与教育.md` → 主题名：AI与教育
- `知识库-编程与工具.md` → 主题名：编程与工具
- `知识库-设计系统.md` → 主题名：设计系统
- `知识库-GitHub×设计师.md` → 主题名：GitHub×设计师

---

### A5：提示词模板库.md

```markdown
# 📋 提示词模板库

直接复制使用。按场景找，不按来源找。

← [返回 Wiki 主页](./📚%20Wiki%20主页.md)

---

## 快速索引

| 分类 | 直达 |
|------|------|
| （随内容增加自动填充） | |

---
```

---

### A6：🛠 Skills库.md

```markdown
# 🛠 Skills 库

可直接调用的技能包。按「我要做什么」查找。

← [返回 Wiki 主页](./📚%20Wiki%20主页.md)

---

## 快速索引

| 我要做… | 跳转 |
|---------|------|
| （随内容增加自动填充） | |

---
```

---

## 附录 B：clipping_watcher.py 完整代码

> **给 Claude 的指令：** 将以下代码保存为 `Claude/clipping_watcher.py`，修改顶部配置区后即可使用。

```python
#!/usr/bin/env python3
"""
Clipping Auto-Processor
=======================
监控 Clippings 文件夹，新文件出现时自动调用本地 Ollama 处理，
写入 Wiki 知识库，更新学习日志，标记 frontmatter，移入 RAW 文件夹。

依赖安装：
    pip3 install watchdog requests python-frontmatter
"""

import re
import sys
import json
import time
import shutil
import logging
import threading
import requests
import frontmatter
from datetime import datetime
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ─────────────────────────────────────────────
#  ⚙️  配置区（必须修改）
# ─────────────────────────────────────────────

# Obsidian vault 根目录
# iCloud 存储：
VAULT_ROOT = Path.home() / "Library" / "Mobile Documents" / "iCloud~md~obsidian" / "Documents"
# 本地存储（按需取消注释）：
# VAULT_ROOT = Path.home() / "Documents" / "Obsidian"

CLIPPINGS_DIR = VAULT_ROOT / "Clippings"
RAW_DIR       = VAULT_ROOT / "RAW"
WIKI_DIR      = VAULT_ROOT / "Claude"

OLLAMA_URL = "http://localhost:11434"
MODEL      = "gemma4:26b"   # ← 改成 ollama list 里的实际名称
TIMEOUT    = 180            # 超时秒数，慢模型可改为 300
DEBOUNCE_SECONDS = 3

# ─────────────────────────────────────────────
#  📝  日志配置
# ─────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(Path.home() / "clipping_watcher.log", encoding="utf-8"),
    ],
)
log = logging.getLogger(__name__)

# ─────────────────────────────────────────────
#  🗂  Wiki 文件路径映射（按需新增）
# ─────────────────────────────────────────────

WIKI_FILES = {
    "学习日志":      WIKI_DIR / "📅 学习日志.md",
    "提示词模板库":  WIKI_DIR / "提示词模板库.md",
    "Skills库":     WIKI_DIR / "🛠 Skills库.md",
    "AI工具评估":   WIKI_DIR / "知识库-AI工具评估.md",
    "AI与教育":     WIKI_DIR / "知识库-AI与教育.md",
    "GitHub设计师": WIKI_DIR / "知识库-GitHub×设计师.md",
    "设计系统":     WIKI_DIR / "知识库-设计系统.md",
    "编程与工具":   WIKI_DIR / "知识库-编程与工具.md",
}

DEST_ALIAS = {
    "提示词模板库":       "提示词模板库",
    "skills库":           "Skills库",
    "ai工具评估":         "AI工具评估",
    "知识库-ai工具评估":  "AI工具评估",
    "ai与教育":           "AI与教育",
    "知识库-ai与教育":    "AI与教育",
    "github×设计师":      "GitHub设计师",
    "github设计师":       "GitHub设计师",
    "知识库-github×设计师":"GitHub设计师",
    "设计系统":           "设计系统",
    "知识库-设计系统":    "设计系统",
    "编程与工具":         "编程与工具",
    "知识库-编程与工具":  "编程与工具",
    "学习日志":           "学习日志",
}

# ─────────────────────────────────────────────
#  🤖  Ollama API
# ─────────────────────────────────────────────

def ollama_chat(system_prompt: str, user_prompt: str, json_mode: bool = False) -> str:
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt},
        ],
        "stream": False,
        "options": {"temperature": 0.1, "num_predict": 4096},
    }
    if json_mode:
        payload["format"] = "json"
    try:
        resp = requests.post(f"{OLLAMA_URL}/api/chat", json=payload, timeout=TIMEOUT)
        resp.raise_for_status()
        return resp.json()["message"]["content"].strip()
    except requests.exceptions.ConnectionError:
        raise RuntimeError(f"无法连接 Ollama（{OLLAMA_URL}）。请确保 Ollama 正在运行：ollama serve")
    except Exception as e:
        raise RuntimeError(f"Ollama API 错误：{e}")

# ─────────────────────────────────────────────
#  📋  提示词（可按需修改知识库分类描述）
# ─────────────────────────────────────────────

SYSTEM_CLASSIFY = """你是一个个人知识库管理助手。分析 Obsidian Clipping 文件，判断价值等级和归宿。

## Wiki 结构
- 学习日志：时间线索引，每条一行，所有文章都要加
- 提示词模板库：提示词/Claude 使用技巧
- Skills库：AI 工具技能包、Claude Skills
- 知识库-AI工具评估：AI 工具、插件评估
- 知识库-AI与教育：AI 与教育、认知、反思类
- 知识库-GitHub×设计师：GitHub 与设计相关
- 知识库-设计系统：UI/UX 设计系统
- 知识库-编程与工具：编程、vibe-coding、开发工具

## 价值等级
- A级：有独特洞察，值得深度整理 → 进知识库 + 学习日志
- B级：有用信息，无需展开 → 只记学习日志一行
- C级：重复或价值低 → 学习日志记「已存档」

## 输出合法 JSON：
{
  "value_level": "A" | "B" | "C",
  "destination": "目标文件名（如：知识库-AI工具评估 或 提示词模板库）",
  "log_entry_text": "一句话描述（不含日期和标签）",
  "tags": "#标签1 #标签2",
  "reason": "简短判断理由"
}

标签只能从以下选择：#知识学习 #技术编程 #提示词 #工作效率 #写作创作 #设计 #AI工具
"""

SYSTEM_GENERATE = """你是一个个人知识库管理助手。根据 Clipping 内容生成符合 Wiki 格式的条目。

## 目标知识库 → 对应格式

### 知识库-xxx（AI工具评估、编程与工具等）：
```markdown
## 条目标题 <a id="anchor-id"></a>

> 日期 · 来源（如有）

**一句话：** 这个东西是什么 / 解决什么问题

**核心内容：**
（用表格、要点列表，保持精简）

**我的判断：**
（值得用吗？什么场景？局限是什么？）
```

### 提示词模板库：
```markdown
### 提示词名称

> 日期 · 来源

**适用场景：** 一句话说明

```prompt
（提示词原文）
```
```

### Skills库：
```markdown
## Skill名称

> 日期 · 来源

**一句话：** 解决什么问题

**使用方法：**（关键步骤）

**我的判断：** 适合场景/局限
```

## 要求
- 直接输出 markdown，不加说明文字
- anchor-id 用小写英文+连字符
- 日期格式：YYYY-MM-DD
- 内容控制在 300 字以内
"""

# ─────────────────────────────────────────────
#  📄  文件操作
# ─────────────────────────────────────────────

def read_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception as e:
        log.warning(f"读取文件失败 {path}: {e}")
        return ""


def append_to_wiki(dest_key: str, content: str) -> bool:
    path = WIKI_FILES.get(dest_key)
    if not path or not path.exists():
        log.error(f"目标文件不存在：{dest_key} → {path}")
        return False
    try:
        header_match = re.search(r'^## (.+?)\s*<a id="([^"]+)"', content, re.MULTILINE)
        entry_title = header_match.group(1).strip() if header_match else None
        anchor_id   = header_match.group(2).strip() if header_match else None

        separator = "\n---\n" if dest_key not in ("提示词模板库", "Skills库") else "\n"
        with open(path, "a", encoding="utf-8") as f:
            f.write("\n" + content.strip() + separator)
        log.info(f"已写入 {path.name}")

        if dest_key in ("提示词模板库", "Skills库"):
            log.info("提示词/Skills 条目已追加，索引由用户手动维护")
        elif entry_title and anchor_id:
            wiki_text = path.read_text(encoding="utf-8")
            index_row = f"| {entry_title} | 工具评估 | [↓ 本文](#{anchor_id}) |"
            table_pattern = re.compile(
                r'(\| 主题 \|.*?\n\|[-| ]+\|\n)((?:\|.*\|\n)*)', re.DOTALL
            )
            m = table_pattern.search(wiki_text)
            if m:
                new_text = (
                    wiki_text[:m.start(2)] + m.group(2) + index_row + "\n" + wiki_text[m.end(2):]
                )
                path.write_text(new_text, encoding="utf-8")
                log.info(f"索引表已更新：{entry_title}")
        return True
    except Exception as e:
        log.error(f"写入失败 {path}: {e}")
        return False


def insert_log_entry(entry_text: str, tags: str, dest_link: str) -> bool:
    log_path = WIKI_FILES["学习日志"]
    if not log_path.exists():
        log.error("学习日志文件不存在")
        return False
    today = datetime.now().strftime("%Y-%m-%d")
    new_row = f"| {today} | {entry_text} | {tags} | {dest_link} |"
    content = log_path.read_text(encoding="utf-8")
    header_pattern = re.compile(r"\| 日期 \|.*?\n\|[-| ]+\|\n", re.DOTALL)
    match = header_pattern.search(content)
    if match:
        insert_pos = match.end()
        new_content = content[:insert_pos] + new_row + "\n" + content[insert_pos:]
    else:
        new_content = content.rstrip() + "\n" + new_row + "\n"
    try:
        log_path.write_text(new_content, encoding="utf-8")
        log.info(f"学习日志已更新：{new_row[:60]}...")
        return True
    except Exception as e:
        log.error(f"学习日志写入失败：{e}")
        return False


def mark_frontmatter(file_path: Path, destination: str) -> bool:
    today = datetime.now().strftime("%Y-%m-%d")
    try:
        post = frontmatter.load(str(file_path))
        post["processed"] = "true"
        post["processed_date"] = today
        post["destination"] = destination
        content = frontmatter.dumps(post)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except Exception as e:
        log.error(f"Frontmatter 标记失败 {file_path}: {e}")
        return False


def move_to_raw(file_path: Path) -> bool:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    dest = RAW_DIR / file_path.name
    try:
        shutil.move(str(file_path), str(dest))
        log.info(f"已移入 RAW：{file_path.name}")
        return True
    except Exception as e:
        log.error(f"移动文件失败：{e}")
        return False


def resolve_dest_key(dest_str: str) -> str:
    normalized = dest_str.lower().replace(" ", "").replace("_", "")
    for alias, key in DEST_ALIAS.items():
        if alias.replace(" ", "") in normalized or normalized in alias.replace(" ", ""):
            return key
    return ""

# ─────────────────────────────────────────────
#  🧠  核心处理逻辑
# ─────────────────────────────────────────────

def process_clipping(file_path: Path):
    log.info(f"{'='*50}")
    log.info(f"开始处理：{file_path.name}")

    raw_content = read_file(file_path)
    if not raw_content.strip():
        log.warning("文件为空，跳过")
        return

    try:
        post = frontmatter.loads(raw_content)
        if str(post.get("processed", "")).lower() == "true":
            log.info("已标记为 processed，跳过")
            return
    except Exception:
        pass

    content_for_llm = raw_content[:6000]
    if len(raw_content) > 6000:
        content_for_llm += "\n\n[... 内容过长，已截断 ...]"

    log.info("Phase 1：调用 Ollama 分类...")
    try:
        classify_response = ollama_chat(
            system_prompt=SYSTEM_CLASSIFY,
            user_prompt=f"请分析以下 Clipping 文件内容：\n\n{content_for_llm}",
            json_mode=True,
        )
    except RuntimeError as e:
        log.error(f"Phase 1 失败：{e}")
        return

    try:
        json_match = re.search(r'\{.*\}', classify_response, re.DOTALL)
        decision = json.loads(json_match.group() if json_match else classify_response)
    except json.JSONDecodeError as e:
        log.error(f"JSON 解析失败：{e}\n原始回复：{classify_response[:300]}")
        return

    value_level = decision.get("value_level", "B").upper()
    destination = decision.get("destination", "")
    log_text    = decision.get("log_entry_text", file_path.stem)
    tags        = decision.get("tags", "#知识学习")
    reason      = decision.get("reason", "")

    log.info(f"判断结果：{value_level} 级 → {destination}")
    log.info(f"理由：{reason}")

    dest_key = resolve_dest_key(destination)

    wiki_content = ""
    if value_level == "A" and dest_key and dest_key != "学习日志":
        log.info(f"Phase 2：生成知识库内容 → {dest_key}...")
        try:
            wiki_content = ollama_chat(
                system_prompt=SYSTEM_GENERATE,
                user_prompt=(
                    f"目标知识库：{destination}\n"
                    f"今天日期：{datetime.now().strftime('%Y-%m-%d')}\n\n"
                    f"Clipping 内容：\n\n{content_for_llm}"
                ),
                json_mode=False,
            )
        except RuntimeError as e:
            log.error(f"Phase 2 失败：{e}")
            value_level = "B"

    dest_link = ""
    if value_level == "A" and wiki_content and dest_key:
        success = append_to_wiki(dest_key, wiki_content)
        if success:
            wiki_file = WIKI_FILES.get(dest_key)
            if wiki_file:
                dest_link = f"[{dest_key}](./{wiki_file.name})"

    if value_level == "C":
        log_text = f"{log_text}（已存档）"
        dest_link = "已存档"

    insert_log_entry(log_text, tags, dest_link or destination)
    mark_frontmatter(file_path, destination or "已存档")
    move_to_raw(file_path)

    log.info(f"✅ 处理完成：{file_path.name}")
    log.info(f"{'='*50}\n")

# ─────────────────────────────────────────────
#  👀  文件夹监控
# ─────────────────────────────────────────────

class ClippingHandler(FileSystemEventHandler):
    def __init__(self):
        self._lock = threading.Lock()
        self._processing = set()

    def _handle(self, src_path: str):
        path = Path(src_path)
        if path.suffix.lower() != ".md":
            return
        if path.name.startswith(".") or path.name.startswith("~"):
            return
        with self._lock:
            if str(path) in self._processing:
                return
            self._processing.add(str(path))
        log.info(f"检测到新文件：{path.name}，等待 {DEBOUNCE_SECONDS}s 后处理...")
        time.sleep(DEBOUNCE_SECONDS)
        try:
            process_clipping(path)
        except Exception as e:
            log.error(f"处理异常：{path.name} → {e}", exc_info=True)
        finally:
            with self._lock:
                self._processing.discard(str(path))

    def on_created(self, event):
        if not event.is_directory:
            self._handle(event.src_path)

# ─────────────────────────────────────────────
#  🚀  主程序
# ─────────────────────────────────────────────

def check_ollama():
    try:
        resp = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        models = [m["name"] for m in resp.json().get("models", [])]
        log.info(f"Ollama 可用，已加载模型：{', '.join(models)}")
        if MODEL not in models:
            log.warning(f"⚠️  配置的模型 '{MODEL}' 未找到。可用：{models}")
        return True
    except Exception:
        log.error("❌ 无法连接 Ollama。请先运行：ollama serve")
        return False


def main():
    log.info("=" * 50)
    log.info("Clipping Auto-Processor 启动")
    log.info(f"监控目录：{CLIPPINGS_DIR}")
    log.info(f"RAW 目录：{RAW_DIR}")
    log.info(f"Wiki 目录：{WIKI_DIR}")
    log.info(f"模型：{MODEL}")
    log.info("=" * 50)

    if not CLIPPINGS_DIR.exists():
        log.error(f"Clippings 目录不存在：{CLIPPINGS_DIR}")
        sys.exit(1)
    if not WIKI_DIR.exists():
        log.error(f"Wiki 目录不存在：{WIKI_DIR}")
        sys.exit(1)

    if not check_ollama():
        log.warning("Ollama 不可用，仍将启动监控（Ollama 启动后自动生效）")

    existing = list(CLIPPINGS_DIR.glob("*.md"))
    if existing:
        log.info(f"发现 {len(existing)} 个已有文件，开始处理...")
        for f in existing:
            try:
                process_clipping(f)
            except Exception as e:
                log.error(f"处理已有文件失败：{f.name} → {e}")

    handler = ClippingHandler()
    observer = Observer()
    observer.schedule(handler, str(CLIPPINGS_DIR), recursive=False)
    observer.start()

    log.info("✅ 监控已启动，等待新 Clipping 文件...")
    log.info("按 Ctrl+C 停止\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        log.info("监控已停止")
    observer.join()


if __name__ == "__main__":
    main()
```

---

## 附录 C：给 Claude 的执行清单

收到这两份教程文件后，按以下顺序执行：

- [ ] 问用户：vault 路径 / 存储方式（iCloud or 本地）/ Ollama 模型名
- [ ] 确认前置软件已安装（Obsidian / Ollama / Python）
- [ ] 创建 Clippings / RAW / Claude 三个文件夹
- [ ] 创建附录 A 中的所有 Wiki 文件
- [ ] 保存附录 B 中的 clipping_watcher.py（修改 VAULT_ROOT 和 MODEL）
- [ ] 测试脚本运行
- [ ] 配置 Web Clipper 保存路径
- [ ] 设置 LaunchAgent 开机自启动
- [ ] 用 Web Clipper 保存一篇文章做端到端测试
- [ ] 确认文章出现在学习日志和对应知识库

---

*版本：1.0 · 2026-04-22*
