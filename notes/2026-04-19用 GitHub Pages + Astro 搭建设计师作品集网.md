# 用 GitHub Pages + Astro 搭建设计师作品集网站

> 本教程面向没有编程基础的设计师学生。你不需要懂代码，只需要跟着步骤走。全程约 3-4 小时，完成后你将拥有一个免费、可自定义、终身维护的个人作品集网站。

---

## 你将得到什么

- 一个部署在 `你的用户名.github.io/portfolio/` 的作品集网站
- 导航栏、首页、项目页的完整骨架
- 图文俱全的第一个项目页
- 之后每次更新只需三行命令

**最终效果预览**：顶部固定导航 + 暖白背景 + 衬线字体 + 克制的编辑美学。

---

## 准备工作（开始前确认）

- Mac 电脑（本教程基于 macOS）
- 一个 GitHub 账号（没有就去 github.com 注册，免费）
- 安装好 Visual Studio Code（简称 VS Code，免费下载）
- 稳定的网络连接

---

## 第一章：环境准备

### 1.1 检查 Node.js

打开**终端**（在 Mac 上按 `Cmd+空格`，输入"终端"回车），输入：

```bash
node -v
```

如果显示 `v22.x.x` 或更高版本，可以跳到 1.2。

如果显示版本低于 22，或者提示"command not found"，需要安装/升级 Node.js：

1. 打开浏览器，访问 `https://nodejs.org`
2. 下载标有 **LTS** 的版本（长期支持版）
3. 双击安装包，一路点"继续"安装完成
4. 重新打开终端，再次运行 `node -v` 确认版本

> **💡 小贴士**：终端是你和电脑"对话"的地方。每输入一行命令，按回车执行，等它跑完再输下一行。不要把多行命令一起复制粘贴进去。

### 1.2 检查 Git

```bash
git -v
```

如果显示版本号就没问题。如果提示未安装，按照弹出的提示安装 Xcode Command Line Tools。

### 1.3 在 VS Code 里注册 `code` 命令

安装好 VS Code 后，需要让终端能识别 `code` 这个命令：

1. 打开 VS Code
2. 按 `Cmd+Shift+P`（三键同时按）
3. 在弹出的搜索框里输入：`Shell Command`
4. 选择 **Shell Command: Install 'code' command in PATH**
5. 点击执行，输入 Mac 密码确认

> **⚠️ 注意**：这一步必须在 VS Code 里操作，不是在终端输入这段文字。

完成后**关闭当前终端，重新打开一个新的终端窗口**，环境变量才会刷新生效。

---

## 第二章：创建 GitHub 仓库

### 2.1 新建仓库

1. 登录 GitHub，点右上角 `+` → **New repository**
2. Repository name 填：`portfolio`
3. 设为 **Public**（GitHub Pages 免费版需要公开仓库）
4. **不要**勾选任何初始化选项（README、.gitignore、License 都不勾）
5. 点 **Create repository**

创建后会看到一个空仓库页面，先不管它，我们去本地建项目。

---

## 第三章：创建 Astro 项目

### 3.1 建一个专门放项目的文件夹

在终端里执行：

```bash
mkdir -p ~/Projects
cd ~/Projects
```

> **💡 小贴士**：`~` 是你的家目录（就是 `/Users/你的用户名/`）。建议把所有开发项目放在 `~/Projects/` 里，避免文件散落在桌面或下载文件夹。

### 3.2 创建 Astro 项目

```bash
npm create astro@latest portfolio
```

这条命令会启动一个交互式问答，按下面回答：

| 问题 | 选择 |
|------|------|
| How would you like to start? | **Empty**（空模板） |
| Install dependencies? | **Yes** |
| Do you plan to write TypeScript? | **Yes** |
| How strict? | **Strict** |
| Initialize a new git repository? | **Yes** |

等待安装完成，看到 Houston 宇航员的欢迎提示就成功了。

> **⚠️ 常见错误**：如果看到 `Dependencies failed to install`，不要慌。项目骨架已经创建好了，只是依赖包没装上。继续下一步手动安装。

### 3.3 进入项目并安装依赖

```bash
cd ~/Projects/portfolio
npm install
```

