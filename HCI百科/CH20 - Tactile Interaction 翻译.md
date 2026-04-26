# 20. 触觉交互（Tactile Interaction）

**来源**：The Encyclopedia of Human-Computer Interaction, 2nd Ed.
**Notion 原页面**：https://www.notion.so/69119776b5b1481f8d18f32d5061a56e

---

[Ben Challis](https://www.interaction-design.org/literature/author/ben-challis)
本章描述了利用触觉交互（Tactile Interaction）来增强人机界面（Human-Computer Interface），即交互产品（Interactive Products）设计的多种方式。本章首先对触觉交互的广泛潜在应用进行总体讨论，随后迅速转向探讨可能影响我们利用这一潜在丰富交互资源的物理、感知和技术关键问题。在此过程中，本文探讨了广泛的研究课题，并为任何试图利用某种程度触觉交互的界面提供了应考虑的基础设计原则（Design Principles）建议。

## 20.1 引言 (Introduction)

让我们探讨一下，为什么我们会对在[设计过程（design process）](https://www.interaction-design.org/literature/topics/design-process)中探索触觉交互（tactile interaction）感兴趣？毕竟，在任何给定的界面中，占据主导地位的通常不是视觉通道（visual channel）吗？就显示和反馈而言，情况通常如此；作为用户，我们可能期望在开始交互之前先*看到*可用的控件和选项，同样，我们也可能期望*看到*所采取的任何操作的结果。界面设计长期以来一直认可在可能的情况下提供额外增强方法的理念，尤其[强调（emphasis）](https://www.interaction-design.org/literature/topics/emphasis)听觉反馈（auditory feedback）的使用。因此，任何给定的操作都可能通过视觉和听觉反馈的结合来增强；事实上，在不断扩大的音乐和音频软件市场中，反馈可能主要就是听觉上的，即音乐或声音本身。这种无疑强大的组合实现了丰富形式的显示和反馈，但将我们从一种状态引导至另一种状态的交互，通常是通过*触觉（touch）*来支持的。

我们选择和操作这些各种物理和虚拟对象的方式，将是通过动作和触觉的结合，即*触觉交互（haptic interaction）*。这或许正是事情开始变得有趣的地方，因为...

虽然关于视觉和听觉反馈的界面设计（Interface Design）已有大量研究和详尽的“良好”实践记录，但关于触觉交互（Haptic Interaction）“良好”设计的具体细节研究仍然很少。因此，针对我们开篇提出的问题，第一个答案可能是：触觉交互（Tactile Interaction）作为一种潜在反馈来源的价值或许被低估了。之前的研究重点可能过于集中在“执行（doing）”而非“接收（receiving）”上。在视觉显示已经相当拥挤的今天，将部分信息分担（Off-loading）到听觉通道可能会带来切实的好处，但同样可能的是，某些反馈对于我们的触觉来说具有更直接的意义。例如，选择和定位虚拟屏幕推子（Virtual On-screen Fader）的操作，其带来的*感觉*可能比任何*声音*都更具意义。

![](https://public-media.interaction-design.org/images/encyclopedia/tactile_interaction/tactile-doing-Reactable_Multitouch.jpg)
作者/版权持有者：Courtesy of Daniel Williams。版权条款和许可：CC-Att-SA-2 (Creative Commons Attribution-ShareAlike 2.0 Unported)。

**图 20.1**：一个用于“执行”的有形交互设计（Tangible Interaction Design）示例——“Reactable”。请注意，告知用户每个模块功能的信息线索（Informational Cues）是视觉性的，而触觉性则体现在用户如何采取行动。

![](https://public-media.interaction-design.org/images/encyclopedia/tactile_interaction/Tactile_paving_2.jpg)
作者/版权持有者：Courtesy of Richard Drdul。版权条款与许可：CC-Att-SA-2 (Creative Commons Attribution-ShareAlike 2.0 Unported)。
![](https://public-media.interaction-design.org/images/encyclopedia/tactile_interaction/tactile_pavings.jpg)
作者/版权持有者：Courtesy of Mailer Diablo。版权条款与许可：CC-Att-SA-3 (Creative Commons Attribution-ShareAlike 3.0)。
**图 20.2 A-B**：用于“接收（receiving）”的触觉设计（Tactile Design）示例。这些不同的纹理在脚下感觉不同，而纹理的变化会告知盲人（或正在发短信的）行人何时停止或何时需要注意。

仅凭这一论点就非常有说服力，但现在让我们考虑许多视觉主导显示（Visually Dominant Display）不切实际或无法实现的场景和环境。最显而易见的例子可能是为盲人用户设计非视觉界面（Non-visual Interfaces）。这里有许多需要考虑的问题，其中一些将在本章后面出现。然而，目前的关键点在于，[图形用户界面](https://www.interaction-design.org/literature/topics/ui-design)（Graphical User Interface, GUI）需要通过非视觉手段进行有效的转换和传递。这里可以利用一些辅助工具，例如屏幕阅读器（Screen-readers）可以使用合成语音（Synthetic Speech）来朗读屏幕上的文本或描述一个...

结构布局（structural layout）——但如果以一种让用户能够“感知”控件的方式来展示结构组件，是否会更快速且提供更多信息？因此，对于某些计算机用户而言，存在一些*特殊*的需求，在这种情况下，大幅度地摆脱以视觉为主的界面（visually dominant interface）可能会带来益处。然而，在许多其他场合，对于没有额外个体需求（additional individual needs）的用户来说，情况可能同样如此。例如，在驾驶车辆或操作专业机械时，能够与周围环境保持近乎持续的视觉接触可能单纯地更“安全”。事实上，车载娱乐系统（in-car entertainment systems）的控件现在经常被安置在方向盘柱上——这样既触手可及，又无需将视线从道路上移开。在某些情况下，周围环境可能无法提供足够的光线，导致难以清晰地看到正在发生的情况。在这些[场景](https://www.interaction-design.org/literature/topics/user-scenarios)的极端情况下，环境可能正处于应急照明状态；而在安全性要求较低的情况下，可能是客厅太暗，难以通过遥控器轻松控制家庭影院。

因此，作为设计师，我们希望探索非视觉通信模式（non-visual modes of communication）的原因非常广泛。不过，在本章的语境中，我们的关注点在于触觉交互（tactile interaction），并且随后

我们将探讨可用于实现这一目标的各种技术（包括现有技术和新兴技术）。然而，与所有其他形式的交互（Interaction）和反馈（Feedback）一样，物理和感知（Perceptual）层面的限制与边界将影响任何新设计的实际效果。

## 20.2 触觉心理学（The Psychology of Touch）

为了开始理解触觉交互（tactual interaction）如何成功地集成到人机界面（human-computer interface）中，必须首先理解人体是如何获取并处理关于其周围环境的信息的。这一过程发生在两个层面：物理层面（physical level）和感知层面（perceptual level）。在物理层面，我们的周围神经系统（peripheral nervous systems）利用多种不同类型的神经来收集信息，每种神经对特定[类型](https://www.interaction-design.org/literature/topics/type)的刺激（stimulus）敏感。所有由周围神经系统收集的信息都通过中枢神经系统（central nervous system）传递到其最终的汇聚点：大脑。信息在这里被解读并随后转化为行动，而正是这种解读过程构成了感知层面。出于本章的目的，我们将避免进一步讨论人体神经系统的生理结构，但对于任何考虑在设计语境下探索触觉交互的人来说，这确实应该是推荐阅读的一部分。

Loomis and Lederman (1986) 对通过触觉解读信息的三个方面提供了有用的概述，这些方面可以统称为*触觉感知（tactual perception）*。他们指出，存在两种基本且截然不同的感觉，它们

……共同为我们提供了触觉：皮肤感觉（cutaneous sense）和动觉（kinesthesis）。皮肤感觉提供的是对皮肤内感受器受刺激的感知，而动觉则提供的是对身体（头部、躯干、四肢等）相对位置的感知。涉及其中一项或多项的感知可被视为*触觉感知（tactual perception）*，因此，此类感知有三种形式。

**触觉感知（Tactile perception）**完全依赖于皮肤刺激的变化，例如在个体的皮肤上描绘图案等行为。纯粹的触觉感知意味着相关个体必须处于静止状态；否则，动觉将被纳入其中。

**动觉感知（Kinesthetic perception）**关注的是动觉刺激的变化。然而，不含皮肤感觉贡献的触觉感知只能在人为设计的特殊情况下实现，例如使用麻醉剂来抑制皮肤感觉的贡献。

**力触觉感知（Haptic perception）**是同时涉及触觉感知和动觉感知的触觉感知形式，也是我们在日常生活中通过触碰来探索和理解周围环境所采用的方式。

个体在任何给定时间对皮肤感觉或动觉感觉信息采集的控制程度，导致了以下五种触觉模式（tactual modes），其中前三种模式……

无控制。事实上，从这些定义可以看出，在五种模式中，只有最后一种——*主动触觉感知（active haptic perception）*——在采用触觉交互（tactile interaction）的界面设计中可能具有真正的意义。

1. 触觉感知（Tactile perception）——仅包含皮肤信息（Cutaneous information）。
1. 被动动觉感知（Passive kinesthetic perception）——传入动觉（Afferent kinesthesis）。
1. 被动触觉感知（Passive haptic perception）——皮肤信息与传入动觉。
1. 主动动觉感知（Active kinesthetic perception）——传入动觉与传出副本（Efference copy）。
1. 主动触觉感知（Active haptic perception）——皮肤信息、传入动觉与传出副本。

![](https://public-media.interaction-design.org/images/encyclopedia/tactile_interaction/vibrotactile.jpg)
作者/版权持有者：Amanda M. Williams 提供。版权条款与许可：CC-Att-SA-3 (Creative Commons Attribution-ShareAlike 3.0)。

![](https://public-media.interaction-design.org/images/encyclopedia/tactile_interaction/vibrotactile2.jpg)
作者/版权持有者：Amanda M. Williams 提供。版权条款与许可：CC-Att-SA-3 (Creative Commons Attribution-ShareAlike 3.0)。

**图 20.3 A-B**：振动触觉反馈（Vibrotactile feedback），例如这款原型手套所采用的，利用了用户的皮肤感觉（Cutaneous sense）。

![](https://public-media.interaction-design.org/images/encyclopedia/tactile_interaction/kinesthetic_2.jpg)
作者/版权持有者：Maria Ly 提供。版权条款与许可：CC-Att-SA-2 (Creative Commons Attribution-ShareAlike 2.0 Unported)。

**图 20.4**：动觉（Kinesthetic sense）提供了对身体相对位置的感知。

## 20.3 触觉交互的实践细节（The Practicalities of Tactile Interaction）

归根结底，任何集成触觉交互（Tactile Interaction）的人机界面（Human-Computer Interface）在设计时，其构建方面的考量与设计触觉图表（Tactile Diagrams）时所面临的问题在很大程度上是相同的；此外，该领域已有大量可供参考的研究成果。在深入探讨这些感知特性（Perceptual Properties）之前，让我们先简要分析一下“触觉（Touch）”与“视觉（Sight）”之间的关系。

### 20.3.1 视觉与触觉（Vision versus Touch）

我们对视觉的普遍依赖表明，一旦触觉与视觉之间产生冲突，视觉方面通常会占据主导地位（Visual Dominance）。这种感官信息（Sensory Information）的冲突构成了 Rock and Victor (1964) 研究的基础。他们利用光学圆柱体（Optical Cylinder）使一组受试者在视觉上产生错觉，认为一个实心的正方形物体实际上是长方形的。对于实验中的受试者而言，其触觉印象（Tactual Impression）并未改变。面对此类冲突的受试者，在对尺寸和形状做出判断时，其结果通常与仅接收到 [视觉信息（Visual Information）](https://www.interaction-design.org/literature/topics/information-visualization) 的对照组（Control Group）成员相似。

然而，McDonnell and Duffett (1972) 指出，Rock and Victor 的实验可能存在方法论缺陷（Methodological Failings），从而导致了倾向于视觉的 [偏差（Bias）](https://www.interaction-design.org/literature/topics/bias)。在他们对原实验的重新设计中，受试者被要求检查放置在桌面上的木块。为了检查木块的下半部分，受试者必须在桌面下方进行触觉感知。受试者接收到的印象是木块穿过了桌面，而实际上是通过两个木块的组合来营造这种错觉。实际上，受试者检查的每个“木块”实际上是一对木块，其中木材的宽度与

桌子两边的突出部分相同，但长度可能不同。实验使用了五对方块，其差异比（discrepancy ratios）分别为 1:1, 1.29:1, 1.67:1, 2.2:1 和 3:1。在检查每个方块后，受试者必须从一组没有长度差异的对比方块（comparison blocks）中选择最匹配的一个。该组的平均得分显示，受试者选择的对比方块是其视觉印象（visual impression）与触觉印象（tactual impression）之间的一种折中。然而，进一步的分析表明，受试者的选择倾向于符合视觉或触觉印象中的一种，且响应模式（response pattern）存在相当大的多样性，因此视觉[主导性（dominance）](https://www.interaction-design.org/literature/topics/dominance)不能被认为是显著的。

Heller (1992) 同样表明，Rock and Victor 的原始研究结果不应被如此泛化地应用于断言：当触觉与视觉发生冲突时，视觉总是更具主导性的感官。在 Heller 的实验中，受试者被要求在通过镜子观察的同时，探索凸印字母（embossed letters）*p, q, b, d, w* 和 *m*。例如，受试者在观察字母 *m* 的同时，实际上是在探索字母 *w*。当被要求识别字母时，出现了广泛的响应，其中大多数受试者依赖触觉，部分受试者在两者之间寻求折中，而仅有一名受试者依赖视觉。

看来，

因此，视觉主导（Visual Dominance）与触觉主导（Tactual Dominance）不应被视为一种二分法（Dichotomy），因为有证据表明，当两种感官发生冲突时，两者之间存在某种程度的权衡（Compromise）。此外，这种权衡的程度可能具有高度的个体差异，并且还会受到某种偏好（Bias）的影响，即一种或两种感官对于特定任务性质的适用性（Suitability）。

### 20.3.2 视觉到触觉的映射（Visual to Tactile Mapping）

Klatzky and Lederman (1987) 认为，许多触觉图表（tactile diagrams）可能会因为空间分辨率（spatial resolution）的局限性而出现问题。例如，一些视觉上清晰的线图，在触觉上可能并不清晰，因为对于如此有限的带宽（bandwidth）而言，其比例尺变得太小了。Klatzky and Lederman 还指出，在触觉图形显示设备（tactile graphics displays）的设计中，经常采用一种存在根本缺陷的触觉处理（haptic processing）模型。该模型被称为 *图像中介模型（image mediation model）*，在这种模型中，“手的功能就像一只急需眼镜的游走之眼”（Klatzky and Lederman 1987）。其假设是，触觉会产生一个与视觉产生的空间图像（spatial image）等同的图像。然而，这个图像会受到触觉传感器（haptic sensors）低分辨率等因素的影响，同时由于随时间探索“图像”的特性，还会对记忆产生需求。随后，该图像被传递给视觉系统的图像解释器（image interpreters），从而形成一个心像（mental-image），这个心像看起来就像是一个视力不佳的人在视觉上观察原图的结果。

与此模型相反，Klatzky and Lederman 认为触觉系统拥有其自身的感知系统（perceptual system）和解释处理器（interpretive processors）。触觉与视觉仅仅是两种不同的感知方式，尽管在更高的认知层面，触觉系统可能会与视觉系统产生某种融合（convergence）。也许最

Klatzky 和 Lederman 提出了一个重要的观点，即触觉系统（haptic system）并不是一个高效的图像中介。例如，如果要求一个人想象在看一只猫，他/她可能会在脑海中呈现出猫的身体形状，以及可能的皮毛颜色和花纹。然而，如果要求同一个人想象触摸一只猫，则会产生截然不同的意象：皮毛的柔软度以及身体的温暖感。

在 Klatzky 和 Lederman 对三维物体探索（exploration of three-dimensional objects）的研究中，记录了一系列探索方法。特别值得关注的是，材质维度（substance dimensions，例如硬度和纹理）可以被快速且可靠地提取，而结构信息（structural information）的提取速度较慢且容易出错。如果假设触觉系统倾向于选择那些能以最小努力获得最大回报的编码机制（encoding mechanisms），那么可以预见，一个经济的系统会倾向于基于材质的探索和编码。

其中一项具体研究要求受试者对在四个维度上有所不同的物体进行分类：硬度、表面粗糙度（surface-roughness）、尺寸和形状。每个维度有三种变化，所有可能的组合都涵盖在整个实验组中。受试者只需将相似的物体放入同一个收集桶中。通过检查每个桶中的物体，可以确定哪个维度被证明

最显著的维度可以被确定。例如，如果所有粗糙的物体都在一个箱子中，中等粗糙的在另一个箱子中，而光滑的在第三个箱子中，那么表面纹理（Surface Texture）将成为最显著的维度。

结果随所允许的探索条件（Exploratory Conditions）而异，具体而言，当被剥夺视觉时，受试者更倾向于选择硬度或纹理等物质维度（Substance Dimensions）。当相似性被定义为物体的“触感”时，这一模式保持不变；但当相似性被定义为物体在“视觉上”相似时，则出现了向依赖结构维度（Structural Dimensions）的大幅转变。最后，当受试者被允许看到物体时，结构维度再次占据主导地位。尽管这些研究是使用三维物体进行的，但其结论在触觉图表设计（Tactile Diagram Design）中可能同样有效，尽管此时仅轮廓（Contour）和纹理适用。特别是，如果一个显示界面既包含部分视觉信息，又通过一些触觉元素进行增强，Klatzky 和 Lederman 的研究结果可能有助于确定如何在视觉通道和触觉通道（Haptic Channels）之间最佳地分配信息。

### 20.3.3 线条符号（Line Symbols）

最简单的触觉对象或许就是代表线条这一绘图原语（drawing primitive）的对象。直线和曲线可被视为大多数图形表示（graphical representations）的基础构建模块，而图表、地图和其他图示在构建过程中在很大程度上依赖于线条的使用。当使用凸起线条（raised lines）作为视觉线条的触觉替代物（tactile substitutes）时，两个问题会迅速显现：

1. 它们被追踪（traced）的难易程度如何？
2. 不同线宽之间区分的难易程度如何？

关于线条的可追踪性（traceability），Bentzen and Peck (1979) 进行了一项对比研究，探讨了哪些风格的线条最容易通过手指追踪来跟随。研究使用了四种线条风格：单连续线（single continuous，平滑）、双连续线、单点线（single dotted，粗糙）和双点线。选择这些风格是因为它们似乎被公认为最常用的四种，但并没有证据证明其中哪一种更优。除了确定哪些线条通常最容易追踪外，Bentzen 还对追踪在两种特定场景下的受影响情况感兴趣：

- 线条没有交点的显示界面（Displays）。
- 线条存在交点的显示界面。对比粗糙与平滑，以及单线与双线。

研究者使用凸印塑料片（embossed plastic sheets）创建了两个显示界面。其中一个简单的显示界面使用了所有四种线型且没有交点，其中全部包含一个

一个直角、一个钝角、一个锐角以及一个 1.5 英寸的半圆。这些元素通过三段 3 英寸和三段 1.5 英寸的直线段连接。该复杂显示采用了四种线型，并使用了相同的描迹组件（tracing components），但每条线在某处都与其他三条线相交。

得出的结论是，粗糙线与光滑线的表现没有显著差异，因此在触觉图表（tactile diagrams）的使用中，这并不是一个真正的设计问题。在没有相交线的触觉显示中，无论是粗糙还是光滑的单线，都比双线（间距 0.25 英寸）更理想。关于双线相对于单线的优势，除了双线在相交处表现更好之外，没有得出实质性的结论。然而，这被认为与所使用的显示设计特有相关，因此在现阶段并不具有显著意义。最后的一项观察是，单条细线与双线相交是一种不理想的特征。

Lederman and Campbell (1983) 的一项实验探讨了在面向盲人的有形图表显示（tangible graph displays）中使用凸起线（raised lines）的情况。实验采用了四种不同的图表呈现方法：

- **无网格（No-**[**grid**](https://www.interaction-design.org/literature/topics/grid-systems)**）** —— 除了主轴上的刻度（tics）外，主图表区域内没有网格线。
- **图表网格（Grid-on-graph）** —— 刻度以网格形式延伸至主区域。

- **网格覆盖层（Grid-on-overlay）** —— 网格是无网格版本的覆盖层。受试者可以将覆盖层不断地放置在图表之上。
- **网格底层（Grid-on-underlay）** —— 与网格覆盖层相反。在这种情况下，网格作为底层部分，而图表可以被放置在网格之上。

研究使用了三种线型：平滑线、大点线和小点线。从可追踪性（traceability）的角度来看，结果令人鼓舞，但在三种线型紧密相邻的图表中，执行任务所需的时间显著增加，且更容易出现错误。研究人员的记录提到，当受试者最初接触图表时，倾向于探索其整体格式，例如主轴、符号和标签。在角落使用砂纸方块（sandpaper squares）效果显著，因为通过检查这些方块和主轴，受试者可以通过大范围的手部扫视，迅速熟悉图表的尺寸和比例。研究还观察到了个体差异：有些人会使用双手进行探索，而另一些人则倾向于将一只手放在原点（origin）作为参考点。结果还表明，无网格格式和图上网格（grid-on-graph）格式比其他选项更受欢迎；两者似乎同样[易于使用（easy to use）](https://www.interaction-design.org/literature/topics/ease-of-use)。

另一项关于影响可区分性（discriminability）因素的探索...

触觉线条（Tactile lines）的研究关注于感知一条线比另一条线更宽（Berla and Murr 1975）。基本上，研究将五种标准线宽分别与一组线条进行比较，其中一半比标准线窄，另一半则更宽。使用的五种标准线宽分别为 0.1、0.15、0.2、0.25 和 0.3 厘米。对于 0.1 厘米的线条，设有六条逐渐变窄和六条逐渐变宽的线条，步长为 0.01 厘米；而其他所有线条的步长则为 0.013 厘米。每条线的高度约为 0.64 厘米。当受试者同时面对一条标准线和一条可变线（Variable line）时，需要指出哪一条最宽。

结果表明，个体感知到一条线比标准线更宽所需的额外宽度百分比（Percentage of extra width）随着标准线宽的增加而降低。例如，最细的标准线（0.1 厘米）需要宽 20% 到 48% 才能被感知为更宽，而最粗的线（0.3 厘米）则需要宽 11% 到 27%。然而，这一趋势并非无限持续。当标准线宽包含 0.64 厘米和 1.27 厘米时，感知表现开始下降。这被归因于线宽开始超过平均指尖（Fingertip）的宽度，导致无法轻易感知到线条的两侧（或边缘）。尽管如此，目前的结果提供了一组非常有用的、具有高度可区分性的线宽，在线宽差异对触觉显示（Tactile display）起重要作用的场景中可以安全地采用。

Nolan and Morris (1971) 指出，在任何给定时间，仅能使用大约 8 个触觉线性符号（tactile linear symbols），否则会出现相似性（similarities），且其最大数量可能仅为 10 个。James and Gill (1975) 的一项研究表明，存在 10 个此类可区分的（distinguishable）线性符号，但他们未能突破 Nolan and Morris 设定的上限。

### 20.3.4 点符号（Point Symbols）

点符号（Point symbols）最合适的定义可能是指那些旨在通过指尖极小幅度移动即可探索的符号。使用此类符号的一个重要方面是它们相对于背景的感知效果如何，这通常被称为*图形-背景问题（figure-ground problem）*。该问题的一个方面是凸起符号（raised symbols）是否比凹刻符号（incised symbols）更容易识别。Nolan and Morris (1971) 对“两者之间没有显著差异”这一假设进行了测试，结果与普遍认知相反，两者之间似乎*确实*存在显著差异。实验要求盲文阅读者（Braille readers）追踪一个触觉符号（tactile symbol），然后从五个选项中找出相同的符号。该实验分别使用了一组凸起图形和一组等效的凹刻图形来完成。Nolan 的结果表明，事实上，凸起图形明显优于凹刻图形。尽管使用凹刻符号时错误率有所增加，但更显著的结果是阅读时间增加了约 38%。这意味着如果使用凸起图形，大多数触觉符号的阅读速度会更快，准确率也会更高。

Lambert and Lederman (1989) 关于触觉地图符号相对易读性（legibility）和意义性（meaningfulness）的研究表明，触觉符号可分为三类。一些符号具有内在含义，例如...

……电话形状，其中一些符号可以蕴含某种含义，例如用尖形符号表示“停止”，而另一些则具有相当任意的含义，例如用正方形代表洗手间。所使用的符号尺寸每边在 0.635 厘米至 1.27 厘米之间，这是基于先前对盲人的观察和研究而定的。Lederman 讨论的一个显著特点是，尽管有些人会立即偏好或识别某些符号，但符号是否具有固有含义（inherent meaning）并非至关重要。随着长期使用，任何符号都会开始蕴含特定的含义，因此，在成功实施任何触觉图表（tactile diagram）时，预计都会存在一定的学习成本（learning overhead）。

### 20.3.5 区域符号（Areal Symbols）

“区域符号（areal symbol）”一词用于描述触觉图（tactile diagram）中那些使用纹理（texture）或触觉图案（tactile pattern）来传递信息的区域。“触觉图案”这个词可能意味着一个覆盖了刻入或凸起符号的区域，这些符号可以被轻易地感知为可识别的，并且能与类似的图案区分开来。然而，Lederman (1982) 指出，触觉图案感知的一个基本方面是对纹理的感知。她举了婴儿皮肤的“光滑感（smoothness）”、砂纸的“粗糙感（roughness）”、羊绒的“柔软感（softness）”、橡皮筋的“橡胶感（rubberiness）”以及冰的“湿滑感（slipperiness）”作为例子。仅凭纹理就能提供大量的触觉反馈（tactual feedback），使我们能够判断某种区域触觉图案是否能与其他区域图案高度区分。

![](https://public-media.interaction-design.org/images/encyclopedia/tactile_interaction/tactual_feedback_areal_patterns.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

**图 20.5**：一些可能的区域触觉符号示例

Lederman 讨论了纹理感知中一些已知的问题，概述了她如何使用表面切割有线性槽口的铝板来研究对粗糙感的感知。她的结果

……表明影响粗糙度感知（perception of roughness）的主要因素是沟槽切口（groove cuts）的宽度与其间距的关系。然而，她还表明施加力（applied force）是次重要的因素，其次是手速（hand speed）。较大的施加力会导致感知粗糙度的比例更高，且在手速逐渐降低的情况下，这一结论依然成立。这些发现具有重要意义，因为它们可以在设计用作区域符号（areal symbols）的合适触觉模式（tactile patterns）中发挥重要作用。

Loomis (1981) 描述了一系列影响触觉模式感知的限制因素：空间分辨率（spatial resolution）、间距超过分辨率极限的刺激之间的相互作用（干扰 [interference]）、时间分辨率（temporal resolution）、感知整合（perceptual integration）以及有限的注意力（limited attention）。

空间分辨率 —— 这通常与两点辨别阈 [测试](https://www.interaction-design.org/literature/topics/test)（two-point limen test）相关，在该测试中，绘图圆规的两个尖端被紧密地放置在个体的皮肤上。关注的距离是两个点被感知为一个点的阈值（threshold）。然而，Loomis 将空间分辨率进一步分为三个因素。首先是皮肤的力学特性（mechanical property）。当一个点放置在皮肤上时，皮肤形变的梯度（gradient of skin deformation）将明显小于刺激物的梯度。其次是……

机械波传播的特性。当某一点受到刺激时，会产生行波（travelling waves），当这些波被其他机械感受器（mechanoreceptors）捕捉时，会产生一种“模糊（blurring）”效应。最后，神经组织（neural organisation）决定了空间分辨率（spatial resolution）取决于：
1. 皮肤特定区域内机械感受单位（mechanoreceptive units）的密度。
1. 这些单位的大小和[灵敏度（sensitivity）](https://www.interaction-design.org/literature/topics/empathy)。
1. 代表同一区域的皮层投射区（cortical projection areas）中的神经元数量。

**宽间距刺激之间的相互作用**
 - 两点辨别阈测试（two-point limen test）就是一个典型的例子，但其重点是评估两个刺激被感知为一个刺激时的距离。将两个此类刺激施加在相距较远的身体部位（例如两只不同的手），可能会在两者之间的某个点产生幻触感（phantom sensation）。幻触感的另一个例子发生在快速地刺激一个点，然后立即刺激另一个点时。由此产生的感觉是，一系列等间距的触感从一个位置移动到另一个位置。皮肤掩蔽（cutaneous masking）也可能发生，即一个刺激可能会被另一个强得多的刺激完全掩盖。

**时间分辨率（Temporal resolution）**
 - 指个体仍能清晰地将两个短暂脉冲感知为独立个体所需的最小时间间隔。Loomis 指出，针对此项研究的许多实验得出的估计值在 2ms 到

40ms。

**知觉整合（Perceptual integration）** —— 指所有这些信息在皮层阶段（cortical stage）被利用的方式，即使这些信息在传输至该阶段时没有明显的细节丢失。该观点认为，与[视觉感知（visual perception）](https://www.interaction-design.org/literature/topics/visual-perception)不同，来自刺激模式（stimulus pattern）的信息可能会无法被识别。

**有限注意力（Limited attention）** —— 即使信息在感知过程中没有丢失且在皮层中得到了整合，个体仍可能因为注意力容量（attentional capacity）不足而无法感知到该模式。在视觉通道（visual channel）方面，人们普遍认为，当信息量开始超过处理能力时，人们能够集中注意力。而触觉通道（tactual channel）在这种形式的集中注意力方面似乎效率较低。

在将触觉模式（tactile patterns）作为显示设备一部分的实际应用方面，Lederman and Kinch (1979) 对该领域的现有研究进行了综述。一个可以得出的普遍结论是，虽然可以找到大约 40 种易于识别的触觉模式，但同时能一起使用的最多只有 8 种。很难找到超过 8 种可以作为一组使用且不会产生歧义的模式。例如，一个典型的糟糕选择是使用方向相反的对角线来表示不同的功能。

因此，在之前图 5 所示的 12 个区域符号（Areal Symbols）示例集中，已经开始出现一些歧义性（Ambiguities），导致某些符号对之间的快速区分会受到阻碍。Lederman 讨论的一个重要效应是在触觉显示器（Tactile Display）中使用高度来提供一种过滤方法（Filtering Method）。符号可以用三种高度之一来呈现，以指示其重要程度；通过使用扫手动作，这可以作为过滤掉不需要的信息的一种方式。

![](https://public-media.interaction-design.org/images/encyclopedia/tactile_interaction/tactile_overlay_0.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

**图 20.6**：
一个用于传递音乐记谱（Music Notation）页面结构信息的触觉覆盖层（Tactile Overlay）。该覆盖层由真空成型 PVC（Vacuum-formed PVC）制成，显示了关键元素，如小节线、页面线、重复标记等。类似的覆盖层被用于一个为盲人提供音乐记谱访问权限的实验系统中（Challis and Edwards 2000）。通过与覆盖层交互，用户可以提取关于节奏和旋律内容的语音和音频描述。

![](https://public-media.interaction-design.org/images/encyclopedia/tactile_interaction/tactile_overlay_1.jpg)

作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

![](https://public-media.interaction-design.org/images/encyclopedia/tactile_interaction/tactile_overlay_2.jpg)

作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

**图 20.7 A-B**：“Weasel”非视觉音乐记谱系统（non-visual music notation system）中其他覆盖层（overlays）的示例。此处，每个覆盖层都安置在 Intellikeys 触敏平板（touch-sensitive tablet）中；这种设备在特殊教育（special needs education）中相当常用。

![](https://public-media.interaction-design.org/images/encyclopedia/tactile_interaction/taxel_pic.jpg)

作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

**图 20.8**：触觉像素（Taxels）可以被认为是像素（pixels）在触觉上的等效物。此插图展示了触觉像素阵列如何被用于为手机创建动态界面（dynamic interface）。

### 20.3.6 探索策略（Strategies for Exploration）

Berla (1972) 定义了盲人在使用触觉图（tactile diagrams）时的三个问题领域：*可读性（legibility）*、*组织性（organisation）*和*探索策略（strategies for exploration）*。在这三个问题中，最后一个尤其令人关注，因为它涉及个体如何采用不同的方法来探索图表。Berla 在该领域的一项实验结果表明，一些个体使用单手扫描策略（one-handed scanning strategy），而另一些则使用双手。事实证明，使用双手的个体比仅使用单手的个体能更好地保持在图表中的方向感（sense of orientation）和位置感。他认为这是因为能够将一只手作为参考点（reference point）。Berla 识别出的策略可描述为：

- **水平单向（Horizontal-unidirectional）**：手在页面上水平移动，在向下或向上移动到下一行进行下一次扫描之前，先返回到该行的起点。
- **水平双向（Horizontal-bidirectional）**：手在页面上沿一个方向追踪，然后下移或上移到下一扫描行，接着反向扫描页面。
- **非对称水平扫描（Asymmetrical horizontal scan）**：双手放置在图表的中心，然后向相反方向向外移动，随后再次回到中心。接着，双手下移或上移到下一扫描行。
- **垂直单向（Vertical-unidirectional）**：手在页面上垂直追踪，并返回到...

在向右或向左移动到下一行扫描之前，先回到行首。
- **垂直双向扫描（Vertical-bidirectional scan）**：手在页面上垂直追踪，然后向左或向右移动到下一行扫描，接着再次在页面上垂直反向扫描。
- **周边或“时钟面”扫描（Perimeter or 'clock-face' scan）**：手追踪图表的完整周边，然后逐渐向中间移动，扫描较小的内部周边。
- **有界搜索（Bounded search）**：由读者在图表上叠加任意大小的“方框”。搜索将被限制在特定的方框内。
- **密度分布扫描（Density distribution scan）**：使用手快速确定大部分符号分布在哪些区域，随后优先探索符号分布最稀疏的区域。
- **辐条轮式扫描（Spoked wheel scan）**：一只手作为参考点，另一只手从中心向外扫描，并逐渐围绕图表移动。

Berla 得出结论，这些策略各有相对的优缺点，因此很难建议采用某种“理想”的策略。他还描述了最合适的方法可能是将所有这些策略教授给那些需要处理此类图表的人，这样他们就能针对任何给定的探索任务应用最合适的策略。Berla and Butterfield (1977) 还建议，个体可能需要接受关于如何...

在取得显著成效之前，需要先使用特定类型的触觉图（tactile diagram）。在他的研究中，他表明，如果学生首先接受线条追踪（line tracing）和区分特征分析（distinctive features analysis）的训练，那么他们在区分和理解触觉符号（tactile symbols）方面的表现会有所提升。人们可能会产生一种预期，认为个体无需任何先验经验就能简单地理解此类触觉图。Berla 强调，在计划设计和实现触觉显示器（tactile display）时，这是一个至关重要的领域。

### 20.3.7 盲文符号（Braille Symbols）

盲文系统（Braille system）是视障人士广泛用于阅读和书写的一种方法。盲文由法国盲人 Louis Braille 于 1825 年发明。每个盲文字符，或称单元（cell），由六个点位组成，排列成一个包含两列、每列三个点的矩形。

![](https://public-media.interaction-design.org/images/encyclopedia/tactile_interaction/braille_letters_and_numbers.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。

**图 20.9**：盲文符号

尽管盲文符号并非触觉图表设计（tactile diagram design）中不可或缺的部分，但每个单元实际上都是一个触觉符号（tactile symbol），因此，影响这些单元的易读性（legibility）和感知（perception）的因素可能具有研究价值。一项关于盲文与模式感知（pattern perception）的特定研究探讨了盲文单元是被感知为一组独立的点，还是被感知为轮廓形状。Millar (1985) 进行的一系列实验使用部分轮廓（partial outlines）来代表通常以盲文显示的字母。这些并非普通印刷字母的触觉轮廓，而是盲文单元的连线版本。Millar 的研究结果表明，盲文字母可以被阅读和识别

使用点阵单元（cells of dots）比使用连线（joined lines）的速度显著更快。这意味着小型触觉符号（tactile symbols）如果采用点阵模式而非轮廓（outlines）设计，可能也会获益。

![](https://public-media.interaction-design.org/images/encyclopedia/tactile_interaction/outline_shapes_and_braille_cells.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”章节。

**图 20.10**：Millar (1985) 用于替代盲文单元（braille cells）的轮廓形状示例

![](https://public-media.interaction-design.org/images/encyclopedia/tactile_interaction/braille_text_french.jpg)
作者/版权持有者：由 Christophe Moustier 提供。版权条款和许可：pd（公有领域（Public Domain），即属于公共财产且不含原创作者身份的信息）。

**图 20.11**：单词“premier”（法语，意为“第一”）的木雕盲文代码（braille code）

### 20.3.8 触觉交互（Tactile Interaction）的设计原则

目前已有一套关于在人机界面（human-computer interface）中加入触觉信息的初步设计原则被提出 (Challis and Edwards 2000, Challis and Edwards 2000)。研究者以音乐记谱法（music notation）作为复杂图形信息类型的示例，开发了一个实验系统，使盲人音乐学习者能够采用一种非视觉的多模态方法（multi-modal approach）来阅读乐谱。该系统将静态覆盖层（static overlays）与电阻式触摸板（resistive touch-pad）结合使用，以创建交互式页面，用户可以通过这些页面“感受”页面布局的结构，然后利用音频和合成语音（synthetic speech）选择合适的信息检索级别。

在研究之初，研究者采用了三项基础原则，涵盖了*映射的一致性（consistency of mapping）*、*高度的使用（use of height）*以及*静态数据的使用（use of static data）*。在研究过程中，又确定了额外的原则以解决诸如*显示尺寸（size of display）*、*视觉到触觉的映射（visual-to-tactile mapping）*、符号设计的[*简洁性（simplicity）*](https://www.interaction-design.org/literature/topics/simplicity)以及（或许是最重要的）*空白区域（empty space）*等方面的问题；空白区域简单来说是指用户对于在何处或如何探索缺乏信息的区域。一个简单但关键的观察结果是，触觉图表在视觉上可能并不那么美观，且设计不太可能从过度依赖直接的视觉到触觉映射中获益。

## 20.4 人机界面中的触觉交互（Tactile Interaction in the Human Computer Interface）

在采用利用触觉交互的技术时，可以考虑三种主要方法：静态触觉显示设备（static tactile displays）、动态触觉显示设备（dynamic tactile displays）和力反馈技术（force-feedback technology）。每种方法都有明显的优点和局限性，因此交互任务的性质将决定哪一类方法最为有效。事实上，Oakley et al. (2000) 提出了相应的定义，以便对这些不同的技术进行分类，其分类依据是受交互影响最显著的感觉系统。

- **触觉（Haptic）** —— 与触觉相关。
- **本体感觉（Proprioceptive）** —— 与关于身体状态的感觉信息相关（包括皮层感觉、动觉和前庭感觉）。
- **前庭感觉（Vestibular）** —— 涉及对头部位置、加速和减速的感知。
- **动觉（Kinesthetic）** —— 指运动的感觉。与源自肌肉、腱和关节的感觉相关。
- **皮层感觉（Cutaneous）** —— 涉及皮肤本身或作为感觉器官的皮肤。包括压力、温度和疼痛的感觉。
- **触觉（Tactile）** —— 涉及皮层感觉，但更具体地指压力感，而非温度或疼痛感。
- **力反馈（Force Feedback）** —— 涉及由人类动觉系统感知的信息的机械产生。

### 20.4.1 静态与动态触觉显示器（Static and Dynamic Tactile Displays）

在适用永久性显示器（permanent display）的场景中，例如交互式信息显示器或专用设备的控制面板，将静态覆盖层（static overlay）叠加在适当的触控响应表面（touch-responsive surface，如电阻式、电容式、红外式、声波式或压力感应式）上将具有实用性，且在需要时能提供精细的细节水平。相比之下，动态显示器（dynamic display）可以提供更高的灵活性，因为其界面并不“绑定”在特定的布局上。可刷新盲文显示器（Refreshable braille displays）在某种程度上实现了这种灵活性，但目前可用技术的尺寸并不利于创建具有实用分辨率的触觉符号（tactile symbols）。

![](https://public-media.interaction-design.org/images/encyclopedia/tactile_interaction/braille_display_1.jpg)
作者/版权持有者：未知（待调查）。版权条款与许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”章节。

![](https://public-media.interaction-design.org/images/encyclopedia/tactile_interaction/braille_terminal.jpg)
作者/版权持有者：由 Sebastien Delorme 提供。版权条款与许可：CC-Att-SA-3 (Creative Commons Attribution-ShareAlike 3.0)。

**图 20.12** A-B：盲文显示器

例如，为了实现追踪一条连续线条的感觉，一个

需要 20 dpi 的分辨率 (Fricke and Bahring 1992, Fricke 1997)。即使在这种分辨率下，一个 20 英寸 $\times$ 15 英寸的显示区域将需要 120,000 个元件（elements），而对角线依然会感觉是不连续的。假设有技术可以实现更高且更精确的分辨率，那么该技术必须更加微小。这些元件中的每一个都需要被单独控制；系统必须能够独立地且极快速地对这 120,000 个元件进行寻址（addressing）。用于此目的且达到此尺寸的机械技术目前尚不存在，即使是最基础的现有技术也极其昂贵。

针对这一复合问题，Heidelberg Tactile Vision Substitution System (Maucher et al 2000) 探索了一种替代方案，该方案通过使用虚拟显示区域（virtual display area）大大减少了所需的触觉像素（taxels，可将其视为视觉像素在触觉领域的对应物）数量。为了实现这一点，48 个此类触觉像素被安装在一个载台（carriage）上，该载台在较大的显示区域内移动，而若采用静态布局，该区域将需要 2600 个触觉像素；就整体清晰度而言，这仍然是非常低的分辨率。

### 20.4.2 触觉显示技术（Haptic Display Technology）

在计算机游戏市场的快速扩张以及人们对虚拟环境（virtual environments）普遍兴趣的部分影响下，价格低廉的力反馈（force-feedback）和触觉技术（haptic-technology）已经出现一段时间了（例如力反馈操纵杆、“震动手柄（rumble-pads）”、振动触觉鼠标等）。基于与 SensAble Technologies 的 Phantom 系列力反馈设备相似的技术，诸如 Novint Falcon 等先进的游戏设备正被用于在计算机游戏中提供丰富且沉浸式的物理存在感（physical presence）。该设备提供三个自由度（degrees of freedom），通过一个电机控制的机械臂，将后坐力、冲击力或不同程度的阻力等感觉传递给玩家手持的控制设备（该设备可以采取枪支或球棒等形式）。Phantom 设备与之类似，且像 Falcon 一样可以控制用户的手或肢体，从而创造出丰富多样的虚拟纹理（virtual textures）和其他效果。但请记住，触觉（haptics）意味着触觉反馈（tactile feedback）和动觉反馈（kinesthetic feedback）的结合；然而，这里描述的设备在触觉层面上并没有提供太多的反馈。从这个意义上说，虚拟显示领域中的触觉感知（haptic perception）不太可能是主动的，因此不符合该定义。

在此程度上，此类显示设备的[有用性（usefulness）](https://www.interaction-design.org/literature/topics/usefulness)在于其动态特性，而非在于能够实现的触觉交互（haptic interaction）的丰富程度。

![](https://public-media.interaction-design.org/images/encyclopedia/tactile_interaction/force_feedback.jpg)
作者/版权持有者：Courtesy of Lapsus Antepedis。版权条款和许可：CC-Att-SA-3 (Creative Commons Attribution-ShareAlike 3.0)。

**图 20.13**：一对放置在桌面上的黑色 Novint Falcon，配备了手枪式和球形握把附件。

在最初涉足力反馈（force-feedback）和振动触觉反馈（vibro-tactile feedback）游戏设备的基础上，Immersion 公司目前正在生产多执行器控制器（multi-actuator controllers），旨在将触觉交互引入如今智能手机和平板电脑上无处不在的触摸屏界面。这些控制器被设计为放置在屏幕区域的后方或周围，最多可编程 16 个执行器以产生各种振动效果，从而增强用户的操作感。例如，按下屏幕上的按钮时，可以伴随一种效果，在一定程度上告知用户该操作已完成。同样，这是一种有用的反馈，且显示设备的动态特性为界面带来了相当大的灵活性，但例如，用户将无法像在静态设备中那样感受到轮廓或详细的纹理。

显示设备所能提供的；就“显示（display）”本身而言，它仍然主要以视觉为主。

![](https://public-media.interaction-design.org/images/encyclopedia/tactile_interaction/Microsoft_Force_Feedback_Joystick.jpg)
版权条款与许可：pd（公有领域（Public Domain），指属于公共财产且不含原创作者权的资料））。

**图 20.14**：
视频游戏设备可以有效地利用力反馈（force feedback）为游戏过程带来沉浸感（immersive qualities）。这些设备涵盖了从用于模拟碰撞和冲击波的振动“震动手柄（rumble pads）”，到像图中所示的力反馈操纵杆（如 Microsoft 的 Sidewinder Force-feedback Pro）所提供的更具物理感的交互。在后者中，手部会被控制和移动，以此来暗示障碍物的阻力，或模拟开枪时的后坐力（recoil）等动作。

![](https://public-media.interaction-design.org/images/encyclopedia/tactile_interaction/interactive_virtual_reality_immersive_simulation_with_force_feedback.jpg)
作者/版权持有者：由 HAPTION 提供。版权条款与许可：CC-Att-SA-3 (Creative Commons Attribution-ShareAlike 3.0)。

**图 20.15**：
更先进的力反馈系统（如 Haption 制造的系统）可用于在虚拟环境（virtual environments）中提供丰富的触觉增强（haptic-reinforcement）。

![](https://public-media.interaction-design.org/images/encyclopedia/tactile_interaction/virtual_reality_cutaneous_sense.jpg)
作者/版权持有者

提供者：Courtesy of Chris Desmond US Navy。版权条款与许可：pd（公有领域 (Public Domain)，指属于公共财产且不含原创作者权的资料）。

**图 20.16**：[虚拟现实 (Virtual Reality, VR)](https://www.interaction-design.org/literature/topics/virtual-reality) 跳伞训练器。学生在悬挂于跳伞吊带 (parachute harness) 的同时佩戴 VR 眼镜，随后通过一系列计算机模拟场景 (computer-simulated scenarios) 学习如何控制自己的动作。当学生拉动控制降落伞的连接带 (risers) 时，计算机将接收到相应的信号。该 VR 训练器还教授机组人员 (aircrew personnel) 如何在不同的天气条件下以及在可能出现设备故障 (equipment malfunctions) 时处理降落伞。

## 20.5 未来方向

显然，目前的技术还无法实现能够提供与我们日常接触的物体具有相同细节丰富度和对比度的动态触觉显示器（Dynamic Tactile Displays）。然而，尽管在[增强现实（Augmented Reality）](https://www.interaction-design.org/literature/topics/augmented-reality)或虚拟环境的语境下，这显然是一个最终目标，但可能还存在一些更易实现且依然具有重大用途的目标。视障用户（Visually Impaired, VI）的信息获取一直是我们讨论的重点，显然，一个真正动态且丰富的触觉显示器能为这一领域带来巨大的益处。例如，电子书现在已十分普及，但如果电子书能让用户探索并与盲文（Braille）和触觉图表（Tactile Diagrams）进行交互，情况会如何？类似的技术是否还会有其他更主流的用途？从个人层面来看，我的背景跨越了技术与音乐，尽管我对虚拟合成器（Virtual Synthesisers）和音乐环境充满热情，但我仍然更倾向于真实控件带来的触感和“感觉”，而非触摸屏（Touch-screen）所提供的触感。在这种情况下，对我而言，一个色彩丰富、图形精美但缺乏有意义的触觉交互的界面，与一个允许我触摸并感知控件的简单图形显示器，哪一个更有用？毕竟，两者都将

控制并产生相同的声学输出（sonic output），这将始终是我关注的核心。从现实角度来看，我认为两者兼而有之可能会对我有所帮助。那么，我们距离实现这种沉浸式动态触觉显示（immersive level of dynamic tactile display）还有多远？我们之前讨论过机械部件的尺寸如何在控制和分辨率（resolution）方面造成限制，但在这一领域，通过对热响应型基于凝胶的像素（gel-based pixels）的探索，已经取得了重大突破。

这种像素的直径仅为 300 微米，它会对精细光源产生的热量做出响应，并缩减至其 0.5 毫米原始高度的一半；同时，该像素会变得不透明，使得这种变化非常明显。该实验性显示器包含 4000 多个此类像素，每平方厘米约有 297 个可用像素，从而能够实现高分辨率的触觉图形（tactile graphics）。然而，例如与标准 LCD 显示器相比，其刷新率（refresh rate）仍然较低，但典型的电子书也是如此。这仍是一项新兴技术，但如果能够得到充分开发，将很容易促成我们刚才讨论的触觉电子书（tactile e-book）的诞生。如果这项技术能进一步增强，以支持用户的输入，那么它将真正成为在各种新型触觉界面（tactile-interfaces）中实现丰富触觉交互（haptic interaction）的门户。

## 20.6 更多学习资源

并不令人惊讶的是，本章中引用的许多信息都源自于旨在让视障用户能够获取信息的非视觉方法（non-visual approaches）研究。尽管人们对触觉交互（tactile interaction）在主流设备中的应用产生了浓厚兴趣，但得益于通过新技术实现无障碍（accessibility）的研究，目前已经积累了大量的知识体系。有许多会议在更广泛的残障相关议题中探讨非视觉交互（non-visual interaction），其中包括：

- [ICCHP](http://www.icchp.org/) - International Conference on Computers Helping People with Special Needs
- [CSUN](http://www.csun.edu/cod/conference/) - Annual International Technology and Persons with Disabilities Conference
- [ArtAbilitation](http://artabilitation.expositus.com/)
- [ASSETS](http://www.sigaccess.org/conferences) - International ACM SIGACCESS Conference on Computers and Accessibility
- [ICDVRAT](http://www.icdvrat.rdg.ac.uk/) - International Conference on Disability, Virtual Reality and Associated Technologies

此外，关于[人机交互（Human Computer Interaction）](https://www.interaction-design.org/literature/topics/human-computer-interaction)的会议也应被视为获取进一步信息的潜在来源：

- [CHI](http://acm.org/) — ACM 计算系统中的人类因素（Human Factors）会议
- [HCI](http://www.bcs.org/) — 英国计算机学会（British Computer Society）HCI 会议

此外，还有一些期刊偶尔会探讨触觉交互（Tactile Interaction）的概念，尽管可能是将其置于更广泛的交互性（interactivity）范畴之内。这些期刊包括：
- Journal of Visual Impairment and Blindness
- Perception
- Digital [Creativity](https://www.interaction-design.org/literature/topics/creativity)
- Technology and Disability
- International Journal of Arts and Technology
- Computer Music Journal

## 20.7 References

[Bentzen](https://www.interaction-design.org/references/authors/billie_louise_bentzen.html), Billie Louise and [Peck](https://www.interaction-design.org/references/authors/alec_f__peck.html), Alec F. (1979): *Factors Affecting the Traceability of Lines for Tactile Graphics*. In[Journal of Visual Impairment and Blindness](https://www.interaction-design.org/references/periodicals/journal_of_visual_impairment_and_blindness.html), 73 (7) pp. 264-269
[Berla](https://www.interaction-design.org/references/authors/edward_p__berla.html), Edward P. (1972): *Behavioral Strategies and Problems in Scanning and Interpreting Tactual Displays*. In[New Outlook for the Blind](https://www.interaction-design.org/references/periodicals/new_outlook_for_the_blind.html), 66 (6) pp. 277-286
[Berla](https://www.interaction-design.org/references/authors/edward_p__berla.html), Edward P. and [Butterfield](https://www.interaction-design.org/references/authors/lawrence_h__butterfield.html), Lawrence H. (1977): *Tactual Distinctive Features Analysis: Training Blind Students in Shape Recognition and in Locating Shapes On a Map*. In [The Journal of Special Education](https://www.interaction-design.org/references/periodicals/the_journal_of_special_education.html), 11 (3) pp. 335-346

[Berla](https://www.interaction-design.org/references/authors/edward_p__berla.html), Edward P. and [Murr](https://www.interaction-design.org/references/authors/marvin_j__murr.html), Marvin J. (1975): *Psychophysical functions for active tactual discrimination of line width by blind children*. In [Perception and Psychophysics](https://www.interaction-design.org/references/periodicals/perception_and_psychophysics.html), 17 (6) pp. 607-612
[Challis](https://www.interaction-design.org/references/authors/ben_challis.html), Ben (2002): Designing Interactive Tactile Diagrams. In: [Miesenberger](https://www.interaction-design.org/references/authors/klaus_miesenberger.html), Klaus, [Klaus](https://www.interaction-design.org/references/authors/joachim_klaus.html), Joachim and [Zagler](https://www.interaction-design.org/references/authors/wolfgang_l__zagler.html), Wolfgang L. (eds.) [ICCHP 2002 - Computers Helping People with Special Needs - 8th International Conference](https://www.interaction-design.org/references/conferences/icchp_2002_-_computers_helping_people_with_special_needs_-_8th_international_conference.html)July 15-20, 2002, Linz, Austria. pp. 559-561

[Challis](https://www.interaction-design.org/references/authors/ben_challis.html), Ben and [Edwards](https://www.interaction-design.org/references/authors/alistair_d__n__edwards.html), Alistair D. N. (2000): Design Principles for Tactile Interaction. In: [Proceedings of the First International Workshop on Haptic Human-Computer Interaction](https://www.interaction-design.org/references/conferences/proceedings_of_the_first_international_workshop_on_haptic_human-computer_interaction.html) 2000. pp. 17-24
[Challis](https://www.interaction-design.org/references/authors/ben_challis.html), Ben and [Edwards](https://www.interaction-design.org/references/authors/alistair_d__n__edwards.html), Alistair D. N. (2000): Weasel: A System for the Non-Visual Presentation of Music Notation. In: [Proceedings of 6th International Conference on Computers Helping People with Special Needs. ICCHP 2000](https://www.interaction-design.org/references/conferences/proceedings_of_6th_international_conference_on_computers_helping_people_with_special_needs__icchp_2000.html) 2000.

[Fricke](https://www.interaction-design.org/references/authors/joerg_fricke.html), Joerg and [Baehring](https://www.interaction-design.org/references/authors/helmut_baehring.html), Helmut (1993): *Design of a tactile graphic I/O tablet and its integration into a personal computer system for blind users*. In [Journal of Microcomputer Applications](https://www.interaction-design.org/references/periodicals/journal_of_microcomputer_applications.html), 16 (3) pp. 259-269
[Fricke](https://www.interaction-design.org/references/authors/joerg_fricke.html), Joerg and [Bahring](https://www.interaction-design.org/references/authors/h__a__bahring.html), H. A. (1992): A Graphic Input/Output Tablet for Blind Users. In: [Proceedings of 3rd International Conference on Computers for Handicapped People](https://www.interaction-design.org/references/conferences/proceedings_of_3rd_international_conference_on_computers_for_handicapped_people.html) 1992.
[Fricke](https://www.interaction-design.org/references/authors/j__fricke.html), J. and [Edwards](https://www.interaction-design.org/references/authors/alistair_d__n__edwards.html), Alistair D. N. (2000): Tactile Displays Based on Modulated Electromagnetic Radiation. In:[Proceedings of 6th International Conference on Computers Helping People with Special Needs. ICCHP 2000](https://www.interaction-design.org/references/conferences/proceedings_of_6th_international_conference_on_computers_helping_people_with_special_needs__icchp_2000.html)2000.

[Heller](https://www.interaction-design.org/references/authors/morton_a__heller.html), Morton A. (1992): *Haptic dominance in form perception: vision versus proprioception*. In [Perception](https://www.interaction-design.org/references/periodicals/perception.html), 21 (5) pp. 655-660
[James](https://www.interaction-design.org/references/authors/g__a__james.html), G. A. and [Gill](https://www.interaction-design.org/references/authors/j__m__gill.html), J. M. (1975): *A pilot study on the discriminability of tactile areal and line symbols for the blind*. In [Research Bulletin of the American Foundation for the Blind](https://www.interaction-design.org/references/periodicals/research_bulletin_of_the_american_foundation_for_the_blind.html), 29 pp. 23-31
[Klatzky](https://www.interaction-design.org/references/authors/roberta_l__klatzky.html), Roberta L. and [Lederman](https://www.interaction-design.org/references/authors/susan_j__lederman.html), Susan J. (1987): The Representation of Objects in Memory: Contrasting Perspectives from Vision and Touch. In: [Gruneberg](https://www.interaction-design.org/references/authors/m__m__gruneberg.html), M. M., [Morris](https://www.interaction-design.org/references/authors/p__e__morris.html), P. E. and [Sykes](https://www.interaction-design.org/references/authors/r__n__sykes.html), R. N. (eds.). "Practical Aspects of Memory: Current Research and Issues". Wiley

[Lambert](https://www.interaction-design.org/references/authors/l__m__lambert.html), L. M. and [Lederman](https://www.interaction-design.org/references/authors/susan_j__lederman.html), Susan J. (1989): *An evaluation of the legibility and meaningfulness of potential map symbols*. In [Journal of Visual Impairment and Blindness](https://www.interaction-design.org/references/periodicals/journal_of_visual_impairment_and_blindness.html), 83 pp. 397-403
[Lederman](https://www.interaction-design.org/references/authors/susan_j__lederman.html), Susan J. (1982): The Perception of Texture by Touch. In: [Schiff](https://www.interaction-design.org/references/authors/william_schiff.html), William and [Foulke](https://www.interaction-design.org/references/authors/emerson_foulke.html), Emerson (eds.). "Tactual Perception: A Sourcebook". Cambridge University Press
[Lederman](https://www.interaction-design.org/references/authors/susan_j__lederman.html), Susan J. and [Campbell](https://www.interaction-design.org/references/authors/j__i__campbell.html), J. I. (1983): *Tangible line graphs: An evaluation and some systematic strategies for exploration*. In [Journal of Visual Impairment and Blindness](https://www.interaction-design.org/references/periodicals/journal_of_visual_impairment_and_blindness.html), 77

[Lederman](https://www.interaction-design.org/references/authors/susan_j__lederman.html), Susan J. and [Kinch](https://www.interaction-design.org/references/authors/denise_h__kinch.html), Denise H. (1979): *Texture in Tactual Maps and Graphics for the Visually Handicapped*. In [Journal of Visual Impairment and Blindness](https://www.interaction-design.org/references/periodicals/journal_of_visual_impairment_and_blindness.html), 73 (6) pp. 217-227
[Loomis](https://www.interaction-design.org/references/authors/jack_m__loomis.html), Jack M. (1981): *Tactile pattern perception*. In [Perception](https://www.interaction-design.org/references/periodicals/perception.html), 10 (1) pp. 5-27
[Loomis](https://www.interaction-design.org/references/authors/jack__m__loomis.html), Jack. M. and [Lederman](https://www.interaction-design.org/references/authors/susan_j__lederman.html), Susan J. (1986): Tactual Perception. In: [Boff](https://www.interaction-design.org/references/authors/kenneth_r__boff.html), Kenneth R. (ed.). "Handbook of Perception and Human Performance". New York: John Wiley and Sons

[Maucher](https://www.interaction-design.org/references/authors/thorsten_maucher.html), Thorsten, [Schemmel](https://www.interaction-design.org/references/authors/johannes_schemmel.html), Johannes and [Meier](https://www.interaction-design.org/references/authors/karlheinz_meier.html), Karlheinz (2000): The Heidelberg Tactile Vision Substitution System. In: [Proceedings of 6th International Conference on Computers Helping People with Special Needs, ICCHP 2000](https://www.interaction-design.org/references/conferences/proceedings_of_6th_international_conference_on_computers_helping_people_with_special_needs%2C_icchp_2000.html) 2000.
[McDonnell](https://www.interaction-design.org/references/authors/paul_m__mcdonnell.html), Paul M. and [Duffett](https://www.interaction-design.org/references/authors/james_duffett.html), James (1972): *Vision and touch: a reconsideration of conflict between the two senses*. In [Canadian Journal Of Psychology](https://www.interaction-design.org/references/periodicals/canadian_journal_of_psychology.html), 26 (2) pp. 171-180
[Millar](https://www.interaction-design.org/references/authors/susanna_millar.html), Susanna (1985): *The perception of complex patterns by touch*. In [Perception](https://www.interaction-design.org/references/periodicals/perception.html), 14 (3) pp. 293-303

[Nolan](https://www.interaction-design.org/references/authors/carson_y__nolan.html), Carson Y. (1971): *Relative Legibility of Raised and Incised Tactual Figures*. In [Education of the Visually Handicapped](https://www.interaction-design.org/references/periodicals/education_of_the_visually_handicapped.html), 3 (2) pp. 33-36
[Nolan](https://www.interaction-design.org/references/authors/carson_y__nolan.html), Carson Y. and [Morris](https://www.interaction-design.org/references/authors/june_e__morris.html), June E. (1971): *Improvement of tactual symbols for blind children: 1 June 1964--28 February 1969 : final report.* American Printing House for the Blind

[Oakley](https://www.interaction-design.org/references/authors/ian_oakley.html), Ian, [McGee](https://www.interaction-design.org/references/authors/marilyn_rose_mcgee.html), Marilyn Rose, [Brewster](https://www.interaction-design.org/references/authors/stephen_a__brewster.html), Stephen A. and [Gray](https://www.interaction-design.org/references/authors/philip_d__gray.html), Philip D. (2000): Putting the Feel in 'Look and Feel'. In: [Turner](https://www.interaction-design.org/references/authors/thea_turner.html), Thea, [Szwillus](https://www.interaction-design.org/references/authors/gerd_szwillus.html), Gerd, [Czerwinski](https://www.interaction-design.org/references/authors/mary_czerwinski.html), Mary, [Peterno](https://www.interaction-design.org/references/authors/fabio_peterno.html), Fabio and [Pemberton](https://www.interaction-design.org/references/authors/steven_pemberton.html), Steven (eds.)[Proceedings of the ACM CHI 2000 Human Factors in Computing Systems Conference](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_2000_human_factors_in_computing_systems_conference.html) April 1-6, 2000, The Hague, The Netherlands. pp. 415-422

[Richter](https://www.interaction-design.org/references/authors/andreas_richter.html), Andreas and [Paschew](https://www.interaction-design.org/references/authors/georgi_paschew.html), Georgi (2009): *Optoelectrothermic Control of Highly Integrated Polymer-Based MEMS Applied in an Artificial Skin*. In [Advanced Materials](https://www.interaction-design.org/references/periodicals/advanced_materials.html), 21 (9) pp. 979-983
[Rock](https://www.interaction-design.org/references/authors/irvin_rock.html), Irvin and [Victor](https://www.interaction-design.org/references/authors/jack_victor.html), Jack (1964): *Vision and Touch: An Experimentally Created Conflict between the Two Senses*. In [Science](https://www.interaction-design.org/references/periodicals/science.html), 143 (3606) pp. 594-596
**Chapter TOC**
[**Human-Computer Interaction: The Foundations of UX Design**](https://www.interaction-design.org/courses/hci-foundations-of-ux-design)
![](https://public-media.interaction-design.org/images/courses/hds/course_72--square_thumbnail.jpg?tr=fo-auto)
Human-Computer Interaction: The Foundations of UX Design
Closes in
10
days
booked
View Course

## 获取每周用户体验（User Experience, UX）洞察

加入 **314,337 位设计师** 的行列，通过我们的时事通讯（Newsletter）获取实用的 UX 技巧。
需要提供有效的电子邮件地址。

# 20.7 Alistair D. N. Edwards 的评论

触觉交互（Tactile interaction）在交互学科中处于一个奇特的位置——正如本章所反映的那样。一方面，它与那些仍远离主流应用的未来主义、新奇的技术联系在一起；但另一方面，它又是大多数传统人机交互（Human-Computer Interaction）中的一个元素，而我们几乎对此毫无察觉。也就是说，无处不在的键盘和鼠标输入在潜意识中严重依赖于力触觉（Haptic）和本体感受（Proprioceptive senses），而我们往往将其视为理所当然。因此，大多数人可能认为自己并没有进行力触觉交互，但会承认这对于缺乏其他感官（尤其是视觉）的人来说一定很有用，对于这些人而言，诸如盲文（Braille）之类的触觉通信显得极其宝贵。

希望本章能让读者更加意识到这一现状以及触觉交互的潜力。键盘和鼠标随着时间的推移而演进，适应了用户的生理能力，但极少参考底层的生物学原理。当然，键盘是非最优演进（Non-optimal evolution）的一个经典例子：有观点认为（Noyes 1983），传统的 *qwerty* 布局旨在降低打字员的速度，以减少机械打字机上连续字母的碰撞，而现在我们却不得不沿用它。一方面，推测……是很有趣的

如果发明者能读到像本章这样的内容，键盘的设计可能会有所不同；但另一方面，人们必须注意到，即使拥有这些知识，触觉交互（Haptic Interaction）显然仍远未达到其全部潜力。

我们拥有一些物理设备，包括键盘、调音台（Mixing Desks）和灯光控制台（Lighting Desks），它们天生就具有良好的触觉反馈（Haptic Feedback）和交互能力，但在数字化、虚拟化的世界中，我们受限于技术。使用如图 21.13 所示的设备所需的投入（时间、金钱、空间等）是否值得其带来的收益？

触觉图像（Tactile Picture）在某种意义上似乎是一个“显而易见”的设备，尤其是对于我们这些有视力的人来说：如果你无法看到一张图片，那么你应该能够感受到它。我投入了大量的时间和精力研究触觉图表（Tactile Diagrams），主要是在 University of York Centre for Tactile Images 工作（遗憾的是，该中心因缺乏财务可行性 [Financial Viability] 而已不复存在）。我们与许多重要客户（包括 Hull 的 *The Deep*、The Jorvik Centre、The National Trust、English Heritage 以及 The National Railway Museum）合作，为不同目的制作了大量图表。我们发现自己一直在重复（Challis 提到过的）这样一个断言：一张优秀的触觉图表在视觉上可能*看起来*很糟糕。也就是说，触觉（Haptic Senses）与视觉截然不同。

一旦人们停下来思考，那些直接的区别就变得显而易见了。

触觉灵敏度（Tactual sensitivity）较低。Challis 提到了两点辨别阈（two-point limen），但并未给出具体数值。这可能是明智的，因为作为触觉灵敏度的衡量标准，它至少存在争议，且很难就平均值达成共识。但关键在于，该数值在毫米量级——远低于视觉分辨率（visual resolution）。在图 21.5 中，Challis 展示了可以在凸点纸（swell paper）上生成的图案示例。在视觉呈现中，这些图案都截然不同，但在使用凸点纸样本的实验中（Magill 1999），我们发现普通人只能区分三种图案级别：光滑、中等和粗糙，而与其视觉图案无关。例如，虽然图 21.5 中显示的垂直和水平交叉阴影（cross-hatching）在视觉上明显不同，但在触觉检查时，它们可能会被感知为相同。

此外，在探索触觉图（tactile diagram）时，用户最多可能使用两个指尖，而更可能只使用一个。这种行为很容易被描述为通过一个“触觉针孔（tactile pinhole）”进行探索。然而在实践中，情况可能比这更糟糕。视觉本质上是一种整合性感觉（integrative sense）。眼睛感知的角度非常小，但由于眼睛不断移动且大脑能够整合信息，我们获得了一个宽广的视野，从而形成我们所感知的图像...

连贯的。唯一需要学习如何进行视觉感知（Visually perceive）的人，是那些曾经缺失视觉并在随后获得视觉的人（通常是通过手术，如 Sacks (2009) 中提到的 Virgil 的案例），而即使是熟练的盲文阅读者也需要学习如何使用触觉图像（Tactile pictures）。来自这类后天获得视力（Lately-acquired sight）案例的证据表明，在没有视力的情况下成长的人可能永远无法发展出将碎片整合为完整图像（无论是字面意义上还是比喻意义上）的能力。换句话说，触觉图像的价值可能始终有限——即使其设计已经最大限度地利用了触觉（Haptic senses）。

大多数触觉图形技术（Tactile graphic technologies）的一个局限性（例如膨胀纸 Swell paper）在于它是静态的，因此，触觉屏幕（Tactile screen）的想法极具吸引力——且经久不衰。我已经不再关注那些再次提出这一想法并认为自己找到了可行方案的公告和论文。我建议暂停此类出版物，直到有人能展示出一种切实可行、可靠且价格合理的设备。在没有这种禁令的情况下，我将通过不再阅读它们来实施我自己的禁令。我毫不怀疑有一天会有人发明出合适的技术，但——基于本章阐述的原因——这是一个难以实现的目标。即使在本章中也提到了另一次此类尝试（“基于凝胶的像素 Gel-based pixels，它们...

（对热量做出反应），但这显然再次具有相当大的推测性，因为甚至没有引用相关的出版物。

显而易见，在主导的视觉感知缺失的情况下，触觉（haptic sense）变得更加重要。盲文（Braille）是最丰富的触觉通信（tactile communication）形式，但盲人群体对其的使用率却非常低。据估计，阅读盲文的盲人比例不足 2% (Bruce, McKennell et al. 1991)。这种低采用率的原因尚不明确且可能十分复杂，但核心解释必然是：盲人认为学习盲文所付出的努力与其能获得的收益相比并不值得。这尤其适用于那些曾经拥有视力但后来失去视力的人——而这部分人占据了绝大多数。对于我们这些拥有视力的人来说，无法接触（印刷）文献似乎是一个巨大的损失，但对于大多数经历这种情况的人而言，学习触觉阅读（read tactually）的难度不足以成为足够的动力。

然而，视力正常的人之所以没有充分利用其非视觉感官，并非单纯是因为懒惰。在 (Pascual-Leone, Theoret et al. 2004) 进行的一项激进实验中，视力正常的参与者在数日内每天 24 小时被蒙上眼睛，并接受每日的盲文阅读训练。他们在学习盲文方面取得了显著进展，且脑扫描结果显示，通常与视觉处理（visual processing）相关的大脑皮层（brain cortex）区域正被重新分配用于处理

触觉信息（tactile information）。一组未被遮眼且视力正常的参与者作为对照组（control group），在学习盲文方面进展极小，且未表现出大脑适应（brain adaptation）。换言之，盲文不仅可能对盲人有用，而且盲人似乎是唯一可能能够使用它的人群。

综上所述，触觉（haptic senses）在传统交互（conventional interaction）中的应用程度远超大多数人的认知。如果设计师能更深入地了解触觉，那么触觉可以被更广泛且更有效地利用。虚拟触觉（virtual haptics）的使用正日益增加，且随着技术的发展，这一趋势将会加速；但（设计良好的）传统物理交互元件（physical interactors）（如旋钮、开关等）的使用依然具有其独特的价值。然而，考虑到触觉感知的生理限制（physiological limitations），其利用程度最终仍存在上限。

## 20.7.1 References

- Bruce, I., A. McKennell, et al. (1991). . London, HMSO.
  Blind and Partially Sighted Adults in Britain: The RNIB Survey
- Magill, D. (1999).  MSc (IT) Project Report, Department of Computer Science, University of York.
  Experiments to test differentiation of patterns for tactile human-computer interaction
- Noyes, J. (1983). "The QWERTY keyboard: a review." **18**(3): 265-281 DOI: [http://dx.doi.org/10.1016/S0020-7373(83)80010-8](http://dx.doi.org/10.1016/S0020-7373(83)80010-8).
  International Journal of Man-Machine Studies
- Pascual-Leone, A., H. Theoret, et al. (2004). Tactile processing in the visual cortex. . S. Ballesteros and M. A. Heller. Madrid, Spain, UNED**: **51-52.
  Touch Blindness and Neuroscience
- Sacks, O. (2009). , Picador.
  An Anthropologist on Mars

# 20.8 Klaus Miesenberger 的评述

我非常喜欢这一章——对于需要了解领域前沿（state of the art）的学生和从业者来说，这是一个极佳的资源。特别是以下两点：

1. 在开启新的冒险之前，我们绝不能忘记回顾基础知识、研究结果、成功案例以及失败教训！
2. 那些难以理解的内容会让读者和学生难以应对该主题。本章通过总结并直击要点，在这一方面提供了帮助。

本章介绍了与触觉信息呈现（tactile information presentation）相关的不同组件及其细节，探讨了触觉/实体/触摸界面（tactile/tangible/touch interfaces）的潜力，以及我们在提升与技术系统和内容交互的效率、质量和愉悦感方面所面临的挑战。本章没有做出无法兑现的承诺，也没有试图预测触觉/实体/触摸交互的下一步发展——因为没有人能预见到触摸显示屏会突然普及：尽管相关的技术、概念、想法和原型已经存在并被讨论了数十年，但直到最近，这一概念及其实现才迎来爆发式增长。

为什么实体交互（tangible interaction）在吸引大量“非技术”人群，并让如此多的人（包括老年人和残障人士）参与到信息与通信技术（ICT）中方面如此成功？是因为触觉？是因为视觉？是因为克服了手/触觉-眼睛-耳朵的协调问题？还是因为移动

……维度？它是非文本导向的维度（non-text oriented aspect）吗？……？最终，必须综合考虑许多答案和因素才能把握全局，从而让我们在界面设计（interface design）的旅程中迈出下一步，例如在触觉体验（tactile experience）中加入一种新的感知质量。

Ben Challis 的章节收集了可能构成界面革命下一步的内容。这场革命可以概括为“从手斧到指针（From the hand-axe to the pointer）”：它始于开关和接线板（包含大量的实体交互（tangible interaction）），经过控制台（console）、WIMP、SILK，向触觉/触摸/实体（tactile/touch/tangible）演进。有趣的是，我们首先是从使用触觉交互的直接且直观的交互方式，转向了一种全新的虚拟、无形的体验（即 WIMP 界面），这种体验在效率和独立性方面具有优势，但由于缺乏直观性，在接受度方面也存在局限。

在追求创造直观、可用、愉悦且高效的用户体验（user experiences）的过程中，研发工作越来越多地利用触觉、声音以及其他感官（如加速度、重力和嗅觉（olfactory sense））来实现这一目标。触觉交互（Tactile interaction）结合了多种类型的感官体验，这或许就是它显得直观的原因——它带给我们一种简单、高效、有效、直接且愉悦的交互感。然而，作为设计师，我们必须首先独立地理解触摸（touch）、触觉（tactile）和实体（tangible）界面。

在深入探讨跨传感方法（cross-sensing approaches）之前。

Ben 的这一章节引发了此类思考，使其成为学生、研究人员和开发人员在深入探讨那些乍看之下“显而易见”的问题时的理想参考资料。在界面与交互设计（interface and interaction design）领域，我们绝不能期待简单且易于应用的答案。我们必须学会将正确的问题置于正确的语境中，准备好质疑显而易见之物，并在对现有技术水平（state of the art）进行严谨且审慎的分析基础上寻求进步。这正是本章的核心意义所在。

最后但同样重要的一点是，我非常认同从极端情况中学习：在许多方面，视觉功能受损或缺失（reduced or no visual sense）的人群向我们展示了触觉或替代界面（tactile or alternative interfaces）应当如何设计。他们是关键经验与专业知识（know-how）的持有者。

优秀的界面应当“不要让我们思考（don't make us think）”。但优秀的界面设计则取决于设计师和开发人员是否愿意并准备好去思考交互与界面设计的全局图景。Ben 的这一章节正是引导我们在实施之前进行深思的绝佳资源！

## 本书章节涵盖的主题：

[触觉交互 (Tactile Interaction)](https://www.interaction-design.org/literature/topics/tactile-interaction)[
                        用户体验 (User Experience, UX) 设计](https://www.interaction-design.org/literature/topics/ux-design)[
                        人机交互 (Human-Computer Interaction, HCI)](https://www.interaction-design.org/literature/topics/human-computer-interaction)[
                        交互设计 (Interaction Design)](https://www.interaction-design.org/literature/topics/interaction-design)[
                        设计原则 (Design Principles)](https://www.interaction-design.org/literature/topics/design-principles)[
                        可访问性 (Accessibility)](https://www.interaction-design.org/literature/topics/accessibility)
