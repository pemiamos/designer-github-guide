# 用 Netlify + Decap CMS 为设计师作品集添加可视化内容管理

> 本教程面向已经完成基础 Astro 作品集搭建的设计师。完成后，你可以在浏览器里用表单界面直接编辑项目内容、上传图片，不再需要打开 VS Code 或写任何代码。
>
> **前置条件**：已有一个在 GitHub 上托管的 Astro 作品集项目。

---

## 你将得到什么

- 一个部署在 Netlify 上的作品集网站（免费）
- 一个可以在任何浏览器里登录的 CMS 后台（`你的域名/admin/`）
- 在后台新建、编辑、删除项目内容，保存后自动发布
- 图片上传到 GitHub 仓库，容量充足

**工作流变化对比**：

| 操作 | 之前 | 之后 |
|------|------|------|
| 加新项目 | VS Code 写 MDX 文件 | 浏览器填表单 |
| 上传图片 | 终端命令 + git push | 拖拽到 CMS 媒体库 |
| 编辑内容 | VS Code 改文件 | 浏览器直接编辑 |
| 发布更新 | git add / commit / push | 点"发布"按钮 |

---

## 第一章：把站点迁移到 Netlify

### 1.1 注册 Netlify

打开 `https://netlify.com`，点 **Sign up**，选择 **Sign up with GitHub**，用你的 GitHub 账号登录。

> **💡 为什么要迁移到 Netlify**：Decap CMS 需要 Netlify Identity 作为登录系统，Git Gateway 作为写入 GitHub 的通道。这两个功能都是 Netlify 独有的，GitHub Pages 没有。迁移后 GitHub 仓库本身不变，只是换了一个部署平台。

### 1.2 导入你的 GitHub 仓库

登录后点 **Add new site** → **Import an existing project** → **GitHub**，授权 Netlify 访问你的仓库，找到 `portfolio` 仓库选中。

填写构建配置：

| 字段 | 填写内容 |
|------|---------|
| Branch to deploy | `main` |
| Build command | `npm run build` |
| Publish directory | `dist` |

点 **Deploy site**，等 1-2 分钟。

> **⚠️ 关于 base 路径**：如果你的 `astro.config.mjs` 里有 `base: '/portfolio'` 这行，**必须删除**。Netlify 从根路径 `/` 托管，不需要子路径前缀。删掉后 `Cmd+S` 保存，重新 push 一次。

### 1.3 确认部署成功

Netlify 会分配一个随机域名，比如 `snazzy-fox-123.netlify.app`。点击访问，确认样式和内容都正常显示。

> **⚠️ 样式丢失怎么办**：如果页面内容显示但没有样式，几乎一定是 `base` 路径问题。检查 `astro.config.mjs`，确认没有 `base` 字段，同时图片路径也不要有 `/portfolio/` 前缀。

---

## 第二章：开启 Netlify Identity 和 Git Gateway

这两项是 CMS 工作的核心基础：**Identity** 负责你的登录认证，**Git Gateway** 负责让 CMS 把内容写回 GitHub 仓库。

### 2.1 找到 Identity 设置

在 Netlify 后台，进入你的站点 → **Project configuration** → 左侧菜单找 **Identity** → 点 **Enable Identity**。

> **💡 界面找不到**：Netlify 会不定期改版界面。如果找不到 Integrations 标签，直接访问 `app.netlify.com/projects/你的项目名/configuration/identity` 可以直达。

### 2.2 设置注册方式为仅邀请

Identity 开启后，找到 **Registration preferences** 区域，点 **Configure**，把 Registration 改为 **Invite only**。

> **⚠️ 必须改成 Invite only**：默认是 Open（任何人都可以注册），这意味着陌生人也能登录你的 CMS 后台编辑内容。改成 Invite only 后只有你邀请的邮箱才能注册。

### 2.3 开启 Git Gateway

在同一个 Identity 设置页面，找到 **Git Gateway** 区域，点 **Enable Git Gateway**。

开启成功后会显示：
- Repository: `https://github.com/你的用户名/portfolio`
- GitHub API access token: `****`（已自动配置）

> **⚠️ Git Gateway 是必须的**：没有它，CMS 后台可以登录但无法保存任何内容。它的作用是替你执行 git commit，把你在浏览器里编辑的内容推送到 GitHub。

---

## 第三章：配置 CMS 后台文件

需要在项目里创建两个文件，告诉 CMS 后台怎么显示、管理哪些内容。

### 3.1 创建后台目录

在终端执行：

