# 15. 可用性评估 (1) (Usability Evaluation)

**来源**：The Encyclopedia of Human-Computer Interaction, 2nd Ed.
**Notion 原页面**：https://www.notion.so/d405fe40837c439ca0765ac27c108ae7

---

[Gilbert Cockton](https://www.interaction-design.org/literature/author/gilbert-cockton)
简单来说，[可用性评估](https://www.interaction-design.org/literature/topics/usability)（Usability Evaluation）旨在评估一个[交互系统](https://www.interaction-design.org/literature/topics/usability)（Interactive System）在易用性和愉悦感方面的程度。尽管实际情况并非如此简单，但让我们先从关于可用性评估的以下几个命题开始讨论：

1. 可用性（Usability）是所有交互式数字技术中一种固有的、可衡量的属性（Measurable Property）。
1. [人机交互](https://www.interaction-design.org/literature/topics/usability)（Human-Computer Interaction）研究人员和[交互设计](https://www.interaction-design.org/literature/topics/interaction-design)（Interaction Design）专业人士已经开发出了能够判定交互系统或设备是否可用的评估方法。
1. 当系统或设备被判定为可用时，可用性评估方法还能通过使用稳健、客观且可靠的[指标](https://www.interaction-design.org/literature/topics/usability)（Metrics）来确定其可用性的程度。
1. 评估方法和指标在人机交互的研究文献和从业者文献中有着详尽的记录。希望在可用性测量与评估方面培养专业能力的人，可以通过阅读这些方法、学习如何应用它们，从而熟练地判定一个交互系统或设备是否可用，以及在何种程度上可用。

以上命题代表了一种理想状态。我们需要了解当前的研究与实践在哪些方面未能达到这一理想状态，以及差距程度如何。在理想与现实之间仍存在差距的地方，我们需要探讨如何改进方法（methods）和指标（metrics）以弥补这一差距。正如任何学术探索（intellectual endeavour）一样，我们应当保持开放的心态，并承认上述部分或全部命题不仅目前并非真实，而且可能永远无法实现。我们可能需要在此关闭一些大门，但通过这样做，我们将能更好地开启新的大门，甚至穿过它们。

## 15.1 从第一世界的压迫到第三世界的赋能

自从人机交互（Human-Computer Interaction, HCI）作为一项跨学科尝试（inter-disciplinary endeavour）诞生以来，可用性（Usability）一直是交互设计（Interaction Design）研究与实践中的一个基础概念。对某些人而言，它过去是且现在依然是 HCI 的核心概念。而对另一些人来说，它虽然依然重要，但仅是交互设计中几个关键关注点之一。

最好能从可用性的定义开始，但在这个问题上，我们正处于一个存在分歧的领域。相关的定义将结合关于可用性的具体立场来呈现。你必须选择一个符合你设计哲学（design philosophy）的定义。下文提供了三种不同的定义。

同样，描述可用性如何被评估也是有益的，但对可用性的不同理解会导致不同的实践方式。专业实践具有很大的多样性，且许多经验无法从一个项目直接推广到另一个项目。评估者必须选择如何进行评估。评估必须经过设计，而设计则需要做出选择。

### 15.1.1 人机交互与可用性的起源

人机交互（Human-Computer Interaction, HCI）与可用性（Usability）起源于 20 世纪 80 年代计算机价格的下降。当时，许多员工首次能够拥有自己的*个人计算机*（Personal Computer，简称 PC）。在计算机发展的最初三十年里，几乎所有用户都是操作昂贵集中式设备的资深专业人员。从 20 世纪 60 年代分时系统（Timesharing）和小型机（Minicomputers）的引入开始，用户群体逐渐向低专业技能方向转移。随着 80 年代 PC 的普及，计算机用户在操作系统（Operating Systems）和应用软件（Applications Software）方面缺乏培训，或仅接受过基础培训。然而，当时的软件设计实践仍默认用户是具备专业知识且能力出众的，认为用户熟悉技术术语和系统架构，并具备解决计算机使用问题的能力。这种隐含假设很快变得不可接受。对于普通用户而言，交互式计算往往与持续的挫败感以及随之而来的焦虑联系在一起。对于大多数用户来说，计算机显然过于难以使用，甚至在很多情况下完全不可用。因此，对于任何非专业技术人员使用的交互式软件而言，*可用性*成为了设计的核心目标。“用户友好（User-friendly）”等流行词也随之进入日常语境。最初，可用性和用户友好都被理解为一种

交互式软件（Interactive Software）。软件要么是可用的，要么是不可用的。不可用的软件可以通过重新设计（Re-design）使其变得可用。

![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/IBM_Personal_Computer_5150.jpg)
作者/版权持有者：Courtesy of Boffy b。版权条款与许可：CC-Att-SA-3 (Creative Commons Attribution-ShareAlike 3.0)。

![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/Desktop_personal_computer.jpg)
作者/版权持有者：Courtesy of Jeremy Banks。版权条款与许可：CC-Att-2 (Creative Commons Attribution 2.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/usability_and_ergonomics_of_computer_workstation.jpg)
作者/版权持有者：Courtesy of Berkeley Lab。版权条款与许可：pd (Public Domain (公共领域，指共有财产且不含原创作者身份的信息))。

**图 15.1 A-B-C**：家用个人计算机（PC）及其相关外设（Associated Peripherals）如今在世界各地的家庭中已成为常见景象。随着 PC 的引入，可用性（Usability）成为了一个关键问题。

### 15.1.2 从可用性到用户体验：经由使用质量的演进

在 20 世纪 90 年代，人们对可用性（Usability）更深入的理解将其从一种“全或无”的二元属性（Binary property）转变为一个涵盖不同可用程度的连续体（Continuum）。与此同时，人机交互（HCI）的关注点转向了[使用情境（Contexts of Use）](https://www.interaction-design.org/literature/topics/contexts-of-use) (Cockton 2004)。可用性不再是 HCI 的主导概念，研究日益关注交互软件与其周围使用情境之间的适配度（Fit）。使用质量（Quality in Use）不再被简单地视为一个交互系统本身具有多少可用性的问题，而在于它在多大程度上适配其使用情境。在国际标准工作中，“使用质量”成为了替代“可用性”的首选术语，因为它避免了将可用性视为交互系统的一种绝对的、与情境无关的不变属性（Context-free invariant property）的暗示。在世纪之交，网络数字化媒体（如 Web、移动端、交互式电视、公共装置）的兴起为 HCI 带来了全新的情感关注，从而产生了一个比可用性更具吸引力的术语：[用户体验（User Experience）](https://www.interaction-design.org/literature/topics/ux-design)。

因此，目前对可用性的理解与 20 世纪 80 年代 HCI 早期阶段的理解有所不同。从那时起，[易用性（Ease of Use）](https://www.interaction-design.org/literature/topics/ease-of-use)

[这种情况] 已经有所改善，这得益于人们对交互设计（Interaction Design）的关注，以及发达经济体中大部分人口 IT 素养（IT Literacy）的提升。对基础计算机操作的熟悉程度现已广泛普及，诸如“数字原住民（Digital Natives）”和“数字排斥（Digital Exclusion）”等术语便证明了这一点，而这些词汇在 20 世纪 80 年代几乎不会引起关注。可用性（Usability）在交互设计中不再自动成为主导关注点。它依然至关重要，因为面对难以使用的数字技术而产生的挫败感在现实中依然普遍。糟糕的可用性依然存在，但我们已经超越了 Thomas Landauer 在 1996 年提出的 *Trouble with Computers* (Landauer 1996) 所描述的阶段。当个人电脑、手机和互联网在 2011 年的“阿拉伯之春（Arab Spring）”等重大国际动荡中发挥关键作用时，数字技术的价值可以极大地掩盖其缺陷。

### 15.1.3 从“计算机带来的麻烦”到“数字技术引发的麻烦”

如今，来自发展中国家的读者可能会将 Landauer 的 *Trouble with Computers* 视为那些过度敏感且缺乏动力（poorly motivated）的西方用户的抱怨。1999 年 1 月 26 日，在新德里的 NIIT 办公场所被开了一个“墙洞（hole in the wall）”。通过这个洞，邻近的 Kalkaji 贫民窟的居民可以免费使用一台计算机。这迅速走红，尤其是那些没有任何经验、能够自行学会使用计算机的孩子们。这促使 NIIT 的 Dr. Mitra [提出](http://www.hole-in-the-wall.com/docs/Paper01.pdf) 如下假设：

> 只要为学习者提供合适的计算设施，并配备具有娱乐性和激励性的内容以及极少量的（人为）指导，任何一组儿童都可以通过偶然学习（incidental learning）掌握基础的计算机技能。
> —— [http://www.hole-in-the-wall.com/Beginnings.html](http://www.hole-in-the-wall.com/Beginnings.html)

这与 20 世纪 80 年代的可用性危机（usability crisis）形成了鲜明对比。1999 年的计算机比 80 年代的更容易使用，但仍然存在使用挑战。尽管如此，残余的可用性困扰对于本世纪 Kalkaji 贫民窟的孩子们来说，其相关性非常有限。

世界是复杂的，人们在意的事情是复杂的，数字技术也是多样化的。在这种多样性的……

面对复杂性，我们不能简单地进行一次“审判”，将数字技术直接送入“可用性天堂”或“不可用地狱”。

可用性（Usability）的故事是一场从[简单性（Simplicity）](https://www.interaction-design.org/literature/topics/simplicity)到复杂性的反直觉之旅。数字技术的演进如此迅速，以至于人们对可用性的理论认知始终未能跟上计算机实际使用的现状。20 世纪 80 年代新旧世界企业为确保 IT 投资回报（Returns on Investment）而苦苦挣扎的痛苦，与第三世界独裁政权中争取民主运动对社交媒体的利用之间，毫无交集。然而，我们不能简单地抛弃可用性的概念而止步于此。即使是对最熟练、最有经验的用户而言，使用过程依然可能令人沮丧、烦躁，且存在不必要的困难，甚至完全无法操作。

![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/hole_in_the_wall_1.jpg)
版权条款与许可：版权所有。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅[版权声明](https://www.interaction-design.org/about/terms-of-use)页面的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

**图 15.2**：NIIT 在新德里的“墙洞（hole in the wall）”计算机

![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/hole_in_the_wall_2.jpg)
版权

条款与许可：版权所有。根据合理使用原则（Fair Use Doctrine），在无法获得许可的情况下，未经许可使用。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面中的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

**图 15.3**：NIIT 在新德里的“墙洞（hole in the wall）”计算机

### 15.1.4 从人机交互（HCI）的唯一关注点到用户体验中持久且重要的因素

这篇百科条目并非是对可用性（Usability）的挽歌。尽管可用性现在被掩盖在更广泛的*使用质量（quality in use）*和*用户体验（user experience）*层级之下，但它并未消亡。例如，我偶尔会通过短信为我女儿提供一些 IT 技术支持。有一次，我不得不向她解释如何强制重启一台死机且无法响应的笔记本电脑。她关于这个问题的最后一条信息是：

> 现在修好了！我之前不知道长按电源键和短按的效果是不一样的。

考虑到这一功能的隐蔽性（短按会让许多笔记本电脑进入休眠状态），我女儿不知道存在“长按”这一操作也就不足为奇了。此外，由于笔记本电脑死机的情况很少发生，我女儿几乎没有机会学习这一操作。在这种情况下，她必须依赖我的知识。如果没有先前的经验（例如关闭 iPhone 的操作），她很难凭自己知道这一点。

![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/power_button_holding_or_pressing.jpg)
作者/版权持有者：Courtesy of Rico Shen. 版权条款与许可：CC-Att-SA-3 (Creative Commons Attribution-ShareAlike 3.0).
**图 15.4**：长按还是短按？谁能知道？

可用性试图涵盖的那些关于计算机使用的持久现实依然存在，且它们对设计成功的潜在破坏力并未减轻。

与三十多年前相比，情况已然不同。正如所有学科历史一样，新事物并未抹除旧事物，而是像地质地层（geological strata）一样，新层覆盖在旧层之上，而可用性（Usability）的露头（outcrops）在不断演进的更广泛的用户体验（User Experience）图景中依然可见。正如地质学一样，我们需要根据其潜在的历史进程和剧变来理解当前的知识图景（intellectual landscape）。

因此，接下来的内容并非一次景观之旅，而是一系列挖掘，旨在揭示在过去三十年里，可用性在不同时间、不同地点的具体内涵。在此基础上，我们将重新关注交互设计（Interaction Design）图景中的当前变化，这些变化应当让可用性在更广泛的“为人类价值而设计（Designing for Human Values）”（Harper et al. 2008）的理解中占据一个稳定的位置。但现在，让我们从头开始，快速回顾人机交互（Human-Computer Interaction, HCI）的历史，以揭示关于可用性的本质及其与交互设计之间关系的未解决的矛盾。

## 15.2 从可用性到用户体验——张力与方法

在 20 世纪 70 年代，人们首次意识到需要设计一种仅需具备计算机硬件和操作系统基础知识即可使用的交互式软件（interactive software）。这一领域的先驱性软件设计工作由 Carnegie Mellon University (CMU) 的 Fred Hansen、University of California, San Francisco (UCSF) 的 Tony Wasserman、Xerox Palo Alto Research Center (PARC) 的 Alan Kay、IBM 的 Engel 和 Granda，以及 BBN Technologies 的 Pew 和 Rollins 共同推动（关于早期人机交互（Human-Computer Interaction, HCI）工作的回顾，请参阅 Pew 2002）。这些工作采用了多种方法，涵盖了从详细的[设计指南（design guidelines）](https://www.interaction-design.org/literature/topics/design-guidelines)到针对软件设计及其开发过程的高层原则。它将心理学和计算机科学的知识与能力结合在一起。这一先驱团体被称为 *Software Psychology Society*（软件心理学协会），成立于 1976 年，总部位于华盛顿特区（Washington DC）地区 (Shneiderman 1986)。这种由认知心理学（cognitive psychology）和计算机科学领域的学者与从业者共同开展的协作，锻造了一套研究与实践方法。这套方法在近 20 年的时间里一直是交互设计（Interaction Design）研究的主导范式（paradigm），并在随后的十年中依然保持着强大的影响力。然而，这种协作在可用性（usability）的本质问题上存在着某种张力（tension）。

最初的关注点主要集中在认知层面，探讨[用户界面](https://www.interaction-design.org/literature/topics/ui-design)（User Interface）特性与人类绩效（Human Performance）之间的因果关系，但对于用户界面特性与人类属性如何相互作用持有不同的观点。如果人类的认知属性是固定且普适的，那么用户界面特性就可能是固有地可用或不可用的，这使得可用性（Usability）成为交互软件的一种*固有二元属性（inherent binary property）*，即一个交互系统简单地被定义为“可用”或“不可用”。软件可以通过符合那些可通过心理学实验发现、制定和验证的准则与原则，从而在固有上实现可用。然而，如果人类的认知属性不仅在个体之间存在差异，而且在不同环境下也有所不同，那么可用性就变成了一种涌现属性（Emergent Property），它不仅取决于交互系统的特性和质量，还取决于谁在使用该系统，以及他们试图用它做什么。后者的观点在 20 世纪 90 年代因“社会转向（turn to the social）”（Rogers et al. 1994）而得到了极大的加强。然而，随着 HCI 研究扩展到一系列专注于 Association for Computing Machinery (ACM) 会议的专业社区，这里的许多理论张力（Intellectual Tension）得到了化解，例如 1986 年开始的 ACM Conference on Computer Supported Cooperative Work (CSCW) 或 ACM Symposium on User Interface Software。

自 1988 年起，可用性（Usability）的社会学理解开始与计算机支持的协同工作（Computer-Supported Cooperative Work, CSCW）联系在一起，而技术层面的理解则与用户界面软件与技术（User Interface Software and Technology, UIST）相关联。

在 20 世纪 90 年代初，各大顶级会议中基于心理学的可用性方法研究依然强劲。然而，可用性从业者对学术研究场所（venues）感到不满，于是首届可用性专业人士协会（Usability Professionals Association, UPA）会议于 1992 年举行。这种从业者的分歧发生在软件心理学会（Software Psychology Society）在盖瑟斯堡（Gaithersburg）组织会议仅 10 年之后，而 ACM CHI 系列会议正是由此产生。这使得许多应用可用性研究逐渐脱离了主流人机交互（Human-Computer Interaction, HCI）研究者的视野。这种分离在一定程度上被 UPA 的开放获取（Open Access）期刊《可用性研究杂志》（*Journal of Usability Studies*）所弥补，该杂志于 2005 年创刊。

![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/shneiderman_designing_the_user_interface_UI_87.jpg)
作者/版权持有者：Ben Shneiderman 和 Addison-Wesley。版权条款与许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

**图 15.5**：软件心理学先驱 Ben Shneiderman 编写了第一本 HCI 教科书

### 15.2.1 新方法、受损的商品与一个令人心寒的事实

因此，可用性（Usability）概念的核心存在一个困境：它究竟是系统的属性，还是使用的属性？20 世纪 90 年代人机交互（HCI）研究的碎片化导致了一个结果，即那些专注于可用性的研究人员和从业者为了追求实用主义（Pragmatism），而忽略了这些重要的概念性问题。到 20 世纪 90 年代初，已经开发出一系列评估可用性的方法。[*用户测试*（User Testing）](https://www.interaction-design.org/literature/topics/user-testing) (Dumas and Redish 1993) 在 80 年代末就已经相当成熟，它本质上是心理学实验的一种变体，仅包含因变量（Dependent variables）（被测试的交互系统成为了独立常量 [Independent constant]）。*低成本方法*（Discount methods）包括快速且低成本的用户测试，以及诸如 [*启发式评估*（Heuristic Evaluation）](https://www.interaction-design.org/literature/topics/heuristic-evaluation) (Nielsen 1994) 等检查法（Inspection methods）。关于 *基于模型的方法*（Model-based methods）的研究（例如 *GOMS* 模型 [Goals, Operators, Methods, and Selection rules] - John and Kieras 1996）仍在继续，但到 2000 年，主流出版物已变得越来越少。

随着检查法、基于模型的方法以及实证（Empirical）（例如用户测试）评估方法的出现，人们开始质疑哪种评估方法最好，以及在何时、为何使用该方法。实验性研究试图通过将评估方法视为

……在对比研究中的自变量，这些研究通常将问题数量（Problem counts）和/或问题分类（Problem classifications）作为因变量（Dependent variables）。然而，可用性方法（Usability methods）的规范过于不足，导致无法被一致地应用，这使得 Wayne Gray 和 Marilyn Salzman 在其 1998 年的 *Damaged Merchandise* 论文中证伪了几项关键研究。

针对该论文的评论未能消除 *Damaged Merchandise* 指控所带来的影响，而本世纪前十年的进一步研究不仅增加了对方法对比的担忧，还对可用性方法本身的有效性提出了质疑。因此，Morten Hertzum 和 Niels Jacobsen 在 2001 年发表了关于使用可用性方法的“令人心惊的事实”：存在显著的评估者效应（Evaluator effects）。对于深入理解 Gray 和 Salzman 批判的人来说，这并不令人惊讶，因为可用性方法应用中的不一致性使得在正式研究中进行有效的对比几乎成为不可能，而在那些未尝试进行控制的研究中，这种情况则更为严重。

Gray 和 Salzman 以及 Hertzum 和 Jacobsen 的批判性分析，使得关于可用性的实用主义研究（Pragmatic research）对顶尖的人机交互（Human-Computer Interaction, HCI）期刊和会议而言更缺乏吸引力。可用性研究对方法的关注度有所下降，批判性观点不仅揭示了在可用性差的原因（是系统、用户还是两者兼有？）上存在不确定性所带来的后果，还揭示了人们对于“可用性（Usability）”一词涵盖范围缺乏共识。

![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/usability_winners.jpg)
作者/版权持有者：由 kinnigurl 提供。版权条款与许可：CC-Att-SA-2 (Creative Commons Attribution-ShareAlike 2.0 Unported)。
**图 15.6**：2020 年可用性评估方法（Usability Evaluation Method）奖牌获得者

### 15.2.2 我们可以解决这个问题：将评估方法置于其（工作）语境之中

自 21 世纪 00 年代后期以来，关于*可用性（usability）*和*方法（methods）*的研究已被关于*用户体验（user experience）*和*可用性工作（usability work）*的研究所取代。*用户体验*是一个比可用性更广泛的概念，它超越了效率、任务质量和模糊的用户满意度，转而广泛地考虑交互中的认知、情感、社会和生理方面。*可用性工作*是指由可用性专家开展的工作，而方法为这项工作提供支持。方法并非孤立地被使用，也不应被孤立地评估。孤立地评估方法忽略了这样一个事实，即可用性工作在特定的项目或组织语境（organisational contexts）中，会对多种方法进行结合、配置和适配。对这一事实的认识体现在研究重点从*可用性方法*向*可用性工作*的扩展，例如在与欧洲 MAUSE 项目（COST Action 294, 2004-2009）相关的博士论文（Dominic Furniss, Tobias Uldall-Espersen, Mie Nørgaard）中有所体现。这在 MAUSE 第二工作组的协作研究（Cockton and Woolrych 2009）中也得到了证明。

关注实际工作使得人们能够客观地认识设计和评估方法。方法仅是可用性工作的一个方面。它们并非可用性工作中具有决定性影响（deterministic effects）的独立组件，即其影响并非在所有项目和组织语境中都保证会发生且完全一致。

相反，由于不同开发环境下设计与评估资源的程度和质量各异，预计会出现广泛的评估者效应（Evaluator Effects）。这意味着我们不能也不应该在人为隔离的研究环境（Artificial Isolated Research Settings）中评估可用性评估方法。相反，研究应当从可用性工作的具体现实出发，并在该背景下探索评估方法的真实本质及其影响。

![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/Usability_Lab_Alan_Woolrych_at_the_University_of_Sunderland.jpg)
作者/版权持有者：未知（待调查）。版权条款与许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 15.7**：
工作中可用性专家：University of Sunderland 的 Alan Woolrych 正在使用一套极简的移动可用性实验室（Mobile Usability Lab）配置，包括带有音频录制的网络摄像头、PC 屏幕及声音录制，其右侧还配备了一个眼动仪（Eye Tracker）。

### 15.2.3 漫长而曲折的道路：可用性从过去到现在的演进

可用性（Usability）如今已成为用户体验（User Experience, UX）的一个维度，而可用性方法则成为了用户体验工作中一个相对松散的预设领域。尽管如此，可用性依然至关重要。近年来将关注点扩大至用户体验的价值在于，它将可用性工作置于具体的语境（Context）之中。可用性工作不再被要求孤立地证明其价值，而是作为提升设计质量的多个互补因素之一。

因此，作为人机交互（Human-Computer Interaction, HCI）核心关注点的可用性，已经历了心理学理论（Psychological Theory）、方法论实用主义（Methodological Pragmatism）以及认知幻灭（Intellectual Disillusionment）等阶段。近期对使用质量（Quality in Use）和用户体验的关注表明，交互设计（Interaction Design）不能仅仅聚焦于交互软件的功能（Features）和属性（Attributes）。相反，我们必须关注用户与软件在特定场景（Specific Settings）下的交互。我们不能仅凭软件本身是否具有“可用性”来推论，而必须考虑软件在实际使用过程中发生了什么或将发生什么——无论其结果是成功、失败，还是两者的结合。一旦我们将重心转向交互，更宽广的视野便不可避免，从而倾向于关注广泛的综合因素，而非狭隘地局限于软件和硬件的功能特性。

![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/usable_systems_boat_alone.jpg)
作者/版权持有者：未知（待调查）。版权条款与许可：

未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。
![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/usable_systems_multible_boats.jpg)
作者/版权持有者：未知（待调查）。版权条款与许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 15.8 A-B**：什么是可航行的：是一艘单独的船，还是在特定海况下由船员操纵的船？对于可用系统（Usable Systems）也存在类似的问题。

20 世纪 80 年代可用性（Usability）研究中的许多最初关注点，在今天看来与 30 年前一样具有价值。改变的是，我们不再期望可用性成为交互系统（Interactive Systems）成功中唯一或主导的人因（Human Factor）。没有改变的是，关于可用性定义可能存在的混淆——这种混淆自人机交互（HCI）诞生之初就一直存在，即：究竟是软件本身可用，还是软件的使用过程可用。虽然这看起来像是无关紧要的哲学上的钻牛角尖，但它对可用性评估（Usability Evaluation）具有重大影响。如果软件可以具有内在的可用性，那么可用性就可以仅通过直接检查（Direct Inspection）来评估。如果可用性只能通过考虑实际使用情况来确定，那么就必须使用间接检查方法（如走查法 Walkthroughs）或实证用户测试（Empirical User Testing）方法来进行评估。

### 15.2.4 可用性的未来：从理解张力到解决张力

“可用性（Usability）”这个词的形式暗示了一种需要*本质主义（essentialist）*立场的属性，即认为属性和特质是自然物体和人工物体固有的（在哲学中，这被称为本质主义或实体主义*本体论（ontology）*）。对可用性的字面理解要求交互式软件本身必须是可用的或不可用的。虽然一种更现实的理解将可用性视为交互使用（interactive use）的属性，而非仅是软件的属性，但讨论“使用”是否“可用”是没有意义的，就像讨论“进食”是否“可食用”一样没有意义。这就是为什么一些国际标准更倾向于使用*使用质量（quality in use）*这一术语，因为这为交互表现的各种可能质量开辟了空间，无论是在体验方面还是在达成目标方面。例如，一次交互可以是“成功的”、“有价值的”、“令人沮丧的”、“不愉快的”、“具有挑战性的”或“无效的”。

可用性的许多发展历程反映了狭义的软件视角与更广泛的系统边界社会技术视角（sociotechnical view）之间的张力（tension）。更抽象地说，这是实体（本质）与关系之间的张力，即交互式软件的*固有属性（inherent qualities）*与交互的*涌现属性（emergent qualities）*之间的张力。在哲学中，认为关系比事物本身更基础的立场构成了*关系本体论（relational ontology）*的特征。

本体论（Ontologies）是关于存在、生存和现实的理论。它们导致了对世界截然不同的理解。HCI 领域的技术专家和许多心理学家倾向于本质主义本体论（essentialist ontologies），并主要通过考虑用户界面（user interface）特性来提升可用性（usability）。而关注面更广的人文专家则大多倾向于关系本体论（relational ontologies），旨在理解情境因素（contextual factors）如何与用户界面特性相互作用，从而塑造体验和性能。每种本体论在 HCI 领域中都占据一定的地位。下文将依次对两者进行回顾，随后将简要回顾可用性评估方法。虽然这两种立场之间的紧张关系主导了可用性在理论和实践上的演进，但我们可以摆脱这一僵局。本文将提出一种摆脱可用性领域长期紧张关系的策略，并在结尾部分指出可用性在用户体验（user experience）框架下的未来方向。

## 15.3 软件开发中的可用性定位：准则（Guidelines）、启发式原则（Heuristics）、模式（Patterns）与 ISO 9126

### 15.3.1 可用用户界面指南（Guidelines for Usable User Interfaces）

许多早期的可用性（Usability）指南源自计算机科学家，例如来自 Carnegie Mellon University (CMU) 的 Fred Hansen 和当时就职于 University of California, San Francisco (UCSF) 的 Tony Wasserman。计算机科学深受数学的影响，在数学中，相似三角形或等边三角形等实体具有永恒且绝对的内在属性（intrinsic properties）。计算机科学家试图为计算机程序建立类似的固有属性，包括那些能够确保交互式软件可用性的属性。因此，早期的用户界面设计指南包含了一种以技术为中心（technocentric）的信念，即仅通过软件和硬件特性就能确保可用性。如果一个用户界面符合相关指南，那么它在本质上就是可用的，例如涵盖菜单选项的命名、排序和分组，输入类型的提示，[数据输入（data entry）](https://www.interaction-design.org/literature/topics/data-entry) 字段的输入格式和值范围，错误消息结构，响应时间以及撤销功能（undoing capabilities）。以下四个示例指南摘自 Smith and Mosier 在 1986 年受美国空军委托编写的汇编（Smith and Mosier 1986）：

**1.0/4 + 快速响应（Fast Response）**
确保计算机能够迅速响应数据输入操作，从而避免用户因计算机响应延迟而导致操作速度降低或被其节奏掌控；在正常运行情况下，显示反馈的延迟不应超过 0.2 秒。

**1.0/15 保持数据项简短**
对于编码数据（Coded data）、数字等，应保持数据输入项简短，使单个项目的长度不超过 5-7 个字符。

**1.0/16 + 长数据项的分段**
当必须输入较长的数据项时，应将其分为较短的符号组，以便于输入和显示。

**示例**
一个 10 位电话号码可以分为三组输入：NNN-NNN-NNNN。

**1.4/12 + 标记必填和选填数据字段**
在设计表单界面时，应清晰且一致地区分必填项（Required entry fields）和选填项（Optional entry fields）。

**图 15.9**：摘自 Smith 和 Mosier 1986 年指南集的四个示例准则

在上述指南发布 25 年后，许多当代的网站数据输入表单如果能遵循这些准则，其用户将从中受益。即便如此，虽然遵循准则可以极大地提高软件的可用性（Usability），但并不能以此作为保证。

![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/guidelines_for_designing_user_interface_software.jpg)

作者/版权持有者：Sidney L. Smith, Jane N. Mosier 以及 The MITRE Corporation。版权条款与许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 15.10**：本书包含的准则数量超乎想象

### 15.3.2 可管理的指导：可用用户界面的设计启发式（Design Heuristics）

我原本持有的 Smith 和 Mosier 指南的纸质副本占据了书架上 10 厘米的宝贵空间。它已有 25 年以上的历史，而我从未全部读完，而且大概永远也不会读完。那里的指南实在太多了，以至于阅读它们并不划算（相比之下，我过去读完了 Windows 和 Apple 用户界面的完整风格指南）。

指南集的臃肿并没有消除以技术为中心（technocentric）的可用性（usability）观点的吸引力。相反，Rolf Molich 和 Jakob Nielsen 将数百条指南浓缩成了十条[启发式（heuristics）](https://www.interaction-design.org/literature/topics/heuristics)。这些启发式在 *Heuristic Evaluation* (Nielsen 1994) 中被进一步评估和完善，这是一种通过检查软件功能以寻找潜在可用性问题的检查方法（inspection method）。启发式将来自 Smith 和 Mosier 等指南集中的详细指南进行了概括。其中许多具有以技术为中心的焦点，例如：

**系统状态的可见性（Visibility of system status）**
系统应始终通过在合理时间内提供适当的反馈，让用户了解当前发生了什么。

**用户控制和自由（User control and freedom）**
用户经常会误选系统功能，因此需要一个标记清晰的“紧急出口”，以便在无需经过冗长对话的情况下离开不想要的状态。支持撤销（undo）和重做（redo）。

**错误预防（Error prevention）**
即使

比起优秀的错误提示，更好的做法是通过细致的设计从根源上防止问题的发生。要么消除容易出错的条件，要么对其进行检查，并在用户执行操作前提供确认选项。

**识别而非回忆（Recognition rather than recall）**
通过使对象、操作和选项可见，最大限度地减轻用户的记忆负担。用户不应在对话的不同部分之间记忆信息。在适当的情况下，系统的使用说明应可见或易于检索。

**使用的灵活性与效率（Flexibility and efficiency of use）**
加速键（Accelerators）——虽然新手用户难以察觉——通常可以加快专家用户的交互速度，从而使系统能够同时满足初学者和经验丰富用户的需求。允许用户自定义高频操作。

**图 15.11**：最初由 Molich and Nielsen 1990 以及 Nielsen and Molich 1990 开发的启发式评估（Heuristics）示例。

启发式评估（Heuristic Evaluation）在 20 世纪 90 年代成为了最受欢迎的用户中心设计（user-centred design）方法，但随着人们逐渐脱离桌面应用程序，其地位有所下降。快速且粗略的用户测试（Quick and dirty user testing）很快就超过了启发式评估（可对比 Venturi et al. 2006 与 Rosenbaum et al. 2000 的调查）。

![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/two_hands_usability_figure.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：

未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。
**图 15.12**：来自 Nielsen 的每个数字对应一个启发式原则（Heuristic）

### 15.3.3 不可撼动的内在属性：模式与标准使可用性成为核心

在以用户为中心的设计（User-Centred Design）中，尽管人们开始远离以系统为中心的方法（System-centric approaches），但这并不意味着那些仅关注软件制品（Software artefacts）而几乎不关注实际使用的可用性（Usability）方法已经终结。这可能是由于可用性社区（现在称为用户体验 User Experience）与软件工程专业之间存在脱节。以系统为中心的可用性在用户界面模式语言（User Interface Pattern Languages）中依然很常见。例如，Jenifer Tidwell 提供的一个模式为当代网页设计师更新了 Smith 和 Mosier 的风格指南 ([designinginterfaces.com/Input_Prompt](http://designinginterfaces.com/Input_Prompt))。

**模式：输入提示（Input Prompt）**
![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/input_prompt.jpg)
使用提示词预填文本字段或下拉菜单，告知用户需要执行的操作或输入的内容。

**图 15.13**：来自 Jenifer Tidwell 的 *Designing Interfaces* 中的一个模式示例

1991 年关于《软件工程——产品质量》（*Software Engineering - Product Quality*）的 ISO 9126 标准深受计算机科学本质主义（Essentialist）偏好的影响，其中将可用性定义为：

> 一组[产品]属性，这些属性关系到一组明确或隐含的用户在使用时所需的努力，以及个人对该使用的评估。

这是本百科条目中给出的三个定义中的第一个。这里的属性被假定为软件产品的属性。

……是属性，而非用户交互属性。然而，人机交互（Human-Computer Interaction, HCI）领域所青睐的关系（情境）视角（relational (contextual) view）已逐渐占据主导地位。到 2001 年，ISO 9126 经过修订，将可用性（usability）定义为：

> (1’) 软件产品在指定条件下使用时，能够被用户理解、学习、使用且具有吸引力的能力

此次修订仍然以产品为中心（本质主义的，essentialist），但其中的“当……时”（when）子句通过隐式地承认使用情境（context of use，即“指定条件”）的影响，使 ISO 9126 摆脱了关于可用性的完全本质主义立场，因为这种影响超出了“一组明确或隐含的用户”。

为了使技术标准 ISO 9126 与人因工程（human factors）标准 ISO 9241（见下文）保持一致，ISO 9126 在 2004 年增加了一个关于*使用质量（quality in use）*的第四章节，这导致了软件工程师与人因专家之间的一种勉强的妥协。这种勉强的妥协一直持续，作为 ISO 9126 的替代标准，2011 年发布的 ISO 25010 依然维持着可用性的本质主义视角。在 ISO 25010 中，可用性既是一项内在产品质量特性（intrinsic product quality characteristic），又是使用质量的一个子集（包括有效性 effectiveness、效率 efficiency 和满意度 satisfaction）。作为 ISO 25010 中的一项产品特性，可用性具有以下内在子特性：

- 适当性（Appropriateness）
- 可识别性（Recognisability）
- 可学习性（Learnability）
- 可操作性（Operability，指产品或系统具有使其*易于*操作和控制的属性的程度——*强调为后加*）

- 用户错误保护（User error protection）
- 用户界面[美学](https://www.interaction-design.org/literature/topics/aesthetics)（User interface aesthetics）
- [可访问性](https://www.interaction-design.org/literature/topics/accessibility)（Accessibility）

因此，ISO 25010 必须包含一项注释，以揭示软件工程（software engineering）与人因工程（human factors）世界观之间的内部冲突：

> 可用性（Usability）既可以根据其子特性（subcharacteristics）作为一种产品质量特性（product quality characteristic）来定义或衡量，也可以通过使用质量（quality in use）的子集衡量指标来直接定义或衡量。

关于可学习性（learnability）和可访问性的注释也与之类似。在软件工程标准的领域中，一种数学世界观坚守着关于可用性的本质主义立场（essentialist position）。而在人机交互（Human-Computer Interaction, HCI）领域，上下文（context）已占据主导地位数十年，这种观点可能会让人觉得极其反直觉。

然而，尽管 HCI 对可用性持有基于上下文立场的、自然而然的多因素理解（multi-factorial understanding），但 HCI 的倡导者在面对糟糕的可用性而愤怒时，其矛头总是指向软件产品。尽管人们都知道用户、任务和上下文都会影响可用性，但为了提高可用性，通常认为只有硬件或软件才需要被更改，这实际上认同了 ISO 25010 中软件工程师的立场（即属性应使 *软件* *易于操作和控制*）。尽管 HCI 的世界观通常拒绝对可用性进行本质主义的单因解释（monocausal explanations），但当他们代表用户表达愤怒时，软件总是成为被指责的对象。

显然，这里的问题容易陈述，但难以剖析。ISO 25010 中的僵局表明，人机交互（Human-Computer Interaction, HCI）领域需要更加重视软件设计对可用性（Usability）的影响。如果用户、任务和情境（Contexts）不可更改，那么我们唯一能改变的就是硬件和/或软件。尽管设计师的经验和专业知识在以指南（Guidelines）、模式（Patterns）和启发式（Heuristics）形式表达时，在心理层面被边缘化了，但这些依然是实现可用性最佳实践（Best Practice）最关键的资源。在我们接下来的讨论中，当我们考虑 HCI 在可用性方面占据的主导情境地位时，应当牢记这一点。

## 15.4 将可用性置于交互之中：使用情境与 ISO 标准

国际标准内部的矛盾在 Nielsen 的启发式评估（Heuristics）中便可见一斑，这比 2004 年 ISO 9126 的折衷方案早了十多年。虽然前一节中的五个启发式示例侧重于软件属性，但其中一项启发式则关注设计与其使用情境（Context of Use）之间的关系 (Nielsen 1994)：

> 系统与现实世界的匹配
> 系统应使用用户的语言，采用用户熟悉的词汇、短语和概念，而非以系统为中心的术语。遵循现实世界的惯例，使信息以自然且符合逻辑的顺序呈现。

这种将可用性与“现实世界”联系起来的做法，在 ISO 9241-11 人因工程标准（Human Factors standard）中得到了更结构化的定义，该标准将可用性与使用情境联系在一起，定义为：

> 特定用户在特定使用情境中，为了实现特定目标而使用产品时所达到的有效性（Effectiveness）、效率（Efficiency）和满意度（Satisfaction）的程度。

这是本百科全书条目中提出的三个定义中的第二个。与最初及修订后的 ISO 9126 定义不同，该定义并非由软件工程师编写，而是由具有人机工程学（Ergonomics）、心理学及相关背景的人因专家编写。

ISO 9241-11 区分了*可用性*（Usability）的三个组成因素：有效性、效率和满意度。这些因素源于用户、目标、情境以及 [此处原文截断] 之间的多因素交互。

软件产品。可用性（Usability）并非一种特征、属性或质量，而是在一个多维空间（multi-dimensional space）中的一种*程度（extent）*。这种程度体现在人们使用软件产品实际上能达成什么，以及达成这些目标所付出的成本。从实际角度来看，任何关于可用性的判断都是一种整体评估（holistic assessment），它将多方面的质量特质综合成一个单一的判断。

这种单一的判断用途有限。出于实际目的，关注用户体验（User Experience）中独立的具体质量特质会更有用，即不同质量特质在多大程度上达到了*阈值（thresholds）*。例如，如果在正常的运行场景（operating contexts）中，关键任务无法在可接受的时间内完成，那么该软件产品可能被认为不可用。在这里，关注点将在于*效率（efficiency）*标准。在许多使用场景（usage contexts）中，时间是受限的。时间限制的依据差异很大，包括物理学（军事作战中的弹道学）、生理学（医疗创伤）、化学（过程控制）或社会契约（新闻编辑室的印刷/广播截止日期）。

*有效性（Effectiveness）*标准增加了质量阈值的复杂性。一个军事系统可能是高效的，但如果其使用导致了被委婉地称为“附带损伤（collateral damage）”的结果（包括“误伤（friendly fire）”错误），那么它就不是有效的。我们可以想象一种创伤复苏软件，它能够实现及时的响应，但却导致了可避免的“并发症（complications）”（另一个领域

（此处为委婉语）在患者病情稳定之后。过程控制系统（process control system）可能会支持及时的干预，但可能会导致浪费或环境破坏，从而限制操作员响应的有效性（effectiveness）。同样，新闻编辑室系统可能会支持内容的快速准备，但可能会阻碍高质量稿件的交付。

对于*满意度（satisfaction）*而言，使用过程在客观上可能是高效且有效的，但却可能导致不舒适的用户体验，从而引发高员工流失率（这在呼叫中心很常见）。同样，员工可能会非常喜欢一个华丽的多媒体消防安全培训课程，但与枯燥的图文说明版本相比，其有效性可能低得多（因此潜在地具有危险性）。

ISO 9241-11 的三个可用性（usability）因素最近在 ISO 25010 的使用质量（quality in use）因素中增加到了五个：
- 有效性（Effectiveness）
- 效率（Efficiency）
- 满意度（Satisfaction）
- 无风险性（Freedom from risk）
- 上下文覆盖范围（Context coverage）

这两个新增因素很有意思。*上下文覆盖范围（Context coverage）*是一个比上下文适配（contextual fit）以及 Nielsen (1994) 的*系统与现实世界匹配（Match between System and Real World）*启发式（heuristic）更广泛的概念。它将*指定用户（specified users）*和*指定目标（specified goals）*扩展到了使用上下文（context of use）的任何潜在方面。这应当包括所有与*无风险性（freedom from risk）*相关的因素，因此，看到该因素被给予特殊关注，而不是仅仅依赖于*有效性（effectiveness）*和*满意度（satisfaction）*，这一点很有趣。

在此开展工作。然而，ISO 25010 中的这类碎片化扩展（piecemeal extensions）引发了关于完整性（comprehensiveness）和侧重点（emphasis）的问题。例如，为什么像学习便捷性（ease of learning）这样的因素要么被忽视，要么被隐藏在效率（efficiency）或有效性（effectiveness）之中？

![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/iso_international_standards_organization_accessibility_discussion.jpg)
作者/版权持有者：ISO 和 Lionel Egger。版权条款和许可：保留所有权利。经许可转载。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”部分。

**图 15.14**：ISO 无障碍标准讨论

### 15.4.1 情境覆盖带来了复杂的设计议程

关于可用性的关系论立场（Relational positions）本质上比本质论立场（Essentialist positions）更为复杂。后者允许通过对交互系统进行*检查（inspected）*，基于其设计特征来评估其可用性潜力。本质论方法之所以具有吸引力，是因为评估可以完全依赖于指南（Guidelines）、模式（Patterns）以及类似的交互设计最佳实践。而关系论方法则需要一套更为复杂的协同方法。随着关系论立场的日益复杂（例如从 ISO 9241-11 向 ISO 25010 的演进），需要更广泛的评估方法。在关系论视角下，可用性是一系列复杂交互的结果，并体现在一系列使用因素（Usage factors）中。很难想象单一的评估方法如何能涵盖所有这些因素。无论这是否可行，目前尚不存在这样的一种方法。

关系论的可用性方法需要多种评估方法来确定其*程度（Extent）*。而“程度”引入了进一步的复杂性，因为所有识别出的可用性因素必须经过*测量（measured）*，随后必须判断所达到的程度是否充分。在这种情况下，可用性评估不再是简单的检查问题，而变成了一项复杂的组织运作（Logistical operation），其核心在于实施一项*设计议程（Design agenda）*。

*议程（Agenda）*是指待办事项清单。而*设计（Design）*

因此，议程（agenda）是一系列设计任务的清单，需要在一个整体的开发流程中进行管理。ISO 9241-11 中存在一个隐含的设计议程，它要求交互设计师为特定项目确定目标受益者（target beneficiaries）、使用目标（usage goals）以及效率（efficiency）、有效性（effectiveness）和满意度（satisfaction）的水平。只有这样，详细且稳健的可用性评估（usability evaluation）才成为可能。请注意，这适用于 ISO 9241-11 及其类似的评估哲学（evaluation philosophies），但不适用于某些会导致不同设计议程的其他设计哲学（例如 Sengers and Gaver 2006）。

因此，ISO 9241-11 评估议程中的一项关键任务是通过一套协调的指标（metrics）来衡量可用性的程度，这些指标通常将 [定量](https://www.interaction-design.org/literature/topics/quantitative-research)（quantitative）和 [定性](https://www.interaction-design.org/literature/topics/qualitative-research)（qualitative）测量方法相结合，且往往明显偏向其中一种。然而，测量方法仅能为评估提供可能。为了进行评估，测量方法需要配合目标（targets）一起使用。设定此类目标是 ISO 9241-11 评估议程中的另一项关键任务。这通常是通过使用通用的 *严重程度量表（severity scales）* 来实现的。为了使用这些资源，评估者需要将其置于特定的项目语境中进行解读。这表明，可复用（re-usable）的评估资源并非完整的可复用解决方案。工作是

需要将这些资源转化为可执行的评估任务（actionable evaluation tasks）。

例如，Chauncey Wilson 的问题严重程度量表（problem severity scale, Wilson 1999）中最严重的两个级别为：
- 级别 1 —— 灾难性错误（Catastrophic error），导致不可恢复的数据丢失或硬件/软件损坏。该问题可能会导致大规模故障，使许多人无法开展工作。性能极差，以至于系统无法实现业务目标。
- 级别 2 —— 严重问题（Severe problem），可能导致数据丢失。用户没有该问题的替代方案（workaround）。性能如此之差，以至于……被普遍认为是“糟糕透顶（pitiful）”的。

每个严重程度级别都需要回答关于具体衡量指标和上下文信息的问题，即：在特定的项目语境中，应如何解读以下表述：“许多人无法开展工作”、“无法实现业务目标”以及“性能被认为是糟糕透顶的”。这最高两个级别还需要关于软件产品的信息，例如：“数据丢失”、“硬件或软件损坏”以及“没有替代方案”。

Wilson 的另外三个较低级别的量表增加了如下考量因素：“浪费时间”、“错误率或学习率增加”以及“重要功能未按预期运行”。这些都设定了一套必须回答的问题设计议程（design agenda）。因此，为了得知性能是否被认为是“糟糕透顶”，我们需要选择衡量相关的主观判断（subjective judgments）。其他标准则更具挑战性，例如，我们如何知道时间是否被浪费了，

……还是业务目标无法实现？前者取决于价值观（values）。“浪费”时间（如同浪费金钱）这一概念在特定的文化语境中有所不同，且取决于使用新系统完成任务的预期时长，以及在学习和探索上可以投入多少时间。至于业务目标，例如，一家企业可能希望被视为具有社会和环境责任感，但并不期望公司每个系统的每一项功能都能支持这些目标。

一旦确定了严重性标准（severity criteria）的阈值，设计师如何或应当如何在效率（efficiency）、有效性（effectiveness）和满意度（satisfaction）等因素之间进行权衡，目前尚不明确。例如，即使用户的效率和有效性超过了目标值，他们可能仍然不满意；反之，即使其性能相对于设计目标而言并不足以支撑，他们也可能感到满意。因此，目标水平是对结果的解读及其应对方式起引导作用，而非决定性作用。

因此，可用性（usability）的本质主义方法（essentialist approach）与关系主义方法（relational approach）在方法要求上存在显著差异。为了基于任何关系主义立场（不仅限于 ISO 9241-11）进行高质量的评估，评估者必须能够针对特定的项目语境，对现有的可复用资源进行修改和组合。理想情况下，这些可复用资源应承担大部分工作，从而实现高效、有效且令人满意的可用性评估。如果这不能

在这种情况下，高质量的可用性评估（Usability Evaluation）将带来复杂的组织挑战（Logistical Challenges），需要评估者具备深厚的专业知识以及针对特定项目的资源。

![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/control_room_gauges.jpg)
作者/版权持有者：Simon Christen - iseemooi。版权条款和许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。

**图 15.15**：可用性的关系方法（Relational Approaches to Usability）需要多种衡量指标

## 15.5 可用性评估的发展：测试、建模与检查

可用性（Usability）是一个具有争议的历史术语，且难以被替代。用户体验（User Experience）专家必须提及可用性，因为它是 IT 领域中一个根深蒂固的概念。然而，在使用这个本质上存在缺陷的概念时，我们需要保持谨慎。软件本身并非“可用的”。相反，是*软件被使用*，而由此产生的用户体验是多种特性的复合体，这些特性由产品属性、用户属性以及更广泛的使用情境（Context of Use）共同塑造。

当然，关于定义的争论不一定会影响“现实世界”中的实践。常识可能会占据主导地位，并为那些可能仅仅是缺乏实际意义的语义干扰（Semantic Distractions）找到替代方案。然而，当我们审视可用性评估方法时，我们会发现，对可用性的不同概念化会导致对可用性好坏之*原因*的看法产生分歧。

本质主义可用性（Essentialist Usability）在因果上是*同质的（Homogeneous）*。这意味着影响用户绩效的所有原因都属于同一类型，即由技术决定。以系统为中心的检查方法（System-centred inspection methods）可以识别此类原因。

情境可用性（Contextual Usability）在因果上是*异质的（Heterogeneous）*。这意味着影响用户绩效的原因具有不同类型：一部分源于技术，一部分源于使用情境的某些方面，但大多数则源于两者之间的交互作用。若干评估及其他

可能需要一些方法来识别并关联一系列因果关系。

无论是哪种可用性范式（Usability Paradigm）（即本质主义 Essentialist 或关系主义 Relational），都尚未解决关于相关“影响（effects）”的问题，也就是说，什么才算作可用性良好或糟糕的证据，因此在这一方面缺乏足够的方法。本质主义的可用性可能极少关注其影响 (Lavery et al. 1997)：谁在乎糟糕的设计会对用户产生什么影响，设计糟糕本身就已经足够糟糕了！情境可用性（Contextual Usability）更加关注影响，但对于什么样的影响应被视为可用性糟糕的证据，目前尚未达成广泛共识。虽然有很多可以被视为证据的例子，但究竟哪些应该被视为证据，则取决于设计团队的判断。

一些方法可以预测影响。*GOMS* 模型（目标、操作、方法和选择规则，Goals, Operators, Methods, and Selection rules）可以预测专家无错任务完成时间（expert error free task completion time）的影响，这在某些项目场景中非常有用 (Card et al 1980, John and Kieras 1996)。例如，外部流程可能要求一项任务必须在最大时间限制内完成。如果预测的专家无错任务完成时间超过了这一限制，那么非专家且易出错的任务完成时间极有可能会更长。当车载系统等交互设备分散用户对主任务（如驾驶）的注意力时，时间预测就至关重要。近期的进展（如 CogTool, Bellamy et al. 2011）为实际的基于模型（model-based）的[方法]赋予了新的生命。

HCI 中的评估。目前，比 GOMS 更强大的模型正被集成到评估工具中（例如 Salvucci 2009）。

![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/texting_while_driving.jpg)
作者/版权持有者：Courtesy of Ed Brown。版权条款和许可：CC-Att-SA-2 (Creative Commons Attribution-ShareAlike 2.0 Unported)。

**图 15.16**：基于模型的方法（Model-Based methods）可以预测驾驶员被分心的时长以及更多其他信息。

因此，可用性（Usability）研究预计将涉及多种方法的混合使用。这种混合可以由方法之间的高层级区分来引导。评估方法可以是*分析性的*（analytical，基于对交互系统及其潜在交互的检查）或*经验性的*（empirical，基于实际使用数据）。一些分析性方法需要构建一个或多个模型。例如，GOMS 对软件与人类绩效（human performance）之间的关系进行建模。GOMS 中的软件属性都与用户输入方式相关，其抽象层级由低到高，从按键级（keystroke level）一直延伸到抽象命令结构（abstract command constructs）。系统动作与用户动作在任务模型（task models）中交织在一起，用以预测用户的方法（以及在按键级分析下的执行时间）。

### 15.5.1 分析性评估方法与实证评估方法及其混合使用

*分析性评估方法*（Analytical evaluation methods）可以是*以系统为中心的*（system-centred）（例如，启发式评估 Heuristic Evaluation）或*以交互为中心的*（interaction-centred）（例如，认知走查 Cognitive Walkthrough）。设计团队利用某种方法提供的资源（例如，启发式原则 heuristics），从可用性（usability）的角度来识别设计的强项和弱项。检查方法（Inspection methods）倾向于关注导致可用性良好或糟糕的*原因*（causes）。*以系统为中心*的检查方法仅关注软件和硬件特性中那些会促进或阻碍可用性的属性。*以交互为中心*的方法则关注两个或更多因果因素（即软件特性、用户特征、任务需求以及其他上下文因素 contextual factors）。

*实证评估方法*（Empirical evaluation methods）关注可用性良好或糟糕的证据，即软件、硬件、用户能力和使用环境等属性所产生的正向或负向*影响*（effects）。用户测试（User testing）是主要的以项目为中心的方法。它利用特定于项目的资源，如[测试任务](https://www.interaction-design.org/literature/topics/test)（test tasks）、用户以及测量工具，以揭示在使用过程中可能出现的可用性问题。此外，本质主义可用性（essentialist usability）可以使用实证实验来证明由用户界面组件（例如，手机上的文本输入）带来的卓越可用性，或用于优化调优参数（例如，窗口动画的时间）。

（如开启和关闭）。此类实验假设测试任务、测试用户和测试情境允许泛化（Generalisation）到其他用户、任务和情境中。这种假设很容易被打破，例如，当用户是非常年幼或年长的人，或者存在运动或感知障碍时。

分析法（Analytical methods）和实证法（Empirical methods）相继出现，其中实证法最早出现在 20 世纪 70 年代，形式为简化的心理学实验（例如，参见 *International Journal of Man-Machine Studies* 1969-79 年的早期卷册）。基于模型的方法（Model-based approaches）在 20 世纪 80 年代随之而来，但其中最实用的方法均是初始 GOMS 方法（John and Kieras 1996）的变体。无模型检查法（Model-free inspection methods）出现在 20 世纪 80 年代末，并在 90 年代初迅速演进。这些方法试图通过在多种资源上进行“折减”（*discounting*）来降低可用性评估（Usability evaluation）的成本，特别是用户（与用户测试不同，无需用户）、专业知识（通过启发式（Heuristics）/模型转移给新手）或详尽的模型（与 GOMS 不同，无需模型）。

![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/fajita_dinner_kit.jpg)
作者/版权持有者：Old El Paso。版权条款和许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因为无法获得许可）。请参阅“例外（Exceptions）”章节（及其子章节...）

"allRightsReserved-UsedWithoutPermission") 见 [版权声明 (copyright notice)](https://www.interaction-design.org/about/terms-of-use) 页面。

**图 15.17**：
鸡肉法希塔套装（Chicken Fajitas Kit）：除了鸡肉、洋葱、辣椒、食用油、刀具、切菜板、煎锅、炉灶等，它包含了你所需的一切。可用性评估方法（Usability Evaluation Methods）也非常相似——一旦你努力提供了所有缺失的部分，一切就都没问题了。

在多种评估方法的组合中实现平衡并非易事，且不仅仅是简单地将分析法（analytical methods）和经验法（empirical methods）结合在一起。这是因为可用性工作不仅仅是选择和使用方法。评估方法的完整程度就像一个“鸡肉法希塔套装”，其中包含的实际制作所需食材极少：没有鸡肉，没有洋葱，没有辣椒，没有食用油，没有用于削皮/去芯和切片的刀具，没有切菜板，没有煎锅，也没有炉灶等。同样地，已发表的用户测试（user testing）“方法”也缺失了同样至关重要的要素以及特定于项目的资源，例如：参与者招募标准（participant recruitment criteria）、筛选问卷（screening questionnaires）、知情同意书（consent forms）、测试任务选择标准（test task selection criteria）、测试前（及后）简报脚本（test (de)briefing scripts）、目标阈值（target thresholds），甚至包括数据收集工具（data collection instruments）、评估指标（evaluation measures）、数据整理格式（data collation formats）、数据分析方法（data analysis methods）或报告格式（reporting formats）。目前没有一种完整的、已发表的用户测试方法能让初学者直接拿来就用（"as is"）。所有的用户测试都需要大量的针对特定项目的规划。

以及实施。相反，许多可用性（Usability）工作侧重于针对特定项目的需求，对方法进行配置与组合。

### 15.5.2 唯一真正的方法是你亲自执行的方法

在规划可用性工作（Usability work）时，重要的是要认识到，所谓的“方法（Methods）”严格来说是资源的松散集合，更应被理解为“路径（Approaches）”。使可用性工作真正发挥作用需要投入大量精力，而且与所有基于知识的工作一样，如果不对基础底层概念有深刻的理解，就不能简单地从书中复制方法并直接应用。这里的一个关键结果是，在实证研究（Empirical studies）中，只能对方法的具体实例进行比较，因此无法设计出可靠的研究来收集关于不同可用性评估方法之间存在系统性可靠差异的证据。所有方法都有独特的使用场景，需要项目特定的资源，例如在用户测试（User testing）中，这些资源包括参与者招募、测试流程以及简报与事后访谈（(de-)briefings）。即使是更通用的资源，如问题提取方法（Problem extraction methods, Cockton and Lavery 1999），在不同的用户测试语境下也可能有所不同。这些因素不可避免地阻碍了可靠的比较。

![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/usability_cats_and_dogs_1.jpg)
作者/版权持有者：George Eastman House Collection。版权条款和许可：保留所有权利。经许可转载。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/usability_cats_and_dogs_0.jpg)
作者/版权持有者：George Eastman House Collection。版权条款与许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 15.18 A-B**：狗还是猫：哪种是更好的宠物？这完全取决于你比较的是什么样的猫和狗，以及你如何比较它们。评估方法（Evaluation methods）也是如此。

考虑一个关于启发式评估（Heuristic evaluation）与用户测试（User testing）的简单对比。为了确保公平比较（Fair comparison），需要投入大量的精力。例如，如果用户测试要求测试用户执行固定任务（Fixed tasks），那么启发式评估者也需要使用相同的任务来探索同一个系统。这两种方法的评估结果之间任何差异或相似之处都无法泛化（Generalise）到这些固定任务之外，而且评估者的专业知识（Expertise）和表现的个体差异也可能会产生广泛的评估效应（Evaluation effects）。如果在评估中没有指定任务，那么结果之间的差异和相似性是由所采用的方法引起的，还是由评估过程中未记录的任务引起的，将无法确定。考虑到为特定的用户测试配置资源所需的范围，它...

想要控制所有已知的潜在混淆变量（Confounds）简直是不可能的（更不用说所有目前未知的变量了）。如果没有这些控制，不同方法之间产生差异的主要原因可能是与实际可用性（Usability）无关的因素。

因此，在比较评估方法时，用户执行的任务（在用户测试 User testing 中）或评估者使用的任务（在评估检查 Inspections 或模型规范 Model specifications 中）是一个可能的混淆变量。评估指标（Evaluation measures）和目标阈值（Target thresholds）同样如此。任务执行时间（Time on task）是一个便捷的可用性指标，并且在某些使用场景下，可以设定有意义的目标。例如，对于超市结账，结账 10 辆典型购物车的代表性购物时间目标可以是 30 分钟。然而，在许多场景中，并不存在可以可靠使用的效率时间阈值（例如，起草并打印一页商业信函的时间，与根据纸质草稿或口述录入的时间相比）。

与设定阈值相关的问题，因选择需要设定阈值的指标而产生的问题而变得更加复杂。用户测试可以选择广泛的潜在指标。例如，1988 年，来自 Digital Equipment Corporation 和 IBM 的可用性专家 (Whiteside et al. 1988) 发布了一份详尽的可能评估指标清单，包括：

- 无量化指标的度量（Measure without measure）：评分的空间非常大
- 以下各项的计数（Counts of）：
  - 使用的命令数
  - 失败命令的重复次数

- 连续成功或失败的次数
  - 用户回忆起的功能优点与缺点
  - 未被调用的可用命令/退行性行为（Regressive Behaviours）
  - 用户更倾向于使用本系统
- 在特定时间段内完成任务的百分比
- 以下各项的数量或百分比：
  - 错误（Errors）
  - 在某项衡量指标上优于竞争对手的产品
- 以下各项的比率：
  - 成功与失败的比率
  - 正面评价与负面评价的比率
- 时间：
  - 完成任务所需时间
  - 在错误中花费的时间
  - 使用帮助或文档的时间
- 频率：
  - 使用帮助和文档的频率
  - 界面误导用户的频率
  - 用户需要采取规避方案（Work around）解决问题的频率
  - 用户工作任务被中断的频率
  - 用户失去系统控制权的频率
  - 用户表达沮丧或满意情绪的频率

作者并未声称该衡量指标完整列表涵盖了截至出版时 Digital Equipment Corporation 或 IBM 内部已知的所有指标。明确的一点是，项目团队必须选择自己的度量指标（Metrics）和阈值（Thresholds）。目前尚不存在能够可靠地支持此类选择的方法。

不存在适用于所有软件开发项目的通用可用性（Usability）衡量标准。有趣的是，Whiteside et al. (1988) 是第一篇将“情境设计（Contextual Design）”引入人机交互（HCI）社区的出版物。其核心观点是，现有的用户测试实践为设计带来的价值远低于情境研究（Contextual Research）。文中表达了一种希望，即一旦人们能更好地理解使用情境（Contexts of Use），并且

如果能证明情境洞察（contextual insights）可以为各种不同项目的成功设计提供指导，那么就能找到新的情境衡量指标（contextual measures），以便对用户体验（user experiences）进行更恰当的评估。在人机交互（HCI）研究和专业实践中，直到二十年后才出现了实现这一愿景的基础。本百科条目的最后几个章节将探讨可能的未来方向。

### 15.5.3 很抱歉让你失望，但是……

总结到目前为止的观点：

1. 关于可用性（Usability）的本质存在根本分歧，即：它要么是交互系统（Interactive systems）的内在属性（Inherent property），要么是使用过程中产生的涌现属性（Emergent property）。对于可用性“是什么”，没有单一且绝对的答案。只有那些拒绝以其他方式思考的人，才会认为可用性是所有交互式数字技术的内在可衡量属性。
2. 不存在通用的可用性衡量标准（Universal measures），也不存在一个固定的阈值（Fixed thresholds）来判定所有交互系统是否可用。不存在*通用*的、鲁棒的（Robust）、客观且可靠的指标（Metrics）。没有一种评估方法（Evaluation methods）能够明确地判定一个交互系统或设备是否可用，或者可用程度如何。这里的所有结论都涉及艰苦积累的专业知识、主观判断，以及超出所有记录在案的评估方法所能提供的项目特定资源。
3. 可用性工作过于复杂且具有项目特异性，无法采用可推广的方法（Generalisable methods）。所谓的“方法”在现实中更像是“路径”（Approaches），它们提供了一组松散的资源，需要根据具体项目进行调整和配置。不存在可靠的、预设的可用性评估方法。实际使用的每种方法都是独特的，且严重依赖于评估者的技能和知识，以及项目特定的资源。不存在现成的评估

方法。没有任何文献能完整地记录所有的评估方法和指标（metrics）。要在可用性度量（usability measurement）和评估方面培养专业能力，绝不仅仅是阅读相关方法、学习如何应用这些方法，并仅凭此就精通于判断一个交互系统或设备是否可用，以及在何种程度上可用。即便是以系统为中心的本质主义方法（system-centred essentialist methods），也会给评估者留下需要自行填补的空白 (Cockton et al. 2004, Cockton et al. 2012)。

上述内容应与开篇的四个命题进行对比，这四个命题共同构成了一种极具吸引力的观念，承诺无论评估者的经验和能力如何，都能获得确定性的结果。每个命题并非完全正确，且在很大程度上可能是错误的。评估绝不能成为软件开发项目的附加项（add-on）。相反，可用性工作的范围以及所采用的方法，需要与其他设计和开发活动共同规划。可用性评估需要支持资源，这些资源应是每个项目不可或缺的一部分，且必须在项目中同步开发。

可用性的本质主义（essentialist）与关系主义（relational）概念化之间的紧张关系，仅仅是可用性工作所面临挑战的冰山一角。不仅可用性的定义尚不明确（尽管存在多种相互竞争的定义），而且在具体项目的语境之外，具体应如何评估可用性也并不明确。在某种语境下至关重要的因素，在另一种语境下可能并不

……在另一个项目中至关重要。项目团队必须决定哪些因素至关重要。可用性（Usability）文献可以提供可能的可用性衡量指标，但没有一种是普遍适用的。可用性工作的现实情况是，每个项目都带来了独特的挑战，需要凭借经验和专业知识来应对。初级评估者不能简单地研究、选择并应用可用性评估方法。相反，实际采用的方法才是所有可用性工作最关键的*成果*（achievement）。

方法是在具体实践中基于每个项目的实际情况*构建*（made）出来的。它们并非以“即拿即用”的形式存档在学术或专业文献中。相反，存在两个起点。首先，关于一系列方法的文献为评估者提供了一些可复用的资源，但在将其实践方法化之前，还需要结合项目语境提供额外的信息和判断。其次，存在针对特定项目可用性工作的详细案例研究（Case studies）。在这种情况下，评估者的挑战在于识别案例研究中的资源和实践，并判断其是否与其他项目语境相契合。例如，用户测试案例研究中的参与者招募流程可能在其他项目中可复用，尽管可能需要进行某些修改。

读者可能会根据上述内容得出结论，认为可用性在原则上是一个吸引人的想法，但在现实中缺乏实质内容。然而，现实情况是我们依然在不断经历挫败感……

在使用交互式数字技术时，我们经常会觉得它们难以使用。尽管如此，令人沮丧的用户体验（User Experiences）可能并非源于某个被称为“可用性（Usability）”的单一抽象概念，而是人、技术与使用情境（Usage Contexts）之间独特的复杂交互作用的结果。此处的交互因素必须被综合考虑。我们无法仅凭孤立的使用困难、用户不适或不满来判定其严重程度。对交互软件质量的整体评价，必须在通过使用它所能实现的成果与使用成本之间取得平衡。没有任何一项成功的数字技术是没有在某些 HCI 专家看来属于“可用性缺陷”的问题的（我*总是*能发现一些！）。某些技术看似存在严重的缺陷，但对许多用户而言却极其成功。理解其中的原因能为我们提供深刻的见解，使我们在交互设计（Interaction Design）中不再仅仅将重点放在可用性上。

## 15.6 有价值的可用性（Worthwhile Usability）：可用性何时重要、为何重要以及重要程度如何

在编写前一节时，我通过 Facebook 寻求关于将联系人从我的旧款 Nokia N96 手机转移到新 iPhone 的建议。其中一条建议被证明仅适用于 Apple 电脑，但对于 Wintel PC 来说也部分正确。最终，我找到了一条可行的数据路径，其步骤包括：在目前的笔记本电脑上安装 Nokia PC 套件，将联系人从旧手机备份到笔记本电脑，下载一个能将联系人从 Nokia 的专有备份格式（proprietary backup format）转换为适用于电子表格/数据库的文本格式（即逗号分隔值 .csv）的免费软件，尝试将其导入云服务（但失败了），（在对电子表格进行编辑后）将其导入笔记本电脑上的 Windows 地址簿，最后通过 iTunes 将联系人同步到我的新 iPhone 中。

### 15.6.1 一个极低频的多设备日常可用性案例

从开始到结束，我的电话号码迁移任务花费了两个半小时。只有不到一半的联系人成功迁移，且由于电子表格编辑的问题，我不得不以一种需要在 iPhone 或 Windows 联系人文件夹中进一步编辑的形式来迁移联系人。

聚焦于 ISO 9241-11 对可用性（Usability）的定义，对于一个涉及社交网络、云计算资源、网页搜索、两个组件产品服务系统（Product-Service System, PSS）（Nokia 96 + Nokia PC Suite, iPhone + iTunes）以及 Windows 笔记本实用程序的复杂临时综合产品服务系统，我们可以对其可用性做出怎样的评价？

![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/two_mobiles_and_a_computer.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

**图 15.19**：两部手机与若干软件实用程序的故事

花费 2.5 小时来完成这项任务高效吗？以下各项任务大约各花费了 30 分钟：

1. 网页搜索、阅读可能的解决方案以及下载免费软件（Freeware）。
2. 安装手机软件（因为我买了 Nokia，所以使用了新笔记本电脑）、尝试将 Nokia 连接到笔记本电脑、重启笔记本电脑、成功备份、使用免费软件将其提取为 .csv 格式。

1. 探索一项云端电子邮件联系人服务，但上传失败。
1. 测试上传至 Windows 地址簿，通过编辑以优化导入，电话号码编辑失败，最终成功导入。
1. iPhone 与 iTunes 的同步（Synchronisation）。

为了对效率（Efficiency）做出判断，我们首先需要记住，在等待期间（上传、下载、同步、安装），我校对了本条目的当前草稿并进行了修改。无论如何，这本来就需要花费 30 分钟。其次，我通过网络搜索找到了有用的信息，从而引导我找到了最终的解决方案。第三，我必须学习如何使用 iTunes 针对 iPhone 的同步功能，这花费了大约 10 分钟，是对未来的必要投资。然而，我在 Facebook 推荐的一个云计算（Cloud Computing）方案上浪费了至少 30 分钟（在尝试从 .csv 文件上传失败之前，我必须先将电子邮件添加到该云服务中）。这里存在明显的可用性（Usability）问题，因为该电子邮件服务没有就联系人上传失败的原因提供任何反馈（Feedback）。在 2011 年，如此糟糕的交互设计（Interaction Design）是不可原谅的，这迫使我尝试了多次才意识到它无法运行，至少对我所拥有的数据而言如此。此外，提取的电话号码带有文本前缀，但在电子表格中进行全局搜索和替换导致了无法解决的数据格式问题。我将这两者都视为可用性

存在两个问题，一个源于提取出的电话号码格式，另一个则源于某知名电子表格软件的异常行为。

我尚未回答这一过程是否符合 ISO 9241-11 标准中的效率（Efficiency）定义。我不得不得出结论：它并不高效，但这在一定程度上是因为我对协调复杂的设备与软件工具组合缺乏相关知识。然而，在联系人仅存储在手机 SIM 卡的时代，在手机店完成迁移仅需几分钟。因此，目前的可用性（Usability）问题源于联系人存储方式的转变——即从 SIM 卡转向更全面且独立于 SIM 卡的存储格式。尽管过去存在更高效的选择，但如今大多数人都使用功能更全面的手机内存联系人，因此之前的快速方案是以牺牲最原始的联系人格式为代价的。所以，虽然该活动相对低效，但可能存在相应的补偿性原因。

真正意义上的可用性问题仅涉及云端电子邮件功能的反馈缺失、提取的电话号码格式以及电子表格软件的异常行为。然而，我是在收到 Facebook 上的建议后才尝试云端电子邮件选项的。我对该问题的体验具有高度的情境性（Contextual）。至于另外两个问题，如果第二个问题不存在，我就永远不会遇到第三个问题。

存在明显的...问题

效率（Efficiency）。在最理想的情况下，如果扣除交错工作（interleaved work）和许多有价值的可复用学习成果（re-usable learning），这所花费的时间仍是应有时间的两倍。然而，在我工作的复杂社会塑造语境（socially shaped context）中，很难精准地指出导致这种低效率的原因。

有效性（Effectiveness）则很容易评估。我仅迁移了不到 50% 的联系人。请注意，与涉及复杂产品服务系统（product-service system）的效率分析相比，这里的分析是多么简单直接。

综合来看，你可能会惊讶地发现，我对此相当满意。接近 50% 总比没有好。我第一次学会了如何通过 iTunes 同步我的 iPhone。我也利用等待的时间编辑了这篇百科条目（encyclopaedia entry）。但我绝非感到 *愉快*，我对电话号码格式、难以捉摸的电子表格行为，以及某前三大免费电子邮件服务中那个毫无响应的导入功能依然感到不满。

### 15.6.2 故事的寓意是：权衡之后，这是值得的

我们在这里可以得出怎样的总体判断？从二元（binary）的角度来看，我最终选择的数据路径是可用的（usable）。而一条被放弃的路径则不可用，因此在我尝试转移电话号码的过程中，确实遇到了一个不可用的组件。至于更实际的可用性程度（extent of usability），而非简单的二元可用与不可用之分，我们必须在效率（efficiency）、有效性（effectiveness）和满意度（satisfaction）等因素之间进行权衡。我可以将最终的数据路径评为 60% 的可用性，因为有效的价值学习抵消了丢失一半以上联系人这一低效结果（我随后不得不手动输入这些联系人）。如果加上这个案例为本百科条目带来的价值，我可以将其大幅提升至 150%！这揭示了评估涉及多个设备和实用程序（utilities）的交互可用性的复杂性。描述使用过程很简单，但判断其质量却并非易事。

因此，糟糕的可用性依然存在，但它最常出现在我们尝试在一个复合的、临时的（ad-hoc）产品服务系统（product-service system）中协调多个数字设备时。Forlizzi (2008) 等人将这些如今典型的使用情境称为产品生态学（product ecologies），尽管有些人（例如 Harper et al. 2008）更倾向于使用产品生态系统（product ecosystems）或产品服务生态系统（product-service ecosystems）这一术语（生态学是研究生态系统的学科，而非系统本身）。

那些单独使用时足够好用的组件，在组合使用时可用性却降低了。在这种情况下，关于可用性（Usability）的本质主义（Essentialist）立场变得完全难以成立，因为电话格式可能会归咎于古怪的电子表格，反之亦然。低可用性的影响是显而易见的，但其原因却不明确。最终，在这种环境下，可用性的程度及其原因，取决于基于所获价值与所付成本之判断的解释（Interpretation）。

将可用性视为一个“解释问题”远非陷入僵局，反而为评估用户体验（User Experiences）开辟了一条前进之路。我们能够对效率（Efficiency）、有效性（Effectiveness）和满意度（Satisfaction）做出稳健的解释，并为评估这些因素之间如何权衡（Trade-off）而建立稳健的基础。对许多人来说，这些基础看起来是主观的，但这并不是问题，或者至少比起错误地假设我们拥有某种通用且普适的客观标准来衡量任何交互系统（Interactive System）中可用性的存在与否或程度，这个问题要小得多。继续追求此类标准绝对是低效且无效的，即便对 17 世纪科学价值观的坚守能带来某种程度的个人（主观）满足感。

正是低可用性（Poor Usability）吸引了 20 世纪 80 年代人机交互（HCI）领域的关注。当时对于什么是“良好”的可用性并没有一个积极的定义。低可用性可能会降低甚至破坏预期的

交互系统的价值。然而，良好的可用性（Usability）无法在设计团队预设的价值之外*额外提供*价值。可用性评估方法侧重于发现问题，而非寻找成功之处（认知走查 [Cognitive Walkthrough] 除外）。尽管如此，经验丰富的可用性从业者知道，评估报告应首先赞赏设计的优点，但这些优点并非可用性方法旨在检测的重点。

现实且相关的评估必须衡量*产生成本（Incurred costs）*与*获得收益（Achieved benefits）*之间的关系。在不同手机之间传输联系人时，我遇到了以下问题及相关成本：

1. 尽管尝试了多次，仍无法将联系人上传到云端电子邮件系统（成本：浪费 30 分钟）。
2. 无法理解为何无法将联系人上传到云端电子邮件系统（成本：长期的挫败感、烦躁、轻微愤怒，以及对同事公司的抱怨）。
3. 第一次无法从 Nokia 手机启动数据传输，需要按照 Nokia 诊断程序的建议进行尝试并重启笔记本电脑（成本：浪费 15 分钟）。
4. 超过一半的联系人未能传输（未来成本：根据是使用笔记本电脑还是 iPhone，需要额外花费 30-60 分钟输入号码，此外还包括已花费的 15 分钟用于查找和记录缺失的联系人）。
5. 在电子表格中删除电话号码的类型前缀（例如 TEL CELL）导致号码被不可逆地转换为科学计数法格式（Scientific format number）（成本：浪费 10 分钟，以及未来的成本...

……在手机中编辑号码的额外 30-60 分钟，困惑、恼怒、轻微的愤怒，以及对同事公司的辱骂 #2）
1. 必须设置一系列复杂的同步设置（synchronisation settings）以将同步范围限制在联系人（耗时额外 10 分钟，最初感到失望和焦虑）
1. （这次）无法将任何问题归咎于 Windows！

通过列出上述清单，我在一定程度上对什么是「糟糕的可用性（poor usability）」采取了某种立场。为了判断这些成本是否*值得*，我还需要对积极的结果和体验采取立场：
1. 有机会向 Facebook 朋友寻求并获得帮助（实现了现有社会资本（social capital）的部分价值）
1. 通过现有的云计算（cloud computing）账户获得了一个新的电子邮件地址 gilbertcockton@...（当时尚不清楚其未来价值，但后来证明很有用）
1. 发现了一条半有效的数据路径（data path），将我近一半的联系人传输到了 iPhone（节省了 30-60 分钟的手动输入时间，且为未来的问题解决提供了潜在的可复用知识）
1. 了解了一种糟糕的电子表格行为（spreadsheet behaviour），除非我找出如何避免它，否则未来可能会产生问题（未来价值可能为零）
1. 了解了 Windows 地址簿以及如何将新联系人作为 .csv 文件上传（未来价值极高——至少 PC 端的编辑/更新比 iPhone 更快，且能非常方便地从网页和电子邮件中复制粘贴）
1. 学习了如何通过 iTunes 将我的新 iPhone 与笔记本电脑同步（广泛的

不可否认的未来价值，在编辑本条目期间反复得到验证，包括轻松扩展到我最近新买的 iPad)
1. 校对本条目前一草稿并编辑下一版本的时间（在安装、重启和上传过程中进行了 30 分钟的有效工作）
1. 为本百科全书条目寻找了主要的详细示例（希望对于作为读者的你来说，它与对于作为作者的我一样有价值：我发现它确实非常有帮助）

在许多方面，关于组合设备和实用工具是否“可用（usable）”的问题几乎没有价值，任何关于其组合可用性（usability）程度的问题也是如此。一个更有意义的问题是，这种交互是否“值得（worthwhile）”，即：所获得的最终收益是否足以抵消所付出的成本？“Worth”是一个非常有用的英文单词，它捕捉了成本与收益之间的关系：所获得的“收益（benefits）”是否（不）“值得（worth）”所承担的“成本（costs）”。“Worth”将正向价值与负向价值联系起来，考虑两者的平衡，而不是像在可用性差的情况下那样，主要或完全关注负面因素。

![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/usability_ruling.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”部分。

**图 15.20**：可用性裁决：无罪

因此，

我所获得的收益是否证明了我付出的成本是合理的？我的答案是肯定的，这就是为什么我当时感到满意，而现在随着挫败感的消退和潜在未来价值的稳步实现，我感到更加满意。

考虑到遇到的两三个可用性问题（Usability problems）及其相关成本，很明显，这次交互本可以更有价值（即以更低的成本获得更高的价值），但这种立场比孤立地决定可用性问题的程度和严重性要更加明确。如果没有可用性问题，这次交互会更有价值（但那样我就没有这个例子了）。如果我预先知道如何从 Nokia 备份文件中提取联系人，并将其转换为可以上传到 Windows 联系人地址簿的格式，那么这次交互也会更有价值。更理想的情况是，手机自带的工具软件套装（Utility suite）如果具备 .cvs 文件的导入/导出功能会更好。也许最好的解决方案是让手机支持 Windows 直接从中导入联系人。此外，如果我使用之前的笔记本电脑，所需的手机工具软件套装已经安装好了，应该不会出现初始连接问题。因此，存在一些降低成本并增加价值的方法，这些方法不需要对我使用的软件进行修改，而是用*一个简单的专用工具（Purpose-built tool）*来替代它们。这样一来，之前经历的可用性问题一个都没有被解决。

在意识到所需数据路径（Data path）的复杂性后，显然最理想的做法是对其进行彻底的重构（Re-engineer）。在这种情况下，彻底推翻重来比循序渐进的[迭代（Iteration）](https://www.interaction-design.org/literature/topics/design-iteration)更为有效。

![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/the_big_picture_in_usability.jpg)
作者/版权持有者：未知（待调查）。版权条款与许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

**图 15.21**：归根结底，你必须审视全局（Big picture）

### 15.6.3 可用性（Usability）只是交互设计（Interaction Design）宏大图景的一部分

通过将可用性置于体验（Experience）和结果（Outcomes）更广泛的语境中来考虑，许多与孤立地看待可用性相关的困境便会消失。这一点可以推广到整个以人为中心的设计（Human-Centred Design, HCD）。IDEO 的 CEO Tim Brown 在其著作 *Change by Design* 中，为多学科设计团队的以人为中心实践提供了极具说服力的论证。即便如此，他也承认，目前仍缺乏能够充分证明以人为中心的设计对[创新（Innovation）](https://www.interaction-design.org/literature/topics/innovation)至关重要的、真正具有说服力的故事，因为人们经常克服不便的例子削弱了这些论点（Brown 2009, pp.39-40），正如我上文所补充的。

通过将自行车锁在公园长椅上等例子，Brown 阐述了“实践中的价值（Worth in Action）”：收益（自行车的安全性）证明了成本（寻找附近合适的固定结构进行锁止）的合理性。可用性评估（Usability Evaluations）的问题在于，它们通常关注所产生的成本，而缺乏对所获收益的平衡关注。Brown 在最后一章中回到了平衡问题，他认为[设计思维（Design Thinking）](https://www.interaction-design.org/literature/topics/design-thinking)通过其综合特性（Integrative Nature）实现了这种平衡（p.229）。

以人为中心对设计的贡献仅是一组输入。设计的成功

取决于所有输入端的有效整合。卓越的设计总是能超越预期，为用户、所有者或赞助者提供远超其预期的价值。因此，最优秀的设计应该是平衡的（Balanced）、整合的（Integrative）且慷慨的（Generous）——简称为 **BIG**。在这里，可用性（Usability）需要融入这个大局之中。

可用性评估（Usability evaluation）能够发现使用问题。在提出可能的解决方案之前，需要将这些问题置于完整的设计语境（Design context）中进行整体性的理解。可用性评估不能孤立地运作，至少在不将可用性功能孤立化的情况下不能如此。自 90 年代初以来，可用性专家拥有多种可借鉴的方法，一旦经过适当的适配、配置和组合，这些方法可以为交互设计（Interaction designs）的迭代开发提供极具价值的输入。然而，我们仍然会遇到交互设计的缺陷，例如针对错误和问题缺乏具有指导意义且可操作的反馈（Actionable feedback），而这些缺陷是可以且应当被消除的。然而，恰当地利用可用性专业知识仅是答案的一部分。一个完整的解决方案需要将使用评估更好地整合到其他设计活动中。如果缺乏这种整合，在某些技术开发环境中，可用性实践将继续经常面临失望、不信任、怀疑以及缺乏认可的情况 (Iivari 2005)。

这为我们引入可用性的第三种替代定义奠定了基础，该定义在本质主义（Essentialism）与关系主义（Relationalism）之间寻求一种折中方案：

**“可用性（Usability）是指负面用户体验和负面结果对交互系统可实现价值（achievable worth）的影响程度。一个可用的系统不会通过过度或难以承受的使用成本（usage costs）来降低或破坏可实现的价值。”**

因此，可用性可以被理解为用户体验（user experience）的一个主要方面，它可能通过不利的使用成本降低已实现价值（achieved worth），但只能通过迭代地消除可用性问题来增加已实现价值。可用性的提升能够降低使用成本，但不能增加使用体验或结果的价值。在这个意义上，可用性与 Herzberg (Herzberg 1966) 提出的*保健因素（hygiene factors）*相对于其*激励因素（motivator factors）*具有相同的结构位置。

### 15.6.4 从保健因素到激励因素

![](https://public-media.interaction-design.org/images/encyclopedia/usability_evaluation/usability_evaluation_as_washing_hands.jpg)
Author/Copyright holder: Courtesy of Office for Emergency Management. U.S. Office of War Information. Domestic Operations Branch. Bureau of Special Services. 
Copyright terms and licence: pd (Public Domain (information that is common property and contains no original authorship)).
**图 15.22**：可用性（Usability）是一个负面的保健因素，而非正面的激励因素

Herzberg 研究了工作中的激励机制，并将职场中的正面“激励因素（Motivators）”与负面“保健因素（Hygiene factors）”区分开来。在工作中获得公开且持续的认可是一个激励因素的例子，而薪资不足则是一个保健因素的例子。激励因素能够带来工作满意度，而保健因素则可能导致不满。虽然该理论因这两组因素而被称作 Herzberg 的双因素理论（Two-factor theory），但它涵盖了三种效价（Valences）：正向、中性和负向。激励因素的缺失并不会导致不满，而会导致（中性的）既无满意也无不满的状态。同样地，负面保健因素的缺失并不会带来满意，而会导致（中性的）既无满意也无不满的状态。因此，失去正面的激励因素会导致不满意，而失去负面的保健因素则会导致...

……不再感到不满！因此，可用性（Usability）可以被视为用户体验（User Experience）中“保健因素（Hygiene factors）”的一个统称。关注并解决糟糕的可用性可以消除负面的、降低积极性的保健因素，但它无法引入正向激励因素（Positive motivators）。

正向激励因素可以被视为用户体验中与糟糕可用性相对立的另一极。糟糕的可用性会降低积极性，但良好的可用性并不能产生激励作用，只有正向的体验和结果才能做到这一点。将可用性孤立地看待而脱离其他设计考量，其问题在于它仅支持缺陷的识别与修正，而不能支持正向特质（Positive qualities）的识别与创造。在商业层面，糟糕的可用性会使产品或服务失去竞争力，但可用性只能使其相对于那些价值相当但可用性更差的产品或服务具有竞争力。从战略角度来看，在竞争对手的产品或服务整体可用性都已达到“足够好（good enough）”的任何市场中，提升价值比降低使用成本（Usage costs）是一个更好的方案。
