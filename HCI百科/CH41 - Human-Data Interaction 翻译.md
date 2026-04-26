# 41. 人-数据交互 (Human-Data Interaction)

**来源**：*The Encyclopedia of Human-Computer Interaction*, 2nd Ed.
**Notion 原页面**：https://www.notion.so/c230f13c8f4a41078ee1afa2c6bd93b6

---

[Richard Mortier](https://www.interaction-design.org/literature/author/richard), [Hamed Haddadi](https://www.interaction-design.org/literature/author/hamed), [Tristan Henderson](https://www.interaction-design.org/literature/author/tristan), [Derek McAuley](https://www.interaction-design.org/literature/author/derek), [Jon Crowcroft](https://www.interaction-design.org/literature/author/jon) and [Andy Crabtree](https://www.interaction-design.org/literature/author/andy-crabtree)

## 41.1 引言（Introduction）

我们已经从一个计算被孤立且专业化（siloed and specialised）的世界，进入了一个计算无处不在且日常化的世界。在世界的许多（如果不是大多数）地区，网络计算作为前台（foreground，如智能手机、平板电脑）和后台（background，如道路交通管理、金融系统）技术，现已变得十分平常。这使得现有交互方式（如网上银行）能够获得全新的诠释，同时也催生了截然不同的新交互方式（如大规模可扩展的分布式实时移动游戏），且这种趋势仍在继续。网络计算在我们的环境和生活中的普及性日益增强，其结果是*数据*也变得无处不在：在许多地方，社会的大部分领域正迅速变得“数据驱动（data driven）”。

我们使用的许多设备、它们连接的网络——不仅是互联网，还包括固定电话和蜂窝电话网络等替代技术——以及我们与这些技术产生的交互（如使用信用卡、在公共高速公路上驾驶、在线购物），都产生了大量的数据足迹（trails of data）。这些数据既是由我们自觉地*创造*的——无论是通过在线社交网络（Online Social Network, OSN）个人资料主动提供，还是像在线购物行为那样被观察到（World Economic Forum 2011）——也是由他人*关于*我们而推断和创造的——这些“他人”不仅是指其他人类，而且越来越多地是指机器和算法。

![](https://public-media.interaction-design.org/images/uploads/5124b3a3d3f997e1d55ff9cea9168743.jpg)
作者/版权持有者：tara hunt。版权条款与许可：CC BY-SA 2.0

*我们在有意识和无意识的情况下都会产生数据足迹（Data trails）。我们大多数人对于在 Facebook 和 Twitter 账号上发布的内容非常谨慎，但只有少数人意识到，他们在许多其他方面也会留下非常详细的数据足迹，例如在进行在线浏览或携带智能手机在城市中行走时。机器和算法（Algorithms）正日益追踪我们的每一步——无论是在线还是线下——而我们极少收到关于这种监控（Surveillance）的“警告”或通知。*

### 41.1.1 人机交互的演进

我们观察到，人机交互（Human-Computer Interaction, [HCI](https://www.interaction-design.org/literature/topics/human-computer-interaction)）源于且传统上专注于人类与作为人工制品（artefacts）的计算机之间的交互，即那些被交互的设备。正如 Microsoft Research 的 HCI 领域首席研究员 Jonathan Grudin (1990a, 1990b) 所述，HCI 的研究重点经历了从心理学（psychology, Card, Moran, and Newell 1983）到硬件（hardware）、软件（software）、界面（interface），随后进一步深入到组织（organisation）层面的演变。这一趋势将关注点从“操作员使用单台硬件设备”的相对简单视角向外扩展；随着计算机系统渗透到组织内部并实现网络化，研究开始关注用户与计算机系统之间丰富的相互关系，从而产生了“打破界面（explode the interface）”的需求，例如 Newcastle 大学和 Nottingham 大学分别由 Bowers 和 Rodden (1993) 提出的观点。

**人机交互的演进：**
![](https://public-media.interaction-design.org/images/uploads/89b3b19b2f11c7d5947a57b2fd9626e7.jpg)
作者/版权持有者：Jorge Gonzalez。版权条款和许可：CC BY-SA 2.0

我们认为，向真正的普适计算（ubiquitous computing）和泛在计算（pervasive computing）持续且加速发展的趋势，表明有必要强调另一个

这是关于人们如何与计算机系统交互这一广泛话题的一个方面：*人们应该如何与数据交互*。也就是说，这并非是指我们需要直接与海量数据进行交互（这在目前仍然是一个相对少见的职业），而是指我们所有人都需要了解我们的行为、这些行为产生的数据，以及处理这些数据的算法是如何日益塑造我们的生活的。一个复杂的生态系统（通常是协作的，但有时也是对抗性的 (Brown 2014)）正围绕着从事数据利用的公司和个人而形成。新兴的、跨学科的人机数据交互（Human-Data Interaction, HDI）领域对此做出了响应，它将人置于这些数据流的中心，并致力于提供让人们能够与这些系统和数据进行显式交互（explicitly interact）的机制。

![](https://public-media.interaction-design.org/images/uploads/0ffb60cd4ec57b31155ef64e5735ffe6.jpg)
作者/版权持有者：Thierry Gregorius。版权条款与许可：CC BY 2.0

*我们认为，理解以下几点至关重要：1) 我们的行为，2) 我们的行为所产生的数据，以及 3) 处理这些数据的算法是如何日益塑造我们的生活的。人机数据交互（Human-Data Interaction, HDI）将人置于这些数据流的中心，并提供能够帮助个人和群体与这些系统及数据进行显式交互的机制。*

在这

在本文中，我们将首先详细阐述为什么人机数据交互（Human-Data Interaction, HDI）值得被定义为一个独立的问题域（problematic） (§2)，随后将定义 HDI 的具体含义 (§3)。接着，我们将讲述 HDI 发展至 2010 年代中期状态的过程，首先介绍 Dataware——一个旨在实现 HDI 的早期技术尝试 (§4)。随后，我们将深入探讨 HDI 中“I”的准确含义——即在 HDI 中如何理解（construed）和构建（constructed）交互（interaction）——以及基于这一理解，近期在定义支持 HDI 的技术平台方面所做的第二次尝试（分别见 §5 和 §6）。最后，我们将简要讨论 2010 年代下半叶我们所识别出的一些令人兴奋的研究领域 (§7)，尽管毫无疑问还存在更多其他领域！最后，在总结之后 (§8)，我们将提供一些进一步学习的指引 (§9)。

## 41.2 为什么我们需要 HDI（Human-Data Interaction，人机数据交互）？

### 41.2.1 生活在继续：我们依然需要隐私

![](https://public-media.interaction-design.org/images/uploads/dfef71df6a73f10f114b5d14248d999a.png)
作者/版权持有者：Sean MacEntee。版权条款与许可：CC BY 2.0
*隐私并非一个过时的模型。我们现在比以往任何时候都更需要它。*
> “有一点应当明确，尽管我们生活在一个比过去更自由地分享个人信息的世界上，但我们必须拒绝‘隐私是一种过时价值’这一结论……我们现在比以往任何时候都更需要它。”
  – Barack Obama, 美国总统 (US Consumer Privacy Bill of Rights 2012)

随着数字技术以前所未有的规模生成并交易个人数据（Personal data），隐私（Privacy）长期以来一直是广泛的社会关注和讨论的话题。政府和工业界宣称个人数据能带来社会和经济效益，而与之相对的则是源源不断的关于个人数据被误用和滥用的恐慌性报道。工业界试图通过提供加密（Encryption）技术作为解决公众担忧的万灵药来缓解焦虑，而这反过来又成为了国家安全负责人员关注的问题。这种对加密技术的利用掩盖、隐藏或至少模糊了一个对消费者或用户隐私的关键威胁：即设备“窃听”以及阻止设备过多地“泄露”关于我们的信息的能力。正如 Stanford University 计算机科学与法律教授 Keith Winstein (2015) 所言：

> “制造商

“他们将设备作为封闭产品（sealed-off products）出货，这些设备仅通过加密方式与制造商的服务器在互联网上通信。加密是防止恶意攻击者窃听的绝佳方式。但当它阻碍了设备的实际所有者通过监听来确保设备没有在‘告密’时，这种效果就变成了反消费者的。”
—— Keith Winstein

许多互联网企业依赖于收集的关于用户的广泛且丰富的数据，无论其目的是为了有效地进行精准广告投放（target advertising），还是将其作为产品出售给第三方。针对大量用户收集的丰富数据所产生的强大网络外部性（network externalities），使得真正的竞争性市场难以形成。我们可以从第三方网站收集关于我们的信息范围和触达能力的不断扩大中看到一个具体的例子，该领域由少数几家巨头主导，包括 Google, Yahoo, Rubicon Project, Facebook 和 Microsoft (Falahrastegar et al. 2014, 2016)。这种主导地位对更广泛的生态系统产生了不利影响：在线服务供应商发现自己受制于大型平台和应用程序接口（Application Programming Interface, API）提供商的意愿，从而阻碍了[创新](https://www.interaction-design.org/literature/topics/innovation)并扭曲了市场。

### 41.2.2 隐私悖论（The Paradox of Privacy）：揭露得越多，对隐私的渴望就越多

然而，个人数据管理（Personal Data Management）被认为是一件极其私人的事务：例如，信息学教授 Paul Dourish (2004) 指出，个人对个人数据和隐私的态度非常复杂，且依赖于具体情境（Context Dependent）。研究表明，人们在[社交媒体](https://www.interaction-design.org/literature/topics/social-media)上披露的信息越多，他们声称对隐私的渴望就越强烈，例如来自 Hamburg 大学和 Hohenheim 大学分别由 Taddicken 和 Jers (2011) 开展的研究。这一悖论意味着，参与者对于在网上公开如此多个人信息所获得的回报感到不满，但尽管如此，“他们仍然继续参与，因为他们害怕被排挤，或者被他人视为脱离网络且不参与社交的失败者（unplugged and unengaged losers）”。这一例子还揭示了许多“个人”数据固有的社交属性（Social Nature）：正如 Nottingham 大学计算机科学教授 Andy Crabtree 和 Cambridge University Computer Laboratory 的大学讲师 Richard Mortier (2015) 所指出的，仅仅为了保护隐私而退出所有在线活动是不切实际的。

情境[敏感性](https://www.interaction-design.org/literature/topics/empathy)（Context Sensitivity）、数据收集及其推断（Drawn Inferences）的不透明性、第三方与数据聚合商（Data Aggregators）之间的个人数据交易，以及近期的数据泄露和

隐私侵害（privacy infringements）促使人们寻求参与并控制其个人数据组合（personal data portfolios）的手段。然而，如果技术约束（technical constraints）忽略了广告商和分析服务提供商（analytics providers）的利益，从而导致支撑“免费”服务和应用程序的收益减少或消失，那么这些约束终将失败 (Vallina-Rodriguez et al. 2012; Leontiadis et al. 2012)。

### 41.2.3 物联网重塑了数据收集的本质：从主动到被动

物联网（Internet of Things, IoT）进一步增加了情况的复杂性，它将数据收集的本质从人机交互（Human-Computer Interaction）的一种主动特性，重塑为一种被动特性——在这种模式下，设备通过计算机网络无缝地相互传输个人数据。如果将加密（Encryption）视为解决隐私问题的万灵药（但事实并非如此：消费者数据依然面临着我们所有人都日益熟悉的行业滥用风险），那么这便催生了“围墙花园（Walled Gardens）”，个人数据在交付给最终用户之前，会先被分发至云端。诸如 Samsung 的 ARTIK 等开放式 IoT 平台也未能规避这一问题：它们仅对开发者开放。这并非一个仅限于 IoT 的问题，但 IoT 使其变得尤为凸显：虽然安全性显然是隐私问题（Privacy Equation）中的重要组成部分，但同样明显的是，仅靠安全性是不够的。

### 41.2.4 重塑人性：数字经济中的积极参与者而非被动受害者

特别需要将终端用户（End-user）置于个人数据（Personal data）的流动之中；使那些产生个人数据的人成为其分发和使用过程中的积极参与者，而非被动参与者。对支持个人数据管理的需求体现在广泛的法律、政策和行业倡议中，例如欧洲的 $\text{General Data Protection Directive}$ (European Parliament 2014)、美国的 $\text{Consumer Privacy Bill of Rights}$ (US Consumer Privacy Bill of Rights 2012) 以及日本关于个人数据使用政策的修订 (Strategic Headquarters for the Promotion of an Advanced Information and Telecommunications Network Society 2014)。

在此，信任（Trust）、问责制（Accountability）和用户赋能（User Empowerment）的问题至关重要。这些问题不仅涉及数据控制者（Data Controllers）——即负责处理个人数据并确保符合法规和法律的一方——的义务，而且旨在将代理与控制的中心（Locus of Agency and Control）向消费者转移，力求将用户从被动的“数据主体（Data Subject）”转变为个人数据处理过程中的积极参与者。也就是说，使其成为能够行使控制权并管理自身数据与隐私的人，从而成为新兴数据经济（Data Economy）中的积极参与者或玩家，而非被动的受害者。

Having

在探讨了为何 HDI（Human-Data Interaction，人机数据交互）是一个值得我们关注的话题之后，我们现在将详细讨论当我们使用 HDI 这一术语时，其具体含义究竟是指什么。

## 41.3 究竟什么是 HDI？

与大多数学术探索（academic ventures）一样，你可能会预料到回答上述问题并非易事。我们认为，数据（data）概念的丰富性体现在其通用定义中，进而导致了人机数据交互（Human-Data Interaction, HDI）的定义具有广泛性。例如，Oxford English Dictionary (2014) 对数据的定义如下：

- 作为可数名词：一项信息；一个数据项（datum）；一组数据。
- 作为不可数名词：
  - 统称为相关（主要是数值性的）信息项，通常通过科学研究获得，并用于参考、分析或计算。
  - 计算领域：由计算机执行操作的数量、字符或符号的集合。此外（在非技术语境下）：数字化形式的信息。

然而，当它与其他名词组合时，情况变得更有趣：

- **数据足迹（Data trail）**：**特定个人、组织等的交易或活动的电子记录**。现在尤其指一个人的财务交易、电话和互联网使用情况等。
- **数据烟雾（Data smog）**：**一种令人困惑的大量信息**（尤其是来自互联网的信息），其中错误、琐碎或无关的信息无法被轻易或高效地从真正有价值或有意义的信息中分离出来（通常用于比喻语境）；以及由此产生的模糊状态；参见 [信息过载（information overload）](https://www.interaction-design.org/literature/topics/information-overload)。

- **大数据（Big Data）**：计算（首字母亦可大写）**规模极大的数据**，通常其处理和管理会带来显著的管理与操作挑战（logistical challenges）；（同时）指涉及此类数据的计算分支。

在许多方面，我们认为正是最后三个定义之间的相互作用，产生了对更广泛的人机数据交互（Human-Data Interaction, HDI）概念的需求：即当个人私密行为的数据轨迹（data trails）被聚合并作为大数据进行分析时；以及这些分析结果（无论是否正确）被反馈到与个人相关的数据中时。数据，尤其是个人数据，可以被视为一种*边界对象（boundary object）* (Star and Griesemer 1989; Star 2010)，这体现在不同群体对数据的称呼和思考方式的多样性中。例如，为了与大数据形成对比，我们看到数据轨迹被地称为*小数据（small data）* (Estrin 2013)，在这种语境下 *“N = 我”*，指的是我们每个作为个体的个体。我们在其他领域还看到了其他术语：健康领域的*参与式数据（participatory data）* (Shilton 2012)、人口信息学（population informatics）中的*微观数据（microdata）* (Kum et al. 2014)，以及数字经济中的*数字足迹（digital footprint）* (Madden et al. 2007)。

查阅文献表明，该术语已被赋予多种含义；截至 2016 年，我们已知至少有五个不同的版本：

- HDI（人机数据交互，Human-Data Interaction）旨在联邦化（federating）异构的个人数据源，并实现对“我的数据”使用的[用户控制（user control）](https://www.interaction-design.org/literature/topics/user-control) (McAuley, Mortier, and Goulding 2011)。
- HDI 关注于人类对大规模、非结构化且复杂数据集的操纵（manipulation）、分析和意义构建（sense-making） (Elmqvist 2011)。
- HDI 涉及与数据的协作过程，以及能够实现交互的通信工具的开发 (Kee et al. 2012)。
- HDI 旨在从大数据集中提供个性化（personalised）、上下文感知（context-aware）且可理解的数据 (Cafaro 2012)。
- HDI 旨在提供关于个人的数据的访问权限及其理解，以及这些数据如何影响个人 (Mashhadi, Kawsar, and Acer 2014)。

尽管这些定义各不相同，但不同版本的 HDI 之间存在一条共同的线索，表明：
- 存在着海量的数字数据，以至于它可能被视为计算领域和社会共同的下一个前沿 (Pentland 2012)。
- HDI 在很大程度上是围绕大量的“个人数据”构建的，无论是在提供个性化体验方面，还是在涉及个体本身方面。
- 交互涵盖了一系列相互关联的主题，从数据分析（data analytics）到数据[定制（tailoring）](https://www.interaction-design.org/literature/topics/tailoring)，以及实现访问、控制和协作。

![](https://public-media.interaction-design.org/images/uploads/3ca0136a8958be22e55f13ef640893.png)

作者/版权持有者：Richard Mortier。版权条款与许可：CC BY-NC-ND
- 
*图 1：人-数据交互（Human-Data Interaction, HDI）模型中的数据流。我们产生数据，这些数据经过分析以产生推论（inferences）。这些推论反过来被反馈，影响我们的行为，并使其自身成为进一步分析的对象。*

在阅读 2010 年代中期的相关文献时，我们可以发现这仍然是一个新兴领域（fledgling field）！——我们认为，当时的 HDI 并非关注数据本身（per se），甚至不是关注数字数据，而是高度聚焦于与人相关的数字数据，以及在性质上可被视为“个人”数据的数字数据。正如 McAuley（Horizon Digital Economy Research 数字经济教授）、Mortier 以及 Goulding（Horizon Digital Economy Research 研究员）(2011) 和 Haddadi（Queen Mary University 讲师）等人 (2013) 分别所述：

> “现代生活使我们每个人都参与到数据的创建和管理之中。关于我们的数据要么由我们自己创建和管理（例如：我们的地址簿、电子邮件账户），要么由他人创建和管理（例如：我们的健康记录、银行交易、会员卡活动）。有些数据甚至可能是由我们产生且关于我们，但由他人管理（例如：政府的税务记录）。”

> “一个通常是协作但有时具有对抗性的生态系统，正围绕着从事个人数据使用的公司和个人而形成。”

HDI 的核心在于 Mortier et al. (2014) 提出的三个核心原则：可读性（legibility）、能动性（agency）和可协商性（negotiability）：

- **可读性（Legibility）。** 基于对数据流（data flows）和数据处理过程（data processes）的交互通常是不透明的这一认识，可读性关注于*使数据和分析算法（analytic algorithms）对用户而言既透明又易于理解*。
- **能动性（Agency）。** 能动性是指*管理“我们的”数据及其访问权限的手段*，它使我们能够在认为合适的时候，在这些系统中*有效地采取行动*。这不仅包括选择加入（opt-in）或退出（opt-out）数据收集和处理的能力，还包括更广泛地参与数据收集、存储和使用的能力，以及理解并修改数据及其推导出的结论的能力。
- **可协商性（Negotiability）。** 可协商性是指*处理数据[社会方面（social aspects）](https://www.interaction-design.org/literature/topics/social-aspects)的手段*，它支持其他数据主体（data subjects）及其政策之间的交互。这使得用户能够*持续参与，从而能够全部或部分地退出数据处理*，并能从数据采集（data harvesting）中为自己获取价值。

### 41.3.1 可读性（Legibility）—— 使数据主体能够理解与其相关的数据

我们与在线数据系统的交互通常对我们而言是不透明的（opaque）：很少有能与物理世界人造物（physical world artefacts）相对应的在线形式，例如在安装有闭路电视（CCTV, closed-circuit television）的场所中要求的强制性标识（mandatory signage），这些场所通常出于监控和安全目的进行录像和监测。我们认为，仅仅让这些过程变得透明（transparent）是不够的：它们通常具有技术复杂性，且所收集和处理的数据所带来的影响往往难以理解。相反，我们认为这些过程必须具有*可读性（legible）*，即能够被相关人员所理解。这是我们在个人数据被收集和处理的情况下，能够自觉地行使能动性（agency）的前提条件。这种对数据可读性需求的认可已在同意（consent）和撤回（withdrawal）等特定场景中得到体现（Coles-Kemp and Zabihi 2010），且随着社会日益向数据驱动（data-driven）方向发展，这一需求正变得无处不在。

![](https://public-media.interaction-design.org/images/uploads/a6299daeed42cb2e99e12529513b95f8.jpg)
Author/Copyright holder:Jorge Gonzalez. Copyright terms and licence: CC BY-SA 2.0

*仅仅让在线数据系统的过程可见或透明是不够的。其技术复杂性以及收集和处理数据的多重影响也必须具有可读性，以便相关人员能够理解它们。*

关于我们的数据，我们往往对其了解不足。例如，第三方网站追踪（third-party website tracking）在与推荐系统（recommender systems）和数据挖掘算法（data-mining algorithms）相结合时，可以通过推断（inferences）产生新数据，例如广告偏好（Vallina-Rodriguez et al. 2012）。信用评分公司（Credit-scoring companies）和“客户科学（customer science）”公司收集并挖掘购物和交易数据，旨在预测并促成特定行为。然而，并非*所有*此类数据用途都纯粹是商业性的。例如，个人数据可用于为新的众包应用（crowdsourced applications）生成数据，如交通报告或优化后的公交路线（Berlingerio et al. 2013）。但目前迫切需要新的工具，以告知人们其数据的相关情况以及围绕这些数据所采取的实践。我们产生的数据源于我们与众多传感器和技术的交互，包括如今已变得平凡的技术，如在线社交网络（Online Social Networks, OSNs）和网站。然而，这类数据的丰富度和多样性正在不断增加，特别是随着人们对生活记录（lifelogging）和“量化自我（Quantified Self）”（Choe et al. 2014）的兴趣日益增长。例如，我们在监测健康时会显式交互的设备和传感器（如连续血糖监测、智能哮喘吸入器、追踪体重的体重秤，或监测睡眠模式的智能手机应用程序）。这些设备可以创建“以人为中心（people-centric）”的传感器轨迹（sensor trails）（Campbell et al. 2008）。便携式医疗传感器、低成本个人基因组筛查（personal genomics screening）以及其他移动健康诊断工具的相关进展，将产生新的个人医疗数据集（Kumar et al. 2013）。

可读性（Legibility）包含几个特征。首先，我们需要意识到数据正在被收集。这一点相对容易实现，例如近期欧洲的立法要求网站在存储浏览器 Cookie 时必须向用户明确告知。第二个且更为复杂的要求是，我们需要意识到数据本身及其含义。一种以数据为中心（data-centric）的世界观要求我们关注数据的正确性（在客观知识的意义上）。相比之下，以人为中心（human-centric）的视角则要求系统允许存在不同 *但同样有效* 的

数据的视角。同样，对数据的解读（interpretations of data）可能会随着时间的推移而产生显著变化，例如，Court of Justice of the European Union (2014) 最近提出的“被遗忘权（right-to-be-forgotten）”，允许从 [搜索引擎](https://www.interaction-design.org/literature/topics/search-engine-optimization) 结果中删除关于个人的公开数据，从而使遥远的过去不会在人们心中保持新鲜，这在某种程度上镜像了人类在面对过时信息时自然遗忘的行为。

仅仅提供数据可视化（visualisations of data）只是一个起点，并且是 HCI（人机交互）领域中一个被广泛研究的课题。然而，MetroMile 的设计师 Chloe Fan (2013) 观察到，由于涉及的数据规模（scale of data）巨大，即使是可视化也可能带来问题；Quantified Self（量化自我）应用的开发者在展示关于单个个体的各项详细且丰富的数据（从身体活动到睡眠模式和饮食）时也发现了这一点。CSIRO 的首席研究员 Zaslavsky，The Open University 的研究员 Perera，以及澳大利亚 RMIT 的教授 Georgakopoulos (2012) 指出，对于具有固有模糊性（inherent ambiguous）的数据，也会出现类似的问题，例如通过物联网（Internet-of-Things）技术收集的关于社区的数据。然而，数据可视化在揭示与数据处理相关的激励模型（incentive models）以及处理算法（processing algorithms）本身细节方面的潜力，可能会带来更多

商业环境中所面临的棘手挑战。一种可能的途径是与艺术家合作，尝试将这些极其抽象的概念（数据 Data、算法 Algorithm、推理 Inference）转化为用户可理解（Legible）的形式 (Jacobs et al. 2013, 2016)。

### 41.3.2 能动性（Agency）—— 在数据系统中为自己采取行动的能力

使我们能够意识到个人数据收集的事实及其影响，是一个有益的第一步。然而，要将人置于这些数据处理系统的核心，还需要更多：我们需要*能动性（Agency）*，即在这些系统中为自己采取行动的能力。2016年，在个人数据被收集时获得告知的权利被写入了诸如《欧洲通用数据保护指令》（European General Data Protection Directive）等法律中。但随着关于我们的个人数据在私密性、普遍性和重要性方面的增加，我们需要更广泛的能力来参与其收集、存储和使用，以便理解并修改原始数据以及从中得出的推断（Inferences）。

这不仅仅是提供知情同意（Informed consent）的能力，尽管即便如此，这一点往往也未能实现（或在 2010 年代中期尚未实现）(Ioannidis 2013; Luger, Moran, and Rodden 2013; Luger and Rodden 2013)。数据收集过程可能由于上下文依赖（Contextual dependencies）、时间及其他抽样偏差（Sampling biases）以及简单的语义（Semantics）误解而存在固有偏差。从我们的个人数据中得出的推断可能是错误的，无论是因为算法缺陷、数据不完整，还是因为我们的态度和偏好随时间而变化。因此，我们需要以用户为中心的控制（User-centric controls），不仅是为了获得同意，也是为了撤回（Revocation）已收集的个人数据 (Whitley 2009)。

除了监管机构与……之间更丰富、更强有力的对话之外

我们认为，要实现这些目标，需要包括研究人员、监管机构、技术专家和工业界在内的利益相关者（stakeholders），建立[定性（qualitative）](https://www.interaction-design.org/literature/topics/qualitative-research)和[定量（quantitative）](https://www.interaction-design.org/literature/topics/quantitative-research)的技术，以理解并指导围绕人类数据（human data）的活动。一项针对 1,464 名英国消费者的调查显示，94% 的受访者认为他们应该能够控制关于自身被收集的信息 (Bartlett 2012)。值得注意的是，提供此类能力可能也会给数据收集和处理机构带来益处：同一项调查报告称，65% 的受访者表示，如果机构“能够公开且清晰地说明数据将如何被使用，并且我可以授予或撤回许可”，他们愿意与这些机构分享更多数据。- 剩余 6 小时 50 分 8 秒：[ Gamification - How to Create Engaging User Experiences](https://www.interaction-design.org/courses/gamification-how-to-create-engaging-user-experiences)

请注意，我们并非建议所有用户都必须持续参与其个人数据的收集、管理和处理。在隐私和个人数据领域的大量研究已经揭示了诸如「隐私悖论（Privacy Paradox）」之类的特性，即隐私仅在受到侵害（Barnes 2006）后才会成为关注点；因此，我们可以合理地预期，许多人可能并不经常需要或希望在这些数据收集和处理系统中拥有操作能力。然而，许多人会不时地这样做，而一些爱好者可能会更频繁地操作。我们主张，必须在这些方面为他们提供支持。

证据表明，表达数据管理机制的手段，例如「隐私政策（Privacy Policies）」，在设计（Trudeau, Sinclair, and Smith 2009）和解读（Leon et al. 2012）方面都具有难度，因此，支持用户进行更广泛的操作可能会是一个巨大的挑战。数据收集者与第三方数据使用者之间的相互作用，给个人数据的隐私及其对隐私的理解带来了新的挑战：当数据收集的影响可能跨越多个实体和多个时间段时，我们如何才能准确地衡量个人数据收集的影响？如果我们无法衡量这些

……的影响，那么就很难说服人们应该对此感到担忧，或者应该采用诸如差分隐私（Differential Privacy, Dwork 2006）、隐私保护画像和广告方案（Privacy-preserving Profiling and Advertising Schemes, Haddadi, Hui, and Brown 2010; Guha et al. 2009），或是用于简化此类系统配置的隐喻（Metaphors, Adams, Intwala, and Kapadia 2010; Kapadia et al. 2007）。

同时值得注意的是，并非所有与个人数据处理（Processing of Personal Data）相关的活动都是有害的，因此在这些系统中赋予用户能动性（Agency）并不一定只会产生负面影响。推荐系统（Recommender Systems, Ricci et al. 2010）可以提供有用的功能，为我们节省时间和精力。通过 Google Maps 等服务提供的实时交通更新能帮助我们避开交通拥堵。公共卫生计划通常基于大量高度个人化数据的聚合（Aggregation）。数据主体（Data Subjects）与数据系统互动的机会，可能使他们能够纠正和改进所持有的数据以及得出的推断（Inferences），从而提高使用我们个人数据的应用程序的整体质量和效用（Utility）。

### 41.3.3 可协商性（Negotiability）——人们在情境变化时重新评估其决策的能力

可读性（Legibility）和能动性（Agency）固然重要，但我们还需要允许人们在情境（Contexts）发生变化时重新评估其决策，这种变化可以是外部的（例如，人员和数据跨越司法管辖边界），也可以是内部的（例如，反馈与控制机制已被证明会影响数据共享行为 (Patil et al. 2014)）。我们将此称为*可协商性（negotiability）*。

关于个人数据使用的许多争论都假设数据被视为一种可以交易且应从中提取经济价值的“商品（good）”（Organisation for Economic Co-operation and Development 2013）。虽然我们同意，利用经济价值模型来构建个人数据利用生态系统和市场可能是可行的 (Aperjis and Huberman 2012)，但我们认为，截至 2016 年，系统中的权力分布极不均衡，过度倾向于那些充当用户经纪人和中介的数据聚合商（data aggregators），从而导致信息时代经济价值呈现出明显的下降趋势 (Lanier 2013)。

有效地纠正这种失衡需要通过研究来理解个人数据使用的*情境完整性（contextual integrity）* (Nissenbaum 2004)，以及这如何影响研究和商业领域中数据的服务及新用途 (Shilton et al. 2009)。情境效应意味着与……相关的数据

人在现实中不能被视为是*中立的*或*价值中立的（value-free）*，这导致将*数据驱动社会（data-driven society）*或*大数据（Big Data）*等概念应用于个体时会出现问题。鉴于数据收集量的增加 (Solove 2013)，期望人们能够自我管理其个人私密数据可能是不恰当的，因此法律和监管框架（legal and regulatory frameworks）可能需要重新审视和处理 (Westby 2011)。

开展使用个人数据实验的研究人员已经在面临其中一些问题。实验设计（Experiment design）需要仔细考虑所使用的数据类型，以及如何获得使用数据的适当知情同意（consent）(Brown, Brown, and Korﬀ 2010)。研究数据的共享正变得流行，甚至被强制要求，以此作为确保优质科学研究及其传播的机制 (Callaghan et al. 2012)。因此，关于共享——以及不共享 (Huberman 2012)——数据的隐私和伦理问题（privacy and ethics issues）正日益受到讨论 (O’Rourke et al. 2006)。- 剩余 6 小时 50 分 8 秒：[可用性交互设计 (Interaction Design for Usability)](https://www.interaction-design.org/courses/interaction-design-for-usability)
- 剩余 6 小时 50 分 8 秒：[游戏化：如何创建具有吸引力的用户体验 (Gamification - How to Create Engaging User Experiences)](https://www.interaction-design.org/courses/gamification-how-to-create-engaging-user-experiences)

我们的演示大部分集中在围绕个人数据（personal data）的具体问题上。开放数据（open data）、开放知识（open knowledge）和开放创新（open innovation）的力量也正被许多独立组织广泛倡导，例如 The Open Data Institute。这些努力的目标是将个人和 Web 从回声室（echo chambers）和过滤气泡（filter bubbles）（Pariser 2011）中解放出来，通过对政府及各类组织的透明访问和审计来赋予他们权力。其潜在信念是，发布数据将有助于提高数据的参与性和[可访问性（accessible）](https://www.interaction-design.org/literature/topics/accessibility)，从而推动创新并使大众受益。然而，向公众发布数据需要谨慎，并对数据的使用、相关性以及声誉方面的副作用具有前瞻性。例如，某个特定社区的犯罪数据公开，最终可能会强化该地区作为“犯罪中心”的刻板印象。隐藏在先前经过匿名化（anonymized）和去链接（delinked）的个人数据中的个体，可能会通过应用新公开的数据而被重新识别（Ohm 2010）。因此，HDI 需要考虑...

不仅要考虑个人数据，还要考虑当前*以及未来*的数据。

最后，在我们构建能够让用户理解并参与数据处理系统的基础设施（Infrastructures）和界面（Interfaces）时，必须考虑这些设施将如何塑造我们对数据的推理方式，以及反过来，这种推理方式又将如何塑造它们。我们在这种推理过程中构建和使用的[类比（Analogies）](https://www.interaction-design.org/literature/topics/analogies)将受到文化和语境（Contextual）差异与相似性的影响，而反过来，这些类比又将影响我们在不同社区和文化中如何使用、发布和分发个人数据。

在讨论了 HDI（Human-Data Interaction，人机数据交互）的具体含义之后，我们现在将回顾早期对技术问题的探索，这些探索为 HDI 的发展提供了启发。这为 HDI 的演进方向及其当前的发展轨迹提供了基础。

## 41.4 Dataware: HDI v0

McAuley, Mortier, and Goulding (2011) 提出的 Dataware 模型是对后来成为人机数据交互（Human-Data Interaction, HDI）核心概念的特定实例化（Instantiation）的一次非常早期的尝试。该模型基于三种基本的交互实体，如图 2 所示：*所有者*（Owner，或称*用户* User 或*主体* Subject），即数据的创建者或数据所指向的对象；*数据源*（Data sources），负责生成和整理数据；以及*数据处理器*（Data processors），旨在以某种方式利用用户的数据。

![](https://public-media.interaction-design.org/images/uploads/113969ead7714b4f61353752304fe77e.png)
Author/Copyright holder: Richard Mortier. Copyright terms and licence: CC BY-NC-ND
*图 2：Dataware 模型中的参与者：所有者（或用户或主体）、数据源和处理器，他们之间的交互是通过所有者的个人容器（Personal container）来介导的。*

为了帮助所有者管理这些实体之间的关系，该模型假设底层技术将为他们提供一个*个人容器*（Personal container）——这是后文（§6）将讨论的 Databox 的前身——使其能够监督并管理其数据源的访问权限，以及各种数据消费者对其数据的处理。这是一个逻辑上的、主要由云端托管（Cloud-hosted）的实体，其形式为一个分布式计算系统（Distributed computing system），而设想用于支持该系统的软件则由一组提供对数据源所持数据访问权限的 API 组成。*数据处理器*（Data processors）将

编写调用这些 API 的代码，然后将该代码分发至负责执行该代码的数据源（data sources），并按照数据处理器（data processor）的指示返回结果。构想中的最后一件关键基础设施是一个*目录（catalogue）*，所有者在此注册其所有数据源，处理器则向其提交关于可用数据源的元数据（metadata）请求，以及以指定方式处理数据的请求。

![](https://public-media.interaction-design.org/images/uploads/f318c83733431af4cc5fa9396fbc2a83.png)
Author/Copyright holder: Richard Mortier. Copyright terms and licence: CC BY-NC-ND
*图 3：Dataware 架构中的工作流：向所有者的目录发起请求，目录通过对请求进行签名来授予权限。当签署的请求被提交至数据源进行处理时，数据源可以验证其是否具有运行权限。*

从用户的[观点（point of view）](https://www.interaction-design.org/literature/topics/point-of-view)来看，与图 2 所示模型的交互方式如图 3 所示：希望访问目录中一个或多个数据集的处理器提交访问请求以及关于该请求的信息（至少包含待执行处理过程的表示形式）；用户允许（或拒绝）该请求，目录通过向处理器返回某种形式的令牌（token）来表示...

在获得权限后，处理器（processor）随后将请求（即要执行的处理操作）和令牌（token）提交给其覆盖的数据源；最后，数据源按照请求中的指示将处理结果返回给数据消费者（data consumer）。该模型假设目录（catalogue）及其引用的数据源由用户管理，包括对数据使用的日志记录（logging）和审计（auditing），以便用户能够追溯检查执行了什么操作、何时执行、由谁执行以及出于何种目的。该模型还允许用户操作多个相互独立的目录，从而提供了一种控制跨不同数据源链接账户（linking accounts）问题的方法。此类目录之间的交互不被视为系统的显式功能。

尽管 Dataware 从未实际部署，但它探讨了 HDI 中出现的一些关键交互和技术问题：
- 对通用或至少是自描述（self-describing）的数据格式以及相关的源发现（source discovery）手段的需求。
- 对支持所有者多个数据源之间联邦化（federation）的需求，因为许多现有数据源将保留在不同的组织中，以及与之相关的身份机制（identity mechanisms）的需求。
- 对协议的需求，这些协议不仅要支持资源发现（resource discovery），还要支持数据处理权限的协商（negotiation of permission），以及用户控制数据处理执行环境的能力，从而让他们能够完全控制具体有哪些数据被外传（exfiltrated）给请求的数据[消费者]。

处理器。

接下来，我们将深入探讨 HDI（Human-Data Interaction）所引发的交互问题（interactional issues）。

## 41.5 交互：HDI 中的 “I”

因此，我们可以将 dataware 视为一种构建数字基础设施的尝试，旨在通过呈现用户的个人数据源，以及第三方将如何使用或已经如何使用这些数据，来支持[人机数据交互（Human Data Interaction, HDI）](https://www.interaction-design.org/literature/topics/human-data-interaction)。它将 HDI 中的 “I”（Interaction，交互）解读为相关方之间的一种可问责的交易（accountable transaction），并以请求（request）、许可（permission）和审计（audit）的形式进行配置。这无疑能够改变（截至 2010 年代中期）的现状，因为当时的特点是第三方对个人数据的使用在很大程度上缺乏问责机制。然而，它并未描述此类交易在实践中将如何以可问责的方式进行：请求、许可和审计将围绕哪些可问责的事项（accountable matters）展开？我们接下来的重点将转向剖析人机数据交互中所谓“可问责事项”的具体含义。

### 41.5.1 数据作为边界对象（Boundary Object）

正如前文所述，HDI 关注的是与人相关的、被认为具有个人性质的数字数据：它是一个嵌入在人类关系中的对象（object-embedded-in-human-relationships），而这些关系中的数据交易视角可以通过“边界对象（Boundary Objects）”这一概念来详细阐述。也就是说，HDI 依赖于一种“共同的操作模式（mutual modus operandi）”，其中涉及通过参与者的“网络（networks）”来规范信息“流（flow）”的“沟通（communications）”和“翻译（translations）”。

然而，接下来的问题是：Dataware 提供的这种“请求-许可-审计（request-permission-audit）”的交互安排，是否具有足够的连贯性，从而使 HDI 成为一种“平凡的基础设施（mundane infrastructure）”？仔细观察后，答案是否定的：沟通并非真正意义上的相互。相反，驱动沟通的是第三方而非数据主体（data subjects），交互是作用于“用户”的，而非由用户发起的。即使在用户拥有拒绝或撤销许可的能力时，他们面对的依然是单向流量：Dataware 的操作模式是不对称的（asymmetrical）。这便引出了一个问题：对称的关系应该是怎样的？例如，用户如何通过（例如）主动寻找数据处理者（data processors）来驱动数据共享？Dataware 模型的固有认知特性（inherently cognitive character）使情况进一步复杂化：它基于“我的数据”和“关于我的数据”，忽略了人类数据的 $N$ 维特性（*N*-dimensional character），因为数据往往并非仅与“我”或“你”相关，而更多地与“我们”相关。由此，“我的数据”模型的连贯性（coherence）开始瓦解，且这种瓦解方式极具挑战性。这不仅仅是处理例如“你”在“我的” Facebook 页面上发布了什么的问题，而是关于如何处理我们*共同*生产和消费的媒介。因此，数据单元（unit of data）并不总是“我的”，而经常是“我们的”。“我们的数据”应当如何处理？社交数据（social data）又该如何编目和治理（governed）？当我们开始思考“我们的”数据如何被所有、控制和管理时，“我的”数据的个体化模型（individuated model）便崩溃了。仅仅像家庭网络（home network）的日常管理那样，指定家庭中的某个个体来对其进行“维护”（house keep）是不够的 (Tolmie et

al. 2007). 任何此类尝试都涉及一系列关系性问题（relational issues）：我们这一“群体”（cohort）成员的年龄将决定所有权（ownership）与控制权（control），成员所处的个人情况亦然。例如，谁将拥有并控制“我们”孩子的个人数据？那么，我们群体中年迈、体弱或暂时丧失行为能力（temporally incapacitated）的成员又该如何处理？

以幼儿的个人数据为例——谁拥有它，谁又控制它？不能假设行使所有权与控制权的是*同一个人*。所有权可以说归属于数据所指向的个人。然而，在这种情况下，控制权很可能被委托给他人（例如父母），从而反映了组织化的个人数据处理实践（organised practices of personal data handling）（例如，幼儿的健康记录或银行详情）。

然而，这种情况并不适用于青少年。随着他们独立意识的发展，我们可以预见，同样基于当前人类数据交互（human data interaction）的组织化实践，他们将接管对自己数据的控制权，以及生活中许多其他方面的控制权。即便如此，这可能是一个阶段性的过程，而非剧烈的转变。相反地，这种情况也可能适用于群体中希望将个人事务管理移交给他人的老年成员。在活跃的社会语境（social context）中，伴随着不同的关系性权利与义务（relational rights and obligations），所有权与控制权不能被永久地固定并绑定在某个

……个体，正如 Dataware 模型所假设的那样。相反，它将随着一系列不断演变的关系和偶然因素而随时间变化。

在现实世界中，数据共享是“接收者设计（recipient designed）”的——也就是说，它是由人们根据其与共享行为相关方之间的关系而塑造的。例如，你告诉他人关于你抽烟喝酒的量、饮食习惯或体重等信息，在很大程度上取决于你是在向*谁*讲述。例如，医生们非常清楚，当患者向他们陈述此类情况时，往往会严重低估其实际程度。同样的情况更普遍地存在；并非我们总是严重低估事物，而是我们在披露个人生活信息时具有“选择性（selectivity）”，这种选择性取决于我们与相关其他方之间的关系。HDI（Human-Data Interaction，人机数据交互）将接收者视为处理者（processor），在获得许可后，处理者向数据源（data source）提交特定的计算请求以执行相关操作。虽然这一点成立，但问题的关键在于如何让用户能够设计权限，从而决定数据的*哪些*部分可供处理者以及特定群体（cohort）中的其他成员*使用*。接收者设计将我们的注意力引导至在 HDI 过程中支持人类判断、决策和干预的必要性。

HDI 在社会世界中的这些微妙之处表明，有必要开发一个更全面且动态的人类-数据*交互（interaction）*模型。

这将包括用户拒绝或撤销数据访问权限以及对数据进行脱敏（redact）的可能性，无论是在群体（cohort，无论是家庭还是其他人群组合）内部，还是在与第三方的外部交互中。这些问题绝非构建支持 HDI 的数字基础设施所面临挑战的全部，但它们表明，在很大程度上，我们需要将“衔接工作（articulation work）”纳入到 HDI 中。

### 41.5.2 HDI 中的衔接工作

衔接工作（Articulation work）探讨了人类行为的协调特性，以及个体行动过程之间的相互衔接（gearing in）。Copenhagen Business School 的社会学博士、工作、技术与组织教授 Kjeld Schmidt 利用民族志数据（ethnographic data），强调了协调所依赖的行动与交互的几个通用特征 (Schmidt 1994)。这些特征包括：在协作整体（cooperative ensemble）中对显著活动“维持互惠意识（maintaining reciprocal awareness）”；将“注意力导向（directing attention）”协作活动的当前状态；向整体成员“分配任务（assigning tasks）”；以及将工作的某些方面“移交（handing over）”给他人接手并自行处理。这些协调行动的通用属性具体体现在创建并维持“共同工作领域（common field of work）”的情境化实践（situated practices）中，无论是协调与他人同行“行走”，还是与处理者“共享”个人数据。在 HDI 中，共同工作领域是用户生成的数据源目录。数据的“共享”围绕该目录组织，并且表面上是通过“请求-许可-审计（request-permission-audit）”这一交互安排来协调的。然而，从协作工作的角度来看，这种安排是不充分的，原因正如 Schmidt 所指出的：

> “……为了能够将支持需求概念化并具体化

关于协作工作，我们需要在以下两者之间做出一个基础性的分析区分：(a) 与工作场域（field of work）的状态相关，并由工作场域状态的变化所中介的协作工作活动；以及 (b) 由于工作需要并涉及多个代理（agents），且这些代理的个体活动需要被协调、调度、啮合、整合等——简而言之，需要被“衔接（articulated）”而产生的活动。
—— Kjeld Schmidt

请求、权限和审计日志是工作场域内部的协调机制，但它们并没有对工作场域进行衔接。它们规范了用户与第三方之间的信息流，但信息流本身需要被衔接。例如，是什么促使了一个请求的发出，且使其发送方式在用户看来是“合理的”？考虑我们通常会对陌生人的请求持有怎样的预期，以及可能产生的相应反应。再加上我们通常如何应对陌生人关于个人数据的请求，很快就会发现，发起请求并非一件简单的事情；它需要经过衔接。

因此，人机数据交互（Human-Data Interaction, HDI）中的一个关键设计挑战，不仅在于开发合适的机制来协调工作场域内的信息流，还在于对使这种流动成为*可能*的工作进行衔接，从而实现协调。

HDI 中存在这样一个限制：请求（request）功能和审计（audit）功能都无法提供足够的支持，因此无法让用户洞察用户与第三方之间协作工作（cooperative arrangement of work）的安排，或该安排中数据处理的状态。HDI 中的协作工作实际上是在一个“黑盒（black box）”中进行的。用户无法通过请求或审计功能获知诸如：数据处理在工作安排中进行到了哪个阶段、谁在对其进行何种操作、接下来将发生什么、是否存在问题或令人担忧的事项等等。工作的衔接（articulation of work）仅限于谁出于什么目的需要数据，以及对这些信息的审查。因此，目前的 HDI 几乎没有提供任何支持，以用于持续管理涉及个人数据共享的各种参与者（actors）之间的关系。再次强调，如果缺乏这些机制，很难想象 HDI 将基于何种基础成为日常生活中稳定的社会技术基础设施（socio-technical infrastructure）。- 剩余 6 小时 50 分 8 秒：[ Gamification - How to Create Engaging User Experiences](https://www.interaction-design.org/courses/gamification-how-to-create-engaging-user-experiences)

因此，一个关键挑战在于创建计算交互机制，将衔接工作（Articulation Work）的基础对象构建到 HDI 中，使分布式行动（Distributed Action）的显著维度对用户可见且可追溯，从而使他们能够管理和协调交互。这么说并不是指我们应该盲目遵循先前对显著特征的规定（尽管其中一些似乎仍然适用），而是我们需要对个人数据共享及其涉及的协作工作安排中需要被“衔接”的内容建立*更深刻的理解*。

同样的情况也适用于工作领域（Field of Work）本身。Schmidt 指出，协作工作安排中的分布式活动是围绕工作领域内部的对象（例如目录中的数据源）而展开衔接的。这里的一个关键问题围绕着对工作领域进行排序的“概念结构与资源（Conceptual Structures and Resources）”，这些资源使协作集群（Cooperative Ensemble）的成员能够理解该领域并据此采取行动。当我们询问 HDI 提供了什么样的概念结构时，交互充分性（Interactional Adequacy）的问题再次出现。这并不是说它没有提供任何结构，而是它提供结构的方式从交互的角度来看是有问题的。

以 Dataware 目录为例。它在概念上是通过“表（tables）”来组织的，这些表通过账户、应用程序、安装项和服务等维度，使数据源变得可理解。这里的问题在于，Dataware 中实例化的 HDI 概念结构是基于底层技术来呈现的，而不是基于通过该技术所执行的具体操作（例如作为医疗体系一部分的生物数据处理）。因此，问题在于如何组织工作领域（field of work），使其能够反映“正在进行的工作（work-being-done）”或“将要进行的工作（work-to-be-done）”，而非该工作的底层技术组件。那么，当这些对象（即数据源）对于普通大众而言缺乏可读性（Legibility）或可理解性（Intelligibility），而仅对计算机科学家和软件工程师可见时，很难想象用户如何能就工作领域中的对象来阐明其分布式活动（distributed activities）。因此，需要其他更“用户友好”——更准确地说，是与数据相关且针对特定服务的——概念结构和资源。

### 41.5.3 阐明 HDI 的交互挑战

阐明 HDI 中涉及的工作领域（field of work）以及工作的协作安排（cooperative arrangements of work），是 HDI 面临的两个关键挑战。我们已经看到，目前尚未建立起一种共同的操作模式（modus operandi），且那些数据被他人用于特定目的的用户，并*没有*获得互惠的发现机会（reciprocal opportunities for discovery）。我们已经看到，数据不仅是“我的”，也是“我们的”，因此具有社会属性。我们已经看到，所有权（ownership）与控制权（control）并非同构（isomorphic），且生活世界（life world）驱动着这些交互方面的动态。我们已经看到，数据共享是由接收者设计的（recipient designed）。简而言之，我们已经看到，组织该工作领域的概念结构和资源缺乏可读性（legibility）、可理解性（intelligibility）和问责制（accountability）。这些问题中的每一个都是 HDI 工作领域的固有特征，并为其持续的阐明带来了挑战。

### 41.5.3.1 用户驱动的发现（User-driven Discovery）

究竟什么应该被设置为可发现的，以及用户在发现过程中可以行使什么样的控制权？这些问题在很大程度上取决于对用户个人数据源元数据（metadata）的阐明（articulation），其范围（例如）可以从仅仅阐明用户目录（catalogue）的访问位置，到关于目录内容的更详细信息。阐明工作（articulation work）的需求对这一过程提出了进一步的要求。即使用户愿意发布关于其数据的元数据，为了在过程中建立信任，可能仍需要某种手段来了解*谁*有兴趣发现这些数据。这可能包括提供关于*哪些*处理者（processors）感兴趣、何时感兴趣、频率如何等分析数据（analytics）。此类分析可以为用户提供资源，使其能够决定公开或隐藏哪些数据，尽管在重要方面，发现过程还可能取决于访问控制（access control）的其他方面，包括定义关于谁可以或不可以发现其数据的预设策略（policies）。

关于用户如何驱动发现过程（为自己寻找数据处理者，无论是出于个人、财务还是社交目的）的问题则更为复杂。我们稍后将讨论关于如何解决这一问题的初步想法（§6），其核心在于使数据处理者的发现过程类似于在应用商店中发现新应用。用户熟悉并会自觉地选择

访问应用商店，用户可以在那里获取关于应用及其开发者的丰富元数据（metadata），这些信息影响着他们的决策过程。数据处理者（Data processors）可以像 iTunes Store 中的应用一样经过“审核（vetted）”，并且可以像 Google Play Store 中的应用权限（app permissions）一样，逐步提供关于处理过程的更详细信息。此外，应用商店的社交维度在发现过程（discovery process）中也起着重要作用：用户评分和社交网络链接有助于建立用户与服务提供商之间的信任，而这种信任对于新技术的发现和采用至关重要。

### 41.5.3.2 从“我的数据”到“我们的数据”

数据所有权（Data Ownership）与控制权的社会挑战，使得研究用户如何整理并协作管理个人与集体数据源变得至关重要。个人将需要能够控制其个人数据源的资源，以及允许其将数据源和目录（Catalogues）的控制权委派给他人的资源，例如，“我”可以将“我的”数据源控制权分配给“你”。所有权与控制关系在目录内部以及目录之间如何表示，以及需要什么样的机制来为其持续的定义（Articulation）提供充分支持，目前仍是一个开放性问题。即便如此，透明度/感知度（Transparency/Awareness）将是与权限管理（Rights Management）一同需要考虑的重要事项。

集体数据源的创建与策展（Curation）同样具有挑战性。虽然这看起来可能很简单——例如，能源消耗数据目前可能与家庭相关，而非与特定个人相关，不涉及复杂的身份和管理问题——但为这类数据设定用途（Purposing）绝非易事。谁有权查看和共享此类数据？谁可以编辑它或撤销其使用权？谁实际上拥有并控制它？一种观点可能是默认由缴费人拥有，但并非所有集体数据源都必然基于合同关系。在个人数据采集（Personal Data Harvesting）盛行的环境下，情况变得更加复杂……

[它]日益与我们日常交互（mundanely interact）的物品相结合，而通过数据分析（Data Analytics）使集体与个人行为处于前所未有的审视之下的可能性，已成为一个现实且具有挑战性的前景。个人数据与集体数据之间固有的张力（inherent tension），将要求开发能够支持群体内部协商数据采集（negotiated data collection）、分析与共享的群组管理机制（group management mechanisms）。

### 41.5.3.3 数据源的可读性（The Legibility of Data Sources）

无论是个人独立完成还是经过协商而产生的个人数据的生产、分析与共享，都取决于数据源对用户而言是否具有可读性（Legibility）。为了让用户能够在 HDI 系统中以任何有意义的方式拥有能动性（Agency）——即行使控制的能力——数据源必须在以下方面提供最低限度的可读性：包含哪些数据、可以从这些数据中得出什么样的推断（Inferences）、这些数据如何与其他数据关联，等等。如果没有某种手段（最好是以某种可以标准化的形式）来呈现这些关键信息，用户将很难开始理解他们所做决定以及授予的数据处理权限可能带来的影响。

作为其中的一部分，关键在于用户不仅能够可视化（Visualise）并检查数据源中所持有的数据，而且能够可视化并由此理解数据处理者（Data processor）想要从某个数据源或一组数据源中获取什么以及原因——即确保“共享”的具体内容对用户而言是透明且可问责的（Transparently accountable），这可能还涉及将外部数据源（例如消费者趋势数据）可见化，以便用户理解具体交出了什么。与此相关的是，需要允许用户进行接收端设计（Recipient design）。这包含两个不同的方面：一个围绕于允许用户编辑数据，对他们不希望向他人公开的数据部分进行脱敏（Redacting），无论是在...

该群体内部及其外部。另一个方面则围绕在需要保证数据准确性时（例如，能耗读数），如何控制向处理器（processors）呈现的数据。

总之，在人机数据交互（Human-Data Interaction, HDI）中表述（articulating）个人数据的挑战尚未得到解决。相反，它们为进一步的调查、详述和支持开辟了若干主题领域：

- *个人数据发现（Personal data discovery）*，包括元数据（meta-data）发布、消费者分析、[可发现性（discoverability）](https://www.interaction-design.org/literature/topics/discoverability) 策略、身份机制，以及支持发现数据处理器的应用商店模型。
- *个人数据所有权与控制（Personal data ownership and control）*，包括数据源的群体管理、协商、委派、透明度/感知机制以及权利管理。
- *个人数据可读性（Personal data legibility）*，包括处理器将从数据源中提取内容的视觉化呈现，以及帮助用户理解数据用法的视觉化呈现，以及支持数据编辑和数据呈现的接收端设计。
- *个人数据追踪（Personal data tracking）*，包括数据共享过程的实时表述（例如，当前状态报告和聚合输出），以及数据追踪（例如，随后的消费者处理或数据传输）。

这些主题中的每一个都需要跨学科的调查和详述。这包括对个人和群体在个人数据创建与策展（curation）方面当前实践的人类学研究（ethnographic studies）。

通过共同设计干预（co-designed interventions）来理解未来的可能性，并开发合适的模型、工具和技术，以提供支持人类数据基础设施（Human Data Infrastructure, HDI）中复杂过程所需的技术，并将个人数据的衔接（articulation）与日常生活的组织实践相结合。在许多方面，这意味着号召更广泛的人机交互（HCI）社区去研究和设计那些“无聊”的事物——即基础设施（infrastructures）——因为个人数据就嵌入在其中：例如健康基础设施、通信基础设施、金融基础设施、消费基础设施、能源基础设施、媒体基础设施等。这是一个号召，旨在围绕个人数据在日常生活中多样化基础设施中产生和使用的那些平凡方式，来研究和构建 HDI。通过这样做，我们或许能理解个人数据如何在人际关系中被负责地交换，从而就未来如何衔接这些关系产生[可操作的洞察（actionable insights）](https://www.interaction-design.org/literature/topics/information-visualization)。

因此，对 Dataware 提案讨论所产生的分析，以及随后采用更具交互性的视角（interactional lens）审视该问题，极大地推进了我们对 HDI 的概念认知。相应地，这也使我们对支持 HDI 的技术平台可能是什么有了更深入的细化——我们将在接下来的部分讨论其中一个提案。

## 41.6 Databox: HDI v1

Dataware 专注于一种处理个人数据的计算模型——通过将代码移至数据端（moving code to data），可以避免与将数据发布给第三方相关的问题。然而，它未能详细考虑通过研究人机交互（HCI, Human-Computer Interaction）文献以及在前一节中讨论的边界对象（boundary object）和衔接工作（articulation work）概念而识别出的众多交互挑战。在这些考量的基础上，我们目前关于人机数据交互（HDI, Human-Data Interaction）的工作致力于开发基础设施技术，旨在支持个人（首先是个人）管理其个人数据。这项工作将最初的云托管在线个人容器（Personal Container）概念完善为 *Databox* (Haddadi et al. 2015)。

你的 Databox 是一个由相关服务支持的物理设备，它使你能够协调个人数据的收集，并有选择地、临时地将这些数据用于特定目的。该设备支持不同的模型，使你能够将数据与此类目的相匹配：从在隐私保护的数据发现服务（privacy-preserving data discovery services）中注册，以便数据处理者（data processors）能够找到你的 Databox 并请求访问其持有的数据，到在应用商店中搜索你希望通过 Databox 提供数据访问权限的数据处理应用程序。它的物理形态提供了一系列

……提供纯虚拟方案无法实现的各种可供性（Affordances），例如基于其位置和用户接近程度的定位物理交互。

值得注意的是，我们并不设想 Databoxes 将完全取代如 Facebook 和 Gmail 等专门的、特定应用的服务。这些提供价值的网站将继续接收个人数据进行处理，以换取它们所提供的服务。此外，Databox 也不仅仅是以隐私和防止涉及个人数据的活动为导向。相反，它的明确目的是为了实现新的应用程序，这些程序能够结合来自多个数据孤岛（Data silos）的数据，从而得出目前无法获得的推论。通过纠正当前个人数据生态系统（Personal data ecosystem）中权力关系的极不对称性，Databox 为我们如何构思、管理、交叉关联和利用“我们的”数据以改善“我们的”生活，开辟了一系列市场和社会方案。

为了实现这些目标，Databox 必须提供哪些功能？我们从四个方面来回答：它必须是一个*可信平台（Trusted platform）*，为数据主体提供*数据管理（Data management）*设施，同时允许希望使用其数据的其他方进行*受控访问（Controlled access）*，并为所有相关方*提供激励机制（Supporting incentives）*。

### 41.6.1 可信平台（Trusted Platform）

您的 Databox 负责协调、索引、保障安全并管理关于您的以及由您产生的数据。这些数据可能分布在多个位置，但 Databox 持有索引并授权访问这些数据的手段。因此，它必须具有极高的可信度：与传统数据孤岛（Data Silos）可获取的数据相比，它所能处理的数据范围潜在地更具侵入性，同时也更有用。因此，尽管隐私并非 Databox 的首要目标，但在其实现过程中，保护隐私有着明确的要求 (Haddadi, Hui, and Brown 2010)。对平台的信任需要强大的安全性、可靠的行为以及持续的可用性。Databox 的所有操作和行为必须由全方位日志记录（Pervasive Logging）及其相关工具提供支持，以便用户以及（潜在的）第三方审计员能够建立信任，确认系统运行符合预期；且一旦发生不可预见的情况，至少可以追踪其结果。我们设想这样一个平台拥有一个物理组件，其形态（Form-factor）可能是一个[增强型](https://www.interaction-design.org/literature/topics/augmented-reality)家庭宽带路由器，并由个人直接进行物理控制。因此，在利用和整理来自远程云服务的数据时，它还能管理那些个人不愿将其发布到任何远程云平台上的数据。

### 41.6.2 数据管理（Data Management）

Databox 必须提供手段让用户审视其包含的数据，从而实现知情决策（informed decision-making），特别是关于是否将访问权限委派给他人。作为这些交互的一部分，并且为了增强对平台的信任，用户必须能够通过其 Databox 编辑和删除数据，以此来处理不可避免的情况——即发现错误数据已被推断并分发。这可能需要 Databox 能够将此情况告知第三方。同样地，某些数据可能不应表现出数字记录通常具有的“完美记录（perfect record）”倾向。使 Databox 能够自动遗忘不再相关或已不再真实的数据的手段，可能会增加用户对平台的信任 (Mayer-Schonberger 2009)，尽管自动确定这些特征可能具有挑战性。即使数据之前已被使用，它可能仍需要被“停止使用（put beyond use）” (Brown and Laurie 2000)。诸如欧盟的“被遗忘权（Right to be Forgotten）”等概念，要求第三方服务和数据聚合商（data aggregators）遵守约定的协议及其他形式的协作。Databox 可作为协商此类数据访问和发布权限的中心点。

### 41.6.3 受控访问（Controlled Access）

用户必须对提供给第三方的数据拥有细粒度控制（fine-grained control）。至少，Databox 必须支持可选择性查询（selectively queryable），而更复杂的功能则包括支持隐私保护数据分析技术（privacy-preserving data analytics techniques），例如差分隐私（differential privacy, Dwork 2006）和同态加密（homomorphic encryption, Naehrig, Lauter, and Vaikuntanathan 2011）。Databox 的一个关键特性是它支持撤销（revocation）先前授予的访问权限。在那些授予访问权限意味着数据可以被复制到其他地方的系统中，实际上无法撤销对已访问数据的访问权限。相比之下，Databox 可以授予在本地处理数据的访问权限，而*无需*允许复制原始数据（raw data），除非该请求中明确包含了此项。因此，随后的访问可以被轻松撤销 (McAuley, Mortier, and Goulding 2011)。随之而来的挑战是如何让用户就发布特定数据项（datum）的影响做出知情决策（informed decisions），因为这需要了解所有可能访问新发布数据的第三方的未来可能信息状态（information-states）。简化这一过程的一种方法是，仅在对结果进行谨慎且不可逆的聚合（irreversible aggregation），且达到使去匿名化（de-anonymisation）变得不可能的程度后，才发布数据。更复杂的决策将需要用户与其 Databox 之间进行持续的对话，以帮助用户理解其决策的影响，甚至进行学习

利用这些决策来指导未来的行为。

### 41.6.4 支持性激励机制（Supporting Incentives）

上述设想的受控访问（controlled access）导致的一个结果是，用户可能会拒绝第三方服务（third-party services）访问其数据。因此，Databox 必须为服务提供者提供向用户收费的替代方案：希望通过提供数据访问权限来支付的用户可以这样做，而不想这样做的人则可以通过更传统的财务手段支付。这种方案的一种可能实现方式是，允许 Databox 进行支付，并将其与通过某种形式的应用商店（app store）提供的不同第三方服务之间的数据流（data flows）同步追踪。

商业激励（commercial incentives）包括让 Databox 充当访问目前处于其他数据孤岛（silos）中个人数据的网关，并作为商业组织的风险敞口降低机制（exposure reduction mechanism）。这消除了它们直接对个人数据负责的需求，以及随之而来的所有法律成本和限制，转而将控制权交给数据主体（data subject）。这对于必须关注多种法律框架（legal frameworks）的国际组织尤为重要。一个简单的类比是，在线商店使用支付服务（如 PayPal, Google Wallet）以避免支付卡基础设施（Payment Card Infrastructure）合规带来的开销。

至此，这就是人机数据交互（Human-Data Interaction, HDI）在 2010 年代中期的状态：一个新兴领域（nascent field），在技术开发和人类研究方面都具有一些令人兴奋的可能性。接下来，我们将概述其中的一部分。

## 41.7 未来方向：接下来的重点是什么？

人机数据交互（Human-Data Interaction, HDI）的原则强调了在 21 世纪开发一个以用户为中心的个人数据处理平台的必要性。尽管 HDI 仍处于起步阶段，但日益明显的是，它带来了一系列广泛的挑战，而这些挑战直到现在才开始被阐明，例如 Crabtree and Mortier (2015)。其中许多挑战源于互联网早期阶段所做的工程决策，当时为了构建一个能够运行的系统，许多功能被舍弃了 (Clark 1995)。因此，应用（及更高）层的数据流（data flows）并非互联网所关注的问题。互联网过去和现在的重点一直在于在网络接口之间传输数据包（data packets），并支持将这些数据包交付给正确的应用程序。在目前的阶段，很难想象能够完全重新设计互联网的整个基础。然而，解决一些具体的挑战对于将 HDI 的原则付诸实践至关重要。

### 41.7.1 可问责性（Accountability）

HDI 的潜在效能从根本上取决于将互联网在某种程度上“开放”，并使其对用户具有可问责性（Accountability）。我们的意思是，在网络层（network layer），互联网实际上仅支持为了互联网服务提供商（Internet Service Providers, ISPs）之间结算而所需的核算（accounting），例如统计通过特定网络接口交换的字节数，以实现基于用量的计费（usage-based billing）。考虑到物联网（IoT）预计将提供的那类私密数据（intimate data），这种底层的“比特与字节”级别的核算将完全不足。有必要将设备生成了哪些数据、这些数据如何被记录和处理、由谁处理、流向何处等信息显现出来。这些元数据（metadata）必须对用户可见，以便在不侵犯用户隐私的前提下，实现可读性（legibility）、能动性（agency）和可协商性（negotiability）。

### 41.7.2 个人基础设施（Personal Infrastructures）

物联网（IoT）的出现与增长，加上缺乏便捷管理网络连接设备集群（ensembles of network-connected devices）的手段（至少在 2010 年代中期是这样），增加了我们因泄露私密信息而遭受损害的可能性。有必要在互联网开放的同时，开发能够让用户管理数据流的个人基础设施（Personal Infrastructures）。

一种可能的方法是提供更智能的家庭枢纽（Home Hubs），以支持一系列为特定目的而开发的接口和控制点。另一种方法是在更大程度上支持用户构建自己的基础设施，使其远超目前可能实现的程度。我们不应依赖他人（例如互联网服务提供商 ISPs）来提供、配置和管理支持用户的基础设施，而应寻求让用户能够简单地创建自己的基础设施服务，配置并管理诸如防火墙（Firewalling）、虚拟专用网络（VPNs）、域名系统（DNS）等设施及服务。

### 41.7.3 韧性（Resilience）

韧性（Resilience）是互联网、个人基础设施以及关键领域（如健康与福祉或智能设备能源管理）物联网应用之间协同运作的关键要素。简而言之，我们需要思考当互联网中断时（例如，本地接入路由器故障或本地交换局出现问题），这些应用将如何运行。若要依赖关键领域的应用，就必须在物联网基础设施中构建韧性。

一种可能的解决方案是将物联网基础设施集成到本地物理环境中（例如，集成到家庭的建筑结构中），以提供必要的备用机制（Fallback）。这可以通过形式化建模技术（Formal modelling techniques）来进一步增强，从而实现对由“哑”设备（“dumb” devices）组成的复杂网络系统的本地化管理。而这反过来又带来了新的挑战：用户应如何理解这些技术并与之交互，从而在面对突发状况（Contingency）时，确保服务质量（Quality of Service）以及隐私的持续保护。

### 41.7.4 身份（Identity）

正如 Peter Steiner 在 1993 年 *The New Yorker* 的一张漫画中所言：“在互联网上，没人知道你是一条狗。”身份（Identity）涉及 HDI 的方方面面，并要求能够就究竟谁有权访问用户数据做出有意义的陈述。互联网关注的是在网络接口（Network interfaces）之间传输数据包，因此不提供对高层身份表达的内在支持。虽然存在支持身份的应用层（Application layer）手段——例如 TLS 客户端证书（TLS client certificates）和 PGP 公钥（PGP public keys）——但它们的管理极其复杂。此处的具体挑战包括：如何确保在所有可能用于访问相关数据的设备上，必要的“秘密”（Secrets，如密钥、证书）是可用的；如何支持对用户持有的多个身份所对应数据的管理；以及如何处理访问权限的撤销（Revocation of access）。

![](https://public-media.interaction-design.org/images/uploads/1a6b301f0546ed08702c0662f6bfaf74.jpg)
*作者/版权持有者：Peter Steiner。版权条款与许可：合理使用（Fair Use）。*
*“在互联网上，没人知道你是一条狗”是一句名言，最初源自 Peter Steiner 创作并由 *The New Yorker* 于 1993 年 7 月 5 日发表的一幅漫画标题。*

### 41.7.5 动态性（Dynamics）

生成数据的设备在不同个体之间共享时，其情境（Context）会发生变化；同样，个体在时间和空间中的移动也会导致情境的变化。应用程序和服务同样会不断更迭。使用户能够感知并管理持续数据处理的动态性（Dynamics）——例如谁或什么设备可以访问哪些数据、出于何种目的等——是实现个人数据持续采集（Sustained harvesting）的一项关键挑战。这种持续的数据采集具有动态性，且可能涉及多个相关方（包括用户和数据消费者/Data consumers），这进一步带来了如何理解维持该过程所需之“对话”（Dialogues）的挑战；特别是这些对话需要支持的具体“工作”（Work），以及这些对话应当如何被构建、实现与维护。

### 41.7.6 协作（Collaboration）

旨在支持个人数据管理（personal data management）的系统通常侧重于个体。然而，个人数据很少仅涉及单一的人员。更常见的情况是，个人数据源将多个个体的信息融合在一起，而这些个体对于数据的私密程度可能有不同的看法。例如，智能电表数据（smart metering data）提供的是家庭能源消耗的聚合数据，而不同的家庭成员可能希望以不同的粒度（granularity）将该数据与数据消费者共享。支持个人数据的协作管理（collaborative management）和使用是其中的另一个关键要素，而这一切都依赖于提高数据及其处理过程的可读性（legible），并建立相应的机制，使用户能够在其所属的群体内部（*locally*）以及在全局范围内（*globally*）行使能动性（agency）和可协商性（negotiability）。

## 41.8 核心要点

![](https://public-media.interaction-design.org/images/uploads/5b834db70c8595ae8eed736d7b4e56bc.png)
作者/版权持有者：Peter Steiner。版权条款与许可：合理使用（Fair Use）。
*“还记得在互联网上，没有人知道你是谁的时候吗？”是 Kaamran Hafeez 对 Steiner 那幅著名漫画的改编，该漫画于 2015 年 2 月 16 日发表在 The New Yorker 上。*

那么，在这个如此复杂且新兴的领域中，你应该获得什么样的启示？上述漫画给出了一个关键的启示：一个简单的事实，即我们*确实*生活在一个复杂且日益数据驱动（data-driven）的世界中，无论我们是否理解或在意，情况皆是如此。将人-数据交互（Human-Data Interaction, HDI）作为一项研究议程（research agenda）的目标，就是将这一事实推向前台，激发各方的参与，以应对我们认为由此产生的挑战。我们希望，将这些讨论界定为“人-数据交互”，以及我们主张的 HDI 核心原则，能够协助并鼓励许多领域的学者——包括计算机科学、法律、社会学、统计学、[机器学习（Machine Learning）](https://www.interaction-design.org/literature/topics/ai) 等——共同面对我们共同的数据驱动未来所带来的挑战与机遇。

## 41.9 在哪里可以了解更多信息？

作为一个新兴领域，人机数据交互（Human-Data Interaction, HDI）仍处于发展阶段——目前还没有相关的书籍！然而，一个致力于推动其发展的社区正在不断壮大，访问地址为：http://hdiresearch.org/。此外，在不同名义下还开展了许多专项研讨会（ad hoc workshops）和其他活动，例如在英国的 Alan Turing Institute 和 IT as a Utility Network+。

此外，一些新闻文章的评论区也引起了关注，为公众对隐私和 HDI 的反应提供了一些小规模的样本，例如：
- Murphy 2014: [http://www.nytimes.com/2014/10/05/sundayreview/we-...](http://www.nytimes.com/2014/10/05/sundayreview/we-want-privacy-but-cant-stop-sharing.html)
- MIT Technology Review 2015: http: //[www.technologyreview.com/view/533901/the-emerging-...](http://www.technologyreview.com/view/533901/the-emerging-science-of-human-datainteraction)
- Kellingley 2015: [https://www.interaction-design.org/literature/article/human-data-interaction-hdi-the-new-information-frontier](https://www.interaction-design.org/literature/article/human-data-interaction-hdi-the-new-information-frontier)
- Naughton 2015: http: //www.theguardian.com/technology/2015/feb/01/control-personal-data-databoxend-user-agreement.

## 41.10 致谢

本文的研究工作得到了多个机构的资助，包括 RCUK 的 Horizon Digital Economy Research (EP/G065802/1)、Privacy By Design: Building Accountability into the Internet of Things (EP/M001636/1)、CREATe (AH/K000179/1)、Databox (EP/N028260/1) 以及 IT as a Utility Network+ (EP/K003569/1) 等资助项目；以及 EU FP7 的 User Centric Networking 项目（资助编号：611001）。除感谢 HDI（Human-Data Interaction，人机数据交互）社区 (http://hdiresearch.org) 的持续参与和贡献外，我们特别感谢 Kuan Hon, Yvonne Rogers, Elizabeth Churchill, Ian Brown, Laura James, Tom Rodden, QMUL 认知科学研究小组的成员，以及参加 IT-as-a-Utility Network+ 人机数据交互（Human-Data Interaction）研讨会（2013年10月2日）的与会者所提供的建议。

## 41.11 References

- Adams, Emily K., Mehool Intwala, and Apu Kapadia. 2010. “MeD-Lights: a [usable](https://www.interaction-design.org/literature/topics/usability) metaphor for patient controlled access to electronic health records.”
In Proceedings of the 1st ACM International Health Informatics
Symposium, 800–808. IHI ’10. Arlington, Virginia, USA: ACM. isbn:
978-1-4503-0030-8. doi:10.1145/1882992.1883112.
- Aperjis,
Christina, and Bernardo A. Huberman. 2012. “A Market for Unbiased
Private Data: Paying Individuals According to their Privacy Attitudes.”
First Monday 17, nos. 5-7 (May). doi:10.5210/fm.v17i5.4013.
- Barnes, Susan B. 2006. “A privacy paradox: Social networking in the United
States.” First Monday 11, no. 9 (September 4).
doi:10.5210/fm.v11i9.1394.
- Bartlett, Jamie. 2012. The Data Dialogue. London, UK: Demos, September 14. isbn: 978-1-909037-16-8.
- Berlingerio, Michele, Francesco Calabrese, Giusy Lorenzo, Rahul Nair, Fabio Pinelli, and Marco Luca Sbodio. 2013. “AllAboard: A System for Exploring Urban
Mobility and Optimizing Public Transport Using Cellphone Data.” In
Machine Learning and Knowledge Discovery in Databases, edited by Hendrik Blockeel, Kristian Kersting, Siegfried Nijssen, and Filip elezn,
8190:663–666. Lecture Notes in Computer Science. Berlin, Germany:
Springer. doi:10.1007/978-3-642-40994-3
- Bowers, John, and Tom Rodden. 1993. “Exploding the Interface: Experiences of a CSCW
Network.” In Proceedings of the INTERACT ’93 and CHI ’93 Conference on

Human Factors in Computing Systems, 255–262. CHI ’93. Amsterdam, The
Netherlands: ACM. isbn: 0-89791-575-5. doi:10.1145/ 169059.169205.
- Brown, I., and B. Laurie. 2000. “Security against compelled disclosure.” In
Proc. IEEE ACSAC, 2–10. December. doi:10.1109/ACSAC.2000.898852.
- Brown, Ian. 2014. “The Economics of Privacy, Data Protection and
Surveillance.” In Handbook on the Economics of the Internet, edited by
M. Latzer and J.M. Bauer. Cheltenham, UK: Edward Elgar Publishing.
- Brown, Ian, Lindsey Brown, and Douwe Korﬀ. 2010. “Using NHS Patient Data for
Research Without Consent.” Law, Innovation and Technology 2, no. 2
(December): 219–258. issn: 1757-9961. doi:10.5235/175799610794046186.
- Cafaro, Francesco. 2012. “Using embodied allegories to design gesture suites
for human-data interaction.” In Proceedings of the 2012 ACM Conference
on Ubiquitous Computing, 560–563. New York, NY, USA: ACM. isbn:
978-14503-1224-0. doi:10.1145/2370216.2370309.
- Callaghan, Sarah, Steve Donegan, Sam Pepler, Mark Thorley, Nathan Cunningham,
Peter Kirsch, Linda Ault, et al. 2012. “Making Data a First Class
Scientiﬁc Output: Data Citation and Publication by NERC’s Environmental
Data Centres.” International Journal of Digital Curation 7, no. 1 (March 10): 107–113. issn: 1746-8256. doi:10.2218/ijdc.v7i1.218.
- Campbell, Andrew T., Shane B. Eisenman, Nicholas D. Lane, Emiliano Miluzzo,
Ronald A. Peterson, Hong Lu, Xiao Zheng, Mirco Musolesi, Kristf Fodor,

and Gahng-Seop Ahn. 2008. “The Rise of People-Centric Sensing,” IEEE
Internet Computing 12, no. 4 (July): 12–21. issn: 1089-7801.
doi:10.1109/ mic.2008.90.
- Card, Stuart K., Thomas P.
Moran, and Allen Newell. 1983. The psychology of human-computer
interaction. Hillsdale, NJ, USA: Lawrence Erlbaum Associates, February.
isbn: 0898598591.
- Choe, Eun K., Nicole B. Lee, Bongshin
Lee, Wanda Pratt, and Julie A. Kientz. 2014. “Understanding
quantiﬁed-selfers’ practices in collecting and exploring personal data.” In Proceedings of the SIGCHI Conference on Human Factors in Computing
Systems, 1143–1152. Toronto, ON, Canada: ACM Press. isbn: 9781450324731. doi:10.1145/2556288.2557372.
- Clark, David D. 1995. “The
Design Philosophy of the DARPA Internet Protocols.” SIGCOMM Comput.
Commun. Rev. (New York, NY, USA) 25, no. 1 (January): 102–111. issn:
0146-4833. doi:10.1145/205447.205458.
- Coles-Kemp, Lizzie, and Elahe K. Zabihi. 2010. “On-line privacy and consent: a dialogue,
not a monologue.” In Proceedings of the 2010 workshop on New security
paradigms, 95–106. NSPW ’10. Concord, MA, USA: ACM, September. isbn:
978-1-4503-0415-3. doi:10.1145/1900546.1900560.
- Court of
Justice of the European Union. 2014. An internet search engine operator
is responsible for the processing that it carries out of personal data
which appear on web pages published by third parties. Judgment in Case
C-131/12, May 13.
- Crabtree, Andy, and Richard Mortier.

2015. “Human Data Interaction: Historical Lessons from Social Studies
and CSCW.” In Proceedings of European Conference on Computer Supported
Cooperative Work (ECSCW). Oslo, Norway, September.
- Dourish, Paul. 2004. “What We Talk About when We Talk About Context.” Personal
Ubiquitous Comput. (London, UK, UK) 8, no. 1 (February): 19– 30. issn:
1617-4909. doi:10.1007/s00779-003-0253-8.
- Dwork, Cynthia. 2006. “Diﬀerential Privacy.” In Automata, Languages and Programming,
edited by Michele Bugliesi, Bart Preneel, Vladimiro Sassone, and Ingo
Wegener, 1–12. Berlin, Germany: Springer Berlin / Heidelberg.
doi:10.1007/11787006 1.
- Elmqvist, Niklas. 2011. “Embodied Human-Data Interaction.” In Proceedings of the CHI Workshop on Embodied Interaction: Theory and Practice in HCI, 104–107. May.
- Estrin, Deborah. 2013. small data, N=me, Digital Traces. Talk presented at TEDMED 2013, Washington, DC, USA, April.
- European Parliament. 2014. Legislative resolution of 12 March 2014 on the
proposal for a regulation of the European Parliament and of the Council
on the protection of individuals with regard to the processing of
personal data and on the free movement of such data (General Data
Protection Regulation). http://www.europarl.europa.eu/sides/getDoc.do?[type](https://www.interaction-design.org/literature/topics/type)=TA&reference=P7TA-2014-0212&language=EN, March.
- Falahrastegar, Marjan, Hamed Haddadi, Steve Uhlig, and Richard Mortier. 2014. “The

Rise of Panopticons: Examining Region-Speciﬁc Third-Party Web Tracking.” In Proc. Traﬃc Monitoring and Analysis, edited by Alberto Dainotti,
Anirban Mahanti, and Steve Uhlig, 8406:104–114. Lecture Notes in
Computer Science. Also as arXiv preprint arXiv:1409.1066. Springer
Berlin Heidelberg, April. isbn: 978-3-642-54998-4.
doi:10.1007/978-3-64254999-1 9.
- 2016. “Tracking Personal Identiﬁers Across the Web.” In Proceedings of Passive and Active Measurement (PAM).
- Fan, Chloe. 2013. “The Future of [Data Visualization](https://www.interaction-design.org/literature/topics/data-visualization) in Personal Informatics Tools.” In Personal Informatics in the Wild:
Hacking Habits for Health & Happiness CHI 2013 Workshops. ACM.
- Grudin, Jonathan. 1990a. “Interface.” In Proceedings of the 1990 ACM Conference on Computer-supported Cooperative Work, 269–278. CSCW ’90. Los Angeles, California, USA: ACM. isbn: 0-89791-402-3. doi:10.1145/99332. 99360.
- Grudin, Jonathan. 1990b. “The Computer Reaches out: The Historical Continuity of [Interface Design](https://www.interaction-design.org/literature/topics/ui-design).” In Proceedings of the SIGCHI Conference on Human Factors in Computing
Systems, 261–268. CHI ’90. Seattle, Washington, USA: ACM. isbn:
0-201-50932-6. doi:10.1145/97243.97284.
- Guha, Saikat,
Alexey Reznichenko, Kevin Tang, Hamed Haddadi, and Paul Francis. 2009.
“Serving Ads from localhost for Performance, Privacy, and Proﬁt.” In

Proceedings of the Eighth ACM Workshop on Hot Topics in Networks
(HotNets-VIII). New York City, NY, USA.
- Hamed Haddadi,
Heidi Howard, Amir Chaudhry, Jon Crowcroft, Anil Madhavapeddy, Derek
McAuley, Richard Mortier, "Personal Data: Thinking Inside the Box”, The
5th decennial Aarhus conference (Aarhus 2015), August 2015
- Haddadi, Hamed, Pan Hui, and Ian Brown. 2010. “MobiAd: private and scalable
mobile advertising.” In Proceedings of the ﬁfth ACM International
Workshop on Mobility in the Evolving Internet Architecture, 33–38.
MobiArch ’10. Chicago, Illinois, USA: ACM. isbn: 978-1-4503-0143-5.
doi:10.1145/ 1859983.1859993.
- Haddadi, Hamed, Richard
Mortier, Derek McAuley, and Jon Crowcroft. 2013. Human-data interaction. Technical report UCAM-CL-TR-837. Computer Laboratory, University of
Cambridge, June.
- Huberman, Bernardo A. 2012. “Sociology
of science: Big data deserve a bigger audience.” Nature 482, no. 7385
(February 16): 308. issn: 1476-4687. doi:10. 1038/482308d.
- Ioannidis, John P. A. 2013. “Informed Consent, Big Data, and the Oxymoron of
Research That Is Not Research.” American Journal of Bioethics 13, no. 4
(March 20): 40–42. doi:10.1080/15265161.2013.768864.
- Jacobs, Rachel, Steve Benford, Mark Selby, Michael Golembewski, Dominic Price,
and Gabriella Giannachi. 2013. A conversation between trees: what data
feels like in the forest. In Proceedings of the SIGCHI Conference on
Human Factors in Computing Systems (CHI '13). ACM, New York, NY, USA,

129-138. DOI=[http://dx.doi.org/10.1145/2470654.2470673](http://dx.doi.org/10.1145/2470654.2470673)
- Jacobs, Rachel, Steve Benford, Ewa Luger, and Candice Howarth. 2016. The
Prediction Machine: Performing Scientific and Artistic Process. In
Proceedings of the 2016 ACM Conference on Designing Interactive Systems
(DIS '16). ACM, New York, NY, USA, 497-508. DOI: [http://dx.doi.org/10.1145/2901790.2901825](http://dx.doi.org/10.1145/2901790.2901825)
- Kapadia, Apu, Tristan Henderson, Jeﬀrey J. Fielding, and David Kotz. 2007.
“Virtual Walls: Protecting Digital Privacy in Pervasive Environments.”
Chap. 10 in Proceedings of the 5th International Conference on Pervasive Computing, edited by Anthony LaMarca, Marc Langheinrich, and Khai N.
Truong, 4480:162–179. Lecture Notes in Computer Science. Toronto, ON,
Canada: Springer Berlin / Heidelberg, May. isbn: 978-3-540-72036-2.
doi:10.1007/978-3-540-72037-9 10.
- Kee, Kerk F., Larry D.
Browning, Dawna I. Ballard, and Emily B. Cicchini. 2012. “Sociomaterial
processes, long term planning, and infrastructure funding: Towards
eﬀective collaboration and collaboration tools for visual and data
analytics.” In Presented at the NSF sponsored Science of Interaction for Data and Visual Analytics Workshop. Austin, TX, March.
- Kellingley, Nick. 2015. Human Data Interaction (HDI): The New Information Frontier.
https://www.interaction-design.org/literature/article/human-datainteraction-hdi-the-new-information-frontier, November.

- Kum, Hye-Chung, Ashok Krishnamurthy, Ashwin
Machanavajjhala, and Stanley C. Ahalt. 2014. “Social Genome: Putting Big Data to Work for Population Informatics.” Computer 47, no. 1 (January): 56–63. issn: 0018-9162. doi:10.1109/mc.2013.405.
- Kumar,
Santosh, Wendy Nilsen, Misha Pavel, and Mani Srivastava. 2013. “Mobile
Health: Revolutionizing Healthcare Through Transdisciplinary Research.”
Computer 46, no. 1 (January): 28–35. issn: 0018-9162. doi:10.1109/mc.
2012.392.
- Lanier, Jaron. 2013. Who Owns The Future? New York, NY, USA: Simon & Schuster.
- Leon, Pedro G., Justin Cranshaw, Lorrie F. Cranor, Jim Graves, Manoj Hastak,
Blase Ur, and Guzi Xu. 2012. “What do online behavioral advertising
privacy disclosures communicate to users?” In Proceedings of the 2012
ACM workshop on Privacy in the electronic society, 19–30. WPES ’12.
Raleigh, North Carolina, USA: ACM. isbn: 978-1-4503-1663-7.
doi:10.1145/2381966. 2381970.
- Leontiadis, Ilias, Christos Efstratiou, Marco Picone, and Cecilia Mascolo. 2012. “Don’T Kill My
Ads!: Balancing Privacy in an Ad-supported Mobile Application Market.”
In Proceedings of the Twelfth Workshop on [Mobile Computing](https://www.interaction-design.org/literature/topics/mobile-computing) Systems & Applications, 2:1–2:6. HotMobile ’12. San Diego,
California: ACM. isbn: 978-1-4503-1207-3. doi:10.1145/2162081.2162084.
- Luger, Ewa, Stuart Moran, and Tom Rodden. 2013. “Consent for All: Revealing

the Hidden Complexity of Terms and Conditions.” In Proceedings of the
SIGCHI Conference on Human Factors in Computing Systems, 2687– 2696. CHI ’13. Paris, France: ACM. isbn: 978-1-4503-1899-0. doi:10.1145/
2470654.2481371.
- Luger, Ewa, and Tom Rodden. 2013. “An
Informed View on Consent for UbiComp.” In Proceedings of the 2013 ACM
International Joint Conference on Pervasive and Ubiquitous Computing,
529–538. UbiComp ’13. Zurich, Switzerland: ACM. isbn: 978-1-4503-1770-2. doi:10.1145/2493432.2493446.
- Madden, Mary, Susannah Fox, Aaron Smith, and Jessica Vitak. 2007. Digital Footprints: Online
identity management and search in the age of transparency. PEW Internet
& American Life Project. Retrieved Feb. 23, 2014 from [http://www.pewinternet.org/ﬁles/old-media//Files/R...](http://www.pewinternet.org/%EF%AC%81les/old-media//Files/Reports/2007/) PIP Digital Footprints.pdf.pdf. 1615 L ST., NW – Suite 700 Washington, D.C. 20036: PEW Internet, December.
- Mashhadi, Afra, Fahim Kawsar, and Utku G. Acer. 2014. “Human Data Interaction in
IoT: The ownership aspect.” In IEEE World Forum on Internet of Things
(WF-IoT), 159–162. March. doi:10.1109/WF-IoT.2014.6803139.
- Mayer-Schonberger, V. 2009. Delete: The Virtue of Forgetting in the Digital Age. Princeton University Press. isbn: 9781400831289.
- McAuley, Derek,
Richard Mortier, and James Goulding. 2011. “The Dataware Manifesto.” In
Proceedings of the 3rd IEEE International Conference on Communication

Systems and Networks (COMSNETS). Invited paper. Bangalore, India,
January.
- MIT Technology Review. 2015. The Emerging
Science of Human-Data Interaction.
http://www.technologyreview.com/view/533901/the-emerging-scienceof-human-data-interaction/, January.
- Mortier, Richard, Hamed Haddadi, Tristan
Henderson, Derek McAuley, and Jon Crowcroft. 2014. “Human-Data
Interaction: The Human Face of the Data-Driven Society.”
http://dx.doi.org/10.2139/ssrn.2508051, SSRN (October).
- Murphy, Kate. 2014. “We Want Privacy, but Can’t Stop Sharing.” http://www.
nytimes.com/2014/10/05/sunday-review/we-want-privacy-but-cant-stopsharing.html, New York Times (October).
- Naehrig, Michael, Kristin
Lauter, and Vinod Vaikuntanathan. 2011. “Can Homomorphic Encryption Be
Practical?” In Proc. ACM Cloud Computing Security Workshop, 113–124.
Chicago, Illinois, USA. isbn: 978-1-4503-1004-8.
doi:10.1145/2046660.2046682.
- Naughton, John. 2015. “Fightback against internet giants’ stranglehold on personal data starts here.” [http://www.theguardian.com/technology/2015/](http://www.theguardian.com/technology/2015/) feb/01/control-personal-data-databox-end-user-agreement, The Guardian (February).
- Nissenbaum, Helen F. 2004. “Privacy as Contextual Integrity.” Washington Law Review 79, no. 1 (February): 119–157.
- Ohm, Paul. 2010. “Broken Promises of Privacy: Responding to the Surprising
Failure of Anonymization.” http://uclalawreview.org/pdf/57-6-3.pdf, UCLA Law Review 57:1701–1778.
- Organisation for Economic

Co-operation and Development. 2013. Exploring the Economics of Personal
Data - A Survey of Methodologies for Measuring Monetary Value. Technical report, OECD Digital Economy Papers 220. OECD, April 2.
doi:10.1787/5k486qtxldmq-en.
- O’Rourke, JoAnne M., Stephen Roehrig, Steven G. Heeringa, Beth G. Reed, William C. Birdsall,
Margaret Overcashier, and Kelly Zidar. 2006. “Solving Problems of
Disclosure Risk While Retaining Key Analytic Uses of Publicly Released
Microdata.” Journal of Empirical Research on Human Research Ethics 1,
no. 3 (September): 63–84. issn: 1556-2646. doi:10.1525/jer.2006. 1.3.63.
- Oxford English Dictionary. 2014. http://www.oed.com/view/Entry/296948, February.
- Pariser, Eli. 2011. The Filter Bubble: What the Internet Is Hiding from You. New York, NY, USA: Penguin Press, May. isbn: 1594203008.
- Patil, Sameer, Roman Schlegel, Apu Kapadia, and Adam J. Lee. 2014. “Reﬂection
or Action?: How Feedback and Control Aﬀect Location Sharing Decisions.”
In Proceedings of the ACM SIGCHI Conference on Human Factors in
Computing Systems, 101–110. Toronto, ON, Canada, April. doi:10.1145/
2556288.2557121.
- Pentland, Alex. 2012. “Reinventing
society in the wake of Big Data.” http:
//edge.org/conversation/reinventing-society-in-the-wake-of-big-data,
Edge (August).
- Ricci, Francesco, Lior Rokach, Bracha
Shapira, and Paul B. Kantor. 2010. Recommender Systems Handbook. 1st.
New York, NY, USA: Springer-Verlag New York, Inc. isbn: 0387858199,
9780387858197.

- Schmidt, Kjeld. 1994. Social Mechanisms of Interaction. Technical report COMIC Deliverable 3.2. ISBN
0-901800-55-4. Esprit Basic Research Action 6225.
- Shilton, Katie. 2012. “Participatory personal data: An emerging research
challenge for the information sciences.” Journal of the American Society for Information Science and Technology 63, no. 10 (October): 1905–1915. issn: 1532-2882. doi:10.1002/asi.22655.
- Shilton, Katie,
Jeﬀ Burke, Deborah Estrin, Ramesh Govindan, Mark Hansen, Jerry Kang, and Min Mun. 2009. “Designing the Personal Data Stream: Enabling
Participatory Privacy in Mobile Personal Sensing.” In Proceedings of the 37th Research Conference on Communication, Information and Internet
Policy (TPRC). Arlington, VA, USA, September.
- Solove, Daniel J. 2013. “Privacy Self-Management and the Consent Dilemma.” Harvard Law Review 126, no. 7 (May): 1880–1903.
- Star, Susan Leigh. 2010. “This is Not a Boundary Object: Reﬂections on the
Origin of a Concept.” Science, Technology & Human Values 35 (5):
601–617. doi:10.1177/0162243910377624. eprint: [http://sth.sagepub.com/content/](http://sth.sagepub.com/content/) 35/5/601.full.pdf+html.
- Star, Susan Leigh, and James R. Griesemer. 1989. “Institutional Ecology,
‘Translations’ and Boundary Objects: Amateurs and Professionals in
Berkeley’s Museum of Vertebrate Zoology, 1907-39.” Social Studies of
Science 19 (3): 387–420. doi:10.1177/030631289019003001.
- Strategic Headquarters for the Promotion of an Advanced Information and

Telecommunications Network Society. 2014. Policy Outline of the
Institutional Revision for Utilization of Personal Data. http://[japan.kantei.go.jp/policy/it/20140715_2.pdf](http://japan.kantei.go.jp/policy/it/20140715_2.pdf).
- Taddicken, Monika, and Cornelia Jers. 2011. “The Uses of Privacy Online: Trading a Loss of Privacy for Social Web Gratiﬁcations?” In Privacy Online:
Perspectives on Privacy and Self-Disclosure in the Social Web, 1st ed.,
edited by Sabine Trepte and Leonard Reinecke, 143–156. Springer-Verlag
Berlin Heidelberg. isbn: 978-3-642-21520-9. doi:
10.1007/978-3-642-21521-6_11.
- The Open Data Institute. http://theodi.org/.
- Tolmie, P., A. Crabtree, T. Rodden, C. Greenhalgh, and S. Benford. 2007.
“Making the home network at home: digital housekeeping.” In Proceedings
of ECSCW, 331–350. Limerick, Ireland: Springer.
- Trudeau,
Stephanie, Sara Sinclair, and Sean W. Smith. 2009. “The eﬀects of
introspection on creating privacy policy.” In WPES ’09: Proceedings of
the 8th ACM workshop on Privacy in the electronic society, 1–10.
Chicago, IL, USA: ACM, November. isbn: 978-1-60558-783-7.
doi:10.1145/1655188. 1655190.
- US Consumer Privacy Bill of Rights. 2012. Consumer Data Privacy in a Networked World: A Framework
for Protecting Privacy and Promoting Innovation in the Global Digital
Economy. [https://www.whitehouse.gov/sites/](https://www.whitehouse.gov/sites/) default/ﬁles/privacy-ﬁnal.pdf, February.

- Vallina-Rodriguez, Narseo, Jay Shah, Alessandro Finamore, Yan Grunenberger, Konstantina
Papagiannaki, Hamed Haddadi, and Jon Crowcroft. 2012. “Breaking for
commercials: characterizing mobile advertising.” In Proceedings of the
2012 ACM Internet Measurement Conference, 343–356. Boston, MA, USA: ACM, November. isbn: 978-1-4503-1705-4. doi:10.1145/2398776. 2398812.
- Westby, Jody R. 2011. “Legal issues associated with data collection &
sharing.” In Proceedings of the First Workshop on Building Analysis
Datasets and Gathering Experience Returns for Security, 97–102.
Salzburg, Austria, April. isbn: 978-1-4503-0768-0.
doi:10.1145/1978672.1978684.
- Whitley, Edgar A. 2009.
“Informational privacy, consent and the “control” of personal data.”
Information Security Technical Report 14, no. 3 (August): 154–159. issn: 13634127. doi:10.1016/j.istr.2009.10.001.
- Winstein,
Keith. 2015. “Introducing the right to eavesdrop on your things.”
http://www.politico.com/agenda/story/2015/06/internet-of-things-privacyconcerns-000107, The Agenda Magazine (July).
- World Economic Forum. 2011.
Personal Data: The Emergence of a New Asset Class.
http://www.weforum.org/reports/personal-data-emergence-newasset-class.
In collaboration with Bain & Company, January.
- Zaslavsky, Arkady, Charith Perera, and Dimitrios Georgakopoulos. 2012. “Sensing as a Service and Big Data.” In Proceedings of the International Conference on Advances in Cloud Computing (ACC). Bangalore, India, July.