> **⚠️ 常见错误**：如果提示 `cd: no such file or directory`，说明项目创建时文件夹名字有误。用 `ls ~/Projects/` 查看实际文件夹名，再 `cd` 进去。

如果 `npm install` 因为网络问题失败，换国内镜像：

```bash
npm config set registry https://registry.npmmirror.com
npm install
```

### 3.4 启动开发服务器

```bash
npm run dev
```

看到这样的输出说明成功：

```
astro  v6.x.x ready in XXX ms

  Local    http://localhost:4321/
```

打开浏览器访问 `http://localhost:4321`，能看到页面就说明环境完全正常。

按 `Ctrl+C` 停止服务器，继续下面的配置。

---

## 第四章：安装必要插件

在项目目录里依次执行：

```bash
npx astro add mdx
```

提示 Continue? 时输入 `y` 回车。

```bash
npx astro add sitemap
```

同样输入 `y` 回车。

```bash
npm install @fontsource/eb-garamond @fontsource/inter
```

安装完成后，用 VS Code 打开项目：

```bash
code .
```

VS Code 会打开整个 portfolio 文件夹，左侧文件树可以看到所有文件。

> **💡 小贴士**：从现在开始，你可以在 VS Code 底部的**集成终端**（按 `Ctrl+反引号` 打开）里操作，不用再切换到系统终端。

---

## 第五章：搭建目录结构

在 VS Code 的集成终端里执行：

```bash
mkdir -p src/content/projects src/content/themes src/content/writings
mkdir -p src/components/narrative src/components/viz src/components/layout
mkdir -p src/layouts src/styles
```

完成后左侧文件树应该能看到这些文件夹。

---

## 第六章：配置 Astro

打开 `astro.config.mjs`，替换为（把 `YOUR-USERNAME` 换成你的 GitHub 用户名）：

```javascript
// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://YOUR-USERNAME.github.io',
  base: '/portfolio',
  integrations: [mdx(), sitemap()],
});
```

> **⚠️ 重要**：`base: '/portfolio'` 这一行和你的仓库名必须完全一致。如果你的仓库叫 `portfolio`，就写 `/portfolio`。这个配置同时影响本地预览和线上访问的路径。

---

## 第七章：建立设计系统

### 7.1 创建全局样式

在 `src/styles/` 里新建文件 `global.css`，粘贴以下内容：

```css
@import '@fontsource/eb-garamond/400.css';
@import '@fontsource/eb-garamond/400-italic.css';
@import '@fontsource/eb-garamond/600.css';
@import '@fontsource/inter/400.css';
@import '@fontsource/inter/600.css';

:root {
  /* 颜色 */
  --color-bg: #FAFAF7;
  --color-text: #1A1A1A;
  --color-text-secondary: #6B6B6B;
  --color-divider: #E5E3DD;
  --color-accent: #2B2620;

  /* 字体 */
  --font-serif: 'EB Garamond', Georgia, serif;
  --font-sans: 'Inter', system-ui, sans-serif;

  /* 字号（模块化音阶 1.25）*/
  --text-sm:   0.875rem;
  --text-base: 1.125rem;
  --text-lg:   1.375rem;
  --text-xl:   1.75rem;
  --text-2xl:  2.25rem;
  --text-3xl:  2.8125rem;
  --text-4xl:  3.5rem;

  /* 间距（基于 8px）*/
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 1rem;
  --space-4: 1.5rem;
  --space-5: 2rem;
  --space-6: 3rem;
  --space-7: 4rem;
  --space-8: 6rem;
  --space-9: 8rem;

  /* 布局 */
  --measure:   42rem;
  --container: 80rem;

  /* 行高 */
  --leading-tight:  1.2;
  --leading-normal: 1.6;
  --leading-loose:  1.8;
}

*, *::before, *::after {
  box-sizing: border-box;
}

body {
  margin: 0;
  background: var(--color-bg);
  color: var(--color-text);
  font-family: var(--font-serif);
  font-size: var(--text-base);
  line-height: var(--leading-normal);
  -webkit-font-smoothing: antialiased;
}

a {
  color: var(--color-accent);
  text-decoration: none;
  border-bottom: 1px solid currentColor;
  transition: opacity 0.2s ease;
}

a:hover { opacity: 0.6; }

img {
  max-width: 100%;
  height: auto;
  display: block;
}

h1, h2, h3, h4 {
  line-height: var(--leading-tight);
  font-weight: 600;
}
```

