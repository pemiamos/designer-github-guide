# 13. 需求工程（Requirements Engineering）

**来源**：The Encyclopedia of Human-Computer Interaction, 2nd Ed.
**Notion 原页面**：https://www.notion.so/97d4de22f8a84c349b3d6c1c04ff9613

---

[Alistair G. Sutcliffe](https://www.interaction-design.org/literature/author/alistair-g-sutcliffe)
需求工程（Requirements Engineering）顾名思义，是一门建立用户需求（user requirements）并定义软件系统（software systems）的工程学科。关于需求工程有许多定义 (Zave, 1995)；然而，它们都认同一个观点，即“需求”涉及探索人们希望从计算机系统中获得什么，并理解这些需求在设计层面意味着什么。需求工程与软件工程（software engineering）密切相关，而后者更侧重于设计用户所需系统的过程。最简洁的总结或许来自 Barry Boehm：需求是“设计正确的事物（designing the right thing）”，而软件工程则是“正确地设计事物（designing the thing right）” (Boehm, 1981)。Nuseibeh and Easterbrook (2000) 给出了一个更全面的定义：“软件系统需求工程（software systems requirements engineering, RE）是通过识别利益相关者（stakeholders）及其需求，并将这些需求以一种便于分析、沟通和后续实现（implementation）的形式记录下来，从而发现系统目的的过程”。

需求工程（Requirements Engineering）与[人机交互](https://www.interaction-design.org/literature/topics/human-computer-interaction)（Human Computer Interaction, HCI）在许多概念、技术和关注点上具有共同之处，特别是以用户为中心的设计（user-centred design）、参与式设计（participatory design）和[交互设计](https://www.interaction-design.org/literature/topics/interaction-design)（interaction design）。

然而，它在设计范围的视角上与 HCI 不同；例如，社会技术设计（socio-technical design）在需求工程中很少被提及（尽管 Sutcliffe et al.(2005) 是一个例外），而在社会技术设计中，系统的组织和人员部分是需求和设计的明确目标。另一个区别在于 HCI 关注设计本身（design *per se*）和交互设计，在这种视角下，用户需求被视为设计探索、[原型制作](https://www.interaction-design.org/literature/topics/prototyping)（prototyping）以及与用户进行评估对话过程的一部分，而非需求工程社区所青睐的更为线性的“规格说明-设计-实现”（specify-design-implement）过程。不过，需求工程确实支持迭代设计（iterative design）、原型制作和评估（在需求术语中通常称为验证（validation））。此外，人们日益意识到，如果不进行一定的设计，就无法定义需求，这导致了“架构需求”（architecture requirements）的出现。在本章中，我将探讨其共同点以及

[探讨] 人机交互（Human-Computer Interaction, HCI）与需求工程（Requirements Engineering, RE）之间的差异，以反思这两个社区是如何处理本质上相同的问题的：即构建一个基于软件且能满足人们需求的系统。

本章分为接下来的六个部分。在接下来的第 1 节中，将描述需求工程的流程。随后，第 2 节将回顾基于场景的方法（scenario-based approaches），这些方法阐明了需求工程与 HCI 之间的融合（convergence）。第 3 节探讨这两个学科中的模型与表示（models and representations），随后第 4 节将回到流程主题，以评估 HCI 与需求工程在开发方法上的差异。第 5 节回顾知识在需求与设计流程中是如何被复用的，并由此简要讨论 HCI 与需求工程之间融合的前景。

## 13.1 需求工程（Requirements Engineering）活动与流程

### 13.1.1 范围界定（Scoping）

需求通常始于一个模糊的意向陈述。首要问题是确定调研边界（boundary of investigation），以及（*inter alia*）预期系统的范围（scope）。不幸的是，这个过程很少简单，因为客户通常不清楚自己具体想要什么，且关于预期系统的认知较为模糊。范围界定（Scoping）往往是一项迭代活动，因为随着所有利益相关者（stakeholders）对该领域（domain）的共同理解不断深入，边界会变得更加清晰。然而，人们对这一过程的理解不足，且很少有研究直接探讨这一难题。

以一个旨在帮助流行病学家（epidemiologists）开展研究的系统为例，这就是 ADVISES 项目的任务书（Thew et al., 2009; Sutcliffe et al., 2011）。利益相关者可能包括对流行病学感兴趣的公共卫生分析师以及医学研究人员。可能的决策支持工具（decision-support tools）范围可能涵盖数据收集、数据准备、统计分析、可视化、图表、地图，以及用于协作讨论结果的协作工作支持（groupworking support）。由于该项目是作为英国政府支持的电子科学研究计划（e-science research programme）的一部分启动的，且用户既包括流行病学领域的学术研究人员，也包括在当地医院工作的公共卫生分析师，因此系统的所有者（systems owner）和范围并不明确。

对于一般的范围界定，企业建模（enterprise modelling）（Kirikova & Bubenko,

1994) 提供了一种描述业务上下文（business context）的方法，用以挖掘宏观需求（requirements in the large）（即目标、宗旨、政策），但提供的过程指导（process guidance）较少。以其发明者 Jiro Kawakita 命名的 KJ [头脑风暴（brainstorming）](https://www.interaction-design.org/literature/topics/brainstorming) 法研讨会，以及快速应用程序开发（Rapid Applications Development, DSDM Consortium, 1995）是目前的主流方法（state of the art）；它们主张使用列表和问题空间（problem space）的非正式映射图，尽管这些方法同样缺乏系统性的指导。Jackson and Zave (1993) 对更详细的范围界定（scoping）进行了研究，他们提出了通过检查目标系统在响应现实世界事件时的义务（obligations）来建立系统边界（system boundary）的技术，尽管这对于从用户意图的通用陈述开始的调查界定没有太大帮助。

范围界定最好通过与所有利益相关者（stakeholders）讨论，并将高层系统目标记录为职权范围（terms of reference）来实现。将范围写下来往往能让用户将注意力集中在系统调查的边界应在何处，并有助于确定系统至少初步的范围。

### 13.1.2 事实收集（Fact gathering）

在很大程度上，这项活动的技巧借鉴自系统分析（Systems Analysis），例如访谈（Interviews）、观察（Observation）、问卷（Questionnaires）以及文本和文档分析（Text and Document Analysis）(Gause & Weinberg, 1989)。知识获取（Knowledge Acquisition）中的技术，如概貌网格（Repertory Grids）和协议分析（Protocol Analysis），也被应用于此。但除了 Maiden and Rugg (1994) 的一项初步研究外，目前还没有针对不同事实捕获技术（Fact-capture techniques）优劣的系统性研究。一个有趣的新兴领域是民族志（Ethnographic）及相关的观察方法（Observational methods）的应用 (Goguen & Linde, 1993; Luff et al., 1993)；然而，到目前为止，这些方法未能为事实捕获或分析提供明确的指导，导致软件工程师们提出了自己的“快速且粗糙”（Quick and dirty）的方法 (Hughes et al., 1995)。

### 13.1.3 分析（Analysis）

分析和建模通常采用自顶向下方法（Top-down approaches），重点关注目标分解（Goal decomposition）。分析通常由 5 个“W”问题驱动：
- 系统的目的是什么（目标）？
- 涉及哪些对象？
- 系统位于何处？
- 事情应该在何时发生？
- 为什么需要该系统（它旨在解决的目标或问题）？

在一个常用方法的示例中，Potts et al. (1994, 1995) 提供了一种与目标相关的分析手段，该方法利用 [场景（Scenarios）](https://www.interaction-design.org/literature/topics/user-scenarios) 来发现障碍（Obstacles），即系统必须处理的由外部代理（External agents）引起的潜在问题。基于这些障碍，可以进一步详细阐述关于维持、避免和修复特定情境的目标。其他的目标分解方法则采用分类法（Taxonomic approach），并尝试在领域模型（Domain models）的语境下分析目标 (Sutcliffe & Maiden, 1993)。

对于问题分析，软系统方法论（Soft systems methodology, Checkland, 1981）提供了一种非正式建模（Informal modelling）的手段，以及一种发现面向问题需求（Problem-oriented requirements）的分析方法。非正式的图表和草图（可被称为领域模型或丰富图景 Rich pictures, Checkland 1981）被用于记录分析的进展过程。图 1 展示了 ADVISES 项目的一个领域模型。

![](https://public-media.interaction-design.org/images/encyclopedia/requirements_engineering/fig01_domain_model.gif)

作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 13.1**：ADVISES 项目的领域模型（Domain model），该非正式图表展示了涉及的利益相关者（Stakeholders）和组织。

相关组织以矩形表示，作为次要利益相关者（Secondary stakeholders），即对系统输出感兴趣但并非直接操作系统的主要用户（Primary users）；后者在图中以圆形表示。主要利益相关者包括 Primary Care Trusts（英国国家医疗服务体系 NHS 的地方组织单位）的公共卫生分析师，以及共同组成 NIHBI 部门（North West Institute of Bio-Health Informatics）的学术健康信息学（Health informatics）研究人员。

基于理由（Rationale-based）的技术同样适用于分析和建模。这些技术将分析结构化为层级图，将目标与潜在解决方案及支持性论据联系起来；参见 gIBIS (Conklin & Begeman, 1988) 和 QOC (MacLean et al., 1991)。

### 13.1.4 建模（Modelling）

这一活动利用分析阶段的输出，对事实进行结构化处理，并使用某种表示法（notation）将其呈现。需求工程（Requirements Engineering）为此活动从结构化系统开发方法（structured system development methods）和概念建模（conceptual modelling）中借鉴了相关技术。非正式建模表示法（Informal modelling notations），如数据流图（data flow diagrams）和实体关系图（entity relationship diagrams），已被广泛使用。许多建模的正式方法（formal approaches）被引入自软件工程（software engineering）(Goguen & Linde, 1993; Van Lamsweerde, 2009; Van Lamsweerde et al., 1995)，尽管这些技术的有效性在工业实践中尚未得到证明。分析与建模通常交替进行，以细化需求，因为随着表示行为的开展，对问题域（problem domain）的理解也会随之增加。

图 2-4 展示了一些建模表示法的示例。图 2 中的实体关系图展示了实体及其功能关系（如“拥有”、“定价”等），这些关系支持数据建模（data modelling），并最终服务于数据库设计（database design）。

![](https://public-media.interaction-design.org/images/encyclopedia/requirements_engineering/fig02_entity_relationship_diagram.gif)

作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”章节。

**图 13.2**：实体关系图（Entity Relationship Diagram）；其中实体以矩形表示，关系以连接线表示。
![](https://public-media.interaction-design.org/images/encyclopedia/requirements_engineering/fig03_data_flow_diagram.gif)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 13.3**：数据流图（Data Flow Diagram）：在此表示法中，矩形代表过程（Processes），椭圆代表外部代理（External Agents），箭头则显示过程之间信息流的方向。

数据流图对系统的处理方面进行建模，并对实体关系图的“数据视图（Data View）”模型起到了补充作用。

![](https://public-media.interaction-design.org/images/encyclopedia/requirements_engineering/fig04_grn_goal_requirements_notation.gif)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 13.4**：$i^*$ 图（$i^*$ diagram），也称为目标需求表示法（Goal Requirements Notation, GRN）。

圆形代表代理（Agents），椭圆代表目标（Goals），云形代表“软目标（Soft Goals）”或质量准则（Quality Criteria），矩形代表资源（Resources），带有 D 标注的关系则代表依赖关系（Dependencies）。为了简化图表，实现目标的任务（Tasks）已被省略。

图 4 中的 *i* 图展示了 ADVISES 应用程序中利益相关者（stakeholders）、主要目标（major goals）和非功能性需求（non-functional requirements，在 *i* 术语中称为软目标 soft goals）之间的关系。代理（agents）与目标之间的依赖关系（dependencies）由弧线上的 D 符号（Dsymbols）标出。

### 13.1.5 验证（Validation）

需求工程（Requirements Engineering）中的这一关键活动，尽管得到了广泛的研究，但仍然存在问题。验证意味着让用户理解需求规格说明（Requirements Specification）的影响，然后同意（即验证）该说明准确地反映了他们的意愿。目前最先进的方法是走查技术（Walkthrough Techniques），在这种技术中，设计师和用户在研讨会中对数据流图（Data Flow Diagrams）等半形式化规格说明（Semi-formal Specifications）进行评议。走查的优点是对规格说明进行早期验证，而原型（Prototypes）可能更为强大，因为用户对实际运行的系统的反应更为强烈。不幸的是，原型仍然会产生构建成本，而且组织不当的原型使用可能会产生负面影响 (Attwood et al., 1995)。然而，将原型与收集和评估用户反馈的技术相结合可以非常有效 (Gould, 1987)。总体而言，人们对验证过程的理解不足，而解释（Explanation）是一个重要但经常被忽视的组成部分。一些关于解释复杂需求的研究表明，可视化（Visualisation）、示例和模拟（Simulation）的结合是必要的 (Carroll et al., 1994; Maiden & Sutcliffe, 1994)。基于场景的表示（Scenario-based Representations）和动画模拟有助于用户了解系统行为的影响，从而改善验证 (Johnson et al., 1992)；此外，带有场景的早期原型是诱导（eliciting）...的强大手段

验证反馈（validation feedback）(Sutcliffe, 1995)。Potts et al. (1994) 提出的询问周期技术（inquiry cycle technique）通过将想象中的真实世界行为脚本（scripts of imagined real-world behaviour）与规范（specification）中要求的行为进行对比来实现验证。目前人们对验证的理解仍然不足，需要进一步研究以探索解释、表示以及用户对系统规范的理解是如何相互作用的。

在 ADVISES 项目中，需求验证（requirements validation）是一个迭代过程（iterative process），最初向用户展示的分镜脚本（storyboards），随后则是静态模型（mock-ups）和原型（prototypes）。这促进了与用户关于其具体需求的讨论，同时也帮助需求工程（Requirements Engineering）团队更深入地了解用户的工作。向用户展示设计方案几乎总能激发有用的反馈，而这种方法是以用户为中心的设计（user-centred design）的核心。

![](https://public-media.interaction-design.org/images/encyclopedia/requirements_engineering/fig05a_storyboards_used_in_validation_sessions.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

![](https://public-media.interaction-design.org/images/encyclopedia/requirements_engineering/fig05b_storyboards_used_in_validation_sessions.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅部分

下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外情况（Exceptions）”。

**图 13.5 A-B**：在用户验证环节（Validation sessions）中使用的 ADVISES 分镜脚本（Storyboards）示意图。

ADVISES 原型（Prototype）的演示视频可见于补充材料或访问：[http://www.youtube.com/watch?v=8EfSM9KG3Dg](http://www.youtube.com/watch?v=8EfSM9KG3Dg)

图 5 展示了 ADVISES 纸质原型（Paper prototype）的两种配置，旨在支持对流行病学数据（Epidemiological data）的探索。(A) 展示了一座虚拟城市的地图，该地图根据初级保健信托（Primary Care Trust）的边界进行了划分，其中一个区域通过阴影显示出明显的“热点（Hotspot）”，以表明该区域的平均值处于分布（Distribution）的极端位置。(B) 展示了同一张地图，但此时被划分为更小的子区域，并配有这些区域的类直方图图表（Histogram-like plot）。醋酸纤维透明胶片（Acetate transparencies）被用作覆盖层（Overlays），以便以交互序列的形式呈现不同的选项；而贴纸便签（Post-it notes）则用于记录验证环节中的想法和反馈建议。鼓励用户在纸质原型上绘图，以阐述他们自己的设计想法。图 6 展示了一个交互式需求验证环节（Interactive requirements validation session），其中贴纸便签成为了所有参与者之间分享想法的一种手段。

![](https://public-media.interaction-design.org/images/encyclopedia/requirements_engineering/fig06_interactive_requirements_validation_session.jpg)

作者/版权持有者：未知（待调查）。版权条款与许可（Licence）：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”章节。

**图 13.6**：用户在需求验证（Requirements Validation）环节中使用便签纸讨论想法

### 13.1.6 权衡分析（Trade-off Analysis）

需求往往无法通过单一的规范（Specification）完全满足。非功能性需求（Non-functional requirements）就属于这一类；尽管设计可以在一定程度上兼顾这些需求，但一个完美的解决方案通常是不可行的。需求通常由不同的利益相关者（Stakeholders）持有，而他们之间可能存在冲突的观点，因此，权衡分析（Trade-off analysis）是对比、排列优先级以及在不同需求或设计方案之间做出决策的一项关键活动。使用决策表（Decision tables）的排序列表或基于矩阵的技术对该分析很有帮助。

Chung (1993) 和 Yu (1993) 提出的用于映射目标（Goals）、任务（Tasks）、参与者（Actors）和软目标（Soft goals，即非功能性需求的别称）之间关系与依赖性的建模技术，为权衡分析提供了一些指导。他们的方法和支持工具有助于追踪目标与非功能性需求（NFRs）之间的影响，并能针对不同类型 NFR 之间潜在的冲突提供积极的指导（例如，安全性可能会损害[易用性（ease of use）](https://www.interaction-design.org/literature/topics/ease-of-use)）。

这项工作在处理权衡问题方面取得了显著进展。尽管如此，能帮助需求工程师（Requirements engineer）的工具或方法仍然很少，虽然质量屋（House of Quality, Hauser and Clausing, 1988）技术已被引入到需求工程（RE）中，并且已有部分工具支持（Jacobs and Kethers, 1994）。更复杂的方法，如多准则决策（Multi-criteria decision）...

(Fenton, 1995) 似乎尚未在需求工程（Requirements Engineering, RE）中被考虑。

表 1 展示了 ADVISES 中权衡分析（Trade-off Analysis）的一个示例。研究收集了两组需求，一组来自学术研究人员，另一组来自公共卫生分析师。表中展示了需求与不同质量标准（Quality Criteria）或非功能性需求（Non-functional requirements, NFRs）（如准确性、隐私性等）之间的关系。

| 目标 | 医学研究人员 | 卫生分析师 | 非功能性需求 |
|---|---|---|---|
| 准确性 | 安全性 | [可用性 (Usability)](https://www.interaction-design.org/literature/topics/usability) |  |
| 在地图上绘制数据 | ✓ | ✓✓ |  |
| 在地图上显示热点 | - | ✓✓✓ |  |
| 提供简单统计 | ✓ | ✓✓ |  |
| 标注地图 | - | ✓✓✓ |  |
| 检查数据错误 | ✓✓ | ✓ | ++ |
| 提供高级统计 | ✓✓✓ | - | ++ |
| 防止分析错误 | ✓✓✓ | **--** | ++ |
| 加密数据 | ✓✓ | - |  |
| 集成地图与图表 | ✓✓ | - | + |

**表 13.1**：ADVISES 中两种利益相关者视角（Stakeholder views）下需求目标与质量标准之间的依赖关系。对勾（✓）表示各组利益相关者对目标的优先级排序（Prioritisation），- 表示中立，-- 表示反对或目标冲突，而 + 则表示目标与 NFRs 之间的关联。

决策表（Decision tables）、决策树（Decision trees）和流程图（Flowcharts）是其他可以促进协商（Negotiation）和权衡分析的表示方法，它们能够使选项空间清晰化，并帮助利益相关者从他人的角度审视自己的优先级。

### 13.1.7 协商（Negotiation）

需求工程（Requirements Engineering）的社会维度尚未被充分理解。这一活动涵盖了许多其他活动，例如分析（analysis）、权衡（trade-off）和建模（modelling），但其核心在于对冲突需求的讨论、解释和协商（negotiation）。表 1 展示了 ADVISES 中的协商问题。显然，两组利益相关者（stakeholders）具有不同的优先级，仅在少数目标（如数据错误、地图和简单统计）上达成共识。如果利益相关者的目标不冲突，那么所有目标都可以纳入设计中，尽管这可能会增加复杂性。然而，当目标发生冲突时（例如“防止分析错误”这一目标），则必须通过协商来调和冲突的观点。健康分析师认为这一目标是对其专业诚信的轻视；然而，当该功能在提高结果准确性方面的积极作用得到解释后，他们接受了这一需求。

Chung (1993) 的建模工作通过创建一种共享制品（shared artefact）来助力协商，从而可以通过该制品讨论影响因素和设计替代方案（design alternatives）。这一过程是通过创建战略依赖模型（strategic dependency model）来描绘目标、任务、参与者（actors）等之间的关系，随后通过战略理由模型（strategic rationale model）来阐明需求的潜在系统解决方案及其支持或反对的论据来实现的。遗憾的是，这些模型并未为达成需求一致提供积极的指导，尽管 Boehm et al. (1994)

建议一些用于构建成功需求协商（Negotiation of Requirements）的[启发式方法（Heuristics）](https://www.interaction-design.org/literature/topics/heuristics)。协作式需求获取（Co-operative Requirements Capture）中的利益相关者分析方法（Stakeholder Analysis Methods）（Macaulay, 1993）有助于构建包含不同利益相关者的研讨会组成，并为从不同视角考虑需求提供了一个框架。然而，关于管理需求工程（Requirements Engineering）会议以及处理协商与冲突解决（Conflict Resolution）的指导方案较为匮乏。关于会议的社会科学研究描述了角色、领导力的理想条件（Desiderata）以及群体共识（Consensus）的管理（Viller et al., 1994）；但这些研究尚未被应用于需求工程中。

![](https://public-media.interaction-design.org/images/encyclopedia/requirements_engineering/fig07_requirements_negotiation_among_stakeholders_in_interactive_system.jpg)
Author/Copyright holder: Unknown (pending investigation). Copyright terms and licence: Unknown (pending investigation). See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/about/terms-of-use) below.
**图 13.7**：不同用户群体可能存在冲突的需求，这些需求将在由设计师引导的研讨会中进行协商。

正如图 7 所示，在协商过程中由专家在轻松的环境中引导讨论，有助于减轻利益相关者之间的紧张情绪和潜在冲突。

下一节将需求工程（Requirements Engineering）活动纳入一个通用流程图（generic process map）中，以阐明其典型路径。

### 13.1.8 需求工程的过程图（Process Map of Requirements Engineering）

需求工程（Requirements Engineering）遵循不同的路径和活动组合；例如，需求可能始于当前系统存在的问题，或者用户所期望的产品示例。用于选择产品的基于采购的需求工程（Procurement-based Requirements Engineering）超出了本章的范围（关于基于商业现成软件的需求工程，见 Maiden & Ncube, 1998），因此本章仅解释最常见的、目标导向的（goal-oriented）路径。需求由高级管理人员和公司高管以政策、宗旨、目标和其他高层意向声明的形式发起。如图 8 所示，由于需求始于表达模糊的意向和用户的愿望清单，因此该路径需要大量的范围界定活动（scoping activity）。该过程借鉴了业务分析（business analysis），例如 *设定政策目标* (1) 和 *分析并建模业务* (2)。政策可以通过企业模型（enterprise models）在业务语境中进行分析。与政策分析相关的非需求工程活动包括业务建模（business modelling）、价值链分析（value-chain analysis, Porter, 1980）、竞争优势理论以及业务流程重组（business process re-engineering, Davenport, 1993）。业务分析技术，如业务流程分析（business process analysis）、概念图（concept maps, Eden, 1988）和关键成功因素（critical success factors, Rockart & Short, 1991），在此阶段同样适用；然而，提出一套详细的方法论超出了...的职责范围

需求工程（Requirements Engineering）。其核心问题在于对业务进行建模，以发现开发计算机系统从而增强竞争优势（Competitive Advantage）的机会。尽管在价值链模型（Value-chain models）[例如 (Porter, 1980)] 以及组织间系统设计（Inter-organisational system design）的案例历史 (Holland, 1995) 中可以找到一些建议，但该领域仍缺乏深入的理解。业务分析社区（Business analysis community）中的方法和手段在很大程度上仍依赖于直觉，因此遗憾的是，从该来源中只能获得有限的指导。

![](https://public-media.interaction-design.org/images/encyclopedia/requirements_engineering/fig08_Goal_oriented_pathway_for_requirements_engineering.gif)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 13.8**：需求工程的目标导向路径（Goal-oriented pathway）

自顶向下的分解（Top-down decomposition）是一种常规方法，通过该方法将策略层意图（Policy-level intentions）逐步分解为目标。管理层的目标与通过访谈、焦点小组（Focus groups）、研讨会等方式在“需求获取（Elicit requirements）”(3) 步骤中收集的用户事实、信息和目标相结合。这些内容构成了“需求分析（Analyse requirements）”(4) 的输入，在该步骤中，通常以列表和笔记形式呈现的初步信息将被组织起来，并建立事实之间的联系。例如，

随着对策略上下文（context of the policy）的理解——即为了实现策略而必须执行的操作（目标，goals）以及对人员（参与者，actors）及其组织（组织单位，organisation unit、对象，objects 等）的影响——关系被逐步添加。 “分析需求（Analyse requirements）”与“需求与领域建模（Model requirements and domain）”(5) 是交织进行的，因为分析过程会产生用于记录事实及其关联的模型。

例如，在目标如何影响任务和组织的上下文中对目标进行建模，不仅对于详细阐述非正式意图陈述（informal statements of intent）的含义至关重要，而且能够实现对变更影响的评估 (Chung, 1993; Yu, 1993)。目标需要作为语言形式的意图陈述进行细化，直到能够描述系统期望状态的阶段，届时可能可以进行形式化（formalisation）(Dardenne et al., 1993)。超文本工具（Hypertext tools）可以帮助表示非正式的目标层次结构（goal hierarchies）(Pohl, 1996)，标准概念模型（conceptual models，例如数据流图 data flow diagrams）同样可以实现，但目前针对目标相关的需求分析，缺乏足够的建议或过程指导。Chung (1993) 和 Yu (1993) 在上下文模型（context models）中提供了目标的表示方法，展示了目标（包括功能性和非功能性目标）、参与者和任务之间的依赖关系，并给出了一些关于目标分解（goal decomposition）和建模的指南。在此路径中，建模是“验证需求（Validate requirements）”阶段 (6) 的必要前置步骤，因为如果没有上下文，目标将难以被理解。

详细说明如何实现这些目标，以及它们与代理（agents）和过程（processes）之间的关系。*验证需求（Validate requirements）* 通常与 *协商需求（Negotiate requirements）*(7) 交织在一起，因为利益相关者（stakeholders）与设计者之间的讨论会导致需求被接受或拒绝，并解决利益相关者之间的冲突。该过程中的第 4 至 7 阶段构成一个迭代循环（iterative loop），因为需求很少能在第一次就被正确地定义；相反，需求是通过分析、建模、验证和协商的迭代而逐渐显现的。策略路径（policy route）与其他需求工程（Requirements Engineering）路径在权衡分析（trade-off analysis）和协商等共同活动中汇合，这两者对于面向目标的需求工程（goal-oriented Requirements Engineering）都至关重要。一旦目标被分解到能够（至少是非正式地）描述系统期望状态的阶段，就可以就技术的使用做出初步决定（first-cut decisions）。一些目标会转化为功能性需求（functional requirements），而另一些则仅对管理具有影响（例如关于资源、组织和人类活动的决定）。

在描述了需求工程活动之后，下一节将回顾基于场景的方法（scenario-based approaches），这些方法构成了需求工程与人机交互（HCI）之间的共同基础。

## 13.2 基于场景的设计：HCI 与 RE 的共同点

人机交互（Human-Computer Interaction, HCI）与需求工程（Requirements Engineering, RE）的母学科软件工程（Software Engineering, SE）都是旨在开发软件系统的设计学科。两者之间紧密的关系引发了广泛的讨论，但遗憾的是，很少有建设性的综合研究。需求工程可以被视为软件工程的前端，因为它专注于实现之前的需求和过程阶段，尽管需求工程与软件工程之间的界限正变得日益模糊。相比之下，HCI 涵盖了整个设计过程。它与软件工程的界限取决于这两个学科的关注重点。软件工程的核心关注点是软件，因此社会技术（socio-technical）意义上的人员和系统是次要关注点；而 HCI 则专注于人员和 [用户界面（user interface）](https://www.interaction-design.org/literature/topics/ui-design) 以及更广泛的社会技术系统的设计，而相对地牺牲了对软件架构的关注。需求工程与 HCI 的共同点在于共享的过程和表示方法，这些方法以不同的形式被倡导，如以用户为中心的设计（user-centred design）、基于场景的设计（scenario-based design）、[迭代开发（iterative development）](https://www.interaction-design.org/literature/topics/iterative-development%09) 以及 [敏捷（agile）](https://www.interaction-design.org/literature/topics/agile-development) 方法。

人机交互 (Human-Computer Interaction, HCI) 和需求工程 (Requirements Engineering) 都将场景 (scenarios) 作为设计的[驱动 (motivation)](https://www.interaction-design.org/literature/topics/motivation)，尽管这两个领域在形式和功能上有所不同。

不幸的是，“场景”一词在文献中被滥用了，目前存在大量的定义（参见 Rolland et al., 1998）。事实上，许多关于场景的文献，特别是软件工程 (Software Engineering) 传统 (Kaindl, 1995) 中的文献，实际上是在描述通过状态转移模型 (state transition models) 的事件序列轨迹 (event-sequence traces)。在面向对象设计 (object-oriented design) 中，很难区分用例 (use cases)、用例的替代路径 (alternative paths) 以及场景 (scenarios)——而场景仅仅是穿过用例的另一种路径 (Cockburn, 2001; Graham, 1996; Jacobson et al., 1992)。场景在设计中扮演着多种角色，从激发设计师想象力的“认知假体 (cognitive prosthesis)”，到关于系统使用和问题的叙事 (narratives)，而需求正是在这些叙事中产生的 (Carroll, 2002)。Certificates在需求工程（Requirements Engineering）中，场景（scenarios）通常被视为建模（modelling）的输入，并与用例（use cases）和需求获取（requirements elicitation）密切相关，构成了 RUP（Rational Unified Process）的早期阶段。相比之下，人机交互（HCI）较少强调从场景到建模的联系；相反，场景以及诸如 [用户角色（personas）](https://www.interaction-design.org/literature/topics/personas) 等其他技术旨在激发设计过程中的思考 (Carroll, 2002)。场景可以与用户角色相结合，通过描述典型用户来增强叙事体验（narrative experiences）。事实上，一些学者建议设计刻意设置的极端场景，以激发建设性的思考 (Djajadiningrat et al., 2000)。

可以说，场景是所有建模和设计的起点；然而，建模在 HCI 领域已不再流行，任务模型（task models）也很少被提及为设计过程的组成部分。在需求工程和软件工程（Software Engineering）中，建模仍然是一项主流活动，这体现了这两个学科之间的关键分歧。见图 2。

场景与模型的一种高效结合方式是将场景作为 [测试（test）](https://www.interaction-design.org/literature/topics/test) 数据来验证设计模型。这种方法一直被积极地

这在 Potts (1999) 的探究循环（Inquiry Cycle）中得到了研究，该循环建议将场景（scenarios）作为具体语境，以测试系统输出（system output）的实用性（utility）和可接受性（acceptability）。通过质疑系统输出与场景中所描述的一组利益相关者（stakeholders）及其任务的相关性，分析师可以发现实现系统需求（system requirements）的障碍。输入事件（input events）可以从场景中导出，用于测试验证程序（validation routines）和其他功能需求（functional requirements）。这一方法已被优化为一个正式流程，用于根据从场景中提取的一组环境状态（environmental states）来探索系统目标的可实现性（achievability）(Van Lamsweerde & Letier, 2000)。

![](https://public-media.interaction-design.org/images/encyclopedia/requirements_engineering/fig09_scenarios_in_requirements_engineering_software_engineering_process.gif)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 13.9**：场景在需求工程-软件工程流程（Requirements Engineering-Software Engineering process）不同阶段的应用

为了通过 ADVISES 电子科学系统（e-science system）的一些示例进行说明，初始愿景场景（vision scenario）描述了医学研究人员在未来可能的工作方式：

> 流行病学家（Epidemiologists）在地图和不同的图表中查看来自英国不同地区的数据集。他们可以提出问题

使用有限的自然语言和简单的控件（如滑块 Sliders）来处理数据，以便他们能立即看到全国不同地区数据的各种分析结果。当他们发现有趣的结果时，可以添加注释并将结果发送给其他研究团队的同事。

愿景场景（Vision scenarios）在任何原型（Prototype）出现之前就为开发项目设定了场景，因此它们侧重于预期结果。

相比之下，使用场景（Usage scenarios）则更详细地描绘了系统的运行方式，并且通常伴有故事板（Storyboards）和原型以阐明设计：

> Iain 想要查看大曼彻斯特（Greater Manchester）不同地区学龄儿童的哮喘与肥胖之间是否存在某种联系。他加载了不同地区哮喘和肥胖发病率的数据集。地图显示，除两个局部地区外，大多数地区之间几乎没有关联，而这两个地区的肥胖和哮喘高发情况通过地图上的颜色编码（Colour coding）显示出来。他通过应用区域密度修正统计量（Area density correction statistic）并运行相关性分析（Correlation analysis）来验证该结果的准确性。结果显示具有显著性。然而，饮食和缺乏运动是儿童肥胖更常见的原因，因此 Iain 在地图上加载了体育设施的位置，发现这两个哮喘-肥胖热点（Hotspots）地区的体育设施也较少。他的调查仍在继续。

在开发周期的后期，语境与使用（Context and use）

场景（Scenarios）描述了系统的使用方式，但同时包含了对系统输出如何被使用的预期，其中包括用于验证和评估环节的测试探针（Test Probes），例如：

> 你是 Greater Heaton PCT 的一名公共卫生分析师。你希望查看你所在区域 6 年级（11 岁）儿童的体质指数（BMI）。请基于中层超级输出区域（Middle Layer Super Output Areas）并使用你的第一组数据集创建一张新地图。加载较小年龄儿童的数据集并检查地图显示，使用滑块（Sliders）通过年龄、性别和其他提供的变量来更改结果的视图。观察在仅查看男性、仅查看女性以及两者共同查看的地图时，是否能发现任何普遍模式。

> 你注意到幼儿班（Reception Class）地图的一个区域存在一个肥胖率似乎较高的热点（Hotspot）。加载较小年龄儿童的数据集并检查地图显示，使用滑块通过年龄、性别和其他提供的变量来更改结果的视图。调查这是否看起来像一个真实的热点。

人机交互（HCI）在可用性评估（Usability Evaluation）中以类似的方式使用场景，尽管场景的作用并没有被阐述得如此清晰。尽管如此，评估方法（Monk & Wright, 1993; Sutcliffe, 2000a）中的任务或测试脚本（Task or Test Scripts）本质上就是场景。Carroll 还认可了场景在任务-人工制品循环（Task-Artefact Cycle）中的验证作用。在该循环中，对已实现的人工制品（Implemented Artefact）进行评估，从而引导设计改进，并通过声明分析（Claims Analysis）的过程产生新的 HCI 知识。

Carroll 阐述了场景（Scenarios）在设计过程中的多种不同作用，包括将其作为设计探索、需求获取（Requirements Elicitation）和验证（Validation）的设想（Envisionment）工具 (Carroll, 1995)。其他作用还包括：用于揭示问题的使用场景（Usage Scenarios）；用于激发新的人造物（Artefact）设计的启动或愿景场景（Initiating or Visioning Scenarios）；以及描述已设计的人造物未来使用情况的预期使用场景（Projected Use Scenarios） (Sutcliffe & Carroll, 1998)。

## 13.3 模型与设计表示（Models and Design Representations）

模型是需求工程（Requirements Engineering）的核心关注点，因为它们既是系统的表示，也能为需求过程中的推理提供支持。需求工程中最流行的模型是用例（Use cases），这与商业系统开发和软件工程（Software Engineering）所采用的模型相同；见图 10。

| 用例编号 | EM3 |
|---|---|
| 名称： | 查看地图区域名称 |
| 描述： | 已创建基础主题地图（Theme map） |
| 主参与者（Primary actor）： | 流行病学家（Epidemiologist） |
| 前置条件（Pre-condition）： | 用户已成功创建一张划分为地理区域的主题地图 |
| 触发条件（Trigger）： | 地图已创建，用户准备探索地图 |
| 基本流（Basic flow）： | 选择区域，查看名称 |
| 替代流（Alternate flows）： | 错误处理——无法显示所选区域的名称<br>• 用户通过将鼠标指针悬停在感兴趣的区域上，选择其感兴趣的地图区域<br>• 暂停 1 秒后，显示区域名称的悬停文本（Hovertext）——该悬停文本将一直存在，直到用户移动鼠标 |

![](https://public-media.interaction-design.org/images/encyclopedia/requirements_engineering/fig10_use_case_context_diagram_action_sequence_template.gif)

作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”部分。

**图 13.10**：用例上下文图（Use case context diagram）以及在动作序列模板（action sequence template）中定义的低层级用例（lower-level use case）

与需求工程（Requirements Engineering）更为具体相关的是 $i^*$ 模型族（$i^*$ family of models），该模型记录了由依赖（dependency）和手段-目的关系（means-ends relationships）连接的代理（agents）、目标（goals）、任务（tasks）和资源（resources），如图 4 和图 11 所示。

![](https://public-media.interaction-design.org/images/encyclopedia/requirements_engineering/fig11_strategic_dependency_model_functional_requirements_and_non-functional_requirements.gif)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”部分。

**图 13.11**：$i^*$ 战略依赖模型（strategic dependency model），展示了代理（圆圈）、目标或高层级功能性需求（functional requirements，圆角矩形）、资源（rectangles，矩形）以及软目标（soft goals）或非功能性需求（non-functional requirements，云形）

目标模型（Goal models）和面向目标的分析（goal-oriented analysis）也是需求工程中的关键影响因素（GORE：参见 Potts, 1999）。目标层级（Goal hierarchies）代表了用户需求的分解（decomposition），其中的关系展示了它们之间的相互作用，例如支持（support）、抑制（inhibit）或阻碍（hinder）。目标模型与任务模型（task models）具有共同的渊源，尽管任务模型不仅记录意图（intent），还记录执行任务的操作序列（operational sequence）。任务模型（例如 HTA：Annett, 1996；TAKD：

(Diaper & Johnson, 1989) 将目标分解层级（goal-decomposition hierarchies）与较低细节层级的动作序列描述（action sequence descriptions）联系起来。目标模型和任务模型均采用层级表示法（hierarchical notation），如图 12 所示。

![](https://public-media.interaction-design.org/images/encyclopedia/requirements_engineering/fig12_goal_model_similar_to_task_model.gif)

作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

**图 13.12**：图书馆目标模型，其中高层目标被分解为低层子目标。人机交互（HCI）中的任务模型也遵循类似的模式。

依赖关系（Dependency relationships）由弧线上的 D 符号表示，意味着某种关联，例如一个目标依赖于某个代理（agent）来实现，或者一个目标依赖于某种资源（resource）以达成。手段-目的关系（Means-end relationships）记录了目标如何通过任务、代理和资源来交付。目标属于用户，且等同于需求（requirements）。在 $i^*$ 中，硬目标（hard goals）与软目标（soft goals, NFRs）之间存在区别：前者将成为由软件程序实现的功能性需求（functional requirements）；后者则是质量需求，如可用性（usability）、安全性（safety）、成本（cost）或准确性（accuracy）。

软件工程（SE）扩展了需求工程（Requirements Engineering）模型，以提供软件系统的不同视图，例如类中的数据处理结构...

...图表，活动序列图（activity sequence diagrams）中的行为，或状态转换图（state transition diagrams）中的事件序列。

任务模型（Task models）提供了一种对现实世界的抽象视图，其一组语义（semantics）由建模目标所驱动。同样地，软件工程（Software Engineering）中的类图（class diagrams）代表了系统对象的抽象继承结构（inheritance structure），而状态转换图则代表了面向活动的规范（activity-oriented specification）。任务模型属于一种表示意图（intent，即目标 goals）和活动（activity，即过程 procedures 或动作序列 action sequences）的建模类型（modelling genre）。任务建模已通过 TKS（Task Knowledge Structures: Johnson et al., 1988）中的领域知识结构（domain knowledge structures）扩展到涵盖面向数据的视图，并被适配到 MAD（Methode Analytique et Description: Rodriquez & Scapin, 1997）中的面向对象范式（object-oriented paradigm）。任务模型的一个主要作用是在对功能分配（functional allocation）进行推理时表示问题空间（problem space）。尽管关于功能分配的文献承认了[任务分析（task analysis）](https://www.interaction-design.org/literature/topics/task-analysis)的必要性，但很少显式地表示任务模型（参见 Dearden et al., 2000）。相反，在诸如 IDAS（Information, Decision, Action, Supervision: Wright et al., 2000）等与任务相关的框架中，可能会使用场景（scenarios）来驱动功能分配的决策。然而，任务模型可用于在功能分配过程中对活动进行划分（partition activity）。

(Sutcliffe, 1997; Vicente, 2000)，且这仍然是它们的主要作用之一。对任务分析（Task Analysis）的一种批评是，与侧重于上下文描述（Contextual Description）的场景叙事（Scenario Narratives）相比，它无法捕捉现实世界中交互的丰富性（例如 Kuutti, 1995; Kyng, 1995）。然而，任务模型（Task Models）已被扩展用于描述任务中隐含的信息需求（Information Requirements）（Sutcliffe, 1997），以及生态界面设计（Ecological Interface Design）中工作制品（Work Artefacts）的作用（Vicente, 2000）。另一个缺失之处是对参与协作任务（Collaborative Tasks）的主体（Agents）之间通信缺乏显式表示（Explicit Representation），尽管这在 GTA (Van Der Veer et al., 1996) 中得到了部分规定，并在耦合分析（Coupling Analysis）中得到了更明确的处理，后者提供了一个可以整合到任务中的话语分析框架（Discourse Analysis Framework）。

工作量分析（workload analysis）(Sutcliffe, 2000b, 2002b)。最后，任务模型（task models）可能会因为未能表示主体（agents）、活动（activity）与组织结构（organisational structures）之间的关系而受到批评，尽管这些概念在诸如 ORDIT (Eason et al., 1996) 等社会技术系统设计框架（socio-technical system design frameworks）中有所描述；而更全面的建模语言则可以在需求工程（Requirements Engineering）中找到，例如分析主体、任务、目标和资源之间依赖关系（dependencies）的 *i** (Mylopoulos et al., 1999; Yu, 1993)。

任务分析（Task analysis）作为一种方法或符号表示法（notation），除了在人因安全工程社区（human factors safety engineering community）（例如分层任务分析 Hierarchical Task Analysis: Annett, 1996）之外，在实践中并未被广泛采用 (Bellotti, 1988; Diaper, 1999)。此外，建模在 HCI 领域已不再受到青睐，取而代之的是一些轻量级表示（lightweight representations），例如用于 [信息架构（information architecture）](https://www.interaction-design.org/literature/topics/information-architecture) 的层级图（hierarchy diagrams）、设计草图（design sketches）、线框图（wireframes）和故事板（storyboards），这些已成为常态。

一种共同的表示类型是设计理由（Design Rationale），它被 HCI 和需求工程共同采用，用于记录设计决策并提出可供讨论的替代设计方案。在需求工程中，gIBIS (Conklin & Begeman, 1988) 符号表示法被用于将用户目标表示为问题（issues），并将其映射到带有论据（arguments）的设计替代方案（design alternatives，即需求）中。QOC (MacLean &

McKerlie, 1995），其 HCI（人机交互）版本采用了类似的格式，将问题（Questions）视为设计议题（design issues），将选项（Options）视为设计替代方案（design alternative），并将准则（Criteria）用于在不同设计之间选择权衡（trade-offs）；参见图 13。

![](https://public-media.interaction-design.org/images/encyclopedia/requirements_engineering/fig13_design_rationale_diagram.gif)

作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

**图 13.13**：展示 gIBIS-需求工程（Requirements Engineering）变体的设计理由图（Design Rationale Diagram）

图 13 中所示的设计议题源自一个关于集装箱船安全至关重要（safety-critical）的火灾管理系统需求分析的案例研究。当热传感器检测到火灾时，接下来的议题是如何通知船员。该图展示了三种设计替代方案，并将其与权衡准则相联系。第一种方案建议使用声音警报（audio alarm），它可以将警报播报至全船，但无法提供关于火灾位置的关键信息。第二种方案是在面板显示屏上使用视觉警报（visual alarm），这种方式虽然可靠，但更具局部性（localised）；而第三种方案是使用船舶的视觉图表并高亮显示火灾位置，这能提供更好的信息。设计理由图允许用户将不同的需求作为设计选项来观察其权衡关系；然而，QOC（Questions, Options, Criteria）在实际应用中一直难以……

引入到新的实践共同体（Communities of Practice）(MacLean & McKerlie, 1995) 中，而在 gIBIS (Conklin & Begeman, 1988) 版本的设计理由（Design Rationale）(Buckingham Shum, 1996; Sutcliffe & Ryan, 1997) 中也遇到了类似的问题。

## 13.4 需求工程与人机交互中的设计流程

需求工程（Requirements Engineering）与人机交互（Human-Computer Interaction, HCI）之间的关键区别之一在于流程。需求工程是一门系统化的工程学科，因此更倾向于采用特定的技术和系统化的流程。虽然需求工程没有像软件工程（Software Engineering, SE）中的 RUP 那样的标准方法，但它仍然遵循一定的流程，并应用一套技术来对需求进行获取（elicit）、分析（analyse）、规格化（specify）和验证（validate），例如 Volere 方法 (Robertson & Robertson, 2002)。在软件工程中，流程指导的性质各异，既有像 RUP 这样较为繁重的（substantial），也有类似于基于场景的设计（scenario-based design）的轻量级敏捷方法（agile methods）(Beck, 1999)。

在 HCI 中，开发通过以用户为中心的设计（user-centred design）展开，通过设计探索（design exploration）和用户评估（user evaluation）的迭代周期，逐步优化设计，最终收敛于一个能够满足用户需求的解决方案。在此过程中，不采用正式的设计检查或测试程序。相比之下，需求工程更强调对规格说明（specifications）的自动化检查，这通常被称为模型检测（model checking）。这涉及对软件规格说明的自动化检查，以确保程序代码最终能够正确且可靠地运行。需求工程中最具影响力的形式化方法之一是 KAOS 方法及其相关工具 (Van Lamsweerde, 2009)。KAOS 遵循...

需求工程（Requirements Engineering）的主流方法采用目标导向方法（goal-oriented approach），但它在规范（specification）方面走得更远，因为目标被细化为更低层级的细节，用以表达系统应当实现、维持或避免的状态。随后，模型检测器（Model checkers）会验证指定的过程是否能够实现这些目标。KAOS 通过工具支持需求工程，从而可以评估目标的约束（constraints）、假设（assumptions）以及目标的障碍（barriers），后者被称为“阻碍（obstacles）”；例如，为了实现某个特定目标，需要哪些必要的假设？这仅仅概括了 KAOS 及其支持工具 GRAIL 的功能；实际上它更为复杂，其采用的时序逻辑（temporal logic）还能够对目标何时能被实现进行推理。然而，KAOS 以及所有形式化软件工程（formal Software Engineering）方法都假设关于规范和系统环境的细节已知且相当详尽。这是其与人机交互（HCI）的一个关键分歧点，后者将开发概念化为一个知识是不完整的、更具动态性的过程。HCI 曾经对形式化分析（formal analysis）感兴趣，但这种兴趣在多年间有所减弱，尽管目前该领域依然活跃（Thimbleby, 2007），且在模型检测方面有类似的兴趣。

## 13.5 设计建议与知识复用（Design Advice and Knowledge Reuse）

人机交互（HCI）和需求工程（Requirements Engineering）都会复用知识，尽管方式有所不同。在需求工程中，产品线需求（product-line requirements）是复用的主要方法，其中需求与特定应用领域（application domain）的一组相关设计相绑定。产品线是对某一主题的变体，这在工程领域十分常见；例如，汽车工业中用于发动机控制和制动系统的软件。需求可分为由许多应用共享的共同核心需求（common core requirements）和变体点（variation points）：即在不同设计版本之间发生变化的需求。需求工程采用了更广泛的软件复用（software reuse）领域的方法，通过创建特征层次图（hierarchy diagrams of features），展示特征分解（feature decomposition）中可能进行定制（tailoring）的点。在需求工程中，已有研究探讨了管理产品线需求的流程，旨在规划发布计划并确定变体和版本的优先级 (Finkelstein et al., 2008)。

需求复用受到的关注较少，尽管在航空发动机控制器的研究中提出了一些通用需求 (Lam et al., 1997)；并且在更抽象的层面上，一个可复用的通用需求库被与抽象问题模型（abstract problem models）联系在一起 (Sutcliffe, 2002a)。这些抽象模型与更详细且特定于领域的产品线之间关系较远，因此复用的目的是

旨在在需求过程中提供思考工具（tools for thought），而非可定制的规范（specifications）。在需求工程（Requirements Engineering）中，最抽象的复用模型是问题框架（Problem Frames, Jackson, 2001），它通过软件过程与其外部环境之间的依赖关系（dependencies）来描述高层需求。四种问题框架分别描述了：监控与控制设备（所需行为，required behaviour）、响应外部指令（指令行为，commanded behaviour）、编辑与更新状态（工件，workpieces）以及通用转换（general transformations）。抽象问题模型（Abstract problem models）提供了更多细节，涵盖了 11 类问题族（families of problems），包括事务（transactions）、租赁（hiring）、监控控制（monitoring control）、物流（logistics）和追踪（tracking）。人机交互（HCI）非常强调知识的复用（reuse of knowledge）。目前已经产生了大量的指南（guidelines）（ISO1997, 1998），其中...

将原则与启发式（principles and heuristics）视为设计建议（design advice）的一种更通用的表达方式 (Benyon & Macaulay, 2002)。图 14 所示的任务-人工制品循环（task-artefact cycle, Carroll, 2000）通过人工制品（artefacts）来促进复用。这些人工制品是设计示例，可以像产品线（product lines）一样被组织成族（families）(Sutcliffe, 2000b)；不过，人工制品的驱动因素往往是交互设计关注点（interaction design concerns），而非像产品线需求那样由功能性（functionality）驱动。人工制品与主张（claims）相关联，这些主张以类似于设计理由（design rationale）的方式，将设计权衡（design trade-offs）封装为优势（upsides）和劣势（downsides）。主张还与使用场景（scenarios of use）相关联，以便将设计建议锚定在现实场景中。

![](https://public-media.interaction-design.org/images/encyclopedia/requirements_engineering/fig14_task-artefact_cycle.gif)
作者/版权持有者：未知（待调查）。版权条款与许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”章节。
**图 13.14**：用于在人机交互（HCI）中创建可复用知识的任务-人工制品循环

主张中的优势和劣势将可用性论据（usability arguments）呈现为基于心理学的设计理由中的权衡。主张的生成过程包括：实现一项设计，评估所实现人工制品的可用性，随后提取出主张，并迭代地改进设计。该人工制品由此成为了一个实例化……的示例。

该主张（claim），而主张及其与理论的链接则为为什么该主张能够提升可用性（usability）提供了证明，并补充了关于依赖关系和设计权衡（design trade-offs）的信息。见图 15。

| 主张 ID： | 颜色编码的电报式显示（Colour-coded Telegraphic Display） |
|---|---|
| 作者： | Singley, M.K.; Carroll, J.M. |
| 人工制品（Artifact）： | MoleHill tutor - Goalposter tool |
| 描述： | 一种对目标的颜色编码电报式显示 |
| 优点（Upside）： | 提供关于操作正确性的持续反馈，以及获取进一步信息的途径 |
| 缺点（Downside）： | 学习者必须学习该显示的特征语言（feature-language）和控制方式 |
| 场景： | 窗口中单个目标的呈现方式是电报式的，最多包含几个单词。然而，学习者可以通过菜单选择展开任何电报式目标，以显示关于该目标是否值得追求的更详细解释。因此，系统既提供了关于正确性的简写反馈，又提供了获取进一步帮助的途径。 |

**图 13.15**：主张的示例（改编自 Carroll et al., 1992）

凭借提供上下文的“任务-人工制品循环（task-artefact cycle）”，主张比指南（guidelines）能更具针对性地传递人机交互（HCI）知识。主张在人工制品上下文中具有特定领域的锚点（domain-specific anchor）；然而，它们可以与通用问题模型（generic problem models）相链接，从而为重复利用提供更广泛的上下文（Sutcliffe & Carroll, 1998; Sutcliffe, 2002a）；例如，人因工程（human factors）问题与监控任务或

用于招聘/贷款、销售以及物流/分销等方面的事务处理（transaction processing）。此外，断言（claims）可以与交互模式（interaction patterns）相关联，从而将人机交互（HCI）知识与软件工程（Software Engineering）的用例（use cases）联系起来。

- **- 购买流程（Purchase Process）-**

**问题**
用户希望购买已选中的产品。

**解决方案**
向用户展示购买步骤。
[示例来自 [www.bn.com](http://www.bn.com/)]

**适用场景**
该网站允许购买商品，通常是[电子商务网站（E-commerce Site）](http://www.welie.com/patterns/showPattern.php?patternID=commerce)，但也可以是恰好销售产品的网站，例如[博物馆网站（Museum Site）](http://www.welie.com/patterns/showPattern.php?patternID=museum)。购买行为也可以是更大型任务的一部分，例如[预订（Booking）](http://www.welie.com/patterns/showPattern.php?patternID=booking)。

**实现方式**
为了购买购物车中的产品，用户需要选择结账（checkout）操作。结账是一个包含五个步骤的[购买流程（Purchase Process）](http://www.welie.com/patterns/showPattern.php?patternID=purchase-process)，具体任务如下：
1. 识别客户
2. 选择配送地址和特殊选项
3. 选择支付方式
4. 查看整个订单的概览
5. 确认并提交订单
6. 通过电子邮件接收确认函

用户可以在任何步骤中止结账流程。当用户稍后重新尝试结账时，将从第一个任务重新开始。可考虑使用[向导（Wizard）](http://www.welie.com/patterns/showPattern.php?patternID=wizard)。

旨在引导用户完成这些任务，同时尽量减少所使用的网页数量。然而，并非所有的购买流程都需要引导程序（Wizard）。许多网站经常要求提供一些对于处理订单并非绝对必要的详细信息。在许多情况下，所有订单信息都可以轻松地容纳在一个页面中，从而无需使用引导程序。

**尽量减少[导航（Navigation）](https://www.interaction-design.org/literature/topics/navigation-1)和非相关页面元素**

由于购买是一项需要高度专注的任务，因此购买过程中的标准页面布局必须简化。不应显示次级导航（Sub-navigation）和上下文元素（Contextual elements）。所有干扰元素都应被移除。

**用户登录（User Login）**

许多网站要求用户在流程的第一步进行[登录（Login）](http://www.welie.com/patterns/showPattern.php?patternID=login)。虽然这对回头客来说很方便，因为他们所有的个人数据都可以被重复利用，但对于新用户来说体验并不理想。应允许新客户在不创建账户的情况下购买商品。在购买结束时，可以引导用户进行[注册（Registration）](http://www.welie.com/patterns/showPattern.php?patternID=registration)。这样注册过程可以变得非常简单，因为所有基础数据在购买过程中已经采集完毕，用户仅需选择用户名和密码即可。**电子邮件确认**
在浏览器关闭后，向用户提供一个易于[访问（accessible）](https://www.interaction-design.org/literature/topics/accessibility)的内容至关重要。包含购买信息的电子邮件就像是用户的“收据”。它应包含订单号、订单商品清单、总金额、配送地址、支付信息以及下单日期。此外，还应包含引导用户如何追踪订单、取消订单或请求帮助的说明。

**原因分析**
对于初次购买或低频客户，使用[向导（Wizard）](https://www.interaction-design.org/literature/topics/wizard)能更好地帮助用户通过简单的步骤完成购买。而再次购买的客户通常使用相同的配送地址和信用卡，因此，通过一个带有“购买”按钮的概览界面即可更高效地完成流程。

**图 13.16**：电子商务购买交互设计的 HCI 模式（HCI pattern）示例

这种对主张（claims）的视角与这两个学科共同采用的模式（patterns）相似。模式记录了可复用的设计建议，并包含其使用示例、激励场景（motivating scenario）、应用内容描述以及力（forces）——本质上是指优势与劣势之间的权衡。在 HCI 领域，模式倾向于关注用户界面（user interface）的问题与设计 (Tidwell, 2005)，而软件工程（Software Engineering）的模式则涵盖了从低层软件解决方案 (Gamma et al., 1995) 到高层流程与设计的范围 (Coplein, 1996)。模式建议将设计建议置于激励问题的语境中呈现，并提供其应用示例 (Borchers, 2001)。尽管模式确实包含一个指明设计建议适用问题范围的条款，但这种范围界定（scoping）是 *ad hoc*（缺乏系统性）的。模式的倡导者提出在单个模式之间建立关系，将其构建为类超文本的模式网络或模式语言（pattern language）(Alexander et al., 1977) 以设定语境。不幸的是，模式语言同样是 *ad hoc* 的，且往往是不完整的。

图 16 以简略形式展示了来自 van Welie 集合 ([www.welie.com](http://www.welie.com/)) 的一个 HCI 模式示例。该模式描述了其适用的问题语境，随后给出了解决方案及示例，并提供了指向相关模式的链接。

并且一些模式格式增加了“驱动力（Forces）”，以便就使用该模式的优缺点提供论据。

## 13.6 结论与未来方向

人机交互（Human-Computer Interaction, HCI）和需求工程（Requirements Engineering, RE）在设计过程方面持有许多共同观点。这两个学科都主张采用包含测试和评估的迭代设计周期（iterative design cycles），尽管其以用户为中心（user-centredness）的程度有所不同。一个被这两个学科共同忽视的话题是确定自动化边界（automation boundary）。这在人因工程（human factors）领域已有研究，其中用于功能分配（functional allocation）的方法和启发式规则决定了哪些过程应完全自动化、由人工操作或通过人机协作共同完成 (Wright et al., 2000; Sutcliffe, 2002c)。然而，在需求工程中，这个问题很少被提及，而主流的 HCI 则假设用户界面边界是从设计探索（design exploration）的过程中自然产生的。

随着时间的推移，HCI 变得不再那么依赖于方法，而需求工程则保持了更为系统化的工程方法。专家设计师很少显式地使用方法、指南、原则和模型 (Guindon & Curtis, 1988)。基于场景的设计（scenario-based design）是 HCI 最接近系统化方法的一种方式，尽管这种方法可能被视为一种思考工具（tools for thought），而非逐步的指导指南。正如 Carroll 所建议的，场景在运行时作为探测手段（probes）支持设计过程，用以测试假设并激发创造力。场景可以激发思考，但知识只有在以主张（claims）、原则和指南等概括形式存在时，才能被有效地复用。

人机交互（Human-Computer Interaction, HCI）的研究重点已从目标导向（Goal-oriented）的办公类应用扩展到娱乐领域的[用户体验（User Experience）](https://www.interaction-design.org/literature/topics/ux-design)和[产品设计（Product Design）](https://www.interaction-design.org/literature/topics/product-design) (Hassenzahl, 2010; Sutcliffe, 2009)，且情绪和感受的作用被认为是构建成功交互系统的关键需求 (Norman, 2004)。相比之下，需求工程（Requirements Engineering）除了偶尔处理情感需求 (Callele et al., 2006) 和价值 (Thew et al., 2008) 之外，几乎没有意识到在目标导向的应用之外还存在其他类型的应用。需求工程需要扩大其研究范围，以涵盖用户体验需求和基于价值的设计（Value-based Design） (Cockton, 2009)。

另一方面，HCI 可以从需求工程中获益，通过重新挖掘关于系统化规范（Systematic Specification）的既往研究，因为这些考量在安全关键型应用（Safety-critical Applications）中至关重要。障碍分析（Obstacle Analysis）技术 (Van Lamsweerde, 2009) 以及关于假设和用户偏好的推理 (Jureta et al., 2008) 都可以有效地引入到 HCI 中。

最后，随着应用变得更加智能化、具有自感知（Self-aware）和自适应（Adaptable）能力，这两个学科都需要认识到软件性质的变化。在需求工程中，针对智能应用的需求仍然处于研究议程（Research Agendas）阶段 (Sawyer et al., 2010)，而...

人机交互（Human-Computer Interaction, HCI）领域的智能用户界面（Intelligent User Interfaces, IUI）不仅体现在推荐系统（recommenders）和注意力用户界面（attentional user interfaces）中，而且还拥有其独立的 IUI 系列会议。然而，智能且社交网络化软件（socially networked software）的需求分析和以人为中心的设计（human-centric design）仍是这两个学科共同面临的未来挑战。

## 13.7 更多学习资源

### 13.7.1 教科书

最全面的教科书是 Van Lamsweerde (2009) 所著的 *Requirements engineering: From system goals to UML models to software specifications* (Chichester: Wiley)。
[Lamsweerde](https://www.interaction-design.org/references/authors/axel_van_lamsweerde.html), Axel van (2009): *Requirements Engineering: From System Goals to UML Models to Software Specifications.* Wiley

### 13.7.2 期刊与会议系列

该学科的主要期刊是 *Requirements Engineering* (Springer)。IEEE International Conference on Requirements Engineering 的会议论文集（Proceedings）可追溯至 2002 年；在 2002 年之前，该领域有两个独立的会议：IEEE Symposium of Requirements Engineering 和 International Conference on Requirements Engineering。

### 13.7.3 需求工程（Requirements Engineering）

[2009](https://www.interaction-design.org/references/periodicals/requirements_engineering_volume_14.html)[2007](https://www.interaction-design.org/references/periodicals/requirements_engineering_volume_12.html)[2004](https://www.interaction-design.org/references/periodicals/requirements_engineering_volume_9.html)[1998](https://www.interaction-design.org/references/periodicals/requirements_engineering_volume_3.html)

### 13.7.3.1 RE（需求工程，Requirements Engineering）- IEEE International Conference on Requirements Engineering

[2008](https://www.interaction-design.org/references/conferences/16th_ieee_international_requirements_engineering_conference_re_2008.html)[2007](https://www.interaction-design.org/references/conferences/15th_ieee_international_requirements_engineering_conference_re_2007.html)[2006](https://www.interaction-design.org/references/conferences/14th_ieee_international_conference_on_requirements_engineering_re_2006.html)[2005](https://www.interaction-design.org/references/conferences/13th_ieee_international_conference_on_requirements_engineering_re_2005.html)[2004](https://www.interaction-design.org/references/conferences/12th_ieee_international_conference_on_requirements_engineering_re_2004.html)[2003](https://www.interaction-design.org/references/conferences/11th_ieee_international_conference_on_requirements_engineering_re_2003.html)[2002](https://www.interaction-design.org/references/conferences/10th_anniversary_ieee_joint_international_conference_on_requirements_engineering_re_2002.html)[2001](https://www.interaction-design.org/references/conferences/5th_ieee_international_symposium_on_requirements_engineering_re_2001.html)[2000](https://www.interaction-design.org/references/conferences/icre_2000.html)[1999](https://www.interaction-design.org/references/conferences/4th_ieee_international_symposium_on_requirements_engineering_re_99.html)[1998](https://www.interaction-design.org/references/conferences/3rd_international_conference_on_requirements_engineering_icre_98%2C_putting_requirements_engineering_to_practice%2C_april_6-10%2C_1998%2C_colorado_springs%2C_co%2C_usa%2C_proceedings.html)[1997](https://www.interaction-design.org/references/conferences/3rd_ieee_international_symposium_on_requirements_engineering_re97.html)[1996](https://www.interaction-design.org/references/conferences/icre_1996.html)[1995](https://www.interaction-design.org/references/conferences/second_ieee_international_symposium_on_requirements_engineering_1995.html)

另请参阅 *IEEE Software, Information and Software Technology, Journal of Information Technology*。

### 13.7.4 IEEE Software Magazine

[2002](https://www.interaction-design.org/references/periodicals/ieee_software_magazine_volume_19.html)

### 13.7.5 Information and Software Technology

[2010](https://www.interaction-design.org/references/periodicals/information_and_software_technology_volume_52.html)[2007](https://www.interaction-design.org/references/periodicals/information_and_software_technology_volume_49.html)[1999](https://www.interaction-design.org/references/periodicals/information_and_software_technology_volume_41.html)[1997](https://www.interaction-design.org/references/periodicals/information_and_software_technology_volume_39.html)[1996](https://www.interaction-design.org/references/periodicals/information_and_software_technology_volume_38.html)

### 13.7.6 Journal of Information Technology

### [2006](https://www.interaction-design.org/references/periodicals/journal_of_information_technology_volume_21.html)

### 13.7.7 互联网 (Internet)

英国计算机学会 (British Computer Society, [www.resg.org.uk/](http://www.resg.org.uk/)) 的需求工程 (Requirements Engineering, RE) 专家组提供了一份关于 RE 资源、工具及参考文献目录的详尽列表；该专家组还出版一份*通讯 (Newsletter)*，用于列举相关活动并刊登评论和非正式文章。

### 13.7.8 相关领域（Related Fields）

*Human Computer Interaction*、*Software Engineering*、International Conference on Software Engineering (ICSE) 的 *Proceedings* 以及 *IEEE Transactions on Software Engineering* 等期刊发表过关于需求工程（Requirements Engineering, RE）相关的文章。关于 RE 流程的斯堪的纳维亚（Scandinavian）视角，请参阅 *Proceedings* of the Participatory Design Conferences。

### 13.7.9 IEEE Transactions on Software Engineering

[1992](https://www.interaction-design.org/references/periodicals/ieee_transactions_on_software_engineering_volume_18.html)[1981](https://www.interaction-design.org/references/periodicals/ieee_transactions_on_software_engineering_volume_16.html)

### 13.7.10 Human Computer Interaction

[2011](https://www.interaction-design.org/references/periodicals/human_computer_interaction_volume_26.html)[2010](https://www.interaction-design.org/references/periodicals/human_computer_interaction_volume_25.html)[2007](https://www.interaction-design.org/references/periodicals/human_computer_interaction_volume_22.html)[2006](https://www.interaction-design.org/references/periodicals/human_computer_interaction_volume_21.html)

### 13.7.10.1 PDC - International Conference on Participatory Design (参与式设计国际会议)

[2012](https://www.interaction-design.org/references/conferences/proceedings_of_the_12th_participatory_design_conference__volume_1_research_papers.html)[2012](https://www.interaction-design.org/references/conferences/proceedings_of_the_12th_participatory_design_conference__volume_2_exploratory_papers%2C_workshop_descriptions%2C_industry_cases.html)[2006](https://www.interaction-design.org/references/conferences/pdc_2006_-_proceedings_of_the_ninth_conference_on_participatory_design.html)[2004](https://www.interaction-design.org/references/conferences/pdc_2004_-_proceedings_of_the_eighth_conference_on_participatory_design.html)

## 13.8 References

[Alexander](https://www.interaction-design.org/references/authors/christopher_alexander.html), Christopher, [Ishikawa](https://www.interaction-design.org/references/authors/sara_ishikawa.html), Sara and [Silverstein](https://www.interaction-design.org/references/authors/murray_silverstein.html), Murray (1977): *A Pattern Language.* Oxford University Press
[Beck](https://www.interaction-design.org/references/authors/kent_beck.html), Kent (1999): *Extreme Programming Explained: Embrace Change.* Reading, MA, Addison-Wesley Publishing
[Bellotti](https://www.interaction-design.org/references/authors/victoria_bellotti.html), Victoria (1988): Implications of Current Design Practice for the Use of HCI Techniques. In: [Jones](https://www.interaction-design.org/references/authors/dylan_m__jones.html), Dylan M. and [Winder](https://www.interaction-design.org/references/authors/r__winder.html), R. (eds.) [Proceedings
 of the Fourth Conference of the British Computer Society Human Computer
 Interaction Specialist Group - People and Computers IV](https://www.interaction-design.org/references/conferences/proceedings_of_the_fourth_conference_of_the_british_computer_society_human_computer_interaction_specialist_group_-_people_and_computers_iv.html) August 5-9, 1988, University of Manchester, UK. pp. 13-34

[Benyon](https://www.interaction-design.org/references/authors/david_benyon.html), David and [Macaulay](https://www.interaction-design.org/references/authors/catriona_macaulay.html), Catriona (2002): *Scenarios and the HCI-SE design problem*. In [Interacting with Computers](https://www.interaction-design.org/references/periodicals/interacting_with_computers.html), 14 (4) pp. 397-405
[Boehm](https://www.interaction-design.org/references/authors/barry_w__boehm.html), Barry W. (1981a): *Software Engineering Economics.* Prentice Hall
[Boehm](https://www.interaction-design.org/references/authors/barry_w_boehm.html), Barry W (1981b): *Software Engineering Economics*. In [IEEE Transactions on Software Engineering](https://www.interaction-design.org/references/periodicals/ieee_transactions_on_software_engineering.html), 16 (1) pp. 4-21
[Boehm](https://www.interaction-design.org/references/authors/barry_boehm.html), Barry, [Bose](https://www.interaction-design.org/references/authors/prasanta_bose.html), Prasanta, [Horowitz](https://www.interaction-design.org/references/authors/ellis_horowitz.html), Ellis and [Lee](https://www.interaction-design.org/references/authors/ming-june_lee.html), Ming-June (1994): *Software requirements as negotiated win conditions*. In [Proceedings of IEEE International Conference on Requirements Engineering](https://www.interaction-design.org/references/periodicals/proceedings_of_ieee_international_conference_on_requirements_engineering.html), pp. 74-83

[Borchers](https://www.interaction-design.org/references/authors/jan_o__borchers.html), Jan O. (2001): *A Pattern Approach to Interaction Design.* John Wiley and Sons
[Borchers](https://www.interaction-design.org/references/authors/jan_o__borchers.html), Jan O. (2000): A Pattern Approach to Interaction Design. In: [Proceedings of DIS00: Designing Interactive Systems: Processes, Practices, Methods, & Techniques](https://www.interaction-design.org/references/conferences/proceedings_of_dis00-_designing_interactive_systems-_processes%2C_practices%2C_methods%2C_%26_techniques.html) 2000. pp. 369-378
[Bubenko](https://www.interaction-design.org/references/authors/janis_a__bubenko.html), Janis A. and [Kirikova](https://www.interaction-design.org/references/authors/marite_kirikova.html), Marite (1994). *Enterprise Modelling: Improving the Quality of Requirements Specifications*.
[Callele](https://www.interaction-design.org/references/authors/david_callele.html), David, [Neufeld](https://www.interaction-design.org/references/authors/eric_neufeld.html), Eric and [Schneider](https://www.interaction-design.org/references/authors/kevin_schneider.html), Kevin (2006): Emotional Requirements in Video Games. In: [14th IEEE International Conference on Requirements Engineering RE 2006](https://www.interaction-design.org/references/conferences/14th_ieee_international_conference_on_requirements_engineering_re_2006.html) 11-15 September, 2006, Minneapolis/St.Paul, Minnesota, USA. pp. 292-295

[Carroll](https://www.interaction-design.org/references/authors/john_m__carroll.html), John M. (2002): *Making use is more than a matter of task analysis*. In [Interacting with Computers](https://www.interaction-design.org/references/periodicals/interacting_with_computers.html), 14 (5) pp. 619-627
[Carroll](https://www.interaction-design.org/references/authors/john_m__carroll.html), John M. (2000): *Making Use: Scenario-Based Design of Human-Computer Interactions.* MIT Press
[Carroll](https://www.interaction-design.org/references/authors/john_m__carroll.html), John M. (ed.) (1995): *Scenario-Based Design: Envisioning Work and Technology in System Development.*John Wiley and Sons
[Carroll](https://www.interaction-design.org/references/authors/john_m__carroll.html), John M., [Singley](https://www.interaction-design.org/references/authors/mark_k__singley.html), Mark K. and [Rosson](https://www.interaction-design.org/references/authors/mary_beth_rosson.html), Mary Beth (1992): *Integrating Theory Development with Design Evaluation*. In [Behaviour and Information Technology](https://www.interaction-design.org/references/periodicals/behaviour_and_information_technology.html), 11 (5) pp. 247-255

[Carroll](https://www.interaction-design.org/references/authors/john_m__carroll.html), John M., [Alpert](https://www.interaction-design.org/references/authors/sherman_r__alpert.html), Sherman R., [Karat](https://www.interaction-design.org/references/authors/john_karat.html), John, [Deusen](https://www.interaction-design.org/references/authors/mary_s__van_deusen.html), Mary S. Van and [Rosson](https://www.interaction-design.org/references/authors/mary_beth_rosson.html), Mary Beth (1994): Raison d'Etre: capturing [design history](https://www.interaction-design.org/literature/topics/design-history) and rationale in mutimedia narratives. In: [Plaisant](https://www.interaction-design.org/references/authors/catherine_plaisant.html), Catherine (ed.) [Conference on Human Factors in Computing Systems, CHI 1994, Boston, Massachusetts, USA, April 24-28, 1994, Conference Companion](https://www.interaction-design.org/references/conferences/conference_on_human_factors_in_computing_systems%2C_chi_1994%2C_boston%2C_massachusetts%2C_usa%2C_april_24-28%2C_1994%2C_conference_companion.html) 1994. p. 213
[Checkland](https://www.interaction-design.org/references/authors/peter_checkland.html), Peter (1981): *Systems Thinking, Systems Practice: Includes a 30-Year Retrospective.* Wiley
[Cockburn](https://www.interaction-design.org/references/authors/alistair_cockburn.html), Alistair (2000): *Writing Effective Use Cases.* Addison-Wesley Professional

[Cockton](https://www.interaction-design.org/references/authors/gilbert_cockton.html), Gilbert (2009): Getting there: six meta-principles and interaction design. In: [Proceedings of ACM CHI 2009 Conference on Human Factors in Computing Systems](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2009_conference_on_human_factors_in_computing_systems.html) 2009. pp. 2223-2232
[Conklin](https://www.interaction-design.org/references/authors/jeff_conklin.html), Jeff and [Begeman](https://www.interaction-design.org/references/authors/michael_l__begeman.html), Michael L. (1988): gIBIS: A Hypertext Tool for Exploratory Policy Discussion. In: [Greif](https://www.interaction-design.org/references/authors/irene_greif.html), Irene (ed.) [Proceedings of the 1988 ACM conference on Computer-supported cooperative work](https://www.interaction-design.org/references/conferences/proceedings_of_the_1988_acm_conference_on_computer-supported_cooperative_work.html) September 26 - 28, 1988, Portland, Oregon, United States. pp. 140-152
[Conklin](https://www.interaction-design.org/references/authors/jeff_conklin.html), Jeff and [Begeman](https://www.interaction-design.org/references/authors/michael_l__begeman.html), Michael L. (1988a): *gIBIS: A Hypertext Tool for Exploratory Policy Discussion*. In [ACM Transactions on Information Systems](https://www.interaction-design.org/references/periodicals/acm_transactions_on_information_systems.html), 6 (4) pp. 303-331

[Dardenne](https://www.interaction-design.org/references/authors/anne_dardenne.html), Anne, [Lamsweerde](https://www.interaction-design.org/references/authors/axel_van_lamsweerde.html), Axel van and [Fickas](https://www.interaction-design.org/references/authors/stephen_fickas.html), Stephen (1993): *Goal-directed requirements acquisition*. In[Science of Computer Programming](https://www.interaction-design.org/references/periodicals/science_of_computer_programming.html), 20 (1) pp. 3-50
[Davenport](https://www.interaction-design.org/references/authors/thomas_h__davenport.html), Thomas H. (1992): *Process *[*Innovation*](https://www.interaction-design.org/literature/topics/innovation)*: Reengineering Work Through Information Technology.* Harvard Business Press
[Dearden](https://www.interaction-design.org/references/authors/andy_dearden.html), Andy, [Harrison](https://www.interaction-design.org/references/authors/michael_harrison.html), Michael and [Wright](https://www.interaction-design.org/references/authors/peter_c__wright.html), Peter C. (2000): *Allocation of Function: Scenarios, Context and the Economics of Effort*. In [International Journal of Human-Computer Studies](https://www.interaction-design.org/references/periodicals/international_journal_of_human-computer_studies.html), 52 (2) pp. 289-318

[Diaper](https://www.interaction-design.org/references/authors/dan_diaper.html), Dan (2001): *Task analysis for knowledge descriptions (TAKD): a requiem for a method*. In [Behaviour and Information Technology](https://www.interaction-design.org/references/periodicals/behaviour_and_information_technology.html), 20 (3) pp. 199-212
[Diaper](https://www.interaction-design.org/references/authors/dan_diaper.html), Dan and [Johnson](https://www.interaction-design.org/references/authors/peter_johnson.html), Peter (1989): Task analysis for knowledge descriptions: Theory and application in training. In: [Long](https://www.interaction-design.org/references/authors/john_long.html), John and [Whitefield](https://www.interaction-design.org/references/authors/a__whitefield.html),
 A. (eds.). "Cognitive Ergonomics and Human-Computer Interaction 
(Cambridge Series on Human-Computer Interaction)". Cambridge University 
Press

[Djajadiningrat](https://www.interaction-design.org/references/authors/j__p__djajadiningrat.html), J. P., [Gaver](https://www.interaction-design.org/references/authors/william_w__gaver.html), William W. and [Fres](https://www.interaction-design.org/references/authors/j__w__fres.html), J. W. (2000): Interaction Relabelling and Extreme Characters: Methods for Exploring [Aesthetic](https://www.interaction-design.org/literature/topics/aesthetics) Interactions. In: [Proceedings of DIS00: Designing Interactive Systems: Processes, Practices, Methods, & Techniques](https://www.interaction-design.org/references/conferences/proceedings_of_dis00-_designing_interactive_systems-_processes%2C_practices%2C_methods%2C_%26_techniques.html) 2000. pp. 66-71
[Eason](https://www.interaction-design.org/references/authors/k__d__eason.html), K. D., [Harker](https://www.interaction-design.org/references/authors/s__d__p__harker.html), S. D. P. and [Olphert](https://www.interaction-design.org/references/authors/c__w__olphert.html), C. W. (1996): *Representing *[*socio-technical systems*](https://www.interaction-design.org/literature/topics/socio-technical-systems)* options in the development of new forms of work organisation*. In [European Journal of Work and Organisational Psychology](https://www.interaction-design.org/references/periodicals/european_journal_of_work_and_organisational_psychology.html),

[Eden](https://www.interaction-design.org/references/authors/colin_eden.html), Colin (1988): *Cognitive mapping*. In [European Journal of Operational Research](https://www.interaction-design.org/references/periodicals/european_journal_of_operational_research.html), 36 (1) pp. 1-13
[Fenton](https://www.interaction-design.org/references/authors/norman_e__fenton.html), Norman E. (1995): The role of measurement in software safety assessment. In: [12th Annual CSR/ENCRESS Conference on Software Safety Case](https://www.interaction-design.org/references/conferences/12th_annual_csr%2Fencress_conference_on_software_safety_case.html) 13 Sept, 1995, Bruges, Belgium.
[Finkelstein](https://www.interaction-design.org/references/authors/anthony_finkelstein.html), Anthony, [Harman](https://www.interaction-design.org/references/authors/mark_harman.html), Mark, [Mansouri](https://www.interaction-design.org/references/authors/s__afshin_mansouri.html), S. Afshin, [Ren](https://www.interaction-design.org/references/authors/jian_ren.html), Jian and [Zhang](https://www.interaction-design.org/references/authors/yuanyuan_zhang.html), Yuanyuan (2008): "Fairness Analysis" in Requirements Assignments. In: [Proceedings of the 2008 16th IEEE International Requirements Engineering Conference](https://www.interaction-design.org/references/conferences/proceedings_of_the_2008_16th_ieee_international_requirements_engineering_conference.html) 2008. pp. 115-124

[Gamma](https://www.interaction-design.org/references/authors/erich_gamma.html), Erich, [Helm](https://www.interaction-design.org/references/authors/richard_helm.html), Richard, [Johnson](https://www.interaction-design.org/references/authors/ralph_johnson.html), Ralph and [Vlissides](https://www.interaction-design.org/references/authors/john_vlissides.html), John (1995): *Design Patterns: Elements of reusable object-oriented software.* Addison-Wesley Publishing
[Gause](https://www.interaction-design.org/references/authors/donald_c__gause.html), Donald C. and [Weinberg](https://www.interaction-design.org/references/authors/gerald_m__weinberg.html), Gerald M. (1989): *Exploring Requirements: Quality Before Design.* Dorset House Publishing Company, Incorporated
[Goguen](https://www.interaction-design.org/references/authors/joseph_a__goguen.html), Joseph A. and [Linde](https://www.interaction-design.org/references/authors/charlotte_linde.html), Charlotte (1993): *Techniques for requirements elicitation*. In [1993 Proceedings of the IEEE International Symposium on Requirements Engineering](https://www.interaction-design.org/references/periodicals/1993_proceedings_of_the_ieee_international_symposium_on_requirements_engineering.html), pp. 152-164

[Gould](https://www.interaction-design.org/references/authors/john_d__gould.html), John D. (1987): How to Design Usable Systems. In: [Bullinger](https://www.interaction-design.org/references/authors/hans-jorg_bullinger.html), Hans-Jorg and [Shackel](https://www.interaction-design.org/references/authors/brian_shackel.html), Brian (eds.)[INTERACT 87 - 2nd IFIP International Conference on Human-Computer Interaction](https://www.interaction-design.org/references/conferences/interact_87_-_2nd_ifip_international_conference_on_human-computer_interaction.html) September 1-4, 1987, Stuttgart, Germany. pp. xxxv-xli
[Graham](https://www.interaction-design.org/references/authors/ian_m__graham.html), Ian M. (1996): *Task scripts, use cases and scenarios in object oriented analysis*. In [Object Oriented Systems](https://www.interaction-design.org/references/periodicals/object_oriented_systems.html), 3 pp. 123-142
[Graham](https://www.interaction-design.org/references/authors/ian_graham.html), Ian (): Task scripts, use cases and scenarios in objectoriented analysis. In: [Object-Oriented Systems](https://www.interaction-design.org/references/conferences/object-oriented_systems.html) .

[Guindon](https://www.interaction-design.org/references/authors/raymonde_guindon.html), Raymonde and [Curtis](https://www.interaction-design.org/references/authors/bill_curtis.html), Bill (1988): Control of Cognitive Processes During Software Design: What Tools Are Needed?. In: [Soloway](https://www.interaction-design.org/references/authors/elliot_soloway.html), Elliot, [Frye](https://www.interaction-design.org/references/authors/douglas_frye.html), Douglas and [Sheppard](https://www.interaction-design.org/references/authors/sylvia_b__sheppard.html), Sylvia B. (eds.) [Proceedings of the ACM CHI 88 Human Factors in Computing Systems Conference](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_88_human_factors_in_computing_systems_conference.html) June 15-19, 1988, Washington, DC, USA. pp. 263-268
[Hassenzahl](https://www.interaction-design.org/references/authors/marc_hassenzahl.html), Marc (2010): *Experience Design: Technology for All the Right Reasons.* Morgan and Claypool Publishers
[Hauser](https://www.interaction-design.org/references/authors/john_r__hauser.html), John R. and [Clausing](https://www.interaction-design.org/references/authors/don_clausing.html), Don (1988): *The House of Quality*. In [Harvard Business Review](https://www.interaction-design.org/references/periodicals/harvard_business_review.html), 66 (3) pp. 63-73

[Holland](https://www.interaction-design.org/references/authors/christopher_p__holland.html), Christopher P. (1995): *Cooperative supply chain management: the impact of interorganizational information systems*. In [Journal of Strategic Information Systems](https://www.interaction-design.org/references/periodicals/journal_of_strategic_information_systems.html), 4 (2) pp. 117-133
[Hughes](https://www.interaction-design.org/references/authors/john_a__hughes.html), John A., [O'Brien](https://www.interaction-design.org/references/authors/jon_o%27brien.html), Jon, [Rodden](https://www.interaction-design.org/references/authors/tom_rodden.html), Tom, [Rouncefield](https://www.interaction-design.org/references/authors/mark_rouncefield.html), Mark and [Sommerville](https://www.interaction-design.org/references/authors/ian_sommerville.html), Ian (1995): Presenting ethnography in the requirements process. In: [Second IEEE International Symposium on Requirements Engineering 1995](https://www.interaction-design.org/references/conferences/second_ieee_international_symposium_on_requirements_engineering_1995.html) March 27 - 29, 1995, York, England. pp. 27-39
[Jackson](https://www.interaction-design.org/references/authors/michael_jackson.html), Michael (2000): *Problem Frames: Analysing & Structuring Software Development Problems.* Addison-Wesley Professional

[Jackson](https://www.interaction-design.org/references/authors/michael_jackson.html), Michael (2001): *Problem Frames: Analysing & Structuring Software Development Problems.* Addison-Wesley Professional
[Jackson](https://www.interaction-design.org/references/authors/michael_jackson.html), Michael and [Zave](https://www.interaction-design.org/references/authors/pamela_zave.html), Pamela (1993): *Domain Descriptions*. In [RE](https://www.interaction-design.org/references/periodicals/re.html), pp. 56-64
[Jacobson](https://www.interaction-design.org/references/authors/ivar_jacobson.html), Ivar, [Christerson](https://www.interaction-design.org/references/authors/magnus_christerson.html), Magnus, [Jonsson](https://www.interaction-design.org/references/authors/patrik_jonsson.html), Patrik and [Övergaard](https://www.interaction-design.org/references/authors/gunnar_%D6vergaard.html), Gunnar (1992): *Object-oriented software engineering: A use-case driven approach.* Reading, MA, Addison-Wesley Publishing

[Johnson](https://www.interaction-design.org/references/authors/peter_johnson.html), Peter, [Johnson](https://www.interaction-design.org/references/authors/hilary_johnson.html), Hilary, [Waddington](https://www.interaction-design.org/references/authors/ray_waddington.html), Ray and [Shouls](https://www.interaction-design.org/references/authors/alan_shouls.html), Alan (1988): Task-Related Knowledge Structures: Analysis, Modelling and Application. In: [Jones](https://www.interaction-design.org/references/authors/dylan_m__jones.html), Dylan M. and [Winder](https://www.interaction-design.org/references/authors/r__winder.html), R. (eds.) [Proceedings
 of the Fourth Conference of the British Computer Society Human Computer
 Interaction Specialist Group - People and Computers IV](https://www.interaction-design.org/references/conferences/proceedings_of_the_fourth_conference_of_the_british_computer_society_human_computer_interaction_specialist_group_-_people_and_computers_iv.html) August 5-9, 1988, University of Manchester, UK. pp. 35-62

[Johnson](https://www.interaction-design.org/references/authors/w__lewis_johnson.html), W. Lewis, [Feather](https://www.interaction-design.org/references/authors/martin_s__feather.html), Martin S. and [Harris](https://www.interaction-design.org/references/authors/david_r__harris.html), David R. (1992): *Representation and Presentation of Requirements Knowledge*. In [IEEE Trans. Software Eng.](https://www.interaction-design.org/references/periodicals/ieee_trans__software_eng-dot-.html), 18 (10) pp. 853-869
[Jureta](https://www.interaction-design.org/references/authors/ivan_jureta.html), Ivan, [Mylopoulos](https://www.interaction-design.org/references/authors/john_mylopoulos.html), John and [Faulkner](https://www.interaction-design.org/references/authors/st%E9phane_faulkner.html), Stéphane (2008): Revisiting the Core Ontology and Problem in Requirements Engineering. In: [16th IEEE International Requirements Engineering Conference RE 2008](https://www.interaction-design.org/references/conferences/16th_ieee_international_requirements_engineering_conference_re_2008.html) 8-12 September, 2008, Barcelona, Catalunya, Spain. pp. 71-80

[Kaindl](https://www.interaction-design.org/references/authors/hermann_kaindl.html), Hermann (1995): An integration of scenarios with their purposes in task modeling. In: [Proceedings of the 1st conference on Designing interactive systems processes, practices, methods, and techniques](https://www.interaction-design.org/references/conferences/proceedings_of_the_1st_conference_on_designing_interactive_systems_processes%2C_practices%2C_methods%2C_and_techniques.html) 1995. pp. 227-235
[Kethers](https://www.interaction-design.org/references/authors/stefanie_kethers.html), Stefanie and [Jacobs](https://www.interaction-design.org/references/authors/stephan_jacobs.html), Stephan (1994): Improving Communication and Decision Making within Quality Function Deployment. In: [First International Conference on Concurrent Engineering, Research, and Application](https://www.interaction-design.org/references/conferences/first_international_conference_on_concurrent_engineering%2C_research%2C_and_application.html)1994.
[Kuuti](https://www.interaction-design.org/references/authors/kari_kuuti.html), Kari (1995): Workprocess: Scenarios as a preliminary vocabulary. In: [Carroll](https://www.interaction-design.org/references/authors/john_m__carroll.html), John M. (ed.). "Scenario-Based Design: Envisioning Work and Technology in System Development". John Wiley and Sonspp. 19-36

[Kyng](https://www.interaction-design.org/references/authors/morten_kyng.html), Morten (1995): Creating contexts for design. In: [Carroll](https://www.interaction-design.org/references/authors/john_m__carroll.html), John M. (ed.). "Scenario-Based Design: Envisioning Work and Technology in System Development". John Wiley and Sonspp. 85-108
[Lam](https://www.interaction-design.org/references/authors/w__lam.html), W., [McDermid](https://www.interaction-design.org/references/authors/john_a__mcdermid.html), John A. and [Vickers](https://www.interaction-design.org/references/authors/andrew_vickers.html), Andrew (1997b): *Ten Steps Towards Systematic Requirements Reuse*. In[Requir. Eng.](https://www.interaction-design.org/references/periodicals/requir__eng-dot-.html), 2 (2) pp. 102-113
[Lam](https://www.interaction-design.org/references/authors/w__lam.html), W., [McDermid](https://www.interaction-design.org/references/authors/john_a__mcdermid.html), John A. and [Vickers](https://www.interaction-design.org/references/authors/andrew_vickers.html), Andrew (1997): Ten Steps Towards Systematic Requirements Reuse. In:[3rd IEEE International Symposium on Requirements Engineering RE97](https://www.interaction-design.org/references/conferences/3rd_ieee_international_symposium_on_requirements_engineering_re97.html) January 5-8, 1997, Annapolis, MD, USA. pp. 6-15

[Lamsweerde](https://www.interaction-design.org/references/authors/axel_van_lamsweerde.html), Axel van (2009): *Requirements Engineering: From System Goals to UML Models to Software Specifications.* Wiley
[Lamsweerde](https://www.interaction-design.org/references/authors/axel_van_lamsweerde.html), Axel van and [Letier](https://www.interaction-design.org/references/authors/emmanuel_letier.html), Emmanuel (2000): *Handling Obstacles in Goal-Oriented Requirements Engineering*. In [IEEE Trans. Software Eng.](https://www.interaction-design.org/references/periodicals/ieee_trans__software_eng-dot-.html), 26 (10) pp. 978-1005
[Lamsweerde](https://www.interaction-design.org/references/authors/axel_van_lamsweerde.html), Axel van, [Darimont](https://www.interaction-design.org/references/authors/r__darimont.html), R. and [Massonet](https://www.interaction-design.org/references/authors/p__massonet.html), P. (1995): *Goal-directed elaboration of requirements for a meeting scheduler: problems and lessons learnt*. In [RE](https://www.interaction-design.org/references/periodicals/re.html), pp. 194-203
[Luff](https://www.interaction-design.org/references/authors/paul_luff.html), Paul, [Jirotka](https://www.interaction-design.org/references/authors/marina_jirotka.html), Marina, [Heath](https://www.interaction-design.org/references/authors/christian_c__heath.html), Christian C. and [Greatbatch](https://www.interaction-design.org/references/authors/david_greatbatch.html),

 David (1993): Tasks and social interaction: the relevance of 
naturalistic analyses of conduct for requirements engineering. In: [Proceedings of IEEE International Symposium on Requirements Engineering 1993](https://www.interaction-design.org/references/conferences/proceedings_of_ieee_international_symposium_on_requirements_engineering_1993.html) 1993, San Diego, CA , USA . pp. 187-190
[Macaulay](https://www.interaction-design.org/references/authors/l__macaulay.html), L. (1993): Requirements capture as a cooperative activity. In: [Proceedings of IEEE International Symposium on Requirements Engineering 1993](https://www.interaction-design.org/references/conferences/proceedings_of_ieee_international_symposium_on_requirements_engineering_1993.html) 1993, San Diego, CA , USA . pp. 174-181
[MacLean](https://www.interaction-design.org/references/authors/allan_maclean.html), Allan, [Young](https://www.interaction-design.org/references/authors/richard_m__young.html), Richard M., [Bellotti](https://www.interaction-design.org/references/authors/victoria_bellotti.html), Victoria and [Moran](https://www.interaction-design.org/references/authors/thomas_p__moran.html), Thomas P. (1991): *Questions, Options, and Criteria: Elements of Design Space Analysis*. In [Human-Computer Interaction](https://www.interaction-design.org/references/periodicals/human-computer_interaction.html), 6 (3) pp. 201-250

[Maiden](https://www.interaction-design.org/references/authors/n__a__m__maiden.html), N. A. M. and [Ncube](https://www.interaction-design.org/references/authors/c__ncube.html), C. (1998): *Acquiring requirements for Commercial Off-The-Shelf package selection*. In[IEEE Software](https://www.interaction-design.org/references/periodicals/ieee_software.html), 15 (2) pp. 46-56
[Maiden](https://www.interaction-design.org/references/authors/n__a__m__maiden.html), N. A. M. and [Rugg](https://www.interaction-design.org/references/authors/g__rugg.html), G. (1994): Knowledge acquisition techniques for requirements engineering. In:[Proceedings of the Workshop on Requirements Elicitation for System Specification](https://www.interaction-design.org/references/conferences/proceedings_of_the_workshop_on_requirements_elicitation_for_system_specification.html) 12-14 July, 1994, Keele, University of Keele.
[Maiden](https://www.interaction-design.org/references/authors/n__a__m__maiden.html), N. A. M. and [Sutcliffe](https://www.interaction-design.org/references/authors/alistair_g__sutcliffe.html), Alistair G. (1994): Requirements critiquing using domain abstractions. In:[Requirements Engineering 1994 - Proceedings of the First International Conference on Requirements Engineering](https://www.interaction-design.org/references/conferences/requirements_engineering_1994_-_proceedings_of_the_first_international_conference_on_requirements_engineering.html) 1994, Colorado Springs, CO , USA. pp. 184-193

[Monk](https://www.interaction-design.org/references/authors/andrew_monk.html), Andrew, [Wright](https://www.interaction-design.org/references/authors/peter_wright.html), Peter, [Haber](https://www.interaction-design.org/references/authors/jeanne_haber.html), Jeanne and [Davenport](https://www.interaction-design.org/references/authors/lora_davenport.html), Lora (1993): *Improving Your Human-Computer Interface: A Practical Technique (Bcs Practitioner).* Prentice Hall
[Mylopoulos](https://www.interaction-design.org/references/authors/john_mylopoulos.html), John, [Chung](https://www.interaction-design.org/references/authors/lawrence_chung.html), Lawrence and [Nixon](https://www.interaction-design.org/references/authors/brian_nixon.html), Brian (1992): *Representing and using nonfunctional requirements: a process-oriented approach*. In [IEEE Transactions on Software Engineering](https://www.interaction-design.org/references/periodicals/ieee_transactions_on_software_engineering.html), 18 (6) pp. 483-497

[Mylopoulos](https://www.interaction-design.org/references/authors/john_mylopoulos.html), John, [Chung](https://www.interaction-design.org/references/authors/lawrence_chung.html), Lawrence and [Yu](https://www.interaction-design.org/references/authors/eric_s__k__yu.html), Eric S. K. (1999): *From Object-Oriented to Goal-Oriented Requirements Analysis*. In [Communications of the ACM](https://www.interaction-design.org/references/periodicals/communications_of_the_acm.html), 42 (1) pp. 31-37
[Norman](https://www.interaction-design.org/references/authors/donald_a__norman.html), Donald A. (2004): [*Emotional Design*](https://www.interaction-design.org/literature/topics/emotional-design)*: Why We Love (Or Hate) Everyday Things.* Basic Books
[Nuseibeh](https://www.interaction-design.org/references/authors/bashar_nuseibeh.html), Bashar and [Easterbrook](https://www.interaction-design.org/references/authors/steve_m__easterbrook.html), Steve M. (2000): Requirements engineering: a roadmap. In: [ICSE - Future of SE Track 2000](https://www.interaction-design.org/references/conferences/icse_-_future_of_se_track_2000.html) 2000. pp. 35-46
[Pohl](https://www.interaction-design.org/references/authors/klaus_pohl.html), Klaus (1996): *Process-Centered Requirements Engineering (Advanced Software Development Series).*Research Studies Press

[Porter](https://www.interaction-design.org/references/authors/michael_e__porter.html), Michael E. (1980): *Competitive Strategy: Techniques for Analyzing Industries and Competitors.* Free Press
[Potts](https://www.interaction-design.org/references/authors/colin_potts.html), Colin (1999): ScenIC: A Strategy for Inquiry-Driven Requirements Determination. In: [4th IEEE International Symposium on Requirements Engineering RE 99](https://www.interaction-design.org/references/conferences/4th_ieee_international_symposium_on_requirements_engineering_re_99.html) 7-11 June, 1999, Limerick, Ireland. pp. 58-65
[Potts](https://www.interaction-design.org/references/authors/colin_potts.html), Colin, [Takahashi](https://www.interaction-design.org/references/authors/k__takahashi.html), K. and [Anton](https://www.interaction-design.org/references/authors/a__i__anton.html), A. I. (1994): *Inquiry-based requirements analysis*. In [IEEE Software](https://www.interaction-design.org/references/periodicals/ieee_software.html), 11 (2) pp. 21-32

[Potts](https://www.interaction-design.org/references/authors/colin_potts.html), Colin, [Takahashi](https://www.interaction-design.org/references/authors/kenji_takahashi.html), Kenji, [Smith](https://www.interaction-design.org/references/authors/jeffrey_d__smith.html), Jeffrey D. and [Ota](https://www.interaction-design.org/references/authors/kenji_ota.html), Kenji (1995): An evaluation of inquiry-based requirements analysis for an Internet service. 1995. pp. 172-180
[Robertson](https://www.interaction-design.org/references/authors/suzanne_robertson.html), Suzanne and [Robertson](https://www.interaction-design.org/references/authors/james_robertson.html), James (1999): *Mastering the Requirements Process.* Addison-Wesley Professional
[Rockart](https://www.interaction-design.org/references/authors/j__f__rockart.html), J. F. and [Short](https://www.interaction-design.org/references/authors/j__e__short.html), J. E. (1991): The networked organisation and the management of interdependence. In:[Morton](https://www.interaction-design.org/references/authors/michael_s__scott_morton.html),
 Michael S. Scott (ed.). "The Corporation of the 1990s: Information 
Technology and Organizational Transformation". Oxford University Press, 
USA
[Rodden](https://www.interaction-design.org/references/authors/tom_rodden.html), Tom (1999): *Human
 factors in requirements engineering: - A survey of human sciences 
literature relevant to the improvement of dependable systems development

 processes*. In [Interacting with Computers](https://www.interaction-design.org/references/periodicals/interacting_with_computers.html), 11 (6) pp. 665-698
[Rodriguez](https://www.interaction-design.org/references/authors/f__gamboa_rodriguez.html), F. Gamboa and [Scapin](https://www.interaction-design.org/references/authors/d__l__scapin.html), D. L. (1997): Editing MAD* task description for specifying interfaces, at both semantic and presentation level. In: [Design, specification and verification of interactive systems 1997](https://www.interaction-design.org/references/conferences/design%2C_specification_and_verification_of_interactive_systems_1997.html) 1997.

[Rolland](https://www.interaction-design.org/references/authors/c__rolland.html), C., [Achour](https://www.interaction-design.org/references/authors/c__ben_achour.html), C. Ben, [Cauvet](https://www.interaction-design.org/references/authors/c__cauvet.html), C., [Ralyté](https://www.interaction-design.org/references/authors/j__ralyt%E9.html), J., [Sutcliffe](https://www.interaction-design.org/references/authors/alistair_g__sutcliffe.html), Alistair G., [Maiden](https://www.interaction-design.org/references/authors/n__maiden.html), N., [Jarke](https://www.interaction-design.org/references/authors/m__jarke.html), M., [Haumer](https://www.interaction-design.org/references/authors/p__haumer.html), P., [Pohl](https://www.interaction-design.org/references/authors/klaus_pohl.html), Klaus, [Dubois](https://www.interaction-design.org/references/authors/e__dubois.html), E. and [Heymans](https://www.interaction-design.org/references/authors/p__heymans.html), P. (1998): *A proposal for a scenario classification framework*. In [Requirements Engineering](https://www.interaction-design.org/references/periodicals/requirements_engineering.html), 3 (1) pp. 23-47

[Sawyer](https://www.interaction-design.org/references/authors/peter_sawyer.html), Peter, [Bencomo](https://www.interaction-design.org/references/authors/nelly_bencomo.html), Nelly, [Whittle](https://www.interaction-design.org/references/authors/jon_whittle.html), Jon, [Letier](https://www.interaction-design.org/references/authors/emmanuel_letier.html), Emmanuel and [Finkelstein](https://www.interaction-design.org/references/authors/anthony_finkelstein.html), Anthony (2010): Requirements-Aware Systems: A Research Agenda for RE for Self-adaptive Systems. In: [RE
 2010, 18th IEEE International Requirements Engineering Conference, 
Sydney, New South Wales, Australia, September 27 - October 1, 2010](https://www.interaction-design.org/references/conferences/re_2010%2C_18th_ieee_international_requirements_engineering_conference%2C_sydney%2C_new_south_wales%2C_australia%2C_september_27_-_october_1%2C_2010.html)2010. pp. 95-103
[Shum](https://www.interaction-design.org/references/authors/s__buckingham_shum.html), S. Buckingham (1996): Analyzing the usability of a design rationale notation. In: [Moran](https://www.interaction-design.org/references/authors/thomas_p__moran.html), Thomas P. and[Carroll](https://www.interaction-design.org/references/authors/john_m__carroll.html), John M. (eds.). "Design Rationale: Concepts, Techniques, and Use (Computers, Cognition, and Work Series)". CRC Press

[Stapleton](https://www.interaction-design.org/references/authors/jennifer_stapleton.html), Jennifer and [Constable](https://www.interaction-design.org/references/authors/peter_constable.html), Peter (1997): *DSDM: Dynamic Systems Development Method: The Method in Practice.* Addison-Wesley Professional
[Sutcliffe](https://www.interaction-design.org/references/authors/alistair_g__sutcliffe.html), Alistair G. (2002c): *The Domain Theory: Patterns for Knowledge and Software Reuse.* CRC Press
[Sutcliffe](https://www.interaction-design.org/references/authors/alistair_g__sutcliffe.html), Alistair G. (1997): *Task-Related Information Analysis*. In [International Journal of Human-Computer Studies](https://www.interaction-design.org/references/periodicals/international_journal_of_human-computer_studies.html), 47 (2) pp. 223-257
[Sutcliffe](https://www.interaction-design.org/references/authors/alistair_g__sutcliffe.html), Alistair G. (1995): Requirements Rationales: Integrating Approaches to Requirement Analysis. In:[Proceedings of DIS95: Designing Interactive Systems: Processes, Practices, Methods, & Techniques](https://www.interaction-design.org/references/conferences/proceedings_of_dis95-_designing_interactive_systems-_processes%2C_practices%2C_methods%2C_%26_techniques.html) 1995. pp. 33-42

[Sutcliffe](https://www.interaction-design.org/references/authors/alistair_g__sutcliffe.html), Alistair G. (2000): Bridging the communications gap: developing a Lingua Franca for software developers and users. In: [Actes du XVIIIe Congres 2000](https://www.interaction-design.org/references/conferences/actes_du_xviiie_congres_2000.html) 2000, Toulouse, France. pp. 13-32
[Sutcliffe](https://www.interaction-design.org/references/authors/aiistair_sutcliffe.html), Aiistair (2009): *Designing for User Engagement: Aesthetic and Attractive User Interfaces*. In [Synthesis Lectures on HumanCentered Informatics](https://www.interaction-design.org/references/periodicals/synthesis_lectures_on_humancentered_informatics.html), 2 (1) pp. 1-55
[Sutcliffe](https://www.interaction-design.org/references/authors/alistair_g__sutcliffe.html), Alistair G. (2002): Modelling collaboration in loosely coupled inter-organisational relationships. In: [Systems engineering for business process change](https://www.interaction-design.org/references/conferences/systems_engineering_for_business_process_change.html) 2002. pp. 347-366
[Sutcliffe](https://www.interaction-design.org/references/authors/alistair_g__sutcliffe.html), Alistair G. (2000a): *On the Effective Use and Reuse of HCI Knowledge*. In [ACM Transactions on Computer-Human Interaction](https://www.interaction-design.org/references/periodicals/acm_transactions_on_computer-human_interaction.html), 7 (2) pp. 197-221

[Sutcliffe](https://www.interaction-design.org/references/authors/alistair_g__sutcliffe.html), Alistair G. (2002a): *User-Centred Requirements Engineering.* Springer
[Sutcliffe](https://www.interaction-design.org/references/authors/alistair_g__sutcliffe.html), Alistair G. and [Carroll](https://www.interaction-design.org/references/authors/john_m__carroll.html), John M. (1998): Generalizing Claims and Reuse of HCI Knowledge. In: [Johnson](https://www.interaction-design.org/references/authors/hilary_johnson.html), Hilary, [Nigay](https://www.interaction-design.org/references/authors/laurence_nigay.html), Laurence and [Roast](https://www.interaction-design.org/references/authors/c__r__roast.html), C. R. (eds.) [Proceedings
 of the Thirteenth Conference of the British Computer Society Human 
Computer Interaction Specialist Group - People and Computers XIII](https://www.interaction-design.org/references/conferences/proceedings_of_the_thirteenth_conference_of_the_british_computer_society_human_computer_interaction_specialist_group_-_people_and_computers_xiii.html) August 1-4, 1998, Sheffield, UK. pp. 159-176

[Sutcliffe](https://www.interaction-design.org/references/authors/alistair_g__sutcliffe.html), Alistair G. and [Ryan](https://www.interaction-design.org/references/authors/michele_ryan.html), Michele (1997): Assessing the usability and efficiency of Design Rationale. In: [Howard](https://www.interaction-design.org/references/authors/steve_howard.html), Steve, [Hammond](https://www.interaction-design.org/references/authors/judy_hammond.html), Judy and [Lindgaard](https://www.interaction-design.org/references/authors/gitte_lindgaard.html), Gitte (eds.) [Human-Computer
 Interaction, INTERACT 97, IFIP TC13 Interantional Conference on 
Human-Computer Interaction, 14th-18th July 1997, Sydney, Australia](https://www.interaction-design.org/references/conferences/human-computer_interaction%2C_interact_97%2C_ifip_tc13_interantional_conference_on_human-computer_interaction%2C_14th-18th_july_1997%2C_sydney%2C_australia.html) 1997. pp. 148-155

[Sutcliffe](https://www.interaction-design.org/references/authors/alistair_g__sutcliffe.html), Alistair G., [Fickas](https://www.interaction-design.org/references/authors/stephen_fickas.html), Stephen and [Sohlberg](https://www.interaction-design.org/references/authors/mckay_moore_sohlberg.html), McKay Moore (2005): Personal and Contextual Requirements Engineering. In: [13th IEEE International Conference on Requirements Engineering RE 2005](https://www.interaction-design.org/references/conferences/13th_ieee_international_conference_on_requirements_engineering_re_2005.html) 29 August - 2 September, 2005, Paris, France. pp. 19-30

[Thew](https://www.interaction-design.org/references/authors/sarah_thew.html), Sarah, [Sutcliffe](https://www.interaction-design.org/references/authors/alistair_g__sutcliffe.html), Alistair G., [Bruijn](https://www.interaction-design.org/references/authors/oscar_de_bruijn.html), Oscar de, [McNaught](https://www.interaction-design.org/references/authors/john_mcnaught.html), John, [Procter](https://www.interaction-design.org/references/authors/rob_procter.html), Rob, [Venters](https://www.interaction-design.org/references/authors/colin_venters.html), Colin and [Buchan](https://www.interaction-design.org/references/authors/iain_buchan.html), Iain (2008): Experience in e-Science Requirements Engineering. In: [16th IEEE International Requirements Engineering Conference RE 2008](https://www.interaction-design.org/references/conferences/16th_ieee_international_requirements_engineering_conference_re_2008.html) 8-12 September, 2008, Barcelona, Catalunya, Spain. pp. 277-282

[Thew](https://www.interaction-design.org/references/authors/sarah_thew.html), Sarah, [Sutcliffe](https://www.interaction-design.org/references/authors/alistair_g__sutcliffe.html), Alistair G., [Procter](https://www.interaction-design.org/references/authors/rob_procter.html), Rob, [Bruijn](https://www.interaction-design.org/references/authors/oscar_de_bruijn.html), Oscar de, [McNaught](https://www.interaction-design.org/references/authors/john_mcnaught.html), John, [Venters](https://www.interaction-design.org/references/authors/colin_c__venters.html), Colin C. and [Buchan](https://www.interaction-design.org/references/authors/iain_buchan.html), Iain (2009): *Requirements Engineering for E-science: Experiences in Epidemiology*. In [IEEE Software](https://www.interaction-design.org/references/periodicals/ieee_software.html), 26 (1) pp. 80-87
[Thimbleby](https://www.interaction-design.org/references/authors/harold_thimbleby.html), Harold (2007): *Press On: Principles of Interaction Programming.* The MIT Press
[Tidwell](https://www.interaction-design.org/references/authors/jenifer_tidwell.html), Jenifer (2005): *Designing Interfaces: Patterns for Effective Interaction Design.* O'Reilly and Associates

[Veer](https://www.interaction-design.org/references/authors/gerrit_c_van_der_veer.html), Gerrit C Van Der, [Lenting](https://www.interaction-design.org/references/authors/bert_f_lenting.html), Bert F and [Bergevoet](https://www.interaction-design.org/references/authors/bas_a_j_bergevoet.html), Bas A J (1996): *GTA : Groupware Task Analysis - Modeling Complexity*. In [Acta Psychologica](https://www.interaction-design.org/references/periodicals/acta_psychologica.html), 91 (3) pp. 297-322
[Vicente](https://www.interaction-design.org/references/authors/kim_j__vicente.html), Kim J. (2000): *HCI in the Global Knowledge-Based Economy: Designing to Support Worker Adaptation*. In [ACM Transactions on Computer-Human Interaction](https://www.interaction-design.org/references/periodicals/acm_transactions_on_computer-human_interaction.html), 7 (2) pp. 263-280
[Viller](https://www.interaction-design.org/references/authors/stephen_viller.html), Stephen, [Bowers](https://www.interaction-design.org/references/authors/john_bowers.html), John and [Rodden](https://www.interaction-design.org/references/authors/tom_rodden.html), Tom (1999): *Human
 Factors in Requirements Engineering: A Survey of Human Sciences 
Literature Relevant to the Improvement of Dependable Systems Development
 Processes*. In[Interacting with Computers](https://www.interaction-design.org/references/periodicals/interacting_with_computers.html), 11 (6) pp. 665-698

[Wright](https://www.interaction-design.org/references/authors/peter_c__wright.html), Peter C., [Dearden](https://www.interaction-design.org/references/authors/andy_dearden.html), Andy and [Fields](https://www.interaction-design.org/references/authors/bob_fields.html), Bob (2000): *Function Allocation: A Perspective from Studies of Work Practice*. In [International Journal of Human-Computer Studies](https://www.interaction-design.org/references/periodicals/international_journal_of_human-computer_studies.html), 52 (2) pp. 335-355
[Yu](https://www.interaction-design.org/references/authors/e-dot-s-dot-k__yu.html), E.S.K. (1993): *Modeling organizations for information systems requirements engineering*. In [1993 Proceedings of the IEEE International Symposium on Requirements Engineering](https://www.interaction-design.org/references/periodicals/1993_proceedings_of_the_ieee_international_symposium_on_requirements_engineering.html), pp. 34-41
[Zave](https://www.interaction-design.org/references/authors/pamela_zave.html), Pamela (1995): Classification of research efforts in requirements engineering. In: [Second IEEE International Symposium on Requirements Engineering 1995](https://www.interaction-design.org/references/conferences/second_ieee_international_symposium_on_requirements_engineering_1995.html) March 27 - 29, 1995, York, England. pp. 214-216
**Chapter TOC**

[**Human-Computer Interaction: The Foundations of UX Design**](https://www.interaction-design.org/courses/hci-foundations-of-ux-design)
![](https://public-media.interaction-design.org/images/courses/hds/course_72--square_thumbnail.jpg?tr=fo-auto)
Human-Computer Interaction: The Foundations of UX Design
Closes in
10
days
booked
View Course

## 获取每周 UX 洞察

加入 **314,524 位设计师** 的行列，通过我们的时事通讯获取实用的用户体验（User Experience, UX）技巧。
需要提供有效的电子邮件地址。

## 本书章节涉及的主题：

[需求工程（Requirements Engineering）](https://www.interaction-design.org/literature/topics/requirements-engineering)[
                        用户体验（UX）设计（User Experience (UX) Design）
                    ](https://www.interaction-design.org/literature/topics/ux-design)[
                        人机交互（Human-Computer Interaction, HCI）
                    ](https://www.interaction-design.org/literature/topics/human-computer-interaction)[
                        以用户为中心的设计（User Centered Design）](https://www.interaction-design.org/literature/topics/user-centered-design)
