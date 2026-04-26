# 38. 人-机器人交互 (1)

**来源**：The Encyclopedia of Human-Computer Interaction, 2nd Ed.
**Notion 原页面**：https://www.notion.so/17859438d87e419abca84c8ab3d1fa24

---

[Kerstin Dautenhahn](https://www.interaction-design.org/literature/author/kerstin-dautenhahn)
本章介绍并批判性地反思了人-机器人交互（Human-Robot Interaction, HRI）研究中的一些关键挑战和开放性问题。本章强调，为了应对这些挑战，需要同时处理 HRI 中以用户为中心（user-centred）和以机器人为中心（robotics-centred）的方面。本文重点讨论了 HRI 的合成特性（synthetic nature），并将其置于方法论问题的语境下进行分析。同时，文中描述并比较了 HRI 中不同的实验范式（experimental paradigms）。此外，我将论证，由于机器人的人造性（artificiality），我们在对 HRI 的“自然度（naturalness）”做出假设时需要谨慎，并质疑一种广泛存在的假设，即类人机器人（humanoid robots）应该是设计成功 HRI 的最终目标。除了为了向人们提供服务或代表人们提供服务而构建机器人外，本文还介绍了一个不同的 HRI 方向，即将机器人用作人与人之间的社交中介（social mediators）。HRI 研究的实例将进一步阐明这些观点。

## 38.1 背景（Background）

人机交互（Human-Robot Interaction, HRI）是一门相对年轻的学科。近年来，由于复杂机器人的普及以及人们在日常生活中接触这类机器人的机会增加（例如机器人玩具，或在某种程度上作为家用电器，如扫地机器人或割草机器人），该领域引起了广泛关注。此外，机器人正越来越多地被开发用于实际应用领域，例如康复机器人、养老机器人，以及用于机器人辅助治疗（robot-assisted therapy）和其他辅助或教育应用的机器人。

本文并非旨在成为一篇关于 HRI 的综述文章（review article），关于该领域的历史、起源及其相关[综述（surveys）](https://www.interaction-design.org/literature/topics/surveys)和讨论，请参阅 (Goodrich and Schultz, 2007; Dautenhahn, 2007a) 等文献。相反，我想讨论 HRI 领域内的一些关键问题，这些问题往往会导致对该领域研究的误解或误读。本章不会深入探讨技术细节，而是侧重于该研究领域的跨学科（interdisciplinary）方面，旨在启发能够突破现有学科传统边界的创新研究。

研究人员加入 HRI 领域的动机可能各不相同。有些人可能是机器人专家（roboticists），致力于开发具有潜在实际应用价值的高级机器人系统，例如旨在提供辅助的服务机器人（service robots）...

人们在家庭或工作场所中使用机器人，他们加入这个领域可能是为了探索在机器人需要与人交互时应如何处理，从而提高机器人的效率。其他人可能是心理学家或行为学家，他们对人机交互（Human-Robot Interaction, HRI）采取以人为中心（human-centred）的视角；他们可能将机器人作为工具，以理解人类如何进行社交互动，以及如何与他人和交互式人工制品（interactive artifacts）进行沟通等基本问题。[人工智能（Artificial Intelligence）](https://www.interaction-design.org/literature/topics/ai) 和认知科学（Cognitive Science）研究人员加入该领域的[动机（motivation）](https://www.interaction-design.org/literature/topics/motivation)可能是为了理解和开发复杂的智能系统，并将机器人作为这些系统的具身实例化（embodied instantiations）和测试平台（testbeds）。

最后但同样重要的是，许多人对研究人与机器人之间的*交互（interaction）*感兴趣，例如人们如何感知不同类型和行为的机器人，以及他们如何感知社交线索（social cues）或不同的机器人具身（robot embodiments）等。开展此类工作的手段通常是通过“用户研究（user studies）”。这类工作通常不包含太多的技术内容；例如，它可能会使用商业可用且已完成编程的机器人，或者仅表现出少量行为或由远程控制的研究原型（通过“奥兹国魔法师（Wizard-of-Oz）”方法，即由一名参与者不知情的操纵员来控制机器人），从而创建非常受限的

以及受控的实验条件。此类研究重点关注人类对机器人的反应和态度。该领域的研究通常涉及大规模评估，旨在寻求具有统计学显著性（Statistically Significant）的结果。不幸的是，这一在方法论上深受实验心理学（Experimental Psychology）和人机交互（[HCI](https://www.interaction-design.org/literature/topics/human-computer-interaction)）研究影响的“用户研究（User Studies）”领域，往往被狭隘地等同于“人机交互（HRI, Human-Robot Interaction）”领域。“我们是应该关注机器人的 AI 和技术开发，还是应该做 HRI 研究？”这种言论在研究讨论中并不罕见。在我看来，这种将 HRI 与“用户研究”等同起来的倾向是非常不幸的，从长远来看，这可能会使 HRI 被边缘化，并将其变成一个分众的小众领域（Niche-domain）。HRI 作为一个研究领域是一门综合性科学（Synthetic Science），它应当应对从技术、认知/AI 到心理、社会、认知和行为的全方位挑战。

### 38.2 HRI——是一门合成科学（Synthetic Science），而非自然科学

HRI 兴起于 20 世纪 90 年代初，其特点被描述为：
> “人机交互（Human—Robot Interaction, HRI）是一个致力于理解、设计和评估由人类使用或与人类共同使用的机器人系统的研究领域”
  (Goodrich and Schultz, 2007, p. 204)。

什么是人机交互（HRI），它试图实现什么目标？
> “HRI 的问题在于理解并塑造一个或多个人类与一个或多个机器人之间的交互”
  (Goodrich and Schultz, 2007, p. 216)。

上述对 HRI 核心问题的描述，重点在于理解机器人与人之间发生了什么，以及如何塑造这些交互，即如何对其产生影响，或朝着某个特定目标进行改进等。

上述观点隐含地假设了一个关于“机器人（robot）”含义的参考点。该术语通常追溯到捷克语词汇 *robota*（意为“工作”），其首次使用可归功于 Karel Capek 的剧作 $\textit{R.U.R.: Rossum's Universal Robots}$ (1920)。然而，“机器人”一词远未得到清晰的定义。虽然关于其运动、感知和认知功能的各种技术定义层出不穷，但很少有定义明确规定机器人的外观、行为以及与人的交互。事实上，如果一名非研究人员与一个他/她从未接触过的机器人进行交互，那么关键在于……

机器人的外观、功能，以及它如何与人进行交互和沟通。在这种语境下，“用户”并不太关心所实现的认知架构（cognitive architecture）、所使用的编程语言或机械设计的细节。

自 20 世纪 90 年代初以来，机器人的行为和外观发生了巨大的变化，并且仍在不断变化——新机器人不断涌现于市场，而旧机器人则逐渐被淘汰。机器人外观的设计范围极其广泛，从类机械（mechanoid，外观像机器的）到类动物（zoomorphic，外观像动物的），再到类人（humanoid，像人的）机器，以及处于类人化极端顶端的仿生机器人（android robots）。机器人外观、行为及其认知能力的设计空间（design space）同样巨大。大多数机器人都是独特的设计，其硬件（通常也包括软件）可能与其他机器人、甚至同一机器人的先前版本不兼容。因此，机器人通常是离散的、孤立的系统，它们不像自然物种那样进化，也没有在进化过程中适应其环境。当生物物种进化时，新一代与前一代之间存在着复杂的联系；事实上，人们需要了解一个物种的进化历史，才能充分理解其形态（morphology）、生物学特性、行为和其他特征。机器人是由人类设计并由人类编程的。即使对于机器人

即使是那些具有学习能力的机器人，其学习的方式和时机也是经过编程预设的。针对机器人具身化与控制（Embodiment and control）的演化方法（Evolutionary approaches）（Nolfi and Floreano, 2000; Harvey et al., 2005）以及针对机器人社会与认知能力发育的发育方法（Developmental approaches）（Lungarella et al., 2003; Asada et al., 2009; Cangelosi et al., 2010; Vernon et al., 2011; Nehaniv et al., 2013）或许在未来能创造出不同的局面，但目前，用于人机交互（HRI, Human-Robot Interaction）的机器人仍是人工设计的系统。这与研究生物系统的动物行为学（Ethology）、实验心理学（Experimental psychology）等学科截然不同。

例如，Edward C. Tolman 在 1948 年撰写了其著名的文章 "Cognitive Maps in Rats and Men"。直到今天，他的研究仍然是人类及其他动物的[导航（Navigation）](https://www.interaction-design.org/literature/topics/navigation-1)与认知地图（Cognitive Maps）研究中被频繁引用的关键文献。大鼠和人类依然是相同的两个物种；自 1948 年以来，它们并未演变成完全不同的生物，因此 1948 年获得的结果在今天依然具有可比性。相比之下，20 世纪 90 年代初的机器人与如今的机器人并不具有共同的演化历史；它们简直就是截然不同的机器人“物种”。

因此，我们今天所定义的“机器人”与几百年后所定义的“机器人”将大相径庭。机器人的概念是一个*动态目标（Moving target）*，我们一直在不断重新定义我们所认为的

“机器人”。因此，研究与机器人的交互并获得可应用于不同平台的 人机交互（Human-Robot Interaction, HRI）通用见解是一项巨大的挑战。如果仅关注 HRI 中的“H”，即“用户研究（user studies）”或人类视角，就会忽略重要的“R”，即机器人组件及其技术和机器人学特性。只有对这两个方面进行深入研究，最终才能揭示那个难以捉摸的“I”，即当我们把人和交互式机器人置于一个 共享情境（shared context）中时所产生的交互。在我看来，HRI 的核心挑战和定义可以表述如下：

“HRI 是一门研究人们对机器人的行为和态度与其物理、技术和交互特性之间关系的科学，其目标是开发能够促进人机*交互（interactions）*产生的机器人，这种交互既要高效（符合其预期应用领域的原始需求），又要能被人们接受，并满足个体用户的社交和情感需求，同时尊重人类价值观。”

## 38.3 HRI - 方法论问题

正如前一节所讨论的，“机器人”这个概念是一个动态目标（moving target）。因此，与生物科学不同，人机交互（Human-Robot Interaction, HRI）研究面临的困境是，无法直接比较使用不同类型机器人的研究结果。理想情况下，研究者希望在每次 HRI 实验中使用多种机器人及其相应的行为——但这在实际操作中是不可能的。

让我们考虑一个思想实验（thought experiment），假设我们的研究问题是探讨一个圆柱形移动机器人应该如何接近一名坐着的人，以及机器人的行为和外观如何影响人们的反应。机器人将被编程为携带一瓶水，从一定距离接近该人员，在人员附近的一定距离处停止，将其正面（或头部）朝向该人员，并说：“您想喝水吗？”摄像机记录人们对机器人的反应，实验结束后，参与者填写一份关于他们对实验看法和体验的问卷。请注意，实际上这里并不涉及双向交互（bi-directional interaction），人在其中主要是被动的。场景被这样简化是为了能够[测试](https://www.interaction-design.org/literature/topics/test)不同的条件。我们为每个类别仅考虑三个值，即没有连续值（continuous values）。尽管有这些粗略的简化，由于

如表 1 所示，我们将最终得到 $3^7 = 2187$ 种组合以及可能让参与者接触的实验条件。为了满足统计约束（statistical constraints），每种条件都需要 $X$ 名参与者。每个实验环节（session）即使在最精简的场景下，也至少需要 15 分钟，此外还需要 15 分钟用于介绍、事后访谈（debriefing）、问卷/访谈以及签署知情同意书（consent forms）等。需要注意的是，更有意义的人机交互（Human-Robot Interaction, HRI）[场景（scenarios）](https://www.interaction-design.org/literature/topics/user-scenarios)——例如我们在下文描述的 Robot House 中开展的场景——通常需要为每位参与者的每个环节安排整整一小时。由于人们对机器人的看法和行为在长期交互（long-term interactions）中可能会发生变化，因此每位参与者应在相同条件下重复 5 次，这将产生 10935 个不同的实验环节。此外，参与者的选择需要非常谨慎，理想情况下还应考虑可能的年龄和性别差异，以及人格特质和其他个体差异（individual differences）——这意味着需要针对不同组别的参与者重复实验。无论我们是让一名参与者接触所有条件，还是为每种条件选择不同的参与者，获取足以进行有意义的统计分析的数据显然是不切实际的。最终，该实验所需的时间约为 $328050 \times X$ 分钟，而...

考虑到由于系统故障、参与者预约时间调整等原因导致实验不得不中断的情况。显然，在这种仅考虑极少数条件的情况下，运行此类实验是不切实际且不可取的，因为该实验的结果必然非常有限，且投入的精力显然不值得。

| 特征 |  |  |  |
|---|---|---|---|
| 高度 | 2m | 1m | 50cm |
| 速度 | 快 | 中等 | 慢 |
| 语音 | 类人（Human-like） | 机器人风格（Robot-like） | 无 |
| 机身颜色 | 红色 | 蓝色 | 白色 |
| 接近人的距离 | 近 | 中等 | 远 |
| 接近人的方向 | 正面接近 | 侧面接近 | 侧后方接近 |
| 头部 | 具有类人特征的头部 | 机械头部 | 无头部 |
| ... |  |  |  |
**表 38.1**：HRI（Human-Robot Interaction，人机交互）思想实验。

考虑到这些限制，典型的 HRI 实验会进一步简化。上述研究可以将范围限制在“矮机器人”和“高机器人”以及两种不同的接近距离，从而产生 4 种实验条件（experimental conditions）。结果将表明机器人高度如何影响人们偏好的接近距离，但这种结论的适用范围非常有限，因为所有其他特征都必须保持恒定，即机器人的外观（除高度外）、速度、语音、颜色、接近方向、头部特征等将被一次性选定，并在整个实验过程中保持不变。因此，我们得到的任何结果...

假设性实验将使我们难以将其结果轻易地外推（extrapolate）到其他机器人设计、行为或其他用户群体中。机器人是设计的人造制品（designed artifacts），且是一个动态目标（moving target）；我们今天认为的典型“机器人”，可能与 200 年后人们认为的“机器人”截然不同。那么，我们在过去 15 或 20 年中获得的结果，在未来的机器人身上是否依然适用？

正如我之前所指出的 (Dautenhahn, 2007b)，人机交互（Human-Robot Interaction, HRI）经常被拿来与其他实验科学进行比较，例如行为学（ethology），尤其是实验心理学，甚至是临床心理学（clinical psychology）。事实上，这些领域所采用的 [定量（quantitative）](https://www.interaction-design.org/literature/topics/quantitative-research) 方法通常为设计和评估 HRI 实验提供了宝贵的指导方针和一套成熟的研究方法。这些方法通常侧重于定量统计，需要大规模的实验，即涉及大量的参与者样本，并且通常包含一个或多个对照条件（control conditions）。由于这类工作的性质，相关研究通常是短期的，参与者仅一次或少数几次接触特定条件。实验心理学研究方法的教科书可以为该领域的新入者提供指导。然而，如果将此类方法视为 HRI 研究的“金标准（gold standard）”，即用它来衡量任何 HRI 研究，那么就存在一种内在的危险。这非常

这很遗憾，因为事实上，存在许多能够为人机交互（Human-Robot Interaction, HRI）提供不同但同样有价值的见解的方法论途径（Methodological Approaches）。这种[定性研究方法（Qualitative Methods）](https://www.interaction-design.org/literature/topics/qualitative-research)可能包括深入的长期案例研究，在这种研究中，个体参与者会在较长时间内与机器人接触。此类研究的目的更侧重于交互的实际*意义*、参与者的体验、可能发生的任何行为变化，以及参与者对机器人或交互态度的转变。这些方法通常缺乏对照组（Control Conditions），但能详细分析较长时间内的交互过程。其他方法，例如会话分析方法（Conversation-Analytic Methods）（Dickerson et al., 2013; Rossano et al., 2013），可以深入分析交互的详细性质，以及交互伙伴如何相互响应、关注并协调其行为。

在[辅助技术（Assistive Technology）](https://www.interaction-design.org/literature/topics/assistive-technology)和康复机器人学（Rehabilitation Robotics）领域，研究人员为特定的用户群体开发机器人系统，通常不需要设置不同用户群体的对照组：例如，如果开发用于辅助或康复中风后运动功能障碍（Motor Impairments）患者的系统，设计帮助视障人士的辅助工具，或开发机器人技术以帮助

在让自闭症儿童学习社交行为与沟通时，将他们使用机器人系统的形式与健康/神经典型（neurotypical）人群使用同一系统的方式进行对比并没有太大意义。我们已经了解目标用户群体的特定功能障碍（specific impairments），此类研究的目的并非为了再次强调他们与健康/神经典型人群的差异。此外，目标用户群体内部反应的多样性通常也是研究关注的重点。因此，在该领域中，只有当这些系统旨在面向不同的目标用户群体时，设置对照组（control groups）才有意义，这样比较研究才能揭示不同群体将如何使用该系统，以及他们能否从中获益。然而，大多数辅助与康复系统（assistive, rehabilitative systems）是专门为有特殊需求的人群设计的，在这种情况下，设置不同用户群体的对照条件（control conditions）未必有用。

需要注意的是，辅助技术（assistive technology）中对照条件的一个重要部分，是在不同的实验条件下测试不同的系统或同一系统的不同版本。这种比较至关重要，因为它们 a) 能够获取用于进一步改进系统的数据，且 b) 能突出辅助系统相对于其他传统系统或方法的附加值（added value）。例如，Werry and Dautenhahn (2007) 表明，交互式移动机器人比非机器人的传统玩具更能吸引自闭症儿童。

医生或物理治疗师可能会利用机器人技术来探究某种特定医疗状况或损伤的*本质（nature）*，例如探究中风后运动损伤（motor impairment）的本质，并可能使用评估机器人（assessment robot）对健康人群和中风患者同时进行测试。同样地，心理学家可以通过使用机器人装置（robotic artefacts）来研究自闭症的本质，例如比较儿童对社交线索（social cues）、语言或[触觉交互（tactile interaction）](https://www.interaction-design.org/literature/topics/tactile-interaction)的反应方式。此类装置是研究该障碍（disorder）或[残障（disability）](https://www.interaction-design.org/literature/topics/accessibility)本质的*工具（tools）*，而非旨在帮助患者的辅助工具（assistive tool）——因为后者在工具使用场景中，还必须考虑患者的个体差异、喜好以及偏好。

开发用于人机交互（human-robot interaction）的复杂机器人需要大量资源，包括研究人员、设备、专业知识（know-how）和资金；此类机器人的开发往往需要数年时间才能完全投入运行，这在业内并不罕见。典型的例子包括机器人“管家” Care-O-bot® 3 (Parlitz et al, 2008; Reiser et al., 2013, 参见图 1)，其首个原型机最初是作为欧盟 FP6 项目 COGNIRON (2004-2008) 的一部分而开发的，以及 iCub 机器人 (Metta et al.

（2010, 图 2）是在 2004 年至 2008 年间作为为期 5.5 年的 FP6 项目 Robotcub 的一部分而开发的。这两种机器人目前仍处于开发阶段，并定期进行升级。iCub 由一个大型联盟开发，旨在作为发育与认知机器人学（developmental and cognitive robotics）的研究平台，该联盟由数个负责开发机器人硬件和软件的欧洲合作伙伴组成。另一个例子是 IROMEC 平台，它是在 2006 年至 2009 年间作为 FP6 项目 IROMEC 的一部分而开发的（图 3）。该机器人被开发为一种社交中介（social mediator），旨在帮助可以通过游戏进行学习的特殊需求儿童。IROMEC 项目的成果不仅包括机器人平台，还包括一个用于开发机器人辅助游戏（robot-assisted play）场景的框架 (Robins et al., 2010)，以及一套包含 12 个详细游戏场景的方案，机器人辅助治疗（Robot-Assisted Therapy, RAT）社区可以根据每个儿童的具体发育和教育目标来使用这些方案 (Robins et al., 2012)。在 IROMEC 项目中，采用了专门的以用户为中心的设计方法（user-centred design approach）(Marti and Bannon, 2009; Robins et al. 2010)，然而在项目结束时，已没有足够的时间进行第二次设计周期（design cycle），以便根据目标最终用户的试用情况对平台进行修改。这种修改是非常必要的，因为用户与新技术的交互通常会揭示最初未被考虑到的问题。就 iCub 而言，该机器人最初被开发为一种新的认知系统（cognitive systems）

这是一个研究机器人平台（Research Robotics Platform），因此并未设想具体的最终用户（End Users）。以 Care-O-bot® 为例，三位专业设计师参与其中，旨在推导出一种“友好”的设计（Friendly Design）（Parlitz et al., 2008）。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image1.jpg)
作者/版权持有者：Courtesy of Kerstin Dautenhahn。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image2.jpg)
作者/版权持有者：Courtesy of Kerstin Dautenhahn。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

**图 38.1 A-B**：位于 UH Robot House 的 Care-O-bot® 3 机器人，作为 ACCOMPANY 项目（2011 年，进行中）的一部分，旨在研究针对老年用户的机器人辅助（Robot Assistance）。观看视频 ([http://www.youtube.com/watch?v=qp47BPw__9M](http://www.youtube.com/watch?v=qp47BPw__9M))。Robot House 位于校外的住宅区，相比于实验室环境，它为研究家庭辅助机器人（Home Assistance Robots）提供了一个更具自然主义（Naturalistic）的环境，参见图 6。将人机交互（Human-Robot Interaction, HRI）引入自然环境带来了许多挑战，但同时也带来了机遇（例如 Sabanovic et al. 2006; Kanda et al., 2007; Huttenrauch et al. 2009; Kidd and Breazeal, 2008; Kanda et al. 2010; Dautenhahn, 2007; Woods et al., 2007; Walters et al., 2008）。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image3.jpg)
作者/版权持有者：Courtesy of Kerstin Dautenhahn。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。
**图 38.2**：iCub (2013) 类人开源平台 (humanoid open course platform)，作为 Robotcub 项目 (2013) 的一部分而开发。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image4.jpg)
作者/版权持有者：Courtesy of Kerstin Dautenhahn。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。
**图 38.3**：IROMEC 机器人，作为 IROMEC 项目 (2013) 的一部分而开发。

因此，如何“正确地”为人机交互 (Human-Robot Interaction, HRI) 设计机器人——即让用户参与到设计过程中，并确保所开发的机器人能够履行其预定的角色与功能，且提供积极的 [用户体验 (User Experience)](https://www.interaction-design.org/literature/topics/ux-design) —— 仍然是一项艰巨的任务 (Marti and Bannon, 2009)。因此，在功能完整的机器人原型完成之前，研究者会采用多种方法来获取用户的输入和反馈，详见图 4。图 5 对这些不同的 [原型设计 (Prototyping)](https://www.interaction-design.org/literature/topics/prototyping) 方法和实验范式 (Experimental paradigms) 进行了概念性的对比。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image5.jpg)

作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

**图 38.4**：修改自 Dautenhahn (2007b)，[描绘](https://www.interaction-design.org/literature/topics/sketching) 了人机交互机器人（Human-Robot Interaction, HRI）典型的开发时间线，并展示了不同的实验范式（Experimental Paradigms）。深色箭头表示在这些阶段，特定的实验方法比在其他阶段更为有效。请注意，开发过程中通常存在多次迭代（Iterations）（图中未显示），因为系统可以在获得完整原型（Prototype）的用户研究（User Studies）反馈后进行改进。此外，在向用户或科学界发布首个版本后，根据部署机器人（Deployed Robots）的反馈，可能会产生多个不同系统的版本。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image6.jpg)

作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

**图 38.5**：本章讨论的不同实验范式的概念对比（Conceptual Comparison）。TR（剧场机器人，Theatrical Robot）、VHRI（基于视频的人机交互，Video-based HRI）、THRI（基于剧场的人机交互，Theatre-based HRI）、SISHIR（情境化交互模拟人机交互，Situated Interactive Simulated HRI）、Live HRI（实时人机交互）。资源效率（Resource Efficiency）意味着实验需要快速且低成本地（在...方面）产生相关结果。

（……包括工作量、所需设备、人月等）。结果相对保真度（Outcome-relative fidelity）意味着研究结果必须具有足够的可靠性和准确性，以支持基于这些结果而做出的、可能成本高昂的设计决策 (Derbinsky et al. 2013)。

即使在机器人原型（robot prototype）出现之前，为了支持系统的初始规划和规格定义阶段，也可以使用模拟模型（mock-up models），参见 Bartneck and Jun 2004。一旦系统的主要硬件和基础控制软件开发完成，且满足安全标准，即可开始针对参与者的首次交互研究。

上文提到的奥兹国魔法师技术（Wizard-of-Oz technique, WoZ）是一种流行的评估技术，它起源于人机交互（Human-Computer Interaction, HCI）领域 (Gould et al, 1983; Dahlback et al., 1993; Maulsby et al,. 1993)，目前被广泛应用于人机机器人交互（Human-Robot Interaction, HRI）研究中 (Green et al. 2004, Koay et al., 2008; Kim et al., 2012)。为了开展 WoZ 研究，必须拥有一个可以在参与者不知情的情况下进行远程控制的原型版本。因此，WoZ 常用于机器人硬件已完成，但其感知、运动或认知能力仍然有限的情况。然而，由一两名研究人员远程控制机器人的动作和/或语音可能会带来沉重的认知负担（cognitively demanding），且在目标是让机器人最终实现自主运行（operate autonomously）的情况下是不切实际的。例如，在护理、治疗或教育场景中，

远程控制机器人需要另一名研究员和/或护理人员在场（参见 Kim et al., 2013）。奥兹魔法师（Wizard of Oz, WoZ）方法可用于全远程操作（Full Teleoperation）或部分控制（Partial Control），例如用于模拟机器人的高层决策过程（High-level decision-making process）。图 6 展示了一个使用 WoZ 方法的人机交互（Human-Robot Interaction, HRI）实验示例。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image7.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image8.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image9.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image10.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image11.jpg)

作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。
![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image12.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。
![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image13.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。
**图 38.6**：a) 两名研究人员控制在（模拟）家庭陪伴环境 (b) 中使用的机器人的动作和语音。28 名受试者在物理辅助任务 (c) 中与机器人进行交互，并且他们还需要与机器人进行空间协商 (d)，e) 奥兹国向导法（Wizard of Oz, WoZ）研究的实验区域布局。该研究于 2004 年作为欧盟 COGNIRON 项目的一部分开展。Dautenhahn (2007a), Woods et al. (2007), Koay et al. (2006) 提供了使用 WoZ 方法进行的人机交互（Human-Robot Interaction, HRI）研究的一些结果。

一旦 WoZ 实验在技术上可行，就可以采用基于视频的方法，通常向一组参与者展示机器人与人及其环境交互的视频。基于视频的人机交互（Video-based HRI, VHRI）方法论已成功应用于多种

HRI 研究 (Walters et al., 2011; Severinson-Eklund, 2011; Koay et al. 2007, 2011; Syrdal et al., 2010; Lohse et al., 2008; Syrdal et al., 2008)。先前的研究对比了实时 HRI（live HRI）与基于视频的 HRI（video-based HRI），发现在机器人接近人的场景中，两者的结果相当 (Woods et al., 2006a,b)。然而，在这些对比研究所采用的场景中，机器人与人的行为之间几乎没有动态交互（dynamic interaction）和协调（co-ordination）。可以预见，人机交互之间的权变性（contingency）和协调程度越高，基于视频的 HRI（VHRI）模拟实时交互体验的可能性就越低（参见图 7）。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image14.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

**图 38.7**：随着交互权变性的增加（例如，交互中机器人与人之间的言语或非言语协调），视频 HRI 方法的适用性降低的示意图。

另一种取得了良好效果的原型设计方法（prototyping method）是剧场机器人（Theatrical Robot, TR）方法。该方法可用于机器人尚未就绪，但需要进行实时人机交互研究的情况，例如见图 8。剧场机器人是指由一个人（如演员或哑剧演员等专业人士）扮演

[参与者]扮成机器人，并根据特定的、预先设定的机器人行为库（robotic behaviour repertoire）来行动。因此，戏剧机器人（Theatrical Robot, TR）可以作为一个*等身、具身（embodied）的模拟机器人*，用以模拟类人的行为与认知。Robins et al. (2004) 在一项研究中成功采用了该方法，旨在探讨自闭症儿童对等身机器人的反应，以及这种反应如何取决于机器人看起来像人还是像机器人。在研究的四个儿童的小样本组中，与表现出相同（机器人）行为库但穿着像人类的 TR 相比，孩子们在初始阶段对具有机器人外观的 TR 表现出强烈的偏好，示例结果见图 8。注意，在两种实验条件下，“机器人”都被训练为不对儿童做出回应。在 Robins et al. (2004) 的研究中，聘请了一名哑剧演员（mime artist），以确保 TR 在实验过程中能够精确且可靠地控制其行为。

戏剧机器人范式（Theatrical Robot paradigm）使我们能够在机器人系统的规划极早期阶段就开展用户研究。一旦有了可运行的原型（working prototypes），TR 方法的实用性就会降低，因为此时可以使用“真实”的系统进行研究。然而，TR 本身也可以作为一种有价值的方法，用于研究人们如何根据对方的外观对他人做出反应，或者人们会对一个外观和行为都非常类人的机器人产生怎样的反应。

制造真正外观和行为都像人类的机器人仍然是一个未来的目标，尽管仿人机器人（Android robots）可以模拟外观，但它们缺乏类人的动作、行为和认知（human-like movements, behaviour and cognition）（MacDorman, Ishiguro, 2006）。因此，TR 可以简化冗长的开发过程，使我们能够预测人们对高度类人机器人的反应。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image16.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款和许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image17.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款和许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image18.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款和许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image19.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款和许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image20.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。
![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image21.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。
![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image22.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。
![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image23.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。
**图 38.8**：在一项研究自闭症儿童对真人大小机器人反应的实验中，采用了剧场机器人（Theatrical Robot）范式。机器人分别被装扮成机器人（外观简洁，图 a）或人类（人类外观），且在两种条件下表现出相同的行为。图 b, c, d 展示了三名儿童在两种实验条件下的反应。图 e 展示了儿童对剧场机器人（TR）注视行为（gaze behaviour）的结果示例。

除了机器人原型设计和人机交互（Human-Robot Interaction, HRI）之外，许多 HRI 研究中的一个关键问题是场景原型设计（prototyping of scenarios）。例如，在开发家庭陪伴机器人（home companion robots）领域，研究人员探讨了机器人用于不同类型辅助（assistance）的应用，包括身体辅助、认知辅助和社会辅助（physical, cognitive and social assistance）。这可能包括帮助居家老人完成身体任务（例如：取物与搬运 [fetch-and-carry]），提醒用户预约、活动或服药需求（将机器人作为认知假体 [cognitive prosthetic]），以及社会任务（鼓励人们社交，例如：给朋友或家人打电话，或拜访邻居）。实现此类场景再次带来了巨大的开发工作量，特别是当机器人的行为应该是自主的（autonomous），而非完全脚本化（scripted），且需要适应用户的个人偏好及其日常生活时间表时。

一种场景原型设计的方法是将绿野仙踪法（Wizard-of-Oz method, WoZ）与面向观众的机器人剧场表演（robotic theatre performance）相结合。基于剧场的 HRI 方法（Theatre-based HRI method, THRI）为用户对涉及家庭陪伴机器人等场景的[感知（perception）](https://www.interaction-design.org/literature/topics/perception)提供了宝贵的反馈（Syrdal et al, 2011; Chatley et al., 2010）。剧场和戏剧已被应用于人机交互（Human-Computer Interaction, HCI）中，以探讨未来技术使用的相关问题（参见 Iacuccui and Kuuti, 2002; Newell et al., 2006）。在 HRI 的语境下，THRI 由演员在舞台上的表演组成，他们与...进行交互

机器人由奥兹巫师（Wizard-of-Oz, WoZ）控制或采用半自主控制（semi-autonomously controlled）。随后，通过与受众的讨论以及/或问卷调查和访谈，来研究受众对场景及所展示技术的感知（perception）。受众与舞台上的演员（在角色设定下）之间的讨论通常由一名引导者（facilitator）进行协调。与个体 HRI 研究相比，该方法能够触达更广泛的受众，因此在场景原型化（prototype scenarios）方面非常有用。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image24a.jpg)
Author/Copyright holder: Courtesy of Kerstin Dautenhahn. Copyright terms and licence: CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported).

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image24b.jpg)
Author/Copyright holder: Courtesy of Kerstin Dautenhahn. Copyright terms and licence: CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported).

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image25.jpg)
Author/Copyright holder: Courtesy of Kerstin Dautenhahn. Copyright terms and licence: CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported).

**图 38.9 A-B-C**：a) SISHRI 方法论路径 (Derbinsky et al., 2013) —— 利用模拟机器人进行情境化（situated）、实时的 HRI，以实现场景原型化；b) 交互模拟示例。

显示在参与者使用的平板电脑上。左侧显示的是为快速场景原型设计（rapid scenarios prototyping）而开发的 Web 应用程序的主页。该演示版本展示了三个已实现的动作（Drawer、GoTo 和 ToDo）：Drawer 允许用户打开和关闭机器人的抽屉；GoTo 用于模拟机器人从一个位置移动到另一个位置所需的时间（见右图）；ToDo 的引入是为了扩展该原型的功能，其活动与用户而非机器人相关，并可以记录在系统中（例如：饮水、进食等）。右侧展示了 GoTo 的功能。在这个示例中，用户可以将机器人从厨房（机器人当前位置）发送到用户从列表中选择的任何其他地点（厨房、沙发、书桌、抽屉）。在图中，用户选择了厨房。

最近，一种新的资源高效型场景原型设计方法被提出。Derbinsky et al. (2013) 描述了一个概念验证实现（proof-of-concept implementation）。在这种方法中，单个用户在手持设备的帮助下，在没有实际物理机器人的情况下，模拟执行（goes 'through the motions'）机器人家庭辅助场景。平板电脑模拟了嵌入在智能环境（smart environment）中的机器人动作。该方法的优点在于维持了交互的情境性（situatedness），即用户在真实的环境中进行真实的

...时间，并使用一个模拟机器人。这种方法可被称为 SISHRI（场景化交互模拟人机交互，Situated Interactive Simulated HRI），它保留了场景中的时间与空间维度以及动作序列的逻辑顺序，但省略了机器人本身。它允许在不需要实际机器人的情况下，测试复杂场景（例如用于家庭辅助 Home Assistance 的场景）的可接受度（Acceptability）和整体用户体验（User Experience）。系统根据通过传感器网络（Sensor Network）识别的活动以及用户通过 [用户界面](https://www.interaction-design.org/literature/topics/ui-design)（User Interface）输入的指令做出响应。在高级工作原型（Working Prototype）可用之前，该方法在构建复杂场景的原型时可能最为有用（见图 9）。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image26.jpg)
作者/版权持有者：Courtesy of Kerstin Dautenhahn。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image27.jpg)
作者/版权持有者：Courtesy of Kerstin Dautenhahn。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image28.jpg)
作者/版权持有者：Courtesy of Kerstin Dautenhahn。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image29.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image30.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image30_a.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

**图 38.10**：展示机器人的设计空间（Design Space）。机器人的形状和功能取决于其应用场景和用途。a) KASPAR，由 University of Hertfordshire 开发的极简表达机器人，用于人机交互（Human-Robot Interaction, HRI）研究，包括针对自闭症儿童的机器人辅助治疗（Robot-assisted therapy）；b) Roomba (iRobot)，一台在 University of Hertfordshire Robot House 中运行的真空吸尘机器人；c) Autom，体重管理教练。来源：Intuitive Automata；d) Pleo 机器人 (Ugobe)，被设计为一种“接收照顾”的机器人，旨在鼓励人们与其建立关系；e) Robosapien 玩具机器人 (WowWee)；f) 设计空间（Design space）— 生态位空间（Niche space）— 资源（Resources），详见正文解释。

