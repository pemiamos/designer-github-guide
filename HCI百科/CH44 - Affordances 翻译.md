# 44. 可供性 (Affordances)

**来源**：The Encyclopedia of Human-Computer Interaction, 2nd Ed.
**Notion 原页面**：https://www.notion.so/2cebd50516e54ce5a00858b313b6b6ca

---

[Victor Kaptelinin](https://www.interaction-design.org/literature/author/victor-kaptelinin)

## 44.1 摘要 (Abstract)

[可供性（Affordances）](https://www.interaction-design.org/literature/topics/affordances)的概念源于生态心理学（Ecological psychology）；它由 James Gibson (1977, 1979) 提出，用以表示环境为行为者提供的动作可能性（Action possibilities）。在 20 世纪 80 年代后期，Norman (1988) 建议在设计中利用可供性。这一建议引起了设计师们的强烈共鸣，因为他们一直关注如何让产品的潜在用途变得直观可见，不久，该概念在[交互设计（Interaction design）](https://www.interaction-design.org/literature/topics/interaction-design)和[人机交互（Human-Computer Interaction, HCI）](https://www.interaction-design.org/literature/topics/human-computer-interaction)中占据了核心地位。本章讨论了 HCI 研究中可供性的起源、历史和当前的解读，并对可供性作为 HCI 概念的未来进行了思考。

## 44.2 引言：为什么需要可供性（Affordances）？

优秀的设计是直观的（Intuitive）（脚注 1）。以 19 世纪设计的 Holmes 立体镜（Holmes stereoscope）为例（图 1）。你可以立即发现：(a) 它有一个手柄，你可以用右手或左手抓握；(b) 你持有该设备，使其从下方获得支撑；(c) 你可以将立体卡片（Stereo cards，或称“立体视图 Stereoviews”）插入卡槽（Card holder slot）中；(d) 你可以通过一对透镜观察卡片。围绕透镜的遮光罩（Hood）形状指示了为了获得正确的观看效果，设备应如何精准放置。

即使你以前从未见过 Holmes 立体镜，你也很可能能够立即上手使用。

![](https://public-media.interaction-design.org/images/encyclopedia/affordances_and_design/affordances_and_design.001.jpg)
作者/版权持有者：Courtesy of Victor Kaptelinin. 版权条款与许可：CC-Att-ND-3 (Creative Commons Attribution-NoDerivs 3.0 Unported).

**图 44.1**：一台 Holmes 立体镜

我们周围有无数设计巧妙且直观的物品，无论新旧。一些例子包括汽车门把手，即使是我们第一次接触某个特定的把手，也能在不经思考的情况下正确使用它（图 2），以及瑞士军刀（Swiss Army knife）（图 3）、夏季度假屋的窗锁（图 4）等等。在日常生活中尽职且低调地为我们提供服务的物品清单是无穷无尽的。

![](https://public-media.interaction-design.org/images/encyclopedia/affordances_and_design/affordances_and_design.002.jpg)
作者/版权持有者：由 Victor Kaptelinin 提供。版权条款与许可：CC-Att-ND-3 (Creative Commons Attribution-NoDerivs 3.0 Unported)。
**图 44.2**：直观的日常设计：汽车门把手。

![](https://public-media.interaction-design.org/images/encyclopedia/affordances_and_design/affordances_and_design.006.jpg)
版权条款与许可：pd (公有领域 (Public Domain，指属于公共财产且不包含原始作者身份的信息))。
**图 44.3**：一种直观的日常设计：瑞士军刀。

![](https://public-media.interaction-design.org/images/encyclopedia/affordances_and_design/affordances_and_design.007.jpg)
作者/版权持有者：未知（待调查）。版权条款与许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”章节。
**图 44.4**：一种直观的日常设计：窗锁。

然而，我们在日常生活中遇到的一些物品的设计并不完全直观——不幸的是，设计糟糕的物品并不罕见。关于各种令人困惑且令人沮丧的物品（例如容易变成“陷阱”的门）的深刻讨论，可以在 Norman (1988) 中找到。

糟糕的设计甚至可能产生深远的

政治后果。Tognazzini (2001) 认为，在 2000 年美国总统大选期间，佛罗里达州棕榈滩（Palm Beach, Florida）所采用的蝴蝶选票（Butterfly Ballot）的设计，可能影响了整个选举的最终结果。可以说，数以千计的选民被该选票的设计所误导，从而投给了错误的候选人（见图 5）。

![](https://public-media.interaction-design.org/images/encyclopedia/affordances_and_design/affordances_and_design.009.jpg)
版权条款与许可：pd (Public Domain (公有领域（属于公共财产且不含原创作者身份的信息）))。

**图 44.5**：
一种反直觉设计（Counterintuitive Design）：“蝴蝶选票”。民主党被列在左侧栏的第二个位置，但若要为其投票，选民应按下第三个按钮。按下第二个按钮则意味着将票投给改革党。

让设计变得直观（Intuitive）的秘诀是什么？如上述示例所示，其中至关重要的一部分与[*感知*](https://www.interaction-design.org/literature/topics/perception)（Perception）有关。对于一个[优秀设计](https://www.interaction-design.org/literature/topics/good-design)（Good Design）而言，仅仅具备理性且逻辑严密是不够的。真正伟大且直观的设计，是那些能让我们直接且正确地“看到”我们可以对某个物体执行什么操作的设计。

对行动可能性的直接感知，本质上就是可供性（Affordance）这一概念的核心。该概念最初由一位美国...

心理学家 James Gibson 使用该词来表示环境“为动物所提供的东西，无论好坏，它所提供或赋予的东西” (Gibson, 1979)。这一概念由 [Donald Norman](https://www.interaction-design.org/literature/topics/don-norman) 在其开创性的著作 *The Psychology of Everyday Things* (1988) 中引入到设计领域，并最终进入人机交互（Human-Computer Interaction, HCI）领域。Norman 将可供性（Affordances）定义为：

> “……物体的感知属性或实际属性，主要是那些决定了该物体可能如何被使用的基本属性……椅子提供（‘用于’）支撑，因此提供了坐的功能。椅子也可以被搬运。玻璃用于透视，也用于破碎。”
> (Norman, 1988).

根据 Norman 的观点，可供性可以在设计中得到富有成效的利用：

> “可供性为物体的操作提供了强有力的线索。平板（Plates）用于推动。旋钮（Knobs）用于旋转。插槽（Slots）用于插入。球类用于投掷或弹跳。当充分利用可供性时，用户只需通过观察就能知道该怎么做，无需图片、标签或说明。”
> (Norman, 1988).

可供性的概念迅速被 HCI 和交互设计（Interaction Design）所采纳，并在从业者、研究人员和教育者中流行起来。对于交互技术的设计师而言，这一概念意味着可以通过利用感知能力，使日常物品变得更加直观，并且总体上更具可用性（Usable）。

可供性（Affordance）也被认为是人机交互（Human-Computer Interaction, HCI）研究中的一个核心概念，并在 HCI 和交互设计（Interaction Design）教科书（例如 Rogers et al., 2011）中被描述为一项基础设计原则。

可供性的应用并不局限于物理对象的设计。事实上，这一概念对于图形用户界面（Graphical User Interfaces, GUIs）的设计师来说尤其具有吸引力。与传统的工业设计师相比，[用户界面](https://www.interaction-design.org/literature/topics/ui-design)设计师能够更自由、更便捷地定义其创建对象的视觉属性。因此，他们似乎处于一个极佳的位置，能够提供 Norman (1988) 所称的关于物体操作的“强视觉线索（strong visual clues to the operation of things）”。提供此类强线索的用户界面元素示例包括 *可点击的*（脚注 2）按钮和 [标签页](https://www.interaction-design.org/literature/topics/tabs)、*可拖拽的* 滑块以及 *可旋转的* 控制控件，以及其他在不同程度上直接暗示合适用户操作的元素（见图 6）。

![](https://public-media.interaction-design.org/images/encyclopedia/affordances_and_design/affordances_and_design.010.jpg)
作者/版权持有者：EasyChair。版权条款和许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用。请参阅版权声明的“例外（Exceptions）”部分（以及“fairUse”子节）。

![](https://public-media.interaction-design.org/images/encyclopedia/affordances_and_design/affordances_and_design.011.jpg)
作者/版权持有者：Apple Inc.。版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用。请参阅版权声明的“例外（Exceptions）”部分（以及“fairUse”子章节）。

![](https://public-media.interaction-design.org/images/encyclopedia/affordances_and_design/affordances_and_design.012.jpg)
作者/版权持有者：ResRobot.。版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用。请参阅版权声明的“例外（Exceptions）”部分（以及“fairUse”子章节）。

![](https://public-media.interaction-design.org/images/encyclopedia/affordances_and_design/affordances_and_design.013.jpg)
作者/版权持有者：由 Flickr 用户 Jodiepedia 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/affordances_and_design/affordances_and_design.014.jpg)
作者/版权持有者：由 Flickr 用户 l-i-n-k (Thomas Link) 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

**图 44.6**：用户界面元素（User Interface elements）的示例，这些元素直接提示了合适的用户操作：（a）可点击的按钮与超链接（hyperlinks），（b）可拖动的滑块（draggable sliders），（c）可点击的

标签页（tabs）、(d) 可滑动的触摸屏滑块（swipable touchscreen slider）、(e) 触摸屏组件（touchscreen widget）中“可按”的按钮（“pressable” buttons）和“可旋转”的控件（“spinnable” controls）。

可供性（Affordance）不仅是人机交互（Human-Computer Interaction, HCI）最核心的概念之一，也是最具争议的概念之一：它在 HCI 领域的发展历史充满了曲折。二十多年来，该概念的含义及其与 HCI 和交互设计（interaction design）的相关性一直是争论的焦点。

本章将讨论可供性的概念及其在 HCI 中的应用；并探讨 HCI 研究中关于该概念的理论阐释（theoretical interpretations）和设计启示（design implications）的持续争论。本章接下来的内容分为四个部分：

- **理论根源**：简要回顾 Gibson 的可供性理论的历史及其要点。
- **HCI 研究中的可供性**：对部分选定分析的概述。
- **争论的关键问题**：讨论一些最具争议的问题。
- **结论**：对 HCI 和交互设计中可供性概念的现状与未来的思考。

## 44.3 理论根源（Theoretical roots）

本节简要概述可供性（Affordances）概念的理论根源。文中讨论了生态心理学（Ecological Psychology）中的一些相关研究——该概念在被“引入”到人机交互（Human-Computer Interaction, HCI）领域之前，最初是在这一领域中发展起来的。讨论的重点是 Gibson (1977, 1979) 提出的可供性概念，而生态心理学中较近期的、后 Gibson 时期的发展仅在文中略有提及。本节的讨论并非专门针对 HCI 和交互设计（Interaction Design）；其目的是阐明可供性的原始含义，从而为后续章节的分析提供必要的理论基础。

### 44.3.1 Gibson 的视觉感知生态方法

可供性概念由 James Gibson (1977, 1979) 提出，作为其[视觉感知（Visual Perception）](https://www.interaction-design.org/literature/topics/visual-perception)生态方法的一部分。在传统的[认知心理学（Cognitive Psychology）](https://www.interaction-design.org/literature/topics/cognitive-psychology)中，感知通常被理解为构建表征（Representations）的过程。在这个过程中，最初没有意义的感官数据与存储在记忆中的信息相结合，经过解释，最终变得具有意义。Gibson 强烈反对这一观点。他提出了一种替代性的、*反表征主义的（Anti-representationalist）*感知理论。

### 44.3.1.1 动物与环境的互惠性（Mutuality of animal and environment）

Gibson 方法论的一个核心观点是*动物与环境的互惠性（Mutuality，或称互补性 Complementarity）*。动物与环境是一个整体系统的两个组成部分：其中一方蕴含着另一方。一方面是动物的解剖结构（Anatomy）与行为，另一方面是其环境的结构，两者之间存在一种耦合（Coupling），这使得动物能够在环境中生存并成功地采取行动。同时，“环境”这一概念（即便是在隐含的情况下）也包含了动物。我们不会用原子或星系来描述我们的环境；相反，我们会指向那些与我们（作为具有特定尺寸和特定动作能力 Action capabilities 的动物）相匹配的对象（如房间、家具、树木、路径、街道、山丘等）。

### 44.3.1.2 检测环境光中的不变量

动物与环境的互惠性（Mutuality）这一概念意味着，动物并没有特别的需求去创建关于“客观世界”的表征（Representation）。感知的目的是高效地获取*有意义的*（meaningful）信息，即那些对于在环境中采取行动具有重要意义的信息。

Gibson 的推理过程包含四个关键论点。首先，他观察到环境是*结构化的*（structured）：它们被组织成由物质和表面构成的动态变化的配置（configurations），这些配置包含了物体、布局和事件。其次，环境的这些结构对于动物来说是*有意义的*。例如，它们可以代表避难所、工具、路径、障碍物、碰撞等等。第三，Gibson 断言，这些结构反过来又赋予了*环境光*（ambient light）以结构，即那些由环境中的物体反射并从四面八方向动物传来的光线。结构化的环境光，或称环境光学阵列（ambient optic array），也会随时间而变化，例如，这是因为动物在改变其位置（脚注 3）。第四，Gibson 认为，通过检测环境光中与环境重要方面相对应的*不变量*（invariants），动物可以*直接*地*提取*（pick up）有意义的信息，而无需构建其环境的内部表征。

![](https://public-media.interaction-design.org/images/encyclopedia/affordances_and_design/affordances_and_design.015_alternative.jpg)
作者/版权持有者：Courtesy of Ron Reiring。版权条款与许可：CC-Att-SA-2 (Creative Commons Attribution-ShareAlike 2.0 Unported)。

**图 44.7**：环境光流阵列（ambient optic array）的流出，表明飞机正处于降落下滑路径（landing glide）中。

能量阵列（energy arrays）中的不变量（Invariants）可能相当复杂，且包含在空间和时间上广泛分布的感官数据。例如，整个环境光流阵列随时间变化的某种特定模式，可以向飞行员指示飞机正在降落（图 7），而非起飞或在地形上方飞行。

动物在环境中的活动（包括身体部位的移动和位移 Locomotion）是检测不变量的关键部分。鸟类通过移动头部来感知深度：通过改变[视角（point of view）](https://www.interaction-design.org/literature/topics/point-of-view)而产生的视觉场差异，有助于它们弥补缺乏双眼视觉（binocular vision）的不足。

### 44.3.1.3 可供性（Affordance）的概念

动物从环境光中直接获取什么样的关于环境的有意义的信息？根据 Gibson 的观点，这就是关于可供性（affordances）的信息，即*环境为动物提供的动作可能性（action possibilities）*。可供性由环境和动物（更具体地说，是动物的动作能力）共同决定。例如，对于具有特定身体结构的动物来说，椅子提供了“坐”的可供性——换句话说，对于这类动物，椅子是*可坐的（seatable）*。一座山对于某些动物来说可能是*可攀爬的（climbable）*（而对另一些动物则不可攀爬），一根针对于人类来说是*可穿刺的（pierce-with-able）*（但例如对狗则不然），以此类推。

可供性是环境的一种属性；它可以被客观地测量和研究。同时，它是一种*关系属性（relational property）*——它是由动物与环境之间的关系决定的，而非仅由环境决定（脚注 4）。为了说明这一点，让我们考虑一个简单的例子（Vyas et al., 2006 使用了一个类似的例子）。假设通过实证研究已经确定，如果围栏的高度超过某个特定值（例如 117 厘米，这是一个随机数字），绵羊就无法跳过该围栏。换句话说，围栏的高度作为围栏的一个客观属性（objective attribute），可以通过将其与一个[值]进行比较，来确定该围栏是否是*可跳过的（jump-over-able）*。

一个经验确立的客观值（empirically established, objective value，在我们的案例中为 117 厘米）。但尽管是栅栏决定了是否提供这种可供性（Affordance），栅栏的可供性仅相对于特定的动物物种（如绵羊）而存在。不能假设它对于例如马类来说也是相同的。

需要特别强调的是，Gibson 对可供性*本身*并不感兴趣。对他而言，可供性的相关性仅在于它们能在多大程度上帮助解释动物如何感知其环境。他指出：

> “可供性理论的核心问题不在于它们是否存在以及是否真实，而在于环境光（ambient light）中是否提供了感知它们所需的信息。”
> (Gibson, 1979)。

Gibson 的理论主张动物能够*直接获取*（directly pick up）关于可供性的信息，这使得对环境中至关重要的方面的检测变得快速且高效。例如，当我们看到正前方的悬崖边缘时，我们会直接意识到它提供了“掉下去”的可供性，并且需要立即采取行动（或不采取行动）以规避危险。这种直接感知（Direct perception）似乎非常成功。挪威一座 600 米高的悬崖 Preikestolen（“布道坛”）是一个主要的旅游景点，每年有超过 10 万人参观（图 7）。尽管悬崖顶部没有安全护栏，且许多游客喜欢站在边缘或坐在边缘附近，但到目前为止尚未有意外坠落的报道。

![](https://public-media.interaction-design.org/images/encyclopedia/affordances_and_design/affordances_and_design.016.jpg)
作者/版权持有者：Courtesy of Stefan Krause。版权条款与许可：CC-Att-SA-3 (Creative Commons Attribution-ShareAlike 3.0)。
**图 44.8**：挪威的 Preikestolen

可供性（Affordance）的概念与格式塔心理学（Gestalt psychology）早先提出的某些概念具有相似之处。具体而言，Gibson 承认其研究受到了 Koffka 的“需求特性（demand character）”概念以及 Lewin 的“邀请特性（invitation character）”或“效价（valence）”概念的影响 (Gibson, 1979)。与此同时，Gibson 坚持认为这些概念与“可供性”之间存在实质性的区别：

> “可供性的概念源自效价、邀请和需求这些概念，但存在一个关键的区别。某物的可供性不会随着观察者需求的改变而改变。观察者可能会根据其需求去感知或关注该可供性，也可能不会，但可供性作为一种不变量（invariant），始终存在于那里等待被感知。可供性并非由观察者的需求及其感知行为赋予对象的。对象之所以提供其所提供的功能，是因为它本身就是这样（The object offers what it does because it is what it is）。”
(Gibson, 1979, 原文斜体)

### 44.3.1.4 文化与自然环境

Gibson 的方法并没有在人类与其他动物之间做出根本性的区分。关于动物与环境之互惠性（mutuality）的假设，以及基于该假设并构成了可供性（affordances）理论基础的论点，具有足够的普适性，可应用于任何动物。Gibson 描述的一些可供性示例与人类特有的物体相关，例如信箱，并且他特别关注了各种工具，包括剪刀、刀具和棍棒。然而，这些可供性被认为与“自然”物体提供给非人类动物的可供性相似。Gibson 指出：

> “……将文化环境与自然环境分开……将是一个错误，就好像存在一个与物质产物（material products）世界截然不同的精神产物（mental products）世界一样。然而，世界只有一个，无论其多么多样，所有动物都生活其中，尽管我们人类动物为了适应自身而对其进行了改造。”
  (Gibson, 1979)

### 44.3.2 后吉布森生态心理学中可供性的选定分析

Gibson 的可供性（Affordance）概念在近期许多生态心理学（Ecological Psychology）研究中得到了进一步的探讨和阐述（例如 Heft, 2000）。与 Gibson 的原始著作相比，这些研究对人机交互（Human-Computer Interaction, HCI）研究的影响相对有限，但其中一些研究可能与 HCI 相关。本节将简要讨论其中几个选定的研究示例。

如前所述，此次讨论并非旨在从其对 HCI 的潜在影响角度，对后吉布森生态心理学（post-Gibsonian ecological psychology）的发展进行全面分析。这样的分析是一项独立（且非常必要）的任务，超出了本章的讨论范围。

### 44.3.2.1 学习（Learning）

“学习（learning）”这一概念在 Gibson 最初的可供性（affordances）理论中并没有扮演重要的角色。学习在少数场合被简要提及，例如，在观察到感知可以通过实践而变得丰富和精细时，但关于人们究竟如何学习感知一种新的可供性这一问题基本上被回避了。Gibson 承认对可供性的感知可能是错误的（他将其称为“误感知（misperception）”），因此可能需要摒弃（un-learn）现有的不变量（invariants）和/或学习新的不变量，但他坚持认为基础的可供性不需要太多的学习。

Eleanor Gibson（James Gibson 的妻子，本身也是一位著名的心理学家）和 Anne Pick (2003) 提出了一个关于学习在可供性感知中作用的略有不同的观点。在她们的著作 *An ecological approach to perceptual learning and development* 中，她们主张可供性并不会自动呈现在行为者（actor）面前。相反，它们通常必须通过感知学习（perceptual learning）被“发现”，且行为者必须“学习如何使用”这些可供性，而在某些情况下，这“……可能需要大量的探索、耐心和时间”（Gibson and Pick, 2003, p. 17）。

Eleanor Gibson 和 Anne Pick 报告的研究表明，大量的感知学习发生在婴儿期。生长为婴儿提供了更先进的动作和感觉系统，婴儿利用这些新能力来扩展和区分

他们的知觉世界（perceptual worlds）。Gibson 和 Pick 还得出结论，婴儿的知觉学习（perceptual learning）和发展具有物种典型性（species-typical）：即同一物种的所有婴儿在这一方面通常是相似的。可以认为，Gibson 和 Pick 所提出的分析存在一个局限性，即它主要关注婴儿和幼儿的知觉。虽然文中提到知觉学习在婴儿期之后仍会继续，并变得更加多样化和具体化，但关于这一问题的研究报道较少。

### 44.3.2.2 工具（Tools）

对于 James Gibson 而言，工具是环境中主要且具有意义的对象类型之一。他提到了几种工具及其可供性（Affordances）。例如，剪刀被描述为人手的延伸 (Gibson, 1979)。然而，Gibson 并没有对工具与环境中其他对象的区别进行系统性的概念分析。生态心理学（Ecological Psychology）近期的一些研究为这一问题提供了更具体的证据。

例如，Wagman 和 Carello (2001, 2003) 开展了一系列关于人们如何使用特定工具——杆状物（rod）的研究。杆状物和棍棒除了其他用途外，还可以用于锤击和戳刺，因此它们的可供性包括“*锤击能力（hammer-with-ability）*”和“*戳刺能力（poke-with-ability）*”。在 Wagman 和 Carello 进行的实验中发现，当棍棒被打算用于不同目的（锤击 vs. 戳刺）时，参与者采用了不同的抓握方式（grips），且工具的使用取决于人们如何探索惯性约束（Inertial constraints）——即使在无法看到工具的情况下也是如此。当棍棒的物理参数（例如与*锤击能力*相关的参数，如棍棒不同部分的相对重量）被修改时，观察到了抓握方式的相应变化。Wagman 和 Carello 得出结论，在分析人们如何利用工具的可供性时，应当区分工具-用户界面（Tool-user interface）与工具-环境界面（Tool-environment interface）。

界面。他们还强调了研究[视觉信息](https://www.interaction-design.org/literature/topics/information-visualization)如何与来自其他模态（Modalities）的感知信息（Perceptual Information）相结合的重要性。

### 44.3.2.3 协作行动（Collaborative action）

Gibson 的框架几乎完全关注于*个体*动物如何在其环境中感知并行动（这些环境也可能包括其他动物）。但动物，尤其是人类，也可以执行共同的、集体的行动（joint, collective actions）。例如，几个人可以共同搬运一个物体，比如担架，这类物体可能因为太重或太庞大而无法由单个人搬运。在近期的研究中，Gibson 的可供性（Affordances）理论也被扩展到了此类行动中，并被用于研究人们如何感知共同行动的行动可能性（action possibilities）。例如，Davies et al. (2010) 分析了人们如何看待与另一个人一起通过门口的可能性，结果表明，共同行动的可能性——即由两人同时执行的行动——是可以被直接感知的。

## 44.4 人机交互（HCI）研究中的可供性：概述

本节概述了人机交互（Human-Computer Interaction, HCI）研究中关于可供性（Affordances）的一些关键概念探讨。此次概述不可避免地具有选择性且不完整。由于使用可供性概念的 HCI 文献数量极其庞大（见脚注 5），无法涵盖所有相关工作。因此，下文的讨论中可能未包含某些重要的分析。此外，一些在 HCI 范围之外的领域中对该概念具有深刻见解的解读（例如 Chen et al., 2007; Ihara et al., 2009; Laarni et al., 2007; Suthers, 2006; Sahin et al., 2007; Zhang, 2008）在此不予讨论。

本概述围绕四个主要主题展开：（a）生态界面设计（Ecological Interface Design）中的可供性；（b）将可供性界定为一种 HCI 概念；（c）从非吉布森（non-Gibsonian）理论视角重新审视可供性；以及（d）探索替代性或补充性概念。

### 44.4.1 生态界面设计中的可供性

生态界面设计（Ecological Interface Design, EID）是认知系统工程（cognitive systems engineering）中的一种方法，由 Vicente 和 Rasmussen 在 20 世纪 80 年代末和 90 年代初开发（例如，Rasmussen and Vicente, 1989; Vicente and Rasmussen, 1990）。该框架明确地受到了生态心理学（ecological psychology）的启发，主要是基于 Gibson 和 Brunswik 的研究（参见，例如，Rasmussen and Vicente, 1989）。可供性（affordances）的概念被引入 EID 的时间与 Norman 将其引入设计领域的时间大致相同，且显然是独立于 Norman 开展的。

EID 的主要目标是为复杂工业系统（complex industrial systems）的操作员创建用户界面，以支持高效且安全的工作实践。该方法利用了 Rasmussen 关于认知控制（cognitive control）三个层级的分类法：基于技能的层级（skill-based level）、基于规则的层级（rule-based level）和基于知识的层级（knowledge-based level）。前两个层级关注于感知和行动，且在这些层级上进行的控制比与基于知识层级控制相关的分析性问题解决速度更快、更轻松，且更不容易出错。生态界面设计（Ecological Interface Design, EID）的目标是确保尽可能多的控制在较低层级（即基于技能（skill-based）和基于规则（rule-based）的层级）完成。这一目标的实现方式是设计能够将工业过程的抽象不可见属性可视化（visible）的界面，从而允许操作员利用感知的力量。Gibson 的可供性（Affordances）理论在 EID 中主要用于探索设计策略，以支持操作员在工业控制环境中直接感知（direct perception）行动的可能性。

虽然 EID 是一种具有深远影响且在实际应用中记录良好的方法，但在过去二十年中，它与广泛的人机交互（Human-Computer Interaction, HCI）领域其他发展的联系相对松散。一个可能的原因是，该方法是专门为高度结构化的复杂工业环境开发的，而这些环境在主流 HCI 研究中逐渐变得不再是核心研究对象（目前主流 HCI 主要...

对“松散耦合领域（loosely coupled domains）”感兴趣，参见 Albrechtsen et al., 2001）。

### 44.4.2 将可供性（Affordance）作为 HCI 概念进行界定

当 Norman (1988) 将可供性的通用概念引入设计领域时，用比喻的话来说，他仅用了寥寥几笔便勾勒出了其轮廓。这次引入虽然强而有力且具有说服力，但并非十分详尽，且正如 Norman 后来本人所承认的，在表述上略有不精确。近期一些关于人机交互（Human-Computer Interaction, HCI）和交互设计（Interaction Design）的论文试图阐明可供性的含义，并将该概念与 HCI 研究和实践的具体议程相结合。

### 44.4.2.1 Gaver (1991, 1992, 1996)：可供性与其感知、复杂动作的可供性以及多模态性

Gaver (1991, 1992) 在人机交互（Human-Computer Interaction, HCI）背景下对可供性（Affordances）进行了重要且早期的分析。在他的论文 “Technology affordances” (1991) 中——正如 McGrenere 和 Ho (2000) 所观察到的，这是第一篇关于可供性的 CHI 会议论文——Gaver 对一系列关键问题进行了深刻但较为简洁的讨论，这些问题需要进一步阐述，才能使可供性成为一个有用且可行的 HCI 概念。

首先，Gaver 系统地分析了可供性与关于可供性的感知信息（perceptual information）之间的关系。他识别了两种情况的四种可能组合：一方面是*可供性*的存在与否，另一方面是*关于可供性的信息*的存在与否：可感知的可供性（perceptible affordances）、虚假可供性（false affordances）、隐藏的可供性（hidden affordances）以及正确拒绝（correct rejection）（图 9）。正如 McGrenere 和 Ho (2000) 所指出的，Gaver 将可供性本身与界定可供性的感知信息区分开来（这与该术语最初的吉布森（Gibsonian）含义一致），这与 Norman (1988) 的解释有所不同，后者将可供性及其感知结合在了一起。

![](https://public-media.interaction-design.org/images/encyclopedia/affordances_and_design/affordances_and_design.017.jpg)
作者/版权持有者：William Gaver。版权条款和许可：所有权利保留

保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

**图 44.9**：
将可供性（Affordances）与其可用信息分离开来，可以区分正确拒绝（Correct rejections）以及感知可供性（Perceived affordances）、隐藏可供性（Hidden affordances）和错误可供性（False affordances）。出自 Gaver (1991)。

其次，Gaver 讨论了复杂动作的可供性，即由多个子动作组成的动作。他识别出两类此类可供性：
- *顺序可供性（Sequential affordances）*：“对可感知可供性的操作会导致产生指示新可供性的信息”（Gaver, 1991, p. 82）。例如，关于门把手的视觉信息可能表明该把手是*可抓握的（graspable）*，而抓握把手可能会揭示它也是*可旋转的（turnable）*。
- *嵌套可供性（Nested affordances）*：一种可供性作为另一种可供性的上下文（Context）。例如，门把手的*可抓握性（graspability）*可以嵌套在门的*可拉性（pullability）*之中。

Gaver 强调了*主动探索（Active exploration）*在揭示和使用复杂对象可供性方面的重要性。他还建议，设计中隐喻（Metaphors）的作用应该是引导用户对系统的探索，而不是传达关于该系统具体应如何使用的实际知识。

第三，Gaver 指出，关于可供性的信息并不限于视觉信息。其他模态（Modalities），如触觉信息和

声音及其组合同样重要，在设计中应予以考虑。

此外，Gaver 简要地讨论了如何使可供性（Affordances）可感知的问题。他指出，与动作相关的对象属性应当在无需中介表征（mediating representations）的情况下即可被感知：“所感知之物即为所操作之物”。根据 Gaver 的观点，那些成功提供可感知可供性的设计采用了在 *nomically*（规律性地/因果地）映射的图形对象，其含义可被感知者直接获取（脚注 6）。

可供性的概念为 Gaver 开展的一系列具体研究提供了理论基础，例如一项关于人们如何感知和使用媒介空间（media spaces）而非普通物理空间（physical spaces）的调查（Gaver, 1992; Gaver 1996）。

### 44.4.2.2 Norman (1999)：真实可供性与感知可供性以及约束类型

在将可供性（Affordances）概念引入设计十年后发表的一篇论文中，Norman (1999) 评论了设计师们是如何采用这一概念的。Norman 指出，使用该概念往往伴随着对其真实含义的混淆，并试图澄清这种混淆。特别是，他承认自己的解读与 Gibson 的原始含义有所不同，即他所说的“可供性”是指“感知可供性（Perceived Affordances）”，而这可能与 Gibson 意义上的“真实可供性（Real Affordances）”有所不同。虽然“感知可供性”的含义没有被明确定义，但它似乎与 Gaver (Gaver 1991) 提出的“虚假可供性（False Affordances）”和“可感知可供性（Perceptible Affordances）”相对应（参见 McGrenere and Ho, 2000）。

Norman 利用三种约束（Constraints）——物理约束（Physical Constraints）、逻辑约束（Logical Constraints）和文化约束（Cultural Constraints）之间的区别，来描述“真实可供性”、[心智模型（Mental Models）](https://www.interaction-design.org/literature/topics/mental-models)以及惯例（Conventions）之间的差异。他解释说，真实可供性与物理约束密切相关，而良好的心智模型与逻辑约束相辅相成，且文化约束实际上是社会群体共同遵守的惯例 (Norman, 1999)。

### 44.4.2.3 McGrenere and Ho (2000)：可供性的程度、功能层级以及有用性与可用性

Gaver 在人机交互（HCI）研究中将可供性（Affordances）概念情境化（contextualizing）的工作 (Gaver 1991, 1992) 在 McGrenere and Ho (2000) 的一篇较近的论文中得到了延续。该论文认为，原有的 Gibson 式可供性概念需要进一步发展，以成为交互系统设计中一个更有用的分析工具。McGrenere and Ho 提出了两个研究方向：(a) 引入可供性程度不同的概念，以及 (b) 理解可供性的功能层级（functional hierarchies）。

***可供性的程度（Degree of affordance）***
McGrenere and Ho 主张超越对可供性的二元观点（即认为可供性要么存在，要么不存在），转向对“行动可能性（possibility for action）”更细致的解读。特别是，他们认为使用某种可供性的难度与 [可用性（usability）](https://www.interaction-design.org/literature/topics/usability) 高度相关，因此应当将其考虑在内。McGrenere and Ho 引用了 Warren (1995) 的工作，将其作为生态心理学（ecological psychology）中探讨这一问题的研究示例。

***可供性的功能层级（Functional hierarchies of affordances）***
基于 Gibson (Gibson 1979) 对环境中嵌套对象（nested objects）的论述以及 Gaver 的嵌套可供性（nested affordances）概念，McGrenere and Ho 认为可供性构成了功能层级，且不限于

与系统的物理交互：
> “计算机系统上的可能操作包括与屏幕、键盘和鼠标等设备的物理交互。但可供性（Affordances）的作用并不止于系统的物理层面 […]。应用程序软件同样提供了可能的操作。文字处理器在高级层面提供了写作和编辑的可供性，但它同时也提供了点击、滚动、拖拽和投放的可供性。用户可以调用的功能即为软件中的可供性。”
  (McGrenere and Ho, 2000)。

他们还观察到：
> “需要注意的是，可供性以层级（Hierarchy）形式存在（或嵌套），且该层级的不同级别可能与系统功能相映射，也可能不相映射。”
  (McGrenere and Ho, 2000)。

此外，McGrenere and Ho (2000) 强烈主张将可供性与其感知（Perception，他们将其归于 Gibson 的观点）分开，因为他们认为，这种分离将有助于研究人员和从业者更清晰地区分设计的两个方面，即：设计对象的效用（Utility，即一种可供性）与设计可用性（Usability，即指定该可供性的信息）。Tornvliet (2003) 也表达了类似的观点。（关于可供性与感知之间关系的这一观点将在下文 4.1 节中详细讨论）。

### 44.4.2.4 Hartson (2003)：可供性的类型与 Norman 的行动模型

Norman (1986, 1988) 将人类行动的结构描述为一个包含七个阶段的「执行-评估循环（Execution-Evaluation Cycle）」：(1) 设定目标，(2) 形成行动意图，(3) 规划一系列行动，(4) 执行该系列行动，(5) 感知由行动序列执行所导致的世界状态，(6) 解释感知结果，以及 (7) 评估解释结果。如果目标达成，则行动完成；否则，循环往复或终止行动。该模型通过将任务分解为独立的组件，并允许分析者关注单个阶段及其之间的具体关系，使设计或评估任务更易于管理。该模型表明，交互设计的核心关注点应该是弥合 [执行鸿沟（Gulf of Execution）](https://www.interaction-design.org/literature/topics/gulf-of-execution)（阶段 (2) – (4)）和评估鸿沟（Gulf of Evaluation）（阶段 (5)-(6)）。

Hartson (2003) 认为，Norman 的行动模型可用于使「可供性（Affordances）」的概念在设计语境中变得更加具体且具有可操作性。他区分了四种可供性：认知可供性（Cognitive Affordances）、物理可供性（Physical Affordances）、感官可供性（Sensory Affordances）和功能可供性（Functional Affordances）。其定义如下：

> “我们根据不同类型的可供性所扮演的角色将其命名为……”

“在交互过程中为用户提供支持，反映用户的处理过程以及用户在执行任务时所采取的行动类型。Norman 的感知可供性（perceived affordance）演变为认知可供性（cognitive affordance），旨在辅助用户的认知行为。Norman 的真实可供性（real affordance）演变为物理可供性（physical affordance），旨在辅助用户的物理行为。我们增加了第三种在交互设计（interaction design）与评估中同样扮演重要角色的可供性——感官可供性（sensory affordance），旨在辅助用户的感官行为。第四种是功能可供性（functional affordance），它将使用方式与实用性联系起来。我们为在设计语境中综合考虑这些类型的可供性提供了指导原则。”
(Hartson, 2003, p.316, 原文为斜体)。

这四类可供性被映射到 Norman 的行动模型（model of action）中：对认知可供性和感官可供性的需求存在于从“行动意图”转向“规划一系列行动”的步骤中；物理可供性和感官可供性与行动序列的执行相关；感官可供性与感知世界状态相关；而认知可供性则被认为在解释感知结果时是必需的（图 10）。

Hartson 使用了一个修改版的 Norman 行动模型，称之为“交互循环（Interaction Cycle）”，将其作为用户行动框架（User Action Framework, UAF）的高层组织方案。UAF 包含了与每种可供性相关的、结构化且全面的具体可用性问题（usability issues）集——除了

功能可供性（Functional Affordances）。功能可供性被认为是一个特殊情况：它们与系统对用户操作的响应相关，而这些响应（或称“结果/产出”，outcomes）通常对用户而言并非直接可见。根据 Hartson 的观点，在交互系统（Interactive Systems）的设计中，向用户提供其操作结果的反馈（Feedback）是一项特殊的任务。

![](https://public-media.interaction-design.org/images/encyclopedia/affordances_and_design/affordances_and_design.018.jpg)
作者/版权持有者：R. Hartson。版权条款与许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

**图 44.10**：映射到 Norman 行动模型（Norman’s action model）的四种可供性。(Hartson 2003, p. 328)。

### 44.4.3 从非吉布森（non-Gibsonian）理论视角重新审视可供性（affordances）

当信息处理心理学（information-processing psychology）作为人机交互（HCI）理论基础的局限性在研究界变得明显时（Carroll, 1991），该领域采用了许多替代方法，其中 [活动理论（activity theory）](https://www.interaction-design.org/literature/topics/activity-theory) 和 [现象学（phenomenology）](https://www.interaction-design.org/literature/topics/phenomenology) 成为了领先的“后认知主义（post-cognitivist）”HCI 框架（例如 Boedker, 1991; Dourish, 2001; Rogers, 2004, Rogers, 2012; Kaptelinin and Nardi, 2006）。

无论是强调人类在世存在之首要性的 Heidegger 现象学（Heidegger, 1962），还是将有目的的、社会的、中介的且不断发展的活动作为基础概念的 Leontiev 活动理论（Leontiev, 1978），在各自的方式中都与 Gibson 的生态心理学（ecological psychology）相似，即假设了行动者与环境之间的互构性（mutuality）。

这种互构性的概念具体体现在，例如 Heidegger 的“在世（being-in-the-world）”概念，以及 Leontiev 的活动概念——后者将“主体（subject）”和“客体（object）”整合在同一个分析单位（unit of analysis）中。尽管这些理论没有使用“可供性（affordance）”这个术语，但它们都假设感知与行动是紧密结合的，且关于“对行动可能性的直接感知（direct perception of possibilities for action）”这一通用观点与它们的整体推理逻辑非常契合。

这些方法与 Gibson 的观点也存在显著差异，因为它们旨在超越动物与环境的交互，进而对人类特有的活动和经验提供阐述。在这些方法中，“环境提供的行动可能性（possibilities for action offered by the environment）”的含义与 Gibson 的理解有所不同。因此，许多研究尝试重新界定可供性（Affordance）的概念，并提出基于活动理论（Activity-theory）（Albrechtsen et al, 2001; Baerentsen and Trettvik, 2002; Kaptelinin and Nardi, 2012）、现象学（Phenomenology）（Dourish, 2001; Turner, 2005; Bonderup Dohn, 2009）以及其他一些方法（Vyas et al., Rizzo, 2006; Rizzo et al., 2009; Still and Dark, 2013）的解释，这也就不足为奇了。这些理论阐述的主要观点总结如下。

### 44.4.3.1 基于活动理论的解释（Activity-theoretical accounts）

### 44.4.4 Albrechtsen et al. (2001)：活动理论与 Gibson 生态心理学中的可供性

Albrechtsen et al. (2001) 从活动理论（Activity Theory）的角度对可供性（Affordances）进行了讨论（见脚注 7）。作者特别指出，活动理论与 Gibson 的生态心理学（Ecological Psychology）之间存在一些相似之处：

> “活动理论与 Gibson 的思维方式共享一个基本观点，即感知并非传入性的（afferent），而是与行动相联系的。人们只有通过行动才能感知其环境。”

与此同时，文中认为，与 Gibson 的方法相比，活动理论为感知和行动提供了一个更广泛的视角。与 Gibson 的生态心理学不同，活动理论关注行动者与环境交互的社会历史维度（social-historical dimension），并考虑了中介（mediation）和学习。活动理论旨在对所有层级水平（hierarchical levels）的人类活动提供解释，而 Gibson 的分析通常侧重于操作（operations）层面（此处采用活动理论的术语）。此外，活动理论将工具理解为功能器官（functional organs），这一概念在可供性理论中没有对应的概念。最后，文中提到 Bødker (1991) 将计算技术使用的三个互补方面进行了区分——物理层面（physical，将计算机视为物理人工制品 [physical artifact]）、操作层面（handling）

（指向计算机应用程序），以及主体/客体导向（subject/object-directed，即通过人造物 Artifact 与主体和客体进行交互）——可用于识别可供性（Affordances）的三个维度或类型，并与上述方面相对应。

### 44.4.5 Baerentsen and Trettvik (2002)：迈向基于更成熟的活动概念的可供性概念

Baerentsen and Trettvik (2002) 提出了另一种从活动理论视角（activity-theoretical perspective）分析可供性（Affordance）的方法（脚注 8）。Baerentsen and Trettvik 首先观察到，人机交互（HCI）研究中许多对可供性的解释正偏离吉布森方法（Gibsonian approach）中该概念的基础假设。他们指出：

> “可供性概念旨在打破传统心理学和哲学中的主客体二分法（subjective-objective dichotomy），但在 HCI 中的解释往往保留了这种二分法。”
> (Baerentsen and Trettvik, 2002)。

与此同时，作者指出了 Gibson 可供性理论的一些缺陷。根据 Baerentsen and Trettvik 的观点，该理论在 HCI 中未能成功应用的主要障碍在于 Gibson 所采用的活动概念缺乏区分度，这：

> “……使得处理像 HCI 这样具有显著文化-历史起源（cultural-historical origin）的文化、符号和技术组成部分的研究领域变得困难且复杂。……有必要将可供性及其在机体活动（organismic activity）中基础的分析，扩展到人类活动的文化-历史发展中……”
> (Baerentsen and Trettvik, 2002)。

Baerentsen and Trettvik (2002) 认为，采用活动理论（activity theory, Leontiev, 1978）中发展出的更先进的活动概念可以帮助

将可供性（Affordances）理解为嵌入在文化语境（Cultural Contexts）中，并在行为者（Actor）与环境之间的具体交互中产生。他们指出了为了理解文化特异性可供性（Culturally-specific Affordances）而应考虑的几个问题，例如学习以及符号（Symbols）和表征（Representations）的使用。

### 44.4.6 Kaptelinin and Nardi (2012)：关于可供性的中介行动视角

在活动理论（Activity Theory）中，工具具有特殊的地位。人类行动被认为在根本上是受中介的（mediated）（Leontiev, 1978）；而将交互技术视为人类与世界交互的中介人工制品（mediating artifacts）这一观点，影响了许多人机交互（HCI）的概念、模型和具体研究（例如 Bødker, 1991; Nardi, 1996; Beaudouin-Lafon, 2000; Bødker and Andersen, 2005; Kaptelinin and Nardi, 2006），其中就包括前文提到的基于活动理论的可供性（affordances）分析（Albrechtsen et al., 2001; Baerentsen and Trettvik, 2002）。

在此研究以及生态心理学（ecological psychology）中一些相关的后吉布森（post-Gibsonian）研究（例如 Wagman and Carello, 2001; Wagman and Carello 2003）的基础上，Kaptelinin and Nardi (2012) 提出了人机交互中关于可供性的中介行动（mediated action）视角。他们将工具性可供性（instrumental affordances）（图 11）的结构描述为由操作可供性（handling affordances，即与相关人工制品交互的可能性）和执行可供性（effecter affordances，即利用该人工制品对感兴趣的对象产生影响的可能性）组成。例如，计算机鼠标允许用户在水平面上移动它（操作可供性），而这会导致计算机屏幕上光标位置的改变（执行可供性）。根据 Kaptelinin and Nardi 的观点，除了工具性可供性之外，人工制品还可以提供辅助性的

可供性（Affordances），例如维护可供性（maintenance affordances）、聚合可供性（aggregation affordances）和学习可供性（learning affordances）。

![](https://public-media.interaction-design.org/images/encyclopedia/affordances_and_design/affordances_and_design.019.jpg)
作者/版权持有者：Viktor Kaptelinin 和 Bonnie Nardi。版权条款和许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。

**图 44.11**：工具性技术可供性（instrumental technology affordances）的两个方面：操作可供性（handling affordances）和效能可供性（effecter affordances）—— P：人（Person），T：技术（Technology），O：关注对象（Object of interest）（Kaptelinin and Nardi, 2012）。

Kaptelinin 和 Nardi 指出，他们所主张的关于可供性的中介行动视角（mediated action perspective）与最初的 Gibson 路径（Gibsonian approach）具有一些共同的基本假设：两者都将可供性视为一种关系属性（relational property），并强调直接感知（direct perception）可供性对于在环境中成功采取行动的重要性。与此同时，中介行动视角在许多方面与 Gibson 的方法有所不同。技术可供性被理解为在行动者（actors）、工具（tools）和文化环境（cultural environments）三方交互中产生的一种关系属性。该视角还强调了考虑学习以及由工具切换（tool switching）引起的人员行动能力动态变化的重要性。在这方面，中介...

行动视角（action perspective）与 Bonderup Dohn (2009) 对可供性（affordances）的现象学解释（phenomenological account）相似，这一点将在下一节中讨论。

### 44.4.6.1 现象学描述（Phenomenological accounts）


### 44.4.7 Dourish (2001)：可供性与具身交互（Affordances and embodied interaction）

在 Dourish 的具身交互（Embodied Interaction）框架（Dourish, 1991）中，该框架深受现象学（Phenomenology）的深刻且明确的影响，其中可供性（Affordances）的概念被用于阐明该框架的一些关键维度。将 Gibson 的生态心理学（Ecological Psychology）应用于人机交互（Human-Computer Interaction, HCI）和计算机支持的协同工作（Computer Supported Cooperative Work, CSCW）领域，被视为探索具身交互理念的典型研究案例。具体而言，Dourish 提到 Gaver 及其同事（1992, 1995）在对协作系统的分析与设计中，融入了行动者（Actor）探索世界的观点。

“本体论（Ontology）”是 Dourish 框架中关于“意义”的关键维度，其讨论大多与可供性相关。有观点认为，可供性概念的范畴可以从物理行为扩展到更广的领域，从而涵盖对理解人造物（Artifact）设计的特定方式的可供性。

尽管可供性概念的具体含义并非具身交互框架的核心议题（脚注 9），但该概念的运用表明其在整体上与现象学视角是一致的。

### 44.4.8 Turner (2005)：简单可供性与复杂可供性、意义以及设备

Turner (2005) 尝试从现象学（phenomenological）视角对可供性（affordances）进行概念化。Turner 分析了当前研究中“可供性”一词的多种用法，并观察到人机交互（HCI）及其他一些领域对可供性的解读已远远超出了 Gibson 最初的阐述。

根据 Turner 的观点，目前对可供性的解读可分为两大类：“简单可供性（simple affordances）”和“复杂可供性（complex affordances）”。“简单可供性”是指 Gibson 意义上的可供性。而“复杂可供性”则是基于文化、历史和实践来定义的，因此无法在 Gibson 的生态心理学（ecological psychology）框架内得到妥善处理。

Turner 简要概述了两个他认为能够处理复杂可供性的理论视角。第一个是俄罗斯哲学家 Evald Ilyenkov 提出的“理想（the ideal）”概念。Ilyenkov (1977) 将“理想”理解为以“意义（significances）”的形式客观存在于世界之中，是由人类的有目的活动所产生的。在这方面，Turner 认为“意义”与“可供性”相似。

第二个视角是 Martin Heidegger 的现象学 (Heidegger, 1962)。Turner 认为，Heidegger 提出的几个概念可用于理解复杂可供性。具体而言，Turner 提到

Heidegger 关于失效（breakdowns）以及由此导致的工具从“上手状态”（ready-to-hand）向“在手状态”（present-at-hand）转变的概念，以及熟悉性（familiarity）和尤其是器具（equipment）的概念。他还参考了由 Dreyfus (2001) 提出的一个更详尽的失效分类法（taxonomy of breakdowns）。根据 Turner 的观点，由于 Heidegger 将器具理解为语境（context），将 Heidegger 的框架应用于可供性（affordances）会导致这样一个结论，即“可供性与语境必然是同义词”（第 12 页）。据称，这一结论与将可供性视为 Ilyenkov 的“意义性”（significancies）的观点是一致的。

### 44.4.9 Bonderup-Dohn (2009)：身体图式、动态且文化相对的可供性视角

Bonderup-Dohn (2009) 从现象学视角（phenomenological perspective）对可供性（affordances）进行了另一种分析，她提出了一种关于可供性的“动态的、关系性的，且依赖于文化与技能的视角”。该分析具体面向计算机支持的协作学习（Computer-Supported Collaborative Learning, CSCL）领域，但大量借鉴了人机交互（Human-Computer Interaction, HCI）领域中关于可供性的讨论。

Bonderup-Dohn 指出，由法国现象学哲学家 Merleau-Ponty (1962) 提出的“身体图式（body schema）”（脚注 10）这一概念，与理解可供性直接相关。她观察到，这一概念强调在具体活动中身体与世界之间存在一种前反思的对应关系（pre-reflective correspondence），并作为构建我们周围空间以及直观理解物体间空间关系的基础；它凸显了我们与世界交互中的某些方面，而这些方面对于分析可供性至关重要。根据 Bonderup Dohn 的观点，理解技术可供性（technology affordances）的关键在于，身体图式（body schema）是一个动态实体。它不仅塑造了我们与世界的交互，同时自身也受到此类交互的影响而发生改变。Bonderup Dohn 指出，技术可以改变身体图式，这种方式例如与活动理论（activity-theoretical）中强调的“功能器官（functional organs）”概念相似（例如 Kaptelinin and Nardi, 2006）。例如，对于一名熟练的打字员来说，键盘可能会成为现象身体（phenomenal body）的一部分；而“对于非常有经验的虚拟化身用户，虚拟化身（avatars）可能会被纳入身体图式之中”（Bonderup-Dohn, 2009）。

根据 Bonderup Dohn 的观点，采用梅洛-庞蒂（Merleau-Pontian）关于可供性的视角，意味着应当根据行动者的文化和经验来考虑其行动能力（action capabilities，见脚注 11）。因此，本文拒绝将可供性理解为独立于文化和经验的（例如 McGrenere and Ho, 2000 所主张的那样），而转而提出一种与文化和技能相关的可供性解释。

### 44.4.9.1 其他相关的理论阐述

Vyas et al. (2006) 提出了一种关于可供性（Affordances）的概念化，认为可供性产生于活动和实践之中，并且是社会和文化构建的：

> “……在用户与技术的交互过程中，用户在参与某些活动的同时，会积极地解读情境并理解技术。用户的‘积极解读’对于社会和文化决定的可供性的出现至关重要。” (Vyas et al., 2006)。

文中主张，可供性应在两个层面进行分析：人造物层面（Artifact level）和实践层面（Practice level）。为了在实践层面分析可供性并将其置于更广泛的社会文化语境中进行理解，作者建议使用 Giddens (Giddens 1994) 的结构化理论（Structuration theory）。此外，他们提出的框架区分了两类可供性：信息可供性（Affordance in information，即*什么*被提供）和衔接可供性（Affordance in articulation，即该系统*如何*被使用）。这些观点在随后的一篇论文 (Vyas et al., 2008) 中得到了进一步深化，该论文将可供性的分析分为三个层面：单个用户、组织/工作组以及社会层面。

Rizzo (2006) 指出了神经生理学研究结果 (Rizzolatti and Craighero, 2004)，这些结果表明，某些基础的神经反应与具有共同目标的整类人类行为相对应，且类似的反应可以

当人们观察其他人类尝试实现相同目标时，[这些信息]会被记录下来。研究结论认为，通过模仿学习（imitative learning），儿童能够根据使用这些物体可以实现什么样的目标，从而理解物体的动作潜能（action potential）。Rizzo 认为，理解人们如何传达意图，以及“意向可供性（intentional affordances）”（该术语最初由 Tomasello, 1999 提出）是如何产生和被感知的至关重要。Rizzo 认为，此类分析为研究可供性如何通过个人历史被文化决定（culturally determined）开辟了新途径。Rizzo 等人 (2009) 在随后的一篇论文中指出，为了充分利用可供性概念的启发式潜力（heuristic potential），交互设计（interaction design）研究需要关注一方面是基础的感觉-运动可供性（sensory-motor affordances），另一方面是意向可供性之间的相互作用。

Still and Dark (2013) 根据传统的认知心理学（cognitive psychology）概念和模型对可供性进行了阐述。该阐述中最核心的概念是 *自动化（automatization）*，即认知模式识别系统（cognitive pattern recognition system）学习自动识别约束（constraints）的过程（无论这些约束是物理上的、文化上的还是逻辑上的，等等）。感知可供性（perceived affordances）的出现与从受控处理（controlled processing）到自动处理（automatic processing）的转变相关联。在认知心理学研究中，自动处理被描述为

“不进入意识，无需意图即可执行，长时记忆负载（long-memory load）较低，且能产生快速响应” (p. 293)。控制处理（Controlled Processing）的特征通常恰恰相反。设计师可以通过确保设计具有高度的一致性，来支持从控制处理向自动处理（Automatic Processing）的转变，从而帮助用户利用感知可供性（Perceived Affordances）。

### 44.4.10 探索替代性（Alternative）与互补性（Complementary）概念

### 44.4.10.1 Norman (2008; 2011; 2013)：示能符（Signifiers）

正如前文所述，在将可供性（Affordances）引入人机交互（HCI）十年后，Donald Norman 觉得有必要澄清他对可供性的理解，并警告不要在设计中过度使用（甚至滥用）这一概念 (Norman, 1999)。又过了十年，他提出了一个更为激进的观点，建议设计师应该关注的是 [示能符（Signifiers）](https://www.interaction-design.org/literature/topics/signifiers)，而非可供性。Norman 在 2008 年简要介绍了示能符的概念 (Norman, 2008)，并在随后的著作 *Living with Complexity* (Norman, 2011) 以及修订版的 *The Design of Everyday Things* (Norman 2013) 中进行了更详细的讨论。Norman 解释说，他所理解的示能符是指“任何标记或声音，任何能够向人传达适当行为的可感知指示物” (Norman, 2013)。

在引入示能符概念时，他特别强调了示能符与可供性之间的关系。根据 Norman 的观点，这两个概念有本质的区别，不应将两者混淆（脚注 12）：

> “可供性定义了哪些操作是可能的。而示能符则规定了人们如何发现这些可能性：示能符是符号，是关于‘可以做什么’的可感知信号。对于设计师而言，示能符比可供性重要得多。”
> (Norman, 2013)。

Norman 指出

示能符（Signifiers）经常与可供性（Affordances）被混淆。在许多情况下，当设计师声称他们在“产品上添加了一个可供性”时，他们实际上所做的是让一个已经存在的可供性变得可见。因此，他们添加的是一个示能符，而非可供性 (Norman, 2011)。

因此，Norman 给设计师们的建议是：

> “我强烈建议设计界区分可供性与示能符。在大多数情况下，‘可供性’这个词应该被弃用，因为设计师关心的始终是那些能够被感知到的东西，而这指的正是示能符。”
> (Norman, 2011, p. 229).

### 44.4.10.2 Djajadiningrat et al. (2002) 与 Vermeulen et al. (2013)：前馈（Feedforward）

Vermeulen et al. (2013) 讨论了另一个概念——前馈（feedforward），他们认为在某些情况下，前馈可以替代可供性（affordances）。他们采用了由 Djajadiningrat et al. (2002) 引入设计领域的前馈概念。前馈被定义为在用户执行操作之前提供给用户的信息（与反馈 [feedback] 相对，后者是指在用户执行操作之后提供的信息）。

Vermeulen et al. (2013) 认为，前馈概念在设计中的潜力目前尚未得到充分挖掘，部分原因是前馈的确切含义尚未得到明确定义。他们旨在通过将前馈与反馈及可供性明确区分开来，并利用 Hartson (2003) 提出的可供性分类法（taxonomy of affordances）以及各种类型可供性与 Norman 的行动阶段模型（Norman’s Stages of Action model）的映射（mapping）关系，来阐明其含义。他们声称，Hartson 图表（见图 9）中的某些元素实际上可以被归类为反馈和前馈的示例，而非可供性。文中提出了一个修订后的图表，如图 12 所示。

![](https://public-media.interaction-design.org/images/encyclopedia/affordances_and_design/affordances_and_design.020.jpg)

作者/版权持有者：Vermeulen et al. (2013)。版权条款与许可：保留所有权利。经许可转载。详见“Exceptions”章节。

下方的[版权条款](https://www.interaction-design.org/about/terms-of-use)。

**图 44.12**：根据 Vermeulen et al. (2013) 的观点，感知可供性（perceived affordances）、前馈（feedforward）和反馈（feedback）在 Norman 的动作阶段模型（Stages of Action model）中的位置。

Vermeulen et al. (2013) 将（感知）可供性与前馈之间的区别描述如下：

> “感知可供性和前馈都通过物理可供性（physical affordances）和功能可供性（functional affordances）的结合，向用户传递关于特定动作的信息。感知可供性和前馈本质上为用户提供了关于实现目标所需执行动作的不同信息。感知可供性揭示的是物理可供性，它告诉用户存在某种物理动作以及如何执行该动作；而前馈揭示的是功能可供性，它告诉用户在执行该动作时会发生什么。”
> (Vermeulen et al., 2013, 原文为斜体).

Vermeulen et al. (2013) 对前馈的讨论旨在为 Norman 动作模型（图 12）中的“执行鸿沟（gulf of execution）”提供理论解释。最近，Norman 本人出于类似的原因也使用了前馈这一术语。在 2013 年版 *The Design of Everyday Things* (Norman, 2013) 中，Norman 对其动作模型的更新表述在描述执行鸿沟时提到了前馈。然而，该术语的含义与...

被 Vermeulen et al. (2013) 所理解。Norman 并没有明确地将前馈（feedforward）与可供性（affordances）进行对比。相反，前馈在广义上被理解为任何有助于执行动作的信息。前馈的概念被应用于整个执行鸿沟（gulf of execution），而非其某个特定部分。Norman 指出，前馈是通过恰当地使用能指（signifiers）、约束（constraints）、映射（mappings）以及 [概念模型（conceptual models）](https://www.interaction-design.org/literature/topics/conceptual-models) 来实现的 (Norman, 2013)。

### 44.4.10.3 拟物化（Skeuomorphism）

一个在交互设计从业者中非常流行（但在人机交互（HCI）研究人员中并不那么流行……）且通常被认为与可供性（Affordances）相关的设计概念是 [拟物化（Skeuomorphism）](https://www.interaction-design.org/literature/topics/skeuomorphism)。一般而言，拟物对象（Skeuomorph）是指一个复制了另一种材质中相似人造物（Artifact）设计的对象或特征（Oxford English Dictionary, n.d.）。例如，一种复制砖墙外观的壁纸图案就是一个拟物对象的例子。另一个例子如图 13 所示，是一个立体卡（Stereo cards）盒子（旨在与图 1 所示的 Holmes 立体镜配合使用），其外观看起来像一套两卷本的书籍。

![](https://public-media.interaction-design.org/images/encyclopedia/affordances_and_design/affordances_and_design.021.jpg)
作者/版权持有者：Courtesy of Victor Kaptelinin. 版权条款和许可：CC-Att-ND-3 (Creative Commons Attribution-NoDerivs 3.0 Unported).
**图 44.13**：拟物化：一个看起来像两卷本书籍的立体卡盒子

在数字设计中，拟物化通常意味着对现实世界对象的真实模仿，无论是在外观上（例如，电子日历的缝线皮革外观，见图 14），还是在其他模态（Modalities）上（例如，数码相机产生的快门点击声）。拟物化曾特别常见于 Apple 产品的设计中。支持拟物化的论点是，它使数字对象更加

既美观又能帮助用户理解如何操作一个不熟悉的对象（这可以被视为提供了指定对象可供性（Affordances）的感知信息（Perceptual information））。

![](https://public-media.interaction-design.org/images/encyclopedia/affordances_and_design/affordances_and_design.023.jpg)
作者/版权持有者：Apple Inc (及未知作者)。版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用。请参阅版权声明的“例外（Exceptions）”部分（及其子章节“fairUse”）。

**图 44.14**：拟物化（Skeuomorphism）：电子日历的缝线皮革外观

近年来，拟物化在交互设计（Interaction design）领域逐渐失去了主导地位。例如，Technopedia.com 的一篇文章 (Technopedia, n.d.) 指出：

> “……拟物化日益受到质疑，很大程度上是因为它试图描绘的许多怀旧元素——如日历、日程计划本、地址簿等——对于年轻一代的用户来说几乎完全陌生。此外，拟物化的批评者指出，设计中对物理对象的这种依赖成为了创造更实用设计的障碍。”
(Technopedia, n.d.)。

一些最受欢迎的数字环境（Digital environments）的最新版本（如 Windows 8 和 iOS 7）在设计上显示出明显的去拟物化趋势。正如最近的一篇 BBC News Magazine 文章所观察到的：

> “拟物化已不再受到青睐……”

近年来，它几乎被设计界（design community）的许多人视为一个禁忌之词（dirty word）。”
(Judah, 2013)。

## 44.5 争议的核心问题

前一节对人机交互（Human-Computer Interaction, HCI）研究中关于可供性（Affordances）之争的简要概述，使我们能够识别出该讨论中出现的一些共同问题。需要注意的是，其中许多问题彼此密切相关，甚至相互重叠。

### 44.5.1 可供性与感知（Affordances and perception）

可供性（Affordances）与感知（Perception）之间的关系在人机交互（HCI）研究中已成为二十多年来备受争议的问题，总体趋势是将可供性与感知进行日益严格的分离。这一趋势在 Norman 对可供性解释的演变中尤为明显，具体讨论见上文第 3 节。其演变过程可简述如下（脚注 13）：

- **1988年**：Norman 将可供性引入设计领域，将其描述为“事物的感知属性和实际属性”；该概念被理解为同时指代*提供给执行者的行动可能性及其被执行者的感知*；
- **1999年**：Norman 将“真实可供性（real affordances）”（对应于 Gibson 的“可供性”）与“感知可供性（perceived affordances）”（可能真实也可能不真实）区分开来；他澄清说，在他之前的著作中，所谓的“可供性”实际上是指“感知可供性”；
- **2008/2011/2013年**：Norman 进一步将可供性（此时仅指 Gibson 意义上的可供性，或称“真实”可供性）与其相关信息（即示能符 Signifiers）完全分离。

几位研究人员（例如 McGrenere and Ho (2000) 以及 Tornvliet (2004)）注意到并讨论了 Norman 最初对可供性的解释（Norman, 1988）与该术语原始的 Gibson 含义之间存在的不一致，并认为这是一个问题。Soegaard (2009) 指出：

> “与……不同

“Norman 将对象的感知属性（perceived properties），或者更准确地说，是规定对象如何被使用的信息，纳入其中；而 Gibson 式的可供性（Gibsonian affordance）则独立于行动者（actor）的感知能力。” (Soegaard, 2009)

毫无疑问，这些旨在澄清 Norman 和 Gibson 解释之间差异的努力，在解决某些术语不确定性方面应获得认可。这种澄清至关重要，因为 Norman 早期对可供性的解释（尽管他本人后来已将其放弃）在文献中依然可见。例如，一本广受欢迎的交互设计（interaction design）教科书将可供性描述为“……用于指代对象的一种属性，使人们能够知道如何使用它”的术语 (Rogers et al., 2011)。

与此同时，一些旨在澄清术语问题的尝试甚至主张需要将可供性与感知（perception）完全分开，以回归到原始的 Gibson 式概念。特别是 McGrenere and Ho (2000) 声称，根据 Gibson 的观点，可供性“独立于行动者的经验、知识、文化或*感知能力*”（斜体为后加；关于这一立场的批判性分析，另见 Bonderup Dohn, 2009）。Tornvliet (2003) 也提出了类似的观点：“Gibson 致力于将可供性定义为环境的一种特性，它相对于某个对象而存在，但*独立于感知*。”

（斜体为后加）。有理由相信，将可供性（Affordances）与感知（Perception）如此严格地分开并非没有问题。感知的独立性可以从三种不同的方式来解读，即以下方面的独立性：(a) 行为体（Actor）感知环境的通用能力；(b) 环境能量阵列（Ambient Energy Array）中关于可供性的感知信息；以及 (c) 具备通用感知能力的行为体是否实际提取了关于某种可供性的信息，而该信息存在于环境能量阵列中。可以认为，在 Gibson 的可供性理论语境下，只有最后一种解读既准确又相关。

声称可供性独立于行为体的通用感知能力，显然是错误的。Gibson 强调的紧密耦合（Tight Coupling）

感知与行动的统一意味着行动者的行动能力包括感知。值得注意的是，在现代生态心理学（ecological psychology）中，可供性（affordances）通常被定义为“对于一个*感知-行动*系统（perceiving-acting system）而言的真实行动可能性”（Wagman and Carello, 2001，强调为原作者所加）。感知是定义行动能力的关键因素，这一点可以通过一个简单的例子来说明：如果一名驾驶员打破了他的眼镜，汽车可能会变得“无法驾驶”。在这种情况下，物体的可供性发生变化，并非是因为汽车出了问题，而是因为驾驶员的行动能力变得不足；而行动能力变得不足，并非是因为驾驶员无法再进行肢体运动，而是因为感知功能下降了。

关于可供性独立于环境能量阵列（ambient energy array）中相关感知信息的观点（例如，在镶板房间中隐藏门的例子，见 McGrenere and Ho, 2000），在形式上可能是正确的，但它与 Gibson 的可供性理论没有直接关系。正如前文所述，Gibson (1979) 强调，他的可供性理论主要关注的是关于可供性的信息是否在环境光（ambient light）中可用，而不是可供性是否客观存在或是否真实。因此，Gibson 的可供性理论具体关注于

行动可能性，*这些可能性反映在相应的环境能量阵列（ambient arrays of energy）结构中，因此可以被行动者感知*；而在该理论的语境下，脱离其与感知信息（perceptual information）的关系来独立分析可供性（affordances）在很大程度上是没有意义的。在这方面，Norman 早期以感知为中心的可供性解释——除了某些术语问题以及关于“直接拾取（direct pickup）”含义的某些分歧（见 Norman, 1988）之外——可以说在总体上与原始的 Gibson 方法是一致的。

但是，Gibson 的以下主张之间是否存在矛盾：(a) 可供性理论本质上关注的是环境光中的感知信息，以及 (b) 即使可供性未被行动者注意到，它们依然存在？实际上并没有，因为*存在于环境光中*的信息可能并未被行动者*实际感知*。例如，如果一个人在森林中行走时没有看向蘑菇的方向，那么一颗*可采摘的*蘑菇可能会被其忽略。

因此，虽然当然应该避免将可供性与其感知混为一谈，但如上所述，将可供性与感知完全分离则意味着走向另一个同样不可取的极端。

### 44.5.2 直接感知与“间接”感知

与直接感知（Direct Perception）的相关性，似乎是可供性（Affordances）概念在人机交互（Human-Computer Interaction, HCI）和交互设计（Interaction Design）中广泛流行的关键因素。Gaver (1991) 指出，生态视角（Ecological Perspective）的主要优势在于，它“可能为设计那些能够以直接方式提示相关且理想动作的人造物（Artifacts）提供一种更简洁的方法”（斜体为后加）。

因此，人们会预期，探索如何通过适当的设计来支持对可供性的直接感知，应当是一个关键的研究议题。然而，事实并非如此。“直接感知”一词在 HCI 文献中被广泛使用，但在关于可供性的 HCI 研究中，针对如何实现对交互产品动作可能性（Action Possibilities）的直接感知，其机制、标准、条件和解决方案的分析似乎并未成为一个被积极探索的议题。

存在一些概念障碍（Conceptual Obstacles），可能阻碍了研究人员以具体且建设性的方式有效地解决这一问题。一方面，Gibson 的方法本质上主张，我们对物质环境（Material Environment）的感知只能是直接的。他的可供性理论可以被解读为：无需支持直接感知，因为它自然而然地发生。除此之外别无他法：直接感知是唯一存在的感知方式。另一方面，在语言表达信息的视觉感知（visual perception）方面，可以提出相反的论点。Gibson 的直接感知（direct perception）理论似乎并不适用于此处（脚注 14）：显然，我们需要感知组成单词的字符，并且可能需要在词典中查阅该单词，才能确定单词的含义及其相关的动作可能性（action possibilities）。但在这些情况下，感知似乎只能是间接的——因此，支持向直接感知过渡的任务再次无法被赋予有意义的定义。

因此，将可供性（affordances）的直接感知纳入人机交互（HCI）研究议程的核心问题包括：生态心理学（ecological psychology）的基本原理是否允许存在*非*直接的感知？视觉语言表征（visual language representations）能否被直接感知？可以认为

这两个问题的答案都是“是”。

从生态视角（ecological perspective）研究知觉学习（perceptual learning）的 Eleanor Gibson 和 Anne Pick (Gibson and Pick 2003) 得出结论，可供性（affordances）通常需要被发现，而且有时需要大量的探索、努力和耐心。显然，探索意味着在对可供性的知觉变得直接之前，知觉信息与可供性之间的各种关系需要经过“检验”和“尝试”。因此，生态心理学（ecological psychology）的研究表明，并非所有的知觉都是直接的；直接知觉（direct perception）应当被视为一种成就，而非自然而然发生的事情。

同时，有实证证据表明，对语言材料（verbal material）的视觉识别可以变得直接，即在无需语言识别的情况下，直接利用视觉特征来执行相应的操作。例如，一项关于菜单选择的研究 (Kaptelinin, 1993) 提供的证据表明，随着练习的增加，用户会转而无需阅读名称即可选择命令，也就是说，菜单选择是基于提取“非语言”的视觉特征（例如屏幕位置或命令名称的长度）而进行的。

设计师如何支持向直接知觉的转变？Still and Dark (2013) 提出的通用策略是使设计尽可能保持一致。一个相关的、更具体的

这种策略是通过构建环境光学阵列（ambient optic array），从而在结构与相应的用户操作之间建立清晰的映射（mapping）。例如，可以参考 MS Word 的“更改大小写（Change case）”对话框（图 15）。该组件（widget）的设计采用了特定的视觉特征，使用户无需阅读选项名称即可感知该组件的可供性（affordances）。只要用户熟悉该书写系统，甚至不需要掌握该语言。

![](https://public-media.interaction-design.org/images/encyclopedia/affordances_and_design/affordances_and_design.024.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

**图 44.15**：利用视觉特征支持直接感知（direct perception）：MS Word 的“更改大小写（Change Case）”对话框。

### 44.5.3 文化（Culture）

Gibson 的生态方法（ecological approach）具体且明确地探讨了具有感知和行动能力的动物。该方法的核心概念，包括可供性（affordances），是基于动物与环境的交互（animal-environment interaction）来定义的。尽管 Gibson 本人及其理论支持者提供了许多以人类特有物品（如刀具、信箱、楼梯、飞机、图片等）为例的说明，但与这些物品的交互分析，仍是在一个与其他动物在各自生态位（ecological niches）中与物体交互相同的通用框架下进行的。这种视角是广义上生态心理学（ecological psychology）许多研究的典型特征。例如，Eleanor Gibson 和 Anne Pick (2003) 提到了一种“由动物自身发起的行动，例如驾驶卡车”。

当然，人类确实是动物，而这一事实对于我们人造世界的构建方式及其体验具有深远的影响。我们的建成环境（built environments）以及构成环境的单个物品之所以呈现出现在的样子，在很大程度上是因为我们是拥有特定身体、双手、运动功能和感官的动物。如果我们是另一种动物，那么我们的房屋、汽车、飞机和计算机（假设我们拥有这些东西）将会呈现出不同的面貌。毫无疑问，在设计交互产品时，必须考虑到作为特定动物物种，哪些行动方式对我们而言是自然的。然而，人类在许多方面也具有根本上的独特性。与其他动物不同，我们是社会性和文化性的生物：我们使用语言，参与社会组织的集体活动，并使用其他动物所不具备的各种人工制品（Artifacts）。因此，一个逻辑上的问题是：一种以动物为中心的可供性理论，能否解释人类与世界交互的*全部*范围？Gibson 的可供性概念能否被用于理解专门针对*人类*行为的可能性？如前所述，这些问题在过去十年的 HCI 研究中受到了一定的关注。

一些研究人员，包括 Turner (2005), Rizzo (2006) 和 Vyas et al. (2006)，认为虽然 Gibson 提出的框架可以提供一个

虽然该理论为物体操纵和移动（Locomotion，即与物理环境的直接交互）可能性的感知提供了一个合理的阐述，但很难将这一框架应用于更高级的社会和文化活动示例。即使是 Gibson 的一些示例（例如使用邮箱），也不容易通过布局（Layouts）、物体（Objects）、事件（Events）和环境光线（Ambient light）来进行分析。虽然使用邮箱的物理交互部分相当简单，但准确理解人们如何感知将信件寄往远程地点的可供性（Affordance）似乎相当困难。总的来说，Gibson 对工具的分析几乎完全集中在简单的物理对象上，这些对象原则上不仅可以由人类使用，也可以由其他动物（如类人猿）使用。而对于人机交互（Human-Computer Interaction, HCI）主要关注的更复杂工具的分析，则几乎完全缺失。

在 HCI 研究中，人们对于原始的 Gibson 可供性概念能否作为人类交互技术分析与设计框架的潜力，持有日益增长的怀疑态度。将人类仅仅视为另一种动物物种，正日益被认为是 Gibson 可供性理论在 HCI 中应用的一个主要局限。不过，有理由认为，可供性的通用概念可以有效地应用于超出原始 Gibson 范围（即动物-环境交互）的领域。

人类社会行为的可能性被规定在环境能量阵列（ambient energy arrays）之中，其方式与物理行为的可能性极为相似，且同样可以被直接感知。他人的姿态和面部表情所传达的紧迫言语攻击感，可能与看到悬崖时感知到的坠落威胁一样直接。同事办公室的一扇开着的门，对于发起一场即兴对话（ad hoc conversation）的可能性所提供的线索，可能与物理上穿过该门口的可能性一样强烈。这些及类似的案例显然可以用可供性（affordances）及其感知来描述，尽管它们所涉及的交互并不局限于物体操纵（object manipulation）和移动（locomotion）。

因此，未来关于人机交互（HCI）中可供性研究的一个关键挑战，似乎在于将文化语境（context of culture）纳入考量，从而理解*人类行为*的可能性是如何被创造、感知，以及如何通过适当设计的技术来获得支持。

### 44.5.4 工具的可供性（Affordances of tools）

Gibson 讨论了各种工具，如棍棒、刀具和剪刀，但他并没有系统地探讨是什么让工具与环境中的其他物体有所不同。例如，他指出：“一个具有刚性锐利边缘且可抓握的物体提供了切割和刮除的可供性（如刀）。” (Gibson, 1979)。这一例子表明，该物体的可供性不仅包括“切割能力”（*cut-with-ability*，或刮除能力 *scrape-with-ability*），还包括“可抓握性”（*graspability*），但后者并未被明确地视为一种可供性。此外，Gibson 将工具（如剪刀）描述为身体（如人类的手）的延伸。然而，他并没有系统地探讨工具的使用如何影响环境中其他物体的可供性，例如，使用剪刀如何使一张纸变得“可切割”（*cuttable*）。因此，关于工具的可供性与其他物体的可供性有何不同的问题——这在人机交互（Human-Computer Interaction, HCI）领域至关重要——仍然是一个开放性问题。

HCI 中对可供性的分析同样未能提供该问题的答案。其中大多数分析并未明确区分技术工具的可供性与一般意义上的可供性（即使是那些刻意关注“技术可供性”的分析也是如此）。以 Norman 的动作模型（model of action，见上文图 10 和 12）为例，该模型被应用于 HCI 中关于可供性的多次探索中。该模型并未包含关于技术工具的明确概念；它描述了如何

人们与“世界”进行交互，且这似乎同样适用于，例如，网上银行和采摘浆果。

第 3 节的讨论表明，活动理论（Activity Theory）和现象学（Phenomenology）可以为可供性（Affordances）提供一些“特定于技术（technology-specific）”的阐释。例如，活动理论中的中介（Mediation）概念和现象学中的失效（Breakdowns）概念，分别在中介行动视角（Mediated Action Perspective, Kaptelinin and Nardi, 2012）和失效分析（Analysis of Breakdowns, Turner, 2005）中得到了探讨。然而，这些分析目前都尚不完整，需要进一步深化。

### 44.5.5 学习（Learning）

关于可供性（Affordances）的一个普遍假设是，感知它们通常不需要太多的（甚至不需要任何）学习；直接理解可供性的能力是我们每个人都具备的。无需任何指导，我们就能看出悬崖提供了“掉下去”的可供性，小石头提供了“投掷”的可供性，而椅子则提供了“坐”的可供性。这种假设的学习独立性（independence of learning）可能是可供性在设计师中如此受欢迎的原因之一。然而，如下文所述，这一假设实际上是一个误区。

公平地说，这个误区并非完全没有根据：事实上，在 Gibson 对其可供性理论的阐述中，几乎没有讨论过学习的问题。动物正确获取行为相关信息（behaviorally relevant information）的能力在本质上被认为是理所当然的，被视为动物与环境之间互补性（mutuality）的直接结果。在生物进化的宏大尺度上，这一假设是合理的：一个动物物种的存在（即生存）本身就证明了该物种的个体在原则上能够正确感知环境的可供性。然而，这一论点不能直接应用于个体动物的具体生活环境层面。当动物出生时，其感知功能（perceptual functions）尚处于初步阶段，行动能力（action capabilities）极其有限。只有通过成熟（maturation）和实践，它们才能获得行动能力以及获取新兴可供性（affordances）信息的能力。此外，即使是同种动物，个体的生活条件也可能截然不同，因此动物所面对以及必须感知的可供性也各不相同。因此，对于个体动物而言，感知可供性的能力并非理所当然，而是一种成就，是学习和发展的结果。

由 Eleanor Gibson 及其同事（例如 Gibson and Pick, 2003）在 Gibson 的生态方法（ecological approach）通用框架下开展的感知学习与发展研究，无疑为学习的核心地位提供了重要的见解。

在可供性（Affordances）的感知中。这些研究的一个局限性在于，它们主要处理在*稳定*生活条件下发生的进程（例如，婴儿时期的感知学习 [Perceptual Learning]）。在此类条件下，学习的结果是行动者（Actors）在较长时间内逐渐更先进地适应其环境。尽管这些研究具有深刻的见解且十分重要，但它们与设计的相关性有限。

新的设计通常具有颠覆性（Disruptive）。通过提供新的可供性，它们可能会引起环境的重大变化，并产生对新学习努力的需求。预测此类需求并高效地支持用户的学习，需要理解当颠覆发生时，行动者-环境互惠性（Actor-environment Mutuality）是如何恢复的——也就是说，在新的可供性取代旧的可供性之刻，与行动者获得直接感知新可供性能力之刻之间，发生了什么。遗憾的是，目前关于此类现象的实证证据（Empirical Evidence）仍然匮乏。

因此可以得出结论，明确地考虑可供性意味着，支持用户发现可供性以及学习如何使用它们，应当成为设计师关注的核心问题。目前，关于人们究竟如何学习、摒弃（Unlearn）以及重新学习新可供性的证据仍然不足。

## 44.6 结论：对可供性（Affordance）作为人机交互（HCI）概念的现状与未来的思考

### 44.6.1 不同研究语境下可供性的解读

正如本章所讨论的，自从 Norman (Norman 1988) 将该概念引入该领域以来，人机交互（Human-Computer Interaction, HCI）研究中关于可供性（Affordance）的争论经历了相当剧烈的波折。研究发现，Norman 最初的解释与该术语的吉布森（Gibsonian）含义并不完全一致 (Norman, 1999; McGrenere and Ho, 2000; Tornvliet, 2003; Soegaard, 2008)。有观点认为，吉布森的可供性理论与 HCI 的相关性有限，因为它无法为理解人类与技术的具体交互以及通过技术执行的操作提供足够的支持 (Albrechtsen et al., 2001; Baerntsen and Trettvik, 2002; Turner, 2005; Rizzo, 2006; Kaptelinin and Nardi, 2012)。Norman 本人也多次尝试淡化可供性在 HCI 和交互设计（Interaction Design）中的作用 (Norman, 1999, 2008, 2011)。随后，人们提出了替代性或补充性的概念，例如示能符（Signifiers）和前馈（Feedforward） (Norman, 2011; Vermeulen et al., 2013)。因此，目前该领域对于可供性概念的含义和作用存在很大程度的不确定性。虽然将可供性普遍理解为“环境所提供的动作可能性（Action Possibilities）”已获得广泛认可，但对这一通用理念的具体解读在不同的研究语境下却有所不同。

广义上来说，该

人机交互（Human-Computer Interaction, HCI）中的可供性（Affordances）概念被用于三个相关但不同的研究议程，这些议程主要分别关注于理解和支持：(a) 直接感知（direct perception），(b) 一般的有目的的用户行为（purposeful user action），以及 (c) 意义构建（meaning making）。每一个关注点都与一种特定的可供性视角相关联。

支持对合适用户行为的*直接感知*，是将可供性概念引入 HCI 的最初初衷 (Norman, 1988; Gaver, 1991)。在该研究议程中，对可供性的解释接近于 Gibson 的概念，但不同之处在于，“直接感知”并不一定是在 Gibson 的反表征主义（anti-representationalist）意义上被理解的；它可能仅仅是指在弄清楚如何使用一个人工制品（artifact）时，不需要标签或指令 (Norman, 1988)。将可供性（Affordances）作为一种分析工具，用以开发*一般意义上有目的的人类行为的技术支持*，是对“直接感知（direct perception）”研究议程的延伸。将可供性作为此类分析工具通常有两种通用策略。

第一种策略是：(a) 提供一套层级化组织的可供性系统，即行动可能性（action possibilities），通过这些可能性的共同作用使用户能够实现其有意义的目标；(b) 支持用户感知这些行动可能性 (Vicente and Rasmussen, 1990; McGrenere and Ho, 2000)。第二种策略是关注某个特定动作的“执行-评估（execution-evaluation）”循环。该循环利用 Norman (1988) 提出的行动模型（model of action）被分解为若干具体阶段，随后通过应用可供性概念——无论是单独应用 (Hartson, 2003)，还是结合其他相关概念应用 (Vermeulen et al., 2013)——来识别在每个阶段支持用户的可能方式。无论采用哪种策略，感知在分析中都起着关键作用。然而，“直接”感知与“间接（indirect）”感知之间的区别通常是次要的。

最后，在一些较近期的研究中 (Turner, 2006; Rizzo, 2006; Vyas et al., 2006; Vyas et al., 2008)，有学者建议进一步扩展该概念的范围，将其涵盖至*社会语境下的意义构建（meaning making in social context）*。基于 Gibson 原始概念的可供性观念，是

被认为具有局限性，因为它仅描述了最基础类型的可供性（Affordances）（例如，“简单可供性 [simple affordances]”，Turner, 2005）。有观点认为，需要一个更先进的概念，在该概念下，可供性被理解为在社会和文化语境中，个体和集体行动的涌现可能性（emerging possibilities），是由技术用户在日常实践中通过实践（doing）和解释（interpretation）共同主动构建的。该研究议程（research agenda）的分析重点不在于“感知-行动（perception – action）”循环，而在于人们通常如何根据环境提供的行动可能性来理解世界。因此，与其他研究议程不同，感知（perception）在此要么被顺带提及，要么完全不被提及。

这些研究议程中的每一个都面临着各自的挑战。到目前为止，关于可供性直接感知（direct perception）的分析大多处理的是物理或物理/虚拟行动，例如抓握门把手或点击屏幕上的按钮（例如，Norman, 1988; Gaver, 1991）。虽然在理论上可行，但如何支持对“非物理（non-physical）”行动可能性的直接感知（例如调用一个抽象逻辑功能，见 McGrenere and Ho, 2000），仍然是一个尚未解决的问题。这个问题与理解直接感知在学习过程中是如何形成的密切相关，也就是说，一个最初的间接感知过程是如何转化为直接感知过程的。

使用

将可供性（Affordances）作为设计有目的行动（purposeful action）支持的分析工具，引发了以下问题：(a) 在人机交互（HCI）研究中确定的可供性类型和属性（例如 Gaver, 1991 提出的“顺序可供性 [sequential affordances]”或 McGrenere and Ho, 2000 提出的“可供性程度 [degrees of affordances]”）如何系统地应用于交互设计（interaction design）；(b) 可供性的概念是否可以应用于行动的阶段（stages of an action）而非整个行动（whole actions）（Hartson, 2003; Vermeulen et al., 2013）。最后，在意义构建（meaning making）研究中尝试采用可供性概念的努力（Turner, 2005; Vyas et al, 2006; Vyas et al., 2008），尚未对该术语的新理解给出清晰的定义，也未能证明其相对于其他现有概念的“附加值（added value）”。

### 44.6.2 与替代概念相关的挑战

正如前一节所述，可供性（Affordances）这一概念涉及许多术语上的不确定性以及其他概念上的挑战。因此，一个逻辑上的问题是：使用人机交互（HCI）研究中提出的替代或补充概念（至少在部分情况下），例如示能符（Signifiers）或前馈（Feedforward），是否会是一个更好的解决方案？让我们逐一探讨这些替代方案。

示能符概念（Norman, 2008, Norman, 2011, Norman, 2013）的一个明显优势在于，它为设计师提供了广泛的可能性，使其能够引导、指示以及在其他方面支持人们应对由交互人工制品（Interactive Artifacts）、实践（Practices）和（社会）环境（(Social) Environments）构成的复杂配置。设计师不再狭隘地关注于帮助用户操作某个特定的设备，而是被鼓励去思考如何支持人们处理具有实际意义的现实生活问题。提供能够帮助人们在日常情境中做出正确决策的高效线索，成为了设计的核心目标。

然而，这一优势的另一面是，该概念的含义变得极其宽泛。示能符被定义为“任何可感知的、关于适当行为的符号，无论是有意还是无意地产生”（Norman, 2011），因此它几乎可以指代任何感官可获取的信息。可能是由此产生的最大问题是

由于该概念含义广泛且与可供性（Affordances）严格区分，导致示能符（Signifiers）这一概念在区分成功设计与不成功设计方面几乎没有提供指导。显然，并非所有示能符的效果都一样好。根据 Norman (2011) 的观点，使用某些类型的示能符是设计糟糕的迹象，例如标签（如“推”）或解释如何操作设备的手写标志。因此，一个真正的问题在于如何选择或设计*正确*的示能符。这个问题在很大程度上仍然没有定论。一个可能的解决办法是将示能符的概念与支持直接感知（Direct Perception）的概念更紧密且明确地联系起来（这可能意味着需要引入 Gibson 的可供性理论所提供的一些见解）。前馈（Feedforward）的概念（Djajadiningrat et al., 2002, Vermeulen et al., 2013）面临着类似的挑战。与可供性（Affordances）相比，前馈在为设计师提供更具体的指导方面具有怎样的附加值？例如，基于前馈的概念，可以使用哪些具体标准来区分更成功的设计与较不成功的设计？一个直接的建议（源于将前馈概念引入设计）是，设计师应当关注如何告知用户其操作的结果。这一建议无疑是有用的，但它也相当笼统。

此外，尽管在区分“前馈”与“可供性”的含义方面已取得了显著进展（Vermeulen et al., 2013），但在如何准确区分这两个概念方面仍存在一些不确定性。简单地声称可供性是指动作，而前馈是指动作的结果，似乎是不够的，因为在某些情况下，将动作与其结果分开可能会产生问题。例如，“打印预览”似乎是一个典型的前馈案例。但窗口的“关闭”按钮告知用户的是*结果*（即窗口被关闭），还是告知的是关闭这一*动作*（该动作可能会被误用，导致用户意外关闭错误的窗口）？

因此，尽管示能符（Signifiers）和前馈这两个概念似乎都提供了

这些重要的洞察（insights）、其具体含义、它们与可供性（Affordances）的关系，以及对分析与设计的启示，仍需进一步探讨。

### 44.6.3 可供性作为人机交互（HCI）概念的未来如何？

未来的人机交互（Human-Computer Interaction, HCI）关于可供性（Affordances）的研究预计会有怎样的发展？在目前对可供性的各种解释中，哪一种（如果有的话）将在该领域发挥核心作用？这个术语是否会被弃用，而转而采用其他概念，例如示能符（Signifiers）或前馈（Feedforward）？虽然可能没有人能肯定地回答这些问题，但可以谨慎地认为，可供性及其相关概念在 HCI 中的未来，将主要取决于它们是否能被清晰地定义，并证明其具有实际的相关性。

正如上文所述，目前 HCI 对可供性的探索存在的一个主要问题是，由于该领域对该术语的解释多样，从而导致了不确定性。为了成为一个有用的概念工具，对可供性的新解释以及其他提出的概念（如示能符或前馈）需要被清晰地呈现，并与其他解释（尤其是最初的吉布森意义 [Gibsonian meaning]）进行明确的对比，并被置于特定的研究语境中。

另一个重要的挑战是确保一个概念具有实际的相关性和实用性，即它能提供新的见解，帮助从业者处理交互技术在分析、设计、评估以及[挪用（Appropriation）](https://www.interaction-design.org/literature/topics/appropriation)方面的具体问题。

当可供性首次被提出作为设计概念时，它立即

[被] 认为具有实际应用价值。例如，它建议将用户界面对象设计得像熟悉的物理对象，可以帮助用户了解如何操作该对象。但这已不再是一个新颖的想法：现代界面中充斥着各种屏幕按钮、旋钮、滑块等。看来，最初引入人机交互（Human-Computer Interaction, HCI）的可供性（Affordances）概念，对于设计从业者来说已经非常熟悉了。

HCI 研究中对可供性的分析提出了一些高级的概念区分，从而能够更具体地定义可供性。通过应用顺序可供性（sequential affordances）和嵌套可供性（nested affordances）、可供性程度（degree of affordance）以及工具性可供性（instrumental affordances）的结构等概念，可以识别出可供性的不同类型和组成部分。这些见解为设计师提供了新的可能性，以帮助人们解决与现代交互技术使用相关的问题。可以说，如今的用户不再对单个界面对象（如按钮）感到困惑。相反，他们可能会发现，在时间和空间维度上组织起来的复杂可供性配置（complex configurations of affordances）难以发现和学习，难以评估执行某种可供性所需的努力，以及难以将工具与目标对象之间的相互可供性（mutual affordances）联系起来，以了解该工具提供了哪些行动可能性。对可供性进行高级理论分析的一个局限性在于，它们很少能促成分析性（analytical）...

……适用于实际情境中技术分析、设计和评估具体任务的工具。将人机交互（Human-Computer Interaction, HCI）中关于可供性（Affordances）研究的新理论洞察进行操作化（Operationalizing），是提高该研究对从业者相关性的一种方式。

总之，在 HCI 中采用可供性（或相关概念）的新概念化（Conceptualizations）所面临的主要挑战包括：明确该概念的含义及其在特定研究议程（Research Agenda）中的地位，并使其对设计师和其他 HCI 从业者具有实用性和相关性。能否实现这一点，似乎对于决定可供性作为一项 HCI 概念的未来至关重要。

## 44.7 延伸阅读


### 44.7.1 可供性（Affordances）与生态心理学（Ecological Psychology）概论

- Gibson, J. J. The theory of affordances. In: R. Shaw and J. Bransford (eds.) *Perceiving, Acting and Knowing*. Hillsdale, NJ: Erlbaum (1977).
- Gibson, J. J. *The Ecological Approach to Visual Perception*. Boston: Houghton Mifflin (1979).
- Gibson, E. J. and Pick, A. D. *An Ecological Approach to Perceptual Learning and Development*. Cary, NC: Oxford University Press (2003).
- Heft, H. *Ecological psychology in context: James Gibson, Roger Barker, and the legacy of William James’s radical empiricism*. Lawrence Erlbaum, Mahwah, N.J., (2001).
- Norman, Donald A. (2013): The Design of Everyday Things: Revised and Expanded Edition. Basic Books.
- Sanders, J.T. An ontology of affordances. *Ecological Psychology*, 9 (1997), 97-112.
- Stoffregen, T. A. Affordances as Properties of the Animal-Environment System. *Ecological Psychology*, 15, 2 (2003), 115-134.
- Wagman, J. and Carello, C. Haptically creating affordances: The user–tool interface. *Journal of Experimental Psychology: Applied*, 9, 4 (2003), 175-186.
- Warren, W. (1995). Constructing an econiche. In J. Flach, P. Hancock, J. Caird, & K. Vicente (Eds.) *Global perspectives on the ecology of human-machine systems*. Hillsdale, NJ: Erlbaum (1995), 210-237.

### 44.7.2 人机交互（HCI）中的可供性（Affordances）

- Baerentsen, K. B. and Trettvik, J. 基于活动理论（Activity Theory）的可供性研究方法。In *Proceedings of NordiCHI 2002.* ACM Press, NY (2002), 51-60.
- Bonderup Dohn, N. 重新审视可供性：阐述一种梅洛-庞蒂（Merleau-Pontian）的视角。*International Journal of Computer-Supported Collaborative Learning,* 4, 2 (2009), 151-170.
- Gaver, W. 技术可供性（Technology affordances）。In Proceedings of CHI 91. ACM Press: NY (1991), 79-84.
- Gaver, W. 用于协作的媒介空间（Media spaces）的可供性。In Proceedings of CSCW 92. ACM Press: NY (1992), 17-24.
- Hartson, R. 交互设计（Interaction design）中的认知、物理、感官和功能可供性（Cognitive, physical, sensory, and functional affordances）。*Behaviour & Information Technology*, 22, 5 (2003), 315–338.
- Kaptelinin, V. and Nardi, B. 人机交互中的可供性：迈向一种中介行动（Mediated action）视角。In *Proceedings of CHI 2012.* ACM Press, NY (2012).
- McGrenere, J., and Ho, W. 可供性：概念的澄清与演进。In *Proceedings of Graphic Interfaces 2000*. New York: ACM Press (2000), 179-186.
- Norman, D. A. *The Psychology of Everyday Things.* Basic Books, New York (1988).
- Norman, D. A. 可供性、惯例（Conventions）与设计。*interactions*, 6 (3), (1999), 38-43.
- Norman, D. 示能符（Signifiers）而非可供性。*interactions*, 15, 6 (2008).
- Norman, D. *Living with Complexity*. Cambridge, Mass.: The MIT Press (2011).
- Rizzo, A. 意向可供性（Intentional affordances）的起源与设计。In *Proceedings of DIS 2006*. New York: ACM Press (2006).

- Still, J. D., Dark, V. J. 从认知角度描述和设计可供性（Affordances）。*Design Studies*, 34 (2013), 285-301.
- Turner, P. 作为上下文（Context）的可供性。*Interacting with Computers*, 17 (6), (2005), 787-800.
- Vyas, D., Chisalita, C. M., and van der Veer, G. C. 交互中的可供性。In *Proc. ECCE 2006*. Zurich, Switzerland (2006), 92-99.

## 44.8 致谢

我要感谢 Mads Soegaard, Bonnie Nardi, Antonio Rizzo 以及六位匿名评审员对本章之前版本提出的富有洞察力的建议。非常感谢 Peter Larsen 和 Rune Arntsen 在展示 Holmes 立体镜（Holmes stereoscope）示例方面提供的帮助。

## 44.9 免责声明

部分读者可能会觉得本章的讨论有时并不像人们对百科全书章节所期望的那样客观和中立。问题在于，当前人机交互（Human-Computer Interaction, HCI）领域关于可供性（Affordances）的争论存在许多强有力且有时相互矛盾的观点，很难对其进行精确的平衡。幸运的是，这部*在线*百科全书的“评论”功能为处理这一问题提供了一些可供性（affordances）。

## 44.10 References

[Albrechtsen](https://www.interaction-design.org/references/authors/h__albrechtsen.html), H., [Andersen](https://www.interaction-design.org/references/authors/hans_h-dot-k__andersen.html), Hans H.K., [Bodker](https://www.interaction-design.org/references/authors/s__bodker.html), S. and [Pejtersen](https://www.interaction-design.org/references/authors/annelise_m__pejtersen.html), Annelise M. (2001). *Affordances in Activity Theory and Cognitive Systems Engineering*. Risø National Laboratory[http://www.risoe.dk/rispubl/SYS/syspdf/ris-r-1287.pdf](http://www.risoe.dk/rispubl/SYS/syspdf/ris-r-1287.pdf)
[Baerentsen](https://www.interaction-design.org/references/authors/klaus_b__baerentsen.html), Klaus B. (2000): *Intuitive User Interfaces*. In [Scandinavian Journal of Information Systems](https://www.interaction-design.org/references/periodicals/scandinavian_journal_of_information_systems.html), 12 pp. 29-60

[Baerentsen](https://www.interaction-design.org/references/authors/klaus_b__baerentsen.html), Klaus B. and [Trettvik](https://www.interaction-design.org/references/authors/johan_trettvik.html), Johan (2002): An Activity Theory Approach to Affordance. In: [Bertelsen](https://www.interaction-design.org/references/authors/olav_w__bertelsen.html), Olav W., [Boedker](https://www.interaction-design.org/references/authors/susanne_boedker.html), Susanne and [Kuutti](https://www.interaction-design.org/references/authors/kari_kuutti.html), Kari (eds.) [Nordichi 2002 - Proceedings of the Second Nordic Conference on Human-Computer Interaction](https://www.interaction-design.org/references/conferences/nordichi_2002_-_proceedings_of_the_second_nordic_conference_on_human-computer_interaction.html) October 19-23, 2002, Aarhus, Denmark. pp. 51-60

[Beaudouin-Lafon](https://www.interaction-design.org/references/authors/michel_beaudouin-lafon.html), Michel (2000): Instrumental Interaction: An Interaction Model for Designing Post-WIMP User Interfaces. In: [Turner](https://www.interaction-design.org/references/authors/thea_turner.html), Thea, [Szwillus](https://www.interaction-design.org/references/authors/gerd_szwillus.html), Gerd, [Czerwinski](https://www.interaction-design.org/references/authors/mary_czerwinski.html), Mary, [Peterno](https://www.interaction-design.org/references/authors/fabio_peterno.html), Fabio and [Pemberton](https://www.interaction-design.org/references/authors/steven_pemberton.html), Steven (eds.)[Proceedings of the ACM CHI 2000 Human Factors in Computing Systems Conference](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_2000_human_factors_in_computing_systems_conference.html) April 1-6, 2000, The Hague, The Netherlands. pp. 446-453
[Boedker](https://www.interaction-design.org/references/authors/susanne_boedker.html), Susanne (1991): *Through the Interface - A Human Activity Approach to User Interface Design.*Hillsdale, NJ, Lawrence Erlbaum Associates

[Boedker](https://www.interaction-design.org/references/authors/susanne_boedker.html), Susanne and [Andersen](https://www.interaction-design.org/references/authors/peter_b__andersen.html), Peter B. (2005): *Complex Mediation*. In [Human-Computer Interaction](https://www.interaction-design.org/references/periodicals/human-computer_interaction.html), 20 (4) pp. 353-402
[Bradner](https://www.interaction-design.org/references/authors/erin_bradner.html), Erin (2001): Social affordances of computer-mediated communication technology: Understanding adoption. In: [Proceedings of CHI 01, Extended Abstracts on Human Factors in Computing](https://www.interaction-design.org/references/conferences/proceedings_of_chi_01%2C_extended_abstracts_on_human_factors_in_computing.html) March 31- April 5, 2001, Seattle, USA. pp. 67-68
[Brown](https://www.interaction-design.org/references/authors/john_s__brown.html), John S. and [Duguid](https://www.interaction-design.org/references/authors/paul_duguid.html), Paul (1994): *Borderline Issues: Social and Material Aspects of Design*. In [Human-Computer Interaction](https://www.interaction-design.org/references/periodicals/human-computer_interaction.html), 9 (1) pp. 3-36

[Cairns](https://www.interaction-design.org/references/authors/paul_cairns.html), Paul and [Thimbleby](https://www.interaction-design.org/references/authors/harold_thimbleby.html), Harold (2008): *Affordance and symmetry in user interfaces*. In [The Computer Journal](https://www.interaction-design.org/references/periodicals/the_computer_journal.html), 51 (6) pp. 650-661
[Chen](https://www.interaction-design.org/references/authors/li-hao_chen.html), Li-Hao, [Lee](https://www.interaction-design.org/references/authors/chang-franw_lee.html), Chang-Franw and [Tsai](https://www.interaction-design.org/references/authors/cheng-min_tsai.html), Cheng-Min (2007): Perceiving affordances through perceptual information. In: [Poggenpohl](https://www.interaction-design.org/references/authors/sharon_poggenpohl.html), Sharon (ed.) [Proceedings of IASDR 07](https://www.interaction-design.org/references/conferences/proceedings_of_iasdr_07.html) November 12-15, 2007, Hong Kong, China.

[Davis](https://www.interaction-design.org/references/authors/tehran_j__davis.html), Tehran J., [Riley](https://www.interaction-design.org/references/authors/michael_a__riley.html), Michael A., [Shockley](https://www.interaction-design.org/references/authors/kevin_shockley.html), Kevin and [Cummins-Sebree](https://www.interaction-design.org/references/authors/sarah_cummins-sebree.html), Sarah (2010): *Perceiving affordances for joint actions*. In [Perception](https://www.interaction-design.org/references/periodicals/perception.html), 39 (2) pp. 1624-1644
[Djajadiningrat](https://www.interaction-design.org/references/authors/tom_djajadiningrat.html), Tom, [Overbeeke](https://www.interaction-design.org/references/authors/kees_overbeeke.html), Kees and [Wensveen](https://www.interaction-design.org/references/authors/stephan_wensveen.html),
 Stephan (2002): But how, Donald, tell us how?: on the creation of 
meaning in interaction design through feedforward and inherent feedback.
 In: [Proceedings of DIS02: Designing Interactive Systems: Processes, Practices, Methods, & Techniques](https://www.interaction-design.org/references/conferences/proceedings_of_dis02-_designing_interactive_systems-_processes%2C_practices%2C_methods%2C_%26_techniques.html) 2002. pp. 285-291

[Djajadiningrat](https://www.interaction-design.org/references/authors/tom_djajadiningrat.html), Tom, [Wensveen](https://www.interaction-design.org/references/authors/stephan_wensveen.html), Stephan, [Frens](https://www.interaction-design.org/references/authors/joep_frens.html), Joep and [Overbeeke](https://www.interaction-design.org/references/authors/kees_overbeeke.html), Kees (2004): *Tangible Products: redressing the balance between appearance and action*. In [Personal and Ubiquitous Computing](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing.html), 8 (5) pp. 294-309
[Dohn](https://www.interaction-design.org/references/authors/nina_bonderup_dohn.html), Nina Bonderup (2009): *Affordances revisited: Articulating a Merleau-Pontian view*. In [International Journal of Computer-Supported Collaborative Learning](https://www.interaction-design.org/references/periodicals/international_journal_of_computer-supported_collaborative_learning.html), 4 (2) pp. 151-170
[Dourish](https://www.interaction-design.org/references/authors/paul_dourish.html), Paul (2001): *Where the Action Is: The Foundations of Embodied Interaction.* MIT Press
[Gaver](https://www.interaction-design.org/references/authors/william_w__gaver.html), William W. (1996): *Affordances for interaction: The social is material for design*. In [Ecological psychology](https://www.interaction-design.org/references/periodicals/ecological_psychology.html), 8 (2) pp. 111-129

[Gaver](https://www.interaction-design.org/references/authors/william_w__gaver.html), William W. (1992): The Affordances of Media Spaces for Collaboration. In: [Proceedings of the 1992 ACM conference on Computer-supported cooperative work](https://www.interaction-design.org/references/conferences/proceedings_of_the_1992_acm_conference_on_computer-supported_cooperative_work.html) November 01 - 04, 1992, Toronto, Ontario, Canada. pp. 17-24
[Gaver](https://www.interaction-design.org/references/authors/william_w__gaver.html), William W. (1986): *Auditory Icons: Using Sound in Computer Interfaces*. In [Human-Computer Interaction](https://www.interaction-design.org/references/periodicals/human-computer_interaction.html), 2 (2) pp. 167-177
[Gaver](https://www.interaction-design.org/references/authors/william_w__gaver.html), William W. (1991): Technology Affordances. In: [Robertson](https://www.interaction-design.org/references/authors/scott_p__robertson.html), Scott P., [Olson](https://www.interaction-design.org/references/authors/gary_m__olson.html), Gary M. and [Olson](https://www.interaction-design.org/references/authors/judith_s__olson.html), Judith S. (eds.) [Proceedings of the ACM CHI 91 Human Factors in Computing Systems Conference](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_91_human_factors_in_computing_systems_conference.html) April 28 - June 5, 1991, New Orleans, Louisiana. pp. 79-84

[Gibson](https://www.interaction-design.org/references/authors/james_j__gibson.html), James J. (1979): *The Ecological Approach to Visual Perception.* New Jersey, USA, Lawrence Erlbaum Associates
[Gibson](https://www.interaction-design.org/references/authors/james_j__gibson.html), James J. (1977): The theory of affordances. In: [Shaw](https://www.interaction-design.org/references/authors/robert_shaw.html), Robert and [Bransford](https://www.interaction-design.org/references/authors/john_bransford.html), John (eds.). "Perceiving, Acting and Knowing". Hillsdale, USA: Lawrence Erlbaum
[Gibson](https://www.interaction-design.org/references/authors/eleanor_j__gibson.html), Eleanor J. and [Pick](https://www.interaction-design.org/references/authors/anne_d__pick.html), Anne D. (2003): *An Ecological Approach to Perceptual Learning and Development.*Cary, USA, Oxford University Press
[Giddens](https://www.interaction-design.org/references/authors/anthony_giddens.html), Anthony (1984): *The constitution of society: Outline of the theory of structuration.* University of California Press
[Hartson](https://www.interaction-design.org/references/authors/h__rex_hartson.html), H. Rex (2003): *Cognitive, physical, sensory, and functional affordances in interaction design*. In[Behaviour and Information Technology](https://www.interaction-design.org/references/periodicals/behaviour_and_information_technology.html), 22 (5) pp. 315-338

[Heft](https://www.interaction-design.org/references/authors/harry_heft.html), Harry (2001): *Ecological psychology in context: James Gibson, Roger Barker, and the legacy of William James s radical empiricism.* Mahwah, USA, Lawrence Erlbaum
[Heidegger](https://www.interaction-design.org/references/authors/martin_heidegger.html), Martin (1962): *Being and Time. English translation 1962.*
[Ihara](https://www.interaction-design.org/references/authors/masayuki_ihara.html), Masayuki, [Kobayashi](https://www.interaction-design.org/references/authors/minoru_kobayashi.html), Minoru and [Sakai](https://www.interaction-design.org/references/authors/yoshinori_sakai.html), Yoshinori (2009): *Human affordance*. In [International Journal of Web Based Communities](https://www.interaction-design.org/references/periodicals/international_journal_of_web_based_communities.html), 5 (2) pp. 255-272
[Ilyenkov](https://www.interaction-design.org/references/authors/evald_v__ilyenkov.html),
 Evald V. (1977): The concept of the ideal. In: (ed.). "Philosophy in 
the USSR: Problems of Dialectical Materialism". Moscow, Russia: Progress
 Publisherspp. 71-99
[Judah](https://www.interaction-design.org/references/authors/sam_judah.html), Sam (2013). *What is skeuomorphism*. Retrieved 16 October 2013 from BBC.co.uk: [http://www.bbc.co.uk/news/magazine-22840833](http://www.bbc.co.uk/news/magazine-22840833)

[Kaptelinin](https://www.interaction-design.org/references/authors/victor_kaptelinin.html), Victor (1993): Item recognition in menu selection: The effect of practice. In: [Adjunct proceedings of INTERCHI93](https://www.interaction-design.org/references/conferences/adjunct_proceedings_of_interchi93.html) April 24-29, 1993, Amsterdam, Netherlands. pp. 183-184
[Kaptelinin](https://www.interaction-design.org/references/authors/victor_kaptelinin.html), Victor and [Nardi](https://www.interaction-design.org/references/authors/bonnie_nardi.html), Bonnie (2012): Affordances in HCI: toward a mediated action perspective. In:[Höök](https://www.interaction-design.org/references/authors/kristina_h%C3%B6%C3%B6k.html), Kristina (ed.) [Proceedings of CHI 2012](https://www.interaction-design.org/references/conferences/proceedings_of_chi_2012.html) May 05-10, 2012, Austin, USA. pp. 967-976
[Kaptelinin](https://www.interaction-design.org/references/authors/victor_kaptelinin.html), Victor and [Nardi](https://www.interaction-design.org/references/authors/bonnie_a__nardi.html), Bonnie A. (2006): *Acting with Technology: Activity Theory and Interaction Design.*The MIT Press
[Kirlik](https://www.interaction-design.org/references/authors/alex_kirlik.html), Alex (2004): *On Stoffregen's definition of affordances*. In [Ecological psychology](https://www.interaction-design.org/references/periodicals/ecological_psychology.html), 16 (1) pp. 73-77

[Laarni](https://www.interaction-design.org/references/authors/jari_laarni.html), Jari, [Norros](https://www.interaction-design.org/references/authors/leena_norros.html), Leena and [Koskinen](https://www.interaction-design.org/references/authors/hanna_maria_kaarina_koskinen.html), Hanna Maria Kaarina (2007): Affordance Table - A Collaborative Smart Interface for Process Control. In: [Jacko](https://www.interaction-design.org/references/authors/julie_a__jacko.html), Julie A. (ed.) [HCI International 2007 - 12th International Conference - Part IV](https://www.interaction-design.org/references/conferences/hci_international_2007_-_12th_international_conference_-_part_iv.html) 2007. pp. 611-619
[Leontyev](https://www.interaction-design.org/references/authors/aleksei_n__leontyev.html), Aleksei N. (1978): *Activity, consciousness, and personality.* Pergamon Press
[McGrenere](https://www.interaction-design.org/references/authors/joanna_mcgrenere.html), Joanna and [Ho](https://www.interaction-design.org/references/authors/wayne_ho.html), Wayne (2000): Affordances: Clarifying and Evolving a Concept. In:[Proceedings of Graphics Interface 2000](https://www.interaction-design.org/references/conferences/proceedings_of_graphics_interface_2000.html) May 15-17, 2000, Montreal, Quebec, Canada. pp. 179-186
[Merleau-Ponty](https://www.interaction-design.org/references/authors/maurice_merleau-ponty.html), Maurice (1962): *Phenomenology of Perception: An Introduction.* Routledge

[Michaels](https://www.interaction-design.org/references/authors/claire_f__michaels.html), Claire F. and [Carello](https://www.interaction-design.org/references/authors/claudia_carello.html), Claudia (1981): *Direct Perception.* Prentice Hall
[Nardi](https://www.interaction-design.org/references/authors/bonnie_a__nardi.html), Bonnie A. (ed.) (1996): *Context and Consciousness: Activity Theory and Human-Computer Interaction.*MIT Press
[Norman](https://www.interaction-design.org/references/authors/donald_a__norman.html), Donald A. (2008): *Signifiers, not affordances*. In [Interactions](https://www.interaction-design.org/references/periodicals/interactions.html), 15 (6) pp. 18-19
[Norman](https://www.interaction-design.org/references/authors/donald_a__norman.html), Donald A. (2010): *Living with Complexity.* The MIT Press
[Norman](https://www.interaction-design.org/references/authors/donald_a__norman.html), Donald A. (2013): *The Design of Everyday Things: Revised and Expanded Edition.* Basic Books
[Norman](https://www.interaction-design.org/references/authors/donald_a__norman.html), Donald A. (1999): *Affordances, Conventions, and Design*. In [Interactions](https://www.interaction-design.org/references/periodicals/interactions.html), 6 (3) pp. 38-41
[Norman](https://www.interaction-design.org/references/authors/donald_a__norman.html), Donald A. (1988): *The Psychology of Everyday Things.* New York, Basic Books

[Norman](https://www.interaction-design.org/references/authors/donald_a__norman.html), Donald A. (1991): Cognitive artifacts. In: [Carroll](https://www.interaction-design.org/references/authors/john_m__carroll.html),
 John M. (ed.). "Designing Interaction: Psychology at the Human-Computer
 Interface". Cambridge, UK: Cambridge University Presspp. 17-38
[Norman](https://www.interaction-design.org/references/authors/donald_a__norman.html), Donald A. (1993): *Things That Make Us Smart.* Reading, USA, Addison-Wesley
[Norman](https://www.interaction-design.org/references/authors/donald_a__norman.html), Donald A. (1998): *The
 Invisible Computer: Why Good Products Can Fail, the Personal Computer 
Is So Complex and Information Appliances Are the Solution.* MIT Press

[O'Brien](https://www.interaction-design.org/references/authors/marita_a__o%27brien.html), Marita A., [Rodgers](https://www.interaction-design.org/references/authors/wendy_a__rodgers.html), Wendy A. and [Fisk](https://www.interaction-design.org/references/authors/arthur_d__fisk.html), Arthur D. (2010). *Developing An Organizational Model For *[*Intuitive Design*](https://www.interaction-design.org/literature/topics/intuitive-design). Georgia Institute of Technology[https://smartech.gatech.edu/bitstream/handle/1853/40563/HFA-TR-1001-IntuitiveDesignConceptualOverview.pdf;jsessionid=415E22D63DB9A9E52259BDAE0EC972DF.smart2?sequence=1](https://smartech.gatech.edu/bitstream/handle/1853/40563/HFA-TR-1001-IntuitiveDesignConceptualOverview.pdf;jsessionid=415E22D63DB9A9E52259BDAE0EC972DF.smart2?sequence=1)
[Oshlyansky](https://www.interaction-design.org/references/authors/lidia_oshlyansky.html), Lidia, [Thimbleby](https://www.interaction-design.org/references/authors/harold_thimbleby.html), Harold and [Cairns](https://www.interaction-design.org/references/authors/paul_cairns.html), Paul (2004): Breaking affordance: culture as context. In:[Proceedings of the Third Nordic Conference on Human-Computer Interaction](https://www.interaction-design.org/references/conferences/proceedings_of_the_third_nordic_conference_on_human-computer_interaction.html) October 23-27, 2004, Tampere, Finland. pp. 81-84

[Overbeeke](https://www.interaction-design.org/references/authors/kees_overbeeke.html), Kees and [Hummels](https://www.interaction-design.org/references/authors/caroline_hummels.html), Caroline (2014): [Industrial Design](https://www.interaction-design.org/literature/topics/industrial-design). In: [Soegaard](https://www.interaction-design.org/references/authors/mads_soegaard.html), Mads and [Dam](https://www.interaction-design.org/references/authors/rikke_friis_dam.html),
 Rikke Friis (eds.). "The Encyclopedia of Human-Computer Interaction, 
2nd Ed.". Aarhus, Denmark: The Interaction Design Foundation. Available 
online at [https://www.interaction-design.org/encyclopedia/industrial_design.html](https://www.interaction-design.org/encyclopedia/industrial_design.html)
[Overbeeke](https://www.interaction-design.org/references/authors/kees_overbeeke.html), Kees and [Wensveen](https://www.interaction-design.org/references/authors/stephan_wensveen.html), Stephan (2003): From perception to experience, from affordances to irresistibles. In: [DPPI 2003 - Proceedings of the 2003 International Conference on Designing Pleasurable Products and Interfaces](https://www.interaction-design.org/references/conferences/dppi_2003_-_proceedings_of_the_2003_international_conference_on_designing_pleasurable_products_and_interfaces.html) June 23-26, 2003, Pittsburgh, PA, USA. pp. 92-97

[Raskin](https://www.interaction-design.org/references/authors/jef_raskin.html), Jef (1994): *Viewpoint: Intuitive equals familiar*. In [Communications of the ACM](https://www.interaction-design.org/references/periodicals/communications_of_the_acm.html), 37 (9) pp. 17-18
[Rasmussen](https://www.interaction-design.org/references/authors/jens_rasmussen.html), Jens and [Vicente](https://www.interaction-design.org/references/authors/kim_j__vicente.html), Kim J. (1989): *Coping with Human Errors through System Design: Implications for Ecological Interface Design*. In [International Journal of Man-Machine Studies](https://www.interaction-design.org/references/periodicals/international_journal_of_man-machine_studies.html), 31 (5) pp. 517-534
[Rizzo](https://www.interaction-design.org/references/authors/antonio_rizzo.html), Antonio (2006): The origin and design of intentional affordances. In: [Proceedings of DIS06: Designing Interactive Systems: Processes, Practices, Methods, & Techniques](https://www.interaction-design.org/references/conferences/proceedings_of_dis06-_designing_interactive_systems-_processes%2C_practices%2C_methods%2C_%26_techniques.html) 2006. pp. 239-240

[Rizzo](https://www.interaction-design.org/references/authors/a__rizzo.html), A., [DeMonte](https://www.interaction-design.org/references/authors/m__demonte.html), M., [Rubegni](https://www.interaction-design.org/references/authors/e__rubegni.html), E. and [Torsi](https://www.interaction-design.org/references/authors/s__torsi.html),
 S. (2009): The interplay between sensory-motor and intentional 
affordances. Workshop on Children and Embodied Interaction at IDC09. In:
 [IDC09](https://www.interaction-design.org/references/conferences/idc09.html) June, 2009, Como, Italy.
[Rizzolatti](https://www.interaction-design.org/references/authors/giacomo_rizzolatti.html), Giacomo and [Craighero](https://www.interaction-design.org/references/authors/laila_craighero.html), Laila (2004): *The Mirror-Neuron System*. In [Annual Review of Neuroscience](https://www.interaction-design.org/references/periodicals/annual_review_of_neuroscience.html), 27 pp. 169-192
[Rogers](https://www.interaction-design.org/references/authors/yvonne_rogers.html), Yvonne (2004): *New Theoretical Approaches for HCI*. In [Annual Review of Information Science and Technology](https://www.interaction-design.org/references/periodicals/annual_review_of_information_science_and_technology.html), (38) pp. 1-43

[Rogers](https://www.interaction-design.org/references/authors/yvonne_rogers.html), Yvonne (2012): *HCI Theory: Classical, Modern, and Contemporary*. In [Synthesis Lectures on Human-Centered Informatics](https://www.interaction-design.org/references/periodicals/synthesis_lectures_on_human-centered_informatics.html), 5 (2) pp. 1-129
[Rogers](https://www.interaction-design.org/references/authors/yvonne_rogers.html), Yvonne, [Sharp](https://www.interaction-design.org/references/authors/helen_sharp.html), Helen and [Preece](https://www.interaction-design.org/references/authors/jenny_preece.html), Jenny (2011): *Interaction Design: Beyond Human - Computer Interaction - third edition.* Wiley
[Sanders](https://www.interaction-design.org/references/authors/john_t__sanders.html), John T. (1997): *An ontology of affordances*. In [Ecological psychology](https://www.interaction-design.org/references/periodicals/ecological_psychology.html), 9 (1) pp. 97-112
[Smets](https://www.interaction-design.org/references/authors/gerda_smets.html), Gerda and [Overbeeke](https://www.interaction-design.org/references/authors/kees_overbeeke.html), Kees (1994): *Industrial design engineering and the theory of direct perception*. In [Design Studies](https://www.interaction-design.org/references/periodicals/design_studies.html), 15 (2) pp. 175-184

[Soegaard](https://www.interaction-design.org/references/authors/mads_soegaard.html), Mads (2013). *Affordances*. Retrieved 16 October 2013 from Interaction Design Foundation: [https://www.interaction-design.org/encyclopedia/aff...](https://www.interaction-design.org/encyclopedia/affordances.html)
[Souza](https://www.interaction-design.org/references/authors/clarisse_s__de_souza.html), Clarisse S. de (2007): *Semiotic Engineering of Human-Computer Interaction.* Cambridge, USA, The MIT Press
[Still](https://www.interaction-design.org/references/authors/jeremiah_d__still.html), Jeremiah D. and [Dark](https://www.interaction-design.org/references/authors/veronica_j__dark.html), Veronica J. (2013): *Cognitively describing and designing affordances*. In [Design Studies](https://www.interaction-design.org/references/periodicals/design_studies.html), 34 (3) pp. 285-301
[Stoffregen](https://www.interaction-design.org/references/authors/thomas_a__stoffregen.html), Thomas A. (2003): *Affordances as Properties of the Animal-Environment System*. In [Ecological psychology](https://www.interaction-design.org/references/periodicals/ecological_psychology.html), 15 (2) pp. 115-134

[Suthers](https://www.interaction-design.org/references/authors/daniel_d__suthers.html), Daniel D. (2006): *Technology affordances for intersubjective meaning making: A research agenda for CSCL*. In [International Journal for Computer-Supported Collaborative Learning](https://www.interaction-design.org/references/periodicals/international_journal_for_computer-supported_collaborative_learning.html), 1 (3) pp. 315-337
Technopedia. Skeuomorphism (n/d). Available at: [http://www.techopedia.com/definition/28955/skeuomo...](http://www.techopedia.com/definition/28955/skeuomorphism)
[Tognazzini](https://www.interaction-design.org/references/authors/bruce_tognazzini.html), Bruce (2001). *The Butterfly Ballot: Anatomy of a Disaster*. Retrieved 16 October 2013 from Ask Tog: [http://www.asktog.com/columns/042ButterflyBallot.h...](http://www.asktog.com/columns/042ButterflyBallot.html)
[Tomasello](https://www.interaction-design.org/references/authors/michael_tomasello.html), Michael (1999): *The cultural origins of human cognition.* Cambridge, USA, Harvard University Press
[Torenvliet](https://www.interaction-design.org/references/authors/gerard_torenvliet.html), Gerard (2003): *We can't afford it!: the devaluation of a usability term*. In [Interactions](https://www.interaction-design.org/references/periodicals/interactions.html), 10 (4) pp. 12-17

[Turner](https://www.interaction-design.org/references/authors/phil_turner.html), Phil (2005): *Affordance as context*. In [Interacting with Computers](https://www.interaction-design.org/references/periodicals/interacting_with_computers.html), 17 (6) pp. 787-800
[Turner](https://www.interaction-design.org/references/authors/p__turner.html), P. and [Turner](https://www.interaction-design.org/references/authors/s__turner.html), S. (2002): An Affordance-based Framework for CVE Evaluation. In: [Faulkner](https://www.interaction-design.org/references/authors/xristine_faulkner.html), Xristine,[Finlay](https://www.interaction-design.org/references/authors/janet_finlay.html), Janet and [Détienne](https://www.interaction-design.org/references/authors/fran%C3%A7oise_d%C3%A9tienne.html), Françoise (eds.) [Proceedings of the HCI02 Conference on People and Computers XVI](https://www.interaction-design.org/references/conferences/proceedings_of_the_hci02_conference_on_people_and_computers_xvi.html) September 18-20, 2002, Pisa, Italy. pp. 89-104

[Vermeulen](https://www.interaction-design.org/references/authors/jo_vermeulen.html), Jo, [Luyten](https://www.interaction-design.org/references/authors/kris_luyten.html), Kris, [Hoven](https://www.interaction-design.org/references/authors/elise_van_den_hoven.html), Elise van den and [Coninx](https://www.interaction-design.org/references/authors/karin_coninx.html), Karin (2013): Crossing the bridge over Norman's gulf of execution: Revealing feedforward's true identity. In: [Proceedings of HCI 2013](https://www.interaction-design.org/references/conferences/proceedings_of_hci_2013.html) April 27- May 2, 2013, Paris, France. pp. 1931-1940
[Vicente](https://www.interaction-design.org/references/authors/kim_j__vicente.html), Kim J. and [Rasmussen](https://www.interaction-design.org/references/authors/jens_rasmussen.html), Jens (1990): *The ecology of human-machine systems II: Mediating "direct perception" in complex work domains*. In [Ecological psychology](https://www.interaction-design.org/references/periodicals/ecological_psychology.html), 2 (3) pp. 207-249

[Vyas](https://www.interaction-design.org/references/authors/dhaval_vyas.html), Dhaval, [Chisalita](https://www.interaction-design.org/references/authors/cristina_m__chisalita.html), Cristina M. and [Veer](https://www.interaction-design.org/references/authors/gerrit_c__van_der_veer.html), Gerrit C. van der (2006): Affordance in interaction. In: [13th European Conference on Cognitive Ergonomics](https://www.interaction-design.org/references/conferences/13th_european_conference_on_cognitive_ergonomics.html) September 20-22, 2006, Zurich, Switzerland. pp. 92-99
[Vyas](https://www.interaction-design.org/references/authors/dhaval_vyas.html), Dhaval, [Chisalita](https://www.interaction-design.org/references/authors/christina_m__chisalita.html), Christina M. and [Dix](https://www.interaction-design.org/references/authors/alan_dix.html), Alan (2008). *Dynamics of Affordances and Implications for Design*. University of Twente [http://doc.utwente.nl/64769/](http://doc.utwente.nl/64769/)
[Wagman](https://www.interaction-design.org/references/authors/jeffrey_b__wagman.html), Jeffrey B. and [Carello](https://www.interaction-design.org/references/authors/claudia_carello.html), Claudia (2001): *Affordances and Inertial Constraints on Tool Use*. In[Ecological psychology](https://www.interaction-design.org/references/periodicals/ecological_psychology.html), 13 (3) pp. 173-195

[Wagman](https://www.interaction-design.org/references/authors/jeffrey_b__wagman.html), Jeffrey B. and [Carello](https://www.interaction-design.org/references/authors/claudia_carello.html), Claudia (2003): *Haptically creating affordances: The user tool interface*. In[Journal of Experimental Psychology: Applied](https://www.interaction-design.org/references/periodicals/journal_of_experimental_psychology-_applied.html), 9 (4) pp. 175-186
[Warren](https://www.interaction-design.org/references/authors/william_h__warren.html), William H. (1995): Constructing an econiche. In: [Flach](https://www.interaction-design.org/references/authors/john_m__flach.html), John M., [Hancock](https://www.interaction-design.org/references/authors/peter_a__hancock.html), Peter A., [Caird](https://www.interaction-design.org/references/authors/jeff_caird.html), Jeff and[Vicente](https://www.interaction-design.org/references/authors/kim_j__vicente.html), Kim J. (eds.). "Global perspectives on the ecology of human-machine systems". Hillsdale, USA: Erlbaumpp. 210-237
Wikipedia. Preikestolen (n.d.) Available at [http://en.wikipedia.org/wiki/Preikestolen](http://en.wikipedia.org/wiki/Preikestolen)
[Zhang](https://www.interaction-design.org/references/authors/ping_zhang.html), Ping (2008): *Motivational affordances: Fundamental reasons for ICT design and use*. In[Communications of the ACM](https://www.interaction-design.org/references/periodicals/communications_of_the_acm.html), 51 (11)

[Şahin](https://www.interaction-design.org/references/authors/erol_%C5%9Eahin.html), Erol, [Çakmak](https://www.interaction-design.org/references/authors/maya_%C3%87akmak.html), Maya, [Doğar](https://www.interaction-design.org/references/authors/mehmet_r__do%C4%9Far.html), Mehmet R., [Uğur](https://www.interaction-design.org/references/authors/emre_u%C4%9Fur.html), Emre and [Üçoluk](https://www.interaction-design.org/references/authors/g%C3%B6kt%C3%BCrk_%C3%9C%C3%A7oluk.html), Göktürk (2007): *To afford or not to afford: A new formalization of affordances toward affordance-based robot control*. In [Adaptive Behavior - Animals, Animats, Software Agents, Robots, Adaptive Systems](https://www.interaction-design.org/references/periodicals/adaptive_behavior_-_animals%2C_animats%2C_software_agents%2C_robots%2C_adaptive_systems.html), 15 (4) pp. 447-472
**Chapter TOC**
[**User Experience: The Beginner’s Guide**](https://www.interaction-design.org/courses/user-experience-the-beginner-s-guide)
![](https://public-media.interaction-design.org/images/courses/hds/course_50--square_thumbnail.jpg?tr=fo-auto)
User Experience: The Beginner’s Guide
Closes in
15
days
booked
View Course

## 获取每周 UX 洞察

加入 **314,524 位设计师**的行列，通过我们的时事通讯获取实用的用户体验（User Experience, UX）技巧。
需要提供有效的电子邮件地址。

## 本章涉及的主题：

[现象学（Phenomenology）](https://www.interaction-design.org/literature/topics/phenomenology)[
    可供性（Affordances）](https://www.interaction-design.org/literature/topics/affordances)[
    人机交互（Human-Computer Interaction, HCI）](https://www.interaction-design.org/literature/topics/human-computer-interaction)[
    用户体验（UX）设计（User Experience Design）](https://www.interaction-design.org/literature/topics/ux-design)[
    设计史（Design History）](https://www.interaction-design.org/literature/topics/design-history)[
    直觉设计（Intuitive Design）](https://www.interaction-design.org/literature/topics/intuitive-design)[
    拟物化（Skeuomorphism）](https://www.interaction-design.org/literature/topics/skeuomorphism)[
    示能符（Signifiers）](https://www.interaction-design.org/literature/topics/signifiers)
