# 12. 情感计算（Affective Computing）

**来源**：The Encyclopedia of Human-Computer Interaction, 2nd Ed.
**Notion 原页面**：https://www.notion.so/0b9e35a5bf5e497183f151a351ce5b48

---

[Kristina Höök](https://www.interaction-design.org/literature/author/kristina-hook)
随着人机交互（Human-Computer Interaction, [HCI](https://www.interaction-design.org/literature/topics/human-computer-interaction)）和 [交互设计](https://www.interaction-design.org/literature/topics/interaction-design)（Interaction Design）从设计和评估面向工作的应用程序，转向处理面向休闲的应用程序（如游戏、[社交计算](https://www.interaction-design.org/literature/topics/social-computing)（social computing）、艺术以及 [创造力](https://www.interaction-design.org/literature/topics/creativity)（creativity）工具），我们不得不考虑例如：什么构成了“体验（experience）”、如何处理用户的“情感（emotions）”，以及理解“审美（aesthetic）”实践与体验。在这里，我将简要阐述为什么 [情感](https://www.interaction-design.org/literature/topics/emotion)（emotion）在我们的领域中成为了一个如此重要的研究方向。

作者/版权持有者：由 Rikke Friis Dam 和 Mads Soegaard 提供。版权条款和许可：CC-Att-ND (Creative Commons Attribution-NoDerivs 3.0 Unported)。

[情感计算](https://www.interaction-design.org/literature/topics/affective-computing)（Affective Computing）视频 1 —— 情感计算与情感交互导论

作者/版权持有者：由 Rikke Friis Dam 和 Mads Soegaard 提供。版权条款与许可：CC-Att-ND (Creative Commons Attribution-NoDerivs 3.0 Unported)。
情感计算（Affective Computing）视频 2 - 主要指南与未来方向

作者/版权持有者：由 Rikke Friis Dam 和 Mads Soegaard 提供。版权条款与许可：CC-Att-ND (Creative Commons Attribution-NoDerivs 3.0 Unported)。
情感计算（Affective Computing）视频 3 - 设计应对压力的情感交互产品

作者/版权持有者：由 Rikke Friis Dam 和 Mads Soegaard 提供。版权条款与许可：CC-Att-ND (Creative Commons Attribution-NoDerivs 3.0 Unported)。
情感计算（Affective Computing）视频 4 - 商业价值、价值与灵感

我首先描述了多个不同学术领域中将情感重新视为一个有价值的研究课题的科研浪潮。事实上，在此之前，极少数不将情感视为“问题”的情感及其表达研究，最早可追溯到 Darwin 在 1872 年出版的 “The Expression of the Emotions in Man and Animals” (Darwin, 1872)。在 Darwin 之后，学术界的注意力大多集中在情感如何干扰理性思考上。

新一波关于情感的研究激发了人工智能（Artificial Intelligence, AI）研究人员和人机交互（Human-Computer Interaction, HCI）研究人员的灵感。特别是 Rosalind Picard 在其著作 “Affective Computing” 中所做的工作，为我们的领域开辟了一项可行的研究议程（research agenda）(Picard, 1997)。但正如任何运动一样

在人机交互（HCI）领域，针对这一主题存在不同的理论视角。对 Picard 的认知主义情感模型（cognitivistic models of emotion）的一种反向反应源于 Sengers, Gaver, Dourish 以及我本人的研究（Boehner et al 2005, Boehner et al 2007, dePaula and Dourish 2005, Gaver 2009, Höök, 2008, Höök et al., 2008）。这一分支的研究——情感交互（Affective Interaction）并没有采用认知主义框架，而是借鉴了[现象学（phenomenology）](https://www.interaction-design.org/literature/topics/phenomenology)，并将情感视为在交互中构建的——无论是在人与人之间，还是在人与机器之间。

虽然这两个关于情感设计的研究方向提供了许多深刻的见解、新颖的应用和更优秀的设计，但近期两者都转向了一个更务实的设计目标，即情感仅是我们必须考虑的参数（parameters）之一。情感不再被置于[设计过程（design process）](https://www.interaction-design.org/literature/topics/design-process)的中心位置，而被视为有助于实现整体设计目标的组成部分之一。特别是在我们致力于设计各种体验和交互时，它成为了一个至关重要的考量因素。

## 12.1 历史：情感的复兴

20 世纪 90 年代，心理学（如 Ellsworth and Scherer, 2003）、神经科学（如 LeDoux, 1996）、医学（如 Damasio, 1995）和社会学（如 Katz, 1999）等多个领域掀起了一波关于情感作用的新研究浪潮。在这波新研究出现之前，正如我所提到的，情感一直被认为是一个低地位的研究课题，研究人员主要关注情感如何干扰我们的理性思维（Rational Thinking）。当时的研究结果集中在诸如：当飞行员极度恐惧时，会产生隧道视野（Tunnel Vision），从而无法察觉飞行环境中的重要变化；在商务会议中因对同事不满而愤怒，可能会破坏对话；或者在做演示报告时过于紧张，可能会导致你丢失论证思路。总的来说，在“理性-情感”这一二元对立（Dualistic Pair）中，情感被视为价值较低的一方，并且在“心灵-身体（Mind-Body）”和“男性-女性（Male-Female）”的对立中，情感与身体及女性相关联。这种二元论的概念化（Dualistic Conceptualisation）可以追溯到古希腊哲学家。在西方思想中，心灵与身体的分离被认为是毋庸置疑的；例如，Descartes 曾试图寻找能够将（受上帝启发的）思想与身体行为联系起来的腺体，见图 1。

![](https://public-media.interaction-design.org/images/encyclopedia/affective_computing/Descartes_mind_and_body.jpg)

版权条款与许可：pd（公有领域（Public Domain），指属于公共财产且不含原创作者身份的信息）。

**图 12.1**：René Descartes 对二元论（Dualism）的[插图](https://www.interaction-design.org/literature/topics/illustration)。输入信息由感觉器官传递至大脑中的松果体（Epiphysis），并由此传递给非物质精神（Immaterial Spirit）。

但随着 20 世纪 90 年代新一波研究浪潮的到来，情绪（Emotion）被重新审视并赋予了新的角色。人们意识到，情绪是理性行为的基础。如果没有情绪过程，我们无法生存下来。当被捕食者（或敌机）追猎时，我们需要将所有资源集中在逃跑或攻击上。在这种情况下，隧道视野（Tunnel Vision）具有其合理性。除非我们能将不安感与危险情境（例如不应食用的食物，或意图伤害我们的人）联系起来，否则我们将一次又一次地犯同样的错误，见图 2。

![](https://public-media.interaction-design.org/images/encyclopedia/affective_computing/cockpit_information_usability_critical.jpg)

作者/版权持有者：由 Master Sgt. Lance Cheung 提供。版权条款与许可：pd（公有领域（Public Domain），指属于公共财产且不含原创作者身份的信息）。

**图 12.2**：专注于敌机，产生隧道视野。

虽然恐惧和愤怒似乎对我们的生存技能最为重要，但我们积极且更复杂的社会导向（Socially-oriented）情绪体验同样

这对我们的生存至关重要。如果我们无法理解灵长类群体中其他成员的情绪，我们就无法维持和平、分享食物，也无法建立联盟与友谊，从而分享群体共同创造的成果 (Dunbar, 1997)。为了让孩子能够在如此复杂的社会关系网络中生存，羞耻感（shame）、内疚感（guilt）和尴尬感（embarrassment）等体验被用来塑造他们的行为 (Lutz 1986, Lutz 1988)。但 [正向情感（positive emotions）](https://www.interaction-design.org/literature/topics/positive-emotions) 在抚养孩子过程中同样扮演着重要角色：例如传达我们对孩子的自豪感，让他们感到被成年人关注和需要，以及给予他们无条件的爱。

新一波的研究还质疑了传统的笛卡尔二元论（Cartesian dualistic division）中关于心灵与身体的划分。情感体验并非仅存在于我们的心灵或大脑中，而是由我们的整个身体所体验的：包括血流中的激素变化、肌肉紧张或放松的神经信号、血液涌向身体的不同部位，以及身体姿态、动作和面部表情 (Davidson et al., 2002)。我们的身体反应反过来会反馈给心灵，产生调节思维的体验，而这些体验又会进一步反馈给身体。事实上，情感体验可以始于身体动作；例如，狂野地舞蹈可能会让你感到快乐。神经学家研究了大脑的工作方式以及

情感过程（emotion processes）如何成为[认知（cognition）](https://www.interaction-design.org/literature/topics/cognition)的关键组成部分。

情感过程基本上处于大多数处理流程的中心，这些流程从大脑的前额叶（frontal lobe）处理开始，通过脑干（brain stem）传递至身体，然后再返回（LeDoux, 1996），见图 3。

![](https://public-media.interaction-design.org/images/encyclopedia/affective_computing/brain-amygdala-thalamus.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 12.3**：LeDoux 关于看到蛇时恐惧感的模型。

身体动作（bodily movements）与情感过程紧密耦合（tightly coupled）。正如哲学家 Maxine Sheets-Johnstone 在 *The Corporeal Turn: A interdisciplinary reader* 中所讨论的，动作与情感之间存在一种“*既是生成性的又是表达性的关系（a generative as well as expressive relationship）*”（Sheets-Johnstone, 2009）。特定的动作会产生情感过程，反之亦然。

但情感体验不仅以在身体不同部位之间往复运行的过程形式存在于我们的身体“内部”，在某种意义上，它们还分布在我们所处的社会环境（social setting）之中（Katz, 1999, Lutz, 1986, Lutz 1988, Parkinson, 1996）。情感不（仅仅）是大脑中硬编码（hard-wired）的处理过程，而是我们社会自我（social selves）中可变且有趣的调节过程。因此，它们是

情绪构建于我们自身与我们所生活的文化和社会环境之间的对话之中。情绪是一种社会性的、动态的沟通机制（communication mechanism）。我们学习在何时以及如何表达某些情绪才是恰当的，并学习在不同的文化、语境（contexts）和情境（situations）下如何恰当地表达情绪。我们理解情绪的方式，是身体内部的经验过程（experiential processes）与情绪在现实世界特定情境中产生及表达方式的结合，这种表达是在与他人的交互（interaction）中完成的，并受到我们所习得的文化实践（cultural practices）的影响。我们在生理上会受到他人情绪体验的影响。微笑具有传染性。

例如，Catherine Lutz 展示了南太平洋 Ifaluk 环礁上的居民将一种特定形式的愤怒称为 *song*，这种愤怒在他们的社会中起到了重要的社会化（socializing）作用 (Lutz, 1986, Lutz 1988)。根据 Lutz 的观点，*song* 是一种“正当的愤怒（justifiable anger）”，被用于对待孩子或下属，以教导他们适当的行为，例如在共同进餐时承担应尽的份额、未能向长辈表示尊重或行为不符合社会规范。

Jack Katz (1999) 的民族志（Ethnographic）研究为我们详细描述了人们如何以个人或群体的形式，将积极地产生情绪作为其社会实践的一部分。例如，他讨论了在趣味镜展（funny mirror show）的参观者中，快乐和笑声是如何在同行好友之间被“产生（produced）”并调节的。当他们移步至一面新镜子前时，

面对镜像时试探性地轻笑，瞥一眼你的朋友，而对方可能会因此靠近，最终在共同站在镜子前时演变为“真实的”笑声。当 Katz 讨论洛杉矶驾驶员的愤怒情绪时（见图 4），他将这种情感的产生（production of emotion）置于一个更广泛且复杂的社会与群体环境中。他展示了愤怒是如何作为与汽车、道路以及整体出行体验的具身性（embodiment）缺失而产生的结果。他将道路上的社会状况、车辆及其驾驶员之间沟通可能性的匮乏，以及我们基于文化背景或种族对他人的驾驶能力的偏见等因素联系起来，并阐明所有这些因素是如何共同解释愤怒产生的原因及其时机（例如，当我们被另一辆车强行插队时）。他甚至将愤怒视为一种*优雅的*重新获得具身感（sense of embodiment）的方式。

![](https://public-media.interaction-design.org/images/encyclopedia/affective_computing/los_angeles_freeway_road_rage.jpg)
版权条款与许可：pd (Public Domain (公有领域（属于公共财产且不含原创作者身份的信息）))。

**图 12.4**：Katz 在讨论洛杉矶驾驶员的愤怒情绪时，将情感的产生置于一个更广泛且复杂的社会与群体环境中。

## 12.2 技术中的情感？

新一波关于情感的研究在一定程度上也影响了新技术的研究与[创新（innovation）](https://www.interaction-design.org/literature/topics/innovation)。在[人工智能（artificial intelligence）](https://www.interaction-design.org/literature/topics/ai)领域，情感被视为一种重要的调节过程（regulatory process），决定了各类自主系统（autonomous systems）的行为，例如在动态变化的世界中试图生存的机器人（参见 Cañamero, 2005）。

在人机交互（HCI）领域，我们认识到在设计和评估过程中明确考虑用户情感的重要性。广义上，HCI 研究演变为三个不同的方向，分别基于三种截然不同的关于情感与设计的理论视角。

1. 第一种广为人知且极具影响力的视角是由 Rosalind Picard 及其 MIT 团队提出的，随后被许多其他团队采纳，在欧洲最著名的是 HUMAINE 网络。这种受认知科学启发的设计方法在她 1997 年的开创性著作中被命名为 *情感计算（Affective Computing）*。
2. 第二种设计方法可以被视为对情感计算的一种反作用（counter-reaction）。与其从传统的认知和生物学视角出发，*情感交互（Affective Interaction）*方法则始于一种建构主义的、由文化决定的情感视角。其最著名的支持者包括 Phoebe Sengers, Paul

Dourish, Bill Gaver 以及在某种程度上包括我自己 (Boehner et al., 2007, Boehner et al. 2005, Gaver 2009, Sundström et al. 2007, Höök, 2006, Höök 2008, Höök 2009)。

3. 最后，有些人认为将情感（emotion）从整体交互中单独提取出来会误导我们。相反，他们将情感视为我们可能为其进行设计的更宏大的体验整体的一部分——我们可以将这一运动命名为“技术即体验（Technology as Experience）”。在某种意义上，这正是传统设计师和艺术家一直以来所关注的（例如参见 Dewey 1934）——即创造有趣的体验，其中某种特定的情感是一种凝聚且协调的力量，将艺术作品与观众/艺术家这一整体系统中的不同部分统一起来。这一方向的支持者包括 John McCarthy, Peter Wright, [Don Norman](https://www.interaction-design.org/literature/topics/don-norman) 以及 Bill Gaver (McCarthy and Wright, 2004, Norman, 2004, Gaver, 2009)。

让我们详细阐述这三个方向。它们之间存在明显的重叠，特别是“情感交互（Affective Interaction）”和“技术即体验（Technology as Experience）”这两场运动在许多概念和设计目标上具有共性。尽管如此，如果我们将其简化并描述为独立的运动，将有助于我们看出它们在理论基础（theoretical underpinnings）上的差异。

### 12.2.1 情感计算（Affective Computing）

人工智能（Artificial Intelligence, AI）领域采纳了这样一种观点，即人类的理性思维依赖于情感处理（emotional processing）。Rosalind Picard 的《Affective Computing》对 AI 和人机交互（Human-Computer Interaction, HCI）领域都产生了重大影响 (Picard, 1997)。简而言之，她的观点是，应当能够创造出能够与情感或其他情感现象相关联、源自于此或刻意影响这些现象的机器。情感计算的根源实际上来自于神经科学、医学和心理学。它在脑、身体以及与他人和机器的交互过程中，实现了一种关于情感过程的生物学视角（biologistic perspective）。

在情感计算应用的设计中，最被讨论且最广泛采用的方法是基于通常被称为“第一原理（First Principles）”的原则来构建个体情感认知模型（cognitive model of affect）；也就是说，系统是根据一组通用原则来生成其情感状态和相应的表达，而不是依赖于一组硬编码的信号-情感对（hardwired signal-emotion pairs）。该模型与另一个模型相结合，后者试图通过测量我们面部、身体、声音、皮肤所发出的迹象和信号，或者我们关于当前情感过程的言语，来识别用户的情感状态。例如在图 5 中，我们可以看到描绘不同情感的面部表情是如何根据肌肉运动进行分析和分类的。

![](https://public-media.interaction-design.org/images/encyclopedia/affective_computing/paul_ekman_facial_expressions_affective.jpg)
作者/版权持有者：Paul Ekman 1975。版权条款与许可：保留所有权利。经许可转载。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。
**图 12.5**：Ekman 描绘的愤怒、恐惧、厌恶、惊讶、快乐和悲伤的面部表情

![](https://public-media.interaction-design.org/images/encyclopedia/affective_computing/paul_ekman_facial_muscles_affective.jpg)
作者/版权持有者：Greg Maguire。版权条款与许可：保留所有权利。经许可转载。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。
**图 5B**：表达不同情绪时，移动眉毛及眼睛周围的面部肌肉

用户的情绪（Emotions）或情感（Affects）被视为可识别的状态（identifiable states），或者至少是可识别的过程（identifiable processes）。基于识别出的用户情绪状态，其目标是实现尽可能像生命或像人类一样的交互，通过使用各种表达方式，无缝地适应用户的情绪状态并对其产生影响。这可以通过应用诸如 Ortony et al. 1988 提出的规则来实现，参见图 6。

![](https://public-media.interaction-design.org/images/encyclopedia/affective_computing/structure_of_emotion_types.jpg)
作者/版权持有者：Ortony, Clore and Collins。版权条款与许可：摘自 *The cognitive structure of emotions* (1988)，Cambridge University Press。保留所有权利。经许可转载。详见下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”章节。

**图 12.6**：OCC 模型（OCC-model, Ortony et al., 1988）中的一条规则

该模型存在一定的局限性，一方面在于为了对其进行建模而必须简化人类情感，另一方面在于如何通过解读人类发出的迹象和信号来推断终端用户情感状态（Emotional states）的方法较为困难。尽管如此，它仍然为探索机器和人类的智能提供了一种非常有趣的方式。

情感计算（Affective Computing）系统的示例包括 Rosalind Picard 及其同事在情感学习（Affective Learning）方面的工作。众所周知，适当的鼓励和支持可以提高学生的学习成绩 (Kort et al., 2001)。因此，他们提出了一种基于 James A. Russell 的情感环形模型（Circumplex Model of Affect）的情感模型，将学习阶段与情感联系起来，见图 7。其核心理念是构建一个学习伙伴（Learning Companion），用于追踪学生所处的情感状态，并据此决定她需要什么样的帮助。

![](https://public-media.interaction-design.org/images/encyclopedia/affective_computing/russells_circumplex_model_of_affect.jpg)
作者/版权持有者：James A. Russell 和 American Psychological Association。
版权条款与许可：保留所有权利。经许可转载。详见下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”章节。
**图 12.7**：Russell 的情感环形模型（Circumplex Model of Affect）

但 Rosalind Picard 团队最令人感兴趣的应用涉及一些重要问题，例如如何训练自闭症儿童识别他人以及自身的情感状态（Emotional States）并做出相应反应。在最近成立的一家名为 Affectiva 的衍生公司中，他们将这些研究成果投入商业应用——不仅用于帮助自闭症儿童，还用于识别用户对广告的兴趣，或处理呼叫中心中的压力问题。一款能够识别皮电反应（Galvanic Skin Response, GSR）的传感器手环被应用于他们的各种场景中，见图 8。

![](https://public-media.interaction-design.org/images/encyclopedia/affective_computing/q_sensor_skin_conductance_emotional_arousal.jpg)
作者/版权持有者：Affectiva, Inc. 版权条款与许可：保留所有权利。经许可转载。详见下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”章节。
**图 12.8**：这款名为 Q Sensor 的手环用于测量皮肤电导（Skin Conductance），而皮肤电导进而...

与情绪唤醒（Emotional Arousal）相关——包括正向和负向唤醒。

其他组织，例如欧洲的 HUMAINE 网络，正是基于这种对情感交互（Affective Interaction）的视角展开研究。

![](https://public-media.interaction-design.org/images/encyclopedia/affective_computing/affector_phoebe_sengers_et_al.jpg)

作者/版权持有者：Phoebe Sengers, Kirsten Boehner, Simeon Warner, and Tom Jenkin。
版权条款与许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

**图 12.9**：Affector 输出示例

### 12.2.2 情感交互：交互视角（Affective Interaction: The Interactional Approach）

情感交互视角（affective interactional view）与情感计算（affective computing）方法不同，前者将情绪视为在交互中构建的，而后者则是通过计算机应用程序支持人们理解和体验自己的情绪（Boehner et al., 2005, Boehner et al 2007, Höök et al., 2008, Höök 2008）。从交互视角进行设计，其目标并非像典型的情感计算应用那样，试图检测用户某种单一的“正确”或“真实”的情绪并告知用户，而是旨在让情感体验能够被反思（reflection）。这样的系统会创建一种包含人们日常经验的表征（representation），从而让他们能够对其进行反思。用户自身更丰富的解读，保证了这种方式能更“真实”地描述他们的体验。

根据 Kirsten Boehner 及其同事（2007）的观点，交互式设计方法：

1. 将情感（affect）视为社会和文化的产物
1. 依赖并支持解释灵活性（interpretive flexibility）
1. 避免尝试将不可形式化的事物形式化（formalize the unformalizable）
1. 支持更广泛的沟通行为（communication acts）
1. 关注人们如何使用系统来体验和理解情绪
1. 关注设计能够激发对情感的反思和意识的系统

随后，我和我的同事对该列表进行了两项微调（Höök et al., 2008）：

1. 对 #1 的修改：交互方法（interactional approach）将情感（affect）视为一种具身的（embodied）社会、身体和文化产物。
1. 对 #3 的修改：交互方法是非还原论的（non-reductionist）。

第一个变化与情感体验的身体维度相关。通过明确地指出这些方面，我们希望增加与情感交互系统（affective interactive system）交互时可能涉及的一些物理和身体体验。对于 Boehner 及其同事提出的原则列表中的第三条设计原则——“*交互方法避免尝试将不可形式化的东西形式化（formalize the unformalizable）*”，我们采取了略有不同的立场。为了避免用还原论的方式来解释主观或审美体验，Boehner 及其同事试图通过声称人类体验是独特的、解释性的且不可言说的（ineffable），来保护这些概念。这种立场存在将人类体验神秘化的风险，将其定义为不可言说，从而使其被封闭在研究和讨论之外。虽然我全心支持体验统一性（unity of experience）的概念，并支持让人们生活的魔力保持原貌，但我确实认为可以找到一个折中方案，使我们能够实际讨论体验的特质以及如何为其进行设计的知识，而无需将其还原为低于原貌的东西。这绝不意味着体验的维度（experiential strands）或特质是普适的，且对每个人都相同。相反，它们是

...是主观的，且由每个用户以自己的方式来体验 (McCarthy and Wright, 2004)。

为了阐明这一方法，研究者构建了一系列系统，例如 Affector (Sengers et al., 2005)、VIO (Kaye, 2006)、eMoto (Sundström et al., 2009)、Affective Diary (Ståhl et al., 2009) 以及 Affective Health (Ferreira et al., 2010) —— 仅举几例。

Affector 是一个扭曲的视频窗口（distorted video window），用于连接两位朋友（且是同事）相邻的办公室，见图 9。位于视频屏幕下方的摄像头在捕捉视频的同时，还会捕捉“过滤器（filter）”信息，例如光照水平、颜色和运动。这些过滤器信息会对捕捉到的朋友图像进行扭曲，随后将图像投影到相邻办公室的窗口中。朋友们共同决定使用哪些信息作为过滤器以及采用何种扭曲方式，以此来传达对方的情绪感（sense of mood）。

eMoto 是一种针对手机的扩展短信服务（extended SMS-service），允许用户在手机之间发送文本消息；但除了文本之外，消息的背景还具有彩色且动态的形状（见图 11 中的示例）。为了选择一种表达方式，用户可以使用触控笔（stylus pen，部分手机自带）执行一组手势（gestures）；我们为该触控笔增加了传感器，使其能够捕捉压力和摇晃动作。用户不受限于任何特定的手势集，而是可以根据其个人...

偏好。压力与震动动作可以作为人们大多数情感手势（Emotional Gestures）的基础，这一基础允许用户在这些通用特性的之上构建自己的手势，见图 11。

![](https://public-media.interaction-design.org/images/encyclopedia/affective_computing/subjective_experience_of_emotions_dimensional_model_of_emotions.jpg)

作者/版权持有者：Petra Sundström, Anna Ståhl, and Kristina Höök（左侧和右侧图像）以及 James A. Russell 和 American Psychological Association（中间图像）。版权条款与许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 12.10**：不同的肢体动作（左）让人联想到 Russell 提出的情感环形模型（Circumplex Model of Affect）（中）中潜在的情感体验（Affective Experiences），随后这些动作被映射为色彩丰富的动画表达（右），同样也映射到情感环形模型中。

![](https://public-media.interaction-design.org/images/encyclopedia/affective_computing/emoto_affective_computing_2.jpg)

作者/版权持有者：未知（待调查）。版权条款与许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 12.11**：在 eMoto 的最终研究中发送给男友的 eMoto 消息。在...

左图是研究参与者 Agnes 向其男友表达的一种高能量的爱意；右图是 Mona 使用她最喜欢的绿色来表达对男友的爱。

情感日记（Affective Diary）的工作流程如下：用户在开始新的一天时，佩戴一个身体传感器臂带（body sensor armband）。在白天，系统会收集带有时间戳的传感器数据，以捕捉肢体动作和唤醒度（arousal）。同时，系统会记录手机上的各种活动：发送和接收的短信、拍摄的照片，以及附近其他设备的蓝牙存在情况。当用户回到家中后，可以将记录的数据传输到她的情感日记中。收集到的传感器数据被呈现为沿着时间轴排列的、某种程度上较为抽象且形状模糊的有色字符，见图 12。为了帮助用户反思其活动和生理反应，用户可以在日记中随手记录笔记，或对照片及其他数据进行操作，见图 12 中一名用户的示例。

![](https://public-media.interaction-design.org/images/encyclopedia/affective_computing/affective_diary_system_based_on_bio-sensor_data_12.jpg)

作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”章节。

**图 12.12**：情感日记（Affective Diary）系统。生物传感器数据由...表示

屏幕底部是团块状的图形。移动数据被插入在屏幕上半部分，与这些团块状角色处于同一时间轴上。

![](https://public-media.interaction-design.org/images/encyclopedia/affective_computing/affective_diary_13_interactional_approach_to_affective_design.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 12.13**：一名用户在描述这张截屏（screendump）时说道：“[指向橙色角色] 然后我就变成了这样，在这里我有点，在某种程度上我既开心又难过，类似这样。我喜欢他，但我们见面的次数如此之少，这太令人难过了。而我无法真正地表达出来。”

从这三个例子可以看出，设计中的交互式方法（interactional approach）试图避免将人类体验简化为一组由系统生成的、用于解释用户情感状态的测量值或推断。虽然系统的交互不应显得笨拙，但其追求的实际体验可能不仅仅是积极的。eMoto 可能允许你表达对他人的负面感受；Affector 可能会传达你的负面情绪；Affective Diary 则可能会让你痛苦地意识到自己行为中的负面模式。交互式方法关注的是完整的（无限的）...

世界中可能的人类经验（human experience）。

### 12.2.3 技术即体验（Technology as Experience）

虽然到目前为止，我们在某种意义上将情感过程（emotion processes）与“在世存在（being in the world）”的其他方面分离开来，但也有人主张我们需要采取一种整体论方法（holistic approach）来理解情感。情感过程是我们社会化在世存在方式的一部分，它们为我们的梦想、希望以及对世界的体验染上了色彩。如果我们的目标是进行情感化设计，我们需要将情感置于更广泛的体验图景之中，特别是当我们打算在设计过程中探讨审美体验（aesthetic experiences）的相关方面时（Gaver, 2009, McCarthy and Wright, 2004, Hassenzahl, 2008）。

例如，John Dewey 通过将审美体验置于一个尺度上的两个极端之间，将其与我们生活的其他方面区分开来（Dewey, 1934）。在该尺度的一个极端，我们只是在日常生活中随波逐流，经历着无组织的事件流；而在另一个极端，我们经历的事件虽然有明确的开始和结束，但这些事件之间仅是机械地连接在一起。审美体验则存在于这两个极端之间。它们有开始和结束，并且在事后可以被赋予一个独特的名称，例如“*当我在剑桥和 Christian 一起上马术课的时候*”（Höök, 2010）；此外，这种体验具有一种统一性（unity）——有一种单一的特质贯穿于整个体验之中（Dewey 1934, p. 36-57）：

> 一次体验具有一种统一性，赋予了它其

名字，那顿饭，那场风暴，那段友谊的破裂。这种统一性（unity）的存在是由一种单一的特质构成的，尽管其组成部分各异，但这种特质贯穿于整个体验之中。

在 Dewey 的视角中，情感是 (Dewey, 1934 p. 44)：
> 驱动与凝聚的力量（moving and cementing force）。它筛选出契合之物，并用其色彩为被选中的部分着色，从而赋予那些在外部看来迥异且不相似的素材以质的统一性（qualitative unity）。因此，它在体验的各个不同部分之中并贯穿其中，提供了统一性。

然而，情感并非静态的，而是随着体验本身随时间而变化，正如戏剧性体验（dramatic experience）那样 (Dewey 1934, p. 43)。
> 快乐、悲伤、希望、恐惧、愤怒、好奇，这些情感被对待得仿佛每一种本身都是一种现成地进入场景的实体（entity），这种实体可能持续较长时间或较短时间，但其持续时间、生长过程和演变与其本质无关。事实上，当情感具有重要意义时，它们是一个处于变动和变化之中的复杂体验的特质（qualities）。

虽然情感过程（emotion process）不足以创造出审美体验（aesthetic experience），但情感将成为体验的一部分，且与智力体验和身体体验不可分割。在这种整体论视角（holistic perspective）下，将情感过程视为某种独立于我们“在世的具身体验（embodied experience of being in the world）”之物是没有意义的。

Bill Gaver 在讨论情感设计（design for emotion）时也提出了同样的观点 (Gaver 2009)。他主张与其将……隔离

将情感视为某种“*可以像 Campbell 番茄汤里的番茄一样被装罐*”的东西（正如 John Thackara 在批评 Don Norman 关于该主题的研究时所言），我们需要从更广泛的视角来看待交互设计（Interaction Design），允许个体的[挪用（Appropriation）](https://www.interaction-design.org/literature/topics/appropriation)。Bill Gaver 在其著作中清晰地阐述了这一点：

> 显然，情感是体验（Experience）的一个关键维度。但将其称为“体验的一个维度”意味着两点：一是它只是一个更复杂整体（即体验）的一部分；二是它涉及自身之外的某些事物（是对某物的体验）。正是那个“某物”——一把椅子、一个家、衰老的挑战——才是合适的设计对象，而情感只是在处理这些对象时必须考虑的众多关注点之一。从这个角度来看，为情感而设计就像是为“蓝色”而设计：它将一个修饰语变成了名词。想象一下，如果有人告诉你去设计一个“蓝色的东西”。蓝色的什么？鲸鱼？天空？麂皮鞋？这个要求似乎毫无意义。

如果我们回顾 Affector、eMoto 和 Affective Diary 系统，可以清楚地看到，它们的设计目标并非孤立地针对情感。Affector 和 eMoto 是为人们之间的沟通而设计并被用于沟通的，其中情感是整体沟通的一个方面。事实上，Affector 最终被证明并不是关于

情感沟通（emotion communication），而是成为了一个对身在另一个办公室的朋友产生共情式相互感知（sympathetic mutual awareness）的通道。

## 12.3 结语——未来的研究方向

在进行体验设计（designing for experiences）时，我们显然不能忽视情绪过程（emotion processes）的重要性。另一方面，如果将情绪视为一种可以脱离语境（context）而在用户身上被识别的状态，那么这种设计方式将无法在这个领域产生有意义的应用。相反，关于情绪处理（emotion processing）的知识需要被整合到我们的整体设计流程中。

上文概述的情绪设计（emotion design）三个方向的工作，分别以不同的方式深化了我们的理解，即如何增加相关知识，从而使情绪过程成为设计流程中的重要组成部分。情感计算（Affective Computing）领域为我们提供了一系列情感输入（affective input）工具，例如面部识别工具、语音识别、身体姿态识别、生物传感器模型，以及情感输出（affective output）工具，例如界面中角色的情绪表达或机器人行为的调节。情感交互（Affective Interaction）分支则有助于我们理解情绪的社会文化维度（socio-cultural aspects），将其置于具体语境中，确保情绪不仅仅被描述为超出我们控制的生理过程。而“技术即体验”（Technology as Experience）领域则将我们的关注点从将情绪视为一种孤立现象，转向将情绪过程视为为人类设计工具时需要考虑的（重要）方面之一。

目前仍有许多尚未解决的问题

在所有这三个方向上，在我看来，我们尚未在理解和应对情绪过程（emotion processes）的日常、物理和身体体验方面做出足够的努力（例如 Sundström et al., 2007, Ståhl et al., 2009, Höök et al., 2008, Ferreira et al., 2008, Ferreira et al., 2010, Sundström et al., 2009, Ferreira and Höök, 2011）。早在 1872 年，Charles Darwin 就将情绪与身体动作（bodily movement）紧密联系在一起（Darwin, 1872）。从那时起，神经学（neurology）（leDoux 1996, Davidson et al., 2003）、哲学与舞蹈（Sheets-Johnstone, 1999, Laban and Lawrence, 1974）以及戏剧（Boal, 1992）等不同领域的研究者，都描述了行动准备（readiness to action）、肌肉活动（muscular activity）与情绪共现（co-occurrence of emotion）之间的紧密耦合。

正如 Sheets-Johnstone (1999) 所讨论的，我认为我们真实的具身躯体（corporeal bodies）是在世存在（being in the world）、创造体验、学习和认知中的关键。我们的身体并非我们用来传递信息的工具或客体。沟通是具身的（embodied）——它涉及我们的整个自我。在设计领域，我们对身体能为我们提供什么的看法非常局限。这在一定程度上是因为当时的技术尚不足以涵盖更多的感官、动作和更丰富的模态（modalities）。现在，得益于新型的传感与执行器材料（sensing and actuator materials），我们可以设想为许多不同类型的身体体验进行设计——例如正念（mindfulness）、情感环路（affective loops）、兴奋感、缓慢的内在倾听（slow inwards listening）、心流（flow）以及反思（reflection）。

或沉浸感（Immersion）（参见例如 Moen, 2006, Isbister and Höök, 2009, Hummels et al., 2007）。在近期兴起的[身体美学](https://www.interaction-design.org/literature/topics/somaesthetics)（Somaesthetics）设计领域（Schiphorst, 2007）中，能够增强身体意识（body awareness）的身体学习过程（bodily learning processes）中的有趣方面被捕捉并明确地应用于设计之中。这与大多数商业体育应用（例如计步器或心率计）形成对比，在这些应用中，身体通常被视为心智的工具或客体，被动地接收符号和信号，而非主动地参与到信号的产生过程中。最近，Purpura 及其同事（2011）采用了一种批判性设计方法（Critical Design Method），以精准地指出这种观点所带来的一些问题。通过描述一个名为 Fit4Life 的虚构系统（该系统可测量饮食的方方面面），他们构思出了这样一个系统：就在你准备拿一个甜甜圈时，它可能会在你耳边低语：“对不起，Dave，你不该吃那个。Dave，你知道我不喜欢你吃甜甜圈。”这个虚构系统展示了我们如何轻易地跨越从说服（Persuasion）到强迫（Coercion）之间的细线，从而导致对我们的行为和身体进行技术控制。在我看来，通过设计明确关注[美学](https://www.interaction-design.org/literature/topics/aesthetics)（Aesthetics）、身体美学（Somaesthetics）以及[共情](https://www.interaction-design.org/literature/topics/empathy)（Empathy）的应用……

通过与自身及他人的交互，我们可以超越贫乏的交互模态（Interaction Modalities），以及将身体视为可被修剪和控制的单纯机器的观念，转向基于人类物理栖居（Physically inhabiting）世界之方式的、更丰富且更有意义的交互。

当我们在设计过程中更明确地探讨情感（Emotions）与体验（Experiences）时，我们才刚刚开始揭示许多新颖的设计可能性。这是一个极其丰富的研究领域，我希望它能吸引许多年轻的设计师、设计研究者以及人机交互（HCI）专家。

## 12.4 References

[Boal](https://www.interaction-design.org/references/authors/augusto_boal.html), Augusto (1992): *Games for Actors and Non-Actors.* Routledge
[Boehner](https://www.interaction-design.org/references/authors/kirsten_boehner.html), Kirsten, [dePaula](https://www.interaction-design.org/references/authors/rogerio_depaula.html), Rogerio, [Dourish](https://www.interaction-design.org/references/authors/paul_dourish.html), Paul and [Sengers](https://www.interaction-design.org/references/authors/phoebe_sengers.html), Phoebe (2007): *How emotion is made and measured*. In [International Journal of Human-Computer Studies](https://www.interaction-design.org/references/periodicals/international_journal_of_human-computer_studies.html), 65 (4) pp. 275-291

[Boehner](https://www.interaction-design.org/references/authors/kirsten_boehner.html), Kirsten, [dePaula](https://www.interaction-design.org/references/authors/rogerio_depaula.html), Rogerio, [Dourish](https://www.interaction-design.org/references/authors/paul_dourish.html), Paul and [Sengers](https://www.interaction-design.org/references/authors/phoebe_sengers.html), Phoebe (2005): Affect: from information to interaction. In: [Bertelsen](https://www.interaction-design.org/references/authors/olav_w__bertelsen.html), Olav W., [Bouvin](https://www.interaction-design.org/references/authors/niels_olof_bouvin.html), Niels Olof, [Krogh](https://www.interaction-design.org/references/authors/peter_gall_krogh.html), Peter Gall and [Kyng](https://www.interaction-design.org/references/authors/morten_kyng.html), Morten (eds.) [Proceedings of the 4th Decennial Conference on Critical Computing 2005](https://www.interaction-design.org/references/conferences/proceedings_of_the_4th_decennial_conference_on_critical_computing_2005.html) August 20-24, 2005, Aarhus, Denmark. pp. 59-68
[Cañamero](https://www.interaction-design.org/references/authors/lola_ca%F1amero.html), Lola (2005): *Emotion understanding from the perspective of autonomous robots research*. In [Neural Networks](https://www.interaction-design.org/references/periodicals/neural_networks.html), 18 (4) pp. 445-455

[Damasio](https://www.interaction-design.org/references/authors/antonio_r__damasio.html), Antonio R. (1995): *Descartes' Error: Emotion, Reason, and the Human Brain.* Harper Perennial
[Darwin](https://www.interaction-design.org/references/authors/charles_darwin.html), Charles (0000): *The Expression of the Emotions in Man and Animals.* London, UK, John Murray
[Davidson](https://www.interaction-design.org/references/authors/richard_j__davidson.html), Richard J., [Scherer](https://www.interaction-design.org/references/authors/klaus_r__scherer.html), Klaus R. and [Goldsmith](https://www.interaction-design.org/references/authors/h__hill_goldsmith.html), H. Hill (2002b): *Handbook of Affective Sciences.* Oxford University Press, USA

[Davidson](https://www.interaction-design.org/references/authors/richard_j__davidson.html), Richard J., [Pizzagalli](https://www.interaction-design.org/references/authors/diego_pizzagalli.html), Diego, [Nitschke](https://www.interaction-design.org/references/authors/jack_b__nitschke.html), Jack B. and [Kalin](https://www.interaction-design.org/references/authors/ned_h__kalin.html), Ned H. (2002a): Parsing the subcomponents of emotion and disorders of emotion: perspectives from affective neuroscience. In: [Davidson](https://www.interaction-design.org/references/authors/richard_j__davidson.html), Richard J., [Scherer](https://www.interaction-design.org/references/authors/klaus_r__scherer.html), Klaus R. and [Goldsmith](https://www.interaction-design.org/references/authors/h__hill_goldsmith.html), H. Hill (eds.). "Handbook of Affective Sciences". Oxford University Press, USA
[dePaula](https://www.interaction-design.org/references/authors/rogerio_depaula.html), Rogerio and [Dourish](https://www.interaction-design.org/references/authors/paul_dourish.html), Paul (2005): Cognitive and Cultural Views of Emotions. In: [Proceedings of the Human Computer Interaction Consortium Winter Meeting](https://www.interaction-design.org/references/conferences/proceedings_of_the_human_computer_interaction_consortium_winter_meeting.html) 2005, Douglas, CO, USA.
[Dewey](https://www.interaction-design.org/references/authors/john_dewey.html), John (1934): *Art as Experience.* Perigee Trade

[Dunbar](https://www.interaction-design.org/references/authors/robin_dunbar.html), Robin (1997): *Grooming, Gossip, and the Evolution of Language.* Harvard University Press
[Dunbar](https://www.interaction-design.org/references/authors/robin_dunbar.html), Robin (1998): *Grooming, Gossip, and the Evolution of Language.* Harvard University Press
[Ellsworth](https://www.interaction-design.org/references/authors/phoebe_c__ellsworth.html), Phoebe C. and [Scherer](https://www.interaction-design.org/references/authors/klaus_r__scherer.html), Klaus R. (2003): Appraisal processes in emotion. In: [Davidson](https://www.interaction-design.org/references/authors/richard_j__davidson.html), Richard J., [Sherer](https://www.interaction-design.org/references/authors/klaus_r__sherer.html), Klaus R. and [Goldsmith](https://www.interaction-design.org/references/authors/h__hill_goldsmith.html), H. Hill (eds.). "Handbook of Affective Sciences". Oxford University Press, USA
[Ferreira](https://www.interaction-design.org/references/authors/pedro_ferreira.html), Pedro and [Höök](https://www.interaction-design.org/references/authors/kristina_h%F6%F6k.html), Kristina (2011): Bodily Orientations around Mobiles: Lessons learnt in Vanuatu. In:[Proceedings of the ACM CHI Conference on Human Factors in Computing Systems](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_conference_on_human_factors_in_computing_systems.html) 7-12 May, 2011, Vancouver, Canada.

[Ferreira](https://www.interaction-design.org/references/authors/pedro_ferreira.html), Pedro, [Sanches](https://www.interaction-design.org/references/authors/pedro_sanches.html), Pedro, [Höök](https://www.interaction-design.org/references/authors/kristina_h%F6%F6k.html), Kristina and [Jaensson](https://www.interaction-design.org/references/authors/tove_jaensson.html), Tove (2008): License to chill!: how to empower users to cope with stress. In: [Proceedings of the Fifth Nordic Conference on Human-Computer Interaction](https://www.interaction-design.org/references/conferences/proceedings_of_the_fifth_nordic_conference_on_human-computer_interaction.html) 2008. pp. 123-132
[Gaver](https://www.interaction-design.org/references/authors/william_gaver.html), William (2009): *Designing for emotion (among other things)*. In [Philosophical Transactions of the Royal Society](https://www.interaction-design.org/references/periodicals/philosophical_transactions_of_the_royal_society.html), 364 (1535) pp. 3597-3604
[Grosz](https://www.interaction-design.org/references/authors/elizabeth_grosz.html), Elizabeth (1994): *Volatile Bodies: Toward a Corporeal Feminism (Theories of Representation and Difference).* Indiana University Press

[Hummels](https://www.interaction-design.org/references/authors/caroline_hummels.html), Caroline, [Overbeeke](https://www.interaction-design.org/references/authors/kees_overbeeke.html), Kees and [Klooster](https://www.interaction-design.org/references/authors/sietske_klooster.html), Sietske (2007): *Move to get moved: a search for methods, tools and knowledge to design for expressive and rich movement-based interaction*. In [Personal and Ubiquitous Computing](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing.html), 11 (8) pp. 677-690
[Hutchins](https://www.interaction-design.org/references/authors/edwin_hutchins.html), Edwin (1995): *Cognition in the wild.* Cambridge, Mass, MIT Press
[Höök](https://www.interaction-design.org/references/authors/kristina_h%F6%F6k.html), Kristina (2009): *Affective loop experiences: designing for interactional embodiment*. In [Philosophical Transactions of the Royal Society](https://www.interaction-design.org/references/periodicals/philosophical_transactions_of_the_royal_society.html), 364 p. 3585–3595

[Höök](https://www.interaction-design.org/references/authors/kristina_h%F6%F6k.html), Kristina (2008): Affective Loop Experiences - What Are They?. In: [Oinas-Kukkonen](https://www.interaction-design.org/references/authors/harri_oinas-kukkonen.html), Harri, [Hasle](https://www.interaction-design.org/references/authors/per_f__v__hasle.html), Per F. V.,[Harjumaa](https://www.interaction-design.org/references/authors/marja_harjumaa.html), Marja, [Segerståhl](https://www.interaction-design.org/references/authors/katarina_segerst%E5hl.html), Katarina and [Øhrstrøm](https://www.interaction-design.org/references/authors/peter_%D8hrstr%F8m.html), Peter (eds.) [PERSUASIVE 2008 - Persuasive Technology, Third International Conference](https://www.interaction-design.org/references/conferences/persuasive_2008_-_persuasive_technology%2C_third_international_conference.html) June 4-6, 2008, Oulu, Finland. pp. 1-12
[Höök](https://www.interaction-design.org/references/authors/kristina_h%F6%F6k.html), Kristina (2006): Designing familiar open surfaces. In: [Proceedings of the Fourth Nordic Conference on Human-Computer Interaction](https://www.interaction-design.org/references/conferences/proceedings_of_the_fourth_nordic_conference_on_human-computer_interaction.html) 2006. pp. 242-251

[Höök](https://www.interaction-design.org/references/authors/kristina_h%F6%F6k.html), Kristina (2010): Transferring qualities from horseback riding to design. In: [Proceedings of the Sixth Nordic Conference on Human-Computer Interaction](https://www.interaction-design.org/references/conferences/proceedings_of_the_sixth_nordic_conference_on_human-computer_interaction.html) 2010. pp. 226-235
[Höök](https://www.interaction-design.org/references/authors/kristina_h%F6%F6k.html), Kristina, [Ståhl](https://www.interaction-design.org/references/authors/anna_st%E5hl.html), Anna, [Sundström](https://www.interaction-design.org/references/authors/petra_sundstr%F6m.html), Petra and [Laaksolaahti](https://www.interaction-design.org/references/authors/jarmo_laaksolaahti.html), Jarmo (2008): Interactional empowerment. In:[Proceedings of ACM CHI 2008 Conference on Human Factors in Computing Systems](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2008_conference_on_human_factors_in_computing_systems.html) April 5-10, 2008. pp. 647-656
[Isbister](https://www.interaction-design.org/references/authors/katherine_isbister.html), Katherine and [Höök](https://www.interaction-design.org/references/authors/kristina_h%F6%F6k.html),
 Kristina (2009): On being supple: in search of rigor without rigidity 
in meeting new design and evaluation challenges for HCI practitioners.

In: [Proceedings of ACM CHI 2009 Conference on Human Factors in Computing Systems](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2009_conference_on_human_factors_in_computing_systems.html) 2009. pp. 2233-2242
[Katz](https://www.interaction-design.org/references/authors/jack_katz.html), Jack (2001): *How Emotions Work.* University of Chicago Press
[Katz](https://www.interaction-design.org/references/authors/jack_katz.html), Jack (1999): *How Emotions Work.* University of Chicago Press
[Kaye](https://www.interaction-design.org/references/authors/joseph_jofish_kaye.html), Joseph Jofish (2006): I just clicked to say I love you: rich evaluations of minimal communication. In: [Olson](https://www.interaction-design.org/references/authors/gary_m__olson.html), Gary M. and [Jeffries](https://www.interaction-design.org/references/authors/robin_jeffries.html), Robin (eds.) [Extended Abstracts Proceedings of the 2006 Conference on Human Factors in Computing Systems](https://www.interaction-design.org/references/conferences/extended_abstracts_proceedings_of_the_2006_conference_on_human_factors_in_computing_systems.html) April 22-27, 2006, Montréal, Québec, Canada. pp. 363-368
[Kort](https://www.interaction-design.org/references/authors/barry_kort.html), Barry, [Reilly](https://www.interaction-design.org/references/authors/rob_reilly.html), Rob and [Picard](https://www.interaction-design.org/references/authors/rosalind_w__picard.html),

 Rosalind W. (2001): An Affective Model of Interplay between Emotions 
and Learning: Reengineering Educational Pedagogy - Building a Learning 
Companion. In: [ICALT 2001](https://www.interaction-design.org/references/conferences/icalt_2001.html) 2001. pp. 43-48
[Laban](https://www.interaction-design.org/references/authors/rudolf_von_laban.html), Rudolf von and [Lawrence](https://www.interaction-design.org/references/authors/f__c__lawrence.html), F. C. (1974): *Effort: economy in body movement.* Plays, inc
[Ledoux](https://www.interaction-design.org/references/authors/joseph_ledoux.html), Joseph (1996): *The Emotional Brain: The mysterious underpinnings of emotional life.* Simon and Schuster
[Ledoux](https://www.interaction-design.org/references/authors/joseph_ledoux.html), Joseph (1998): *The Emotional Brain: The mysterious underpinnings of emotional life.* Simon and Schuster
[Longo](https://www.interaction-design.org/references/authors/giuseppe_o__longo.html), Giuseppe O. (2003): Body and Technology: Continuity or Discontinuity?. In: [Fortunati](https://www.interaction-design.org/references/authors/leopoldina_fortunati.html), Leopoldina, [Katz](https://www.interaction-design.org/references/authors/james_e__katz.html), James E. and [Riccini](https://www.interaction-design.org/references/authors/raimonda_riccini.html), Raimonda (eds.). "Mediating the Human Body: Technology, Communication, and Fashion". Routledge

[Lutz](https://www.interaction-design.org/references/authors/catherine_lutz.html), Catherine (1986): *Emotion, Thought, and Estrangement: Emotion as a Cultural Category*. In [Cultural Anthropology](https://www.interaction-design.org/references/periodicals/cultural_anthropology.html), 1 (3) pp. 287-309
[Lutz](https://www.interaction-design.org/references/authors/catherine_a__lutz.html), Catherine A. (1988): *Unnatural Emotions: Everyday Sentiments on a Micronesian Atoll and Their Challenge to Western Theory.* University of Chicago Press
[McCarthy](https://www.interaction-design.org/references/authors/john_mccarthy.html), John and [Wright](https://www.interaction-design.org/references/authors/peter_wright.html), Peter (2004): *Technology as Experience.* The MIT Press
[Merleau-Ponty](https://www.interaction-design.org/references/authors/maurice_merleau-ponty.html), Maurice (1958): *Phenomenology of *[*Perception*](https://www.interaction-design.org/literature/topics/perception)*.* London, England, Routledge
[Moen](https://www.interaction-design.org/references/authors/jin_moen.html), Jin (2006). *KinAesthetic Movement Interaction : Designing for the Pleasure of Motion (Doctoral Thesis)*. KTH
[Norman](https://www.interaction-design.org/references/authors/donald_a__norman.html), Donald A. (2004): [*Emotional Design*](https://www.interaction-design.org/literature/topics/emotional-design)*: Why We Love (Or Hate) Everyday Things.* Basic Books

[Ortony](https://www.interaction-design.org/references/authors/andrew_ortony.html), Andrew, [Clore](https://www.interaction-design.org/references/authors/gerald_l__clore.html), Gerald L. and [Collins](https://www.interaction-design.org/references/authors/allan_collins.html), Allan (1988): *The Cognitive Structure of Emotions.* Cambridge University Press
[Ortony](https://www.interaction-design.org/references/authors/andrew_ortony.html), Andrew, [Clore](https://www.interaction-design.org/references/authors/gerald_l__clore.html), Gerald L. and [Collins](https://www.interaction-design.org/references/authors/allan_collins.html), Allan (1990): *The Cognitive Structure of Emotions.* Cambridge University Press
[Parkinson](https://www.interaction-design.org/references/authors/b__parkinson.html), B. (1996): *Emotions are social*. In [British Journal of Psychology](https://www.interaction-design.org/references/periodicals/british_journal_of_psychology.html), 87 p. 663–683
[Picard](https://www.interaction-design.org/references/authors/rosalind_w__picard.html), Rosalind W. (1997): *Affective computing.* Ma, USA, The MIT Press

[Purpura](https://www.interaction-design.org/references/authors/stephen_purpura.html), Stephen, [Schwanda](https://www.interaction-design.org/references/authors/victoria_schwanda.html), Victoria, [Williams](https://www.interaction-design.org/references/authors/kaiton_williams.html), Kaiton, [Stubler](https://www.interaction-design.org/references/authors/william_stubler.html), William and [Sengers](https://www.interaction-design.org/references/authors/phoebe_sengers.html), Phoebe (2011): Fit4life: the design of a persuasive technology promoting healthy behavior and ideal weight. In: [Proceedings of ACM CHI 2011 Conference on Human Factors in Computing Systems](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2011_conference_on_human_factors_in_computing_systems.html) 2011. pp. 423-432
[Russell](https://www.interaction-design.org/references/authors/james_a__russell.html), James A. (1980): *Circumplex Model of Affect*. In [Journal of Personality and Social Psychology](https://www.interaction-design.org/references/periodicals/journal_of_personality_and_social_psychology.html), 39 (6) pp. 1161-1178

[Sanches](https://www.interaction-design.org/references/authors/pedro_sanches.html), Pedro, [Höök](https://www.interaction-design.org/references/authors/kristina_h%F6%F6k.html), Kristina, [Vaara](https://www.interaction-design.org/references/authors/elsa_vaara.html), Elsa, [Weymann](https://www.interaction-design.org/references/authors/claus_weymann.html), Claus, [Bylund](https://www.interaction-design.org/references/authors/markus_bylund.html), Markus, [Ferreira](https://www.interaction-design.org/references/authors/pedro_ferreira.html), Pedro, [Peira](https://www.interaction-design.org/references/authors/nathalie_peira.html), Nathalie and[Sjölinder](https://www.interaction-design.org/references/authors/marie_sj%F6linder.html), Marie (2010): Mind the body!: designing a mobile stress management application encouraging personal reflection. In: [Proceedings of DIS10 Designing Interactive Systems](https://www.interaction-design.org/references/conferences/proceedings_of_dis10_designing_interactive_systems.html) 2010. pp. 47-56
[Schiphorst](https://www.interaction-design.org/references/authors/thecla_schiphorst.html), Thecla (2007): Really, really small: the palpability of the invisible. In: [Proceedings of the 2007 Conference on Creativity and Cognition](https://www.interaction-design.org/references/conferences/proceedings_of_the_2007_conference_on_creativity_and_cognition.html) 2007, Washington DC, USA. pp. 7-16

[Sengers](https://www.interaction-design.org/references/authors/phoebe_sengers.html), Phoebe, [Boehner](https://www.interaction-design.org/references/authors/kirsten_boehner.html), Kirsten, [Warner](https://www.interaction-design.org/references/authors/simeon_warner.html), Simeon and [Jenkins](https://www.interaction-design.org/references/authors/tom_jenkins.html), Tom (2005): Evaluating Affector: Co-Interpreting What 'Works'. In: [CHI 2005 Workshop on Innovative Approaches to Evaluating Affective Systems](https://www.interaction-design.org/references/conferences/chi_2005_workshop_on_innovative_approaches_to_evaluating_affective_systems.html) 2005.
[Sheets-Johnstone](https://www.interaction-design.org/references/authors/maxine_sheets-johnstone.html), Maxine (2009): *The Corporeal Turn: An Interdisciplinary Reader.* Imprint Academic
[Sheets-Johnstone](https://www.interaction-design.org/references/authors/m__sheets-johnstone.html), M. (1999): *Emotion and Movement: A beginning Empirical-Phenomenological Analysis of Their Relationship*. In [Journal of Consciousness Studies](https://www.interaction-design.org/references/periodicals/journal_of_consciousness_studies.html), 6 (11) pp. 259-277
[Shusterman](https://www.interaction-design.org/references/authors/richard_shusterman.html), Richard (2008): *Body Consciousness: A Philosophy of Mindfulness and Somaesthetics.* Cambridge University Press

[Ståhl](https://www.interaction-design.org/references/authors/anna_st%E5hl.html), Anna, [Höök](https://www.interaction-design.org/references/authors/kristina_h%F6%F6k.html), Kristina, [Svensson](https://www.interaction-design.org/references/authors/martin_svensson.html), Martin, [Taylor](https://www.interaction-design.org/references/authors/alex_s__taylor.html), Alex S. and [Combetto](https://www.interaction-design.org/references/authors/marco_combetto.html), Marco (2009): *Experiencing the Affective Diary*. In [Personal and Ubiquitous Computing](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing.html), 13 (5) pp. 365-378
[Sundström](https://www.interaction-design.org/references/authors/petra_sundstr%F6m.html), Petra, [Ståhl](https://www.interaction-design.org/references/authors/anna_st%E5hl.html), Anna and [Höök](https://www.interaction-design.org/references/authors/kristina_h%F6%F6k.html), Kristina (2007): *In situ informants exploring an emotional mobile messaging system in their everyday practice*. In [International Journal of Human-Computer Studies](https://www.interaction-design.org/references/periodicals/international_journal_of_human-computer_studies.html), 65 (4) pp. 388-403

[Sundström](https://www.interaction-design.org/references/authors/petra_sundstr%F6m.html), Petra, [Jaensson](https://www.interaction-design.org/references/authors/tove_jaensson.html), Tove, [Höök](https://www.interaction-design.org/references/authors/kristina_h%F6%F6k.html), Kristina and [Pommeranz](https://www.interaction-design.org/references/authors/alina_pommeranz.html), Alina (2009): Probing the potential of non-verbal group communication. In: [GROUP09 - International Conference on Supporting Group Work](https://www.interaction-design.org/references/conferences/group09_-_international_conference_on_supporting_group_work.html) 2009. pp. 351-360
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

加入 **314,538 位设计师** 的行列，通过我们的时事通讯（Newsletter）获取实用的 UX 技巧。
需要提供有效的电子邮件地址。

# 12.4 Rosalind W. Picard 的评论

对我而言，尝试理解这一章节是一个有趣的过程，其中有大量值得讨论的内容（宛如一场盛宴），尽管我只有时间讨论其中的一项“主菜”。

首先，我想表示我对 Kia Höök 及其引用的其他学者的工作表示由衷的赞赏，他们开发的技术旨在增强人们的情感意识（awareness of affect），并帮助人们更好地反思和理解自身及他人的情绪。我同样深切赞赏设计师们在处理整体情境（holistic situations）以及为人类进行设计方面所做的工作，这种设计涵盖了人们的感受，但绝不仅仅是*仅*关注感受。这些目标——创建能够增强情感理解（affective understanding）并响应人类需求多样性的交互与设计——对于提升人类生存的许多意义具有真正的重大影响。尽管如此，我想纠正一个重要的误区。让我先讲一个故事。

那是 1999 年，Joe LeDoux、Antonio Damasio 和我受邀在 Barcelona Museum 就“情感与知识（Emotion & Knowledge）”发表演讲。演讲被同步翻译成多种语言，这让我能够用英语缓慢且谨慎地发言，而将翻译成加泰罗尼亚语、西班牙语、法语等语言的艰巨工作交给比我更有才华的人。总的来说，这是一次极佳的体验——结识了迷人的人们，并深入探讨了新颖且具有启发性的课题。但是，其中有一件负面的事情在我的记忆中尤为突出...

在招待会上，一名肤色较深、身材精干的中年男子面色涨红，眉头紧锁，手势激烈地向我大步走来，他激动得几乎无法说话。我在博物馆里从未见过如此愤怒的人。我环顾四周，以为他是在针对附近某个试图抢走他妻子的家伙，毕竟我当时只是在品尝小点心。

但他的愤怒是针对我的。我咽了口唾沫，仔细倾听，逐渐意识到在他听到的翻译版本中，他认为我声称了类似“我们已经或现在可以将人类情感植入计算机”这样的话。事实上，我极其小心地*没有*那样说，但在他的认知中，我是在否认人类情感所伴随的特殊感受和体验，并将我们丰富的情感体验完全简化为像文本编辑器或游戏应用之类的东西。听他说话时，我意识到我为了精准描述我们*正在*做的事情以及我认为*可以*实现的事情而精心选择的英文措辞，在从我的工程文化（engineering culture）翻译到他的社会心理学（social psychology）文化时，出现了偏差。

在那次招待会上，我痛苦地意识到，我对“建模（modeling）”的定义与他听到这个词时的理解截然不同。我意识到，仅仅在陈述工作内容时谨慎措辞是不够的。我还需要预判来自不同领域的人可能会如何误解我的话。我需要学会如何

此外，我对我不希望表达的意思做进一步的澄清。我本应该不仅说“这些是我们能够实现的与情感相关的机制”，还应该说“这些并非情感的全部”。我本应该不仅说“我所说的‘机制’是指‘表征（Representing）的尝试’”，还应该说“表征并不等同于再现（Reproducing）”。我当时没有意识到，否则他会被引导至错误的结论。

我为什么要提到这个故事？Höök 的文章将情感计算（Affective Computing）的方法称为认知主义的（Cognitivistic）和还原主义的（Reductionist），这与 1999 年在巴塞罗那发生的误解非常相似。

当我谈到或写到情感的机制或情感的模型时，我是以一名工程师的身份，尝试利用现有工具尽可能地表征一个复杂的现象：我并没有将这些表征与情感本身混为一谈。我不是一个还原主义者，情感计算也不是还原主义的。我不认为情感可以被还原为这些表征，情感计算也没有这样主张。我不认为情感“仅仅是”我们识别并构建的那些机制。我们实现的机制并不等同于人类丰富的情感体验，我也从未说过它们会等同：我们没有证据支持此类主张。如果人们想要相信情感可以完全还原为逻辑计算和比特（Bits），那么这种信念是基于信仰，而非科学。

虽然人们可以用*信息和比特（bits）来描述任何概念*，包括情感，但我没有看到证据支持将情感完全还原为比特和信息的观点。当我撰写 *Affective Computing* 时，我知道许多读者将来自 AI 领域，并希望了解情感如何在机器中实现，因此我描述了该过程中我能够预见的那些部分。我在措辞上也非常小心，以免暗示这种方法就足够了。然而，那时我还没有遇到那位在巴塞罗那的男子，因此读者需要仔细阅读我的文字。

不幸的是，如果一个人的观点是多维度的，人们往往会试图将其简化为一维，并方便地将其挂在某个特定的“钩子”上。这个过程很像在整理门厅，将每件夹克挂在任何刚好可用且足够结实的钩子上。认知主义（Cognitivism）就是一个方便的钩子，它推动了这样一种信念：思维可以完全还原为规则和算法。

认知主义对像我的朋友兼同事 Marvin Minsky 这样的 AI 先驱产生了深远影响，他一直告诉我“情感仅仅是一种特殊的思维”，我经常就这句话与他产生分歧，有一次我甚至让他至少在删除“仅仅（just）”这个词上达成妥协。Marvin 认为身体是无关紧要的，除非是在婴儿期，那时人们需要被触摸，否则（研究表明）他们会萎缩并

……去世了。我遇到过其他持有类似想法的 AI 先驱，但我并不属于他们的阵营。我在 *Affective Computing* 中的著作讨论了身体以及意识体验的某些方面，而我们目前还完全不知道如何用信息和比特（information and bits）来实现这些方面。虽然在情感计算（Affective Computing）领域有一些研究者持有认知主义（cognitivist）观点，但情感计算本身并不是认知主义的。

没错，情感计算确实包含一些模型和研究者，其工作可能契合认知主义的“挂钩（hook）”，例如像 OCC 那样的认知基于规则的模型（cognitive rule-based models），对于那些相信该方法能完全解释情感的人来说，它可以挂在认知主义的挂钩上（但我并不这么认为）。语音或面部表情动态中情感的随机信号表示模型（stochastic signal-representing models）可能会挂在另一个不同的挂钩上，而且还存在其他挂钩。这个“衣橱”可以组织得比我目前写出来的更井然有序，尤其是随着新“衣物”不断增加。但请不要将挂钩与房子混为一谈。

相关的支持性示例请参阅 *Affective Computing* (1997) 中的“第一章：情感是生理的也是认知的（Chapter 1: Emotions are Physical and Cognitive）”，其中包含了我最早关于情感研究需要结合身心视角（body-mind view）的论述。这显然不契合认知主义的挂钩。同样，读者可能会对我强调的机器与人持续共同创造交互（co-creating interactions）感兴趣，这种交互不仅考虑情感，还考虑语境（context）及更多因素，这与其他的……

Kia Höök 的文章试图界定的领域（更多示例见“第八章：情感可穿戴设备（Affective Wearables）”，请参阅如“走出实验室，进入现实世界（Out of the lab and into the world）”等章节）。一项情感技术（affective technology）并不一定需要使用正式的情感 AI 模型，或者使用离散情感识别（discrete emotion recognition）或模式分类器（pattern classifier）才被归类为情感计算（affective computing）领域。

关于分类的讨论就到此为止。我认为，将一个“饼图”切分并命名——无论它是“情感计算之饼”还是其他种类的饼——并不像另一个问题那样有趣。我发现，在一些设计师试图将自己与更客观的工程方法（objective engineering approach）区分开来的驱动力背后，潜藏着这样一个问题：情感是完全可以被描述的，还是不可言说（ineffable）的？

在我们的工作中，我们通过多种方式在计算（computationally）和语义（semantically）层面描述了情感——包括离散的（discrete）、维度的（dimensioned）、数值的（numeric）、语义的（semantic），以及通过量化创造性行为、面部表情、生理信号测量等方式。我认为，无论在任何情况下，我们都未能通过模型、方法或描述“完全捕捉”到人类的情感。总有一些东西是无法被描述的。

情感计算通常（但并非总是）试图以客观的方式，对情感进行比主观描述更深入的刻画。我的许多工作一直致力于在工程意义上，将此前仅能通过文字、自我报告（self-report）和问卷调查来处理的事物，转化为具体且精确的度量，无论这些工作应用于

……内部感受或外部观察到的行为。我一直对所有主观测量方法本身都会受到情绪影响这一点感到困扰，因此我希望寻找更客观的方法。然而，客观测量并不比主观测量更容易暗示还原论（Reductionism）。两种方法都将情绪“还原”为某种东西——文字、数字、图片或“模糊的对象（blobby objects）”。使用表征（Representation）并不意味着持有还原论观点。还原论是指人们进一步跨越，声称我们的情绪“不过就是”计算机所表征的内容。后者这种跨越是我从未主张过的（除非是通过被误译的言论）。

当我结束与那位在 Barcelona 的男子的交谈时，我们意识到彼此都对深入理解情绪有着浓厚的兴趣，并且意识到我们感知到的分歧实际上根本不是分歧。建模（Model）的尝试并不意味着持有还原论观点。基于规则和类别来构建模仿情绪某些功能的表征，并不意味着认知主义（Cognitivism）。以比特（bits）形式实现情感测量，并不意味着情绪仅仅是信息。情感计算（Affective Computing）创造的工具是为了实现更高的目标——为了更深刻地理解是什么让我们成为了人类。在他离开之前，我和那位男子热情地握手并相视而笑。

在如何沟通我们试图在情绪领域做的事情方面，我仍有许多需要学习的地方——这是一个宏大的课题，而且它不仅仅是……

工程方法可以征服。作为一名工程师，我很高兴能与来自社会心理学、设计、神经科学、人工智能（AI）以及许多其他艺术和科学领域的人们共同开启这段旅程。如果我们不划分阵营，我们将能共同探索出更多的成果。

我最初给出的情感计算（Affective Computing）定义比 Kia 转述的要更广泛：*计算*（包括机器、机器人、手机、传感器、智能服装，以及任何能够进行计算的事物）与情感或其他情感现象（affective phenomena）相关、源于此或刻意影响这些现象。这从来不仅仅关乎 AI 或人机交互（Human-Computer Interaction, HCI），也不仅仅关乎制造智能机器，尽管在当时，这些是我试图说服其研究情感的最大群体。

或许允许我用我在 1997 年写的开篇语来结束，这段话在今天看来依然适用：

**“**
在这项工作的过程中，我更加深刻地体会到人类自身对情感发展的需求。我希望这一研究方向能够鼓励并促成我们在这一方面的发展——通过在人机交互中不再忽视人类情感，通过帮助我们更清晰地意识到我们是如何沟通的，通过为学习及其他功能中的情感理论提供测试平台（testbeds），通过让儿童与之互动的情感角色动画和趣味场景，通过协助科学家收集情感模式（affective patterns），通过帮助推进关于理解...的研究”

……情绪在预防医学（Preventive Medicine）中的作用，以及更多领域。我希望情感计算机（Affective Computers）作为辅助我们的工具，不仅是更智能的机器，更能成为我们探索人类本质、进而提升自身人性（Humanity）过程中的伴侣。
(Preface to *Affective Computing*, 1997)
**”**

# 12.5 Paul Hekkert 的评论

情感计算（Affective Computing）是一个令人兴奋的学科，Kristina Höök 为我们提供了一些该领域能够带来的优秀示例。如果智能机器能够以某种方式“感知”我们在与其交互时的感受，并据此调整其行为，那该有多好？这实际上正是情感计算的先驱们所认为的挑战，也是他们一直追求的目标：

1. 是否可以通过人们的行为、生理反应或面部表情来识别其情感反应/状态（emotional responses/states），并且
2. 我们能否让系统（例如计算机、产品、移动设备）在做出适当响应时将这些信息考虑在内？如果我错了，Rosalind Picard 请纠正我，我认为这些曾是且依然是情感计算（AC）学科的主要挑战。

这是否具有还原论（Reductionist）色彩？当然如此，你只能测量人们情感反应中的少数几个指标，而每一个指标（例如施加的压力、皮肤电导 [skin conductance]、心率变异性 [heart rate variability]、面部肌肉）都只能揭示故事的一小部分。情感包含许多行为、生理和心理层面的维度，而我们根本无法全部捕捉。但除此之外还有什么替代方案？我们希望测量尽可能地是非侵入式的（non-invasive）。如果我们因为测量方式而最终影响了人们的行为，甚至改变了他们的情感状态，那么整个目的就失去了意义。理想情况下，我们在用户不被...的情况下测量其情感反应。

意识到这一点。问题在于，每一个情绪指标实际上告诉了我们什么（即其效度 Validity），以及我们如何准确且非侵入式地（unobtrusively）对其进行测量。情感计算（Affective Computing, AC）领域的大量工作都致力于解决这些问题。

作为一种替代方案，Kristina Höök 提出了“交互方法（Interactional Approach）”，在这种方法中，系统允许用户反思其情感体验。然而，这并没有消除测量问题，例如在“情感日记（Affective Diary）”中就可以看到。该应用程序将动作和唤醒度（arousal）记录为人们情感状态的指标，并将这些数据转化为形状和颜色作为一种反馈形式。如果你旨在向用户提供关于其感受的反馈，那么这就是你决定的“适当响应（appropriate response）”，而你已经进入了 AC 的第二个挑战：如何响应？

当然，你所追求的响应在很大程度上取决于系统的类型和功能。当我像现在这样在 Word 中输入文档时，我不希望系统对我情感状态提供持续的反馈，也不希望看到这些状态反映在我输入的文字中。但我可能希望系统能识别出我正处于匆忙、不耐烦或压力巨大的状态，并微妙地“让我”慢下来，而我对此并不察觉。Miguel Bruns Alonso 最近在设计一款笔时探索了这一想法，该笔能够感知与不安（restlessness）相关的隐式行为（implicit behaviors），并通过提供内在反馈（inherent feedback）来降低压力水平 (Bruns Alonso et al., 2011)。

那么，是否存在解决测量问题（Measurement Problem）的替代方案？在 Kristina Höök 章节中的另一个例子中，她描述了 eMoto，这是一种扩展的短信服务，允许人们通过彩色且动态的形状来传达自己的感受。这种类型的“测量”——即让用户用文字或图像表达自己的情绪——仅在处理通信设备时才有效，且由于多种原因而存在问题。首先，它具有侵入性（Obtrusive），如果传达情绪并非设计目标，那么这种方法并不太被推荐。此外，人们对自己情绪的语言或非语言报告中存在效度问题（Validity Problems）。各种社会规则、需求特征（Demand Characteristics，指设备的特性？）以及反应风格（Response Styles）都可能会干扰对个人感受的有效报告（关于情绪测量方法的综述，请参阅 Mauss and Robinson, 2009）。

没错，我完全同意 Kristina 的观点，即身体在情感计算（Affective Computing, AC）领域的作用相对未被充分探索，且在识别与响应挑战（Recognition and Response Challenge）方面都具有巨大的潜力。鉴于认知科学（Cognitive Science）的最新进展（例如 Johnson, 2007），身体经验（Bodily Experiences）被日益认为是我们思考和感受的根源，我们可以期待出现更多像 Bruns Alonso 那样将身体作为主要中介（Mediator）的研究。否则，我们还能如何“把握”情感领域（Affective Domain）？

### References

- Bruns Alonso, M., Hummels, C.C.M., Keyson, D.V., & Hekkert, P.
(Conditionally accepted). Measuring and adapting behavior during product interaction to influence affect. *Personal and Ubiquitous Computing*.
- Johnson, M. (2007). *The meaning of the body: Aesthetics of human understanding*. Chicago: The University of Chicago Press.
- Mauss, I.B. & Robinson, M.D. (2009). Measures of emotion: A review. *Cognition and Emotion*, *23*, 209-237.

# 12.6 Commentary by Egon L. van den Broek

## 关于情绪的身体表达（Bodily expressions of emotion），请注意：已有超过一个世纪的研究！

在思考这篇评论时，各种想法涌现，情感也随之而生。应该评论什么？Kia Höök 撰写了一个非常出色的章节。她提到了从三个角度来探讨技术中的情绪（参见 Van den Broek, 2011），即：情感计算（Affective computing）、情感交互（Affective interaction）以及作为体验的技术（Technology as experience）。在本评论中，我将把焦点仅缩小在情感计算上。此外，我也选择后退一步，大胆地采取一个带有历史色彩的方法论视角（Methodological perspective）。为什么？因为多年来，我发现了越来越多触及情感计算核心但似乎不为人知的文献（例如 Arnold, 1968; Candland, 1962; Dunbar, 1954）。本评论基于两本书，它们出版于“情感计算”这一术语被创造之前的很久，即上世纪 50 和 60 年代。这两本书分别来自完全不同的科学分支。对科学史的了解可以防止我们——无论是从业者还是科学家——重复同样的错误。因此，本评论触及了科学本身的本质。

Kia Höök 对技术中的情绪提供了一个简洁的概述。她倾向于采用情感交互而非情感计算。与之相反，在本评论中，我采取了情感计算的立场。此外，Kia Höök 采取了设计视角（Design perspective），在这种视角下

本篇述评探讨并质疑了技术中情感（emotions）的基础。一些经验曾被吸取，但如今已被遗忘 (Arnold, 1968; Candland, 1962; Dunbar, 1954)。因此，情感计算（Affective Computing）在某种程度上倾向于“重新发明轮子（reinvent the wheel）”。是的，这是一个大胆的断言，非常大胆，但我希望读者在阅读本述评后，能与我产生共鸣。

1954年，在去世前5年，Flanders Dunbar 出版了 “Emotions and bodily changes: A survey of literature on psychosomatic interrelationships 1910-1953” 的第四版。通过这部令人印象深刻的著作，她对上世纪前五十（约）年关于情感与身体变化（bodily changes）的科学文献进行了详尽且结构化的综述。该书的书名恰到好处，很好地反映了其内容。这使得本书对于情感计算社区而言无疑具有极高价值。然而，据我所知，除了我自己的工作（例如 Van den Broek, 2011）之外，在任何情感计算的文章、报告或书籍中，都没有出现过对该书的引用。我只能希望是我遗漏了相当一部分……

Flanders Dunbar 在她的书 (1954) 开篇写道：

**“**在公元前近五百年，Socrates 从军队服役归来，向他的希腊同胞报告说，在某一方面，野蛮的 Thracians 领先于希腊文明：他们知道身体无法被

离开心灵无法治愈。他继续说道：“这就是为什么希腊（Hellas）的医生们不知道许多疾病的疗法，因为他们对整体缺乏认知。”正是医学之父 Hippocrates 所言：“为了治愈人体，必须具备对万物整体的知识。”而 Paracelsus 写道：“真正的医学仅源于对整个宇宙最深层且最终力量的创造性认知；只有掌握了人类最内在本质的人，才能真正地治愈他。”对今天的我们来说，这似乎是一个相当不可能实现的要求（第 3 页）。**”**

如果说 Dunbar 的研究表明情感计算（Affective Computing）的起源可以追溯到一个多世纪前，那么这段引用则表明，关于身心交互（interaction between body and mind）的知识在 25 个多世纪前就已被人们所知！现在，让我们识别 Dunbar (1954) 引用中提到的一些核心概念，这些概念对于情感计算至关重要。

古希腊人已经注意到“*离开心灵，身体无法被治愈*”（参见 Kia Höök 的章节）。因此，两者无疑是相关的，并且从原则上讲，情绪的测量应该是可行的。这在“*希腊的医生们不知道许多疾病的疗法*”这一评论中得到了很好的体现，因为希腊文化致力于研究身体而非心灵。最近的研究证实了这种关系。例如，当慢性压力（Chronic Stress）……

当经历相关情况时，会产生与最初引发压力的压力事件期间相似的生理反应。如果这类生理反应持续存在，可能会导致人体生理系统出现广泛且结构性的化学失衡，包括自主神经系统（Autonomic nervous system）和中枢神经系统（Central nervous system）、神经内分泌系统（Neuroendocrine system）、免疫系统（Immune system），甚至是大脑 (Brosschot, 2010)。这使我们意识到需要一种“*对整体事物的认知*”，即一种整体观（Holistic view），这可能与 Kia Höök 所定义的“技术即体验（Technology as Experience）”密切相关。尽管前文对人体生理系统的列举可能会让人觉得我们已经接近一个整体模型，但应当注意的是，这与目前的科学水平形成了鲜明对比。例如，对于（慢性）压力（Chronic stress），目前仍然缺乏深入的理解。这可以用人体生理系统的复杂性、所有系统之间的持续交互及其整体动态特性（Integral dynamic nature）来解释。然而，Brosschot (2010) 将情绪视为可以被孤立地仅归因于身体过程。我非常赞同 Kia Höök 的观点，即应当将身体之外的动态因素（Dynamics beyond the body）也纳入考量。此外，正如 Kia Höök 所指出的，在涉及计算实体（Computing entities）时，交互包含的内容远不止情绪；而即使在完全不涉及计算的情况下，情况也是如此。

25 个世纪前，科学家们还没有应用现代统计学；然而，在 1 个世纪前，科学家们已经开始应用统计学了；例如，Fisher 在 1918 年发明了方差分析（ANOVA）类统计模型。这为测试和推广关于情绪和身体变化的发现提供了手段，并促进了行为科学（behavioral sciences）的整体发展 (Dunbar, 1954)。此外，这项工作符合 Rosalind W. Picard 对情感计算（affective computing）的定义：“*……一套关于我所称之为‘情感计算’的观点，即与情感相关、源于情感或影响情感的计算。*” (Picard, 1995, p. 1) 至少在将计算视为传统解释（即通过数学手段进行确定）时，它是符合的。然而，情感计算的附加值在于其工程组件，特别是信号处理（signal processing）和模式识别（pattern recognition） (Van den Broek, 2011)。这将使机器能够感知情感、对其进行推理，甚至可能产生情感。这将标志着计算新时代的到来。

随着二战后不久计算设备的发明，一种新型统计学应运而生：模式识别（pattern recognition）。在他编辑的著作 “Methodologies of Pattern Recognition” (1969) 中，Satosi Watanabe 收集了一系列在 1968 年国际模式识别方法会议（International Conference on Methodologies of Pattern Recognition）上发表或拟发表的论文。Watanabe 在书的开头定义了模式识别：

**“**

在外行看来，“模式识别（Pattern Recognition）”这个词听起来像是一个非常狭窄且晦涩的电子计算机应用领域。但实际上，它是一项宏大且明确的尝试，旨在将人类最基本的感知（Perception）和概念形成（Concept Formation）功能机械化（Mechanization）（第 vii 页）。
**”**
Watanabe 将计算机模式识别定义为“ (i) 感知和 (ii) 概念形成这两项最基本人类功能的机械化”。

迄今为止，人类的模式识别在总体上在很大程度上尚未解决。我们并不了解作为人类的我们是如何处理情感信号（Affective Signals）的 (Van den Broek, 2011)。此外，对信号以及随后的模式的感知是一回事，而从情感角度对其进行解释则是完全不同的另一回事。这个问题涉及内容效度（Content Validity）；即：(i) 情感领域专家之间的一致性；(ii) 一个（低层级的）感知物（Percept）在多大程度上能够充分代表一种情感；以及 (iii) 一组感知物在多大程度上能够充分代表所研究情感的所有方面。

概念形成的问题与构念验证（Construct Validation）的过程相关，其目的是围绕所研究的情感建立一个地面真值（Ground Truth）（或本体 Ontology 或语义网络 Semantic Network）。这样一个框架需要对所有构念及其相互关系给出具有理论基础的、可观察的、操作性定义（Operational Definitions）。这样的

该网络旨在提供一个可验证的理论框架。缺乏这样一个网络是情感计算（Affective Computing）目前面临的最重大问题之一。Kia Höök 将情绪描述为仿佛我们可以精确地定位它们。尽管直觉上确实如此，但在实践中，定义情绪被证明是非常困难的 (Duffy, 1941; Kleinginna & Kleinginna, 1981)。

人类在嘈杂的环境中识别模式（Patterns）的能力极其出色。此外，人类适应新情境和新模式的便捷程度依然令人惊叹。而且，这与信号处理（Signal Processing）和模式识别（Pattern Recognition）算法的性能形成了鲜明对比。通常，这些算法在受控环境中表现良好；然而，在“真实世界”中，其性能会下降 (Healey, 2008)。这个问题涉及情境（Context）对测量结果的影响，这也被称为生态效度（Ecological Validity）。由于缺乏真实世界的研究，通常而言，情感计算研究的生态效度有限，其应用往往仍需在“真实世界”的实践中得到验证。然而，正如 Kia Höök 所阐述的，在过去十年中，已经出现了一些该论断的绝佳特例。

1941年，Elizabeth Duffy 发表了她的文章 “An explanation of ‘emotional’ phenomena without the use of the concept ‘emotion’”，她在文中开篇便指出，她认为 *“… ‘emotion’（情绪），作为一个科学概念，不仅毫无用处，甚至是有害的。……‘Emotion’ 显然……”*

“不代表一个独立且可区分的状态。”尽管这一论述已有 60 年历史，但它依然（或再次）具有时效性，甚至比以往任何时候都更具意义（参见 Kleinginna & Kleinginna, 1981）。约五十年后，在 1990 年，John T. Cacioppo 和 Louis G. Tassinary 表达了类似的担忧；然而，他们更广泛地探讨了心理生理关系（Psychophysiological relations）的复杂性。这些关系“根据其特异性（Specificity，例如：一对一与多对一）及其普遍性（Generality，例如：特定情境或特定个体与跨情境及跨文化）而被概念化”（Cacioppo & Tassinary, 1990）。他们提出了一个模型，该模型“**产生了四类心理生理关系：(a) 结果（Outcomes），(b) 伴随物（Concomitants），(c) 标记物（Markers），以及 (d) 不变量（Invariants）**”。

尽管 Cacioppo 和 Tassinary (1990) 讨论了语境（Context）的影响，但他们并未将其操作化（Operationalize）；因此，这一讨论对情感计算（Affective computing）的价值有限。尽管如此，此类文章仍能提供启发。遗憾的是，在情感计算领域，此类尝试十分罕见；因此，该领域的研究方法较为脆弱，且缺乏一个坚实的理论框架（Van den Broek, 2011）。

为了确保足够的进展，有学者建议开发能够根据用户的生理反应（Physiological response）做出响应的计算实体（Computing entities），而无需将其解释为情感或认知过程（Tractinsky, 2004）。这种方法已经...

已被证明在多个应用领域具有可行性。然而，这种方法也削弱了情感计算（Affective Computing）本身作为一个研究领域的地位。它表明，在情感计算能够投入实践之前，情感研究（Emotion Research）需要进一步成熟。对于情感计算领域而言，这虽然是一个诚实的结论，但过于简单粗暴。这意味着情感计算在实现飞跃之前，应当先退后几步。这一过程的一个良好起点，是 Gross (2010, p. 215) 在其文章 “The future's so bright, I gotta wear shades” 中总结的情感研究热点话题（另见 Van den Broek, 2011）。

综上所述，应当肯定 Kia Höök 对技术中情感问题的简洁概述。在她的章节中，她采取了情感交互（Affective Interaction）的立场。与之相对，在本篇评论中，我采取了情感计算的立场。此外，Kia Höök 采用了设计视角（Design Perspective），而本评论则触及了技术中情感的基础。我认为，如果说情感计算需要做些什么，那就是它必须更多地了解其根源（例如 Arnold, 1968; Candland, 1962; Dunbar, 1954）；届时，情感计算才能够、且很可能会拥有光明的未来！

## References

- Arnold, M.B. (1968). *The nature of emotion: Selected readings*. Harmondsworth, Middlesex, England: Penguin Books Ltd.
- Brosschot, J.F. (2010). Markers of chronic stress: Prolonged
physiological activation and (un)conscious perseverative cognition. *Neuroscience & Biobehavioral Reviews, 35(1)*, 46-50.
- Cacioppo, J.T. and L. Tassinary, L.G. (1990). Inferring psychological significance from physiological signals. *American Psychologist, 45(1)*, 16-28.
- Candland, D.K. (1962). *Emotion: Bodily change - An enduring problem in psychology, Selected readings*. Princeton, NJ, USA: D. van Nostrand Company, Inc.
- Duffy, E. (1941). An explanation of "emotional" phenomena without the use of the concept “emotion”. *Journal of General Psychology, 25*, 283-293.
- Dunbar, F. (1954). *Emotions and bodily changes: A survey of literature on psychosomatic interrelationships 1910—1953* (4th ed.). New York, NY, USA: Columbia University Press.
- Fisher, R.A. (1918). The correlation between relatives on the supposition of Mendelian inheritance. *Transactions of the Royal Society of Edinburgh, 52(2)*, 399-433.
- Gross, J.J. (2010). The future's so bright, I gotta wear shades. *Emotion Review, 2(3)*, 212-216.
- Healey, J.A. (2008). Sensing affective experience. In J.H.D.M.
Westerink, M. Ouwerkerk, T. Overbeek, W.F. Pasveer, and B. de Ruyter

(Eds.), *Probing Experience: From Academic Research to Commercial Propositions* (Part II: Probing in order to feed back), Chapter 8, p. 91-100. Series: Philips Research Book Series, Vol. 8. Dordrecht, The Netherlands:
Springer Science + Business Media B.V.
- Kleinginna, P.R. and Kleinginna, A.M. (1981). A categorized list of emotion definitions, with a suggestion for a consensual definition. *Motivation and Emotion, 5(4)*, 345-379.
- Picard, R.W. (1995). *Affective Computing*. Technical Report No. 321. Perceptual Computing Section, M.I.T. Media Laboratory, Cambridge, MA, USA.
- Tractinsky, N. (2004). Tools over solutions? Comments on Interacting with Computers special issue on affective computing. *Interacting with Computers, 16(4)*, 751-757.
- Van den Broek, E.L. (2011). *Affective Signal Processing (ASP): Unraveling the mystery of emotions*. PhD-thesis, Human Media Interaction (HMI), Faculty of Electrical
Engineering, Mathematics, and Computer Science, University of Twente,
Enschede, The Netherlands.
- Watanabe, S. (1969). *Methodologies of Pattern Recognition*. New York, NY, USA: Academic Press, Inc.

# 12.7 Joyce H. D. M. Westerink 的评论

Kristina Höök 为我们提供了一个启发性的视角，探讨了针对技术与情感（affect）交叉点的三个研究方向，即（传统的）情感计算（Affective Computing）、情感交互（Affective Interaction）以及技术即体验（Technology as Experience）。她强调，由于这些研究方向在方法论上具有互补性，因此每条研究路线都为针对不同类型用户的应用开发做出了贡献。基于我在工业研究（industrial research）中的经验，我非常认同这一结论。我想特别挑选出几个方面进行进一步讨论。

首先，我想谈谈一个存在于本文以及许多其他关于情感计算的文本和观点中，但从未被明确阐述的假设，即：对于该领域任何可行的应用而言，*你需要对与情感相关的信号（emotion-relevant signal）进行测量*。这可以是像 Affector 中的摄像头信号，像 eMoto 中的运动信号，或者是像 Affective Diary 中的生理信号（physiological signals）。此外，我们自己的许多努力也投入到了追求针对情感相关信号的非侵入式测量技术（unobtrusive measurement techniques）中，例如我们的皮肤电导腕带（skin conductance wristband）（Ouwerkerk, 2011）。然而，为了实现“制造一台能够刻意……影响情感或其他情感现象（affective phenomena）的机器”这一目标，测量并非严格必要。一个典型的例子是任何电视机或 MP3 播放器：我们一直使用它们通过音乐来改变心情，或者通过观看电视节目来体验一系列的

……情绪。其之所以奏效，是因为人们在反应上在一定程度上具有相似性，且电视节目导演和音乐作曲家非常擅长为大众或特定目标群体营造情感体验。然而，在我们的研究领域中，人们普遍默认测量情绪相关信号（emotion-related signals）是必要的，且这种测量确实能够进一步精细化情感影响（affective influencing），特别是对于那些偏离群体平均值、趋向于个体适配（adaptation to individuals）的变化。这意味着，正如 Kia Höök 所提出的，*个体模型（individual models）*最终不仅在情感交互方法（Affective Interactional approach）中不可或缺，在情感计算（Affective Computing）范式中同样如此。

一旦引入情绪相关测量，我们便立即进入了*闭环应用（closed-loop applications）*领域（参见 Van Gerven et al., 2009, Van den Broek, 2011）：情绪相关测量被解读为情感状态，随后根据当前及历史测量结果决定采取何种行动，在执行这些行动后，再次进行测量以监测新状态，以此类推（见图 1）。闭环模型（closed-loop model）的基本逻辑是，只要有可用的测量数据，就利用这些数据来尝试改善现状。通过这种方式，个体的（情感）状态可以被引导至预设的目标方向。我们的情感音乐播放器（Affective Music Player）（Janssen et al., 2011,

(Van der Zwaag et al., 2009) 遵循了情感计算（Affective Computing）的最佳传统，可以作为一个例子：它测量我对音乐的个人反应，并利用这些信息来调整播放列表，从而引导我（而非他人）达到某个选定的目标情绪（target mood）。总之，我认为在我们的领域中，任何研究路线中的情绪相关测量（emotion-related measurements）、个体模型（individual models）和闭环应用（closed-loop applications）都是紧密相连的。

![](https://www.interaction-design.org/images/encyclopedia/affective_computing/joyce_emotional_interpretation_measurement.jpg)
版权状态：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/affective-computing#copyrightNotice) 中的“例外”部分。
图 12.1：情绪闭环（Emotional Closed Loop）

图 1 中的情感闭环为*情绪相关信号的解释（interpretation of the emotion-related signal）*预留了很大一部分空间。正如 Kia Höök 在情感交互（Affective Interaction）范式的框架下所主张的，这种解释可以*由* *人类*来完成，而这个人类既可以是被测量者（例如：情感日记 Affective Diary），也可以是其他人（例如：Affector）。在这两种情况下，测量信息都将被用于反思被测量的情境，并在需要时采取行动对其进行改变（从而使其真正成为一个闭环）。如果呈现的是原始情绪相关信号，我们将

确实，这样可以确保不会丢失对用户有价值的信息。但另一方面，这些信息（至少在开始时）可能会过多地令用户不知所措，而用户可能会从由*算法*做出的解释（遵循情感计算 [Affective Computing] 传统）形式的帮助中获益。我们无需在两种方案之间做出选择，可以考虑将两者同时实现。例如，我们的电子腕带确实会显示一天或一周内的原始皮肤电导（skin conductance）/唤醒（arousal）模式，但每当算法解读出紧张程度显著上升时，我们也可以向用户发送一个隐蔽的震动（vibration alarm）。当然，Kia Höök 指出，由于在许多应用中*上下文（context）是变化的*，因此很难做出正确的解读；情感计算领域的大量研究致力于开发从情绪相关信号中推导情感状态（affective states）的算法，这一事实也印证了上述观点。尽管如此，仍有几种尝试克服这一问题的方法：一种技术手段是通过增加额外的传感器来监测上下文，例如我们腕带中的加速度计（accelerometer），它可以帮助我们估算佩戴者的活动水平，并据此解读皮肤电导信号。另一种方法是对不同情况下的多次测量值取平均，从而提取出整体效果。例如，这在我们的 Affective Music 中得到了应用。

在该播放器中，单首歌曲的情绪影响是通过计算多次播放的平均情感效应（affective effect，并根据初始值定律 Law of Initial Values 进行了修正）来建模的，且事实证明，这种方法足以筛选出能够将用户情绪引导至特定状态的歌曲。此外，我们的情感音乐播放器（Affective Music Player）既不会向用户展示原始的情绪相关信号（emotion-related signal），也不会展示其解释结果：用户并不希望被这些信息干扰，而仅仅是体验到自己被引导进入了一种不同的情绪状态。总之，我们发现，人类和算法对情绪相关信号的解释都是未来应用的重要组成部分，且两者在一定程度上都能处理上下文（context）信息。

Kia Höök 主张，在日常生活中，情绪总是*更广泛体验的一部分*，而我们需要通过情感技术（affective technology）来支持的正是这种更广泛的体验，这与“技术即体验（Technology-as-Experience）”的研究方向一致。这无疑将扩大应用领域，涵盖那些情绪发挥作用的相关领域。例如，情绪在沟通和建立关系中至关重要，可以预见情感技术能够在此提供帮助 (Janssen et al., 2010)。这涉及到图 1 中闭环（closed loop）的“决定行动（decide on actions）”部分：我们希望如何利用获取的信息？然而，可能目标的广泛性……

这并不排除也存在那些*旨在影响情感（Affect）本身*的应用。一个典型的例子是前文提到的情感音乐播放器（Affective Music Player），其目的正是为了引导情感，具体而言即是心境（Mood）。我们还证明了 (Van der Zwaag et al., 2011)，经过个体化选择的最佳音乐确实有助于*在 Kia Höök 所描述的令人沮丧的交通状况中，防止愤怒情绪（Emotion）或情感状态（Affective state）的产生*。

另一方面，我不确定消费者是否真的有兴趣了解或影响自己的情绪。尽管电视上充斥着大量情感过载的真人秀节目，且情绪作为研究课题在近年来已成为时尚，但公众仍然持有某种“对他人的情况很好，但对我而言并非如此”的态度。在我看来，这与 Kia Höök 提到的*“情感/女性”与“理性/男性”之区分*有关：普通男性仍然将情绪视为女性软弱的标志，他们不希望被提醒这一点，即便我们的测量技术为其赋予了更具“男性化”色彩的包装。对于女性而言，情况则恰恰相反：她们对心境和情绪感到（更加）自在，并承认这些因素对日常生活的影像，但她们不太倾向于利用这种“男性化”的技术来改变它们。正因如此，我也同意 Kia Höök 的观点，即我们的情感技术（Affective technologies）最有可能被应用于那些针对...

比单纯的情感（affect）体验更为广泛。

综上所述，我想强调 Kia Höök 的故事中所传达的最核心信息：情感技术（affective technologies）将受益于个体模型（individual models）（这不仅针对人类，也针对算法对所测得的情感相关信号的解释），且其应用范围可以极大地扩展，远远超出最初测量和影响情感的领域。我期待看到这些技术被整合到我们周围世界的各种产品和应用之中……

## References

- Janssen, Bailenson, IJsselsteijn, & Westerink (2010), Intimate heartbeats:
Opportunities for affective communication technology. IEEE Transactions
on Affective Computing, Vol. 1, No 2, 72-80.
- Janssen, Van den
Broek, Westerink, Tune in to your emotions: A robust personalized
affective music player, User Modeling and User-Adaptive Interaction, In
Press.
- Ouwerkerk (2011), Unobtrusive Emotions Sensing in Daily
Life, in: Sensing Emotions. The Impact of Context on Experience
Measurements (2011), Westerink, Krans, Ouwerkerk (eds.). Philips
Research Book Series, volume 12, Springer, Dordrecht, The Netherlands,
pages 21-39.
- Van den Broek (2011), Affective Signal Processing, Unraveling the mystery of emotions, Ph.D. Thesis University of Twente.
- Van der Zwaag, Westerink, Van den Broek (2009), Deploying music
characteristics for an affective music player, Proceedings VOLUME I,
2009 International Conference on Affective Computing & Intelligent
Interaction, ACII 2009, September 10-12, 2009, Amsterdam, The
Netherlands, pages 459-465.
- Van der Zwaag, Fairclough,
Spiridon, Westerink (2011). The impact of music on affect during anger
inducing drives. In S. Dmello et al. (Eds.), 4th international
conference on affective computing and intelligent interaction. Part I,
LNCS 6974 (pp. 407-416). Memphis, Tennessee, USA: Springer, Heidelberg.
- Van Gerven, Farquhar, Schaefer, Vlek, Geuze, Nijholt, Ramsey, Haselager,

Vuurpijl, Gielen and Desain (2009). The brain–computer interface cycle.
Journal of Neural Engineering, Vol.6, No.4, 1-10.

## 本章主题：

[用户体验（User Experience, UX）设计](https://www.interaction-design.org/literature/topics/ux-design)[
                        人机交互（Human-Computer Interaction, HCI）](https://www.interaction-design.org/literature/topics/human-computer-interaction)[
                        情感设计（Emotional Design）](https://www.interaction-design.org/literature/topics/emotional-design)[
                        设计史（Design History）](https://www.interaction-design.org/literature/topics/design-history)[
                        美学（Aesthetics）](https://www.interaction-design.org/literature/topics/aesthetics)[
                        情感驱动因素（Emotional Drivers）](https://www.interaction-design.org/literature/topics/emotional-drivers)[
                        情感计算（Affective Computing）](https://www.interaction-design.org/literature/topics/affective-computing)[
                        交互设计（Interaction Design）](https://www.interaction-design.org/literature/topics/interaction-design)