任何特定的人机交互（Human-Robot Interaction, HRI）研究的开展及其所采用的方法论，都需要考虑图 10 所示的三个关键约束。机器人设计空间（Robot Design Space）涵盖了机器人行为与外观方面所有可能的不同设计。生态位空间（Niche Space）则由机器人及其人机交互的需求组成，这些需求与特定的相关场景和应用领域密切相关。在为 HRI 研究选择具体方法时，必须考虑资源（如时间、资金、参与者的可用性等）的限制。由于穷尽式地探索设计空间是不可行的，因此需要谨慎地做出决策。

## 38.4 HRI - 关于（不）将机器人浪漫化

机器人研究的现状是，机器人在身体活动、认知或社交能力方面，远未表现出任何真正像人类的能力（例如在灵活性、能力的“规模化（scaling up）”、 “常识（common sense）”、能力的“优雅降级（graceful degradation）”等方面）。尽管如此，在机器人学和人机交互（Human-Robot Interaction, HRI）的文献中，它们经常被描绘为“朋友”、“伙伴”、“同事”等，而这些全部是真正属于人类的术语。这些术语很少在操作定义（operational sense）的意义上被使用，且几乎没有定义——大多数情况下，这些术语在被使用时缺乏进一步的思考。此前，我为*伴侣机器人（companion robots）*提出了一个更正式的定义，即：“家庭环境中的机器人伴侣需要‘做正确的事’，也就是说，它必须有用并能执行家务任务；但它同时也必须‘正确地做事’，也就是说，其方式必须是人类能够信服且可接受的” (Dautenhahn, 2007a, p. 683)。