```bash
mkdir -p public/admin
```

### 3.2 创建 `public/admin/index.html`

这是 CMS 后台的入口页面：

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Portfolio CMS</title>
</head>
<body>
  <script src="https://identity.netlify.com/v1/netlify-identity-widget.js"></script>
  <script src="https://unpkg.com/decap-cms@^3.0.0/dist/decap-cms.js"></script>
</body>
</html>
```

> **⚠️ 两个脚本都要有**：第一个是 Netlify Identity 的登录弹窗，第二个是 CMS 本体。少了第一个，邀请链接点开不会弹出设置密码的对话框。

### 3.3 创建 `public/admin/config.yml`

这是 CMS 的核心配置，定义了哪些内容可以在后台编辑：

```yaml
backend:
  name: git-gateway
  branch: main

media_folder: public/images/projects
public_folder: /images/projects

locale: zh_Hans

collections:
  - name: projects
    label: 项目
    label_singular: 项目
    folder: src/content/projects
    create: true
    extension: mdx
    format: frontmatter
    fields:
      - { label: 标题, name: title, widget: string }
      - { label: 年份, name: year, widget: number }
      - { label: 媒介, name: medium, widget: string }
      - label: 主题
        name: themes
        widget: list
        default: []
      - { label: 封面图路径, name: cover, widget: string }
      - { label: 一句话简介, name: summary, widget: text }
      - { label: 精选项目, name: featured, widget: boolean, default: false }
      - { label: 正文内容, name: body, widget: markdown }
```

**关键字段说明**：

- `media_folder`：图片上传后存放在 GitHub 仓库的哪个位置
- `public_folder`：图片在网页里引用时的路径前缀
- `folder`：项目 MDX 文件存放位置，必须和你的实际目录一致
- `locale: zh_Hans`：让 CMS 界面显示中文

> **💡 自定义字段**：如果你的项目有额外字段（比如合作者、发表渠道），在 `fields` 里继续添加即可。widget 类型常用的有：`string`（单行文本）、`text`（多行文本）、`number`（数字）、`boolean`（开关）、`markdown`（富文本）、`image`（图片上传）、`list`（列表）。

### 3.4 在 BaseLayout 里加登录回调脚本

打开 `src/layouts/BaseLayout.astro`，在 `</body>` 标签前加入：

```astro
<script>
  if (window.netlifyIdentity) {
    window.netlifyIdentity.on("init", user => {
      if (!user) {
        window.netlifyIdentity.on("login", () => {
          document.location.href = "/admin/";
        });
      }
    });
  }
</script>
```

> **💡 这段脚本的作用**：当你点击邀请邮件里的链接、设置好密码后，会自动跳转到 CMS 后台，而不是停在首页。

---

## 第四章：推送并完成部署

把所有新文件推送到 GitHub：

```bash
git add .
git commit -m "Add: Decap CMS with Netlify Identity"
git push
```

等 Netlify 自动重新部署（约 1-2 分钟）。

> **⚠️ push 被拒绝怎么办**：如果提示 `fetch first` 或 `rejected`，说明远端有你本地没有的提交（通常是 CMS 自动提交的内容）。执行 `git pull --rebase origin main` 再重新 `git push`。

---

## 第五章：邀请自己登录

### 5.1 发送邀请

回到 Netlify 后台，进入 **Project configuration** → **Identity**，找到 **Invite users** 按钮，填入你自己的邮箱，发送邀请。

### 5.2 接受邀请、设置密码

去邮箱查收标题为 **"You've been invited to join..."** 的邮件，点击 **Accept the invite** 链接。

> **⚠️ 点链接后页面没有弹窗**：这是因为当时 CMS 还没部署完成。等 Netlify 部署成功后，把邮件里的链接地址手动修改一下再访问：
>
> 原始链接：`你的域名/#invite_token=xxxxx`
>
> 修改为：`你的域名/admin/#invite_token=xxxxx`
>
> 在 `#` 前面加上 `/admin/`，这样会在 CMS 页面里处理 token，就能弹出设置密码的对话框。

设置好密码后，访问 `你的域名/admin/`，用邮箱和密码登录。

---

## 第六章：日常使用指南

### 6.1 进入后台

直接访问：`https://你的域名/admin/`

用你设置的邮箱和密码登录。

### 6.2 新建项目

