# Vercel 前端项目极速部署标准操作流程 (SOP)

本流程涵盖从 GitHub 仓库导入到 Vercel 自动化部署的全链路操作。部署完成后，项目将自动获得一个免费的 `.vercel.app` 域名，适用于作品集展示与团队协作走查。

---

## 阶段一：前期环境准备

1. **统一账号授权**：
   * 访问 [Vercel 官网](https://vercel.com/)。
   * 选择 **Continue with GitHub** 进行注册/登录。
   * 在授权页面，选择授权 Vercel 访问所有的仓库（All repositories）或指定的单个项目仓库。
2. **确认代码结构**：
   * 确保 GitHub 仓库根目录下包含目标框架的标准配置文件（如 `package.json`、`astro.config.mjs` 等）。Vercel 将依靠这些文件自动识别构建环境。

---

## 阶段二：首次自动部署与域名分配

1. **新建项目**：
   * 登录 Vercel 控制台大盘（Dashboard），点击右上角的 **Add New...** -> **Project**。
2. **导入仓库**：
   * 在左侧的 "Import Git Repository" 列表中，找到目标代码仓库，点击 **Import**。
3. **配置项目参数（决定你的免费域名）**：
   * **Project Name**：这里的名字**非常重要**。它将直接成为你最终网址的前缀（例如，填入 `my-design-portfolio`，你的网址就是 `my-design-portfolio.vercel.app`）。如果名字已被全球其他用户占用，Vercel 会自动在后面加随机数字。
   * **Framework Preset**：Vercel 会自动侦测框架类型，保持默认。
   * **Root Directory**：若代码位于仓库根目录，保持 `./` 即可。
   * **Build and Output Settings**：保持默认，Vercel 已内置主流框架的最优打包命令。
4. **执行部署**：
   * 点击 **Deploy**。
   * 页面将进入终端日志视图，展示拉取代码、安装依赖、构建打包的实时过程。约 1-2 分钟后，屏幕飘落彩纸（Confetti）即代表部署成功。
   * 点击 **Continue to Dashboard**，你就能看到系统分配给你的最终访问链接。

---

## 阶段三：日常迭代与团队协作流 (Workflow)

部署完成后，Vercel 将完全融入 Git 自动化工作流，后续的所有更新均只需在代码端操作，无需再登录 Vercel 后台。

* **生产环境自动更新 (Production)**：
  * 任何合并至 GitHub `main`（或 `master`）主分支的代码提交，均会自动触发 Vercel 构建。约 1 分钟后，线上 `.vercel.app` 主站会自动刷新为最新版本。
* **预览环境走查 (Preview Deployments)**：
  * 当团队成员在 GitHub 提交新分支（Branch）或发起 Pull Request (PR) 时，Vercel 会自动为该分支生成一个**临时、独立**的预览链接（带有随机哈希值，不会影响主站）。
  * 该预览链接会自动作为评论附在 GitHub 的 PR 页面。团队可直接点击访问，进行视觉走查和交互测试。
  * **悬浮评论 (Vercel Toolbar)**：在预览环境页面底部，Vercel 提供了原生悬浮工具栏，允许团队成员直接在网页 UI 上打点标注，修改意见会自动同步给代码提交者，确认无误后再合并进主干。