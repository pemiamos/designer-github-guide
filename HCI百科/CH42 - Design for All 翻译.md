# 42. 全民设计 (Design for All)

**来源**：The Encyclopedia of Human-Computer Interaction, 2nd Ed.
**Notion 原页面**：https://www.notion.so/05ca9616d00e45ada16e3198bb1fc907

---

[Constantine Stephanidis](https://www.interaction-design.org/literature/author/constantine-stephanidis)

## 42.1 什么是通用设计（Design for All）？

当代的交互技术与环境被具有多样化特征、需求和要求的众多用户所使用，其中包括健全人与残障人士，涵盖所有年龄段的人群，以及具有不同技能和专业水平的人群，以及来自世界各地、拥有不同语言、文化和教育背景的人群。此外，交互技术正渗透到日常生活的方方面面，包括沟通、工作与协作、健康与福祉、家居控制与自动化、公共服务、学习与教育、文化、旅行、旅游和休闲等诸多领域。旨在满足上述场景中人类需求的新技术层出不穷，无论其是固定式还是移动式，集中式还是分布式，是可见的还是封装在环境中的。种类繁多的设备已经投入使用，且新设备正频繁且规律地出现。

在上述背景下，[交互设计（interaction design）](https://www.interaction-design.org/literature/topics/interaction-design) 获得了一个新的维度，随之而来的问题是：如何设计出能够以系统化且具有成本效益的方式来适配所有用户的系统。「通用设计（Design for All）」是一个统称，涵盖了广泛的设计方法、手段、技术和工具，旨在帮助解决设计过程中面对的这种巨大的需求与要求多样性。

交互技术（Interactive Technologies）。全员设计（Design for All）旨在将访问特性（Access Features）融入产品中，这一过程始于产品的构思阶段，并贯穿于整个开发生命周期（Development Life-cycle）。

本章内容：
- 通过对其根源和起源的简要探讨，介绍全员设计（Design for All）
- 概述在当今技术格局（Technological Landscape）中使全员设计成为必然的多样性维度（Dimensions of Diversity）
- 阐述全员设计的主要视角及相关的技术方法（Technical Approaches）
- 讨论全员设计背景下一些常用的设计方法与技术（Design Methods and Techniques）
- 介绍成熟且新兴的交互技术与手段
- 在环境智能（Ambient Intelligence）这一新兴范式的背景下，探讨未来的发展方向

### 42.1.1 简史

全员设计（Design for All）的概念在 20 世纪 90 年代末引入到[人机交互（Human-Computer Interaction, HCI）](https://www.interaction-design.org/literature/topics/human-computer-interaction)文献中，此前由欧盟委员会（European Commission）资助了一系列研究工作（Stephanidis and Emiliani, 1999; Stephanidis et al., 1998; Stephanidis et al., 1999）。HCI 中的全员设计根植于三种传统的融合：

1. 以用户为中心的设计（User-Centered Design），将用户置于交互设计过程的中心。
1. 针对残障人士的[可访问性（Accessibility）](https://www.interaction-design.org/literature/topics/accessibility)和辅助技术（Assistive Technologies）。
1. 针对实体产品和建筑环境的通用设计（Universal Design）。

### 42.1.1.1 从以用户为中心的设计到全民设计（Design for All）

以用户为中心的设计（User-centered design, UCD）（Vrendenburg et al., 2001; ISO 1999; ISO 2010）是一种交互系统设计与开发方法，其核心在于提高系统的可用性（Usability）。这是一个迭代过程，其目标是通过在系统设计过程中引入潜在用户，从而开发出具有可用性的系统。

***定义***
以用户为中心的设计（User-centered design）
一种将[易用性（Ease of use）](https://www.interaction-design.org/literature/topics/ease-of-use)融入产品和系统整体[用户体验（User experience）](https://www.interaction-design.org/literature/topics/ux-design)的设计方法。它包含两个基本要素：多学科团队协作，以及一套用于获取用户输入并将其转化为设计的专业方法。
Vrendenburg et al., 2001

以用户为中心的设计包括四项迭代设计活动，所有活动均需用户的直接参与：
1. 理解并明确使用情境（Context of use）、用户的特质、其目标和任务，以及产品将在其中使用的环境；
1. 明确用户和组织在有效性（Effectiveness）、效率（Efficiency）和满意度（Satisfaction）方面的需求，以及用户与系统之间的功能分配；
1. 针对可行方案产出设计方案和原型；
1. 进行基于用户的评估。

![](https://public-media.interaction-design.org/images/encyclopedia/design_4_all/Figure1.jpg)

作者/版权持有者：UXPA。版权条款与许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 42.1**：以用户为中心的设计（User-Centered Design, UCD）循环。

以用户为中心的设计要求：
- 用户的积极参与以及对用户和任务需求的清晰理解。最终用户的积极参与是其核心优势之一，因为它能向设计者传达系统将被使用的使用情境（Context of Use），从而潜在地提高最终成果的认可度。
- 用户与系统之间合理的功能分配（Allocation of Functions）。确定一项工作或任务中的哪些方面由用户处理，哪些可以由系统本身处理至关重要。这种分工应基于对人类能力及其局限性的认识，以及对任务具体需求的深入掌握。
- 设计方案的[迭代](https://www.interaction-design.org/literature/topics/design-iteration)（Iteration）。迭代设计（Iterative Design）意味着在最终用户使用早期设计方案后获取其反馈。用户尝试使用原型（Prototype）来完成“现实世界”中的任务。此次练习的反馈将用于进一步优化设计。

- 多学科设计团队（Multi-disciplinary design teams）。[以用户为中心（User centered）](https://www.interaction-design.org/literature/topics/user-centered-design)的系统开发是一个协作过程，得益于各方的积极参与，每位参与者都能分享其见解和专业知识。因此，开发团队应由在设计生命周期（design life cycle）各个阶段具备技术能力的专家组成。该团队可能包括管理人员、[可用性（usability）](https://www.interaction-design.org/literature/topics/usability)专家、最终用户、软件工程师、平面设计师、交互设计师、培训与支持人员以及任务专家。

以用户为中心的设计（User-centered design）认为，系统的使用质量（quality of use），包括可用性以及用户的健康与安全，取决于用户、任务以及系统所处组织环境和物理环境的特征。此外，它强调了理解并识别该情境（context）细节的重要性，以便指导早期的设计决策，并为规定可用性评估的内容提供基础。然而，它在处理用户需求多元性（diversity in user requirements）方面的能力有限，因为它倾向于传统的视角，即认为“典型”或“平均”用户在工作环境中与桌面计算机进行交互 (Stephanidis, 2001)。虽然以用户为中心的设计专注于保持一种多学科且让用户参与的视角来...

在系统开发（systems development）中，它并未明确说明设计师应如何应对截然不同的用户群体。

### 42.1.1.2 从无障碍与辅助技术到全员设计（Design for All）

在人机交互（Human-Computer Interaction, HCI）语境下，无障碍（Accessibility）是指残障人士对信息与通信技术（Information and Communication Technologies, ICT）的访问能力。用户与 ICT 的交互可能会受到其个人能力或功能限制（functional limitations）的多种影响，这些限制可能是永久性的、临时的、情境性的（situational）或上下文相关的（contextual）。例如，视觉功能受限的人无法使用仅提供图形输出的交互系统；而骨骼或关节活动能力受限、影响上肢运动功能的人，在面对仅接受标准键盘和鼠标输入的交互系统时会遇到困难。

HCI 语境下的无障碍旨在通过使具有各种功能或情境限制的人员的交互体验尽可能接近于没有此类限制的人员，从而克服这些障碍。

交互过程大致可以分析如下：
- 用户通过使用输入设备执行动作向系统提供输入（例如，用户按下鼠标按钮以输入命令）；
- 系统对输入进行解析（例如，系统识别并执行该命令）；
- 系统生成响应（例如，系统为用户生成一条通知命令已执行的响应消息）；
- 响应通过系统动作呈现给用户。

使用输出设备（例如，消息通过消息窗口显示在屏幕上）；
- 用户感知并解读响应（例如，用户在屏幕的消息窗口中看到并阅读该消息）。

物理设备（Physical Device）是系统的某种人造物（Artifact），用于获取（输入设备）或传递（输出设备）信息。示例包括键盘、鼠标、屏幕和扬声器。交互技术（Interaction Technique）涉及使用一个或多个物理设备，以便最终用户在系统运行期间提供输入或接收输出。

交互风格（Interaction Style）是一组可感知的交互元素（Perceivable Interaction Elements），由用户（通过交互技术）或系统用于交换信息，且这些元素具有共同的[审美（Aesthetic）](https://www.interaction-design.org/literature/topics/aesthetics)和行为特征。在图形用户界面（Graphical User Interfaces）中，“交互风格”一词用于表示交互元素之间共同的视觉外观与操作体验（Look and Feel）。典型的例子包括菜单选择（Menu Selection）和直接操纵（Direct Manipulation）。交互元素构成了系统的[用户界面（User Interface）](https://www.interaction-design.org/literature/topics/ui-design)，而用户交互则是由物理动作（Physical Actions）产生的。物理动作是指由系统或用户在物理设备上执行的操作。通常，系统动作涉及反馈（Feedback）和输出，而用户动作则提供输入。输入动作的示例包括

这包括点击鼠标按钮或在键盘上打字。不同的交互技术（interaction techniques）和交互风格（interaction styles）利用了不同的感官模态（sensory modalities）。在实践中，与视觉和听觉相关的模态最常用于输出，而触觉（haptics）的使用较少。然而有趣的是，触觉仍然是输入的主要模态（例如：打字、指针定位、触摸、滑动、抓取等）。味觉和嗅觉直到最近才开始被研究用于输出目的。

总之，交互中涉及的实际人体功能是运动（motion）、感知（perception）和认知（cognition）。在此背景下，可访问性（accessibility）意味着：

- 输入设备及相关的交互技术应确保用户能够可行地进行操作（即它们与用户的运动功能相兼容）；
- 所采用的交互风格（以及由此产生的用户界面）能够被用户感知（即它们与用户的感官功能相兼容）；
- 所采用的交互风格（以及由此产生的用户界面）能够被用户理解（即它们与用户的认知功能相兼容）。

考虑到人类在相关功能方面存在的高度多样性，可访问性要求提供替代设备和交互风格，以适应不同的需求。

在提高可访问性的传统努力中，主要遵循的方向是使残障用户能够访问交互式

通过适当的辅助技术（Assistive Technologies, AT），使最初为身体健全用户开发的应用程序变得可用。

辅助技术（Assistive Technology, AT）是一个通用术语，涵盖了广泛的可访问性插件（accessibility plug-ins），包括特殊用途的输入和输出设备（input and output devices），以及选择、定位和使用这些设备的流程。AT 通过使残障人士能够执行他们原本无法完成或难以完成的任务，从而提升其独立性。在这种语境下，它为完成此类任务所涉及的技术交互提供了增强或替代的方法。

***定义***

辅助或适配技术（Assistive or Adaptive Technology）通常是指“……无论是通过商业购买、修改还是定制的产品、设备或装备，用于维持、增加或提高残障人士的功能能力（functional capabilities）……”

Assistive Technology Act of 1998

常见的辅助技术包括：为盲人用户提供的屏幕阅读器（screen readers）和盲文显示器（Braille displays）；为低视力（low vision）用户提供的屏幕放大镜（screen magnifiers）；为运动障碍用户（motor impaired users）提供的替代输入和输出设备（例如：适配键盘 adapted keyboards、鼠标模拟器 mouse emulators、摇杆 joystick、二进制开关 binary switches）；专用浏览器（specialized browsers）以及文本预测系统（text prediction systems）。

![](https://public-media.interaction-design.org/images/encyclopedia/design_4_all/Figure2.jpg)

作者/版权持有者：Clevy Keyboard。版权条款和许可：保留所有权利。在合理使用（Fair Use）原则下未经许可使用。

原则（因无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面中的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

**图 42.2**：适配键盘（Adapted keyboard）
![](https://public-media.interaction-design.org/images/encyclopedia/design_4_all/Figure3.jpg)
作者/版权持有者：gizmodo.com。版权条款与许可：保留所有权利（All Rights Reserved）。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面中的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

**图 42.3**：脚鼠（Footmouse）

辅助技术（Assistive Technologies）在本质上具有反应性（reactive）。它们为最初针对健全人用户（able-bodied users）设计和开发的交互式应用程序和服务提供产品级（product-level）和平台级（platform-level）的适配。为了在提供可访问性（Accessibility）方面采取更系统化和前瞻性（proactive）的方法，从而产生了全员设计（Design for All）的概念。这种从辅助技术领域传统定义的可访问性向全员设计视角的转变，是由于：(i) 技术发展的快速步伐，伴随着大量新系统、设备、应用程序和用户的出现，使得开发可访问性插件（accessibility add-ons）变得非常困难；(ii) 对面临技术排斥（technological exclusion）风险的人群关注度增加，且不仅限于那些……

在这一视角下，无障碍性（Accessibility）必须被设计为一项核心系统特性，而非在事后（*a posteriori*）才决定并实施，从而将无障碍性整合到所有应用程序和服务的设计过程中。

### 42.1.1.3 从通用设计到人机交互中的全民设计 (Design for All)

应对人类多样性的前瞻性方法最早出现在工程学科中，例如土木工程和建筑学，并在室内设计、建筑和道路建设中得到了广泛应用。

“通用设计（Universal Design）”这一术语由建筑师 Ronald L. Mace 提出，旨在描述这样一种概念：在设计所有产品和建成环境（built environment）时，应使其在最大程度上兼顾美观与可用性，且无论使用者的年龄、能力或生活状态如何均可使用 (Mace et al., 1991)。尽管该概念的范围一直较为广泛，但其重点往往集中在建成环境上。

> 定义
  ***通用设计（Universal Design）：***是指在最大程度上使产品和环境能够被所有人使用，而无需进行适配或专门设计。***通用设计的意图是通过使产品、通信和建成环境在增加极少或不增加额外成本的情况下，让尽可能多的人能够更方便地使用，从而简化每个人的生活。通用设计使所有年龄段和能力的人受益。***
  *(Mace et al., 1991)*

通用设计的一个经典例子是路缘切口（kerb cut，或称人行道坡道），最初是为轮椅使用者从街道进入人行道而设计的，如今已广泛应用于许多建筑中。其他例子还包括低底盘巴士、带有抽拉式搁板的橱柜以及厨房

设置不同高度的台面，以适应不同的任务和姿势。
![](https://public-media.interaction-design.org/images/encyclopedia/design_4_all/Figure4.jpg)
作者/版权持有者：[www.thelittlehousecompany.co.uk](http://www.thelittlehousecompany.co.uk/)。
版权条款与许可：保留所有权利（All Rights Reserved）。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面上的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。
**图 42.4**：无障碍家居
![](https://public-media.interaction-design.org/images/encyclopedia/design_4_all/Figure5.jpg)
作者/版权持有者：Mohammed Yousuf 和 Mark Fitzgerald。
版权条款与许可：保留所有权利（All Rights Reserved）。经许可转载。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”章节。
**图 42.5**：无障碍交通信号灯

在通用设计（Universal Design）中，最常见的方法或许是通过多种模态（modalities）提供关于物体或建筑的信息，例如电梯按钮上的盲文（Braille）以及交通信号灯的声学反馈（acoustic feedback）。没有残障的人群通常也能从中受益。例如，为听障人士设计的电视字幕或多媒体内容，对于非母语使用者、旨在提高识字能力的儿童，以及在嘈杂环境中观看电视的人来说同样有用。

通用设计（Universal Design）的七项原则由 Ronald Mace 领导的北卡罗来纳州立大学（North Carolina State University）的一个由建筑师、产品设计师、工程师和环境设计研究人员组成的工作组于 1997 年制定。这些原则“可用于评估现有设计，指导设计过程，并向设计师和消费者普及更具可用性的产品和环境的特征”。

***公平使用（Equitable use）***：设计对于具有不同能力的人群而言都是有用且具有市场吸引力的。

***使用的灵活性（Flexibility in use）***：设计能够适应广泛的个人偏好和能力。

***简单且直观（Simple and intuitive）***：无论用户的经验、知识、语言能力或当前的注意力集中程度如何，该设计的使用方式都易于理解。

[***可感知的信息（Perceptible information）***](https://www.interaction-design.org/literature/topics/affordances)：无论环境条件或用户的感官能力如何，设计都能有效地向用户传递必要的信息。

***容错性（Tolerance for error）***：设计能够最大限度地减少危险以及意外或无意行为带来的不利后果。

***低体力消耗（Low physical effort）***：设计能够高效、舒适地使用，且能最大限度地减少疲劳。

***接近和使用的尺寸与空间（Size and space for approach and use）***：无论用户的体型、姿势或移动能力如何，设计都提供了适当的尺寸和空间以便于接近、触及、操作和使用。

版权所有 © 1997 NC State University, The Center for Universal Design. (http://www.ncsu.edu/ncsu/design/cud/about_ud/udprinciples.htm)

在人机交互（Human-Computer Interaction, HCI）的语境下，上述概念在 90 年代末被用于表示让任何人都能在任何时间、任何地点访问交互式产品和服务的设计。

> “全民设计（Design for All）”这一术语要么涵盖，要么是以下术语的同义词：无障碍设计（accessible design）、包容性设计（inclusive design）、无障碍环境设计（barrier-free design）、通用设计（universal design），其中每个术语都强调了该概念的不同方面。
>
> *(Stephanidis et al., 1998)*

> 定义
>
> ***HCI 中的全民设计（Design for All in HCI）：*** **是指一种自觉且系统性的努力，旨在主动应用原则和方法，并采用适当的工具，以开发能够被所有公民访问且易用的信息技术与电信（Information Technology & Telecommunications, IT&T）产品和服务，从而避免事后（a posteriori）的适配或专门化设计。这意味着需要从产品的构思阶段开始，在整个开发生命周期中将访问特性构建到产品之中。**(Stephanidis et al., 1998)*

HCI 中的全民设计意味着需要重新审视传统的设计质量，如可访问性（accessibility）和可用性（usability）。

> 定义
>
> *可访问性（Accessibility）：* 对于用户需要通过交互系统完成的每项任务，在考虑到特定的功能限制和能力以及其他相关上下文因素的情况下，存在一个...

输入和输出操作，从而实现任务的成功完成 (Savidis and Stephanidis, 2004)。**可用性（Usability）：** 指所有支持的任务完成路径，在特定的使用语境（Context）和情境（Situation）下，能够“最大程度地契合”个体用户需求和要求的能力 (Savidis and Stephanidis, 2004)。
***由此可见，可访问性（Accessibility）是可用性的基础前提，因为如果首先不存在交互的可能性，那么就不可能存在最佳的交互。***

## 42.2 多样性的维度（Dimensions of diversity）

### 42.2.1 用户多样性（User diversity）

“用户多样性（User diversity）”这一术语是指用户在对技术的感知（Perception）、操作（Manipulation）和利用（Utilization）方面存在的各种差异。理解用户多样性的各个维度，有助于设计和开发能够为不同类型用户带来最大收益的用户界面（User interfaces）。存在几个多样性维度，这些维度决定了人们与技术交互方式的不同。

### 42.2.1.1 残疾（Disability）

无障碍（Accessibility）的核心在于关注人类在访问和使用信息与通信技术（Information and Communication Technologies, ICTs）方面的多样性。这一方向的主要工作集中在识别和研究多样化的目标用户群体（target user groups）（例如，患有各种类型残疾的人群和老年人），以及他们对交互的需求，以及能够满足这些需求的适当模态（modalities）、交互设备和技术。近年来，研究者开展了大量的实验工作，旨在收集并详细阐述各种残疾如何影响与技术的交互。这种理解可以通过 World Health Organization (2001) 提出的《国际功能、残疾和健康分类》（International Classification of Functioning, Disability and Health, ICF）的功能方法（functional approach）来促进。在该分类中，“残疾（disability）”一词被用来表示由个体与其物理和社会环境之间的交互而产生的一种多维现象。这使得研究者能够对各种限制进行分组和分析，而这些限制不仅是由损伤（impairments）引起的，还可能是由于环境因素等原因造成的。

### 42.2.2 42.2.1.1.1 感知（Perception）

视觉和听觉障碍（Visual and auditory impairments）显著影响人机交互（Human-Computer Interaction）。失明（Blindness）是指视觉感官在解剖学和功能上的障碍程度足以导致光感完全丧失；而视力受损（Visual impairment）则是指任何偏离普遍认可的标准的情况。盲人用户可以通过使用听觉模态（Auditory modality）和触觉模态（Haptic modality）来进行输入和输出。在实践中，盲人用户的交互是通过屏幕阅读器（Screen readers，即向用户朗读图形界面的专业软件 (Asakawa and Leporini, 2009)）、语音输出以及盲文显示器（Braille displays）（见***Haptics***章节）来支持的。后者属于触觉设备，但需要用户掌握盲文代码（Braille code）。音频（非语音）声音也可用于提升盲人用户的交互体验 (Nees and Walker, 2009)。盲人用户可以使用键盘和摇杆，但无法使用鼠标。因此，用户界面中的所有操作必须在不使用鼠标的情况下即可完成。无论是对于输出还是输入，提供的用户界面结构都至关重要，应尽可能缩短在以顺序方式（Sequential fashion，例如通过语音）提供时，访问特定重要元素（如菜单或链接）所需的时间。

程度较轻的视觉限制通常通过增加交互构件（Interactive artifacts）的尺寸以及提高...之间的颜色对比度来解决。

用户界面（User Interface）的背景和前景元素。对于患有各种类型色盲（Color-blindness）的用户，可能需要特定的颜色组合。

听力障碍（Hearing impairments）包括任何程度和类型的听觉障碍（Auditory disorder），其范围从轻微到严重不等。听力限制可能会显著影响用户与技术的交互（Interaction）。听障人士常用的应对策略（Coping strategies）包括使用助听器、读唇术以及聋哑人电信设备。聋哑用户可能不习惯用户界面中的书面语言，因此可能会从所提供信息的手语翻译（Sign-language translations）中获益（参见 ***Sign Language*** 章节）。

### 42.2.3 42.2.1.1.2 运动（Motion）

肢体障碍（physical impairments）的性质和原因各异；然而，肢体障碍者面临的最常见问题包括肌肉控制能力差、虚弱和疲劳，以及在行走、交谈、视觉、说话、感知或抓握（由于疼痛或虚弱）、触及物品以及执行复杂或复合操作（如推和转）方面存在困难。严重肢体障碍者通常需要依赖辅助设备（assistive devices），例如移动辅助工具（mobility aids）、操作辅助工具（manipulation aids）、沟通辅助工具（communication aids）和计算机接口辅助工具（computer interface aids）(Keates, 2009)。

运动障碍（Motion impairments）会干扰与技术交互所需的各项功能。例如，使用鼠标和键盘可能会具有挑战性或带来疼痛。因此，运动障碍用户可能会从专门的输入设备中获益，这些设备能最大限度地减少输入所需的动作和体力消耗，包括适配键盘（adapted keyboards）、鼠标模拟器（mouse emulators）、摇杆（joystick）和二进制开关（binary switches）。这些设备通常与一种称为扫描（scanning）的交互技术（见 ***Scanning-based Interaction*** 章节）结合使用，此外还包括用于文本输入的虚拟屏幕键盘（virtual on-screen keyboards），有时这些键盘还由文本预测系统（text prediction systems）提供支持。其他针对运动功能障碍人士而研究的交互技术……

针对这些限制的方案包括口头指令的语音输入（Voice Input，见 ***Speech*** 节）、通过头部动作模拟键盘和鼠标（Keyboard and Mouse Simulation，见 ***Gestures and Head Tracking*** 节）以及眼动追踪（Eye-tracking，见 ***Eye-tracking*** 节）。此外，研究人员还在探索脑机接口（Brain-computer interfaces），使其能够仅通过思维即可控制应用程序，从而为患有严重运动功能障碍（Motor Impairments）的人群提供沟通支持（见 ***Brain Interfaces*** 节）。

### 42.2.4 42.2.1.1.3 认知（Cognition）

认知（Cognition）是指人类大脑处理信息、思考、记忆、推理和做出决策的能力。认知能力（cognitive abilities）的程度因人而异，差异巨大。认知障碍（Cognitive disability）意味着个体在思考能力方面存在显著限制，包括：概念化（conceptualizing）、规划以及对思想和行动进行排序（sequencing）；记忆、解读微妙的社会线索（social cues）以及理解数字和符号。认知障碍可能源于脑损伤、Alzheimer's disease（阿尔茨海默病）和痴呆症（dementia）、严重且持续的精神疾病以及中风。认知障碍的形式多样且复杂，这些用户群体的个体差异通常非常显著，因此在研究该人群的用户需求（user requirements）时，很难将涉及的问题进行抽象和概括。

各种认知限制和学习困难可能会影响交互过程（interaction process）。为了方便具有某些类型认知困难的用户（以及其他用户群体，例如老年用户）进行访问，通用原则包括：尽可能保持用户界面（user interface）简单且极简（minimalistic），提供语法和词汇简单的文本，减少对记忆的依赖，为交互预留充足的时间，并支持用户的注意力（user attention）(Lewis, 2009)。特定的发育性学习状况，例如读写障碍（dyslexia），也

需要在文本、字体、颜色、对比度和图像的使用上格外注意，以提高可理解性（Comprehension）。

### 42.2.4.1 年龄（Age）

年龄在个体如何感知和处理信息方面起着重要作用。了解技术产品的目标群体（Target Population）的年龄，可以为如何呈现信息、反馈（Feedback）、视频、音频等提供关键线索。有两类用户群体具有依赖于年龄的特殊需求：儿童（定义为 18 岁以下的用户，重点关注 12 岁以下儿童）和老年人（通常定义为 65 岁以上用户）。

### 42.2.5 42.2.1.2.1 儿童（Children）

在美国，近一半（48%）的六岁及以下儿童使用过计算机，且超过四分之一（30%）的人玩过电子游戏。当他们处于四到六岁年龄段时，有七成的人使用过计算机 (Wartella et al., 2005)。

儿童作为技术领域一个重要的新兴用户群体（user group）出现，决定了必须以一种对他们有益、有效且符合其需求的方式来为他们提供支持。

儿童的生理与认知能力（physical and cognitive abilities）在从婴儿期到成年期的多年时间里不断发展。儿童，尤其是年幼的儿童，缺乏广泛的经验储备（repertoire of experiences）来引导他们对线索（cues）做出反应。除了缺乏经验之外，儿童感知世界的方式与成年人不同，并且拥有与成年人不同的喜好、厌恶、好奇心和需求。因此，儿童应被视为一个具有自身文化和规范（culture and norms）的不同用户群体（user population） (Bruckman and Bandlow, 2002)。

为儿童设计应用程序带来了特殊的挑战，因为设计师必须学习如何通过儿童的视角来感知系统。例如，听觉反馈（audio feedback）可能会惊吓到年幼的儿童，而极亮色彩和视频则容易分散他们对任务的注意力。

### 42.2.6 42.2.1.2.2 老年用户（Older users）

有大量证据表明，发达国家的人口正在老龄化。除了美国老年人口的增长（到 2030 年将占总人口的 20%）外，全球范围内的老年人口数量也在增加。据估计，到 2050 年，老年人口将首次在历史上超过儿童（0-14 岁）人口。到 2050 年，将有近 20 亿人被视为老年人 (US Department of Health and Human Services Administration on Ageing 2009)。

这一庞大且多样化的用户群体具有不同的身体、感官和认知能力，他们可以从能够帮助其维持健康、福祉和独立生活的技术应用中获益。

老年用户可能会经历运动、感官和认知功能的下降，这可能导致复合性损伤（combined impairments）并严重影响交互 (Kurniawan, 2009)。为老年用户提供可访问性（Accessibility）的原则包括：提高对比度、放大屏幕呈现的信息、谨慎地组织信息、选择合适的输入设备、避免依赖记忆以及设计[简洁性（Simplicity）](https://www.interaction-design.org/literature/topics/simplicity)。

老年人拥有大量来自过去经验的记忆，构成了丰富的经验储备（repertoire）。这自然地影响了他们的

对技术的感受（feelings towards technology）。老年用户可能会对某些技术产生抵触感（sense of resistance），尤其是在使用那些用于处理人们习惯于在无需技术辅助下即可完成的任务的应用时，例如在线银行系统（online banking systems）。在生命晚年感到被“强迫”去适应技术，可能会进一步增强这种抵触情绪。

### 42.2.6.1 计算机使用熟练度（Computer use expertise）

大量人群对技术的广泛使用，使得人们对基础技术工具的熟悉程度有所提高。然而，技术的使用舒适度和易用性（Ease of use）因用户的技能水平而异，差异显著 (Ashok and Jacko, 2009)。

部分用户群体对技术并不熟悉，尤其是老年用户以及受教育程度极低或未受教育的人群，但为了跟上当前的社会演进，他们仍被要求使用计算工具。结果就是用户群体在技术技能水平上呈现出极大的多样性。

为技能范围广泛且不均衡的用户设计系统，其挑战之大令人望而却步。这种情况尤为突出，因为设计师通常是其各自领域的专家，很难理解并整合初学者（Novices）的需求。判断用户的技能水平可能比评估其损伤（Impairments）或障碍更为困难，因为某个特定工具的专家可能会发现新的替代工具难以使用和理解。这导致了一种情况：一个表面上的专家实际上表现得像个初学者。来自不同技能水平用户的反馈可以提供新鲜的视角和新的见解。

包括提供有用的帮助选项、可展开并详细查看的解释、一致的命名规范（Naming conventions）以及

简洁的用户界面（Uncluttered User Interfaces）仅是使技术对领域和系统知识较少的用户而言更具可访问性（Accessible）的几种方式之一，且同时不会降低专家用户（Expert Users）的效率。事实上，这些建议构成了[良好设计](https://www.interaction-design.org/literature/topics/good-design)的准则，无论用户的技能水平如何，都能从中受益。

### 42.2.6.2 文化与语言

在当今世界，由于全球化技术（Globalized technology）的影响，人们对文化的感知、理解和体验发生了显著变化。将这些知识融入技术将有助于提高包容性和宽容度。

语言是文化不可或缺的一部分，由于语言障碍，许多信息在翻译过程中可能会丢失。例如，许多技术应用使用英语，这本身对于不具备该语言听说读写能力的人来说可能是一个限制因素。缩写、拼写和标点符号均属于语言变量（Linguistic variables）。语言与技术应用中文本布局（Layout）之间的关系是一个需要考虑的因素，因为英语和法语等某些语言倾向于较短的表达方式，而其他语言可能需要更长的格式。

“本地化（Localization）”一词是指为了实现有效使用而针对特定市场对产品进行定制。本地化涵盖了语言翻译以及对图形、图标、内容等方面的修改。

其他文化差异还包括对符号、颜色、手势等的解读。例如，颜色使用存在差异（绿色在伊斯兰教中是神圣的颜色，黄色在佛教中如此），阅读方向也存在差异（例如，北美和欧洲是从左到右，中东是从右到左）。关于服装、饮食和审美吸引力的观念在不同文化之间也各不相同。

这些诸多差异使得设计师在开发技术时必须敏锐地意识到这些差异，并避免将所有文化同质化。Design for All（全员设计）并非旨在消除文化和语言差异，而是承认、认可、欣赏并整合这些差异 (Marcus and Rau, 2009)。

### 42.2.6.3 社会问题（Social Issues）

全球化创造了一个信息丰富且沟通便捷的环境。然而，经济和社会地位等社会问题在技术获取（access to technology）方面带来了严峻挑战。在世界许多地区，只有社会中较富裕的阶层才有机会使用技术并从中受益。

贫困、社会地位和有限的教育机会构成了技术获取的障碍。为全球每一个社会经济群体（socio-economic group）设计出同样易于获取且同样易于使用的应用程序几乎是不可能的，但通过考虑不同社会群体的需求，仍有值得借鉴的经验。

研究表明，要通过使用技术获得最佳生产力，需要具备一定的教育水平，更准确地说，是技术教育（technical education）(Castells, 1999)。意识到受教育者更容易获得技术红利，这向设计师、开发人员、工程师以及所有参与技术创造的人员传达了一个关于其责任的简单信息。这一团队负责技术的创造和分发，因此，让他们接受关于通用访问（universal access）以及与用户多样性相关问题的教育至关重要，其中就包括考虑为受教育程度较低的人群进行设计。因此，针对技术素养（technological literacy）进行设计成为了首要任务。

### 42.2.7 技术环境的多样性（Diversity in the technological environment）

多样性不仅关乎用户，还关乎交互环境（interaction environments）和技术，而这些环境与技术正在不断发展和多样化。

用户与技术交互时的特定情境可能会导致临时的功能障碍状态（temporary states of impairment）。例如，一个噪声水平高且视觉干扰严重的办公环境可能会干扰计算机应用程序的高效使用。由情境因素引起的功能障碍被称为情境诱发的功能障碍（situationally-induced impairments）(Sears et al., 2003)。技术本身也可能导致情境诱发的功能障碍。例如，当屏幕过小时，用户在这种特定情况下可能会出现视力受限的情况。互联网的普及和先进技术的激增...

交互技术（Interaction Technologies）（例如：移动设备、网络可连接设备、[虚拟现实](https://www.interaction-design.org/literature/topics/virtual-reality)、智能体（Agents）等）表明，许多应用程序和服务不再局限于视觉桌面（Visual Desktop），而是扩展到了新的现实（New Realities）和交互环境（Interaction Environments）中。总体而言，各种技术范式（Technological Paradigms）在全员设计（Design for All）中发挥着重要作用，它们要么提供了新的交互平台（Interaction Platforms），要么在不同层面上为确保并扩大访问权限做出了贡献。

万维网（World Wide Web）及其技术无疑是这一格局中的核心组成部分。为了使 Web 具有无障碍性（Accessible），人们已经面对各种挑战并制定了相应的解决方案。对于能够访问其内容的人来说，万维网提供了丰富的资源，但与此同时，由于视觉、运动、语言或认知能力（Visual, Motor, Language, or Cognitive Abilities）的限制，访问权限受到了严重障碍的限制。

另一个非常重要且快速进步的技术进步是移动计算（Mobile Computing）。移动设备在日常生活中扮演着越来越重要的角色，既作为专用工具（Dedicated Tools）（如媒体播放器），也作为多功能设备（Multi-purpose Devices）（如智能手机）。设备需要易于使用，即使在移动过程中也是如此。移动交互（Mobile Interaction）往往会带来矛盾的设计目标与需求（Contradictory Design Goals and Requirements）。由于其特性，移动情境（Mobile Contexts）的环境要求较高

例如噪声或光线不足。用户可能需要进行多任务处理（Multitasking），导致其只能将部分注意力投入到设备的使用中。此外，文化差异和用户预期（User expectations）对设备的使用也有重大影响。移动设备及其使用情境（Usage situations）的这些特性对设计提出了极高要求。与其他任何应用领域一样，移动用户群体可以根据年龄、能力以及对环境的熟悉程度来定义。然而，不同用户群体对移动设备和服务的要求在不同的[使用语境（Contexts of Use）](https://www.interaction-design.org/literature/topics/contexts-of-use)中有所不同。

移动性（Mobility）带来的挑战在于，使用语境差异巨大，且即使在具体的使用情境过程中也可能发生变化。在设计移动设备和服务时，需要考虑这种可变的使用语境。移动设备和服务最初的假设是它们可以在“任何地方”使用。但这一假设并不总是成立；环境和语境给使用带来了挑战。在某些环境下禁止使用手机，且在某些地方可能没有网络覆盖（Network coverage）。

用户可能存在身体上的障碍，或处于暂时性障碍（Temporally disabled）状态。在黑暗或强光环境下，可能难以看清用户界面（User Interface）元素。在拥挤的地方，通过电话进行语音通话可能很困难——甚至比面对面的情况更困难，当你

即使无法听到每一个词，人们也可以利用非语言线索（Non-verbal cues）来推断对方在说什么。在社会沟通（Social communication）中，情境（Context）起着重要作用；人们在开始电话交谈时，经常会询问对方的物理位置——“你在哪里”——以判断对方所处的情境是否允许接听电话。

## 42.3 视角与方法

在全员设计（Design for All）的背景下，用户界面设计的方法论、技术和工具变得日益重要。为了使设计者能够主动地在交互制品（interactive artifacts）的设计中考虑并妥善处理多样性（diversity），人们提出了各种方法、技术和实践规范（codes of practice）。下文概述了三种基本方法。

### 42.3.1 指南与标准

在支持交互产品、服务和应用设计的国际协作计划（international collaborative initiatives）背景下，人们制定了相关指南和标准，旨在使大多数潜在用户无需任何修改即可访问这些产品。这种方法主要应用于万维网（World Wide Web）的无障碍性（accessibility）。

### 42.3.1.1 Web 无障碍 (Web accessibility)

> Web 无障碍 (Web accessibility) 意味着残障人士能够使用 Web。更具体地说，Web 无障碍意味着残障人士能够感知、理解、导航并与 Web 交互，并且能够为 Web 做出贡献。Web 无障碍同样使其他人受益，包括因衰老而能力发生变化的老年人。http://www.w3.org/WAI/intro/accessibility.php

目前已开发出许多无障碍指南集 (Pernice and Nielsen, 2001; Vanderheiden et al., 1996)。其中，Web 内容无障碍指南 (Web Content Accessibility Guidelines, WCAG) 详细阐述了如何使 Web 内容对残障人士可见 (W3C, 1999)。Web “内容”通常指 Web 页面或 Web 应用程序中的信息，包括文本、图像、表单、声音等。WCAG 1.0 提供了 14 条作为无障碍设计通用原则的指南。每条指南包含一个或多个检查点 (checkpoints)，用以解释该指南在特定领域中的应用方式。WCAG 预设了三个合规性 (compliance) 等级：A、AA 和 AAA。每个等级都要求执行一套更严格的一致性指南 (conformance guidelines)，例如不同版本的 HTML（过渡模式 Transitional 与 严格模式 Strict），以及在完成验证 (validation) 之前需要整合到代码中的其他技术。在 WCAG 1.0 的基础上，W3C 于 2008 年 12 月发布了新版本的指南，旨在帮助 Web 设计师和开发人员创建能够更好地满足需求的网站。

高龄用户和残障用户。基于广泛的经验和社区反馈，WCAG 2.0 (W3C, 2008) 在 WCAG 1.0 的基础上进行了改进，并适用于更先进的技术。此外，针对移动设备上 Web 界面（web interfaces）的可用性（usability）也提供了相关指南 (W3C, 2005)。WCAG 2.0 指南围绕四项原则构建，这些原则为 Web 可访问性（Web accessibility）奠定了基础，即 *可感知（perceivable）、可操作（operable）、可理解（understandable）和鲁棒性（robust）*。

这 12 项指南提供了作者应努力实现的基准目标，旨在使不同残障用户能够更方便地访问内容。这些指南本身不可测试，但它们提供了框架和总体目标，以帮助作者理解成功标准（success criteria）并更好地实施相关技术。针对每项指南，都提供了可测试的成功标准，使得 WCAG 2.0 能够应用于需要明确要求和一致性测试（conformance testing）的场景，例如设计规范（design specification）、采购、监管和合同协议。为了满足不同群体和不同场景的需求，定义了三个一致性级别（levels of conformance）：A（最低）、AA 和 AAA（最高）。WCAG 指南还涵盖了在移动设备上使用的内容。

如今，使用这些指南是 Web 作者创建可访问 Web 内容（accessible web content）最广泛采用的流程。事实证明，这种方法对于消除目前残障人士面临的诸多障碍具有重要价值。

残障人士。此外，这些指南还服务于计算机经验不足的用户，并促进与新兴技术解决方案的互操作性（Interoperability）（例如，为驾驶员提供的具有语音识别功能的导航系统）。此外，指南构成了事实标准（*de facto* standards），并且是许多国家关于可访问性（Accessibility）立法和法规的基础 (Kemppainen, 2009)。例如，美国政府的《康复法》（Rehabilitation Act of 1973, Amendment of 1998）第 508 条（Section 508）提供了一套全面的规则，旨在帮助网站设计者提高其网站的可访问性。然而，由于多种原因，在应用指南时会出现许多局限性。其中包括对指南的解读和应用存在困难，这需要大量的培训。此外，该过程

使用或测试是否符合广泛认可的无障碍指南（accessibility guidelines）是一个复杂且耗时的过程。为了解决这一问题，目前已开发出多种能够对 HTML 文档进行半自动检查（semi-automatic checking）的工具。这些工具使无障碍网页内容的开发变得更加容易，尤其是因为符合性检查不再仅仅依赖于开发者的专业知识。在网页无障碍方面经验有限的开发者可以使用这些工具来评估网页内容，而无需查阅大量的检查清单（checklists）。

尽管 WCAG 在网页无障碍方面的[实用性（usefulness）](https://www.interaction-design.org/literature/topics/usefulness)已得到证明，但网页内容制作者经常忽略或忽视这些指南，从而限制了残障用户在网站中浏览信息和服务的能力。因此，这些指南原则远未得到良好的整合，即使是在法律强制执行的公共网站中也是如此。最近的研究表明，全球范围内的网页无障碍指标（web accessibility metrics）正在恶化 (Basdekis, et al., 2010)。

最后需要考虑的是，无障碍指南通常采用一种“一刀切（one-size-fits-all）”的方法，虽然这能为各种类型的残障用户确保基础的无障碍水平，但并不支持个性化（personalization）和交互体验的提升。

### 42.3.1.2 其他可访问性指南与标准

除了网页可访问性（Web Accessibility）之外，其他类型的应用程序也拥有相应的指南和标准。例如，主要的软件公司已经启动了可访问性计划（Accessibility Initiatives），并为使用其工具和开发环境的开发人员提供可访问性指南（Accessibility Guidelines）。示例包括 (Microsoft, 2013), (Adobe, 2013), 以及 (IBM, 2013)。

多媒体内容（Multimedia Content）的可访问性也得到了国际联盟（International Consortia）的关注，尤其是在教育领域，例如 (IMS, 2013)，同时内容提供商也对此进行了探讨，例如 (BBC, 2013)。

国际、欧洲和国家标准化机构（Standardization Bodies）开展的其他与可访问性相关的活动在 (Engelen, 2009) 中有详细讨论。

### 42.3.2 用户界面适配（User Interface Adaptation）

鉴于上述情况，看来那些专注于提供供所有人使用的单一交互元素的设计方法，在应对所有用户所体现的多样化需求方面，其可能性十分有限。因此，交互元素的一个关键属性便成为了其实现某种形式的自动适配（Automatic Adaptation）和个性化（Personalization）的能力 (Stephanidis, 2001)。

基于适配的方法通过引入可适配或可定制的用户界面（User Interfaces），推动设计出能够轻松适配不同用户的产品。这意味着需要努力将访问特性（Access Features）构建到产品中，从其构思阶段开始，并贯穿于整个开发生命周期（Development Life-cycle）。

用户界面适配的方法和技术在现代界面中取得了显著成功。一些典型的例子包括 Microsoft Windows 各个版本中的桌面适配，例如，提供隐藏或删除未使用的桌面项的能力，以及基于用户偏好的桌面个性化功能，如添加有用的动画、透明玻璃菜单栏、打开程序的实时缩略图预览以及桌面小工具（如时钟、日历、天气预报等）。同样，Microsoft Office 应用程序也提供了多种定制化（Customizations）选项，例如工具栏的定位以及显示/隐藏最近使用的选项。然而，适配

集成到商业系统中的设置需要手动配置，且主要侧重于审美偏好。在可访问性（Accessibility）和可用性（Usability）方面，仅提供了有限的适配选项，例如键盘快捷键、尺寸和缩放选项、颜色和声音设置的更改以及自动化任务等。

在过去几十年的研究中，学者们在全民设计（Design for All）的背景下，阐述了更为全面且系统化的用户界面适配（User Interface Adaptations）方法。Unified User Interfaces 方法论由 Savidis and Stephanidis (2009) 提出并应用，旨在通过自动适配（Automatic Adaptation）高效且有效地确保具有不同特征的用户能够获得 UI 的可访问性和可用性，同时支持技术平台独立性（Technological Platform Independence）、隐喻独立性（Metaphor Independence）以及用户配置文件独立性（User-profile Independence）。自动 UI 适配旨在最大限度地减少对后验（*a posteriori*）适配的需求，并提供能够适配给尽可能广泛的终端用户群体使用的产品（即可适配用户界面，Adaptable User Interfaces）。这意味着需要根据目标用户群体的能力、需求和偏好，以及使用情境（Context of Use，例如技术平台、物理环境）的特征，提供不同的替代界面实例（Alternative Interface Instances）。其主要目标是确保每位终端用户在运行时（Run-time）都能获得最合适的交互体验（Interactive Experience）。证书为自动适配（automatic adaptation）进行设计是一个复杂的过程。设计师应准备好应对庞大的设计空间（design spaces），以兼容由目标用户群体（target user population）的多样性以及不断出现的使用情境（contexts of use）所带来的设计约束（design constraints）。因此，设计师需要具备无障碍（accessibility）相关的知识与专业技能。此外，用户适配（user adaptation）必须经过仔细的规划与设计，并将其纳入交互系统（interactive system）的生命周期（life-cycle）中——从早期的设计探索阶段（exploratory phases），一直到评估、实现、部署和维护。

![](https://public-media.interaction-design.org/images/encyclopedia/design_4_all/Figure6.jpg)
作者/版权持有者：Stephanidis。版权条款与许可：保留所有权利。经许可转载。请参阅下方 [版权条款 (copyright terms)](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”章节。

**图 42.6**：可适配用户界面（adaptable user interface）的架构

为了支持统一用户界面（Unified User Interface, UUI）设计，一系列工具和组件已被开发出来，包括可适配交互对象（adaptable interaction objects）工具包、用于用户画像（user profiling）和适配决策（adaptation decision making）的语言，以及原型工具（prototyping tools）(Stephanidis et al., 2012)。这些工具旨在支持具有适配行为（adaptation behavior）的用户界面的设计与开发，特别是统一用户界面开发方法的实施与应用。多年来，这些工具证明了该方法在技术上的可行性，并有助于缩小传统用户界面设计与适配设计（design for adaptation）之间的实践差距（practice gap）。它们已被应用于大量的试点应用（pilot applications）和案例研究中。

![](https://public-media.interaction-design.org/images/encyclopedia/design_4_all/Figure7.jpg)
作者/版权持有者：Stephanidis et al., 2001. 版权条款和许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。

**图 42.7**：***AVANTI 浏览器***：一个具有统一用户界面的通用可访问（universally accessible）Web 浏览器。AVANTI 浏览器为多种类别的用户提供了访问基于 Web 的信息系统的界面，包括：(i) “身体健全”的人员；(ii) 盲人；以及 (iii) 在使用传统输入设备时存在不同程度困难的运动障碍（motor-impaired）人员。

Stephanidis et al., 2001
![](https://public-media.interaction-design.org/images/encyclopedia/design_4_all/Figure8.jpg)
作者/版权持有者：Stephanidis et al., 2005。版权条款与许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。
**图 42.8**：**PALIO**：一个支持提供基于 Web 的服务的系统，该系统能够根据用户和上下文特征（context characteristics）以及用户当前位置表现出自动适配行为（automatic adaptation behavior）。Stephanidis et al., 2005
![](https://public-media.interaction-design.org/images/encyclopedia/design_4_all/Figure9.jpg)
作者/版权持有者：Grammenos et al., 2005。版权条款与许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。
**图 42.9**：***UA-Chess***：一款通用可访问（universally accessible）的多模态（multi-modal）国际象棋游戏。该游戏支持两名玩家（包括低视力、盲人及手部运动障碍等残障人士）在同一台计算机上本地对弈，或通过互联网远程对弈。Grammenos et al., 2005
![](https://public-media.interaction-design.org/images/encyclopedia/design_4_all/Figure10.jpg)
作者/版权持有者：Doulgeraki et al., 2009。版权条款与许可：保留所有权利。经许可转载。请参阅章节

下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外情况（Exceptions）”。

**图 42.10**：***EDeAN Portal***：一个用于支持 EDeAN 网络活动的自适应（adaptable）Web 门户。自适应过程在服务端通过一套自适应交互对象（adaptable interaction objects）工具包来实现。Doulgeraki et al., 2009

### 42.3.3 云端无障碍性（Accessibility in the cloud）

近年来云计算的出现为提供无障碍性开辟了新的机遇。云端无障碍性是另一种方法，旨在摆脱特殊的“辅助技术（Assistive Technologies）”和“残障访问功能（Disability Access Features）”的概念，转而为所有人提供更主流的界面选项（Mainstream Interface Options），即：不仅为那些因残障、读写能力（Literacy）或年龄相关问题而在使用交互技术（Interactive Technologies）时面临障碍的人群提供合适的界面，也为那些仅仅想要更简单的界面、患有临时性障碍（Temporary Disability）、在眼睛被其他事情占用时需要访问、想要让手或眼睛休息，或者想在嘈杂环境中获取信息的人群提供服务 (Vanderheiden et al., 2013)。因此，该方法面向所有人，包括具有特定残障的人群，例如（概括而言）盲人和低视力用户、运动障碍用户、认知障碍用户、听力障碍用户以及言语障碍用户。

其主要目标是创建一种基础设施，以支持开发能够对应并尊重人类多样性（Human Diversity）全范围的解决方案。新系统需要允许潜在用户不仅在单台计算机上，而且在他们必须使用的所有不同计算机和信息与通信技术（ICT）设备上（如在家里、在工作中、在旅行时等）访问和使用这些解决方案。证书该基础设施将允许用户以功能性术语（functional terms）来声明需求（无论这些需求是否符合传统的残障类别），并允许服务提供商、众包机制（crowd sourcing mechanisms）和商业实体对这些需求做出响应。这意味着残障用户无需受限于其诊断类别（diagnostic categories），从而避免刻板印象（stereotyping），并承认每个人的需求都是不同的，且每个个体的需求可能会根据情境（context）而改变。

从技术上讲，该方法基于创建显式和隐式用户画像（explicit and implicit user profile）（存储在本地或云端），该画像能自动将主流产品和服务与必要的访问特性（access features）相匹配，并根据用户的偏好和使用情境（context of use）对其进行配置。该基础设施将由对以下内容的增强组成：

平台和网络技术旨在简化访问技术（access technologies）的开发、交付和支持，并为用户提供一种方式，使其能够自动地在任何计算机或其他信息通信技术（ICT, Information and Communication Technology）设备上，立即应用其所需的访问技术和手段。

目前，该基础设施处于概念化（conceptualization）和开发阶段。尽管其基本概念基于以往的工作和实现，但目前的努力旨在将这些概念综合应用于不同的平台和技术中，并以一种能够扩展以满足需求的方式进行。目前，多种交付选项正在开发和测试中，包括针对不同操作系统（OSs）、浏览器、手机、Web 应用程序、自助服务终端（kiosks）、交互式远程银行终端（ITMs）、数字电视（DTVs）、智能家居以及辅助技术（assistive technologies，包括云端和本地安装）的自动个性化（auto-personalization）。

## 42.4 设计方法与技术

以用户为中心的设计（User-Centered Design，见***Brief History***章节）的出现，促使了大量设计方法和技术的开发与实践。这些方法主要源自社会科学、心理学、组织理论、[创造力（Creativity）](https://www.interaction-design.org/literature/topics/creativity)和艺术，以及实际经验 (Maguire and Bevan 2002)。其中许多技术基于用户或用户代表直接参与设计过程。然而，绝大多数现有技术在开发时，考虑的是“平均”的身体健全用户（Able-bodied user）及其工作环境。

在全员设计（Design for All）中，这一前提不再成立，而“了解用户”这一基本设计原则演变为“了解用户的多样性（Diversity of users）”。因此，随之而来的问题是：在处理设计中的多样性时，哪些方法和技术可以被有效地采用，以及如何使用、修订和修改这些技术，以达到最佳目的。此外，由于在全员设计中，需要考虑具有不同特征和需求的一组或多组用户，这使得情况变得更加复杂 (Antona et al., 2009)。

当涉及非传统用户群体（Non-traditional user groups）时，参与过程中的实际操作和组织方面起着重要作用，并且对整个工作的成功至关重要。它们的重要性

不容低估。

在面对多样化的用户群体（Diverse User Groups）时，极少有设计方法（Design Methods）能够直接原封不动地应用。因此，核心问题之一在于如何针对参与者的特性，对方法进行适当的适配（Adapt）与微调（Fine-tune）。由于这些方法主要依赖于用户与设计过程（Design Process）中其他利益相关者（Stakeholders）之间的沟通，因此，参与用户的沟通能力应成为首要关注点。

### 42.4.1 观察法（Observation）

探索用户体验（User Experience）的常用方法源自人类学（Anthropology）、民族志（Ethnography）和民族方法学（Ethnomethodology）的田野研究（Field Research）（Beyer and Holtzblatt, 1997）。

直接观察（Direct Observation）是民族志方法的标志性方法之一。它涉及研究人员在用户执行某些活动时对其进行观察。田野观察的目标是深入了解在具体使用情境（Contexts of Use）中被体验和理解的用户体验。据称，在情境中考察用户能够更丰富地理解偏好、行为、问题与价值观之间的关系。

观察环节通常会进行视频录制，随后对视频进行分析。观察法和其他民族志技术的有效性可能有所不同，因为用户在意识到被观察时，往往会调整其执行任务的方式。观察者在过程中需要尽量不干扰用户，仅在需要澄清时提出问题。

在为残障用户和老年用户进行设计时，可以使用田野研究和直接观察法。该方法不特别依赖于参与者的沟通能力，因此在用户患有认知障碍（Cognitive Disabilities）时非常有用。研究人员已针对盲人用户开展了观察性研究，旨在通过开发设计洞察，增强盲人与家中常见的日常技术制品（Technological Artifacts）之间的交互，例如

腕表、手机或软件应用程序 (Shinohara, 2006)。

分析利用权宜之计（work-arounds）来弥补任务失败（task failures）的情况，能够为未来针对盲人的的人造物设计（artifact design）提供重要启示，例如触觉和听觉反馈，以及增强用户的独立性（user independence）。

直接观察研究（direct observation studies）的一个难点在于，在某些情况下，这类研究可能会被视为是对用户空间和隐私的一种“侵犯”，因此可能不被某些群体所接受，例如不愿在日常活动中暴露其困难的残障人士或老年人。

### 42.4.2 调查与问卷（Surveys and Questionnaires）

用户调查（User surveys）源自社会科学研究，其方式是向一组用户样本群体（sample population）发放一套书面问题，通常旨在获取具有统计学意义（statistically relevant）的结果。问卷在人机交互（Human-Computer Interaction, HCI）中被广泛使用，尤其是在早期设计阶段以及评估阶段。为了获得有意义的结果，问卷需要经过精心设计（Oppenheim, 2000）。

研究表明，年长者和年轻者在回答问卷的方式上存在年龄差异。例如，年长者比年轻者更倾向于选择“不知道（Don't know）”这一选项。当面对句法（syntax）复杂的问题时，他们似乎也更倾向于使用该答案。此外，他们的回答似乎会避开量表范围的极端值（extreme ends of ranges）。由研究人员直接向用户实施问卷，可能有助于获取更有用且更具洞察力的信息（Eisma et al., 2004）。居家访谈（In-home interviews）能有效地从用户那里获取大量信息，而这些信息是仅靠回答问卷无法获得的（Dickinson et al., 2002）。

由于问卷和调查面向的是广泛的公众，且研究者并不总是能掌握确切的用户特征（例如，用户是否使用盲文（Braille），或者是否熟悉计算机及辅助硬件和软件（assistive hardware and software）），因此这些问卷应当提供多种替代形式...

格式或以易于获取的电子形式（accessible electronic form）呈现。问题的表述（formulation of questions）应当简单且易于理解，这一点至关重要。此外，问题必须具有针对性（focused），以避免收集大量无关信息。

### 42.4.3 访谈（Interviews）

访谈是另一种受民族志启发（ethnographically-inspired）的用户需求收集方法。在人机交互（HCI）以及软件系统开发领域，这是一种常用的技术，通过对用户、利益相关者（stakeholders）和领域专家（domain experts）进行询问，以获取他们关于系统的需求或要求的信息 (Macaulay, 1996)。访谈可以是非结构化的（unstructured，即不遵循特定的问题顺序）、结构化的（structured，即问题提前准备并排序）或半结构化的（semi-structured，即基于一系列固定问题，但允许用户对回答进行扩展）。为了获得有价值的结果，选择具有代表性的用户（representative users）进行访谈至关重要。由系统开发团队的代表在客户现场（customer site）进行的访谈可以提供非常丰富的信息。

半结构化访谈已被用于识别盲人及肢体障碍用户在手机使用中遇到的可访问性（accessibility）问题 (Smith-Jackson et al., 2003)。对于老年人而言，将访谈作为收集用户需求的手段也被证明是一种有效的方法，不过，居家访谈（in-house interviews）可能会更高效，因为它们往往能引导用户自发地深入探讨个人经历，并演示所使用的各种个人设备。

显然，当涉及听障人士时，访谈会面临困难，此时可能需要手语翻译。访谈是

当目标用户群体由认知与沟通障碍人群（Cognitively and Communication Impaired People）组成时，[该方法]通常会被避免。近期，利用聊天工具进行在线访谈的趋势也逐渐显现。在这方面，一个显而易见的考量是，所使用的聊天工具必须具备无障碍性（Accessibility）并与屏幕阅读器（Screen Readers）兼容。

### 42.4.4 活动日记与文化探针（Activity Diaries and Cultural Probes）

日记记录（Diary keeping）是另一种受民族志（Ethnography）启发的方法，它提供了用户在一段时间内的行为自我报告记录（Self-reported record）(Gaver et al., 1999)。参与者需要记录他们在日常生活中所从事的活动。日记能够帮助识别那些通过短期观察无法发现的行为模式（Patterns of behavior）。然而，为了让参与者能够正确地使用日记，需要对其进行精心设计并提供相应的提示（Prompting）。日记可以是文本形式的，也可以是视觉形式的，例如采用图片和视频。

将日记的概念进一步泛化，“文化探针（Cultural Probes）”基于一套包含相机、录音机、日记本、明信片及其他物品的“工具包（Kits）”。这种方法已成功应用于针对敏感用户群体（如精神病康复患者和老年人）在家庭环境下的用户需求获取（User requirements elicitation）(Crabtree et al., 2003)。对于盲人以及患有运动障碍（Motor impairments）的用户来说，阅读和书写纸质日记可能是一个困难的过程。因此，在这些情况下应采用电子形式的日记或音频记录日记。

### 42.4.5 小组讨论（Group discussions）

[头脑风暴（Brainstorming）](https://www.interaction-design.org/literature/topics/brainstorming)起源于早期的群体创造力方法，其过程是让来自不同利益相关者群体（Stakeholder groups）的参与者通过非正式讨论，快速地产生尽可能多的想法。所有想法都会被记录下来，且禁止批评他人的想法。总的来说，当参与用户具备良好的沟通能力和技巧（不一定是口头的）时，头脑风暴被认为是合适的，但它也可以根据其他群体的需求进行调整。这可能会在讨论节奏和想法产生速度方面产生影响。

焦点小组（Focus groups）的灵感源自[市场调研（Market research）](https://www.interaction-design.org/literature/topics/market-research)技术。它们以讨论组的形式聚集不同层面的利益相关者代表。其核心理念是，每位参与者都能起到激发想法的作用，并且通过讨论过程建立起一种集体观点（Bruseberg and McDonagh-Philp, 2001）。焦点小组通常由一名引导者（Facilitator）带领六到十二人参加，并可能组织多次讨论会议。对残障用户采用焦点小组（Focus Groups）的主要优势在于，它不会歧视无法读写的人员，并且能够鼓励那些不愿单独接受访谈或认为自己没有什么可说的人参与其中。在焦点小组讨论期间，可以使用各种材料进行评审，例如故事板（Storyboards）（参见 ***Scenario, Storyboards and ***[***Personas***](https://www.interaction-design.org/literature/topics/personas) 章节）。如果目标用户群存在严重的沟通障碍，则不应采用此方法进行需求获取（Requirements Elicitation）。此外，讨论引导者有效地且高效地管理讨论至关重要，以确保所有用户无论其残障情况如何，都能积极地参与到过程中。

焦点小组已被用于获取学习障碍者（Learning disabled）的预期和需求，因为人们认为这种方法能产生最大数量的高质量数据 (Hall and Mallalieu, 2003)。它们允许一系列的

（旨在使）观点能够在短时间内以一种令人鼓舞且愉快的方式被收集。这至关重要，因为通常情况下，学习障碍（learning disabilities）人群的注意力时长（attention span）较短。

关于老年人，相关研究发现，很难让老年人的焦点小组（focus group）始终专注于讨论的主题 (Newell et al., 2007)。参与者往往会让讨论偏离主题，因为对他们而言，焦点小组会议是一个社交机会。因此，重要的是将社交聚会作为与 IT 研究人员合作体验的一部分，而不是简单地将他们视为参与者。

### 42.4.6 共情建模（Empathic modeling）

共情建模（Empathic modeling）是一种旨在帮助设计者/开发人员设身处地地体验残障用户处境的技术，通常通过残障模拟（disability simulation）来实现 (Nicolle and Maguire, 2003)。该技术最初被用于模拟各种日常环境任务中与年龄相关的视觉变化，旨在挖掘视障人士在不同建筑环境中的设计需求。共情建模可被定义为一种非正式技术，目前尚无关于其具体使用方法的指导方针。

- 针对特定残障的建模技术可以通过简单的设备来实现。
- 白内障（cataracts）导致的视觉障碍可以通过在旧眼镜上涂抹凡士林（Vaseline）来模拟。
- 全盲可以通过用围巾或绷带蒙住眼睛来轻松模拟。
- 全聋可以通过使用耳塞来轻松模拟。
- 上肢运动功能障碍（Upper limb mobility impairments）可以通过使用弹性带和夹板来模拟。

### 42.4.7 场景、故事板与用户角色

[场景（Scenarios）](https://www.interaction-design.org/literature/topics/user-scenarios) 广泛应用于需求获取（requirements elicitation）中。正如其名，场景是对交互过程的叙事性描述，包括用户和系统的操作以及对话。场景提供了详细且真实的示例，展示用户在特定语境下如何使用未来的系统来执行其任务。构建场景的主要目的是提供未来使用的示例，以辅助理解和明确用户需求，并为随后的 [可用性测试（usability testing）](https://www.interaction-design.org/literature/topics/usability-testing) 提供基础。场景有助于确定可用性目标（usability targets）以及可能的任务完成时间 (Carroll, 1995)。

故事板（Storyboards）是场景的图形化描绘，通过一系列图像展示用户操作或输入与系统输出之间的关系。故事板技术起源于电影、电视和动画行业。一个典型的故事板包含若干图像，用于描绘菜单、对话框和窗口等功能 (Truong et al., 2006)。

另一种与场景相关的方法被称为用户角色（personas）(Cooper, 1999)，该方法通过为每个最重要的用户群体创建包含姓名、性格和照片的用户模型来对其进行代表。

用户角色模型是真实或潜在用户的原型化表示（archetypical representation）。它并非是对某个真实用户或平均用户的描述

用户角色（Persona）代表了用户目标和行为的模式，并被汇总为对单个虚拟个体的描述。随后，可以通过特定用户角色的需求及其预期执行的任务，来评估潜在的设计方案。Zimmermann and Vanderheiden (2008) 提出了一种基于场景（Scenarios）和用户角色（Personas）的方法论，旨在捕捉老年人及残障人士的可访问性（Accessibility）需求，并构建可访问性[设计指南（Design Guidelines）](https://www.interaction-design.org/literature/topics/design-guidelines)。其基本原理是，使用这些方法具有巨大的潜力，能够让那些不熟悉可访问性问题的设计师和开发人员更具体、更清晰地理解这类需求。

然而，创建真正可靠且具有代表性的用户角色可能需要很长时间

此外，角色（Personas）可能并不适合呈现详细的技术信息（例如关于残障方面的信息），且其对代表性个体（representative individuals）的关注可能会增加捕捉人群中能力范围（range of abilities）的复杂性。

显而易见，故事板（Storyboarding）并不适合盲人用户，而对于视力受限（limited vision）或色盲（color-blindness）用户，则需要特别的关注。相反，对于聋哑或听力受损（deaf or hearing-impaired）用户而言，这似乎是一种极具前景的方法。

### 42.4.8 原型设计（Prototyping）

原型（Prototype）是一个交互系统（Interactive system）部分或全部内容的具体呈现。它是一种有形的实物（Tangible artifact），不需要过多的解释，可供最终用户和其他利益相关者（Stakeholders）用来构思并反思最终系统 (Beaudouin-Lafon and Mackay 2002)。

原型也被称为模拟模型（Mockups），其用途不同，因此形式也各异：
- **离线原型（Off-line prototypes）**（也称为纸质原型 Paper prototypes）包括纸上草图、图解故事板（Story-boards）、纸板模型和视频。它们创建速度快，通常处于设计的早期阶段，且在完成既定目标后通常会被丢弃。
- **在线原型（On-line prototypes）**则包括计算机动画、交互式视频演示以及使用界面构建工具（Interface builders）开发的应用程序。

原型在精确度、交互性和演进程度方面也存在差异。关于演进程度，快速原型（Rapid prototypes）是为特定目的而创建，随后被丢弃；迭代原型（Iterative prototypes）则不断演进，旨在完善某些细节（提高其精确度）或探索各种替代方案；而演进原型（Evolutionary prototypes）则旨在成为最终系统的一部分。

研究表明，在为残障人士设计创新系统时，使用原型的效果比访谈和焦点小组（Focus groups）等其他方法更有效，因为潜在用户

可能难以想象他们如何在新的情境（contexts）中执行熟悉的任务 (Petrie et al., 1998)。使用原型（prototypes）可以作为推测性讨论（speculative discussions）的一个有用起点，使用户能够就细节和首选方案提供丰富的信息。

原型通常通过用户测试（user-trials）进行评审，因此，所有与用户测试和评估相关的考量都至关重要。一个显而易见的推论是，为了能让残障人士参与测试，原型必须具备可访问性（accessible）。相比于纸质原型（paper prototypes），使用与最终系统高度相似的在线原型（on-line prototypes）可能更容易实现这一点。

### 42.4.9 用户测试（User trials）

在用户测试（User trials）中，产品由“真实用户”在相对受控或实验性的环境下，按照一套标准化的任务集进行试用。用户测试旨在进行可用性评估（Usability evaluation）。然而，对现有系统、竞争系统，或早期设计及原型（Prototypes）的评估，也是收集用户需求（User requirements）的一种方式 (Maguire and Bevan 2002)。

虽然用户测试的实施地点和方式存在很大差异，但每项用户测试都具有一些共同特征。其主要目标是通过让具有真实用户代表性的参与者在被观察的情况下使用产品执行实际任务，从而提高产品的可用性；随后对收集到的数据进行分析。在实地研究（Field studies）中，产品或服务则是在“真实生活”场景中进行测试的。

在用户测试中，每次测试环节都需要一个配备适当设备的房间。在规划[测试](https://www.interaction-design.org/literature/topics/test)时，应考虑到针对老年人及残障用户的测试可能需要比平时更长的时间，以便他们在没有焦虑和挫败感的情况下完成测试。

对最常用方法的研究表明，当涉及残障用户时，有必要对成熟的用户测试方法进行修改。例如，出声思考法（Think aloud protocol）在执行时已被调整以进行不同的应用

分别与聋哑用户和盲人用户进行用户测试（User Trials）(Chandrashekar et al., 2006; Roberts and Fels, 2006)。

此外，在指导过程中明确强调测试的对象是产品而非用户至关重要 (Poulson, Ashby and Richardson, 1996)，因为测试可能会揭示产品存在的严重问题，甚至导致某些任务无法完成。因此，确保用户不会感到不适，且不会将产品的失效归因于其自身的残障（Disability）非常重要。

当用户测试的参与者是上肢运动功能障碍（Upper Limb Motor Impairments）且肌肉控制能力较差的用户时，应确保测试环节时间较短，以防止过度疲劳。

对儿童进行应用程序测试需要特殊的规划和细心对待。目前已有针对儿童开展可用性测试（Usability Testing）的指南。这些指南提供了一个有用的框架，旨在从儿童那里获取最大程度的反馈，同时确保他们的舒适感、安全感和幸福感 (Hanna, Risden and Alexander 1997)。在儿童技术（Children’s Technology）领域，让儿童参与设计的每一个阶段尤为重要，因为对于成年设计师而言，很难（且往往是错误地）去假设儿童如何看待或解读数据。

### 42.4.10 协作式与参与式设计（Cooperative and Participatory Design）

参与式设计（Participatory Design）可以采用多种技术，包括头脑风暴（Brainstorming）、场景构建（Scenario Building）、访谈、[草图绘制](https://www.interaction-design.org/literature/topics/sketching)（Sketching）、分镜绘制（Storyboarding）和原型制作（Prototyping），并让用户充分参与其中。

传统上，伙伴关系设计技术被用于从成年用户那里收集用户需求（User Requirements）。然而，在过去几年中，许多研究项目展示了如何调整这些技术，以使非传统用户群体（如儿童和老年人）能够从技术设计过程中获益。

协作探究（Cooperative Inquiry）已被广泛用于让年幼的儿童在整个技术开发过程中拥有话语权（Druin, 1999）。这一做法基于这样一种观察：尽管儿童正逐渐成为频繁且经验丰富的技术用户，但他们很少参与到开发过程中。在这些努力中，研究者对过程中使用的传统用户需求收集技术进行了修改，以满足儿童的需求。例如，成年研究人员使用记录表，而儿童则使用带有少量文字的绘画来创建类似漫画的流程图。总之，将儿童作为平等伙伴引入设计过程被证明是一次非常有意义的体验，并且在开发新技术方面取得了令人兴奋的成果。随着发达国家人口老龄化的加剧，设计旨在支持老年人在家中生活的技术应用变得日益必要。然而，针对这一用户群体进行设计并非易事，因为开发人员和设计师往往无法充分理解该群体在利用影响其日常生活的技术时所面临的问题。当应用于这一用户群体时，人机交互（Human-Computer Interaction, HCI）的研究方法需要进行调整。这些方法必须考虑到老年人会经历广泛的与年龄相关的功能障碍（age-related impairments），包括视力、听力、记忆力和行动能力的下降，而这些因素最终会导致其自信心降低，并在定向（orientation）和信息吸收方面产生困难。

参与式设计（Participatory Design）技术可以帮助设计师缩小其与老年人之间的代际差距，并有助于更好地

理解这一用户群体的需求 (Demirbileka and Demirkan, 2004)。当老年人从项目初期就参与到设计过程（Design Process）中时，他们对使用技术的普遍恐惧感会降低，因为他们能感受到更强的掌控感，并确信设计过程的最终成果真正地考虑到了他们的需求。

### 42.4.11 设计方法与技术的总结

下表（改编自 Antona et al., 2009）总结了前几节讨论的设计方法与技术，为针对不同目标用户群体（target user groups）选择方法提供了一条指导路径。

|  | **残障（Disability）** | **年龄（Age）** |
|---|---|---|
| **运动（Motion）** | **视觉（Vision）** | **听觉（Hearing）** |
| **直接观察（Direct observation）** | ✓ | ✓ |
| **调查与问卷（Survey and questionnaires）** | ∎ | ∎ |
| **访谈（Interviews）** | ✓ | ✓ |
| **活动日记与文化探针（Activity diaries and cultural probes）** | ∎ | ∎ |
| **小组讨论（Group discussions）** | ✓ | ✓ |
| **共情建模（Empathic modeling）** | ✓ | ✓ |
| **场景、故事板与人物角色（Scenarios, storyboards and personas）** | ✓ | ✓ |
| **原型设计（Prototyping）** | ✓ | ✓ |
| **用户测试（User trials）** | ∎ | ∎ |
| **协作设计与参与式设计（Cooperative and participatory design）** | ✓ | ✓ |

✓ **适用**  **∎** **需要修改与调整**  **⌧** **不推荐**
**表 42.1**

## 42.5 交互技术（Interaction Techniques）

### 42.5.1 语音（Speech）

语音交互（Speech-based interactions）允许用户在不使用键盘、鼠标、按钮或其他物理交互设备（physical interaction devices）的情况下，与计算机或计算机相关设备进行通信。语音交互利用了人们在生命早期就已掌握的技能，因此比键盘等其他技术具有更强的自然性（natural）潜力。语音交互对于儿童、老年人以及残障人士（individuals with disabilities）具有特殊的意义 (Feng and Sears, 2009)。此外，当用户的手正忙于其他任务（例如驾驶汽车、执行医疗操作），且传统的键盘和鼠标无法使用或不适用时，语音是一种极具吸引力的输入替代方案（input alternative）。根据所采用的输入和输出通道（input and output channels），语音交互可分为三类：

1. 语音输出系统（Speech output systems），包括仅将语音用于输出，而利用键盘和鼠标等其他技术进行输入的应用程序。常用于视觉障碍（visual impairments）人士的屏幕访问软件（Screen access software）就是语音输出的一个例子。
2. 语音识别系统（Speech recognition systems），包括利用语音进行输入并利用其他模态（modalities）进行输出的应用程序，例如图形用户界面（Graphical User Interface, GUI）中的语音光标控制和语音听写系统（speech-based dictation systems）。
3. 口语对话系统（Spoken dialogue systems），包括利用

语音既可作为输入也可作为输出，例如电话系统以及带有语音反馈的基于语音的环境控制系统。

典型应用包括：
- 电话系统，这类系统倾向于使用较小的输入词汇量（input vocabularies）以及语音输出；以及环境控制应用，这类应用同样使用较小的输入词汇量，并可能支持语音或非语音输出；
- 与图形用户界面（Graphical User Interfaces, GUI）的基于语音的交互，可支持导航、窗口操作以及各种其他基于命令的交互，其输入词汇量差异很大，从仅几个单词到数百个单词不等；
- 听写应用（dictation applications），支持用户撰写电子邮件、信函和报告，以及完成较小的任务，例如在允许自由格式输入的表单中填写部分内容。

迄今为止，使用基于语音的用户界面最关键的障碍可能是识别错误（recognition errors）以及繁琐的恢复过程（recovery process）。

![](https://public-media.interaction-design.org/images/encyclopedia/design_4_all/Figure11.jpg)
作者/版权持有者：Emerging Technologies。版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅[版权声明](https://www.interaction-design.org/about/terms-of-use)页面的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

**图 42.11**：语音交互（Speech interaction）

使用小词汇量（Small Vocabularies）可以显著降低识别错误率（Recognition Error Rates）。基于语音的命令与控制系统（Speech-based Command and Control Systems）允许用户通过说出预定义命令（Predefined Commands）进行交互。此类系统通常通过将声学信号（Acoustic Signal）与当前可用命令的相应模型进行匹配，从而将用户的话语（Utterances）转换为系统命令。

部分系统采用简单的菜单，允许用户在每个阶段使用简单的语音命令选择合适的选项。其他系统则尝试与用户建立对话（Dialogue），旨在尽可能快地收集必要信息并完成交易。

目前存在多种基于语音的命令与控制解决方案，它们可以模拟传统的键盘和鼠标，允许用户通过语音操作传统的图形用户界面（Graphical User Interfaces, GUI）。这些解决方案被一些难以使用传统交互方案的肢体残障人士所采用。基于语音的命令与控制系统还被用于环境控制应用（Environmental Control Applications），允许用户操作恒温器、灯光、电视以及许多其他设备。- 剩余 6 小时 49 分 4 秒关闭：[ The Practical Guide to Usability](https://www.interaction-design.org/courses/the-practical-guide-to-usability)
- 剩余 2 天关闭：[ Accessibility: How to Design for All](https://www.interaction-design.org/courses/accessibility-how-to-design-for-all)

基于语音的听写系统（Speech-based dictation systems）允许用户通过语音生成大量文本。语音识别器（speech recognizer）用于将音频信号转换为文本。听写系统使用了更大的词汇量（vocabulary）。因此，听写应用程序的准确率往往低于命令与控制系统（command and control systems），通常建议用户创建个人语音配置文件（personal speech profile）以提高识别准确率（recognition accuracy）。在用户、环境和任务条件允许的情况下，有效的多模态错误修正方案（multimodal error correction solutions）可以提供一种高效的替代方案。

大词汇量听写系统（Large vocabulary dictation systems）可以作为传统键盘和鼠标的强大替代方案，允许生成各种文档，如电子邮件、论文和商业报告。重要的是，产出此类文档的能力可以显著增加教育和职业机会。对于普通大众而言，此类系统可以作为一种有用的替代方案，降低因使用键盘或鼠标而导致重复性劳损损伤（repetitive strain injuries）的风险。

### 42.5.2 触觉感知（Haptics）

手部具有执行各类操作任务（manipulation tasks）的卓越能力，从处理微小细节到搬运沉重物体。通过皮肤获取的触觉信息（tactual information）对操作性能至关重要，但在手部运作时，皮肤传感器与肌肉、腱和关节中的传感器之间存在着紧密的协作。神经系统有效地协调了各类感觉信息与执行动作的肌肉。

作为一种皮肤感觉，触觉（touch）通常被认为是环境刺激的被动接收器。然而，手部也依赖于探索（exploration）来收集信息。这种主动触觉通常被称为 *触觉感知（haptics）*。

在交互中使用触觉感知可以支持视觉和听觉，并为视觉或听觉等感官功能受损的人群提供替代方案。同样的界面可被所有用户在视觉占用（eyes-busy）的情况下使用，或被视障人士用于计算机操作。此外，触觉感知还具有帮助运动功能障碍（motor problems）人群的潜力，因为力反馈（force feedback）可用于增强运动动作的力量或稳定性 (Jansson and Raisamo, 2009)。

与视觉相比，触觉感知有时能提供更高级的信息，例如关于物体的重量以及表面的纹理和硬度。然而，在

提供场景的概览。通过触觉（haptically）获取场景概览可能是一项艰巨且耗时的任务，需要对场景进行多次探索。在分配视觉显示（visual displays）与触觉显示（haptic displays）的任务时，考虑这些差异至关重要。两种感官覆盖的空间范围也是一个非常重要的区别：视觉允许感知数公里外的信息，而触觉主要局限于手臂可触及的范围内。

触觉的一个特性是远程触摸（remote touching），即通过某种媒介体验远处的物体。手可以通过工具获取信息，并将信息定位到工具的末端。视障人士（visually impaired persons）使用长杖（long cane）在触碰地面时可以感知地面的属性。视障人士经常使用低技术辅助工具，如长杖、盲文（Braille）和凸点图（embossed pictures）。在所有这些情况下，触觉（haptic sense）与环境之间的交互都至关重要。如果能提供适当的信息并利用触觉的自然能力，即使是技术上非常简单的辅助工具（如长杖）也能非常高效。

视障人士可以通过双手获取视觉字母和其他符号的触觉等效物（tactile equivalent）来阅读文本，最常见的形式是盲文，它被编码在一个以凸起形式呈现的六点（有时是八点）矩形矩阵中，并且

...由手指读取。此外，还有一种由针矩阵（matrices of pins）组成的机械盲文版本。点刺激（point stimuli）矩阵可被视为低空间分辨率（spatial resolution）物理表面的表示。此类矩阵利用能够提供更先进信息的t技术，取代或补充了低技术辅助工具。其中一种方案是在皮肤接触面上呈现一个扩展矩阵。通过动态地将部分针头升至矩阵其余部分之上，该矩阵能够形成特定的图案。这些针头可以是静态的，也可以是振动的。

![](https://public-media.interaction-design.org/images/encyclopedia/design_4_all/Figure12.jpg)
作者/版权持有者：handytech.de。版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因为无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面上的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

**图 42.12**：来自 [www.handytech.de](http://www.handytech.de/) 的盲文显示器（Braille display）

触觉显示器（Haptic displays）之于触觉学（haptics），正如计算机屏幕之于视觉、扬声器之于听觉。它们是通过计算机实现对虚拟对象和场景进行触觉操纵（haptic manipulation）的设备。它们不仅能为视力正常的人提供视觉和听觉信息的补充，因此受到关注，而且对于视障人士而言，它们可以作为...的替代方案

在这个意义上，触觉显示设备（Haptic displays）通过用户手中的触控笔（stylus）、指套（thimble）或类似工具的末端与虚拟对象表面的“碰撞”来提供力反馈（force feedback）。除了对象的形状外，硬度/柔软度、纹理和摩擦力等表面属性也可以在 3D 中进行渲染（rendered），以进行触觉探索（haptic exploration）。触觉技术在自然情境（natural contexts）中运作时具有巨大的潜力，但目前开发的触觉显示设备仅利用了其中一部分。最主要的限制在于接触面（contact surfaces）的数量和尺寸。当人们自然地使用裸手时，存在多个接触面，且每个接触面的延伸范围大致至少为一个指腹（finger pad）。在当今的触觉显示设备中，接触点的数量非常少，大多数情况下仅有一个。此外，除了少数设备外，接触面通常仅为一个极小的点。这些与...的差异

对自然触觉（natural haptics）的关注对于触觉显示设备（haptic displays）的效率具有重要影响。

![](https://public-media.interaction-design.org/images/encyclopedia/design_4_all/Figure13.jpg)
作者/版权持有者：Novint Technologies Inc.。版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅[版权声明](https://www.interaction-design.org/about/terms-of-use)页面的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

**图 42.13**：一种触觉设备

### 42.5.3 基于扫描的交互（Scanning-based interaction）

扫描是一种针对上肢严重运动功能障碍（severe motor impairments in upper limbs）用户的交互方法 (Ntoa et al, 2009)。该技术的核心理念是消除通过鼠标或键盘等传统输入设备（traditional input devices）与计算机应用程序进行交互的需求。相反，用户可以使用开关（switches）进行交互。扫描软件使得构成图形用户界面（graphical user interface, GUI）的交互对象可以通过开关来访问。它会遍历交互式界面元素，并在用户按下开关时激活所指定的元素。在大多数扫描软件中，交互元素会依次获得焦点并被高亮显示（例如，通过彩色标记）。此外，为了避免使用键盘输入文本，通常会提供一个屏幕键盘（on-screen keyboard）。

在扫描过程中，焦点标记（focus marker）会按照预定义的顺序（例如，从左到右，从上到下）扫描界面并依次高亮显示交互对象。扫描可以是自动的，也可以是手动的。在第一种情况下，在用户处于预定义的时间间隔内无操作（即未按下激活开关）后，标记会自动从一个界面元素移动到下一个；该时间间隔通常可以根据用户需求进行自定义。在手动扫描（manual scanning）中，用户将焦点标记移动到下一个界面元素。

用户可以通过使用开关（Switch）在任何想要的时候进行操作。激活开关（Activation switches）多种多样，包括手部、手指、足部、舌头或头部开关，以及呼吸控制开关或眼动追踪（Eye-tracking）开关。此外，任何键盘按键（例如空格键）或鼠标点击也可以作为开关使用。

![](https://public-media.interaction-design.org/images/uploads/6ef8c5890d90207e20986907f7df416f.jpeg)
Author/Copyright holder: Stephanidis. Copyright terms and licence: 
All Rights Reserved. Reproduced with permission. See section 
"Exceptions" in the [copyright terms](https://www.interaction-design.org/about/terms-of-use) below.
**图 42.14**：基于扫描的交互（Scanning-based interaction）

扫描技术（Scanning techniques）有多种类型，主要区别在于访问单个交互元素的具体方式。最常用的扫描技术包括：
- 块扫描（Block scanning）：将项目分组为块，旨在最大限度地减少用户输入并提高交互速度。
- 双向扫描（Two-directional scanning）：用户通过指定被扫描屏幕上的坐标来选择元素。首先是纵向扫描，由一条线从屏幕顶部向底部移动；然后是横向扫描，由一个指针沿选定的水平线移动。
- 八向扫描（Eight-directional scanning）：被多种鼠标模拟软件（Mouse emulation software）产品所采用。在这种方法中，鼠标指针可以

根据用户的偏好，指针沿八个方向之一移动。为了实现这一点，指针图标在特定的时间间隔内变换，以指示这八个方向之一。用户通过按下开关（switch）来选择所需方向，随后指针开始向该方向移动。一旦指针到达用户想要选择的特定屏幕位置，可以通过开关或按键将其停止。

- 层级扫描（Hierarchical scanning）：在这种模式下，对窗口及其窗口元素的访问是根据它们在窗口层级结构（hierarchical structure）中的位置来提供的。元素通常根据其层级被分为组和子组（例如，工具栏作为其包含的单个按钮的容器，列表框作为包含的列表项的容器，等等）。
- 簇扫描（Cluster scanning）：在这种模式下，屏幕上的元素根据其位置被划分为若干目标簇（clusters of targets）。
- 自适应扫描（Adaptive scanning）：在这种模式下，系统的扫描延迟（scan delay）会根据对用户性能的测量在运行时（runtime）进行调整。

具有嵌入式扫描（embedded scanning）功能的应用程序在开发之初就旨在支持扫描，从而使运动障碍（motor impairments）人士能够使用。然而，用户需要使用多个应用程序才能完成各种日常计算任务（例如，网页浏览器、电子邮件客户端、娱乐软件、教育软件、文档编辑软件等）。扫描工具使用户能够

操作操作系统的图形环境，从而无需使用各种专用应用程序来执行日常任务。具有内置扫描功能的键盘和鼠标模拟软件（Keyboard and mouse emulation software）在扫描工具中十分普及，因为它们能够确保用户在无需使用传统键盘和鼠标的情况下实现交互。研究者已经开发出多种实现键盘和鼠标模拟的方法 (Evreinov, 2009)。具有扫描支持的鼠标模拟软件允许用户通过一个或两个开关（Switches）来控制鼠标指针。

### 42.5.4 眼动追踪（Eye tracking）

人们使用眼睛主要为了观察，但也会利用视线（Gaze）来增强沟通。一个人视线的方向揭示了其视觉注意力（Visual Attention）的焦点，因此可以通过眼动追踪来实现沟通。

在某些情况下，视线可能是个体唯一可行的沟通方式。例如，在发生严重事故后，一个人可能无法说话，在这种情况下，医生可能会要求对方“向上看”或“向下看”，以此作为理解和同意的信号。通过在用户的视野中添加具有实际意义的物体，这种沟通方式可以从简单的“是”或“否”指令扩展为一套完整的沟通系统。这种方法的一个例子是视线沟通板（Gaze communication board），该板上附有图片、指令或字母。用户通过注视板上的项目来进行选择，而其他人则通过追踪用户的视线来解读其传递的信息。这样的系统展示了眼动追踪在沟通方面的基础能力。基于计算机的注视通信系统（Computer-based Gaze Communication Systems）已经得到开发，其中眼动追踪设备（Eye Tracking Device）和计算机取代了手动通信板（Manual Communication Board）(Majaranta, Bates and Donegan, 2009)。在这些眼动追踪系统中，字母（或任何其他符号、图像或对象）显示在用户面前的计算机屏幕上。用户只需通过注视这些项目来指向并选择它们，由眼动追踪设备记录其眼动，并由计算机程序对其眼动进行分析和解释。这样的系统构成了一个基础的注视通信系统。

近年来的技术进步显著提高了眼动追踪系统的质量，使得更广泛的人群现在能够从眼控（Eye Control）技术中获益。

![](https://public-media.interaction-design.org/images/encyclopedia/design_4_all/Figure15.jpg)

作者/版权持有者：Designtechnica Corporation。版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因为无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面上的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子部分）。

**图 42.15**：眼动追踪（Eye Tracking）

正常的眼动是由对感兴趣对象的注视（Fixations）构成的。

（200 - 600 毫秒），其间伴随着在这些物体之间快速的扫视（Saccades, 30 - 120 毫秒），以及偶尔对移动物体的平滑追踪（Smooth Pursuit，即跟随移动目标）。由于敏锐视觉（Acute Vision）的黄斑中心凹（Fovea）区域相当小，人们实际上需要将视线几乎直接地指向感兴趣的物体，才能获得该物体的清晰视野（大约在 1 度以内），这使得追踪视线方向（Gaze Direction）成为可能：因此，如果眼睛指向某个物体，用户很可能正在观察并感知该物体。眼球运动在很大程度上也是无意识且自动的；人们通常不需要思考该看哪里。然而，在需要时，人们可以随意控制视线，从而使眼控（Eye Control）成为可能。

计算能力的提升使得实时采集眼动追踪数据（Eye Tracking Data）成为可能，同时也推动了直接面向残障人士的辅助技术系统（Assistive Technology Systems）的发展。当前的眼动追踪技术已演变为一系列技术：电眼图（Electro-oculography, EOG），用户在眼睛周围佩戴小型电极以检测眼睛位置；巩膜接触镜/搜索线圈（Scleral Contact Lens/Search Coil），用户在眼睛上佩戴带有磁线圈的接触镜，由外部磁系统进行追踪；视频眼动记录法（Video-oculography, VOG）或照片眼动记录法（Photo-oculography, POG），通过拍摄眼睛的静态或动态图像来确定其位置；最后是基于视频的瞳孔/角膜反射结合技术（Combined Pupil/Corneal Reflection Techniques），该技术通过人工方式扩展了 VOG...

通过同时照射眼睛的瞳孔和角膜来提高追踪精度。目前大多数可用的眼控系统（Eye Control Systems）是基于视频的角膜反射（Corneal Reflection）技术。

传统上，无法移动但能良好控制眼球运动的人群是眼动追踪系统（Eye Tracking Systems）的最佳适用对象。与能够移动的人（无论是自愿还是非自愿地移动，例如脑瘫 [Cerebral Palsy] 患者）相比，身体不动可以使追踪更加容易。然而，眼控对于所有用户来说可能仍然是一个切实可行的选择，因为与基于手动开关（Manual Switch）或头部指向（Head Pointing）的系统相比，眼控可能更快且更不易疲劳。眼球运动速度极快，视线指向（Gaze Pointing）在手动控制的鼠标光标到达目标之前，就能定位并指向目标。

从一个人的眼球运动中解读其意图并非易事。眼睛主要是一个感知器官（Perceptual Organ），通常不用于控制，因此出现了一个问题：如何将随意的观看与有意的视线驱动指令区分开来。如果计算机屏幕上的所有对象都对用户的视线做出反应，就会导致所谓的“迈达斯之触”（Midas Touch，或称“迈达斯之视” [Midas Gaze]）问题：“无论你看向哪里，都会激活某些东西”。显而易见的解决方案是将视线指向与另一种选择模态（Modality）相结合。如果用户能够产生一个独立的“点击”动作，那么这个点击就可以用来选择

聚焦项。这可以是一个开关（switch）、一次眨眼（blink）、一次单眼眨眼（wink）、额头上的皱纹，甚至是微笑或任何其他可用的肌肉活动。眨眼和单眼眨眼可以通过用于分析眼动（eye movements）的同一视频信号来检测，从而无需额外的开关设备。如果用户仅能移动眼睛，那么独立的开关就不是一个可行选项，系统必须能够将随意浏览（casual viewing）与有意识的眼控（intentional eye control）区分开来。最常见的解决方案是使用停留时间（dwell time），即一种持续时间长于典型注视（fixation）（通常为 500-1000 毫秒）的延长注视。目前大多数眼控系统都提供可调节的停留时间作为选择方法之一。要求用户长时间注视确实能减少误选（false selections），但这会让用户感到不适，因为超过 800 毫秒的注视通常

被眨眼（blinks）或眼跳（saccades）所中断。解决“迈达斯接触问题（Midas touch problem）”的另一种方案是使用特定的选择区域或屏幕上的按钮。

增加屏幕上目标的尺寸可以提高眼球注视输入（eye gaze input）的性能。增大屏幕对象的尺寸，可能决定了用户是否能够使用眼动追踪设备（eye-tracking device）。然而，一次仅显示少量的大尺寸屏幕按钮，会限制全尺寸键盘（如完整的 “qwerty” 键盘）的使用。相反，按键和控件可以通过菜单和子菜单进行层级化组织，并且可以使用自动词预测（automatic word prediction）等特殊技术来加速文本输入过程，同时采用模糊的或不断变化且具有自适应性的键盘布局。

注视指针（Gaze pointing），即将计算机鼠标光标置于用户在屏幕上注视的位置，是一种直观且几乎不需要培训的方法，因为它模拟了普通桌面鼠标的操作。将眼球运动直接绑定到鼠标运动，便创建了“眼球鼠标（eye mouse）”。这看起来像是一个简单的解决方案；然而，有几个问题必须予以考虑。

眼睛在不断移动，即使在注视（fixating）时也会产生微小的修正运动。如果这种“眼球鼠标”的光标在没有任何平滑处理（smoothing）的情况下跟随眼球运动，光标的移动会显得非常抖动，且由于光标本身会吸引注意力，用户将难以集中精力进行指针操作。

使用鼠标模拟（mouse emulation）的主要好处是它能够访问基于窗口的图形用户界面（window-based graphical user interfaces）。此外，它还允许使用任何现有的辅助访问软件（access software），例如环境控制应用程序（environmental control applications）或“停留点击（dwell click）”工具。然而，需要注意的是，对于没有任何计算机控制方法经验的重度残障人士来说，掌握注视点眼控系统（gaze-pointing eye control system）可能需要一段时间。

使某些眼动追踪系统（eye tracking systems）更适合残障人士的因素，是该系统所支持或自带的应用程序（软件）。

![](https://public-media.interaction-design.org/images/encyclopedia/design_4_all/Figure16.jpg)
*作者/版权持有者：DynaVox。版权条款和许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在无法获得许可的情况下使用。请参阅页面上的 [版权声明](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分（以及“allRightsReserved-UsedWithoutPermission”子节）。*

**图 42.16**：眼动追踪用户界面

眼动输入（Eye typing）通常是使用眼控系统的用户首先实现并尝试的应用程序。由于停留时间（dwell-time durations）限制了最高输入速度，眼动输入的效率可能较低，通常每分钟词数（words per minute, wpm）低于 10 个词。当用户通过注视进行输入时，他们无法看到文本出现在文本输入框中的...

与此同时，用户通过在屏幕键盘上对某个按键进行“眼部点击（eye pressing）”来选择字母。为了回顾目前已输入的内容，用户需要将视线从屏幕键盘移至文本输入区域。这种视线转移可以通过增加听觉反馈（auditory feedback）来减少，例如发出可听见的“点击声”，或者在输入每个字母时将其读出。适当的反馈还能提高性能并提升准确率。为停留时间（dwell-time）进度和选择过程提供适当的反馈，可能会显著提高性能，并让用户在进行眼控（eye control）时感到更加愉悦。

当物理点击按钮时，用户能感受到并听到按钮的“点击声”。当使用“眼部点击”进行操作时，这种额外的确认性反馈（听觉或触觉反馈 [tactile feedback]）是缺失的，因此必须予以提供。除了眼动输入（eye typing）之外，还有几种（专门的）眼控应用程序，例如眼动绘画、眼动音乐、网页浏览、电子邮件、游戏等。许多面向残障人士的商业眼控系统中都包含了此类应用程序。

尽管如此，Donegan et al. (2005) 对用户需求进行的一项广泛研究表明，迄今为止，眼控仅能有效满足有限范围的用户需求，且仅能被少数残障人士有效使用。此外，适合通过眼睛进行轻松且毫不费力控制的应用程序范围也十分有限。

### 42.5.5 手势与头部追踪（Gestures & head tracking）

在人机交互（Human-Computer Interaction, HCI）领域，人们很早就意识到，除了典型的鼠标和键盘之外，丰富用户与计算机系统的交互方式是一项挑战。手势是人类表达的一种强大特征，既可以独立使用，也可以作为增强口语表达的手段。

在技术层面，手势识别（Gesture Recognition）有多种实现方法，采用了各种成像与追踪设备或小工具。可穿戴设备（Wearable devices）为基于手势的交互提供了一种非侵入式（unobtrusive）的解决方案，它们不仅可以作为输出设备，还可以作为输入设备。利用许多消费电子产品中配备的基于加速度计（accelerometer-based）的信息，也可以实现手势识别。计算机视觉（Computer vision）也被用于识别用户的裸手手势。Zabulis et al. (2009) 总结了文献中提出的许多方法，这些方法利用了多种类型的视觉特征，如肤色、形状、运动以及手部解剖模型（anatomical models of hands）。最后，近期的研究工作探讨了利用 Microsoft Kinect 等游戏设备进行手势识别的问题。

![](https://public-media.interaction-design.org/images/encyclopedia/design_4_all/Figure17.jpg)
作者/版权持有者：Microsoft Corp.。版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因为无法获得许可）。请参阅“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

[版权声明](https://www.interaction-design.org/about/terms-of-use) 页面。

**图 42.17**：可穿戴手势识别系统

基于手势的界面（Gesture-based interfaces）可用于满足残障人士的需求，例如用于家庭自动化（Home automation）（Starner et al., 2000）。然而，需要注意的是，残障人士与基于手势系统的交互及其适配问题，因为对于患有手部或认知障碍（Cognitive disabilities）的用户来说，交互可能会存在相当大的局限性。此外，应注意为盲人和低视力用户提供适当的系统反馈（System feedback）。当面对因年龄或疾病而具有多种局限性的用户时，手势界面会变得更具挑战性。

技术的最新进展使得我们不仅可以利用手势，还可以利用用户的头部和身体动作作为向计算机系统提供信息的手段。计算机控制是一个使用基于头部的交互（Head-based interaction）的领域，主要面向残障人士或情境性障碍（Situationally disabled）用户。例如，使用双目摄像头（Stereo camera）和头戴式追踪设备（Head-mounted tracking device）的头部追踪（Head tracking）已被用于桌面和交互式房间环境中的光标控制（Cursor control）和目标选择（Target selection）任务（Morency et al., 2005）。其他方法建议使用鼻子进行光标控制以及通用的免手操作游戏和界面（Gorodnichy and Roth, 2004），考虑到鼻子...

作为人脸中最凸出且距离头部旋转轴（Axes of head rotation）最远的部分，[它]具有最大的运动自由度（Motion Freedom）。另一种新颖的交互技术采用了通过头部手势（Head Gestures）操作的 3D 音频径向饼图菜单（3D Audio Radial Pie Menu）来选择项目 (Brewster et al., 2003)。在“免视（Eyes-free）”移动环境下进行测试时，用户认为此类新颖的交互方式舒适且可接受。用于计算机控制的商业产品包括头部鼠标控制（Head Mouse Control）以及头部控制开关（Head-controlled Switches）。头部鼠标控制设备使用红外无线光学传感器或高分辨率摄像头，通过追踪用户佩戴在额头、眼镜、帽子等方便位置的一个微小一次性标记点（Disposable Target），从而将用户的头部运动转化为与之成正比的计算机鼠标指针运动。

### 42.5.6 脑接口（Brain Interfaces）

脑接口（Brain Interfaces）被定义为一种实时通信系统（real-time communication system），旨在允许用户在不通过大脑正常的输出路径（如语言、手势或其他运动功能）的情况下，仅利用大脑的生物信号（bio-signals）自愿地发送信息。

这类通信系统对于那些大脑部分区域仍活跃，但无法与外界沟通的残障人士至关重要。对于严重运动功能障碍者，脑接口可以提供新的增强通信通道（augmentative communications channels）(Gnanayutham and George, 2009)。

脑接口分为两种类型：侵入式（invasive，通过手术将探针插入大脑内部获取信号）和非侵入式（non-invasive，将电极放置在身体外部）。由于侵入式脑接口涉及的风险、难度和要求较高，非侵入式脑接口成为辅助技术设备的首选。非侵入式技术无需使用任何手术手段，通过将电极放置在面部、颅骨或其他身体部位来收集脑接口的控制信号。获取的信号首先经过放大，然后经过滤波，最后从模拟信号转换为数字信号（analogue to a digital signal）。生物电势（Bio-potentials）是来自大脑的电信号，可以通过头骨、前额或身体其他部位获取（由于这些区域的生物电势较为丰富，因此主要使用头骨和前额）。每种生物电势都具有其独特的特征，例如幅度（amplitude）、频率（frequency）、提取方法（method of extraction）和发生时间（time of occurrence）。每位脑损伤患者（除持久性植物状态患者外）都能以不同程度的一致性产生一种或多种此类生物电势。脑损伤患者可以根据其能够产生的生物电势的可靠性来操作脑机接口（Brain Interfaces）。目前的脑机接口数据传输速率最高可达 68 bits/秒。

脑电图（Electroencephalography, EEG）用于测量由思考或想象的动作引起的大脑电活动。脑电信号（Electroencephalographic signals）可以通过放置在头皮或前额的电极来采集。

肌电信号（Electromyographic signals）和眼电信号（Electrooculargraphic signals）是非侵入式脑机接口（non-invasive Brain Interfaces）中最合适的两种生物电势（bio-potentials）的主要候选方案。它们属于高幅度（high amplitude）生物电势，与其他生物电势相比，患者更容易产生这类信号。

开发人员会选择不同的电极位置，例如电极帽（electrode caps）、具有不同位置和电极数量的电极头带（electrode headbands），或者采用国际 10-20 系统（International 10-20 System）。电极帽可能包含多达 256 个电极，尽管典型的电极帽使用 16、32、64 或 128 个位置，且每种电极帽都有其潜在的误差来源。高密度电极帽（High-density caps）可以提供更多信息，但在实践中，它们难以用于实时通信（real time communications）。这是因为从如此大量的电极中获取的生物电势可能需要大量的离线处理（off-line processing），才能解析出用户试图表达的内容。目前关于电极位置和数量仅有一个公认的标准，即国际 10-20 电极系统（International 10-20 System of electrodes）。

![](https://public-media.interaction-design.org/images/encyclopedia/design_4_all/Figure18.jpg)

作者/版权持有者：Honda。版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅“例外（Exceptions）”章节（以及

subsection "allRightsReserved-UsedWithoutPermission")，详见 [版权声明（copyright notice）](https://www.interaction-design.org/about/terms-of-use) 页面。

**图 42.18**：脑机接口（Brain Interface）技术

脑机接口可用于通过包含单词或短语的目标进行通信，执行设备的开关控制，启动计算机应用程序，通过选择单个单词进行拼写，拨打电话，浏览网络，操作康复机器人，控制轮椅等。

到目前为止，脑机接口尚未表现出足够的可靠性，以至于主流软件制造商将其集成到主流操作系统和应用程序中。许多脑机接口的研究应用仅限于实验室实现，且从脑损伤群体中获得的测试结果有限。目前研究速度正在加快，辅助技术（Assistive Technology）领域正取得良好进展。

该技术前景广阔，但仍需在实际场景中对残障参与者进行更多评估。尽管许多脑机接口设备展现出了潜力，但残障群体对它们的使用仍然有限。显然，需要将这项技术从实验室移至实际场景，如养老院和医院。目前，可穿戴无线脑机接口（Wearable Wireless Brain Interfaces）的研究也在进行中，其中建议使用 Bluetooth 等技术来传输和接收参与者的信号。

### 42.5.7 手语（Sign language）

与计算机的交互涉及文本的阅读或编写。乍一看，聋人用户在读写能力方面似乎并不处于劣势。然而，需要读写的界面也有可能使许多聋人用户处于不利地位（disenfranchise）。

全球有数百万聋人及听力受损（hard of hearing）的人士使用手语进行交流。手语是自然产生的语言，其语言结构（linguistic structures，例如语法、词汇、词序等）与口语截然不同。例如，美国手语（American Sign Language, ASL）是美国约 50 万人的主要交流方式。ASL 是一种完整的自然语言，包含多种使其与英语区分开来的语言现象（linguistic phenomena）。手语并非基于该地区的口语。ASL 是一种视觉语言，通过手语者的面部表情、眼神、头部动作、肩部倾斜、手臂动作和手形来传递语言信息；然而，仅仅知道手语者的身体如何移动是不足以理解一个 ASL 句子的。还需要记住他们身体周围的“手语空间（signing space）”是如何被代表讨论实体的虚拟占位符（imaginary placeholders）所填充的。

有许多因素决定了听力受损者是否会使用手语，其中包括其家庭

……环境、教育经历、听力损失的起始年龄以及听力损失程度。手语使用者（Signers）构成了聋人社区（Deaf Community），其成员身份更多地是由共同的语言而非听力损失程度决定的。

事实上，成年后出现听力损失的人往往不会成为手语使用者或该社区的成员。与大众的预期相反，手语并非通用语言；世界各地的聋人社区都有其原生的手语。聋人通常将手语作为其第一语言（First Language）习得，并且在这种第一语言中最为流畅和自在。

很少有计算机用户界面（Computer User Interfaces）能为聋人用户提供足够的适配（Accommodation）。尽管许多聋人具备熟练的阅读能力，但并非所有手语使用者都能达到这一熟练程度。例如，研究表明，美国大多数聋人高中毕业生的英语阅读水平仅为四年级——这意味着大约 18 岁的聋人学生的阅读水平更接近于 10 岁的健听（Hearing）学生。对于那些在读写方面存在困难的聋人群体而言，手语界面（Sign Language Interfaces）是必不可少的 (Huenerfauth and Hanson, 2009)。

一个将英文文本翻译为美国手语（ASL, American Sign Language）动画的机器翻译系统（Machine Translation System）可以提高手语使用者使用用户界面的可访问性（Accessibility）。与其在电视屏幕、电话显示屏上呈现书面文本，

...或计算机显示器，它们都可以改为显示美国手语（American Sign Language, ASL）。

此外，手语识别（Sign Language Recognition）技术也能让聋人手语使用者受益。通过 ASL 向计算系统输入指令的能力将使聋人手语使用者的交互（Interaction）更加自然；而系统将手语输入翻译为英文文本或语音的能力，则能为英语读写能力（English literacy）较低的聋人手语使用者开辟额外的沟通途径。最终的手语交互界面工具（Sign Language Interface Tool）应当能够识别手语输入，同时能够将口语表达或文本输出为手语。这样的工具将使聋人手语使用者与听力正常者之间能够轻松地进行交互。它还将使聋人手语使用者能够自然且便捷地使用计算机及其他设备。然而，在今天，无论是手语生成（Production）还是（更为困难的）识别（Recognition）...

这些系统仍处于相对早期的开发阶段。

目前已开发出许多用于展示人类表演手语视频的应用程序。这些界面不仅被用于让手语使用者能够获取音频和语音材料，还被用于教授聋人手语者的阅读和写作。虽然在系统需要向用户传达的句子数量有限时，使用人类手语表演的视频是合适的，但若要将视频作为计算机系统的基础来生成或组装全新的手语句子，则十分困难。

大多数成功的手语生成系统则选择了创建 3D 类人角色（3D human-like character）的动画，通过其动作来传递手语信息。这种方法的优势在于，它允许系统更轻松地将单个手势融合（blend）成流畅的手语句子。虚拟现实（Virtual Reality）、人体建模（Human Modeling）和动画（Animation）的研究已经达到了相当成熟的程度，现在可以构建一个足够灵活且响应迅速的人体模型来执行手语。这类人类虚拟分身（Human Avatar）动画的质量已经提高到让手语使用者能够观看屏幕上的动画，并成功解读分身的动作以理解其含义的程度。

![](https://public-media.interaction-design.org/images/encyclopedia/design_4_all/Figure19.jpg)

作者/版权持有者：BBC。版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用（因无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面中的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

**图 42.19**：一个手语虚拟形象（signing avatar）

手语翻译系统（Sign Language Translation Systems）分析输入文本的语言结构（linguistic structure）。文本的语法结构、词序和词汇被翻译成相应的手语语法结构、词序和词汇。此类系统会生成一份规定手语表演的脚本——通常使用手语合成软件（sign language synthesis software）来产生实际的动画输出，由一个类人角色执行手语句子。

手语识别（Sign recognition）的目标是将人类用户的手语表演自动转换为该表演的计算表示（computational representation）；这使得计算机能够识别用户手语的含义，并可能在随后将其翻译成文本或语音。

可以开发教育软件来帮助用户学习手语读写能力（sign language literacy skills）（通过观看手语动画或执行由系统识别的手语），或帮助用户学习其他学术内容（通过手语形式的讲解

（动画）。此外，还可以开发手语脚本软件（Sign language scripting software），使用户能够创建和编辑手语动画，正如文字处理软件（word processing software）允许用户编辑书面语言内容一样。

在不久的将来，只要聋人手语使用者（deaf signers）意识到机器翻译的准确率可能不如人类翻译员（human interpreters），他们或许能在各种应用场景中从机器手语翻译技术（machine sign language translation technologies）中获益。鉴于手语技术的现有技术水平（state-of-the-art）相对较低，服务提供商（如政府、公司、媒体机构等）必须谨慎，避免以可访问性（Accessibility）之名过早地部署这些技术。

### 42.5.8 多模态界面（Multimodal interfaces）

多模态交互（Multimodal interaction）是人类日常交流的一个特征。人们在高效的沟通流中通过说话、转移视线、做手势以及肢体移动来交流。多模态用户界面（Multimodal user interfaces）通过引入这些自然的人类行为元素来丰富交互。多模态系统以协调的方式处理两种或多种组合的用户输入模式——例如语音、手写笔、触摸、手动手势、视线以及头部和身体动作——并与多媒体系统输出相结合 (Oviatt, 2003)。它们具有“多感官性”（multi-sensory，即利用多种感官模态）、“多通道性”（multi-channel，即在相同或不同的模态上利用多个通道）、“多任务性”（multi-tasking，即允许用户同时执行多项任务）以及“多形式性”（multi-form，即允许用户以不同的替代方式执行相同的任务）。

人机交互（Human-Computer Interaction）中关于模态（modalities）和多模态（multimodality）的研究对全员设计（Design for All）产生了重大积极影响。可用模态范围的扩大以及多模态交互风格的增加，使得补偿日益多样化的身体残疾成为可能，从而为更广泛的残障用户群体提供更便捷的计算机访问方式，以及浏览和处理数字信息的适当设施，从而减少对辅助技术（assistive technologies）的需求。多模态界面具有极大地扩展计算对各类非专业人士的无障碍性（accessibility）的潜力。

用户，并且它们将“提高不同年龄、技能水平、认知风格（cognitive styles）、感觉和运动障碍、母语，甚至暂时性疾病用户的计算无障碍性（accessibility）”（Oviatt and Cohen, 2000）。例如，多模态界面（multimodal interfaces）具有能够帮助克服现有盲人解决方案中某些局限性的特性。具体而言，它们能够更好地适应用户的需求，提供更直观、简洁且快速的交互模式（interaction modes），降低学习难度并减少记忆负担，并能增强表达能力（power expression）（Bellik and Burger, 1994）。不同的模态（modalities）可以并发使用，从而增加可用信息的数量，或者在不同的语境中以冗余的方式呈现相同的信息，以应对不同的交互通道，两者都旨在

...强化某项特定信息，或照顾到用户不同的能力差异 (Antona et al., 2007)。

近年来，在处理新型输入模态（novel input modalities）——例如语音、手势、注视或触觉（haptics）以及模态的协同组合（synergistic combinations of modalities）——方面的进展，为在不便或无法使用键盘、鼠标和标准屏幕的场景下，提供了直接操纵（direct manipulation）的合适替代方案 (Carbonell, 2009)。

### 42.5.9 交互技术（Interaction Techniques）总结

下表总结了前几节讨论的交互技术、相关的目标用户群体以及最典型的应用场景。

|  | **目标群体（Target Groups）** | **典型应用（Typical Applications）** |
|---|---|---|
| **语音（Speech）** | 视障人士（Visually impaired）<br>肢体障碍人士（Motor Impaired）*<br>儿童（Children）*<br>老年人（Elderly）* | 电话系统（Telephony systems）<br>基于语音的交互（Speech-based interaction）<br>听写系统（Dictation systems） |
| **触觉（Haptics）** | 视障人士<br>听障人士（Hearing Impaired）<br>肢体障碍人士* | 盲文显示器（Braille displays）<br>远程传感（Remote sensing）<br>触觉显示器（Haptic displays） |
| **基于扫描的交互（Scanning-based Interaction）** | 肢体/言语障碍人士（Motor / speech Impaired）<br>认知障碍人士（Cognitively impaired） | 带有嵌入式扫描（Embedded scanning）的应用<br>扫描工具（Scanning tools）<br>键盘和鼠标模拟（Keyboard and mouse emulation） |
| **眼动追踪（Eye-tracking）** | 肢体障碍人士 | 视线通信系统（Gaze communication systems）<br>鼠标模拟（Mouse emulation）<br>眼动输入（Eye-typing） |
| **手势与头部追踪（Gesture and head tracking）** | 肢体/言语障碍人士*<br>视障人士<br>听障人士<br>儿童<br>老年人 | 家庭自动化（Home automation）<br>鼠标模拟<br>目标选择应用（Target selection applications）<br>头部控制开关（Head-controlled switches） |
| **脑机接口（Brain Interfaces）** | 肢体/言语障碍人士 | 通信系统（Communication systems）<br>计算机控制（Computer control）<br>轮椅控制（Wheelchair control） |
| **手语（Sign Language）** | 听障人士 | 手势识别（Sign recognition）<br>手语生成（Sign language generation） |

- *需提供必要的配置/修改

## 42.6 未来方向

由于人们对普适（Ubiquitous）且持续获取信息和服务的需求日益增加，交互技术正向一种被称为环境智能（Ambient Intelligence, AmI）的新交互范式（Interaction paradigm）演进。

***定义***
***环境智能（Ambient Intelligence）：*** *在 AmI 世界中，海量的分布式设备（Distributed devices）在嵌入环境的同时，利用隐藏在互连网络（Interconnection network）中的信息和智能进行协同运行。照明、声音、视觉、家用电器、个人健康护理设备以及分布式服务通过自然且直观的用户界面（Natural and intuitive user interfaces）的支持，彼此无缝协作，以提升整体用户体验。简而言之，环境智能是指能够感知人类存在并对其做出响应的电子系统。*
Aarts & de Ruyter, 2009

环境智能将对新兴产品和服务的类型、内容和功能，以及人们与它们的交互方式产生深远影响，从而带来诸多新需求。AmI 环境在满足老年人及残障人士日常生活需求方面的潜力，预计将对社会包容（Social inclusion）和独立生活（Independent living）产生根本性影响。许多旨在解决老年人和残障人士关键问题的应用程序和服务已经开始出现，例如在

环境辅助生活（Ambient Assisted Living, AAL）领域，旨在使更加独立、积极和健康的生活成为可能且令人愉悦。许多信息与通信技术（Information and Communication Technology, ICT）解决方案致力于解决日常生活和独立生活中的问题，涵盖领域包括社交沟通、日常购物、出行、社交生活、公共服务、安全、提醒、远程护理（Telecare）和远程医疗（Telemedicine）、个人健康系统，以及为认知障碍患者及其护理人员提供支持（The European strategy in ICT for Ageing Well of 2010）。考虑到许多老年人在视觉、听觉、行动能力或灵活性（Dexterity）方面存在障碍，无论是在室内还是室外的各类设备，用户友好界面（User-friendly interfaces）都是必不可少的。显然，只有当这些技术能够被证明……时，环境智能（Ambient Intelligence, AmI）环境的益处才能被目标终端用户充分实现并接受。

以确保针对由年龄或残疾引起的各种功能限制提供包容性可访问性（inclusive accessibility）的方式进行开发。

在这样一个动态演进且复杂的技术环境中，具有不同特征和需求的用户的可访问性（accessibility）和可用性（usability）问题，不能通过在新环境的主要构建组件就位后再引入的解决方案来解决。在此背景下，“全民设计（Design for All）”的概念变得至关重要，旨在通过通用解决方案（generic solutions）将可访问性高效地整合到新的技术环境中 (Emiliani and Stephanidis, 2005)。然而，在环境智能（Ambient Intelligence, AmI）的语境下，全民设计需要进一步演进，以应对不断变化的技术环境所带来的一系列新挑战。

AmI 环境的可访问性所面临的问题与目前针对桌面或 Web 应用程序及服务的可访问性方法不同，且更为复杂，因为 AmI 环境引入的不仅仅是一项新技术，而是一套集成技术。可访问性可以分为不同的层级。第一层级涉及单个设备的可访问性。交互式设备需要根据所有者的需求确保其可访问，但同时也应为具有潜在不同需求的其他用户提供基础的可访问性。第二层级涉及可访问性

...整个环境，旨在为具有多样化特征的用户提供对内容和功能的等同访问（equivalent access），且不一定是通过相同的设备，而是通过集成在环境中的一套动态交互选项（dynamic interaction options）。

环境智能（Ambient Intelligence, AmI）环境中的一些内置特性，例如多模态（multi-modality），可能会有助于提供在设计上即具备可访问性（accessible by design）的解决方案。例如，盲人用户将受益于更广泛的语音输入和输出。一个新颖的方面是，在 AmI 环境中，物理世界与虚拟世界的可访问性需要相结合。例如，对于盲人、视障者和运动障碍用户，与交互相关的需求需要与交互环境中的物理导航（physical navigation）需求相结合。

因此，目前开发真正具备可访问性的 AmI 环境在时间、精力、成本和所需知识方面都非常昂贵，且在可访问性解决方案和目标用户群体方面，其结果往往缺乏灵活性和可重用性。

因此，一方面有必要制定一种既以用户为中心又具备上下文感知（context-aware）的方法论，以实现环境智能中的全员设计（Design for All）；另一方面，需要开发现代化的工具和个性化辅助解决方案，这些将成为开发独立生活 AmI 环境的基石。

解决老年人及残障人士的交互需求。

为了在环境智能（Ambient Intelligence, AmI）环境中制定一套关于无障碍性（Accessibility）和全员设计（Design for All）的系统化方法，需要解决以下几项挑战 (Margetis et al., 2012)：

- 深入研究用户需求，以及针对不同用户特征/功能限制与环境特征/功能的组合，探讨不同解决方案的适用性，并构建相关的本体模型（Ontological models）。
- 开发参考架构模型（Reference architectural models），以满足 AmI 环境中全员设计需求所固有的系统要求，同时支持无障碍的多模态交互（Multi-modal interaction）。
- 提供开箱即用的无障碍解决方案，以支持针对各种用户能力/功能限制组合的替代交互技术。
- 开发用于无障碍 AmI 环境的设计工具。
- 在关键的日常生活领域（如家庭、工作、学习、健康和自我护理）开发无障碍 AmI 应用。
- 对所开发的辅助方案（Assistive solutions）、工具和应用进行评估，以衡量其针对目标用户的无障碍性、可用性（Usability）及附加价值。

## 42.7 更多学习资源


### 42.7.1 书籍

![](https://public-media.interaction-design.org/images/encyclopedia/design_4_all/Figure20.jpg)
作者/版权持有者：未知（待核实）。版权条款与许可：未知（待核实）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外情况（Exceptions）”章节。
**图 42.20**：USER INTERFACES FOR ALL: Concepts, Methods, and Tools。编辑：Constantine Stephanidis。出版社：Lawrence Erlbaum Associates。ISBN: 0-8058-2967-9。[更多信息](http://www.ics.forth.gr/hci/index_main.php?l=e&c=469)

![](https://public-media.interaction-design.org/images/encyclopedia/design_4_all/Figure21.jpg)
作者/版权持有者：未知（待核实）。版权条款与许可：未知（待核实）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外情况（Exceptions）”章节。
**图 42.21**：THE UNIVERSAL ACCESS HANDBOOK。编辑：Constantine Stephanidis。出版社：CRC Press Taylor & Francis Group。ISBN: 978-0-8058-6280-5。[更多信息](http://www.ics.forth.gr/hci/index_main.php?l=e&c=468)

### 42.7.2 期刊 (Journal)

![](https://public-media.interaction-design.org/images/encyclopedia/design_4_all/Figure22.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外 (Exceptions)”部分。
**图 42.22**：*Universal Access in the Information Society*。主编：Constantine Stephanidis。出版商：Springer-Verlag Heidelberg。[更多信息](http://www.springeronline.com/journal/10209/about)

### 42.7.3 会议 (Conference)

*Universal Access in Human-Computer Interaction*，隶属于 [Human-Computer Interaction International Conference Series](http://www.hci-international.org/)。
**章节目录 (Chapter TOC)**
[**The Practical Guide to Usability**](https://www.interaction-design.org/courses/the-practical-guide-to-usability)
![](https://public-media.interaction-design.org/images/courses/hds/course_15--square_thumbnail.jpg?tr=fo-auto)
*The Practical Guide to Usability*
剩余 7 天
已预订
查看课程
                

## 获取每周 UX 洞察 (UX Insights)

加入 **314,524 位设计师** 的行列，通过我们的时事通讯 (Newsletter) 获取有用的 UX 技巧。
需要提供有效的电子邮件地址。

## 本书章节涵盖的主题：

[全员设计 (Design for All)](https://www.interaction-design.org/literature/topics/design-for-all)[
                        用户体验 (User Experience, UX) 设计](https://www.interaction-design.org/literature/topics/ux-design)[
                        人机交互 (Human-Computer Interaction, HCI)](https://www.interaction-design.org/literature/topics/human-computer-interaction)[
                        可访问性 (Accessibility)](https://www.interaction-design.org/literature/topics/accessibility)[
                        设计史 (Design History)](https://www.interaction-design.org/literature/topics/design-history)[
                        Web 内容可访问性指南 (Web Content Accessibility Guidelines)](https://www.interaction-design.org/literature/topics/web-content-accessibility-guidelines)[
                        用户访谈 (User Interviews)](https://www.interaction-design.org/literature/topics/user-interviews)[
                        可用性 (Usability)](https://www.interaction-design.org/literature/topics/usability)[
                        用户故事 (User Stories)](https://www.interaction-design.org/literature/topics/user-stories)[
                        用户场景 (User Scenarios)](https://www.interaction-design.org/literature/topics/user-scenarios)