与伴侣范式（companion paradigm）——即机器人的核心功能是照顾人类需求——相反，在*照顾者范式（caretaker paradigm）*中，照顾“不成熟”的机器人则是人的职责。在同一篇文章中，我还论证了由于进化决定的认知限制（evolutionarily determined cognitive limits），我们在能够结交多少个“朋友”方面可能会受到限制。当人类与他人建立关系时，这涉及到情感、心理和生理上的投入。我们往往倾向于

对机器人进行类似的投入，但机器人无法回报这种投入。机器人对我们的“关心”程度，完全取决于程序员的设定。*机器人不是人，而是机器*。

生物有机体（Biological organisms）而非机器人，才是具有感知能力的生物（Sentient beings）；它们拥有生命，拥有进化与发育历史，并拥有塑造其行为及其与环境关系的生命经验。相比之下，机器既没有生命也没有感知能力；它们可以表达情感，伪装成与你建立了“纽带（Bond）”，但这仅仅是模拟（Simulations），而非人类所共有的真实体验。类人机器人（Humanoid robot）的“情感”可能看起来像人，但机器人本身没有任何感觉，其表达也不基于任何经验性理解（Experiential understanding）。一个深情地凝视着你的眼睛并低语“我爱你”的类人机器人，其实是在运行一个程序。我们可能会享受这种互动，就像享受角色扮演或沉浸在虚构世界一样，但人们需要清楚这种互动本质上的机械属性。正如 Sherry Turkle 所指出的，机器人作为旨在鼓励人们与其建立关系的“关系人工制品（Relational artifacts）”，可能会导致人们对互动的真实性（Authenticity）产生误解 (Turkle, 2007)。如果儿童在成长过程中将机器人伴侣作为主要朋友，且每天与其互动数小时，他们将会