### 7.2 创建基础布局

在 `src/layouts/` 里新建 `BaseLayout.astro`：

```astro
---
interface Props {
  title: string;
  description?: string;
}
const { title, description = '' } = Astro.props;
---
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  {description && <meta name="description" content={description} />}
</head>
<body>
  <slot name="nav" />
  <slot />
</body>
</html>

<style is:global>
  @import '../styles/global.css';
</style>
```

### 7.3 创建导航组件

在 `src/components/layout/` 里新建 `SiteNav.astro`：

```astro
---
const navItems = [
  { href: '/', label: 'Works' },
  { href: '/themes', label: 'Themes' },
  { href: '/writing', label: 'Writing' },
  { href: '/about', label: 'About' },
];

const currentPath = Astro.url.pathname;
---

<header class="site-header">
  <nav class="site-nav">
    <a href="/" class="brand">你的名字</a>
    <ul class="nav-list">
      {navItems.map(item => (
        <li>
          <a href={item.href} class:list={['nav-link', { active: currentPath === item.href }]}>
            {item.label}
          </a>
        </li>
      ))}
    </ul>
  </nav>
</header>

<style>
  .site-header {
    position: sticky;
    top: 0;
    z-index: 100;
    background: var(--color-bg);
    border-bottom: 1px solid var(--color-divider);
  }
  .site-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: var(--container);
    margin: 0 auto;
    padding: var(--space-3) var(--space-5);
  }
  .brand {
    font-family: var(--font-sans);
    font-size: var(--text-sm);
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    border: none;
    color: var(--color-text);
  }
  .nav-list {
    display: flex;
    gap: var(--space-5);
    list-style: none;
    margin: 0;
    padding: 0;
  }
  .nav-link {
    font-family: var(--font-sans);
    font-size: var(--text-sm);
    color: var(--color-text-secondary);
    border: none;
  }
  .nav-link:hover,
  .nav-link.active {
    color: var(--color-text);
    opacity: 1;
  }
</style>
```

把 `你的名字` 改成你的真实姓名或英文名。

### 7.4 创建首页

打开 `src/pages/index.astro`，**全选删除**，粘贴：

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
import SiteNav from '../components/layout/SiteNav.astro';
---

<BaseLayout title="Portfolio">
  <SiteNav slot="nav" />
  <main class="home">
    <section class="intro">
      <h1>在这里写你最想说的一句话。</h1>
      <p class="lede">这里补充两三句，说清楚你是谁、你关心什么、你在探索什么。</p>
    </section>
  </main>
</BaseLayout>

<style>
  .home {
    max-width: var(--container);
    margin: 0 auto;
    padding: var(--space-8) var(--space-5);
  }
  .intro {
    max-width: var(--measure);
  }
  .intro h1 {
    font-size: var(--text-3xl);
    margin: 0 0 var(--space-4);
  }
  .lede {
    font-size: var(--text-lg);
    color: var(--color-text-secondary);
    margin: 0;
  }
</style>
```

### 7.5 预览效果

```bash
npm run dev
```

打开 `http://localhost:4321/portfolio`，应该能看到带导航条的首页。

> **💡 注意本地访问地址**：因为配置了 `base: '/portfolio'`，本地预览时地址是 `localhost:4321/portfolio`，不是 `localhost:4321`。这是正常的。

---

## 第八章：建立内容模型

### 8.1 创建内容配置文件

在 `src/` 目录下新建 `content.config.ts`（注意：在 `src/` 里，不是在 `src/content/` 里）：

```typescript
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const projects = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/projects' }),
  schema: z.object({
    title: z.string(),
    year: z.number(),
    medium: z.string(),
    themes: z.array(z.string()),
    cover: z.string(),
    summary: z.string(),
    collaborators: z.array(z.string()).optional(),
    featured: z.boolean().default(false),
  }),
});

const themes = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/themes' }),
  schema: z.object({
    title: z.string(),
    slug: z.string(),
    tagline: z.string(),
  }),
});

export const collections = { projects, themes };
```

