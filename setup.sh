#!/bin/bash
# 
# 设计师 GitHub 指南仓库 - 一键初始化脚本
# 
# 这个脚本会自动完成:
# 1. 初始化 Git 仓库
# 2. 添加所有文件到暂存区
# 3. 创建第一次提交
# 4. 关联到 GitHub 远程仓库
# 5. 推送到 GitHub
#
# 使用方法:
#   1. 先在 GitHub 网页建好空仓库(不要勾选任何初始化选项)
#   2. 在终端里进入当前文件夹: cd 当前文件夹路径
#   3. 运行本脚本: bash setup.sh

set -e  # 遇到错误立即退出

echo ""
echo "================================================"
echo "  设计师 GitHub 指南 · 仓库初始化脚本"
echo "================================================"
echo ""

# 检查是否已经是 Git 仓库
if [ -d ".git" ]; then
    echo "⚠️  这个文件夹已经是 Git 仓库了,跳过初始化步骤"
else
    echo "▶ 正在初始化 Git 仓库..."
    git init -b main
    echo "✓ Git 仓库初始化完成"
fi
echo ""

# 询问 GitHub 用户名
read -p "请输入你的 GitHub 用户名(例如 pemiamos): " GITHUB_USER

if [ -z "$GITHUB_USER" ]; then
    echo "❌ 用户名不能为空,退出"
    exit 1
fi

# 询问仓库名(提供默认值)
read -p "请输入仓库名(直接回车使用默认值 designer-github-guide): " REPO_NAME
REPO_NAME=${REPO_NAME:-designer-github-guide}

REMOTE_URL="https://github.com/${GITHUB_USER}/${REPO_NAME}.git"

echo ""
echo "即将使用的仓库地址:"
echo "  ${REMOTE_URL}"
echo ""
read -p "确认无误吗?(y/回车 继续,其他键取消): " CONFIRM
if [ ! -z "$CONFIRM" ] && [ "$CONFIRM" != "y" ] && [ "$CONFIRM" != "Y" ]; then
    echo "已取消"
    exit 0
fi
echo ""

# 添加所有文件
echo "▶ 正在添加所有文件..."
git add .
echo "✓ 文件已添加到暂存区"
echo ""

# 检查是否有 Git 身份配置
if [ -z "$(git config user.name)" ] || [ -z "$(git config user.email)" ]; then
    echo "⚠️  检测到 Git 还没有配置身份信息,请输入:"
    read -p "  你的显示名称(例如你的英文名或昵称): " GIT_NAME
    read -p "  你的邮箱(建议使用 GitHub 注册邮箱): " GIT_EMAIL
    git config user.name "$GIT_NAME"
    git config user.email "$GIT_EMAIL"
    echo "✓ 身份信息已配置"
    echo ""
fi

# 创建第一次提交
echo "▶ 正在创建首次提交..."
if git diff --cached --quiet; then
    echo "  没有需要提交的变化,跳过"
else
    git commit -m "初始化:设计师视角的 GitHub 指南 v0.1"
    echo "✓ 首次提交已创建"
fi
echo ""

# 配置远程仓库
echo "▶ 正在关联远程仓库..."
if git remote get-url origin > /dev/null 2>&1; then
    git remote set-url origin "$REMOTE_URL"
    echo "✓ 已更新远程仓库地址"
else
    git remote add origin "$REMOTE_URL"
    echo "✓ 已关联远程仓库"
fi
echo ""

# 推送到 GitHub
echo "▶ 正在推送到 GitHub..."
echo "  (如果弹出登录窗口,请按提示授权)"
echo ""

if git push -u origin main; then
    echo ""
    echo "================================================"
    echo "  🎉 完成!仓库已成功发布到 GitHub"
    echo "================================================"
    echo ""
    echo "  访问你的仓库:"
    echo "    https://github.com/${GITHUB_USER}/${REPO_NAME}"
    echo ""
    echo "  接下来可以做的事:"
    echo "    1. 在 GitHub 网页上打开仓库 Settings → Pages,"
    echo "       启用 GitHub Pages,让仓库变成网站"
    echo "    2. 用 GitHub Desktop 打开这个文件夹,"
    echo "       之后就可以用图形界面管理日常更新"
    echo "    3. 把仓库链接分享到社交平台,开启社区互动"
    echo ""
else
    echo ""
    echo "❌ 推送失败。常见原因:"
    echo ""
    echo "  1. 你还没在 GitHub 网页上创建名为 ${REPO_NAME} 的空仓库"
    echo "     → 访问 https://github.com/new 创建"
    echo "     → 注意:创建时不要勾选任何初始化选项"
    echo ""
    echo "  2. GitHub 账号未登录或认证失败"
    echo "     → 如果弹出过登录窗口,请确认完成授权"
    echo "     → 或参考 https://docs.github.com/authentication"
    echo ""
    echo "  解决后,重新运行本脚本即可。"
    exit 1
fi