意识到每当机器人让他们感到厌烦或产生挑战时，他们可以简单地将其关掉或锁在橱柜里。这些孩子将会形成怎样的友谊概念？他们是否会建立独立的类别，例如“与机器人的友谊”、“与宠物的友谊”以及“与人的友谊”？他们是否会对机器人、动物和人类适用相同的道德和伦理考量（Moral and ethical concerns）？或者，由与机器人交互而塑造的友谊观念，会延伸到生物世界中？类似的议题在讨论儿童可能对电脑游戏及其游戏角色产生成瘾（Addiction）时也被提及，以及这些因素在多大程度上会对他们的社会化与道德发展产生负面影响。与社交机器人（Social robot）共同成长的人，是否会将其视为一种“不同的种类”，而不管它具有类人或类动物的相似性？社交机器人是否会成为新的本体论类别（Ontological categories）（cf. Kahn et al. 2004; Melson et al. 2009）？目前这些问题尚无法回答，它们需要针对人们如何与机器人交互进行长达数年甚至数十年的长期研究——而这类结果难以获得，且在伦理上可能不可取。然而，面向儿童的机器人宠物和面向成人的机器人助手正变得越来越普及，因此我们未来可能会得到这些问题的答案。这些答案不太可能是“非黑即白”的——就像关于电脑游戏是否有利于儿童认知、学业和社会发展的讨论一样。