> **⚠️ Astro v6 重要变化**：在 Astro v6 中，内容配置文件必须放在 `src/content.config.ts`，而不是旧版本的 `src/content/config.ts`。如果放错位置，会出现 `Content config not loaded` 警告，导致项目页 404。

---

## 第九章：创建第一个项目页

### 9.1 准备图片

在 `public/` 目录下建立图片文件夹：

```bash
mkdir -p public/images/projects/my-project
```

把项目图片复制到这个文件夹里。建议按用途命名：

```
cover.jpg      ← 封面图
hero.jpg       ← 项目页顶部大图
process-1.jpg  ← 过程图1
final.jpg      ← 最终成品图
```

> **⚠️ 图片路径大坑**：图片文件名的大小写和扩展名必须完全一致。`hero.jpg` 和 `hero.JPG` 是不同的文件。`.jpg` 和 `.png` 也不能混用。如果图片显示破损，先用 `ls public/images/projects/my-project/` 确认实际文件名。

> **⚠️ 路径前缀问题**：因为配置了 `base: '/portfolio'`，MDX 里引用图片时路径要加 `/portfolio` 前缀。正确写法是 `/portfolio/images/projects/my-project/hero.jpg`，而不是 `/images/projects/my-project/hero.jpg`。

### 9.2 创建项目 MDX 文件

在 `src/content/projects/` 里新建 `my-project.mdx`（文件名就是之后 URL 里的路径，建议用英文小写加连字符）：

```mdx
---
title: 项目标题
year: 2025
medium: 产品设计 / 交互原型
themes: [theme-one]
cover: /portfolio/images/projects/my-project/cover.jpg
summary: 用一两句话说清楚这个项目回答了什么问题。
featured: true
---

![项目主视觉](/portfolio/images/projects/my-project/hero.jpg)

## 核心问题

在这里写这个项目的背景和你面对的核心挑战。

## 设计决策一：标题写这个决策是什么

解释你为什么做了这个选择，以及你放弃了什么。

![配图说明](/portfolio/images/projects/my-project/process-1.jpg)

## 最终成品

![成品展示](/portfolio/images/projects/my-project/final.jpg)

## 反思

这个项目让你学到了什么？
```

### 9.3 创建项目页路由

在 `src/pages/` 里新建 `projects/` 文件夹，在里面新建 `[slug].astro`：

```astro
---
import { getCollection, render } from 'astro:content';
import BaseLayout from '../../layouts/BaseLayout.astro';
import SiteNav from '../../components/layout/SiteNav.astro';

export async function getStaticPaths() {
  const projects = await getCollection('projects');
  return projects.map(project => ({
    params: { slug: project.id },
    props: { project },
  }));
}

const { project } = Astro.props;
const { Content } = await render(project);
---

<BaseLayout title={project.data.title}>
  <SiteNav slot="nav" />
  <main class="project">

    <header class="project-hero">
      <h1>{project.data.title}</h1>
      <p class="summary">{project.data.summary}</p>
    </header>

    <div class="project-meta">
      <dl>
        <dt>年份</dt><dd>{project.data.year}</dd>
        <dt>媒介</dt><dd>{project.data.medium}</dd>
      </dl>
    </div>

    <div class="project-body">
      <Content />
    </div>

  </main>
</BaseLayout>

<style>
  .project {
    max-width: var(--container);
    margin: 0 auto;
    padding: 0 var(--space-5) var(--space-9);
  }
  .project-hero {
    max-width: var(--measure);
    padding: var(--space-8) 0 var(--space-6);
    border-bottom: 1px solid var(--color-divider);
    margin-bottom: var(--space-6);
  }
  .project-hero h1 {
    font-size: var(--text-3xl);
    margin: 0 0 var(--space-4);
  }
  .summary {
    font-size: var(--text-lg);
    color: var(--color-text-secondary);
    margin: 0;
  }
  .project-meta {
    margin-bottom: var(--space-7);
  }
  .project-meta dl {
    display: grid;
    grid-template-columns: auto 1fr;
    gap: var(--space-2) var(--space-4);
    font-family: var(--font-sans);
    font-size: var(--text-sm);
    max-width: 20rem;
  }
  .project-meta dt {
    color: var(--color-text-secondary);
  }
  .project-body {
    max-width: var(--measure);
  }
  .project-body h2 {
    font-size: var(--text-xl);
    margin-top: var(--space-7);
    margin-bottom: var(--space-4);
    padding-top: var(--space-6);
    border-top: 1px solid var(--color-divider);
  }
  .project-body p {
    margin: 0 0 var(--space-4);
  }
</style>
```

