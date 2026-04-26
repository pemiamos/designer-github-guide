# 14. 上下文感知计算 (Context-Aware Computing)

**来源**：The Encyclopedia of Human-Computer Interaction, 2nd Ed.
**Notion 原页面**：https://www.notion.so/6840a26311fa49f2ab10c6ccc401d5e1

---

[Albrecht Schmidt](https://www.interaction-design.org/literature/author/albrecht-schmidt)
平板电脑自动切换屏幕方向、地图根据用户的当前方向进行调整并根据当前速度适配缩放级别，以及在黑暗环境下使用手机时自动开启背光，这些都是计算机能够感知其环境及其使用上下文（Context of Use）的例子。在不到 10 年前，此类功能并不常见，仅存在于从事[上下文感知计算（Context-Aware Computing）](https://www.interaction-design.org/literature/topics/context-aware-computing)研究的实验室原型设备中。

![](https://public-media.interaction-design.org/images/encyclopedia/context-aware_computing/ipad-orientation.jpg)
*作者/版权持有者：SermonAudio.com。版权条款与许可：保留所有权利。经许可转载。请参阅下文[*版权条款*](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。*

**图 14.1**：一台自动切换屏幕方向的 iPad 是上下文感知计算的一个典型例子

## 14.1 引言（Introduction）

当我们旨在创建*易于使用*的应用程序、设备和系统时，理解*使用情境（context of use）*至关重要。借助情境感知计算（context-aware computing），我们现在不仅可以在[设计流程（design process）](https://www.interaction-design.org/literature/topics/design-process)中，而且可以在设备使用时的实时状态下考虑使用场景（situation of use）。在人机交互（Human-Computer Interaction, HCI）领域，我们传统上旨在理解用户和使用情境，并创建能够支持主要预期使用案例（use cases）和使用场景的设计。另一方面，在情境感知计算中，对情境的利用带来了根本性的变化：我们可以支持多个同样最优的使用情境。在运行时（runtime）——即用户与应用程序交互时——系统可以判定当前的使用情境，并提供一个专门针对该情境而优化的[用户界面（user interface）](https://www.interaction-design.org/literature/topics/ui-design)。随着情境感知能力的引入，用户界面的设计工作通常会变得更加复杂，因为系统将被用于的场景和情境数量通常会增加。与传统系统不同，我们不再是为单一的或有限的一组[使用情境（contexts of use）](https://www.interaction-design.org/literature/topics/contexts-of-use)而设计；相反，我们要为多种情境进行设计。这种方法的优势在于

我们可以为一系列情境（Contexts）提供优化的用户界面。

让我们假设这样一个例子：你被要求为一款腕表设计用户界面。在研究中你发现，人们会在室内和室外使用它，在黑暗中以及阳光下使用它，在奔向火车站赶车时以及在课堂上感到无聊时使用它。作为一个优秀的用户界面设计师，你会针对每种情况产生许多令人兴奋的界面创意：例如，当用户在奔向火车站赶车时，用户界面应以极大的字体显示时间，并突出显示分钟和秒数。另一方面，当用户在听课时，用户界面应以极小的字体显示时间，并额外提供一句幽默的语录。

在传统的设计流程中，在完成草图和设计简报（Design Briefs）之后，你会意识到你必须决定使用哪一个界面创意。你会发现，在单一的设计中支持所有情境是不可行的。典型的结果是一个折中方案——而这往往会丧失你最初构思的那些创意的许多亮点。然而，如果你采用情境感知计算（Context-Aware Computing）的方法，你就可以创造一款情境感知腕表，将所有针对特定情境优化的设计整合到同一个设计中。如果你将腕表设计成能够识别每一种

根据你在初步研究中发现的情况（例如：奔向车站赶火车、听讲座等），你的手表可以根据识别出的上下文（Context）自动重新配置。图 2 展示了一个上下文感知（Context-aware）手表的设计草图。

![](https://public-media.interaction-design.org/images/encyclopedia/context-aware_computing/figure1a-context-aware-watch.jpg)

作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”章节。

**图 14.2**：展示在不同上下文中时间可视化（Time visualizations）构思的设计草图。左图：适用于奔向车站赶火车的用户，使其能够轻松查看分钟。中图：适用于枯燥的讲座和会议的时间可视化，显示距离结束的倒计时，以及一些能吸引用户关注的信息。右图：仅提供非常粗略的时间概念的可视化，类似于从太阳光线中获得的时间信息，例如在时间并不重要地与朋友闲逛时使用。通过上下文感知（Context-awareness），你可以创造一款结合了这三种可视化的产品，并根据识别出的上下文选择最合适的一种。该示例展示了上下文感知计算系统（context-aware computing systems）的巨大优势，因为设计自由度得到了提升，但与此同时，系统也变得更加复杂，且通常更难进行设计和实现。在本章中，我们将介绍创建上下文感知应用程序的基础知识，并探讨这些见解如何有助于构建更易用、更令人愉悦的[设计系统（design systems）](https://www.interaction-design.org/literature/topics/design-systems)。

作者/版权持有者：由 Albrecht Schmidt 提供。版权条款与许可：CC-Att-ND (Creative Commons Attribution-NoDerivs 3.0 Unported)。

什么是上下文（Context）？

作者/版权持有者：由 Albrecht Schmidt 提供。版权条款与许可：CC-Att-ND (Creative Commons Attribution-NoDerivs 3.0 Unported)。

建议、批评与商业价值

作者/版权持有者：由 Albrecht Schmidt 提供。版权条款与许可：CC-Att-ND (Creative Commons Attribution-NoDerivs 3.0 Unported)。

使用上下文感知计算设计产品的指南

作者/版权持有者：由 Albrecht Schmidt 提供。版权条款与许可：CC-Att-ND (Creative Commons Attribution-NoDerivs 3.0 Unported)。

# 上下文感知计算（Context Aware Computing）的当前挑战与未来

## 14.2 情境感知（Context-Awareness）

在计算技术的早期，系统被使用的情境（context）在很大程度上由计算机设置的地点决定，见图 3。个人计算机被用于办公环境或工厂车间。使用情境变化不大，且计算机周围的情况几乎没有差异。因此，当时不需要适应不同的环境。人机交互（Human-Computer Interaction, HCI）学科中的许多传统方法，例如情境访谈（contextual inquiry）或 [任务分析（task analysis）](https://www.interaction-design.org/literature/topics/task-analysis)，都起源于这一时期，并且在不经常变化的情况下最容易使用。随着移动计算机和普适计算（ubiquitous computing）的兴起，这种情况发生了改变。用户随身携带计算机并在许多不同的场景中使用它们，见图 4。

在 80 年代末和 90 年代的 [移动计算（mobile computing）](https://www.interaction-design.org/literature/topics/mobile-computing) 时代初期，核心主题是如何让移动性对用户而言是“透明”的（transparent），即在任何地方都能自动提供相同的服务。在这里，“透明”意味着用户无需关心环境的变化，并且无论环境如何，都可以依赖于相同的功能。

在 90 年代初，Xerox PARC 对普适计算的研究引起了思维方式的转变。除了使功能...

透明的（transparent），例如在整个校园内提供网络连接，而用户无需意识到不同网络之间的切换（hand-over），研究人员发现了利用使用情境（context of use）作为系统可适配资源的潜力。Bill Schilit 在其 1994 年发表于 Workshop on Mobile Computing Systems and Applications (WMCSA) 的论文中，引入了情境感知计算（context-aware computing）的概念，并将其描述如下：

> 这种情境感知软件能够根据使用位置、周围的人员、主机和可访问设备的集合，以及这些因素随时间的变化而进行适配。具备这些能力的系统可以检查计算环境并对环境的变化做出反应。
>
> —— Schilit et al 1994

其基本理念是，移动设备可以在不同的情境中提供不同的服务——而情境与设备的地理位置密切相关。

因此，情境感知计算的早期研究大多集中在*位置感知（location-aware）*系统上。从这个意义上说，如今汽车中广泛使用的卫星[导航（navigation）](https://www.interaction-design.org/literature/topics/navigation-1)系统就是情境感知系统。然而，正如我们在 (Schmidt et al 1999) 以及本章全文中所论证的，情境不仅仅是指位置。

![](https://public-media.interaction-design.org/images/encyclopedia/context-aware_computing/fig2a_context-awareness.jpg)
作者/版权持有者：Courtesy of Library of Virginia. Copyright

版权条款与许可：pd（公有领域（Public Domain），指属于公共财产且不包含原创作者权的信息）。
![](https://public-media.interaction-design.org/images/encyclopedia/context-aware_computing/fig2b_context-awareness.jpg)
作者/版权持有者：由 Library of Virginia 提供。版权条款与许可：pd（公有领域（Public Domain），指属于公共财产且不包含原创作者权的信息）。
![](https://public-media.interaction-design.org/images/encyclopedia/context-aware_computing/fig2c_context-awareness.jpg)
作者/版权持有者：由 The Library of the London School of Economics and Political Science 提供。版权条款与许可：pd（公有领域（Public Domain），指属于公共财产且不包含原创作者权的信息）。
**图 14.3 A-B-C**：在计算技术的早期阶段，上下文（Context）由计算机本身定义，因为计算机就是实际的工作场所。随后，计算机被安置在特定位置以辅助完成特定任务，因此上下文在很大程度上由计算机所在的地理位置决定。个人计算机（Personal computers）被应用于办公环境或工厂车间。
![](https://public-media.interaction-design.org/images/encyclopedia/context-aware_computing/fig3a_mobile_computing.jpg)
作者/版权持有者：未知（待核实）。版权条款与许可：未知（待核实）。请参阅下方[版权条款（copyright terms）](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

![](https://public-media.interaction-design.org/images/encyclopedia/context-aware_computing/fig3b_mobile_computing.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

**图 14.4 A-B**：即便在移动计算（Mobile Computing）的早期阶段（当时笔记本电脑被视为移动设备），用户也可以选择工作的情境（Context）。随着移动设备、手持计算机以及普适计算（Ubiquitous Computing）的兴起，这种情况发生了更剧烈的变化。用户随身携带计算机，并在现实世界的许多不同场景中使用它们。下次你散步时，观察一下大量的移动使用场景（Scenarios），你会惊讶于人们如何使用他们的设备。

### 14.2.1 示例 1：作为上下文感知系统的卫星导航 (SatNav)

在卫星导航系统（Satellite Navigation System, SatNav）中，当前位置是用于根据用户的当前位置自动调整可视化（Visualization，例如地图、箭头、方向等）的主要上下文参数（Contextual parameter）。图 5 展示了一个示例。然而，观察目前的商业系统可以发现，系统使用了更多的上下文信息（Context information），且许多可视化方式也发生了变化。除了当前的 [GPS](https://www.interaction-design.org/literature/topics/gps) 位置外，上下文参数还可能包括时间、光线条件、计算路线上的交通状况或用户的偏好地点。除了可视化和是否开启背光（Backlight）之外，计算出的路线也可能受到上下文的影响，例如在特定时间段避开可能拥堵的街道。

![](https://public-media.interaction-design.org/images/encyclopedia/context-aware_computing/fig4a_Nokia_N95_running_TomTom_Navigator.jpg)
作者/版权持有者：由 Eirik Solheim 提供。版权条款与许可：CC-Att-SA-2 (Creative Commons Attribution-ShareAlike 2.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/context-aware_computing/fig4b_google_maps_nokia.jpg)
作者/版权持有者：由 Satish Krishnamurthy 提供。版权条款与许可：CC-Att-2 (Creative Commons Attribution 2.0 Unported)。

**图 14.5 A-B**：导航设备已经变得

...很常见，且被汽车驾驶员和行人广泛使用。图 4a 展示了在 Nokia N95 设备上运行的 TomTom 导航应用程序。图 4B 展示了在另一台 Nokia 设备上运行的 Google Maps。卫星导航系统（SatNavs）可能是最广泛应用的上下文感知计算系统（Context-aware computing systems）。

### 14.2.2 示例 2：作为上下文感知系统的自动灯光

在房屋入口和酒店走廊，自动灯光已变得十分普遍。这些系统也可以被视为简单的上下文感知系统（Context-aware systems）。其中考虑的上下文参数（Contextual parameters）是当前的光照条件以及附近是否有动作。其适配机制（Adaptation mechanism）相当简单：如果检测到的情况是环境黑暗且有人在移动，灯光将被开启。只要人员在移动，灯光就会保持开启；在一段时间内未检测到动作后，灯光将再次关闭。同样，如果环境不再黑暗，灯光也会关闭。

这些简单的例子概述了上下文感知系统的基本原理。图 6 展示了上下文感知计算系统（Context-aware computing systems）的参考架构（Reference architecture）。传感器提供关于现实世界中活动和事件的数据。[感知（Perception）](https://www.interaction-design.org/literature/topics/perception)算法将对这些刺激进行解析，并将具体情况分类为上下文（Context）。系统将根据观察到的上下文触发相应的动作。

![](https://public-media.interaction-design.org/images/encyclopedia/context-aware_computing/fig5_reference_architecture_for_context-aware_computing_systems.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。见相关章节

下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“除外条款（Exceptions）”。

**图 14.6**：该图展示了一个上下文感知计算系统（Context-aware Computing Systems）的参考架构（Reference Architecture）。它假设通过传感器的数据采集（Data Acquisition）来支持多个应用程序的上下文行为（Contextual Behavior）。

## 14.3 上下文感知作为普适计算的赋能机制

上下文感知（Context-awareness）的概念与 Mark Weiser 在 *Scientific American* 杂志发表的开创性论文中提出的普适计算（Ubiquitous computing）愿景密切相关（见图 7）。随着计算机成为日常生活的一部分，其易用性变得至关重要。这一点在以下陈述中得到了强调：

> 最深刻的技术是那些消失的技术。它们将自身编织进日常生活的肌理之中，直到与生活融为一体。
>
> —— Weiser 1991

![](https://public-media.interaction-design.org/images/encyclopedia/context-aware_computing/fig6_Mark_weiser_ubiquitous_computing.jpg)
作者/版权持有者：Mark Weiser。版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面上的“例外”部分（以及“allRightsReserved-UsedWithoutPermission”小节）。

**图 14.7**：Mark Weiser 阐述了普适计算的愿景。上下文感知是实现这一愿景的核心基石。

许多人将计算技术达到这种集成程度视为计算机发展的最终目标。在这种情况下，技术将不再需要用户投入过多的主动注意力（Active attention），并且

能够让人一目了然地直接使用。如果实现了这一点，计算机就会“消失”——并非在技术层面，而是在心理层面。

> 从本质上讲，只有当事物以这种方式消失时，我们才能在无需思考的情况下自由地使用它们。
  - - Weiser 1991

为了实现具有最优[可用性（usability）](https://www.interaction-design.org/literature/topics/usability)（即*使用的透明性 (transparency of use)*）的普适计算（ubiquitous computing）系统，上下文感知行为（context-aware behaviour）被认为是关键的赋能因素。计算机已经渗透到我们的日常生活中——存在于手机、冰箱、电视、烤面包机、闹钟、手表等设备中——但要像 Weiser 的普适计算愿景那样完全“消失”，它们必须能够预判用户在特定情境下的需求，并主动采取行动以提供适当的帮助。这种能力需要一种感知周围环境的手段，即上下文感知（context-awareness）。

许多计算系统的实现程度极高，以至于用户甚至没有意识到自己与它们进行了交互。汽车就是一个典型的例子：防抱死制动系统（ABS, anti-lock braking system）和电子稳定程序（ESP, Electronic Stability Program）被集成在汽车中，并在极端情况下影响车辆的运行。尽管如此，大多数人在驾驶汽车时并不会有意识地想到这些技术。这些技术无处不在，并且已经从用户的意识中“消失”了。

## 14.4 情境（Context）的概念

“情境（context）”一词被广泛使用，且含义迥异。以下来自词典的定义及其同义词，为理解情境的含义提供了基础。

**情境（context），名词**。*事件的原因*
某事存在或发生时的状况，且该状况有助于对其进行解释。
*Cambridge Dictionary*

**情境的同义词：** circumstance（环境/情况）、situation（局面/处境）、phase（阶段）、position（位置）、posture（姿态）、attitude（态度）、place（地点）、point（观点/点）、terms（条件/条款）、regime（体制/政体）、footing（基础/立足点）、standing（地位）、status（状态）、occasion（场合）、surroundings（周围环境）、environment（环境）、location（位置）、dependence（依赖性）。

情境感知计算（Context-aware computing）的相关文献中，对于情境的定义和解释也多种多样。以下是几个突出的例子，体现了该学术社区共同的基础理解。

Kent 大学开展的一项研究探讨了配备 GPS（外接）、网络访问及其他传感器的移动设备如何支持移动办公人员（mobile workers）的实地调研（fieldwork）。研究团队提出了以下定义：

> ……「情境感知（context awareness）」，这是一个描述计算机感知其环境信息（如位置、时间、温度或用户身份）并据此采取行动的能力的术语。这些信息不仅可用于在实地收集信息时为其打标签（tag），还能实现选择性响应，例如触发警报或检索与当前任务相关的信息。
>
> —— Ryan et al 1998

![](https://public-media.interaction-design.org/images/encyclopedia/context-aware_computing/figure7_Lancaster_Castle_tourist_system.jpg)
作者/版权持有者：Courtesy of Tom Oates。版权条款与许可：CC-Att-SA-3 (Creative Commons Attribution-ShareAlike 3.0)。
**图 14.8**：Lancaster castle 是 GUIDE 旅游系统中所涵盖的地点之一。

Lancaster University 的 GUIDE 项目 (GUIDE 2001) 是首个用于探索旅游领域中上下文感知（Context-awareness）的大规模公共研究原型（Research prototype）部署。该项目重点研究如何利用上下文来改进面向 Lancaster 历史名城游客的移动信息系统（Mobile information system）。Keith Mitchell 在其基于 GUIDE 系统的论文中提出了如下关于上下文的概念：

> ……确定了两类上下文，即个人上下文（Personal context）和环境上下文（Environmental context）。……环境上下文的示例包括：时间、景点的开放时间以及当前的天气预报。
>
> —— Mitchell 2002

这种对上下文的理解将用户本身也视为上下文的一部分（例如：配置文件 Profiles、偏好 Preferences）。在技术实现上，GUIDE 采用了一种有趣的方法，它使用了一个修改后的浏览器（Modified browser），在后台利用上下文信息来适配内容和呈现方式。

Anind Dey 对构成上下文的定义给出了一个非常通用的描述：

> 上下文是指任何可以被用于

描述一个实体的状态。实体（Entity）是指被认为与用户和应用程序之间交互（Interaction）相关的个人、地点或对象，包括用户和应用程序本身。
  - - Dey 2000
![](https://public-media.interaction-design.org/images/encyclopedia/context-aware_computing/figure8a-menu-public-display.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。
**图 14.9**：这个传统的广告牌向所有路人展示相同的产品——自制汤配面包。在未来，此类广告牌将被数字屏幕取代，从而使内容能够适应当前的情境（Context）。如果您对公共显示网络（Public Display Networks）的未来愿景感兴趣，请访问 pd-net.org。在实际应用中，情境（Context）通常采用层级化结构来描述相关特征。Schmidt et al (1999) 所描述的特征空间（Feature space）便是这种情境结构化表示的一个典型示例（见图 10）。假设您希望设计一个数字化菜单，以替代餐厅入口处常见的实体菜单（示例见图 9）。如果这是一个非情境感知（Non context-aware）的版本，它通常仅显示当日特惠。相反，如果您将其设计为情境感知系统，则可以根据经过的人群在菜单上提供不同的建议。例如，当携带孩子的父母经过时，显示面向家庭的菜单；当一对情侣在傍晚观看时，显示烛光晚餐菜单；而如果在炎热晴朗的下午，则宣传冰淇淋系列。

该应用的特征空间可以包括：观看者、时间以及天气。其中，“观看者”可以进一步细分为人数、年龄和性别；“天气”则可包括温度以及是否下雨。通过构建这样一个结构化空间，能够更便捷地将现实世界中的情境与系统的适配（Adaptations）方案联系起来。请尝试为该菜单构建一个完整的特征空间，并定义相应的...

适配。即使是一个检查清单（checklist）也可以被视为非层级特征空间（non-hierarchical feature space）的一个非常简单的例子。

不存在一个完整且能描述所有可能选项的特征空间——事实上，这样的特征空间将是对世界进行完整描述的一种尝试。通常的做法是为所设计的特定上下文感知（context-aware）应用创建特征空间。特征空间的优势在于，通过观察一组参数，可以轻松地判断某种情境是否与某个上下文相匹配。

![](https://public-media.interaction-design.org/images/encyclopedia/context-aware_computing/figure9a-feature-space.jpg)
Author/Copyright holder: Unknown (pending investigation). Copyright terms and licence: Unknown (pending investigation). See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/about/terms-of-use) below.
**图 14.10**：上下文特征空间，详细说明了光线作为物理环境条件中的一项特征。

设计提示 1：在构建上下文感知系统时，首先应创建一个包含将影响系统行为之因素的（层级）特征空间。

在明确哪些因素应影响系统行为后，可以开始研究如何在设备中确定这些因素。在许多情况下，这将需要能够提供上下文信息的传感器（sensors）。

## 14.5 从传感器到上下文

上下文感知系统（Context-aware system）的最终目标是让系统获得一个与用户感知（Perception）接近的周围世界表征（Representation）。一个重要的问题是如何缩小用户与系统对现实世界的感知（或理解）之间的差距。对于位置信息，不同的传感（Sensing）手段（如 GPS）和解释（Interpretation）方式（如世界大地坐标系统 World Geodetic System, WSG84、邮政编码）已经非常成熟。然而，对于许多其他传感器而言，通常不存在一种单一且被广泛认可的传感信息解释方式。

用户对周围环境的感知基于人类的感官，但同时也与经验和记忆相关。人类的感知是多维度的。当一名用户在深夜从公交站步行回家时，他可能会感知到环境昏暗、安静且寒冷，但与此同时，他可能会觉得这种情况令人恐惧。而另一名整天忙碌且被人群包围的用户，可能同样感知到环境昏暗、安静且寒冷，但与此同时，他可能会觉得这是一种放松且自由的状态。这个例子表明，仅依赖传感器数据无法提供完整的图景。必须记住，即使是完美的设计和实现，也无法以与用户完全相同的方式来感知环境。

我们现在拥有以下要素：用户的感知和用户的经验，这两者共同构成了用户的预期（Expectations）；以及...

系统基于传感器输入（sensor input）所感知的情境（perceived context）；以及系统包含用户模型的世界模型（model of the world），该模型驱动着系统的反应。参见图 5。一个优秀且可用的设计的核心目标应该是最大限度地减少如图 11 所示的“感知失配（awareness mismatch）”。

![](https://public-media.interaction-design.org/images/encyclopedia/context-aware_computing/figure10a-User-Context_Perception_Model.jpg)
Author/Copyright holder: Unknown (pending investigation). Copyright terms and licence: Unknown (pending investigation). See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/about/terms-of-use) below.

**图 14.11**：所示的用户情境感知模型（User-Context Perception Model, UCPM）强调了用户与系统之间平行的感知过程。如果两者之间存在差异，我们所创建的系统就会出现感知失配，导致系统行为与用户的预期不一致。

用户情境感知模型（UCPM）旨在帮助设计者理解在构建情境感知系统（context-aware systems）时所面临的挑战。它既不描述人类的工作方式，也不规定如何实现系统。尽管如此，如模型所示，情境感知系统的模型可以为设计情境感知应用的系统架构（system architecture）提供一个良好的起点。通过汽车导航系统的例子，我们可以进一步探讨用户认知过程模型（User Cognitive Process Model, UCPM）的细节。如果你使用导航系统，你可能会注意到，当你身处一座从未去过的城市时，它的表现非常好。然而，如果你在居住地附近使用它，有时你可能会对它引导你行驶的路线感到惊讶。这一现象可以用 UCPM 来解释。假设上下文感知系统（Context-aware system，见图 11 右侧）在两种场景下的质量是相同的；这意味着差异必然存在于用户端。在熟悉的地方和陌生的地方，感官知觉（Sensory perception，例如基于视力的建筑物和已知地点的视觉匹配）是不同的。对于陌生的地方，你缺乏参考点（Reference points），且模型中的“记忆与经验（Memory and Experience）”部分存在显著差异。在熟悉的环境中，你会产生预期

关于应该选择哪条路线以及哪种方式是更好的选择。在不熟悉的环境中，你缺乏经验和参考点，因此你的预期仅仅是系统能够引导你到达目的地。结果是，一个能够通过*非最优路线（non-optimal route）*成功引导你到达目的地的导航系统，在*不熟悉*的环境中会满足你的预期，但在*熟悉*的环境中则会受到诟病。非最优路线可能包括由于地图过时而绕路几个街区，或者必须在三个红绿灯前等待，而你本可以通过一座没有红绿灯的桥梁走一条稍长但更顺畅的路线。在熟悉的环境中，我们存在显著的认知失配（awareness mismatch），而当在陌生环境中导航时，认知失配则极小。

**设计提示 2：在用户界面中，提供关于用于确定情境（context）的感官信息（sensory information）的相关信息，以最大限度地减少认知失配。**

用户感知到的情境感知系统（context-aware systems）的质量与认知失配直接相关，而[优秀的设计（good design）](https://www.interaction-design.org/literature/topics/good-design)旨在设计认知失配最小的系统。实现最小认知失配的前提是用户能够理解哪些因素会对系统产生影响。在上述示例中

在一个简单的车载导航系统中，这一因素仅为当前位置（current location），而没有其他因素。在这种情况下，用户知道系统的反应纯粹基于当前位置以及目的地，因此用户可以将系统的响应归因于这些因素。当其他参数发挥作用时——例如考虑交通状况的导航系统——用户可能更难理解系统行为背后的因果关系（causalities）。在这个例子中，由于交通状况不同，导航系统在早晨和晚上可能会建议不同的路线。如果用户不知道系统是基于当前位置和交通状况来提供路线建议的，那么用户可能很难理解系统的运作方式。作为上下文感知系统（context-aware systems）设计的一项重要原则，应当让用户意识到系统所使用的感知信息（sensory information）。

许多设备和应用程序都提供了此类反馈，例如手机中的无线连接[类型](https://www.interaction-design.org/literature/topics/type)以及 GPS 接收符号。这些提示对于用户理解系统行为至关重要。例如，用户可能会理解并接受，在以下情况下，移动设备的下载速度存在显著差异：

系统提供了关于下载有时是通过 GSM 网络、有时是通过 WiFi 连接进行的信息。然而，如果用户不了解 GSM 和 WiFi 数据连接之间的区别，所有这些信息都将没什么帮助，认知失配（Awareness Mismatch）依然存在。因此，如前所述的“设计提示 2”等设计提示（Design Hints）并非绝对的规则，也不能免除设计师进行用户研究（User Studies）和可用性测试（Usability Tests）的责任：正如一句流行的话所说，“了解你的用户（*Know thy user*）”。

![](https://public-media.interaction-design.org/images/encyclopedia/context-aware_computing/figure11a-context-aware-phone.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

**图 14.12**：手机在用户界面中提供了非常简单的上下文信息（Context-information）。在这张图中，手机同时连接到了 GSM 网络和 WiFi 基站。拥有这些信息可以让用户更好地理解系统行为——例如，当用户在通话过程中进入建筑物后，语音质量下降时。通过查看表示网络强度的信号条，用户可能会意识到信号覆盖不足。由于你对该问题拥有一个心智模型（Mental Model），并且

为了解决这个问题，你会向窗户移动或回到门口，以重新获得令人满意的信号质量。

基于传感器的上下文感知（sensor-based context awareness）最基本的理念是：相似的情境（被视为一个上下文 context）由相似的刺激（stimuli）来表示。因此，传感器可以基于这样一个假设来确定上下文：*在相似的上下文中，表征特征（characterizing features）的传感器输入是相似的*。

困难之处在于评估并定义哪些是相关的且具有表征意义的特征。作为人类，我们在日常活动中不断地重复这一过程。当我们进入一个房间，看到人们围坐在桌旁交谈时，即使我们不熟悉这个房间，也不认识任何参会人员，我们也能意识到会议正在进行。其基本方法是对从周围环境接收到的传感器输入进行（隐式 implicit）分析，并将其与早先经历过的情境进行比较。让我们假设在 University of Stuttgart 的 SimTech 建筑一楼会议室有一个晚间会议，此外在 Lancaster 的 InfoLab 二楼会议室也有一个会议——两者均在上午 10 点举行。让我们比较这两种情境的传感器读数（sensory readings），并增加另外两种情境：Stuttgart 的一次学生实验课，以及 Lancaster 会议室的清洁工作。

|  | [情境] |
|---|---|
| [特征] | **Stuttgart 会议** |
| **地理位置：** | Stuttgart |

| **灯光开关状态：** | 灯亮 |
| **房间人数：** | 7 |
| **使用语言：** | 德语 |
| **房间内活动：** | 坐姿 |
| **房间功耗：** | 2kw |
| **使用设备：** | 笔记本电脑, 手机 |
**表 14.1**：情境及其特征属性（Characterizing features）示例

如果我们构建一个矩阵（Matrix）来统计相同特征（Features）的数量，即可得出表 2 中的结果。使用这组特征，我们可以发现，斯图加特（Stuttgart）的会议与实验室环节（Lab Session）的相似度（Similarity），比与兰开斯特（Lancaster）的另一场会议更高。如果我们选择另一组特征，将会得到不同的相似度结果。这说明了为分类（Classification）选择正确特征的重要性。寻找特定情境（Context）的特有特征至关重要，而且在许多情况下，增加更多特征可能会适得其反。

| [相似度] | **S 城市会议** | **L 城市会议** | **实验室环节** | **清洁工作** |
|---|---|---|---|---|
| **S 城市会议** | 7 | 1 | 4 | 1 |
| **L 城市会议** | 1 | 7 | 2 | 1 |
| **实验室环节** | 4 | 2 | 7 | 0 |
| **清洁工作** | 1 | 1 | 0 | 7 |
**表 14.2**：统计每对情境之间的相似特征。由此可见，仅仅统计任意一组特征是行不通的。选择具有代表性的“正确”特征至关重要。

通用方法是观察在特定情境中预期会出现哪些传感器输入（Sensor input）。表 3 中给出了两个示例。一场会议是

在有数人出现且这些人相互交互时被检测到。

当传感器信息表明光线在持续变化且音频电平（Audio level）处于一定水平，且用户处于静止的室内位置时，我们假设用户正在观看电视。示例表明，预期的传感器读数与图 10 中描述的特征空间（Feature space）相关。从这些对预期传感器输入的描述来看，显然检测结果并非完美。很容易出现并非会议但被分类为会议的情况（例如，根据下文的描述，一起吃午餐很可能会被分类为会议）。同样地，我们可以构建一种属于该上下文（Context）但无法通过预期传感器输入被识别的情况。如果用户在花园里看电视，甚至可能使用了字幕并关闭了声音，那么这种情况将无法被识别。

此类描述可以在截然不同的抽象层级（Abstraction levels）上进行（例如，“有人在场”与“被动红外传感器（Passive Infrared Sensor）指示有移动”）。所采用的描述通常取决于所假设的传感器类型。

| ***上下文 (Context)*** | ***预期传感器输入 (Expected Sensor Input)*** |
|---|---|
| 会议 | 数人在场<br>人员之间存在交互 |
| 用户在观看电视 | 光线水平/[颜色](https://www.interaction-design.org/literature/topics/color)正在变化，音频电平处于一定水平（非静音），位置类型为室内，用户基本处于静止状态 |

**表 14.3**：展示了针对两种情境（Context）下特定传感器输入的示例假设

**设计提示 3：寻找你想要检测的情境的特征参数，并寻找测量这些参数的方法**

在当前的系统中，使用了多种传感器来获取情境信息（Contextual Information）。关键的传感器包括：GPS（用于位置和速度）、光感和视觉传感器（用于检测物体和活动）、麦克风（用于获取噪声、活动和谈话信息）、加速度计（Accelerometers）和陀螺仪（Gyroscopes）（用于检测运动、设备方向和震动）、磁场传感器（作为指南针以确定方向）、接近感应（Proximity sensing）和触摸感应（Touch sensing）（用于检测显式和隐式用户交互）、温度和湿度传感器（用于评估环境）以及气压/大气压传感器。此外，还有用于检测用户生理情境（Physiological Context）的传感器（例如：皮肤电反应 [Galvanic skin response]、EEG [脑电图] 和 ECG [心电图]）。皮肤电反应测量皮肤上两个电极之间的电阻，其测量值取决于皮肤的干燥程度。通常，此类测量可用于确定会导致皮肤干燥度变化的反应，例如惊讶或恐惧（测谎仪即基于类似机制）。原则上，可以使用市场上所有类型的传感器为系统提供情境信息。在某些应用中，使用更多同类型的传感器来简化情境识别（Context Detection）任务可能是合理的。例如，使用一组麦克风可以很方便地确定房间内说话者的数量及其位置，而使用单个麦克风则无法实现。使用一组传感器而非单个传感器还可以提高获取信息的质量。一个简单的例子是，单个光传感器只能检测环境的光照水平，而大量的光传感器则是摄像机（Camera）的基础。

为了将传感器信息与情境相匹配，必须执行匹配操作。这些感知任务（Perception Tasks）通常通过[机器学习（Machine Learning）](https://www.interaction-design.org/literature/topics/ai)和数据挖掘（Data Mining）手段来完成。最简单的方法是描述一组定义特定情境的特征（Features）。那么，在任何给定情境中，系统将

监控其传感器输入（sensory input）并检查特征是否与该输入相匹配。简单的基于规则的系统（rule-based systems）属于这一类。另一个例子是记录典型情境（typical situations）并计算这些情境的代表性特征（representative features）。在新情境中，计算其特征并将其与已学习（记录）的情境进行比较。通过一种简单的所谓“最近邻匹配（nearest neighbour matching）”，即可计算出当前的上下文（context）。

应当对计算上下文的算法质量进行评估，以确定系统的运行效果。与经典的信息检索系统（information retrieval systems）类似，这些算法可以针对精确率（precision）或召回率（recall）进行优化。在评估上下文感知系统（context-aware systems）时，考虑特定上下文出现的概率至关重要，否则可能会遗漏极罕见的事件。假设如下示例：你想构建一个火灾报警器，并假设在 10,000 天中，只有 1 天会发生火灾。如果你从地上捡起一块石头并宣布它是一个火灾报警器，你可以很确定它并不具备该功能。尽管如此，你仍然可以声称你的“火灾报警器”在 99.99% 的时间里都能“正常工作”。然而，当提供关于“火灾（0%）”和“非火灾（100%）”上下文的信息时，立刻就能明显看出，石头并不是实现该目的的有用设备。为了评估这一点，通常使用混淆矩阵（confusion matrix），它展示了真实情况与感知情况之间的关系。

为每个定义的上下文提供上下文。

|  | **“系统”感知到的上下文 (Perceived context)** |
|---|---|
| 火灾 | 无火灾 |
| **现实世界中的情况 (Situation in the real world)** | 火灾 |
| 无火灾 | 0 % |
**表 14.4**：石头的混淆矩阵 (Confusion matrix)

|  | **系统感知到的上下文 (Perceived context)** |
|---|---|
| 火灾 | 无火灾 |
| **现实世界中的情况 (Situation in the real world)** | 火灾 |
| 无火灾 | 0 % |
**表 14.5**：理想火灾报警器的混淆矩阵 (Confusion matrix)

![](https://public-media.interaction-design.org/images/encyclopedia/context-aware_computing/figure12a-fire-alarm-context-aware_version2.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

**图 14.13**：为了了解上下文检测器 (Context detector) 的工作效果，你需要知道每个上下文的识别性能 (Recognition performance)。与实际的火灾报警器相比，你很可能同意一块石头无法很好地充当火灾报警器。

## 14.6 在应用程序和用户界面中使用上下文

当感官信息（sensory information）可用，且由此可以确定给定的上下文（context）时，系统和应用程序的各种功能和行为就可以与上下文相关联。如前所述，计算/建立给定上下文的主要[动机（motivation）](https://www.interaction-design.org/literature/topics/motivation)是增强系统对其周围环境的理解。这使得设计者能够创建在不同上下文中表现不同的系统；如果设计得当，这些系统将符合用户在该上下文中的预期，即实现一种*感知匹配（awareness match）*，参见图 11。

不同的行为可以在系统的不同层级上进行设计，其范围涵盖了从低层功能（例如，为当前上下文选择最合适的网络协议），到应用程序行为和支持的功能（例如，在公司网络内使用的移动设备可以访问所有公司文档，而同一设备在公司外部使用时可能只能访问部分文档），再到用户界面层级的变更（例如，地图的缩放级别取决于汽车的行驶速度）。通常很难明确区分此类自适应行为（adaptive behaviour）具体属于哪个类别。

我们通常将上下文感知（context-awareness）分为以下几种类型：
- 上下文自适应系统（Context-adaptive systems）
- 主动式应用（proactive applications）、功能触发器（function triggers）以及自适应应用（adaptive applications）

- 自适应且上下文感知（context-aware）的用户界面
- 基于情境的中断管理
- 上下文共享与上下文通信
- 用于元数据（metadata）的生成数据以及隐式用户生成内容（implicitly user-generated content）
- 上下文感知的资源管理

这些基本类别有助于设计基于上下文的应用。在某些情况下，这些类别之间可能没有明确的区分，或者它们可能会被整合在同一个应用中。早在 Schilit et al (1994) 的原始论文中，就已经包含了关于如何利用上下文的讨论及相关表格。他们在表中将“什么是上下文依赖（context-dependent）的（信息或命令）”与“上下文如何被使用（手动或自动）”进行了区分。这种对上下文感知应用的视角主要反映了上述列表中的第一类和最后一类，即主动式应用（proactive applications）和资源管理。

强烈建议阅读 Bill Schilit et al (Schilit et al 1994) 的这篇论文，因为它是上下文感知计算（context-aware computing）的基石和核心基础。如果您对上下文感知的原始研究感兴趣，可以阅读 Bill Schilit 的博士论文。

|  | 手动 (manual) | 自动 (automatic) |
|---|---|---|
| 信息 (information) | 近端选择与上下文信息 | 自动上下文重构 |
| 命令 (command) | 上下文命令 | 上下文触发动作 |

**表 14.6**：Schilit 等人在 1994 年提出了一套关于构建上下文感知系统（Context-aware systems）的基础分类法（Basic taxonomy）。

### 14.6.1 上下文自适应系统——主动式应用、功能触发器与自适应应用（Context-adaptive systems - proactive applications, function triggers, and adaptive applications）

主动式应用（Proactive applications）根据环境和上下文（Context）代表用户采取主动。例如，当检测到“用户在回家路上”这一上下文时，暖气系统会主动开始为房屋加热。另一个例子是，当用户在公交车站启动设备时，系统会自动启动公交时刻表应用。主动式应用的基本理念是，系统基于上下文预测用户将需要哪个应用，并提前执行该应用。在技术层面，这些有时被称为触发器（Triggers）。即由上下文“触发”应用的启动。

自适应应用（Adaptive applications）在概念上非常相似。主要区别在于，触发的是基于上下文的“功能（Functions）”，而非完整的“应用（Applications）”。然而，应用和功能的粒度（Granularity）可能大不相同，因此这种区分并不具有太大的实际意义。在创建上下文自适应系统时，基本方法是首先定义一组与自适应相关的上下文，然后选择一组要使用的功能或应用，最后在上下文和功能之间创建映射（Mapping）。这可以通过创建类似于表 7 的表格来实现，该表适用于一个自适应的“主屏幕”。该映射还定义了触发器执行的具体方式。

在本示例中，大多数应用程序功能在“进入时（On Entry）”执行，这意味着当用户进入某个上下文（Context）时，该功能将被触发。当用户切换到另一个应用程序时，触发器（Trigger）不会重复执行。名为“始终（Always）”的触发器将确保被触发的应用程序被重复调用；在我们的案例中，当用户在车内时，地图将始终显示在主屏幕上。如果用户切换到另一个应用程序，触发器将每 30 秒检查一次，并在没有用户活动的情况下切换回地图。

另一个例子是名为“每 60 秒（Every 60 Seconds）”的触发器。这种触发器适用于在用户处于特定上下文期间，持续地（在本例中为每 60 秒一次）调用某个功能。触发器的最后一个示例是“退出时（On Exit）”，它在用户离开某个上下文时调用相应功能。虽然不需要正式的描述，但创建如下所示的表格有助于应用程序的设计与实现。表格还显示，上下文可能会出现在多个行中，因为某些上下文需要触发多个功能。同样，功能并不唯一地属于某个上下文；一个功能可以由多个上下文触发。

| **上下文 (Context)** | **时间/触发模式 (Timing/Trigger-Mode)** | **被触发的功能 (Triggered Function)** |
|---|---|---|
| **在办公室** | 进入时 (On Entry) | 在主屏幕显示日历 |
| **在公交车上** | 进入时 (On Entry) | 运行音乐播放器 |

| **在车内** | 始终，每 30 秒检查一次 | 在主屏幕上显示地图 |
| **在车内** | 每 60 秒 | 将当前位置提交至 Web 服务 |
| **在家中** | 进入时 | 在主屏幕上显示 Facebook 消息 |
| **在家中** | 离开时 | 显示待办事项和购物清单 |
| **在健身房** | 进入时 | 运行音乐播放器 |
**表 14.7**：示例应用的上下文-功能映射（Context-Function mapping）

设计提示 4：设计主动式应用（proactive applications）非常困难，因为系统必须预测用户的需求。在许多情况下，与其直接呈现“该应用”，不如提供一组用户可以启动的潜在感兴趣的应用，这样会简单得多。例如，一个上下文感知（context-aware）的“主屏幕”可以提供一组在特定上下文中非常有用的应用供选择，而不是试图直接选择唯一正确的一个。

### 14.6.2 自适应与上下文感知用户界面（Adaptive and context-aware user interfaces）

上下文感知用户界面是上下文感知功能（Context-aware functions）的一个特例。基本上，这意味着一个其上下文感知功能即为用户界面元素的系统。自适应（Adaptation）和感知（Awareness）的复杂程度可能大相径庭。一个非常简单的上下文感知用户界面示例是设备的背光，它在环境黑暗时会自动开启。其他示例还包括适用于特定场景的音频配置文件（Audio profiles）或针对给定上下文优化的屏幕布局。在移动设备上，输入模态（Input modalities）可能取决于上下文。例如，在车内，移动设备可能会使用一个字体较大且可通过简单语音命令激活的简易菜单；而同一台设备在会议中使用时，则可能会呈现一个更复杂的用户界面。Bill Schilit 等人 (1994) 最初提出这一想法的论文中，使用了一个选择打印机的用户界面作为示例。图 14 展示了当“邻近性（Proximity）”可作为上下文时，如何呈现打印机选择菜单的各种选项。这似乎是呈现打印机列表的一种显而易见的方式——但即便在数十年后的今天，我们依然在操作系统中看不到这种方法。

![](https://public-media.interaction-design.org/images/encyclopedia/context-aware_computing/figure13a-ui.jpg)
作者/版权持有者：未知（待调查）。版权所有

条款与许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

**图 14.14**：该用户界面（User Interface, UI）设计展示了向用户呈现上下文（Context）（在本例中为打印机的距离）的不同方式；源自 (Schilit 1994)

上下文感知（Context-aware）的用户界面可能包含输出和输入，以及多种模态（Modalities）。使用户界面具备上下文感知能力，为创建针对每种特定上下文量身定制的[用户体验（User Experience, UX）](https://www.interaction-design.org/literature/topics/ux-design)提供了手段。然而，这并不像听起来那么简单。用户会学习如何使用用户界面，并使其行为与之适应。用户会记住菜单项的位置，或者为了实现特定功能需要执行哪项导航任务。通过使界面元素的布局具有自适应性（Adaptive）且界面结构具有动态性（Dynamic），我们增加了学习使用特定用户界面的难度。如果自适应呈现方式缺乏可理解性（例如，未能向用户清晰地揭示自适应背后的潜在因果关系），可能会阻碍用户记忆用户界面以及高效交互的能力。以 WIMP 风格界面（WIMP-style interface）中的菜单项为例，有人认为应该根据使用频率重新排列菜单项，且不常用的项应当消失。早期的 Microsoft Office 版本曾提供过自适应菜单（Adaptive menus），但事实证明这是一个糟糕的主意——它让许多用户感到困惑，并增加了探索和学习产品使用的难度。随后的 Microsoft Office 版本通过保持所有菜单项可见，但将当前上下文中不可用的功能置灰，从而结合了稳定性与上下文感知（Context-awareness）。这种转变效果非常好。

**设计提示 5：在 UI 中使用自适应机制时需极其谨慎，并确保用户能够理解。优秀的设计应保持稳定性，在支持用户记忆 UI 的同时，利用上下文来降低复杂度。**

### 14.6.3 基于情境管理中断以及在通信中共享上下文（Context）

中断（Interruptions）无处不在。当你正在写一封电子邮件，且句子还未写完时，你收到了一条短信。在通知铃声的干扰下，你将注意力转移到手机屏幕上并阅读消息。然后你重新看向电子邮件……却发现不记得自己刚才想写什么了。这种情况很常见，但大多数时候它们并不关键，我们也已经学会了如何应对。

审视这些中断，我们可以得出一个基本事实：计算机和通信设备是非常“粗鲁”的。想象一下你在图书馆排队。你排在第三位，耐心地等待管理员处理你前面的人。突然，一个人走进来，直接插队到队列最前面，打断了图书管理员与第一位顾客之间的对话，并询问关于她一周前预订的书籍。这种情况很少发生，而且每个人都会对这个人感到厌烦。然而，在电信（Telecommunication）领域，这种情况却时刻在发生。如果两个人正在面对面交谈，其中一人接到了电话，那么这个人很可能会将注意力转移到电话上，从而中断面对面的对话。这种行为可能源于早期的同步通信（Synchronous Telecommunication）模式，在那个时代，电话通话费用昂贵且至关重要——而这一点在今天已不再适用。此外，在……之前

在主叫显示（Caller-ID）出现之前，你无法简单地回电，因为除非你真正接听电话，否则你无法知道是谁给你打电话。尽管技术发生了巨大变化，但我们围绕新技术的某些行为仍然根植于对旧技术的理解。

有多种利用上下文（Context）来最大限度减少中断（Interruptions）的方法。例如：
- 将上下文作为调度中断和通信的来源
- 通过上下文共享（Context sharing）来引导通信的时机

利用上下文信息，我们可以决定何时以及如何传递异步通信（Asynchronous communication）。以短信中断写邮件的过程为例，可以想象将通知推迟到用户在邮件程序中点击发送按钮为止。另一种选择是改变模态（Modality），例如，与其让手机发出音频通知，我们可以采用像计算机状态栏气泡一样的通知，这样对当前任务的侵入性（Intrusive）较低。然而，这个例子表明设计中存在权衡（Trade-off）：如果我们推迟通知，用户可能会太晚收到消息；而如果我们使用额外的或替代的模态，我们可能仍然会中断用户。

在同步通信（Synchronous communication）中，[自动化（Automation）](https://www.interaction-design.org/literature/topics/automation) 很难实现。在这种情况下，上下文共享是利用上下文来提升用户体验的一种极具前景的方法。在 Schmidt et al

(2000)，我们提出了将个人上下文（Context）发布给潜在呼叫者的想法——例如，“我正在开会”这样的状态——并将是否拨打电话的决定权交给呼叫者。其基本原理是，只有在同时了解呼叫者和被呼叫者的上下文的情况下，人们才能决定是否建立连接。关于上下文感知通信（Context-aware communication）的介绍，请参阅 (Schmidt et al 2000) 和 (Schmidt et al 2001)。

随着 Facebook 和 Google+ 等 [社交媒体（Social media）](https://www.interaction-design.org/literature/topics/social-media) 服务的出现，在主流通信系统中使用上下文已成为可能。例如，一些手机将地址簿与用户的 Facebook 状态和位置信息相结合。

### 14.6.4 用于元数据和隐式用户生成内容的生成数据

显而易见的是，无论我们做什么，都是在某种情境（Context）中进行的。如果我们写一篇论文——我们是在某个地方、在一天中的某个时间点，在另一项活动之后或之前完成的。在写作时，我们可能与他人在一起，并且很可能会查阅其他资料。目前，我们撰写的文本并不反映其创建时的情境。你无法看出你在本章中阅读的这些文字是在几次火车旅途中写成的。然而，如果我们能够获取情境信息，就可以在写下的每个词语中附加元信息（Meta-information）。之后在查看文本时，我们可以查询它是在哪里创建的，以及写作时谁在场。自动收集元信息的一个有用领域是支持个人记忆（Personal Memory）和个人搜索（Personal Search）。想象一下你在寻找会议记录：你可能不记得会议是在什么时候举行的，但你可能记得会议地点、在场人员，以及会议结束时已是深夜。如果这些元信息被记录下来，你就可以将其用于搜索。

像 YouTube、Wikipedia、Flickr 或 Facebook 这样的服务，都是人们生成内容并进行分享的媒体示例。所有这些内容都是显式生成（Explicitly Generated）的：视频被录制，文章被撰写，照片被拍摄——然后被分享。这种显式生成的

内容创造了海量的信息，并从根本上改变了 Web。

如果我们审视上下文信息（Context Information），会发现另一个同样有趣的用户生成信息（User-Generated Information）数据源：*隐式*用户生成数据（Implicitly User-Generated Data）。当你开车从家中前往办公室时，你就在生成信息。假设你记录来自车辆（例如加速度传感器、振动传感器、温度传感器、雨量传感器以及轮胎与路面的摩擦力）和导航系统（例如速度、位置、方向）的信息，并将这些信息分享到 Web 上。如果有大量用户分享此类上下文信息，它将构成一个全新的信息领域，涵盖从实时交通信息到路况以及细粒度天气报告（Fine-grained Weather Reports）的广泛内容。尽管这一场景在技术上可行，但在隐私（Privacy）方面仍留有许多待解决的问题。

### 14.6.5 上下文感知资源管理（Context-Aware Resource Management）

资源管理（超出用户界面范围）与用户体验（User Experience）仅有间接关系。上下文感知资源管理的基本方法是根据上下文（Context）来优化设备的运行及其资源利用。一个非常显著的例子是通过使用上下文信息来最大化电池电量，另一个则是根据当前上下文在可用网络之间进行切换。这些功能通常在操作系统的底层实现。

应当记住，这些自适应调整可能会对用户体验产生影响。透明的资源管理对于系统的[易用性（Ease of Use）](https://www.interaction-design.org/literature/topics/ease-of-use)至关重要；想象一下，如果你每次前往城市的另一个区域时，都必须为手机通信选择合适的基站。即使你每次注册新基站时仅收到一个消息框，这也会让手机变得烦人而非实用。只要这种透明性能够正常运作，它就是极好的。然而，如果它失效了，或者用户对系统执行的自动自适应感到困惑，我们应当为用户提供排查问题的方法。            Certificates这将我们带回了一个基础的设计挑战，以及在实现上下文感知系统（context-aware systems）时经常面临的一种权衡（trade-off）：在可见性（visibility）与透明度（transparency）之间寻找平衡。这个问题通常与[视觉设计（visual design）](https://www.interaction-design.org/literature/topics/visual-design)以及抽象（abstraction）相关。以手机上简单的信号强度指示器为例：它展示了关于“连接性（connectivity）”这一资源的某些上下文信息。在这种情况下，关于网络接口质量的所有信息（包括丢包 package loss、延迟 delays、信噪比 SNR、接收信号强度 RSS 等）都由五个信号条来表示，这种抽象使得用户即使对无线电通信（wireless radios）了解不多，也能进行推理。

一个将上下文信息作为游戏资源并用于创造有趣体验的有趣领域是上下文游戏（Contextual Gaming），即在不同的现实世界情境中进行游戏。这里有一份关于情境游戏的入门介绍，以及关于如何将上下文与动作进行映射的具体示例说明...

Holleis 等 (2011)

## 14.7 隐式人机交互（Implicit Human Computer Interaction）

隐式人机交互（Implicit Human-Computer Interaction, iHCI）(Schmidt 2000) 概括了人机交互中上下文感知（Context Awareness）的概念。显式交互（Explicit Interaction，即传统的与计算机的显式交互）与不可见计算（Invisible Computing）和消失的界面（Disappearing Interfaces）的理念相矛盾。为了创造自然交互，除了*显式交互*之外，我们似乎还需要理解*隐式交互*。显式和隐式交互可以基于不同的模态（Modalities），包括命令行（Command Line）、图形用户界面（Graphical User Interfaces, GUI）以及在现实世界中的交互。图 9 概述了一个将隐式和显式[人机交互](https://www.interaction-design.org/literature/topics/human-computer-interaction)纳入考虑的交互模型。

![](https://public-media.interaction-design.org/images/encyclopedia/context-aware_computing/figure15a-implicit.jpg)

作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 14.15**：该模型解释了隐式和显式人机交互的概念，源自 Schmidt 2000。

定义：隐式人机交互（Implicit Human-Computer Interaction, iHCI）
iHCI 是指人类为了实现某个目标而与其环境（包括人造物 Artefacts）进行的交互。在此过程中，

系统从用户处获取隐式输入（Implicit Input），并可能向用户呈现隐式输出（Implicit Output）。

**定义：隐式输入**
隐式输入是指人类为了实现某个目标而采取的行动和行为，这些行为最初并非被视为与计算机的交互，但被计算机系统捕获、识别并解释为输入。

**定义：隐式输出**
指计算机的输出并非直接源于显式输入（Explicit Input），且与用户的环境及任务无缝集成。

隐式人机交互（Implicit Human-Computer Interaction）并非传统显式人机交互（Explicit Human-Computer Interaction）的替代方案，而是在某种程度上是正交的（orthogonal）。为了使计算机在使用中更加敏锐且自然，我们需要在人类与计算机之间建立隐式通信通道。Alan Dix 使用了 *incidental interaction*（偶然交互）一词来描述一个类似的概念。

## 14.8 总结与未来方向

情境感知（Context-awareness）是人机交互（Human-computer interaction）领域中一个令人兴奋且具有挑战性的方向。其核心思想是赋予计算机感知能力（perceptual qualities，即“眼睛和耳朵”），使其能够识别用户与信息系统交互时的具体情境（situations）。通过使用传感器，可以将这些情境检测并分类为上下文（contexts）。一旦系统识别出交互发生在何种上下文中，该信息便可用于更改、触发以及调整应用程序和系统的行为。隐式人机交互（Implicit human computer interaction）的输入端关注用户为了与现实世界交互而产生的信息，从而为人机交互中的情境感知提供了一种泛化（generalization）。

构建情境感知交互系统并非易事。必须意识到，用户在学习如何与系统交互，并且他们会调整自己的行为。至关重要的是，用户需要理解应用程序多变且自适应（adaptive）的行为，并将其与他们所处的情境联系起来。否则，他们将很难学会如何使用该系统。因此，创建符合用户预期且易于理解的情境感知系统至关重要。简而言之：设计良好的情境感知是打造用户友好且令人愉悦的应用程序的一种极佳且强大的方式。然而，如果设计不当，情境感知应用可能会成为挫败感的来源。试想

一个自动灯，你可能会想到一些运行得非常好的例子，以及一些运行不佳的例子。作为上下文（context）的一种特殊形式，位置感知（Location-awareness）已成为主流，因为大多数中高端手机都配备了 GPS 接收器和其他位置检测手段。对亲友行踪的感知结合步行导航（pedestrian navigation），可能会改变我们协调行为的方式；随着多年来技术的演进，我们将逐渐以不同的方式利用我们的环境。你不再需要打电话告诉某人你迟到了，或者询问在何处见面，因为他们可以直接获取这些信息（因为他们能够感知你的移动/位置）。从设计与研究的角度来看，此类场景面临的重大挑战是

创建允许个体以最小的努力（可能通过隐式方式）控制其可见性（Visibility）的模型。

随着能够更详细地监测用户的设备出现，上下文感知（Context-awareness）将在消费级设备中得到日益广泛的集成。想象一下，如果像摄像头和 Kinect（由 Microsoft 为 Xbox 360 游戏机开发的动作捕捉输入设备）这样的技术被集成到家用电器、设备以及你的办公室和家庭环境中。识别人们所处的位置及其行为，将使设计者能够创建关注式应用（Attentive applications）——即能够观察用户的行为并做出相应反应的应用。例如，淋浴设备将识别哪个家庭成员准备使用它（例如基于身体特征 Body profile），并预先选择该成员最喜欢的温度。设计者可以探索如何以极少的交互来操作设备——潜在地，仅仅是“在场”就足以与环境进行交互。在这里，一个核心挑战是在用户界面（User interface）中提供纠正系统错误选择的手段，且这种方式要让用户感到自己拥有控制权。

另一个有趣领域是隐式生成内容（Implicitly generated content）。如果我们生活在传感器丰富环境（Sensor-rich environments）中并使用传感器丰富的设备，我们将拥有前所未有的机会来构建人类生活与交互方式的模型。收集 GPS 轨迹来创建地图是一个开始——openstreetmap.org 就是一个很好的例子。如果我们拥有类似数量的

若能获取关于人们饮食习惯、睡眠质量以及社交频率的信息，我们将能够得出诸如“在傍晚 5 点至 7 点之间食用苹果的人，其睡眠质量比观看肥皂剧的人高 20%”之类的结论。请花些时间深入思考这个例子……我想你可能会由此产生许多关于系统与应用的全新想法，但与此同时，这或许也会令你感到不安。作为系统设计者，我们的责任是利用现有的工具与技术来创造一个更美好、更有趣的世界——而上下文（Context）正是其中一项极其强大的技术！

思考丰富的感知（Sensing）与通信将如何改变我们的生活方式，是一件令人兴奋的事情。我与 Kristian Kersting 和 Marc Langheirich 共同撰写了名为 “Perception beyond the here and now” (Schmidt et al 2011) 的文章。该文探讨了配备传感器的计算设备如何突破人类感知长期以来在时间和空间上的界限。

## 14.9 更多学习资源

如果你想进一步了解上下文感知（Context-awareness），有几个不错的资源可以参考。一个很好的起点是[我的博士论文](http://www.comp.lancs.ac.uk/~albrecht/phd/Albrecht_Schmidt_PhD-Thesis_Ubiquitous-Computing_ebook1.pdf)的第 2 章和第 3 章。在这些章节中，讨论了相关工作并给出了一种上下文获取（Context-acquisition）的方法。

有几位研究人员已经并且仍在从事这一课题的研究，阅读他们的论文也是一个很好的切入点。关于早期工作和基础理论（1994-2001），可以参考 [Keith Cheverst](http://scholar.google.de/scholar?q=Keith%20Cheverst%20Context)、[Anind Dey](http://scholar.google.de/scholar?q=Anind%20Dey%20Context)、[Jason Pascoe](http://scholar.google.de/scholar?q=Jason%20Pascoe%20Context)、[Bill Schilit](http://scholar.google.de/scholar?q=Bill%20Schilit%20Context) 以及 [Albrecht Schmidt](http://scholar.google.de/scholar?q=Albrecht%20Schmidt%20Context) 的出版物。

### 14.9.1 会议

在过去的十年中，该领域变得更加广泛，与人机交互（Human Computer Interaction）相关的上下文感知研究已在以下会议中发表：

### 14.9.1.1 CHI - 计算系统中的人因工程（Human Factors in Computing Systems）

[2011](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2011_conference_on_human_factors_in_computing_systems.html)[2010](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2010_conference_on_human_factors_in_computing_systems.html)[2009](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2009_conference_on_human_factors_in_computing_systems.html)[2008](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2008_conference_on_human_factors_in_computing_systems.html)[2007](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2007_conference_on_human_factors_in_computing_systems.html)[2006](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2006_conference_on_human_factors_in_computing_systems.html)[2005](https://www.interaction-design.org/references/conferences/proceeding_of_the_sigchi_2005_conference_on_human_factors_in_computing_systems.html)[2004](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2004_conference_on_human_factors_in_computing_systems.html)[2003](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_2003_human_factors_in_computing_systems_conference.html)[2002](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_2002_conference_on_human_factors_in_computing_systems_conference.html)[2001](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_2001_human_factors_in_computing_systems_conference.html)[2000](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_2000_human_factors_in_computing_systems_conference.html)[1999](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_99_human_factors_in_computing_systems_conference.html)[1998](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_98_human_factors_in_computing_systems_conference.html)[1997](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_97_human_factors_in_computing_systems_conference.html)[1996](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_96_human_factors_in_computing_systems_conference.html)[1995](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_95_human_factors_in_computing_systems_conference.html)[1994](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_94_human_factors_in_computing_systems_conference.html)[1993](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_93_human_factors_in_computing_systems_conference.html)[1992](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_92_human_factors_in_computing_systems_conference.html)[1991](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_91_human_factors_in_computing_systems_conference.html)[1990](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_90_human_factors_in_computing_systems_conference.html)[1989](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_89_human_factors_in_computing_systems_conference.html)[1988](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_88_human_factors_in_computing_systems_conference.html)[1987](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_87_human_factors_in_computing_systems_conference.html)[1986](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_86_human_factors_in_computing_systems_conference.html)[1985](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_85_human_factors_in_computing_systems_conference.html)[1983](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_83_human_factors_in_computing_systems_conferenc.html)[1982](https://www.interaction-design.org/references/conferences/proceedings_of_the_sigchi_conference_on_human_factors_in_computing_systems.html)

### 14.9.1.2 UbiComp - 普适计算（Ubiquitous Computing）国际会议

[2012](https://www.interaction-design.org/references/conferences/proceedings_of_the_2012_international_conference_on_uniquitous_computing.html)[2011](https://www.interaction-design.org/references/conferences/proceedings_of_the_2011_international_conference_on_uniquitous_computing.html)[2010](https://www.interaction-design.org/references/conferences/proceedings_of_the_2010_international_conference_on_uniquitous_computing.html)[2008](https://www.interaction-design.org/references/conferences/ubicomp_2008_ubiquitous_computing_-_10th_international_conference.html)[2007](https://www.interaction-design.org/references/conferences/ubicomp_2007_ubiquitous_computing_-_9th_international_conference.html)[2006](https://www.interaction-design.org/references/conferences/ubicomp_2006_ubiquitous_computing_-_8th_international_conference.html)[2005](https://www.interaction-design.org/references/conferences/ubicomp_2005_ubiquitous_computing_-_7th_international_conference.html)[2004](https://www.interaction-design.org/references/conferences/ubicomp_2004_ubiquitous_computing_6th_international_conference.html)[2003](https://www.interaction-design.org/references/conferences/ubicomp_2003_ubiquitous_computing_-_5th_international_conference.html)[2002](https://www.interaction-design.org/references/conferences/ubicomp_2002_ubiquitous_computing_-_4th_international_conference.html)[2001](https://www.interaction-design.org/references/conferences/ubicomp_2001_ubiquitous_computing_-_third_international_conference.html)[2000](https://www.interaction-design.org/references/conferences/handheld_and_ubiquitous_computing_-_second_international_symposium_-_huc_2000.html)[1999](https://www.interaction-design.org/references/conferences/handheld_and_ubiquitous_computing_-_first_international_symposium_-_huc99.html)

### 14.9.1.3 PerCom - IEEE 普适计算与通信国际会议 (IEEE International Conference on Pervasive Computing and Communications)

[2008](https://www.interaction-design.org/references/conferences/percom_2008_-_sixth_annual_ieee_international_conference_on_pervasive_computing_and_communications.html)[2007](https://www.interaction-design.org/references/conferences/percom_workshops_2007_-_fifth_annual_ieee_international_conference_on_pervasive_computing_and_communications.html)[2007](https://www.interaction-design.org/references/conferences/percom_2007_-_fifth_annual_ieee_international_conference_on_pervasive_computing_and_communications.html)[2006](https://www.interaction-design.org/references/conferences/percom_2006_-_4th_ieee_conference_on_pervasive_computing_and_communications_workshops.html)[2006](https://www.interaction-design.org/references/conferences/percom_2006_-_4th_ieee_international_conference_on_pervasive_computing_and_communications.html)[2005](https://www.interaction-design.org/references/conferences/percom_2005_workshops_-_3rd_ieee_conference_on_pervasive_computing_and_communications_workshops.html)[2005](https://www.interaction-design.org/references/conferences/percom_2005_-_3rd_ieee_international_conference_on_pervasive_computing_and_communications.html)[2004](https://www.interaction-design.org/references/conferences/percom_2004_-_proceedings_of_the_second_ieee_international_conference_on_pervasive_computing_and_communications.html)[2004](https://www.interaction-design.org/references/conferences/2nd_ieee_conference_on_pervasive_computing_and_communications_workshops_percom_2004_workshops.html)[2003](https://www.interaction-design.org/references/conferences/percom03_-_proceedings_of_the_first_ieee_international_conference_on_pervasive_computing_and_communications.html)

### 14.9.1.4 Pervasive - 普适计算国际会议 (International Conference on Pervasive Computing)

[第6届普适计算（Pervasive Computing）国际会议](https://www.interaction-design.org/references/conferences/pervasive_2008_-_pervasive_computing%2C_6th_international_conference.html)[第二届 ACM 自管理系统上下文感知（Context-Awareness）国际会议论文集](https://www.interaction-design.org/references/conferences/casemans_2008_-_proceedings_of_the_2nd_acm_international_conference_on_context-awareness_for_self-managing_systems.html)[第5届普适计算国际会议](https://www.interaction-design.org/references/conferences/pervasive_2007_-_pervasive_computing_5th_international_conference.html)[第一届环境信息系统（Ambient Information Systems）国际研讨会论文集（与 Pervasive 2007 同期举行）](https://www.interaction-design.org/references/conferences/proceedings_of_the_1st_international_workshop_on_ambient_information_systems_-_colocated_at_pervasive_2007.html)[第4届普适计算国际会议](https://www.interaction-design.org/references/conferences/pervasive_2006_-_pervasive_computing_4th_international_conference.html)[普适移动交互设备：移动设备作为普适用户界面（User Interfaces）与交互设备研讨会（与第三届普适计算国际会议 Pervasive 2005 同期举行）](https://www.interaction-design.org/references/conferences/permid_2005_-_pervasive_mobile_interaction_devices_-_mobile_devices_as_pervasive_user_interfaces_and_interaction_devices_-_workshop_in_conjunction_with_the_3rd_international_conference_on_pervasive_computing_pervasive_2005.html)[第三届普适计算国际会议](https://www.interaction-design.org/references/conferences/pervasive_2005_-_pervasive_computing%2C_third_international_conference.html)[第二届普适计算国际会议](https://www.interaction-design.org/references/conferences/pervasive_2004_-_pervasive_computing%2C_second_international_conference.html)[第一届普适计算国际会议](https://www.interaction-design.org/references/conferences/pervasive_2002_-_pervasive_computing%2C_first_international_conference.html)

### 14.9.1.5 LoCA - 位置与上下文感知研讨会（Symposium on Location and Context Awareness）

[2009](https://www.interaction-design.org/references/conferences/location_and_context_awareness_-_fourth_international_symposium_-_loca_2009.html)[2007](https://www.interaction-design.org/references/conferences/location-_and_context-awareness_-_third_international_symposium_-_loca_2007.html)[2006](https://www.interaction-design.org/references/conferences/location-_and_context-awareness_-_second_international_workshop_-_loca_2006.html)[2005](https://www.interaction-design.org/references/conferences/location-_and_context-awareness_-_first_international_workshop_-_loca_2005.html)

### 14.9.2 期刊

Springer Personal and Ubiquitous Computing

[2009](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing_volume_13.html)[2008](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing_volume_12.html)[2007](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing_volume_11.html)[2006](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing_volume_10.html)[2005](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing_volume_9.html)[2004](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing_volume_8.html)[2003](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing_volume_7.html)[2002](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing_volume_6.html)[2001](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing_volume_5.html)[2000](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing_volume_4.html)[1999](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing_volume_3.html)[1998](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing_volume_2.html)[1997](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing_volume_1.html)
IEEE Pervasive Computing

[2012](https://www.interaction-design.org/references/periodicals/ieee_pervasive_computing_volume_11.html)[2010](https://www.interaction-design.org/references/periodicals/ieee_pervasive_computing_volume_9.html)[2008](https://www.interaction-design.org/references/periodicals/ieee_pervasive_computing_volume_8.html)[2009](https://www.interaction-design.org/references/periodicals/ieee_pervasive_computing_volume_8.html)[2008](https://www.interaction-design.org/references/periodicals/ieee_pervasive_computing_volume_7.html)[2007](https://www.interaction-design.org/references/periodicals/ieee_pervasive_computing_volume_6.html)[2006](https://www.interaction-design.org/references/periodicals/ieee_pervasive_computing_volume_5.html)[2005](https://www.interaction-design.org/references/periodicals/ieee_pervasive_computing_volume_4.html)[2004](https://www.interaction-design.org/references/periodicals/ieee_pervasive_computing_volume_3.html)[2003](https://www.interaction-design.org/references/periodicals/ieee_pervasive_computing_volume_2.html)

### 14.9.3 其他资源

如果你有兴趣思考或设计感知与上下文（Sensing and Context）的未来，有许多方向可以探索。其中一个领域是现实挖掘（Reality Mining），它与前文讨论的隐式内容生成（Implicit Content Generation）密切相关：入门介绍请参阅 [reality.media.mit.edu/](http://reality.media.mit.edu/)，相关出版物可见 [reality.media.mit.edu/publications](http://reality.media.mit.edu/publications.php)。

## 14.10 References

[Dey](https://www.interaction-design.org/references/authors/anind_dey.html), Anind (2000). *Providing Architectural Support for Building Context-Aware Applications - Ph. D. Thesis Dissertation*. College of Computing, Georgia Tech [http://www.cc.gatech.edu/fce/ctk/pubs/dey-thesis.pdf](http://www.cc.gatech.edu/fce/ctk/pubs/dey-thesis.pdf)
GUIDE (2011). *The GUIDE Project Home Page - at Lancaster University*. Retrieved 19 January 2011 from GUIDE: [http://www.guide.lancs.ac.uk/overview.html](http://www.guide.lancs.ac.uk/overview.html)
[Mitchell](https://www.interaction-design.org/references/authors/keith_mitchell.html), Keith (2002). *Supporting the Development of Mobile Context-Aware Computing - Ph.D. Thesis*. Department of Computing, Lancaster University

[Ryan](https://www.interaction-design.org/references/authors/nick_s__ryan.html), Nick S., [Pascoe](https://www.interaction-design.org/references/authors/jason_pascoe.html), Jason and [Morse](https://www.interaction-design.org/references/authors/david_r__morse.html), David R. (1998): Enhanced Reality Fieldwork: the Context-aware Archaeological Assistant. In: [Gaffney](https://www.interaction-design.org/references/authors/v__gaffney.html), V., [Leusen](https://www.interaction-design.org/references/authors/m__van_leusen.html), M. van and [Exxon](https://www.interaction-design.org/references/authors/s__exxon.html), S. (eds.). "Computer Applications in Archaeology - British Archaeological Reports". Oxford: Tempus Reparatum
[Schilit](https://www.interaction-design.org/references/authors/bill_n__schilit.html), Bill N., [Adams](https://www.interaction-design.org/references/authors/norman_i__adams.html), Norman I. and [Want](https://www.interaction-design.org/references/authors/roy_want.html), Roy (1994): Context-Aware Computing Applications. In: [Proceedings of the Workshop on Mobile Computing Systems and Applications](https://www.interaction-design.org/references/conferences/proceedings_of_the_workshop_on_mobile_computing_systems_and_applications.html) December, 1994, Santa Cruz, CA, USA.

[Schmidt](https://www.interaction-design.org/references/authors/albrecht_schmidt.html), Albrecht (2000): *Implicit Human Computer Interaction Through Context*. In [Personal and Ubiquitous Computing](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing.html), 4 (2)
[Schmidt](https://www.interaction-design.org/references/authors/albrecht_schmidt.html), Albrecht, [Beigl](https://www.interaction-design.org/references/authors/michael_beigl.html), Michael and [Gellersen](https://www.interaction-design.org/references/authors/hans-werner_gellersen.html), Hans-Werner (1999): *There is more to context than location*. In[Computers & Graphics](https://www.interaction-design.org/references/periodicals/computers_%26_graphics.html), 23 (6) pp. 893-901
[Schmidt](https://www.interaction-design.org/references/authors/albrecht_schmidt.html), Albrecht, [Takaluoma](https://www.interaction-design.org/references/authors/antti_takaluoma.html), Antti and [Mäntyjärvi](https://www.interaction-design.org/references/authors/jani_m%E4ntyj%E4rvi.html), Jani (2000): *Context-Aware Telephony Over WAP*. In[Personal and Ubiquitous Computing](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing.html), 4 (4) pp. 225-229

[Schmidt](https://www.interaction-design.org/references/authors/albrecht_schmidt.html), Albrecht, [Langheinrich](https://www.interaction-design.org/references/authors/marc_langheinrich.html), Marc and [Kersting](https://www.interaction-design.org/references/authors/kristian_kersting.html), Kristian (2011): *Perception beyond the Here and Now*. In [IEEE Computer](https://www.interaction-design.org/references/periodicals/ieee_computer.html), 44 (2) p. 86–88
[Schmidt](https://www.interaction-design.org/references/authors/albrecht_schmidt.html), Albrecht, [Stuhr](https://www.interaction-design.org/references/authors/tanjev_stuhr.html), Tanjev and [Gellersen](https://www.interaction-design.org/references/authors/hans-werner_gellersen.html), Hans-Werner (2001): Context-Phonebook - Extending Mobile Phone Applications with Context. In: [3rd Mobile Human-Computer Interaction Workshop](https://www.interaction-design.org/references/conferences/3rd_mobile_human-computer_interaction_workshop.html) 2001.
[Weiser](https://www.interaction-design.org/references/authors/mark_weiser.html), Mark (1991): *The Computer for the 21st Century*. In [Scientific American](https://www.interaction-design.org/references/periodicals/scientific_american.html), 265 (3) pp. 94-104
**Chapter TOC**
[**Mobile UX Design: The Beginner's Guide**](https://www.interaction-design.org/courses/mobile-ux-design-course-the-beginners-guide)

![](https://public-media.interaction-design.org/images/courses/hds/course_74--square_thumbnail.jpg?tr=fo-auto)
Mobile UX Design: The Beginner's Guide
Closes in
1
day
08
hrs
19
mins
18
secs
booked
View Course

## 获取每周 UX 洞察（UX Insights）

加入 **314,524 位设计师** 的行列，通过我们的时事通讯（Newsletter）获取实用的 UX 技巧。
需要提供有效的电子邮件地址。

# 14.10 Keith Cheverst 的评论

上下文感知行为（Context-aware behaviour）在现代智能手机中已成为标准配置。对我而言，想到在短短十年前左右，我们还在撰写关于该主题的研究论文，感觉有些奇怪（但也令人鼓舞）。在此期间，Albrecht 一直是上下文感知（context-awareness）领域的杰出人物，本章以一种令人耳目一新的、易于理解的方式，毫不费力地捕捉到了该主题的深度与广度。

最近，我悄悄地将本章的草稿作为一门硕士级别人机交互（HCI）课程的阅读材料，效果确实非常好。本章为该主题提供了一个极佳的历史视角，包括上下文感知背后的关键驱动力，即移动计算（mobile computing）和普适计算（ubiquitous computing）。能再次回顾 Bill Schilit 引入的早期示例（例如根据距离远近列出打印机——这依然是我希望看到的功能）是一件好事。而 Albrecht 在本章中给出的示例，既有助于阐明关键概念，又激发了许多有趣的设计讨论。

Albrecht 非常清晰地阐述了一个重要的关键概念，而学生们往往在这一点上感到困难，即通过层级模型（hierarchical model）将原始传感器数据（raw sensor data）转化为更高层级的上下文触发器（context triggers）。在研读本节详细的实例分析时，我不禁在思考，我目前这批学生对

传感器（如加速度计和陀螺仪），与几年前的情况相比。

除了对上下文感知（context-awareness）在技术/架构层面的探讨外，本章还详尽地涵盖了其“对人机交互（HCI）的影响”。正如 Albrecht 清晰地论证的那样，上下文感知为交互设计师提供了一个强大的工具。如果运用得当，它可以支持设计出能够帮助“减轻负担”的系统；但如果运用不当，则可能导致所产生的系统至少可以说是一种负担。

任何希望实现上下文感知行为的设计师所面临的关键挑战之一就是维持可预测性（predictability）。在阅读 Albrecht 关于他所谓的“感知不匹配（awareness mismatch）”的讨论时，我深感认同，而他通过用户-上下文感知模型（User-Context Perception Model, UCPM）简洁地对其进行了建模。

对设计师而言，另一个具有挑战性的问题是如何为用户维持适当的控制程度，也就是说，如何让用户“保持在回路中（keep the user in the loop）”。对于那些实现了主动/自适应行为（proactive/adaptive behaviour）的上下文感知系统来说，这一点尤为重要。正如 Albrecht 所言，“……一个核心挑战是在用户界面中提供纠正系统错误选择的手段，并且要让用户在这一过程中感到自己拥有控制权”。这让我想起我目前的“智能”手机表现出的一种令人恼火的“习惯”：每当它执意暂停音乐时，我就感到很沮丧。

每当我将设备屏幕朝下放置时，它就会开始播放。我经常将其屏幕朝下放置，因为扬声器在手机背面，因此通过屏幕朝下（即“扬声器朝上”）放置，我可以获得最大的音量。在这种时候，我希望有一个某种形式的“锁定键（hold button）”，能让手机进入一种模式，从而禁用（或者说是摒弃）所有基于物理操作的上下文触发器（context triggers）。然而，由于某种原因（可能是专利问题？），手机没有这个功能，因此我觉得自己缺乏这种控制感（也许说明书的某个地方描述过这个功能……）。

在锁定键旁边，我还会想要一个“向我展示解释你为何这么做的规则”按钮。正如 Albrecht 所言：“……如果用户对系统执行的自动适配（automatic adaptation）感到困惑，我们应当为用户提供查询该问题的方法”。这让我想起了 Judy Kay 在用户建模领域（user modelling domain）关于可审查性（scrutability）的一些研究 (Kay, 1998)。在 Lancaster，我们通过开发一个系统来探讨这个问题，该系统允许用户审查（并可能覆盖）由一个基于上下文历史（context history）的主动式上下文感知系统（proactive context-aware system，用于支持办公环境控制）所推导出的规则 (Cheverst, 2005)。

在保持简洁的同时支持这种用户查询显然很困难（而且不仅仅是增加几个按钮那么简单……）。但如果任其发展，那种“为什么它要这么做，我该如何停止它！？”的感觉会开始像一场消耗战（war of attrition）。

与一个相反的存在。事实上，在总结上下文感知行为（context-aware behaviour）时，Albrecht 指出：“其基本理念是赋予计算机感知特性（perceptual qualities）（‘眼睛和耳朵’），使其能够识别用户与信息系统（information systems）交互的具体情境。”因此，我的手机需要足够智能，以识别并区分以下两种情况：一种是我为了获得更大的音量而将其面朝下放置，另一种是我在会议期间手机突然响起，为了让其立即静音而迅速将其面朝下放置。Albrecht 提供了一个极其清晰的实例，演示了如何从程序化角度思考如何将基于传感器的输入（sensory-based inputs）与特定情境进行恰当的匹配，即“评估并定义哪些是相关且具有表征性的特征（characterizing features）”。因此，希望未来的上下文感知行为设计者能借此机会阅读 Albrecht 的章节，从而创造出能够辅助而非阻碍、亲近而非疏离的智能行为。

## References

- Kay, J.: A scrutable user modelling shell for user-adapted interaction, PhD Thesis, Basser Department of Computer Science, University of
Sydney, Australia (1998)
- Cheverst, K, Byun, H, Fitton, D, Sas,
C, Kray, C & Villar, N, 'Exploring Issues of User Model Transparency and Proactive Behaviour in an Office Environment Control System', *Special Issue of UMUAI (User Modelling and User-Adapted Interaction) on User Modeling in Ubiquitous Computing**,* pp. 235-273. (2005)

## 本书章节涵盖的主题：

[人机交互 (Human-Computer Interaction, HCI)](https://www.interaction-design.org/literature/topics/human-computer-interaction)
[用户体验 (User Experience, UX) 设计](https://www.interaction-design.org/literature/topics/ux-design)
[移动用户体验 (Mobile User Experience, UX) 设计](https://www.interaction-design.org/literature/topics/mobile-ux-design)
[上下文感知计算 (Context-Aware Computing)](https://www.interaction-design.org/literature/topics/context-aware-computing)
[自适应设计 (Adaptive Design)](https://www.interaction-design.org/literature/topics/adaptive-design)
[设计史 (Design History)](https://www.interaction-design.org/literature/topics/design-history)
[GPS (Global Positioning System)](https://www.interaction-design.org/literature/topics/gps)
[使用情境 (Contexts of Use)](https://www.interaction-design.org/literature/topics/contexts-of-use)