在这些方面，答案尚无定论 (Griffiths, 2002; Kierkegaard, 2008; Dye et al., 2009; Anderson et al., 2010; Jackson et al. 2011)。

纵观历史，人类一直对自主机器（Autonomous Machines）深感兴趣，因此，人们对机器人及其本质和潜能的痴迷在未来很长一段时间内都将持续。然而，关于机器人本质（Nature of Robots）的讨论应当基于事实、证据和有据可依的预测，而非追求浪漫化的虚构（Romanticizing Fiction）。

## 38.5 HRI —— 并不存在所谓的“自然交互”

人机交互（Human-Robot Interaction, HRI）领域中一个广泛的假设是，与机器人的“良好”交互必须尽可能地反映*自然*（人与人之间）的交互和沟通，以减轻人们解读机器人行为的需求。事实上，人们的面对面交互具有高度的动态性和多模态（Multi-modal）特性——涉及各种手势、语言（内容和韵律 [Prosody] 均很重要）、身体姿态、面部表情、眼神注视，以及在某些情境下的触觉交互等。这导致了针对机器人如何产生和理解手势、在被交谈时如何理解并做出相应反应、以及机器人如何利用身体姿态、眼神注视和其他线索来调节交互的深入研究；同时，研究者们正在开发认知架构（Cognitive Architectures），旨在赋予机器人自然的社交行为和沟通技巧（例如 Yamaoka et al. 2007; Shimada and Kanda, 2012; Salem, 2012; Mutlu et al., 2012）。此类工作的内在最终目标是创建类人（Human-like）机器人，使其外观像人且行为方式也像人。虽然我们将在下文详细讨论为什么类人机器人的目标需要被批判性地反思，但关于“自然”人类行为存在的根本假设本身也是有问题的。首先，什么是*自然*的行为？一个人在自己的