> **⚠️ Astro v6 重要变化**：有两处和旧教程不同：
> 1. `render` 函数需要从 `astro:content` 单独导入
> 2. 用 `project.id` 而不是 `project.slug` 生成路由参数

### 9.4 预览项目页

确保开发服务器在运行，访问：

```
http://localhost:4321/portfolio/projects/my-project
```

（把 `my-project` 换成你的 MDX 文件名，不含 `.mdx` 后缀）

如果出现 404，先检查：
1. `src/content.config.ts` 是否在 `src/` 目录下（不是 `src/content/` 下）
2. 终端有没有 `Content config not loaded` 警告
3. 如果有，执行 `rm -rf .astro && npm run dev` 清除缓存重启

---

## 第十章：部署到 GitHub Pages

### 10.1 获取 GitHub Personal Access Token

GitHub 不接受密码进行 git 操作，需要用 Token 代替密码：

1. 登录 GitHub，点右上角头像 → **Settings**
2. 左侧滚到底部 → **Developer settings**
3. **Personal access tokens** → **Tokens (classic)**
4. **Generate new token (classic)**
5. 填写：
   - Note：`portfolio-deploy`
   - Expiration：90 days
   - 勾选 **`repo`** 和 **`workflow`** 两个权限组
6. 点 **Generate token**
7. **立刻复制那串 token**（以 `ghp_` 开头，页面关闭后无法再看到）

> **⚠️ 两个权限都要勾**：`repo` 权限用于推送代码，`workflow` 权限用于推送 GitHub Actions 配置文件。少勾一个都会导致推送失败。

### 10.2 创建部署配置文件

在项目根目录新建 `.github/workflows/deploy.yml`：

```bash
mkdir -p .github/workflows
```

然后在 VS Code 里新建 `.github/workflows/deploy.yml`，粘贴：

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Install, build, and upload
        uses: withastro/action@v3
        with:
          node-version: 22

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

> **⚠️ Node 版本必须指定**：Astro v6 需要 Node.js 22+，但 GitHub Actions 默认使用 Node 20，会导致构建失败。必须在 `withastro/action` 里明确传入 `node-version: 22`。

### 10.3 推送到 GitHub

```bash
git add .
git commit -m "Initial portfolio setup"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/portfolio.git
git push -u origin main
```

推送时会要求输入用户名和密码：
- 用户名：你的 GitHub 用户名
- 密码：**粘贴刚才复制的 Token**（不是 GitHub 登录密码）

> **💡 保存 Token 到钥匙串**：推送成功后执行这条命令，以后就不用每次输 Token 了：
> ```bash
> git config --global credential.helper osxkeychain
> ```

### 10.4 在 GitHub 开启 Pages

1. 打开你的 GitHub 仓库页面
2. 点顶部 **Settings** 标签
3. 左侧菜单找 **Pages**
4. Source 选择 **GitHub Actions**
5. 保存

### 10.5 查看部署结果

进入仓库的 **Actions** 标签，看到最新一条 workflow：
- 黄色转圈 = 正在部署，等待
- 绿色打勾 = 部署成功
- 红色叉号 = 部署失败，点进去看错误信息

部署成功后访问：

```
https://YOUR-USERNAME.github.io/portfolio/
```

---

## 第十一章：日常更新工作流

网站上线后，每次更新只需要三步：

```bash
git add .
git commit -m "简短描述你改了什么"
git push
```

约 30-60 秒后，GitHub 自动重新部署，线上页面自动更新。

**加新项目**：在 `src/content/projects/` 里新建一个 MDX 文件，把图片放到 `public/images/projects/新项目名/` 里，push 即可。

