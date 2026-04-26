# 43. 通过设计的研究 (Research through Design)

**来源**：The Encyclopedia of Human-Computer Interaction, 2nd Ed.
**Notion 原页面**：https://www.notion.so/4126e95ab3364b3782d98251af06d8c1

---

[Pieter Jan Stappers](https://www.interaction-design.org/literature/author/pieter-jan-stappers-24142) 和 [Elisa Giaccardi](https://www.interaction-design.org/literature/author/elisa-giaccardi-24143)

长期以来，设计与研究被认为是两种截然不同的活动——前者根植于工业实践与工艺（Industrial practice and craft），后者则存在于学术实验与反思（Academic experiments and reflection）之中。在过去的几十年里，随着[交互设计（Interaction Design）](https://www.interaction-design.org/literature/topics/interaction-design)及其他形式的设计在学术基础上不断增强，在大学中作为教学科目日益普及，并形成了研究文化，随之发生了两件事。首先，开展研究成为了产品设计（以及后来的服务设计）中被认可的一部分。其次，设计活动以及设计产物（Designed Artifacts）逐渐成为了生成和传播知识过程中的核心要素。自 Frayling 极具影响力的演讲（1993, 2015）以来，这两者分别被地称为 *为设计的研究（Research for Design）* 和 *通过设计的研究（Research through Design, RtD）*。

直到 2010 年代后期，关于 RtD 的明确理论仍处于形成阶段。因此，相关学术共同体仍在努力寻找合适的措辞、模型和实践方法。

在本章中（如表 1.1 所示），我们尝试概述该领域及其主题，展示已发表的研究成果，并将该方法与交互设计（Interaction Design）内部以及更广泛的设计和工程领域中的其他研究方法进行类比。

|  |  |  |  |
|---|---|---|---|
| 1 | 前言 (Preface) |  |  |
| 2 | 工作定义 (Working definitions) | 研究、设计、原型、人工制品 (Artifact)、知识、实践 | 对该领域中的术语进行定位并快速扫描，以便您日后重新查阅 |
|  | 术语历史 | RtD 及其相关术语 |  |
| 3 | 示例 | Wensveen, Keller, Gaver, Mattelmäki, Lundström, Rygh, Wright | 涵盖下文主题的相关示例 |
| 4 | 主题 | 人工制品 (Artifact)、知识、学习、分享 | 关联主要讨论主题和提出的理论 |
| 5 | 结论 |  |  |
| 6 | 参考文献 |  |  |
| 7 | 附录：框架 (Framings) | Horvath, Mintzberg, Stokes, Harré | 引入 [HCI](https://www.interaction-design.org/literature/topics/human-computer-interaction)（人机交互）领域之外的视角，从而将 RtD 置于更广泛的视角下审视 |
***表 1.1**** – 本章阅读指南*

## 43.1 引言：“设计”与“研究”

“研究（Research）”和“设计（Design）”这两个核心术语都具有多种含义、内涵和预期，且这些定义往往模糊不清。研究的目的被视为产生知识，使他人能够在知识生产者所从事的领域之外的其他领域中使用这些知识。这种知识是概括且抽象的。而设计的目的通常被理解为创建一种可应用于现实世界的具体解决方案：例如，一辆赛车、一个智能药盒或一项在线银行服务。该解决方案必须契合当前的具体情境（here and now）。尽管如此，人们经常注意到两者之间存在一些差异（见表 2.1）：

|  | **研究** | **设计** |
|---|---|---|
| 目的 | 通用知识 | 具体解决方案 |
| 结果 | 抽象的（Abstracted） | 情境化的（Situated） |
| 取向 | 长期 | 短期 |
| 产出 | 理论 | 实现（Realization） |
***表 2.1**** – 通常情况下，“研究”和“设计”这两个术语承载着不同的内涵。*

Liz Sanders (2005) 对学术界和工业界的设计研究进行了比较，并指出这两种方法之间存在类似的差异。我们可以在下表 2.2 中看到这些差异。

|  | **基于信息的设计研究（Information-Based Design Research）** | **基于灵感的设计研究（Inspiration-Based Design Research）** |
|---|---|---|
|  |  |  |
| 1 | 倾向于由接受过研究和/或应用社会科学培训的人员开展 | 倾向于由设计师进行探索和应用 |

| 2 | 大量借鉴了科学研究模型（Scientific model of research），坚持良好研究的原则：信度（Reliability）、效度（Validity）和严谨性（Rigor） | 正在探索其自身的良好研究原则，例如相关性（Relevance）、生成性（Generativity）和启发性（Evocativeness） |
| 3 | 基于调查、分析和规划的结果而构建 | 通过实验、模糊性和惊喜而构建 |
| 4 | 主要依赖于对过去事件的推演（Extrapolation）作为迈向未来的方式 | 主要从未来和未知中汲取灵感，将想象力作为表达的基础 |
***表 2.2**** – Sanders (2005) 列出了“传统”方法（例如 [可用性（Usability）](https://www.interaction-design.org/literature/topics/usability) 测试和民族志（Ethnography））与更具“设计式（Designerly）”方法（例如文化探针（Cultural probes）和生成式技术（Generative techniques））在设计研究中的区别。

尽管存在这些差异，设计活动与研究活动之间可能具有惊人的相似性——两者都旨在基于已知知识创造新事物。

两者互为组成部分。分析和评估是设计过程中的研究活动（但其可见度低于概念设计草图或最终产品）。而研究项目同样涉及实验装置（Apparatus）、刺激物（Stimuli）以及创造性新方向的开发（包括设计）（但在学术出版文化中，这些内容的可见度低于结果、证明和理论陈述）。

通过设计的研究 (Research through Design, RtD) 在这些张力 (tensions) 之中继续发展。与此同时，[设计教育 (design education)](https://www.interaction-design.org/literature/topics/design-education) 作为一门科学学科 (scientific discipline) 在艺术学院以及普通大学和工程类大学中不断发展，且博士生们不仅将设计技能作为其研究的核心组成部分，而且开始公开主张这一点。因此，这个令人兴奋的领域在不断扩张，持续推向最前沿，以便随着认知的深入，丰富的可能性能够产生突破性的洞见。

### 43.1.1 定义研究与设计

学术设计文化（academic design culture）仍在发展中，并与工程学、艺术、（社会）科学、认知科学、商业研究、人文学科、研究方法论和哲学等多样且截然不同的文化相重叠。话语（discourse）中使用的许多术语源自这些学科，并带有隐含的意义和内涵。这可能会导致误解，因为作者与读者，或说话者与听者，可能具有不同的背景，从而对术语产生不同的理解。虽然当不同的领域以这种方式“碰撞”时，这种风险往往不可避免，但其影响是不容忽视的：当 *设计（design）*、*研究（research）*、*交互（interaction）* 和 *体验（experience）* 等术语以各种组合形式串联在一起时，讨论可能会变得非常混乱。

为了弥补这一点，在本章中，我们将使用以简单术语表述的操作性定义（working definitions），以避免（或至少推迟）陷入与我们主题相关的各个学术领域的专业术语（jargon）和背景知识中。

表 2.3 列出了一些在后续讨论中将起到重要作用的术语。

|  | **操作性定义** | **关键相关术语** |
|---|---|---|
| 进行研究（Doing Research） | 以产生可供他人使用的知识为目的而开展的工作 | 问题（Question）、假设（hypothesis）、理论（theory）、调查（investigation）、解释（interpretation）、概括（generalization）、验证（validation）、发现（discovery） |

| 开展设计 (Doing Design) | 以产生可行方案 (feasible solution) 以改善给定情况为目的而开展的工作 | 想法与概念生成、综合 (synthesis)、开发、集成、发现、原型制作 (prototyping)、发明、实现 (implementation)、具现化 (realization) |
| :--- | :--- | :--- |
| 设计产出物 (Artifact) | 在设计过程中创建的对象（通常是物质性的） | 草图、蓝图、设计简报 (brief)、规格说明 (specifications)、愿景、提案、建议书、商业计划书 |
| 原型 (Prototype) | 研究中用于实现所研究的（交互）行为的产出物 | 实现 (implementation)、具现化 (realization)、[测试](https://www.interaction-design.org/literature/topics/test)、探索、解决方案、概念验证 (proof of concept)、构建 |
| 知识 (Knowledge) | 可以传达给他人的关于世界的理解 | 理论、书籍、出版物、专业知识 (expertise) |
| 设计实践 (Design Practice) | 设计专业人士开展工作的方式 | 设计简报 (brief)、合同、客户、利益相关者 (stakeholder)、工作室 |
| 实验 (Experiment) | 特定含义：一项受控的、假设检验 (hypothesis-testing) 的研究；通用含义：与现实世界情况的探索性接触 (explorative confrontation) | 特定含义：假设、统计数据、（因）变量 (independent variables)；通用含义：尝试、干预 (intervention)、探索 |
***表 2.3**** – 本章所用关键术语的工作定义*

这些定义并非没有争议。因此，这里对这些术语做一些说明，以阐明为什么我们需要对其进行明确定义。例如，将研究定义为“供他人使用”这一包含项，是一种界限 (demarcation) 设定，表明讨论的重点在于构建共享的

[知识体系（body of knowledge）](https://www.interaction-design.org/literature/topics/personal-development)而非仅仅是 [个人成长（personal growth）](https://www.interaction-design.org/literature/topics/personal-development)，这并不是说后者在其他语境下不能被称为“研究”。

我们在设计（以及研究）之前都加上了动词“进行（doing）”，以强调我们主要讨论的是 *设计活动（design activities）*，而非名词“设计（design）”可能具有的多种不同含义：如产品、造型、专业群体等 (Sanders & Stappers 2014, p26)。

在“进行设计（doing design）”的定义中，我们使用“解决方案（solution）”一词（而非“计划”或“提案”），以表明一个实现过程（realization）——尽管具有实验性质——通常是通过设计进行研究（Research through Design, RtD）的一部分。在某些语境下，“设计”一词的使用仅止于以愿景、插图或分镜脚本（storyboard）形式提交提案。而在 RtD 中，在实现过程中所面对的挑战通常被认为是工作的重要组成部分。设计所追求的改进可以针对问题（例如，现有情况中的糟糕元素）或机遇（例如，新技术的可能性）。其结果同样多种多样：一个（量产的）产品、一段软件、一项服务或一个系统。见图 2.4。

![](https://public-media.interaction-design.org/images/uploads/3ac428be526d747f9f336f1f9dc2134f.png)
***图 2.4**** —— 研究与设计所追求的结果通常不同。本章旨在描述关于设计对知识贡献的学术理论，并且在其中...

...本身属于中间类别，即“关于设计方法的研究（research about design methods）”。*

**“人造物（artifact）”**一词源于人类学/考古学，指代由人制造的东西，通常是一个物质对象。它将发挥重要作用，因为许多研究者认为设计师所制造的东西是“通过设计进行研究（Research through Design, RtD）”的核心。（注：在测量方法论（measurement methodology）中，“artifact”一词的含义完全不同，指的是测量误差，例如照片上的划痕。）

**“原型（prototype）”**一词以及动词“原型制作（prototyping）”在设计研究中，尤其是交互设计（interaction design）领域中变得非常流行。最初，该词是指量产产品的前身，它具有与最终产品相同的材质特性，但在实施过程中需要经过测试和开发。在设计研究中，“*原型（prototype）*”一词也被用于指代所有类产品的物理构建物。在交互设计中，纸质原型制作（paper prototyping）可以简单到仅为纸上的绘图。原型是比人造物更窄的一个类别。它们在某种意义上“像产品”，因为人们可以与它们交互并体验它们；而草图和蓝图则是关于预期情境和交互的较不直接的表征（representations），而非其实现（realizations）。在 RtD 文献中，一些作者使用“artifact”（或在英式/联邦英语中写作“artefact”）一词来表达我们预留给“原型”的含义，但并未明确区分两者。在

在本章中，我们采用上述区分——即每个原型（prototype）都涉及一个或多个人工制品（artifact），但并非每个人工制品都是“原型”（见图 2.5）。

***图 2.5**** —— 设计中不同类型“人工制品”的示例，其中只有一种我们将称之为“原型”（摘自 Keller, 2005, 第 89, 109, 107 页）。

对于**“知识（knowledge）”**这一术语，我们同样希望它不会引起任何混淆。知识的一个重要方面在于它与现实世界中的某些事物*相联系*，并且在引导人们未来的行动方面具有*用途*。知识可以是显性的（explicit，例如在书中用文字和图片描述）或隐性的（tacit，例如专业工匠基于其早先的经验进行创作时）。在研究背景下（无论是通过设计还是其他方式），寻求知识是为了能够将其与他人共享。显性知识可以通过直接的方式共享；而隐性或内隐知识（implicit knowledge）如何共享以及在何种程度上可以共享，则是讨论的一部分（见 4.1 节）。

最后，让我们来看看两个含义截然不同的词：**（设计）实践（(design) practice）**和**实验（experiment）**。我们不会广泛使用“实践”这个词，但它在文献中以两种截然不同的含义出现。一种含义是“一种设计式地处理问题的方式”，例如通过草图和快速原型而非理论推理来寻找可能的解决方案，这主要用于指代艺术与设计工作室中的工作方式。

另一种含义是指“设计专业人士的工作情境（the work situation of design professionals）”，在这种情境下，他们通常为客户服务，并遵循一份设计任务书（brief），其中可能包含客户提供的产品或服务是设计方案的一部分，且受到时间、手段和预算等商业约束。当 RtD（Research through Design，通过设计的研究）被定义为“将设计实践应用于因其主题和理论潜力而被选中的情境 [...]”（Gaver 2012, p937）时，可能指的是前一种含义；而当 Zimmerman, Forlizzi, and Evenson (2007) 提出一个旨在“造福 HCI（Human-Computer Interaction，人机交互）研究和实践社区”的模型（p493）时，则指的是后一种含义。

同样，“实验（experiment）”一词在狭义上（在“科学方法”中）被理解为一项受控研究（controlled research），其中变量被隔离和控制，且假设被验证或拒绝。但该词还有另一种用法——在更广泛的意义上，它指“尝试某些东西以观察其是否有效”，这既可以是探究（inquiry）或计划（program）的一部分（Redström 2011），也可以是面向行动的干预（action-oriented intervention）的一部分（Halse et al. 2010）（见 4.3 节）。

### 43.1.2 设计与研究的关系

研究与设计密切相关，但有所不同。两者都是旨在创造新事物的有目的活动（intentional activities）。然而，它们在（通常的）执行方式以及（通常）衡量其结果的价值标准方面存在差异。自本世纪第一个十年的后半段以来，许多可能的并置（juxtapositions）关系受到了关注——例如，将其中一个视为另一个的一部分，将两者视为相同或完全不同，或者探讨将其中一个应用于另一个（或应用于自身）时所产生的复杂情况。

### 43.1.3 面向设计的研究：将研究作为设计过程的一部分

观察、测量、访谈、文献综述、分析和验证等活动是许多设计方法的一部分，这些活动显然属于“研究”范畴。现代设计课程（design curricula）明确关注研究技能，其范围涵盖了从收集和解释科学知识的能力，到在需要时产生新知识的能力，如图 2.6 所示。由于科学理论是在概括和抽象的层面（generalized and abstracted level）定义的——例如，“人们能够很好地处理最多 7±2 个类别”——因此在将其应用于设计简报（design brief）时，必须弥补一个差距，例如，“为荷兰老年人设计一个组织每周购物的信息服务”。这一差距既涉及抽象程度（level of abstraction）（例如，“在设计情境中，哪些‘*类别*’起作用？”），也涉及充分性（sufficiency）（例如，“我们能否找到‘识别和处理’所选类别的适当方法？”以及“这些方法如何与该情境下所需的数十项其他考虑因素相协调？”）。如今，许多设计课程明确关注于收集和应用相关的科学技术信息，以及开展研究以了解设计对象所在情境的具体信息，这有时被称为**面向设计的研究（research for design）**。特别是，关于……的技术可行性（technical feasibility）和可用性研究（usability studies）

原型（Prototypes）——以及最近出现的关于用户需求（user requirements）的早期参与式研究（early phase participative studies）（即“[用户研究](https://www.interaction-design.org/literature/topics/user-research)”或“设计研究（design research）”）——已成为以用户/人为中心的设计方法论（user/human-centered design methodology）中被广泛认可的组成部分。

![](https://public-media.interaction-design.org/images/uploads/65b567b9d75b45330aebf5fdabbf74e1.jpeg)

***图 2.6**** – 基于研究的设计（Design informed by research）：收集并应用相关的科学和技术信息，并开展研究以获取有关设计场景的具体信息。

### 43.1.4 通过设计的研究（Research through Design, RtD）：将设计作为研究的一部分

当我们讨论 RtD 时，是指那些在知识生成过程中起塑造性作用（formative role）的设计活动。通常，这些活动被识别为来自设计专业的设计行为，且依赖于设计师的专业技能，例如：对复杂情况获得可操作的理解（actionable understanding）、对其进行框架构建与重构（framing and reframing），以及迭代地开发旨在解决该问题的原型（prototypes）。这种设计性的贡献（designerly contribution）可能简单到仅是为他人的研究制作刺激材料（stimulus material）。然而，更典型的情况是，它包含开发一个可能被误认为“产品”的原型或人造物（artifact），并且该原型在知识生成过程中起核心作用（见图 2.7）。例如，它将此前不存在的因素组合呈现出来，作为讨论的启发（provocation）；或者它创造了人们与产品之间进行此前无法实现的交互的可能性，而这些可能性是通过设计才得以存在——事实上，是变得*可观察（observable）*的。此外，在将该原型转化为现实的[构思（ideation）](https://www.interaction-design.org/literature/topics/ideation)、概念开发（concept development）和制作（making）的生成过程中，设计师将不得不面对机遇与限制，以及理论目标/构念（theoretical goals/constructs）的影响，以及

这些与世界中经验现实（empirical realities）之间的碰撞。换句话说，任何参与原型（prototype）设计的设计师都必须在现实世界的障碍中寻找路径，而这些障碍阻碍了在产品与其用户使用情况（usership）之间构建最佳桥梁。这一思考过程本身就带来了洞察（insights），其中一些可以被显性化并与他人分享。这就是事实如何从阴影中浮现并助力未来尝试的方式。

> “悲观者抱怨风向；乐观者期待风向改变；而现实主义者则调整风帆。”
> *—William Arthur Ward, 美国励志格言作家*

大多数关于通过设计进行研究（Research through Design, RtD）的学术出版物都聚焦于原型，并阐述导致该原型的某些设计步骤，其传达的信息类似于“制作这个原型确实需要设计技能，而且我们考虑了许多因素”，这就像工业设计实践中常见的对设计活动的描述一样。然而，这些活动本身可能正是产生洞察的地方。

> “创建原型的设计行为本身就是潜在的知识生成器（只要其洞察力不消失在原型中，而是反馈到能够将这些洞察融入理论增长的学科内及跨学科平台中）。”
> *—(Stappers 2007)*

设计和制作的行为要求设计师面对几种碰撞：在竞争或冲突的...

背景知识，在理论与技术之间，以及在梦想与现实之间。制作（Making）会激发一种特定的认知活动，这种活动可用于让人们意识到隐性价值（tacit values）和潜在需求（latent needs）（Stappers 2013）。

![](https://public-media.interaction-design.org/images/uploads/5c46c7a4d0865b43f035e75a921a9649.jpeg)

***图 2.7**** – 贡献于研究（左）与进行研究（右）的设计方式（Designerly ways）。在前者中，设计活动根据研究结果“凭推测（on spec）”地创建工具或刺激物；在后者中，设计行为在知识的生成过程中起到了塑造作用（formative role）。*

### 43.1.5 研究即设计：从事设计即从事研究

一些作者（例如 E. Zimmerman 2003）指出，设计是研究的一种形式，或者说设计与研究在本质上是相同的，因为这两项活动都能产生新知识。图 2.8 延续之前图表的风格，将其表示为一个单一的“团块（blob）”且没有箭头。这表达了设计师们的喜悦，即在每个设计项目中，他们（能够）学到一些东西：关于用户的生活、关于某项技术、关于一种新的机制或形式、关于如何创建有效的原型（Prototype），或者关于如何在预算、时间和手段有限的挑战性环境下对其进行评估。但将两者等同会剥夺我们讨论潜在差异的工具，而差异确实是*存在*的。而且并非每个设计过程都能产生（并）*提供给他人*的知识；事实上，大多数设计产物在完成一个“设计”后就结束了……仅此而已。许多设计并未最终转化为产品。历史上散布着许多从未进入“现实世界”的瑰宝，即便它们在现实世界中的潜力足以让其畅销。同样，并非每项研究都需要创建一种新的解决方案——许多研究仅满足于描述现状（status quo）。Friedman (2008) 抱怨道，许多采用通过设计进行研究（Research by Design）方法的作者，“为了追求术语的朗朗上口而采用了被误解的词汇，将其与一系列定义模糊的

“将隐性知识（Tacit Knowledge）与设计知识（Design Knowledge）等同起来的观点，提出将隐性知识与设计实践（Design Practice）作为一种新的理论化（Theorizing）形式”（第157页）。
与其他人一样，Friedman 认为将两者等同起来是没有意义的。

![](https://public-media.interaction-design.org/images/uploads/b47b27375c045b63485f4952804e7c2e.jpeg)
***图 2.8**** —— 一些作者将研究活动与设计活动视为同一回事。

### 43.1.6 开展研究，反之亦然

另一种相反的观点，即**设计与研究是完全不同或互补的**活动，甚至认为两者是互斥的（Mutually Exclusive），这种情况较少见。在那些由学者（Academics）主导研究、而由设计从业者（Design Practitioners）专门负责教学的学校中，人们有时会将研究者与设计者的区别视为角色与价值的分离，通常认为适用于其中一方的原则对于另一方而言无关紧要。同样，这种区分在本章的语境下并没有太大帮助；然而，从广义上来说，了解这一点是有用的。

### 43.1.7 其他关系

研究与设计之间还存在几种其他关系。在这里，我们将介绍其中几种，并非为了用文字游戏来困扰读者，而是因为我们在随后的讨论（即第 5 节）中会用到它们。研究者可以通过进入**设计研究（research into design）** (Frayling 1993) 的领域来研究设计是如何进行的；有时，它也被称为**设计方法论研究（design methodology research）**。[[1]](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/research-through-design#example)

同样，这些术语也可以用于自我指涉，例如在 Science Studies 中对研究方法进行评估的**研究研究（researching research）**，以及在设计师开发新方法和工具以支持设计活动（例如文化探针 [cultural probes]）时的**设计设计（designing design）**。在设计领域海量的会议和期刊论文中，很大一部分致力于描述所执行的过程，以及展示并反思使用这些工具和方法的经验。通常，这构成了论文主要学术贡献的核心。

最后，从某种意义上说，任何研究项目本身就是经过设计的。“实验设计（experimental design）”或“研究设计（design of the study）”这两个术语在各个学科中被用来指代一项研究的规划和设置——例如，使用哪些条件，或者如何将理论概念操作化（operationalize）为测量行为。虽然这些行为

虽然这些情况确实存在（且同样适用于我们讨论的这类研究项目），但这种普遍的理解并非我们所定义的「通过设计进行研究（Research through Design, RtD）」。相反，我们将 RtD 理解为通过*设计活动（design activities）*来产出知识。

### 43.1.8 er?

这些活动是否应当由经过专门培训的专业人士，例如拥有“设计师”等正式学位的专业人员来执行？一些作者将通过设计进行研究（Research through Design, RtD）视为设计从业者为研究做出贡献的方式，或者将设计实践视为产生通用知识的一种方式。本章的重点在于用于知识生产的设计（化）活动（design(erly) activities），而*非*那些在培训或经验方面*最适合*执行这些活动的人员的资质。

尽管如此，我们选择的示例主要来自具有设计培训背景的人员的工作，因为 RtD 的讨论在这一群体中最为活跃。但即便在这一群体中，设计专业的内涵、定义其专业活动的标准，以及知识产生和分享的方式与维度也存在巨大的差异。

设计与研究的许多应用领域需要来自不同学科的人员协作，每个人都拥有自己的技能、专业知识和态度。在这样的团队中，一名受过培训的设计师可以承担多种角色，包括沟通、引导（facilitation）、流程管理、框架构建（framing）与概念形成、探索性原型制作（explorative prototyping）、评估和评议——而过程中的其他利益相关者（stakeholders）同样可以承担这些角色 (Basballe & Halskov 2012)。

### 43.1.9 结论

这种多样化的关系导致人们在分析采用设计方法（Design Methods）的研究项目时，很容易对其中发生的过程产生困惑。所产生的知识是关于原型（Prototype）的吗（即，属于设计结果 [Design Result]）？还是关于参与者与其交互的方式（即，属于情境研究结果 [Contextual Research Result]）？或者是设计或研究的开展方式具有某种特殊性？该研究是否依赖于（专业的）设计技能（Professional Design Skills）？抑或是上述所有因素的（综合）体现？我们将在本章后续内容中不断回到这些问题。

### 43.1.10 “RtD”术语的历史

虽然大多数使用“通过设计进行研究（Research through Design, RtD）”这一术语的学术文献都集中在人机交互（Human-Computer Interaction, HCI）社区，但该术语起源于设计领域，并未特指交互设计（Interaction Design）。事实上，它还涵盖了诸如材料等其他领域。“通过艺术与设计进行研究（Research through Art and Design）”这一短语是由 Frayling (1993, 随后在 2015 年将其置于历史背景中讨论) 在一次面向 RCA 的演讲中提出的。在演讲中，他指出了设计社区感兴趣的三种研究方式：关于艺术与设计的研究（research into art and design，包括历史研究和感知研究）、通过艺术与设计进行研究（research through art and design，提及材料、产品开发和行动研究 [Action Research]），以及为艺术与设计而进行的研究（research for art and design，他以 Picasso 收集参考资料为例来说明，在这种情况下，“思维可以说，*体现在人工制品（artefact）中*”，第 5 页）。Frayling 的简短描述与上文 2.2 节中给出的定义非常一致。在随后的讨论中，“艺术与设计”这一短语被简化为仅指“设计”。一些作者出于方便而采用较短的术语，或者是因为他们在自己的学术社区中对“艺术”一词感到不太自在；另一些人则是为了将论点扩展到设计内部文化的多样性，甚至是因为他们认为艺术与设计之间没有区别。

“通过设计进行研究”这一术语主要在四个具有不同背景文化和地理特征的“活力中心（pockets of energy）”中被使用。

这些地点包括：英国和斯堪的纳维亚的艺术与设计社区，荷兰的技术大学和设计学院，以及美国的 人机交互（Human-Computer Interaction, HCI）社区。图 2.1 概述了本章所使用的关键来源。但相关文献的范围更为广泛，因为并非所有探讨我们在第 4 节中确定并讨论的问题的人都使用相同的术语（Terminology）。

![](https://public-media.interaction-design.org/images/uploads/cef8f1ad0f29c90ce18305c02ada7767.png)
***图 2.1**** – 通过设计进行研究（Research through Design, RtD）项目与文章的分布图，按时间及作者原籍国分布。此处显示的论文在本文参考文献列表中被引用 10 次或更多次。斜体表示第 3 节中的示例项目；粗体表示会议和资助计划（Funding schemes）。*

### 43.1.11 在 HCI 和 IxD 中

人机交互（Human-Computer Interaction, HCI）和交互设计（Interaction Design, IxD）社区在开发关于通过设计进行研究（Research through Design, RtD）的显性理论方面最为活跃，这可能是因为这些领域的出现是在研究型大学中，深深植根于且接近于计算机科学的同行评审（peer-reviewed）学术文化之中。HCI 和 IxD 都是年轻的领域。由于与实际应用紧密相关，它们必须处理由将信息技术提供的新可能性和复杂性具象化（giving form to）所带来的困难而引发的抽象问题。

以这种方式首次提及研究与设计之间关系的，可能是 Laurel (2003) 的著作 *Design Research* 的引言，且该主题在 E. Zimmerman 关于通过游戏进行设计研究的章节中得到了探讨。这简洁地描述了每个设计项目中出现的学习与解决问题的交织，并强调了问题是从设计实践中产生这一观点。

> Needs and Pleasures
  “设计是一种提出问题的方式。当设计研究通过设计实践本身发生时，它是一种在特定设计问题的有限范围之外提出更大问题的方式。当设计研究被整合到设计过程中时，新的且出乎意料的问题会直接从设计行为中产生。**(…)** 迭代设计（Iterative Design）是一种基于过程的设计方法论，但它也是设计研究的一种形式。在这三个案例研究中，问题产生于”

“设计过程——那些并非初始问题的一部分，但通过迭代设计和玩乐（play）而得以解答的问题。”**—(Zimmerman, 2003, p. 184)*

人机交互（Human-Computer Interaction, HCI）领域的讨论随着 J. Zimmerman 和 Forlizzi 的论文而兴起。Zimmerman, Forlizzi, and Evenson (2007, p. 494) 将该主题界定如下：“我们意在将‘设计研究（design research）’一词定义为产生知识的意图，而非旨在更直接地为商业产品的开发提供信息的工作”。在 Zimmerman, Stolterman, and Forlizzi (2010) 中，通过设计研究（Research through Design, RtD）被定义为“一种采用设计实践中的方法和过程作为合法探究手段的研究方法”。他们访谈了研究人员并发现，许多人将 RtD 视为一种“专注于通过制作人工制品（artifact）以实现社会变革目标的‘设计师式探究（designerly inquiry）’”（这在其他领域可能被称为‘社会设计（social design）’或‘批判性设计（critical design）’），并主张制定更严谨的方法论，以使其合法性更容易被既有的科学传统所接受。同样，Keyson et al. (2009) 建议将正式测量（formal measurement）纳入 RtD 的一部分，以验证并增强研究结果的鲁棒性（robustness）和泛化性（generalization）。

Gaver 反对这种形式化，认为这有扼杀设计本质特性的风险，并将设计实践置于与“某些主导的研究模式”相对立的位置；他警告不要“期望研究结果具有普遍适用性”。相反，该...

对通识知识（general knowledge）的主张以及分享洞察的期望，应当通过示例和反思，更深入地了解专家知识（expert knowledge）在手工艺社区（craft communities）中分享的模式。Gaver (2012) 将通过设计进行研究（Research through Design, RtD）定义为一种“设计实践（design practice）”，它被“应用于那些因其主题和理论潜力而被选中的情境”；由此产生的设计被视为“体现了设计师关于如何有效处理这些情境中隐含的可能性和问题的判断”，而对这些结果的反思则允许“阐明一系列主题、程序、实用和概念上的洞察”。Bowers (2012) 以及 Gaver and Bowers (2012) 指出，许多关于设计或设计内部的知识无法通过学术期刊的语言渠道轻易地抽象出来，而是通过带注释的作品集（annotated portfolios）来传达：这些作品集由设计模型、草图、照片等集合而成，并结合了旨在界定并突出这些人工制品（artifacts）中所承载的显著特征的解释。

Koskinen et al. (2011) 在教科书 *Design Research through Practice* 中总结了这些观点。此外，他们通过区分三种由传播（dissemination）地点定义的、具有设计特性的研究方式（designerly ways of doing research）——现场（field）、展厅（showroom）和实验室（lab）——展示了一系列项目及其如何融入设计活动中。

### 43.1.12 在设计领域

在设计界，该术语直到最近才变得流行，这同样是因为该领域正寻求加强其学术基础（academic grounding）并发展研究文化。Horváth (2007) 评述了多种设计研究项目，并根据设计与研究之间的关系将其分为三种方法：1）研究人员使用成熟学科的方法并将其应用于设计实践；2）工业实践中的设计师对他们在工业项目中的经验进行反思；3）“包含设计的研究（design-inclusive research）”，其中设计性行动（designerly actions），特别是研究原型（research prototypes）的创建，发挥了重要作用（另见 7.1 节）。

几位作者开始收集并研究一些研究项目的案例，在这些项目中，研究者本身就是设计师，且用 Brandt 和 Binder 的话来说，他们将“设计性实验（designerly experiments）置于研究的核心”（Brandt & Binder 2007）。例如，他们的研究比较了三位设计师的博士研究项目，每个项目都以不同的方式利用设计实验作为探索可能方案（possible program，旨在作为一组问题或探究）的手段：Kristina Niedderer (Falmouth College of Arts, UK 2004)、Ianus Keller (TU Delft, Netherlands 2005) 以及 Tuuli Mattelmäki (University of Arts and Design Helsinki, Finland 2006)。

在英国，一个每两年举办一次的会议于 2013 年启动，该会议专注于

基于实践的设计研究（practice-based design research），即从设计项目中产生的知识。该会议欢迎来自所有设计领域的投稿，并包含一个由设计研究产物（design research artifacts）组成的精选展览，以及在所谓的“兴趣室（Rooms of Interest）”中进行的圆桌讨论。
(RTD-conference, http://researchthroughdesign.org/)

“RtD”这一术语也已进入研究政策领域。2014年，Netherlands Organisation for Scientific Research 启动了一项名为“通过设计进行研究（Research through Design）”的研究计划，旨在加强创意产业以及从工业设计（Industrial Design）到游戏（Gaming）、建筑（Architecture）和时尚（Fashion）等各种设计学科的研究 (NWO-call)。在该荷兰计划中，大多数获得资助的项目是大学与学院之间的合作，且通常涉及专业设计机构和工业合作伙伴。

欧洲各大学的设计系正将对设计与研究方法的明确反思（explicit reflection）列入重要议程。然而，在工作方法以及进行讨论的学术环境方面存在显著差异。例如，在英国和斯堪的纳维亚国家，RtD 在艺术学校中成长，侧重于工艺（crafts）、工作室（studios）和展览（exhibitions）。在荷兰，Delft 和 Eindhoven 的技术大学（Universities of Technology）表现突出，这显示了其与工业和技术的明确联系，

以及社会科学。在美国，相关工作主要集中在基于人机交互（Human-Computer Interaction, HCI）的研究人员身上（如 CMU 的 Zimmerman 和 Forlizzi，以及 Indiana University 的 Stolterman 和 Bardzell）。

北欧国家受到的限制较少，不像英国以及澳大利亚、加拿大等英联邦国家那样，研究的许多方面由绩效评估（performance assessments）决定；此外，由于通常拥有全额薪资的博士职位（例如在 Sweden）以及与创意产业（creative industries）的紧密联系（例如在 Netherlands），北欧国家在知识生产（knowledge production）的问题、形式和格式方面发展出了极强的批判性（criticality）和实验精神。因此，斯堪的纳维亚国家并没有强调强烈的区分，而是发展出了一系列可被广泛定义为“通过设计进行研究（research through design）”的方法，其范围涵盖了从基于实践（practice-based, Mäkelä 2007）到“建构主义（constructivist, Koskinen et al. 2011）”，再到跨学科研究的“程序化（programmatic, Brandt & Binder 2007）”方法。

### 43.1.13 超越设计社区（Beyond the design community）

在 2.2 节中，通过设计研究（Research through Design, RtD）被操作化（operationalized）为通过一个过程来创造知识，在这个过程中，设计人工制品（design artifacts）——尤其是原型（prototypes）——被制作、试用并进行反思。尽管 RtD 文献将此视为设计技能、专业人员和社区在研究领域获得地位的特定生态位（niche），但此类方法在“设计”之外也同样存在。

社会科学中经常被提及与 RtD 开展方式相关的一种方法是行动研究（Action Research）。行动研究之父 Kurt Lewin 强调，理解某事（研究）与改进某事（设计）可以很好地结合在一起。改进的愿望可以激励并引导学习者，这一观点深得设计师的认同（并与本节前面提到的 E. Zimmerman 关于从设计项目中学习的观察相呼应）：

> “如果你真正想理解某件事，请尝试去改变它。”
> *—(Kurt Lewin 见于 Charles W. Tolman (1996) “Problems of Theoretical Psychology – ISTP” 1995. p. 31)*

另一个开展 RtD 的快速增长领域是设计人类学（Design Anthropology）（Smith et al. 2016）。设计人类学专注于解决人类学研究的描述性特质（descriptive nature）与从事设计时创造未来的态度（future-making attitude）之间的紧张关系。通过探讨设计人类学的定义及其演变，该领域的学者和从业者参与并推广 RtD 过程以及

关于将通过设计进行研究（Research through Design, RtD）视为一种不同研究方式的大部分论证，都涉及将其与占据主导地位的实验研究方法论的实证主义范式（Positivist Paradigm）进行比较。由于人机交互（Human-Computer Interaction, HCI）根植于 20 世纪 60 年代的心理学研究，这种范式在 HCI 领域尤为强势。不同的作者对 RtD 的正当性给出了不同的解释：有的认为 RtD 与那些还原论的、理性的范式（Reductionist, Rational Paradigms）截然不同 (Stolterman 2008)，有的警告不要将 RtD 简化为其方法 (Gaver 2012)，而有的则主张加强这两者之间的联系 (Keyson 2009, Zimmerman et al. 2010)。但更广泛的科学研究领域要大得多。Rom Harré 在其《20 great experiments》中，概述了科学史上突破性进展背后的多种方法：从 [Aristotle](https://www.interaction-design.org/literature/topics/aristotle) 对鸡蛋生长的观察，到 Michelson 和 Morley 的零结果（Null Results），后者为相对论提供了主要支持（见 5.4 节）。设计研究之外的方法多样性如此之高，以至于设计研究内部的方法可能比我们预想的具有更多的连接点。

特别是工程学，其历史证明了人造物（Artifacts）以及设计目标一直起着引领作用。桥梁、载人飞行、农业、医学和军事提供了许多可供比较的案例和框架。在下一节中，我们将引入这样一个例子——即 Wright 兄弟对飞机的开发，将其作为一个 RtD 案例。

类似的类比也可以在汽车行业的工业实践中找到。在这一领域，大型制造商让其设计师开发概念车（concept cars），并非为了将其推向市场，而是将其作为一种探索、验证并传达公司可能（且期望）的新方向的方式。尽管概念车已有数十年的历史且投入巨大，但关于*如何*将其视为研究项目（research projects）的学术研究却相对匮乏 (Mejia 2016)。这种前瞻性的项目和实践在人机交互（Human-Computer Interaction, HCI）领域也得到了关注。Zimmerman, Forlizzi, and Evenson (2007) 将 Philips 的“未来愿景（vision of the future）”作为通过设计进行研究（Research through Design, RtD）的一个例子进行了讨论。在这些案例中，设计行为（designerly action）的目的并非为了立即产出商业产品，而是为了获得一种更普遍的理解，从而引导其在其他地方的应用。

### 43.1.14 标签与名称

“RtD”这一术语作为一种标签已广受欢迎，用以表示从事设计实践能为研究工作带来的具体且独特的贡献，但相关问题并不总是以这个名称被提出。正如设计领域通常的情况一样，出现了大量用于推广技术和理论的“品牌（brands）”。作者们经常选择不同的名称，因为他们认为“通过设计进行研究（Research through Design, RtD）”这一术语并不完全与其所探讨的研究-设计结合方式相一致。

该领域并没有统一的专业术语。表 2.9 列出了为这类具有设计特质（designerly component）的研究方式所赋予的一些标签。然而，请注意，其中很少有描述足够精确到能给出清晰的界限（demarcation），或告知他人如何成功地开展此类研究。我们将会在第 4 节讨论一些此前尚未提及的作者。

| **标签** | **作者包括（但不限于）** |
|---|---|
| 实验性设计研究 (Experimental Design Research) | Brandt & Binder (2007) |
| 通过设计的实验性研究 (Experimental Research through Design) | Keyson & Bruns-Alonso (2009) |
| 通过实践的设计研究 (Design Research through Practice) | Koskinen et al. (2011) |
| 建设性设计研究 (Constructive Design Research) | Wensveen & Matthews (2014) |
| 概念驱动的设计研究 (Concept-Driven Design Research) | Stolterman & Wiberg (2010), Höök & Lowgren (2012) |
| 包含设计的研究 (Design-Inclusive Research) | Horváth (2007) |
| 探究驱动的 RtD (Inquiry-driven RtD) | Odom & Wakkary (2015) |
| 交互设计研究 (Interaction Design Research) | Zimmerman, Forlizzi, Stolterman (2007) |

| 迭代设计 (Iterative Design) | Zimmerman, E. (2003) |
| :--- | :--- |
| 程序化设计研究 (Programmatic Design Research) | Brandt, Redström, Eriksen, Binder (2011) <br> Bang & Eriksen (2014) |
| 研究导向设计 (Research-Oriented Design) | Falmann (2007) |

***表 2.9**** – 一些用于指代以设计方式开展研究 (designerly ways of doing research) 的不同专业术语 (jargon terms) 的示例*

### 43.1.15 结论

「通过设计进行研究（Research through Design, RtD）」这一术语主要用于设计社区的学术工作中，尤其是交互设计（Interaction Design）和人机交互（HCI）领域，但它与其他艺术、工程学科以及设计实践之间的共同点，比通常讨论的要多。在许多情况下，我们发现设计性行动（Designerly actions）不仅有助于实现单个产品或具体情境的局部改进，还能用于发现、例证、阐明和推广更普适的原则，从而使其能够应用于其他地方。

文献中表达的观点难以被统一地归类。作者们来自不同的背景并参考不同的资料，拥有不同的目标，探讨不同的方面，且基于不同的价值观。一些人试图将 RtD 与其他类型的研究（例如自然科学和社会科学中成熟的方法）区分开来；另一些人则试图将其与这些方法拉近，或者证明其作为另一种研究形式的合理性。其共同核心在于，他们主张设计活动及其特质对*知识产出（Knowledge outcome）*的贡献，特别是那些将原型（Prototypes）引入现实世界，并对其效果（有时包括这些人造物（Artifacts）的生成过程（Coming-into-being））进行反思、衡量、讨论和分析的活动。

正如 2.4 节所示，文献经常引入新的标签，尤其是用名词来表示某种特定类型的研究，而不是讨论一种共同研究方式的不同方面。特别是在

如果作者不提及“研究”或“设计”的具体实例，读者将很难分辨他们是在阐述同一种开展通过设计进行研究（Research through Design, RtD）的方式，还是在阐述几种可能并行存在且截然不同的方式。正如在讨论抽象概念（abstractions）时一贯的情况，拥有一组共同的具体示例、案例和可能实例无疑会有所帮助。这正是我们在下一节中试图提出的内容。

## 43.2 七个 RtD 项目案例

正如前文所述，关于设计与研究的讨论很容易陷入抽象概念之中。在本节中，我们将简要介绍一些能够体现第 4 节将要讨论的主题的项目。在选择这些案例时，我们首先选取了几个已经在 RtD（Research through Design，通过设计进行研究）背景下的学术文献中被讨论过的项目（例如 Brandt & Binder 2007, Zimmerman et al. 2010, Koskinen et al. 2011）。另外一些项目的加入是为了提供实证案例（empirical examples），以为第 4 节的主题讨论提供基础，并纳入 HCI（Human-Computer Interaction，人机交互）领域之外的相关工作描述。

本章介绍的七个案例展示了在探索、描述和评估方法上的多样性，以反映该领域的现状。在每个案例中，研究者-设计师（researcher-designer）都有一个被阐明的知识目标（knowledge goal），且研究结果已记录在案并与目标受众共享。但具体的问题以及传播（dissemination）方式各不相同。在每个案例中，为了探索关于研究问题的知识，研究者制作了一系列原型（prototypes）和其他人工制品（artifacts）。然而，这些人工制品的作用各异，设计师制作它们的方式，以及每个人工制品与先前知识之间的关系也各不相同。

接下来的章节将详细描述每个示例项目。在总结章节（3.8）中，我们将从四个主要方面对它们进行综合分析：

- 他们学到了什么？
- 这些知识是如何与他人分享的，分享对象又是谁？
- 他们做了什么（方法与过程）？
- 创造了什么（原型（Prototypes）的作用）？

随后，在 4.1–4.4 节中，我们将讨论文献中是如何探讨这四个方面的。

该列表并非所有通过设计研究（Research through Design, RtD）项目的完整概览，也不包含所有被高频引用的作品。相反，选择这些示例是因为（在网上）有充足的文档记录，以便读者能够自行查找研究的更多细节。对于每个示例，我们提供了相关参考文献，其中该工作被描述为 RtD，并由研究者本人以外的人员对其进行定位或界定（Framed）。通常，第一篇参考文献是博士论文，其中通常包含基于该项目的其他文章的进一步引用。在本节中，只有在后者明确讨论研究方法时，我们才会将其纳入。

在可能的情况下，我们用“创造之物”的名称来标记示例。一个原因是帮助读者记住这七个示例。第二个原因是，原型和其他设计产物（Design Artifacts）的作用将是 4.2 节的一个重要主题。对于每个示例，我们还备注了第 4 节的其他主题：产生的知识、知识是如何习得的，以及分享知识的目标受众。

### 43.2.1 Wensveen 的闹钟

Stephan Wensveen 在 Delft University of Technology 的博士项目始于一个理论问题：设计交互的情感质量（Emotional Quality of Interactions）是否可行？为了研究这些交互，Wensveen 设计并制作了一款闹钟，其界面包含 12 个滑块，用户可以用双手移动这些滑块，以设定所需的闹钟“情绪”（Alarm 'mood'）。

![](https://public-media.interaction-design.org/images/uploads/d83020cf0f7b5944c6c7d7dc1b2c874d.png)
***图 3.1** – 设定闹钟的不同方式（由 Stephan Wensveen 提供）。请思考这 12 个滑块所带来的可能性范围——以及其中涉及的所有手指“编舞”（Finger choreography）。*

该原型记录了滑块随时间变化的运动模式（Motion-over-time patterns），以捕捉用户的手势（Gestures）。在主要实验中，研究者记录了处于不同情感状态的参与者的运动模式。为了让参与者进入这些状态，他们被要求观看选定的电影片段，然后以与场景相匹配的方式设定闹钟。随后，这些模式被观察并记录下来。

测量手段和“实验设计”（Experimental design）使得研究者能够将研究结果拟合并发表在实验研究传统（Experimental research tradition）的框架内。该原型和实验在多篇论文中得到了探讨和讨论（Djajadiningrat et al. 2004, Wensveen et al. 2002, Zimmerman 2010, Wensveen & Matthews 2015），但许多细节仅见于

这篇博士论文 (Wensveen 2005) 中，值得注意的是，论文包含了极其丰富的插图，包括相关现有产品的示例（33 幅图）、研究者制作的原型（19 幅）及他人制作的原型（9 幅）、研究工具（21 幅）、结果数据（28 幅）以及图表（14 幅）。这些视觉资料构成了论文论证过程的重要组成部分。

在此过程中产生的**知识（Knowledge）**涉及对有形交互（Tangible Interaction）的理论贡献，具体而言，是关于有形交互中[为情感而设计（Designing for Emotion）](https://www.interaction-design.org/literature/topics/emotional-design)的原则。

研究者制作了几个闹钟的**原型（Prototypes）**，用户可以通过物理交互来设置所需的闹钟“氛围（mood）”。

知识是通过“实验设计（Experimental Design）”产生的（此处指研究方法论意义上的自变量和因变量的设计）。结果通过博士论文和学术出版物进行分享。视觉记录（Visual documentation）在此过程中也发挥了重要作用。

*发表于 Wensveen 2005，描述见 Zimmerman et al. 2010, Koskinen et al. 2011。*

### 43.2.2 Keller’s Cabinet

Ianus Keller 在代尔夫特理工大学（Delft University of Technology）的博士项目专注于支持设计师如何处理他们为寻求灵感而收集的视觉素材（visual materials）。在项目过程中，研究者收集了相关的理论要素，并据此做出选择，以支持开发一系列交互原型（interactive prototypes），让人们能够操纵并体验这些视觉素材。初步原型探索了不同显示表面、交互尺度（scales of interactions，例如手指 vs. 手掌 vs. 手臂）以及技术（例如表面投影 vs. [虚拟现实（Virtual Reality）](https://www.interaction-design.org/literature/topics/virtual-reality)）的可能性和效果。最终的原型名为 Cabinet（橱柜），由一个可对图像进行分组和排列的桌面显示器，以及一种导入数字和物理图像的手段组成。

![](https://public-media.interaction-design.org/images/uploads/53cbbac10c84d5f3fd53f6c18d51ba92.jpeg)
***图 3.2**** – 用户使用 Cabinet 排列用于寻求灵感的视觉素材（图片由 Ianus Keller 提供）*

在此过程中学到的许多内容跨越（连接或介于）不同的学科或理论之间；大部分学习发生在原型制作过程中，以及向实验室访客进行非正式演示时的解释、提问和讨论中，而非在正式的实验中。

该研究原型在会议上展出（并获得了一项设计

（在第 3 届国际家电设计会议 [3rd International Conference on Appliance Design] 上获得研究奖），且研究结果以独立研究的形式发表在期刊上。但研究团队认为极其有价值的几项洞察——例如三种交互范围（three ranges of interaction）——结果却难以发表，因为它们不属于任何现有的期刊类别。同样，该论文包含了在其他地方找不到的关键信息——这反映出你正在阅读的主题确实在触及现有知识的前沿。

在此过程中产生的**知识（knowledge）**涉及创意专业人士利用视觉材料获取灵感的多种方式，以及他们如何访问和存储这些材料。这包括处理虚拟现实（Virtual Reality）环境的“草图式（sketchy）”交互可能性、各种显示格式（墙面、桌面、手持设备）的可用性（usability），以及桌面交互格式。

研究中使用了一系列交互式**原型（prototypes）**，人们可以通过这些原型操纵并体验用于激发灵感的视觉材料。知识是通过结合用户研究（user research）（包括对领域专家的访谈以及对创意专业人士使用灵感材料的上下文研究 [contextual studies]）和迭代原型设计（iterative prototyping）（其中第一个原型在设计研究工作室中使用，最终原型在三个设计工作室为期一个月的干预期间进行了测试）而产生的。

机构）。研究结果通过学术出版物（Academic publications，包括博士论文和论文）以及展览（Exhibitions）进行分享。
*发表于 Keller 2005；详见 Brandt & Binder 2007, Stappers 2007, Stappers et al. 2014。*

### 43.2.3 Gaver 的漂移桌（Drift Table）

Bill Gaver 在 Royal College of Art 的 Drift Table 项目被呈现为一个开放式研究（open study），旨在探讨如何探索数字技术对家庭环境的影响与机遇。Gaver 强调其开放性，并拒绝任何先验框架（a priori framing）或概括性的结论。

正如 Gaver et al. (2004) 所描述的：
> “Drift Table 是一张咖啡桌，配有一个小型视口（viewport），用于显示缓慢变化的英国景观鸟瞰图（aerial view）。在桌面上移动重量会改变其表观高度、方向和速度。由于有约 1 TB 的英格兰和威尔士摄影照片可供查看，这张桌子可用于探索乡村、前往朋友家、探讨地理问题，或者仅仅是静静地观察世界的变迁。”

![](https://public-media.interaction-design.org/images/uploads/e1ac4772ae8e2039b2d6909b83f8d3ee.jpeg)
***图 3.3**** – Drift Table 的细节与部署（由 Interaction Design Studio 提供）*

该原型（prototype）具有明确的功能并采用了最先进的技术；然而，它明确地不基于用户需求（user needs）、功能目的或预期的效益。相反，它是文化探针（cultural probe）的延伸，是设计师向参与者发起的一种启发（provocation），旨在“获得惊喜，学习能够学习的一切……”，并且是“一种开发新价值和目标、学习新事物以及实现新 [目标/成果] 的机制”。

“理解（understandings）” (Gaver et al. 2003)。

在此过程中产生的**知识（knowledge）**涉及对家庭环境数字技术的新理解和新价值，以及游戏化设计（ludic design）的原则（这些原则是通过实践和策略（tactics）而开发的）。

在本案例中，经过多次**迭代（iterations）**，最终将最先进的原型部署在实地，以进行民族志观察（ethnographic observation）。知识是通过在详细的设计决策过程中所制定的策略而产生的。这些策略兼顾了初始假设（opening assumptions，旨在明确地引导设计过程）以及团队理解的变化（这些变化源于观察人们在长达六周的时间里如何与该人造物（artifact）共处）。结果通过多种方式分享，包括学术出版物、视觉文档、带注释的作品集以及展览。

*发表于 Gaver et al. 2003，描述于 Zimmerman et al. 2010。*

### 43.2.4 Mattelmäki 的探测工具包（Probing Kits）

Tuuli Mattelmäki 在芬兰赫尔辛基艺术设计大学（University of Arts and Design, Helsinki）的博士项目旨在为共情设计（Empathic Design）方法提供支持。在一系列于不同工业产品开发环境下开展的案例研究中，研究者设计并评估了用于引导最终用户（End-users）和其他利益相关者（Stakeholders）参与共情设计过程的工具和技术。本研究中的原型既包括有形的（Material，如工具包 Toolkits 和工作手册 Workbooks），也包括无形的（Immaterial，如计划、引导环节的脚本）。

![](https://public-media.interaction-design.org/images/uploads/e1058e9edb225c1eb7c9b30885b4e330.jpeg)
***图 3.4**** – 支持共情设计的有形与无形原型（图片由 Tuuli Mattelmäki 提供）*

Mattelmäki 的实验探讨了如何在特定设计项目的背景下，为特定场景设计共情探测器（Empathic Probes）。每个设计项目都是一个迭代过程，包括在接近正常的专业环境下进行规划（Programming，即反思并向前推进）和开展实验。这种从一个项目到另一个项目的循环，与其说是方法的积累或完善，不如说是一种特定的设计实践，它得益于在广泛不同领域中反复进行的迭代。通过这种方式，它建立了一套自己的典范工具库（Repertoire of exemplary tools）。

在此过程中产生的**知识（Knowledge）**与共情设计相关，并包含了一套典范工具库。

有形和无形的**原型（Prototypes）**包括用于开展环节（技术）的工具包（Toolkits）、工作手册（Workbooks）和脚本（Scripts）。

该工作通过在不同领域中进行探测实验（Probing experiments）与反思的循环，**迭代地（Iteratively）**推进，直到形成一套共情设计实践（Empathic design practice）并建立起一套工具库（Repertoire of tools）。

结果主要通过博士论文和学术出版物进行分享。此外，还通过将其嵌入到特定的设计实践/工作室（Design practices/studios）并对其进行转化而得以传播。

*发表于 Mattelmäki 2006，描述见于 Brandt & Binder 2007。*

### 43.2.5 Lundström 的能量可视化（Energy Visualizations）

Anders Lundström 在瑞典斯德哥尔摩的瑞典皇家理工学院（Royal Institute of Technology, KTH）开展的博士研究，关注于如何为能量敏感交互（energy-sensitive interaction）进行设计，以便电动汽车的驾驶员能够更好地管理能量的使用与消耗。该项工作的核心[动机（motivation）](https://www.interaction-design.org/literature/topics/motivation)是利用设计来探索此前未被发掘的领域，并开辟一个新的设计空间（design space）（例如，能量敏感交互）。这一设计空间被认为包含了针对未来电动汽车理想交互方式的、可能无穷无尽且具有价值的设计方案。

![](https://public-media.interaction-design.org/images/uploads/6b4508951e6be47e52e7085d5abe7e56.jpeg)
***图 3.5**** – 能量敏感交互的信息可视化（information visualizations）原型（由 Anders Lundström 提供）*

该研究始于一项实验室研究，旨在实验基于地图的续航里程（driving range）可视化的新维度，随后转向对驾驶行为（driving behavior）的研究。随后的原型和研究逐渐聚焦于那些被认定为关键的方面，即驾驶员为了管理电池而需要理解并积极应对的因素（即续航里程、行驶速度与气候控制（climate control）之间的关系）。

在此过程中产生的**知识（knowledge）**涉及对“能量敏感交互”这一概念的定义及其操作化（operationalizing）。

为了探索驾驶员优化管理电动汽车电池所需的关键维度，本研究创建了一系列信息**可视化（Information Visualizations）**方案。该工作通过一系列旨在研究电动汽车具体续航里程问题（Driving-range issues）的设计实验（Design Experiments）和研究展开。研究结果已通过博士论文（Ph.D. dissertation）和学术出版物（Academic publications）发表。

*发表于 Lundström 2016，在本章中首次进行描述。*

### 43.2.6 Rygh 的 2.5D 材料样本

在 Karianne Rygh 于 Design Academy Eindhoven 开展的研究项目中，其起点是一项由工业合作伙伴开发的全新 2.5D 打印技术，该项目是与印刷行业领导者 Océ/Cannon 合作完成的。与许多新材料和新技术一样，该打印技术虽然前景广阔且引人入胜，但尚未产生实际的应用。其原因被认为是缺乏能为设计师提供灵感的“启发性示例（inspiring examples）”。

![](https://public-media.interaction-design.org/images/uploads/5e4d2bf41739c46789128019793c570b.jpeg)
***图 3.6**** – 2.5D 原型样本（由 Karianne Rygh 提供）。*

Rygh 着手探索 2.5D 打印技术的可能性，并创作了大量打印表面、伪织物（pseudo-cloth）和打印效果的示例。这些成果在展览中给观众留下了深刻印象。随之而来的问题自然是：“这是研究吗？还是设计？”这是一项在寻找应用场景的技术，但既没有在理论层面被界定为“供他人使用的知识”，也没有在产品层面被界定为“应用”。但这个集合能够引导并启发他人；它探索并记录了一个解决方案空间（solution space），就像早期的 18 世纪蝴蝶标本集和探险家地图那样。

在此过程中产生的**知识（knowledge）**涉及 2.5D 打印的解决方案空间，即通过探索和表达这项新技术，创造出种类繁多的 2.5D 打印**人造物（artifacts）**。

这一过程是以一种在制作中思考（thinking through making）的方式展开的。它旨在通过对相关案例的探索与记录来启发他人。研究结果通过丰富的视觉记录和展览进行分享。

*发表于 Rygh, (2015 a,b), CRISP(2015)。*

### 43.2.7 莱特兄弟的飞机

威尔伯和奥维尔·莱特（Wilbur and Orville Wright）作为我们现在所称的飞机的发明者而闻名，或者正如他们在专利中所描述的，是“比空气重的飞行机器（heavier-than-air flying machine）”。他们的发明发生在本文提到的其他项目之前一个多世纪，且并非在大学或设计学院完成。然而，我们将他们列入这些示例中，是因为他们必须克服若干障碍，而他们克服这些障碍的方式，对于我们在“通过设计进行研究（Research through Design, RtD）”中所描述的“设计性行动（designerly actions）”具有典范意义。其中最著名的是他们获得专利的发明——（i）“机翼翘曲（wing warping）”，即通过改变机翼的形状使飞机转向（这一点在后来是通过机翼上的襟翼（flaps）实现的，但在他们的实验中，这意味着他们改变了*整个*机翼框架的形状）。

![](https://public-media.interaction-design.org/images/uploads/aa861f2e5f3dc80fad1e4d9d3278deb3.png)
![](https://public-media.interaction-design.org/images/uploads/156880818a9664dcaf43bc5622a746ac.jpeg)

***图 3.7**** – 莱特兄弟的一些改进：上方：用于比较机翼剖面（wing profiles）空气阻力的第一个风洞（wind tunnel）原型，以及最终的原型风洞（根据 http://www.wright-brothers.org 的图片绘制）；下方：具有机翼翘曲功能和人工控制的飞行器原型。[Library of Congress, Prints & Photographs Division, LC-DIG-ppprs-00626]*

这一解决方案的基础在于他们对飞行核心问题的 (ii) *框架化（framing）*：他们不将其视为如何离开地面，而将其视为如何在 *三* 维空间中控制 *运动方向*。大多数竞争对手都专注于实现升力（lift），但忽略或低估了转向问题，而这类机动（maneuvers）操作需要人类飞行员对飞行器进行精细的操作。到 1903 年 12 月实现动力飞行（powered flight）时，Wright 兄弟自 1900 年起就已使用滑翔机（gliders）进行了广泛的空中探索。

在此过程中，他们的项目要求他们 (iii) 详细研究机翼形状的空气动力学特性（aerodynamic qualities），(iv) 基于对机翼形状的认知制定螺旋桨（propellors）理论，(v) 构建实验室仪器和测量方法（如风洞 wind tunnel），(vi) 寻找让飞行员能够利用体重及双手控制飞机的方法，(vii) 开发轻量化发动机，以及 (viii) 开发用于辅助起飞的发射弹射器（launching catapult）。其中一些贡献 (i–iv) 处于“实现人类可控的动力飞行”的核心；而另一些 (v–viii) 则是次要工作，他们认为这些是为完成任务而 *被迫* 做的，但这些工作本身对于他人而言也是极具价值的贡献。除了实用价值以及系统且精确的测量之外，他们对飞行问题的重新框架化（reframing）是一项核心贡献，这构成了当今设计技能（design skills）概念的核心 (Stappers & Flach 2014)。

在此过程中，他们利用了此前发表的文献（并对其发表了修正），设计、制造并测试了一系列原型（Prototypes）（并记录了其试验过程）。

这一过程中产生的**知识（Knowledge）**涉及多项发现，包括：
- 机翼形状的空气动力学（Aerodynamics）
- 螺旋桨的空气动力学
- 将飞行界定为转向控制（Steering-control）问题，而非升力（Lift）问题
- 人类操作员的控制与交互（Interaction）
- 空气动力学的测试方法（风洞 Wind tunnels）
- 支持实验的辅助设备（轻量化发动机 Lightweight engine）

过程中涉及了实验室仪器、飞机部件以及飞行飞机的多种**原型（Prototypes）**。

该过程包含了实证研究（Empirical studies）和系统性测试。研究人员在仅用时六年的计划中，开展了这些多样化的测试与实现。

结果通过演示和展览、论文、专利以及巡展进行分享。

*详见 Bernstein, 1996, Stappers & Flach 2014, 以及热门在线资源，例如 http://www.wright-brothers.org/。*

### 43.2.8 结论

虽然这仅是七个示例，但它们涵盖了通过设计研究（Research through Design, RtD）实践方式的大部分多样性，并为下一节中关于主题的讨论提供了参考基础。

***表 3.1**** – 七个示例的比较*

## 43.3 RtD 讨论中的主题

在关于通过设计进行研究（Research through Design, RtD）的定义及其开展方式的反思中，设计研究者们正努力寻找通过设计式实验（designerly experimentation）所能产生的知识贡献的特定“特质（qualities）”。目前已有许多问题被讨论：

1. RtD 获得了哪类知识？
2. 原型（prototype）或人工制品（artifact）起到了什么作用？
3. RtD 项目的开展是否有特定的方式？
4. 知识是如何传播的，它是如何触达受众的，而这些受众又是谁？
5. RtD 与其他研究方式之间有何关系？
6. RtD 项目可以将设计作为主要目标吗？
7. 其学术地位如何：RtD 应当归属于哪里？

对于这些相互关联的问题，目前还没有最终答案，甚至没有一个被所有人公认的表述方式。而且，并非所有作者都探讨了所有这些问题。在本节中，我们将探讨一些已被讨论的主题和模型。问题 1 和 2 涉及知识和原型，关注的是符合“是什么（What?）”的名词。问题 3 和 4 涉及学习和分享，需要的是解决“如何做（How?）”的动词。本节将处理如图 4.1 所示的这四个主题。问题 5 到 7 涉及更宏观的视角——即“它在其他研究方式中处于什么位置，以及以这种或那种方式进行研究有什么好处？”——这些将在第 5 节中提及。

![](https://public-media.interaction-design.org/images/uploads/28d0dd2e7435230426275048a4330757.png)
***图 4.1**** – 本节讨论的主题：
左侧显示的是设计师正在进行通过设计的研究（Research through Design, RtD），以及他对下方人工制品（Artifacts）的反思和明确讨论，以及这些制品实现和评估的方式。这些人工制品可以是原型（Prototypes）和草图（Sketches），其中许多被丢弃在“垃圾桶”中，从而失去了沟通的价值。中间是一个光谱，顶部是抽象的显性知识（Explicit Knowledge），底部则是情境化（Situated）、多维的、物质性的隐性知识载体（Tacit Carriers of Knowledge）。右侧的箭头和人物展示了所学到的知识是如何被“知识使用者（Users of Knowledge）”——即其他设计师和研究人员——在他们试图在其他地方产生知识和/或社会影响的过程中所吸收的。垃圾桶则代表了一个问题：在制作那些从未完工的人工制品过程中所学到的经验将何去何从。

### 43.3.1 知识的类型

“知识（Knowledge）”的概念在哲学领域有着悠久且深厚的历史，研究通过设计（Research through Design, RtD）的相关文献有时会提及这一点。然而，鉴于其历史如此丰富且根深蒂固（涵盖了数个世纪和多种传统），大多数研究者在开展工作时倾向于使用通用概念，而无需明确或详尽地依附于特定的历史思想流派。此外，我们在此关注的领域仍然处于“新兴”阶段，并持续在最前沿进行开拓。因此，一个合适的思想流派可能需要根据当前所面临的核心问题而逐步构建。

我们将知识定义为“可以共享的关于世界的理解（understanding about the world which can be shared）”（见 2.1.1 节），这一工作定义（working definition）表达了这样一种考量：尽管设计师在参与设计项目过程中可能会学到很多，但这种个人学习（private learning）通常是直觉性的且处于隐性（tacit）状态，由于其未与他人共享，因此*不应*被计入研究成果。

许多讨论已经探讨了以下问题：“研究通过设计（RtD）中的研究成果是什么？”、“产生了什么样的知识？”、“哪些内容已经或能够传递给他人？”以及“如何对其进行记录？”。较少被讨论但同样重要的问题是：“哪些内容被重复利用了，以及是如何利用的？”。其中部分问题将在本节中探讨，其余问题将在随后的章节中讨论。

### 43.3.2 抽象与泛化（Abstraction and Generalization）

根据定义，理论是在高度抽象（abstraction）的层面上构建的，以便它们可以被应用于许多不同的情境（泛化，generalization），而这些情境随后被呈现为抽象概念的*实例化（instantiations）*。因此，Newton 关于“物体（bodies）”运动的定律既可以应用于苹果和橙子，也可以应用于火箭和网球。在更接近 HCI 的领域，Miller (1956) 的“七加减二法则（Law of Seven, Plus or Minus Two）”（即 7±2，指人们能够流畅地处理少量类别，但在面对大量类别时，其整体掌控力会崩溃）可用于指导计算机界面中菜单的设计，或用于确定创建多少个[用户角色（personas）](https://www.interaction-design.org/literature/topics/personas)以支持设计团队而不过度增加其负担。与抽象原则相对的是我们在现实世界中所处理的具体现象和事物，在那里不存在所谓的“物体”，只有苹果或橙子（更准确地说，只有“这个苹果”和“那个橙子”）。在抽象与具体、普遍与特殊之间建立联系，是任何研究中的一项重要技能和挑战。在科学实验方法中，研究人员寻找或创造能够作为其理论概念之“实例（instances）”的具体事物——也就是说，他们在实验室测试中选择苹果和橙子来充当“物体”。反之，他们可能会收集这个苹果和那个橙子，并

将它们视为“物体（bodies）”以观察其理论如何适用。但这些苹果和橙子同时也是水果、生物实体、食物、有颜色的物体等。Newton 和 Miller 的定律之所以有用，是因为它们隔离了*单一*的维度，而忽略了其他所有方面。正如一个抽象概念（abstract concept）可以应用于许多实例，一个具体事物（concrete thing）也具有许多面向（facets）。因此，可以通过许多不同的*视角（lenses）*对其进行研究。

### 43.3.3 显性（Explicit，陈述以文字形式呈现）与隐性（Tacit，人工制品即陈述）

普遍共识认为，在设计过程中产生的知识通常丰富且多样，但同时也具有不完整性、开放性和模糊性。例如，关于设计和使用的文字记录无法捕捉到隐性知识（Tacit Knowledge, Höök et al. 2015）。这并不是说此类知识无法传递，而是说它不能仅通过文字来传递。物质人工制品（Material Artifacts）和体验被认为是这种传递的一部分。

Ingold (2013) 将隐性知识的区别解释为“认知（knowing）”与“讲述（telling）”之间的差异，并描述了创作者的认知和实践方式是如何通过“双手”来讲述的。人工制品，尤其是原型（Prototypes），被认为是此类知识的载体。基于这一立场，有人认为原型本身*就是*知识，但很少有人会同意仅凭“这个苹果”本身就能说明它是一个“身体”。这种框架（Framing）必须被显式地添加。

在通过设计进行研究（Research through Design, RtD）中，文本和视觉记录（如发表的论文、文档、描述、目录条目、图解）通过指向人工制品中令人感兴趣的特征来突出这些特征，使其成为特定社区内讨论的焦点。这些文本可以被视为对其中所描绘的物理对象的*注释（Annotations）* (Gaver & Bowers 2012)，而不是将物理对象视为抽象概念的实例化（Instantiation）。

由文本表示的概念。Bowers (2012) 引入了 Wittgenstein (1953) 关于由“家族关系（family relations）”定义的类别的观点：在诸如“游戏”之类的类别中，任意两个成员之间都存在易于描述的相似性，但无法为所有成员的属性制定一个统一的通用规则。因此，这些文本-描绘组合（text-depiction combinations）的作用在于解释并将设计实例串联成一个连贯的整体，而非用理论来取代这些实例。

### 43.3.4 处于抽象理论与具体制品之间的中间层

随着通过设计进行研究（Research through Design, RtD）在人机交互（Human-Computer Interaction, HCI）和交互设计（Interaction Design, IxD）领域作为一种有效研究方法的普及，学术界出现了关于设计知识的“中间形式”（intermediary forms）（Höök et al. 2015）的不同提议——也就是说，这些设计知识形式处于“世界中的事物”（things-in-the-world，即“实例” [instances]、实际设计、最终具体物 [ultimate particulars]）与“抽象”（abstractions，即理论、概括）之间。这些中层解决方案（mid-level solutions）关注如何阐明、验证以及构建通过设计研究获得的知识。中间层知识的形式可以涵盖从单一的设计解决方案（single design solutions）（Stolterman 2008）、带注释的作品集（annotated portfolios）（Gaver & Bowers 2012）、强概念（strong concepts）（Höök & Löwgren 2012），到评论（criticism）（Bardzell et al. 2012）以及通用理论的操作化（operationalizations）（Lindwell et al. 2003）。

![](https://public-media.interaction-design.org/images/uploads/5243cb4669fd7cd80930515688c6626a.png)
***图 4.2**** – 作为从通用到具体维度的抽象（Löwgren 2013）*

单个的概念设计（concept design）可以被视为一个更通用理论概念的实例化（instantiation）——即提供具体示例或应用的客观事实或行为——从而为理论提供支持，并且它会对该领域的后续研究和未来的设计产生影响（Stolterman & Wiberg 2010）。例如，Dynabook 的概念设计在 HCI 和计算机科学领域具有深远影响。它由 Alan

20 世纪 70 年代初，Kay 及其在 Xerox PARC 的同事们将 Dynabook 视为儿童学习背景下未来个人计算的愿景。Dynabook 将建构主义学习（constructivist learning）的概念具体化，使其“无法被简单地归类为实例或理论”（引用自 Höök & Löwgren 2012）。进一步而论的是“强概念（strong concept）”这一 notion (Höök & Löwgren 2012)。强概念是一种中层知识（intermediate-level knowledge）形式，它比具体的实例更抽象，并在新设计的创建过程中发挥直接作用。作者将“社交导航（social navigation）”描述为强概念的一个例子。社交导航是指通过将他人的集体或个人行为可视化，从而帮助用户在信息中进行导航。

……空间，并决定下一步去哪里以及选择什么。这一理念已被应用于各种设计场景中，并被广泛借鉴（Appropriated）。

另一个更简单的例子是 *Angry Bird* 应用中的弹弓式触控交互（Slingshot touch interaction），现在它被广泛应用于从休闲游戏到蓝牙配对设备通信的各种触控界面方案中。

然而，通过中间设计知识（Intermediary design knowledge）从具体设计中提取知识，不能且*不应该*取代对具体设计案例和设计评述（Design critique，如在建筑学中）的需求 (**Höök** et al. 2015)。

![](https://public-media.interaction-design.org/images/uploads/a9279024f7408250e7ad13407e098392.png)
***图 4.3**** – Höök & Löwgren 2012, p. 23:2 展示了介于抽象（理论）与具体对象（当其符合理论时的标记实例 [Labeled instances]）之间的几种知识形式。

### 43.3.5 人工制品的多样性与框架化（Multiplicity of artifacts and framings）

Gaver and Bowers (2012) 认为，中层知识（middle-level knowledge）可以通过一组相互关联的设计示例及其相应的框架化注释（annotations framing them）来填充。这与 Wittgenstein (1953) 关于具有「家族相似性（family resemblance）」的对象集合的概念相呼应——即，它们构成一个单一的群体，但该群体无法由单一规则定义；尽管如此，群体中的每对成员之间都共享某些特征。

Gaver 明确反对泛化（generalizing），或者说反对试图提取普遍适用的知识，正如行动研究者（action researchers）否认在特定情境下行之有效的发现具有普遍有效性（general validity）一样 (Gaver 2012)。

对一组人工制品（artifacts）及其注释的描述可以构成一个 *作品集（portfolio）*，将单个人工制品整合为一个系统性的工作体系。通常，一个作品集可以通过多种不同的方式进行注释，以反映不同的目的和兴趣，并面向不同的受众 (Bowers 2012)。例如，Bowers (2012) 将 Interaction Research Studio 作品集中的人工制品分为八个主题进行分析，每个主题涉及由设计所促进的不同类型的交互（interaction）和参与（engagement）。其他注释在 Gaver & Bowers 2012 中有详细阐述。

带注释的作品集（Annotated portfolios）(Gaver & Bowers 2012; Bowers 2012; Löwgren 2013) 是由同一位或相关研究者创作的多个设计的集合...

设计师。他们定义/确立了设计空间（design space）中的一个区域。带有注释的作品集（Annotated portfolios）允许人们比较不同的单个项目、其设计领域（design domain）的相关维度，以及设计师关于在这些维度上应采取的相关位置和配置的观点。图 4.4 被用来举例说明多种设计和注释如何传递关于设计风格（design style）的知识，而这些信息无法仅通过文字或图片有效地传递。

![](https://public-media.interaction-design.org/images/uploads/fcc056d4c60af1c725a8609399b8f99f.png)
***图 4.4**** – 展示 Dieter Rams 风格的带有注释的作品集（摘自 Gaver 2012）*

旨在构建和重构（frame and reframe）可能的设计方案、主题或空间的设计产品收集与基准分析（benchmarking），或者材料探索（material explorations）的收集与构建（Karana et al. 2016, Tsaknaki et al. 2004），都起到了一种类似的中间知识生产（intermediate knowledge production）的作用。

在“传统”的（实证主义的 [positivistic]）科学阐述中，如图 4.4 所示的这种文本与描绘的结合，最多被视为是对理论的阐释。然而，在这里，这些结合被呈现为通过案例讲述来定义一个抽象的理论概念，并主张一个精确的、抽象的概念可能是无法实现的。

### 43.3.6 作为理论阐释或陈述的设计

最后，设计产物（Design artifacts）已被用于——甚至专门为了——阐释理论概念（Theoretical notions）。设计师和艺术家的可视化能力（Visualization skills）在此方面早已获得认可。可视化创作者的贡献范围广泛，从单纯的辅助性阐释到对理论的启发/挑衅（Provocations to theory）不等。艺术家 M. C. Escher 的数学愿景（例如他在 *Klimmen en dalen*, 1960 中的无限上升阶梯；见 SchattSchneider, 2010）以及 Magritte 提出的哲学挑战（*La Trahison des Images*, 1929，更广为人知的名称是 “Ceci n’est pas une pipe”）都是艺术产物引导数学或哲学讨论的典型案例。

在较小规模的层面，在早期的设计研究实践中，特别是在感知研究（Perception research）中，设计专业学生的技能经常被用于创建符合心理学家定义的假设的可视化材料（详见 Stappers et al. 2014）。设计师能够制作更好的刺激物（Stimuli），即在研究中向参与者展示的更高质量的图片。起初，设计专业学生的贡献在于提升表现力（Expressiveness）和可识别性（Recognizability）（心理学实验中的线描图通常图形质量较差）。然而，随着研究问题变得更加聚焦于设计，学生们开始不仅挑战刺激物的图形质量，还挑战研究相关性的局限性。

变量（variables）也是如此。他们反复提出一些刺激设计（stimulus designs）的示例，这些设计仅凭其形式本身就质疑了变量选择的有效性（validity）。设计师在研究团队中的价值在于，他们能够处理物质实体（material things）的复杂性质，并能关注那些恰好处于主导理论（leading theory）视野之外、且在孤立变量（isolated variables）之外的其他视角（lenses）与维度（facets）。

### 43.3.7 知识的“对象”是什么？

由于一个“世界中的物（thing-in-the-world）”具有多个维度，且其中许多维度在设计过程中需要被同时处理，因此设计师很可能会了解到许多方面的事情，例如：

1. 他正在制作的原型（Prototype）（“我们需要它更轻一些，以便于携带。”）
1. 他用来制作原型的技术（“如果通过对齐来增强信号，这些蓝牙发射器就可以使用了。”）
1. 原型与人之间的交互（Interactions）（“他们在尝试三次后就放弃了。”）
1. 与其原型进行交互的人（“他们在与他人交谈时不会使用它。”）
1. 与原型的实现或对研究现象的理解相关的知识/技术领域（“我们可能需要[创造力（creativity）](https://www.interaction-design.org/literature/topics/creativity)理论来开发这种交互。”——例如，图 4.5）
1. 设计师是如何开展设计工作的（“我不得不放弃三条研究路径（lines of inquiry），最后才在采用了不同技术的情况下回到了最初的想法。”）
1. 她对某种解决方案或原则的可行性（Feasibility）的信任（“这种一键式交互不会分散用户的注意力。”）
1. 其可推广性（Generalizability）（“我们可以将该方法再次应用于其他问题。”）
1. 研究是如何开展的，以及如何改进（“在下一次研究中，我们将在开始自行分析之前，先将视频记录进行转录（transcribed）。”）

一些洞察（Insights）对于设计师来说是新的，一些对于该工作所在的领域（Domain）来说可能是新的，而另一些对于与其相关的学科（Disciplines）来说可能是新的。这些知识被复用（Reused，由设计师或与其合作的人员复用）、分享（Shared，可能通过经验或解释教授给他人）甚至被捕捉（Captured，通过文字、图像、视频记录并解释）的程度各不相同。其中大部分知识不会保持在意识层面（Conscious），除非被捕捉和分享，否则将会挥发（Evaporate）（Stappers 2007；参见第 4.2 节、图 4.6 和第 4.4 节）。

![](https://public-media.interaction-design.org/images/uploads/f0e8a2552796f73c3412eabc99572e9a.png)
***图 4.5**** – 关于 Cabinet 开发过程中被认为相关的知识领域（Knowledge Domains）的草图，取自 Keller (2005) 项目的中期。

### 43.3.8 关于人工物的知识与“设计知识”

在某种程度上，可以说设计知识（design knowledge）存在于人工物（artifact）之中 (Cross 1999, Ingold 2013)。但如前所述，这一点被认为是存在问题的，因为人工物“本身”可能无法将这种知识传递给他人。这种局限性可以通过我们实验室中常见的被遗弃的原型（prototypes）来证明：由于这三个关键要素没有被记录和共享，它们的原始目的、功能和价值随着创作者的离开而消失了。Cross 将设计知识视为一种特殊的知识，是艺术和设计学科专业人士所特有的。这表明，将设计知识视为存在于知识创造者之外且首先可以转移的观点，是存在局限性的（见 4.4 节）。

通过参与设计活动而获得的经验性且通常是隐性的知识（tacit knowledge），以及由针对特定情境的主观洞察和理解所构成的知识，对于设计实践至关重要 (Schön 1983)。但在通过设计研究（Research through Design, RtD）中，需要进一步阐明“关于被设计对象、该对象最终将被引入的情境、在两者之间建立适当适配（fit）的过程、设计者的行为与考量，以及所有这些组件之间相互关系的知识” (Höök et al. 2015)。

如果这里的“关于（about）”是指一个已经存在于设计之外的领域，那么

结果可能会契合这些领域，可能处于预先存在的框架（framings）之中，并可能对这些框架提出挑战或对其进行调整。当设计师根据客户心理学家的需求简报（brief）创建刺激物（stimuli），且设计活动和人工制品（artifacts）仅仅是收集信息或测试基于客户理论所构建的假设的手段时，这种情况就会发生。当设计主要被用作一种为现有领域做出贡献的不同方式时，这种情况也会出现——例如，通过在原型（prototype）中实现一个潜在的未来来发现其后果。但如果设计部分仅仅是一项外包的生产活动，而不是研究创造周期（creative cycle）中不可或缺的一部分，那么它将不被视为通过设计进行研究（Research through Design, RtD），而应被视为为研究而设计（Design for Research）。

### 43.3.9 人造物的角色

设计师创造各种事物：草图、模型、计划、视觉呈现、原型和产品。所有相关文献都将这些视为「通过设计进行研究（Research through Design, RtD）」的核心要素。尤其是原型（Prototype）——即体现的、物质化的概念设计（而非早期的草图、图表或贴满便签的墙面）——被认为在 RtD 中发挥着至关重要的作用。尽管物质层面很重要，但人们日益意识到，被原型化的对象不一定被构想为物质对象（尽管它可能由物质对象来辅助或支持），例如对服务、(设计)方法、技术或实践进行原型化。Zimmerman, Forlizzi, and Evenson (2007) 写道：

> “……我们基于 Nigel Cross 的观点，即设计知识存在于产品之中 (Cross, 1999)。人造物（Artifact）反映了对问题的特定界定（Framing），并将其置于其他研究人造物的集合（Constellation）之中，这些人造物可能采用了相似的界定，或者采用了截然不同的界定来解决同一个问题。这些研究人造物为社区的话语（Discourse）提供了催化剂和讨论主题……” (p. 499)

原型在设计实践中扮演着多种重要角色。在 “Prototype: Craft in the Future Tense” 研讨会上，来自不同学科的 11 位研究人员讨论了原型化的各个方面，具体而言，原型是：

> 未完成且可进行实验
> 一种体验未来情境的方式
> 一种将抽象理论与经验（experience）相连接的方式
> (跨学科) 讨论的载体
> 承载活动和讲述故事的道具
> 项目过程中可供参考的里程碑（landmark）（Stappers 2013）

Stappers (2007) 强调了制作原型并使其“运转起来”这一行为的对抗性特征（confrontational character）：它存在于理念世界（world of ideas，如草图、愿景、竞争或冲突的理论、推测）之中，存在于与外部世界（world-out-there，即物理和社会可能性）之间，存在于连接这两个世界（测试与构建）的过程中，以及研究人员之间、研究人员与其他利益相关者（stakeholders）之间的对抗（参见挑衅/provocations）。

单个原型可以作为证明，证明此前被认为不可能的事情实际上*是*可能的，例如 Thor Heyerdahl 乘坐自制的纸莎草船横跨大西洋，证明了利用古埃及技术进行跨大西洋航行是可能的。这与传统设计实践中制作的概念验证（proof-of-concept）原型相似。然而，在学术研究方法论中，它作为一种证明手段往往被忽视。同样地，自 20 世纪 30 年代以来，汽车工业一直致力于创建“概念车（concept cars）”，即通过单件生产来展示使用新技术或为新应用领域进行设计的可能性。这些不仅仅是对新...的审美实验

商业产品。通过制作这些原型（Prototypes），公司能够探索*新*技术、理解*未来*的变化、挖掘市场机会，并提升其创造性问题解决能力（Creative Problem-Solving Capabilities）。这些原型被用于指导公司的设计方向，从而与公众建立更深层次的互动 (Mejia 2016)。

### 43.3.10 产物是“自明”的，还是在“解释某种理论”？

设计师制作的原型（Prototypes）和其他产物（Artifacts）无疑会对人们产生重要影响。它们的有形特质（tangible qualities）能吸引注意力并激发许多人的想象力，正如 David Kelley 的格言所言：“永远要带点东西放在桌上（Always bring something to drop on the table）。”

物理原型在知识方面发挥着多种功能。它可以阐明或实例化（instantiate）抽象的理论概念，并能证明元素新组合的可能性。有人认为原型本身就是知识，或者它承载着知识 (Mäkelä 2007)。对此存在分歧。反对意见认为，原型无法独立讲述其背后的故事：例如 Wensveen 的时钟被误认为是一款消费产品；Keller 的图像输入系统（image-entry system）的设计决策对于访问者来说并不明显。为了从原型中获得洞察，观察者需要具备一种 *框架*（framing），以识别其哪些方面是有意义的，而哪些是偶然的（contingent）（即哪些部分即使改变也无妨）。“实物”的局限性就在于它“仅仅是实物”。在一个紧密的专业社区内，原型的含义可能不需要被明确表达，因为这些人共享隐性价值（implicit values），并且能够识别出原型的显著特征（salient characteristics）。但这将问题转移到了“谁属于这个圈内人（in-crowd）？”这一问题上，而这

这是科学试图避免的事情。这揭示了艺术与工艺的专业实践与科学（及工程学）之间的紧张关系：在前者中，资深匠人（尤其是在行会 Guild 的范围内）对世界拥有一种共同但隐性的框架（Tacit framing）；而后者则希望创建一种显性的、但抽象且普适的框架，以便在更广泛的群体中分享洞见。关于一个制品（Artifact）应当配以多少解释的意见分歧，部分就源于这些不同的价值观和范式（Paradigms）：该制品是否能够“自明”？

此外，一些最深刻的洞见源于我们的失败，源于那些未完成的原型（Prototypes），而它们可能不像成功案例那样能留下痕迹。这些洞见可能没有简单的出版物或展览可供人们回溯查找——它们随其承载的宝贵价值一起，沉入了被遗忘的深渊。

### 43.3.11 “研究原型（Research prototypes）”与“产品概念（concepts for products）”之辨

原型作为由设计师制造的“世界中的实体（thing-in-the-world）”，很容易被误认为是面向消费市场的日常产品。在理论驱动或发现驱动的设计研究（Research through Design, RtD）方法中经常出现这种情况。例如 Wensveen 的时钟，人们一次又一次地问：“对于一个闹钟来说，所有这些交互技术是不是有点太贵了？”以及“什么时候上市？”；同样，对于 Keller 来说，实验室的访客被酷炫的演示所吸引，问道：“我们什么时候能买到它？”Frens (2006, 亦由 Koskinen et al. 2011 讨论) 创作了一系列具有高度美感的相机原型，旨在验证某些[界面设计（interface design）](https://www.interaction-design.org/literature/topics/ui-design)标准的可能性，并在受控条件下对其进行测试，以确保其与理论之间的联系。Wensveen and Matthews (2014) 讨论了原型的两种用途，这两种用途可以毫无困难地融入“传统”的科学方法论中：一是将原型作为测试假设的手段，此时原型被用来实例化（instantiate）选定的变量；二是将原型作为产生分析数据的测量设备（measurement device）。这两者在科学传统中都有着悠久的历史（例如，参见 5.4；Wensveen & Matthews 还讨论了原型的另外两种功能：阐释抽象理论以及为研究提供方向）。

在这些案例中，研究者/设计师投入了巨大的精力去

创建一个具有理想美学效果的原型，使其看起来像是一个真实的产品。他们给出这一理由是因为，这对于确保用户交互的相关性（即具有生态效度 [Ecologically Valid]）至关重要。但随着这种具有说服力的交互而产生的是访问者的预期，即该原型*旨在*成为一款商业产品。在近期一些探究驱动的设计研究（Inquiry-driven Research through Design, RtD）方法中，这些预期被作为一种资源，旨在调查人类与技术在日常生活中私密且具有争议的语境下，随时间演变的复杂关系。在这种情况下，“研究原型（Research Prototype）”的概念可能不足以充分支持这类探究，因此“研究产品（Research Product）”的概念更受青睐 (Odom et al.

2016）。这些是其完工质量（quality of finish）取决于其设计在分辨率（resolution）和清晰度（clarity）方面的表现，以及随后在实际使用中感知质量的人造物（artifacts）。

这些示例均不旨在成为实际的产品。其中所做的设计决策通常是为了研究目的，而非为了最终产品的目的。Wensveen 表示，他从未打算让一个带有 12 个滑块的闹钟成为一个可行（甚至理想）的产品。Keller (2005) 发现，在某些情况下，设计决策是牺牲可用性因素（usability factors）而倾向于研究因素（research factors）的：用户无法通过直接的（以太网）连接将数字图像加载到柜子原型中，而只能通过插入 USB 闪存盘这一明确的操作来完成。前者会让用户更容易上传大量图像，而后者更受青睐，因为它将添加图像变成了一种明确且可观察的社会仪式（social ritual）。同样，Odom et al. 中展示的人造物旨在针对潜在的替代性未来（alternative futures）提出特定的研究问题。它们体现了关于某个设计问题或一组问题的理论立场（theoretical stances）。

莱特兄弟（Wright brothers）似乎并未受到此类困惑的困扰。他们的原型显然是技术试验（technological trials）。并且他们对飞行科学和工程的贡献（至少是现在被人们记住的那些）符合既有的领域：空气动力学（aerodynamics）、控制理论（control theory）和人因工程（human factors）。Wensveen 以及...产生困惑的原因是

Keller 所采用的原型之所以呈现出这种特点，可能是因为其研究课题与交互设计实践（interaction design practice）较为接近，且为了增强研究的说服力，需要采用高保真交互（high-fidelity interactions），这最终导致这些原型看起来更像产品原型（product prototypes），而非研究工具（research instruments）。

### 43.3.12 原型本身为研究提供方向

原型（Prototypes）可以通过嵌入并作为提出特定研究问题的主要手段，从而为研究提供方向。它们可用于研究的展开过程中，旨在证实或挑战研究（Brand et al. 2011, Smith et al. 2016）。从这个意义上说，原型可以具有不同的目的并产生不同的知识。它们有助于开拓一个并非完全不可预见的设计空间（Design space）（Giaccardi et al. 2016, Mazé & Redström 2008）。它们可以作为理论构建（Theory building）的载体（Koskinen et al. 2011, Stappers 2007, Zimmerman, Forlizzi & Evenson 2007, Wensveen & Matthews 2014）。它们有助于确立关键的关注领域和评判标准（Gaver 2012）。原型通常与静态模型（Mock-ups）以及协同设计工具（Co-design tools）——如设计游戏、工作坊和 [情景（Scenarios）](https://www.interaction-design.org/literature/topics/user-scenarios)——相结合，从而产生情境知识（Contextual knowledge），并为围绕生活经验（Lived experiences）而演进的设计机会指明方向（Halse et al. 2010, Sanders & Stappers 2012）。目标驱动设计向前推进，而物理呈现（Physical manifestations）在探究过程中以及塑造研究的方向和轨迹方面发挥着重要作用。

螺旋式设计目标（Spiral design goal，如 Keller 2005 中的“创造一种手动对图像进行排序的方法”）为迭代原型开发工作提供了方向，使其从已知领域出发，向新的未来迈进；在整个过程中，知识...

[知识]从多个维度（技术、人员、商业、方法）进入，并可通过原型（Prototype）体验（第一手）或出版物（第二手）作为中介而输出。第 3.7 节中 Wright brothers 的案例表明，他们学习了围绕“如何制造一个比空气重的飞行器”这一问题的科学与工程领域的现有技术水平（State of the Art），并在其中几个方面（如空气动力学 Aerodynamics、人类控制 Human Control）推动了该技术水平的进步。

### 43.3.13 原型作为过滤器与体现（Prototypes as filters and manifestations）

原型可以帮助设计师反思其设计活动（评估性作用，evaluative role）并探索新的设计空间（生成性作用，generative role）。从这个视角来看，原型既可以充当过滤器（filters），也可以充当体现（manifestations）（Lim et al. 2008, Wensveen & Matthews 2014）。当原型被用作过滤器时，“设计师会筛选掉那些特定原型无需探索的、不必要的设计方面”。这使得设计师能够专注于想象的或可能的设计空间（design space）中的特定区域。“设计师可能会有目的地这样做，以便更精确、更有效地提取关于设计特定方面的知识。关于过滤掉什么的决定，始终基于原型制作的目的。”随后，这些方面在原型中得以体现。例如，一个三维建筑的二维原型可以帮助我们确定房间的空间关系，而无需对墙壁和地板所使用的材料施加任何限制。（将过滤视为一种显式行为的观念，类似于实验室实验中“隔离变量（isolating variables）”的技术：这是一种有意识的努力，旨在集中注意力并限制探究中的变量，从而使某些事物更加突出。）

### 43.3.14 原型作为挑衅（Prototypes as provocations）

人工制品（Artifacts），如草图和视频，也可以被设计成具有刻意的挑衅性。“挑衅原型（Provotypes）”通过揭示并体现围绕某一关注领域的矛盾，从而产生替代方案 (Mogensen 1992)。这可以通过跨利益相关者（Stakeholders）的协作分析和协作设计探索来实现 (Boer & Donovan 2012)。例如，“Indoor Climate and Quality of Life”项目汇集了来自建筑行业五家室内气候相关公司的利益相关者、一支由大学研究人员组成的跨学科团队以及五个参与家庭 (Boer & Donovan 2012)。在该项目的背景下，开发挑衅原型是为了引导参与家庭和工业合作伙伴表达他们对室内气候系统的*重视*之所在。Twist-Vase 和 Render Lamp 被用作技术原型，通过其响应行为（Responsive behavior）促使人们反思与室内气候舒适度相关的主题。

并非所有挑衅原型在实现某种新未来情境的意义上都是原型，但其中许多人工制品是对可能未来情境的充分表达，使得人们可以将它们视为“可能的新未来”来进行反思。与批判性设计方法（Critical design approaches）一致 (Dunne & Raby 2001)，在通过设计进行研究（Research through Design, RtD）的过程中，寻求挑衅也可以是为了打破或逾越社会和文化规范，从而激发讨论和辩论。例如，

Significant Screwdriver (Bardzell et al. 2012) 是一款用于家庭的螺丝刀，它能够记录并可视化关于谁使用了它以及如何使用它的数据。同样，Whispering Wall (Bardzell et al. 2012) 是一种声音显示设备，用于捕捉并播放更衣室中关于异性的内容。同样地，这些推测性人工制品（speculative artifacts）并非旨在量产和销售，而是为了激发人们的反应——正如我们所见，这类设备可以带来一些极具启发性的洞察。

*推测性人工制品（Speculative artifacts）*或*虚构人工制品（fictional artifacts）*可以被用作原型，旨在通过一个以批判为导向的通过设计进行研究（Research through Design, RtD）过程 (Wakkary et al. 2015, Wakkary et al. 2016)，来反思我们的现实世界，并生成替代方案或可能的世界。这类人工制品通常将模糊性（ambiguity）作为一种资源，以支持多种解释和含义 (Gaver et al. 2003)。推测性人工制品的例子包括*反功能设备（counterfunctional devices）* (Pierce and Paulos 2014, 2015)。反功能设备会抑制或移除一项技术中常见或预期的功能。一个例子是 [Inaccessible](https://www.interaction-design.org/literature/topics/accessibility) 数字相机，用户必须通过锯开并拆除椴木外壳才能获取存储图像的 SD 卡。*无意识对象（Unaware objects）* (Wakkary et al. 2015, Odom & Wakkary 2015) 也是推测性原型的一个例子。例如，*The table-non-table*（桌子-非桌子）。

[该作品] 是一个由电动铝制底盘支撑的缓慢移动的纸堆。这一“桌-非桌（table-non-table）”旨在使其在运行过程中完全无感知地忽略所有者的存在或行为，从而在参与者试图理解其目的及其在家庭环境中的定位时，引发一系列思辨（speculations）。尽管从功能角度来看，此类人工制品（artifacts）似乎在自我抵触，但这些作品超越了功能层面，指向了一个更宏大的图景，即这些物品揭示了现实所提供的多样可能性。

### 43.3.15 无形原型：体验、服务与实践（Intangible prototypes: experiences, services, and practices）

物质人工制品（Material artifacts）吸引了大量关注，并作为知识的载体，但它们作为研究工具的意义在于其被*框架化（framed）*的方式。当讨论上升到无形（intangibles）层面，如体验（experiences）、服务（services）和实践（practices）时，这一点尤为明显。当目标是创造或维持一种体验时，例如在体验原型设计（experience prototyping, Buchenau & Fulton Suri 2000）中，许多物质属性仅仅是为了方便而做出的选择，而非原型设计核心的本质。当原型设计的对象是服务或实践时，情况同样如此（Kuijer et al. 2013）。

当设计技术或流程被原型化并测试时，这种情况尤为突出（例如 Mattelmäki (2006) 的探测器（probes）和 Sleeswijk Visser (2009) 的情境映射（contextmapping）技术）。其最终结果包括一种从最终用户和其他利益相关者（stakeholders）中学习的方法，为特定案例而设计的工具包（toolkits）和工作手册（workbooks），以及由丰富的案例描述所支持的[设计指南（design guidelines）](https://www.interaction-design.org/literature/topics/design-guidelines)。详见下文的“设计工具（Design tools）”部分。

### 43.3.16 数据赋能的原型（Data-enabled prototypes）

计算与通信技术的变革开始强调，在人、技术和产品之间交换的数据流同样是一种设计材料（design material）。随着“设计实践（doing design）”向数据技术转移，且工业界开始探索更快速的研究与设计周期，我们预计这将导致数据赋能的原型（data-enabled prototypes）作为研究人工制品（research artifacts）的使用日益增加——例如，能够与云端数据库和服务交换大量传感器数据，甚至能够进行集成 [机器学习（machine learning）](https://www.interaction-design.org/literature/topics/ai) 分析的原型。数据交换将影响此类原型所能促进的流程，以及知识产生、共享并反馈到设计过程中的方式。迭代速度可能会更快，更重要的是，这将打破用户交互（user interaction）、设计参与（design participation）以及产品与服务的创建和分发之间传统的界限 (Giaccardi 2017, Giaccardi et al. 2016)。

### 43.3.17 设计工具、技术和方法作为原型

当设计对象本身就是一个设计方法时，描述研究过程可能会变得非常混乱。但这一点至关重要，因为不出所料，那些开发设计方法的人可能希望以一种「设计的方式（designerly manner）」来完成这项工作。

![](https://public-media.interaction-design.org/images/uploads/2504643199a27a61e27623ef00c48491.png)
***图 4.7**** – 在设计方法的开发过程中，设计活动体现在两个不同的层面。它们既构成了研究对象（右侧），也可以成为开展研究方式的一部分。*

在 Keller (2007) 和 Lucero (2009) 的工作中，项目的目标是开发能够帮助设计师提高创造力的技术、工具和方法。对于 Mattelmäki (2006) 和 Sleeswijk Visser (2009) 而言，其目标则是支持参与「共同设计（Co-design）」的设计研究人员和设计师。在这类研究中，“设计师”扮演着多种角色：既是开发工具、技术和方法的研究人员，又是这些工具的受益者；他们不仅是这些工具的探索者，还在探索如何进行这种探索，学习什么样的证据在什么情况下有效，以及谁需要被说服等。为了阐明这一结论，Stappers and Hoffman (2009) 以及 Stappers and Sleeswijk Visser (2014) 提出了一种「元层级结构（Hierarchy of meta-levels）」，其中各项活动同时发生。

有时涉及相同的参与者（actors）。在每个层级中，都包含一个的人造物/原型/产品（artifact/prototype/product），以及一名设计它的人和一名使用它的人。因此，“设计者（designer）”和“使用者（user）”这两个术语被专门用于表达参与者与该人造物之间的关系，而非用来指示某人的技能集、职业或教育背景。因此，专业设计人员可以是某个设计工具的“使用者”，而设计研究员则是该工具的“设计者”。这种使用与设计之间的关系可以在两个方向上重复：设计研究员可以是研究工具的使用者（以此类推）；而在另一个方向上，最终用户（end-user）则可以将设计出的产品用于创造性目的。

这种分层组织（ordering into layers）有助于澄清一些混淆，尤其是关于人造物与人的角色问题。但它也过度简化了问题，因为它假设存在一种简单的、有界限的“知识（the knowledge）”。如果要包含所有起作用的知识维度（参见 4.1 节“知识关于什么？”），单一的线性排序将不足以涵盖；尽管如此，这种更完整的排序是否真的有帮助仍然令人怀疑。

### 43.3.18 学习：研究的开展方式

在活动、方法和流程方面，设计师开展设计研究（Research through Design, RtD）的方式多种多样。几位作者（Mattelmaki & Matthews 2009, Wensveen & Matthews 2015）指出，目前还没有一种明确定义的单一方法来开展 RtD。通常，这种差异是通过将 RtD 与诸如[可用性测试（usability testing）](https://www.interaction-design.org/literature/topics/usability-testing)等具有标准化协议的研究活动进行对比来解释的。但正如 Feyerabend (1993) 认为的范式转移（paradigm-shifting）研究一样，就方法而言，似乎是“怎么来都可以（anything goes）”。

该领域的大多数作者都认同 Archer (1981, 见于 Cross 1999) 对研究的定义，即研究是“以获取知识为目标的系统性探究（systematic inquiry）”；然而，关于这种“系统性”应达到何种程度，存在相当大的分歧。许多采用 RtD 的研究具有探索性质，希望能够偶然地（serendipitously）发现那些出乎意料但具有价值的东西 (Keller 2005)。有时，RtD 的研究结果源于设计过程中*涌现（emerging）*出的感悟 (Fernaeus et al. 2008)。

在 RtD 中使用设计的另一种方式是将设计作为（用户）研究的基础，其范围涵盖了针对设计的用户研究 (Bourgeois et al. 2014)，以及旨在激发思考和反思的设计 (Bardzell et al. 2012)。

### 43.3.19 活动：我们的实践

通过设计进行研究（Research through Design, RtD）中的活动包括但不限于以下内容：
- 构思并制作原型（prototype），并对所做的设计决策进行反思
- 参与制作原型的人员之间，就原型的各个方面进行决策、反思和讨论
- 与同行在设计评议（design crit）中讨论原型，以探讨该原型如何使研究目标更加清晰
- 在正式和非正式场合（如实验室参观、演示时段和展览）中演示人工制品（artifacts），并与观众的反应进行互动（或选择不互动）
- 将原型部署在实地研究（field study）中，以此作为记录情境/场景数据或获取人员（包括数据技术）输入的一种手段
- 将原型作为一种挑衅/启发（provocation），既针对人工制品本身，也针对其所涉及的人类生活部分
- 将原型作为一种“物理假设（physical hypothesis）”，以证明某个命题的可行性
- 将原型作为一种刺激物，用于测试其作为实例化（instantiation）所代表的整体理论
- 通过利用原型实现某种效果的尝试，为整个研究项目提供方向并界定其范围
- 通过创建一种干预（intervention），使不同的框架/理论（framings/theories）相互碰撞，并与实际情况相对照

这一列表已经很长，我们并不主张它是完整的，甚至不主张它是精确的。它的作用是阐明设计师/研究人员在研究过程中所参与的部分活动（及其目的），而...

产生知识的意图。相关文献往往没有详细阐述具体的操作过程；这种情况通常被如此“括号化（bracketed）”：“方法部分到此为止，让我们进入讨论环节。”

### 43.3.20 目标：我们为何这样做

正如 4.1 节所述，通过实验等活动所追求的知识可能涉及多个方面。具体考虑哪些方面，取决于所选择的框架（Framing）（另见 4.2 节“知识关于什么？”）。

Gaver & Bowers (2012) 提到：
> 设计的功能性（它应该实现什么功能？）
> 审美（人工制品 [Artifact] 应采取什么样的形式和外观？）
> 生产的实际可行性（制作它需要什么样的材料、技能和工具？）
> 制作的动机（我们为什么要这样做？我们试图展示什么？）
> 目标用户的身份和能力（用户将如何看待这个产品？我们如何为他们提供最佳设计？）

Hook et al. (2015) 补充道：
> “涉及审美、设计技能、设计性知识（Designerly knowledge）、政治、价值观以及交互设计（Interaction Design, IxD）实践中其他无形关键要素的知识和洞察”

这两份清单都不完整，但值得注意的是，大多数关于通过设计进行研究（Research through Design, RtD）的文献并未明确描述知识的具体内容、性质及其如何被使用。通常，文中仅泛泛地提到“设计知识（Design knowledge）”，而没有进一步阐明该知识具体是指什么。

如果目标是某个能力领域，例如 Keller 的 Cabinet 研究中提到的“管理用于激发灵感的图像”，那么一系列原型（Prototypes）的目的就是为了支持收集和组织图像的活动，以便于

设计灵感的目的。Keller 所属的研究团队在界面设计方面拥有深厚的历史积淀和一套核心价值观，旨在创造在视觉和交互特性上具有丰富性且兼具草图感（sketchlike）的界面（例如，开创了仅包含视觉元素而无语言元素的界面——双手交互 [two-handed interactions]）。这种功能目标与交互风格价值观，构成了该项目中活动序列的程序性特质（programmatic nature）(Brandt & Binder 2007)。

### 43.3.21 过程：我们如何构建它

一个通过设计研究（Research through Design, RtD）过程可以简单到仅是一组示例的集合，也可以被构建成一个明确的计划（explicit program）。在这两者之间，存在着从单一实例转向更复杂的系列设计探索（design explorations）的工作方式。

### 43.3.22 积累示例集

一种直接的路径是对新领域和新技术进行研究。在这种路径下，研究者会进行一系列大量的短期探索，有时这些探索仅受限于可用时间的限制；其中每一个探索都为可行且有价值的组合之“设计空间（design space）”提供了一个标志点。3.6 节中 Rygh 的 super-maker 示例说明了创建大规模、多样化但未必结构化的样本集之价值，以此激发设计师对新技术可能性的思考。在 Stokes 的研究类型分类（5.3 节）中，这类似于 Linnaeus 和 Leeuwenhoek 在没有明确理论或应用目标的情况下构建集合的活动。

### 43.3.23 在连续原型上进行迭代（Iterating on successive prototypes）

几位作者提到，设计的迭代特性（iterative nature of design）在其中发挥了作用。E. Zimmerman (2003) 警告不要让“设计领先于迭代”，这是一个来自设计实践的警告，旨在防止对单个元素进行过早优化（premature optimization），因为由于设计其他部分的紧迫发现，这些优化在随后可能需要被撤销（这与 Donald Knuth 的观点一致，即“过早优化是万恶之源”）。对这些早期步骤的记录可能会传达许多宝贵的经验，但记录工作并不容易完成。正如 Figure 4.6 所示，许多早期的想法可能最终都被“丢进了垃圾桶”。许多研究人员展示了最终设计的前身（precursors），但往往不会详细阐述这些前身存在的问题或从中吸取的教训，而这些恰恰可能是至关重要的经验。（注：学术出版对将“从失败中学习（learning-from-failure）”作为一种方法并不友好，尽管当它成为论文的*核心*主题时，可能会受到认可。）

### 43.3.24 遵循实验科学方法

第二种方法是将设计行动（design actions）嵌入到已有的相邻学科（例如实验心理学 Experimental Psychology）的研究方法中。在这种方法中，理论主导着整个过程，而实验假设（experimental hypothesis）中的变量驱动着原型的设计。这体现在 Wensveen 的时钟 (3.1) 中，该时钟允许对预期的行为模式（expected patterns of action）进行测量；同时也体现在 Frens 的精细化原型中，他利用这些原型来测试关于其使用的非常具体的假设，并将研究框架设定为自变量（independent variables）和因变量（dependent variables）（见图 4.3）。研究者选择并引入理论概念，生成假设，然后在严格控制的条件下进行测试，并使用统计手段（statistical means）进行评估。在这种方法中，Keyson 和 Bruns-Alonso (2009) 建议将实验测量作为原型研究的必要组成部分，这与 Zimmerman et al. (2010) 所倡导的更具渐进性的理论构建（incremental theory formation）相一致。

![](https://public-media.interaction-design.org/images/uploads/e819ad7ecb5b4cb008eec2d946447fa3.png)
***图 4.9**** – Frens 的研究设计（摘自 Koskinen et al. 2011；请注意其格式与图 7.2 的箭头相似，左上角为理论驱动的输入，右下角为基于实践的反思）。

### 43.3.25 执行一项计划

方法在计划性方法（programmatic approaches）中体现得最为清晰，在这种方法中，为 RtD 项目定义了一个总体目标（Bang & Eriksen 2014, Brandt & Binder 2007）。在这些探究驱动（inquiry-driven）的方法中，原型是实验的一部分，旨在探索并开拓新的设计空间（design spaces）。

在这种方法中（Binder & Redström 2006, Redström 2011），区分了三个结构层级。总体结构即“计划（Program）”，它定义了探索领域（以及活动的总体目标）。在此之下，“实验（Experiments）”是指具体的活动，例如制作原型和进行现场测试。而“问题（Question）”是指引导研究项目的核心研究问题。正是通过计划中各项实验的组合（即[迭代（iteration）](https://www.interaction-design.org/literature/topics/design-iteration)），研究问题才得以解决并获得知识。如图 4.10 所示，可视化图表试图阐明问题、答案和计划这些元素之间的关系。

Redström (2011) 将实验表征为：(a) *探索性（exploratory）*——也就是说，它们在研究计划（或探究）的开始阶段启动、驱动并构建研究框架。(b) 它们可以是 *测试性（testing）* 实验，从而导致研究计划的重新定义（reframing）或巩固（consolidation）。(c) 它们可以是 *闭合性（closing）* 实验——也就是说，有助于对……进行定位和情境化（contextualizing）

...通过论证其主要主张（main claims）来推进研究计划（research program）。在此，所发展的知识与理论贡献将得到整合与传播（consolidated and disseminated）。

### 43.3.26 构建概念框架并填充探索内容

同样地，基于开展具有设计方法目标（Design-methods goal）的设计主导研究项目（Design-led research projects）的经验，Stappers, Sleeswijk Visser, and Keller (2014) 试图总结出一套指南，旨在指导如何利用强调探索与评估（Discovery and evaluation）的设计行为（Designerly actions）来开展一个基于项目的（Program-based，见 4.4 节）博士研究项目。

Stappers, Sleeswijk Visser, and Keller (2014) 对两个主要由设计目标引导的成功博士项目进行了反思。他们的目标是提出指导方案，以确保一系列设计探索（Design explorations）能够产生至少一组连贯的发现，从而有助于理论构建（Theory formation）。在 Keller 的案例中，研究目标是“我们如何利用交互技术解决方案，支持设计师从其收集的图像中获得灵感？”。在 Sleeswijk Visser 的案例中，目标则是“我们如何支持设计研究人员利用其用户研究的发现，来告知并启发设计团队？”。在这两个项目中，研究者开发了一系列原型工具（Prototype tools），并在实践中由设计师进行了试用。与理论方法（Theoretical approach）相反，这些研究并非由理论引导，而是由实现预期效果的机会所引导。通常，这些机会是由所设计的工具和技术原型的可能性所创造的。Keller (2005) 曾明确报道过这种与技术的持续交互……

机会（原型设计 Prototyping）、实地研究（Field Studies，包括民族志研究 Ethnographic 和干预研究 Interventions）以及相关的理论领域（理论和专家咨询）；见图 4.11。此外，在项目进行过程中，研究者选择了不同的文献领域，对其进行了深入探讨，且经常在过程中将其舍弃（图 4.5）。Sleeswijk Visser (2009) 通过一系列八次实地研究，同时开发了工具和理论。在初步探索之后，她构建了一个包含设计目标（顶层）、来自文献的潜在理论概念（中层）以及操作元素（Operational elements，底层）的框架。随后，实地研究的发现被纳入到该框架中（见图 4.12）。该反思提出了两个步骤：第一步是将初始框架构建为一种“支架（Scaffolding）”，第二步则是填充该框架。这两个步骤都包含实证部分（Empirical component，包括设计和实地工作）和理论部分（Theoretical component，包括解读以及对文献的进一步探讨）。

![](https://public-media.interaction-design.org/images/uploads/90b4c5aee08f9a3d35c070ec54fc66e5.png)
***图 4.11**** – Keller 研究过程中理论、技术与实践探索之间的相互作用（摘自 Keller 2005）*

![](https://public-media.interaction-design.org/images/uploads/d01648da6b320ffcc8387bf7b10b6198.jpeg)
***图 4.12**** – Sleeswijk Visser (2009) 概述了她的研究过程：首先建立一个理论概念的初始框架（左），然后通过一系列八次[实地研究]来填充该框架。*

案例研究（中间部分），以便建立联系并细化对最终框架（右侧部分）中术语（Terms）的理解。*

### 43.3.27 显式阶段与循环模型（Explicit phases and cycles models）

研究通过设计（Research through Design, RtD）的过程很少孤立地进行；它们需要积极的利益相关者（stakeholders），且通常需要参与者。在某些情况下，RtD 项目是以大规模协作的方式开展的。在这些情况下，理解过程中展开的不同动态至关重要。根据 Basballe and Halskov (2012) 的观点，RtD 过程沿着三个阶段展开，分别对应过程中利益相关者之间的不同动态：（1）*耦合（coupling）*（研究与设计关注点的耦合），（2）*交织（interweaving）*，以及（3）*解耦（decoupling）*。

*耦合* 是指设计与研究关注点为设计过程的主要部分建立共同出发点的阶段。它为该过程的后续步骤建立了一个框架，并设定了一系列约束。*交织* 发生在某项活动或材料同时为设计和研究关注点提供信息时。例如，工作坊材料被用于探究三维空间和物理表征如何促进未来场景（future scenario）的创建（从研究视角来看），以及在讨论设计想法时支持关于访客移动模式的沟通（从设计视角来看）。*解耦* 发生在研究与设计关注点不再一致时。例如，在由...描述的 “Holger the Dane” 项目中...

Basballe and Halskov (2012) 指出，在制作阶段和最终装置安装过程中进行的设计实验（Design Experiments），要么使设计成为焦点，要么使研究成为焦点，并据此在当时分别启发了设计或研究。研究人员关注的是“参与式体验（Engaging Experiences）”这一概念，而设计师则关注一种新形式的“文化遗产传播（Heritage Communication）”。

![](https://public-media.interaction-design.org/images/uploads/366e488477683b5423c8f49616b043fd.png)
***图 4.13**** – 协作项目中 RtD 动态（RtD Dynamics）的概览 (Basballe & Halskov 2012)*

### 43.3.28 分享：知识传播的方式

尽管关于通过设计的研究（Research through Design, RtD）可能产生的知识类型及其记录方式已有广泛讨论，但 RtD 研究中的许多知识并非通过“期刊和会议论文构建通用理论（Common theory）的常规方式”进行传递。

此外，尽管一些作者对 RtD 结果的可推广性（Generalizability）表示质疑，甚至指出这些洞察主要对直接参与研究的研究人员和设计师有价值，但关于研究结果（即“知识”）如何传递给他人（即“传播”）、这些他人是谁（尤其是当传播是间接的时候），以及这种利用的具体内涵，却鲜有讨论。同样地，关于这些知识如何在其他研究中被（重新）利用，或者如何被应用于产品设计，也缺乏相应的讨论。

### 43.3.29 受众、渠道与形式

虽然大多数关于研究通过设计（Research through Design, RtD）的著作是面向学术受众的，但 RtD 研究者的目标也包括（其他）设计从业者（design practitioners），部分研究甚至将其作为主要目标。学术作者们也揭示了这一目标（例如 Zimmerman et al. 2007）。Cross (1999) 使用了“设计知识（design knowledge）”一词，以表明设计专业人士使用知识的方式和形式可能与其他人不同。

> “[设计知识：] 是一种特有的知识形式，与设计者的意识和能力相关，正如科学和艺术领域中的其他知识文化专注于科学家或艺术家的特有知识形式一样。”
> *—(Cross 1999)*

Koskinen et al. (2011) 提出了实验室（lab）、现场（field）和展厅（showroom）的三分法。他们提出这一分类，不仅是为了区分开展研究的场所和方法，也是为了区分与他人分享结果的不同渠道。实验室研究通常在隔离环境下进行，需要其他传播手段（例如论文），且受众通常为学术群体；现场研究则可以通过参与式研究（participatory research）或行动研究（action research）方法与受益者分享信息。在展厅形式中，原型（prototype）本身及其框架设定（framing）和注释（annotations）构成了传递信息的渠道。

许多研究是在学术机构中开展的，部分结果已被用于培养未来的从业者和研究人员，尤其是在这些机构的设计学院中。

例如，围绕探针（probes）和工具包（toolkits）的技术通过教育渠道传播得相当快。

本章提到的几篇博士论文在 Google Scholar 中具有较高的引用次数。它们被广泛阅读（读者可能包括学生、从业者以及研究人员），因为其详尽的描述满足了期刊论文无法提供的需求。特别是在用户研究方法（user research methods）领域，已发表的博士论文因其对新研究方法和工具的详尽描述而被阅读和引用（例如，Mattelmäki 的论文有 296 次引用，Sleeswijk Visser 的有 101 次，Keller 和 Wensveen 的则有 49 次，数据来自 Google Scholar，检索日期为 2017 年 6 月 10 日）。博士论文也是研究人员描述其所探讨的跨学科议题（interdisciplinary topics）中创造性洞察和推测的场所。尽管这些洞察对于“相邻”学科（adjoining disciplines）具有价值，但要在“它们”的期刊上发表，需要付出巨大努力，将这些洞察转化为该学术共同体当下的专业术语和模型。许多相邻领域可能会将一个设计项目视为“其理论的例证”而予以欢迎，但似乎并不热衷于局外人的框架（framing）。即使在学术发表渠道中，发表文化也存在差异。Gemser et al. (2016) 将设计类期刊分为“与设计相关（design-related）”和“以设计为中心（design-focused）”两类，并指出前者目前的学术影响力大于后者，且与设计相关的期刊文章引用以设计为中心的期刊文章的频率，低于后者引用前者的频率。关于具有设计特性的研究方式（designerly ways of doing research）的出版物通常出现在以设计为中心的期刊以及人机交互（Human-Computer Interaction, HCI）领域中。此外，这两个群体之间还存在认知缺失或价值观方面的障碍。

除了学术期刊和会议，艺术与设计领域还存在通过展览、演示以及评述（critique，如 2014 年 RtD 会议的形式）进行传播的传统。这些方式能以启发且引人入胜的方式触达广泛的受众，但对于未参加活动的人来说，留下的书面记录（paper trail）较少。同样，教育

向下一代设计师传授知识，被认为是设计研究（Design Research）能够影响实践最有效的渠道之一。

另一个要点涉及一项挑战，即如何确保通过“通过设计进行研究”（Research through Design, RtD）过程所产生的知识，对于设计师、设计研究者、其他学科的研究者以及设计与设计研究教育者而言具有相关性——而且更重要的是，确保这些知识对他们（Höök et al. 2015）以及可能的其他受众来说是可理解的。正如 4.1 节中所提到的，从 RtD 中产生的所谓“知识”究竟是什么，并非显而易见。

### 43.3.30 理论的增量构建（Incremental building of theory）

基于实践的研究（practice-based research）中的传统方法通常记录设计过程的中间阶段，旨在支持反思性的“知”与“行”循环（reflective knowing and doing cycle）（Polanyi 1969）。这些方法可能包括书面日记、速写本、设计日志、语音记录和照片。

通过设计进行研究（Research through Design, RtD）的知识通常通过其产出物（what is made）来分享，同时也通过“关于设计与使用的反思性描述，以及将这些元素与其他设计研究联系起来的讨论，从而开发初步理论（nascent theories），例如强概念（strong concepts）、映射（mappings）、框架（frameworks）和注释（annotations）”来分享（Höök et al. 2015）。

在 RtD 中，人们关注如何将设计探索转化为一种足够严谨且记录详尽的研究方法，以便于分享并接受审视（scrutiny）。其核心在于如何让设计研究者能够参与并基于彼此的贡献进行构建（Zimmerman et al. 2010, Höök et al. 2015）。关于严谨性（rigor）和学术参与（scholarly engagement）应处于何种位置，目前尚不明确。这一点在关于 HCI 研究中“设计启示（implications for design）”的意图及其构建基础的讨论中也有所体现（Kostakos 2015 vs. Reeves 2015；见第 6 节，结论）。

根据 Höök et al. (2015) 的观点，该研究领域“仍然缺乏探索、记录和讨论此类知识的手段”。诸如 *pictorials*（图像论文）等新型形式的开发，目前已被 Designing 等活动接受为一种存档格式。

Interactive Systems (DIS) 会议代表了朝着这一方向迈出的重要一步 (Blevis et al. 2015)。图像论文（Pictorials）现在也被 *Design & Emotion* 以及一些 DRS 的专项兴趣会议（例如 EKSIG 2017）所采用。

通过设计研究（Research through Design, RtD）所产生的许多衍生洞察（spinoff insights）可能难以发表。例如，单个项目可能会产生关于制作原型（prototype）所用技术的发现，关于如何衡量人们行为的发现，关于人们如何安排其生活一部分的发现，以及关于如何调整来自另一个领域的极抽象理论以适应所研究情境的发现。但当研究人员试图将这些发现带回各自的领域时，出版渠道会要求其在该领域进行广泛的背景研究，其目的并非为了确保该发现具有新颖性，而是为了确保它符合该学术共同体中被认可的框架（framings）和标准参考文献库，从而使其具有*可信度（credible）*。原型和洞察本身并不能自证其价值 (Stappers 2007)。

同时，人们也尝试开发用于研究目的的通用设计过程记录工具。例如，由 Aarhus University 开发的过程反思工具（Process Reflection Tool, PRT）(Dalsgaard & Halskov 2012) 是一款软件工具，其结构采用类似博客的格式，将内容呈现为事件列表，而这些事件又可以进一步详细描述为子事件。通过使用 PRT，项目参与者可以添加他们的反思

...每个事件（event）和子事件（sub-event）。例如，一个事件可以是计划会议、实地研究（field study）、工作坊（workshop）或原型测试（prototype test）。除了事件之外，该工具还支持“简短注释（brief annotations）”，用于记录电话交谈、简短的电子邮件往来等。视频和静态图像也可以被上传并关联。此外，PRT 支持将对材料的反思（reflection）和分析（analysis）与每个元素相关联，从而能够针对过程中的特定方面，在整个项目范围内进行分析。

## 43.4 结论及更多……

本章讨论了设计性活动（designerly activities）、技能与工具在构建知识过程中的贡献：即“为研究而设计”（design for research）（此处特意将该短语反向表述一次）。在（大约）2007年至2017年期间，涌现出了多样化的案例、方法与路径，同时也开启了关于研究与设计两者的价值、前景及挑战的话语（discourse）讨论。

### 43.4.1 结论

在本章中，我们将通过设计进行研究（Research through Design, RtD）定义为对新知识的设计性贡献（designerly contribution）。但这一概念存在问题。在某种程度上，将知识视为独立实体的观念受到了挑战。在简单的场景中（例如基于既有理论的实验，或学术环境下学生的固定期限作业），知识片段的具体形式是明确的，且有相应的汇报方式。在 RtD 光谱（RtD spectrum）中，这种情况在那些设计行为被嵌入到其他学科（如心理学、工程学或人类学）熟悉的研究结构中的项目（Wensveen, Keller, Wright）中最为明显。在这种情况下，对知识的预期是由外部定义的。但对于更多基于探索（exploration）或思辨（speculation）的项目（Gaver, Mattelmäki, Lundstrom, Rygh）而言则并非如此，这些项目的研究更具开放性。正如 Koskinen et al., 2011 所指出的，Keller 的案例处于两者之间：它具有知识目标，但预期非常开放，其价值主要体现在衍生成果（spinoffs）中。

在目前的论述中，似乎缺失的是 RtD 实践的更宏观背景。一方面，存在着传统的科研项目，它扮演着委托方的角色，具有明确的目标（如回答某个问题或绘制影响图谱）。另一方面，则是一些更像开放式实验和学习的尝试，在这种情况下，不清楚那些未参与其中的人能从中获得多少收益。目前缺乏此类纵向研究（Longitudinal studies），它们不应关注原型（Prototype）在干预（Intervention）（如果存在的话）中的表现，而应关注其如何影响*他人*。这种影响的痕迹并不容易追踪。许多知识的传递（Transfer）在于非正式但同样真实的启发，而非期刊中被引用的参考文献。当今许多学术论文中提供的设计启示（Implications for design）不足以提供可复用的数据（Reusable data）、理论或工具，也无法促进知识在实践性和情境性（Practical and the contextual）之外的积累 (Kostakos 2015)。研究计划（Research programs）、带注释的作品集（Annotated portfolios）以及强概念（Strong concepts）为界定所产生知识的相关性及其传播提供了不同但有效的手段。

Reeves (2015) 针对开放且可复用数据的需求所提出的反驳观点（Counterargument）具有启发性：

> “我认为，关于什么可以被视为一种概括（generalization）、什么是相关的累积过程（accumulation process）（我将其理解为在研究者的论述中建立特定的动力主题 [motor themes]），以及什么能驱动重复实验（replications）的开展，这些标准应当由相关研究者通过达成共识来决定。我不认为这些问题可以通过遵循一套外部且模糊的‘科学标准’来确定，而这些标准通常源自对自然科学方法进行正式描述的教科书。”

但对于设计研究（Research through Design, RtD）而言，其参考群体（reference community）又是谁？

最终，我们应当思考，在 RtD 所处的这种多维度、情境化（situated）且复杂的条件下，我们在多大程度上能将“知识”视为一个有界限的事物。在复杂系统的开发过程中，知识的生命周期较短；它很难与干预措施（intervention）以及“世界中系统”（system-in-the-world）的动态过程相分离。在实用主义者（pragmatist）看来，知识的价值并非一种内在属性，而在于其用途。因此，将目光投向研究工作本身之外，并更加关注研究结果随后在其他地方如何被使用，是有意义的——无论是被设计师/研究者内化的专业知识（internalized expertise）所利用，被参与研究的人员利用，被接收到相关文字或图像的人员利用，还是被其他人利用。同样地，审视启动研究的驱动力也是有意义的。我们的许多示例都来自学术语境（academic context），在这种语境下，一名博士生……

学生或设计实验室通常需要开展一个有固定期限的研究项目，这类项目往往源于某项资助项目征集（funded call），且在申请前需提供学术合理性说明（academic justification）。然而，这并非我们（希望）看到“通过设计进行研究（Research through Design, RtD）”开展的唯一场景。

### 43.4.2 未来方向

RtD 是一个单一的概念吗？关于它应当如何开展以及能带来什么，是否存在共识？不，但尽管这是一个新兴领域，尽管在语言上缺乏统一性，但它确实具有很强的连贯性（coherence）。在方法论、项目组织方式以及哪些问题应被纳入其中等方面，目前仍存在争议。在知识的本质、如何处理中层抽象（mid-level of abstraction），以及构思和制作人造物（artifacts）——尤其是原型（prototypes）——所带来的特定设计性贡献（designerly contribution）方面，也面临着挑战。然而，尽管这些贡献十分明确，且在设计领域之外也能被认可，但似乎仍有某些缺失。

RtD 是否是将设计技能应用于研究的一个有前景的方向？是的。是否应该进一步探索？当然。它是否会扩展我们对知识的理解？毫无疑问！

RtD 的未来必须接纳由不同思想流派和实践所引发的创造性摩擦（creative frictions），并通过一套共同的主题将这些摩擦转化为对日益壮大的 RtD 社区有益的产出；而对于这些主题，目前还没有——或许也不应该有——最终的答案。关键不在于我们是否认同人造物应当是一种具象化（manifestation）还是一个启发（provocation），也不在于我们将其作为批判的媒介（vehicle for critique）还是用于理论开发，更不在于 RtD 的人造物应当是简单的道具（props）还是功能完备且精良的成品。为了从人造物中获得洞察，我们需要

拥有一个*框架（framing）*。正是通过探讨一组连贯且共享的相互关联的主题，才能提供这样一个框架，它将帮助我们提出新问题，设计新实验，并构建一个成熟的 RtD（Research through Design，通过设计进行研究）话语体系。

### 43.4.3 更多学习资源

自 2005 年左右以来，设计（师）在研究中的角色在认可度和内容方面都得到了迅速提升。尽管如此，正如我们在本章中所指出的，该领域仍在探索其话语体系（language）和典型案例，并试图确定是否或如何将多样化的方法（approaches）整合在同一个或多个统一框架（umbrellas）之下。相关文献分布在多种不同的来源中。

### 43.4.3.1 期刊与会议

这里是学术讨论（Academic debate）展开以及主题得以深化之处。本章引用的绝大多数论文均来自关注设计研究方法（Design research methods）的会议和期刊。我们预计相关的讨论也将继续在 ACM 的会议中进行，特别是：
- CHI Conference on Human Factors in Computing Systems (https://chi2017.acm.org)
- DIS Designing Interactive Systems (http://dis2017.org)
- RTD Research Through Design (https://researchthroughdesign.org/)
- DRS Design Research Society (http://www.designresearchsociety.org/cpages/conferences)
- PDC Participatory Design Conference ([http://pdc2016.org)](http://pdc2016.org/%29/)
- Michel, R. (2007) *Design Research Now*. Basel: Birkhäuser 
  包含大量关于设计主导研究（Design-led research）的论文和示例项目；
- Koskinen, I., Zimmerman, J., Binder, T., Redström, J., & Wensveen, S. (2011). *Design research through practice: From the lab, field, and showroom*. Elsevier. 
  是一本面向课堂的设计研究入门书籍，其定位处于通过设计进行研究（Research through Design, RtD）领域的中心。

以及专注于方法的设计会议，例如：

### 43.4.3.2 书籍与章节

通过设计的研究（Research through Design, RtD）在两本书中得到了深入探讨，这些书籍汇集了来自不同视角的贡献，特别是关于原型（prototypes）以及制作（making）作为研究环节一部分的作用。

除此之外，关于通过设计的研究中方法的许多讨论，都是基于社会科学（social sciences）中研究方法的讨论，例如行动研究（action research）。针对这些内容，有一些关于研究方法的指南手册，如下所示：
- Ned Kock. Action Research. Chapter 33. *The Encyclopedia of Human-Computer Interaction*, 2nd Ed. (https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed)
- Bryman, A. (2015). *Social Research Methods*. Oxford University Press.

除上述内容外，[创新](https://www.interaction-design.org/literature/topics/innovation)（innovation）、发明和科学的历史中包含许多“伟大的科学实验”案例，这些案例表明科学发现和验证（validation）可以采取非常多样化的路径（见附录 8.4）。

### 43.4.3.3 已出版的论文

许多记录详尽的通过设计进行研究（Research through Design, RtD）案例均出自博士论文，尤其是来自斯堪的纳维亚和荷兰的论文，这些论文通常以书籍形式出版，并可在互联网上获取。论文不仅包含对研究过程的详细描述，还包含了采用特定方法的论证（通常是通过与传统研究范式（traditional research paradigms）进行对比，或对设计性贡献（designerly contribution）及其动机进行论证）。相比于有严格页数限制的期刊和会议论文，博士论文提供了更丰富的示例和图解。在表 5.1 中，博士论文用星号（*）标出，所有这些论文均可轻松地在网上检索到。

## 43.5 References

**Bang, A. L., & Eriksen, M. A. (2014). **Experiments all the way in programmatic design research. *Artifact*, *3*(2), 4-1.
**Bardzell, S.**, **Bardzell, J.**, **Forlizzi, J.**, **Zimmerman, J.**, **and** **Antanitis, J.** (2012). Critical design and critical theory: The challenge of designing for provocation. In *Proc. of DIS 2012*. ACM: New York.
**Basballe**, **D. A.**, & **Halskov**, **K.** (2012, June). Dynamics of research through design. In *Proceedings of the Designing Interactive Systems Conference* (pp. 58-67). ACM.
**Bernstein**, M. (1996). *Grand eccentrics: turning the century: Dayton and the inventing of America*. Orange Frazer Press.
**Binder, T.** & **Redström**, **J.** (2006) Exemplary Design Research, *Proc. Wonderground 2006*, Redström 2011, Ph.D. theses
**Blevis, E**, **Hauser, S.**, **Odom, W.** (2015) Sharing the hidden treasure of pictorials, *interactions*, *22*(3), 32-43.
**Boer, L**., & **Donovan, J.** (2012, June). Provotypes for participatory innovation. In *Proceedings of the designing interactive systems conference* (pp. 388-397). ACM.
**Boess**, S. (2009). Designing in research: Characteristics and criteria. *Rigor and Relevance in Design*.
**Bowers**,** J.** (2012, June). The logic of annotated portfolios: communicating the value of 'research through design'. In *Proceedings of the Designing Interactive Systems Conference* (pp. 68-77). ACM.

**Brandt**, **E.**, & **Binder**, **T.** (2007). Experimental design research: genealogy, intervention, argument. *International Association of Societies of Design Research, Hong Kong*.
**Brandt**, **E.**, **Redström**, **J.**, **Eriksen**, **M. A.**, & **Binder**, **T.** (2011). *XLAB*. The Danish Design School Press, Denmark.
**Brandt**, **E.** (2016). The Perform 
Codesign Experiment – on what people actually do and the relation 
between program and experiment in research through design. In *Proceedings of IASDR 2015 Interplay *(pp. 234-249).
**Buchenau, M., & Fulton Suri, J.** (2000). Experience prototyping. In *Proceedings of the 3rd conference on Designing interactive systems: processes, practices, methods, and techniques* (pp. 424-433). ACM.
**Cox, D. J.** (2005) “Visualizing the Cosmos,” in INSAP
 Inspiration of Astronomical Phenomena, Fifth International Conference 
Proceedings, June 26 – July 1, 2005, pg. 52; invited speaker, Friday, 
July 1, 2005.
**Crampton-Smith**, **G.** (2006) Design as research that makes a difference. In: van der Lugt, R., and Stappers, P. J., (Eds) *Design and the Growth of Knowledge*. Delft, the Netherlands: ID-StudioLab Press
**CRISP** (2015) Is it a Service? Is it a Course? It’s 
Super-Maker! In van Erp, J., de Lille, C., Vervloed, J., den Hollander, 
M., Aretz, D. *CRISP 5: This is Crisp.* Creative Industry Scientific Programme. Page 5.
**Cross, N.** (1999) DesignResearch: A Disciplined Conversation. *Design Issues 15*, 2, 5-10.

**Dalsgaard**, **P.**, & **Halskov**, **K.** (2012, June). Reflective design documentation. In *Proceedings of the Designing Interactive Systems Conference* (pp. 428-437). ACM.
**Dalsgaard, P., Halskov, K. Basballe, D.A. (2014) **Emergent Boundary Objects and Boundary Zones in Collaborative Design Research Projects, *DIS 2014*
**Dalsgaard, P., Halskov, K., Bardzell, J., Bardzell, S. & Lucero, A.** (2016) Documenting Design Research Processes, *DIS 2016*
**Desmet**,** P.**, **Overbeeke, K.,** & **Tax**,
 S. (2001). Designing products with added emotional value: Development 
and application of an approach for research through design. *The Design Journal*, *4*(1), 32-47.
**Djajadiningrat**,** T.**, **Wensveen**,** S.**, **Frens**,** J.**, & **Overbeeke**,** K.** (2004). Tangible products: redressing the balance between appearance and action. *Personal and Ubiquitous Computing*, *8*(5), 294-309.
**Dunne, A., & Raby, F. **(2001). *Design noir: The secret life of electronic objects*. Springer Science & Business Media.
**Fallman, D.** (2007). Why research-oriented design 
isn’t design-oriented research: On the tensions between design and 
research in an implicit design discipline. *Knowledge, Technology & Policy*, 20(3), 193-200.
**Faste, T.**, & **Faste, H.** (2012). Demystifying “design research”: Design is not research, research is design. In *IDSA Education Symposium*.

**Fernaeus, Y., Tholander, J.**, & **Jonsson, M.** (2008, February). Towards a new set of ideals: consequences of the practice turn in tangible interaction. In *Proceedings of the 2nd international conference on Tangible and embedded interaction* (pp. 223-230). ACM.
**Feyerabend**, P. (1993). *Against method*. Verso.
**Frayling**, C. (1993) Research in Art and Design. *Royal College of Art Research Papers*, 1(1), 1-5
**Frayling, C.** (2015) Closing Provocations of the 2015 Research through Design conference. [http://rtd2015.herokuapp.com/programme/](http://rtd2015.herokuapp.com/programme/) frayling
**Frens, J.** (2006). *Designing for rich interaction. Integrating form, interaction, and function*. Ph.D. Thesis. Eindhoven University of Technology, the Netherlands.
**Friedman, K**. (2008) Research into, by, and for design. Journal of Visual Arts Practice 7(2), 153-160.
**Gaver, W**., **Beaver, J.**, **Benford, S.** (2003). Ambiguity as a Resource for Design. Proc. of CHI ’03, 233-240.
**Gaver**, **W.** (2012, May). What should we expect from research through design?. In *Proceedings of the SIGCHI conference on human factors in computing systems* (pp. 937-946). ACM.
**Gaver, B., & Bowers, J.** (2012). Annotated portfolios. *interactions*, *19*(4), 40-49.
**Giaccardi, E. **(2017). Histories and Futures of Research through Design, *Opening provocation RTD 2017*, Edinburgh, UK: March 21, 2017.

**Giaccardi, E., Speed, C., Cila, N., Caldwell, M.** (2016) Things as Co-Ethnographers: Implications of a Thing Perspective for Design and Anthropology. In R.C. Smith et al. (ed) *Design Anthropological Futures*, Bloomsbury Publishing.
**Hanington**, **B.**, & **Martin**, **B.**
 (2012). Universal methods of design: 100 ways to research complex 
problems, develop innovative ideas, and design effective solutions. 
Rockport Publishers.
**Harré**, **R.** (1981). Great scientific experiments: Twenty experiments that changed our view of the world. Phaidon Press
**Hermans, G. **(2015)** ***Opening Up Design: Engaging the Layperson in the Design of Everyday Products*, Ph.D. dissertation, Umeå Institute of Design, Umeå, Sweden.
**Höök, K., & Löwgren, J.** (2012). Strong concepts: Intermediate-level knowledge in interaction design research. *ACM Transactions on Computer-Human Interaction (TOCHI)*, 19(3), 23.
**Höök, K., Bardzell, J., Bowen, S., Dalsgaard, P., Reeves, S., Waern, A.** (2015) *Framing IxD Knowledge*, XXII.6 November–December 2015, p. 32.
**Horváth**, **I.** (2007) Comparison of three methodological approaches of design research, *International Conference on Engineering Design, ICED’07*, 28-31 August 2007
**Ingold**, **T.** (2013) Making: Anthropology, Archeology, Art, & Architecture. Routledge.
**Jonas, W.** (2007). Research through DESIGN through research: A cybernetic model of designing design foundations. *Kybernetes*, *36*(9/10), 1362-1380.

**Keller**, **A. I.** (2005). *For Inspiration Only; Designer interaction with informal collections of visual material*. Ph.D. dissertation, Delft University of Technology, Delft, Netherlands.
**Keller, A. I., Sleeswijk Visser, F., van der Lugt, R., & Stappers, P. J. **"Collecting with Cabinet: or how designers organise visual material, researched through an experiential prototype." *Design Studies* 30, no. 1 (2009): 69-86.
**Keyson**, **D. V.,** & **Bruns Alonso**, **M.** (2009, October). Empirical research through design. In *Proceedings of the 3rd IASDR Conference on Design Research* (pp. 4548-4557).
**Koskinen, I., Zimmerman, J., Binder, T., Redström, J., & Wensveen, S.** (2011). *Design research through practice: From the lab, field, and showroom*. Elsevier.
**Kostakos, V. **(2015) The Big Hole in HCI Research. *ACM interactions*, 22:2 (March-April 2015), 48-51.
**Kuijer**, **L.**, **de Jong**, **A. M.,** & **van Eijk**, **D**. (2013). Practices as a unit of design. *ACM Transactions on Computer-Human Interaction*, 20(4):21.
**Laurel, B.** (2003). *Design research: Methods and perspectives*. MIT press.
**Lim, Y. K.**, **Stolterman, E.**, & **Tenenberg, J.** (2008). The anatomy of prototypes: Prototypes as filters, prototypes as manifestations of design ideas. *ACM Transactions on Computer-Human Interaction (TOCHI)*, *15*(2), 7.
**Löwgren, J.** (2013). Annotated portfolios and other forms of intermediate-level knowledge. *Interactions*, 20(1), 30-34.

**Löwgren, J.** (2016) On the significance of making in interaction design research. *Interactions*, 23(3), 26-33.
**Lundström, A.** (2016) *Designing Energy-Sensitive Interactions – Conceptualising Energy from the Perspective of Electric Cars*, Ph.D. Dissertation, KTH Royal Institute of Technology, Stockholm, Sweden.
**Lucero Vera, A.** (2009). Co-designing interactive 
spaces for and with designers: supporting mood-board making. Thesis, 
Eindhoven University of Technology.
**Mäkelä**, **M.** (2007) Knowing through making: The role of the artefact in practice-led research. *Knowledge, Technology & Policy* 20(3): 157-163.
**Mattelmäki**, **T.** & **Matthews,** **B.** (2009) Peeling apples: Prototyping Design Experiments as Research, in *Proceedings of Nordes 09*, Oslo.
**Mattelmäki, T.** (2006). *Design probes*. Aalto University.
**Mejia, J.R.**, **Hultink, E. J.,** **Pasman, G**., **Stappers, P.J.** (2016). Concept Cars as a design-led futures technique. *Proceedings of the 23rd Innovation and product development management conference*, Glasgow.
**Miller, G. A.** (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological review*, *63*(2), 81.
**Mintzberg**, **H.**, & **Westley**,** F.** (2001). Decision making: It's not what you think. *MIT Sloan Management Review*, *42*(3), 89.

**Mogensen**,** P.** (1992). Towards a Provotyping Approach in Systems Development. *Scandinavian Journal of Information Systems*, 4, 31-53
**Nimkulrat, **N. (2007) The Role of Documentation in Practice-Led Research, *Journal of Research Practice*, Volume 3, Issue 1, Article M6, 2007
**NWO**-call (2014) [http://www.nwo.nl/en/funding/our-funding-instruments/gw/nwo-creative-industries-research-through-design/nwo-creative-industries-research-through-design.html](http://www.nwo.nl/en/funding/our-funding-instruments/gw/nwo-creative-industries-research-through-design/nwo-creative-industries-research-through-design.html)
**Odom, W.**, & **Wakkary, R.** (2015, June). Intersecting with Unaware Objects. In *Proceedings of the 2015 ACM SIGCHI Conference on Creativity and Cognition* (pp. 33-42). ACM.
**Pierce, J.,** & **Paulos, E.** (2014). Counterfunctional Things: Exploring Possibilities in Designing Digital Limitations. Proc. DIS ’14.
**Pierce, J.**, & **Paulos, E.** (2015,
 April). Making multiple uses of the obscura 1C digital camera: 
reflecting on the design, production, packaging and distribution of a 
counterfunctional device. In *Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems* (pp. 2103-2112). ACM.
**Polanyi, M.** (1969). *Knowing and being*. Chicago: University of Chicago Press.
**Redström, J.** (2011). Some Notes on Program/Experiment Dialectics. In *Nordic Design Research Conference 2011* (pp. 1-8). Helsinki, Finland: Nordes.

**Reeves, S. **(2015) [Locating the 'big hole' in HCI research](http://interactions.acm.org/archive/view/july-august-2015/locating-the-big-hole-in-hci-research).** ***ACM interactions*, 22:4 (July-August 2015), 53-56.
**Rodgers, P**., & **Yee, J**., Eds (2014). *The Routledge Companion to Design Research*. Routledge.
**RTD** conference series (from 2015) [http://researchthroughdesign.org/](http://researchthroughdesign.org/)
**Rygh, K.** (Ed) (2015a) Super-Maker. Eindhoven: The Design Academy. ISBN 978-94-91400-20-9
**Rygh, K. **(2015b) [http://www.super-maker.tumblr.com/](http://www.super-maker.tumblr.com/)
**Sanders, E. B.-N.** (2005). Information, inspiration and co-creation. *The 6th International Conference of the European Academy of Design. *Bremen, Germany.
**Sanders, E. B. N.,** & **Stappers, P. J.** (2012). *Convivial toolbox: Generative research for the front end of design*. BIS.
**Sanders, L.**, & **Stappers, P. J.** (2014). From designing to co-designing to collective dreaming: three slices in time. *ACM Interactions*, *21*(6), 24-33.
**Schattschneider, D.** (2010). The mathematical side of MC Escher. *Notices of the AMS*, *57*(6), 706-718.
**Sleeswijk Visser, F.** (2009). *Bringing the everyday life of people into design. *Ph.D. dissertation, Delft University of Technology, Delft, Netherlands.
**Smith, R. C., Vangkilde, K. T., Kjaersgaard, M. G., Otto, T., Halse, J., Binder, T.** (eds) (2016) *Design Anthropology Futures*. Bloomsbury.

**Stappers, P. J.** (2007). Doing design as a part of doing research. In: Michel, R. (Ed.),* Design research now: essays and selected *projects. Basel: Birkhäuser, 81-91.
**Stappers, P. J.** (2007b) Designing as a Part of Research. In: van der Lugt, R. & Stappers, P. J. (Eds) *Design and the Growth of Knowledge: best practices and ingredients for successful design research*. Delft: StudioLab Press, 12-17.
**Stappers**,** P. J.*** (2013*) Prototypes as central vein for knowledge development. Valentine, L. (Ed).* Prototype: craft in the future tense. 85-97.*
**Stappers, P. J.,** & **Flach, J. M.** (2014). Foreshadowing the Future. *Crisp Magazine*, *3*(2).
**Stappers, P. J., & Hoffman, R. R**. (2009) Once more, into the soup. IEEE Intelligent Systems, 24 (5), 9-13.
**Stappers, P. J., & Sleeswijk Visser**,** F.**
 (2014) Meta-levels in design research: Resolving some confusions. In: 
YK Lim, K Niedderer, J Redstrom, E Stolterman, A Valtonen (eds.), DRS 
2014: Design's big debates, Umea, Sweden, June 16-19, 2014, Printed by: 
Umeå Institute of Design, Umeå, 2014, pp. 847-857.
**Stappers, P. J.,** **Sleeswijk Visser**,** F.**, & **Keller, A. I. **(2014).
 The role of prototypes and frameworks for structuring explorations by 
research through design. In: Rodgers, P. & Yee, J. (2014) *The Routledge Companion to Design Research*.
**Stokes, D. E.** (1994). Completing the Bush model: Pasteur’s quadrant. *Centre for Science, Policy and Outcomes.*

**Stokes, D.** (1997) Pasteur’s quadrant: Basic science and technological innovation. Washington, D.C.: Brookings Institution Press.
**Stolterman, E.** (2008). The nature of design practice and implications for interaction design research. *International Journal of Design*, *2*(1).
**Stolterman, E.,** & **Wiberg, M.** (2010). Concept-driven interaction design research. *Human–Computer Interaction*, *25*(2), 95-118.
**Swann, C.** (2002). Action research and the practice of design. *Design issues*, *18*(1), 49-61.
**Tsaknaki, V., Fernaeus, Y., Schaub, M.** (2014) Leather as a material for crafting interactive and physical artifacts. In *Proceedings of the 2014 ACM Conference on Designing Interactive Systems *(pp. 5-14). New York: ACM Press.
**Van der Lugt, R. & Stappers, P. J. **(2006) *Design and the Growth of Knowledge.* Delft: StudioLab Press
**Wakkary, R., Lin, H.**, **Mortimer, S., Low, L., Desjardins, A. Doyle, K., Robbins, P. **(2016)** **Productive Frictions: Moving from Digital to Material Prototyping and Low-Volume Production for Design Research. In *Proceedings of the 2016 ACM Conference on Designing Interactive Systems *(pp. 1258-1269). New York: ACM Press.
**Wakkary, R.,** **Odom, W.,** **Hauser, S.,** **Hertz, G.,** & **Lin**, **H.** (2015, August). Material speculation: Actual artifacts for critical inquiry. In *Proceedings of The Fifth Decennial Aarhus Conference on Critical Alternatives* (pp. 97-108). Aarhus University Press.

**Wensveen**, **S.** (2005). A Tangibility Approach to Affective Interaction. *Delft University of Technology, Dissertation*.
**Wensveen, S.,** & **Matthews, B**. (2015). Prototypes and prototyping in design research. In: Rodgers, P., & Yee, J. (2014) *The Routledge Companion to Design Research*.
**Wensveen, S., Overbeeke, K., Djajadiningrat, T., & Luxen, R.** (2002). A nod is as good as a wink to a blind horse: How rich behavioural interaction opens up the experiential.
**Wensveen, S., Overbeeke, K., & Djajadiningrat, T.** (2002, June). Push me, shove me and I show you how you feel: recognising mood from emotionally rich interaction. In *Proceedings of the 4th conference on Designing interactive systems: processes, practices, methods, and techniques* (pp. 335-340). ACM.
**Wittgenstein, L.** (1953). *Philosophical Investigations*. Oxford: Blackwell Publishing.
**Zimmerman**, **E.** (2003) Play as Design: the iterative design process. In: Laurel, B. (Ed), Design Research, MIT Press
**Zimmerman**, **J.**, **Forlizzi**, **J.**, & **Evenson, S.** (2007, April). Research through design as a method for interaction design research in HCI. In *Proceedings of the SIGCHI conference on Human factors in computing systems* (pp. 493-502). ACM.

**Zimmerman, J., Stolterman, E., & Forlizzi, J.** (2010, August). An analysis and critique of Research through Design: towards a formalization of a research approach. In *Proceedings of the 8th ACM Conference on Designing Interactive Systems* (pp. 310-319). ACM.

## 43.6 附录：各类研究中的框架设定

通过设计的研究（Research through Design, RtD）通常被呈现为一种*不同*的研究方式——也就是说，它不同于 CHI 领域中常见的实验方法（experimental approach），如可用性测试（usability testing），也不同于“标准科学实验方法（standard scientific experimental approach）”中严格的统计假设检验（statistical hypothesis testing）方法。事实上，大多数作者都认同，设计师在“创造未来”方面的贡献是 RtD 的一个显著特征。

为什么我们需要更广泛地审视？在将 RtD 定位为设计师进行研究的一种方式时，人们进行了一些对比，以便将其与特定形式的“传统”研究区分开来。Zimmerman et al. (2010) 将其与侧重技术的可用性研究进行了对比（即将其与之相对立）；Gaver (2012) 则将其置于与科学哲学家 Popper 和 Kuhn 的观点相对立的位置。但这个光谱要丰富得多，因为设计不仅仅是与实证主义模型（positivistic models）相对立的艺术，而是处于几种传统之间，它可以从中汲取——并为其带来——有价值的视角。

在本节中，我们介绍了四个来自 RtD 核心话语（core discourse）之外的模型，我们认为这些模型能够为前文讨论的主题提供启发。它们可以被视为关于研究方法论的扩展脚注。这也表明，第 4 节中讨论的主题/问题是存在于学术设计社区之外的、更广泛的方法论反思的一部分，设计研究可以与之接轨。并且它表明了...

“设计性的处理方式（designerly ways of going about things）对研究有何贡献？”这一议题，契合于商业与工程领域中一个更为广泛的思考范畴。

### 43.6.1 Horvath 的三种研究类型

Horvath 回顾了德尔夫特理工大学（TU Delft）工业设计工程系数十个博士项目所采用的方法（Horvath 2007），并构建了图 5.1 所示的三类方法。他将这三种研究类型称为“框架方法论（framing methodologies）”，其定义为：

> “框架方法论：(i) 引入一种推理策略（strategy of reasoning），(ii) 指明一种可能的研究设计（research design，即研究行动的结构和设置），以及 (iii) 研究行动的执行方式。”
> —(Horvath 2007, p. 4)

这些博士项目处于两者之间——一方面是成熟学术学科（例如心理学、工程学、[营销学（marketing）](https://www.interaction-design.org/literature/topics/marketing)，通常被称为“基础科学（basic or fundamental science）”）中所开展的研究；另一方面是工业设计实践（有时被称为“应用实践（applied practice）”，但通常不发表）。这三个类别就处于这两个极端之间。这些不同的类别与 Zimmerman, Forlizzi, and Evenson (2007) 所认为的交互设计研究者与人机交互（HCI）研究者之间的区别相似。最接近成熟学科的是“设计语境中的研究（Research In Design Context）”，在这种研究中，使用了成熟学科的方法、理论（以及期刊），但设计被作为研究对象。最接近工业实践一侧的是“基于实践的研究（Practice-Based Research）”，在这种研究中，设计师

对一系列设计项目进行反思，以提取通用见解。这些见解构成了知识，但项目的主要驱动力始终是设计结果，而知识则是其副产品，且通常处于设计方法的元层面（meta-level）。中间类别是设计研究（Research through Design, RtD），Horvath 将其称为 *包含设计的研究（Design Inclusive Research）*。在这一类别中，工作的目标是知识，但设计能力（design competence）提供了至关重要的贡献。

![](https://public-media.interaction-design.org/images/uploads/a0c1f53fb6a7ec404e219b26ec10a608.png)
*表 7.1 – Horvath 2007 年提出的三种研究类型*

在这个核心类别中，设计行为（designerly action）似乎可以扮演两种不同的角色。一种观点认为，研究遵循一条“传统路径”：从理论到假设，再到刺激物（stimulus，即原型），接着是评估，最后是对理论进行调整。在这种方法中，设计者的贡献在于弥合（抽象的）假设与（具体的）刺激物之间的差距。创建原型/刺激物被认为是一项有价值且具有挑战性的任务，如果没有这一环节，研究将无法进行。但它通常也被视为一项 *独立* 的任务——也就是说，推动理论进展的推理被视为一项活动，而为了匹配假设而交付原型的推理则可以是完全独立的。在这种情况下，研究是理论驱动的（theory-driven）。

一个根本不同的观点是发现驱动（discovery-driven）的方法，在这种方法中，创建原型（以及...）的设计反思行为...

（根据时机决定引入或舍弃理论）被视为核心，而理论本身则被视为辅助。在这里，理论洞察（theoretical insights）更多是副产品，而非驱动力。

第 3 节中的示例阐明了这些划分。Wensveen 的“基于设计原型的实验（experiment-with-designed-prototype）”和 Keller 的“产生理论副产品的原型（prototypes-with-theory-spinoffs）”涵盖了核心类别。Gaver 的开放式探索符合基于实践的设计（practice-based design）（尽管该类别中还有许多不那么显著的示例）。我们没有包含来自 RIDC 类别的示例，因为在该类别中，设计特质（design qualities）仅仅是研究对象，而非方法论的组成部分。

![](https://public-media.interaction-design.org/images/uploads/0a17fb77ca37de8c82514e2247ba1ef6.jpeg)
*图 7.2 – Horvath (2007) 识别了学术设计研究中出现的三种方法，并将它们与基础研究（basic research）和设计实践（design practice）区分开来。Stappers et al. (2014) 根据原型的作用以及对“设计行为（act of designing）”的反思，将中心方框内的两种方法进行了区分（摘自 Stappers et al. 2014）。*

### 43.6.2 Mintzberg & Westley 的三种决策方式

Mintzberg and Westley (2001) 批评了管理理论中的决策方法，指出除了理性外推（Rational extrapolation）之外还存在其他替代方案。他们所做的区分不仅适用于决策，同样适用于设计。表 7.3 展示了三种方法、它们在哪些学科中被实践，以及在何种情况下可以使用。

对于设计师而言，这三种方法可能*同样*重要，并在某种程度上构成了日常活动：在理解问题时进行外推（Extrapolate），在需要从不完整且相互矛盾的数据中构建统一视角（Unified view）时进行构想（Envision），而在该领域经验不足时则尝试实践（Trying things out）。设计建立在科学、艺术、工艺和工程的基础之上。- 剩余 6 小时 29 分 46 秒关闭：[ Formal Design Methods: Formalism and Design](https://www.interaction-design.org/courses/formal-design-methods-formalism-and-design)

在第 3 节讨论的示例中，我们发现不仅出现了一种，而是*所有*这些方法。有趣的是，在科学出版物（scientific publications）中，存在一种强烈的偏向，即仅报告第一类（“清晰地阐述操作（manipulations）和结果，以及你是如何论证结论的”），而很少给灵感来源、冲突的解决或大量被放弃的实验方向留出空间（尽管哲学手册告诉我们，我们从错误和证伪（refutation）中学习最多）。

![](https://public-media.interaction-design.org/images/uploads/098e44ff7663656719a102f3274d11ed.png)
*表 7.3 – Mintzberg & Westley (2001) 的三种决策（decision making）方式*

### 43.6.3 Stokes 对「基础研究与应用研究」维度的解构

虽然「基础/根本研究（Basic/Fundamental Research）」和「应用研究（Applied Research）」这两个术语不像世纪之交时那样频繁地被使用，但它们仍然主导着关于研究如何产生价值（以及是否值得资助）的大部分思考。Stokes (1993, 1997) 在分析研究资助政策时，批评这种区分过于简化，且忽略了具有价值的研究类型。他将这种区分追溯到 Vannevar Bush 在第二次世界大战末期提出的政策建议（见图 7.4）。当时的普遍认知是，既然科学研究曾帮助赢得战争，那么它也需要被用于创造经济效益。Bush 的模型将所有研究置于基础研究与应用研究这两个极点之间的单一连续体（Continuum）上，其中源自基础研究的新想法会逐步渗透（Trickle down）到应用研究中，进而转化为工业应用和社会效益，就像量子理论（Quantum Theory）曾助力原子弹（The Bomb）的研制一样。随之而来的观点是，基础研究与应用研究互为对立，向其中一个方向移动就意味着*远离*另一个方向。这种科学观在学术界和大众媒体中仍然被广泛持有。（pj：我记得我的天文学教授在一次讲座中说，他很自豪没有人能应用他的理论，因此他的理论必然更具基础性，从而更有价值）。但 Stokes 认为，这种观点是有缺陷的，且忽略了重要的研究工作。

![](https://public-media.interaction-design.org/images/uploads/dd1338ca14602e12adfc15ec2c414535.png)
*图 7.4 – 在 Vannevar Bush 的模型中，基础研究（Basic Research）和应用研究（Applied Research）是一个维度上的两个对立极点，向其中一方移动即意味着远离另一方；目前尚不清楚 Pasteur 的工作应置于何处，因为他的研究既具有可推广性，又旨在应用于实践（改编自 Stokes 1993）。*

Stokes 提出，基础研究和应用研究并非如图 5.4 所示的两个对立极点，而实际上是两个*独立维度（Independent Dimensions）*。他在图 5.5 的 2x2 表格中填入了截然不同的示例：Niels Bohr（基础研究，无应用意愿）、Thomas Edison（应用研究，无概括意愿），以及 Louis Pasteur——他既是疫苗接种和巴氏杀菌法（pasteurization）的发明者（应用研究），又是微生物学的创始人，推翻了自然发生论（Spontaneous Generation）的理论（基础研究）。Pasteur 成功地将应用研究和基础研究结合在一起。Stokes 的主要论点是，基础研究和应用研究的方面并非互斥（Mutually Exclusive），且像 Pasteur 这样兼具两者的特质应当被珍视（而研究资助计划往往倾向于仅支持 Bohr 和 Edison 所在的领域）。Stokes 同样否定了基础研究和应用研究的互斥性质，通过将两者设定为独立的程度问题来取代并调和它们，他将这些特质分别称为“概括之眼（an eye for generalization）”和“应用之眼（an eye for application）”。

还有一个第四个方格，在 Stokes 的原著中并未讨论

……书中——即那些既不为了普适化（generalization）也不为了应用（application）而开展的研究。属于这一类的是馆藏构建（making of collections），正如在 17 至 19 世纪所见（例如矿物和蝴蝶的收集，Linnaeus 对动物类别的细致组织，以及 Leeuwenhoek 使用显微镜所做的观察）。这一类工作的动力既非普适化也非应用，但它为他人构建理论和应用奠定了基础。

通过设计进行研究（Research through Design, RtD）致力于创造新的解决方案和新的洞察，因此它可以主张占据两个对角线方框：一个是同时产生普适性洞察（general insights）和局部解决方案（local solutions）的方框（无论其驱动力是理论还是应用），另一个是进行纯粹探索（pure exploration）的方框（但其呈现方式允许他人在此基础上继续研究）。

![](https://public-media.interaction-design.org/images/uploads/26cfee8cea738d3b808d4bdd8ccb24c1.png)
*图 7.5 – Stokes 的模型用两个独立的维度取代了两个极点，这两个维度可以同时得到满足，Louis Pasteur 的工作便是一个例证。两张图表均根据 Stokes (1993) 绘制；第 3 节中的七个示例被初步放置在该图谱中。*

那么，这与“通过设计进行研究”有何联系？设计师能否像 Pasteur 那样兼顾两者的优势？他们是否应该为此而努力？

最明显的联系可能在于每种方法如何看待原型（Prototypes）的角色，如表 5.6 所示。

*表 7.6 – Stokes 模型与研究通过设计（Research through Design, RtD）的关系。* 在 Leeuwenhoek 象限中，我们使用“人工制品（Artifacts）”而非“原型（Prototypes）”（因为这些人工制品本身即是目的，而非被定位为其他事物的原型）。

以上讨论揭示了研究与设计的结合所能带来的成果是多么多样。它涵盖了发现（Discovery）与发明（Invention）的维度、为抽象理论寻找实例化（Instantiations）以及从具体经验中进行概括，还包括验证（Validation）与挑衅（Provocation）的元素、灵感以及可行性证明。不同的利益相关者（Stakeholders）侧重于不同的方面。

### Harré 的实验多样性

为了弄清楚 RtD 的特殊之处，几位作者将其与某些既有的、历史性的方法进行了比较。Zimmerman et al. (2010) 将其与可用性研究（Usability Research）中由测量驱动的方法进行了对比；Gaver (2012) 将 RtD 与 Popper 的严格实验方法以及 Kuhn 的范式（Paradigm）概念进行了比较；Koskinen et al. (2011) 则提到了 Lakatos 的科学研究计划（Scientific Programs）概念。这些例子表明，不存在一种单一的方法是成功产生知识的必要且充分条件（Feyerabend, 1993 认为这是不可能的）。

科学哲学家 Harré (1992) 描述了历史性科学突破背后的各种方法，旨在...

阐述了不同的研究者是如何发现、确立、衡量并证明那些我们如今认为正确的科学事实的。在他的书中，他以科普的方式描述了 20 个科学“实验”，并讨论了其背后的逻辑。

四个著名的例子（Harré 提供了 20 个）表明了研究者的方法是多么多样化：

- Aristotle 是第一个通过在鸡蛋产后 1、2、3……天将其打开，来描述雏鸡在蛋内发育情况的人。
- Beaumont 通过将食物系统地放入活人的胃中并在一定时间后将其取出，确立了消化的化学性质；他利用了一名士兵身上方便的战争伤口，该伤口使该士兵的胃拥有一个“侧入口”。
- Theodoric of Freiburg 通过研究光线如何被玻璃瓶反射，并推论玻璃瓶是天空中水滴的模型，从而找到了对彩虹形状和位置的解释。
- Michelson 和 Morley 旨在测量以太（æther）的运动，在 25 年间设计、制造并测量了一台光干涉仪（light interferometer），每次的结果均为零结果（null result），在假设检验（hypothesis-testing）的方法中，这证明了“无”。然而，正是这次失败被认为是拒绝以太理论的基础，并为相对论（theory of relativity）奠定了基础。
- Gibson 的饼干模具实验（cookie-cutter experiment）证明了……的危险

在研究人类感知（human perception）时，隔离易于测量的变量（isolating simple-to-measure variables）：当一个饼干模具形状被压在或转在某人的手掌上时，他很难识别其形状；然而，如果能让他用手指去探索，他就能毫无问题地识别出该形状。

方法的多样性以及研究结果的影响力，使得任何单一的知识获取模型都难以涵盖。有些方法涉及测量，有些涉及构建复杂的测量材料，而有些则涉及敏锐的隐喻性思维（metaphorical thinking）。在某些方法中，演示（demonstration）和框架构建（framing）是其核心，无需重复测量或统计分析。有些贡献则基于尝试不同的变体，或者仅仅是对描述保持系统性。所有这些方法都是设计师在项目中寻找解决方案时所需技能中不可或缺的一部分。

---
[1] （注：“设计研究（design research）”这一组合在文献中具有三种不同的含义：一是“关于设计的研究（research into design）”，如 *Journal of Design Research*；二是“为了设计的研究（research for design）”，尤其是当代 UX 职位空缺中所指的“用户研究（user research）”；三是指“通过设计的研究（RtD, Research through Design）”。）