……在家中，与孩子玩耍时，与父母交谈时，参加求职面试时，会见同事时，或在会议上做报告时？同一个人在不同的语境（contexts）和生命周期的不同阶段，其行为方式各不相同。我们的采集狩猎（hunter-gatherer）祖先在试图避开大型捕食者和寻找避难所时，其行为是否是“自然的”？如果“自然”是指“生物学上的真实性（biologically realistic）”，那么这一论点就是成立的——在这种情况下，“自然的手势（natural gesture）”将是指一个采用生物运动剖面（biological motion profile）且忠实模拟人类手臂形态学（human arm morphology）的手势。同样地，一个自然的微笑将试图模拟人类面部肌肉的复杂性和情感表达。

然而，当我们将讨论层面从动作和行为提升到社会行为（social behaviour）时，“自然”一词的意义就变得不那么明确了。举例来说，机器人应该表现得多么礼貌？人类在参加正式的工作晚餐或在家里吃家宴时，会表现出不同的行为并使用不同的表达方式。作为人类，我们在生活中可能承担许多不同的个人和职业角色，例如：女儿/儿子、兄弟姐妹、祖母、叔伯、配偶、雇员、雇主、委员会成员、志愿者等。在所有这些不同的环境下，我们的行为都会略有不同，从穿着、说话方式、行为举止，到说话的内容及其方式，这些都会影响我们的交互风格（style of interaction）、使用触觉交互（tactile interaction）的方式等。我们可以

无缝地在这些不同的角色之间切换，而这些角色仅仅是“我们是谁”的不同方面——是我们自我的表达，或者用 Daniel Dennett 的话来说，是我们的“叙事重心（centre of narrative gravity）”。人们能够应对如此不同的情境，是因为我们在不断地重构我们（社会）世界的叙事（Dennett, 1989/91；另见 Turner, 1996）。

> “我们进行自我保护、自我控制和自我定义的根本策略，并非筑坝或织网，而是讲述故事——更具体地说，是构思并控制我们向他人以及向自己讲述的关于‘我们是谁’的故事。这些叙事链或叙事流仿佛源自同一个源头——这不仅是指从同一个口中说出，或由一支铅笔或钢笔写出这种明显的物理意义，而是在一种更微妙的意义上：它们对任何听众或读者的影响，是鼓励他们（尝试）假定存在一个统一的主体（unified agent），这些话语出自该主体，且这些话语是关于该主体的：简而言之，就是假定一个我称之为‘叙事重心’的东西（Dennett, 1989/91）。”

因此，对于人类而言，“自然地”行为不仅仅是拥有既定或习得的行为库（behaviour repertoire），并在任何特定情境下就如何行为做出理性决策。我们是在“创造”这些行为，在重构它们，并综合考虑特定的语境、交互历史等，我们创造的行为与我们的“叙事自我（narrative self）”是一致的。对于人类来说，这样的行为可以被称为是“自然的”。

机器人的“自然”行为（natural behaviour）是指什么？“自我”的概念，即它们的“叙事重心（centre of narrative gravity）”又在何处？当今的机器人是机器，它们可能拥有复杂的“经验（experiences）”，但这些经验与其他复杂机器的经验并无二致。我们可以通过编程让它们在不同语境下表现出不同的行为，但从它们的视角来看，采取哪种行为并没有任何区别。它们通常无法将对自己及其环境的感知与一个叙事核心（narrative core）联系起来；它们并非在重新创造经验，而是在调用（recalling）经验。

机器人没有真正的进化史（evolutionary history），它们的身体和行为（包括手势等）并非在漫长的岁月中作为对环境挑战的适应性响应（adaptive response）而演化而来的。例如，人类手臂和手的形状有着充分的“理由”：这可以追溯到我们脊椎动物祖先的前肢设计——最初用于游泳，随后作为四足动物（tetrapods）用于行走和攀爬，而后的双足姿态（bipedal postures）则解放了双手，使其能够抓取和操纵物体、使用工具或通过手势进行交流。我们手臂和手的设计并非偶然，但也并非“完美”。但我们的手臂和手体现（embody）了适应不同环境约束（environmental constraints）的进化史。相比之下，机器人不存在“自然手势（natural gesture）”，正如机器人不存在“自然”的面孔或手臂一样。

综上所述，很难断言某种特定的行为 X 对于机器人 Y 而言是“自然的”。机器人的任何行为被视为自然或人造，完全取决于与之交互的人类如何感知。因此，机器人行为的自然度（Naturalness）取决于观察者（Beholder），即与机器人交互或观察机器人的个体，而非机器人行为本身的固有属性。

## 38.6 HRI - 新角色

随着越来越多的机器人系统被应用于真实场景（'in the wild'）（Sabanovic et al., 2006; Salter et al., 2010），研究人员探讨了此类机器人的不同角色。

此前，我提出了机器人在人类社会中的不同角色（Dautenhahn, 2003），包括：
- 无需人类接触即可运行的机器；
- 人类操作员手中的工具；
- 作为人类居住环境成员的同伴（peer）；
- 作为一种影响人们观点和/或行为的劝说机器（persuasive machine）（例如在治疗场景中）；
- 作为协调人与人之间互动的社会中介（social mediator）；
- 作为模范社会行为体（model social actor）。

Dautenhahn et al. (2005) 调查了人们将机器人视为朋友、助手或管家的看法。其他研究者讨论了机器人与人类的类似角色，例如，人类可以承担监督者、操作员、机械师、同伴或旁观者的角色（Scholtz, 2003）。Goodrich and Schultz (2007) 提出了机器人作为人类导师（mentor）的角色，或者在这种关系中人类作为信息消费者（information consumer）使用机器人提供的信息。最近讨论的其他角色还包括：协作任务中的团队成员（Breazeal et al. 2004）、作为学习者（learners）的机器人（Thomaz and Breazeal, 2008; Calignon et al., 2010; Lohan et al., 2011），以及在人机交互（HRI）教学场景中作为交叉培训者（cross-trainers）的机器人（Nikolaidis & Shal, 2013）。在交互中和/或通过演示来教授机器人动作、技能和语言是

这是一个非常活跃的研究领域（例如 Argall et al. 2009; Thomaz and Cakmak 2009; Konidaris et al., 2012; Lyon et al. 2012; Nehaniv et al., 2013），然而，如何在自然、非结构化（unstructured）且高度动态的环境中进行教学仍然是一个挑战。对于人类和其他一些生物物种而言，*社会学习（social learning）*是了解世界、了解彼此以及传授和发展文化的强大工具；对于在人类居住环境中学习的未来一代机器人来说，这仍然是一个非常有趣的挑战 (Nehaniv & Dautenhahn, 2007)。最终，如果机器人能够灵活、高效地学习在社会层面恰当的行为，从而提升自身的技能和性能，并被与其交互的人类所接受，那么它们必须发展出相应水平的社会智能（social intelligence）(Dautenhahn, 1994, 1995, 2007a)。