**改文字内容**：直接在 VS Code 里修改对应文件，`Cmd+S` 保存，push 即可。

---

## 常见错误速查

### 错误：`cd: no such file or directory`
**原因**：路径写错了，或者上一步命令没有正常完成。  
**解决**：用 `ls` 查看当前目录有什么，确认要进入的文件夹存在。

### 错误：`npm error ENOENT: Could not read package.json`
**原因**：在错误的目录里执行了 npm 命令。  
**解决**：确认终端提示符显示的是 `portfolio %`，说明在项目目录里。用 `cd ~/Projects/portfolio` 进入正确目录。

### 错误：`Content config not loaded`（黄色警告）
**原因**：`content.config.ts` 放错位置了。  
**解决**：确认文件在 `src/content.config.ts`（不是 `src/content/config.ts`）。如果已经正确但警告还在，执行 `rm -rf .astro && npm run dev` 清除缓存。

### 错误：`Missing parameter: slug`
**原因**：Astro v6 改变了路由参数的生成方式。  
**解决**：在 `[slug].astro` 里把 `project.slug` 改成 `project.id`。

### 错误：`project.render is not a function`
**原因**：Astro v6 改变了渲染 API。  
**解决**：在文件顶部改成 `import { getCollection, render } from 'astro:content'`，并把 `project.render()` 改成 `render(project)`。

### 错误：图片显示破损图标
**原因一**：文件名或扩展名不匹配（`.jpg` 写成了 `.png`）。  
**解决**：用 `ls public/images/projects/项目名/` 查看实际文件名，和 MDX 里写的逐一对照。

**原因二**：没有加 `/portfolio` 路径前缀。  
**解决**：MDX 里的图片路径改为 `/portfolio/images/projects/项目名/图片.jpg`。

### 错误：GitHub Actions 失败，提示 `Node.js v20 is not supported`
**原因**：GitHub Actions 默认 Node 版本太低，Astro v6 需要 Node 22+。  
**解决**：在 `deploy.yml` 的 `withastro/action` 步骤里加入 `node-version: 22`。

### 错误：`remote: Invalid username or token`
**原因**：GitHub 不接受密码，需要用 Personal Access Token。  
**解决**：按第十章步骤生成 Token，推送时在"密码"处粘贴 Token。

### 错误：`refusing to allow a Personal Access Token to create or update workflow`
**原因**：Token 没有勾选 `workflow` 权限。  
**解决**：重新生成 Token，确保同时勾选 `repo` 和 `workflow`。

---

## 下一步可以做什么

完成本教程后，你有一个能跑的基础骨架。接下来按优先级：

1. **填充真实内容**：把占位文字换成你自己的首页陈述和项目叙述
2. **做首页项目卡片**：让访客从首页能点进各个项目
3. **做 About 页**：放你的自我介绍和联系方式
4. **加更多项目**：每个项目一个 MDX 文件
5. **绑定自定义域名**：买一个域名（约 ¥70/年），在 GitHub Pages 设置里绑定
6. **加可视化后台**：安装 Decap CMS，用浏览器表单界面管理内容，不用改代码

---

## 附录：文件结构总览

完成本教程后，你的项目结构应该是这样：

```
portfolio/
├── .github/
│   └── workflows/
│       └── deploy.yml          ← GitHub 自动部署配置
├── public/
│   └── images/
│       └── projects/
│           └── my-project/     ← 项目图片放这里
├── src/
│   ├── components/
│   │   └── layout/
│   │       └── SiteNav.astro   ← 导航条
│   ├── content/
│   │   └── projects/
│   │       └── my-project.mdx  ← 项目内容文件
│   ├── content.config.ts       ← 内容模型（在 src/ 下）
│   ├── layouts/
│   │   └── BaseLayout.astro    ← 页面骨架
│   ├── pages/
│   │   ├── index.astro         ← 首页
│   │   └── projects/
│   │       └── [slug].astro    ← 项目页路由
│   └── styles/
│       └── global.css          ← 设计系统
├── astro.config.mjs            ← Astro 配置
├── content.config.ts           ← 内容模型副本（根目录）
└── package.json
```
