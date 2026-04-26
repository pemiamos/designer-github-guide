# 26. 美学计算 (Aesthetic Computing)

**来源**：The Encyclopedia of Human-Computer Interaction, 2nd Ed.
**Notion 原页面**：https://www.notion.so/5262b51c208b4516a41904c9a39f035e

---

[Paul A. Fishwick](https://www.interaction-design.org/literature/author/paul-a-fishwick)

“美学计算（Aesthetic Computing）”这个词如果从字面上理解，是将[美学（aesthetics）](https://www.interaction-design.org/literature/topics/aesthetics)这一哲学领域应用于计算领域，该领域的工作也大致如此定义；然而，在我对我研究实验室和教学工作的操作性定义中，美学计算被视为*具身形式语言（embodied formal language）*。美学计算的目的是以美学产品为媒介，传递形式语言（formal languages）的知识与实践。美学计算基于日益增多的关于身体在学习中（特别是数学学习中）作用的文献。这一基础随后被应用于计算领域，因为计算领域的形式语言元素是数学的延伸。这一新领域提出了两个问题：

- Q1：*具身认知（embodied cognition）如何置于形式语言之中？*
- Q2：*具身认知如何产生用于形式语言的新型计算机界面（computer interfaces）？*

Q1 引出了一系列围绕理论、哲学和分析的子问题。提出这个问题引发了关于[动机（motivation）](https://www.interaction-design.org/literature/topics/motivation)的讨论：

1) 我为什么对这个话题感兴趣？ 2) 审美计算（Aesthetic Computing）领域是如何构建在具身认知（Embodied Cognition）和哲学基础之上的？ 3) 谁在这个领域开展过工作（例如相关文献）？然而，仅有第一个问题是不够的。分析并发展理论是一回事，但问自己“如何将这一理论转化为实践”则是另一回事。这正是第二个问题的核心所在。为了将数学和计算的具身认知提升到新的高度，我们应该*做些什么、实践什么*以及*创造什么*？我们需要构建新一代的人机界面（Human-Computer Interfaces），这些界面应受具身原则（Embodied Principles）的启发，并将这些原则作为与形式语言（Formal Languages）交互的设计元素。一个潜在且至关重要的第三个问题，将围绕通过评估和基于科学的研究方法，来探讨此类计算机界面对学习的影响。这代表了审美计算需要研究的一个领域；然而，迄今为止的大部分工作都集中在理论构建和新型界面的工程实现上。

> 审美计算假设（The Aesthetic Computing Hypothesis）认为，鉴于认知的具身特性，我们应当通过新型的人机界面来实现这种具身性，以用于学习形式语言。

## 26.1 审美计算领域的背景

为了给审美计算（Aesthetic Computing）领域提供背景，我提出两个问题：1）为什么“审美计算”被视为“具身形式语言（Embodied Formal Languages）”？2）什么是“具身形式语言”？对于第一个问题，我们必须重新审视“审美（aesthetics）”一词的根源。审美的原始希腊语定义 *αἰσθητικός* (*aisthetikos*) 源自另一个希腊词 aisthanomai，意为“我感知、感受、觉察”。因此，审美的核心在于身体，以及身体在形成概念和知识过程中的交互：即作为具身化（embodiment）的审美。尽管在广度和深度上，审美是一项远比这一层面更丰富的事业 (Kelly 1998)，但我们依然坚持一种基于身体的审美观，尽管 Diffey (1995) 指出，“aesthetic”一词除了在“anaesthetic”（麻醉）这个词中外，在很大程度上已经失去了其感知层面的含义，而保留了“美”和“艺术”的含义。至于为什么使用“形式语言（Formal Languages）”来表征“计算（Computing）”，我们注意到，自动机理论（theory of automata）和计算理论的大部分内容都处于语言学领域——尽管它是通用语言学的一个子集，需要形式上定义明确的规范和处理方式。