## 38.7 机器人作为服务提供者

许多关于智能自主机器人（intelligent, autonomous robots）的研究都集中在机器人如何提供原本由人类执行的*服务*（services，包括辅助性或其他形式的服务）上。机器人已经取代了工厂装配线上的许多工人；而最近，在人口结构（demographics）快速变化的国家，机器人被讨论用于提供老年护理（elder-care）的解决方案（见图 11）。在许多场景中，机器人的设计目标是与人类协同工作，并取代此前由人类执行的部分任务。

近年来，全球范围内的许多项目正在研究机器人在老年护理中的应用，旨在让用户尽可能长时间地在自己的家中独立生活，例如 Heylen et al. (2012) 和 Huijnen et al. (2011) 的研究。此类研究带来了许多技术、伦理以及与用户相关的挑战。关于此类研究项目的示例，请参阅图 6 中 COGNIRON 项目 (2004-2008) 关于家庭伴侣机器人（home companions）的人机交互（Human-Robot Interaction, HRI）研究，图 12 中 LIREC 项目 (2008-2012) 的研究，以及图 1 中作为上述 ACCOMPANY 项目一部分的智能家居社交与共情家庭辅助（social and empathic home assistance）研究。许多此类项目采用了智能家居环境（smart home environment），例如配备了数十个传感器的 University of Hertfordshire Robot House。该研究领域的成功将取决于可接受度（acceptability），不仅是指此类系统的主要用户（老年人）的可接受度，还包括其他用户（家人、朋友...）的可接受度。

（邻居），包括正式和非正式护理人员（formal and informal carers）。因此，在这些项目中考虑“人的因素”（human component）至关重要。关于 ACCOMPANY 项目所采取的目标和方法的更详细讨论，请参阅 Amirabdollahian et al. (2013)。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image31.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款和许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

**图 38.11**：27 个成员国（Member States）的人口预测（population projections），显示 65 岁及以上人口从 17.57% 增加到 29.54%，而 15-64 岁人口从 67.01% 减少到 57.42%。该图经 Amirabdollahian et al. (2013) 许可使用。

需要注意的是，老年护理（elder-care）机器人领域带来了许多伦理挑战（ethical challenges）（例如参见 Sharkey and Sharkey, 2011, 2012），而对这些问题的探讨确实是 ACCOMPANY 项目的目标之一。在接下来的内容中，我想就其中一些问题提供一些个人思考。机器人通常被设想为提供陪伴、社交接触、刺激和激励，并促进例如护理院居民之间的沟通；参见多年来关于海豹机器人 PARO（seal robot PARO）的研究（Wada and Shibata, 2007; Shibata et al. 2012）。事实上，护理人员通常时间非常有限（通常在...）

（每人每天仅几分钟）用于社交接触（social contact）。因此，护理人员可能会对使用机器人提供社交陪伴（social company）产生浓厚兴趣，而老年人也可能将此类机器人视为对抗孤独的一种手段。然而，正如我此前所论述的，与机器人的交互在本质上是机械的；机器人无法回馈（reciprocate）爱与情感，它们只能模拟这些情感。因此，人类现在且将永远是提供社交接触与陪伴、体验并表达[共情（empathy）](https://www.interaction-design.org/literature/topics/empathy)、情感以及相互理解的最佳专家。虽然设计能够完成占据护理人员大部分工作时间的实际任务（practical tasks）——例如清洁、喂食、为老人洗澡——的机器人十分困难，但如果能设计出履行这些任务的机器人，就有可能将护理人员从繁琐的工作中解放出来，让他们能够提供具有真实意义的社交接触与交互。不幸的是，构建能够实际执行此类任务的机器人面临着极高的技术挑战，尽管这目前是一个活跃的研究领域（参见 [the RI-MAN robot](http://rtc.nagoya.riken.jp/RI-MAN/index_us.html) 和 Yamazaki et al., 2012）；相比之下，构建能够提供基础陪伴与社交交互的机器人则在我们的能力范围之内，Turkle et al. (2006) 将其称为“关系人工制品（relational artifacts）”，且此类机器人目前已经存在。如果有一天机器人能够同时提供这两者

在护理的社交与非[社交维度](https://www.interaction-design.org/literature/topics/social-aspects)（Social Aspects）中，由于老年护理中降低成本的需求，人类护理人员是否会变得过时？还是说，机器人将被用于执行常规工作，从而将人类护理人员的时间释放出来，让他们能以更有意义且在情感上令人满足的方式与老年居民互动？后者不仅能更成功地提供高效且人性化（Humane Care）的护理，还能认可我们的生物学根源、情感需求和进化历史——作为一个物种，社交技能（Social Skills）是我们通常拥有最高专业能力的领域，而我们的“技术/机械专业知识”（Technical/Mechanical Expertise）则更容易被机器取代。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image32.jpg)
作者/版权持有者：Courtesy of Kerstin Dautenhahn。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image33.jpg)
作者/版权持有者：Courtesy of Kerstin Dautenhahn。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image34.jpg)
作者/版权持有者：Courtesy of Kerstin Dautenhahn。版权

条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image35.jpg)

作者/版权持有者：Courtesy of Kerstin Dautenhahn。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image36.jpg)

作者/版权持有者：Courtesy of Kerstin Dautenhahn。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

**图 38.12**：由 University of Hertfordshire 的 Dr. Kheng Lee Koay 开发的 Sunflower 机器人。该机器人基于 Pioneer 移动平台（左图），是一款具有社交交互（socially interactive）和表达能力（expressive）的机器人，旨在研究家庭环境下机器人伴侣（robot companion）的辅助场景（assistance scenarios）。

专门为家庭辅助（home assistance）设计的机器人示例是图 12 所示的 Sunflower 机器人。它由一个移动底盘（mobile base）、一个触摸屏用户界面（touch-screen user interface）以及漫射 LED 显示面板（diffuse LED display panels）组成，旨在向用户提供具有表达力的多色灯光信号。其他表达行为包括声音、底盘移动以及机器人颈部的动作。这些非语言表达行为（non-verbal expressive behaviours）受到了狗在人狗交互（human-dog interaction）中表现出的表达行为的启发，其场景与 Robot House 中所使用的场景相似，且是在协作中

