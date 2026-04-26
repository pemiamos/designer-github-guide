# 34. 人机交互中的实验方法（Experimental Methods in Human-Computer Interaction）

**来源**：The Encyclopedia of Human-Computer Interaction, 2nd Ed.
**Notion 原页面**：https://www.notion.so/e662fea1a5864df7bca1b4b7be4c95d3

---

[Paul Cairns](https://www.interaction-design.org/literature/author/paul-cairns)

### 34.0.1 引言（Introduction）

由于根植于心理学（Psychology），实验在人机交互（Human-Computer Interaction, [HCI](https://www.interaction-design.org/literature/topics/human-computer-interaction)）中一直发挥着重要作用。例如，早期的实验性 HCI 论文包括 English et al. (1968)、Card, Moran and Newell (1980) 以及 Malone (1982)。从这些早期阶段开始，心理学风格的实验逐渐发展成为[可用性](https://www.interaction-design.org/literature/topics/usability)（Usability）测试的基础。在可用性测试中，研究者通过对照研究（Controlled Studies）（例如参见 Preece, Rogers and Sharp, 2010）来比较不同的设计，并衡量其在可用性关键维度——即效率（Efficiency）、有效性（Effectiveness）和满意度（Satisfaction）——方面是否存在显著差异（Hornbaek and Law, 2007）。这体现在所提出的 HCI 工程化方法（Engineering Approach）中，例如 Dowell and Long (1989) 的研究。在这种方法中，新接口的构建是通过应用关于[人因工程](https://www.interaction-design.org/literature/topics/human-factors)（Human Factors）的科学既有知识，从而在用户使用接口时实现可预测且可衡量的效果。

然而，与此同时，HCI 始终意识到技术对人类生活的深远影响，因此也日益受到其他学科的影响，如社会科学（Social Sciences）、文化研究（Cultural Studies），以及近期的艺术与人文学科（Arts and Humanities）。这些不同的影响带来了各自的研究方法，例如

民俗方法论（Ethnomethodology, Suchman, 1995）和批判性阅读（Critical Readings, Blythe et al. 2008）。此外，基于科学原理构建界面工程的愿景已经破灭，因为 HCI 已不再仅仅关注用户的生产力（Productivity），而是开始关注系统对用户体验（User Experiences）更广泛的影响 (McCarthy and Wright, 2005)，包括乐趣 (Blythe at al. 2006)、愉悦感 (Jordan, 2001)、沉浸感（Immersion, Jennett et al. 2008）等。

尽管如此，实验在 HCI 中始终占据着稳定的地位，并在适当的情况下进行调整，以应对这些更广泛的目标。它们依然体现了通过收集可靠数据，为交互提供严谨且经过经验验证（Empirically Validated）的洞察这一原则，但已使其适用于更广泛的研究问题。这在一定程度上体现在 HCI 社区致力于发展一种面向交互科学（Interaction Science）的导向，而理论和实验正是该科学的基石 (Howes et al., 2014)。

此外，随着学科的日益成熟，现在出现了一代纯粹的 HCI 研究者，这与早期不同——早期的研究者在进入 HCI 领域之前，其早期的研究工作是在完全不同的学科中完成的，例如 Psychology, Physics, English, Mathematics 等。因此，开始出现一些旨在描述研究方法，特别是这些第二代 HCI 研究者所需的实验方法的文献。关于……的综述

实验方法（experimental methods）在 Cairns and Cox (2008a)、Lazar et al. (2009) 以及 Gergle and Tan (2014) 中有所阐述。Purchase (2012) 则全书都在讨论人机交互（Human-Computer Interaction, HCI）中实验的设计与分析。此外，一些著作也大量采用了实验方法，例如 Tullis and Albert (2008) 以及 Sauro and Lewis (2012)，旨在演示如何有效地衡量用户交互（user interactions），从而改进交互系统（interactive systems）的设计。因此，即便并非处于纯粹的研究语境下，这些著作理所当然地也提供了关于 HCI 实验设计与实施的许多细节和见解。

此外，还有一些研究论文专注于实验的特定方面，以帮助解决在 HCI 领域部署实验方法时所特有的问题。这些研究论文涵盖了多样化的主题，例如统计分析（statistical analysis）的质量 (Cairns, 2007)、新的统计方法 (Wobbrock et al., 2011) 以及开展高质量实验的实际操作问题 (Hornbaek, 2013)。

这为本章的目标带来了挑战。实验显然是现代 HCI 研究者工具箱中的一项重要方法，但目前已有若干资源能够比本章更详尽地描述实验方法。已经存在一些综述章节（包括我写的一篇！），为新入行的研究者提供了入门资源。那么，本章能提供哪些有益的补充？首先，

应当注意到，这是一个百科全书的章节，因此如果这是一个在人机交互（Human-Computer Interaction, HCI）领域的重要课题，那么它就应当被呈现。本章旨在探讨这一课题。其次，我认为在 HCI 中进行实验存在一个尚未被*明确（explicitly）*探讨的视角，而这正是我希望在此呈现的内容。这并不是说在该领域撰写相关内容的同行们对本章中的内容一无所知，而是说这是我基于自身使用实验方法（experimental methods）的经验，尤其是指导学生使用这些方法的经验，所做出的个人综合总结。

可以理解的是，学生在学习实验方法时会遇到困难，部分原因是这些方法对他们而言是陌生且新颖的，但似乎有些问题源于他们并不完全理解为什么必须按照被告知的方式（无论是来自我还是来自教科书）去操作。实验周围似乎存在一种未能被完全揭示的“仪式性神秘感（ritual mystique）”。这一问题在其他学科中也有记载，例如 Psychology，学生和研究人员往往仪式化地遵循实验方法（Gigerenzer, 2004），却无法识别该方法何时失效或低效。因此，本章旨在简明地传达实验方法背后的核心理念，并演示这些理念在 HCI 实际实验研究的开展中是如何体现的。从这个视角出发，我确定了支撑优秀实验的三大支柱（three pillars）...

实验。它们分别是：
- 实验设计（Experimental design）
- 统计分析（Statistical analysis）
- 实验报告撰写（Experimental write-up）

如果这些支柱中的任何一个薄弱，那么实验的贡献也就薄弱。只有当这三者协同工作时，我们才能对实验得出的研究结果（research findings）充满信心。

本章将依次讨论这些支柱，并在此过程中展示它们之间是如何相互关联的。不过在开始之前，有必要思考什么是实验。这就是哲学（philosophy）。过多的哲学思考会让人陷入瘫痪（至少对于 HCI 研究者来说是这样，尽管对哲学家来说显然不是）。但未经审视的生活是不值得过的（Plato, 1956, The Apology）。那么，让我们开始吧。

### 34.0.2 科学哲学小论

尽管关于什么是科学，以及「科学方法（Scientific Method）」是否真的是一个连贯且有意义的术语（Feyerabend, 2010）存在诸多分歧，但人们普遍认同科学是关于「理论（Theories）」和「实验（Experiments）」的。理论是以数学方式（如 “E = mc²”）或语言方式（如 “数字游戏满足了人们对自主的需求”）表达的陈述，用于描述世界的运作方式，因此可以在一定程度上预测在特定情况下可能发生的事情（Chalmers, 1999, chap. 4）。实验则相对难以定义，因为它们取决于研究领域、研究问题，甚至取决于执行实验的科学家。因此，实验充满了实践技巧（Craft skill）和经验，但基本上可以将它们理解为对想法的测试或尝试。

从历史上看，理论在科学哲学（Philosophy of Science）中占据主导地位，人们非常关注什么是理论以及我们如何知道理论是正确的。这体现在科学哲学中的主导影响力人物如 Popper (1959) 和 Kuhn (1962) 身上。他们的许多思考都集中在理解科学理论的本质上。在这些方法论中，实验是对理论的测试，能够削弱甚至推翻理论，但在本质上是从属于理论的。如果情况确实如此，那么对于人机交互（Human-Computer Interaction, HCI）来说将是一个巨大的问题。因为在 HCI 领域中，很难找到那些能够轻易地...

预测人们将如何与特定系统交互以及结果如何。[菲茨定律（Fitts’ Law）](https://www.interaction-design.org/literature/topics/fitts-law) (MacKenzie, 1992) 是人机交互（Human-Computer Interaction, HCI）领域中一个经过充分验证的理论的典型例子。但首先，它对于诸如按钮布局（button layout）等具体差异的影响极其微小，以至于可以忽略不计 (Thimbleby, 2013)；其次，即使在指导设计时，该定律也经常被误读。例如，人们经常用它来证明将元素放置在屏幕边缘的合理性，因为这样按钮在实际上具有无限的宽度 (例如 Smith, 2012)，但针对现代界面的菲茨定律更新研究表明，高度和宽度同样重要 (MacKenzie and Buxton, 1992)。如果你对人机交互领域中理论的地位仍有疑问，

将其与心理学进行对比，心理学中已有许多成熟的理论可以预测人们在各种情境下的行为：例如[感知（perception）](https://www.interaction-design.org/literature/topics/perception)和非注意盲视（inattentional blindness）（Simons and Chabris, 1999）；决策中的[锚定偏差（anchoring biases）](https://www.interaction-design.org/literature/topics/anchoring)（Kahneman, 2012）；具身认知（embodied cognition）（Wilson, 2002）等等。这并不是说这些理论在我们的日常生活中体现得如此清晰，但它们在实验室中以及在实验室之外的许多情况下都表现得十分稳健。而人机交互（HCI）很难证明存在任何类似的实质性交互理论。

幸运的是，对于 HCI 而言，最近人们意识到实验具有独立于理论的自身价值。这种方法被称为新实验主义（new experimentalism），例如 Chalmers (1999)，它反映了这样一个事实：有时实验的产生源于一个想法，但这个想法不一定得到了现有理论的支持，在某些情况下，甚至恰恰相反。一个经典的例子是 Faraday 首次演示电动机。在 Faraday 的时代，人们已知电流与磁场之间存在某种相互作用，但正是 Faraday 通过证明当电流通过一根悬挂的导线时，该导线会围绕磁铁持续旋转，从而清晰地分离出了这一效应（Hacking,

1983年）。Maxwell 随后又花了 60 年时间才定义了完整的电磁学（electromagnetism）理论来解释这一点，尽管该理论在当时看来显然存在缺陷，因为它预测无论观察者的运动状态如何，光速（speed of light）都是恒定的（而事实证明这确实是真的！）。

如果实验不是在测试理论，那么它们是什么？从某种意义上说，实验仅仅是分离出（isolate）一个感兴趣的现象（Hacking, 1983）。我们最初是如何识别出该现象的（是通过理论、直觉还是纯粹的偶然）并不重要。一旦我们将其分离出来并能够可靠地复现（reproduce），该实验就成为了一个需要被解释的对象，就像 Faraday 的电动机一样。不过，很少有实验真的是纯粹的偶然。相反，它们源于一个人或多人为了识别正在发生的有趣事物、为了分离出一个已知现象而做出的共同努力。

关于实验在科学中作用的一种更精细的阐述是，实验是对一个想法的[严苛测试（severe test）](https://www.interaction-design.org/literature/topics/test)（Mayo, 1996）。在这种表述中，我们可能有一个想法——无论它是既有的理论还是关于事物运作方式的某种直觉——然后我们构建一个情境，使该想法能够接受严苛的测试。例如，我们可能认为数字游戏能够改善心理治疗（psychotherapy）的效果。因此，我们需要构建一个情境，以便能够清晰地判断数字游戏是否产生了改善效果。

……心理治疗的成效，且任何此类改善的原因都可以直接归因于数字游戏（digital games）。这直接决定了此类实验的设计形式：固定的治疗方式；甚至可能是固定的治疗师或一组治疗师；具有可比性的患者；明确的结果评估等。尽管如此，在统一了基准（levelled the playing field）之后，我们期望数字游戏能够证明其带来的改善。该实验隔离了研究者感兴趣的现象——在本例中即心理治疗背景下的数字游戏，并对其进行设定，使得如果该方案注定失败，那么这种失败将是显而易见的。或者，如果它取得了成功，那么显然数字游戏就是成功的唯一原因。因此，正是通过这类严谨的实验，该观点才得到了严苛测试（severe testing），而每一次实验也因此为其提供了支持性证据。

在严苛测试的定义中，另一件需要注意的是，在构建实验时，存在一个被测试的预测，且该预测具有一定的结构，即：在实验所代表的情境中，结果将以某种特定的方式呈现。这种预测是任何实验的核心 (Abelson 1995; Cairns and Cox 2008a)，但同样需要注意的是，这是一种因果预测（causal prediction）：当 X 发生时，Y 将随之而来。这两点对于如何定义实验方法以及如何进行统计分析（statistical analysis）都至关重要。

将实验视为“严苛测试（severe tests）”的另一个直接推论是，没有任何单一实验能够足以验证一个想法的所有含义（至少对于那些主张其影响力不限于极窄范围的想法而言）。单次实验仅是一次测试。可能还存在其他能使该想法失效的测试，或者通过对测试进行改进，使其更加严苛，从而成为更好的测试。实验并非孤立存在，而需要围绕某个特定想法形成集群（cluster）。尽管通过测试对于确立一个想法的鲁棒性（robustness）至关重要，但这仅是支持该想法的证据，而绝非证明该想法绝对正确的证据。

正如任何哲学分支一样，Mayo 关于严苛测试的概念并非关于实验本质及其与科学关系的最终定论 (Mayo and Spanos, 2010)。然而，这一观点显然具有坚实的基础；而且从更务实（pragmatically）的角度来看，我发现它在人机交互（HCI）领域非常有用。许多 HCI 实验并不诉诸理论（recourse to theory）：所研究的语境（contexts）、任务和设备过于复杂，难以被纳入一个简单且被广泛认可的理论之中。相反，研究者倾向于论证在特定情况下，某种特定的交互为何会导致某种特定的结果，并希望借此深化对这类交互的理解。也许随着时间的推移，这种做法会催生出某种理论，但也许它仅仅是为设计师提供了一些可靠的信息。以……形式进行的传统可用性测试（usability test）

实验是这方面的最佳示例。研究人员感兴趣的并非形式化理论（Formal Theory），而仅仅是某个特定系统在特定语境（Context）下是如何运作的。被预测的交互行为将接受一项严苛测试（Severe Test），在这种测试中，结果可能并不如预期；而一旦通过测试，则有充分的证据表明该交互行为符合预期理解，因此值得进一步使用或研究。            Certificates就本章的目的而言，有趣的是，“严苛测试”这一概念确实解释了人机交互（Human-Computer Interaction, HCI）中实验方法的许多特性（以及问题），尽管这些方法在这一哲学思想出现之前就已经被使用了。同样值得注意的是，此前撰写过关于 HCI 实验的作者（包括我自己）中，没有人

……采用了将实验视为“严苛测试（severe tests）”的观念。尽管如此，那些开发、部署和倡导此类实验的人似乎知道一个优秀的实验中哪些因素至关重要，即便他们缺乏一套能够明确阐述其原因的哲学基础。在对人机交互（Human-Computer Interaction, HCI）中的实验进行了哲学定位之后，接下来将依次探讨实验研究的三大支柱（three pillars of experimental research）。

### 34.0.3 实验设计（Experimental Design）

实验设计基本上是对实验具体执行过程的描述。计算机科学家经常使用 GIGO（Garbage In, Garbage Out，垃圾进，垃圾出）这一缩写，来描述基于低质量数据的程序输出结果。实验亦然：实验所得的数据质量不可能超过产生该数据的实验设计本身。幸运的是，人机交互（HCI）领域的研究者擅长理解[设计过程（design process）](https://www.interaction-design.org/literature/topics/design-process)的复杂性，这一过程结合了[创新（innovation）](https://www.interaction-design.org/literature/topics/innovation)、实践技巧（craft skill）和扎实的知识（Lawson, 1997）。就此而言，实验设计与任何其他形式的设计并无二致。

对初学者而言，最具误导性的一点是，论文中的实验设计通常被写成对既定事实的客观描述，而导致该特定实验方案出台的复杂过程往往被略过。具体而言，一个实验设计可能经历过纸面上的反复迭代、预实验（pilot）的测试，甚至可能经历过彻底的失败并在此基础上进一步迭代，但这些过程在论文中可能仅被简略提及，甚至完全不被提及。鉴于实验设计的这种实践维度（craft element）除了在教科书（如 Purchase, 2012）中极少出现，研究者可能很难察觉到一项[优秀设计（good design）](https://www.interaction-design.org/literature/topics/good-design)所必需的关键特征。

……或是设计过程中需要投入的思考。但这些特性至关重要，因为在将一个宏观想法转化为具体实验的过程中，需要做出许多选择；正如任何设计师都会告诉你的，正确的选择并不总是显而易见的。同时，确实存在错误的选择，但当你初涉实验设计时，这一点并不明显。

将实验作为一种严苛测试（severe test）的起点，是构建一个能够测试某种想法的情境，且该想法必须具有因果关系（causal）：即一件事物应当影响另一件事物。在 HCI 风格的实验中，这也被表述为观察自变量（independent variable）对因变量（dependent variable）的影响。自变量是指处于实验者控制之下且由实验者明确操纵的变量。因变量则是对操纵结果的数值衡量：即实验者收集的数据。

然而，考虑到 GIGO（Garbage In, Garbage Out，垃圾进，垃圾出）原则，确保实验产出的数据具有尽可能高的质量至关重要。在实验领域，质量等同于效度（validity），通常有四种效度至关重要 (Yin, 2003; Harris, 2008)：

- 结构效度（Construct validity）
- 内部效度（Internal validity）
- 外部效度（External validity）
- [生态效度（Ecological validity）](https://www.interaction-design.org/literature/topics/ecological-validity)

此处的排序并非绝对，但可以被理解为

从实验的具体细节延伸至更广泛的实际场景。当然，这些要素对于确保实验作为一项严苛测试（severe test）的整体质量而言，都是必不可少的且相互关联的。虽然还存在其他类型的效度（validity）以及略有不同的划分方式，但这四类效度提供了一个坚实的基础。

### 34.0.3.1 结构效度（Construct validity）

结构效度（Construct validity）旨在确保研究者实际测量的内容与预期测量的内容一致。否则，即便测量了某个因变量（dependent variable），实验也无法验证其预设的理论假设。因此，准确且具有实际意义的测量是人机交互（HCI）实验的核心。

结构效度乍看之下似乎显而易见，但实际上，人们很容易在“测量指标是什么”以及“该指标代表什么”这两个方面产生误解。以一个在测量上相对没有争议且与 HCI 密切相关的时间（time）为例。在本研究语境下，时间的定义明确，且可以通过秒表甚至所用系统的内部时钟轻松测量。因此，当实验旨在考察效率（efficiency）时，用户完成任务所需的时间似乎是没有争议的：即从被告知开始任务到停止任务之间的时间间隔。

然而，若将此置于特定任务的语境中，即便像“任务执行时间（time on task）”这样的指标也难以精确定义。例如，假设你正在进行一项关于加热控制器（heating controllers）使用情况的实验，这类设备以操作困难而著称 (Cox and Young, 2000)。实验任务可能是：将加热设备设置为在每个工作日的早上 6 点开启，并在 9 点关闭。用户何时开始任务是很明确的，但他们可能会在*认为*自己已经完成任务时停止操作，而非在*实际*完成任务时停止。例如，他们可能已经将其设置为了

无论是设定为每天早上 6 点开启，还是仅在周一开启，根据控制器的设计，这两者可能是更容易或更难的任务。因此，将测量的时间直接作为任务完成时间（Task Completion Time）是有缺陷的。即使人们已经完成了任务的所有步骤，他们仍可能犯错，导致定时器在下午 6 点而非早上 6 点开启。正确检查时间的过程可能会增加完成时间，尤其是当检查只能通过在操作过程中进行回溯（Backtracking）来完成时。因此，实验者可能会选择仅考虑那些正确完成任务的用户，但这可能意味着丢弃了对于希望设计更好的加热控制器的设计者而言具有潜在重要洞察的数据。而那些能够准确完成任务的人可能无法可靠地代表更广泛的人群，这为测量引入了另一个问题。那么，在这种情况下，正确的时间衡量标准应该是什么？进一步考虑在中断后的恢复时间（time of resumption）或在切换到不同设备后启动操作的时间的测量。这些关于交互设备（interactive devices）使用的问题非常有趣，但其测量并非简单地启动秒表即可完成。实验设计需要明确计时开始和停止的有意义的时间点，研究人员需要对此做出谨慎的决定，例如 Andersen et al. (2012)。

越来越多地，人机交互（HCI）不仅关注时间等客观指标（objective measures），还关注与 [用户体验（user experience）](https://www.interaction-design.org/literature/topics/ux-design) 相关的主观指标（subjective measures），例如对 [美学（aesthetics）](https://www.interaction-design.org/literature/topics/aesthetics) 的欣赏、对游戏的享受或对网站的挫败感。尽管目前出现了一些使用客观指标的趋势，如眼动追踪（eye-tracking, Cox et al., 2006）或生理指标（physiological measures, Ravaja et al., 2006），但这些指标仍需追溯到用户的实际体验，而这只能通过询问用户其体验来完成。

在某些情况下，一个简单的直觉性问题，如“你对那个游戏的沉浸感（immersed）程度如何（1-10分）？”，可以提供一些见解，但始终存在参与者并未在正面回答该问题的风险。

但实际上，他们回答的是他们能够回答的内容，例如他们对游戏的喜爱程度 (Kahneman, 2012)，或者他们认为自己应该回答的内容 (Field and Hole, 2003)。尽管如此，这类问题在人机交互（Human-Computer Interaction, HCI）领域依然屡见不鲜，应当对其结构效度（Construct Validity）持怀疑态度：我们*如何*才能确定它们真的测量了其声称要测量的内容？

因此，问卷是标准化和量化广泛主观体验（Subjective Experiences）的有用工具。问卷背后的理念是，人们无法直接且准确地表达自己的体验：一个人的沉浸感（Immersion）在另一个人看来可能是愉悦感（Enjoyment）。相反，在人们的思想中存在着内部构念（Internal Constructs），也称为潜变量（Latent Variables），这些构念普遍存在于人们的思维中，但很难被直接触及。尽管如此，人们认为这些构念是有意义的，而且是可以被测量的。只要这些构念能够被有意义地揭示，其测量结果就可以在不同个体之间进行比较。问卷旨在通过人们能够触及的思维，间接地询问关于单个内部构念的不同方面。通过结合这些可触及思维的答案，可以将有意义的数值赋予这些（[不可触及的](https://www.interaction-design.org/literature/topics/accessibility)）潜变量。例如，虽然一个人可能并不真正理解

关于沉浸感（Immersion）在学术上的含义，参与者可能能够更可靠地报告他们感觉自己仿佛脱离了日常生活的琐事，或者失去了时间感等等 (Jennett et al. 2008)。由这些项组成的问卷更有可能构建出关于沉浸感的可靠图景。

仅仅拥有一个问卷并不足以保证其结构效度（Construct Validity）。优秀的问卷设计本身就是一个研究挑战 (Kline, 2000)。首先，需要极其谨慎地设计才能产生一个具有潜力的问卷，随后还需要投入更多工作来证明它在现实情境中具有相关性。可以理解的是，人机交互（HCI）在很大程度上依赖问卷来获取主观体验（Subjective Experiences），但许多问卷并不像声称的那样稳健。专门为某个实验设计的问卷存在与直接提问相同的缺陷：[社会期望偏差](https://www.interaction-design.org/literature/topics/desirability)（Social Desirability）、缺乏一致的含义，以及回答了另一个（更简单的）问题。

此外，更严重的错误是利用实验来证明新问卷的效度：“本实验表明手势界面更容易学习，并且进一步验证了我们的问卷作为[学习易用性](https://www.interaction-design.org/literature/topics/ease-of-use)（Ease of Learning）衡量标准的有效性”——这是一种循环论证（Circular Argument），仅表明了该实验显示了

手势界面（Gestural Interfaces）似乎有些不同。即使在问卷（Questionnaires）设计得更为精细的情况下，人机交互（Human-Computer Interaction, HCI）领域仍然存在一个重大问题，即这些问卷是否设计得足够完善 (Cairns, 2013)。

总而言之，无论所采用的测量指标是关于客观变量（Objective Variables）还是主观体验（Subjective Experiences），每项实验都需要一种方法来衡量实验操纵（Experimental Manipulation）的效果。所有此类测量方法都可能存在缺陷，因此至少需要谨慎地选择一种合理且有据可依的测量方式。

### 34.0.3.2 内部效度（Internal validity）

如果一项实验旨在严谨地测试影响因素 X 是否真的影响结果 Y，那么必须明确 Y 的任何系统性变化（既然我们通过构念效度（Construct validity）确认我们确实在测量 Y）完全是由 X 的变化引起的。这就是内部效度的问题。

对内部效度最明显的威胁来自混淆变量（Confounding variables）。这些是除 X 之外可能影响 Y 的因素，因此当 Y 发生变化时，我们无法证明是*仅由* X 导致 Y 发生变化，从而导致我们的实验不够严谨。考虑一个旨在测试公司网站的 [信息架构（Information Architecture）](https://www.interaction-design.org/literature/topics/information-architecture) 对人们对该公司信任度影响的实验。在操纵信息架构时，一名热心的研究人员可能会对网站的其他方面（如颜色的使用或标志）进行“改进”。因此，在解释公司信任度测量结果时，不同版本的网站之间在信任度上的任何差异，可能归因于网站美学质量的提升，而非网站信息组织的修订。修订后的美学设计就是一个混淆变量。不过，可能还存在一些即使是细心的研究人员也无法避免的更微妙的影响。信息架构可能正被

为了更好地对公司的服务进行分类而进行了修订，但在这样做时，修订可能会导致[导航栏（navigation bars）](https://www.interaction-design.org/literature/topics/navigation-1)变得更短。这使得用户能够更快地做出选择，从而增强其进度感（sense of progress），最终提升整体的用户体验（user experience），包括对公司的信任感。这并非信息架构（information architecture）改进的结果，而仅仅是菜单缩短所致——任何合理的菜单缩短可能都会产生同样好的效果！混淆变量（Confounding variables）可以通过各种与实验操纵（experimental manipulation）无关的方式潜入实验中。其中一些比其他变量更容易被察觉，例如，将所有男性都放在一个

……实验的某个条件（condition）下全是男性，而另一个条件下全是女性，这意味着参与者的性别就是一个混淆变量（confounding variable）。一个不那么明显的例子是，在一个条件下只有 Google Chrome 用户，而在另一个条件下只有 Firefox 用户。除非实验者专门询问浏览器使用情况，否则这一点完全无法被察觉。在这两种情况下（例如在一项关于移动设备文本输入速度的实验中），可能没有明显理由认为这些差异具有相关性，但不能排除它们是导致结果出现系统性差异（systematic variation）的原因。因此，它们是潜在的混淆因素（potential confounds）。其他混淆因素可能包括：参与者参加实验的时间点；对所使用的任务、硬件或软件的熟悉程度；实验者问候参与者的方式；进行实验的房间等。这个列表可能是无穷无尽的。

消除混淆因素通常有两种通用方法。第一种是将参与者在不同的实验条件之间进行随机化（randomize）。第二种是对潜在的混淆因素进行实验控制（experimentally control）。在随机化中，假设如果参与者被随机分配到不同的实验条件中，那么条件之间就不可能出现系统性差异。尽管如此，如果你怀疑可能存在潜在的混淆因素（例如对特定 Web 浏览器的使用经验），那么询问相关情况是一个好主意，即便只是为了……

将其视为混淆变量（confound）而予以排除。此外，这还提供了将此类混淆变量作为统计分析中因素（factors）的机会，从而对这些混淆变量实施统计控制（statistical control）。然而，在实验控制（experimental control）中，其方法是消除参与者之间可能产生混淆效应的差异：例如，所有实验都在同一个房间内进行；仅邀请男性参与研究（Nordin et al., 2014）；在允许参与之前对参与者的技术使用情况进行筛选，等等。即便采用了实验控制，也不可能消除所有可能的混淆变量，而只能消除实验者能够预先想到的部分最严重的问题。

除了混淆变量之外，内部有效性（internal validity）还面临另一种威胁，我将其称之为实验漂移（experimental drift）。在开发任何实验的过程中，必然需要就所选参与者、他们执行的任务、系统的设置方式等方面做出决定。所有这些决定都必须在一定程度上具有实用主义（pragmatism）色彩：如果你无法联系到任何来自前工业时代文化的人，那么即使你对前工业时代文化如何与触摸屏界面交互有一个绝妙的想法也毫无意义！然而，在某些情况下，最初一个合理的实验想法会在设计实验的实际考量中被逐渐削弱。这在 HCI（人机交互）领域旨在……的研究中尤为普遍。

探讨一些对以用户为中心的设计流程（User-Centred Design process）的影响。例如，一个非常具有探讨价值的问题是，可用性设计模式（Usability Design Patterns, Tidwell, 2005）是否能提高交互系统（Interactive Systems）的可用性。因此，理想的实验方案应当是：由两个技能水平相当的团队开发同一个系统，其中一个团队使用设计模式，而另一个则不使用，随后对这两个设计方案的可用性进行评估。然而，极少有商业公司愿意投入精力和成本，让两个团队去开发同一个系统，因此非商业环境更具可行性。幸运的是，许多研究人员在大学工作，因此可以利用现有资源，用学生来替代商业设计团队；而且，可以组建多个团队来执行相同的设计任务。如果这项工作是人机交互（HCI）课程模块的一部分，并且作为该模块的考核内容，那么学生的积极性会最高；此外，可以专门向部分学生教授设计模式，而不对其他学生教授，以观察学生如何使用这些模式。但显而易见，这已经发生了巨大的偏差：研究对象从使用模式的专业设计团队，变成了使用一项可能刚刚学到的技术的初级设计师（Novice Designers，即学生）。除了过程中可能引入的所有混淆变量（Confounding Variables）之外，即便实验得出了预期的结果，它是否真的证明了使用设计模式能提高最终产品的可用性？

实验在最好的情况下，也仅是对最初提出的因果假设（causal idea）进行间接的验证。因此，内部有效性（Internal validity）只能通过一种审慎的过程来维持，即对初始实验设计进行迭代审查，以确保其整体连贯性（overall coherence），并识别该设计可能引入的潜在混淆变量（confounds）。

### 34.0.3.3 外部有效性（External validity）

实验自然地将一个具有广泛适用性的通用问题，简化为实际执行的实验的具体细节。随之而来的问题是，实验结果在多大程度上具有预期的更广泛的适用性。这就是实验的外部有效性（External Validity）或可推广性（Generalisability）。

在所有实验中，外部有效性都是一个判断问题。对于一个典型的人机交互（HCI）实验，某些人在特定的情境下被要求执行某些任务。实验的外部有效性是指实验结果在多大程度上可以推广到在其他情境下执行其他任务的其他人群。为了说明这一点，考虑一项关于基于加速度计的控制（Accelerometer-based controls）对手机数字游戏体验影响的实验。自然的推广是从玩家样本（Sample）推广到更广泛的普通玩家群体。但这个更广泛的群体由什么构成？这在很大程度上取决于参与者：他们的游戏经验范围如何；他们对基于加速度计的控制以及移动设备的经验如何；参与者是什么类型的人，无论是年轻人、老年人、男性、女性还是儿童，等等。极大的样本具有更强可推广性的潜力，但即便如此，如果该样本是从大学的本科生群体（Undergraduate population）中收集的——这种情况非常普遍（Sears, 1986）——那么推广

将结果推广至非本科生群体可能是不成立的。该实验也可以泛化（Generalise）到与其他实验中所用手机类似的设备。例如，如果研究使用了 iPhone，那么将结果推广到尺寸相近的 Samsung Galaxy 手机可能是合理的。但这些结果是否适用于 iPad、Kindle，以及像 PS Vita 或 Nintendo DS 这样非手机类的设备？同样，这些结果是否也适用于其他游戏？通常这类实验仅使用一两款游戏，正如所有的人机交互（Human-Computer Interaction, HCI）实验都会让参与者完成一组少量的任务一样。因此，实验结果是否适用于所有游戏？还是仅适用于与所用游戏相似的游戏？如果是后者，那么“相似”到什么程度？

有趣的是，关于这种跨设备和任务的泛化（generalisation），我们在人机交互（Human-Computer Interaction, HCI）领域很少像对待跨人群的泛化那样给予同样的[强调](https://www.interaction-design.org/literature/topics/emphasis)。一个希望将结果泛化到游戏的真实验（true experiment），实际上应该像我们通常在人群总体中抽样一样，在游戏的总体中进行抽样。随后，这一因素应当被纳入分析之中。但这种情况几乎从未发生，我所知道的唯一例子是 Hassenzahl and Monk (2010)，他们旨在通过对参与者和产品同时进行抽样，来克服之前在关联美学（aesthetics）和感知可用性（perceived usability）方面存在的方法论问题。而这仅仅是任务的一个方面。对于像基于加速度计的交互（accelerometer-based interactions）这类交互，以及许多其他交互模态（interactive modalities），存在一些可以微调的参数和设置，这些设置可能会对人们的交互体验产生显著影响。

因此，外部有效性（external validity）的真实程度可能很难判断。我的感觉是，我们在引用他人工作时，为了能将其应用于自己的研究，可能会过于急切地声称其具有比实际情况更广泛的相关性。当然，所有实验都旨在成为更普遍现象的特定实例，但在 HCI 中，在实验设计时更明确地考虑所有三个方面（不仅是人 H，还包括计算机 C 和交互 I）的泛化，似乎仍有提升空间。

### 34.0.3.4 生态有效性（Ecological Validity）

外部有效性（External Validity）关注的是实验结果在多大程度上适用于其他情境，即如果进行相似但非完全相同的实验，是否会产生相同的结果。相比之下，生态有效性（Ecological Validity）则关注实验结果在现实世界中的相关性，即人们在日常生活中将交互系统（Interactive Systems）作为生活一部分而使用的真实场景。

一个简单的例子是对比不同版本的地图 App，以观察用户是否能更高效地在城市的旅游景点之间进行导航。显然，出于实验目的，参与者会被分配一项导航任务，且该任务可能设定在真实的旅游目的地（对于居住在历史底蕴深厚的 York 市的我来说，这很容易实现）。例如，我们可能会要求参与者从火车站导航至城市城堡。这看起来很合理，但这是否真实反映了游客使用地图 App 的方式？也许有些游客在出发时心中已有明确的目的地，但沿途会允许自己被其他事物吸引而分心。另一些游客可能更倾向于漫无目的地闲逛，对目的地仅有模糊的认知，直到需要返回酒店时，才会使用 App——此时 App 的作用不仅是提供导航，更是告知他们当前所处的位置。或者也许

他们根本不会使用这个 App，而是更倾向于传统的旅游指南，因为后者能在一个便捷的套装中提供大量信息，尤其是量身定制的地图！

实验与实际使用之间的这种相关性，正是人机交互（Human-Computer Interaction, HCI）领域中生态效度（Ecological Validity）的核心所在，且经常被深入讨论。许多研究确实非常重视生态效度，并力求在尽可能真实的语境中开展研究。最极端的例子是 Google 所采用的测试方式，即不同的用户直接看到不同的界面。这并非是为了观察人们如何使用这些界面而设计的场景，而*就是*人们在使用这些界面。这种方式的生态效度已达到了极致。然而，高生态效度的代价通常是实验控制（Experimental Control）的丧失。在真实用户使用真实系统的环境下，可能存在许多其他潜在影响因变量（Dependent Variable）的因素。也就是说，具有生态效度的研究存在许多潜在的混淆变量（Confounds）。Google 可能不需要担心这些问题，但在效应较小或旨在开发底层交互理论的情况下，规模较小的实验始终需要在内部效度（Internal Validity）与生态效度之间进行权衡（Trade-off）。

### 34.0.3.5 整体效度（Validity as a whole）

对于所有实验而言，在各项效度（Validity）方面总会存在折中，至少在生态效度（Ecological Validity）方面如此，因为为了实现实验控制（Experimental Control），必须对现实世界的某些方面进行限制。尽管如此，实验并不一定得完全脱离实际。例如，Anna Cox（个人通信）设计了一个精心构思的实验来研究人们如何管理电子邮件，但为了建立更好的生态效度，她自然地采用了实地研究（in-the-wild style of study）的方式。

根据实验中测试想法的复杂程度，需要做出不同的折中。内部效度（Internal Validity）的提升可能会以牺牲外部效度（External Validity）为代价。过多的实验控制会导致结果无法泛化（Generalise）到各种不同的任务甚至系统中；而实验控制不足则可能会损害内部效度。虽然使用总体的通用样本（General sample of the population）是理想的，但这可能会在实验中产生大量的自然变异，从而掩盖代表实验目标的任何系统性差异（Systematic differences）。用户体验（User Experience）的某些方面可能非常难以衡量，例如文化或信任，因此为了在该领域取得进展，你可能不得不依赖于一个较弱的，或者充其量是一个验证不足的构念（Construct）。

归根结底，所有的实验都并非完美。效度方面总会存在折中，研究人员只能诚实地……

明确具体采取了哪些折衷（compromises）方案。正如前文所述，单次实验永远不足以得出结论，因此，最好的做法或许是承认这些折衷之处，并在接下来的实验中进行改进（或至少尝试不同的方法）。

### 34.0.4 统计分析（Statistical Analysis）

任何在统计学方面有一定名声（无论多么微小）的人都会告诉你，他们经常会收到类似这样的请求：“我刚刚做了一个实验，但不知道该如何分析数据。”这种情况在人机交互（Human-Computer Interaction, HCI）领域（根据我的经验，在心理学领域也是如此）屡见不鲜，因为学习必要的统计方法并非易事。这不仅耗时费力，而且与 HCI 研究者的核心工作并不直接相关——他们从事 HCI 研究并不是为了学习大量的统计学！虽然研究人员可能（相对）快速地学会如何设计一个合理的实验，但要对什么才构成适当的统计分析充满信心，则需要花费更多的时间 (Hulsizer & Woolf, 2009)。

然而，问题在于统计分析并不是实验方法中一种仪式性的“附加项（tag-on）” (Gigerenzer, 2004)，它对于实验的成功至关重要。面对人们在利用交互设备实现各种目标时所表现出的自然变异（natural variation），无法确定实验操纵（experimental manipulation）是否真的以某种系统性的方式影响了因变量（dependent variable）。观察这一点的一种方法是考虑一个具有两种条件的实验，其中每位参与者在满分为 100 分的测试中获得分数。如果你发现每组 20 名参与者的平均分……你将会（且应当）感到非常惊讶。

如果实验条件的结果完全相同，你至少会怀疑这是一个复制粘贴错误。当一项研究中不同条件之间的平均分（mean scores）出现差异时，这是在预料之中的。此时需要统计学（Statistics）来帮助识别这些差异是系统性的且与自变量（independent variable）有显著关联，还是仅仅是随时可能出现的自然变异（natural variation）。即使可以进行统计分析并得出了强有力的结果，也不一定能保证绝对的确定性。有时，两个不同随机样本（random samples）之间的自然变异可能会强到看起来就像是系统性变异（systematic variation）。这对实验者来说纯粹是运气不好。一个强有力的统计结果充其量只能作为支持实验目标的证据。相反，如果实验者

如果对数据的不同方面进行大量测试，那么纯粹出于偶然，其中一些测试很可能会显示出系统性差异（Systematic variation）。仅凭统计数据本身无法提供充分的证据。

统计分析的强度源于将实验视为一种“严苛测试（Severe test）”的概念。实验的设置是为了对某个特定想法进行严苛测试，从而在想法错误时，实验极有可能揭示这一点。统计分析应当通过直接针对研究目标来支持这一严苛测试，而任何其他分析（无论其结果多么有趣）都不能真正支持该测试。

例如，考虑一项关于使用手势（Gestures）控制车载音乐播放器的研究。手势可以通过避免驾驶员在选择曲目或电台时关注小屏幕或小按钮，从而提高安全性。因此，研究者设计了一个实验，让驾驶员在监控其车道保持性能（Lane-keeping performance，在模拟环境下！）的同时，尝试不同的交互方式。在分析中，发现交互方式之间没有统计学显著（Statistically significant）的差异，但基于敏锐的洞察力，实验者怀疑这可能是由于参与者的惯用手（Handed-ness）差异造成的。果然，当将参与者的惯用手纳入分析因素后，结果变得显著，且更容易解释。这就是成果！

但这项实验并不是对驾驶过程中手势交互（gestural interactions）中惯用手差异（handed-ness differences）的严苛测试，因为如果实验者真的对这些差异感兴趣，那么实验中应该会有计划内的、而非偶然的操纵（manipulation）。实验的设计不会像现在这样。例如，样本会刻意尝试在右撇子和左撇子之间保持平衡。

但在解决了这个问题之后，人们习惯于在道路的哪一侧行驶可能也具有相关性，因为这决定了哪只手预计在换挡（gear changes）时处于空闲状态，从而影响其他手势。实验设计也应当将此因素考虑在内。因此，用来测试这一想法的实验现在与最初将惯用手视为偶然因素的实验截然不同。

这明确地基于我之前称之为“金标准统计论点（gold standard statistical argument）”的观点 (Cairns & Cox, 2008)。在该论述中，实验的目的至关重要，因为预测使得低概率事件变得有趣。如果没有预测，低概率事件就只是偶尔发生的事情。这也是许多魔术背后的原理：一些极低概率的事件（例如一手牌拿到四张 A，或猜出某人秘密选择的卡片），虽然偶尔可能凭运气发生，但在观众面前一次性完成。一项实验可能会偶然地呈现出某种结果，但它

这具有重要意义，因为实验结果在实验者预言的情况下，在第一次尝试（first go）时就发生了。然而，在严苛测试（severe testing）下，这种影响力甚至更强，因为预测构成了实验结构的基础。如果预测不同，那么进行的将是一个完全不同的实验。

有趣的是，即使是对经验丰富的研究人员而言，这一点也并非总是显而易见 (Cohen, 1994)。针对零假设显著性检验（null hypothesis significance testing, NHST）存在大量批评，而这正是大多数人在谈论统计学时所想到的常规检验方式。在 NHST 中，实验包含一个对立假设（alternative hypothesis），即实验中所探讨的因果预测（causal prediction）。面对自然变异（natural variation），很难“证明”对立假设成立；因此，实验者转而提出一个零假设（null hypothesis），即预测不成立且不存在效应。随后，这一假设被用于计算：如果实际上确实没有任何影响，那么在实验中获得当前数据的概率是多少。这便产生了统计学中备受推崇的经典 p 值（p value）。p 值是指纯粹由偶然因素获得该数据的概率，也就是说，在零假设成立且预测（即对立假设）错误的情况下，获得该数据的概率。对这种方法的批评在于，统计计算中使用的是零假设而非对立假设，因此我们无法了解到关于...

我们预测的概率，而这无疑才是我们真正感兴趣的 (Cohen 1994)。

但这在逻辑上是不严密的。其谬误（Fallacy）在于，整个实验都是围绕着预测而设计的：零假设（Null Hypothesis）是唯一考虑与预测相反情况的地方。（关于实验语境下概率含义的许多模糊思考也与此直接相关，但那是以后讨论的话题了。）回到那位设计了实验但未设计统计分析（Statistical Analysis）的研究者，显然他们正陷入困境，原因有很多。首先，如果他们不知道该分析什么，那么这表明实验*能够*测试的观点尚未被清晰地阐述。其次，这也表明他们可能正在寻找

为了获得一个实验根本无法提供的“显著结果（significant result）”，这种情况通常被描述为“钓鱼（fishing）”。当研究想法阐述清晰，但分析结果并未达到预期时，解决方法可能仅仅是帮助研究者意识到，一个设计良好的实验即便以“失败”告终，其本身也具有价值。虽然这不像获得显著结果那样令人兴奋，但它可能同样具有深刻的洞察力。追求显著性的“钓鱼”行为并非解决之道。

鉴于将实验设定为“严苛测试（severe test）”所面临的挑战，以及此类测试所能提供的结果较为狭窄，研究者可以采取一种退而求其次的立场，即：实验可以用来探索多种因素对特定交互或体验结果的潜在影响。在这种情况下，实验不再是一次严苛测试，因为并没有某个特定的想法被置于极端的压力之下。因此，统计学不可能为任何特定因素影响实验结果提供证据。统计学能指示的是，某些结果可能比预期更不寻常，因此值得进一步研究。对于更复杂的实验设计而言，这似乎是一个相当无力的“退路（out）”，但对于那些认为这无关紧要的研究者，我的回应将是询问他们究竟在采用什么样的实验哲学（philosophy of experiment）。面对自然变异（natural variation）和不确定性，什么才构成证据并非易事。

### 34.0.4.1 安全的分析（Safe analysis）

考虑到统计分析中存在相当危险的陷阱，且统计学是一个难以掌握的领域，我建议采用工程师们熟知的一种解决方案：保持简单（keep it simple stupid, KISS）。根据严苛测试（severe testing）的理论，实验应当将关于世界运作方式的某种观点置于严苛的条件下，以观察该观点是否能够预测将要发生的事情。但正如前一节所述，实际的实验必须在许多方面缩小范围，从而使其仅成为对该观点中某个单一方面的测试。没有一项实验能够测试整个观点 (Mayo, 1996)。因此，意识到这一点后，进行多次实验总是更好的选择。没有必要期望一次实验就能提供所有结果。此外，如果每个独立的实验都能提供清晰且无歧义的结果，那么这比一个设计复杂且分析更为复杂的庞大实验要好得多。更简单的实验实际上是更严苛的测试，因为在这种情况下没有掩饰的空间：某个事物要么清晰地通过了测试，要么没有。

那么，什么样的简单设计能带来简单且安全的统计分析？以下是我向任何研究人员推荐的一些简单规则：
- 自变量（independent variables）不超过两个，理想情况是一个
- 每个自变量最多三个条件（conditions），理想情况是两个
- 仅设置一个主要因变量（primary dependent variable）（尽管你应该测量其他指标，以解释替代性解释（alternative explanations）或偶然因素

（混淆变量 Confounds、实验操纵 Experimental Manipulation 等）
这些要求看似非常苛刻，但其理由充分：此类设计的统计检验非常直接。目前已有成熟的参数检验（Parametric Tests）和非参数检验（Non-parametric Tests），无论是在应用还是在结果解释方面都易于理解；且针对两种条件的检验比针对两种以上条件的检验更为简单。这可能显得过于限制，但请记住“严苛测试（Severe Test）”的概念：如果存在更多的自变量（Independent Variables）或因变量（Dependent Variables），那么究竟在被“严苛地”测试的是什么？此外，如果存在大量条件，是否对每种条件下会发生的情况有明确的预测？如果并非如此，那么该实验就不是在测试一个形式完备的预测。

让我们看看这在实践中是如何运作的。假设你对老年人使用的触摸屏界面最佳布局（Layout）感兴趣。即使仅考虑按钮，也有许多潜在的重要因素：按钮尺寸、按钮间距、按钮上的文本、[网格（Grid）](https://www.interaction-design.org/literature/topics/grid-systems) 或交错布局（Staggered Layout）等。如果你对该领域完全不了解，首要任务是确定这些因素中是否有任何一个*单独*影响老年人对触摸屏设备的使用。以按钮尺寸为例。总体目标可能是

为了确定哪种按钮尺寸（button size）最佳。但如果你甚至不知道按钮尺寸能产生多大的影响，那么为什么要尝试十几种不同的尺寸呢？尝试那些在合理范围内被认为是最极端的两端——即极小和极大。事实上，仔细想想，在大多数平板电脑或智能手机上，并没有太大的空间去设置一个巨大的尺寸范围。如果极端的两端没有产生显著的差异（appreciable difference），那么更为接近的尺寸也不会带来更好的效果。只有在按钮尺寸确实产生影响的情况下，才值得去研究它如何与按钮间距（button spacing）产生交互作用。

剩下的问题是，布局（layout）中的“最佳”是指什么。是指速度（speed）和准确率（accuracy）吗？这两项指标通常被共同测量，因为两者之间往往存在速度-准确率权衡（speed/accuracy trade-off, Salthouse, 1979）。即便如此，在本文的研究语境下，哪个更重要？如果速度的影响较小，那么准确率可能更为关键。因此，准确率成为了主要的因变量（dependent variable），而速度仅作为一种可能的保障，用以排除那些与按钮尺寸无关的解释。            Certificates当然，作为优秀的人机交互（Human-Computer Interaction, HCI）研究者，我们始终关注用户体验（User Experience, UX）。用户更倾向于哪一种？这是一个完全不同的问题。当然，它可以与速度（speed）和准确率（accuracy）一起进行衡量，但如果某种布局（layout）的准确率很高但用户偏好较低，那么哪一种才是最优的？而且，如果准确率无关紧要，那么一开始就不要衡量它。那只是一个干扰项（red herring）！

研究者往往倾向于设计一个复杂的实验，试图一次性考察所有这些因素，但这会导致分析难度迅速增加，并增加了过度测试（over-testing）的可能性 (Cairns, 2007)。相比之下，显而易见的是，针对不同变量（variables）的一系列实验能够提供更加明确的答案。此外，如果多个不同的实验构建出了一个一致的结论，那么关于“最优布局”的证据就充分得多，因为单一实验始终存在仅凭偶然获得良好结果的可能性。在大量实验的情况下，这种情况较少发生；而如果这些实验彼此不同，则更不可能出现这种情况。

### 34.0.4.2 解读分析结果

在设计了一个易于分析的实验之后，同样重要的是不要在解读统计检验结果这一最后关头出现失误。在传统的零假设显著性检验（Null Hypothesis Significance Testing, NHST）风格的统计分析中，所有统计方法最终都会产生一个统计量（statistic）和一个 p 值（p value）。p 值是指实验结果纯粹由随机偶然因素导致的概率。显著性阈值（threshold of significance）几乎总是设定为 0.05，因此，如果随机结果出现的概率低于 1/20，则该实验结果被宣布为具有显著性（significant）。表 1 总结了其他一些重要的阈值。这些阈值纯粹是约定俗成的，在这一惯例之外并没有特定的科学含义；但在该惯例之内，如果一项检验得出的 $p < 0.05$，则被认为具有显著性，且实验被视为“奏效”了。也就是说，实验提供了支持对立假设（alternative hypothesis）的证据。如果 p 值大于 0.05，则实验被认为未奏效，且零假设（null hypothesis）的可能性更大。

但这并不是一个完全客观的概括。由于这些阈值是约定俗成的，我们需要意识到这些惯例明显的随意性，而不要做出如此非黑即白的解读。因此，特别是当 p 值接近 0.05 但略高于它时，实验有可能正按预期发挥作用，但

可能存在一些问题，例如样本量较小、数据中存在噪声源（source of noise）或任务聚焦不足，这意味着实验无法给出明确的答案。未能达到 0.05 的阈值（threshold）并不意味着没有任何现象发生。事实上，任何不显著（insignificant）的结果并不支持“没有任何现象发生”这一结论，而仅表明本次实验未能显示出预期的情况。因此，当 $p < 0.1$ 时，通常将其视为趋于显著（approaching significance）或边缘显著（marginally significant），并且应非常谨慎地将其解释为具有潜在的研究价值。

| **p 值 (p-value)** | **典型描述词** | **典型但欠谨慎的解释** |
|---|---|---|
| 0.1 < p | 不显著 (Not significant) | 预测不成立 |
| 0.05 < p ≤ 0.1 | 边缘显著，趋于显著 | 预测很可能成立，但未必成立 |
| 0.01 < p ≤ 0.05 | 显著 (Significant) | 预测相当确定成立 |
| 0.001 < p ≤ 0.01 | 显著，高度显著 (Highly significant) | 预测确实成立 |
| p ≤ 0.001 | 显著，高度显著 | 预测确实成立 |

**表 1：解释 p 值的传统阈值及其僵化的解释方式**

在另一个极端，当 p 值非常小（例如 0.001 甚至更低）时，这并不意味着它比其他任何小于 0.05 的 p 值更具说服力或更重要。此类数值确实可能由随机偶然产生（百万分之一的机会发生的频率比你想象的要高得多...

（取决于你如何界定它们）但如果在实验中预期会有某种效应，那么这样的小数值也应当出现。正因如此，至少在心理学领域，目前有一种趋势是尽可能地始终报告效应量（Effect Sizes）。效应量是衡量重要性的指标，因为它们表明了实验操纵（Experimental Manipulation）对数据中观察到的差异产生了多大的影响。但与 p 值（p-values）不同，关于什么构成了“重要的效应量”并没有统一的惯例，这取决于你所进行的[研究类型](https://www.interaction-design.org/literature/topics/type)以及什么样的效应被认为是重要的。与 t 检验（t-tests）配合使用的一种效应衡量指标是 Cohen’s d。该统计量基本上比较了两个...之间的均值差异。

将实验条件与参与者中观察到的基础变异水平（Base Level of Variation）进行对比。这种变异由收集到的数据中的合并标准差（Pooled Standard Deviation）来表示，但如果你（目前）还不确定这意味着什么，不必担心。$d$ 值为 1 大致意味着实验条件产生的效应与参与者之间的 1 个标准差相当，即参与者之间的平均变异。这是一个非常大的效应，因为与自然变异（Natural Variation）相比，实验操纵（Experimental Manipulation）很容易被察觉。相比之下，$d=0.1$ 意味着参与者之间的平均变异远大于实验条件引起的变异，因此该效应不易被察觉。有趣的是，在样本量较大的情况下，出现 $p < 0.001$ 但 $d$ 值较小的情况是有可能的，而且实际上很常见。这应被解释为条件之间存在系统性差异（Systematic Difference），但这种差异很容易被其他因素所掩盖。与 $p$ 值不同，这类微小效应的重要性在很大程度上依赖于具体情境（Context Dependent），因此需要实验者给出明确的解释。

进一步思考，一个产生显著效应（Significant Effect）的小样本也更有可能展示出较大的效应。也就是说，一个能产生显著性结果的小样本，潜在地比大样本更具说服力！这与许多关于实验样本量的建议相反，但这是思考……的结果

将实验视为严苛检验（severe tests, Mayo and Spanos, 2010）。如果一个想法能够预测出稳健的效果（robust effect），那么在进行严苛检验时，这种效果在小样本中也应当可见。小样本确实会对普适性（generalizability）产生威胁，并增加由于少数参与者之间偶然出现的持续性差异而导致混淆变量（confounds）的风险。即便如此，在没有出现这些差异的情况下，小样本反而能提供更具说服力的证据！

效应量（effect sizes）真正的难点在于，它们仅在参数检验（parametric tests）中容易生成，即数据遵循经典正态分布（normal distribution）钟形曲线的情况。但在人机交互（HCI）的许多场景中，数据并非如此。例如，关于用户错误次数的数据通常呈现所谓的长尾分布（long-tailed distribution）：大多数参与者仅犯极少错误，少数人犯数次错误，而一两个人则犯大量错误。此类数据只能使用非参数检验（non-parametric tests）进行稳健分析，而这些检验无法简单地提供效应量的衡量指标。虽然目前出现了一些可用于非参数场景的效应量衡量方法（Vargha and Delaney, 2000），但它们尚未被广泛使用，因此也不被广泛理解。但希望这仅仅是时间问题，且这或许是 HCI 社区（尤其是计算机科学领域）可以发挥引领作用的方向。

总而言之，统计分析应当作为……的一部分进行规划。

在实验中，应尽可能优先采用简单设计而非复杂设计，以确保结果的解释具有清晰度。此外，在可行的情况下，效应量（effect sizes）为评估结果的重要性提供了一种有效的方法，尤其是在结果呈现极显著（very significant）或边缘显著（marginally significant）的情况下。

### 34.0.5 实验报告撰写（Experimental Write-up）

实验设计和统计分析为何是实验开发中的重要支柱，这一点应该是显而易见的。但为什么报告撰写（write-up）也足够重要，以至于被视为一个支柱，这一点可能就不那么明确了。当然，以论文或学位论文形式提交的报告对于传达实验结果并获得对其工作的认可至关重要。Hornbaek (2013) 阐述了报告撰写的许多重要特征（我建议读者在阅读本节的同时也阅读该文章），其核心在于使读者能够追踪所呈现的证据链（chain of evidence）并认可其价值。但需要明确的是，人们撰写实验报告并非是为了让其被复现（replicated）：如果一名研究人员复现了一项实验，即使复现看起来至关重要，他们可能仍难以发表（Ritchie et al., 2012）。Hornbaek (同上) 认为报告撰写可以辅助实验设计，但我认为其作用更深。实验报告撰写是实验开发中的一个重要支柱，因为它迫使研究者对想法做出承诺（commitment to ideas），从而使实验及其效度（validity）、分析和意义变得可审视（scrutable）。

将此与在学术对话（如导师指导/supervision）中描述实验进行对比。在这种情况下，一些细节可能仍然具有流动性（fluid），并会随着对话的结果而修改。这正是对话的优势，正如 Socrates 所知 (Plato, 1973, *Phaedrus*)。正是通过与他人的交谈和互动，其想法和思考

[这些]能得到最好的揭示。然而，对话是瞬时的，尽管有 YouTube，通常只有在场的人才能接触到。通过将实验描述（experimental description）记录下来，细节通常能得到完整（或至少是大部分）的呈现，并供他人（通常是导师）理解和评议。因此，人们能够以一种审慎且深思熟虑的方式，对实验的效度（validity）进行评议。如果实验在执行后被发现缺乏效度，那么就出现了问题。数据将无法被信赖为具有意义。换句话说，该测试不够严谨（severe），因此对我们的认知贡献甚微。但我认为，实验报告（experimental write-up）不仅可以在进行任何[实验]之前撰写...

实验确实*应该*提前撰写，因为如果没有提前的记录，研究者如何能确定实验*究竟是什么*，更不用说它是否优秀了？

尤其支持提前撰写的一点是，所有实验报告都具有一个或多或少已确立的结构：
- 标题与摘要（Title and Abstract）
- [动机（Motivation）](https://www.interaction-design.org/literature/topics/motivation) / 文献综述（Literature Review）
- 实验方法（Experimental Method）
- 结果（Results）
- 讨论（Discussion）
  - 假设（Hypothesis）—— 正在测试的观点
  - 被试（Participants）—— 参与者的概况
  - 设计（Design）—— 明确自变量（Independent Variables）和因变量（Dependent Variables）
  - 材料（Materials）
  - （任务 Tasks）
  - 步骤（Procedure）

而在“实验方法”部分，还包含定义明确的子章节：
任务（Tasks）并不总是被单独考虑，但这在人机交互（HCI, Human-Computer Interaction）领域是一个特殊问题，正如上文在讨论外部有效性（External Validity）时所提到的，因为任务本身实际上可能是研究对象，而非被试。

文献综述在实验撰写中或许占据着特殊的地位，因为它关注的不是实验本身，而是实验可能意味着什么。从这个意义上说，文献综述有两个目的：首先是证明该实验具有一定的价值，从而提供研究动机；其次是向读者提供足够的解释，使他们能够理解实验所展示的内容。价值的动机要么来自于开展重要的工作，要么来自于开展有趣的工作。例如，一个

旨在减少错误的实验可能具有重要意义，因为它能够节省时间、金钱，甚至挽救生命。或者，它可能仅仅是因为许多人都在关注某个特定问题而具有趣味性，例如，新型游戏控制器是否能带来更好的用户体验（User Experience）。在最理想的情况下，实验既重要又有趣：它既解决了研究社区希望解决的问题，又以其他个人、群体或社会所重视的方式，在研究社区之外产生了影响。

然而，文献综述（Literature Review）本身并不能决定一个实验应当是什么样子：任何实验都没有绝对的必要性，因为就像任何设计的人造物（Designed Artefact）一样，它必须适应其设计的上下文（Context）。相反，文献综述或许可以通过定义一个合适的实验可以填补的知识空白（Gap in Knowledge），来界定一个优秀的实验应该具备的范围。实验者如何填补这一空白则是一个设计问题。事实上，进行高质量的实验甚至不需要文献综述，但如果没有文献综述，风险在于你可能会重复一个已有的实验，或者更糟糕的是，去做一个没有人感兴趣的实验。

关于实验报告撰写（Experimental Write-ups）有很多优秀的教科书。我最推荐的是 Harris (2008)，但这纯粹是个人偏好问题。这些书籍不仅就实验报告的结构（就这些标题而言）提供了清晰的指南，还阐明了每个标题下应包含的内容。

与其在这里重复这些内容，本文的目标是将典型的实验方法章节（method section）撰写方式与前文所述的实验工作的两大支柱联系起来。

结构效度（Construct validity），即“你是否在测量你认为自己在测量的东西”，主要体现在指定因变量（dependent variable）的设计阶段。这必须与被研究的概念相关联，这种关联可以通过显而易见的方式（例如，时间是效率的一种衡量标准）、通过与其他研究对比，或者通过论证其为何是一个有效的衡量指标来实现。后两者应当在文献综述（literature review）中得到明确的阐述。特别是如前所述，如果一个实验既用于验证问卷（questionnaire），又同时用于测试另一个不同的想法，这是没有意义的。此外，拥有一个有效的结构意味着统计分析必须仅专注于该结构。在涉及统计数据时，关于什么构成了严苛测试（severe test）不应存在模棱两可之处。Certificates内部有效性（Internal validity）关注的是混淆变量（confounds）以及实验的相关性。混淆变量通常在材料、任务和流程章节中显现，其中的问题可能源于实验中所使用的工具，或实验中所执行的操作。参与者可能未获得正确的引导，或者在培训过程中存在问题，这些情况通常会体现在材料或流程章节的某些部分。此外，参与者本身也可能成为混淆变量的来源，因为某些参与者在与实验任务相关的方面比其他人更具经验。起初，这类问题可能并不明显，但在撰写这些章节时，不仅应当允许质疑的出现，而且应当积极鼓励这种质疑。

内部有效性同样贯穿于统计分析之中。当一项实验旨在建立明确的因果关系（causal connection）时，所有的统计分析都应围绕于验证该关系在所收集的数据中是否存在。其他分析虽然可能很有趣，但对研究的内部论证没有贡献，也无法对另一种观点构成严苛的检验。

外部效度（External validity）是指本实验在多大程度上具有其他实验的代表性，以及本实验的结果在多大程度上可以泛化（generalise），并能在其他类似实验中被观察到。参与者和任务是泛化的明显方向，且这些方面需要描述得清晰明确。没有必要具体阐明预期的泛化范围（至少在方法章节中不需要），而应由读者自行判断。但在设计实验时，研究者应当自问：本实验在多大程度上具有可信的泛化能力。

生态效度（Ecological validity）在论文撰写中最难具体说明，本质上需要对实验的整体结构做出综合判断。设计与流程章节基本上描述了实验中发生了什么。在撰写实验报告时，针对某些特定的设计决策，可能会具体提及生态效度，尤其是当它需要与其他形式的效度进行权衡（trade-off）时。不过在某些情况下，无需明确提及生态效度，而可以通过整个实验过程让读者自然地理解。读者必须自行判断，该实验在多大程度上与人与系统之间现实世界的交互具有足够的关联性。

讨论（Discussion）章节是研究者能够为其...进行论证的地方。

……选择并承认已完成实验的局限性。通常，讨论（Discussion）部分仅在结果出炉后才被考虑，因为理所当然地，在知道结果之前，你无法对其进行讨论。但事实并非完全如此。严格来说，一项实验只会产生两种结果之一：相对于被测试的观点存在显著差异（significant difference），或者不存在显著差异。显著性是一个极佳的结果，但如果结果不显著，讨论部分该写什么？通常情况下，在这种情形下，讨论部分会审视实验的局限性，并指出可能导致意外的零结果（null result）的薄弱环节。然而，出于对这类结果的（悲观）预期，这部分内容其实可以提前写好。那么，为什么不先这样做，然后进而优化实验呢？如果实验无法进一步优化，那么这可以作为一项挑战提交给未来的研究者，看他们是否能做得更好，因为归根结底，任何实验都有其局限性。

当然，也可能出现这样的情况：尽管在报告的前文中（推测）已有充分的论据证明应该存在某种效应，但实验中却未观察到该效应（否则为何要进行这项实验）。然而，这凸显了实验研究的一个特定弱点：它们非常擅长展示事物何时具有因果关系（causally related），但并不擅长证明某种效应的缺失。效应的缺失可能是

……是因为该效应难以观察到，而非其确实不存在。实验设计（experimental design）的缺陷、变量测量（measurement of variables）的问题或参与者之间的个体差异（variability between participants）都可能是导致未能观察到效应的原因，因此无法得出绝对肯定的结论。只有在一种情况下，零结果（null result）才可能具有更大的权重：即该效应此前已被强有力地证实，但在某种新情境下未能再次出现。即便如此，实验因素仍可能阻碍该效应的显现。然而，如果实验接近于对其他研究的重复实验（replications），那么零效应（null effects）可能开始变得有趣。在这种情况下，关于零结果的讨论同样可以提前撰写。

当结果显著（significant）时，实验仍然存在局限性。它仅仅是对某个宏大构思中某一个方面的单次测试。那么，哪些局限性会引导后续的研究工作？为了开展这项特定的实验，做了哪些妥协？在未来如何减轻这些影响？还可以通过什么其他方式，以不同的方法测试该构思的同一个方面？此外，还应该测试哪些其他方面？完全可以在报告中准备两个版本的讨论部分，根据分析结果的不同而选择插入其中一个。

当然，任何实验中都存在导致意外结果的细微差别（subtleties）。是的，结果虽然显著，但参与者……

……做了奇怪的事情，或者全部都是重度游戏玩家（heavy gamers），或者讨厌 iPhone。这些内容需要更仔细的讨论，且确实只能在数据收集完成后才能撰写。但即便考虑到这一点，大部分的实验报告（experimental write up）在招募任何一名参与者之前就可以构建完成：包括文献综述（literature review）、实验方法（experimental method）、讨论（discussion），甚至结果部分的框架（skeleton of the results），因为统计分析（statistical analysis）也应当提前确定。此外，如果该实验对你或你的同事来说缺乏说服力，那么你就没有在收集无用数据上浪费时间。在开展研究之前，先为实验撰写一份具有说服力的报告，这样该实验更有可能成为一个优秀的实验。

### 34.0.5.1 总结

论文撰写（write-up）的每个方面都有其必要性。「方法（Method）」部分揭示了效度（Validity）。「讨论（Discussion）」部分解释了在效度方面所做的妥协，并探讨这些妥协是否在可接受范围内。「结果（Results）」部分则提供了支持讨论的分析。这些部分共同使任何实验对于他人而言都是可审查的（scrutable）；但更有用的是，在进行实验之前，它们可以使实验对于实验者本人而言也是可审查的。

我在撰写论文时遵循的一个通用准则（general maxim）是：我的表述必须足够清晰，以至于如果我错了，这一点会变得显而易见。我相信，正是通过这种透明度（transparency）和对诚实的秉持，科学才能够进步 (Feynman, 1992)。在实验报告撰写中，这意味着如果实验得出了错误的结果（尽管我可能无法察觉），那么勤勉的读者应该能够替我发现它。任何研究者的初衷都是尽可能地完成一个完美的实验，但即便有最强的意愿，这也不总是能实现的。论文撰写不仅是为了向读者承认这一点，也是为了向你自己承认。

### 34.0.6 总结实验支柱

实验是人机交互（Human-Computer Interaction, HCI）研究者工具箱中的一种重要方法。实验具有某种容易识别且相对容易模仿的“形式特征（look and feel）”。问题在于，如果研究者仅仅观察实验中那些形式上的、看似具有仪式感的结构，而没有理解这些形式的目的，那么就存在极大的风险，导致所设计的实验无法提供有用的研究贡献，这非常类似于“货物崇拜科学（Cargo Cult Science）”(Feynman, 1992)。

在将实验视为对想法的严苛测试（severe tests of ideas）这一背景下，我在此阐述了构建有效实验的关键支柱，旨在揭示这些形式化要求的深层原因。实验设计（experimental design）的构建是为了确保测试的效度（validity），而实验报告的撰写（write-up）则使这种效度变得可审查（scrutable）。分析过程揭示了数据是否支持被测试的想法，因此它是实验设计中不可或缺的组成部分。此外，撰写过程可以被用作一种建设性工具，使研究者在实验实施之前，能够就实验的有效性与自己以及他人进行对话。

当然，并非所有问题都能通过实验解决，但当人们对世界的运作方式以及事物之间如何相互影响有着清晰的阐述时，实验可以成为一种既严谨又具有说服力的证明方式。实验的强度（The strength of an experiment）

这源于三者的结合：旨在产生高质量数据的实验设计（Experimental Design）；旨在产生清晰解释的统计分析（Statistical Analysis）；以及旨在呈现研究结果的报告撰写（Write-up）。如果缺失其中任何一项，实验都无法对知识做出可靠的贡献。本章进一步认为，如果在开展实验之前认真对待这三个方面，就有可能在人机交互（Human-Computer Interaction, HCI）领域设计出更好、更严谨且更具说服力的实验。

### 34.0.7 References

Abelson, R.J. (1995) *Statistics as Principled Argument*, Lawrence Erlbaum Assoc.
Andersen, E., O'Rourke, E., Liu, Y-E., Snider, R., Lowdermilk, J., 
Truong, D., Cooper, S. and Popovic, Z. (2012) The impact of tutorials on
 games of varying complexity*. Proc. of ACM CHI 2012*, ACM Press, 59-68
Blythe, M., Bardzell, J., Bardzell, S. and Blackwell, A. (2008) Critical issues in [interaction design](https://www.interaction-design.org/literature/topics/interaction-design). *Proc. of BCS HCI 2008 vol. 2,* BCS, , 183-184.
Blythe, M., Overbeeke, K., Monk, A.F., Wright, P.C. (2003) *Funology: from usability to enjoyment. *Kluwer Academic Publishers.
Cairns, P. (2007) HCI. . . not as it should be: inferential statistics in HCI research. *Proc. of BCS HCI 2007 vol 1, *BCS, 195-201.
Cairns, P. (2013) [A commentary on short questionnaires for assessing usability.](http://www-users.cs.york.ac.uk/~pcairns/papers/Cairns_IwC2013.pdf) *Interacting with Computers*, 25(4), 327-330
Cairns and Cox (2008a) Using statistics in usability research. In Cairns and Cox (2008b)
Cairns, P., Cox, A., eds (2008b) *Research Methods for Human-Computer Interaction,* Cambridge University Press.
Card, S. K., Moran, T. P. and Newell A.(1980) The keystroke-level model for user performance time with interactive systems. *Communications of the ACM* , 23(7 ), July 1980, 396-410.
Chalmers, A.F. (1999) *What is this thing called science? 3rd edn.* Open University Press

Cohen, Jacob (1994) The earth is round (p < .05). *American Psychologist*, 49(12), Dec 1994, 997-1003
Cox, A.L., Cairns, P., Berthouze, N. and Jennett, C. (2006) [The use of eyetracking for measuring immersion.](http://discovery.ucl.ac.uk/149050/) In: (Proceedings) workshop on What have eye movements told us so far, and what is next? at *Proc. of CogSci2006, the Twenty-Eighth Annual Meeting of the Cognitive Science Society*, Vancouver, Canada, July 26-29, 2006.
Cox, A. L., & Young, R. M. (2000). Device-oriented and task-oriented exploratory learning of interactive devices. *Proc. of ICCM*, 70-77.
Dowell, J. , Long, J. (1989) Towards a conception for an engineering disicipline of human-factors, *Ergonomics*, 32(11), 1513-1535.
English, W.K., Engelbart, D.C. and Berman, M.L. (1967) Display-selection techniques for text manipulation*, IEEE Trans. Hum. Factors Electron*., vol. HFE-8, Mar. 1967, 5-15.
Feyerabend, P. K. (2010) *Against Method, 4th edn. *Verso.
Feynman, R. P. (1992) *Surely you’re joking, Mr Feynman*. Vintage.
Field, A., Hole, G. (2003) *How to Design and Report Experiments.* Sage Publications, London.
Gergle, D. and Tan, D. (2014). Experimental Research in HCI. In Olson, J.S. and Kellogg, W. (eds) *Ways of Knowing in HCI*. Springer, 191-227.
Gigerenzer, G. (2004) Mindless statistics. *The Journal of Socio-Economics*, 33( 5), 587-606.
Hacking, I. (1983) *Representing and intervening. *Cambridge University Press.

Harris, P. (2008) *Designing and Reporting Experiment in Psychology, 3rd edn*. Open University Press.
Hassenzahl, M., Monk, A. (2010) [The Inference of Perceived Usability From Beauty](http://www.tandfonline.com/doi/abs/10.1080/07370024.2010.500139), [*Human–Computer Interaction *](http://www.tandfonline.com/toc/hhci20/25/3), 25(3), 235-260.
Hornbaek , K. (2011) Some whys and hows of Experiments in Human-Computer Interaction, *Foundations and Trends in Human–Computer Interaction, *5(4), 299–373
Hornbæk, K. and Law, E. (2007) Meta-analysis of Correlations among Usability Measures, *Proc. of ACM CHI 2007*, ACM Press, 617-626.
Hulsizer, M. R, Woolf, L. M. (2009) *A guide to teaching statistics. *Wiley-Blackwell.
Jennett, C., Cox, A.L., Cairns, P., Dhoparee, S., Epps, A., Tijs, T.,
 Walton, A. (2008). Measuring and Defining the Experience of Immersion 
in Games. *International Journal of Human Computer Studies*, 66(9), 641-661
Jordan, p. (2002) *Designing Pleasurable Products, *CRC Press.
Kahneman, D. (2012) *Thinking Fast and Slow, *Penguin.
Kline, P. (2000) A *Psychometrics Primer*. Free Association Books.
Kuhn (1996), *The Structure of Scientific Revolutions, 3rd edn. *University of Chicago Press.
Lawson, B. (1997) *How designers think: the process demystified. 3rd edn.* Architectural Press.
Lazar, J., Feng, J. H., Hocheiser, H. (2009) *Research Methods in Human-Computer Interaction, *John Wiley & Sons.

MacKenzie, I. S. (1992) Fitts' law as a research and design tool in human-computer interaction. *Human-Computer Interaction,* 7(1), 91-139.
MacKenzie, I. S., Buxton, W. (1992) Extending Fitts’ Law to 2d tasks, *Proc. of ACM CHI 1992*, 219-226
Malone. T. W. (1982) [Heuristics](https://www.interaction-design.org/literature/topics/heuristics) for designing enjoyable user interfaces: Lessons from computer games. *Proc. ACM CHI 1982*. ACM Press, 63-68
Mayo, D. (1996) *Error and the Growth of Experimental Knowledge*, University of Chicago Press.
Mayo, D, Spanos, A. eds (2010) *Error and Inference. *Cambridge University Press.
McCarthy, J., Wright, P. (2007) *Technology as Experience*, MIT Press
Nordin, A.I., Cairns, P., Hudson, M., Alonso, A., Calvillo Gamez, E. 
H. (2014)The effect of surroundings on gaming experience. In *Proc. of 9th Foundation of Digital Games.*
Popper, K. (1977) *The logic of scientific discovery*. Routledge.
Sharp, H. , Preece, J., Rogers, Y. (2010) *Interaction Design, 3rd edn*. John Wiley & Sons.
Plato (1954) *The Last Days of Socrates*. Penguin.
Plato (1973) *Phaedrus and Letters VII and VIII. *Penguin*.*
Purchase, H. (2012) *Experimental Human-Computer Interaction*, Cambridge University Press.

Ravaja, N., Saari, T., Salminen, J., Kallinen, K. (2006) [Phasic Emotional Reactions to Video Game Events: A Psychophysiological Investigation](http://www.tandfonline.com/doi/abs/10.1207/s1532785xmep0804_2), [*Media Psychology *](http://www.tandfonline.com/toc/hmep20/8/4)*, *8(4), 343-367.
Ritchie, S.J., Wiseman, R, French, C. C. (2012) Failing the Future: 
Three Unsuccessful Attempts to Replicate Bem's ‘Retroactive Facilitation
 of Recall’ Effect. *PLoS ONE, *7(3): e33423.
Salthouse, T. A. (1979) Adult age and the speed-accuracy trade-off, *Ergonomics*, 22(7), 811-821.
Sauro, J., Lewis, J. R. (2012) *Quantifying the user experience*. Morgan Kaufmann.
Sears, D. O. (1986), College sophomores in the laboratory: Influences
 of a narrow data base on social psychology's view of human nature. *Journal of Personality and Social Psychology*, 51(3), 515-530.
Simons, D. J., Chabris, C. F. (1999) Gorillas in our midst. *Perception*, 28, 1059-1074.
Smith, J. (2012) Applying Fitts’ Law to Mobile [Interface Design](https://www.interaction-design.org/literature/topics/ui-design).
[http://webdesign.tutsplus.com/articles/applying-fitts-law-to-mobile-interface-design--webdesign-6919](http://webdesign.tutsplus.com/articles/applying-fitts-law-to-mobile-interface-design--webdesign-6919), accessed 28th April, 2014
Suchman, L. (1987) *Plans and Situated Actions, 2nd edn*, Cambridge University Press.

Thimbleby, H. (2013) Action Graphs and User Performance Analysis. *International Journal of Human-Computer Studies*, 71(3), 276–302.
Tidwell, J. (2005) *Designing Interfaces: Patterns for Effective Interaction Design.* O’Reilly.
Tullis, T., Albert, W. (2010) *Measuring the User Experience, *Morgan Kaufmann.
[Vargha](http://jeb.sagepub.com/search?author1=Andr%C3%A1s%20Vargha&sortspec=date&submit=Submit), A., [Delaney](http://jeb.sagepub.com/search?author1=Harold%20D.%20Delaney&sortspec=date&submit=Submit), H., D. (2000) A Critique and Improvement of the *CL*Common Language Effect Size Statistics of McGraw and Wong, *Journal of Educational and Behavioral Statistics, *25(2)*, *101-132
Wilson M. (2002) Six views of embodied cognition. *Psychonomic Bulletin & Review*, 9, 625–636
Wobbrock, J.O., Findlater, L., Gergle, D. and Higgins, J.J. (2011) 
The aligned rank transform for nonparametric factorial analyses using 
only anova procedures. *Proc. of ACM CHI 2011,* ACM Press, 143-146
Yin, R. K. (2003) *Case Study Research: Design and Methods, 3rd edn*. Sage Publications.
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

加入 **314,322 位设计师** 的行列，通过我们的时事通讯（Newsletter）获取实用的用户体验（User Experience, UX）技巧。
需要提供有效的电子邮件地址。

## 本书章节涵盖的主题：

[人机交互（Human-Computer Interaction, HCI）
                    ](https://www.interaction-design.org/literature/topics/human-computer-interaction)[
                        用户体验（User Experience, UX）设计
                    ](https://www.interaction-design.org/literature/topics/ux-design)[
                        设计史（Design History）](https://www.interaction-design.org/literature/topics/design-history)
