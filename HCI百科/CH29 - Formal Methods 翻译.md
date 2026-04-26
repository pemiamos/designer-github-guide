# 29. 正式方法（Formal Methods）

**来源**：The Encyclopedia of Human-Computer Interaction, 2nd Ed.
**Notion 原页面**：https://www.notion.so/c70a4787fb7a4636991677b9533890d9

---

[Alan Dix](https://www.interaction-design.org/literature/author/alan-j-dix)
正式方法（Formal Methods）在人机交互（human-computer interaction）中的应用可以追溯到该学科发展的早期，包括 Phyllis Reisner 在 1981 年使用 BNF（巴科斯-诺尔范式）来定义用户界面 (Reisner 1981)，以及作者本人在 1985 年第一次英国 HCI 会议上发表的关于该主题的第一篇论文 (Dix and Runciman 1985)。

在某种程度上，正式方法在[交互设计（interaction design）](https://www.interaction-design.org/literature/topics/interaction-design)中显得格格不入。人类是丰富、复杂且细腻的，参与着微妙且熟练的社会与物质交互；将这些简化为任何形式的正式描述，在最好的情况下也显得过于简单化。然而，一旦我们创建任何形式的数字系统，这正是我们必须要做的事情：无论是 iPhone 还是电梯，是 Angry Birds 还是 Facebook，软件都已嵌入在我们的生活中。无论我们如何设计设备和产品以满足用户需求或丰富他们的生活体验，其内部的软件依然是由毫无感情、精确且在很大程度上具有确定性逻辑（deterministic logic）的代码所驱动的。如果你从事与计算机相关的工作，你就必然在与形式主义（formalism）打交道。

正式方法处于逻辑与生活、精确与激情之间这个困难的交汇点上，两者都凸显了其中固有的矛盾……

交互设计（interaction design），并提供工具和技术以帮助理解并解决这些问题。

事实上，任何从事交互设计的人可能都使用过某种形式化表示（formal representation），最常见的是某种带有箭头和草图的图表，用于展示应用程序中的界面/页面以及它们之间的跳转。虽然存在许多更复杂的形式化符号（formal notations）和方法，但这些简单的界面与链接网络已经展示了形式化表示的本质。在这种表示中，某些内容总是被简化或忽略（例如界面的具体内容），而另一些内容则被更忠实地记录（例如界面之间的链接模式）。这使我们能够专注于某些方面，并利用该表示本身来理解或分析这些方面（例如，注意到通往某些关键界面的交互路径（interaction paths）非常长）。

> 什么是“形式化（Formal）”？
>
> *与所有词汇一样，“formal”在不同的人和不同的学科中具有不同的含义。在日常生活中，formal 可能意味着穿着晚礼服并打着领结，或者使用得体的语言。也就是说，formal 指的是事物的外部形式——一次正式的问候可能掩盖了表象之下的许多情感。**从严格意义上讲，数学和计算领域中的形式主义（formalism）是指能够以某种方式对事物进行表示，使得该表示可以在不考虑其含义的情况下被分析和操作。这是因为该表示是***

被选择用来忠实地概括其意义（meaning）的显著特征（significant features）。* 摘自 (Dix 2003)

## 29.1 人机交互中的形式化方法种类

在人机交互（HCI, Human-Computer Interaction）领域，使用了大量形式化（formal）或半形式化（semi-formal）的表示法、模型和技术。一种将其分类的方法是根据其所表示的对象：

***用户（users）*** —— 各种形式的认知模型（cognitive models）已被用于分析交互，从诸如 SOAR (Laird 2008) 或 ACT-R (Anderson 2005) 等认知架构（cognitive architectures）到运动层模型（motor level models）。后者持续产生着令人惊讶的影响力，但它们在很大程度上仅限于数据的数值拟合（numerical fitting of data），少数例外包括 Eslambolchilar 利用控制理论（control theory）来模拟人类动作与数字设备之间控制论交互（cybernetic interaction）的工作 (Eslambolchilar and Murray-Smith 2010); (Eslambolchilar 2006)。[任务分析（Task analysis）](https://www.interaction-design.org/literature/topics/task-analysis) 和任务模型（task models）(Diaper and Stanton 2003) 同样旨在分析或记录用户在现有系统或计划系统中的行为。一些任务建模系统考虑了多用户（例如 CTT (Paterno 1999)），且在计算机支持的协同工作（CSCW, Computer-Supported Cooperative Work）社区中也存在一些建模工作 (e.g. (Ellis 1994); (Dix et al. 2000))；然而，在群体或社会层面的建模较为罕见。

***系统（system）*** —— 交互的另一方是用户与之交互的设备或系统。许多技术已被应用于系统行为建模，包括形式文法（formal grammars）、状态机（state machines）、

理论计算机科学中的规范语言（specification languages）以及简单的求和运算！虽然这类模型或表示法（representation）的重点在于客体（如计算机、消费电子设备），但这并不意味着用户被忽略了。相反，用户的需求体现在所考察的属性中，或者体现在对建模方面的选择中。***世界（world）*** —— 对交互语境（context of interaction）的表示可以提供深刻的见解：用户是在物理语境中与设备进行交互的，且他们的数字化交互很可能会产生物理后果，无论是飞机的控制系统，还是简单的打印操作。然而，考虑到这一点的模型出奇地少。其中一个例子是对空间句法（space syntax）的使用，这是一种在建筑理论中开发的技术，旨在

理解人们在城市或办公空间中的移动和访问模式（visitation patterns）（见 4.1 节），作者自己的工作还包括对交互艺术装置（interactive art installations）的建模（modelling）（见 4.2 节）。*上下文感知界面（Context-aware interfaces）*（[见第 14 章](https://www.interaction-design.org/encyclopedia/context-aware_computing.html)）通常也会构建某种形式的内部模型。在本章稍后部分，我们将探讨包含系统和世界两个方面的物理设备的建模。

虽然对用户的表示（representations of the user）确实是形式化的，但它们通常不被认为是所谓的“形式化方法（Formal Methods）”，可能会在其他章节中讨论。此外，如前所述，对世界的表示（representations of the world）较为少见，因此本章的其余部分主要关注应用于系统的形式化方法。

然而，这本身有许多变体：

***我们在哪个架构层级（architectural level）上表示系统？***
—— 这可能侧重于呈现细节（presentation details），例如评估项目的视觉辨识（visual discrimination），或用户操作的 Fitts' Law 定时；它可能处于对话层级（dialogue level），表达潜在用户操作和用户响应的顺序；或者处于更深层级，分析或建模在影响用户的范围内其底层功能（underlying functionality）。

***我们在哪个抽象层级（level of abstraction）上表示系统？***
—— 我们可能拥有某个特定系统设计的非常具体模型（concrete model），或者为了进行研究而选择一个更通用/抽象的模型（generic/abstract model）。

某种与该属性所在具体系统无关的特性。后者的一个例子是对撤销功能（undo functionality）的分析，将在第 3.3 节中讨论。

***我们对系统进行表示的目的是什么？*** —— 我们可能会创建一种形式化表示（formal representation），使其成为运行系统或原型系统*执行（execution）*的一部分。或者，我们可以使用形式化表示来执行自动化或手动*分析（analysis）*（例如，不同系统状态之间的平均按键次数）。最后，通常是形式化（formalising）的过程让分析者对所研究的系统有了更深刻的*理解（understanding）*。

## 29.2 仅为计算——即时计算（ad hoc calculations）

简单的数学计算在人机交互（Human-Computer Interaction, HCI）领域无处不在，且复杂度各异。最简单的层面是基础算术，例如在 GOMS 按键级模型（keystroke-level model）中 (Card et al. 1980; Card et al. 1983)。而 *信息觅食理论（information foraging theory）* 背后的模型则更为复杂，使用了微分方程（differential equations）(Pirolli 2007)。在可视化（visualisation）、信息检索（information retrieval）和图形学（graphics）等领域，数学同样占据核心地位。

即使是简单的“信封背面计算（back of the envelope calculations）”（即快速的粗略估算），在帮助人们理解问题方面也可能出奇地有效。我们将探讨两个这样的例子：屏幕输入（screen typing）和菜单深度（menu depth），随后将分析“五个用户就足够了（five users are enough）”这一观点背后更复杂的数学原理。

### 29.2.1 屏幕输入（On screen typing）

几年前，关于图形界面与更偏向文本的界面的比较（这类比较现在依然存在！）经常使用图形显示具有高“带宽（bandwidth）”这一观点。显然，这应该从[视觉感知（visual perception）](https://www.interaction-design.org/literature/topics/visual-perception)的角度来理解，而不仅仅是每秒的原始像素数，但对于输出而言，这似乎是相当合理的。但输入方面如何呢？屏幕按钮和图标是否增加了输入带宽？事实上，一个简单的菲茨定律（Fitts' law）计算表明，无论屏幕按钮的数量和大小如何，合理的打字速度总是更快（见方框）。两者的区别在于，键盘的词汇表（lexicon）是固定的，且无论在何种语境下都必须由用户来解读；而图形用户界面（GUIs）可以是上下文相关的（contextual），能够显示相应的操作（如果你了解信息论（information theory），这就是一种自适应压缩（adaptive compression）的形式）。请注意，一个小小的数学论证可以引导出一种设计视角。

多年后重新审视这些计算，在面对智能手机和平板设备的屏幕键盘时，它们或许更具相关性。在某种程度上，早期的计算在近期关于 iPad 屏幕键盘的研究中得到了证实，这些研究发现键盘输入与屏幕输入的比例约为 2:1。

**粗略计算（Back of the Envelope） —— 键盘输入 vs. 屏幕输入**

比较键盘与屏幕的输入速率，单位为每秒比特数（bits per second）。

键盘：

采用 (Dix et al. 2004) 中引用的 KLM 时间（Keystroke-Level Model）来计算输入时间。

目标数量 —— 64 个按键
熟练打字员 —— 每秒 9 个按键
速率 = $9 \times \log_2(64) = 54 \text{ bps}$（比特每秒）

屏幕：
屏幕宽度为 $W$，其上的元素大小为 $S$。到达目标的平均距离为宽度的一半。为了简化计算，假设屏幕为正方形且被目标完全填充。

菲茨定律（Fitts' Law）—— $0.1 \log_2 ( D/S + 0.5 )$
$D = W/2$
元素数量 —— $(W/S)^2$
速率 = $\frac{\log_2 ( (W/S)^2 )}{0.1 \log_2 ( W/2S + 0.5 )}$
$\approx \frac{2 \log_2 ( W/S )}{0.1 \log_2 ( W/S )}$
$= 20 \text{ bps}$

因此，屏幕点击的速度比打字慢近三倍！

### 29.2.2 最佳菜单深度（Optimal menu depth）

经常有人错误地过度应用关于工作记忆（working memory）的 7±2 原则（Miller 1956）。一个典型的例子是菜单系统（menu systems），你可能见过这样的建议：每个屏幕（例如网页）上的菜单项数量不应超过 7±2 个。在触摸屏上，较大的目标（targets）更容易点击，这再次暗示了少量且较大的目标是一个好主意。然而，单个屏幕上的菜单项越少，寻找特定内容所需的菜单层级（menu levels）就越多。

假设总共有 $N$ 个项目，且你选择每屏显示 $M$ 个菜单项。那么菜单层级的深度 $d$ 为：
$d = \log N / \log M$

如果我们观察单个显示界面，总耗时将是物理显示屏幕所需的时间与用户选择项目所需时间的之和，再乘以层级数：
$T_{total} = ( T_{display} + T_{select} ) \times d$

将 Fitts' law（菲茨定律）应用于 $T_{select}$ 并代入 $d$ 的公式，我们得到：
$T_{total} = ( T_{display} + A + B \log M ) \times \log N / \log M$
$= ( (T_{display} + A)/ \log M + B ) \times \log N$

请注意，屏幕数量增加带来的影响恰好抵消了较大目标所带来的收益，而唯一随菜单项数量变化的因素是单屏成本 $(T_{display} + A)$。这表明，每屏项目越多越好。看看几乎任何一个门户网站（portal site），你就会发现实践经验得出了同样的结论！事实上，还需要考虑其他额外因素；对于极小的目标，菲茨定律（Fitts' law）开始失效，这为目标尺寸设定了下限。此外，错误率的影响非常显著，因为这会导致屏幕显示的浪费，因此数量较少且解释清晰的项目可能会更好。对于数量较多的项目，另一个因素开始起作用，即用户在显示屏上定位项目所需的时间。有证据表明，对于线性菜单（linear menus），实际的选择时间更接近线性关系而非对数关系。重新计算表明，对于较大的屏幕，这种视觉搜索（visual search）成为了限制因素，导致最大菜单尺寸取决于刷新时间（但在大多数情况下，这仍然远大于 7±2！）。然而，[优秀设计（good design）](https://www.interaction-design.org/literature/topics/good-design)

屏幕组织（Screen Organisation）和子标题（Sub-headings）可以将这种视觉搜索（Visual Search）推回到对数情况（Logarithmic Case）（参见 Larson and Czerwinski 1998）。对于具有小型滚动显示屏（Scrolling Displays）的 WAP，其数据再次有所不同。请注意，追求精确性迫使我们将假设明确化，而且，关注关键因素（Critical Factors）有助于我们寻找潜在的设计方案（Design Solutions）。

### 29.2.3 五个用户就足够了

大多数从事人机交互（HCI, Human-Computer Interaction）和交互设计（Interaction Design）的人都听说过“五个用户就足够了（five users are enough）”这句话，无论它是被用来证明一项小规模研究的合理性，还是用来反驳一项用户数少于五个的研究。事实上，这一观点被过度使用和误用了，其程度可能超过了 Miller 的 7±2 原则。在这里，我们仅探讨其底层的数学模型（Mathematical Model），关于为什么“五个”不能充分回答“多少个用户才足够”这一问题的详细分析，请参阅 (Dix 2011)。

事实上，“五个用户就足够了”的根源最初在于 Nielsen 和 Landauer (Nielsen and Landauer 1993) 对经验数据（Empirical Data）的分析。他们从若干中大型软件项目的 [用户测试（User Testing）](https://www.interaction-design.org/literature/topics/user-testing) 中收集了数据。他们收集的数据包括每个开发周期中参与研究的用户数量、每位用户发现的问题数量，以及这些问题是否与其他用户重复。此外，至关重要的一点是，他们衡量了进行每次 [用户研究（User Study）](https://www.interaction-design.org/literature/topics/user-research) 的成本以及创建软件新 [迭代（Iteration）](https://www.interaction-design.org/literature/topics/design-iteration) 的成本。

随后，他们利用软件工程中用于模拟程序调试的数学方法，将通过用户研究或启发式评估（Heuristic Evaluations）发现的 [用户界面（User Interface）](https://www.interaction-design.org/literature/topics/ui-design) 问题视为

这类似于在软件测试过程中发现的编码 Bug。每个 Bug（用户界面缺陷，User Interface Defect）被认为在任何测试期间被发现的可能性相同，且与其他 Bug 完全独立。在不同 [测试](https://www.interaction-design.org/literature/topics/test) 轮次中发现的 Bug 重叠情况可用于估计发现单个 Bug 的概率，进而可用于（*inter alia*）估计尚未发现的 Bug 的可能数量。这与生物学家在进行标记重捕法（Capture/Recapture）研究以评估野生动物种群生存率时所使用的数学方法相似。

分析（在上述假设条件下）表明，发现的新问题数量随增加的用户数量呈指数级下降，这可用于创建成本效益图（Cost-Benefit Graph）。结果显示，[启发式评估](https://www.interaction-design.org/literature/topics/heuristic-evaluation) 的最大值（在不同类型的项目中取平均值）约为 5，而用户测试（User Testing）则接近 3（主要是因为后者被认为成本更高）。在此之后，执行 [迭代开发](https://www.interaction-design.org/literature/topics/iterative-development%09) 步骤会更具成本效益（与之前的假设相反，迭代开发被认为能为用户界面问题的发现“重置时钟”）。

如前所述，这一结果被广泛误用 (Dix 2011)，但我们可以从中得出两个普遍的教训：

- 数学模型（mathematical models）可能具有极大的影响力
- 在应用这些模型的结果时，理解其关键方面至关重要，尤其是其潜在假设（underlying assumptions）
- 模型的形式化（formality）使得探索这些潜在假设的精确性质变得更加容易，从而能够评估其适用范围（scope of applicability）

## 29.3 详细系统规范（Detailed system specification）

### 29.3.1 对话表示法（Dialogue notations）——何时采取何种操作

在日常生活中，对话是指两个或多个参与者之间的交流，通常（但并非绝对）是协作性的。

在用户界面中，“对话（Dialogue）”是指交互的结构，即人机“对话”的语法层（syntactic level）。对话构成了用户界面三个层级中的中间层，这在用户界面开发的早期阶段，特别是在 Seeheim 模型 (Pfaff and Hagen 1995) 中被定义：

- ***词法层（Lexical）***（在 Seeheim 模型中称为 *表现层 Presentation*）——图标的形状、实际按下的按键。
- ***语法层（Syntactic）***（即 *对话 Dialogue*）——输入和输出的顺序。
- ***语义层（Semantic）***（即 *功能层 Functionality*）——对内部应用程序/数据的影响。

当然，与人类对话相比，人机对话受到极大的限制。然而，某些人与人之间的对话同样具有形式化（formal）的特点。以婚礼仪式为例；它是一种针对三个参与者的脚本，展现了用户界面对话的许多特性：

- 它规定了顺序。
- 部分贡献是固定的——例如“我愿意（I do）”。
- 其他部分则是可变的——例如“你是否愿意，[男方姓名]……”。
- 交换戒指的指令与说出“以此戒指……”这些话是并发（concurrent）执行的。

作者在讲解关于对话的教程时，经常要求人们试着读一遍这些词句。想象一下，你刚刚这样做，对着一个完全陌生的人说了这些话。这是否意味着你与他/她结婚了？当然不是，这些词句本身是空洞且没有意义的；它们仅在法律语境下才具有效力。

如果在正确的地方，持有结婚证等条件下说出这些话，它们纯粹是婚姻的句法（Syntax），而没有任何语义（Semantics）。

![](https://public-media.interaction-design.org/images/encyclopedia/formal_methods/1.jpg)
作者/版权持有者：未知（待调查）。版权条款与许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外情况（Exceptions）”章节。

想象一下，你正在参加一场婚礼仪式，但当被问到时，新娘却说“我不愿意”？真实的对话通常存在多种替代方案（Alternatives）。婚礼剧本并没有考虑到这种情况；它假设当意外发生时，人们会自行解决。然而，在描述人机对话（Human–Computer Dialogues）时，我们不能假设计算机能够处理意外情况，因此我们必须考虑所有其他替代方案，即使其中一些方案可能是“不采取任何行动”。

有时，形式化的人类对话（Formalised Human Dialogues）能更清晰地处理这些替代方案。例如在审判中，当法官询问被告认罪还是不认罪时，审判进程取决于被告的回答。

因为人类具有应对能力，因此形式化人类对话的重点在于规范性响应（Normative Responses）；标准的审判流程无法应对女王突然走进来并说“砍掉她的头”这种情况。同样，虽然人机对话的规范（Specifications）需要更加完整，但它们通常会忽略某些极不可能发生的事情，例如用户

站在键盘上！

让我们来看看你如何运用对话表示法（Dialogue Notations）和分析。

想象你正在分析一个最高机密机构的安全控制面板（图 1.A）。该面板有两个分别标记为“+”和“–”的按钮，用于控制当前的警报状态（Alarm State）。警报状态分为三个等级，由三盏指示灯（绿色、黄色或红色）表示，按钮则用于提高或降低等级。

![](https://public-media.interaction-design.org/images/encyclopedia/formal_methods/image1.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

![](https://public-media.interaction-design.org/images/encyclopedia/formal_methods/image2.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

**图 29.1 A-B**：最高机密控制面板：(A) 控制面板 (B) 状态转移网络

图 1.A 中的图像是呈现层（Presentation Level），即面板的外观。规定对话的一种常用方法是使用某种形式的状态转移网络（State Transition Network, STN）。系统的每个主要状态或模式都被绘制为一个圆圈，有时则是视觉显示关键部分的缩略图。

可能的用户操作（在本例中为“+”和“–”按钮）的效果通过它们转换状态的方式来体现。图 1.B 展示了该控制面板的状态转换网络（State Transition Network, STN）。仅观察 STN——在不了解其具体含义的情况下——我们就可以提出一些问题：当状态为红色时，“+”按钮的作用是什么？当状态为绿色时，“–”按钮的作用又是什么？这就是形式化分析（Formal Analysis）——我们不需要知道 STN 代表的具体含义，但仅从模式中就能看出某些内容缺失了。在许多应用中（例如电视的节目控制），我们可能希望“+”按钮能从红色循环回绿色；但在本应用中（可能是一位处于压力下的操作员），我们可能不希望冒着意外将红色警报（red alert）更改为绿色的风险。

形式分析（Formal Analysis）告诉我们*需要*补充某些内容，而上下文理解（Contextual Understanding）则告诉我们具体*需要什么*。

在本例中，我们通过手动方式检查了图表，但形式化表示（Formal Representations）的一个优势在于它们通常也可以进行自动化分析。这种自动化分析有多种形式。

*模型检测器（Model Checkers）*已被应用于 HCI 研究中，用以验证某些预期的[可用性（Usability）](https://www.interaction-design.org/literature/topics/usability)属性是否成立（例如 (Campos and Harrison 2001)）。需要注意的是，这些工具必须采用相当复杂的方法来减少备选方案的总数，因为即使是简单的界面，其可能的路径数量也会迅速增长：如果仅有 10 种可能的动作（如图标、菜单选择、有效的按键），那么两次动作就有 100 种可能性，三次动作则有 1000 种，依此类推……同样，可能状态（Possible States）的数量也会迅速增长。假设我们有一个选项，例如字体是粗体、斜体、粗斜体还是均非（neither），这便产生了四个状态。现在，假设有第二个选项，例如五种可能的字体大小（9、10、11、12 或 14 磅）：此时可能的字体状态数量并非 4+5，而是 4x5=20。如果我们再增加一个“是否下划线”的选项，状态数将增加到 40 个。因此，模型检测器采用了穷举评估（Exhaustive Evaluation）与符号评估（Symbolic Evaluation）相结合的方法，但其能够分析的系统复杂度仍然受限。

事实上，在许多安全关键（Safety-critical）案例中，选项的数量

[规模]过大，以至于人类无法进行分析，但可以通过模型检测（Model Checking）或其他数学技术（如图分析（Graph Analysis）或矩阵代数（Matrix Algebra））来处理。Swansea 的 FIT Lab 将这些技术应用于医疗设备（Medical Instruments），从而能够计算出各种不同类型错误的概率（Cairns et al. 2010）。

![](https://public-media.interaction-design.org/images/encyclopedia/formal_methods/formal_nethods_for_medical_instruments.jpg)

作者/版权持有者：Courtesy of Bruce Cummins, US Navy。版权条款与许可：pd（公有领域（Public Domain），指共有财产且不含原创作者权的资料）。

**图 29.2**：医疗设备是一个典型的例子，在这种情况下，选项的数量可能过多而无法由人类分析，但可以通过模型检测（Model Checking）等方法来处理。

### 29.3.2 可执行系统模型（Executable system models）

早期对话表示法（dialogue notations）的用途之一是作为原型或部署的用户界面的一部分。在编写用户界面代码时，无论是点选式图形用户界面（GUIs）还是基于 Web 的系统，人们很容易迷失在单个操作的效果中，例如“当按下这个按钮时，接下来会发生什么”。在用户界面管理系统（user interface management systems, UIMS）的早期阶段，各种表示法十分常见，包括诸如 *BNF* 等形式语言、基于规则的转移系统以及状态转移网络（state transition networks, STNs）。其中最后一种最为常见，这可能是由于其图形化特性（尽管通常为了执行而将其转换为文本形式），并且一直在被使用，例如用于基于 JavaScript 用户界面的 Arrowlets 框架 (Phang et al. 2008)。然而，其他形式化方法（formalisms）仍在被使用，例如 Petri 网（Petri Nets）得到了广泛应用，尤其是在涉及空中交通管制等安全关键设计（safety critical design）的工作中 (Navarre et al. 2001)。

在研究实验室之外，很少见到有人使用那些最精确的对话规范（dialogue specification）技术，但链接图（link diagrams）却很常见，例如由 Denim (Lin et al. 2000) 及类似工具生成的图表，其中一些至少在原型阶段是可执行的，尽管这些通常不被视为是“形式化”的。此外，使用 UML 的团队可能会使用状态图（State Charts），尽管其应用是在较低层级而非用于对话层面。

- *基于模型的用户界面（Model-based user interfaces）*

从比对话更高层级的用户任务模型（User Task Models）开始建模，然后分阶段地对其进行细化，最终获得可运行的系统。

CAMELEON 参考模型 (Calvary et al. 2002) 将其分为四个层级：
- **最终用户界面（Final User Interface, FUI）** —— 在特定平台和语言上运行的实际界面，包含平台特定的组件（Widgets）。
- **具体用户界面（Concrete User Interface, CUI）** —— 在此层级，Java Swing 的 `JButton` 和 HTML 的按钮 (`<button>`) 都会被描述为通用的“图形化 2D 按钮（Graphical 2D push button）”。
- **抽象用户界面（Abstract User Interface, AUI）** —— 界面现在以一种模态无关（Modality Independent）的方式被抽象为“抽象交互对象（Abstract Interaction Objects, AIO）”；因此，一个“控制 AIO”可以是屏幕上的 2D 按钮，也可以是设备上的物理按钮。此外，AIO 之间的关系是通过空间和时间约束（Spatial and Temporal Constraints）来定义的，而非精确的布局。
- **领域/任务概念（Domain/Task Concepts）** —— 在此层级，界面本身几乎被忽略。相反，重点在于用户想要实现的目标；例如“加载文件”，而在更具体的层级中，这可能会被呈现为一个启动文件选择对话框的按钮。

该模型已被应用于多个系统中，包括 UsiXML (Limbourg et al. 2005) ([www.usixml.org](http://www.usixml.org/) 访问于 2011 年 3 月)，这是一个基于 XML 的用户界面表示法（Notations）和工具集。

### 29.3.3 抽象系统模型（Abstract system models）

对话模型（Dialogue models）和可执行模型（Executable models）均针对一个特定的被分析或被开发的系统。然而，正式方法（Formal Methods）可用于分析影响一类系统的广泛共性问题。

![](https://public-media.interaction-design.org/images/encyclopedia/formal_methods/image4.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。
**图 29.3**：PIE 模型

此类最早的抽象模型之一是 PIE 模型，由笔者及其在 York 的同事于 20 世纪 80 年代中期开发 (Dix and Runciman 1985)。PIE 模型将交互系统视为输入-输出（Input-Output）关系。用户输入是一系列基础命令的序列（例如，单个鼠标点击、击键）。出于历史原因，这些命令序列的集合被表示为 $P$（代表“程序” Program）。用户命令的轨迹（Traces）由系统进行解释（用 $I$ 表示该函数），从而产生各种形式的“效果”（Effects, $E$），其范围涵盖了从系统内部状态（Internal system state）的改变到蜂鸣器的响铃。通常效果可分为两类：较为持久的结果（Results, $R$），如打印出的文档；以及瞬时的显示（Display, $D$）。后者虽然被称为“显示”，但也包含了触觉（Haptic）或听觉（Aural）反馈等效果。证书为了分析时间、多窗口显示以及非确定性交互（non-deterministic interactions）等问题，研究者开发了多种变体 (Dix 1987; Dix 1990)。此外，基础的 PIE 模型（PIE model）有时会根据系统状态（system states）和更新函数（update function）'doit' 来重新表述，因为这样在讨论和分析问题时有时会更加便捷。使用正式模型（formal model）的一个优点是，我们无需争论哪种表示（representation）是最优的，而是可以直接写出它们之间相互映射（mapped on to one another）的方式：

`doit( c, I(p) ) = I( p c )`

从而使我们能够根据具体任务选择最合适的一种。

尽管 PIE 模型非常极简（minimal），但它使我们能够对一系列与系统可观测性（observability of the system）相关的属性给出精确定义，这在很大程度上是由当时“所见即所得”（WYSIWYG, 'what you see is what you get'）这一理念的流行所推动的。

其中最简单的一个定义是：

$\exists \text{ observe}: D \to R \text{ st. } \forall e \in E : f(\text{display}(e)) = \text{result}(e)$

这意味着存在 ($\exists$) 一个从显示界面（displays）到结果（results）的函数（此处称为 'observe'），使得对于交互系统（interactive system）的所有 ($\forall$) 状态（effects），将该函数应用于当前显示界面即可得出当前结果。换句话说，你可以通过观察当前屏幕来判定将获得什么结果。

当然，文档中经常有部分内容在屏幕之外，因此人们制定了更复杂的变体，以便能够表述为：“始终存在一组 [导航（navigation）](https://www.interaction-design.org/literature/topics/navigation-1) 命令，让你能够看到足够的信息以判定结果”。

随后，那些拥有特定系统符号表示法（notations）和工具的研究人员将这类属性（properties）作为检查项，通过手动方式，或使用模型检测器（model checkers）及其他自动化分析工具进行验证。

撤销系统（Undo systems）得到了广泛的研究，部分原因是这项工作最初开展时它是一个极其热门的话题，部分是因为它具有良好的代数属性（algebraic properties），使用形式化方法（formalisms）相对容易处理，还因为其存在一些棘手的边缘情况（edge case），使得非形式化的处理方式难以应对或容易出错。

最早的研究结果之一 (Dix 1991) 表明，实现“通用撤销（universal undo）”是不可能的，即无法设计一个单一的“撤销”按钮，能够撤销之前的任何操作，包括撤销操作本身。

当时，有多种系统采用了切换式撤销（toggle undo，在两种状态之间切换）的变体，并且据称其中一些系统遵循通用撤销属性（universal undo property）。

通用撤销属性可以使用 `doit` 表示法（'doit' representation）来定义：
$\forall s \in E, c \in Cu \text{ doit}(\text{undo}, \text{doit}(c, s)) = s$

让我们来看一下这个不可能性证明（impossibility proof）：

**1)** 考虑系统的任意状态 $s$ 以及任意两个命令 $a$ 和 $b$。想象执行 $a$ 或执行 $b$ 的效果。这将产生两个（通常是不同的）状态 $sa$ 和 $sb$：
$sa = \text{doit}(a, s), sb = \text{doit}(b, s)$

**2)** 考虑在状态 $sa$ 和 $sb$ 中应用撤销（undo），首先看状态 $sa$：
$\text{doit}(\text{undo}, sa) = \text{doit}(\text{undo}, \text{doit}(a, s)) \{ \text{展开} \}$
$= s \{ \text{通用撤销} \}$
同理，$\text{doit}(\text{undo}, sb) = s$ 同样成立。
也就是说，在每种情况下，撤销都能让我们回到初始状态，正如我们所预期的一样。

**3)** 最后，考虑在状态 $s$ 中应用撤销。除了作为初始状态外，它也是在状态 $sa$ 中应用撤销的结果（步骤 2）。也就是说，我们可能执行了这样一个序列：$a, \text{undo}, \text{undo}$。
从数学上表示：
$\text{doit}(\text{undo}, s) = \text{doit}(\text{undo}, \text{doit}(a, sa)) \{ \text{来自 (2)} \}$
$= sa \{ \text{通用撤销} \}$
然而，如果我们考虑 $b$，同样的论证也适用：
$\text{doit}(\text{undo}, s)= \text{doit}(\text{undo}, \text{doit}(a, sb)) \{ \text{来自 (2)} \}$
$= sb \{ \text{通用撤销} \}$
因此，这两个状态必须相同：$sa = sb$

由于该论证在步骤 (1) 中是通过选择任意状态和任意一对命令开始的，这意味着无论我们在系统的哪个位置，任何... 的效果...

命令总是执行同样的操作！就好像系统中只有一个按钮，每一次按键、鼠标点击，或者用锤子敲击背面，产生的结果都完全一样。此外，由于对“撤销”再次执行“撤销”会让我们回到起点，这意味着系统中最多只有两种状态……灯开关就是能够拥有通用撤销属性（universal undo property）的最复杂系统。

![](https://public-media.interaction-design.org/images/encyclopedia/formal_methods/image5.gif)
Author/Copyright holder: Unknown (pending investigation). Copyright terms and licence: Unknown (pending investigation). See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/about/terms-of-use) below.
**图 29.4**：空间句法着色（Space syntax colouring）

事实上，真实的撤销系统从未遵循这一属性（它们比灯开关复杂得多！），而是两种撤销方式的变体：

*   *切换式撤销（toggle undo）*：撤销操作让你在之前状态和当前状态之间来回切换，但你永远无法回溯超过一步。
*   *栈式撤销（stack undo）*：系统记录一个先前状态的栈（stack）。常规命令会被添加到栈中（形成部分历史记录），而撤销/重做（undo/redo）则在栈中上下导航（类似于 Web 浏览器的前进和后退）。然而，一旦你在执行撤销/重做过程中执行了任何常规命令，栈将在你当前所在的位置被截断，并改为添加新状态。证书对这些替代方案的形式化分析（Formal analysis）导致了对栈式撤销（stack undo）中“危险”点的分析（即在深度撤销/重做循环中，一次失误（slip）可能会导致大量工作丢失的情况），并且它还证明了切换式撤销（toggle undo）和栈式撤销是*唯一*满足撤销基础属性（basic properties）的机制 (Dix et al. 19997)。该分析使用了一个相当复杂的数学分支，称为范畴论（Category Theory），它在处理类似于图 3 和图 4 这种图表的“追箭”（arrow chasing）证明时尤其强大。

此外，撤销与浏览器后退（browser back）之间的结构相似性（structural similarities）意味着相同的分析技术也可以应用于后者，从而区分出这样一个事实：尽管“后退”看起来很简单（像撤销一样），但实际上在不同类型的系统中存在细微但重要的差异。

此时已经存在许多单用户撤销系统（single-user undo systems），但多用户

当时电子编辑（editing）还处于起步阶段。对多用户撤销（multi-user undo）的形式化分析（Formal analysis）使得在首批此类系统被创建之前，就能够识别出潜在的问题和解决方案策略。当组撤销系统（group undo systems）被开发出来时，它们遇到的正是形式化分析所揭示的那些问题和解决方案。

这体现了形式化方法（Formal Methods）的核心优势之一，即在实际系统存在之前就能够分析问题的能力。

## 29.4 世界模型（Models of the world）

正如第 1 节中所述，世界模型（Models of the world）比计算机系统模型（Models of computer systems）更为罕见，但可能具有极高的价值。这类模型没有明确的分类，通常是为了满足特定需求而特设的（ad hoc），因此本节仅给出三种截然不同的形式化模型（Formal models）示例。

### 29.4.1 空间句法——模拟世界中的移动与重要性

[空间句法（Space syntax）](http://www.spacesyntax.net/) 最初由 Hillier 在伦敦的 Bartlett School of Architecture 开发 (Hillier 1999)。此前已有各种研究尝试描述城市空间的连贯性（coherence）或可读性（legibility）问题，其中最具影响力的可能是 Lynch 的 “城市意象（image of the city）” (Lynch 1960)，但 Hillier 寻求的是一种更严谨的理论解释以及更严谨的工具。

在观察城市道路网络时，显而易见的“距离”衡量标准并非两点之间拉直的直线距离（crow-flies string）；除非你驾驶坦克或直升机，否则你无法简单地穿过或飞越建筑物。相反，人们倾向于测量沿道路路径的长度（通常被称为“曼哈顿距离（Manhattan block distance）”），并可能考虑到汽车的单行道系统。如果进一步深化，人们可能会考虑所花费的时间。对于行人来说，这与步行距离接近；但对于汽车而言，由于市中心通常较为拥堵，这可能会使地图产生偏差。

空间句法的一个核心洞察是，这些指标都无法捕捉人类对城市的感知，而这一感知的核心在于视线（line of sight）。如果两个地标在彼此的视线范围内，它们在某种意义上就建立了联系，并在我们的城市心理模型（mental model）中变得“接近”。此外，正是那些主要的转折点构成了心理上的

沿途的标记。空间句法（Space Syntax）将这些转弯（turnings）作为距离度量（metric of distance）。如果你需要转弯 5 次才能从 A 点到达 B 点，那么它们的空间句法距离就是 5。

以此作为度量，可以通过分析城市中的位置来获得中心性度量（centrality measure）：如果一个地点到所有其他地点的最大/平均距离较低，那么该地点就更具“中心性”。如果使用直线距离（crow-flies distance）或曼哈顿距离（Manhattan-block distance），这个中心点很可能接近城市的几何中心（geometric centre），但如果使用空间句法的转弯度量，结果可能会在不同的位置。图 5 A-B 展示了统一前后的柏林街道，其颜色根据空间句法方法进行标注。图 5 B 中的白线是柏林墙。请注意，柏林墙的存在意味着，从空间句法的[视角](https://www.interaction-design.org/literature/topics/point-of-view)来看，最中心区域（红色标注）在统一前并不位于城市的中心。

![](https://public-media.interaction-design.org/images/encyclopedia/formal_methods/image6a.jpg)
作者/版权持有者：Jake Desyllas。版权条款与许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”章节。

![](https://public-media.interaction-design.org/images/encyclopedia/formal_methods/image6b.jpg)
作者/版权持有者：Jake Desyllas。版权条款与许可：保留所有权利。

保留版权。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

**图 29.5 A-B**：柏林的空间句法（Space Syntax）着色图——柏林墙之前与之后

到目前为止，这仅仅是在绘制精美的图片，但令人惊叹的是，这些中心性（Centrality）的度量指标可以与其他指标进行比较，例如商店、餐厅和其他公共聚集地的密度。当进行此类比较时，发现两者之间存在极强的相关性，也就是说，仅基于城市几何结构（Geometry of the city）得出的空间句法度量指标，能够非常强有力地预测城市中真实的、以人为核心的活力中心。

当在移除柏林墙后重新对柏林市进行分析时，空间句法分析中的“中心”区域也随之发生了变化。在统一后的几年内，柏林的繁华区域发生了转移；一些此前安静的住宅区变成了商业区或购物区。这些转变与空间句法的预测完全一致。

类似的分析技术也被应用于建筑内部，使规划者能够确定会议室、咖啡区等设施的合适位置。

空间句法在人机交互（HCI）领域有两种应用方式。

首先，它被用于理解物理空间（Physical Spaces）中的数字干预（Digital Interventions）。例如，在 [Cityware project](http://www.cityware.org.uk/) 中，它被用于分析移动应用程序的使用情况，包括对移动轨迹的计算模拟（Computational Simulations of Movements）（Kostakos et al. 2010）。

第二种用途是用于虚拟环境（Virtual Environments）的生成。在 Tower project (Prinz et al. 2004) 中，研究者构建了居住式虚拟空间（Inhabited Virtual Spaces），用户可以在其中穿梭于文档和文件夹的表征（Representations of Documents and Folders）之间，这与赛博朋克小说（Cyberpunk Novels）中的场景非常相似。真实的城市是演化而来的，而这些则是人造空间，因此空间句法（Space-Syntax）被生成性地（Generatively）用于构建“可理解的”信息空间（Intelligible Information Spaces）。

### 29.4.2 信念与时间——艺术表演的建模

艺术似乎比可用性（Usability）离正式方法（Formal Methods）更远，然而形式主义（Formalism）已被用于理解艺术表演和艺术装置（Art Installations）。

在某些类型的行为艺术（Performance Art）中，谁是表演者、谁是观众的界限可能被刻意地模糊化。想象一下，在拥挤的城市广场中心，一群戴着白帽子的表演者开始同步移动；周围的人可能意识不到这一点，但身处高楼的人或许能清晰地看到。同样地，如果你在购物中心，有人开始表现得古怪，你可能需要一段时间才能意识到她是一名哑剧表演者（Mime Artist）。在某些电视节目的案例中，不知情的旁观者的反应也成为了这场奇观（Spectacle）的一部分。Certificates戏剧理论（Dramatic Theory）的一个关键方面是关于“框架（Frame）”的概念，该框架由时间以及（可能是虚拟的）空间所界定：无论它是剧场演出期间的舞台，还是城市广场中杂耍艺人周围的空间。为了构成一场表演，观众需要意识到存在一个表演框架（Performance Frame），而表演者则需要知道观众知道该框架的存在。这完全涉及到信念（Belief）问题，因此人们使用一种信念逻辑（Belief Logic）来对此进行建模。

![](https://public-media.interaction-design.org/images/encyclopedia/formal_methods/2.jpg)

作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”部分。

**图 29.6**：
本图以图形和逻辑形式展示了该情境。如果满足以下条件，Alison 就在向 Brian 进行表演：(i) Alison 认为她的行为（潜在地且间接地）可被 Brian 观察到；(ii) Brian 认为这些行为是戏剧框架的一部分；(iii) Alison 认为 Brian 认为这些行为是该框架的一部分。这种复杂的信念链（A 认为 B 认为 A 正在做某事）难以通过直觉思考，因此形式化（Formalising）有助于追踪谁在何时知道什么。这随后被用于分析一个名为 Deus Oculi 的特定装置，该装置刻意地将部分组件之间的互连

模糊。分析表明，该装置的关键“顿悟时刻（aha moment）”恰恰发生在特定的信念转换（transition of beliefs）之时。

![](https://public-media.interaction-design.org/images/encyclopedia/formal_methods/image8.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

**图 29.7**：Deus Oculi —— 两人与展品交互时的信念图表（tableaux of beliefs）

### 29.4.3 物理图 (Physigrams) —— 数字设备的物理特性建模

在人机交互（Human-Computer Interaction, HCI）文献中，平凡的灯光开关几乎像文字处理器一样无处不在。它已从多个维度被分析：其使用中隐含的文化理解、开关方向与功能的映射（Mapping）（向下是关还是开？）、一组开关与房间内灯光之间的映射，甚至包括因将其误认为电梯召唤按钮而意外关灯的情况（作者本人也曾因犯相反的错误而触发了火警！）。在这里，我们将重点讨论灯光开关在“脱离电路（unplugged）”状态下的物理交互（Physical interactions）。

我们可以将灯光开关视为一个二状态设备（Two state device）：灯亮/灯灭；按下开关，灯亮；抬起开关，灯灭。然而，请注意前一句中的“然后（and the）”：首先是与开关的物理交互，随后这一交互才引发对灯光的影响。

![](https://public-media.interaction-design.org/images/encyclopedia/formal_methods/image10.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

![](https://public-media.interaction-design.org/images/encyclopedia/formal_methods/image11.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：

未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

**图 29.8 A-B**：灯光开关 (A) 物理设备 (B) 逻辑状态（Logical States）

图 8 将这两者分离开来。左侧（图 8.A）是开关本身的两种状态，右侧（图 8.B）是灯的两种状态。同时绘制这两者使我们能够讨论诸如开关位置与灯光状态之间的映射（Mapping）等问题。在本例中，这种映射相当明显，但在更复杂的设备中，这种映射可能是我们需要详细分析的内容。任何此类讨论的关键都在于同时拥有*这两张*图表。

右侧的图表（灯的开/关状态）通常代表设备的复杂数字状态（Digital State），例如电视当前的频道选择。这类问题在软件工程的形式化方法（Formal Methods）中经常被处理，并且是人机交互（HCI）中形式化方法所采用的典型细节水平。

![](https://public-media.interaction-design.org/images/encyclopedia/formal_methods/image12.jpg)

作者/版权持有者：未知（待调查）。版权条款与许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

**图 29.9**：在按下后会“回弹”的计算机灯光开关

相比之下，左侧的图关注的是物理开关本身。它捕捉了其物理潜能中固有的交互属性/可供性（[Affordances](https://www.interaction-design.org/literature/topics/affordances)），即使该开关被从墙上拆下并断开电源——字面意义上的“拔掉插头”——这些属性依然存在。想象一个小孩在玩一个旧开关，只是简单地前后推动它。

物理图（Physigrams）是状态转移网络（State Transition Network, STN）的一种改进形式，旨在定义这些物理交互。它们类似于普通的 STN，但增加了一些特性，以应对物理行为与数字行为不同的事实。例如，图 9 展示了计算机上常见的按压式按钮开关的物理图。与简单的灯光开关不同，它几乎总是处于相同的位置；它看起来非常像一个单状态设备！然而，事实上它确实有一个“按下（in）”状态，但只有在你按住它时才会处于该状态，这被称为*张力状态（tension state）*。 “按下”状态周围的虚线表示它是一个张力状态，而闪电形状的箭头则表示由于开关内部弹簧的作用，状态转移是自动发生的。正式方法（Formal Methods）通常被认为对于“普通”设计师来说过于困难，仅适用于专家。然而，这种图表化表示（diagrammatic representation）其实是非常易于理解的（[accessible](https://www.interaction-design.org/literature/topics/accessibility)）（事实上，你在消费者指南中也能发现状态转移网络 [STNs]）。图 10 A-B 和 11 A-B 展示了产品设计师绘制的物理图（physigrams），他们利用这些图表来比较针对同一底层数字功能（digital functionality）的两种物理设备设计的属性。虽然这些设备在许多方面都很相似（例如圆形控制装置、管理滚动菜单），但物理图突出了关键差异，特别是其中一台设备（滚动触控板 [scroll pad]）缺乏触觉反馈（tactile feedback）。

![](https://public-media.interaction-design.org/images/encyclopedia/formal_methods/image13.jpg)
作者/版权持有者：未知（待调查）。版权条款与许可：

未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”章节。
![](https://public-media.interaction-design.org/images/encyclopedia/formal_methods/image14.jpg)
作者/版权持有者：未知（待调查）。版权条款与许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”章节。
**图 29.10 A-B**：由产品设计师创建的物理图（Physigrams）
![](https://public-media.interaction-design.org/images/encyclopedia/formal_methods/image15.jpg)
作者/版权持有者：未知（待调查）。版权条款与许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”章节。
![](https://public-media.interaction-design.org/images/encyclopedia/formal_methods/image16.jpg)
作者/版权持有者：未知（待调查）。版权条款与许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”章节。
**图 29.11 A-B**：由产品设计师创建的物理图（Physigrams）

## 29.5 一个成功案例

衡量方法的有效性（effectiveness）通常十分困难，特别是当其主张能够提升诸如质量（quality）或可维护性（maintainability）等无形指标（intangibles）时。此外，考虑到人员和项目的差异性（variability），即使可衡量指标（measurable indicators）出现了 30-50% 的巨大差异，也可能难以被察觉。因此，作为一个例子，我将回顾近 30 年前的一件事。这并不是因为在那之后没有出现过成功案例（！），而是因为该案例的影响极其显著——生产率（productivity）提升了 1000%（没错，是十倍）。

### 29.5.1 问题所在

这源于我的个人经历，那时我还不是一名学者，甚至从未听说过人机交互（Human-Computer Interaction, HCI）。我当时在 Cumbria County Council 工作，使用 COBOL 编写事务处理程序（transaction processing programs），这类程序通常用于大型组织的库存控制或销售点终端（point-of-sale terminals）。

虽然这听起来像是非常古老的技术（大型机！），但事实上，事务处理系统与基于 Web 的系统（web-based systems）非常相似：一个来自某个终端的消息被发送进来，需要经过处理，然后发送回响应，接着处理下一个通常来自完全不同终端的消息。

这些问题与如今在基于 Web 的界面中偶尔见到的问题十分相似：应用程序有时会“丢失”其在交互序列（interaction sequences）中所处的位置，并表现出奇怪的 Bug。其中一次，某个终端的用户在列表界面点击“下一页”，结果得到了一个出乎意料的结果——这竟然是另一个完全不同终端的“下一页”内容。此外，编写这些充满 Bug 的代码耗费了人们大量的时间。

然而，当你审视代码时，其质量和效率的低下也就不足为奇了。图 12 展示了这些代码的大致样子。

```
if confirm_field is empty // 不可能是确认界面<br /> // 或者用户没有填写 Y/N 框<br /> then if record_id is empty // 必须是初始输入 <br /> then prepare 'which record to delete' screen<br /> else if valid record_id<br /> then read
```

记录并准备确认界面<br /> 否则准备错误 
界面<br /> 否则如果 confirm_field = "Y' <br /> 那么如果 
record_id 为空 // 格式错误（malformed）<br /> 那么准备错误 
界面<br /> 否则如果 record_id 有效<br /> 否则执行 
删除<br /> 那么准备错误界面<br /> 否则如果 
confirm_field = "N' <br /> 那么准备“返回主菜单” 
界面<br /> 否则准备“必须回答 Y/N”界面

**Figure 29.12**: 典型的 20 世纪 80 年代事务处理（Transaction Processing）代码

Web 的 URL 结构使得这一点变得简洁了一些，而且我知道一些优秀的 Web 程序员能够编写出极其精简的代码。然而，如果你看过大量的 Web 界面代码，尤其是那些来自大型开源项目的代码，这种选择与子选择的嵌套（Nest）并不罕见。其关注点在于单个页面、单个事务，而开发者的思维模式处于一种“刚刚发生了什么，接下来会发生什么？”的状态。

### 29.5.2 解决方案

面对这种情况，我知道我无法理清其中的头绪，因此寻找了一种使其变得可控的方法。手头最显而易见的工具就是简单的流程图（Flow chart）。然而，我并没有创建程序代码的流程图（这是常规用法），而是使用了如图 11 所示的流程图，用以绘制主要界面及其之间的交互动作。也就是说，我创建了一份对话规范（Dialogue specification）。描述界面之间计算机操作的方框通常描述得较为笼统，例如将记录保存到磁盘可能需要一系列变量的移位、调用文件系统代码等，但这些正是程序员的工作。流程图关注的是最困难的部分：掌控全局（Big picture）。

遗憾的是，当时没有自动化工具，因此我手动将纸质流程图转化为模板化代码（Templated code）。每个界面对应一个代码块，用于组装发送到终端（Terminal）的消息，以及每个界面之后运行的计算代码块。细小的标识符（Identifiers）被用作代码中的标签（goto!），这样当出现问题或需要进行更改时，可以轻松地找到相应的代码。它们也被放置在屏幕的顶角作为标识符，以便用户在报告问题时将其作为代码提供。最后，流程图使得人们能够轻松地查看是否已经对对话中的所有部分进行了测试（这与...不同

（……正如代码中的所有路径 [paths] 一样）。然而，最重要的一点是速度。绘制流程图（Flow Chart）并将其转化为代码，比直接编写代码要快得多（而且这还是在没有任何支持工具的情况下）。在与用户讨论之后，周转时间（Turnaround Time）的差异则更为显著。需要记住的是，那时还处于快速应用程序开发（Rapid Application Development）普及之前的时代；通常情况下，创建和更新这类应用程序需要数天甚至数周的时间，但现在，更改可以在数小时内完成，比标准方法快约 10 倍。

![](https://public-media.interaction-design.org/images/encyclopedia/formal_methods/image17.jpg)
作者/版权持有者：未知（待调查）。版权条款与许可：

未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。
**图 29.13**：用户交互（User Interaction）流程图

### 29.5.3 为什么它能奏效？

虽然这是正式方法（Formal Methods）在界面设计中的一次非常成功的应用，但当时我并不明白*为什么*。直到在随后的几年中通过反思，我才开始理解促成其成功的各种因素之间复杂的相互作用，以及有助于复制这一成功的指导原则。

***实用性（useful）*** —— 解决了实际问题！
该符号系统专注于导致现有系统出现困难的整体用户界面对话结构（user-interface dialogue structure）。通常，许多形式化方法（formalisms）被提出是因为它们具有某些良好的内在属性（intrinsic properties），或者在其他方面表现出色，但并没有解决实际的需求。

***恰当性（appropriate）*** —— 细节程度恰到好处，不过度详细
例如，编写访问数据库等详细代码并没有困难，因此该形式化方法在非常粗粒度（crude level）的级别上处理这些操作，如“读取记录”、“删除记录”等。许多形式化方法会强迫用户填充不必要的细节，这不仅增加了使用成本，还让人难以关注真正需要解决的问题。

***沟通性（communication）*** —— 简单的示意图和清晰的流程，便于与客户进行讨论
人们通常声称，正式方法因其精确性而能成为改善设计团队内部沟通的手段。然而，当精确性是以牺牲可理解性（comprehensibility）为代价时，真正的沟通便不复存在。

***互补性（complementary）*** —— 与实现（implementation）采用不同的范式（paradigm）
常见的情况是使用能够反映最终结构的规范方法（specification methods）

系统的——例如，针对面向对象系统（Object-oriented systems）的面向对象规范（Object-oriented specification）。然而，在这里，该规范代表的是对话结构（Structure of the dialogue），这与代码结构完全不同。这种设计是刻意为之的：这种符号表示法（Notation）允许人们从一个*不同的视角*来审视系统，在这种情况下，该视角更适合于创建和评估界面设计（Interface design）。符号表示法结构与代码结构之间的关系是通过简单的规则来管理的，而这正是形式化方法（Formalisms）的优势所在！

***快速回报（Fast pay back）*** —— 应用程序的产出速度更快（至少提升了 1000%）
通常人们认为，形式化方法（Formal Methods）将带来*长期*的时间节省。然而，大多数人更喜欢即时回报。为了后期的节省而在前期投入大量时间是非常值得赞赏的，但开发者和客户通常更愿意看到一个带有缺陷的原型（Buggy prototype），而不是被告知“……是的，几个月后一切都会就绪”。对话流程图（Dialogue flowcharts）不仅带来了长期节省，还缩短了看到第一个运行系统的前置时间（Lead-time）。

***响应迅速（Responsive）*** —— 变更的快速周转（Turnaround of changes）
掌控感和理解力使得安全地进行变更变得更加容易。在某些形式化方法中，规范与代码之间的转换过程（Transformation process）极其复杂，导致变更成本非常高（关于此点的讨论请参阅 Dix and Harrison 1989）。当然，随着用户

无论界面（interfaces）定义得多么详尽，只有在实际使用时，我们才能真正全面地理解需求（requirements）。

***可靠性（reliability）*** —— 清晰的样板代码（boilerplate code）降低了出错率。
虽然从图表到代码的转换过程并非自动化，但它是一个相当自动化的手动过程，即应用并修改样板代码模板。这种对标准代码片段的高度复用极大地提高了代码的可靠性。

***质量（quality）*** —— 易于建立测试周期（test cycle）。
图表和代码的清晰标注使得追踪所有路径是否都经过测试变得十分简单。然而，请注意，这些路径不仅是指程序的执行路径（程序在每次事务时实际上都会重启），还包括人机对话（human–computer dialogue）中的每条路径。

**维护（maintenance）** —— 易于将缺陷/增强报告与规范（specification）及代码联系起来。
呈现给用户的界面屏幕包含了标签，使得在代码和规范中追踪缺陷报告或变更请求变得十分容易。

简而言之，这种形式化方法（formalism）是为了实现特定目的而使用的，最重要的是，它既不追求完美，也不拘泥于纯粹主义！！

## 29.6 接受度障碍

正如引言中所述，正式方法（Formal Methods）在人机交互（Human-Computer Interaction, HCI）领域中的地位一直较为尴尬，在 CHI 社区中从未受到欢迎，并且可能会引发一些激烈的批评（vitriol）——这在一个通常非常包容的学科中是很难解释的。

几年前，在一次 HCI 会议担任元评审员（meta-reviewer）时，我不得不完全忽略一份评审意见，因为该评审员唯一的批评点就是简单地因为论文采用了正式方法而将其否定，并声称这显然不是一个可接受的领域；评审员建议作者应该转向民族志（ethnography）或社会科学（social science）。请注意，尽管该会议的一个[研讨会（workshops）](https://www.interaction-design.org/literature/topics/workshops)正是关于正式方法的，但这种情况依然发生了。很难想象会有类似的评审意见仅仅因为研究领域而否定一篇民族志或实验性论文。公平地说，这可能反映了社会（或至少是英美社会）的普遍趋势：人们经常听到受过教育的人吹嘘自己的数学能力匮乏（innumeracy），而他们会对文盲（illiteracy）感到深感尴尬。此外，即使在许多计算机科学系中，关于更形式化主题的教学也有所减少，因为学生入学时的数学基础使得这些主题或诸如图形学（graphics）等课题难以达成。

因此，在人机交互（Human-Computer Interaction, HCI）领域倡导形式化方法（Formal Methods）并不会让你受欢迎！形式化方法不仅需要专业知识，而且在时间成本方面往往较高，在任何“实际”工作出现之前，很难证明投入大量分析时间的合理性。虽然可以认为这具有长期收益，但当项目已经进行了三个月且尚未编写任何代码时，这种说法很难被认可。这一直是一个问题，而在采用[敏捷开发（agile development）](https://www.interaction-design.org/literature/topics/agile-development)技术时，这一问题尤为突出。

这些成本障碍在个体层面同样存在。根据我的个人经验，当我在实际开发中广泛使用形式化方法时，事后显而易见的是，由此产生的系统设计更佳、更鲁棒（robust），且开发时间比...更短。

更多临时的处理方法（ad hoc approaches）。然而，尽管深知这一点，每当面对新项目时，我还是习惯于直接上手尝试（hack）！详尽的规划和准备虽然有其价值，但其投入产出比（bang for the buck）在后期才会显现——这与[人类心理学（human psychology）](https://www.interaction-design.org/literature/topics/human-psychology)的特性并不相符。

## 29.7 未来方向

尽管存在上述障碍和普遍的质疑，仍有许多研究小组在该领域持续产出高质量的工作，且通常与工业界紧密合作；此外，基于模型的用户界面开发（model-based user interface development）在 W3C 中也是一个活跃的研究方向。此外，该领域的多项学术会议——包括 DSVIS、EHCI 和 TAMODIA 系列会议——现已成为由 IFIP 和 ACM 共同赞助的新会议 EICS（Engineering Interactive Computer Systems）的一部分。该会议涵盖多个领域，而形式化方法（Formal Methods）是其中的一个重要分支。

考虑到应用形式化方法的成本，多年来该方法最一致地被应用于安全关键（safety critical）场景，这并不令人意外，因为在这些场景中，错误的后果极其严重，因此采用形式化方法的成本是可以接受的。例如，Toulouse 的研究小组在航空交通管制工作中使用了 Petri 网（Petri Nets）的变体，而 Swansea 的研究小组则在医疗仪器中使用了图方法（graph methods）。

然而，从更广泛的视角来看，现在似乎是该领域增长的成熟时机。在 Web 端，界面需要协调多个 API 服务，需要适配不同的设备，并且具有多个执行“线程”（threads of execution），如会话（session）、窗口（window）和严格的时间顺序（strict chronology）。在我们的家庭和工作场所中，多种设备开始相互“对话”，因此我们与手机的交互可能会影响到我们的电视或

洗衣机，我们的中央供暖系统则响应手动控制、外部温度以及智能[电网](https://www.interaction-design.org/literature/topics/grid-systems)（smart grid）的动态定价。传统的功能性设计（functional design）将事物（包括用户界面元素）分解为在认知上可管理的块（intellectually manageable chunks）。相比之下，简单元素之间复杂的交互难以理解，并可能导致在常规测试中无法显现的涌现效应（emergent effects）。在敏捷开发（Agile development）中，自动化测试（automated testing）是该学科的核心，然而用户界面在测试套件（test suite）中的体现往往最不充分。

这些问题迫切需要形式化方法（Formal Methods）来解决！

鉴于此，专注于不同设备适配的 W3C 小组采用基于模型的技术（model-based techniques）也就不足为奇了。同时在英国，有几个大型项目正在研究 Web 上人类主体（human agents）与软件系统之间复杂的交互，而 Web 科学（Web Science）的某些分支显然与此有所重叠。

在实践层面，有趣的是，从业者在基于 Web 的系统的不同层级中创建临时的声明式表示（declarative representations）；他们经常使用 JSON、turtle、XML 或其他通用数据表示来创建专用表示法（special purpose notations）。正如在“成功案例”中所见，他们使用这些形式化表示（尽管他们不会这样称呼），是因为这些方法有效，因为它们让工作变得更轻松。它们并非一项苦差事，而非

这种药物最终会让你康复，但现在就具有价值。形式化方法（Formal Methods）社区的一个弱点在于，未能意识到设计师、开发人员以及用户实际上都是人类。公平地说，这一指责同样可以针对广义上的以用户为中心的设计（User-centred Design），因为所有的人机交互（Human-Computer Interaction, HCI）方法往往在前期投入巨大（up-front heavy），并承诺在未来获得回报。因此，Randolph Bias 和 Deborah Mayhew 在 "Cost Justifying Usability" (Bias and Mayhew 1994) 中所做的工作至关重要。

我希望下一代研究人员（或者当前这一代！）能够解决这个问题。在某种程度上，基于模型的开发（Model-based Development）领域正在发生这样的变化，但其符号表示法（Notations）仍然显得过于复杂（top-heavy）。

理想情况下，我们应当创建这样的符号系统（notations）和工具：在使用的每个阶段，它们仅需要适度的投入（just enough effort）即可在该阶段产生价值。然而，这种“适度”形式化（formality）的累积整体效果，将意味着能够获得一个足够完整的形式化表示（formal representation），从而用于进一步的分析。

什么样的符号系统才能让那些从业者（practitioners）不必每次都创建自己的临时符号（ad hoc notations）？

## 29.8 更多学习资源


### 29.8.1 书籍（纸质版或在线版）

- A. J. Dix (1991). *Formal Methods for Interactive Systems*. Academic Press. ISBN 0-12-218315-0 [http://www.hiraeth.com/books/formal/](http://www.hiraeth.com/books/formal/)
  这是我早期在该领域撰写的专著。书中涵盖了 PIE 模型以及其他正式方法（Formal Methods）和模型。尽管这本书已有 20 年历史，但我最近发现自己仍在重新研究其中的几种技术，并将其应用于近期的开发项目中。
  该书已绝版，但完整文本可在上述书籍网站上免费下载 PDF。
- Paternó, F. (2000). *Model-Based Design and Evaluation of Interactive Applications*. London, Springer-Verlag.
  本书回顾了人机交互（HCI）中使用的多种模型，随后以 ConcurTaskTrees 作为核心表示方法，探讨了整个设计生命周期（design lifecycle）。请注意，这里的“基于模型（model-based）”是指广义上的模型，而非 3.2 节中讨论的“基于模型的用户界面开发（model-based user interface development）”（尽管 Fabio Paternó 也深入参与了该领域的研究）。
- H. Thimbleby, *Press On — Principles of Interaction Programming*, MIT Press, 2007, ISBN: 0262201704
  平装版，ISBN 978–0–262–51423–1, 2010.
  这本书关于交互系统（interactive systems）的编程，但在书中，Harold 详细探讨了在构建和分析过程中各种形式化方法（formalisms）的使用。

### 29.8.2 章节

以下两章可在网上获取，尽管遗憾的是，收录它们的优秀文集目前已绝版。本百科条目的若干部分大量参考了 "Upside down As"：

- A. J. Dix (1995). Formal Methods. In Perspectives on HCI: Diverse Approaches, Eds. A. Monk and N. Gilbert. London, Academic Press. pp. 9-43. [http://www.alandix.com/academic/papers/formal-chapter-95/](http://www.alandix.com/academic/papers/formal-chapter-95/)
- Upside down As and algorithms - computational formalisms and theory In HCI Models, Theories, and Frameworks: Toward an Multidisciplinary Science. John Carroll (ed.) ISBN 1-55860-808-7. Morgan Kaufman, 2003. pp. 381-429 [http://www.alandix.com/academic/papers/theory-formal-2003/](http://www.alandix.com/academic/papers/theory-formal-2003/)

我的 [HCI textbook](http://hcibook.com/e3/) 中有两章详细探讨了与形式化（formalism）相关的问题：

- [第 16 章：对话表示法（Dialogue notations）与设计](http://hcibook.com/e3/chapters/ch16)
- [第 17 章：系统模型（Models of the system）](http://hcibook.com/e3/chapters/ch17)
  A. Dix, J. Finlay, G. Abowd and R. Beale (2004). *Human-Computer Interaction, third edition.* Prentice Hall. ISBN 0-13-239864-8.

### 29.8.3 Conferences

- ***EICS: ACM SIGCHI Symposium on Engineering Interactive Computer Systems***（2009年起每年举办一次）。
  [eics-conference.org](http://eics-conference.org/)
  该会议的职责范围比纯粹的形式化方法（Formal Methods）更广，但该领域的主要研究者倾向于在此发表成果。请注意，若干较早的会议已合并形成 EICS（见下文）。
- ***FMIS: Formal Methods for Interactive Systems***（2006年起每年或每两年举办一次）。
  [fmis.iist.unu.edu/fmis_events.html](http://fmis.iist.unu.edu/fmis_events.html)
  一个专门针对该主题的小型研讨会（Workshop）。

### 29.8.4 Conferences (older)

以下会议已合并至 EICS，但许多关键论文仍可在旧的会议论文集（Proceedings）中找到。
- ***DSVIS: Design, specification, and verification of interactive systems***（1994–2008年每年举办一次）。这可能是人机交互（HCI）领域中形式化方法的关键年度发表场所（尽管并不局限于此）。
- ***EHCI: Engineering Human–Computer Interaction***（每三年举办一次）。由 IFIP WG2.7/13.4（用户界面工程 User Interface Engineering）组织的定期会议，该工作组（Working Group）是唯一一个同时列在两个技术委员会下的 IFIP 工作组。
- ***TAMODIA: Task Models and Diagrams***（2002-2010年每年举办一次）。
- ***CADUI: Computer Aided Design of User Interfaces***（2002??–2008年每年举办一次）。

### 29.8.5 书籍（已绝版，但可能在图书馆中）

这些书籍已绝版，但可以在线购买到少量二手副本。
- Harrison, M.D. and Thimbleby, H.W., editors (1990). Formal Methods in [Human Computer Interaction](https://www.interaction-design.org/literature/topics/human-computer-interaction). Cambridge: Cambridge University Press.
  Harrison 和 Thimbleby 在 1990 年编辑的这部合集包含了许多该领域早期研究者的贡献。
  我在该书中的章节可在以下网址获取：[http://www.alandix.com/academic/papers/nond90/](http://www.alandix.com/academic/papers/nond90/)
- Palanque, P. and Paternó, F., editors (1997). Formal Methods in Human Computer Interaction. London, Springer-Verlag.
  Palanque 和 Paternó 编辑了一部较新的合集，令人困惑的是，其书名与上述书籍完全相同！这部合集是以主题为导向的，贡献者们使用了各种不同的形式化方法（Formal Methods）技术，并以网页浏览器（Web Browser）作为共同示例进行探讨。
  我在该书中的章节可在以下网址获取：[http://www.alandix.com/academic/papers/histchap97/](http://www.alandix.com/academic/papers/histchap97/)

## 29.9 References

[Anderson](https://www.interaction-design.org/references/authors/john_r__anderson.html), John R. (2005): *Human Symbol Manipulation Within an Integrated Cognitive Architecture*. In [Cognitive Science](https://www.interaction-design.org/references/periodicals/cognitive_science.html), 29 (3) pp. 313-341
[Bias](https://www.interaction-design.org/references/authors/randolph_g__bias.html), Randolph G. and [Mayhew](https://www.interaction-design.org/references/authors/deborah_j__mayhew.html), Deborah J. (eds.) (1994): *Cost-Justifying Usability.* Boston, MA, Academic Press
Calvary
 et al. 2002. Calvary, G., Coutaz, J., Bouillon, L., Florins, M., 
Limbourg, Q., Marucci, L., Paternò, F., Santoro, C., Souchon, N., 
Thevenin, D., Vanderdonckt, J., 2002 The CAMELEON Reference Framework, 
Deliverable 1.1, CAMELEON Project. [http://giove.isti.cnr.it/projects/cameleon/deliver...](http://giove.isti.cnr.it/projects/cameleon/deliverable1_1.htm)
[Campos](https://www.interaction-design.org/references/authors/j__c__campos.html), J. C. and [Harrison](https://www.interaction-design.org/references/authors/michael_d__harrison.html), Michael D. (2001): *Model checking interactor specifications*. In [Automated Software Engineering](https://www.interaction-design.org/references/periodicals/automated_software_engineering.html), 8 (3) pp. 275-310

[Card](https://www.interaction-design.org/references/authors/stuart_k__card.html), Stuart K., [Moran](https://www.interaction-design.org/references/authors/thomas_p__moran.html), Thomas P. and [Newell](https://www.interaction-design.org/references/authors/allen_newell.html), Allen (1983): *The Psychology of Human-Computer Interaction.*Hillsdale, NJ, Lawrence Erlbaum Associates
[Card](https://www.interaction-design.org/references/authors/stuart_k__card.html), Stuart K., [Moran](https://www.interaction-design.org/references/authors/thomas_p__moran.html), Thomas P. and [Newell](https://www.interaction-design.org/references/authors/allen_newell.html), Allen (1980): *The keystroke-level model for user performance with interactive systems*. In [Communications of the ACM](https://www.interaction-design.org/references/periodicals/communications_of_the_acm.html), 23 pp. 396-410
[Diaper](https://www.interaction-design.org/references/authors/dan_diaper.html), Dan and [Stanton](https://www.interaction-design.org/references/authors/neville_stanton.html), Neville (2003): *The Handbook of Task Analysis for HCI.* Hillsdale, New Jersey, USA, Lawrence Erlbaum Associates

[Dix](https://www.interaction-design.org/references/authors/alan_j__dix.html), Alan J. (2003): Upside-down A's and Algorithms - Computational Formalisms and Theory. In: [Carroll](https://www.interaction-design.org/references/authors/john_m__carroll.html), John M. (ed.). "HCI Models, Theories, and Frameworks". San Francisco: Morgan Kaufman Publisherspp. 381-428
[Dix](https://www.interaction-design.org/references/authors/alan_j__dix.html), Alan J. (1991): *Formal Methods For Interactive Systems.* Academic Press
[Dix](https://www.interaction-design.org/references/authors/alan_j__dix.html), Alan J. (2011). *Are five users enough? HCI Book: Online*. Retrieved 31 January 2012 from [http://www.hcibook.com/e3/online/are-five-users-en...](http://www.hcibook.com/e3/online/are-five-users-enough/)
[Dix](https://www.interaction-design.org/references/authors/alan_j__dix.html), Alan J. (1987): The Myth of the Infinitely Fast Machine.. In: [Diaper](https://www.interaction-design.org/references/authors/dan_diaper.html), Dan and [Winder](https://www.interaction-design.org/references/authors/russel_winder.html), Russel (eds.) [Proceedings
 of the Third Conference of the British Computer Society Human Computer

Interaction Specialist Group - People and Computers III](https://www.interaction-design.org/references/conferences/proceedings_of_the_third_conference_of_the_british_computer_society_human_computer_interaction_specialist_group_-_people_and_computers_iii.html) August 7-11, 1987, University of Exeter, UK. pp. 215-228
[Dix](https://www.interaction-design.org/references/authors/alan_j__dix.html), Alan J. (1990): Non-determinism as a paradigm for understanding the user interface. In: [Harrison](https://www.interaction-design.org/references/authors/michael_d__harrison.html), Michael D. and [Thimbleby](https://www.interaction-design.org/references/authors/harold_thimbleby.html),
 Harold (eds.). "Formal Methods in Human-Computer Interaction (Cambridge
 Series on Human-Computer Interaction)". Cambridge University Press
[Dix](https://www.interaction-design.org/references/authors/alan_j__dix.html), Alan J. and [Harrison](https://www.interaction-design.org/references/authors/michael_d__harrison.html), Michael D. (1989): Interactive systems design and formal development are incompatible?. In: [McDermid](https://www.interaction-design.org/references/authors/john_a__mcdermid.html),
 John A. (ed.). "The Theory and Practice of Refinement: Approaches to 
the Formal Development of Large-Scale Software Systems". 
Butterworth-Heinemannpp. 12-26

[Dix](https://www.interaction-design.org/references/authors/alan_j__dix.html), Alan J. and [Runciman](https://www.interaction-design.org/references/authors/colin_runciman.html), Colin (1985): Abstract Models of Interactive Systems. In: [Johnson](https://www.interaction-design.org/references/authors/peter_johnson.html), Peter and [Cook](https://www.interaction-design.org/references/authors/stephen_cook.html), Stephen (eds.) [Proceedings
 of the Conference of the British Computer Society Human Computer 
Interaction Specialist Group - People and Computers I](https://www.interaction-design.org/references/conferences/proceedings_of_the_conference_of_the_british_computer_society_human_computer_interaction_specialist_group_-_people_and_computers_i.html) August 17-20, 1985, University of East Anglia. pp. 13-22
[Dix](https://www.interaction-design.org/references/authors/alan_j__dix.html), Alan J., [Mancini](https://www.interaction-design.org/references/authors/roberta_mancini.html), Roberta and [Levialdi](https://www.interaction-design.org/references/authors/stefano_levialdi.html), Stefano (1997): The Cube - Extending Systems for Undo. In: [In Proc. of DSVIS97](https://www.interaction-design.org/references/conferences/in_proc__of_dsvis97.html) 1997.

[Dix](https://www.interaction-design.org/references/authors/alan_j__dix.html), Alan J., [Rodden](https://www.interaction-design.org/references/authors/tom_rodden.html), Tom, [Davies](https://www.interaction-design.org/references/authors/nigel_davies.html), Nigel, [Trevor](https://www.interaction-design.org/references/authors/jonathan_trevor.html), Jonathan, [Friday](https://www.interaction-design.org/references/authors/adrian_friday.html), Adrian and [Palfreyman](https://www.interaction-design.org/references/authors/kevin_palfreyman.html), Kevin (2000):*Exploiting Space and Location as a Design Framework for Interactive Mobile Systems*. In [ACM Transactions on Computer-Human Interaction](https://www.interaction-design.org/references/periodicals/acm_transactions_on_computer-human_interaction.html), 7 (3) pp. 285-321
[Dix](https://www.interaction-design.org/references/authors/alan_j__dix.html), Alan J., [Finlay](https://www.interaction-design.org/references/authors/janet_e__finlay.html), Janet E., [Abowd](https://www.interaction-design.org/references/authors/gregory_d__abowd.html), Gregory D. and [Beale](https://www.interaction-design.org/references/authors/russell_beale.html), Russell (2004): *Human-Computer Interaction (3rd Edition).* Prentice Hall

[Dix](https://www.interaction-design.org/references/authors/alan_j__dix.html), Alan J., [Sheridan](https://www.interaction-design.org/references/authors/jennifer_g__sheridan.html), Jennifer G., [Reeves](https://www.interaction-design.org/references/authors/stuart_reeves.html), Stuart, [Benford](https://www.interaction-design.org/references/authors/steve_benford.html), Steve and [O'Malley](https://www.interaction-design.org/references/authors/claire_o%27malley.html), Claire (2005): Formalising Performative Interaction. In: [Gilroy](https://www.interaction-design.org/references/authors/stephen_w__gilroy.html), Stephen W. and [Harrison](https://www.interaction-design.org/references/authors/michael_d__harrison.html), Michael D. (eds.) [DSV-IS 2005 - Interactive Systems, Design, Specification, and Verification, 12th International Workshop](https://www.interaction-design.org/references/conferences/dsv-is_2005_-_interactive_systems%2C_design%2C_specification%2C_and_verification%2C_12th_international_workshop.html) July 13-15, 2005, Newcastle upon Tyne, UK. pp. 15-25
[Ellis](https://www.interaction-design.org/references/authors/clarence_a__ellis.html), Clarence A. (1994): *Goal Based Workflow Systems*. In [International Journal of Collaborative Computing](https://www.interaction-design.org/references/periodicals/international_journal_of_collaborative_computing.html), 1 (1) pp. 61-86

[Eslambolchilar](https://www.interaction-design.org/references/authors/parisa_eslambolchilar.html), Parisa (2006). *Making Sense of Interaction Using a Model-Based Approach. PhD Thesis*. Hamilton Institute, National University of Ireland
[Eslambolchilar](https://www.interaction-design.org/references/authors/parisa_eslambolchilar.html), Parisa and [Murray-Smith](https://www.interaction-design.org/references/authors/roderick_murray-smith.html), Roderick (2010): *A Model-Based Approach to Analysis and Calibration of Sensor-Based Human Interaction Loops*. In [International Journal of Mobile Human Computer Interaction](https://www.interaction-design.org/references/periodicals/international_journal_of_mobile_human_computer_interaction.html), 2 (1) pp. 48-72
[Hillier](https://www.interaction-design.org/references/authors/bill_hillier.html), Bill (1999): *Space is the Machine: A Configurational Theory of Architecture.* Cambridge University Press[s](https://www.interaction-design.org/encyclopedia/formal_methods.html#copyrightNotice)

[Kostakos](https://www.interaction-design.org/references/authors/vassilis_kostakos.html), Vassilis, [O'Neill](https://www.interaction-design.org/references/authors/eamonn_o%27neill.html), Eamonn, [Penn](https://www.interaction-design.org/references/authors/alan_penn.html), Alan, [Roussos](https://www.interaction-design.org/references/authors/george_roussos.html), George and [Papadongonas](https://www.interaction-design.org/references/authors/dikaios_papadongonas.html), Dikaios (2010): *Brief encounters: Sensing, modeling and visualizing urban mobility and copresence networks*. In [ACM Transactions on Computer-Human Interaction](https://www.interaction-design.org/references/periodicals/acm_transactions_on_computer-human_interaction.html), 17 (1) p. 2
[Laird](https://www.interaction-design.org/references/authors/john_e__laird.html), John E. (2008): Extending the Soar Cognitive Architecture. In: [Proceedings of the 2008 conference on Artificial General Intelligence 2008 Proceedings of the First AGI Conference](https://www.interaction-design.org/references/conferences/proceedings_of_the_2008_conference_on_artificial_general_intelligence_2008_proceedings_of_the_first_agi_conference.html) 2008. pp. 224-235

[Larson](https://www.interaction-design.org/references/authors/kevin_larson.html), Kevin and [Czerwinski](https://www.interaction-design.org/references/authors/mary_czerwinski.html), Mary (1998): Web Page Design: Implications of Memory, Structure and Scent for Information Retrieval. In: [Karat](https://www.interaction-design.org/references/authors/clare-marie_karat.html), Clare-Marie, [Lund](https://www.interaction-design.org/references/authors/arnold_lund.html), Arnold, [Coutaz](https://www.interaction-design.org/references/authors/jo%EBlle_coutaz.html), Joëlle and [Karat](https://www.interaction-design.org/references/authors/john_karat.html), John (eds.) [Proceedings of the ACM CHI 98 Human Factors in Computing Systems Conference](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_98_human_factors_in_computing_systems_conference.html) April 18-23, 1998, Los Angeles, California. pp. 25-32

[Limbourg](https://www.interaction-design.org/references/authors/quentin_limbourg.html), Quentin, [Vanderdonckt](https://www.interaction-design.org/references/authors/jean_m__vanderdonckt.html), Jean M., [Michotte](https://www.interaction-design.org/references/authors/benjamin_michotte.html), Benjamin, [Bouillon](https://www.interaction-design.org/references/authors/laurent_bouillon.html), Laurent and [López-Jaquero](https://www.interaction-design.org/references/authors/v%EDctor_l%F3pez-jaquero.html), Víctor (2005): USIXML: A Language Supporting Multi-path Development of User Interfaces. In: [Bastide](https://www.interaction-design.org/references/authors/remi_bastide.html), Remi,[Palanque](https://www.interaction-design.org/references/authors/philippe_a__palanque.html), Philippe A. and [Roth](https://www.interaction-design.org/references/authors/j%F6rg_roth.html), Jörg (eds.) [Engineering Human Computer Interaction and Interactive Systems, Joint Working Conferences EHCI-DSVIS 2004](https://www.interaction-design.org/references/conferences/engineering_human_computer_interaction_and_interactive_systems%2C_joint_working_conferences_ehci-dsvis_2004.html) July 11-13, 2005, Hamburg, Germany. pp. 200-220

[Lin](https://www.interaction-design.org/references/authors/james_lin.html), James, [Newman](https://www.interaction-design.org/references/authors/mark_w__newman.html), Mark W., [Hong](https://www.interaction-design.org/references/authors/jason_i__hong.html), Jason I. and [Landay](https://www.interaction-design.org/references/authors/james_a__landay.html), James A. (2000): DENIM: Finding a Tighter Fit between Tools and Practice for Web Site Design. In: [Turner](https://www.interaction-design.org/references/authors/thea_turner.html), Thea, [Szwillus](https://www.interaction-design.org/references/authors/gerd_szwillus.html), Gerd, [Czerwinski](https://www.interaction-design.org/references/authors/mary_czerwinski.html), Mary, [Peterno](https://www.interaction-design.org/references/authors/fabio_peterno.html), Fabio and [Pemberton](https://www.interaction-design.org/references/authors/steven_pemberton.html), Steven (eds.) [Proceedings of the ACM CHI 2000 Human Factors in Computing Systems Conference](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_2000_human_factors_in_computing_systems_conference.html) April 1-6, 2000, The Hague, The Netherlands. pp. 510-517
[Lynch](https://www.interaction-design.org/references/authors/kevin_lynch.html), Kevin (1960): *The Image of the City (Harvard-MIT Joint Center for Urban Studies Series).* The MIT Press[s](https://www.interaction-design.org/encyclopedia/formal_methods.html#copyrightNotice)

[Miller](https://www.interaction-design.org/references/authors/george_a__miller.html), George A. (1956): *The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information*. In [Psychological Review](https://www.interaction-design.org/references/periodicals/psychological_review.html), 63 pp. 81-97
[Navarre](https://www.interaction-design.org/references/authors/david_navarre.html), David, [Palanque](https://www.interaction-design.org/references/authors/philippe_a__palanque.html), Philippe A., [Paterno](https://www.interaction-design.org/references/authors/fabio_paterno.html), Fabio, [Santoro](https://www.interaction-design.org/references/authors/carmen_santoro.html), Carmen and [Bastide](https://www.interaction-design.org/references/authors/remi_bastide.html), Remi (2001): A Tool Suite for Integrating Task and System Models through [Scenarios](https://www.interaction-design.org/literature/topics/user-scenarios). In: [Johnson](https://www.interaction-design.org/references/authors/chris_johnson.html), Chris (ed.) [DSV-IS 2001 - Interactive Systems Design, Specification, and Verification, 8th International Workshop](https://www.interaction-design.org/references/conferences/dsv-is_2001_-_interactive_systems_design%2C_specification%2C_and_verification%2C_8th_international_workshop.html) June 13-15, 2001, Glasgow, Scotland, UK. pp. 88-113

[Nielsen](https://www.interaction-design.org/references/authors/jakob_nielsen.html), Jakob and [Landauer](https://www.interaction-design.org/references/authors/thomas_k__landauer.html), Thomas K. (1993): A Mathematical Model of the Finding of Usability Problems. In:[Ashlund](https://www.interaction-design.org/references/authors/stacey_ashlund.html), Stacey, [Mullet](https://www.interaction-design.org/references/authors/kevin_mullet.html), Kevin, [Henderson](https://www.interaction-design.org/references/authors/austin_henderson.html), Austin, [Hollnagel](https://www.interaction-design.org/references/authors/erik_hollnagel.html), Erik and [White](https://www.interaction-design.org/references/authors/ted_white.html), Ted (eds.) [Proceedings of the ACM CHI 93 Human Factors in Computing Systems Conference](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_93_human_factors_in_computing_systems_conference.html) April 24-29, 1993, Amsterdam, The Netherlands. pp. 206-213
[Paterno](https://www.interaction-design.org/references/authors/fabio_paterno.html), Fabio (1999): *Model-Based Design and Evaluation of Interactive Applications (Applied Computing).*Springer
[Pfaff](https://www.interaction-design.org/references/authors/g%FCnther_e__pfaff.html), Günther E. (ed.) (1985): *User Interface Management Systems (Eurographic Seminars).* Springer

[Pirolli](https://www.interaction-design.org/references/authors/peter_pirolli.html), Peter (2007): *Information Foraging Theory: Adaptive Interaction with Information (Series in Human-Technology Interaction).* Oxford University Press, USA
[Prinz](https://www.interaction-design.org/references/authors/wolfgang_prinz.html), Wolfgang, [Pankoke-Babatz](https://www.interaction-design.org/references/authors/uta_pankoke-babatz.html), Uta, [Gräther](https://www.interaction-design.org/references/authors/wolfgang_gr%E4ther.html), Wolfgang, [Gross](https://www.interaction-design.org/references/authors/tom_gross.html), Tom, [Kolvenbach](https://www.interaction-design.org/references/authors/sabine_kolvenbach.html), Sabine and [Schäfer](https://www.interaction-design.org/references/authors/leonie_sch%E4fer.html), Leonie (2004): Presenting Activity Information in an Inhabited Information Space. In: [Snowdon](https://www.interaction-design.org/references/authors/david_n__snowdon.html), David N., [Churchill](https://www.interaction-design.org/references/authors/elizabeth_f__churchill.html), Elizabeth F. and [Frécon](https://www.interaction-design.org/references/authors/emmanuel_fr%E9con.html), Emmanuel (eds.). "Inhabited Information Spaces: Living with your Data ([Computer Supported Cooperative Work](https://www.interaction-design.org/literature/topics/computer-supported-cooperative-work))". Springer

[Reisner](https://www.interaction-design.org/references/authors/phyllis_reisner.html), Phyllis (1981): *Formal Grammar and Human Factors Design of an Interactive Graphics System*. In [IEEE Trans. Software Eng.](https://www.interaction-design.org/references/periodicals/ieee_trans__software_eng-dot-.html), 7 (2) pp. 229-240
[Thimbleby](https://www.interaction-design.org/references/authors/harold_thimbleby.html), Harold and [Cairns](https://www.interaction-design.org/references/authors/paul_cairns.html), Paul (2010): *Reducing number entry errors: solving a widespread, serious problem*. In [Journal of The Royal Society Interface](https://www.interaction-design.org/references/periodicals/journal_of_the_royal_society_interface.html), 7 (51) pp. 1429-1439
Université catholique de Louvain (2011). *UsiXML - Home of the USer Interface eXtensible Markup Language*. Retrieved 29 March 2011 from Université catholique de Louvain: [http://www.usixml.org/](http://www.usixml.org/)
**Chapter TOC**
[**User Experience: The Beginner’s Guide**](https://www.interaction-design.org/courses/user-experience-the-beginner-s-guide)
![](https://public-media.interaction-design.org/images/courses/hds/course_50--square_thumbnail.jpg?tr=fo-auto)
User Experience: The Beginner’s Guide
Closes in
15
days
booked
View Course

## 获取每周用户体验洞察 (UX Insights)

加入 **314,322 位设计师**的行列，通过我们的邮件订阅 (Newsletter) 获取实用的用户体验技巧 (UX tips)。
请提供有效的电子邮件地址。

## 本书章节涉及的主题：

[形式化方法 (Formal Methods)](https://www.interaction-design.org/literature/topics/formal-methods)
[人机交互 (Human-Computer Interaction, HCI)](https://www.interaction-design.org/literature/topics/human-computer-interaction)
[用户体验设计 (User Experience (UX) Design)](https://www.interaction-design.org/literature/topics/ux-design)