与匈牙利 ELTE 大学（Prof. Ádám Miklósi 研究组）合作。该机器人具有一些类人特征（头部、手臂），但其整体设计是非类人的（Non-humanoid）。这一设计遵循了我们之前的研究结果，即具有机械感（Mechanoid）的机器人更容易被具有不同个人偏好的用户所接受。机器人的表达行为（Expressive behaviour，包括灯光、声音、动作）受到了狗与主人互动方式的启发（Syrdal et al., 2010; Koay et al., 2013）。a) Sunflower 的早期原型，b,c) Sunflower，d) 使用 Sunflower 早期原型的 HRI（人机交互）家庭辅助场景，并与类似场景中的狗与主人互动进行对比，e) (Syrdal et al., 2010)。关于 Sunflower 的不同表达方式，请参阅（[图片库](http://adapsys.feis.herts.ac.uk/index.php?option=com_content&view=article&id=175&Itemid=128)）和（[视频](http://www.youtube.com/watch?v=hVB8sYwKdGs)）。

## 38.8 机器人作为社会中介

上文我们讨论了机器人作为服务提供者、陪伴者和“助手”的角色。对机器人的另一种补充视角是将其视为*社会中介（social mediators）*——即帮助人们相互建立联系的机器。这类机器人并非旨在取代或补充人类及其工作；相反，其核心作用是帮助人们与他人进行互动。机器人社会中介被研究的一个领域是针对自闭症儿童的机器人辅助治疗（Robot-Assisted Therapy, RAT）。

自闭症是一种终身性发育障碍，其特征是沟通、社会互动以及想象力和幻想能力的受损（通常被称为“损害三联征 [triad of impairments]”；Wing, 1996），以及兴趣狭窄和刻板行为（stereotypical behaviours）。自闭症是一种谱系障碍（spectrum disorder），在具体儿童身上，自闭症的呈现方式存在巨大的个体差异（诊断标准请参阅 DSM IV, 2000）。自闭症的确切原因仍在研究中，目前尚无治愈方法。目前存在多种治疗方法，而使用机器人或其他计算机技术可以对这些现有方法起到补充作用。自闭症谱系障碍的患病率通常被报道为大约 1/100，但统计数据有所不同。

虽然在 1979 年，Weir 和 Emanuel 在一名自闭症儿童身上取得了令人鼓舞的结果，该儿童使用一个按钮盒来控制一台 LOGO Turtle...

……距离，将交互式社交机器人（interactive, social robots）作为治疗工具（therapeutic tools）的用法最早由本文作者 (Dautenhahn (1999)) 在 Aurora 项目 (1998, 持续进行中) 中提出。在该研究的早期阶段，探讨了针对自闭症儿童的社交中介（social mediator）概念，旨在鼓励自闭症儿童与其他人员之间的交互。在过去几年中，机器人用于治疗或诊断应用（therapeutic or diagnostic applications）的情况迅速增长；与早期的综述 (Dautenhahn & Werry, 2004) 相比，近期的综述文章 (Diehl et al., 2012, Scassellati et al. 2012) 展示了该研究领域的广度以及活跃研究小组的数量。

在关于机器人作为自闭症儿童社交中介的最早研究中，Werry et al. (2001) 和本文作者 (Dautenhahn 2003) 提供了相关实验案例：在需要共同使用一个可供玩耍的自主移动机器人（autonomous, mobile robot）的场景下，一对儿童开始彼此之间产生交互。随后，针对类人机器人（humanoid robot）Robota (Billard et al. 2006) 的研究表明，机器人能够鼓励自闭症儿童彼此之间以及与在场的实验人员（co-present experimenter）进行交互 (Robins et al. 2004; Robins et al. 2005a)。需要注意的是，机器人社交中介的作用并非取代，而是促进人类的接触 (Robins et al., 2005a,b, 2006)。同样地，近期关于极简表达类人机器人（minimally expressive humanoid robot）KASPAR 的研究……

探讨了机器人作为一种显著对象（salient object）的角色，它介导（mediates）并鼓励儿童与在场成年人之间的交互 (Robins et al, 2009; Iacono et al., 2011)。图 13 至 16 给出了由 Ben Robins 博士开展的实验示例，在这些实验中，机器人被用作社交中介（social mediators）。

机器人作为社交中介的一个关键未来挑战是研究机器人如何实时地适应不同的用户。Francois et al. (2009) 提供了一项概念验证研究（proof-of-concept study），展示了 AIBO 机器人如何适应与其互动的自闭症儿童的不同交互风格（interaction styles），另请参阅 Bekele et al. (2013) 最近发表的一篇文章。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image37.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款和许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image38.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款和许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

**图 38.13 A-B**：KASPAR 作为自闭症儿童的社交中介。两名男孩正在进行一项模仿游戏，一名儿童控制机器人的表情，另一名儿童则需要模仿 KASPAR，随后孩子们交换角色。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image39.jpg)

作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。
![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image40.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。
![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image41.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。
![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image42.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。
![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image43.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。
![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image44.jpg)
作者/版权持有者：由 Kerstin Dautenhahn 提供。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

**图 38.14**：两名患有自闭症（Autism）的儿童在与 KASPAR 进行模仿游戏（Imitation game）。一名儿童使用遥控器使 KASPAR 做出手势和身体姿态；另一名儿童的角色则是模仿 KASPAR。一段时间后，两人交换角色。
![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image45.jpg)
作者/版权持有者：Courtesy of Kerstin Dautenhahn。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。
![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image46.jpg)
作者/版权持有者：Courtesy of Kerstin Dautenhahn。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。
**图 38.15 A-B**：在与 KASPAR 玩游戏时，与他人（左侧为成年人，右侧为另一名儿童）进行分享（Sharing）。
![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image47.jpg)
作者/版权持有者：Courtesy of Kerstin Dautenhahn。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。
![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image48.jpg)
作者/版权持有者：Courtesy of Kerstin Dautenhahn。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image49.jpg)
作者/版权持有者：Courtesy of Kerstin Dautenhahn。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

![](https://public-media.interaction-design.org/images/encyclopedia/human-robot_interaction/image50.jpg)
作者/版权持有者：Courtesy of Kerstin Dautenhahn。版权条款与许可：CC-Att-SA (Creative Commons Attribution-ShareAlike 3.0 Unported)。

**图 38.16 A-B-C-D**：两名患有自闭症的孩子在与 Robota 进行协作游戏。该机器人由实验者远程控制。只有当两个孩子同时采取某种姿势时，Robota 才会移动并采取该姿势。研究结果表明，这为孩子们协调其动作提供了强有力的激励。

机器人作为社交中介（Social Mediators）应用的第二个示例领域涉及远程人与人交互（Remote Human-Human Interaction）。

虽然在机器人研究中，触觉传感器（Touch Sensors）已被广泛使用（例如允许机器人避免碰撞或抓取物体），但人机触觉的社交维度（Social Dimension）直到最近才引起关注。人类天生就是社交且具有触觉的生物。寻求与世界（包括社交世界）的接触，是了解自我、环境、他人以及我们与世界之间关系的关键。通过触觉交互（Tactile Interaction），我们发展出认知、社交和情感

技能以及与他人的依恋关系。触觉交互（Tactile interaction）是人类彼此沟通最基础的形式 (Hertenstein, 2006)。研究表明，幼儿时期缺乏触觉接触会产生毁灭性的影响 (e.g. Davis, 1999)。

社交机器人（Social robots）通常配备触觉传感器（tactile sensors），以鼓励玩耍并使机器人能够对人类的触摸做出响应，例如 AIBO (Sony)、Pleo (Ugobe) 和 PARO (Shibata et al., 2012)。利用触觉人机交互（tactile HRI）来支持远距离的人与人之间的沟通，展示了机器人可以在中介人类接触方面发挥的作用 (Mueller et al., 2005; Lee at al. 2008; The et al., 2008; Papadopoulos et al. 2012a,b)。

为了阐明这一研究方向，Fotios Papadopoulos 研究了自主 AIBO 机器人 (Sony) 如何在中介参与在线游戏活动和交互场景的两人之间的远程沟通中发挥作用。在这里，长期目标是将机器人开发为社交中介（social mediators），以协助远程交互场景中的人与人之间的沟通，从而为那些暂时或长期无法进行面对面交互的朋友和家人提供支持。一项研究对比了人们通过名为 AiBone 的通信系统（包含视频通信以及与 AIBO 机器人的交互或通过该机器人进行的交互）进行沟通的情况，以及在不涉及任何机器人且使用标准计算机接口的设置下进行沟通的情况。

相反 (Papadopoulos et al., 2012)。该实验涉及 20 对使用视频会议软件进行沟通的参与者。研究结果表明，参与者在使用机器人时表达了更多的社会线索（Social Cues），并且彼此分享了更多的游戏体验。然而，结果还显示，在执行任务（走迷宫）的效率方面，用户在没有机器人辅助时表现更好。这些结果表明，在交互效率与沟通模式（Communication Modes）之间，以及在调解人与人之间接触和支持关系方面的社会相关性（Social Relevance）之间，存在着微妙的平衡与权衡。

第二项实验采用了一款竞争性较低的协作游戏（Collaborative Game），名为 AIBOStory。通过使用远程交互式故事讲述系统（Remote Interactive Story-telling System），参与者可以通过一个集成且自主的机器人伙伴，在两名远程用户之间充当社会中介（Social Mediator），共同创建并分享共同的故事。在初步研究（Pilot Study）之后，主实验研究了 10 对使用 AIBOStory 的参与者的长期交互情况。结果与不涉及任何实体机器人的对照组进行了比较。结果表明用户更倾向于机器人模式，从而支持了这样一种观点：即充当社会中介、提供基于触觉的人机交互（Touch-based Human-Robot Interaction）并嵌入在远程人与人沟通场景中的实体机器人，能够改善人与人之间的沟通与交互 (Papadopoulos, 2012b)。

将机器人用作社会中介（social mediators）的方法，与将机器人视为“永久性”工具或伴侣的方法截然不同——一旦中介作用（mediation）取得成功，中介就不再被需要。例如，一个从机器人中介那里学到了所有知识的孩子将不再需要该机器人；一对分居数月的夫妇在团聚后也将不再需要远程通信技术（remote communication technology）。因此，机器人中介的最终目标应该是，在“任务”完成后最终消失。
