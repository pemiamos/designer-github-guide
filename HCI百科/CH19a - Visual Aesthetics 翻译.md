# 19. 视觉美学 (1)

**来源**：The Encyclopedia of Human-Computer Interaction, 2nd Ed.
**Notion 原页面**：https://www.notion.so/a9fb8ab8718041b9af2f2c49823c78c3

---

[Noam Tractinsky](https://www.interaction-design.org/literature/author/noam-tractinsky)
本章所讨论的视觉美学（Visual Aesthetics）是指事物的美感或令人愉悦的外观。我们将探讨视觉美学在交互式系统与产品（interactive systems and products）语境下的重要性，阐述其在人机交互（Human-Computer Interaction, HCI）领域的研究现状，并为该领域的未来研究方向提出建议。

## 19.1 引言（Introduction）

对于 20 世纪 90 年代初人机交互（Human-Computer Interaction, HCI）领域的学者和从业者来说，认为美学（aesthetics）在信息技术中至关重要的观点听起来像是异端之说。二十年后，在 2010 年代初，这一观点在学术界和工业界都占据了稳固的地位。虽然利用计算机生成视觉艺术的尝试可以追溯到 20 世纪 60 年代（Nake, 2005），但针对交互系统（interactive systems）视觉美学的系统性研究则只能追溯到 90 年代中期（Kurosu and Kashimura, 1995; Tractinsky, 1997）。从那时起，大量研究不断地探索该领域的各个方面。这一研究的时间线大致与信息技术行业更为剧烈的变革相吻合。自 90 年代后期以来，一种向视觉美学倾斜的强劲趋势席卷了整个行业。工业界和学术界对美学兴趣的增加，反映了 HCI 领域的成熟，以及该学科在克服许多“成长痛（growing pains）”方面的进展——此前，该学科一方面要与不可靠的技术作斗争，另一方面需要满足用户的基本需求。此外，强调设计与风格（design and style）的更广泛的社会进程在同一时期出现（Gibney and Luscombe, 2000; Postrel, 2002），进一步强化了产品整体美学（Bloch, 2011）以及特别是交互系统美学的转变。关于这一过程的更详细描述见于

见于 Tractinsky (2004) 和 Tractinsky (2006)。

Udsen and Jørgensen (2005) 确定了人机交互（Human-Computer Interaction, HCI）中美学研究的几种方法。本章所述的“视觉美学（Visual aesthetics）”大致对应于 Udsen and Jørgensen 所定义的“功能主义（Functionalist）”方法。具体而言，为了将本章的主题与其他类似术语区分开来，我对“美学（aesthetics）”一词的使用倾向于其在词典定义中较为普通且通俗的含义，例如 *The American Heritage Dictionary of the English Language* 中定义的“具有艺术美感或令人愉悦的外观”，或 *Merriam-Webster’s Collegiate Dictionary* 中定义的“令人愉悦的外观或效果：美”。“视觉（visual）”一词表明研究重点在于视觉感官，这是人类的核心感官，占据了“几乎一半的大脑”（Ware, 2008, ix）。因此，本章*并非*探讨在“美学”标题下研究的其他各种现象，例如文学美学、抽象形式的美学体验或标准（例如数学证明的优雅性），以及对那些并非直接且主要源于视觉属性的对象特性的反应。

此外，还可以列举描述该领域研究的几个其他特征。这些特征描述了该领域的研究者如何对待其研究对象。首先，视觉美学研究者的研究方法表现出一种对正向效应（positive effects）的偏好。

关于[视觉设计](https://www.interaction-design.org/literature/topics/visual-design)，我将在本章稍后讨论这个问题。因此，该领域的研究通常关注人造物（Artifacts）——即基于计算技术的设计对象——的美观且令人愉悦的外观，而非其丑陋且令人不快之对应物的效果。其次，在 2008 年举行的一次关于 HCI 中视觉美学的 Dagstuhl 研讨会上，大多数参与者采用了交互主义方法（Interactionist Approach）来研究视觉美学，指出美学体验（Aesthetic Experience）是由人们对物体的反应构成的，而非物体本身固有的美学（Hassenzahl et al., 2008）。这些反应既包括个体的特质（Individual Idiosyncrasies）和品味，也包括个体与专家之间的高度一致性，以至于它们可以被认为是“准客观的（Quasi-objective）”（Hoyer and Stokburger-Sauer, 2011）。第三，虽然上述 Dagstuhl 研讨会未能就视觉美学反应的相关时间范围达成共识，但我个人的观点是，这一范围可以涵盖从极快的本能反应（Visceral Reactions）到极长的沉思性评估（Contemplative Evaluations）的所有区间。第四，设计和评估视觉美学的过程既包含情感的（Affective）也包含认知的（Cognitive）。最后，视觉美学领域的研究主要是实证的（Empirical），并且是

具有描述性（descriptive，即“什么是被认为是美的”）而非规范性（normative，即“什么应该是被认为是‘美的’”）的特征 (Hassenzahl, 2004b)。这一重要的区分强调了该领域根植于应用研究（applied research），并将其与关于该主题的艺术或哲学论述区分开来。

本章的目标是综述人机交互（Human-Computer Interaction, HCI）中的视觉美学（visual aesthetics）领域。我们首先从三个视角阐述视觉美学对 HCI 的重要性。随后，我们将提出一个研究框架（research framework），用于回顾该领域中的关键研究结果。这些方面包括诸如：什么样的系统看起来具有美感、视觉美学系统会产生怎样的影响，以及在交互系统（interactive systems）的语境下，人们进行美学判断涉及哪些机制等问题。我们还将讨论方法论（methodological aspects）方面的问题以及未来研究面临的挑战。

### 19.1.1 视觉美学在人机交互中的重要性

视觉美学（Visual Aesthetics）对人机交互（Human-Computer Interaction, HCI）领域的重要性可以从多个视角来论述。在这里，我提出了三个这样的视角——设计视角（Design Perspective）、心理学视角（Psychological Perspective）和实践视角（Practical Perspective）。尽管这些视角并非旨在穷尽所有可能性，但我认为，综合来看，它们涵盖了将视觉美学作为人机交互实践、研究和教育主要方面的大部分论据 (Tractinsky and Hassenzahl, 2005)。虽然这些视角各不相同，但在某些点上可能会有所重叠。最后，对于某些人来说，提出这些论点可能显得有些冗余，因为近年来这些观点在人机交互社区中已经得到了相当广泛的认可。尽管如此，我认为以有组织的方式呈现这些论点至关重要，这不仅能阐明我的观点，还能为社区成员提供一套论据，以便他们在面对其他受众（例如软件和硬件工程师、产品经理等）时，能够证明视觉美学的重要性。

### 19.1.2 设计视角（The Design Perspective）

尽管是最年轻的设计学科之一，交互技术（Interactive Technology）的发展已迅速成为最显著的设计活动之一。人机交互（Human-Computer Interaction, HCI）与设计（Design）之间的相互关联性早已被认可（例如 Winograd, 1996），但这对 HCI 的研究、实践和教育具有怎样的影响？在这里，我想指出其中的两点影响。第一点影响是意识到美学（Aesthetics）构成了任何设计学科中重要且不可或缺的一部分。随着人造物（Artifact）与受影响人群之间的界面（例如在视觉显著性 [Visual Saliency]、交互时长或共存程度方面）变得更加全面，美学的重要性也随之增加。第二点影响是，视觉美学通常与其他设计维度相关联。因此，我们不仅不应担心交互系统在美学与其他质量属性之间进行权衡（Trade-off），而应将美学视为一个能够增强设计其他方面以及整体交互体验（Interactive Experience）的维度。

### 19.1.2.1 维特鲁威设计原则（The Vitruvian design principles）

Vitruvius（公元前1世纪）可能是第一个提出系统且详尽的[设计原则（principles of design）](https://www.interaction-design.org/literature/topics/design-principles)的人。建筑学作为最显著且复杂的设计学科，普遍地影响着人类生活，因此成为他详尽著作的主题，这并不令人意外。除了信息技术（information technology）和交互系统（interactive systems）如今也变得同样无处不在之外，不难发现建筑学与信息技术之间有许多共同之处（例如 Brooks, 1975; Hooper, 1986; Lee, 1991; Kim et al., 2002; Visser, 2009）。这体现在专业人士用来指代创建基于信息的环境和系统的过程的术语“[信息架构（information architecture）](https://www.interaction-design.org/literature/topics/information-architecture)”中。这两个学科之间的相似性可以通过考察 Vitruvius 关于优秀建筑作品的三项核心原则来阐明：*Firmitas*，即建筑的强度和耐久性；*utilitas*，即建筑的实用性，指其有用程度以及是否符合预期居住者和用户的需求；以及 *venustas*，即建筑的美观性。在建筑学中，维特鲁威原则自 15 世纪被重新发现以来一直具有影响力（Johnson,

1994; Kruft, 1994)。例如，如今它们成为了由英国建筑工业委员会（Construction Industry Council）开发的“设计质量指标（Design Quality Indicator）”的基础，用于评估建筑的设计质量（Whyte et al, 2003）。

对于各种计算机和 IT 学科而言，将 *firmitas*（稳固性）视为其研究和实践的核心原则是非常直观的。自该领域诞生以来，对鲁棒（robust）、可靠（reliable）且可信（dependable）的软件、硬件、系统和产品的需求一直占据着主导地位。我们可以说，正如 *firmitas* 是结构设计的先决条件一样，我们也将其视为任何 IT 系统或产品的前提条件。            Certificates虽然关于 *firmitas* 原则的重要性几乎没有争议，但计算机社区最初对 *utilitas*（实用性）的热情则要低得多。

原则。在 IT 背景下，这一原则涉及旨在满足个人和组织需求与目标的设计，重点在于人与人工制品（artifacts）之间交互的效率和有效性。事实上，人机交互（Human-Computer Interaction, HCI）社区在将 *utilitas*（实用性）原则纳入计算工业的主流实践方面功不可没（参见 Tractinsky, 2006）。HCI 领域根植于对系统和产品的研究与设计，旨在让人们能够高效地使用它们（Card et al, 1983）。例如，作为 HCI 社区核心的[可用性（usability）](https://www.interaction-design.org/literature/topics/usability)概念，不仅渗透到了 IT 行业的其他领域，而且使以人为中心的设计（human-centered design）价值获得了几乎普遍的认可和支持。在关于人与信息技术关系的模型中，被引用最广泛的模型之一——技术接受模型（Technology Acceptance Model, TAM）——指出，一个易于使用且提供更多有用功能的系统，更有可能被其目标用户所采用（Davis, 1989）。

在具备了 *firmitas*（稳固性）和 *utilitas*（实用性）之后，整个计算社区，尤其是 HCI 领域，仍然缺失一个关键的维特鲁威（Vitruvian）原则。多年来，美感（beauty）和愉悦感（delight）被 HCI 社区视为一种不必要的点缀（gratuity），且往往被刻意回避。绝美交互产品的出现

在 21 世纪的第一个十年中，这带来了商业上的成功和学术研究（例如 Kim et al., 2002; Liu, 2003; Tractinsky, 2004），并相当有力地证明了，正如在其他设计学科中一样，维特鲁威（Vitruvian）的第三根支柱——*venustas*（美感），应当被充分接纳为交互技术（interactive technology）设计的基石（另见 Fishwick, 2006）。

![](https://public-media.interaction-design.org/images/encyclopedia/visual_aesthetics/De_architectura.jpg)
作者/版权持有者：由 Mark Pellegrini 提供。版权条款和许可：CC-Att-SA-2 (Creative Commons Attribution-ShareAlike 2.0 Unported)。

**图 19.1**

![](https://public-media.interaction-design.org/images/encyclopedia/visual_aesthetics/Vitruvian.jpg)
版权条款和许可：pd (Public Domain (公共领域（属于公共财产且不含原始作者身份的信息）))。

**图 19.2**：
维特鲁威人（The Vitruvian Man）图绘由 Leonardo da Vinci 约于 1487 年基于 Vitruvius 的著作创作。通过对人体比例进行实证测量和计算，Vitruvius 也可以被认为是人机工程学（ergonomics）的第一位学生。

### 19.1.2.2 美学与其他设计原则的重叠

人机交互（HCI）和可用性（Usability）专家过去常警告不要过分强调美学（Aesthetics）（例如 Norman, 1988; Nielsen, 1993）。他们的警告似乎反映了对这两个设计维度能否共存的担忧。美感被认为是通往[良好设计（good design）](https://www.interaction-design.org/literature/topics/good-design)道路上的障碍：如果设计师强调美学，那么默认情况下就会牺牲可用性。

这一观点一直在逐渐改变，部分原因在于一系列研究结果表明，至少在感知设计属性（perceived design attributes）方面，美学和可用性可以被视为正相关（Tractinsky et al., 2000; Lavie and Tractinsky, 2004, Cawthon and Moere, 2007; Sonderegger and Sauer, 2010）。此外，深入研究可用性指南可以发现，可用性原则与美学原则之间不存在内在冲突。针对可用计算机应用程序的指南在提出建议时（例如：有序的显示、保持元素对齐、将相关的元素分组、将它们与其他元素清晰地分开等），很大程度上依赖于格式塔知觉定律（Gestalt laws of perception）。

当然，这些原则同样被用于解释和推进艺术与设计的理论和实践，这表明它们会影响美学印象（Arnheim, 1966）。我最喜欢用来证明这一点的示例之一是以下屏幕

这出现在 Parush et al (1998) 的一项研究中。该研究的参与者被要求评估两个屏幕的界面质量（Interface Quality）（图 3）。参与者认为左侧屏幕的质量优于右侧屏幕。但他们指的是哪种设计质量（Design Quality）？是可用性（Usability）？还是视觉美学（Visual Aesthetics）？每当我在课堂或受邀讲座中提出这个问题时，答案的分布几乎总是相同：在“可用性”、“美学”和“两者兼有”之间均匀分布！

![](https://public-media.interaction-design.org/images/encyclopedia/visual_aesthetics/good_design_versus_bad_design_from_parush_et_al.jpg)
作者/版权持有者：Parush et al。版权条款与许可：保留所有权利。经许可转载。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”部分。

**图 19.3**：来自 Parush et al (1998) 的两个屏幕。左侧屏幕代表优秀设计，右侧屏幕代表糟糕设计。

这个例子阐明了另一项研究（Lavie and Tractinsky, 2004）的发现，该研究根据两个感知维度（Perceived Dimensions）对网页进行了刻画。我们使用“经典”美学（“Classical” Aesthetics）一词来表示传达秩序感和良好比例的维度。这一子维度与可用性高度相关。而另一个...

该维度代表了设计的原创性（originality）和[创造力（creativity）](https://www.interaction-design.org/literature/topics/creativity)方面，因此被命名为“表现性（expressive）”美学。不出所料，感知到的网站可用性（perceived website usability）与经典美学（classical aesthetics）高度相关，而与表现性美学的相关性仅为中等。因此，意识到以下两点至关重要：(a) 人们能够区分交互系统（interactive systems）中不同的美学维度；(b) 至少某些美学维度能够增强而非削弱可用性（usability）。

### 19.1.3 心理学视角（The Psychological Perspective）

在人机交互（Human-Computer Interaction, HCI）领域的早期，研究人员和从业者强调任务相关标准，例如易用性（ease of use）和效率（efficiency），将其视为[交互设计（interactive design）](https://www.interaction-design.org/literature/topics/interaction-design)的最终目标。审美（Aesthetics）在当时被认为充其量是多余的，甚至是有害的（例如 Norman, 1988）。然而，随着交互技术深深地融入日常生活，触及几乎所有方面，人们意识到这一立场应当被重新评估（Norman, 2002, Hassenzahl, 2007）。在很大程度上，HCI 中视觉审美研究的出现根源于“积极心理学（positive psychology）”运动（Seligman and Csikszentmihalyi, 2000），该运动呼吁将重心从处理人的弱点及其补救措施，转向关注人的优势与福祉（well-being）。这种观点在 HCI 领域研究[用户体验（User Experience, UX）](https://www.interaction-design.org/literature/topics/ux-design)的背景下得到了热烈响应（Hassenzahl and Tractinsky, 2006; Law and Schaik, 2010）。

本节将从心理学角度提供三个论点，以阐述审美设计的重要性。其核心观点是，审美设计对情感过程（emotional processes）和认知过程（cognitive processes）均有积极影响（Norman, 2004; Leder et al., 2004）。这反过来又提升了人们对技术的体验、对其的评价以及他们的

对其的态度（例如，Hartmann et al., 2007, 2008; Thuring and Mahlke, 2007）。在本章中，我们首先探讨情感与动机（emotional and motivational）维度：美学（aesthetics）能带给我们愉悦感并提升我们的福祉（well-being）。随后，我们将讨论认知过程（cognitive processes），通过这些过程，视觉刺激（visual stimuli）能够被高效识别，从而对产品和环境的后续评估起到至关重要的作用。

### 19.1.3.1 审美满足人类的基本需求且是愉悦感的来源

早期的 HCI（Human-Computer Interaction，人机交互）文献似乎轻视了对审美设计的需求。这种观点可能主要是为了推广更紧迫的可用设计（Usable Design）价值而产生的。然而，基于我们对人类天性的认知，这种立场在长期来看是不可持续的。有观点认为，视觉审美（Visual Aesthetics）的价值源于其对愉悦感和幸福感（Well-being）的贡献（例如 Santayana, 1896; Postrel, 2002），以及它作为人类基本需求的作用（[Maslow](https://www.interaction-design.org/literature/topics/abraham-maslow), 1954），这或许与进化过程（Evolutionary Processes）有关（Dutton, 2008）。

![](https://public-media.interaction-design.org/images/encyclopedia/visual_aesthetics/harry_potter_skin_phone.jpg)
作者/版权持有者：Ninety9mall。版权条款与许可：保留所有权利。根据合理使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因为无法获得许可）。请参阅[版权声明](https://www.interaction-design.org/about/terms-of-use)页面上的“例外”部分（以及“allRightsReserved-UsedWithoutPermission”子节）。

**图 19.4**：审美作为自我的延伸（Extension of the Self）：Blackberry 智能手机的 Harry Potter 主题皮肤

当其他需求更为紧迫时，视觉审美可能会暂时让位于其他设计维度；某些人对审美环境的敏感度较低或需求较少（Bloch et al., 2003）；并且

审美趣味（aesthetic tastes）以及对审美刺激（aesthetic stimuli）的反应在个体之间存在差异 (Santayana, 1896; Hoyer and Stokburger-Sauer, 2011)。尽管如此，视觉艺术（visual arts）在不同文化中的普适性及其带来的愉悦感，被进化心理学家（evolutionary psychologists）认为是审美在现代智人（*Homo sapiens*）心理（psyche）中发挥基础性作用的证据 (Dutton, 2008)。审美体验（aesthetic experiences）与情感反应（affective responses）和反思性思考（reflective thought）相关 (Leder et al., 2004)。使用功能性磁共振成像（functional magnetic resonance imaging, fMRI）的研究在产品包装（product packaging）的语境下，为这种关联提供了进一步的神经生理学支持（neurophysiologic support） (Reimann et al., 2010)。任务相关标准（task-related criteria）通常基于外在动机（extrinsic motivation），而审美则通过愉悦感和参与感，主要贡献于内在动机（intrinsic motivation）。因此，没有理由认为审美需求在面对计算机时会消失。视觉上令人愉悦的设计能够丰富我们与交互系统（interactive systems）的体验，就像它在任何其他环境中所起的作用一样 (Hassenzahl, 2007)。经验证据（empirical evidence）表明，交互技术的审美设计能够增加用户的愉悦感和参与感 (e.g., Thuring and Mahlke, 2007; Porat and Tractinsky, 2012; Angeli et al., 2006)。因此，我们预期愉悦的交互能让我们更快乐，从而提升我们的幸福感（well-being） (Lyubomirsky et al., 2005)。此外，它们可能会让我们对其他设计缺陷更具包容心

不完美性 (Imperfections) (Norman, 2004)，并在特定条件下提升我们的任务绩效 (Task Performance) (Moshagen et al., 2009)。

### 19.1.3.2 美学作为自我的延伸（Aesthetics as an extension of the Self）

Belk (1988) 认为，“通过我们的拥有物来学习、定义并提醒自己是谁，似乎是现代生活一个不可回避的事实”（第 160 页）。这种通过拥有物实现自我延伸（self-extension）的过程在人机交互（Human-Computer Interaction, HCI）领域得到了体现，具体表现为人们修改其电脑桌面、屏幕保护程序、个人网站以及各种标准应用程序的方式。这些形式的特质性依恋（idiosyncratic attachments, Kleine et al., 1995）得益于信息技术（IT）的灵活性和可塑性。现代软件应用程序的外观可以根据用户的口味进行个性化定制。尽管规模较小，但这种趋势在硬件中也能发现——例如，种类繁多的手机壳、挂件和其他装饰品。对于大多数热门应用程序，用户可以免费或付费下载软件皮肤（software skins）。事实上，研究表明，影响用户选择皮肤的主要因素是其设计的美学方面（Tractinsky and Lavie, 2002; Tractinsky and Zmiri, 2006）。此类功能的普及在很大程度上可以用个体表达自我的欲望，以及希望被他人以特定方式看待的愿望来解释（Hassenzahl, 2003）；同时，这也是身份构建（identity formation）持续过程的一部分，人们通过这一过程“表达自己是谁，并传达与他人的归属感（affiliation）”（Venkatesh and Meamber, 2008, 第 51 页）。这些不仅是那些个体身份的体现，

他们的过去与现在，以及他们的隶属关系 (Kleine et al., 1995)，同时也涉及当今许多交互产品（interactive products）所处的社会语境（social context）(Turkle, 2005)。

![](https://public-media.interaction-design.org/images/encyclopedia/visual_aesthetics/Harry_Potther_Theme_windows_7.jpg)
版权条款与许可：保留所有权利。根据合理使用原则（Fair Use Doctrine）在未经许可的情况下使用（因无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面上的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

**图 19.5**：作为自我延伸（extension of the Self）的美学：Windows 7 操作系统的 Harry Potter 主题皮肤（skin）

![](https://public-media.interaction-design.org/images/encyclopedia/visual_aesthetics/harry_potter_skin_chrome.jpg)
版权条款与许可：保留所有权利。根据合理使用原则（Fair Use Doctrine）在未经许可的情况下使用（因无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面上的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

**图 19.6**：作为自我延伸（extension of the Self）的美学：Google Chrome 浏览器的 Harry Potter 主题皮肤（skin）

### 19.1.3.3 审美印象是快速、持久且具有影响力的

之前的论点讨论了对审美环境的心理需求，以及拥有、购买和使用审美产品的动机，而目前的论点则基于审美刺激（aesthetic stimuli）所带来的后果。这些后果基于这样一个观点，即审美印象（aesthetic impressions）的形成速度非常快。对大脑活动的研究表明，审美印象在 300 毫秒到 600 毫秒之间形成 (Höfel and Jacobsen, 2007)。关于人们对网页印象的研究证明，在接触时间不足 500 毫秒的情况下，就能形成可靠且一致的审美判断（aesthetic judgments）(Lindgaard et al., 2006; Tractinsky et al., 2006)。这些极快的印象是我们对某个对象（例如一个交互系统 [interactive system]）形成态度的第一个机会，而该对象的其他特性通常在稍后才有机会进行评估时（例如尝试使用该系统完成一项任务时）才会显现。与更详尽的评估相比，这些初始态度倾向于在相对潜意识（subconscious level）的层面形成，因此在不同个体之间可能相对统一 (Kumara and Gargb, 2010)。

第一印象对态度的首要性（primacy of first impression）在社会科学研究中已有充分的记录。其最显著的表现形式是“美即是好（what is beautiful is good）”的刻板印象（stereotype）(Dion et al., 1972)，该观点认为一个人的外貌会影响...

其他人看待该个体的隐藏特质（Hidden Qualities，例如人格特质 [Personality Traits]）。这种对审美外观（Aesthetic Appearance）的偏好可能是进化适应（Evolutionary Adaptation）的结果 (Rhodes, 2006)。研究记录了许多在劳动力市场 (Hamermesh and Biddle, 1994)、信贷市场 (Ravina, 2008) 甚至在课堂上 (Hamermesh and Parker, 2003) 中，外貌出众的人能够获得优先对待（Preferential Treatment）的情况。我们还知道，人们会尝试积极地改善自己在他人眼中的形象，以获取利益或避免惩罚 (Jones, 1990)。这种尝试可见于，例如人们如何通过以更具吸引力的格式呈现信息，来改善关于其职责范围内事务（如在工作中）的信息传递 (Tractinsky and Meyer, 1999)。这种审美上的改进可能会带来回报：

研究表明，在普通情况下，具有美感的财务报告会提高初级投资者和专业投资者对公司的估值 (Townsend and Shu, 2010)。同样地，事物的外观可能会影响我们对它们的态度。这里的“事物”可以指自然环境（natural settings）和对象，例如景观 (Porteous, 1996; Carlson, 2000)，或者各种设计环境（designed environments）(Gilboa and Rafaeli, 2003) 和人造物（artifacts）(Rafaeli and Vilnai-Yavetz, 2004)。例如，Reimann et al (2010) 发现，相比于采用标准化包装的知名品牌且价格较低的产品，用户更倾向于选择具有美感包装的产品。

因此，交互系统（interactive systems）——无论是硬件还是软件——的视觉美感（visual aesthetics）可能会影响我们对其其他系统属性的评估，这一点并不令人意外。由此产生了“美即可用（beautiful is usable）”的观点，即用户认为美观的系统更具可用性（usable）(Tractinsky et al., 2000)。

### 19.1.4 实践视角（The Practical Perspective）

最后，我想指出，即便你并不认同美学（Aesthetics）是优秀设计的支柱，或者不认为美学能够满足心理需求并影响态度与决策，但其在实践中的意义（Practical significance）依然难以否认。日常生活中已有大量证据可以证明这一点。在此，我想从两个方面来阐述这一视角。第一点描述了美学作为相似产品之间差异化因素（Differentiating factor）的重要性。第二个论点则指出，在当前的社会技术过程（Socio-technical processes）中，美学与信息技术（Information Technology）已经深刻地交织在一起。因此，在信息技术中忽视美学不仅是不明智的，事实上，我们还需要对其给予更多关注，进一步研究美学与人机交互（Human-Computer Interaction, HCI）领域其他相关方面之间的关系，并提升其在交互系统（Interactive systems）设计中的整合程度。

### 19.1.4.1 美学作为差异化因素

在过去的五十年里，IT 产业的重心发生了转移：从强调组织的大规模数据处理（number crunching），到支持组织和个人的决策制定与生产力，再到完全融入消费者和娱乐产品之中。在此期间主导 IT 产业的接续公司名单——IBM、Microsoft 和 Apple——简洁地讲述了这一演变过程。交互技术的以消费者为中心（consumer-centeredness）和商品化（commoditization）进程在加速（Norman (1998) 已对此进行了部分描述），这提升了美学（aesthetics）作为竞争产品之间差异化因素的重要性。数字手表行业在 20 世纪 70 年代和 80 年代是这一过程的经典案例，因为当时的功能性和性能已经达到了极高的准确性和可靠性标准。在该行业中，品牌和型号之间的大部分差异现在基于美学创意或对美学典范的模仿。如今，我们被类似的高性能交互式消费产品所包围——例如智能手机和平板电脑。这些产品更倾向于增强用户体验（user experience），而竞争的焦点在很大程度上在于尝试通过外观和基于设计的符号价值（symbolic value）来吸引消费者的目光与心。因此，美学设计作为一种差异化策略或战术正逐渐被认可。

(Simonson and Schmitt, 1997; Luchs and Swan, 2011; Reimann et al., 2011) 在各种市场中。

![](https://public-media.interaction-design.org/images/encyclopedia/visual_aesthetics/smartphones-2007.jpg)
作者/版权持有者：Courtesy of Marco Arment。版权条款与许可：CC-Att-SA-3 (Creative Commons Attribution-ShareAlike 3.0)

**图 19.7**：2007 年发布的首款 iPhone（左）及其同时代产品的对比。iPhone 是手机制造商如何将视觉美学（Visual Aesthetics）作为差异化因素（Differentiating Factor）的绝佳案例——从手机本身到其包装的所有细节均体现了这一点。

![](https://public-media.interaction-design.org/images/encyclopedia/visual_aesthetics/Model_2500_Telephone.jpg)
版权条款与许可：pd (Public Domain (公共领域，指共有财产且不含原创作者身份的信息))。

**图 19.8.A**：1980 年生产的极受欢迎的 Western Electric Model 2500（12 键触键式 Touch-Tone）电话。

![](https://public-media.interaction-design.org/images/encyclopedia/visual_aesthetics/Beocom_telephone.jpg)
版权条款与许可：pd (Public Domain (公共领域，指共有财产且不含原创作者身份的信息))。

**图 19.8.B**：BeoCom 1000 有线模拟电话（Corded Analogue Telephone）利用视觉美学使其在与 Western Electric Model 2500 等流行电话的竞争中脱颖而出。

### 19.1.4.2 审美具有普遍性（Aesthetics is pervasive）

审美与技术之间存在着悠久的关联传统（Petroski, 1992; Norman, 2004），这种关系在 20 世纪技术飞速发展期间变得更加显著。先进技术有助于创造此前无法实现（至少无法大规模实现）的审美形式（Aesthetic forms）；同时，在新的设计、制造或建筑技术的帮助下，审美概念得以从一个技术领域（例如飞机设计）借鉴到另一个领域（例如机车设计或机场航站楼结构）。如今，设计趋势在多个行业中同时出现已成为常态（Gladwell, 2000）。在信息技术时代，这种关系变得比以往任何时候都更加共生（Symbiotic）。信息技术的一个独特特征是它对审美应用（Aesthetic applications）特别友好（Postrel, 2002）。相对于传统方法，它支持对审美材料进行轻松的创建、操纵和传输。例如，可以考虑摄影市场在短短十年内从胶片相机向数字相机的转变。如今，作为视觉审美（Visual aesthetics）主要元素的图像和照片，约占通过互联网传输的网页数据量的 2/3（Rabbat, 2010）。数字技术和应用使各行各业的设计师能够...

更多的设计选项，以及更多探索这些选项的时间，从而创造出更具吸引力的产品。也许更重要的是，这些技术为普通人提供了能够以革命性的规模创造和传播美学（Aesthetics）的工具。美学与信息技术的交织由此创造了一个美学循环（Aesthetic Cycle），在这种循环中，视觉美学刺激的持续供应提升了人们的[美学敏感度（Aesthetic Sensitivity）](https://www.interaction-design.org/literature/topics/empathy)，进而激励人们在包括交互产品（Interactive Products）在内的所有地方寻求美学 (Postrel, 2002)。

### 19.1.4.3 关于实用性考量中道德层面的说明

为了避免我们的立场被误解为：主张美学设计（aesthetic design）意味着实用性考量（practical concerns）应凌驾于所有其他考量之上，必须指出的是，上述描述的现实也包含一个道德维度（moral dimension）。设计中的美学与伦理考量并不一定相互矛盾 (Liu, 2003)。美学设计意味着设计师或组织尊重其受众，关注人们的需求与欲望，并在产品和环境的设计中投入思考与努力。例如，Ulrich (Ulrich 1984) 关于胆囊切除术（cholecystectomy）后住院患者康复情况的开创性研究发现，与窗外面对砖墙的患者相比，窗外能看到自然环境（natural settings）的患者康复速度更快，且需要的强效止痛药（potent analgesics）更少。四分之一个世纪后，Postrel (2008) 对当今医疗机构忽视美学设计的情况表示遗憾。相应地，当人们感受到被尊重和赏识时，会更倾向于维护一个美观且保养良好的环境 (Saito, 2008)。简而言之，美学设计旨在改善我们的生活。

## 19.2 人机交互（HCI）中视觉美学的研究

关于人机交互（Human-Computer Interaction, HCI）中视觉美学（Visual Aesthetics）各方面及其周边的研究，大致可以分为四个主要类别，分别探讨美学过程的不同维度：

1. 美学评估的前因（Antecedents），即是什么促使人们进行美学评估，以及更重要地，是什么导致了美学评估的差异；
2. 美学评估本身及其涉及的心理过程；
3. 美学评估的结果（Outcomes）或后果；
4. 调节变量（Moderating variables），或影响前因如何作用于美学评估以及评估如何影响结果的中介因素（Intervening factors）。

这些类别可以被视为图 8 中所述示意过程的一部分。我将在下文中详细阐述这些元素，并介绍处理这些问题的实证研究（Empirical studies）。

![](https://public-media.interaction-design.org/images/encyclopedia/visual_aesthetics/framework_for_visual_aesthetics_in_HCI_human-computer_interaction.jpg)

作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下文 [版权条款](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/visual-aesthetics#copyrightNotice) 中的“例外（Exceptions）”部分。

**图 19.9**：人机交互（Human-Computer Interaction, HCI）中视觉美学研究的通用框架。图中包含每个类别下的一些相关研究议题。

### 19.2.1 视觉美学的前因（Antecedents of visual aesthetics）

什么样的交互系统（interactive system）看起来更具美感？为什么有的系统以某种方式呈现美感，而另一个系统则以另一种方式呈现？这些问题具有极高的实际意义。只要我们能破译这种“美学代码（aesthetic code）”就好了！幸运的是，在可预见的未来，寻找视觉美学的“圣杯（Holy Grail）”依然遥不可及，因此在实验、新方法和深入研究方面仍有广阔的空间。在研究这一类别时，我们自然会首先关注 [设计指南（design guidelines）](https://www.interaction-design.org/literature/topics/design-guidelines) 和相关见解。然而，由于设计可能性的范围极广，设计工作具有创造性，且设计元素（design elements）之间的关系几乎是无限的，这使得我们极难分离出那些被认为具有美感、或在某种程度上影响美学感知（aesthetic perceptions）的具体设计方面。美学设计指南可能可以分为几类：从非常宽泛且抽象的（例如，“形式追随功能（form follows function）”），到非常具体的（例如，“背景与菜单栏之间应使用不同色相（hues）的颜色” (Kim et al., 2003)），以及介于两者之间的中等范围指南（例如，“视觉布局应是对称的” (Sutcliffe, 2002)）。它们可以用对象属性（object properties）或动机性（motivational）来表达。

以及情感中介（emotional mediators）（例如 Berlyne (1971) 的比较变量 [collative variables]）。

在本节开始时，我们提出了两个不同的问题。第一个问题——是什么让一个系统看起来更具美感或缺乏美感——在多年来的美学（aesthetic）和设计研究中可能更为核心。Park et al. (2005) 收集并列出了 11 个可能回答该问题的视觉属性（visual attributes）。其他更高层级的回答包括对比属性，如新颖性（novelty）和典型性（typicality）（Veryzer and Hutchinson, 1998; Hekkert et al., 2010），以及相关的处理流畅度（processing fluency）概念（Reber et al., 2004）。Hekkert et al. 的研究结果表明，典型性与新颖性的平衡能够提升美学评价（aesthetic evaluations）（另见 Kumara and Gargb, 2010, Tractinsky et al., 2011a）。同样，van Schaik and Ling (2011) 指出，他们称之为实用性（pragmatic）和享乐性（hedonic）的设计质量会影响对整体美感的感知。一些研究人员主张，可以识别出决定审美判断（Aesthetic Judgment）的形式化、客观属性，而这将最终实现对网页等显示界面的自动构图或检查（例如，Ngo et al., 2003）。这种方法受到了批评，理由是根植于客体中的审美规律具有“普适主义（Universalist）”色彩（Krippendorff, 2005），无法在个体、文化和情境差异（Context differences）中保持一致（Martindale et al., 1990; Krippendorff, 2005）。同样，Csikszentmihalyi (1991) 认为，形式方面（Formal aspects）极少能使物体对所有者产生价值。他推测，人们在感知设计中的有序或无序等形式属性时，并非遵循数学原理。尽管审美过程（Aesthetic processes）具有明显的主观性和情境依赖性（Context-dependent），但研究人员仍在继续探索交互系统（Interactive systems）审美属性的基础和形式原则。这些原则可以表达为旨在实现最优设计空间（Optimal design spaces）的计算模型（Computational models）。例如，Bauerly and Liu (2006) 指出，在基础图像中，对称性与平衡感（Symmetry and balance）会影响审美吸引力评分（Aesthetic appeal ratings）。然而，他们还发现，当使用更真实的（即情境依赖的）图像进行测试时，对称性与审美吸引力之间原本强烈的关系有所减弱。

网页。在照片领域，人们提出了其他预测美学评价（aesthetic evaluations）的方法。例如，Aquine 项目 (Datta et al., 2006, Datta et al., 2008) 建议结合多种算法方法（algorithmic approaches），根据各种视觉属性（visual properties）对照片进行分类。

然而，如前所述，由于应用程序和产品的多样性以及众多使用情境（use contexts）的唯一性，在人机交互（Human-Computer Interaction, HCI）领域，寻找通用的视觉美学指南与规律（universal visual aesthetic guidelines and laws）的问题变得更加复杂。此外，当代社会的动态特性（dynamic nature）以及许多交互设备和应用程序设计中类时尚（fashion-like）的趋向，使得美学成为一个变动且往往不可预测的目标 (Korman-Golander, 2011)。

![](https://public-media.interaction-design.org/images/encyclopedia/visual_aesthetics/website_design_fashion_trends_1.jpg)
作者/版权持有者：Gili Korman Golander。版权条款与许可：保留所有权利。经许可转载。详见下方 [版权条款](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/visual-aesthetics#copyrightNotice) 中的“例外”部分。

**图 19.10**：
网站设计的时尚趋势在不断变化。“Web 2.0”设计趋势的流行在 2007 年左右达到顶峰，此后一直呈下降趋势 (Korman-Golander, 2011)。

![](https://public-media.interaction-design.org/images/encyclopedia/visual_aesthetics/website_design_fashion_trends_2.jpg.jpg)
作者/版权持有者：Gili Korman Golander。版权条款和许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。
**图 19.11**：“单页布局（One-Page Layout）”网站设计趋势在 2008 年开始流行 (Korman-Golander, 2011)

这些限制将我们引导至第二个问题。在此，研究人员试图将审美刺激（aesthetic stimuli）分解为若干子维度（sub-dimensions），这些维度在不同场景或个人口味中的适用程度可能有所不同。此类维度通常源于对审美刺激的主观评估。例如，Park et al. (2004) 确定了网页的 13 个审美维度。Lavie and Tractinsky (2004) 采取了一种更为简洁（parsimonious）的维度处理方法，他们在网站设计的语境下，确定了视觉美感（visual aesthetic）的两个感知维度：“经典（classical）”和“表现（expressive）”。经典美感对应于传统的审美观点——即对称、简洁且有组织的设计。而表现维度则与设计者的创造力和原创性相关。该研究的一个重要方面在于证明了这些审美维度与各种交互结果（interaction outcomes）之间存在预期的相关性，例如感知可用性（perceived usability）和愉悦感（pleasing）

交互以及对服务质量的感知。同样地，Moshagen and Thielsch (2010) 提出了四个审美维度（Aesthetic dimensions）：[简洁性（Simplicity）](https://www.interaction-design.org/literature/topics/simplicity)、多样性（Diversity）、色彩丰富度（Colorfulness）和工艺感（Craftsmanship）。前两个维度分别与 Lavie and Tractinsky 的古典审美（Classical aesthetics）和表现审美（Expressive aesthetics）高度相关。所有四个维度都与吸引力（Appeal）相关。与 Lavie and Tractinsky 的结果一致，所有维度与各项结果衡量指标（Outcome measures）均呈正相关，但相关程度有所不同。

### 19.2.2 感知与评估视觉美学（Perceiving and evaluating visual aesthetics）

这一类别探讨了视觉美学（visual aesthetics）领域最基本的问题之一：人们如何从美学角度处理和评估视觉刺激？关于这些过程的详细描述可能并非人机交互（Human-Computer Interaction, HCI）所特有，因此过去和未来可能都会交给更基础研究领域的学者来处理。下文将介绍此类研究的发现，以使读者了解该领域的发展情况。关于美学过程最具有影响力的阐述之一由 Norman (2004) 提出，他认为美学感知和评估可以通过考虑三个不同层级的认知和情感过程来解释，他将其称为本能层（visceral）、行为层（behavioral）和反思层（reflective）。对环境刺激（包括美学刺激）的本能反应在很大程度上是通过进化机制（evolutionary mechanisms）发展而来的，它们在几乎是本能的水平上迅速执行，几乎不需要或完全不需要认知加工（cognitive processing）(Ortony et al., 2005)。因此，这一层级的反应是非常自动化的。另外两个层级的特点是具有日益复杂且截然不同的动机、情感和认知结构与过程，以及对刺激的反应速度较慢，倾向于产生更优（optimal）而非满意化（satisficing）的响应，且个体差异更大 (Ortony et al., 2005)。

美学反应研究（Studies of aesthetic reaction）

[研究] 已在所有层面（levels）上展开（例如，Csikszentmihalyi 1991; Leder et al., 2004; Winkielman et al., 2006; Jacobsen, 2010）。低层级研究（Low level research）的特点是其处理过程仅持续零点几秒。在这一层级，研究表明评价性审美判断（evaluative aesthetic judgment）包含一个两步过程：首先是早期印象形成（early impression formation），随后是评价性分类过程（evaluative categorization process）（Höfel and Jacobsen, 2007）。该层级的另一项研究结果认为，原型性（prototypicality）通过信息处理的便捷性（即流畅性，fluency）对审美评价产生积极影响（Winkielman et al., 2006）。

在人机交互（HCI）领域，已有多项研究探讨了在极短时间接触网页后的审美评价。这一层级的基础研究与 HCI 研究之间的区别之一在于，后者通常采用更具生态代表性（ecologically representative，即“真实”）的刺激物（stimuli）。Lindgaard 及其同事（Lindgaard et al., 2011）指出，即使仅接触某个设计 50 毫秒，也能形成稳定的审美评价。虽然部分研究质疑这些结果的鲁棒性（robustness），但其他研究则支持这样一种观点：我们不需要超过半秒的时间，就能对网页形成初步且稳定的审美印象（Lindgaard et al., 2006; Tractinsky et al., 2006）。

关于高层级审美处理（aesthetic processing）的研究则涉及更详尽的考量。总的来说，Leder et al. (2004) 提出了一个关于...的模型

审美欣赏（aesthetic appreciation）与审美判断（aesthetic judgment）。该模型涵盖了多种类别的审美处理（aesthetic processing），包括“自动（automatic）”和“深思熟虑（deliberate）”阶段，以及认知和情感反应。尽管研究审美评估（aesthetic evaluations）的高层级过程可能会引起人机交互（HCI）社区的兴趣，但迄今为止的研究更多地集中在审美处理作为设计刺激（design stimuli）与结果变量（outcome variables）——如用户参与度（user engagement）和信任（trust）——之间中介变量（mediator）的作用（例如，Hartmann et al., 2008, Lindgaard et al., 2011）。同样，Thuring and Mahlke (2007) 提出了一个模型，该模型整合了感知系统质量（perceived system qualities，包括视觉审美）对情感以及系统评估（appraisal）的影响。关于更长期的、反思性审美评估（reflective aesthetic evaluation）的研究则更为匮乏。在一般语境下，此类研究的一个例子是 Csikszentmihalyi (Csikszentmihalyi 1991) 对家用物品的研究。近期，关于交互系统审美方面研究开始采用更具时间依赖性（time-dependent）的方法 (Schaik and Ling, 2008)，并运用纵向研究方法（longitudinal methods）（例如，Karapanos et al., 2010）。

### 19.2.3 结果变量（Outcome Variables）

本节讨论的是与人机交互（HCI）中视觉美学相关且可能最具有实际意义的问题：美学感知与评价对 HCI 相关变量有哪些影响？虽然美学评价是如何形成的问题相对通用，但这些评价产生的结果可能具有高度的领域特定性（domain-specific）。事实上，HCI 研究主要将视觉美学的价值（无论是显式还是隐式地）视为一种中介力量（mediating force），而非目的本身；它介于 (1) 所设计系统或产品的特性，与 (2a) 产品的其他感知属性或 (2b) 美学评价的行为结果之间。早期研究（Kurasu and Kashimura, 1995, Tractinsky, 1997）就视觉美学与一个核心 HCI 变量——可用性（usability）之间的正相关关系提供了有趣的发现。尽管缺乏关于因果关系的明确指示，但这些研究暗示了后续研究更直接探讨的内容：人们对系统美感的感知可能会影响对系统其他属性的感知，例如易用性（ease of use）（Heijden, 2003; Cyr et al., 2006）、整体满意度（overall satisfaction）（Tractinsky et al., 2000; Lindgaard and Dudek, 2003; Cyr, 2008）、偏好（preferences）（Schmidt and Liu, 2009; Lee and Koubek, 2010）甚至绩效（performance）（Quinn and Tran, 2010, Sonderegger and Sauer, 2010）。

虽然早期的研究似乎...

虽然直觉上人们倾向于接受审美评估（aesthetic evaluations）足够迅速，能够先于对其他相关变量（related variables）的评估而产生，但随后的研究证明了这一观点确实成立（Lindgaard et al., 2006, Lindgaard et al. 2011; Tractinsky et al., 2006；另见上文第 2.2 节）。这些发现进一步推动了对审美设计（aesthetic design）潜在影响的探索，该研究领域可能是我们框架中所概述的四个类别中最为活跃的。这些研究涵盖的变量范围包括：对其他系统属性（system attributes）的评估、对系统的整体评估、对系统所代表的组织的态度，以及交互满意度（satisfaction from the interaction）。相关研究还开始探讨情感（affect）与情绪（emotions）在感知审美（perceived aesthetics）如何影响上述结果过程中所起到的中介作用（mediating）。下文我将综述几项探讨视觉审美（visual aesthetics）对各种变量影响的研究。需要说明的是，该名单仅为部分列举，且具有一定的随机性。*情感 (Affect)* 和 *情绪 (Emotions)* 是视觉美学 (Visual Aesthetics) 中经常被提及的推论。具有吸引力的设计对情绪的影响在多项研究中得到了证实，包括 Thuring and Mahlke (2007) 在便携式音乐播放器领域的研究，以及 Porat and Tractinsky (2012) 和 Cai and Xu (2011) 在在线购物领域的研究。美学对情绪影响的重要性体现在两个方面。首先，如前所述，正向情感有助于提升积极体验和幸福感 (Well-being)，因此其本身就是一个目的。其次，情绪在影响随后的信息处理 (Information Processing)、对其他系统属性的评估以及形成对系统的态度方面发挥着作用 (Sun and Zhang, 2006)。

*可信度 (Trustworthiness)* 是一个较早被研究的变量，被视为在线银行领域中视觉设计的产出 (Kim and Moon, 1998)。在其他关于网站设计的研究中，Cyr et al. (2010) 发现网站的颜色吸引力是网站信任 (Website Trust) 的一个显著决定因素，而 Lindgaard et al. (2011) 同样发现视觉吸引力 (Visual Appeal) 与信任之间存在强相关性...

网站。在一项关于网站的研究中，与信任相关的变量——学术部门的*声誉（reputation）*——与美学（aesthetics）相关 (Hartmann et al., 2007)。

几项研究探讨了视觉吸引力（visual appeal）对感知*可用性（perceived usability）*的影响。Lee and Koubek (2010) 发现，在使用前和使用后，可用性与美学之间存在高度正相关。与 Tractinsky et al. (2000) 的研究结果一致，他们发现感知美学对感知可用性的影响强于客观性能（objective performance）对可用性的影响。Sauer and Sonderegger (2009) 也得到了类似的结论。在另一项研究中，Sonderegger and Sauer (2010) 发现，使用具有高视觉吸引力手机的参与者比使用缺乏吸引力设备的参与者对其可用性的评分更高。在一项关于手机的研究中，Quinn and Tran (2010) 发现，吸引力（attractiveness）对 SUS 分数（SUS scores）方差（variance）的贡献与有效性（effectiveness）和效率（efficiency）相当。另一方面，多项研究发现视觉美学与可用性之间的这种关联较弱或不存在（例如，Lindgaard and Dudek, 2003, study 2; Hassenzahl, 2004a, Hassenzahl 2010; Thuring and Mahlke, 2007）。这些截然不同的结果表明，美学感知与可用性之间被假定的关联可能并非普遍存在。我们将在讨论下一个类别时详细阐述这一点。

视觉美学（Visual Aesthetics）被认为是影响产品*特性*（Product Character）（Hassenzahl, 2003; Krippendorff, 2005）或*品牌个性*（Brand Personality）（Park et al., 2005）感知的关键力量。因此，在一项关于产品选择的研究中，大多数参与者最频繁地提到美学与象征作用（Aesthetic and Symbolic Roles）影响了产品选择，这并不令人意外（Creusen and Schoormans, 2005）。在在线环境下，Mandel and Johnson (2002) 发现颜色和基于图像的启动（Image-based Priming）影响了在线消费者的产品选择。此外，Schmitt and Liu (2009) 发现，用户愿意为了一个在美学上更具吸引力的网页而牺牲加载速度（Loading Speed）。

根据 Norman (Norman 2004) 提出的“美的东西更好用”的观点，关于视觉美学结果最令人感兴趣的问题或许在于，它是否不仅影响用户对系统的感知和评价，还影响其*绩效*（Performance）。最近的研究已开始寻求关于这一问题的实证证据（Empirical Evidence）（例如 Moshagen et al., 2009）。在一项针对 11 种数据可视化技术（Data Visualization Techniques）的研究中，Cawthon and Moere (2007) 发现美学数据可视化与数据检索任务（Data Retrieval Tasks）的绩效之间存在正相关关系。Sonderegger and Sauer (2010) 以及 Quinn and Tran (2010) 同样发现，使用具有吸引力的手机比使用缺乏吸引力的手机时，任务绩效更高效。然而，Van Schaik and Ling (2009) 没有发现对经典（Classical）与表现主义（Expressive）的感知之间存在关系

审美与性能度量（performance measures）。

最后，需要注意的是，视觉美学（visual aesthetics）被认为是“用户体验（User Experience）”概念的一个显著前因（antecedent）（Hassenzahl and Tractinsky, 2006; Sutcliffe, 2009; Law and Schaik, 2010）。在最近一项关于用户体验 (UX) 文献的综述中，Bargas-Avila and Hornbaek (2011) 发现，情感（emotions）、愉悦感（enjoyment）和美学（aesthetics）是 UX 中最常被评估的维度。考虑到美学也是另外两个维度的前因，其在影响 UX 方面的作用确实非常巨大。在很大程度上，它与本章中阐述的几乎所有观点都相关。

### 19.2.4 调节变量（Moderating Variables）

感知美感（perceived beauty）与各种结果之间，或设计属性（design attributes）与审美感知（aesthetic perceptions）之间的关联，即使有坚实的科研证据、常识或哲学论据支持，也不应被认为是普遍的或决定性的 (Sutcliffe, 2010)。首先，如前一小节所述，尽管有研究通过实证发现了审美评价与其他感知系统属性（如可用性 Usability）评价之间的关联，但也有研究发现这种关联较弱甚至不存在，这表明至少在某些情况下，这些关联并不成立。其次，在社会环境下，关于“美即好（beautiful is good）”现象的研究比我们领域积累证据的时间更早且更久，研究结果表明，吸引力与对其他人类属性感知之间的关联并非是无条件的 (Eagly et al., 1991)。第三，基于我们对社会技术现象（socio-technical phenomena）的认知，在涉及个人、社会和技术力量的复杂现实中，存在这种决定性关系是没有意义的。因此，在视觉美学研究中采用权变方法（contingent approach）可能在描述审美评价是否以及如何在中介于各种前因（antecedents）与后果（consequences）之间方面更具成效。

那么，接下来的挑战就是识别并探讨各种因素如何起到

改变或调节审美过程（aesthetic process）。在 Tractinsky (2006) 中，我提供了一份此类潜在调节变量（moderators）的部分清单。该清单包括所使用的系统类型（一种可涵盖多个维度的分类法 [typology]，例如消费产品与计算机应用程序、小尺寸与大尺寸显示屏、个人与公共使用、享乐型 [hedonic] 与实用型 [utilitarian] 等）、使用情境（use context）（例如工作与娱乐）、文化差异（国家、亚文化、意识形态）等等。个体差异（Individual differences）构成了一组有趣的潜在调节变量，因为人们对审美刺激（aesthetic stimuli）的敏感度以及审美偏好（aesthetic preferences）存在巨大差异（例如 Bloch et al., 2003; Hoyer and Stokburger-Sauer, 2011）。Jacobsen (2004) 的研究发现，个体内部（intra-individual）的审美判断具有一致性，但个体之间（inter-individual）在美感判断上存在显著差异。此外，审美判断的群体模型（group model of aesthetic judgment）未能准确描述该研究中约一半的参与者。Pandir and Knight (2006) 在一项针对不同网站的研究中也发现了审美偏好的分歧。Norman (2004) 指出，情境因素（Contextual factors），如领域和任务类型，是决定用户绩效（performance）和满意度所需美学设计类型的重要考量因素。他认为，在某些特定领域（例如控制室）中，具有吸引力的设计未必是人们所追求的。Ben-Bassat et al (2006) 发现，当面对面向绩效的任务（performance-oriented task）时，人们更看重可用性（usability）而非美学因素；而 Van Schaik and Ling (2008) 则证明，为评估任务提供情境会影响吸引力评分（attractiveness ratings）。在在线购物环境中，Cai and Xu (2011) 发现，与购买实用型产品（utilitarian products）相比，在购买享乐型产品（hedonic products）时，表现性美学（expressive aesthetics）对购物愉悦感的影响更为显著。

个体因素（Individual factors）也可能影响具有不同审美偏好（aesthetic tastes）的人如何对前置变量（anteceding variables，例如客观设计属性）产生不同的感知 (Hoyer and Stokburger-Sauer, 2011)。在网站设计领域，Park et al. (2004) 发现，用户口味的差异与美学保真度（aesthetic fidelity）相关（即用户感知到的目标印象与设计者预期的程度...

（设计师）。研究还发现，个体差异（Individual differences）会影响人们在选择网站偏好时美学的相对重要性 (Hartmann et al., 2008)。

选择过程的属性被发现能够调节（moderate）美学评估（aesthetic evaluation）与产品选择（product choice）之间的关系，尤其是当用户需要为了其他系统质量而权衡（trade-off）美学时。例如，Ben-Bassat et al (2006) 发现，在常规条件下（如问卷调查），系统偏好或选择受美学影响，但当参与者必须为一个用于执行竞争性任务的系统出价时，情况则并非如此。Diefenbach and Hassenzahl (2007) 表明，在美观与可用性（beauty-usability）的权衡中，尽管人们可能比起更具可用性的产品更倾向于更美观的产品，但如果他们无法证明选择美观产品的合理性，他们最终会选择可用性更高的产品。

跨文化研究（Cross cultural studies）表明，国家文化和专业文化会影响美学评估及其前因（antecedents）与结果（consequences）之间的各种关系。几项研究在网站背景下证明了这种调节效应（moderating effect）。例如，Cyr (2008) 发现视觉设计（visual design）对中国用户的信任（trust）有影响，但在加拿大或德国用户中没有；Cyr et al (2010) 发现加拿大、德国和日本用户对网站颜色吸引力（color appeal）的反应有所不同。Hartmann et al (2007) 发现，美学评估和美学的重要性取决于用户的背景（设计...

……与技术性的（technical）；西方与东方的（Western vs. Asian）。

美学过程的权变性质（contingent nature）可以通过 Moshagen et al 的研究结果得到证明：高视觉美感（visual aesthetics）在可用性（usability）较低的情况下能提升表现，但在高可用性的情况下则没有影响。因此，他们引用了 Liu (Liu 2003) 的原则：“……工效美学设计（ergo-aesthetic design）并不意味着工作场所或产品设计师应当仅采用悦目或具有吸引力的设计。相反，工效美学设计主张谨慎且恰当地选择设计的美学水平，以适应预期用途的需求和特征”（p. 1298）。

## 19.3 未来研究方向

上述综述介绍了关于人机交互（Human-Computer Interaction, HCI）中视觉美学（Visual Aesthetics）的前因（Antecedents）及其影响的实证研究（Empirical Studies）结果，以及在该美学过程中调节这一关系的各种权变因素（Contingencies）。在本节中，我将讨论该领域的一些方法论问题（Methodological Issues）以及对未来研究的建议。

### 19.3.1 方法论问题（Methodological Issues）

对该领域研究的回顾揭示了几个方法论问题，这些问题可能也涉及审美过程中的掩蔽效应（masking effects）。其中一个方面涉及比整体审美评价（overall aesthetic evaluations）更细致的评价，而整体评价在本章调研的研究中非常普遍。探讨审美子维度（aesthetic sub dimensions）评价的研究（例如 Kim et al., 2003; Lavie and Tractinsky, 2004; Moshagen and Thielsch, 2010）有可能更详尽地阐述设计对审美过程，以及随后对交互系统（interactive system）的评价、态度及其交互行为的影响。

一个相关的问题涉及视觉审美评价或判断（visual aesthetics evaluations or judgment）的测量。在人机交互（HCI）领域，审美评价是通过单项量表（single item）和多项量表（multiple-item scales）来测量的。例如，Kurosu and Kashimura (1995)、Tractinsky (1997)、Schenkman and Jonsson (2000)、Hassenzahl and Monk (2010) 以及 Sonderegger and Sauer (2010) 使用了单项量表来询问各种应用程序和交互产品的美感。其他研究者，如 Schenkman and Jonsson (2000)、Van der Heijden (2003) 和 Moshagen et al., (2009)，则采用多项量表来测量吸引力（attractiveness）。虽然多项量表通常被认为更可靠，但单项量表具有一定的实际优势。总的来说，单项量表的主要优势在于它们使得

使问卷更短，从而减轻参与者的疲劳以及跳过部分项目的倾向。特别是在美学（aesthetics）研究中，使用单项测量（single items）可以让参与者在关注快速美学反应的研究中，对刺激做出更迅速的响应 (Lindgaard et al., 2006; Lindgaard et al., 2011; Tractinsky et al., 2006)。科学指导原则（scientific directives）与实际限制（practical constraints）之间的紧张关系可能并不像最初看起来那样严重。研究表明，当处理具体对象（例如待评估的应用程序或产品）及其具体属性时，单项测量（single item measures）与多项量表（multiple-item scales）一样有效 (Gardner et al., 1998; Bergkvist and Rossiter, 2007)。虽然科学界可能很难定义“美学”或“美（beauty）”这些概念的具体含义——这可能是因为处理这些概念的学科众多且赋予了它们不同的含义——但根据我的经验，普通人对这些术语的直觉理解与上述词典定义非常接近，而这一定义也指导了人机交互（HCI）中的视觉美感（visual beauty）研究。这一点可能值得进一步研究以验证，但如果正确，未来的科学和实践研究将能够安全地使用视觉美学的单项测量。

HCI 中关于视觉美学的研究采用了实验设计（experimental designs）与相关性设计（correlational designs）的混合方法。因为视觉美学中一些最有趣的方面……

如果审美研究涉及因果关系（cause and effect）问题，实验研究（experimental studies）似乎能提供最决定性的证据。使用实验设计来研究基础且相对简单的设计效应（design effects，例如使用基础图案的对称性）对审美感知（aesthetic perceptions）的影响是比较直接的 (Bauerly and Liu, 2006; Winkielman et al., 2006)。然而，如果我们希望使用更复杂且具有生态效度（ecologically valid）的刺激——如相关性研究（correlational studies）中所使用的刺激 (e.g., Lindgaard et al., 2006; Hassenzahl and Monk, 2010)——来研究审美设计的影响，难度会随之增加。因此，采用使用精细且真实刺激的实验设计是一项重大挑战。

理想情况下，为了[测试](https://www.interaction-design.org/literature/topics/test)因果效应（causal effects），研究应当独立地操纵各项设计属性（design attributes），从而将审美感知与对系统其他属性的感知区分开来。然而在实践中，由于这些属性之间存在先验关联（a priori association），这很难实现 (Moshagen et al., 2009)。试图实现这种独立审美操纵的一个常见结果是，它会导致被操纵刺激之间的方差（variance）相对较小（否则，强烈的审美操纵可能会引起其他实验因素的差异）。其危险之处在于，较小的方差和缺乏强烈的审美条件反过来会削弱视觉的效应...

在实验设计中操纵或选择审美刺激（Aesthetic Stimuli）的另一个挑战在于，审美刺激的程度是定义为“平均水平”（例如，通过预实验或操纵检查 [Manipulation Check]），还是为每个个体单独定义（例如，Tractinsky et al., 2000 所描述的程序）。后一种方法的优点是，提高了被分配到实验中不同审美组的个体确实能够以与其组别相对应的方式感知刺激的概率（相比之下，某些刺激虽然在平均意义上属于该组，但可能并不符合参与者的审美口味）。这将增加审美操纵的效应量（Effect Size）。另一方面，这种程序通常需要参与者在实验前接触（Pre-experimental Exposure）一组潜在的审美刺激。这一过程随后可能会与实验产生相互作用（例如，产生对实验的预期），并可能产生不必要的噪声（Noise）。

### 19.3.2 未来研究方向

本章再次确认了视觉美学（Visual Aesthetics）与一系列人机交互（Human-Computer Interaction, HCI）相关变量之间存在关联。然而，显而易见的是，我们对于围绕视觉美学之过程的权变性质（Contingent Nature）的理解仍然有限。因此，进一步探索这些权变因素（即：由于情境因素（Contextual Factors）导致视觉美学的感知或其效果发生变化的条件），似乎比试图确认视觉美学过程链中的直接关系，更有利于该领域知识的推进。

迄今为止，大多数研究都集中在人们对视觉美学的第一反应，或美学设计的短期影响上。这些研究的特点还在于，仅为参与者提供一组有限的美学刺激（Aesthetic Stimuli）供其选择。这类数据集的问题在于，它们不一定包含被参与者认为美观的设计。此外，此类研究很少能体现个体参与者的反思性美学价值（Reflective Aesthetic Value）。这类刺激可能足以产生短期印象，但很难用于评估沉思性评价（Contemplative Evaluations）以及美学过程的长期演变。因此，为了扩展 HCI 中视觉美学的研究图景，未来的研究应更加强调对设计产品和环境的反思性评估与沉思。另一个尚未获得足够关注的研究课题是设计师与用户之间的（脱节）联系（(dis)connect）。在其他设计学科中，研究发现非专业人士（laypeople）与设计师在审美评估（aesthetic evaluation）方面存在显著差异（例如，Nasar, 1997 和 Gifford et al, 2000 在建筑领域的研究）。在人机交互（Human-Computer Interaction, HCI）领域，Korman-Golander (2011) 发现设计师与软件工程专业的学生在评估网站设计趋势时存在类似的差异。同样，Inbar et al. (2007) 和 Bateman et al. (2010) 发现，Tufte (1983) 在其对“图表垃圾（chartjunk）”实践的具有影响力的批判中提出的图表极简主义设计建议，与人们对图表类型的实际偏好并不一致。迄今为止，据我所知，只有少数研究（例如 Park et al. (2004) 和 Bateman et al, 2010）试图剖析（tease out）...

这些差异的来源，并提供有助于弥合设计师与开发团队其他成员之间，以及开发团队与目标用户之间差距的方法。

在关于延伸自我（Extended Self）的开创性著作中，Belk (1988) 列举了多种产品类别，在这些类别中，品牌或产品类别与所有者的自我形象（Self-images）之间存在显著的形象一致性（Image Congruity）。该列表虽然未包含 IT 产品，但有充分的理由预期这种一致性同样存在于 IT 产品中，例如在个人计算设备、智能手机、媒体播放器、软件等的选择上。随后，我们可以探讨视觉美学（Visual Aesthetics）在激励人们选择这些交互媒体（Interactive Media）方面发挥了怎样的作用。

在讨论我们早期关于系统美学属性与感知属性（Perceived Attributes）之间关系的工作时，我们呼吁研究人员“进一步阐明导致用户将界面美学（Interface Aesthetics）与其他系统属性联系起来的认知和/或情感过程（Cognitive and/or Affective Processes）”（Tractinsky et al., 2000, p. 140）。近年来，已有几项研究接受了这一挑战。例如，Hassenzahl and Monk (2010) 指出，感知美学会影响用户对系统优劣（Goodness）的评价，进而影响对系统可用性（Usability）的评价。同样，Lindgaard et al. (2011) 认为，系统美学产生的初始吸引力形成了一种美学的“普遍态度（General Attitude）”，随后通过进一步使用而得到细化……

该系统以及基于高层级情感与认知处理（high level emotional and cognitive processing）的反思。然而，在探讨这些关系背后的机制（mechanisms）方面，似乎仍有广阔的持续研究空间。特别是，迫切需要针对 Norman (2004) 提出的三个处理层级（three levels of processing）中情感因素与认知因素之间相互作用（interplay）的研究 (Sun and Zhang, 2006; Thuring and Mahlke, 2007)。

人机交互（HCI）领域中关于视觉美学（visual aesthetics）的研究大多集中在 [用户界面](https://www.interaction-design.org/literature/topics/ui-design) 设计中相对稳定的属性上。因此，相关研究通常采用网站截图、交互产品的硬件设计或系统的通用美学特征。而视觉美学的动态方面（dynamic aspects）则较少受到关注。随着动态可视化（dynamic visualizations）、视频片段和各种动画在交互系统中被越来越多地嵌入，我们需要更好地掌握其美学特质（aesthetic qualities）(Chen, 2005)。在该方向上的初步尝试可见于一项关于动画感知美学维度（perceived aesthetic dimensions）的研究，该研究是在车载节能驾驶（eco-driving）信息呈现的背景下进行的 (Tractinsky et al., 2011b)。

最后，人们对视觉设计的评估及其效果所产生的诸多差异性（variability）可归因于个体与文化因素（individual and cultural factors）。这些因素可能包括对视觉美学敏感度的差异，以及在评估时对视觉美学赋予的不同权重（weighing）

系统与产品，以及对美的不同认知。此类研究可以探讨人们为何以及如何对交互系统与产品进行个性化（Personalize）处理（例如 Tractinsky and Lavie, 2002; Tractinsky and Zmiri, 2006）；为什么有些人偏好装饰性（Ornamented）的图表或网页，而另一些人则偏好极简主义风格（Minimalist styles）（例如 Inbar et al, 2007; Bateman et al., 2010）；为什么不同文化背景的人对网站色彩处理（Color treatments）的反应有所不同（Cyr et al., 2010）；以及属于不同趋势与时尚采纳群体（Trend and fashion adoption groups）的人是否偏好不同的网站设计（Korman-Golander 2011）。

## 19.4 结论

在过去的 15 年里，人机交互（Human-Computer Interaction, HCI）领域对视觉美学（Visual Aesthetics）的关注显著增加。该领域已从最初仅报道感知美学（Perceived Aesthetics）与表观可用性（Apparent Usability）之间相关性的简短会议论文（Korosu and Kashimura, 1995），发展成为了一个丰富的研究领域（Field of Inquiry）。这种关注可能是由一些具有挑衅性的标题所激发，例如“美即可用”（“What is beautiful is usable”，Tractinsky et al., 2000）和“吸引人的东西运行得更好”（“Attractive things work better”，Norman, 2004）。然而，更有可能的是，这与这段时间以来席卷我们的生活并重塑了人机交互领域的技术和社会变革相一致。

## 19.5 References

[Angeli](https://www.interaction-design.org/references/authors/antonella_de_angeli.html), Antonella De, [Sutcliffe](https://www.interaction-design.org/references/authors/alistair_g__sutcliffe.html), Alistair G. and [Hartmann](https://www.interaction-design.org/references/authors/jan_hartmann.html), Jan (2006): Interaction, usability and aesthetics: what influences users' preferences?. In: [Proceedings of DIS06: Designing Interactive Systems: Processes, Practices, Methods, & Techniques](https://www.interaction-design.org/references/conferences/proceedings_of_dis06-_designing_interactive_systems-_processes%2C_practices%2C_methods%2C_%26_techniques.html) 2006. pp. 271-280
[Arnheim](https://www.interaction-design.org/references/authors/rudolf_arnheim.html), Rudolf (1966): Order and complexity in landscape design. In: [Arnheim](https://www.interaction-design.org/references/authors/rudolf_arnheim.html), Rudolf (ed.). "Toward a Psychology of Art". University of California Press

[Bargas-Avila](https://www.interaction-design.org/references/authors/javier_a__bargas-avila.html), Javier A. and [Hornbæk](https://www.interaction-design.org/references/authors/kasper_hornb%E6k.html), Kasper (2011): Old wine in new bottles or novel challenges: a critical analysis of empirical studies of user experience. In: [Proceedings of ACM CHI 2011 Conference on Human Factors in Computing Systems](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2011_conference_on_human_factors_in_computing_systems.html) 2011. pp. 2689-2698
[Bateman](https://www.interaction-design.org/references/authors/scott_bateman.html), Scott, [Mandryk](https://www.interaction-design.org/references/authors/regan_l__mandryk.html), Regan L., [Gutwin](https://www.interaction-design.org/references/authors/carl_gutwin.html), Carl, [Genest](https://www.interaction-design.org/references/authors/aaron_genest.html), Aaron, [McDine](https://www.interaction-design.org/references/authors/david_mcdine.html), David and [Brooks](https://www.interaction-design.org/references/authors/christopher_brooks.html), Christopher (2010): Useful junk?: the effects of visual embellishment on comprehension and memorability of charts. In: [Proceedings of ACM CHI 2010 Conference on Human Factors in Computing Systems](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2010_conference_on_human_factors_in_computing_systems.html) 2010. pp. 2573-2582

[Bauerly](https://www.interaction-design.org/references/authors/michael_bauerly.html), Michael and [Liu](https://www.interaction-design.org/references/authors/yili_liu.html), Yili (2006): *Computational modeling and experimental investigation of effects of compositional elements on interface and design aesthetics*. In [International Journal of Human-Computer Studies](https://www.interaction-design.org/references/periodicals/international_journal_of_human-computer_studies.html), 64 (8) pp. 670-682
[Belk](https://www.interaction-design.org/references/authors/russell_w__belk.html), Russell W. (1988): *Possessions and the Extended Self*. In [Journal of Consumer Research](https://www.interaction-design.org/references/periodicals/journal_of_consumer_research.html), 15 (2) pp. 139-168
[Ben-Bassat](https://www.interaction-design.org/references/authors/tamar_ben-bassat.html), Tamar, [Meyer](https://www.interaction-design.org/references/authors/joachim_meyer.html), Joachim and [Tractinsky](https://www.interaction-design.org/references/authors/noam_tractinsky.html), Noam (2006): *Economic and subjective measures of the perceived value of aesthetics and usability*. In [ACM Transactions on Computer-Human Interaction](https://www.interaction-design.org/references/periodicals/acm_transactions_on_computer-human_interaction.html), 13 (2) pp. 210-234

[Bergkvist](https://www.interaction-design.org/references/authors/lars_bergkvist.html), Lars and [Rossiter](https://www.interaction-design.org/references/authors/john_r_rossiter.html), John R (2007): *The Predictive Validity of Multiple-Item Versus Single-Item Measures of the Same Constructs*. In [Journal of Marketing Research](https://www.interaction-design.org/references/periodicals/journal_of_marketing_research.html), 44 (2) pp. 175-184
[Berlyne](https://www.interaction-design.org/references/authors/d__e__berlyne.html), D. E. (1971): *Aesthetics and psychobiology.* Appleton-Century-Crofts
[Bloch](https://www.interaction-design.org/references/authors/peter_h__bloch.html), Peter H. (2011): *Product Design and *[*Marketing*](https://www.interaction-design.org/literature/topics/marketing)*: Reflections After Fifteen Years*. In [Design](https://www.interaction-design.org/references/periodicals/design.html), 28 (3) pp. 378-380
[Bloch](https://www.interaction-design.org/references/authors/peter_h__bloch.html), Peter H., [Brunel](https://www.interaction-design.org/references/authors/f__f__brunel.html), F. F. and [Arnold](https://www.interaction-design.org/references/authors/t__j__arnold.html), T. J. (2003): *Individual Differences in the Centrality of Visual Product Aesthetics: Concept and Measurement*. In [Journal of Consumer Research](https://www.interaction-design.org/references/periodicals/journal_of_consumer_research.html), 29 (4) pp. 551-565

[Brooks](https://www.interaction-design.org/references/authors/fred_brooks.html), Fred (1975): *The Mythical Man-Month: Essays on Software Engineering.* Addison-Wesley Publishing
[Cai](https://www.interaction-design.org/references/authors/shun_cai.html), Shun and [Xu](https://www.interaction-design.org/references/authors/yunjie_%28calvin%29_xu.html), Yunjie (Calvin) (2011): *Designing Not Just for Pleasure: Effects of Web Site Aesthetics on Consumer Shopping Value*. In [International Journal of Electronic Commerce](https://www.interaction-design.org/references/periodicals/international_journal_of_electronic_commerce.html), 15 (4) p. 159–187
[Card](https://www.interaction-design.org/references/authors/stuart_k__card.html), Stuart K., [Moran](https://www.interaction-design.org/references/authors/thomas_p__moran.html), Thomas P. and [Newell](https://www.interaction-design.org/references/authors/allen_newell.html), Allen (1983): *The Psychology of Human-Computer Interaction.*Hillsdale, NJ, Lawrence Erlbaum Associates
[Carlson](https://www.interaction-design.org/references/authors/allen_carlson.html), Allen (2000): *Aesthetics and the Environment: The Appreciation of Nature, Art and Architecture.*Routledge

[Cawthon](https://www.interaction-design.org/references/authors/nick_cawthon.html), Nick and [Moere](https://www.interaction-design.org/references/authors/andrew_vande_moere.html), Andrew Vande (2007): The Effect of Aesthetic on the Usability of Data Visualization. In:[Proceedings of the 11th International Conference Information Visualization](https://www.interaction-design.org/references/conferences/proceedings_of_the_11th_international_conference_information_visualization.html) 2007. pp. 637-648
[Chen](https://www.interaction-design.org/references/authors/chaomei_chen.html), Chaomei (2005): *Top 10 unsolved *[*information visualization*](https://www.interaction-design.org/literature/topics/information-visualization)* problems*. In [IEEE Computer Graphics and Applications](https://www.interaction-design.org/references/periodicals/ieee_computer_graphics_and_applications.html), 25 (4) pp. 12-16
[Creusen](https://www.interaction-design.org/references/authors/marielle_e__h__creusen.html), Marielle E. H. and [Schoormans](https://www.interaction-design.org/references/authors/jan_p__l__schoormans.html), Jan P. L. (2005): *The Different Roles of Product Appearance in Consumer Choice*. In [Journal of Product Innovation Management](https://www.interaction-design.org/references/periodicals/journal_of_product_innovation_management.html), 22 (1) pp. 63-81

[Csikszentmihalyi](https://www.interaction-design.org/references/authors/mihaly_csikszentmihalyi.html), Mihaly (1991): *Design and Order in Everyday Life*. In [Design Issues](https://www.interaction-design.org/references/periodicals/design_issues.html), 8 (1) pp. 26-34
[Cyr](https://www.interaction-design.org/references/authors/dianne_cyr.html), Dianne (2008): *Modeling Web Site Design Across Cultures: Relationships to Trust, Satisfaction, and E-Loyalty*. In [Journal of Management Information Systems](https://www.interaction-design.org/references/periodicals/journal_of_management_information_systems.html), 24 (4) pp. 47-72
[Cyr](https://www.interaction-design.org/references/authors/dianne_cyr.html), Dianne, [Head](https://www.interaction-design.org/references/authors/milena_m__head.html), Milena M. and [Ivanov](https://www.interaction-design.org/references/authors/alex_ivanov.html), Alex (2006): *Design aesthetics leading to m-loyalty in mobile commerce*. In [Information & Management](https://www.interaction-design.org/references/periodicals/information_%26_management.html), 43 (8) pp. 950-963

[Cyr](https://www.interaction-design.org/references/authors/dianne_cyr.html), Dianne, [Kindra](https://www.interaction-design.org/references/authors/gurprit_s__kindra.html), Gurprit S. and [Dash](https://www.interaction-design.org/references/authors/satyabhusan_dash.html), Satyabhusan (2008): *Web site design, trust, satisfaction and e-loyalty: the Indian experience*. In [Online Information Review](https://www.interaction-design.org/references/periodicals/online_information_review.html), 32 (6) pp. 773-790
[Cyr](https://www.interaction-design.org/references/authors/dianne_cyr.html), Dianne, [Head](https://www.interaction-design.org/references/authors/milena_head.html), Milena and [Larios](https://www.interaction-design.org/references/authors/hector_larios.html), Hector (2010): *Colour appeal in website design within and across cultures: A multi-method evaluation*. In [International Journal of Human-Computer Studies](https://www.interaction-design.org/references/periodicals/international_journal_of_human-computer_studies.html), 68 (1) pp. 1-21

[Datta](https://www.interaction-design.org/references/authors/ritendra_datta.html), Ritendra, [Li](https://www.interaction-design.org/references/authors/jia_li.html), Jia and [Wang](https://www.interaction-design.org/references/authors/j__z__wang.html), J. Z. (2008): Algorithmic inferencing of aesthetics and emotion in natural images: An exposition. In: [Image Processing, 2008. ICIP 2008. 15th IEEE International Conference on](https://www.interaction-design.org/references/conferences/image_processing%2C_2008__icip_2008__15th_ieee_international_conference_on.html) 2008. pp. 105-108
[Datta](https://www.interaction-design.org/references/authors/ritendra_datta.html), Ritendra, [Joshi](https://www.interaction-design.org/references/authors/d__joshi.html), D., [Li](https://www.interaction-design.org/references/authors/j__li.html), J. and [Wang](https://www.interaction-design.org/references/authors/james_z__wang.html), James Z. (2006): *Studying aesthetics in photographic images using a computational approach*. In [Distribution](https://www.interaction-design.org/references/periodicals/distribution.html), 3953 pp. 288-301
[Davis](https://www.interaction-design.org/references/authors/fred_d__davis.html), Fred D. (1989): *Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology*. In [MIS Quarterly](https://www.interaction-design.org/references/periodicals/mis_quarterly.html), 13 (3) pp. 319-340

[Dion](https://www.interaction-design.org/references/authors/karen_dion.html), Karen, [Berscheid](https://www.interaction-design.org/references/authors/ellen_berscheid.html), Ellen and [Walster](https://www.interaction-design.org/references/authors/elaine_walster.html), Elaine (1972): *What is beautiful is good*. In [Journal of Personality and Social Psychology](https://www.interaction-design.org/references/periodicals/journal_of_personality_and_social_psychology.html), 24 (3) pp. 285-290
[Dutton](https://www.interaction-design.org/references/authors/denis_dutton.html), Denis (2008): *The Art Instinct: Beauty, Pleasure, and Human Evolution.* Bloomsbury Press
[Eagly](https://www.interaction-design.org/references/authors/alice_h__eagly.html), Alice H., [Ashmore](https://www.interaction-design.org/references/authors/richard_d__ashmore.html), Richard D., [Makhijani](https://www.interaction-design.org/references/authors/mona_g__makhijani.html), Mona G. and [Longo](https://www.interaction-design.org/references/authors/laura_c__longo.html), Laura C. (1991): *What is beautiful is good, but..: A meta-analytic review of research on the physical attractiveness stereotype*. In [Psychological Bulletin](https://www.interaction-design.org/references/periodicals/psychological_bulletin.html), 110 (1) pp. 109-128
[Fishwick](https://www.interaction-design.org/references/authors/paul_a__fishwick.html), Paul A. (ed.) (2006): *Aesthetic Computing.* The MIT Press

[Forlizzi](https://www.interaction-design.org/references/authors/jodi_forlizzi.html), Jodi (2008): *The product ecology: Understanding social product use and supporting design culture*. In[International Journal of Design](https://www.interaction-design.org/references/periodicals/international_journal_of_design.html), 2 (1) pp. 11-20
[Gardner](https://www.interaction-design.org/references/authors/d__g__gardner.html), D. G., [Cummings](https://www.interaction-design.org/references/authors/l__l__cummings.html), L. L., [Dunham](https://www.interaction-design.org/references/authors/r__b__dunham.html), R. B. and [Pierce](https://www.interaction-design.org/references/authors/j__l__pierce.html), J. L. (1998): *Single-Item Versus Multiple-Item Measurement Scales: An Empirical Comparison*. In [Educational and Psychological Measurement](https://www.interaction-design.org/references/periodicals/educational_and_psychological_measurement.html), 58 (6) pp. 898-915

[Gifford](https://www.interaction-design.org/references/authors/robert_gifford.html), Robert, [Hine](https://www.interaction-design.org/references/authors/donald_w_hine.html), Donald W, [Muller-Clemm](https://www.interaction-design.org/references/authors/werner_muller-clemm.html), Werner, [Reynolds](https://www.interaction-design.org/references/authors/d%27arcy_j__reynolds.html), D'arcy J. and [Shaw](https://www.interaction-design.org/references/authors/kelly_t__shaw.html), Kelly T. (2000): *Decoding Modern Architecture: A Lens Model Approach for Understanding the Aesthetic Differences of Architects and Laypersons*. In [Environment And Behavior](https://www.interaction-design.org/references/periodicals/environment_and_behavior.html), 32 (2) pp. 163-187
[Gladwell](https://www.interaction-design.org/references/authors/malcolm_gladwell.html), Malcolm (2000): *The Tipping Point: How Little Things Can Make a Big Difference.* Back Bay Books
[Hamermesh](https://www.interaction-design.org/references/authors/daniel_s__hamermesh.html), Daniel S. and [Biddle](https://www.interaction-design.org/references/authors/jeff_e__biddle.html), Jeff E. (1994): *Beauty and the Labor Market*. In [American Economic Review](https://www.interaction-design.org/references/periodicals/american_economic_review.html), 84 (5) pp. 1174-1194

[Hamermesh](https://www.interaction-design.org/references/authors/daniel_s__hamermesh.html), Daniel S. and [Parker](https://www.interaction-design.org/references/authors/amy_m__parker.html), Amy M. (2003): *Beauty in the Classroom: Professors' Pulchritude and Putative Pedagogical Productivity*. In [National Bureau of Economic Research Working Paper Series](https://www.interaction-design.org/references/periodicals/national_bureau_of_economic_research_working_paper_series.html), 9853 (4) pp. 369-376
[Hartmann](https://www.interaction-design.org/references/authors/jan_hartmann.html), Jan, [Sutcliffe](https://www.interaction-design.org/references/authors/alistair_g__sutcliffe.html), Alistair G. and [Angeli](https://www.interaction-design.org/references/authors/antonella_de_angeli.html), Antonella De (2008): *Towards a theory of user judgment of aesthetics and user interface quality*. In [ACM Transactions on Computer-Human Interaction](https://www.interaction-design.org/references/periodicals/acm_transactions_on_computer-human_interaction.html), 15 (4) p. 15

[Hartmann](https://www.interaction-design.org/references/authors/jan_hartmann.html), Jan, [Sutcliffe](https://www.interaction-design.org/references/authors/alistair_g__sutcliffe.html), Alistair G. and [Angeli](https://www.interaction-design.org/references/authors/antonella_de_angeli.html), Antonella De (2007): Investigating attractiveness in web user interfaces. In: [Proceedings of ACM CHI 2007 Conference on Human Factors in Computing Systems](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2007_conference_on_human_factors_in_computing_systems.html) 2007. pp. 387-396
[Hassenzahl](https://www.interaction-design.org/references/authors/marc_hassenzahl.html), Marc (2007): Aesthetics in interactive products: Correlates and consequences of beauty. In: [Schifferstein](https://www.interaction-design.org/references/authors/hendrik_n__j__schifferstein.html), Hendrik N. J. and [Hekkert](https://www.interaction-design.org/references/authors/paul_hekkert.html), Paul (eds.). "Product Experience". Elsevier Science

[Hassenzahl](https://www.interaction-design.org/references/authors/marc_hassenzahl.html), Marc (2003): The Thing and I: Understanding the Relationship Between User and Product. In: [Blythe](https://www.interaction-design.org/references/authors/mark-dot-a__blythe.html), Mark.A., [Overbeeke](https://www.interaction-design.org/references/authors/kees_overbeeke.html), Kees, [Monk](https://www.interaction-design.org/references/authors/andrew_f__monk.html), Andrew F. and [Wright](https://www.interaction-design.org/references/authors/peter_c__wright.html), Peter C. (eds.). "Funology: From Usability to Enjoyment". Springerpp. 31-42
[Hassenzahl](https://www.interaction-design.org/references/authors/marc_hassenzahl.html), Marc (2004b): *Beautiful Objects as an Extension of the Self: A Reply*. In [Human-Computer Interaction](https://www.interaction-design.org/references/periodicals/human-computer_interaction.html), 19 (4) pp. 377-386
[Hassenzahl](https://www.interaction-design.org/references/authors/marc_hassenzahl.html), Marc (2004a): *The Interplay of Beauty, Goodness, and Usability in Interactive Products*. In [Human-Computer Interaction](https://www.interaction-design.org/references/periodicals/human-computer_interaction.html), 19 (4) pp. 319-349

[Hassenzahl](https://www.interaction-design.org/references/authors/marc_hassenzahl.html), Marc and [Monk](https://www.interaction-design.org/references/authors/andrew_monk.html), Andrew (2010): *The Inference of Perceived Usability From Beauty*. In [Human Computer Interaction](https://www.interaction-design.org/references/periodicals/human_computer_interaction.html), 25 (3) pp. 235-260
[Hassenzahl](https://www.interaction-design.org/references/authors/marc_hassenzahl.html), Marc and [Tractinsky](https://www.interaction-design.org/references/authors/noam_tractinsky.html), Noam (2006): *User experience - a research agenda*. In [Behaviour and Information Technology](https://www.interaction-design.org/references/periodicals/behaviour_and_information_technology.html), 25 (2) pp. 91-97
[Heijden](https://www.interaction-design.org/references/authors/hans_van_der_heijden.html), Hans van der (2003): *Factors influencing the usage of websites: the case of a generic portal in The Netherlands*. In [Information and Management](https://www.interaction-design.org/references/periodicals/information_and_management.html), 40 (6) pp. 541-549

[Hekkert](https://www.interaction-design.org/references/authors/paul_hekkert.html), Paul, [Snelders](https://www.interaction-design.org/references/authors/dirk_snelders.html), Dirk and [Wieringen](https://www.interaction-design.org/references/authors/piet_c__w__wieringen.html), Piet C. W. (2010): *"Most advanced, yet acceptable": Typicality and novelty as joint predictors of aesthetic preference in industrial design*. In [British Journal of Psychology](https://www.interaction-design.org/references/periodicals/british_journal_of_psychology.html), 94 (1) pp. 111-124
[Hooper](https://www.interaction-design.org/references/authors/kristina_hooper.html), Kristina (1986): Architectural design: an analogy. In: [Norman](https://www.interaction-design.org/references/authors/donald_a__norman.html), Donald A. and [Draper](https://www.interaction-design.org/references/authors/stephen_w__draper.html), Stephen W. (eds.). "[User Centered](https://www.interaction-design.org/literature/topics/user-centered-design) System Design: New Perspectives on Human-Computer Interaction". Hillsdale, NJ: Lawrence Erlbaum Associates

[Hoyer](https://www.interaction-design.org/references/authors/wayne_hoyer.html), Wayne and [Stokburger-Sauer](https://www.interaction-design.org/references/authors/nicola_stokburger-sauer.html), Nicola (2011): *The role of aesthetic taste in consumer behavior*. In [Journal of the Academy of Marketing Science](https://www.interaction-design.org/references/periodicals/journal_of_the_academy_of_marketing_science.html),
[Höfela](https://www.interaction-design.org/references/authors/lea_h%F6fela.html), Lea and [Jacobsena](https://www.interaction-design.org/references/authors/thomas_jacobsena.html), Thomas (2007): *Electrophysiological Indices of Processing Symmetry and Aesthetics: A Result of Judgment Categorization or Judgment Report?*. In [Journal of Psychophysiology](https://www.interaction-design.org/references/periodicals/journal_of_psychophysiology.html), 21 (1) pp. 9-21

[Inbar](https://www.interaction-design.org/references/authors/ohad_inbar.html), Ohad, [Tractinsky](https://www.interaction-design.org/references/authors/noam_tractinsky.html), Noam and [Meyer](https://www.interaction-design.org/references/authors/joachim_meyer.html), Joachim (2007): Minimalism in information visualization: attitudes towards maximizing the data-ink ratio. In: [Brinkman](https://www.interaction-design.org/references/authors/willem-paul_brinkman.html), Willem-Paul, [Ham](https://www.interaction-design.org/references/authors/dong-han_ham.html), Dong-Han and [Wong](https://www.interaction-design.org/references/authors/b__l__william_wong.html), B. L. William (eds.) [ECCE 2007 - Proceedings of the 14th European Conference on Cognitive Ergonomics](https://www.interaction-design.org/references/conferences/ecce_2007_-_proceedings_of_the_14th_european_conference_on_cognitive_ergonomics.html) August 28-31, 2007, London, UK. pp. 185-188
[Jacobsen](https://www.interaction-design.org/references/authors/thomas_jacobsen.html), Thomas (2004): *Individual and group modelling of aesthetic judgment strategies*. In [British journal of psychology London England 1953](https://www.interaction-design.org/references/periodicals/british_journal_of_psychology_london_england_1953.html), 95 (0) pp. 41-56

[Jacobsen](https://www.interaction-design.org/references/authors/thomas_jacobsen.html), Thomas (2010): *Beauty and the brain: culture, history and individual differences in aesthetic appreciation*. In [Journal of Anatomy](https://www.interaction-design.org/references/periodicals/journal_of_anatomy.html), 216 (2) pp. 184-191
[Johnson](https://www.interaction-design.org/references/authors/paul-alan_johnson.html), Paul-Alan (1994): *The Theory of Architecture: Concepts, Themes & Practices.* Van Nostrand Reinhold
[Jones](https://www.interaction-design.org/references/authors/edward_ellsworth_jones.html), Edward Ellsworth (1990): *Interpersonal Perception.* W H Freeman and Co (Sd)
[Jr.](https://www.interaction-design.org/references/authors/frank_gibney_jr-dot-.html), Frank Gibney and [Luscombe](https://www.interaction-design.org/references/authors/belinda_luscombe.html), Belinda (2008). *The Redesigning Of America*. Retrieved 1 December 2011 from Times.com: [http://www.time.com/time/magazine/article/0,9171,9...](http://www.time.com/time/magazine/article/0,9171,996372,00.html)

[Karapanos](https://www.interaction-design.org/references/authors/evangelos_karapanos.html), Evangelos, [Zimmerman](https://www.interaction-design.org/references/authors/john_zimmerman.html), John, [Forlizzi](https://www.interaction-design.org/references/authors/jodi_forlizzi.html), Jodi and [Martens](https://www.interaction-design.org/references/authors/jean-bernard_martens.html), Jean-Bernard (2010): *Measuring the dynamics of remembered experience over time*. In [Interacting with Computers](https://www.interaction-design.org/references/periodicals/interacting_with_computers.html), 22 (5) pp. 328-335
[Kim](https://www.interaction-design.org/references/authors/jinwoo_kim.html), Jinwoo and [Moon](https://www.interaction-design.org/references/authors/jae_yun_moon.html), Jae Yun (1998): *Designing Towards Emotional Usability in Customer Interfaces -- Trustworthiness of Cyber-Banking System Interfaces*. In [Interacting with Computers](https://www.interaction-design.org/references/periodicals/interacting_with_computers.html), 10 (1) pp. 1-29

[Kim](https://www.interaction-design.org/references/authors/jinwoo_kim.html), Jinwoo, [Lee](https://www.interaction-design.org/references/authors/jungwon_lee.html), Jungwon, [Han](https://www.interaction-design.org/references/authors/kwanghee_han.html), Kwanghee and [Lee](https://www.interaction-design.org/references/authors/moonkyu_lee.html), Moonkyu (2002): *Businesses as Buildings: Metrics for the Architectural Quality of Internet Businesses*. In [Information Systems Research](https://www.interaction-design.org/references/periodicals/information_systems_research.html), 13 (3) pp. 239-254
[Kim](https://www.interaction-design.org/references/authors/jinwoo_kim.html), Jinwoo, [Lee](https://www.interaction-design.org/references/authors/jooeun_lee.html), Jooeun and [Choi](https://www.interaction-design.org/references/authors/dongseong_choi.html), Dongseong (2003): *Designing emotionally evocative homepages: an empirical study of the *[*quantitative*](https://www.interaction-design.org/literature/topics/quantitative-research)* relations between design factors and emotional dimensions*. In [International Journal of Human-Computer Studies](https://www.interaction-design.org/references/periodicals/international_journal_of_human-computer_studies.html), 59 (6) pp. 899-940

[Kleine](https://www.interaction-design.org/references/authors/susan_schultz_kleine.html), Susan Schultz, [Kleine](https://www.interaction-design.org/references/authors/robert_e__kleine.html), Robert E. and [Allen](https://www.interaction-design.org/references/authors/chris_t__allen.html), Chris T. (1995): *How Is a Possession "Me" or "Not Me"? Characterizing Types and an Antecedent of Material Possession Attachment*. In [Journal of Consumer Research](https://www.interaction-design.org/references/periodicals/journal_of_consumer_research.html), 22 (3) pp. 327-43
[Korman-Golander](https://www.interaction-design.org/references/authors/gili_korman-golander.html), Gili (2011). *Aspects of Fashion/Trends in *[*Web Design*](https://www.interaction-design.org/literature/topics/web-design)*, M.Sc. Thesis*. Ben-Gurion Univerity of the Negev [http://aranne5.lib.ad.bgu.ac.il/others/KormanGolanderGili.pdf](http://aranne5.lib.ad.bgu.ac.il/others/KormanGolanderGili.pdf)
[Krippendorff](https://www.interaction-design.org/references/authors/klaus_krippendorff.html), Klaus (2005): *The Semantic Turn: A New Foundation for Design.* CRC Press
[Kruft](https://www.interaction-design.org/references/authors/hanno-walter_kruft.html), Hanno-Walter (1994): *A History of Architectural Theory: From Vitruvius to the Present.* Zwemmer

[Kumara](https://www.interaction-design.org/references/authors/minu_kumara.html), Minu and [Gargb](https://www.interaction-design.org/references/authors/nitika_gargb.html), Nitika (2010): *Aesthetic principles and cognitive emotion appraisals: How much of the beauty lies in the eye of the beholder?*. In [Journal of Consumer Psychology](https://www.interaction-design.org/references/periodicals/journal_of_consumer_psychology.html), 20 (4) pp. 485-494
[Kurosu](https://www.interaction-design.org/references/authors/masaaki_kurosu.html), Masaaki and [Kashimura](https://www.interaction-design.org/references/authors/kaori_kashimura.html),
 Kaori (1995): Apparent usability vs. inherent usability: experimental 
analysis on the determinants of the apparent usability. In: [CHI 95 Conference Companion 1995](https://www.interaction-design.org/references/conferences/chi_95_conference_companion_1995.html) 1995. pp. 292-293
[Lavie](https://www.interaction-design.org/references/authors/talia_lavie.html), Talia and [Tractinsky](https://www.interaction-design.org/references/authors/noam_tractinsky.html), Noam (2004): *Assessing dimensions of perceived visual aesthetics of web sites*. In[International Journal of Human-Computer Studies](https://www.interaction-design.org/references/periodicals/international_journal_of_human-computer_studies.html), 60 (3) pp. 269-298

[Law](https://www.interaction-design.org/references/authors/effie_l-dot--c__law.html), Effie L.-C. and [Schaik](https://www.interaction-design.org/references/authors/paul_van_schaik.html), Paul Van (2010): *Modelling user experience -- An agenda for research and practice*. In[Interacting with Computers](https://www.interaction-design.org/references/periodicals/interacting_with_computers.html), 22 (5) pp. 313-322
[Leder](https://www.interaction-design.org/references/authors/helmut_leder.html), Helmut, [Belke](https://www.interaction-design.org/references/authors/benno_belke.html), Benno, [Oeberst](https://www.interaction-design.org/references/authors/andries_oeberst.html), Andries and [Augustin](https://www.interaction-design.org/references/authors/dorothee_augustin.html), Dorothee (2004): *A model of aesthetic appreciation and aesthetic judgments*. In [British Journal of Psychology](https://www.interaction-design.org/references/periodicals/british_journal_of_psychology.html), 95 (0) pp. 489-508

[Lee](https://www.interaction-design.org/references/authors/allen_s__lee.html), Allen S. (1991): Architecture as a reference discipline for MIS. In: [Nissen](https://www.interaction-design.org/references/authors/h__e__nissen.html), H. E., [Klein](https://www.interaction-design.org/references/authors/h__k__klein.html), H. K. and [Hirschheim](https://www.interaction-design.org/references/authors/r__hirschheim.html), R. (eds.). "Information Systems Research: Contemporary Approaches & Emergent Traditions". North Hollandp. 573–592.
[Lee](https://www.interaction-design.org/references/authors/sangwon_lee.html), Sangwon and [Koubek](https://www.interaction-design.org/references/authors/richard_j__koubek.html), Richard J. (2010): *Understanding user preferences based on usability and aesthetics before and after actual use*. In [Interacting with Computers](https://www.interaction-design.org/references/periodicals/interacting_with_computers.html), 22 (6) pp. 530-543
[Lindgaard](https://www.interaction-design.org/references/authors/gitte_lindgaard.html), Gitte and [Dudek](https://www.interaction-design.org/references/authors/cathy_dudek.html), Cathy (2003): *What is this evasive beast we call user satisfaction?*. In [Interacting with Computers](https://www.interaction-design.org/references/periodicals/interacting_with_computers.html), 15 (3) pp. 429-452

[Lindgaard](https://www.interaction-design.org/references/authors/gitte_lindgaard.html), Gitte, [Dudek](https://www.interaction-design.org/references/authors/cathy_dudek.html), Cathy, [Sen](https://www.interaction-design.org/references/authors/devjani_sen.html), Devjani, [Sumegi](https://www.interaction-design.org/references/authors/livia_sumegi.html), Livia and [Noonan](https://www.interaction-design.org/references/authors/patrick_noonan.html), Patrick (2011): *An exploration of relations between visual appeal, trustworthiness and perceived usability of homepages*. In [ACM Transactions on Computer-Human Interaction (TOCHI)](https://www.interaction-design.org/references/periodicals/acm_transactions_on_computer-human_interaction_%28tochi%29.html), 18 (1)
[Lindgaard](https://www.interaction-design.org/references/authors/gitte_lindgaard.html), Gitte, [Fernandes](https://www.interaction-design.org/references/authors/gary_fernandes.html), Gary, [Dudek](https://www.interaction-design.org/references/authors/cathy_dudek.html), Cathy and [Brown](https://www.interaction-design.org/references/authors/j__brown.html), J. (2006): *Attention web designers: You have 50 milliseconds to make a good first impression*. In [Behaviour and Information Technology](https://www.interaction-design.org/references/periodicals/behaviour_and_information_technology.html), 25 (2) pp. 115-126

[Liu](https://www.interaction-design.org/references/authors/yili_liu.html), Yili (2003): *Engineering aesthetics and aesthetic ergonomics: theoretical foundations and a dual-process research methodology*. In [Ergonomics](https://www.interaction-design.org/references/periodicals/ergonomics.html), 46 (13) pp. 1273-1292
[Luchs](https://www.interaction-design.org/references/authors/michael_luchs.html), Michael and [Swan](https://www.interaction-design.org/references/authors/k__scott_swan.html), K. Scott (2011): *Perspective: The Emergence of Product Design as a Field of Marketing Inquiry*. In [Journal of Product Innovation Management](https://www.interaction-design.org/references/periodicals/journal_of_product_innovation_management.html), 28 (3) pp. 327-345
[Lyubomirsky](https://www.interaction-design.org/references/authors/sonja_lyubomirsky.html), Sonja, [King](https://www.interaction-design.org/references/authors/laura_king.html), Laura and [Diener](https://www.interaction-design.org/references/authors/ed_diener.html), Ed (2005): *The benefits of frequent positive affect: does happiness lead to success?*. In [Psychological Bulletin](https://www.interaction-design.org/references/periodicals/psychological_bulletin.html), 131 (6)

[Mandel](https://www.interaction-design.org/references/authors/naomi_mandel.html), Naomi and [Johnson](https://www.interaction-design.org/references/authors/e__j__johnson.html), E. J. (2002): *When Web Pages Influence Choice: Effects of Visual Primes on Experts and Novices*. In [Journal of Consumer Research](https://www.interaction-design.org/references/periodicals/journal_of_consumer_research.html), 29 (2) pp. 235-245
[Martindale](https://www.interaction-design.org/references/authors/colin_martindale.html), Colin, [Moore](https://www.interaction-design.org/references/authors/kathleen_moore.html), Kathleen and [Borkum](https://www.interaction-design.org/references/authors/jonathan_borkum.html), Jonathan (1990): *Aesthetic Preference: Anomalous Findings for Berlyne's Psychobiological Theory*. In [The American Journal of Psychology](https://www.interaction-design.org/references/periodicals/the_american_journal_of_psychology.html), 103 (1)
[Maslow](https://www.interaction-design.org/references/authors/abraham_h__maslow.html), Abraham H. (1954): *Motivation and Personality.* HarperCollins Publishers
[Maslow](https://www.interaction-design.org/references/authors/abraham_harold_maslow.html), Abraham Harold (1987): *Motivation and Personality.* HarperCollins Publishers

[Moshagen](https://www.interaction-design.org/references/authors/morten_moshagen.html), Morten and [Thielsch](https://www.interaction-design.org/references/authors/meinald_t__thielsch.html), Meinald T. (2010): *Facets of visual aesthetics*. In [International Journal of Human-Computer Studies](https://www.interaction-design.org/references/periodicals/international_journal_of_human-computer_studies.html), 68 (10) pp. 689-709
[Moshagen](https://www.interaction-design.org/references/authors/morten_moshagen.html), Morten, [Musch](https://www.interaction-design.org/references/authors/jochen_musch.html), Jochen and [Göritz](https://www.interaction-design.org/references/authors/anja_s_g%F6ritz.html), Anja S (2009): *A blessing, not a curse: experimental evidence for beneficial effects of visual aesthetics on performance*. In [Ergonomics](https://www.interaction-design.org/references/periodicals/ergonomics.html), 52 (10) pp. 1311-1320
[Nake](https://www.interaction-design.org/references/authors/frieder_nake.html), Frieder (2005): *Computer art: a personal recollection*. In [Proceedings of the 5th conference on Creativity cognition](https://www.interaction-design.org/references/periodicals/proceedings_of_the_5th_conference_on_creativity_cognition.html),
[Nasar](https://www.interaction-design.org/references/authors/jack_l__nasar.html), Jack L. (1997): *The Evaluative Image of the City.* Sage Publications, Inc

[Ngo](https://www.interaction-design.org/references/authors/david_chek_ling_ngo.html), David Chek Ling, [Teo](https://www.interaction-design.org/references/authors/lian_seng_teo.html), Lian Seng and [Byrne](https://www.interaction-design.org/references/authors/john_g__byrne.html), John G. (2003): *Modelling interface aesthetics*. In [Information Sciences](https://www.interaction-design.org/references/periodicals/information_sciences.html), 152 pp. 25-46
[Nielsen](https://www.interaction-design.org/references/authors/jakob_nielsen.html), Jakob (1993): *Usability Engineering.* Boston, MA, Morgan Kaufmann
[Norman](https://www.interaction-design.org/references/authors/donald_a__norman.html), Donald A. (1988): *The Psychology of Everyday Things.* New York, Basic Books
[Norman](https://www.interaction-design.org/references/authors/donald_a__norman.html), Donald A. (1998): *The
 Invisible Computer: Why Good Products Can Fail, the Personal Computer 
Is So Complex and Information Appliances Are the Solution.* MIT Press
[Norman](https://www.interaction-design.org/references/authors/donald_a__norman.html), Donald A. (2004): [*Emotional Design*](https://www.interaction-design.org/literature/topics/emotional-design)*: Why We Love (Or Hate) Everyday Things.* Basic Books

[Ortony](https://www.interaction-design.org/references/authors/andrew_ortony.html), Andrew, [Norman](https://www.interaction-design.org/references/authors/donald_a__norman.html), Donald A. and [Revelle](https://www.interaction-design.org/references/authors/william_revelle.html), William (2005): The role of affect and proto-affect in effective functioning. In: [Fellous](https://www.interaction-design.org/references/authors/jean-marc_fellous.html), Jean-Marc and [Arbib](https://www.interaction-design.org/references/authors/michael_a__arbib.html), Michael A. (eds.). "Who Needs Emotions?: The Brain Meets the Robot (Series in Affective Science)". Oxford University Press
[Pandir](https://www.interaction-design.org/references/authors/muzeyyen_pandir.html), Muzeyyen and [Knight](https://www.interaction-design.org/references/authors/john_knight.html), John (2006): *Homepage aesthetics: The search for preference factors and the challenges of subjectivity*. In [Interacting with Computers](https://www.interaction-design.org/references/periodicals/interacting_with_computers.html), 18 (6) pp. 1351-1370

[Park](https://www.interaction-design.org/references/authors/su-e_park.html), Su-e, [Choi](https://www.interaction-design.org/references/authors/dongsung_choi.html), Dongsung and [Kim](https://www.interaction-design.org/references/authors/jinwoo_kim.html), Jinwoo (2004): *Critical factors for the aesthetic fidelity of web pages: empirical studies with professional web designers and users*. In [Interacting with Computers](https://www.interaction-design.org/references/periodicals/interacting_with_computers.html), 16 (2) pp. 351-37
[Park](https://www.interaction-design.org/references/authors/su-e_park.html), Su-e, [Choi](https://www.interaction-design.org/references/authors/dongsung_choi.html), Dongsung and [Kim](https://www.interaction-design.org/references/authors/jinwoo_kim.html), Jinwoo (2005): *Visualizing E-Brand Personality: Exploratory Studies on Visual Attributes and E-Brand Personalities in Korea*. In [International Journal of Human-Computer Interaction](https://www.interaction-design.org/references/periodicals/international_journal_of_human-computer_interaction.html), 19 (1) pp. 7-34

[Parush](https://www.interaction-design.org/references/authors/avraham_parush.html), Avraham, [Nadir](https://www.interaction-design.org/references/authors/ronen_nadir.html), Ronen and [Shtub](https://www.interaction-design.org/references/authors/avraham_shtub.html), Avraham (1998): *Evaluating the Layout of Graphical User Interface Screens: Validation of a Numerical Computerized Model*. In [International Journal of Human-Computer Interaction](https://www.interaction-design.org/references/periodicals/international_journal_of_human-computer_interaction.html), 10 (4) pp. 343-360
[Porteous](https://www.interaction-design.org/references/authors/j__douglas_porteous.html), J. Douglas (1996): *Environmental Aesthetics: Ideas, Politics and Planning.* Routledge
[Postrel](https://www.interaction-design.org/references/authors/virginia_postrel.html), Virginia (2002): *The Substance of Style: How the Rise of Aesthetic Value Is Remaking Commerce, Culture, and Consciousness.* HarperCollins
[Postrel](https://www.interaction-design.org/references/authors/virginia_postrel.html), Virginia (2008). *The Art of Healing - Magazine - The Atlantic*. Retrieved 1 January 2011 from
[Postrel](https://www.interaction-design.org/references/authors/virginia_postrel.html), Virginia (2003): *The Substance of Style: How the Rise of Aesthetic Value Is Remaking Commerce, Culture, and Consciousness.* HarperCollins

[Quinn](https://www.interaction-design.org/references/authors/jeffrey_m__quinn.html), Jeffrey M. and [Tran](https://www.interaction-design.org/references/authors/tuan_q__tran.html),
 Tuan Q. (2010): Attractive phones don't have to work better: 
independent effects of attractiveness, effectiveness, and efficiency on 
perceived usability. In: [Proceedings of ACM CHI 2010 Conference on Human Factors in Computing Systems](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2010_conference_on_human_factors_in_computing_systems.html) 2010. pp. 353-362
[Rafaeli](https://www.interaction-design.org/references/authors/anat_rafaeli.html), Anat and [Vilnai-Yavetz](https://www.interaction-design.org/references/authors/iris_vilnai-yavetz.html), Iris (2004): *Emotion as a Connection of Physical Artifacts and Organizations*. In[Organization Science](https://www.interaction-design.org/references/periodicals/organization_science.html), 15 (6) pp. 671-686
[Ravina](https://www.interaction-design.org/references/authors/enrichetta_ravina.html), Enrichetta (2008). *Love & Loans: The Effect of Beauty and Personal Characteristics in Credit Markets*. Columbia Business School

[Reber](https://www.interaction-design.org/references/authors/rolf_reber.html), Rolf, [Schwarz](https://www.interaction-design.org/references/authors/norbert_schwarz.html), Norbert and [Winkielman](https://www.interaction-design.org/references/authors/piotr_winkielman.html), Piotr (2004): *Processing fluency and aesthetic pleasure: is beauty in the perceiver's processing experience?*. In [Personality and social psychology review an official journal of the Society for Personality and Social Psychology Inc](https://www.interaction-design.org/references/periodicals/personality_and_social_psychology_review_an_official_journal_of_the_society_for_personality_and_social_psychology_inc.html), 8 (4) pp. 364-382
[Reimann](https://www.interaction-design.org/references/authors/m__reimann.html), M., [Zaichkowsky](https://www.interaction-design.org/references/authors/j__zaichkowsky.html), J., [Neuhaus](https://www.interaction-design.org/references/authors/c__neuhaus.html), C., [Bender](https://www.interaction-design.org/references/authors/t__bender.html), T. and [Weber](https://www.interaction-design.org/references/authors/b__weber.html), B. (2010): *Aesthetic package design: A behavioral, neural, and psychological investigation*. In [Journal of Consumer Psychology](https://www.interaction-design.org/references/periodicals/journal_of_consumer_psychology.html), 20 (4) pp. 431-441

[Rhodes](https://www.interaction-design.org/references/authors/gillian_rhodes.html), Gillian (2006): *The evolutionary psychology of facial beauty*. In [Annual Review of Psychology](https://www.interaction-design.org/references/periodicals/annual_review_of_psychology.html), 57 (1) pp. 199-226
[Santayana](https://www.interaction-design.org/references/authors/george_santayana.html), George (1955): *The Sense of Beauty: Being the Outline of Aesthetic Theory.* Dover Publications
[Sauer](https://www.interaction-design.org/references/authors/juergen_sauer.html), Juergen and [Sonderegger](https://www.interaction-design.org/references/authors/andreas_sonderegger.html), Andreas (2009): *The
 influence of prototype fidelity and aesthetics of design in usability 
tests: effects on user behaviour, subjective evaluation and emotion*. In [Applied Ergonomics](https://www.interaction-design.org/references/periodicals/applied_ergonomics.html), 40 (4)
[Schaik](https://www.interaction-design.org/references/authors/paul_van_schaik.html), Paul Van and [Ling](https://www.interaction-design.org/references/authors/jonathan_ling.html), Jonathan (2009): *The role of context in perceptions of the aesthetics of web pages over time*. In [International Journal of Human-Computer Studies](https://www.interaction-design.org/references/periodicals/international_journal_of_human-computer_studies.html), 67 (1) pp. 79-89

[Schaik](https://www.interaction-design.org/references/authors/paul_van_schaik.html), Paul Van and [Ling](https://www.interaction-design.org/references/authors/jonathan_ling.html), Jonathan (2011): *An integrated model of interaction experience for information retrieval in a Web-based encyclopaedia*. In [Interacting with Computers](https://www.interaction-design.org/references/periodicals/interacting_with_computers.html), 23 (1) pp. 18-32
[Schenkman](https://www.interaction-design.org/references/authors/bo_n__schenkman.html), Bo N. and [Jonsson](https://www.interaction-design.org/references/authors/fredrik_u__jonsson.html), Fredrik U. (2000): *Aesthetics and preferences of web pages*. In [Behaviour & Information Technology](https://www.interaction-design.org/references/periodicals/behaviour_%26_information_technology.html), 19 (5) pp. 367-377
[Seligman](https://www.interaction-design.org/references/authors/martin_e__p__seligman.html), Martin E. P. and [Csikszentmihalyi](https://www.interaction-design.org/references/authors/mihaly_csikszentmihalyi.html), Mihaly (2000): *Positive Psychology: An Introduction. [Article]*. In[American Psychologist](https://www.interaction-design.org/references/periodicals/american_psychologist.html), 55 (1) pp. 5-14

[Shaked](https://www.interaction-design.org/references/authors/gilboa%2C_shaked.html), Gilboa, and [Rafael](https://www.interaction-design.org/references/authors/anat_rafael.html), Anat (2003): *Store environment, emotions and approach behaviour: applying environmental aesthetics to retailing*. In [The International Review of Retail, Distribution and Consumer Research](https://www.interaction-design.org/references/periodicals/the_international_review_of_retail%2C_distribution_and_consumer_research.html), 13 (2) pp. 195-211
[Simonson](https://www.interaction-design.org/references/authors/alex_simonson.html), Alex and [Schmitt](https://www.interaction-design.org/references/authors/bernd_h__schmitt.html), Bernd H. (1997): *Marketing Aesthetics: The Strategic Management of Brands, Identity and Image.* Free Press
[Sonderegger](https://www.interaction-design.org/references/authors/andreas_sonderegger.html), Andreas and [Sauer](https://www.interaction-design.org/references/authors/juergen_sauer.html), Juergen (2010): *The influence of design aesthetics in *[*usability testing*](https://www.interaction-design.org/literature/topics/usability-testing)*: effects on user performance and perceived usability*. In [Applied Ergonomics](https://www.interaction-design.org/references/periodicals/applied_ergonomics.html), 41 (3) pp. 403-410

[Sun](https://www.interaction-design.org/references/authors/heshan_sun.html), Heshan and [Zhang](https://www.interaction-design.org/references/authors/ping_zhang.html), Ping (2006): The role of affect in Information systems research. In: [Zhang](https://www.interaction-design.org/references/authors/ping_zhang.html), Ping and[Galletta](https://www.interaction-design.org/references/authors/dennis_galletta.html),
 Dennis (eds.). "Human-Computer Interaction and Management Information 
Systems: Foundations (Advances in Management Information Systems)". M.E.
 Sharpe
[Sutcliffe](https://www.interaction-design.org/references/authors/aiistair_sutcliffe.html), Aiistair (2009): *Designing for User Engagement: Aesthetic and Attractive User Interfaces*. In [Synthesis Lectures on HumanCentered Informatics](https://www.interaction-design.org/references/periodicals/synthesis_lectures_on_humancentered_informatics.html), 2 (1) pp. 1-55
[Sutcliffe](https://www.interaction-design.org/references/authors/alistair_g__sutcliffe.html), Alistair G. (2002): Assessing the Reliability of [Heuristic Evaluation](https://www.interaction-design.org/literature/topics/heuristic-evaluation) for Website Attractiveness and Usability. In: [HICSS 2002](https://www.interaction-design.org/references/conferences/hicss_2002.html) 2002. p. 137

The Chromium Blog (2009). *WebP, a new image format for the Web*. Retrieved 1 December 2011 from The Chromium Blog: [http://blog.chromium.org/2010/09/webp-new-image-fo...](http://blog.chromium.org/2010/09/webp-new-image-format-for-web.html)
[Thuring](https://www.interaction-design.org/references/authors/manfred_thuring.html), Manfred and [Mahlke](https://www.interaction-design.org/references/authors/sascha_mahlke.html), Sascha (2007): *Usability, aesthetics and emotions in human-technology interaction*. In [International Journal of Psychology](https://www.interaction-design.org/references/periodicals/international_journal_of_psychology.html), 42 (4) pp. 253-264
[Townsend](https://www.interaction-design.org/references/authors/claudia_townsend.html), Claudia and [Shu](https://www.interaction-design.org/references/authors/suzanne_b__shu.html), Suzanne B. (2010): *When and how aesthetics influences financial decisions*. In [Journal of Consumer Psychology](https://www.interaction-design.org/references/periodicals/journal_of_consumer_psychology.html), 20 (4) pp. 452-458

[Tractinsky](https://www.interaction-design.org/references/authors/noam_tractinsky.html), Noam (1997): Aesthetics and apparent usability: empirically assessing cultural and methodological issues. In: [Proceedings of the SIGCHI conference on Human factors in computing systems](https://www.interaction-design.org/references/conferences/proceedings_of_the_sigchi_conference_on_human_factors_in_computing_systems.html) 1997. pp. 115-122
[Tractinsky](https://www.interaction-design.org/references/authors/noam_tractinsky.html), Noam (2004): Toward the study of aesthetics in information technology. In: [Proceedings of the 25th International Conference on Information Systems](https://www.interaction-design.org/references/conferences/proceedings_of_the_25th_international_conference_on_information_systems.html) December 12-15, 2004, Washington, DC, USA. pp. 771-780
[Tractinsky](https://www.interaction-design.org/references/authors/noam_tractinsky.html), Noam (2006): Aesthetics in Information Technology: Motivation and Future Research Directions. In:[Zhang](https://www.interaction-design.org/references/authors/ping_zhang.html), Ping and [Galletta](https://www.interaction-design.org/references/authors/dennis_galletta.html),
 Dennis (eds.). "Human-Computer Interaction and Management Information 
Systems: Foundations (Advances in Management Information Systems)". M.E.
 Sharpe

[Tractinsky](https://www.interaction-design.org/references/authors/noam_tractinsky.html), Noam and [Hassenzahl](https://www.interaction-design.org/references/authors/marc_hassenzahl.html), Marc (2005): *Arguing for Aesthetics in Human-Computer Interaction*. In [i-com Zeitschrift für interaktive und kooperative Medien](https://www.interaction-design.org/references/periodicals/i-com_zeitschrift_f%FCr_interaktive_und_kooperative_medien.html), 4 (3) p. 66–68
[Tractinsky](https://www.interaction-design.org/references/authors/noam_tractinsky.html), Noam and [Meyer](https://www.interaction-design.org/references/authors/joachim_meyer.html), Joachim (1999): *Junkchart or Goldgraph? Effects of Presentation Objectives and Content *[*Desirability*](https://www.interaction-design.org/literature/topics/desirability)* on Information Presentation*. In [MIS Quarterly](https://www.interaction-design.org/references/periodicals/mis_quarterly.html), 23 pp. 397-420
[Tractinsky](https://www.interaction-design.org/references/authors/noam_tractinsky.html), Noam and [Zmiri](https://www.interaction-design.org/references/authors/dror_zmiri.html), Dror (2006): Exploring Attributes of Skins as Potential Antecedents of Emotion in HCI. In: [Fishwick](https://www.interaction-design.org/references/authors/paul_a__fishwick.html), Paul A. (ed.). "Aesthetic Computing". The MIT Press

[Tractinsky](https://www.interaction-design.org/references/authors/noam_tractinsky.html), Noam, [Katz](https://www.interaction-design.org/references/authors/a__s__katz.html), A. S. and [Ikar](https://www.interaction-design.org/references/authors/d__ikar.html), D. (2000): *What is Beautiful is Usable*. In [Interacting with Computers](https://www.interaction-design.org/references/periodicals/interacting_with_computers.html), 13 (2) pp. 127-145
[Tractinsky](https://www.interaction-design.org/references/authors/noam_tractinsky.html), Noam, [Inbar](https://www.interaction-design.org/references/authors/ohad_inbar.html), Ohad, [Tsimhoni](https://www.interaction-design.org/references/authors/omer_tsimhoni.html), Omer and [Seder](https://www.interaction-design.org/references/authors/thomas_seder.html), Thomas (2011): Slow down, you move too fast: Examining animation aesthetics to promote eco-driving. In: [3rd International Conference on Automotive User Interfaces and Interactive Vehicular Applications AutomotiveUI 2011](https://www.interaction-design.org/references/conferences/3rd_international_conference_on_automotive_user_interfaces_and_interactive_vehicular_applications_automotiveui_2011.html) November 30th-December 2nd, 2011, Salzburg, Austria.

[Tractinsky](https://www.interaction-design.org/references/authors/noam_tractinsky.html), Noam, [Cokhavi](https://www.interaction-design.org/references/authors/avivit_cokhavi.html), Avivit, [Kirschenbaum](https://www.interaction-design.org/references/authors/moti_kirschenbaum.html), Moti and [Sharfi](https://www.interaction-design.org/references/authors/tal_sharfi.html), Tal (2006): *Evaluating the consistency of immediate aesthetic perceptions of web pages*. In [International Journal of Human-Computer Studies](https://www.interaction-design.org/references/periodicals/international_journal_of_human-computer_studies.html), 64 (11) pp. 1071-1083
[Tractinsky](https://www.interaction-design.org/references/authors/noam_tractinsky.html), Noam, [Abdu](https://www.interaction-design.org/references/authors/rotem_abdu.html), Rotem, [Forlizzi](https://www.interaction-design.org/references/authors/jodi_forlizzi.html), Jodi and [Seder](https://www.interaction-design.org/references/authors/thomas_seder.html), Thomas (2011a): *Towards personalisation of the driver environment: investigating responses to instrument cluster design*. In [International Journal of Vehicle Design](https://www.interaction-design.org/references/periodicals/international_journal_of_vehicle_design.html), 55 (2) pp. 208-236
[Tufte](https://www.interaction-design.org/references/authors/edward_r__tufte.html), Edward R. (1992): *The Visual Display of Quantitative Information.* Graphics Press

[Turkle](https://www.interaction-design.org/references/authors/sherry_turkle.html), Sherry (2005): *The Second Self: Computers and the Human Spirit - Twentieth Anniversary Edition.* The MIT Press
[Udsen](https://www.interaction-design.org/references/authors/lars_erik_udsen.html), Lars Erik and [Jørgensen](https://www.interaction-design.org/references/authors/anker_helms_j%F8rgensen.html), Anker Helms (2005): *The aesthetic turn: unravelling recent aesthetic approaches to human-computer interaction*. In [Digital Creativity](https://www.interaction-design.org/references/periodicals/digital_creativity.html), 16 (4) pp. 205-216
[Ulrich](https://www.interaction-design.org/references/authors/r__s__ulrich.html), R. S. (1984): *View through a window may influence recovery from surgery*. In [Science](https://www.interaction-design.org/references/periodicals/science.html), 224 (4647) pp. 420-421
[Venkatesh](https://www.interaction-design.org/references/authors/alladi_venkatesh.html), Alladi and [Meamber](https://www.interaction-design.org/references/authors/laurie_meamber.html), Laurie (2008): *The aesthetics of consumption and the consumer as an aesthetic subject*. In [Consumption Markets Culture](https://www.interaction-design.org/references/periodicals/consumption_markets_culture.html), 11 (1) pp. 45-70

[Veryzer](https://www.interaction-design.org/references/authors/robert%A0w__veryzer.html), Robert W. and [Hutchinson](https://www.interaction-design.org/references/authors/j_wesley_hutchinson.html), J Wesley (1998): *The Influence of Unity and Prototypicality on Aesthetic Responses to New Product Designs*. In [Journal of Consumer Research](https://www.interaction-design.org/references/periodicals/journal_of_consumer_research.html), 24 (4) pp. 374-385
[Visser](https://www.interaction-design.org/references/authors/willemien_visser.html), Willemien (2009): *Design: one, but in different forms*. In [Design Studies](https://www.interaction-design.org/references/periodicals/design_studies.html), 30 (3) pp. 187-223
[Ware](https://www.interaction-design.org/references/authors/colin_ware.html), Colin (2008): *Visual Thinking: for Design.* Morgan Kaufmann
[Whyte](https://www.interaction-design.org/references/authors/jennifer_whyte.html), Jennifer, [Gann](https://www.interaction-design.org/references/authors/d__gann.html), D. and [Salter](https://www.interaction-design.org/references/authors/a__salter.html), A. (2003): *Design quality indicator as a tool for thinking*. In [Building Research Information](https://www.interaction-design.org/references/periodicals/building_research_information.html), 31 (5) pp. 318-333

[Winkielman](https://www.interaction-design.org/references/authors/piotr_winkielman.html), Piotr, [Halberstadt](https://www.interaction-design.org/references/authors/jamin_halberstadt.html), Jamin, [Fazendeiro](https://www.interaction-design.org/references/authors/tedra_fazendeiro.html), Tedra and [Catty](https://www.interaction-design.org/references/authors/steve_catty.html), Steve (2006): *Prototypes are attractive because they are easy on the mind*. In [Psychological Science](https://www.interaction-design.org/references/periodicals/psychological_science.html), 17 (9) pp. 799-806
[Winograd](https://www.interaction-design.org/references/authors/terry_winograd.html), Terry (1996): *Bringing Design to Software.* ACM Press
**Chapter TOC**
[**The Practical Guide to Usability**](https://www.interaction-design.org/courses/the-practical-guide-to-usability)
![](https://public-media.interaction-design.org/images/courses/hds/course_15--square_thumbnail.jpg?tr=fo-auto)
The Practical Guide to Usability
Closes in
7
days
booked
View Course

## 获取每周用户体验（User Experience, UX）洞察

加入 **314,524 位设计师** 的行列，通过我们的时事通讯（Newsletter）获取实用的 UX 技巧。
需要提供有效的电子邮件地址。

# 19.5 Jeffrey Bardzell 的评论

**“**数学魔术师（The Mathemagician）：“如果没有两个人，就不能喝‘双人茶’，对吧？”
Azaz 国王：“如果没有茶，就不能喝‘双人茶’，对吧？”**”**
- - *The Phantom Tollbooth*

我这篇评论的论点是，Noam Tractinsky 关于视觉美学（Visual Aesthetics）的章节仅反映并支持了影响人机交互（Human-Computer Interaction, HCI）的一部分美学研究，他（希望是无意地）边缘化了其他替代方法，因此有必要提供一个更平衡的视角。为了论证这一观点，我的评论将开展以下工作：

- 通过细读（close reading）证明 Tractinsky 的章节提供了一种美学哲学理论，同时为了避免深入探讨美学理论，他在修辞策略（rhetorical strategy）上否认了这一点
- 提出三个支持在交互设计（interaction design）中引入视觉美学的论据
- 根据这三个论据，批判性地评估 Tractinsky 的（我将其称为）“面向 HCI 的美学处理理论（aesthetic processing theory for HCI）”
- 探讨来自人文科学（humanities）的竞争性美学理论
- 介绍利用这些竞争性理论的 HCI 研究与设计，并根据上述三个论据对其进行评估
- 主张如果交互设计社区希望解决所有三个支持视觉美学与交互设计的论据，那么我们需要一个比 Tractinsky 所提供的更平衡、更全面的视角

我将对 Tractinsky 的文章提出最实质性的批评，即

我的观点是，他对于一般美学，尤其是人机交互（Human-Computer Interaction, HCI）中视觉美学的阐述极其有限，而非他所承诺的那样全面，并且排除了主要的美学思想以及对交互设计（Interaction Design）的主要美学贡献。因此，在我看来，这种边缘化对他所谓的课题——HCI 中的视觉美学——提供了一种扭曲的描述，并可能导致读者错过一个我们*所有*人都共同追求的目标：让交互变得更具美感。

虽然我的评论对 Tractinsky 的文章采取了批判性立场，但我首先想强调，Tractinsky 的研究以及其传统领域内其他人的工作（包括本章几乎所有共同评论者）多年来在 HCI 领域产生了巨大的积极影响；我自己也在教学和使用这些成果；而且我大致同意 Tractinsky 对此类研究未来的建议（Prescriptions）。我的目的并非攻击一个显然严谨、有用且具有影响力的研究方法，而是对其定位和局限性进行批判，并探索能够补充和增强（而非取代）其在 HCI 中地位的替代性表述（Alternative Formulations）。

归根结底，如果我们能帮助设计师创造出更具美感的交互，我们才算成功，而不是赢得学术地盘之争（Academic Turf Wars）。

## 19.5.1 一种反理论的理论及其后果

Tractinsky 在其章节的开头，通过分别定义“视觉（visual）”和“美学（aesthetics）”，界定了他对“视觉美学（visual aesthetics）”的操作性理解（operational understanding）及其范围：

**“**我对‘美学’一词的使用是基于其相当普通且通俗的含义，正如词典定义中所反映的那样，例如‘具有艺术美感或令人愉悦的外观’（The American Heritage Dictionary of the English Language），或者‘令人愉悦的外观或效果：美’（Merriam-Webster’s Collegiate Dictionary）。‘视觉’一词则表示专注于视觉感官，这是人类的核心感官，占据了‘几乎一半的大脑’（Ware, 2008, ix）。因此，本章并不涉及在‘美学’标题下研究的其他各种现象，例如文学美学、审美体验或标准的抽象形式……或者对那些并非直接且主要源于物体视觉属性的物体特性的反应。**”**
- - 第 19.1 节

通过使用两个标准的词典定义，并撇开“在‘美学’标题下研究的其他各种现象”，Tractinsky 明确地脱离了哲学、艺术史、文学、建筑和电影领域数千年的美学思考。然而，通过在对视觉的定义中引用脑科学，他表明了自己愿意参与到科学学术研究（scientific scholarship）之中。因此，Tractinsky

他已经表明了自己的意图——并且将在整篇文章中贯彻这一意图——即在对待美学的经验科学（empirical science of aesthetics）时保持学术严谨，而在对待美学哲学（philosophy of aesthetics）时则在策略上采取非学术的态度。后者并非我的指责，而是他对自己描述的方式：

**“**
虽然科学界可能难以定义“美学（aesthetics）”或“美（beauty）”这些概念——这或许是因为处理这些概念且赋予其不同含义的学科众多——但根据我的经验，普通人对这些术语的直觉解读与上述词典定义 [sic] 非常接近，而这正是指导人机交互（Human-Computer Interaction, HCI）中视觉美研究的依据。
**”**
- - 第 19.3.1 节

这里提出了一个强有力的主张，即跨学科定义美学的尝试令科学界感到困惑，而前进的方向则看似简单：将 HCI 中的美学研究基于他所谓的“普通人对这些术语的直觉解读”（这些解读反映在词典定义中），并忽略所有那些多学科的纠结（multidisciplinary handwringing）。在此基础上，研究就变成了“主要是经验性的且……具有典型的描述性（即‘什么

“被认为是‘美的’”，而不是规范性的（Normative，即，什么*应该*被认为是‘美的’）”第 19.1 节。在这里，Tractinsky 再次将自己和其他研究者置于美学争论的*之外*：他的工作仅仅是*发现*世界上已经存在的东西，而不是在美学争论中采取立场（如果采取立场，他就会处于争论之中）。

因此，Tractinsky 对美学的“日常语言（Ordinary language）”定义能否成功，取决于他所呈现的美学观点是否合理地反映了人们对美学的日常看法。如果确实如此，那么他对他数千年人文主义学术研究（Humanist scholarship）的断然拒绝就显得合理，因为这些研究似乎无法为他的研究项目提供任何有用的东西，甚至可能通过多种且令人困惑的技术定义而对其产生不利影响。此外，如果他确实坚持美学的日常定义，那么他就可以理直气壮地主张自己处于美学争论之外，仅仅是在发现既有的事实（这就是他所说的“描述性（Descriptive）”而非“规范性（Normative）”的含义）。

但如果事实证明 Tractinsky 的工作*并非*基于对美学的日常看法，那么他就为自己制造了两个问题：首先，他容易受到其方法缺乏学术严谨性（Scholarly rigor）的批评，因为他似乎只是在面对大多数人认为的概念困难时选择了退缩。

……是审美推理（aesthetic reasoning）所固有的；其次，他失去了声称自己仅仅是描述性的（descriptive）而非规范性的（normative）这一权利，因此，他所提出的审美科学实际上变成了另一种候选的审美哲学观点，从而使其受到他最初试图通过避免理论来规避的那类哲学批判。

我认为，显而易见的是，Tractinsky 在文中赞同并引用的审美概念，既不符合他所引用的那些简短且近乎空洞的词典定义，他所推崇的审美观点也未能反映普通人所持有的常见的、非学术的、直觉性的审美看法。因此，我认为，“指导人机交互（Human-Computer Interaction, HCI）中视觉美研究”的并非大多数人直觉上共享的简单想法，而是一个复杂、专业且具有强学术性的理论；该理论不可避免地具有规范性维度（顺便提一句，我很难理解为什么任何具有“设计启示”的东西在本质上不是规范性的），因此需要经过批判性审视（critical scrutiny）才能被理性地使用。简而言之，我认为 Tractinsky 引入了一种披着所谓描述性经验科学外衣的审美教条（aesthetic dogma）；作为一个领域，我们需要将两者区分开来，以免在倒掉洗澡水时把孩子也一起倒掉（throw out the baby with the bathwater）。

## 19.5.2 Tractinsky 对美学的非寻常语言定义（Extra-ordinary language definition of aesthetics）

在本文中，Tractinsky 赞同地引用了一系列多样化的（且毫不掩饰其学术性的）美学概念。任何人很难声称这些概念属于他所谓的“普通人对这些术语的直觉解释”，而且在大学词典的“美学（aesthetics）”条目下肯定找不到这些内容。这些概念包括：

- 建筑学的三大维特鲁威原则（Vitruvian principles）——*firmitas*（坚固性）、*utilitas*（实用性）和 *venustas*（美观性）——被提出作为一种阐述设计价值不同维度的古老手段，从而建立了一种对设计价值的分析性理解，其包含强度、耐用性与结构；实用性与适用性；以及美感之间的结构关系（第 19.1.2.1 节）。
- 格式塔知觉心理学（Gestalt psychology of perception）被用来解释为什么可用性（usability）与美感（beauty）是和谐的，而非冲突的价值（第 19.1.2.2 节）。
- Tractinsky 自身极具影响力的“经典（classical）”与“表现（expressive）”美学维度的区分，被作为进一步探索可用性与美感之间关系的手段（第 19.1.2.2 节）。
- 文中还提出了众多心理学对美学的理解（此处无法详尽列举），包括“视觉美学的价值”源于“愉悦感与福祉（pleasure and wellbeing）”、“人类的基本需求”以及“或许……进化过程（evolutionary processes）”（第 19.1.3.1 节），以及“美学体验（aesthetic experience）”是“情感反应（affective responses）与...

- “反思性思维（reflective thought）”（第 19.1.3.1 节），审美与自我心理学（psychology of the self）有关（第 19.1.3.2 节），且“审美刺激（aesthetic stimuli）”会产生“极快”的“审美印象（aesthetic impressions）”（第 19.1.3.3 节），最重要的是，审美可以用信息处理隐喻（information processing metaphor）来建模（第 19.2 节）。
- 设计领域对审美的理解（Design understandings of aesthetics）被总结为：尊重受众、对需求和欲望保持敏感，以及投入精力和细心进行设计（第 19.1.4.3 节）。
- Norman 将“审美感知与评估（aesthetic perceptions and evaluations）”划分为“本能（visceral）、行为（behavioral）、反思（reflective）”……“处理层级（levels of processing）”，这一观点被多次总结并推崇（例如第 19.2.2 节）。

此处没有空间去评估这些不同的概念（每个概念都带来了洞见与困难），而 Tractinsky 将其概述为在心理学、设计以及近期的 HCI（人机交互）领域中被探讨的具有影响力的重要审美观点，这无疑是合理的。但在采纳所有这些观点时，Tractinsky 为一种学术性的审美理论构建了一个哲学基础架构（philosophical infrastructure），并脱离了对审美的常识性或词典定义上的概念（commonsense or dictionary notion）。我认为我可以合理地断言，上述列表中的任何观点都不是“普通人对这些术语的直觉解释（intuitive interpretation）”的一部分，*并且* 我也可以合理地断言，所有这些观点都是 Tractinsky 研究项目的基石。

因此，他的反理论立场是无效的：他为自己构建了一套由一系列技术性且环环相扣的观点组成的理论装置（theoretical apparatus），而他并没有像他声称的那样，仅仅依赖于简单的词典定义。

正是在这一装置的基础上，Tractinsky 在 19.2 节中提出了一种特定的审美学术理论，并在其中概述了一个他称之为“审美过程（the aesthetic process）”的流模型（flow model）。根据该模型，*设计变量（design variables）*（包括诸如颜色使用和对称性等“低层”属性，以及新颖性、典型性和流畅性等“高层”属性）会导致（或引起？）*审美评价（aesthetic valuations）*（遵循 Norman 的分类，如本能的、行为的和反思的评价），而审美评价反过来又会导致（或引起？）*结果（outcomes）*（如情感与情绪、品牌信任、感知可用性、感知产品特性）。这些关系中的每一项都受到所使用的系统类型、文化输入、领域、任务类型以及审美趣味的*调节（modified）*。在这个模型中，Tractinsky 将**传统审美类别（traditional aesthetic categories）**（例如对称性、形式、构图、典型性与新颖性的平衡、多样性、工艺、表现力）与**实验心理学的语言（the language of experimental psychology）**（例如信息处理隐喻、变量、调节变量、输入/输出、绩效、动机）交织在一起。

这是一个非常复杂的理论，此时我想重新审视 Tractinsky 的基础主张：

1. 这两个词典定义（两者都断言美即是令人愉悦之物）*准确地反映了* 普通人对美学（Aesthetics）的直觉理解，而这些理解正是“指导 HCI 中视觉美研究”的内容。
1. 因此：
  1. 为了开展这项研究，不需要除词典定义之外的任何关于美的学术理论；且
  2. HCI 的视觉美学实证科学（Empirical science）是描述性的（Descriptive）而非规范性的（Normative），因为它避开了多学科的美学争论。

但仅仅是对 Tractinsky 的总结就表明，他在此提供的远不止于词典定义，而是构成了一种*美学的信息处理理论（Information processing theory of aesthetics）*。在这种理论中，设计输入（Design inputs）产生评估输出（Evaluation outputs），而评估输出又成为结果输出（Outcomes outputs）的输入。根据该理论，这一过程本身具有“调节变量（Moderators）”，包括使用情境（Use context）、系统属性（System attributes）、文化和个体差异等输入。这比他的词典定义（“美：令人愉悦的外观或效果”）要具体得多，且更具指导意义；而后者这个短语模糊到了毫无意义的程度，显然不足以指导 HCI 中美学的实证研究！

我认为，我已经证明了尽管 Tractinsky 声称如此，但他在实际操作中采用的美学哲学远比词典定义要复杂得多，但我尚未评论他的理论如何

这与普通人的直觉理解相关。但我认为，一些简单的反思也能让我们意识到这种自以为是的想法是错误的。例如，我在信息与计算学院（School of Informatics and Computing）为 HCI（人机交互）专业的学生教授一门名为《交互文化》（*Interaction Culture*）的课程。在该课程第一节课的开场几分钟里，在我自我介绍或分发教学大纲之前，我会播放一部获得了一定大众成功的艺术电影的前几分钟。今年，我播放了 1998 年德国动作电影《奔跑吧，萝拉》（*Run Lola Run*）的前 5 到 6 分钟，这部电影具有哲学潜台词（philosophical subtext）。电影的开篇包含了 3D 计算机图形学（3D computer graphics）、2D 卡通动画（2D cartoon animation）、2.5D 后期合成（2.5 post-production compositing，例如标题）、实拍表演（live motion acting）、强烈的图像处理（heavy image manipulation）以及强烈的 Techno 节奏；除了这种令人眼花缭乱的视觉冲击外，还有一段简短但带有神秘哲学意味的对白，其与图像之间的关系并不明显。在播放完这段开场后，我要求学生们简单地大声讨论他们对此的反应。有些人描述*他们的感受*——兴奋、焦虑、好奇。另一些人则讨论*将该作品视为一种人工制品（artifact）的符号*——例如时钟意象的频繁使用以及 Techno 音乐中像节拍器一样的节奏……

……原声带相互增强。另一些人则就*导演可能意图表达*什么、试图传达或执行什么，以及这如何契合德国电影传统等提出建议。还有一些人讨论*电影拍摄时的背景*（如 20 世纪 90 年代的德国或一般的流行文化）。这些难道不是普通、常见且直觉性的审美反应（aesthetic reactions）吗？这种解释策略（interpretative strategies）——而非审美处理理论（aesthetic processing theory）——是在我们孩童时期的学校和家庭中被教授的，并在我们成年后几乎自然而然地产生。我的感觉是，如果一个人真的想理解普通人直觉上是如何操作的，那么只需要观察普通人直觉地接触美的事物即可。Tractinsky 在其研究中远不止于此，且这样做是正确的，但如果声称他既不需要也不使用任何严谨的学术审美理论（academic theory of aesthetics），则是不诚实的。

![](https://www.interaction-design.org/images/encyclopedia/visual_aesthetics/lola_rennt_aesthetic_1.jpg)

版权所有 © Sony Pictures Classics。保留所有权利。根据合理使用原则（Fair Use Doctrine）在未经许可的情况下使用（因为无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/visual-aesthetics#copyrightNotice) 页面上的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

![](https://www.interaction-design.org/images/encyclopedia/visual_aesthetics/lola_rennt_aesthetic_2.jpg)
版权所有 © Sony Pictures Classics。保留所有权利。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用（因无法获得许可）。请参阅 [版权声明（copyright notice）](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/visual-aesthetics#copyrightNotice) 页面中的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

![](https://www.interaction-design.org/images/encyclopedia/visual_aesthetics/lola_rennt_aesthetic_3.jpg)
版权所有 © Sony Pictures Classics。保留所有权利。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用（因无法获得许可）。请参阅 [版权声明（copyright notice）](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/visual-aesthetics#copyrightNotice) 页面中的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

![](https://www.interaction-design.org/images/encyclopedia/visual_aesthetics/lola_rennt_aesthetic_4.jpg)
版权所有 © Sony Pictures Classics。保留所有权利。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用（因无法获得许可）。请参阅“例外（Exceptions）”部分（以及

subsection "allRightsReserved-UsedWithoutPermission") on the page [copyright notice](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/visual-aesthetics#copyrightNotice).
![](https://www.interaction-design.org/images/encyclopedia/visual_aesthetics/lola_rennt_aesthetic_5.jpg)
版权所有 © Sony Pictures Classics。保留所有权利。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用（因无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/visual-aesthetics#copyrightNotice) 页面上的“Exceptions”（例外情况）章节（以及“allRightsReserved-UsedWithoutPermission”子章节）。
![](https://www.interaction-design.org/images/encyclopedia/visual_aesthetics/lola_rennt_aesthetic_6.jpg)
版权所有 © Sony Pictures Classics。保留所有权利。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用（因无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/visual-aesthetics#copyrightNotice) 页面上的“Exceptions”（例外情况）章节（以及“allRightsReserved-UsedWithoutPermission”子章节）。
图 19.1：《Run Lola Run》片尾名单中的一段序列

因此，Tractinsky 的审美处理理论（aesthetic processing theory）并非直觉性的或普遍的。它也不是一个在现实世界中被经验性地发现的事实。因此，该理论是一种*美学哲学理论（philosophical theory of aesthetics）*，或者用逻辑实证主义（logical positivism，我个人并不认同，但不确定 Tractinsky 是否认同）的语言来说，是一种*教条（dogma）*。

审美处理是一种关于审美响应（aesthetic response）的理论，它构建于信息处理心理学（information processing psychology）的方法论和概念体系之上，并采用了来自科学和艺术领域的美学词汇。例如，Tractinsky 对“古典”美学（classical aesthetics）与“表现”美学（expressive aesthetics）所做的具有开创性的区分，均源自艺术史和艺术哲学；前者可归功于 Hutcheson、Bell 和 Beardsley 等哲学家，而后者则可归功于 Langer 和 Collingwood 等哲学家。（这两个概念在过去一个多世纪中都得到了*发展*和*批判*，且各自在概念上的困难在分析艺术哲学家（analytic philosophers of art）中已是众所周知，即便在 HCI 社区中并非如此。）

## 19.5.3 审美处理理论及其不足

到目前为止，我的论点在很大程度上是哲学性的，旨在表明 Tractinsky 构建其审美处理理论（Aesthetic Processing Theory）的概念体系（Conceptual Edifice）存在缺陷，因为它声称自己是非理论的（a-theoretical），但显然并非如此。

然而，这一切的真正目的则更具实践意义：我想证明，Tractinsky 的视觉审美哲学中内置的理论盲点（Theoretical Blindness）对人机交互（Human-Computer Interaction, HCI）产生了需要解决的重要影响。其中两点如下：

- 非理论的立场使自己免于批判性审查（Critical Scrutiny），因为它否认自身理论构建性（Theoretical Constructedness）和规范性承诺（Normative Commitments）的存在，而将自己天真地呈现为纯粹的经验数据（Empirical Data）；该立场暗示，此类数据可以通过科学手段而非哲学手段进行审视。
- 非理论的立场被用来边缘化 Tractinsky 的竞争对手——基本上是任何具有人文主义（Humanist）或公开的理论审美倾向并试图为 HCI 做出贡献的人；值得注意的是，尽管其中一些研究在领域内具有极大的影响力，但所有此类研究在 Tractinsky 的论文（以及其他评论者的论文）中几乎被完全忽略了。

在这两点中，第二点是一个更严重的缺陷，尤其是考虑到 Tractinsky 声称“本文的目标是综述 HCI 领域中的视觉审美”，而事实上它综述的是

仅涵盖了该领域中一小部分被偏好的子集（favored subset）。在下文中，我将探讨这两项实践后果（practical consequences）。

## 19.5.4 我们希望在 HCI 中从视觉美学（Visual Aesthetics）中获得什么？

科学研究成本高昂，无论以何种方式，最终都由公众买单，因此任何科学议程都应提供某种形式的公共利益（Public Good）。人机交互（HCI）中美学研究的社会价值是什么？让我们效仿 Tractinsky 的做法，从词典定义开始：

**“**
一种具有艺术美感或令人愉悦的外观” (The American Heritage Dictionary of the English Language)，或者被定义为“一种令人愉悦的外观或效果：美（Beauty）
**”**

这些定义并没有太大的帮助。我能想象到从中获得的唯一公共利益，就是这项研究将使与数字系统的交互变得更加“愉悦”。但这显然是一个苍白的论据：就像我的保险公司不会为让我看起来更愉悦的自愿性整形手术买单一样，我无法想象在当前的紧缩时代（Era of Austerity），政策制定者会投资于旨在让用户界面（User Interfaces）变得更“愉悦”的科学研究。

Tractinsky 在其论文中提出了许多更为充分的论据。他指出，美学长期以来一直被整合在设计学科（Design Disciplines）之中，这些学科在专业和社会经济方面取得的成功是不容置疑的，其理论和方法可以被应用于 HCI 和交互设计（Interaction Design）。他指出，格式塔心理学（Gestalt Psychology）已经证明，美学标准与其他设计价值相关联，包括实用性（Usefulness）和适用性（Suitability），这是他对 HCI 领域最强有力的论据。

该社区在历史上一直倾向于实用性（the useful）。

他补充道，美学（aesthetics）满足人类的需求（而非仅仅是表层的欲望），有助于福祉（wellness），且似乎与自我的形成和体验相关，从而论证了美学对人们的生活有益。他还指出，美学有助于使原本相似的产品产生差异化，从而创造经济价值（在 Apple 的案例中，这种价值十分巨大）。我接受上述每一项（规范性，normative）论点，并强调他在此提出了该研究可能带来的诸多社会效益，其中大多数在本质上是功能性的：美学支持可用性（usability），美学满足需求，美学有助于自我构建，美学有助于经济繁荣。

如果我们关注 Tractinsky 之外的其他美学哲学家（无论他是否认同，我都将其视为其中之一），我们可以看到许多其他常见的论点，这些论点支持该研究有助于公共利益（public good）的观点。美学文献中的常见主张包括以下关于美学响应（aesthetic response）和/或美学体验（aesthetic experience）的陈述（综合自 Bardzell, 2011）：

- 美学体验在理智和情感上都是丰富且充实的，从而提高了日常生活的质量。在 HCI 领域，McCarthy

& Wright (2004) 基于哲学家 John Dewey 的美学理论，提出了一个关于良好体验的整体视角（holistic view），以便体验设计师在工作中有所指引。

- 它能够以有价值的方式引导我们的感知（perception），并挑战且提升我们的认知能力（cognitive abilities）（例如：推理 reasoning、意义构建 sense-making、学习 learning）。人机交互（HCI）研究员 Yvonne Rogers (2006) 在其工作中长期主张强调主动而非被动地使用计算机；尽管她没有使用美学的语言，但她的思考方向显然与此一致。
- 它直接有助于人类对世界的知识积累和理解。批判性设计（critical design）研究者 (Dunne & Raby, 2001) 已利用美学设计来产生关于交互设计（interaction design）的知识。
- 它可以在个人层面带来启发，并在伦理层面提升境界，例如通过增强个体的共情能力（capacity for empathy）。批判性设计研究者同样认为，他们的研究方法有助于实现这些结果。

回溯到 Plato，美学不仅涉及愉悦感，还涉及其在构建（或损害）一个受过教育且负责任的公众中所扮演的角色，这种倾向在上述列表中得到了充分体现。随着交互技术继续取代旧有的媒介形式，在中介（mediating）人们与自身、他人以及世界的交互方式方面发挥作用，使交互在这些意义上具有美学特质似乎已成为一种必然，而非可选项。

通过审美参与（aesthetic engagement）将我们自身培养为具有感知力、想象力和洞察力的公民（这是一种认识论立场 [epistemological position]），似乎越来越依赖于人机交互（human-computer interaction）。

我简要地概述了三个证明审美交互（aesthetic interaction）合理性的简单论点：享乐主义论点（hedonic argument）、功能主义论点（functionalist argument）以及认识论论点（epistemological argument）。虽然我个人支持这三个论点，但看来第二个（Tractinsky 的功能主义论点）和第三个（审美哲学家的认识论论点）对于政策制定者，以及 HCI 和交互设计（interaction design）领域的研究人员与从业者来说，可能最具说服力。