现在让我们考虑具身化和形式语言的定义。具身化意味着[感知](https://www.interaction-design.org/literature/topics/perception)/行动

当身体与环境交互时，便会产生反馈循环（feedback loop）。因此，显而易见的是，任何具身化方法（embodied approach）都将涉及感觉运动功能（sensorimotor functions）——例如使用鼠标、键盘、多点触控显示器，以及佩戴头戴式显示器（head-mounted display）或使用触觉反馈设备（tactile feedback device）。人机交互（Human-Computer Interaction, HCI）领域充满了利用此类技术的各种方法。然而，具身性（embodiment）是一个比感官刺激（sensory stimuli）和物理操作（physical manipulation）深得多的概念。在使用某些先进技术（如多用户虚拟环境）时，我们会产生一种存在感（sense of presence）（即实现包括社会存在感在内的不同类型的存在感）。在阅读书籍时，我们同样会产生存在感，因为书籍将我们的“心灵之身（mind's body）”置于叙事之中（参考 Beck et al. 2011 中的“叙事心理学（narrative psychology）”）。因此，具身性既可以通过用于启用感官的硬件进行客观测量，也可以通过对人类受试者使用存在感测量工具（presence instrument）进行主观测量。具身性不应被视为对抽象（abstraction）的否定，而应被视为其补充（Devlin 2006）。

形式语言（Formal languages）定义了一类人工语言，例如编程语言。这些语言源于形式文法（formal grammars），而形式文法可以基于文本、形状或图表。FORTRAN、Java 和 Perl 是形式语言的例子，可扩展标记语言（XML）、统一建模语言（UML）以及数据结构（data structures）同样如此。

摩尔斯电码（Morse code），以及用于仿真的动态模型结构（dynamic model structures）（Fishwick 1995, Fishwick 2007b）。形式语言（Formal languages）通常使用诸如巴科斯-诺尔形式（Backus-Naur Form, BNF）之类的文法（grammars）来定义，且不一定必须基于文本。例如，可以存在形式化的视听语言（audiovisual languages）以及图文法（graph grammars）。所有形式语言结构都可以通过抽象层级（levels of abstraction）进行层级化定义（例如，由 3 个有限状态机（finite state machine）层级管理一组底层的常微分方程（ordinary differential equations），而这些方程随后被翻译成 Java 编程语言，并进一步转换为字节码（byte code））。因此，语言通常是在长长的规范（specification）和转换（translation）链条中定义的。每种语言都有其目标功能、文化和追随者。Ghezzi and Jazayeri (1997) 提供了关于编程语言规范的一般性概念。

## 26.2 个人经验与影响

### 26.2.1 艺术（Art）

具身认知（Embodied Cognition）的概念很容易被视为理所当然，因为它看起来如此自然——即身体在认知中起着核心作用。然而，坚持具身观往往会改变你观察客体时的世界观。作为一名业余艺术家，我收集了许多历史上著名艺术家的海报和版画。在中学时期，我深受 Thomas Gainsborough 作品的影响，尤其是图 1。

![](https://public-media.interaction-design.org/images/encyclopedia/aesthetic_computing/Oil_on_canvas_thomas_gainsborougs_andrews.jpg)
版权条款与许可：pd（公有领域（Public Domain），指共有财产且不含原始作者权的资料）。
**图 26.1**：*Mr. and Mrs. Andrews*，布面油画，Thomas Gainsborough，1750 年。英国伦敦 National Gallery。

我想象着将自己作为一个化身（Avatar），我可以进入画作，漫步在麦田之中，观察那些树木，并与 Mr. and Mrs. Andrews 进行社交对话。这引发了一系列“在世界中”（in world）的想象对话与观察。这里的关键点在于将这部作品的“阅读”*视为一种具身经验（Embodied Experience）的形式*。对我而言，Gainsborough 的这幅画并非一个遥远的研究对象，而是一个[虚拟现实（Virtual Reality）](https://www.interaction-design.org/literature/topics/virtual-reality) 的例子，一台时光机——一种让我能够让自己沉浸在其中的幻象。

18 世纪的英国世界。这种方法是 Dewey 的“艺术即经验（*art as experience*）”(Dewey 1934) 的一个实例，并与 Grau (Grau 2004) 关于艺术家是首批虚拟现实（Virtual Reality）创造者的论点相关。该方法强调，当我们面对一个对象时，可以通过身体模拟（Bodily Simulation）动态地对其进行解读，而这种模拟涵盖了身体所能提供的所有基于感知和运动的动作（perceptual and motor-based actions），即身体的可供性（Affordance）。这种思考和行动方式可以应用于所有对象和媒介，包括数学和计算。

### 26.2.2 数学（Mathematics）

在小学期间，就像世界上无数其他学生一样，我学习了算术（Arithmetic）的基础知识——其方法和定律，并通过大量的例子，通过死记硬背（Rote memorization）和高强度练习来掌握。学习数学在很大程度上是基于行动的（Action-based），但这种“行动”仅限于在长时间内解决大量重复的问题。在掌握了算术的基础元素之后，接着学习的是代数（Algebra）。让我们来看一个包含算术且带有少量代数元素的数学表达式（Mathematical expression）：

> X = 2 * (3 + 4)

我们都接触过这类数学对象，因为它们对于受过教育的公众来说至关重要。学习这个等式的所有组成部分并非易事——学习者必须理解变量（Variable）的概念、乘法和加法运算，以及随后出现的括号限定组（Parenthetically-delimited group）的概念。运算顺序（Order of operations）也至关重要，正如该分组所暗示的那样。例如，我可以将 3 与 4 相加，然后乘以 2 得到 14，随后将其设定为与 X 等价（Equivalence）。

某些算术定律在转换此类表达式时非常有用。分配律（Law of Distribution）规定 $x(y + z) = xy + xz$，其中 $x, y, z$ 为数字，且乘法是隐式的（Implicit），而不是像上述等式那样使用 `*` 来显式地（Explicitly）定义。老师会定义分配律，并给我们提供许多有用的例子，以此来强化我们对……的理解。

定律及其在符号操纵（symbolic manipulation）中的应用方式。这种等价模式驱动了一种静态的模式匹配（pattern-matching）[类型](https://www.interaction-design.org/literature/topics/type)的数学研究方法。

然而，在随后的课程中，我发现创建一种将数字和符号视为物理对象的虚拟解题方法会更加方便。在数学教育中，这种过程被称为具体化（reification, Sfard 1994），并与建构主义（constructivism, Piaget 1950）和构造主义（constructionism, Papert 1980）相关，即学生通过思想与生活经验的结合来构建自己的知识。我通过类比（analogy）和隐喻（metaphor）来呈现分配律（distributive law），从而对上述表达式进行虚拟操纵（virtual manipulation）：

> 抓住“2”这个对象，当它与“*”运算符并列时，会产生一种生物力学状态（biomechanical state），使得“2”被向内推向由括号“(...)”定义的组对象（group object）。“2”被逐渐推进，当它到达由“(”表示的空间边界（spatial boundary）边缘时，它穿过边界到达另一侧，并以生物方式分裂成两个克隆体，分别附着在“3”和“4”上。这种克隆活动产生了表达式 (2 * 3 + 2 * 4)。子表达式 2 * 3 和 2 * 4 通过进一步的身体活动（bodily activity）进行求值。例如，将 2 和 3 推入 * 中，会导致乘法运算。类似的反应也发生在

按照习得的运算顺序（order of operations），最后执行加法（+）运算。然后将结果手动放入一个印有 X 的方框中。

因此，对我而言，数学变得像是一项全身运动，而不再是仅需要一组静态的、基于文本的规则和模式的简单运算。虚拟操作（virtual manipulations）可能涉及其他具身活动（embodied activities），例如我可能会将某个对象“抛过”一道界定括号表达式的墙。虽然这是一个个人经验，但绝非特例。正如 Sfard 在与 Thompson 的对话（Thompson and Sfard 1994）中所观察到的，她注意到了产生类似心理表象（mental imagery）的倾向：“我与数学家的合作提供了更多证据，证明数学化（mathematizing）的人的内心世界确实看起来非常像一个物质世界，其中充满了等待被组合、分解、移动和抛掷的对象。”

Arzarello (2004) 解释了自然数学呈现（natural mathematical presentations）与形式数学呈现（formal mathematical presentations）之间的区别，并揭示了在采用自然主义解释和阐释以补充形式化表达、或作为通往形式化表达之路径时，手势（gesture）的重要性。前文所述的具身描述可被称作“自然的”。Goldin and Kaput (1996) 概述了媒介对数学表征（mathematical representation）的影响，他们指出：“……物理媒介的变化使得外部表征（external representations）能够成为动作表征（action representations）而非展示表征（display representations），这赋予了这些表征一个特性……”

“强大的内部表征（Internal Representations）。” Hadamard (1996) 研究了数学思维，其结果与类似的认知处理过程相呼应。对我而言，这种关于数学符号的基于动作的叙事（Action-based narrative）并不局限于分配律（Distributive law）。例如，在某个表达式中，当数字穿过等号时，会发生一些有趣的事情。存在一条虚拟线或平面，它与 $\text{ }$ 垂直相交。当像 $\text{ }$ 这样的数字被拖过这个垂直平面时，该数字在另一侧会产生镜像效果（Mirror-like effect），从而导致其符号反转，结果变为 $\text{ }$。交换律（Commutativity）和结合律（Associativity）也具有类似的伪物理的、物质性的行为，可用于理解和处理算术表达式。

我早期关于符号操作具身感（Embodied sense）的体验问题在于，没有任何书籍（或教师）以这种方式解释数学，因此我以及可能很多其他人，不得不将这些有些奇特的“电影般片段（Cinematic episodes）”深藏在心中。这种思维方式是否普遍，需要更多的科学研究以及对数学本质的反思。在 University of Florida，我们开发了一个基于 Web 的交互工具，允许任何人以这种方式操作表达式。我们此前还探索过类似的具身表征（Embodied representations），其中涉及虚拟环境中的存在感（Sense of presence）(Fishwick and Park 2008a)。

我讲述这段经历的目的是为了强调……的重要性

……身体在理解数学等形式语言（formal languages）中的作用。

Lakoff and Nunez (2001) 提出了一部具有里程碑意义的数学隐喻（mathematical metaphors）汇编，该研究建立在具身认知（embodied cognition）哲学（Johnson 1987, Varela et al. 1991, Barsalou 2010）的基础之上。特别是 Johnson 的意象图式（image schemata），如包含（containment）、吸引（attraction）和平衡（equilibrium），是我算术体验中不可或缺的一部分。关于具身思维（embodied thinking）的文献将思维和知识的核心置于身体之上，这不仅受到了概念隐喻（conceptual metaphor）（Lakoff and Johnson 1999, Lakoff and Johnson 2003）等领域的影响，还受到了随后针对大脑的实证研究（empirical studies）（Feldman and Narayanan 2004, Feldman 2006）的启发。更广泛地说，基于语言的叙事（language-based narratives）似乎包含一个具身基础（embodied basis）（Speer et al. 2007, Mar and Oatley 2008），从而将自然语言定义为一种模拟（simulation）。阅读关于抓取或奔跑的故事可能会导致对这些事件和活动的认知模拟（cognitive simulation），就好像读者在身体上参与了这些活动一样。回溯到地点法（Method of Loci）（Yates 1966）盛行的时期，我们可以发现，记忆一组事实的行为被转化为一个丰富的具身过程，而非被简单地视为关联检索（associative retrieval）。情境学习与认知（situated learning and cognition）（Brown et al. 1989, Lave and Wenger 1991）领域在目标和方法上与具身方法（embodied approach）高度契合，即：在做中学（learning by doing）。

在结束关于具身数学（embodied mathematics）的讨论时，我们应当注意到

“动作”（action）、“交互”（interaction）和“过程”（process）这些概念可以被纳入包含函数复合（functional composition）、动力学（dynamics）和程序（procedure）等显式方面的标准数学符号体系中（即具身思维类型 [embodied-types of thought]）。例如，几何与形状的美学可以通过生成式方式（generatively）构建（Leyton 2001, Leyton 2006），并利用 Blum 基于波传播的中轴（wave propagation-based medial axis）进行动态构建（Leymarie 2006）。我们还可以利用数学来创建数学隐喻（mathematical metaphors）的形式化表示（formal representation）（Guhe et al. 2009），从而形成一个闭环：将隐喻建立在数学表达式之上，而隐喻本身又是被形式化定义的。

具身方法（embodied approach）对数学，以及延伸至应用数学和计算科学具有深远影响，因为计算科学是数学的直接产物，且前文所述的公式在软件“表达式”（expressions）中十分常见。如果我们的思维是具身的，那么：

- 我们应当研究数学和计算科学中所使用的各种隐喻，及其起源和文化关联。
- 我们应当通过创建能够强化并增强这种体验的新型人机界面（human-computer interfaces），来利用语言中隐喻性且具身的基质（substrate）。
- 我们应当引入其他将“身体”视为天然组成部分的学科，例如艺术与人文科学（Slingerland 2008），从而形成跨越学术界的全新跨学科协作。

### 26.2.3 编程（Programming）

具身方法（Embodied approach）已从数学领域扩展到编程和数据结构（Data structures）的学习中。尤其是编程，众所周知其充满了隐喻（Metaphor）。循环（Loops）正是如此：它们是循环行为的模式——即小对象在执行其他任务时沿着闭合路径移动。顺序行为（Sequential behavior）有时被视为沿着空间路径的移动，而函数（Functions）则被视为接收产品输入并产生输出的机器。Papert (1980) 在解释 LOGO 语言时，通过一个他称之为“同调性（Syntonicity）”的术语强调了具身性的重要性，他指出：“我们强调了这样一个事实，即使用‘海龟’作为角度概念的隐喻载体，将其与身体几何（Body geometry）紧密地联系在一起。” Petre and Blackwell (1999) 对程序员进行了研究，结果表明，隐喻推理（Metaphorical reasoning）涉及对象、运动以及一般的具身交互（Embodied interaction）。此类隐喻不仅存在于所有编程语言中，也存在于计算理论（Theory of computation）的基础之中。例如，图灵机（Turing machine）就是一个极佳的例子：这是 Alan Turing 在 20 世纪 30 年代构思的一台机器，由磁带读写头（Read/write head）和一条无限长的磁带组成。这一隐喻可能是由于当时磁带被广泛使用。在上个世纪，Charles Babbage 在他的计算引擎（Computing engine）中使用了“磨坊（Mill）”的概念。有趣的是，在这些历史概念所在的庞大计算历史中...

正如 Ifrah (2002) 所讨论的，大多数编程与计算在定义和实现层面均具有模拟性（Analog）和具身性（Embodied）。直到近期，从模拟到数字的演进在加速计算速度、推动计算机革命的同时，也使我们与计算之间的关系呈现出一种去具身化（Disembodied）的趋势。

### 26.2.4 媒介（Media）

媒介理论家为理解媒介的演进提供了多种方法。McLuhan (1964) 不仅重视通过调制媒介（modulated medium）所创建的信息，更重视影响信息的媒介本身。McLuhan 以灯泡为例，称其为一种“没有信息的媒介（medium without a message）”。然而，灯泡可以承载二进制数字（binary digit），在多路开关灯泡的情况下可能承载更多信息，其方式与通过信号灯操作的摩尔斯电码（Morse code）并无二致。Bolter and Grusin (2000) 提出了一种媒介形式逐渐演变的理论，这种演变通常由技术驱动，促使我们探讨即时性（immediacy，即透过媒介看到目标所指 [target signified]）与超媒介性（hypermediacy，即意识到并反思媒介本身）的问题。新媒介研究（New media studies）特别强调物质性（materiality）、媒介以及具身性（embodiment）。Manovich (2002, p. 317) 在将“循环（loop）视为叙事引擎”时——此处循环被定义为一种允许基于索引的[迭代](https://www.interaction-design.org/literature/topics/design-iteration)（iteration）的通用编程结构——提出了这样一个问题：“循环能否成为一种适用于计算机时代的新叙事形式？”

大众媒介在很大程度上塑造了我关于审美计算（aesthetic computing）的思考过程。例如，1982年首映的 *Tron* (Kallay 2011) 值得关注，因为它基于一个极具创新性的剧本，其中包含了一段庞大的软件，即一个

“操作系统（Operating System）”，且这种系统是可以被直接体验到的。程序被具象化为实体（Bodies），而操作系统则由一个类似城市的空间组成，其中有灯光闪烁、穿梭的车辆以及相互交互的程序。在科幻/奇幻类型中，*Tron* 在这方面相当独特。其他更近期的电影作品虽然令人印象深刻且引人入胜，但往往忽略了“程序”本身。例如，在 *Star Trek: The Next Generation* 中，我们接触到了全息甲板（Holodeck），人们可以在其中体验具有全感官模拟（Full Sensory Simulation）的极致虚拟现实（Virtual Reality）。用户会停在全息甲板之外，说“计算机，加载全息甲板程序 A-3”或类似的指令，随后全息甲板加载该程序，用户便进入其中。然而，我们从未真正体验到程序本身——而仅仅是它的输入和输出。同样，在 *The Matrix* 中，我们拥有关于人类角色的丰富具身经验（Embodied Experience），而这些角色在现实中其实是被存储在充满液体的舱体网络之中。

尽管我们熟悉且习惯于基于文本的过程描述，但令人惊叹且讽刺的是，像 *The Matrix* 这样一个提供实时合成交互（Synthetic Interactions）和拟像（Simulacra）的超真实环境（Hyper-real Environment），竟然必须通过那些奇怪的绿色雨滴流来编程，而这些代码对任何人来说都晦涩难懂，大概只有那些精通这种楔形文字（Cuneiform Script）后现代后裔的操纵员才能理解。这种符号学状态（Semiotic Condition）呈现出一种鲜明的对比：在实践中

一方面是程序所产生的无限全感官模拟（full-sensory simulation），而另一方面则是定义程序本身的、所谓的打字机符号。这就像是有人给了你一架高机动的高超音速喷气式飞机（hypersonic jet plane）去驾驶，但前提条件是你必须通过敲击一个单一按键来产生摩尔斯电码（Morse code）的点和划来操纵飞机。人们或许会期待，构建程序和数据的能力能够利用 Matrix 所提供的几乎无限的人机界面（human-computer interface）。Rotman (2000, p. 67) 提出了引发这一担忧的问题：“如果语言不再局限于纸张和黑板上的书写（inscriptions），而是变成了在计算机屏幕上创建像素排列（pixel arrangements），会怎样？”

## 26.3 审美计算（Aesthetic Computing）：将计算机“由内而外”地翻转

在过去的半个世纪里，计算机的体积显著缩小，数量大幅增加。我们经常在新闻中看到，体积越来越小、厚度越来越薄的计算机和软件在我们的文化中已变得无处不在（Ubiquitous），以至于我们在日常生活中随身携带或穿着它们。体积的减小和数量的增加，使得计算（Computing）影响到了大多数消费产品。例如，数字视频录像机（Digital Video Recorder, DVR）实现了电影和电视节目的时间与空间转移（Time and Place Shifting）。同样有趣的是，探讨计算如何影响我们以及我们的思维方式。Turkle (2004) 解释了这一心理现象，并以“我们现在都是计算机人（computer people）”这句话作为结尾。

Turkle 的观点对计算领域具有深远的影响。我想在此基础上进一步提出：随着我们使用这些设备，我们的思维在文化层面的改变，将计算中深层的抽象概念呈现给了我们：从数字（Number），到信息结构（Information Structure），再到过程（Process）。数字手表和数字视频录像机（DVRs）就是很好的例子。大多数数字手表都是多功能的。这些手表具备计时、设置秒表或闹钟唤醒等功能。要使用这款手表，你必须学习如何通过重复按下模式按钮（Mode Button）来导航菜单。在每种模式中，都有进一步细化该模式交互的子功能。这种模式按钮的体验...

按压直接映射到计算领域中一个基础的理论结构，称为*有限状态机（finite state machine）* (Hopcroft et al. 2000)。有限状态机不仅被嵌入在手表的硅片（silicon）中，而且佩戴手表的人通过使用手表的经验，意识到了这个虚拟机器（virtual machine）的结构及其组成部分。状态机*改变了佩戴者的思考方式*，尽管佩戴者可能并不了解状态机的正式数学表示法（formal mathematical notation）。手表的软件内部机制（software internals）由此嵌入到了我们的心理和文化之中。类似的过程也发生在大多数其他家用电器中，例如数字视频录像机（DVR）；然而，DVR 中的状态机比手表中的更为复杂——为了理解如何操作层级菜单（hierarchical menus），人们必须充分意识到一种新型的思维方式 (Negroponte 1996)。计算对思维的影响（例如，新千禧一代/数字原住民（digital native）的学习风格）在学习的语境下也得到了探讨 (Dieterle et al. 2007)。

与计算人工制品（computing artifacts）的交互经验是一种信息表示（information representation）形式，其中“表示”的定义被扩展为一种交互形式，而非一种以符号形式存在的静态对象。如果计算的原始元素——信息、数据和软件——正在改变我们的思考方式并进入我们的流行文化，那么自然可以推论，这些原始元素的美学（aesthetics）

[美学] 可以且应当在计算中发挥核心作用。美学（Aesthetics）已从具身（embodied）、感官的定义，演变为 Kelly (1998) 所提出的一个更全面的定义，即“对艺术、文化和自然的批判性反思（critical reflection）”。计算领域中的美学为计算人工制品（computing artifacts）——例如形式语言（formal languages）——带来了新的交互模态（interaction modalities）。鉴于人机连接方式的日益多样化，创造性表征（creative representation）拥有诸多机遇。我们使用 *美学计算（aesthetic computing）* 这一术语来对这些新方式进行分类和研究。

## 26.4 为什么需要审美计算（Aesthetic Computing）？

审美计算的表示目标（Representation targets）包括数据（data）、信息（information）、软件（software）和代码（code）等术语。由于语义上的重叠，我在使用这些术语时在某种程度上是可以互换的。数据可以是原子的（atomic），也可以是以结构的形式存在。代码通常是指软件，而软件既包含数据也包含过程（process）。信息论（Information theory）告诉我们，所有这些都是信息的一种形式，因为信息可以被解码为原子的、结构性的或程序性的（procedural）。在提及审美计算中的“计算”部分时，我更倾向于使用代码、软件或信息等术语，因为这些术语涵盖了更广泛的可表示项目类别，而通常意义上的“数据”一词往往指的是非程序性的信息形式。

支持审美计算的论点涉及那些已经发生改变的计算新兴领域：
- 我们彼此之间以及与自然的关系。这些方面包括普适计算（ubiquitous computing, Greenfield 2006, Gershenfeld et al. 2004）和泛在计算（pervasive computing）、界面的定制化（customization）与个性化（personalization），以及通过计算介导的人-自然交互（human-nature interaction）的新模态（modalities）（例如，跨越物理空间的虚拟现实连续体 [virtual reality continuum]...）

虚拟以及 [增强现实（Augmented Reality）](https://www.interaction-design.org/literature/topics/augmented-reality))。用于 [信息可视化（Information Visualization）](https://www.interaction-design.org/literature/topics/information-visualization) (Viegas et al. 2007) 和代码共享 (Reas and Fry 2007) 的共享且定制化的界面，在“再创作文化（Remix Culture）” (Lessig 2008) 的辅助下，构建了一个网络化的、定制化的 (Pine 1999) 表征空间（Representational Space）。

- 我们的思维模式，使得信息和软件等计算人工制品（Computing Artifacts）能够渗透到我们的体验之中。Salomon (1990) 认为计算正在改变思维，从而在人机交互中产生了 *认知残留（Cognitive Residues）*。这些研究与 Turkle (2005) 的观点一致。

- 计算在 [人机交互（Human-Computer Interaction, HCI）](https://www.interaction-design.org/literature/topics/human-computer-interaction) 中体验的重要性。Cockton (2011) 和 Hassenzahl (2011) 描述了 HCI 从单纯追求效率向追求体验的转变，而 Löwgren (2011) 则强调了交互（Interaction）的重要性——这是体验的核心维度。对体验的强调在概念上与作为认知基础的具身性（Embodiment） (Lakoff and Nunez 2001, Johnson 2007) 相关。Tractinsky et al. (2000) 和 Norman (2004) 讨论了美学（Aesthetics）在 HCI 中的相关性。Dourish (2001) 通过 [现象学（Phenomenology）](https://www.interaction-design.org/literature/topics/phenomenology) 的起点，为 HCI 中的具身性奠定了哲学基础。

- 作为计算机科学家，我们需要更频繁地与艺术家和设计师进行交流，因为他们代表了审美探究（aesthetic inquiry）的创造性组成部分；因此，针对日益普及的计算人工制品（computing artifacts）的基于经验的表征（experience-based representations），需要借助艺术家与科学家的协作（artist-scientist collaborations）来开展研究 (Buxton 1988, Malina 2011)。

## 26.5 审美计算领域的历史

自 2000 年以来，我一直在教授一门关于审美计算（Aesthetic Computing）的课程，关于最近一次课程的信息可见于 (Fishwick 2012)。关于该概念的一篇初步论文已发表 (Fishwick 2002)。2002 年夏天，我与 Roger Malina 和 Christa Sommerer 在德国共同组织了一场关于审美计算的 Dagstuhl 研讨会 (Fishwick and Bertelsen 2002; Dagstuhl 2011)。此次交流产生了多篇出版物 (Fishwick et al. 2005, Fishwick 2006, Fishwick, 2007a, Fishwick 2008b)。Kelly et al. (2009) 代表了该领域最近发表的研讨会成果。

“审美（aesthetics）”和“程序（programs）”这两个词出现在多种语境中，包括 Mohr (2011) 和 Nake (2009) 的研究，他们是较早探索通过将计算机程序作为艺术表达手段来实现交互审美（aesthetics of interaction）的研究者。Knuth (1992) 开发了文学编程（Literate Programming），并强调了编程中审美的重要性。Knuth 对审美的兴趣不仅限于纯粹的认知（cognitive）层面，还包括程序的[排版（typography）](https://www.interaction-design.org/literature/topics/typography)和布局设计的艺术形式。对于 Knuth 而言，计算似乎是一种具身经验（Embodied Experience）。

审美计算的独特之处在于，它旨在将审美应用于计算，而非反向操作：即使用

利用计算来创造艺术产品。因此，审美计算（Aesthetic Computing）的实例捕捉到了一种“回力镖效应”（boomerang effect），即计算机图形学（computer graphics）、普适计算（ubiquitous computing）和混合现实界面（mixed reality interfaces）的元素，可被用于交互式地表征构成这些技术的基础——即信息与软件。

在学术课程方面，University of Florida 在过去十年中通过两门通常合并授课的课程教授审美计算：CAP 4403（本科）和 CAP 6402（研究生）。这两门合并课程最初是数字艺术与科学（Digital Arts & Sciences, DAS）项目（Fishwick 2012）的一部分，该项目旨在将计算与艺术联系起来。自 2000 年以来，该课程经历了几个阶段：

- （2000-2005）软件制品（software artifacts）的表征替代方案（Representational alternatives）——从数字和表达式，到数据结构和程序。其中包含一个实体项目，另外两个项目则产生数字表征。该实体产品在校内外几个展厅区域展出，允许路人进行评论和探索。
- （2006-2009）大众媒体与传播的替代性表征。这一重点要求学生运用表征[创造力](https://www.interaction-design.org/literature/topics/creativity)（representational creativity），但其核心思路是从一个当代新闻故事开始，然后挖掘该议题中涉及的软件制品，这些制品旨在...

...被表征。由于中后期许多计算机科学专业的学生几乎没有设计和艺术背景，物理项目最终被取消了。
- (2010-2011) 使用网络挖掘（Web mining）和应用程序接口（APIs）进行表征（Representation）。这是一次尝试在表征过程中实现更多的[自动化（automation）](https://www.interaction-design.org/literature/topics/automation)，学生们寻找信息源，然后主要通过 API 将这些信息转化为创意表征。大多数学生使用数据作为信息，而其他学生则使用更复杂的网络结构（例如 XML）作为来源。
- (2012) 重点在于数据结构、数学模型以及动态模型和程序的表征。最终产出是一个交互式游戏或视频作品，其目标是促进低龄群体和非计算专业人士对计算概念的学习。这是该课程目前的形态 (Fishwick 2012)。

我们在 Kelly 定义的精神基础上使用美学（aesthetics）一词，但同时也扩展了“批判性探究（critical inquiry）”的概念，将其涵盖设计和艺术的创意方面。这是理所当然的，因为参与批判性探究是以创意行为为前提且需要创意行为的。关于美学的研究非常多 (Audi 1999, Kivy 2004)，且通常旨在寻找美的普遍属性 (Scruton 2011)。我对美学的看法则侧重于其产生的结果...

...文化探究（cultural inquiry），也就是说设计与艺术形式的巨大多样性。这种“美学即多样性”（aesthetics as diversity）的方法，在精神上与 Hogarth (Burke 1943) 及其相关的“多样中的统一”（unity in variety）这一表述相契合。

## 26.6 迈向作为具身经验的软件（Toward Software as Embodied Experience）


### 26.6.1 引言

将具身（Embodiment）作为一种表征（Representation）形式的部分合理性，是基于教育学习风格（Dede 2005）的。此外，我们正在进行的研究表明，在虚拟环境（Virtual Environment）中，存在感（Presence）与记忆之间存在显著相关性（Fishwick et al. 2010），相关结果目前处于期刊提交阶段。最近的混合现实（Mixed Reality）记忆研究，如 (Ikei and Ota 2008)，表明增强环境（Augmented Environment）对记忆具有积极影响。针对虚拟环境中记忆表现的工具和研究正在不断地被优化和探讨。Parsons and Rizzo (2008) 为一种名为 VRCPAT 的虚拟环境认知工具引入了一项[效度测试（Test of validity）](https://www.interaction-design.org/literature/topics/test)。Johnson and Adamo-Villani (2010) 指出，沉浸感（Immersion）对短期空间记忆有显著影响。

与技术的具身交互（Embodied Interaction）通常通过纯粹的经验，让我们能够理解其内部逻辑、软件和流程。例如，我们通过重复使用数字视频录像机（DVR），学习其状态机（State Machine）。虽然大部分人群可能需要这种学习，但并非每个人都需要将表征推向下一步：即从交互（Interaction）转向反思（Reflection）和具体化（Reification）。然而，后两个步骤在娱乐（艺术、游戏）以及教育领域具有潜在的实用价值。

### 26.6.2 视听探索：蒸汽朋克肥胖机器（Steampunk Obesity Machine）

让我们考虑这样一个作品，它是由系统科学（Systems science）和仿真（Simulation）领域中的一个系统动力学模型（System Dynamics model）所定义的。图 2 和图 3 是系统动力学流图（System Dynamics flow graph, Forrester 1991）的两种不同表示形式，捕捉了人体代谢（Human metabolism）的时间特性（Temporal nature）。

![](https://public-media.interaction-design.org/images/encyclopedia/aesthetic_computing/system_dynamics_flow_graph.jpg)
作者/版权持有者：Inderscience Publishing。版权条款和许可：保留所有权利。经许可转载。详见下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

**图 26.2**：一个包含两个能级（即存量，Stocks）和三个速率（Rates）的系统动力学流图。

图 2 中的图表代表了一个基于流体流动（Fluid flow）类比的虚拟机器（Virtual machine）。流体从源节点（Source node，最左侧的“云”图标）开始，通过由速率分隔的一系列能级系统，最终流向汇节点（Sink node，最右侧的云图标）。更广泛地说，由于流体速度是主导的流动变量，流体流动可以被解释为动能流（Kinetic energy flow）。在机器的起始端（左侧），流体注入代谢和食物摄入，旨在表明能量越多，*身体健康水平（Fitness Level）*越高，但同时*体重（Weight）*也会增加。速率变量 *代谢（Metabolism）* 与身体健康水平、运动等因素的函数组合成正比，

以及营养。由于该模型是动力学（dynamics）的抽象表示（abstract representation），因此模型中并未包含这一精确公式的具体性质。实线曲线箭头反映了通过系统的流体流动（fluid flow），而虚线曲线箭头则反映了用于改变阀门速率的控制设置（control settings）。图 2 是一个假设性的示例，并非旨在作为一个准确或有效的营养模拟模型（simulation model），而是为了证明类似的图表模型（diagrammatic models）在科学和工程领域被广泛使用。这类模型最初是以物理模拟计算机（analog computers）的形式实现的，尽管如今它们更多地以具有图表前端创作能力（diagrammatic front end authoring capability）的数字模型形式存在。MONIAC 或称“Phillips Machine”就是模拟计算时代的一个典型例子 (Swade 2000, Ryder 2009)。

图 3 展示了同一个模型，它是图 2 的合成呈现（synthetic rendition），通过一台“蒸汽朋克机器（steampunk machine）”将其具体化（reified），因为其结构让人联想到自 Gibson 的作品 (Cavallaro 2001) 诞生以来一直广受欢迎的赛博朋克美学（cyberpunk aesthetic）。蒸汽朋克文化具有“为大众夺回技术（reclaiming tech for the masses）”的内涵 (Grossman 2009)。水通过木地板下方的蒸汽动力被泵出，并从两个黄铜孔口喷出，这两个孔口代表了图 2 中的两个阀门图标（valve-icons）。装满水的玻璃容器代表液位数量（level quantities），而木制/黄铜控制杆将所有部件连接在一起。

如图 2 所示。左侧的人类虚拟分身（Human Avatar）正在向我们演示该机器的运行情况，或者我们也可以成为这个分身。自然而然产生的问题是，既然图 2 已经足够，为什么还会有人想要构建这样一个机器。为了回答这个问题，我们需要提出更多的问题，并探讨可能的应用场景（Use-cases）。

![](https://public-media.interaction-design.org/images/encyclopedia/aesthetic_computing/isomorphic_to_fig2_steampunk_obesity_machine.jpg)
Author/Copyright holder: Inderscience Publishing. Copyright terms and
licence: All Rights Reserved. Reproduced with permission. See section 
"Exceptions" in the [copyright terms](https://www.interaction-design.org/about/terms-of-use) below.
**图 26.3**：一个与图 2 同构（Isomorphic）的蒸汽朋克肥胖机器

图 2 以及与该图相对应的方程，最常被熟悉系统动力学方法（System Dynamics Method）的科学家所使用。这些科学家不太可能对如图 3 所示的结构感兴趣，主要是因为他们习惯于并熟悉更形式化的表示（Formal Representations）。然而，对于绝大多数人来说，如果要让他们理解形式化表示，并从中获得动力或受到影响，可能需要额外的激励。因此，图 3 中的机器适用于教育和娱乐。不难想象，图 3 中的机器会非常吸引人，尤其是如果加入需要达成特定目标（如维持稳定）的游戏化特性时。

重量容器（Weight container）中的水位。

### 26.6.3 数据的视觉表示（Visual Representations of Data）

还有许多其他的艺术作品示例，如果将其作为指导，可以开发出对教育有益的审美计算（Aesthetic Computing）产品。绝大多数示例是关于数据的编码（Encoding）和呈现（Presentation），而非程序或模型的编码与呈现。考虑到数据仓库（Data Repositories）和[可访问性（Accessibility）](https://www.interaction-design.org/literature/topics/accessibility)正在迅速扩展，且数据代表了最简单、最容易理解的信息形式，这种趋势是符合逻辑的。请参考图 4 中展示的单个数字模型。

![](https://public-media.interaction-design.org/images/encyclopedia/aesthetic_computing/debt_visualization_infographic.jpg)
作者/版权持有者：Oto Godfrey。版权条款和许可：保留所有权利。经许可转载。详见下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”章节。

**图 26.4**：如果美国债务达到 15 万亿美元时的相对规模。巨大的矩形块代表成叠的 100 美元钞票。

这种将数字编码为成叠 100 美元钞票的方式，通过人们通过图片或经验已知其尺寸的熟悉对象（例如：自由女神像、足球场、卡车）来提供语境（Context）。人们可以通过选择不同的熟悉对象，采用同样的方法来呈现货币金额的其他模拟表示（Analog Representations）。

对象。参与者的投入（Engagement）既可以产生艺术上的结果，也可以产生数学上的结果。例如，我们可以想象在这种表征（Representation）方式中进行数值运算，就像我们过去使用奇普（Quipus）和算盘（Abaci）手动操作那样。

请看 Huff (2006) 的质数序列，图 5 展示了两个质因数编码（Encodings of prime factors）的示例。

![](https://public-media.interaction-design.org/images/encyclopedia/aesthetic_computing/Prime_number_factorization_encodings_1.jpg)
作者/版权持有者：Kenneth A. Huff。版权条款与许可：保留所有权利。经许可转载。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”章节。

![](https://public-media.interaction-design.org/images/encyclopedia/aesthetic_computing/Prime_number_factorization_encodings_2.jpg)
作者/版权持有者：Kenneth A. Huff。版权条款与许可：保留所有权利。经许可转载。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”章节。

**图 26.5 A-B**：质数分解编码（Prime number factorization encodings）（EPF: 2003:V:A:997141 和 2000.24）

图 5 中的这两个编码是纯艺术作品，但同时也可能被用于通过制作谜题来激励学生去理解质因数分解（Prime factorization）。例如，可以想象一个人向他人提供一个视觉编码的整数，然后要求其

让人能够识别数值和因素。图 6 展示了信息存在感（Information Presence）的另外两个示例：Levin 为数据设计的信息可视化涂鸦（Infoviz Graffiti），以及 Living Light。这种涂鸦是一种刻意设计的机制，旨在将具有社会相关性的数值呈现在公共场所。Living Light 是位于韩国首尔的一个永久性户外展亭。该展亭的目的是让观众能够将空气质量等环境指标可视化。随着普适计算（Pervasive Computing）在未来的延伸，大多数平面将变成显示表面，从而为将信息引入我们的日常生活开辟了无数可能性。图 7 展示了一个城市模型，它被转化为一个类似于计算机程序的制品，或称为自动机（Automaton），其输出结果是一份乐谱。

![](https://public-media.interaction-design.org/images/encyclopedia/aesthetic_computing/Infoviz_Adjustable_Pie-Chart_Stencil.jpg)
作者/版权持有者：Golan Levin。版权条款和许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”章节。

![](https://public-media.interaction-design.org/images/encyclopedia/aesthetic_computing/Living_Light.jpg)
作者/版权持有者：David Benjamin 和 Soo-In Yang。版权条款和许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”章节。

**Figure 26.6 A-B**：最左侧：Infoviz

Golan Levin 的 Graffiti/可调节饼图模板（Adjustable Pie-Chart Stencil）。最右侧：David Benjamin 和 Soo-In Yang 的 Living Light。
![](https://public-media.interaction-design.org/images/encyclopedia/aesthetic_computing/Pianola_City_Music.jpg)
作者/版权持有者：Akko Goldenbeld。版权条款与许可：保留所有权利（All Rights Reserved）。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。
**图 26.7**：Pianola City Music

### 26.6.4 文本表示（Textual Representations）

到目前为止，所举的示例主要集中在视觉方面；然而，人们通常希望将此前描述的用于数学表达式的思维方式，扩展到例如软件等领域。人文学科中新兴的领域，如软件研究（Software Studies, Fuller 2008）和批判性代码研究（Critical Code Studies, Marino 2006），将研究形式语言（Formal Languages）的需求置于诠释学（Hermeneutics）的某个维度之下。这些领域也为创建新型人机界面（Human-Computer Interfaces）提供了机遇。例如，我们可以将软件视为一个完整的超媒介化结构（Hyper-mediated Structure, Roth et al. 1994, Anderson et al. 2000）。随后，人们可以通过由链接交互（Link Interaction）促成的具身方法（Embodied Approach），将基于形式语言的构建物视为超媒体（Hypermedia）。

## 26.7 艺术与设计作为具身形式语言的创意影响

提供的示例（包括图 3 至图 7）以不同的方式与审美计算（Aesthetic Computing）相关。由于审美计算是以教育目标为最终产出而具身于形式语言（Formal Languages）之中的，我将概述这些示例如何实现该目标。表 1 包含 5 列：第 1 列是指前文描述的图像或产品；第 2 列是原始媒介；第 3 列是最后 5 行的假设目标（即由于原始意图未知而进行的假设）；第 4 列是将原始产品重新利用于形式语言目标（第 5 列）的示例。让我们看第 3 行：该产品被设计成一种极具吸引力和冲击力的国家债务展示方式。这种创意用法可以被重新定义为学习*数感（Number Sense）*的一种新方式。这些形式语言产品仅为示例，尚未被实际构建；然而，原始的艺术和设计具有双重启发意义——一方面在于其原始目标或用途，另一方面在于其形式能够利用其具身特性（Embodied Characteristics）来实现形式语言教学的目的。

| **示例** | **原始产品** | **审美目标（假设）** | **形式语言产品（示例）** | **形式语言目标** |
|---|---|---|---|---|

| 个人经验（算术） | 字体图像（Typographic Image） | 旨在展示数学形式的优雅 | 包含可移动运算符和操作数的游戏 | 旨在教授算术法则（laws of arithmetic） |
| :--- | :--- | :--- | :--- | :--- |
| Steampunk Obesity Machine (图 2) | 光栅图像（Raster Image）艺术作品 | 旨在创建与蒸汽朋克（steampunk）风格相关的意象 | 展示功能机制与控制的视频 | 旨在教授系统动力学方法论（System Dynamics Methodology） |
| 美国国债（US National Debt, 图 3） | 光栅图像艺术作品 | 旨在利用比例（scale）展示美国债务的规模 | 一套触觉（tactile）积木与物体 | 旨在教授数感（number sense） |
| 质数分解（Prime Number Factorization, 图 4） | 光栅图像艺术作品 | 旨在利用质数编码（prime number encoding）赞美有机形式 | 将编码作为 3D 谜题的冒险游戏 | 旨在教授质数与分解 |
| 信息可视化涂鸦（Infoviz Graffiti, 图 5a） | 户外场所的涂鸦与模板 | 旨在向公众呈现社会信息 | 一款替代现实游戏（alternate reality game, ARG）（寻找涂鸦） | 旨在教授百分比概念 |
| Living Light (图 5b) | 户外雕塑 | 旨在向公众呈现环境信息 | 一件动力学雕塑（kinetic sculpture） | 旨在教授数据结构（data structures） |
| Pianola City Music (图 6) | 室内动力学艺术作品 | 旨在探索建筑-音乐接口（interface） | 室内动力学物体 | 旨在教授通过声音进行数据搜索的概念 |
| 超媒介化软件工程（Hyper-mediated software engineering） | 基于 Web 的计算文学（computational literature） | 旨在代表文化知识 | 超媒介化软件/代码 | 旨在鼓励学习如何编程 |

**表 26.1**：审美转换（Aesthetic Transformation）至形式语言学习目标

表 1 通过对现有艺术作品的重新利用（Repurposing）来展示审美计算（Aesthetic Computing），但这一步骤是可选的。捕捉具身交互（Embodied Interaction）精髓的基于形式语言的产品，可以直接从初步设计、详细设计一直进行到具体实现。Steampunk Obesity Machine（表 1，第 2 行）就是一个典型的案例。尽管一张海报图像（图 3）曾是一场策划艺术展（Harn 2011）的一部分，但该图像的初衷是作为一台用于教授系统动力学（System Dynamics）概念的虚拟机的初步设计。该机器目前尚未被构建。

## 26.8 利用严肃游戏（Serious Gaming）实现具身计算（Embodied Computing）

如果不提及视频游戏和主机游戏文化，关于审美计算（aesthetic computing）及其通过具身形式语言（embodied formal language）进行解释的讨论将是不完整的。这里有两个具有代表性的例子：游戏 *Minecraft* (2011) 中的逻辑电路，以及名为 *Code Hero* (PrimerLabs 2011) 的游戏。*Minecraft* 是一款“方块游戏”，玩家在空间中移动，并使用挖掘（mining）的隐喻来构建方块。游戏中的一些程序化能力（procedural capabilities）吸引了社区成员创建基础电路，进而利用逻辑电路构建出功能完备的计算机。由于 *Minecraft* 具有高度的交互性，并且还能唤起临场感（sense of presence），这种类型的“黑客行为”与审美计算的概念是一致的：玩家们通过具身交互（embodied interaction）共同构建电路。

Primer Labs 最近创建了一款名为 *Code Hero* 的游戏，玩家在其中学习 Javascript 等编程脚本语言。然而，正是这种教学法（pedagogy）的手段将其直接置于具身领域：玩家拥有一把枪，可以将“代码射向”目标对象，从而使该对象对代码做出反应。实际上，这是一种数据流的具体化（reified）形式，类似于 $\lambda$ 演算（lambda calculus）及其基于该形式体系（formalism）的语言（如 Lisp）中的能力（例如，考虑一个函数可以接收另一个函数的 “map” 函数）。

将函数作为输入，然后将该函数应用于参数，从而产生输出）。图 8 展示了由 Ganapati (2010) 描述的一个 Minecraft 算术逻辑单元（Arithmetic Logic Unit, ALU），图 9 展示了 *Code Hero* 的一张截图。

![](https://public-media.interaction-design.org/images/encyclopedia/aesthetic_computing/Arithmetic_Logic_Unit_minecraft.jpg)
版权条款与许可：版权所有。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面中的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子节）。

**图 26.8**：在利用 Minecraft 游戏引擎构建的沉浸式游戏空间（immersive play space）中，使用“红石”构建的算术逻辑单元。

![](https://public-media.interaction-design.org/images/encyclopedia/aesthetic_computing/Code_Hero_Game.jpg)
作者/版权持有者：Primer Labs。版权条款与许可：版权所有。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面中的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子节）。

**图 26.9**：*Code Hero* 游戏：在进入学习空间之前与 Ada Lovelace 的虚拟形象（avatar）对话，在该空间中，玩家可以通过向物体发射脚本来学习如何编写脚本代码（script code）。

## 26.9 协作角色、可用性与体验

审美计算（Aesthetic Computing）始于一个形式语言结构（formal language construct），例如数字、数据、模型或软件。随后的挑战在于如何通过具身化（embodiment）来呈现这一结构。我们注意到，当我们演示能够抓取数字并将其移向运算符时，“具身化”可以简单到仅仅是纯粹的具体化（reification），而无需对现有对象进行表示。然而，具体化也可以暗示对象的表示，如图 4 至图 7 所示。我需要探讨审美计算中关于“谁”和“为什么”这两个方面。

首先，谁来创建这些表示？在协作的情况下，我建议由人文学者、艺术家和计算机科学家组成团队。人文学者能带来不同的哲学和理论，有助于塑造最终的表示形式。艺术家拥有创建表示形式的创意视角和工具，而计算机科学家可以承担两个角色：一是帮助构建人文学者和艺术家用于提取信息的工具，二是通过在人机界面（human-computer interface）中将具身化外部化（externalizing embodiment），从而实现随之而来的交互。

其次，谁将使用这些表示？在我的审美计算课程中，学生们起初经常感到困惑，不明白为什么除了图表之外还要构建其他东西。这种困惑是在预料之中的，但我们必须

在定义[可用性（Usability）](https://www.interaction-design.org/literature/topics/usability)时需谨慎：对谁可用，以及出于什么目的而可用？我们需要明确 1) 表征（Representation）的目标，以及 2) 最终目标用户。具身表征（Embodied Representations）的目标包括教育、艺术和娱乐（例如：电影、视觉与表演艺术、小说）。目标用户可以是学校中的任何年级，或者是公众中的某个群体。从心理学角度来看，对“可用性”的广义理解可以涵盖[用户目标（User Goals）](https://www.interaction-design.org/literature/topics/user-goals)，包括：提升效价（Valence）、增强动力、改变态度，以及改善短期或长期记忆。数学家和计算机科学家并非目标群体，因为这些人群已经熟练掌握现有的符号系统（Notations）。审美计算（Aesthetic Computing）并不强调信息提取（Information Extraction），而更侧重于将娱乐、艺术和人文应用于形式语言（Formal Languages），其最大的实际效果体现在教育领域。因此，目标用户是所有基于形式语言教学（如数学、计算机科学）的正式和非正式学习者。

鉴于各方的利益点不同，参与者在审美计算中的角色可能会有所不同。例如，对于计算机科学家而言，图 5 可作为创建特效和交互式游戏的设计模板，旨在表达

质数（prime numbers）的元素以及将其分解为这些质数的过程。艺术家的作品是一种媒介，通过它，形式语言（formal language）的这一方面得到了创造性的表达。艺术家与计算机科学家的目标显然不同，但手段（即质数的表示方式）是共同的。这种目的不同但手段相似的情况在其他示例中也有体现。例如，Perl 诗歌（Perl poetry，即使用 Perl 编程语言创作的诗歌）对于作者来说可能是一种审美产品（aesthetic product）——其本身就是一个正当的目的。而对于计算机科学家来说，这种产品则代表了一种表达不同目的的媒介——即形式语言的“信息（message）”。因此，从“美学计算（aesthetic computing）”这一短语的词语排列来看，其核心在于计算——即形式语言的学习。然而，审美产品在这一学习活动中起着关键作用，使得艺术家、学者和计算机科学家能够在不同的意图和目标下进行协作。

与美学计算相关的其他领域还包括信息可视化（information visualization）（Card et al. 1999, Ward et al. 2010）和软件可视化（software visualization）（Eades and Zhang 1996, Stasko et al. 1998, Zhang 2007, Diehl 2007）；然而，这些领域的目标通常与美学计算截然不同。在信息可视化中，目标是高效地传递数据和信息，而对于美学计算，其目标则是通过高度具身化（embodied）的……

交互式且具有美感的艺术与娱乐产品。
因此，美学计算（Aesthetic Computing）比构建旨在即时消费的表征（representations）（例如报纸上的图表和地图）能提供更深层的体验。读者会发现，在与计算机的高层交互中，隐喻（metaphor）的使用非常丰富。我们处于一种界面文化（interface culture）之中 (Johnson 1997)。然而，例如在“桌面”上使用的隐喻，尚未进入数学和计算的核心。诸如计算思维（computational thinking）(Wing 2006) 等努力是朝着正确方向迈出的一步。

Laurel (1991) 在其《Computing as Theatre》中预见性地捕捉到了美学计算的一个前提条件。然而，Laurel 主要是将人机交互（human-computer interaction）构建为一场复杂的剧场制作，其中包含许多与剧场相同的元素。计算的*使用*及其相关的交互现象就像剧场一样。然而，我们发现，当我们打开包含通常被隐藏的数据、公式、代码和模型等原子元素的“黑盒（black box）”盖子时，会发现计算从底层到顶层彻头彻尾就是一场剧场。

## 26.10 迈向一种美学计算方法

虽然提出想法和方向很有趣，但一个程序化方法（procedural method）即使仅作为通用指南，也能有助于构建一个学科。Fishwick (2007a) 是这一过程的初步尝试，他使用了一个简单的代码示例，将其表示为建筑物中的一组房间，并配以部分叙事以提供上下文。图 10 为描述 (Fishwick 2012) 中使用的方法提供了基础：

![](https://public-media.interaction-design.org/images/encyclopedia/aesthetic_computing/Aesthetic_Computing_Method.jpg)
作者/版权持有者：由 Paul Fishwick 提供。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。
**图 26.10**：美学计算方法（Aesthetic Computing Method）

我们从（图 10 的左上角）一个形式语言结构（formal language construct）开始，旨在将其传达给数学和计算领域的非专业人士，以扩大人们对计算概念的接触。星号表示 (Fishwick 2012) 中的当前重点。目标用户将取决于形式语言的类型。如果目标是数感（number sense）且数字较为简单，那么目标群体可能是小学生。如果形式语言是简单的代数公式，那么目标群体可能是八年级的数学学习者。更复杂的数学和计算结构则可能需要更高年级的学生。

包括大学以及研究生阶段的非正式学习环境（informal learning contexts）。

然而，这种表征（Representation）方法的一个理想结果是，通过将游戏和视频作为激励媒介（motivational media），让年幼的孩子接触到看似复杂的数据结构和程序。我预期这些方法可以起到以下作用：1）为随后更传统的教学和符号表示（notations）提供脚手架（scaffolding）；2）作为辅助工具（secondary devices，例如拼图），用以强化那些部分学习者在使用标准符号时难以理解的概念。其目标并非消除标准符号，因为这样做会适得其反。在图 10 中，表征被分为两个组成部分：实现表征的方法，以及支持具身化（embodiment）的技术。强调或体现具身化的最终产品各不相同。一部优秀的虚构作品可以营造强烈的存在感（presence）和虚拟具身感（virtual embodiment），而一个设计欠佳的劣质交互游戏则可能会被人们忽视。

## 26.11 新的连接

我在推动审美计算（Aesthetic Computing）方面的一个主要目标是连接不同的学科——特别是将计算领域与人文艺术联系起来。正如设计师和人文主义学者所证明的，“代码”和“数据”等人工制品（Artifacts）现在正被重新解读和创作。出现这种情况的原因有很多。也许，普适计算（Ubiquitous Computing）的趋势是最重要的驱动因素——软件无处不在，因此，作为一种自然的延伸，它也具有文化属性。我欢迎艺术家、设计师和人文主义者进入“形式语言（Formal Languages）”领域，并希望通过协作、跨学科讨论和批判，我们能够让计算的核心元素，甚至可能是数学，重新人性化（Re-humanize）。

## 26.12 学科与技术挑战

审美计算（Aesthetic Computing）领域并非没有挑战。其目标是利用具身理论（Embodiment Theories）来构建用于学习形式语言（Formal Languages）的新型计算机界面。我所涵盖的学科中，其子领域均指向这一目标，但每个领域仍面临重大挑战：

- *数学（Mathematics）*：数学教育以及认知语言学（Cognitive Linguistics）在数学学习中应用的相关文献基础深厚，且支持审美计算。然而，这部分知识体系更多地侧重于分析和理论构建，而非通过类比，在数学教育中构建新型界面，从而通过实现（Realization）来充分利用具身理论。一些关于*虚拟教具（Virtual Manipulatives）*的尝试是一个良好的开端，但这项工作应进一步扩展，采用强调具身性的下一代界面能力（例如：多点触控显示屏、身体追踪、混合/虚拟现实技术）。
- *计算（Computing）*：计算教育（Computing Education）的相关文献提供了相当易用的界面，用于查看程序执行的结果；然而，这些程序通常局限于标准的字母数字表示法（Canonical Alphanumeric Notation），所有的人机交互都发生在程序执行过程中，而非在程序内部。软件可视化（Software Visualization）的尝试正朝着审美计算所需的方向发展，然而，还存在更广泛的可能性用于

如果目标是通过沉浸（immersion）、情境学习（situated learning）和交互式游戏来教授非专业人士，那么目前的表示法（representation）可能不足。图表适用于沟通，但如果目标是探索深度具身化（embodied）的学习方法，则应更深入地研究额外的媒介和更新的界面——正如数学教育中所建议的那样。

- *人文科学（Humanities）：* 认知语言学（cognitive linguistics）及其衍生的具身理论（embodiment theories）为美学计算（aesthetic computing）奠定了基础，但与数学学习哲学方面的工作类似，在将这些理论转化为人机界面（human-computer interface）方面，相应的努力较少。相反，文化理论产出近期将“代码”专门视为一种新型的素养（literacy）（例如，批判性代码研究 critical code studies）。然而，这类产出倾向于避开语言分析，而侧重于社会历史分析。新型的、具身化的代码界面可以基于这些学术分析而构建，但这些界面还应参考符号学（semiotics）的关键事实（如类比 analogy 和隐喻 metaphor），因为这些事实构成了形式语言（formal languages）的基础。目前似乎存在一种倾向于文本表示（textual notation）的 [偏见（bias）](https://www.interaction-design.org/literature/topics/bias)，而未能探索更广泛形式的“具身素养（embodied literacy）”，而文本表示应仅作为其中的一个维度。

- *艺术与设计（Art & Design）：* 艺术作品传统上

将形式语言（formal languages）视为“黑盒”，即创建艺术或设计所需的工具。与人文科学不同——在人文科学中，代码已成为主体材料（subject material）——在艺术领域，代码往往被纯粹地视为一种工具，无论它是嵌入在软件包中，还是通过基于文本的开发环境进行编程。这一观察的唯一例外可能是 [平面设计](https://www.interaction-design.org/literature/topics/graphic-design) 中的排版学（typography），其主体材料即为文本。需要更多的探索，使形式语言能够成为艺术作品的积极主体。

这四个领域中的每一个都面临着一些共同的挑战。考虑到类比（analogy）是科学实践中隐喻（metaphor）的引擎，美学计算（aesthetic computing）产品可以通过增加对类比的关注而得以创建。另一个观察结果是，除艺术与设计外，人们传统上侧重于字母记号（alphabetic notation）。这种记号法为我们提供了极大的便利，并丰富了我们的形式语言。然而，还有其他类型的记号法能够更多地调用身体的感觉运动功能（sensorimotor functions）。图表（diagrams）是观察这一转变的良好切入点，因为在图表中，针对基于文本记号的空间隐喻（spatial metaphors）大量存在；但我们不应将具身探索（embodied explorations）局限于图表。

美学计算的一个主要挑战在于技术层面。基于前文图示中所描述的产品类型来构建新界面，目前成本仍然相对较高。“3D 建模（3D modeling）”作为一种

实时技术界面能力（real-time technical interface capability）远未达到 *Tron*、*The Matrix* 和 *Holodeck* 中所描绘的未来主义景象。与图表化方法（diagrammatic approaches）相比，三维建模与动画制作仍然是一项重大挑战；即便是在软件工程解决方案市场中，基于图表的软件建模（diagram-based software modeling，例如模型驱动架构 model-driven architecture）也因文本符号（textual symbols）使用起来相对便捷而难以被广泛接受。人机交互（Human-computer interaction）解决方案的范围和能力正在不断扩展，但要实现能够简单且低成本地在形式语言结构（formal language constructs）中获得具身化（embodied），我们仍有很长的路要走。

## 26.13 总结：具身形式语言的论据

本章以数学方面的个人经历开始，随后转向对具身认知（Embodied Cognition）的讨论，并给出了一些审美计算（Aesthetic Computing）可以应用的示例。审美计算领域主要建立在具身性（Embodiment）的基础之上——即我们是否相信身体的交互塑造了我们的思维。这种关于具身性的假设在哲学中根深蒂固。我们都意识到自己拥有身体和心灵，且大多数人会同意后者是前者的产物。然而，直到最近才出现相关文献表明两者之间存在强烈的关系，以至于思维本身——即使是对抽象对象的思维——也是具身的。支撑具身性的理论具有说服力，但我们心中一直存在一个挥之不去的疑问：这一理论如何能改变我们的行为方式和实践方式。如果我想象自己在算术运算过程中，将一个数字抓取并推过一层伪生物膜（Pseudo-biological membrane），那么我想构建一个能够将理论注入实践的人机界面（Human-Computer Interface），从而强化这一心理序列。这种感知到的需求与本章开头提出的审美计算假设相一致：*鉴于认知的具身特质，我们应当通过创新的学习形式语言（Formal Languages）的人机界面来实现这种具身性。*

实现这一目标需要对

学科之间的相互作用，以及这些学科中的具身理论（Embodiment Theories）是如何相互作用和关联的。其实现还需要一系列较新的“虚拟连续体（Virtuality Continuum）”技术，使我们能够实现 Biocca (1997) 所称的渐进式具身程度（Degrees of Progressive Embodiment）。关于虚拟现实（Virtual Reality）的技术及其特性，Sherman and Craig (2002) 以及 Bowman et al. (2004) 进行了综述；而关于增强现实（Augmented Reality）的部分则由 Bimber and Raskar (2005) 进行了综述。

## 26.14 学习审美计算的更多资源

为了深入理解计算（Computing）作为一门学科及其在审美计算（Aesthetic Computing）中所体现的产物（Artifacts），1998 年的 ACM 计算分类系统（Computing Classification System, CCS 1998）是一个很好的起点。尽管我对美学的探讨是基于其原始的感知定义（Perceptual Definition），但 Kelly (1998) 在四卷书中收集了从哲学和艺术这一核心衍生出的相关内容。尽管信息可视化（Information Visualization）侧重于高效沟通（例如，阅读类似于报纸中的图表），但一些由 Vande Moere (2011) 策划的档案（如 *infosthetics*，即信息美学）则更为广泛，涵盖了各种潜在的应用场景——从高效沟通到体验、教育和游戏。对于基于文本的表示形式，HASTAC (2011) 是一个高层级的博主和项目仓库，其中许多与数字人文（Digital Humanities）相关。建议读者查阅本章中引用的文章。

## 26.15 致谢

我首先要感谢所有从始创之初就参与到这段旅程中的个人，包括我在艺术、自然科学与社会科学、计算机科学以及数学领域的同事们。我《审美计算（Aesthetic Computing）》课程的学生们不得不包容这些想法，并且他们创作出了我从未想象过的精彩作品。感谢以下抽出时间对本手稿早期版本提出极具价值的批判性建议的同事：Sophia Acord (University of Florida), Michael Kelly (University of North Carolina at Charlotte), Mads Søgaard ([Interaction Design](https://www.interaction-design.org/literature/topics/interaction-design)), 以及 Kang Zhang (University of Texas at Dallas)。文中如有任何错误或遗漏，由我本人承担全部责任。

## 26.16 References

[Anderson](https://www.interaction-design.org/references/authors/kenneth_m__anderson.html), Kenneth M., [Taylor](https://www.interaction-design.org/references/authors/richard_n__taylor.html), Richard N. and [Whitehead](https://www.interaction-design.org/references/authors/e__james_whitehead.html), E. James (2000): *Chimera: hypermedia for heterogeneous software development environments*. In [ACM Transactions on Information Systems](https://www.interaction-design.org/references/periodicals/acm_transactions_on_information_systems.html), 18 (3) pp. 211-245
[Audi](https://www.interaction-design.org/references/authors/robert_audi.html), Robert (ed.) (1999): *The Cambridge Dictionary of Philosophy.* Cambridge University Press
[Barsalou](https://www.interaction-design.org/references/authors/lawrence_w__barsalou.html), Lawrence W. (2010): *Grounded Cognition: Past, Present, and Future*. In [Topics in Cognitive Science](https://www.interaction-design.org/references/periodicals/topics_in_cognitive_science.html), 2 (4)

[Beck](https://www.interaction-design.org/references/authors/dennis_beck.html), Dennis, [Fishwick](https://www.interaction-design.org/references/authors/paul_a__fishwick.html), Paul A., [Kamhawi](https://www.interaction-design.org/references/authors/rasha_kamhawi.html), Rasha, [Coffey](https://www.interaction-design.org/references/authors/amy_jo_coffey.html), Amy Jo and [Henderson](https://www.interaction-design.org/references/authors/julie_henderson.html), Julie (2011): *Synthesizing Presence: A Multidisciplinary Review of the Literature*. In [Journal of Virtual Worlds Research](https://www.interaction-design.org/references/periodicals/journal_of_virtual_worlds_research.html), 3 (3)
[Bimber](https://www.interaction-design.org/references/authors/oliver_bimber.html), Oliver and [Raskar](https://www.interaction-design.org/references/authors/ramesh_raskar.html), Ramesh (2005): *Spatial Augmented Reality: Merging Real and Virtual Worlds.* A K Peters, Ltd
[Biocca](https://www.interaction-design.org/references/authors/frank_biocca.html), Frank (1997): *The Cyborg's Dilemma: Progressive Embodiment in Virtual Environments*. In [Journal of Computer-Mediated Communication](https://www.interaction-design.org/references/periodicals/journal_of_computer-mediated_communication.html), 3 (2)

[Bolter](https://www.interaction-design.org/references/authors/jay_david_bolter.html), Jay David and [Grusin](https://www.interaction-design.org/references/authors/richard_grusin.html), Richard (2000): *Remediation: Understanding New Media.* The MIT Press
[Bowman](https://www.interaction-design.org/references/authors/doug_a__bowman.html), Doug A., [Kruijff](https://www.interaction-design.org/references/authors/ernst_kruijff.html), Ernst, [LaViola](https://www.interaction-design.org/references/authors/joseph_j__laviola.html), Joseph J. and [Poupyrev](https://www.interaction-design.org/references/authors/ivan_poupyrev.html), Ivan (2004): *3D User Interfaces: Theory and Practice.* Addison-Wesley Professional
[Brown](https://www.interaction-design.org/references/authors/john_seely_brown.html), John Seely, [Collins](https://www.interaction-design.org/references/authors/allan_collins.html), Allan and [Duguid](https://www.interaction-design.org/references/authors/paul_duguid.html), Paul (1989): *Situated Cognition and the Culture of Learning*. In[Educational Researcher](https://www.interaction-design.org/references/periodicals/educational_researcher.html), 18 (1)
[Burke](https://www.interaction-design.org/references/authors/joseph_burke.html), Joseph (1943): *Hogarth and Reynolds: A contrast in English art theory.* Oxford University Press

[Buxton](https://www.interaction-design.org/references/authors/bill_buxton.html), Bill (2008): The Role of the Artist in the Laboratory. In: (ed.). "Meisterwerke der Computer Kunst". pp. 29-32
[Card](https://www.interaction-design.org/references/authors/stuart_k__card.html), Stuart K., [Mackinlay](https://www.interaction-design.org/references/authors/jock_d__mackinlay.html), Jock D. and [Shneiderman](https://www.interaction-design.org/references/authors/ben_shneiderman.html), Ben (eds.) (1999): *Readings in Information Visualization: Using Vision to Think.* Academic Press
[Cavallaro](https://www.interaction-design.org/references/authors/dani_cavallaro.html), Dani (2001): *Cyberpunk & Cyberculture: Science Fiction and the Work of William Gibson.* The Athlone Press
[Cockton](https://www.interaction-design.org/references/authors/gilbert_cockton.html), Gilbert (2012). *Usability Evaluation*. Retrieved 4 November 2013 from [URL to be defined - in press]
[Dede](https://www.interaction-design.org/references/authors/chris_dede.html), Chris (2005): *Planning for Neomillennial Learning Styles Neomillennial Learning Styles and Mediated Immersion*. In [EDUCAUSE Quarterly](https://www.interaction-design.org/references/periodicals/educause_quarterly.html), 28 (1) pp. 18-21

[Devlin](https://www.interaction-design.org/references/authors/keith_devlin.html), Keith (2006): The Useful and Reliable Illusion of Reality in Mathematics. In: [Towards a New Epistemology of Mathematics. Workshop at GAP.6 Freie Universität Berlin](https://www.interaction-design.org/references/conferences/towards_a_new_epistemology_of_mathematics__workshop_at_gap-dot-6_freie_universit%E4t_berlin.html) 2006.
[Dewey](https://www.interaction-design.org/references/authors/john_dewey.html), John (1934): *Art as Experience.* Perigee Trade
[Diehl](https://www.interaction-design.org/references/authors/stephan_diehl.html), Stephan (2007): *Software Visualization: Visualizing the Structure, Behaviour, and Evolution of Software.*Springer
[Dieterle](https://www.interaction-design.org/references/authors/edward_dieterle.html), Edward, [Dede](https://www.interaction-design.org/references/authors/chris_dede.html), Chris and [Schrier](https://www.interaction-design.org/references/authors/karen_schrier.html), Karen (2007): "Neomillennial" Learning Styles Propagated by Wireless Handheld Devices. In: [Lytras](https://www.interaction-design.org/references/authors/miltiadis_d__lytras.html), Miltiadis D. and [Naeve](https://www.interaction-design.org/references/authors/ambjorn_naeve.html),
 Ambjorn (eds.). "Ubiquitous and Pervasive Knowledge and Learning 
Management: Semantics, Social Networking and New Media to Their Full 
Potential". pp. 35-66

[Diffey](https://www.interaction-design.org/references/authors/t__j__diffey.html), T. J. (1995): *A note on the meanings of the term 'aesthetic'*. In [The British Journal of Aesthetics](https://www.interaction-design.org/references/periodicals/the_british_journal_of_aesthetics.html), 35 (1) pp. 61-66
[Dourish](https://www.interaction-design.org/references/authors/paul_dourish.html), Paul (2001): *Where the Action Is: The Foundations of Embodied Interaction.* MIT Press
[Eades](https://www.interaction-design.org/references/authors/peter_eades.html), Peter and [Zhang](https://www.interaction-design.org/references/authors/kang_zhang.html), Kang (1996): *Software Visualization. Series on Software Engineering and Knowledge Engineering.* World Scientific Pub Co Inc
[Feldman](https://www.interaction-design.org/references/authors/jerome_feldman.html), Jerome (2006): *From Molecule to Metaphor: A Neural Theory of Language.* A Bradford Book
[Feldman](https://www.interaction-design.org/references/authors/jerome_feldman.html), Jerome and [Narayanan](https://www.interaction-design.org/references/authors/srinivas_narayanan.html), Srinivas (2004): *Embodied meaning in a neural theory of language*. In [Brain and Language](https://www.interaction-design.org/references/periodicals/brain_and_language.html), 89 (2) pp. 385-392

[Fishwick](https://www.interaction-design.org/references/authors/paul_a__fishwick.html), Paul A. (2012). *Aesthetic Computing Class*. Retrieved 1 January 2012 from University of Florida: [http://www.cise.ufl.edu/~fishwick/ac/2012](http://www.cise.ufl.edu/~fishwick/ac/2012)
[Fishwick](https://www.interaction-design.org/references/authors/paul_a__fishwick.html), Paul A. (ed.) (2006): *Aesthetic Computing.* The MIT Press
[Fishwick](https://www.interaction-design.org/references/authors/paul_a__fishwick.html), Paul A. (2007a): Customized Visual Computing: The Aesthetic Computing Method. In: [Ferri](https://www.interaction-design.org/references/authors/fernando_ferri.html),
 Fernando (ed.). "Visual Languages for Interactive Computing: 
Definitions and Formalizations (Premier Reference Source)". pp. 425-435
[Fishwick](https://www.interaction-design.org/references/authors/paul_a__fishwick.html), Paul A. (ed.) (2007b): *Handbook of Dynamic System Modeling.* Chapman and Hall - CRC
[Fishwick](https://www.interaction-design.org/references/authors/paul_a__fishwick.html), Paul A. (2002): *Aesthetic Programming: Crafting Personalized Software*. In [Leonardo](https://www.interaction-design.org/references/periodicals/leonardo.html), 35 (4) pp. 383-390
[Fishwick](https://www.interaction-design.org/references/authors/paul_a__fishwick.html), Paul A. (1995): *Simulation Model Design and Execution: Building Digital Worlds.* Prentice Hall

[Fishwick](https://www.interaction-design.org/references/authors/paul_a__fishwick.html), Paul A. (2008): *Software Aesthetics: From Text and Diagrams to Interactive Spaces Paul A. Fishwick*. In[International Journal of Arts and Technology](https://www.interaction-design.org/references/periodicals/international_journal_of_arts_and_technology.html), 1 (1) pp. 1-13
[Fishwick](https://www.interaction-design.org/references/authors/paul_a__fishwick.html), Paul A. (2012b): *A Decade of Digital Arts and Sciences at the University of Florida*. In [Leonardo](https://www.interaction-design.org/references/periodicals/leonardo.html), pp. 211-216
[Fishwick](https://www.interaction-design.org/references/authors/paul_a__fishwick.html), Paul A. and [Bertelsen](https://www.interaction-design.org/references/authors/olav_w__bertelsen.html), Olav W. (2002). *Dagstuhl Seminar Report Number 348*.[http://www.dagstuhl.de/Reports/02/02291.pdf](http://www.dagstuhl.de/Reports/02/02291.pdf)
[Fishwick](https://www.interaction-design.org/references/authors/paul_a__fishwick.html), Paul A. and [Park](https://www.interaction-design.org/references/authors/yuna_a__park.html), Yuna A. (2008): A 3D Environment for Exploring Algebraic Structure and Behavior. In:[Ferdig](https://www.interaction-design.org/references/authors/richard_e__ferdig.html),
 Richard E. (ed.). "Handbook of Research on Effective Electronic Gaming 
in Education Set of 3". Information Science Referencepp. 546-559

[Fishwick](https://www.interaction-design.org/references/authors/paul_a__fishwick.html), Paul A., [Coffey](https://www.interaction-design.org/references/authors/amy_j__coffey.html), Amy J., [Kamhawi](https://www.interaction-design.org/references/authors/rasha_kamhawi.html), Rasha and [Henderson](https://www.interaction-design.org/references/authors/julie_henderson.html), Julie (2005): An experimental design and preliminary results for a cultural training system simulation. In: [Simulation Conference WSC, Proceedings of the 2010 Winter](https://www.interaction-design.org/references/conferences/simulation_conference_wsc%2C_proceedings_of_the_2010_winter.html) 2005. pp. 799-810
[Fishwick](https://www.interaction-design.org/references/authors/paul_a__fishwick.html), Paul A., [Diehl](https://www.interaction-design.org/references/authors/stephan_diehl.html), Stephan, [Prophet](https://www.interaction-design.org/references/authors/jane_prophet.html), Jane and [Lowgren](https://www.interaction-design.org/references/authors/jonas_lowgren.html), Jonas (2005b): *Perspectives on Aesthetic Computing*. In [Leonardo](https://www.interaction-design.org/references/periodicals/leonardo.html), 38 (2) pp. 133-141
[Fuller](https://www.interaction-design.org/references/authors/matthew_fuller.html), Matthew (ed.) (2008): *Software Studies: A Lexicon (Leonardo Book Series).* The MIT Press

[Gershenfeld](https://www.interaction-design.org/references/authors/neil_gershenfeld.html), Neil, [Krikorian](https://www.interaction-design.org/references/authors/raffi_krikorian.html), Raffi and [Cohen](https://www.interaction-design.org/references/authors/danny_cohen.html), Danny (2004): *The Internet of things*. In [Scientific American](https://www.interaction-design.org/references/periodicals/scientific_american.html), 291 (4) pp. 76-81
[Ghezzi](https://www.interaction-design.org/references/authors/carlo_ghezzi.html), Carlo and [Jazayeri](https://www.interaction-design.org/references/authors/mehdi_jazayeri.html), Mehdi (1997): *Programming Language Concepts.* Wiley
[Goldin](https://www.interaction-design.org/references/authors/gerald_a_goldin.html), Gerald A and [Kaput](https://www.interaction-design.org/references/authors/james_j_kaput.html), James J (1996): A Joint Perspective on the Idea of Representation in Learning and Doing Mathematics. In: [Steffe](https://www.interaction-design.org/references/authors/leslie_p__steffe.html), Leslie P., [Nesher](https://www.interaction-design.org/references/authors/pearla_nesher.html), Pearla, [Cobb](https://www.interaction-design.org/references/authors/paul_cobb.html), Paul, [Goldin](https://www.interaction-design.org/references/authors/gerard_a__goldin.html), Gerard A. and [Greer](https://www.interaction-design.org/references/authors/brian_greer.html), Brian (eds.). "Theories of Mathematical Learning". Routledgepp. 397-431

[Grau](https://www.interaction-design.org/references/authors/oliver_grau.html), Oliver (2004): *Virtual Art: From Illusion to Immersion (Leonardo Books).* The MIT Press
[Greenfield](https://www.interaction-design.org/references/authors/adam_greenfield.html), Adam (2006): *Everyware: The Dawning Age of Ubiquitous Computing.* New Riders Publishing
[Grossman](https://www.interaction-design.org/references/authors/lev_grossman.html), Lev (2009). *Steampunk: Reclaiming Tech for the Masses*. Retrieved 19 April 2012 from Times Magazine: [http://www.time.com/time/magazine/article/0,9171,1...](http://www.time.com/time/magazine/article/0,9171,1945343,00.html)
[Guhe](https://www.interaction-design.org/references/authors/markus_guhe.html), Markus, [Smaill](https://www.interaction-design.org/references/authors/alan_smaill.html), Alan and [Pease](https://www.interaction-design.org/references/authors/alison_pease.html), Alison (2009): A formal cognitive model of mathematical metaphors. In:[Proceedings of the 32nd annual German conference on Advances in artificial intelligence](https://www.interaction-design.org/references/conferences/proceedings_of_the_32nd_annual_german_conference_on_advances_in_artificial_intelligence.html) 2009. pp. 323-330
[Hadamard](https://www.interaction-design.org/references/authors/jacques_hadamard.html), Jacques (1996): *The Mathematician's Mind.* Princeton University Press

[Hassenzahl](https://www.interaction-design.org/references/authors/marc_hassenzahl.html), Marc (2011). [*User Experience*](https://www.interaction-design.org/literature/topics/ux-design)* and Experience Design*. Retrieved 4 November 2013 from [URL to be defined - in press]
[Hopcroft](https://www.interaction-design.org/references/authors/john_e__hopcroft.html), John E., [Motwani](https://www.interaction-design.org/references/authors/rajeev_motwani.html), Rajeev and [Ullman](https://www.interaction-design.org/references/authors/jeffrey_d__ullman.html), Jeffrey D. (2000): *Introduction to Automata Theory, Languages, and Computation (2nd Edition).* Addison Wesley
[Huff](https://www.interaction-design.org/references/authors/kenneth_a__huff.html), Kenneth A. (2006): Visually Encoding Numbers using Prime Factors. In: [Fishwick](https://www.interaction-design.org/references/authors/paul_a__fishwick.html), Paul A. (ed.). "Aesthetic Computing (Leonardo Books)". The MIT Press
[Ifrah](https://www.interaction-design.org/references/authors/georges_ifrah.html), Georges (2002): *The Universal History of Computing: From the Abacus to the Quantum Computer.* Wiley

[Ikei](https://www.interaction-design.org/references/authors/yasushi_ikei.html), Yasushi and [Ota](https://www.interaction-design.org/references/authors/hirofumi_ota.html), Hirofumi (2008): *Spatial Electronic Mnemonics for Augmentation of *[*Human Memory*](https://www.interaction-design.org/literature/topics/human-memory). In[2008 IEEE Virtual Reality Conference](https://www.interaction-design.org/references/periodicals/2008_ieee_virtual_reality_conference.html), 53 (14) pp. 217-224
[Johnson](https://www.interaction-design.org/references/authors/mark_johnson.html), Mark (2007): *The Meaning of the Body: Aesthetics of Human Understanding.* University of Chicago Press
[Johnson](https://www.interaction-design.org/references/authors/steven_a__johnson.html), Steven A. (1997): *Interface Culture.* Basic Books
[Johnson](https://www.interaction-design.org/references/authors/mark_johnson.html), Mark (1987): *Body in the Mind: The Bodily Basis of Meaning, Imagination and Reason.* University of Chicago Press
[Johnson](https://www.interaction-design.org/references/authors/eric_johnson.html), Eric and [Adamo-Villani](https://www.interaction-design.org/references/authors/nicoletta_adamo-villani.html), Nicoletta (2010): *A Study of the Effects of Immersion on Short-term Spatial Memory*. In [Virtual Reality](https://www.interaction-design.org/references/periodicals/virtual_reality.html), 71 pp. 1-44

[Kallay](https://www.interaction-design.org/references/authors/william_kallay.html), William (2011): *The Making of Tron: How Tron Changed Visual Effects and Disney Forever.* William Kallay
[Kelly](https://www.interaction-design.org/references/authors/michael_kelly.html), Michael (ed.) (1998): *Encyclopedia of Aesthetics.* Oxford University Press, USA
[Kelly](https://www.interaction-design.org/references/authors/michael_kelly.html), Michael, [Vesna](https://www.interaction-design.org/references/authors/victoria_vesna.html), Victoria, [Fishwick](https://www.interaction-design.org/references/authors/paul_a__fishwick.html), Paul A., [Moere](https://www.interaction-design.org/references/authors/andrew_vande_moere.html), Andrew Vande and [Huff](https://www.interaction-design.org/references/authors/kenneth_huff.html), Kenneth (2009): The state of aesthetic computing or info-aesthetics: curated panel discussion. In: [ACM SIGGRAPH 2009 Art Gallery](https://www.interaction-design.org/references/conferences/acm_siggraph_2009_art_gallery.html) 2009. pp. 43-
[Kivy](https://www.interaction-design.org/references/authors/peter_kivy.html), Peter (ed.) (2004): *The Blackwell Guide to Aesthetics.* Wiley-Blackwell
[Knuth](https://www.interaction-design.org/references/authors/donald_e__knuth.html), Donald E. (1992): *Literate Programming.* Center for the Study of Language and Information

[Lakoff](https://www.interaction-design.org/references/authors/george_lakoff.html), George and [Johnson](https://www.interaction-design.org/references/authors/mark_johnson.html), Mark (2003): *Metaphors We Live By, 2nd edition.* University of Chicago Press
[Lakoff](https://www.interaction-design.org/references/authors/george_lakoff.html), George and [Johnson](https://www.interaction-design.org/references/authors/mark_johnson.html), Mark (1983): *Metaphors We Live by.* New York, Basic Books
[Lakoff](https://www.interaction-design.org/references/authors/george_lakoff.html), George and [Johnson](https://www.interaction-design.org/references/authors/mark_johnson.html), Mark (1999): *Philosophy in the Flesh: The Embodied Mind and Its Challenge to Western Thought.* New York, Basic Books
[Lakoff](https://www.interaction-design.org/references/authors/george_lakoff.html), George and [Nunez](https://www.interaction-design.org/references/authors/rafael_nunez.html), Rafael (2001): *Where Mathematics Comes From: How the Embodied Mind Brings Mathematics into Being.* Basic Books
[Laurel](https://www.interaction-design.org/references/authors/brenda_k__laurel.html), Brenda K. (1991): *Computers as Theatre.* Reading, MA, Addison-Wesley Publishing

[Lave](https://www.interaction-design.org/references/authors/jean_lave.html), Jean and [Wenger](https://www.interaction-design.org/references/authors/etienne_wenger.html), Etienne (1991): *Situated Learning: Legitimate Peripheral Participation (Learning in Doing: Social, Cognitive and Computational Perspectives).* Cambridge University Press
[Lessig](https://www.interaction-design.org/references/authors/lawrence_lessig.html), Lawrence (2008): *Remix: Making Art and Commerce Thrive in the Hybrid Economy.* Penguin Press HC, The
[Leymarie](https://www.interaction-design.org/references/authors/frederic_fol_leymarie.html), Frederic Fol (2006): Aesthetic Computing and Shape. In: [Fishwick](https://www.interaction-design.org/references/authors/paul_a__fishwick.html), Paul A. (ed.). "Aesthetic Computing". The MIT Presspp. 258-288
[Lowgren](https://www.interaction-design.org/references/authors/jonas_lowgren.html), Jonas (2008). *Interaction Design - brief intro*. Retrieved 4 November 2013 from [URL to be defined - in press]
[Malina](https://www.interaction-design.org/references/authors/roger_malina.html), Roger (2011). *The Strong Case for Art-Science Interaction*. Retrieved 19 March 2012 from thoughtmesh: [http://vectors.usc.edu/thoughtmesh/publish/120.php](http://vectors.usc.edu/thoughtmesh/publish/120.php)
[Manovich](https://www.interaction-design.org/references/authors/lev_manovich.html), Lev (2001): *The Language of New Media.* The MIT Press

[Mar](https://www.interaction-design.org/references/authors/raymond_a__mar.html), Raymond A. and [Oatley](https://www.interaction-design.org/references/authors/keith_oatley.html), Keith (2008): *The Function of Fiction is the Abstraction and Simulation of Social Experience*. In [Perspectives on Psychological Science](https://www.interaction-design.org/references/periodicals/perspectives_on_psychological_science.html), 3 (3) pp. 173-192
[Marino](https://www.interaction-design.org/references/authors/mark_c__marino.html), Mark C. (2006). *Critical Code Studies*. Retrieved 18 April 2012 from Electronic Book Review: [http://www.electronicbookreview.com/thread/electro...](http://www.electronicbookreview.com/thread/electropoetics/codology)
[McLuhan](https://www.interaction-design.org/references/authors/marshall_mcluhan.html), Marshall (1964): *Understanding Media: The Extensions of Man.* The MIT Press
[Mohr](https://www.interaction-design.org/references/authors/manfred_mohr.html), Manfred (2011). *Réflexions Sur Une Ésthetique Programmée*. Retrieved 18 March 2012 from Bitforms Gallery, New York: [http://www.bitforms.com/press-releases/405-2011-ma...](http://www.bitforms.com/press-releases/405-2011-manfred-mohr.html)

[Nake](https://www.interaction-design.org/references/authors/frieder_nake.html), Frieder (2009): *The semiotic engine: notes on the history of algorithmic images in Europe*. In [Art Journal](https://www.interaction-design.org/references/periodicals/art_journal.html), pp. 76-89
[Negroponte](https://www.interaction-design.org/references/authors/nicholas_negroponte.html), Nicholas (1996): *Being Digital.* Vintage
[Norman](https://www.interaction-design.org/references/authors/donald_a__norman.html), Donald A. (2004): [*Emotional Design*](https://www.interaction-design.org/literature/topics/emotional-design)*: Why We Love (Or Hate) Everyday Things.* Basic Books
[Papert](https://www.interaction-design.org/references/authors/seymour_papert.html), Seymour (1980): *Mindstorms: Children, Computers and Powerful Ideas.* New York, Basic Books
[Parsons](https://www.interaction-design.org/references/authors/thomas_d_parsons.html), Thomas D and [Rizzo](https://www.interaction-design.org/references/authors/albert_a_rizzo.html), Albert A (2008): *Initial
 validation of a virtual environment for assessment of memory 
functioning: virtual reality cognitive performance assessment test*. In [CyberPsychology and Behavior](https://www.interaction-design.org/references/periodicals/cyberpsychology_and_behavior.html), 11 (1) pp. 17-25

[Petre](https://www.interaction-design.org/references/authors/marian_petre.html), Marian and [Blackwell](https://www.interaction-design.org/references/authors/alan_blackwell.html), Alan (1999): *Mental Imagery in Program Design and Visual Programming*. In[International Journal of Human-Computer Studies](https://www.interaction-design.org/references/periodicals/international_journal_of_human-computer_studies.html), 51 (1) pp. 7-30
[Piaget](https://www.interaction-design.org/references/authors/jean_piaget.html), Jean (1950): *The Psychology of Intelligence.* Routledge
[Pine](https://www.interaction-design.org/references/authors/b__joseph_pine.html), B. Joseph (1999): *The Experience Economy: Work Is Theater & Every Business a Stage.* Harvard Business Press
[Pine](https://www.interaction-design.org/references/authors/b__joseph_pine.html), B. Joseph and [Davis](https://www.interaction-design.org/references/authors/stan_davis.html), Stan (eds.) (1999): *Mass Customization: The New Frontier in Business Competition.*Harvard Business School Press
[Reas](https://www.interaction-design.org/references/authors/casey_reas.html), Casey and [Fry](https://www.interaction-design.org/references/authors/ben_fry.html), Ben (eds.) (2007): *Processing: A Programming Handbook for Visual Designers and Artists.*The MIT Press
[Ritchie](https://www.interaction-design.org/references/authors/andrew_c__ritchie.html), Andrew C. (1968): *English Painters, Hogarth to Constable.* Ayer Co Pub

[Roth](https://www.interaction-design.org/references/authors/tina_roth.html), Tina, [Aiken](https://www.interaction-design.org/references/authors/peter_aiken.html), Peter and [Hobbs](https://www.interaction-design.org/references/authors/scarlette_hobbs.html), Scarlette (1994): *Hypermedia Support for Software Development: A Retrospective Assessment*. In [Hypermedia](https://www.interaction-design.org/references/periodicals/hypermedia.html), 6 (3) pp. 149-173
[Rotman](https://www.interaction-design.org/references/authors/brian_rotman.html), Brian (2000): *Mathematics as Sign: Writing, Imagining, Counting (Writing Science).* Stanford University Press
[Ryder](https://www.interaction-design.org/references/authors/william_ryder.html), William (2009): *A System Dynamics View of the Phillips Machine*. In [Proceedings of the 27th International Conference of the System Dynamics Society](https://www.interaction-design.org/references/periodicals/proceedings_of_the_27th_international_conference_of_the_system_dynamics_society.html),
[Salomon](https://www.interaction-design.org/references/authors/gavriel_salomon.html), Gavriel (1990): *Cognitive Effects With and Of Computer Technology*. In [Communication Research](https://www.interaction-design.org/references/periodicals/communication_research.html), 17 (1) pp. 26-44

Samuel P. Harn Museum of Art (2011). *Art in Engineering. Museum Nights at the Harn Museum of Art*. Retrieved 19 April 2012 from Samuel P. Harn Museum of Art: [http://www.harn.ufl.edu/octmuseumnight.pdf](http://www.harn.ufl.edu/octmuseumnight.pdf)
[Scruton](https://www.interaction-design.org/references/authors/roger_scruton.html), Roger (2011): *Beauty: A Very Short Introduction.* Oxford University Press
[Sfard](https://www.interaction-design.org/references/authors/anna_sfard.html), Anna (1994): *Reification as the birth of metaphor*. In [For the Learning of Mathematics](https://www.interaction-design.org/references/periodicals/for_the_learning_of_mathematics.html), 14 (1) pp. 44-55
[Sfard](https://www.interaction-design.org/references/authors/anna_sfard.html), Anna and [Thompson](https://www.interaction-design.org/references/authors/patrick_w__thompson.html), Patrick W. (1994): *Problems of reification: Representations and mathematical objects*. In [Proceedings
 of the Annual Meeting of the International Group for the Psychology of 
Mathematics Education North America Plenary Sessions](https://www.interaction-design.org/references/periodicals/proceedings_of_the_annual_meeting_of_the_international_group_for_the_psychology_of_mathematics_education_north_america_plenary_sessions.html), 1

[Sherman](https://www.interaction-design.org/references/authors/william_r__sherman.html), William R. and [Craig](https://www.interaction-design.org/references/authors/alan_b__craig.html), Alan B. (2002): *Understanding Virtual Reality: Interface, Application, and Design (The Morgan Kaufmann Series in Computer Graphics).* Morgan Kaufmann
[Slingerland](https://www.interaction-design.org/references/authors/edward_slingerland.html), Edward (2008): *What Science Offers the Humanities: Integrating Body and Culture (New Approaches to European His).* Cambridge University Press
[Speer](https://www.interaction-design.org/references/authors/nicole_k__speer.html), Nicole K., [Zacks](https://www.interaction-design.org/references/authors/jeffrey_m__zacks.html), Jeffrey M. and [Reynolds](https://www.interaction-design.org/references/authors/jeremy_r__reynolds.html), Jeremy R. (2007): *Human brain activity time-locked to narrative event boundaries*. In [Psychological Science](https://www.interaction-design.org/references/periodicals/psychological_science.html), 18 (5) pp. 449-455

[Stasko](https://www.interaction-design.org/references/authors/john_t__stasko.html), John T., [Domingue](https://www.interaction-design.org/references/authors/john_b__domingue.html), John B., [Brown](https://www.interaction-design.org/references/authors/marc_h__brown.html), Marc H. and [Price](https://www.interaction-design.org/references/authors/blaine_a__price.html), Blaine A. (eds.) (1998): *Software Visualization.* The MIT Press
[Swade](https://www.interaction-design.org/references/authors/doron_swade.html), Doron (2000): The Phillips Machine and the history of computing. In: [Leeson](https://www.interaction-design.org/references/authors/robert_leeson.html), Robert (ed.). "A. W. H. Phillips: Collected Works in Contemporary Perspective". Cambridge University Presspp. 120-126
[Thompson](https://www.interaction-design.org/references/authors/patrick_w__thompson.html), Patrick W. and [Sfard](https://www.interaction-design.org/references/authors/anna_sfard.html), Anna (1994): Problems of reification: Representation and Mathematical objects. In:[Proceedings of the Annual Meeting of the International Group for the Psychology of Mathematics Education - North America](https://www.interaction-design.org/references/conferences/proceedings_of_the_annual_meeting_of_the_international_group_for_the_psychology_of_mathematics_education_-_north_america.html) 1994, Baton Rouge, USA.

[Tractinsky](https://www.interaction-design.org/references/authors/noam_tractinsky.html), Noam, [Katz](https://www.interaction-design.org/references/authors/a__s__katz.html), A. S. and [Ikar](https://www.interaction-design.org/references/authors/d__ikar.html), D. (2000): *What is Beautiful is Usable*. In [Interacting with Computers](https://www.interaction-design.org/references/periodicals/interacting_with_computers.html), 13 (2) pp. 127-145
[Tufte](https://www.interaction-design.org/references/authors/edward_r__tufte.html), Edward R. (1983): *The Visual Display of *[*Quantitative*](https://www.interaction-design.org/literature/topics/quantitative-research)* Information.* Cheshire, CT, Graphics Press
[Turkle](https://www.interaction-design.org/references/authors/sherry_turkle.html), Sherry (2004): *How Computers Change the Way We Think*. In [Higher Education](https://www.interaction-design.org/references/periodicals/higher_education.html), 50 (21)
[Varela](https://www.interaction-design.org/references/authors/francisco_j__varela.html), Francisco J., [Thompson](https://www.interaction-design.org/references/authors/evan_thompson.html), Evan and [Rosch](https://www.interaction-design.org/references/authors/eleanor_rosch.html), Eleanor (1991): *The Embodied Mind: Cognitive Science and Human Experience.* Cambridge, Massachusetts, MIT Press

[Viégas](https://www.interaction-design.org/references/authors/fernanda_b__vi%E9gas.html), Fernanda B., [Wattenberg](https://www.interaction-design.org/references/authors/martin_wattenberg.html), Martin, [Ham](https://www.interaction-design.org/references/authors/frank_van_ham.html), Frank van, [Kriss](https://www.interaction-design.org/references/authors/jesse_kriss.html), Jesse and [McKeon](https://www.interaction-design.org/references/authors/matt_mckeon.html), Matt (2007): *ManyEyes: a Site for Visualization at Internet Scale*. In [IEEE Transactions on Visualization and Computer Graphics](https://www.interaction-design.org/references/periodicals/ieee_transactions_on_visualization_and_computer_graphics.html), 13 (6) pp. 1121-1128
[Ward](https://www.interaction-design.org/references/authors/matthew_o__ward.html), Matthew O., [Grinstein](https://www.interaction-design.org/references/authors/georges_grinstein.html), Georges and [Keim](https://www.interaction-design.org/references/authors/daniel_keim.html), Daniel (2010): *Interactive *[*Data Visualization*](https://www.interaction-design.org/literature/topics/data-visualization)*: Foundations, Techniques, and Applications.* A K Peters Ltd
[Wing](https://www.interaction-design.org/references/authors/jeannette_m__wing.html), Jeannette M. (2006): *Computational thinking*. In [Communications of the ACM](https://www.interaction-design.org/references/periodicals/communications_of_the_acm.html), 49 (3) pp. 33-35

[Yates](https://www.interaction-design.org/references/authors/frances_a__yates.html), Frances A. (1966): *The Art of Memory.* University of Chicago Press
[Zhang](https://www.interaction-design.org/references/authors/kang_zhang.html), Kang (2007): *Visual Languages and Applications.* Springer
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

加入 **314,536 位设计师** 的行列，通过我们的时事通讯（Newsletter）获取实用的 UX 技巧。
需要提供有效的电子邮件地址。

# 26.16 Michael Kelly 的评论

**“**信息的掌控者们已经忘记了诗歌，在诗歌中，词语的含义可能与词典所载截然不同，隐喻的火花总是领先于解码功能（Decoding Function）一步。**”**
- - J. M. Coetzee, *Diary of a Bad Year* [1]

## 26.16.1 Fishwick 关于审美计算的百科全书条目

Paul Fishwick 在佛罗里达大学（University of Florida）拥有一个成熟且令人印象深刻的研究与教学平台，他一直以此为基础探索审美计算（Aesthetic Computing）的某个特定版本；不过，由于他从该领域创立之初就参与其中，他对整个领域也拥有全局性的认识。事实上，如果没有他，这个领域几乎不会存在。我想探讨的问题是，他的具体项目在多大程度上影响了他对审美计算的总体构想，以及他是否在此达到了某种恰当的（尽管很难实现的）编辑平衡 [2]。

Fishwick 从教学视角切入：他在数学方面的个人经历引导他发现了具身认知（Embodied Cognition）并对其进行了探索。具体而言，他利用具身知识（Embodied Knowledge）的概念分析了“向形式语言（Formal Language）的审美转换”。这里的具身知识被理解为一种感知-动作反馈循环（Perception-action Feedback Loop），其基础观点是：具身化本身就是一种表征（Representation）形式，而不仅仅是严格认知模式表征过程中一个无关紧要的步骤。基于此，他通过一系列丰富的项目论证道：“审美计算的目的是利用审美产品作为媒介，来传递形式语言的知识与实践。”简而言之，那些引导 Fishwick 进入审美计算领域的抽象数学概念教学案例，在其整个……中一直扮演着结构性和主题性的角色。

……条目，并在很大程度上决定了他对该领域的认知。结果是，他呈现了一幅关于美学计算（Aesthetic Computing）的极佳但片面的图景，如果将其视为整体，将会产生误导。

Fishwick 在“为什么是美学计算？”（Why Aesthetic Computing?）章节（26.4）中承认了美学计算的一种更广泛的定义。但他并未对其进行充分的阐明，也没有具体展示这种定义如何影响或以其他方式与其研究相关联。也许在过去的十年里，他改变了对美学计算的看法？早在 2006 年，他就发表了许多关于美学的论述，这些论述指向的一种美学计算概念比他在百科全书条目中普遍呈现的更为宽泛 (Fishwick 2006)。例如，他提到美学触及了“对称性（Symmetry）和不变性（Invariance）等经典概念之外”的领域，并涵盖了“通常与艺术创作相关的广泛的美学定义和类别”。然而现在，他似乎将美学计算限制在那些通常与他的项目具体相关的经典概念之中。在引用 *Encyclopedia of Aesthetics* 的前言时，他认同将美学视为“对隐含在艺术的创作、体验、解读或评论之中的信念、概念和理论的哲学分析”。然而，当他在百科全书条目中引用同一个观点时，他似乎在回避该观点对美学计算的全部深层含义。Fishwick 此前还提到，美学具有

[它涵盖了]逻辑以及物质层面，因此它可以延伸至计算领域以及艺术领域。以离散数学（discrete mathematics）为例，他声称美学计算（aesthetic computing）涵盖了形式语言（formal language）、几何学（geometry）和拓扑学（topology）的概念，并基于这些主张得出结论：*美学计算与数学形式主义（mathematical formalism）自然地相对应*。在他目前的研究和百科全书条目中，Fishwick 主要关注美学的最后一种含义，并且虽然研究得非常出色，但仅发展了该含义所隐含的较狭隘的美学计算观点。

然而，即便在 Fishwick 自己的项目中，也可以为一种更广泛的美学计算概念提供论据，因为他认为美学计算主要建立在具身性（embodiment）的基础之上，而具身性本身就是美学以及许多学科（如认知心理学 [cognitive psychology]、情感计算 [affective computing]、心灵哲学 [philosophy of mind] 等）中一个非常重要的研究课题。但即便在此，Fishwick 对具身性的理解也主要集中在认知和教学法（pedagogical）层面，因为它主要与形式语言相关联。这种关联似乎是恰当的，因为计算在很大程度上就是关于形式语言的。但美学计算的核心目的，难道不是为了开发并维持一种更丰富的计算概念吗？

事实上，艺术史学家兼理论家 Caroline A. Jones 在构思这种更丰富的概念时，提供了一种更以艺术为中心且基于美学的具身性阐释，其重点在于其影响……

……计算机技术对人体，即“技术-人类（techno-human）”的影响。

[3]. 她首先主张，使对我们技术文化（techno-culture）的批判能够跟上“技术创新的速度”的最佳方式，是“将这些技术用于美学服务”，这为质疑我们的“身体在当下如何与技术进行交互”提供了一个“场所”。美学为这种批判提供了沉思空间，因为它为我们“争取了时间和空间”，去接触并反思“在一个日益技术化的世界中的具身经验（embodied experience）”。也就是说，美学在计算内部建立了一种批判机制，用以考察人机交互（human-computer interactions）如何影响我们的身体。这种批判的目标不仅在于理解所有已经经历过的由计算机生成的身体交互，更在于探索哪些交互是可能被经历的，以及在未来我们更倾向于经历哪些交互。最终，Jones 对具身性（embodiment）阐述的一个主要优势在于，她明确了这种计算内部的批判性思维其实已经有一个具有悠久传统的名称：美学（aesthetics）。通过将具身性、计算与美学之间的联系显性化，她为计算以及美学计算（aesthetic computing）都提供了更广泛的构想。

Jones 对具身性的阐述由参与 *Sensorium* 展览或目录的众多艺术家和理论家共同探讨，这也与……的美学契合。

近期在当代艺术中发展的参与式艺术（Participatory Art）实践，也将有助于拓展审美计算（Aesthetic Computing）[4]。简而言之，参与式艺术是出现于前卫现代主义（Avant-garde Modernism）或当代艺术中的多种艺术形式的融合：包括交互艺术（Interactive Art）、装置艺术（Installation Art）、行为艺术（Performance Art）、观念艺术（Conceptual Art）、新媒体艺术（New Media Art）、公共艺术（Public Art）、社会参与艺术（Socially Engaged Art）等。这种融合改变了当代艺术的审美方式（例如：能动性（Agency）是集体的，形式是参与式的，交互是具有变革性的），而随着计算变得日益无处不在（Ubiquitous）、参与式、协作式、社交化且交互化，这些变化在计算领域也产生了共鸣。由于审美计算的一个核心关注点是审美与计算之间的相关性，因此探讨当代艺术审美的最新进展将有助于推动这一目标。这并不意味着古典艺术或现代艺术的审美无关紧要，但由于参与式艺术的出现部分源于计算对当代艺术创作（Production）与接收（Reception）已经产生的影响，因此在发展审美计算的同时，参与式艺术是一个极佳的探索领域。

除了编辑上的不平衡外，我对 Fishwick 在 Encyclopedia 条目中的另一个主要担忧是，他将审美主要视为一种手段（“一个载体（Vehicle）”）：“审美计算是一种具身形式语言（Embodied Formal Language），其最终目标是教育目标……

“产品”。因此，美学的批判性思考核心（critical thinking core of aesthetics）似乎丢失了。例如，尽管 Fishwick 在 26.7 中确定了一些他自己的美学规范（aesthetic norms）（其中仅有部分在我看来具有美学意义）以及他对美学的假设（例如，主要关注点仍然是“美的普遍属性 [universal attributes of beauty]”），但他并未对其进行批判性分析 [5]。例如，他所支持的“多样性中的统一（unity in variety）”概念是 18 世纪英国美学（由 Francis Hutcheson 等人发展）中的一种策略，旨在识别出对象的某种属性以解释其美感，同时又不违背经验主义者（empiricists）和理性主义者（rationalists）共同认可的原则，即美本身并非任何对象的属性。这样的概念或策略如何能帮助阐明计算的“多样性”，或者如何在美学的概念本质与计算的经验实践（empirical practices）之间进行协调？此外，正如 Jones 所主张的，美学还可以通过阐明和批判其美学及相关规范来帮助确定计算的目的（ends），因此不应将其主要视为在引入美学计算（aesthetic computing）之前就已确定之目的的实现手段。

公平地说，即使 Fishwick 处理美学计算的方法如我所述那样狭隘，该领域可能首先需要通过特定的（因此也是狭隘的）项目来发展。也许只有那样，我们才能在广义的美学领域之间启动一种反思平衡（reflective equilibrium）

计算以及 Fishwick 等人所从事的各种具体且多样化的项目。尽管我认为一般性（general）与特殊性（particular）必须从一开始就同步发展，但 Fishwick 在这部百科全书及其研究中，显然为美学计算（aesthetic computing）做出了重要贡献。

基于同样的反思平衡（reflective equilibrium），我现在想阐明我对美学计算更广泛概念的理解，因为我在评述 Fishwick [6] 时诉诸了这一概念。

## 26.16.2 计算美学（Aesthetics in Computing）

John Maeda（计算机科学家、设计师，以及 Rhode Island School of Design 的校长）曾创作过“Palm Paintings”：这些是采用各种抽象风格绘制的小型浅盒，每个盒子中心都内置了一台 Palm 电脑作为其可见的中心。他所陈述的目的，是让我们能够从内部“思考”这幅画作“意味着什么（signified）”。我认为，他的观点并不一定是说意义（signification）在物质上位于艺术品内部，而更具挑衅性地指出，如果我们希望批判性思考（critical thinking）真正地处于作品内部，而非仅仅在事后作为补充而添加，那么我们对作品的批判性思考应当在作品创作的过程中同步进行。此处的批判性思考模式即为美学（aesthetics），因为艺术中的关键规范性问题（normative issues）是美学问题，这使得美学成为了（Maeda）绘画中不可或缺的一部分。

采取一种互惠的姿态，现在请想象我们将美学嵌入到所有与计算机相关的人工制品（artifacts）的设计与生产中——包括数据库、程序、网络、数据可视化、游戏等 [7]。其目的同样是为了思考这些制品意味着什么，并且前瞻性地思考在未来我们希望它们意味着什么（以及除了意义之外，我们还希望看到什么样的其他效果）。这些嵌入了美学的计算人工制品可以通过某种方式进行标记，以将它们与

我们可以希望从内部了解普适计算（Ubiquitous Computing），在它被开发的过程中就进行了解，而不仅仅是在它已经被社会大众使用时。

这种互惠的姿态并非凭空想象，因为正如 Fishwick 所证实的，计算的许多领域已经出现了一种“审美转向（Aesthetic Turn）”，从而引入了诸如审美计算（Aesthetic Computing）、计算美学（Computational Aesthetics）、数据库美学（Database Aesthetics）、数字美学（Digital Aesthetics）、信息美学（Information Aesthetics）、网络美学（Network Aesthetics）或软件研究（Software Studies）等新子领域 [8]。这些由计算机科学家及其他人员（如艺术家、哲学家、艺术史学家）组成的协作研究团队所提出的多样化名称，其区别在于美学是在何处，或者按照 Nelson Goodman 的观点，是在*何时*被引入计算的 [9]。也就是说，如果我们考虑计算机栈（Computer Stack）——即计算的各个层级（底层是比特和硬件，顶层是用户交互）——那么这里名称的选择取决于审美规范（Aesthetic Norms）首次进入计算的时间点。例如，如果审美规范参与到数据库的构建中，那么我们就有了数据库美学；如果它们影响我们如何赋予信息形式，那么我们就有了信息美学；如果它们是组织参与各种社交媒体的人员网络的一部分，那么我们就有了网络美学——以此类推，涵盖在计算机栈的各个层级之中。审美规范所处的层级越低...

这些规范越是隐性存在，对其进行的批判在计算的高层（higher layers of computing）中产生的涟漪效应（ripple effect）就越大 [10]。

从这个角度来看，在所有选项中，“审美计算（aesthetic computing）”这个名称在原则上涵盖了整个计算栈（computing stack），因此最能捕捉到计算领域中“审美转向（aesthetic turn）”的全部广度与深度。在进一步探讨美学为计算带来了什么时，我想强调的是，审美计算不仅仅关乎计算*之*美学（aesthetics *of* computing）（即仅仅是程序或产品的设计，或者仅仅是对计算审美规范的外部批判）。借鉴 Maede 的 “Palm Paintings”，我所设想的是计算*中*的美学（aesthetics *in* computing），尽管这种视角会前瞻性地关注其伦理和社会政治影响，而不仅仅是其内部结构（即，不仅仅是计算美学 [computational aesthetics]）。

## 26.16.3 什么是美学计算（Aesthetic Computing）？

美学（Aesthetics）是对引导或产生于艺术、文化或自然之生产、体验或接收的规范、概念、价值或原则的批判性思考。 “计算（Computing）”一词（与“计算机科学”不同）除了指代与计算机编程、数据库、计算、软件、操作系统和硬件（从数字到设备的所有一切）相关的理论和实践范围外，还体现了这样一种认知，即计算机科学是在一个广泛的社会（道德-政治）语境中运行的。美学计算（Aesthetic computing）是将这一认知操作化（operationalize）的一种首选方式，因为它是对塑造计算所有层级的复杂规范集进行批判性思考，而这些规范反过来又在塑造这一道德-政治-社会语境 [11]。

尽管美学计算有各种不同的名称，但在其所有版本或迭代中都有一条共同的主线。这条主线是计算领域从业者的共识，即在计算所有层级所做的决策或判断中，都隐含着美学规范（aesthetic norms）。因此，美学计算的主要任务是：（1）识别计算领域中在很大程度上处于隐性状态的美学规范的谱系（genealogy）和现状，并使其显性化；（2）审视这些美学规范对用户产生的道德-政治-社会影响并对其进行批判；（3）帮助在……中做出决策或判断。

在考虑到 (1) 和 (2)，以及计算领域内部的技术规范（technical norms）的情况下，未来的问题在于计算领域中哪些审美规范（aesthetic norms）应当被放弃、修订或维持。

通过审视 Zadie Smith 对 David Fincher 的电影 *The Social Network* 以及 Jaron Lanier 的著作 *You Are Not A Gadget: A Manifesto* [12] 的评论，我们可以更清晰地认识到审美计算（aesthetic computing）的必要性及其任务。根据 Smith 的分析，这部电影和这本书的共同点在于它们都主张：“不同的软件嵌入了不同的哲学，而这些哲学在变得普及的同时，也变得不可见。”软件不仅不是中立的，而且其中嵌入了重要的规范（例如：人格 [personhood]、隐私 [privacy]、社交性 [sociality]），而且在使用过程中，软件还会执行（enacts）这些规范（即将其付诸实践）。然而，软件不仅仅是复制我们关于自身和世界的现有规范，它还执行新的规范，并在此过程中构建一个世界。在 Smith 看来，问题在于这些隐形嵌入且被执行的规范在事前并未经过批判性的讨论；相反，它们是由程序员直接嵌入并执行的。在 Facebook 的案例中这一点尤为突出，因为 8 亿多用户对其规范几乎没有发言权。Smith 正确地指出，这种情况涉及伦理问题：为什么是这些规范而不是其他规范？为什么采用这种连接人们的方式而不是另一种方式？这种连接的质量如何？为什么是这种

隐私政策（privacy policy）？例如，用户被期望在很大程度上放弃其隐私，而且他们似乎是心甘情愿地这样做，尽管根据 Lanier 的观点，他们是在通过自我简化（reducing themselves）以适应所使用的软件，以至于他们的“生活变成了数据库”。

Smith 的分析与审美计算（Aesthetic Computing）相关，不仅是因为她指出了管理 Facebook、互联网或 Web 的规范的*不可见性（invisibility）*，还因为当她对这些规范展开批判时，她经常提到它们的“外观（look）”或“感觉（feel）”。例如，虽然我们“知道”认为计算机可以拟人化（personify）人类关系是一个错误，但我们仅是通过“感受”这种错误信念所带来的情感后果（affective consequences）才能直觉地意识到这一点，而 Facebook 正是这种信念的体现：“我们知道拥有两千个 Facebook 好友并不是[友谊]应有的样子。”我们所感受到的这种“样子”究竟是什么，又是它让我们反过来意识到 Facebook 中嵌入并执行（embedded and enacted）的某些规范可能存在问题？我们通过其底层规范的不可见性，逐渐意识到 Facebook *正在*对我们做某些事情；而如果我们持续的批判性反思（critical reflection）取得成功，我们将了解到 Facebook *具体在*对我们做什么，以及是否存在任何替代方案。为了成功，我们需要将 Facebook 中运行的不可见规范可视化（render visible），这样当我们有时感到“对他们[在 Facebook 中]所创造的世界感到不安”时，我们就有了“充分的理由”。这种类型的

批判性思维（Critical Thinking）正是审美计算（Aesthetic Computing）所提供的，因为其主要任务之一就是将计算的隐含规范（Implicit Norms）显性化。

但让我回到这个问题：为什么是审美学（Aesthetics）？我们首先可能会问，为什么是哲学（Philosophy）？Smith 通过强调“令人失望的是 Facebook 的*理念*（Idea）”，而不仅仅是其理念的实现，来回答第二个问题。为了分析其理念，我们需要哲学来对抗她所观察到的英美世界的一种普遍文化倾向，即“在技术上快步疾行，并希望理念能够自行解决”。我们需要审视 Facebook 的理念以及在 Web 和互联网上实施的所有其他理念，以免像 Lanier 所说的那样，我们被其“锁定（Locked in）”，或“被困在他人粗心的思考之中”。这意味着我们被锁定在塑造这些理念的不可见规范之中，而一旦这些规范在 Web 或互联网上得以实施，它们就会塑造我们的世界以及我们自身。但为什么特别要转向审美学来审视这些涉及伦理（Ethics，例如安全性）、形而上学（Metaphysics，例如人格 Personhood 或虚拟现实 Virtual Reality）等方面的理念呢？回到 Smith 对 Facebook “外观（Look）”的讨论，并回顾 Jones 对具身性（Embodiment）的阐述，我们最接近体验 Web 或互联网软件中所实施的不可见规范的方式，就是体验这些规范给作为用户的我们所带来的情感影响（Affects）。其中许多情感影响是可见的，但它们涉及所有的

感官（听觉，以及日益重要的触觉），正如艺术作品以及我们日常生活的审美体验所做的那样。美学（Aesthetics）将我们计算体验中的情感维度（affective dimensions）凸显出来，并且其方式为 Smith, Jones 和 Lanier 所探讨的那类批判提供了基础。这些批判正是审美计算（aesthetic computing）在实践中的例证。

为了举另一个显然属于计算领域内部的例子，人机交互（Human-Computer Interaction, HCI）领域出现了一次“审美转向（aesthetic turn）”，因为一些研究人员认为，随着计算机界面变得更具交互性、参与性、沉浸性和泛在性（ubiquitous）[13]，获得一个关于“用户”更全面的认识至关重要。简而言之，他们需要从情感、道德、政治以及认知维度来理解用户，从而反过来创建正确的（即有效的、可用的）界面。因此，随着可用性（usability）的概念在规范性上变得更加复杂，美学也随之进入了视野。为什么要转向美学？一个主要原因是，美学在批判构成我们艺术体验的特定情感与认知交互以及参与模式方面有着悠久的历史，而这些批判与人机交互中用户情感-认知体验的批判具有相关性 [14]。这些交互（及其特有的参与模式）同样具有道德和

政治维度，因为用户必须被公平对待（例如，在获取机会（access）方面，无论是出于经济还是残疾原因），且其政治或文化信仰必须得到尊重。同样，美学在历史上一直将艺术作品的评判与道德-政治以及美学考量联系在一起。因此，无论是在人机交互（HCI）还是任何其他计算领域，这里的“美学转向（aesthetic turn）”并非将道德-政治-社会的社会影响缩小为单纯的美学问题；相反，美学为批判性地思考那些同时兼具道德、政治、社会和美学属性的规范（norms）提供了一个哲学结构 [15]。

## 26.16.4 审美计算与科学（Aesthetic Computing and Science）

虽然针对计算领域中审美规范（aesthetic norms）及其道德-政治-社会影响的批判是一个相对较新的过程，但如果我们将其视为对计算领域现有批判性思维（critical thinking）实践的一种扩展 [16]，就能更容易地体会其相关性和重要性。也就是说，计算领域一直对其规范性（normativity）进行批判性分析，尽管这些规范大多是在技术层面（例如，什么是最高效或最有效的）被理解的。审美计算（aesthetic computing）的出现，源于计算领域内部的一种认识，即其规范不仅仅是技术性的，正如我们在人机交互（HCI）的案例中所见。因此，审美计算在本质上是对计算领域中一直存在且起作用的复杂规范性的认识之延伸与精炼。强调这一点至关重要，因为一些计算机科学家看待美学的方式，可能就像他们看待伦理、政治或其他看似与计算无关的问题一样：这些问题与他们作为（qua）科学家的工作（基于其方法论、目标等）无关，因此，赋予这些问题方法论上的可信度（methodological credibility）只会给科学研究带来限制。然而，如果美学（以及相关的规范性）问题被理解为源自计算内部，那么科学家们就不再需要担心美学在限制计算的发展。

然而，研究人员可能仍然担心审美计算会改变

……以某种方式使计算机科学变得不那么具有科学性，特别是如果 Roger Molina 的观点是正确的，即审美计算（aesthetic computing）的强主张是它将产生一些“不会在计算科学内部自然演化而出”的新目标，并且，将“重新引导计算的未来发展”[17]。也就是说，计算栈（computing stack）各层中审美规范从隐式（implicit）到显式（explicit）的转变，其结果可能是我们将改变技术规范以及审美规范，并在此基础上改变计算的目标。但同样地，如果计算具有规范性（normative），且对规范性的自我批判（self-critique）是科学的一部分，那么审美计算带来的唯一实质性变化，就是那些始终已经是计算一部分的审美规范现在将变得显式化并受到批判性审视。计算怎么可能不会从更多的自我批判中获益呢？因为根据现代科学自身的逻辑，对其内部规范的修订正是推动其进步的引擎的一部分。例如，随着计算更加意识到有助于环境可持续性（environmental sustainability）的设计问题，这可能会改变计算的某些目标，但并不会使其科学性降低；因为如果它变得不那么具有科学性，它就无法为可持续性做出贡献。简而言之，审美计算表明了那些看似外部的规范实际上是计算内部的。

关于计算作为一种……的地位问题

科学这一概念值得更深入地探讨，因为它能够直接回应并化解关于审美计算（Aesthetic Computing）讨论中的某些僵局。有些人可能仍然担心，审美涉及品味（Taste），因此具有主观性。从这个角度来看，将审美整合到计算之中，就等同于将主观性引入一门原本客观的科学。然而，实际情况是，计算机科学家们正逐渐意识到：(a) 计算的规范复杂性（Normative Complexity）已经塑造了他们对科学的认知，从而为采用更具跨学科性（Interdisciplinary）的计算方法创造了空间；(b) 计算不仅仅是一门科学，这不仅是因为计算在道德、政治和社会方面的影响涉及过多非技术性问题，而科学家为了推动计算的内部发展必须理解这些问题；而且还因为计算中隐含的非技术规范（Nontechnical Norms）已经在潜移默化地塑造其发展，为了计算本身，以及为了我们这些在计算机环境下生活和工作的人，这些规范需要被进行批判性的分析 [18]。简而言之，计算领域的“审美转向”（Aesthetic Turn）是通过批判其非技术规范，从而在当前的发展阶段强化其作为科学的地位。为什么选择审美？同样是因为审美作为哲学领域的一个长期分支，已经发展出多种方法，能够批判性地思考审美规范及其与道德、政治、社会以及技术规范之间的关系。

## 26.16.5 开放的审美属性与对象（Open Aesthetic Properties and Objects）

那么，如果审美规范（aesthetic norms）一直以来就是计算的一部分，为什么审美计算（aesthetic computing）至今仅有十年左右的历史，而美学（aesthetics）起源于 18 世纪，计算机也已经存在数十年了？根据 Fishwick 的解释，计算必须发展到一定阶段，其与美学的联系才能清晰地显现：“我们必须等待技术成熟，以便利用艺术，”特别是在人机交互（HCI）、普适计算（ubiquitous computing）、增强现实（augmented reality）和虚拟现实（virtual reality）等领域 [19]。然而，如果美学与计算的关系如此明显，为什么这种延迟是必要的？毕竟，美学是批判性思维（critical thinking）的一种形式，而计算的演进一直依赖于批判性思维，那么为什么审美计算没有更早地出现？除了担心科学会受到限制或变得主观之外，关于其出现缓慢的另一个解释是，计算机科学领域有太多的人对美学的看法相当狭隘，有时甚至过时，因此无法看到美学与计算的相关性；或者，即使他们意识到了这种相关性，也无法从狭隘的观念转向他们希望美学能为计算带来的贡献。

如今，仍有太多人假设（且一些哲学家仍然认为）美学主要关注

……通过对一类被称为艺术品（works of art）的独特且自主对象的内在美质做出无私的判断（disinterested judgments）。然而，美学（aesthetics）并没有一组唯一的对象，这不仅是因为现代艺术史告诉我们，如此多的“事物”都可以成为艺术品，还因为美学在关注对象或事物的同时，同样关注人、经验和价值。并且，美（beauty）不再是美学的核心关注点，因为在艺术中它也不再是核心关注点（原因由其他学者在别处进行了大量分析）[20]。此外，美学关注的并非任何对象的固定属性（fixed properties），无论这些对象是艺术品、自然对象还是计算人工制品（artifacts of computing）。这并不意味着——无论是刻意还是无意地——美学仅仅是主观的，或者像我们有时听到的那样，“美在观者的眼中”。美学并非仅仅是主观的，同样也不是仅仅客观的，因为美（这里不应仅被理解为一种特定的美学属性，而应被视为整套美学属性的代表）既不在于主体，也不在于客体。但是，如果美不是任何主体或客体的固定属性，那么美在哪里？用 18 世纪美学的语言来说，美是一种 *关系属性*（relational property），也就是说，它是一种产生于人类主体之间，或者人类主体与一组开放的艺术品、自然对象或计算人工制品之间的认知与情感关系或交互而形成的属性。

从这个角度来看，美学计算（aesthetic computing）的任务是识别、显性化并批判性地分析使此类关系或交互成为可能的各种条件——包括技术、社会、本体论（ontological）、心理等条件——而不仅仅是研究如何使它们更有效、更可用、更易于沟通或更令人愉悦等，尽管通过理解其可能性，我们大概能更好地解决这些其他问题。由于这里的交互涉及人类，且特别是交互不仅发生在人类与对象之间，还发生在人类*之间*（因此需要将视角从交互转向参与（participation）），这里的美学规范（aesthetic norms）同时也具有道德和政治属性。同样，美学比伦理学或政治学能更好地协调这些规范的所有维度，因为在艺术语境中，美学一直以来就在扮演这样的角色。

基于此，美学是计算的天然盟友，因为计算同样处理缺乏固定属性（fixed properties）的对象，这一点在 Lev Manovich 在 *The Language of New Media* 导论中对“对象（object）”一词的讨论中可见一斑。诸如人工智能（Artificial Intelligence）、虚拟现实（Virtual Reality）、模拟（Simulation）和第二人生（Second Life）等术语，同样涉及基于计算机的、非固定的“现实”和对象。此外，在涉及分子生物学（molecular biology）等领域的科学可视化（scientific visualization）中，那些...

可视化内容对于人类感官而言是不可触及的，因为在分子层面不存在光。因此，这些数据在通常意义上并不构成“对象（objects）”，且其可视化结果没有客观对应物（objective correlates）。这意味着，不存在一种单一且客观的分子数据可视化方式，也不存在一种本质的（essential）可视化方案正等待着计算机科学家去发现（尽管任何可视化都始终受到科学方法论和目标的约束）。此外，这意味着这些“对象”即使在可视化之后仍然是不可见的，因此，认为分子数据的可视化具有固定属性是没有意义的（除非是在数据属性的最广泛意义上——即作为数字和代码而言）。

审视这种对科学可视化（scientific visualization）的描述，从事科学可视化（及其他形式可视化）的计算机科学家应当会对美学（aesthetics）感到亲切，因为分子（及其他）数据与当代艺术作品非常相似：它们同样不（必然）是对象；即使它们采取了感官形式（sensuous form），其本质也更偏向于概念性（conceptual）而非感官性（sensuous）；而且它们并非是对客观现实的模仿，因此无法以此作为评判标准，所以它们可以采取多种形式，仅受限于可视化的限制以及科学（或艺术）的方法论结构和目标。

现在，如果美学计算（aesthetic computing）在关注对象或属性的同时，同样关注人类交互（human interactions），那么这里的一个关键问题是，是什么使得这些

交互的*美学（aesthetic）*属性。我们如何界定人机交互（human-computer interactions）这个开放的范围，并从中分离出那些具有特定美学特性的交互？特别是当“美”并非一个固定属性，而实际上是这些交互产生的结果，而非识别它们的标准时 [21]？在美学计算（aesthetic computing）的情况下，回答这个问题比在更广泛的美学领域中既更容易也更困难；更容易是因为这些交互必须涉及某些计算活动、人工制品（artifacts）或类似事物，而这些在大多数情况下比近年来被证明难以捉摸的“艺术品”更容易识别；但同时也更困难，因为涉及计算机的人机交互中，究竟什么是*美学的*？最后一个问题的答案是：隐式嵌入并执行于计算各层级中的规范（norms）引入了美学维度（因此产生了数据库美学 database aesthetics、信息美学 information aesthetics 等，具体取决于涉及计算栈 computing stack 的哪个层级）。

美学计算的开放性可能会让一些计算机科学家感到困惑，或者至少在我研究、讲座或教授美学计算时的经验是这样的。因为人们倾向于期望美学家能够提供客观的规范（概念、标准或类似之物），从而为计算领域的研究人员提供实践指南（在“评论/批评（criticism）”领域中...）

（计算（computing）有时体现了这种倾向）。然而，如果遵循这一倾向，美学（aesthetics）将变成一个外部于计算的领域，随后被应用于计算之中。与此相反，我提出了一种美学计算（aesthetic computing）模型，该模型仅在计算内部运行，其方式是将计算栈（computing stack）各层中始终隐含且起作用的美学规范（aesthetic norms）显性化。任何新规范都必须从计算实践（computing practices）内部产生，正如新规范在艺术实践（artistic practices）中被引入一样。最终，美学要么是计算内部的，要么与计算几乎没有批判性相关性（critical relevance）。

## 26.16.6 尾注（Endnotes）

1. J. M. Coetzee, *Diary of a Bad Year* (New York: Penguin, 2008)。另见 Jaron Lanier：“信息系统（Information systems）需要有信息才能运行，但信息并不能充分代表现实（underrepresents reality）”——*You Are Not A Gadget: A Manifesto* (New York: Knopf, 2006)。
1. 作为 *Encyclopedia of Aesthetics* (New York: Oxford University Press, 1998) 的编辑，我并非在暗示普遍性（general）应当排除特殊性（particular）——这完全是一个平衡问题。
1. Caroline A. Jones, “Introduction,” 载于 Jones, Ed. *Sensorium: Embodied Experience, Technology, and Contemporary Art* (Cambridge: MIT Press, 2006)。

1. 关于参与式艺术（Participatory Art）的更多讨论，请参阅，例如 Claire Bishop 编著的 *Participation* (London & Cambridge: Whitechapel Gallery MIT Press, 2006)；以及 *Artificial Hells: Participatory Art and the Politics of Spectatorship* (London: Verso, 2012)。Nicolas Bourriaud 的 *Relational Aesthetics* (France: Les Presse Du Reel, 2002)。Rudolf Freiling 编著的 *The Art of Participation: 1950 to Now* (San Francisco & London: San Francisco Museum of Modern Art and Thames & Hudson)。Pablo Helguera 的 *Education for Socially Engaged Art* (New York: Jorge Pinto Books, 2011)。Grant Kester 的 *Conversation Pieces: Community and Communication in Modern Art* (Berkeley: University of California Press, 2004)；以及 *The One and the Many: Contemporary Collaborative Art in a Global Context* (Durham: Duke University Press, 2011)。Nato Thompson 编著的 *Seeing Power: Art and Activism in the Age of Cultural Production* (New York: Melville House, 2012)；以及 *Living as Form: Socially Engaged Art from 1991-2011* (Cambridge: MIT Press, 2012)。

1. 再举一个例子，Lev Manovich 指出，人们经常将目前网络上可见的用户生成内容（User-Generated Content, UGC）（例如动漫音乐视频 [Anime Music Videos]、政治混剪 [Political Mashups]）视为互联网上艺术自由或创造力（甚至是增强的民主 [Enhanced Democracy]）的证据，但他们未能批判性地反思这样一个事实：这些内容实际上遵循着隐式嵌入并执行的行业模板与惯例，或者重复使用了...

专业制作的内容。Manovich, “Art After Web 2.0” 见于 *The Art of Participation: 1950 to Now*。

1. 由于我是一名哲学家，我对这个新领域的看法不可避免地会比较宏观。但这种概括性也源于美学（Aesthetics）是一个概念性和规范性（normative）的领域，尽管如果美学想要作为一种计算内部的批判性思维模式（mode of critical thinking）而具有效力，它显然必须与计算的经验现实（empirical reality of computing）相结合。

1. Mary Flanagan 和 Helen Nissenbaum 提出了“游戏中的价值（values at play）”，这是一种批判性游戏（critical play）的概念，旨在识别并转化计算机（及其他）游戏中嵌入并体现的价值。在我看来，她们的方法是美学计算（aesthetic computing）的一个很好的例子，因为她们将游戏中隐含的规范（implicit norms）显性化了。但她们并没有诉诸美学。事实上，她们似乎在回避美学，这可能是因为 Flanagan 是一位艺术家，似乎不加批判地采用了当代艺术中常见的反美学立场（anti-aesthetic stance），而 Nissenbaum 是一位尚未意识到美学之批判价值的哲学家。我认为这很遗憾，因为美学恰恰提供了 Flanagan 和 Nissenbaum 在分析和创建那些嵌入并体现变革性价值（transformative values）的游戏时，所试图开发的那类概念性和批判性资源。参见 Flanagan, *Critical Play: Radical Game Design* (Cambridge: MIT Press, 2009)；以及 Flanagan and Nissenbaum, *Values at Play* (forthcoming)。

1. 审美计算（Aesthetic Computing）始于 2002 年在德国达格斯图尔（Dagstuhl）举行的一次会议。这次会议促成了一篇于 2003 年发表在 *Leonardo* 上的宣言（manifesto），以及一部由 Paul Fishwick 编辑的文集（anthology）——*Aesthetic Computing* (Cambridge: MIT Press, 2006)（我曾在 2007 年 1 月的 *Leonardo On-line Reviews* 中对其进行过评论：[http://www.leonardo.info/reviews/jan2007/aest_kelly.html](http://www.leonardo.info/reviews/jan2007/aest_kelly.html)）。该领域也被称为（或与……相关联）算法美学（algorithmic aesthetics）或精确美学（exact aesthetics），其渊源可追溯至 20 世纪 30 年代；参见 Gary Greenfield 的 “On

“计算美学（Computational Aesthetics）”这一术语的起源；以及 Florian Hoenig 在 *Computational Aesthetics in Graphics, Visualization and Imaging*（I. Neumann, M. Sbert, B. Gooch, W. Purgathofer 编辑，2005年）第 9-12 页和 13-18 页中撰写的 “Defining Computational Aesthetics”。可追溯至至少 1999 年；参见 Victoria Vesna 编辑的 *Database Aesthetics* (Minneapolis: University of Minnesota Press, 2007)。关于数字美学（Digital Aesthetics）的示例，请参阅 Sean Cubitt 的网站：[http://www.ucl.ac.uk/slade/digita/](http://www.ucl.ac.uk/slade/digita/)；以及 Johanna Drucker 的 *SpecLab: Digital Aesthetics and Projects in Speculative Computing* (Chicago: University of Chicago Press, 2009)。信息美学（Information Aesthetics）拥有一个活跃的网站：[http://infosthetics.com/](http://infosthetics.com/)。另请参阅 2009 年 SIGGRAPH 的信息美学展（Information Aesthetics Showcase）：[http://www.siggraph.org/s2009/galleries_experiences/information_aesthetics/](http://www.siggraph.org/s2009/galleries_experiences/information_aesthetics/)。关于网络美学（Network Aesthetics）的示例，请参阅 Warren Sack 在 *Database Aesthetics* 第 183-210 页中撰写的 “Network Aesthetics”。关于软件美学（Software Aesthetics）的示例，请参阅 Stephan Diehl 和 Carsten Görg 在 Fishwick 的 *Aesthetic Computing* 第 230-37 页中撰写的 “Aesthetics and the Visualization and Quality of Software”。此外，还有许多致力于该主题的网站。同时还有 [此处缺失术语]，在本百科全书的其他部分有详细讨论。

- 计算美学（Computational aesthetics）
- 数据库美学（Database Aesthetics）
- 数字美学（Digital Aesthetics）
- 信息美学（Information Aesthetics）
- 网络美学（Network Aesthetics）
- 软件美学（Software Aesthetics）

视觉美学（Visual Aesthetics）

1. Goodman, “Art in Action,” 载于 *Encyclopedia of Aesthetics*, 第 322-25 页。关于 Goodman 与审美计算（Aesthetic Computing）之相关性的论述，请参阅 John Lee, “Goodman’s Aesthetics and the Language of Computing,” 载于 *Aesthetic Computing*, 第 29-42 页。

1. Manovich 谈到了除计算层（Computing Layer）之外的文化层（Cultural Layer），但我设想的审美计算是将这些层面整合而非分离。参见 *The Language of New Media* (Cambridge: MIT Press, 2001)。

1. 正如 Fishwick 在其百科全书条目中所阐明的，审美计算（Aesthetic Computing）不同于计算机艺术或数字艺术（Digital Art），即数字技术在艺术领域的应用。“审美计算”是指艺术实践和审美原则对计算领域的影响，因此，这种影响是从艺术和审美流向计算。例如，计算机科学家希望向艺术家学习如何对其新技术的原型进行评析（正如艺术家对其新作品所做的那样）；如何在科学、信息或知识可视化中实现最佳的数据可视化；以及如何理解新技术中形式与功能（Form and Function）之间的平衡，或者在计算领域更典型的——美感与可用性（Beauty and Usability）之间的平衡，尤其是涉及用户界面（User Interfaces）的技术。随着这类艺术对计算的影响不断深化，审美（Aesthetics）自然成为了第三方，因为艺术总是涉及某种形式的审美。

1. Zadie Smith, “Generation Why?” (对 David Fincher 导演、Aaron Sorkin 编剧的电影 *The Social Network* 以及 Jaron Lanier 的 *You Are Not a Gadget: A Manifesto* (New York: Knopf, 2010) 的评论)，载于 *New York Review of Books* (2010年11月25日): [http://www.nybooks.com/articles/archives/2010/nov/25/generation-why/?pagination=false](http://www.nybooks.com/articles/archives/2010/nov/25/generation-why/?pagination=false)
1. 参见，例如 Olav W. Bertelsen 和 Søren Pold, “Criticism as an Approach to Interface Aesthetics,” NordiCHI '04, 2004年10月23-27日；Lars Erik Udsen 和 Anker Helms Jørgensen, “The Aesthetic Turn: Unravelling Recent Aesthetic Approaches to Human-computer Interaction,” *Digital Creativity*, 16, 4 (2005): 205–16；Jeffrey Bardzell, “Interaction Criticism and Aesthetics,” *Proc. of CHI’09.* ACM Press (2009), 2357-66，以及 Jeffrey Bardzell, “Interaction Criticism: An Introduction to the Practice,” *Interacting with Computers*, 23 (2011) 604–21。另见 Olav W. Bertelsen: “Tertiary Artifacts at the Interface,” 载于 *Aesthetic Computing*, Paul Fishwick 编 (Cambridge: MIT Press, 2006), pp. 357-368。根据 Bertelsen 的观点，“人机交互（Human-computer Interaction）需要对计算技术的美学（aesthetics of computing technology）有所理解”，即“计算技术是如何被体验以及‘可体验的’。人机交互领域极需美学计算（Aesthetic Computing）的输入” (p. 359)。在解释

为了阐明其意图，Bertelsen 分析了艺术与科学哲学家 Marx Wartofsky 的著作。我认为这是一篇关于美学计算（aesthetic computing）的优秀文章，即使人们不接受 Wartofsky 的框架，因为 Bertelsen 对美学的阐释在哲学上是严谨的，且将美学与艺术、科学以及计算紧密联系在一起。

1. 参见，例如 Kirsten Boehner, Rogério DePaula, Paul Dourish, 和 Phoebe Sengers, “Affect: From Information to Interaction,” CC 05, *Proceedings of the Dicennial Conference on Critical Computing* (New York: ACM Press), pp. 59-68. 另见 MIT Lab for Affective Computing: [http://affect.media.mit.edu/](http://affect.media.mit.edu/)

1. 虽然涉及这一规范综合体（normative complex）的其他任何话语或学科都可以对其自身的规范性（normativity）进行批判，但唯有美学能够批判规范性的全部复杂性。例如，当 Ken Goldberg 在 University of California at Berkeley 校园的 Sproul Plaza 安装作品 “Demonstrate” (2004) 时，该项目引发了各种问题，而美学可以说处于所有这些问题的中心。他安装了一个机器人网络摄像头，持续运行六周（全天候 24/7），允许远程用户对其进行操作（如缩放、拍照等），这意味着例如在东京的人可以对 Berkeley 广场上的人进行监视（surveillance）。尽管是技术使这一装置成为可能，但显然它不仅仅是一个

这项工程项目，因为远程监控（remote surveillance）会对公立大学校园开放广场上不知情的人们产生影响。这里涉及法律问题，首先是受监控者的隐私权（privacy rights）问题，特别是据我了解，摄像机最初的校准不够精确，因此能够扫描到项目预定参数之外的区域。此外，由于该项目也被视为一件艺术作品，因此还涉及艺术自由（artistic freedom）的问题，这不仅涉及 Goldberg（以及可能执行监控的人员），还涉及广场上的人们；因为他们觉得自己是在参与一件艺术作品，因此在公共行为上不再受到那么严格的约束（显然，有些人是在艺术自由的保护下进行或至少是模拟性行为）。最后，该项目是为了纪念由 Berkeley 领导的言论自由运动（Free Speech Movement） 40 周年，因此还涉及重要的政治问题，因为该运动在当时也曾受到监控，尽管当时没有如今这样先进的技术。美学批判（Aesthetic critique）能够理解像 Goldberg 的 *Demonstrate* 这样项目的规范复杂性（normative complexity）（包括技术、法律、伦理和政治层面），因为美学在分析具有此类规范复杂性的艺术作品方面有着悠久的历史。

1. 据我理解，Warren Sack 认为，对软件和计算的审美维度（Aesthetic dimensions）以及其他非技术性维度的认可，在计算的早期阶段就已显现。参见其网站：[http://people.ucsc.edu/~wsack/](http://people.ucsc.edu/~wsack/)
1. Roger Malina, “A Forty-Year Perspective on Aesthetic Computing in the *Leonardo* Journal,” 载于 Fishwick, *Aesthetic Computing*, p. 48. 另一个较为弱的观点是，审美计算（Aesthetic Computing）可能帮助计算机科学家“更轻松、更快速或更优雅地实现其（现有）目标”（p. 47）。
1. 关于其他科学领域的类似发展，可参见例如 *Aesthetic Science: Connecting Minds, Brains, and Experience*, Arthur P. Shimamura and Stephen E. Palmer, Eds. (New York: Oxford University Press, 2012)。
1. Fishwick, *Aesthetic Computing*, p. 13.
1. 关于现代艺术中“美”的命运，可参见例如 Arthur C. Danto, *The Abuse of Beauty: Aesthetics and the Concept of Art* (Chicago: Open Court Press, 2003); Elizabeth Prettejohn, *Beauty and Art: 1750-2000* (New York: Oxford University Press, 2005); 以及 Wendy Steiner, *Venus in Exile: The Rejection of Beauty in 20th Century Art* (Chicago: University of Chicago Press, 2001)。
1. 在当代美学（Contemporary aesthetics）的历史中，关于艺术作品的开放性（Open nature）一直存在着长期的讨论。参见例如 Umberto Eco, *The Open Work*, tr. A. Cancogni (Cambridge: Harvard University Press, 1989; originally published in 1962)。

# 26.17 Roger Malina 的评论

Paul Fishwick 多年来一直在构建他的“美学计算（Aesthetic Computing）”概念，该概念被广泛定义为将美学的理论与实践应用于计算；在此过程中，他主张使用一种“具身化（embodied）”的形式语言（formal language）。在我看来，如果在这一过程中，作为科学和工程的计算的方法和内容能够得到改变和增强，那么这种方法将变得尤为切题。我将这类目标称为艺术-科学交互（art-science interaction）的“强主张（strong case）”[1]，在这种交互中，其作用超越了演示性或教学性。在 Dagstuhl 工作坊上发布一份“宣言（manifesto）”[2] 也许并非巧合，因为参与者普遍认为，艺术、设计和人文科学对计算机科学的潜在贡献，在爱好者群体之外并未得到广泛认可。

文中提到了一些进展，其中部分已被 Fishwick 提及，但在这里，我想探讨一些包含在美学计算概念中但又超越该概念的问题。Fishwick 谈到，美学计算旨在处理形式语言的不同元素，即数字、数据、模型和软件。

在这里，引入 Denning [3] 的计算七原则（seven principles of computing）或许会有所帮助；这些原则的优势在于它们是面向过程（process oriented）的，有助于聚焦艺术和设计可能进行干预（intervention）的领域：

1. 计算（Computation）：什么可以被计算，什么不能被计算

1. 通信（Communication）：可靠地在不同地点之间传输信息
1. 协作（Coordination）：高效地利用多台计算机
1. 记忆（Recollection）：在媒介中对信息进行表示、存储和检索
1. 自动化（Automation）：为信息处理过程探索算法
1. 评估（Evaluation）：预测复杂系统的性能
1. 设计（Design）：构建具有可靠性的软件系统结构

这显著拓展了审美计算（Aesthetic Computing）方法可能介入的领域；事实上，直到目前为止，艺术与人文领域几乎很少涉及其中的许多领域。

## 26.17.1 大数据转型与表征危机（Big Data Transition and the Crisis of Representation）

过去十年中的一项重大进展有时被称为“大数据”转型（big data transition）[4]。随着数据量和增长速度持续加速，各科学学科正在经历变革性的变化。天文学可能是第一个完成这一转型的学科，其标志是数据存档和软件方面虚拟天文台（virtual observatory）策略的出现。基因组学（genomics）等领域紧随其后，如今商业和文化的各个领域都受到了影响（例如见 [5]）。这导致了所谓的“表征危机（crisis of representation）”，以及信息可视化（infoviz）和数据可视化（dataviz）等新学科的出现。人们迅速意识到，问题不再是通过插图技术（illustration techniques）来“传播（communication）”数据内容（例如 [6]），而变成了如何“沉浸（immersion）”在数据之中。数据不再能被视为“对象（objects）”，而应被视为一种“流体（fluid）”；因此，随着我们进入媒体领域，Fishwick 所提到的具体化（reification）策略已被证明是不充分的。许多研究人员一直试图将“图像科学（image science）”的触角延伸到这一新领域，而这需要尚未开发出的符号学方法（semiotic approaches）。大多数数据从未被分析或查看，因此需要新型的“注意力技术（technologies of attention）”来帮助导航并分离出具有特定内容或意义的数据。这种表征危机为艺术领域提供了一个良好的研究方向。

以及人文科学的参与，这将成为审美计算（Aesthetic Computing）的长期议程；正如 Fishwick 所强调的，关键问题在于具身性（Embodiment），即如何将数据转化为可以通过人类感官感知的形式。许多艺术家在数据导航的探索性项目中表现突出，例如 Donna Cox [7] 和 Ruth West [8]。此外，已有许多展览旨在展示多样化的实现方法（例如 siggraph 的信息美学 [Information Aesthetics] [9]）。在我看来，Fishwick 对这些迅速催生新研究领域的进展关注不足。

## 26.17.2 人工生命艺术、视觉数学与具身代码（Embodied Code）

Paul Fishwick 简要地指出，严肃游戏（Serious Gaming）是代码可以被视为具有具身性（Embodied）的一个领域。但在我看来，算法艺术（Algorithmic Art）、视觉数学（Visual Mathematics）和人工生命艺术（Artificial Life Art）涵盖了更广阔的领域，并且在代码的具身化方面提供了更强有力的实例。由 Michael Noll, Roman Verostko, Harold Cohen 等计算机艺术先驱所推动的算法艺术的发展，已经建立了长达 50 年的历史，旨在通过美学手段和目标，使算法能够被人类的视觉和听觉所感知（Apprehensible）。视觉数学领域（参见 Michele Emmer 及其在 *Leonardo* 出版的两本关于视觉心智 [10] 的著作）已经提供了许多成功案例，展示了美学方法如何引导科学或数学上的发现。继 Santa Fe Institute 举办的奠定了人工生命（Artificial Life）可见基础的研讨会 [11] 及其近期在合成生物学（Synthetic Biology）中的应用之后，艺术界迅速接受了这一挑战，开发了人工生命艺术项目。这导致了机器人学、虚拟世界、交互式装置（Interactive Installations）以及其他将代码与人类感官进行物理接触方式的项目大量涌现。最近，*Leonardo Journal* [12] 发表了一系列选作，以纪念 VIDA 人工生命竞赛（VIDA artificial life competition）十周年，该竞赛是人工生命艺术从业者的顶尖论坛。

## 26.17.3 翻译作为审美计算的一种可能方法

在 26.10 节中，Fishwick 阐述了审美计算（Aesthetic Computing）方法论的要素。在近期与德克萨斯大学达拉斯分校（University of Texas, Dallas）的同事 Rainer Schulte 和 Frank Dufour 的讨论中 [13]，我对他们的研究工作印象深刻。该研究旨在将基于人文学科的翻译研究（Translation Studies）方法，应用于计算机生成或中介的创意“写作”形式（无论是文本、图像、声音，还是多媒体和多感官形式）所带来的问题。正如 Fishwick 在 26.2.4 节关于媒介（Media）的部分中所指出的，这里存在媒介“本质主义（Essentialism）”的问题，即每种媒介都具有特定的特性，这些特性决定了某些概念能否从一种媒介翻译到另一种媒介。但除此之外——正如 Fishwick 所指出的——技术的局限性可能会限制某些形式的具身化（Embodiment）。他举了一个早期文字处理软件体验的例子：作者必须“停止并等待”微处理器跟上进度；同样，现在某些微处理器的运行速度快于人类大脑皮层（Human Cortex）的周期时间，因此，从代码到具身感知（Embodied Perception）的翻译行为需要对现象进行减速和时间拉伸。从“计算形式语言（Formal Languages of Computing）”文化到“艺术与文学形式语言（Formal Languages of the Arts and Literature）”文化（或反之）的翻译行为，需要人文学科的方法论。

以期为审美计算（Aesthetic Computing）构建具有实质意义的具身策略（Embodiment Strategies）。

## 26.17.4 亲密科学（Intimate Science）

在其他文章中 [14]，我探讨了一个普遍问题：如何使人类能够将那些感官无法触及的科学现象进行文化内化（cultural appropriation）。我将这一议程称为“亲密科学（intimate science）”，目前许多艺术家正致力于此。正如哲学家们所指出的，我们认知世界的方式在很大程度上是基于从出生起就积累的经验而构建的。我们对因果关系（causality）或更广泛的解释系统（explanatory systems）的理解，源于我们通过身体和感官与世界的交互。但现在的科学处理的许多现象，不仅超出了我们感官的“放大（amplification）”或“增强（augmentation）”范围，而且在本质上与我们感官运作的方式“不相称（non-commensurate）”。

这个问题在量子力学（quantum mechanics）中表现得最为明显：我们的基础本体论（ontologies）不再适用（物体可以既是波又是粒子），且其中的因果关系概念（例如在量子纠缠 entanglement 的情况下）与我们在宏观世界的经验完全背离。我认为，在复杂性科学（complexity science）的涌现（emergence）概念中，我们也遇到了类似的问题。当然，在理解广义相对论（general relativity）、时空（space-time）的扭曲以及空间本身的结构时，我们也面临类似的问题；作为人类，我们无法直接体验引力波（gravity waves）。在我看来，Fishwick 关于审美计算（aesthetic computing）的议程，在某种程度上将“使科学亲密化”的问题转移到了计算机科学领域。

计算机具有与人体不同的内部逻辑（internal logics）和不同的目的论（teleologies），只有通过他所讨论的具身化（embodiment）机制，我们才能开始“想象”计算机“想象”的方式。将“模型（models）”转换为“小模型（maquettes）”的实践，正是这样一个文化挪用（cultural appropriation）的过程。

## 26.17.5 从 STEM 到 STEAM

在过去的两年中，美国国家科学基金会（U.S National Science Foundation, NSF）与美国国家艺术基金会（U.S National Endowment for the Arts, NEA）合作，组织了一系列研讨会，旨在将科学与工程领域的研究群体与艺术与设计领域的创意群体聚集在一起 [15]。这些举措是对一个社会学事实的回应，即目前有越来越多的研究实践正在将科学与工程桥接至艺术与设计；在某些情况下，艺术与设计学院发现其从事的研究议程与科学或工程部门非常相似，当然，其预期的成果有所不同或存在重叠。有时这涉及到不寻常的跨学科（Trans-disciplinary）协作，而在其他情况下，艺术家和设计师则扮演着发明者和技术创新者的角色。这一发展首先在信息技术（Information Technology）领域被意识到。2003 年的 "Mitchell" 报告《Beyond Productivity》[15] 阐述了其中的问题与机遇。类似的进展目前也正在科学和工程的其他领域发生。作为这些研讨会的成果，NSF 通过 SEAD 计划 [16] 设立了两项研究合同以促进网络开发，并通过 XSEAD 合同 [17] 建立了一个跨学科的文档平台。这些研讨会的早期成果之一是加速了将“STEM 转化为 STEAM”这一概念的普及。在美国又经过三十年的国家级努力以

在培养 STEM 人才管线（STEM workforce pipeline）方面，美国面临着训练有素的科学家和工程师短缺的问题。正如“STEM 到 STEAM 运动（STEM to STEAM movement）”所阐述的（例如，参见由 Rhode Island School of Design 校长 John Maeda 组织的国会证词 [18]），我们需要将艺术与设计，或者更广泛地说，将艺术与人文（Arts and Humanities）整合到科学、技术、工程和数学（STEM）的教育与研究策略中。一些增长最快的计算机科学相关项目集中在计算机艺术、游戏和社交媒体领域；且正如创新研究（innovation studies）理论家所指出的，社会和文化创新的过程在颠覆性技术（disruptive technologies）的成功采用中发挥着越来越重要的作用。基于艺术与人文的可视化和图像科学领域的专业知识，是 Fishwick 所概述的审美计算（aesthetic computing）议程中出现且具有前景的领域。Fishwick 指出，我们的高等教育机构在应对这些研究议程方面的组织结构非常糟糕；Fishwick 在 University of Florida 开发的项目就是一种可能方法的典范。

Fishwick 探讨了针对形式语言构建（formal language construct）——即数字、数据、模型和软件——的审美计算策略。如果我们将 Denning 的七项计算原则，即计算（Computation）、通信（Communication）、协调（Coordination）、记忆（Recollection）、自动化（Automation）、评估（Evaluation）以及

显然，美学计算（Aesthetic Computing）是更广泛的艺术与人文研究策略（Arts and Humanities research strategies）组合的一部分，这些策略为在未来几十年为计算机科学（Computer Science）做出重大贡献提供了机遇。在我撰写这些评论时，网络上正围绕着“新美学”（The New Aesthetics）展开一场广泛的讨论，这场讨论将其来源归功于 James Bridle 在 2011 年 5 月开设的博客 "The New Aesthetics" [20]。该讨论以“计算现已在文化上融入到我们存在于世界的方式之中”为起点（例如，可参阅 Ian Bogost [20] 的反驳），讨论过程十分激烈——这表明我们仅处于美学计算的起步阶段。

## 26.17.6 References

1. Malina, Roger (2011), The Strong Case for Art-Science Interaction, Retrieved
from http://vectors.usc.edu/thoughtmesh/publish/120.php
1. Paul Fishwick et al., 2003, 'Aesthetic Computing Manifesto'. Leonardo, 36, Issue No 4,
1. Peter Denning, http://cs.gmu.edu/cne/pjd/GP/GP-site/welcome.html
1. The fourth paradigm, Data Intensive Scientific Discovery, EDITED BY Tony
Hey, Stewart Tansley,and Kristin Tolle, 2009 Microsoft Corporation, ISBN 978-0-9825442-0-4.
1. http://datajournalism.stanford.edu/
1. Edward Tufte, http://www.edwardtufte.com/tufte/
1. Donna Cox, http://www.ncsa.illinois.edu/~cox/
1. Ruth West, http://www.atlasinsilico.net/gallery.html
1. 2003 Siggraph Information Aesthetics Show case, http://www.siggraph.org/s2009/galleries_experiences/information_aesthetics/
1. Michele Emmer, The Visual Mind, Leonardo Books, 1993, http://leonardo.info/isast/leobooks/books/emmer.html
1. Christopher G Langton (1998). Artificial life: an overview. MIT Press.ISBN 0262621126 ,
1. Leonardo Journal Vida Gallery, http://www.leonardo.info/isast/journal/toc411.html
1. http://translation.utdallas.edu/
1. http://www.sonicacts.com/portal/index.php/roger-malina-intimate-science-or-artists-in-the-dark-universe/
1. Beyond Productivity : http://www.nap.edu/openbook.php?record_id=10671&page=235
1. http://sead.viz.tamu.edu/index.html
1. http://www.slideshare.net/ironman28/xsead-presentation-scalar-11912
1. http://stemtosteam.org/

1. James Bridle, http://new-aesthetic.tumblr.com/
1. Ian Bogost, http://www.wired.com/beyond_the_beyond/2012/04/ian-bogost-the-new-aesthetic-needs-to-get-weirder/

# 26.18 Sophia Krzys Acord 的评论

“手知道心中无法言说之物。”这句关于具身认知（Embodied Cognition）的经典格言，对于艺术家（参见 Sudnow, 1978）和工匠（我推荐 Crawford, 2009）来说并不陌生。它在呈现我们学习和理解构建物理世界所需的知识与实质的复杂方式方面，发挥着重要作用。这句格言还揭示了长期以来笛卡尔式（Cartesian）的“心高于身”之优越感的缺陷，这种观点将语言视为知识的权威中介。Paul Fishwick 致力于开发和构建审美计算（Aesthetic Computing）这一新领域的职业生涯，展示了一种令人兴奋且重要的方式，即将感官和身体经验的概念应用于最形式化的语言——计算机代码。在本评论中，我将简要定义具身认知，简述从审美角度思考交互如何揭示知识构建（Knowledge-making）的重要维度，然后提出审美计算可能为不断发展的数字人文（Digital Humanities）带来变革的几种方式。

认知（Cognition）是指与获取知识相关的心理过程，包括那些涉及语言产生和理解的过程。引用另一部优秀的开放获取学术百科全书关于“具身认知”的条目，

根据 [Stanford Encyclopedia of Philosophy](http://plato.stanford.edu/entries/embodied-cognition/)，当个体“大脑之外”的身体部分在获取、处理和深化对新知识的理解能力中发挥显著的构成性作用（constitutive role）时，我们可以将认知视为是“具身化的”（embodied）。认知科学（cognitive sciences）的新研究进一步证明了具身性（embodiment）在概念学习（conceptual learning）中的重要性。正如心智哲学家 Alva Noë (2006) 在总结这项工作时所描述的，触觉而非视觉，应当成为我们思考知觉（perception）的模型；我们通过主动探究与探索（active inquiry and exploration）来获取新内容。（当然，这并非一个新观点，维科哲学（Vichean philosophy）——参见 Vico, 1725 ——借鉴了 Aristotle 的著作，认为人类只能认知他们所创造的东西。）将知识视为一种行动——即我们与物质对象、身体及环境协同完成的事情——这一观点也得到了我所在的艺术社会学（sociology of the arts）领域许多定性研究的支持（参见 Acord and DeNora, 2008; Sutherland and Acord, 2007）。

从这个视角来看，审美计算（aesthetic computing）是一种契合于更广泛理论范式的尝试，该范式致力于探索行为、知识生产（knowledge-production）和交互中的非认知与准认知维度（non- and quasi-cognitive aspects），以及材料、技术和对象在我们创造的世界中所扮演的重要角色。正如 MIT 的社会科学家

Sherry Turkle 在其 2007 年主编的著作 *Evocative Objects* 中描述道，我们生活中的物理对象是我们记忆、思考和行动的锚点（Anchors）；我们与这些对象的交互方式证明了思考与情感是相连的。同样，音乐社会学家 Tia DeNora (2000) 指出，审美材料（Aesthetic materials）——例如我们听到的歌曲——是我们日常生活中的助力；它们使我们能够完成如果没有它们就无法实现的任务。（任何 Zumba  instructor 都会熟悉音乐的这种力量。）

早期的科学和数学研究也支持这一观点。Jean Lave (1988) 通过观察杂货店购物者如何使用数学，证明了认知（Cognition）是一个在行动者与构成其活动场景（Settings）之间展开的交互过程（Interactive process）。这一点在许多职业中也被发现，包括：设计工程师 (Henderson, 1999)、饼干制造商 (Streeck, 1996) 和船舶导航员 (Hutchins, 1995)。

正如 Fishwick 正确指出的那样，将审美遭遇（Aesthetic encounters）纳入学习软件设计，能够将计算机科学家的心智与身体重新统一，从而使物理编码（Physical coding）或严肃游戏（Serious gaming）的体验能够构建对更抽象分析概念的理解。为学习代码创建嵌入式虚拟体验（Embedded virtual experiences），或者将现实世界的身体隐喻（Bodily metaphors）引入软件设计，对于学生与形式语言（Formal language）的交互具有重要意义。我们所拥有的资源……

构建意义的双手影响着我们能够认知的内容。

在本章中，Fishwick 将审美计算（Aesthetic Computing）的挑战定义为“将人类与计算机连接起来”。在对佛罗里达大学（University of Florida）的一门审美计算课程进行评估时，Fishwick *et al.* (2005) 发现，许多本科生认为审美计算非常耗时，但在向非工程专业人员解释计算概念时特别有用。然而，在深入探讨审美计算背后的理论时，我主张在这里将人类与计算机连接起来，还存在其他重要的机会可以推进计算机科学以及人文科学学科的知识。

正如科学社会学家所展示的，产生科学知识需要从“肮脏”、“模糊”且亲身实践的经验，转向抽象且编码化的表征（Codified representations）（参见 Latour and Woolgar, 1979）。因此，科学结果和发现是我们人类经验的翻译，这可能会扭曲我们真正认知的内容。Ong (1982) 对人类书面语言技术提出了类似的观点：学习一种书面语言必然伴随着意识的转变；我们开始用文字思考，而不再是直接表达我们的想法。虽然 Fishwick 引用了 Mark Johnson 和 George Lakoff 的优秀著作，以表明我们的具身经验（Embodied experiences）通过隐喻（Metaphor）存在于语言中，但 Ong 同样证明了书面语言

……通过将词汇和书面语言符号定位为我们认知内容及其表达方式的人工中介（artificial mediators），从而面临消除具身化（embodiment）过程的风险。我们如何才能跳出语言，去研究语言概念？

我认为审美计算（aesthetic computing）为计算机科学家（及其学生）提供了一个契机，让他们通过创造一种全新的、具身的体验，与构建形式语言符号（formal language notation）的基础概念进行“游戏”（‘play’，参见 Huizinga, 1944），从而以不同的方式参与到软件设计中。通过绕过作为数学关系认知中介的形式语言符号，并将身体作为另一种中介参与其中，审美计算可能会开启思考软件设计的新路径。简而言之，让我们以艺术作为一种审美活动为例：在艺术中，艺术创作或参与是一种将“感受到的”体验外化（externalize）并进行反思的方式，旨在把握（并扩展）那些由语言中介的情境（linguistically mediated situations）。艺术可以成为一个通过替代性构建和实现来深化我们理解的空间；通过这种方式，艺术能够促进疗愈、冲突解决以及社会运动（Acord and DeNora, 2008）。同样，正如教育学者 Donald Schön (1987) 对建筑系学生的观察，通过构建物理模型进行亲手“制作”（‘making’）并对更抽象的建筑概念进行审视，为即时实验、问题解决以及……创造了机会。

他将其称为“行动中反思（reflection-in-action）”的修补（tinkering）。重要的是，这种具身修补（embodied tinkering）可以创造质疑和改变语言设计概念的机会，从而可能导致对形式语言系统（formal language systems）的修正。（手的感觉可能与大脑对其的分类不同。）在本章中，Fishwick 观察到，“当我们打开包含通常隐藏的数据、公式、代码和模型等原子元素的黑盒盖子时，我们发现计算从始至终都是一场戏剧（theatre all the way down）。”如果计算是一场戏剧，那么诀窍就在于将其视为如此：一个进行具身游戏（embodied play）的场所，不仅是为了简单地重复那些排练得很好的形式语言概念，而且是为了对它们进行修补或改进。对我而言，这种“即兴发挥（improvisation）”的可能性是审美计算（aesthetic computing）最令人兴奋的潜力之一。

最后，Fishwick 将审美计算描述为一个将计算机科学家、艺术家和人文领域学者聚集在一起的领域，以扩展我们在数字时代中意义构建（meaning-making）的模型。然而，在本章的前文中，Fishwick 借鉴了 Sherry Turkle 的研究以及数字手表的例子，讨论了计算（作为一种形式语言）中深层的抽象概念如何影响用户的思维。形式语言塑造（并由此推断，限制）我们思考方式的观点，对于一些希望利用计算技术来扩展（而非限制）阐释可能性（interpretive possibilities）的人文学者来说，尤其令人不安。

（正如 Jaron Lanier, 2010 所指出的：我们应该使用设备，而不是被设备使用。）尤其是 Johanna Drucker，她探讨了基于数学的形式语言（formal languages）与图像及数字人文（digital humanities）数据之间的紧张关系，而后者质疑了形式化且既定的意义体制（regimes of meaning）（参见 Drucker, 2001, 2009, 2011）。

审美计算（Aesthetic computing）允许人们对形式语言概念本身（而不仅仅是作为代码的书写符号）进行质疑和探索，这很可能是创建真正全新且开放的解释性界面（interpretive interfaces）的解决方案。正如 Dexter et al. (2011) 在 *Culture Machine* 最近一期关于数字人文的特刊中所论证的，“当美学被置于软件开发创意过程的一部分这一语境中时，其功能性作用得到了最充分的体现”（pp. 16-17）。换句话说，当程序员将自己视为具身化（embodied）的存在时，变革交互计算环境的机会将得以增加。

因此，我认为，为了推进数字人文，我们不仅要像批判性代码研究（critical code studies）领域那样，从美学或符号学的角度思考代码，还必须更进一步，以不同的方式思考编程所基于的心理/生理构建（mental/physical constructions）。通过这种方式，审美计算提供了物理和身体层面的工具，从而能够彻底重新思考数字时代文化计算（cultural computing）的可能性。

## 26.18.1 References

- Acord, Sophia Krzys and DeNora, Tia (2008). Culture and the arts: From art worlds to arts-in-action. *The Annals of the American Academy of Political and Social Science*, 619(1): 223-237.
- *Crawford, Matthew (2009) **Shop Class as Soul Craft: An Inquiry into the Value of Work**. New York: The Penguin Press.*
- DeNora, Tia (2000) *Music in Everyday Life*. Cambridge: Cambridge University Press.
- Dexter, Scott, Melissa Dolese, Angelika Seidel, and Aaron Kozbelt (2011) On the embodied aesthetics of code. *Culture Machine*, 12.
- Drucker, Johanna (2001) Digital ontologies: The ideality of form in/and code storage: Or: Can graphesis challenge mathesis? *Leonardo*, 34(2): 141-145.
- *-- (2009) **SPECLAB: Digital Aesthetics and Projects in Speculative Computing**. Chicago, London: University of Chicago Press.*
- -- (2011) Humanities approaches to interface theory. *Culture Machine*, North America, 12.
- Fishwick, Paul, Timothy Davis, and Jane Douglas (2005) Model representation with
aesthetic computing: Method and empirical study. *ACM Transactions on Modeling and Computer Simulation*, 15(3): 254—279.
- Henderson, Kathryn (1999) *On Line and On Paper: Visual Representations, Visual Culture, and* *Computer Graphics in Design Engineering*. Cambridge, MA: The MIT Press.
- Huizinga, Johan (1944) *Homo ludens: A study of the play element in culture*. Translated by G. Steiner, 1970. London: Paladin.

- Hutchins, Edwin (1995) *Cognition in the Wild*. Cambridge, MA: The MIT Press.
- *Lanier, Jaron (2010)* *You Are Not a Gadget: A Manifesto**. New York:* Alfred A. Knopf.
- Latour, Bruno and Steve Woolgar (1979) *Laboratory Life: The Construction of Scientific Facts*. Beverly Hills: SAGE Publications.
- Lave, Jean (1988) *Cognition in Practice: Mind, Mathematics, and Culture in Everyday Life*. Cambridge: Cambridge University Press.
- Noë, Alva (2006) *Action in Perception*. Cambridge, MA: The MIT Press.
- Ong, Walter J. (1982) *Orality and Literacy: The Technologizing of the Word.* New York: Methuen.
- Schön, Donald A. (1987) *Educating the Reflective Practitioner*. San Francisco: Jossey-Bass Publishers.
- Streeck, Jürgen (1996) How to do things with things: Objects trouvés and symbolization. *Human Studies*, 19: 365-384.
- Sudnow, David (1978) *Ways of the Hand: The Organization of Improvised Conduct*. Cambridge, MA: Harvard University Press.
- Sutherland, Ian and Sophia Krzys Acord (2007). Thinking with art: From situated knowledge to experiential knowing. *The Journal of Visual Art Practice*, 6(2): 125-140.
- *Turkle, Sherry (ed.) (2007) **Evocative Objects: Things We Think With**. Cambridge, MA: The MIT Press.*
- *Vico, Giambattista. (1725) **Scienza Nuova*. (*The First New Science*, edited and translated by Leon Pompa, Cambridge: Cambridge University Press, 2002.)

# 26.19 Kang Zhang 的评论

Fishwick 在 2006 年出版的编著中正式引入了审美计算（Aesthetic Computing）[1] 的概念。根据当时的定义，*审美计算* 旨在探讨“传统视觉艺术中的理论和技术如何帮助美化现代技术的输出结果与产品，并增强其可用性（usability）？”。它涵盖了计算机算法、模拟、可视化（visualization）[4]、人机界面（human-machine interfaces）以及高科技产品的审美设计，从而使用户能够高度参与，进而提升可用性。审美计算的一个有趣案例是将 Kandinsky 的美学应用于 Java 编程 [3]。Malina [2] 重点介绍了过去四十年中发表在 *Leonardo* 期刊上的审美计算活动。Fishwick 关于审美计算的新章节采取了更具体且更具操作性的视角（operational view），重点关注具身形式语言（embodied formal language）的概念。类比于被认为是首批虚拟现实（virtual reality）创造者的艺术家，计算机科学家可以通过身体模拟（bodily simulations）——可能是在虚拟现实环境中——来动态地解释对象。

一个相关的新兴学科，但在概念方向上相反，是计算美学（computational aesthetics），其旨在回答“计算机如何自动生成各种形式的视觉审美表达？” [6]。换句话说，计算美学研究现代

技术助力艺术。技术旨在创造能够增强视觉艺术表现力，并深化人类对审美评价（aesthetic evaluation）、感知（perception）和意义理解的工具。

本章阐述的观点和概念（其中部分深植于艺术、科学与技术之中）具有启发性，对于任何对计算（computing，或数学）与艺术均感兴趣的人来说都具有极大的吸引力。技术已发展到这样一个阶段：艺术与设计在科学技术中的重要性和相关性日益增加，而纯粹技术知识的重要性则在下降。这一趋势将持续下去，且近期的一项发现间接支持了这一论点，即互联网和搜索技术正在改变我们的大脑以及我们的思维方式，因为我们不再需要记忆，而只需知道如何搜索以获取所需信息。

1. P. Fishwick (Ed.) ***Aesthetic Computing***, MIT Press, Cambridge, 2006.
1. R.F. Malina, **A Forty-Year Perspective on Aesthetic Computing in the Leonardo Journal**, in: P. Fishwick (Ed.) *Aesthetic Computing*, MIT Press, 2006, 43-52.
1. C.B. Price, **From Kandinsky to Java (The Use of 20th Century Abstract Art in Learning Programming)**, *ITALICS*, Vo.6, No.4, October 2007, 35-50.
1. K. Zhang, **From Abstract Painting to Information Visualization**, *IEEE Computer Graphics and Applications*, May/June 2007, 12-16.

1. K. Zhang, **书评：《Aesthetic Computing》（Paul Fishwick 主编）, MIT Press, 2006, ISBN 0-262-06250-X**, *Journal of Visual Languages and Computing*, 第 18 卷, 第 6 期, 2007 年 12 月, Elsevier Science Inc., New York, 613-616 页.
1. K. Zhang, S. Harrell, and X. Ji, **计算美学（Computational Aesthetics）——论计算机生成绘画的复杂度（Complexity of Computer-Generated Paintings）**, *Leonardo Journal*, MIT Press, 2012, 第 45 卷, 第 3 期（待出版）.

# 26.20 David J. Therriault 的评论

在关于审美计算（Aesthetic Computing）的章节中，Paul Fishwick 为将具身性（embodiment）应用于人机界面（human-computer interfaces）提出了一个非常易懂且极具说服力的论点。Fishwick 的论证是通过考察具身示例中不同层次的临场感（presence）来构建的。你能否想象自己身处一幅画作的风景之中，或者在进行数学运算时虚拟地操纵物体，亦或是成为一个文字描述世界中的角色？事实上，你是可以做到的，而且更重要的是，这样做可能会带来学习上的益处。Fishwick 提供了软件中使用具身性的丰富示例（例如，一台由水桶制成的蒸汽朋克（steampunk）肥胖机器，用于解释动力系统（dynamic systems）），这些示例让我们得以窥见审美计算的潜力。在本评论的剩余部分中，我将简要讨论认知历史以及我自己在研究具身性方面的经验，并认为 Fishwick 的见解让读者真正地窥见了编程的未来。

认知心理学（cognitive psychology）的传统观点认为，信息处理（information processing）利用的是抽象符号（abstract symbols）。自 20 世纪 50 年代以来，对抽象/非模态符号（amodal symbols）的操作已成为研究记忆、阅读和思考理论的基石。让我们以阅读心理学为例。Kintsch (1974, 1998) 关于阅读理解（reading comprehension）的影响深远的研究是基于命题（propositions，即抽象的思想单位）构建的。

Kintsch 还为命题（propositions）的心理现实（psychological reality）提供了证据，在很大程度上塑造了我们目前对阅读时大脑中发生之过程的理解。然而，在我们的阅读体验中，始终缺失了一部分表征（representation）——即一种存在感（presence）或具身性（embodiment）（这通常被称为符号接地问题 [symbol grounding problem]）。我们该如何解释命题是如何获得意义的？我们又是如何真正体验到所读内容的？在许多方面，Fishwick 正在解决同一个符号接地问题（但是在编程框架 [programming framework] 之内）。

简单来说，具身性是指尝试通过身体的经验和感知来理解心智（例如，感知符号 [perceptual symbols] 或接地认知 [grounded cognition]）。有趣的是，探讨身体如何影响我们理解的研究在话语心理学（discourse psychology）中最为突出，特别是文本理解（text comprehension）领域。Barsalou (1999), Glenberg (1997), Lakoff and Johnson (1999) 以及 Pecher & Zwaan (2005) 等研究者都认为，具身认知方法（embodied approach to cognition）相比于传统的心理表征（mental representation）观点可能具有优势。

我自己接触具身性是在 21 世纪初担任 Rolf Zwaan 的博士后（post doc）期间。那是一段美好的经历，我们的大部分时间都花在讨论如何测试认知与行动之间的联系上，期间伴随着优质的咖啡，甚至是更好的苏格兰威士忌，并见证这些想法在...中变为现实。

...实验室。在我入职之前，其他教职员工曾警告我，研究具身认知（Grounded Cognition）是“古怪的”，而且人们对这一话题的关注很快就会消退。

从那时起，已有大量令人信服的证据证明了具身性（Embodiment）的心理现实性。例如，我们知道，当听众闭上眼睛听故事时，他们的眼球会像在现实世界中观看故事一样移动（Spivey, Richardson, Tyler, & Young, 2000）；在执行身体任务时所激活的大脑区域，与阅读关于该任务的描述时所激活的区域相同（Feldman & Narayanan, 2004）；甚至我们的道德判断也能影响我们的感知，例如对房间内光线强度的感知（Banerjee, Chatterjee, & Sinha, 2012）。我们自己的研究（Kaschak et al. (2002)）提供了证据，表明运动感知利用了部分与理解运动的语言描述相同的神经机制（Neural Machinery）。

探索认知具身视角的研究继续繁荣，但目前尚无统一的理论。大多数研究人员强烈主张认知的符号视角（Symbolic view）或具身视角，但该领域正逐渐摆脱这种二分法（Dichotomy）。例如，Louwerse (2007) 主张探讨符号和具身性的相对贡献。Fishwick 的章节代表了一种真正新颖的具身化方法：将其应用于更好地理解诸如系统之类的事物

动力学（Dynamics）、数感（Number Sense）或编程。这一观点也令人耳目一新，因为具身计算（Embodied Computing）并非旨在取代编码中丰富的符号传统（Symbols Tradition）。但具身性（Embodiment）可能会积极地增强我们未来与计算机交互的方式，而谁不希望如此呢？

总之，我认为 Fishwick 的这一章节是一次成功的尝试，其影响不仅限于为审美计算（Aesthetic Computing）的研究提供支撑（Undergirding，请原谅这个双关语）。编程成为了我所在学科的人员继续研究心理表征（Mental Representation）的一个更具吸引力的领域。

## 26.20.1 References

- Banerjee, P., Chatterjee P., & Sinha, J. (2012). Is it light or
dark? Recalling moral behavior changes perception of brightness. *Psychological Science*, 23 (4), 407-409.
- Barsalou, L. W. (1999). Perceptual symbol systems. *Behavioral and Brain Sciences*, 22, 577-660.
- Glenberg, A. M. (1997). What memory is for. *Behavioral and Brain Sciences,* 20, 1-55.
- Kaschak, M. P., Madden, C. J., Therriault, D. J., Yaxley, R. H., Aveyard, M.,
Blanchard, A., & Zwaan, R. A. (2005). Perception of Motion Affects
Language Processing. , B79-B89.
  Cognition, 94(3)
- Kintsch, W. (1974). *The representation of meaning in memory.* Hillsdale, New Jersey: Erlbaum
- Kintsch, W. (1998). *Comprehension: A paradigm for cognition.* New York: Cambridge University Press
- Lakoff, G. & Johnson, M. (1999). *Philosophy in the flesh: The embodied mind and its challenge to Western thought*. New York: Basic Books.
- Louwerse, M. M. (2007). Symbolic or embodied representations: A case for symbol
interdependency. In T. Landauer, D. McNamara, S. Dennis, & W. Kinsch (Eds.). Handbook of latent semantic analysis (pp. 107-120). Mahwah, NJ: Erlbaum.
- Pecher, D. & Zwaan, R. A. (Eds.) (2005). *Grounding Cognition: The role of perception and action in memory, language, and thinking.* New York: Cambridge University Press.
- Spivey, M. J., Richardson, D. C., Tyler, M. J., & Young, E. E. (2000). Eye

movements during comprehension of spoken scene descriptions. *Proceedings of the Twenty-second Annual Meeting of the Cognitive Science Society*, (pp. 487-492), Erlbaum: Mawhah, NJ.

## 本书章节涵盖的主题：

[美学 (Aesthetics)](https://www.interaction-design.org/literature/topics/aesthetics)
[用户体验 (User Experience, UX) 设计](https://www.interaction-design.org/literature/topics/ux-design)
[人机交互 (Human-Computer Interaction, HCI)](https://www.interaction-design.org/literature/topics/human-computer-interaction)
[设计史 (Design History)](https://www.interaction-design.org/literature/topics/design-history)
[视觉呈现 (Visual Representation)](https://www.interaction-design.org/literature/topics/visual-representation)
