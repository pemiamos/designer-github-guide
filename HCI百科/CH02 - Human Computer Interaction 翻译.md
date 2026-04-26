# 2. 人机交互 - 简要介绍

**来源**：*The Encyclopedia of Human-Computer Interaction, 2nd Ed.*
**Notion 原页面**：https://www.notim.so/32ec3638cbb240d299e73747f78b179e

---

[John M. Carroll](https://www.interaction-design.org/literature/author/john-m-carroll)
    人机交互（Human-Computer Interaction, HCI）是一个兴起于 20 世纪 80 年代初的研究与实践领域，最初是计算机科学中一个融合了认知科学（Cognitive Science）与人因工程（Human Factors Engineering）的专业领域。三十年来，HCI 经历了快速且稳定的扩张，吸引了来自许多其他学科的专业人士，并纳入了多样化的概念与方法。在很大程度上，HCI 现在汇集了以人为本的信息学（Human-centered Informatics）中一系列半自治的研究与实践领域。然而，HCI 中科学与实践方面迥异的概念与方法的持续融合，提供了一个极佳的范例，展示了不同的认识论（Epistemologies）与范式（Paradigms）如何在这样一个充满活力且富有成效的学术项目中实现调和与整合。

### 2.1 人机交互（HCI）的起源

    直到 20 世纪 70 年代后期，只有信息技术专业人员和狂热的爱好者才会与计算机进行交互。随着 20 世纪 70 年代后期个人计算（personal computing）的出现，这一局面发生了颠覆性的变化。个人计算既包括个人软件（生产力应用，如文本编辑器和电子表格，以及交互式电脑游戏），也包括个人电脑平台（操作系统、编程语言和硬件）；它使全世界的每个人都成为了潜在的计算机用户，并为那些希望将计算机作为工具的人，鲜明地凸显了计算机在[可用性（usability）](https://www.interaction-design.org/literature/topics/usability)方面的缺陷。

![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/unix_mailx.jpg)
    作者/版权持有者：Steven Weyhrich。版权条款与许可：保留所有权利。经许可转载。参见下文版权条款中的“例外”章节。

![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/the_herder_institute_leipzig_1989_computers_har.jpg)
    作者/版权持有者：由 Grubitzsch (geb. Raphael), Waltraud 提供。版权条款与许可：CC-Att-SA-3 (知识共享 署名-相同方式共享 3.0)

    **图 2.1** A-B：从 20 世纪 70 年代后期开始，个人计算迅速推动了计算机在普通大众中的普及。然而，非专业计算机用户经常不得不面对晦涩难懂的命令和系统对话框。

    个人计算带来的挑战在恰当的时机显现出来。认知科学（cognitive science）这一宏大项目——涵盖了认知心理学（cognitive psychology）、[人工智能（artificial intelligence）](https://www.interaction-design.org/literature/topics/ai)、语言学（linguistics）、认知人类学（cognitive anthropology）和心灵哲学（philosophy of mind）——已在 20 世纪 70 年代末形成。认知科学计划的一部分旨在阐明系统化且具有科学依据的应用，即所谓的“认知工程（cognitive engineering）”。因此，正当个人计算提出了对 HCI 的实际需求时，认知科学恰好提供了人员、概念、技能以及通过科学与工程的宏大综合来解决此类需求的前景。HCI 是认知工程的首批范例之一。

![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/human_processor.jpg)
    作者/版权持有者：Card, Moran and Newell。版权条款与许可：保留所有权利。经许可转载。参见下文[版权条款](https://www.interaction-design.org/admin/book-chapters/35313/edit?return_page=publication#copyrightNotice)中的“例外”章节。

    **图 2.2**：人类处理器模型（Model Human Processor）是一种早期的认知工程模型，旨在帮助开发人员应用认知心理学的原理。

    这一进程也得益于 HCI 邻近领域（且实际上经常与 HCI 重叠）在工程和设计方面的类似发展，特别是人因工程（human factors engineering）和文档开发（documentation development）。人因工程已开发出用于评估航空和制造业等领域人机交互的经验性和任务分析（task-analytic）技术，并正转向应对交互式系统环境，在这些环境中，人类操作员通常拥有更大的问题解决自主权。文档开发也正在超越其生产系统化技术描述的传统角色，转向一种结合了写作、阅读和媒介理论，并包含经验性[用户测试（user testing）](https://www.interaction-design.org/literature/topics/user-testing)的认知方法。文档和其他信息同样需要具备可用性。

![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/first_minimal_manual_nurnberg_funnel.jpg)
    作者/版权持有者：MIT Press。版权条款与许可：保留所有权利。经许可转载。参见下文[版权条款](https://www.interaction-design.org/admin/book-chapters/35313/edit?return_page=publication#copyrightNotice)中的“例外”章节。

    **图 2.3**：极简主义信息（Minimalist information）强调支持特定领域内的目标导向型活动。它不再采用主题层级和结构化练习，而是强调为自主行为提供简洁的支持，并帮助用户识别和从错误中恢复。

    其他在历史上具有偶然性的发展也促成了 HCI 的建立。软件工程在 20 世纪 70 年代深陷于无法处理的软件复杂度之中（即“软件危机”），开始转向关注非功能性需求（nonfunctional requirements），包括可用性和可维护性，以及依赖于迭代[原型设计（prototyping）](https://www.interaction-design.org/literature/topics/prototyping)和经验测试的经验性软件开发流程。计算机图形学（computer graphics）和信息检索（information retrieval）兴起于 20 世纪 70 年代，并迅速意识到交互式系统是超越早期[成就（achievements）](https://www.interaction-design.org/literature/topics/achievements)的关键。计算机科学中所有这些发展脉络都指向同一个结论：计算技术的未来在于理解并更好地赋能用户。这些来自需求与机遇的多元力量在 1980 年前后汇聚，激发了巨大的创造力，并形成了一个极具影响力的跨学科项目。

### 2.2 从小圈子到共同体

    人机交互（Human-Computer Interaction, HCI）最初且持久的技术核心一直是“可用性（Usability）”这一概念。这一概念最初在“易学易用”这一口号中得到了较为朴素的阐述。这种概念化的直白[简单性（Simplicity）](https://www.interaction-design.org/literature/topics/simplicity)使 HCI 在计算机领域拥有了一个尖锐且突出的身份。它起到了凝聚该领域的作用，并帮助其更广泛、更有效地影响计算机科学和技术的发展。然而，在 HCI 内部，可用性的概念几乎在不断地被重新阐释和重构，并变得日益丰富且具有引人入胜的复杂性。现在的可用性往往涵盖了诸如趣味性、福祉（Well-being）、集体效能（Collective efficacy）、审美张力（Aesthetic tension）、增强的[创造力（Creativity）](https://www.interaction-design.org/literature/topics/creativity)、心流（Flow）、对人类发展的支持等品质。对于可用性的一种更动态的看法是，将其视为一个纲领性目标，随着我们实现该目标的能力不断提升，它应当且将会持续发展。

![](https://public-arg.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/kiss.jpg)
    作者/版权持有者：©. 版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用（因无法获得许可）。参见页面[版权声明](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节（及“allRightsReserved-UsedWithoutPermission”子章节）。

    **图 2.4**：
    可用性是一种涌现的品质（Emergent quality），反映了 HCI 的掌握程度与触达范围。当代用户对系统的需求不仅仅是“[易用性（Ease of use）](https://www.interaction-design.org/literature/topics/ease-of-use）”。

    尽管 HCI 最初的学术归宿是计算机科学，且最初的重点是个人生产力应用（主要是文本编辑和电子表格），但该领域一直在不断地多样化并突破了所有边界。它迅速扩张，涵盖了可视化、信息系统、协作系统、系统开发流程以及设计领域的许多方面。如今，HCI 在许多涉及信息技术的系/学院中都有教授，包括心理学、设计、传播学、认知科学（Cognitive science）、信息科学、科学技术研究（Science and technology studies）、地理科学、管理信息系统，以及工业、制造与系统工程。HCI 的研究与实践借鉴并整合了所有这些视角。

    这种增长的结果是，H变现在对于核心概念与方法、问题领域，以及关于基础设施、应用和用户类型的假设，不再具有单一的聚焦性。事实上，再将 HCI 仅仅视为计算机科学的一个专业领域已不再合理；HCI 已经成长为比计算机科学本身更广泛、更庞大且更加多样化的领域。HCI 从最初关注个体和通用的[用户行为（User behavior）](https://www.interaction-design.org/literature/topics/user-behavior)扩展到包含社会与组织计算、针对老年人及认知与身体障碍者的[无障碍性/可访问性（Accessibility）](https://www.interaction-design.org/literature/topics/accessibility)、面向所有人以及尽可能广泛的人类经验与活动。它从桌面办公应用扩展到包含游戏、学习与教育、商业、医疗与健康应用、应急规划与响应，以及支持协作与社区的系统。它从早期的图形用户界面扩展到包含无数的交互技术与设备、多模态交互（Multi-modal interactions）、用于基于模型的[用户界面（User interface, UI）](https://www.interaction-design.org/literature/topics/ui-design)规范的工具支持，以及大量新兴的普适计算（Ubiquitous computing）、手持式和情境感知（Context-aware）交互。

    目前并没有一个统一的 HCI 专业人员概念。在 20 世纪 80 年代，HCI 的认知科学侧有时会与 HCI 的软件工具及用户界面侧进行对比。如今，HCI 核心概念与技能的版图要分化得多，也复杂得多。HCI 学术项目培养了许多不同类型的专业人员：用户体验设计师、交互设计师、用户界面设计师、应用设计师、可用性工程师、用户界面开发人员、应用开发人员、技术传播者/在线信息设计师等。事实上，HCI 的许多子社区本身也非常多样化。例如，普适计算（Ubiqu computng，又称 ubicomp）是 HCI 的一个子领域，但它同时也是一个整合了多个可辨识子领域的上位领域，例如[移动计算（Mobile computing）](https://www.interaction-design.org/literature/topics/mobile-computing)、地理空间信息系统、车载系统、社区信息化、分布式系统、手持设备、可穿戴设备、环境智能（Ambient intelligence）、传感器网络，以及可用性评估、编程工具与技术、应用基础设施的专门视角。普适计算与 HCI 之间的关系具有范式意义：HCI 是“共同体的集合（A community of communities）”。

![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/UPA_matrix.jpg)
    作者/版权持有者：User Experience Professionals Association。版权条款与许可：保留所有权利。经许可转载。参见下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/Interaction-Design-Disciplines.jpg)
    作者/版权持有者：Envis Precisely。版权条款与许可：保留所有权利。经许可转载。参见下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

    **图 2.5 A-B**：
    两幅展示当代人机交互设计中所涉及的多元学科知识与技能的可视化图表。

    事实上，“HCI 是共同体的集合”这一原则现在已成为一个被编纂的定义特征，例如体现在主要 HCI 会议和期刊的组织架构中。贯穿 HCI 各个社区的整合元素，始终是广义上的可用性批判性分析与新技术及应用开发之间的紧密联系。这是 HCI 社区定义性的身份承诺。这使得 HCI 能够成功地培养出对支撑创新技术开发的多元技能与概念的尊重，并能够定期超越学科障碍。在 2 世纪 80 年代初期，HCI 是一个规模较小且专注的专业领域。它曾是一个试图确立当时被视为“计算异端观点”的小圈子。而今天，HCI 是一个庞大且多维的共同体，由不断演进的可用性概念以及将人类活动与经验作为技术主要驱动力的整合性承诺所维系。

### 2.3 超越桌面

    考虑到人机交互（HCI）的现状，重要的是要记住，它的起源是受限于桌面的个人生产力交互，例如文字处理和电子表格。事实上，20 世纪 80 年代初最大的设计理念之一是所谓的“凌乱桌面隐喻（messy desk metaphor）”，由 Apple Macintosh 推向大众：文件和文件夹以图标的形式显示，并可以（也确实如此）散布在显示表面。凌乱的桌面是图形用户界面（Graphical User Interfaces, GUI）发展范式的完美孵化器。也许它并不像声称的那样易于学习和使用，但世界各地的人们很快就开始在显示器上双击、拖动窗口和图标，并像在物理桌面上一样，在桌面界面上弄丢东西。这与此前 Unix 的电传打型机隐喻（teletype metaphor）形成了鲜明对比，在那种模式下，所有的交互都是通过输入命令来完成的。
![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/Apple_Macintosh_Desktop.jpg)
    作者/版权持有者：未知（待调查）。版权条款与许可：未知（待调查）。参见下文[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。
    **图 2.6**：早期的 Macintosh 桌面隐喻：散布在桌面上的图标代表了文档和功能，用户可以对其进行选择和访问（如示例中的系统盘 System Disk）。
    尽管可以认为桌面隐喻是肤浅的，或者作为一种设计范式未被充分利用，但它确实激发了设计师和公众的想象力。对于 1980 年代的许多人来说，这些都是全新的可能性，专家们纷纷推测它们将如何改变办公工作。事实上，桌面设计的浪潮挑战、甚至有时威胁到了办公人员的专业技能和工作实践。如今，它们已成为文化背景的一部分。孩子们在日常生活中就能学习这些概念和技能。
    随着 HCI 的发展，它在三个不同的维度上超越了桌面。首先，桌面隐喻被证明比最初看起来更具局限性。将几十个数字对象直接表示为图标是没问题的，但这种方法很快会导致混乱，对于拥有成千上个人文件和文件夹的人来说并不实用。到 20 世纪 90 年代中期，HCI 专业人士及所有人意识到，在用户界面中，搜索（Search）比浏览（Browsing）是更基础的查找事物范式。然而讽刺的是，当 20 世纪 90 年代中期早期的万维网（World Wide Web）页面出现时，它们不仅抛弃了凌乱的桌面隐喻，而且在很大程度上完全放弃了图形交互。尽管如此，它们仍被视为可用性的突破（当然，这与 Unix 风格的工具如 ftp 和 tel算 telnet 形成了直接对比）。以图标形式展示并直接与数据对象交互的设计方法并未消失，但它不再是一种霸权式的设计概念。
![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/cluttered_desktop.jpg)
    作者/版权持有者：未知（待调查）。版权条款与许可：未知（待调查）。参见下文[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。
    **图 2.7**：早期将凌乱桌面用于个人信息空间的做法无法实现规模化（scale）。
    HCI 超越桌面的第二个维度是通过互联网对计算和社会日益增长的影响。从 20 世纪 80 年代中期开始，电子邮件（email）成为最重要的 HCI 应用之一，但讽刺的是，电子邮件使计算机和网络变成了通信渠道；人们不再是与计算机“进行”交互，而是通过计算机与其他人类进行交互。支持协作活动的工具和应用现在包括即时通讯、维基（wikis）、博客、在线论坛、社交网络、社交书签与标签服务、媒体空间和其他协作工作空间、推荐和协同过滤系统（collaborative filtering systems），以及各种在线小组和社区。集体活动的新范式和机制已经出现，包括在线拍卖、声誉系统、软传感器（soft sensors）和众包（crowdsourcing）。HCI 的这一领域，现在通常被称为[社会计算（social computing）](https://www.interaction-design.org/literature/topics/social-computing)，是发展最快的领域之一。
![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/social_media_collage.arg)
    作者/版权持有者：©。版权条款与许可：版权所有。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用（因为无法获得许可）。参见[版权声明](https://www.interaction-design.org/about/terms-of-use)页面上的“例外（Exceptions）”章节（以及“allRightsReserved-UsedWithoutPermission”子章节）。
![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/Tux.jpg)
    作者/版权持有者：由 Larry Ewing 提供。版权条款与许可：CC-Att-3 (Creative Commons Attribution 3.0 Unported)。
![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/github.jpg)
    作者/版权持有者：GitHub Inc.。版权条款与许可：版权所有。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用（因为无法获得许可）。参见[版权声明](https://www.interaction-design.org/about/terms-of-use)页面上的“例外（Exceptions）”章节（以及“allRightsReserved-UsedWithoutPermission”子章节）。
    **图 2.8 A-B-C**：极其多样化且不断扩张的社交网络服务已成为许多人日常计算体验的一部分。在线社区，如 Linux 社区和 GitHub，利用社会计算来产出高质量的知识工作。
    HCI 超越桌面的第三种方式是通过计算设备生态的持续且偶尔爆发式的多样化。在桌面应用趋于统一之前，新的设备上下文（device contexts）开始出现，特别是 20 世纪 80 年代初出现的笔记本电脑，以及 20 世纪 80 年代中期出现的掌上设备。当今的一个前沿领域是无处不在的计算（ubiquitous computing）：将计算无缝融入人类生活环境（human habitats）——汽车、家用电器、家具、服装等等。尽管桌面环境已因笔记本电脑的广泛使用而发生了变革，但桌面计算仍然非常重要。在很大程度上，桌面本身已经“走出了”桌面。
![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/telepresence.jpg)
    作者/版权持有者：由 Andrew Stern 提供。版权条款与许可：CC-Att-SA-3 (Creative Commons Attribution-ShareAlike 3.0)。
![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/Police_car_computer_USA.jpg)
    作者/版权持有者：由美国联邦政府提供。版权条款与许可：pd (Public Domain (信息为共有财产且不含原创作者身份))。
![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/augmented_reality_glogger_iphone.jpg)
    作者/版权持有者：未知（待调查）。版权条款与许可：未知（待调查）。参见下文[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。
    **图 2.9 A-B-C**：计算已走出桌面，实现随时随地的存在。计算机存在于手机、汽车、会议室和咖啡馆中。
    HCI 的重心已经超越了桌面，并且其重心将继续移动。HCI 是一个技术领域，它不可避免地受技术前沿和应用可能性的驱动。HCI 的特殊价值和贡献在于，它将研究、开发并利用这些新的可能性领域，不仅将其视为技术或设计，更将其视为增强人类活动和体验的手段。

### 2.4 任务-人工制品循环 (The task-artifact cycle)

    人机交互（HCI）脱离桌面端的过程，是技术发展模式的一个大规模范例，这种模式在人机交互的多个分析层级中均有体现。人机交互关注于人们参与并体验的活动，与中介这些活动的人工制品（Artifacts，如交互式工具和环境）之间的动态协同演化（Co-evolution）。人机交互旨在理解并批判性地评估人们使用和体验的交互技术。同时，它也关注随着人们对技术的挪用（Appropriation）、期望、概念和技能的发展，以及随着他们提出新的需求、兴趣、愿景和议程，这些交互是如何演变的。
    
    与此同时，人机交互也致力于理解当代人类的实践与愿景，包括这些活动是如何被当前的基础设施和工具所体现、细化，甚至可能受到其限制的。人机交互旨在将实践与活动理解为一种需求和设计可能性，从而构想并实现新的技术、工具和环境。它是通过活动与人工制品的协同演化——即[任务-人工制品循环](https://www.interaction-design.org/literature/topics/task-artifact-cycle)——来探索设计空间，并实现新系统与新设备的过程。
    
    ![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/task_artifact_model.jpg)
    作者/版权持有者：由 John M. Carroll 提供。版权条款与许可：CC-Att-SA-3 (Creative Commons Attribution-ShareAlike 3.0)
    **图 2.10**：人类活动隐含地表达了需求、偏好和设计愿景。人工制品的设计是对这些需求的响应，但其作用不可避免地超越了单纯的响应。在技术被采用和[挪用（Appropriation）](https://www.interaction-design.org/literature/topics/appropriation)的过程中，新的设计为行动和交互提供了新的可能性。最终，这一活动又会进一步阐明人类的新需求、偏好和设计愿景。

    将人机交互理解为植根于活动与技术人工制品之协同演化中，是非常有益的。最简单地说，它提醒我们人机交互的本质：人机交互的所有基础设施，包括其概念、方法、核心问题和令人振奋的成就，都将始终处于变动之中。此外，由于活动与人工制品的协同演化是由多元参与者之间一系列偶然性的倡议所塑造的，因此没有理由期望人机交互是趋同的或可预测的。这并不是说人机交互的进步是随机或随意的，而仅仅是说它更像世界历史，而非物理学。我们可以对此持乐观态度：个人和集体的主动性塑造了人机交互的形态，却无法改变物理定律。
    
    ![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/historical_smalltalk_gui_parc.jpg)
    作者/版权持有者：Palo Alto Research Center Incorporated (PARC) - 一家 Xerox 旗下的公司。版权条款与许可：版权所有。经许可转载。参见下文[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。
    **图 2.11**：Smalltalk 是 20 世纪 70 年代 Xerox Palo Alto Research Center 的一个编程语言和环境项目。尽管仅由少数人完成，它却成为了现代图形用户界面（GUI）的直接前身。

    任务-人工制品循环的第二个启示是，在人机交互领域，对新应用、新应用领域、新设计、新设计范式、新体验和新活动的持续探索应当始终被高度重视。我们可能觉得今天清楚地知道前进的方向，但考虑到活动与人工制品显而易见的协同演化速率，我们实际的前瞻能力可能比想象的要低。此外，由于我们实际上是在构建未来的轨迹，而不仅仅是在寻找它，因此失误的代价是巨大的。活动与人工制品的协同演化表现出强烈的滞后性（Hysteresis），也就是说，过去协同演化调整的影响会持续到遥远的未来。例如，许多人每天都在与操作系统和核心生产力应用“搏斗”，而这些应用的设计实际上是对二十多年前错误分析的演化式反应。当然，对于未来才会出现并凝聚成的价值观和标准，我们不可能始终保持正确，但我们至少应当意识到，发生具有重大后果的失误是完全可能的。
    
    ![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/Drift_table_bill_gaver_studio_shot.jpg)
    作者/版权持有者：未知（调查中）。版权条款与许可：未知（调查中）。参见下文[版权模版](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。
    
    ![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/Drift_table_bill_gaver_ceployed.jpg)
    作者/版权持有者：未知（调查中）。版权条款与许可：未知（调查中）。参见下文[版权模版](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。
    **图 2.12 A-B**：Drift Table 是一款交互式咖啡桌；桌面上方的视窗展示着英格兰和威尔士的航拍图；在桌上放置或移动物体会导致航拍图像滚动。该设计旨在引发反应，并挑战人们对家用技术的思考。

    补救措施是在发展的每一个节点都考虑多种替代方案。开展大量探索可能体验与活动的工作至关重要，例如通过设计探针（Design probes）和原型（Prototypes）来进行探索。如果我们过度关注当前具身技术（Embodied technology）的[可供性（Affordances）](https://www.interaction-design.org/literature/topics/affordances)，我们就会太容易且不加批判地接受那些会限制当代人机交互及所有未来轨迹的约束。
    
    ![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/Siri-screenshot.jpg)
    作者/版权持有者：Apple Computer, Inc.。版权条款与许可：版权所有。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用（因无法获得许可）。参见[版权声明](https://www.interaction-design.org/about/terms-of-use)页面上的“例外（Exceptions）”章节（及“allRightsReserved-UsedWithoutPermission”子章节）。
    
    ![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/Google_Glass_detail.jpg)
    作者/版权持有者：由 Antonio Zugaldia 提供。版权条款与许可：CC-Att-SA-2 (Creative Commons Attribution-ShareAlike 2.0 Unported)。
    **图 2.13 A-B**：Siri（苹果 iPhone 的语音智能助手）和 Google Project Glass 的[增强现实（Augmented Reality）](https://www.interaction-design.org/literature/topics/augmented-reality)眼镜，都是技术愿景转化为日常人机交互体验的近期案例。

    从根本上说，人机交互并非关乎自然定律。相反，它管理着[创新（Innovation）](https://www.interaction-design.org/literature/topics/innovation)，以确保人类的价值观和优先事项通过新技术得以推进，而不是被削弱。正是这一点创造了人机交互；正是这一点引领人机交互脱离了桌面端；它将继续引领人机交互走向技术中介下人类可能性的新领域。这也是为什么可用性（Usability）是一个开放式的概念，永远无法被简化为一份固定的清单。

### 2.5 理论的熔炉

    尽管人机交互（Human-Computer Interaction, HCI）作为一个通过设计来改变人类活动与体验的项目，其演进轨迹具有偶然性，但它始终与社会科学和认知科学中理论的应用与发展紧密结合。由于 HCI 所涉及的技术与人类活动处于不断的协同演进（co-evolving）之中，这一领域在某种程度上也充当了理论的实验室与孵化器。HCI 作为早期认知工程（cognitive engineering）案例研究的起源，对其学科特征产生了印记效应。从一开始，HCI 中开发并使用的模型、理论和框架就是作为科学贡献而追求的：HCI 丰富了它所借鉴的每一个理论。例如，GOMS（Goals, Operations, Methods, Selection rules；目标、操作、方法、选择规则）模型作为 HCI 中最早的原生理论，其作为认知模型的全面程度超过了当时认知科学与工程领域的其他尝试；该模型化人类处理器（model human processor）在单一模型中包含了[感知](https://www.interaction-design.org/literature/topics/perception)、注意力、短期记忆操作、规划和运动行为的简单层面。但 GOMS 同时也是一种实用工具，它阐明了科学贡献与工程及设计效能（engineering and design efficacy）并重的双重标准，而这已成为 HCI 理论与应用并行的文化。

![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/cogtool_2.jpg)
    作者/版权持有者：Bonnie E. John。版权条款与许可：保留所有权利。经许可转载。请参阅下文[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”章节。

![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/cogtool.jpg)
    作者/版权持有者：Bonnie E. John。版权条款与许可：保留所有权利。经许可转载。请参阅下文[版权und terms](https://www.interaction-design.org/about/terms-of-use)中的“例外”章节。

    **图 2.14 A-B**：
    CogTool 通过分析用户任务的演示来生成任务执行背后认知过程的模型；并基于该模型预测专家执行这些任务所需的时间。

    随着活动与人工制品（artifacts）协同演进的重心发生转移，理论开发与应用的研究重点也随之变迁。因此，早期的基于信息处理的心理学理论（如 GOMS）被用于模拟个体与键盘、简单显示器及指向设备交互时的认知与行为。随着交互变得更加多样化、应用变得更加丰富，HCI 理论的最初构想也随之扩展。例如，感知理论（perceptual theories）被用来解释图形显示器中物体的识别；心智模型理论（mental model theories）被引入以解释概念（如“凌乱的桌面”隐喻，messy desktop metaphor）在塑造交互中的作用；主动用户理论（active user theories）则被开发出来，用以解释用户如何以及为何学习并理解交互。然而，在每种情况下，这些深化研究既是科学上的进步，也为更优的工具和设计实践提供了基础。

    这种理论与应用之间的辩证关系（dialectic）在 HCI 中得以延续。我们可以很容易地识别出十余个主要的理论流派，它们本身大致可以分为三个时代：将人机交互视为信息处理的理论、将交互视为代理人（agents）执行任务的理论，以及将交互视为社会与物质环境深度嵌入（socially and materially embedded）的理论。在某种程度上，理论的演进序列可以被理解为科学机遇与应用需求的一种趋同：对相对精简的模型进行规范化与应用，明确了更丰富的人类与交互观可以如何被阐述以及能做出怎样的贡献；与此同时，个人设备成为了通往社会与物理世界交互的门户，这要求更丰富的理论框架来进行分析与设计。

![](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/hci_taxonomy.jpg)
    作者/版权持有者：未知（调查中）。版权条款与许可：未知（调查中）。请参阅下文[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”章节。

    **图 2.15**：
    在过去的三十年里，一系列理论范式相继出现，以应对 HCI 研究、设计和产品开发日益扩大的雄心。接续而来的理论既挑战了先前的关于人与交互的概念，也丰富了这些概念。所有这些理论在今日的 HCI 中仍然具有相关性且仍在被使用。

    当然，理论与时代的演进序列在某种程度上是理想化的。人们现在仍在研究 GOMS 模型；事实上，所有曾在 HCI 中被采用过的主要模型、理论和框架目前仍在使用中。而且，随着学科背景的发展，它们也在不断演进。如今的 GOMS 更多地是作为一种小众模型（niche model）而非 HCI 的主流范式，但近期已应用于智能手机设计和人机交互（human-robot interactions）的研究中。

    在 HCI 中，如何将描述性与解释性的科学目标，与规范性（prescriptive）及构建性的设计目标进行整合，或至少是实现更好的协调，是一项持久的挑战。目前至少存在三个持续发展的方向：传统上对日益广泛且深入的基础理论的应用；在特定设计领域内开发局部的、有时是依赖于特定领域的原型理论（proto-theories）；以及将设计原理（design rationale）作为基础科学与设计实践之间的中介层描述。

### 2.6 人机交互对科学、实践与认识论的影响

    人机交互（Human-Computer Interaction, HCI）最显著的成就之一，在于其不断演进的研究与实践整合模型。最初，该模型被阐述为认知科学（cognitive science）与认知工程（cognitive engineering）之间的互惠关系。随后，它雄心勃勃地纳入了多样化的科学基础，特别是社会与组织心理学、[活动理论](https://www.interaction-design.org/literature/topics/activity-theory)（Activity Theory）、分布式认知（distributed cognition）和社会学，以及用于研究人类活动（包括设计、技术开发与应用过程）的民族志方法（ethnographic approaches）。目前，该模型正在整合广泛领域的设计实践与研究，例如用户体验（user experience）的理论化以及生态可持续性。在这些发展过程中，HCI 为科学与实践之间前所未有的相互关系提供了蓝图。

    尽管 HCI 一直被视为一种设计科学（design science）或致力于为设计师提供指导，但起初这被解读为一种边界，即 HCI 研究与设计是两个各自独立的专业领域。然而，在整个 20 世纪 90 年代，HCI 直接吸收并最终催生了一系列设计社区。起初，这仅仅是对超越科学与工程范畴的方法和技术的广泛接纳。但这种向外拓展的冲动恰逢用户界面（user interface）技术的重大进步，这些进步将用户界面的大部分潜在专有价值转移到了图形设计以及更丰富的用户体验本体（ontologies）之中。

    颇具讽刺意味的是，设计师被引入 HCI 社区的时机恰到好处，帮助其重塑为一个设计学科。这一转型的很大一部分在于创造了此前并不存在的设计学科与议题。例如，[用户体验设计](https://www.interaction-design.org/literature/topics/ux-design)（user experience design）和[交互设计](https://www.interaction-design.org/literature/topics/interaction-design)（interaction design）并非被引入 HCI 的，反而属于 HCI 向设计界输出的首批成果。同样，对设计中创造力与理性之间生产性张力的分析，需要像 HCI 这样既要求设计具备内在逻辑、可进行系统化评估与维护，同时又能激发新体验与新见解的设计领域。设计目前是 HCI 中变化最快的方面。在未来十年内，很可能会有更多新的设计原型学科（proto-disciplines）从 HCI 中涌现。

    没人能指责 HCI 固步自封（resting on laurels）。自诞生以来，HCI 关于底层科学如何启发实践与活动领域，以及如何被实践与活动领域所启发的观念一直在不断演进。在 HCI 的发展过程中，无论从何种衡量标准来看，这个在智力与实践上都取得成功的领域，都主动拥抱了具有范式变革意义的科学与认识论（epistemological）修正。其结果是一个日益碎片化且复杂的领域，但其成功程度却进一步提升。这一案例与 Kuhn 关于智力项目通过最终被推翻的范式进行发展的观点（Kuhnian view）相矛盾。因此，HCI 社区在推进其元项目（meta-project）方面的持续成功，不仅对以人为本的信息学（human-centered informatics）具有深远意义，对认识论（epistemology）也具有深远影响。

### 2.7 指引（Pointers）：如何进一步学习

    在这些“指引”中，我列出了针对上述讨论的通用背景参考文献、针对文中具体论点的特定参考文献，以及对《人机交互百科全书》（*Encyclopedia of Human-Computer Interaction*，来自 Interaction-Design.org）中其他章节的引用。我按章节对这些指引进行了组织，因此接下来的六个部分（见下文）与本文本身的六个主要章节标题相呼应（见上文）。

### 2.7.1 人机交互（HCI）的起源

    关于早期 HCI 发展的学科版图（disciplinary landscape），已有许多非常易读的描述：
    - 《Cognitive Science》期刊 1980 年的卷次，生动地展现了当时正在构建的认知科学（cognitive science）基础 (http://csjarchive.cogsci.rpi.edu/1980v04/index.html)；
    - F. Brooks 的著作 *The Mythical Man-Month* (1975, Addison-Wesley) 对软件工程（software engineering）进行了深刻的分析，并且是“在复杂软件的设计与开发中，迭代原型设计（iterative prototyping）是不可避免的”这一观点的原始出处；
    - J. Foley 和 A. van Dam 的著作 *Computer Graphics* (1982, Addison Wesley) 将早期的计算机图形学（computer graphics）领域描述为后来发展成为人机交互（human-computer interaction）的根源。
    关于 HCI 创立的生动原始资料——1982 年在美国马里兰州盖瑟斯堡（Gaithersburg, Maryland）举行的美国标准局（US Bureau of Standards）会议论文集（proceedings），可在 ACM Digital Library 中获取：[http://dl.acm.org/citation.cfm?id=800049](http://dl.acm.org/citation.cfm?id=800049)。
    目前已有多部关于 HCI 历史的著作出版：
    - Carroll, J.M. (1997) Human-Computer Interaction: Psychology as a science of design. *Annual Review of Psychology, 48, *61-83.?á (Co-published (slightly revised) in *International Journal of Human-Computer Studies, 46,* 501-522).
    - Grudin, J. (2012) A Moving Target: The evolution of Human-computer Interaction. In J. Jacko (Ed.), *Human-computer interaction handbook: Fundamentals, evolving technologies, and emerging applications. (3rd edition).* Taylor & Francis.
    - Myers, B.A. (1998) A Brief History of [Human Computer Interaction](https://www.interaction-design.org/literature/topics/human-computer-interaction) Technology. *ACM interactions*. Vol. 5, no. 2, March. pp. 44-54.
    领先的 HCI 教科书也包含了一些关于历史的讨论（见下文）。

### 2.7.2 从小圈子到共同体

关于如何描述可用性（Usability）的演进，存在一些争议。在本综述中，我采取一种历史视角，认为该概念本身正在演进，这类似于物理学对待其基本概念（如重力和质量）的方式。另请参阅：
- Carroll, J.M. (2004) Beyond fun. *ACM interactions, 11(5),* 38-40.

ACM 人机交互特别兴趣小组（SIGCHI）及其 CHI 会议——这是最通用且最重要的 HCI 会议之一——现在已明确地组织成了若干社区，负责管理技术议程（technical program）的各个部分（http://www.sigchi.org/communities）。在 2012 年秋季，这些社区包括：CCaA（Creativity, Cognition and Art，创造力、认知与艺术）、CSCW（Computer-Supported Cooperative Work，计算机支持的协同工作）、EICS（Engineering Interactive Computer Systems，工程交互计算机系统）、HCI 与可持续发展、HCI 教育、HCI4D（HCI for Development，面向发展的 HCI）、文化遗产研究（Heritage Matters）、拉丁美洲 HCI、模式语言与 HCI、研究与实践的交互（Research-practice Interaction）、UbiComp（Ubiquitous Computing，普适计算）以及 UIST（User Interface Software and Tools，用户界面软件与工具）。

通过考察嵌入在 ACM 之外的其他专业共同体（professional communities）中的 HCI 活动和兴趣小组，可以更全面地理解 HCI 的多样性：Design Research Society（设计研究学会）([designresearchsociety.org](http://www.designresearchsociety.org/))、Association for Information Systems（信息系统协会）([sighci.org](http://sighci.org/))、Human Factors and Ergonomics Society（人因与工效学学会）([hfes.org](http://www.hfes.org/))、Society for Technical Communication（技术传播学会）([stc.org](http://www.stc.org/))、AIGA ([aiga.org](http://aiga.org))、International Communication Association（国际传播学会）([icahdq.org](http://icahdq.org))、Interaction Design Association（交互设计协会）([https://www.ixda.org/](https://www.ixda.org/))、IEEE Professional Communication Society（IEEE 专业传播学会）([pcs.ieee.org](http://pcs.ieee.org/))、European Association of Work and Organizational Psychology（欧洲工作与组织心理学协会）([eawop2013.org](http://eawop2013.org/))，以及许多其他组织。

在《人机交互百科全书》（*Encyclopedia of Human-Computer Interaction*）中，可以在[第 1、3、8、13、15、19、21 和 22 章](https://www.interaction-design.org/encyclopedia/)找到更多相关材料。

### 2.7.3 超越桌面 (Beyond the desktop)

    关于桌面隐喻（desktop metaphor）的一个经典讨论见于 Apple 的人机交互指南：[Apple](http://en.wikipedia.org/wiki/Apple_Inc.) & [Raskin, J](http://en.wikipedia.org/wiki/Jef_Raskin). (1992). *Macintosh Human Interface Guidelines*. [Addison-Wesley Professional](http://en.wikipedia.org/wiki/Addison-Wesley). [ISBN](http://en.wikipedia.org/wiki/International_Standard_Book_Number) [0-201-62216-5](http://en.wikipedia.org/wiki/Special:BookSources/0-201-62216-5).
    对 Macintosh 用户界面范式（user interface paradigm）的早期批判包括：
    - Gentner, D. and Nielsen, J. (1996) The Anti-Mac interface, *Communications of the ACM* **39**, 8 (August), 70-82.
    协作（collaboration）、移动性（mobility）以及新型用户设备与交互方式的兴起，作为推动“桌面之外的人机交互（HCI beyond the desktop）”的主要主题，自然已被广泛讨论；以下是一些切入点：
    - Horn, D.B., Finholt, T.A., Birnholtz, J.P., Motwani, D. and Jayaraman, S.
(2004) Six degrees of jonathan grudin: a social network analysis of the
evolution and impact of CSCW research. In *Proceedings of the 2004 ACM conference on Computer supported cooperative work* (CSCW '04). ACM, New York, NY, USA, 582-591.
    - Luff, P. and Heath, C. (1998) Mobility in collaboration. In *Proceedings of the 1998 ACM conference on Computer supported cooperative work* (CSCW '98). ACM, New York, NY, USA, 305-314.
    - Shaer, O. and Hornecker, E. (2010) Tangible User Interfaces: Past, Present, and Future Directions. *Found. Trends Hum.-Comput. Interact.* 3, 1-2 (January), 1-137.
    - Waller V. and Johnston, R.B. (2009) Making ubiquitous computing available. *Commun. ACM* 52, 10 (October 2009), 127-130.
    在《人机交互百科全书》（Encyclopedia of Human-Computer Interaction）中可以找到更多相关材料，见于[第 4、14、23 和 27 章](https://www.interaction-design.org/encyclopedia/)。

### 2.7.4 任务-人工制品循环 (The task-artifact cycle)

    我在此使用“任务-人工制品循环（task-artifact cycle）”这一术语，该术语最初由我在 1991 年与 Wendy Kellogg 及 Mary Beth Rosson 合作的一篇论文中提出，尽管我认为“活动（activity）”比“任务（task）”更能准确表达我的本意。不出所料，任务-人工制品循环的术语本身就是人机交互（HCA）在其自身基础之上发生变迁的一个例证；参见：
    - Carroll, J.M., Kellogg, W.A., & Rosson, M.B. (1991) The task-artifact cycle.?á In J.M. Carroll (Ed.),?á *Designing Interaction: Psychology at the human-computer interface. *?áNew York: Cambridge University Press, pages 74-102.
    关于 Smalltalk 项目历史的优秀参考文献为：
    - Kay, A.C. (1996) The early history of Smalltalk. In *History of programming languages---II*, Thomas J. Bergin, Jr. and Richard G. Gibson, Jr. (Eds.). ACM, New York, NY, USA 511-598.
    关于漂移桌项目（drift table project）的更多讨论，请参见：
    - Boucher, A. and Gaver, W. 2006. Developing the drift table. *interactions* 13, 1 (January 2006), 24-27.
    关于通过漂移桌示例所强调的普遍观点的更多讨论，请参见：
    - Sengers, P. and W. Gaver, W. (2006) Staying open to 
interpretation: engaging multiple meanings in design and evaluation. In *Proceedings of the 6th conference on Designing Interactive systems* (DIS '06). ACM, New York, NY, USA, 99-108.
    在《人机交互百科全书》（Encyclopedia of Human-Computer Interaction）中可以找到更多相关材料，见 [第 7、12、14 和 20 章](https://www.interaction-design.org/encyclopedia/)。

### 2.7.5 理论的熔炉 (A caldron of theory)

    我编辑了一本关于理论综述（theory overviews）的书籍（Carroll, 2003），见下文引用。该书可在网上获取 (http://www.sciencedirect.com/science/book/9781558608085)。目前，我正在《以人为本的信息学综合讲座》（Synthesis Lectures on Human-Centered Informatics）中策划理论综述 (http://www.morganclaypool.com/toc/hci/1/1)。
    - John, B.E. (2011) Using predictive human performance models to inspire and support UI design recommendations. In *Proceedings of the 2011 annual conference on Human factors in computing systems* (CHI '11). ACM, New York, NY, USA, 983-986.
    在《人机交互百科全书》（Encyclopedia of Human-Computer Interaction）中可以找到更多相关材料，见第 [5, 6, 9, 11, 16, 17, 24, 25, 26 和 28 章](https://www.interaction-design.org/encyclopedia/)。

### 2.7.6 HCI 对科学实践与认识论的启示

我在文中提到的关于创造力（Creativity）与设计合理性（Design Rationale）的研究汇编于 Carroll (2012) 一书中，参考文献见下文。我认为，通过对比以下三种在 HCI 设计中对[美学（Aesthetics）](https://www.interaction-design.org/literature/topics/aesthetics)的处理方式，可以很好地理解本节所描述的理论多声部性（Theoretical multi-vocality）（所有文献均出版于 *Synthesis Lectures on Human-Centered Informatics*, http://www.morganclaypool.com/toc/hci/1/1）：
- Hassenzahl, M. (2010). *Experience Design: Technology for All the Right Reasons*.
- Sutcliffe, A. (2009) *Designing for User Engagement: Aesthetic and Attractive User Interfaces*
- Wright, P. and McCarthy, J. (2010) *Experience-Centered Design: Designers, Users, and Communities in Dialogue*.

我在关于科学与知识发展方面引用 Kuhn 的文献如下：
- Kuhn, T.S. (1962) [*The Structure of Scientific Revolutions*](http://en.wikipedia.org/wiki/The_Structure_of_Scientific_Revolutions). Chicago: University of Chicago Press.
- Kuhn, T.S. (1977) *The Essential Tension: Selected Studies in Scientific Tradition and Change*. Chicago and London: University of Chicago Press.

### 2.7.7 教科书 (Textbooks)

    由于重要的专著 (monographs) 数量过于庞大，无法一一列举，因此我在下文中重点列出了几本重要的教科书。读者还应查阅 [HCI Bibliography](http://hcibib.org/)、[HCC Education Digital Library](http://hcc.cc.gatech.edu/)、[ACM Digital Library](http://www.acm.org/dl) 以及 [Synthesis Series of lectures on human-centered informatics](http://www.morganclaypool.com/toc/hci/1/1)。以下是三本最全面的教科书：
    - [Dix](https://www.interaction-design.org/references/authors/alan_j__dix.html), A.J., [Finlay](https://www.interaction-design.org/references/authors/janet_e__finlay.html), J.E., [Abowd](https://www.interaction-design.org/references/authors/gregory_d__abowd.html), G.D. and [Beale](https://www.interaction-design.org/references/authors/russell_beale.html), R. (2003). *Human-Computer Interaction (3rd Edition).* Prentice Hall
    - [Rogers](https://www.interaction-design.org/references/authors/yvonne_rogers.html), Y., [Sharp](https://www.interaction-design.org/references/authors/helen_sharp.html), H. and [Preece](https://www.interaction-design.org/references/authors/jennifer_j__preece.html), J.J. (2011) *Interaction Design: Beyond Human-Computer Interaction (3rd ed.).* John Wiley and Sons
    - [Shneiderman](https://www.interaction-design.org/references/authors/ben_shneiderman.html), B. and [Plaisant](https://www.interaction-design.org/references/authors/catherine_plaisant.html), C. (2009). *Designing the User Interface: Strategies for Effective Human-Computer Interaction (5th ed.).* Addison-Wesley
    另有一些著作提供了更具专业性的 HCI 视角。Carroll (2003) 汇编了一系列关于 HCI 主要理论的入门论文。Löwgren 和 Stolterman (2007) 从设计视角 (design perspective) 探讨了 HCI。Rosson 和 Carroll (2002) 强调了 HCI 的软件工程 (software engineering) 视角，并通过一系列案例研究传达了可用性 (usability) 的工程过程视角。Tidwell (2011) 提出了一种基于模式 (pattern-based) 的用户界面设计方法。
    - [Carroll](https://www.interaction-design.org/references/authors/john_m__carroll.html), John M. (ed.) (2003). *HCI Models, Theories, and Frameworks: Toward a Multidisciplinary Science.* Morgan Kaufmann
    - Löwgren, J. and Stolterman, E. (2007) *Thoughtful Interaction Design: A Design Perspective on Information Technology.* MIT Press.
    - [Rosson](https://www.interaction-design.org/references/authors/mary_beth_rosson.html), M.B. and [Carroll](https://www.interaction-design.org/references/authors/john_m__carroll.html), J.M. (2002). *Usability Engineering: Scenario-Based Development of Human Computer Interaction.* Morgan Kaufmann.
    - Tidwell, J. (2011) *Designing Interfaces (2nd ed.).* O’Reilly Media.

### 2.7.8 期刊 (Journals)

人机交互（Human-Computer Interaction, HCI）领域领先的综合性期刊是 [*ACM Transactions on Computer-Human Interaction*]。然而，还有许多其他质量相当的知名期刊：[*Human-Computer Interaction*]（侧重于设计研究（design research））、[*Interacting With Computers*]、[*International Journal of Human-Computer Studies*]、*Behaviour and Information Technology*、[*International Journal of Human-Computer Interaction*] 以及 [*Journal of Computer-Supported Cooperative Work*]。近期，信息系统协会（Association for Information Systems）创办了 *[*Transactions on Human-Computer Interaction.*]。Morgan-Claypool 出版了一系列专题丛书（monograph series），即 [*Synthesis Lectures on Human-Centered Informatics*]。

我个人对于 HCI 的兴起与发展的观点，在以下其他论文、专著（monographs）及编著（edited books）的引言中均有详细阐述：

- Carroll, J.M. (1995) Introduction: The scenario perspective on system development. 载于 Carroll, J.M. (Ed.), *Scenario-based design: Envisioning work and technology in system development.* New York: John Wiley & Sons, pp 1-17.
- [Carroll](https://www.interaction-design.org/references/authors/john_m__carroll.html), John M. (1997) Human-Computer Interaction: Psychology as a Science of Design. *Annual Review of Psychology*, 48, 61-83. 该文曾共同出版（并经过轻微修订）于 [*International Journal of Human-Computer Studies*], 46(4), 501-522.
- Carroll, J.M. (1998) Reconstructing minimalism. 载于 J.M. Carroll (Ed.) *Minimalism beyond “The Nurnberg Funnel”.* M.I.T. Press.
- Carroll, J.M. (2000) *Making use: Scenario-based design of human-computer interactions.* MIT Press. 日文版由 Kyoritsu Publishing 于 2003 年出版；由 Kentaro Go 教授翻译。
- [Carroll](https://www.interaction-design.org/references/authors/john_m__carroll.html), John M. (2002). Human-Computer Interaction. 载于: (ed.), *MacMillan Encyclopedia of Cognitive Science*. Macmillan-Nature Publishing Group.
- [Carroll](https://www.interaction-design.org/references/authors/john_m__carroll.html), John M. (2004). Beyond fun. [*Interactions*], 11(5), 38-40.
- Carroll, J.M. (2010) Narrating the Future: [Scenarios](https://www.interaction-design.org/literature/topics/user-scenarios) and the Cult of Specification. 载于 Selber, S. (Ed.), *Rhetorics And Technologies: New directions in writing and communication.* University of South Carolina Press, pp. 134-147.
- Carroll, J.M. (2010). Conceptualizing a possible discipline of Human-Computer Interaction. *Interacting with Computers*, 22, 3-12.
- Carroll, J.M. (2012) *The neighborhood in the Internet: Design research projects in community informatics (社区信息学).* Routledge.
- Carroll, J.M. (2012) Creativity and Rationale: The Essential Tension, 载于 J.M. Carroll (Ed.) *Creativity and rationale: Enhancing human experience by design.* Springer, pages 1-10.

### 2.7.9 相关会议系列

### 2.7.9.1 CHI - 人机交互计算系统中的人类因素 (Human Factors in Computing Systems)

    [2011](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2011_conference_on_human_factors_in_computing_systems.html)[2010](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2010_conference_on_human_factors_in_computing_systems.html)[2009](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2009_conference_on_human_factors_in_computing_systems.html)[2008](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2008_conference_on_human_factors_in_computing_systems.html)[2007](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2007_conference_on_human_factors_in_computing_systems.html)[2006](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2006_conference_on_human_factors_in_computing_systems.html)[2005](https://www.interaction-design.org/references/conferences/proceeding_of_the_sigchi_2005_conference_on_human_factors_in_computing_systems.html)[2004](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2004_conference_on_human_factors_in_computing_systems.html)[2003](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_2003_human_factors_in_computing_systems_conference.html)[2002](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_2002_conference_on_human_factors_in_computing_systems_conference.html)[2001](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_2001_human_factors_in_computing_systems_conference.html)[2000](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_2000_human_factors_in_computing_systems_conference.html)[1999](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_99_human_factors_in_computing_systems_conference.html)[1998](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_98_human_factors_in_computing_systems_conference.html)[1997](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_97_human_factors_in_computing_systems_conference.html)[1996](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_96_human_factors_in_computing_systems_conference.html)[1995](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_95_human_factors_in_computing_systems_conference.html)[1994](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_94_human_factors_in_computing_systems_conference.html)[1993](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_93_human_factors_in_computing_systems_conference.html)[1992](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_92_human_factors_in_computing_systems_conference.html)[1991](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_91_human_factors_in_computing_systems_conference.html)[1990](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_90_human_factors_in_computing_systems_conference.html)[1989](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_89_human_factors_in_computing_systems_conference.html)[1988](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_88_human_factors_in_computing_systems_conference.html)[1987](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_87_human_factors_in_computing_systems_conference.html)[1986](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_86_human_factors_in_computing_systems_conference.html)[1985](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_85_human_factors_in_computing_systems_conference.html)[1983](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_83_human_factors_in_computing_systems_conferenc.html)[1982](https://www.interaction-design.org/references/conferences/proceedings_of_the_sigchi_conference_on_human_factors_in_computing_systems.html)

### 2.7.9.2 ECSCW - 欧洲计算机支持的协同工作会议 (European Conference on Computer Supported Cooperative Work)

    [2009](https://www.interaction-design.org/references/conferences/proceedings_of_the_11th_european_conference_on_computer-supported_cooperative_work.html)[2007](https://www.interaction-design.org/references/conferences/proceedings_of_the_tenth_european_conference_on_computer-supported_cooperative_work.html)[2003](https://www.interaction-design.org/references/conferences/proceedings_of_the_eighth_european_conference_on_computer-supported_cooperative_work.html)[2003](https://www.interaction-design.org/references/conferences/proceedings_of_the_fifth_european_conference_on_computer_supported_cooperative_work_%28ecscw2003%29.html)[2001](https://www.interaction-design.org/references/conferences/proceedings_of_the_seventh_european_conference_on_computer-supported_cooperative_work.html)[2001](https://www.interaction-design.org/references/conferences/ecscw_2001_-_proceedings_of_the_seventh_european_conference_on_computer_supported_cooperative_work.html)[1999](https://www.interaction-design.org/references/conferences/ecscw_99_-_proceedings_of_the_sixth_european_conference_on_computer_supported_cooperative_work.html)[1997](https://www.interaction-design.org/references/conferences/proceedings_of_the_fifth_european_conference_on_computer-supported_cooperative_work.html)[1995](https://www.interaction-design.org/references/conferences/ecscw_95_-_proceedings_of_the_fourth_european_conference_on_computer-supported_cooperative_work.html)[1993](https://www.interaction-design.org/references/conferences/ecscw_93_-_proceedings_of_the_third_european_conference_on_computer_supported_cooperative_work.html)[1991](https://www.interaction-design.org/references/conferences/ecscw_91_-_proceedings_of_the_second_european_conference_on_computer-supported_cooperative_work.html)[1989](https://www.interaction-design.org/references/conferences/ec-cscw_89_-_proceedings_of_the_first_european_conference_on_computer-supported_cooperative_work.html)

### 2.7.9.3 CSCW - 计算机支持的协同工作会议 (Conference On Computer-Supported Cooperative Work)

    [2012](https://www.interaction-design.org/references/conferences/proceedings_of_acm_cscw12_conference_on_computer-supported_cooperative_work.html)[2012](https://www.interaction-design.org/references/conferences/companion_proceedings_of_acm_cscw12_conference_on_computer-supported_cooperative_work.html)[2012](https://www.interaction-design.org/references/conferences/xxxxxx_ings_of_acm_cscw12_conference_on_computer-supported_cooperative_work.html)[2011](https://www.interaction-design.org/references/conferences/proceedings_of_acm_cscw11_conference_on_computer-supported_cooperative_work.html)[2010](https://www.interaction-design.org/references/conferences/proceedings_of_acm_cscw10_conference_on_computer-supported_cooperative_work.html)[2008](https://www.interaction-design.org/references/conferences/proceedings_of_acm_cscw08_conference_on_computer-supported_cooperative_work.html)[2006](https://www.interaction-design.org/references/conferences/proceedings_of_acm_cscw06_conference_on_computer-supported_cooperative_work.html)[2004](https://www.interaction-design.org/references/conferences/proceedings_of_acm_cscw04_conference_on_computer-supported_cooperative_work.html)[2004](https://www.interaction-design.org/references/conferences/proceedings_of_the_2004_acm_conference_on_computer_supported_cooperative_work.html)[2002](https://www.interaction-design.org/references/conferences/proceedings_of_the_2002_acm_conference_on_computer_supported_cooperative_work.html)[2000](https://www.interaction-design.org/references/conferences/proceedings_of_the_2000_acm_conference_on_computer_supported_cooperative_work.html)[1998](https://www.interaction-design.org/references/conferences/proceedings_of_the_1998_acm_conference_on_computer_supported_cooperative_work.html)[1996](https://www.interaction-design.org/references/conferences/proceedings_of_the_1996_acm_conference_on_computer_supported_cooperative_work.html)[1994](https://www.interaction-design.org/references/conferences/proceedings_of_the_1994_acm_conference_on_computer_supported_cooperative_work.html)[1992](https://www.interaction-design.org/references/conferences/proceedings_of_the_1992_acm_conference_on_computer-supported_cooperative_work.html)[1990](https://www.interaction-design.org/references/conferences/proceedings_of_the_1990_acm_conference_on_computer-supported_cooperative_work.html)[1988](https://www.interaction-design.org/references/conferences/proceedings_of_the_1988_acm_conference_on_computer-supported_cooperative_work.html)[1986](https://www.interaction-design.org/references/conferences/proceedings_of_the_1986_acm_conference_on_computer-supported_cooperative_work.html)

### 2.7.9.4 UIST - 用户界面软件与技术研讨会 (Symposium on User Interface Software and Technology)

    [2012](https://www.interaction-design.org/references/conferences/adjunct_proceedings_of_the_2012_acm_symposium_on_user_interface_software_and_technology.html)[2012](https://www.interaction-design.org/references/conferences/proceedings_of_the_2012_acm_symposium_on_user_interface_software_and_technology.html)[2011](https://www.interaction-design.org/references/conferences/proceedings_of_the_2011_acm_symposium_on_user_interface_software_and_technology.html)[2010](https://www.interaction-design.org/references/conferences/proceedings_of_the_2010_acm_symposium_on_user_interface_software_and_technology.html)[2009](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_symposium_on_user_interface_software_and_technology.html)[2008](https://www.interaction-design.org/references/conferences/proceedings_of_the_21st_annual_acm_symposium_on_user_interface_software_and_technology.html)[2007](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_symposium_on_user_interface_software_and_technology.html)[2007](https://www.interaction-design.org/references/conferences/proceedings_of_the_20th_annual_acm_symposium_on_user_interface_software_and_technology.html)[2007](https://www.interaction-design.org/references/conferences/proceedings_of_20th_acm_symposium_on_user_interface_software_and_technology.html)[2006](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_symposium_on_user_interface_software_and_technology.html)[2005](https://www.interaction-design.org/references/conferences/proceedings_of_the_2005_acm_symposium_on_user_interface_software_and_technology.html)[2004](https://www.interaction-design.org/references/conferences/proceedings_of_the_2004_acm_symposium_on_user_interface_software_and_technology.html)[2003](https://www.interaction-design.org/references/conferences/proceedings_of_the_16th_annural_acm_symposium_on_user_interface_software_and_technology.html)[2003](https://www.interaction-design.org/references/conferences/companion_proceedings_of_acm_uist03_conference_on_user_interface_software_and_technology.html)[2002](https://www.interaction-design.org/references/conferences/proceedings_of_the_15th_annual_acm_symposium_on_user_interface_software_and_technology.html)[2001](https://www.interaction-design.org/references/conferences/proceedings_of_the_14th_annual_acm_symposium_on_user_interface_software_and_technology.html)[2000](https://www.interaction-design.org/references/conferences/proceedings_of_the_13th_annual_acm_symposium_on_user_interface_software_and_technology.html)[1999](https://www.interaction-design.org/references/conferences/proceedings_of_the_12th_annual_acm_symposium_on_user_interface_software_and_technology.html)[1998](https://www.interaction-design.org/references/conferences/proceedings_of_the_11th_annual_acm_symposium_on_user_interface_software_and_technology.html)[1997](https://www.interaction-design.org/references/conferences/proceedings_of_the_10th_annual_acm_symposium_on_user_interface_software_and_technology.html)[1996](https://www.interaction-design.org/references/conferences/proceedings_of_the_9th_annual_acm_symposium_on_user_interface_software_and_technology.html)[1995](https://www.interaction-design.org/references/conferences/proceedings_of_the_8th_annual_acm_symposium_on_user_interface_and_software_technology.html)[1994](https://www.interaction-design.org/references/conferences/proceedings_of_the_7th_annual_acm_symposium_on_user_interface_software_and_technology.html)[1993](https://www.interaction-design.org/references/conferences/proceedings_of_the_6th_annual_acm_symposium_on_user_interface_software_and_technology.html)[1992](https://www.interaction-design.org/references/conferences/proceedings_of_the_5th_annual_acm_symposium_on_user_interface_software_and_technology.html)[1991](https://www.interaction-design.org/references/conferences/proceedings_of_the_4th_annual_acm_symposium_on_user_interface_software_and_technology.html)[1990](https://www.interaction-design.org/references/conferences/proceedings_of_the_3rd_annual_acm_siggraph_symposium_on_user_interface_software_and_technology.html)[1989](https://www.interaction-design.org/references/conferences/proceedings_of_the_2nd_annual_acm_siggraph_symposium_on_user_interface_software_and_technology.html)[1988](https://www.interaction-design.org/references/conferences/proceedings_of_the_1st_annual_acm_siggraph_symposium_on_user_interface_software.html)

### 2.7.9.5 NordiCHI - 北欧人机交互会议 (Nordic conference on human-computer interaction)

    [2010](https://www.interaction-design.org/references/conferences/proceedings_of_the_sixth_nordic_conference_on_human-computer_interaction.html)[2008](https://www.interaction-design.org/references/conferences/proceedings_of_the_fifth_nordic_conference_on_human-computer_interaction.html)[2006](https://www.interaction-design.org/references/conferences/proceedings_of_the_fourth_nordic_conference_on_human-computer_interaction.html)[2004](https://www.interaction-design.org/references/conferences/proceedings_of_the_third_nordic_conference_on_human-computer_interaction.html)[2002](https://www.interaction-design.org/references/conferences/proceedings_of_the_second_nordic_conference_on_human-computer_interaction.html)[2002](https://www.interaction-design.org/references/conferences/nordichi_2002_-_proceedings_of_the_second_nordic_conference_on_human-computer_interaction.html)[2000](https://www.interaction-design.org/references/conferences/proceedings_of_the_first_nordic_conference_on_human-computer_interaction.html)[2000](https://www.interaction-design.org/references/conferences/proceedings_of_the_first_nordic_conference_on_computer-human_interaction.html)

### 2.7.9.6 BCSHCI People and Computers

    [2012](https://www.interaction-design.org/references/conferences/proceedings_of_the_hci12_conference_on_people_and_computers_xxvi.html)[2010](https://www.interaction-design.org/references/conferences/proceedings_of_the_hci10_conference_on_people_and_computers_xxiv.html)[2009](https://www.interaction-design.org/references/conferences/proceedings_of_the_hci09_conference_on_people_and_computers_xxiii.html)[2008](https://www.interaction-design.org/references/conferences/proceedings_of_the_hci08_conference_on_people_and_computers_xxii.html)[2006](https://www.interaction-design.org/references/conferences/proceedings_of_the_hci06_conference_on_people_and_computers_xx.html)[2006](https://www.interaction-design.org/references/conferences/people_and_computers_xx_-_proceedings_of_hci.html)[2005](https://www.interaction-design.org/references/conferences/proceedings_of_the_hci05_conference_on_people_and_computers_xix.html)[2004](https://www.interaction-design.org/references/conferences/proceedings_of_the_hci04_conference_on_people_and_computers_xviii.html)[2003](https://www.interaction-design.org/references/conferences/proceedings_of_the_hci03_conference_on_people_and_computers_xvii.html)[2002](https://www.interaction-design.org/references/conferences/proceedings_of_the_hci02_conference_on_people_and_computers_xvi.html)[2001](https://www.interaction-design.org/references/conferences/proceedings_of_the_hci01_conference_on_people_and_computers_xv.html)[2000](https://www.interaction-design.org/references/conferences/proceedings_of_the_hci00_conference_on_people_and_computers_xiv.html)[1998](https://www.interaction-design.org/references/conferences/proceedings_of_the_thirteenth_conference_of_the_british_computer_society_human_computer_interaction_specialist_group_-_people_and_computers_xiii.html)[1997](https://www.interaction-design.org/references/conferences/proceedings_of_the_twelfth_conference_of_the_british_computer_society_human_computer_interaction_specialist_group_-_people_and_computers_xii.html)[1996](https://www.interaction-design.org/references/conferences/proceedings_of_the_eleventh_conference_of_the_british_computer_society_human_computer_interaction_specialist_group_-_people_and_computers_xi.html)[1995](https://www.interaction-design.org/references/conferences/proceedings_of_the_tenth_conference_of_the_british_computer_society_human_computer_interaction_specialist_group_-_people_and_computers_x.html)[1994](https://www.interaction-design.org/references/conferences/proceedings_of_the_ninth_conference_of_the_british_computer_society_human_computer_interaction_specialist_group_-_people_and_computers_ix.html)[1993](https://www.interaction-design.org/references/conferences/proceedings_of_the_eighth_conference_of_the_british_computer_society_human_computer_interaction_specialist_group_-_people_and_computers_viii.html)[1992](https://www.interaction-design.org/references/conferences/proceedings_of_the_seventh_conference_of_the_british_computer_society_human_computer_interaction_specialist_group_-_people_and_computers_vii.html)[1991](https://www.interaction-design.org/references/conferences/proceedings_of_the_sixth_conference_of_the_british_computer_society_human_computer_interaction_specialist_group_-_people_and_computers_vi.html)[1989](https://www.interaction-design.org/references/conferences/proceedings_of_the_fifth_conference_of_the_british_computer_society_human_computer_interaction_specialist_group_-_people_and_computers_v.html)[1988](https://www.interaction-design.org/references/conferences/proceedings_of_the_fourth_conference_of_the_british_computer_society_human_computer_interaction_specialist_group_-_people_and_computers_iv.html)[1987](https://www.interaction-design.org/references/conferences/proceedings_of_the_third_conference_of_the_british_computer_society_human_computer_interaction_specialist_group_-_people_and_computers_iii.html)[1986](https://www.interaction-design.org/references/conferences/proceedings_of_the_second_conference_of_the_british_computer_society_human_computer_interaction_specialist_group_-_people_and_computers_ii.html)[1985](https://www.interaction-design.org/references/conferences/proceedings_of_the_conference_of_the_british_computer_society_human_computer_interaction_specialist_group_-_people_and_computers_i.html)

### 2.7.9.7 SIGGROUP - 支持小组工作的会议 (Conference on Supporting Group Work)

    [2010](https://www.interaction-design.org/references/conferences/group10_international_conference_on_supporting_group_work.html)[2009](https://www.interaction-design.org/references/conferences/group09_-_international_conference_on_supporting_group_work.html)[2007](https://www.interaction-design.org/references/conferences/group07-_international_conference_on_supporting_group_work.html)[2005](https://www.interaction-design.org/references/conferences/group05-_international_conference_on_supporting_group_work.html)[2003](https://www.interaction-design.org/references/conferences/proceedings_of_the_international_acm_siggroup_conference_on_supporting_group_work_2003.html)[2001](https://www.interaction-design.org/references/conferences/proceedings_of_the_international_acm_siggroup_conference_on_supporting_group_work_2001.html)[1999](https://www.interaction-design.org/references/conferences/proceedings_of_the_international_acm_siggroup_conference_on_supporting_group_work_1999.html)[1997](https://www.interaction-design.org/references/conferences/proceedings_of_the_international_acm_siggroup_conference_on_supporting_group_work_1997.html)[1995](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_conference_on_organizational_computing_systems_1995.html)[1993](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_conference_on_organizational_computing_systems_1993.html)[1991](https://www.interaction-design.org/references/conferences/proceedings_of_the_conference_on_organizational_computing_systems_1991.html)[1990](https://www.interaction-design.org/references/conferences/proceedings_of_the_conference_on_office_information_systems_1990.html)[1988](https://www.interaction-design.org/references/conferences/proceedings_of_the_conference_on_office_information_systems_1988.html)[1986](https://www.interaction-design.org/references/conferences/proceedings_of_the_third_acm-sigois_conference_on_office_information_systems_1986.html)[1984](https://www.interaction-design.org/references/conferences/proceedings_of_the_second_acm-sigoa_conference_on_office_information_systems_1984.html)[1982](https://www.interaction-design.org/references/conferences/proceedings_of_the_sigoa_conference_on_office_information_systems_1982.html)

### 2.7.9.8 DIS - 交互系统设计 (Designing Interactive Systems)

    [2012](https://www.interaction-design.org/references/conferences/proceedings_of_dis12_designing_interactive_systems.html)[2010](https://www.interaction-design.org/references/conferences/proceedings_of_dis10_designing_interactive_systems.html)[2008](https://www.interaction-design.org/references/conferences/proceedings_of_dis08_designing_interactive_systems.html)[2006](https://www.interaction-design.org/references/conferences/proceedings_of_dis06-_designing_interactive_systems-_processes%2C_practices%2C_methods%2C_%26_techniques.html)[2004](https://www.interaction-design.org/references/conferences/proceedings_of_dis04-_designing_interactive_systems-_processes%2C_practices%2C_methods%2C_%26_techniques.html)[2002](https://www.interaction-design.org/references/conferences/proceedings_of_dis02-_designing_interactive_systems-_processes%2C_practices%2C_methods%2C_%26_techniques.html)[2000](https://www.interaction-design.org/references/conferences/proceedings_of_dis00-_designing_interactive_systems-_processes%2C_practices%2C_methods%2C_%26_techniques.html)[1997](https://www.interaction-design.org/references/conferences/proceedings_of_dis97-_designing_interactive_systems-_processes%2C_practices%2C_methods%2C_%26_techniques.html)[1995](https://www.interaction-design.org/references/conferences/proceedings_of_dis95-_designing_interactive_systems-_processes%2C_practices%2C_methods%2C_%26_techniques.html)
    下届会议将于 [2016 年 6 月 8 日](https://www.interaction-design.org/calendar/designing_interactive_systems_dis_2016_jun_8th_2016.html) 在澳大利亚布里斯班 (Brisbane, Australia) 举行

### 2.7.9.9 CC - 创造力与认知 (Creativity and Cognition)

    [2011](https://www.interaction-design.org/references/conferences/proceedings_of_the_2011_conference_on_creativity_and_cognition.html)[2009](https://www.interaction-design.org/references/conferences/proceedings_of_the_2009_conference_on_creativity_and_cognition.html)[2007](https://www.interaction-design.org/references/conferences/proceedings_of_the_2007_conference_on_creativity_and_cognition.html)[2005](https://www.interaction-design.org/references/conferences/proceedings_of_the_2005_conference_on_creativity_and_cognition.html)[2002](https://www.interaction-design.org/references/conferences/proceedings_of_the_2002_conference_on_creativity_and_cognition.html)1999

### 2.8 参考文献 (References)

    [Myers](https://www.interaction-design.org/references/authors/brad_a__myers.html), Brad A. (1998): A Brief History of Human-Computer Interaction Technology. In [Interactions](https://www.interaction-design.org/references/periodicals/interactions.html), 5 (2) pp. 44-54

    人机交互（Human-Computer Interaction, HCI）是一个研究与实践领域，最初于 20 世纪 80 年代初作为计算机科学的一个子领域出现，融合了认知科学（cognitive science）与人因工程（human factors engineering）。在过去的三十年里，HCI 经历了迅速而稳定的扩张，吸引了许多其他学科的专业人士，并采用了多种不同的概念与方法。在很大程度上，HCI 现在涵盖了以人为中心的信息科学（human-centered information science）中一系列半自治的研究与实践领域。然而，HCI 中不同视角与方法的持续综合，提供了一个极佳的范例，展示了不同的认识论（epistemologies）与范式（paradigms）如何在这样一个充满活力且富有成效的智力项目中得到调和与整合。

### 2.1 HCI 的起源

    直到 20 世纪 70 年代末，与计算机进行交互（interaction）的人仅限于信息技术专业人员和爱好者。随着个人计算机（personal computer）在 20 世纪 70 年代后期的出现，这一局面发生了剧变。个人计算机，包括个人软件（productivity applications，如文本编辑器和电子表格，以及交互式电子游戏）和个人计算机平台（操作系统、编程语言和硬件），使全世界的每个人都成为了潜在的计算机用户，并生动地凸显了那些希望将计算机作为工具的人们在可用性（usability）方面所面临的缺陷。
    ![https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/unix_mailx.jpg](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/unix_mailx.jpg)
    作者/版权所有者：Steven Weyhrich。版权条款与许可：版权所有，保留所有权利。经许可复制。请参阅下文版权条款中的“例外”部分。
    ![https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/the_herder_institute_leipzig_1989_computers_har.jpg](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/the_herder_institute_leipzig_1989_computers_har.jpg)
    作者/版权所有者：Grubitzsch（出生名 Raphael），Waltraud。版权条款与许可：CC-Att-SA-3（署名-相同方式共享 3.0 协议）
    **图 2.1** A-B：个人计算机在 20 世纪 70 年代后期开始，迅速将计算机的使用推向了普通大众。然而，非专业计算机用户经常受到晦涩的命令和系统对话框的困扰。
    个人计算机带来的挑战在恰当的时机显现出来。在 20 世纪 70 年代末，认知科学（cognitive science）的广泛研究项目开始形成，其中包括认知心理学（cognitive psychology）、[人工智能](https://www.interaction-arg.org/literature/topics/ai)、语言学（linguistics）、认知人类学（cognitive anthropology）和心灵哲学（philosophy of mind）。认知科学的部分项目旨在应用系统化的表达与科学知识，被称为“认知工程（cognitive engineering）”。因此，正当个人计算机呈现出 HCI 的实际需求时，认知科学提供了人员、概念、技能，以及通过科学与工程手段解决这些需求的愿景。HCI 是认知工程的首批范例之一。
    ![https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/human_processor.jpg](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/human_processor.jpg)
    作者/版权所有者：Card、Moran 和 Newell。版权条款与许可：版权所有，保留所有权利。经许可复制。请参阅下文版权条款中的“例外”部分。
    **图 2.2**：人类处理器（Human Processor）模型是一种早期的认知工程模型，旨在帮助开发人员应用来自认知心理学的原则。
    这得益于与 HCI 相邻的工程与设计领域中类似的进展，事实上，这些领域经常与 HCI 重叠，特别是人类因素工程（human factors engineering）和文档开发（documentation development）。人类因素工程已经发展出了用于评估人-系统交互（human-system interaction）的经验性技术和任务分析（task analysis）技术（例如在航空和制造业领域），并正朝着人机操作员拥有更大问题解决自由度的交互式系统上下文（context）方向发展。文档开发正在从其传统角色——即生成系统化的技术描述——转向包含写作、阅读和媒体理论的认知方法，以及经验性的[用户测试](https://www.interaction-design.org/literature/topics/user-testing)。文档和其他信息同样需要具备可用性。
    ![https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/first_minimal_manual_nurnberg_funnel.jpg](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/first_minimal_manual_nurnberg_funnel.jpg)
    作者/版权所有者：MIT Press。版权条款与许可：版权所有，保留所有权利。经许可复制。请参阅下文版权条款中的“例外”部分。
    **图 2.3**：极简主义信息（Minimalism in information）强调支持面向领域的、目标导向（goal-directed）的活动。它强调对自主行动的简洁支持，并支持错误的识别与纠正。
    其他历史性的有利发展也促成了 HCI 的建立。在 20 世纪 70 年代，软件工程陷入了无法管理的软件复杂性（即“软件危机（software crisis）”）之中，开始关注非功能性需求（non-functional requirements），包括可用性（usability）和可维护性（maintainability），并依赖于包含迭代[原型制作](https://www.interaction-design.org/literature/topics/prototyping)和经验性测试的经验性软件开发过程。计算机图形学（computer graphics）和信息检索（information retrieval）出现在 20 世纪 70 年代，并迅速意识到交互式系统是超越早期[成就](https://www.interaction-design.org/literature/topics/achievements)的关键。计算机科学中所有这些发展线索都指向同一个结论：前进的道路在于理解用户并更好地赋能（empower）用户。计算机设备生态系统的不断多样化是 HCI 超越桌面端的第三种方式。在桌面应用程序稳固之前，新的设备上下文（context）出现了，特别是 20 世纪 80 年代初开始出现的笔记本电脑，以及 80 年代中期开始出现的手持设备。如今，普适计算（ubiquitous computing）是一个前沿领域：每个人都拥有一台计算机，而计算机不再是一个独立的实体，而是嵌入在环境中的网络与计算力量。

### 2.2 从团伙到社群

人机交互（Human-Computer Interaction, HCI）的初始和持久的技术焦点是“可用性（Usability）”概念。这个概念最初有点幼稚地表达为“易于学习，易于使用”的口号。这种概念的直白[简单性（Simplicity）](https://www.interaction-design.org/literature/topics/simplicity)赋予了 HCI 在计算机领域中一个突出的身份。它在领域内保持了凝聚力，并帮助它更广泛地和有效地影响了计算机科学和技术的发展。然而，在 HCI 内部，可用性概念几乎不断地被重新表述和重构，变得越来越丰富和有趣。可用性现在通常包括诸如乐趣、健康、集体效能、美学张力、增强的[创造力（Creativity）](https://www.interaction-design.org/literature/topics/creativity)、流（Flow）、支持人类发展等品质。对可用性更动态的看法是一个计划性目标，随着我们更进一步地达到它的能力而不断发展。

![https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/kiss.jpg](https://public-media.interaction-design.org/images/encyclopedia/human_computer_interaction_hci/kiss.jpg)
作者/版权所有者：©。版权条款和许可证：版权所有，保留所有权利。根据公平使用原则未经许可使用。请参阅下面的版权条款中的“例外”一节。
**图2.4**：可用性是反映 HCI 掌握和触及的品质。当代用户想从系统中得到的不仅仅是“易于使用”。

尽管 HCI 的初始学术家园是计算机科学，它的初始重点是个人生产力应用程序，主要是文本编辑和电子表格，但该领域不断多样化并超越了所有界限。它迅速扩展到包括可视化、信息系统、协同系统、系统开发过程和许多设计领域。HCI 现在在许多涉及信息技术的部门/学院中进行教学，包括心理学、设计、传播研究、认知科学（Cognitive Science）、信息科学、科学技术研究、地理科学、管理信息系统和工业、制造与系统工程。HCI 研究和实践利用并整合了所有这些视角。

这种增长的结果是，HCI 现在与核心概念和方法、问题领域和基础设施、应用程序和用户类型的假设方面较少地集中。实际上，现在不再将 HCI 视为计算机科学的一个专业领域；HCI 已经变得比计算机科学本身更加广泛、更大和更多样化。HCI 从其最初的关注个人和通用[用户行为（User Behavior）](https://www.interaction-design.org/literature/topics/user-behavior)扩展到社交和组织计算、面向老年人、认知和身体障碍者的[可访问性（Accessibility）](https://www.interaction-design.org/literature/topics/accessibility)，以及最广泛的人类经验和活动领域。它从桌面办公应用程序扩展到游戏、学习和教育、商务、健康和医疗应用程序、紧急规划和响应以及支持协作和社群的系统。它从早期的图形用户界面（Graphical User Interface, GUI）扩展到多种交互技术和设备、多模态交互（Multimodal Interaction）、面向模型的[用户界面（User Interface, UI）](https://www.interaction-design.org/literature/topics/ui-design)规范的工具支持，以及许多新兴的普遍、手持和上下文感知交互（Context-aware Interaction）。

没有统一的 HCI 专业概念。在 20 世纪 80 年代，HCI 的认知科学方面有时与 HCI 的软件工具和用户界面方面形成对比。现在，HCI 核心概念和技能的景观更加分化和复杂。