1. 点左侧"项目"集合
2. 点右上角"新建项目"
3. 填写各个字段：
   - **标题**：项目名称
   - **年份**：数字，比如 2025
   - **媒介**：比如"图书设计 / 信息可视化"
   - **主题**：用英文短横线格式，比如 `natural-history`
   - **封面图路径**：图片上传后会自动填入，也可以手动写路径
   - **一句话简介**：项目摘要，会显示在首页卡片上
   - **精选项目**：开关打开后会出现在首页
   - **正文内容**：富文本编辑器，支持标题、粗体、图片、链接等
4. 右上角点"已发布"旁边的下拉箭头，选择"发布"
5. Netlify 自动触发部署，约 1 分钟后网站更新

### 6.3 上传图片

1. 点顶部"媒体"标签
2. 把图片文件拖拽进来，或点"上传"选择文件
3. 上传后图片会存入 GitHub 仓库的 `public/images/projects/` 目录
4. 在项目编辑页面，正文里点工具栏的图片图标可以插入

> **💡 图片上传建议**：
> - 格式：JPG 用于照片，PNG 用于需要透明背景的图
> - 尺寸：宽度不超过 2000px
> - 大小：单张控制在 500KB 以内
> - 命名：用英文小写加连字符，比如 `project-cover.jpg`
>
> Mac 上压缩图片最简单的方式：用"预览"打开 → 文件 → 导出 → 调整品质到 70-80%。

### 6.4 编辑已有项目

1. 在左侧点击项目名称进入编辑页
2. 直接修改任意字段
3. 右上角点"保存"，然后选择"发布"

### 6.5 删除项目

进入项目编辑页，点顶部"删除内容"按钮。删除后 Netlify 自动部署，项目从网站消失。

> **⚠️ 删除不可撤销**：CMS 里的删除操作会直接删除 GitHub 仓库里的 MDX 文件。如果误删，可以去 GitHub 仓库的 Commits 历史里找到之前的版本恢复。

---

## 什么能在 CMS 里改，什么不能

| 操作 | CMS 后台 | VS Code |
|------|---------|---------|
| 新建/编辑/删除项目 | ✅ | ✅ |
| 上传项目图片 | ✅ | ✅ |
| 修改项目标题、年份、简介 | ✅ | ✅ |
| 修改项目正文内容 | ✅ | ✅ |
| 修改导航栏名字和链接 | ❌ | ✅ |
| 修改首页陈述文字 | ❌ | ✅ |
| 修改颜色、字号、间距 | ❌ | ✅ |
| 添加新页面（About、主题页）| ❌ | ✅ |
| 修改页面布局结构 | ❌ | ✅ |

**记住这个原则**：项目内容用 CMS，页面结构和视觉用 VS Code。

---

## 常见问题速查

**Q：点邀请链接后直接进了网站首页，没有弹出设置密码的对话框**

A：部署还没完成，或者链接格式不对。等部署完成后，把链接里的 `#invite_token` 前面加上 `/admin/`，重新访问。

**Q：CMS 后台能登录，但保存时提示错误**

A：检查 Git Gateway 是否已开启（Project configuration → Identity → Git Gateway）。

**Q：图片上传成功，但在网站上显示破损**

A：检查 `config.yml` 里的 `public_folder` 路径是否正确。如果站点没有 `base` 路径，`public_folder` 应该是 `/images/projects`。

**Q：push 代码时提示 "fetch first" 被拒绝**

A：CMS 自动提交了内容，导致远端比本地新。执行 `git pull --rebase origin main` 合并后再 push。

**Q：想换一个更好看的 Netlify 域名**

A：在 Netlify 后台 → Domain management → 可以修改 Netlify 子域名（免费），或者绑定自己买的域名。

**Q：忘记 CMS 登录密码**

A：访问 `你的域名/admin/`，点登录框下方的"Forgot password?"，用邮箱重置密码。

---

## 附录：三个平台的分工

```
GitHub                 Netlify                你的浏览器
  │                      │                       │
  │  存储所有代码和内容    │  构建并托管网站         │  CMS 后台编辑
  │  每次有改动自动触发   ◄─┤  提供 Identity 登录    │  在表单里填内容
  │  部署流水线           │  提供 Git Gateway      │  上传图片
  │                      │  （写回 GitHub）        │  点发布按钮
  └──────────────────────┘                        │
           ▲                                      │
           └──────────────────────────────────────┘
                    CMS 保存时自动 git commit
```

所有数据的最终存储位置都是 **GitHub 仓库**。Netlify 是中间层，负责构建、托管和提供编辑入口。你在 CMS 里的每一次"保存并发布"，本质上都是 Netlify 替你执行了一次 `git commit + git push`。
