# 9. 移动计算（Mobile Computing）

**来源**：The Encyclopedia of Human-Computer Interaction, 2nd Ed.
**Notion 原页面**：https://www.notion.so/7c35528e0d474429b4610399df597fc6

---

[Jesper Kjeldskov](https://www.interaction-design.org/literature/author/jesper-kjeldskov)
使[移动计算（Mobile Computing）](https://www.interaction-design.org/literature/topics/mobile-computing)成为一个有趣的研发和设计课题的原因之一是，该领域在很大程度上由[创新（Innovation）](https://www.interaction-design.org/literature/topics/innovation)驱动，其特点是使用方式快速演进，且具有巨大的市场潜力和增长空间。新技术在不断开发，新的使用领域（Use domains）在不断探索，而成功的创意和应用则能触达数百万用户。事实上，到 2010 年底，全球范围内智能手机（Smartphones）的销量首次超过了个人电脑，仅在当年最后三个月就出货了超过 1 亿台。正是由于该领域具有这种动态且快速演进的特性，工业领先地位在短短十年内就发生了多次更迭——从 Palm 到 Nokia 再到 Apple，并且在未来很可能再次发生更迭。这显然激励着研究人员和设计师不断创新，开发新技术和新应用。

移动技术发展的主要驱动力之一，是人们在工作和休闲领域对交互系统与设备（Interactive systems and devices）的广泛采用。长期以来，手机几乎是每个人都至少拥有一部，并且不仅用于工作，还广泛用于个人用途。随着支持互联网和多媒体功能的手机（如 Apple iPhone）的出现，智能手机现在也牢牢地占据了大众市场，不再是少数商业精英的专属工具。移动技术在工作和私人领域的普及，极大地影响了我们感知和使用这些技术的方式。它们不再仅仅是运行电池的计算机，而是变成了功能性设计对象（Functional design objects），我们深切关注其外观、触感和体验，并在日常生活中同时使用多种此类设备。

## 9.1 引言（Introduction）

移动计算（Mobile Computing）是一个相对较新的研究领域，其历史仅有三十余年。在其发展过程中，该领域已从最初侧重于技术层面，扩展到如今同样关注[可用性（Usability）](https://www.interaction-design.org/literature/topics/usability)、[有用性（Usefulness）](https://www.interaction-design.org/literature/topics/usefulness)以及用户体验（User Experience）。这促使了充满活力的移动[交互设计（Interaction Design）](https://www.interaction-design.org/literature/topics/interaction-design)领域的诞生，该领域处于移动计算、社会科学、人机交互（Human-Computer Interaction）、[工业设计（Industrial Design）](https://www.interaction-design.org/literature/topics/industrial-design)以及[用户体验设计（User Experience Design）](https://www.interaction-design.org/literature/topics/ux-design)等学科的交汇点。

移动计算为现代西方文明中计算资源的普及（Pervasiveness）做出了重大贡献。随着固定式和嵌入式计算机技术在整个社会的扩散，手机以及其他手持或可穿戴计算技术等移动设备，共同创造了一种泛在计算（Ubiquitous Computing）和遍在计算（Pervasive Computing）的状态，在这种状态下，我们周围的计算设备比人还多（Weiser 1991）。如何使我们能够协调这些设备以适应并服务于个人生活和工作，对于技术开发人员来说是一个巨大的挑战，且“由于遍在计算的影响，*交互设计*有望成为 21 世纪的主要人文艺术（Liberal Arts）之一”（McCullough 2004）。

移动计算领域的起源于技术人员与消费者之间利益的幸运契合。自计算时代开启以来，技术上一直渴望使计算硬件小型化；而自从计算机变得广泛[可获取（Accessible）](https://www.interaction-design.org/literature/topics/accessibility)以来，消费者对于能够随身携带计算机产生了浓厚兴趣（Atkinson 2005）。因此，移动计算的历史是由无数商业化设备铺就的。其中大多数设备的生命周期较短且影响微小，但另一些则显著地拓展了工程学和交互设计的边界。我在此希望强调的正是这些设备及其重要性。

## 9.2 移动计算的七次浪潮

移动计算的历史可以分为若干个时代或“浪潮（Waves）”，每个浪潮都以特定的技术重点、交互设计趋势为特征，并导致了移动设备设计和使用的根本性变化。在我看来，到目前为止，移动计算的历史包含了七个尤为重要的浪潮。虽然这些浪潮并非严格的线性顺序，但它们为当前的移动计算研究和设计所基于的传承提供了良好的概览。

1. 便携性（Portability）
2. 小型化（Miniaturization）
3. 连通性（Connectivity）
4. 融合（Convergence）
5. 分化（Divergence）
6. 应用（Apps）
7. 数字生态系统（Digital ecosystems）

关注**便携性（Portability）**的时代旨在缩小硬件尺寸，从而创造出能够在物理空间中相对容易移动的计算机。**小型化（Miniaturization）**旨在创造全新且尺寸显著更小的移动形态（Form factors），使得用户在移动过程中也能使用个人移动设备。**连通性（Connectivity）**侧重于开发能够让用户在移动过程中通过无线数据网络保持在线并进行通信的设备和应用。**融合（Convergence）**旨在将新兴类型的数字移动设备（如个人数字助理 (PDAs)、手机、音乐播放器、相机、游戏机等）整合到混合设备中。**分化（Divergence）**在交互设计上采取了相反的方法，通过推广具有专门功能而非通用功能的“信息设备（Information appliances）”来实现。最新的**应用（Apps）**浪潮旨在开发在移动设备上使用和消费的内容与实质，并让用户能够轻松且愉快地访问这些具有趣味性或功能性的交互式应用内容。最后，新兴的**数字生态系统（Digital ecosystems）**浪潮关注的是普适（Pervasive）且相互关联的技术所构成的更大整体，交互式移动系统正日益成为这一整体的一部分。

### 9.2.1 便携性（Portability）

第一批移动计算机（Mobile computers）——即现代笔记本电脑的前身——开发于 20 世纪 70 年代末和 80 年代初，其灵感源自 Alan Kay 在 1968 年提出的 Dynabook 概念的便携性（Portability）（Kay 1972）。Dynabook 概念最初被构想为一台面向儿童的机器，但敏锐的企业家，如 [GRiD Systems](https://www.interaction-design.org/literature/topics/grid-systems) 的创始人 John Ellenby 很快意识到，如此具有创新性的产品，其切入点必须是“资金最充足且需求最迫切的客户”（Moggridge 2007）。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_01.jpg)
作者/版权持有者：GRiD Systems Corporation; Alan C. Kay。版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅[版权声明](https://www.interaction-design.org/about/terms-of-use)页面的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

**图 9.1**：Alan Kay 的 Dynabook：“一台面向所有年龄段儿童的个人计算机”（Kay 1972）

第一台笔记本电脑是 Bill Moggridge 在 1981 年设计的 GRiD Compass 1101，其设计目标是使其能够放入仅占公文包一半空间的区域（Moggridge 2007; Atkinson 2005）。Compass 配备了 16MHz 的 Intel 8086 处理器、256K DRAM、一块 6 英寸 320x240 像素的平板显示屏、340kb 的气泡存储器（Bubble memory）、一个 1200 bit/s 的调制解调器，重量为 5 公斤，并运行名为 GRiD OS 的图形操作系统。它主要销售给美国政府，并在 20 世纪 80 年代初被 NASA 用于航天飞机任务以及在战斗中使用。GRiD Compass 的实用专利中包含 43 项令人惊叹的创新特性，包括平板显示屏和铰接屏幕（Hinged screen）。然而，第一款取得真正商业成功的便携式计算机是 1982 年推出的手提箱式 Compaq Portable，作为首款正式的 IBM 兼容机（IBM clone），它可以运行 MS-DOS 和标准 PC 程序。1988 年，Grid Systems 还开发了第一台平板电脑 GRiDpad，该项目由 Jeff Hawkins 发起并领导，他后来设计了第一款 PalmPilot 并创立了 Palm Computing。

从设计的持久性和影响力来看，Bill Moggridge 对第一台笔记本电脑的开发以及 Jeff Hawkins 对 GRiDpad 的工作，证明了在移动计算中进行细致且深思熟虑的交互设计（Interaction Design）的价值。GRiD Compass 在设计和性能方面领先了十年。它定义了 30 年后至今仍在笔记本电脑中使用的折叠设计，而其基础形态（Form factor）直到 1991 年 Apple PowerBook 100 引入如今已成为标准的蛤壳式设计（Clam-shell design）和集成指点设备（Pointing device）才被超越。GRiDpad 的基础设计为平板电脑和手持设备（如 Apple Newton、PalmPilot 甚至 iPad）铺平了道路。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_02_1.jpg)
作者/版权持有者：未知（待调查）。版权条款与许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_02_2.jpg)
作者/版权持有者：Compaq Computers。版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅[版权声明](https://www.interaction-design.org/about/terms-of-use)页面的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_02_3.jpg)
作者/版权持有者：GRiD Systems Corporation。版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅[版权声明](https://www.interaction-design.org/about/terms-of-use)页面的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

**图 9.2 A-B-C**：20 世纪 80-90 年代的移动计算机：GRiD Compass 1101 (1981)、Compaq Portable 1 (1982) 和 GRiDpad 1910 (1989)

### 9.2.2 小型化（Miniaturization）

到 20 世纪 90 年代初，计算机硬件的尺寸已经缩小到可以使全新的、更小尺寸规格（Form Factors）的移动计算机在市场上出现并演进。这些设备主要是手持设备，被称为掌上电脑（Palmtop Computers）、数字组织器（Digital Organizers）或“个人数字助理（Personal Digital Assistants, PDAs）”。PDA 与笔记本电脑的不同之处在于它们具有真正的移动性，用户可以在实际走动时操作。它们不被视为台式机或笔记本电脑的替代品，而是为那些需要离开电脑工作的忙碌商务人士提供的轻便补充设备。第一款 PDA 是 1992 年的 Apple Newton。1997 年，第一款 PalmPilot 面世，2000 年 Compaq 推出了 iPAQ Pocket PC。笔记本计算的重点主要在于便携性以及对台式机文档和应用的移动访问，而掌上电脑计算则引入了一个额外的重点：专门为移动设备和移动用户设计的应用程序和交互风格。

PDA 这一代移动设备代表了一系列独特的交互设计选择和尺寸规格。最显著的是，它们引入了相对较小的触控屏（Touch-sensitive screen）与独立触控笔（Stylus）相结合的交互方式。通过使用触控笔，用户可以直接在屏幕上与内容交互，并通过屏幕键盘或手写识别（Handwriting recognition）软件输入文本。其他交互设计创新还包括用于访问预定义应用程序和功能的函数按钮、用于操作菜单的[导航（Navigation）](https://www.interaction-design.org/literature/topics/navigation-1)键，以及用于与固定计算机同步和充电的“一键式”扩展坞（Dock）。虽然 Psion series 3 到 5 复制了“微型笔记本”的设计，但 Newton、PalmPilot 和 iPAQ 都代表了一种根本性的新型移动计算形态，其设备表面的大部分区域被用于显示。在交互设计方面，尤其是 PalmPilot，是针对新兴的手持计算机类别进行细致且深入重新思考的产物；包括它们应该具有什么样的外观和触感，应该执行哪些功能，以及如何执行这些功能。例如，PalmPilot 的创造者 Jeff Hawkins 后来解释说，他随身携带不同尺寸和形状的木块，直到他找到了该设备的完美物理形态 (Bergman and Haitani 2000)。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_03_1.jpg)
作者/版权持有者：Apple Computer, Inc. 版权条款和许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因为无法获得许可）。请参阅[版权声明](https://www.interaction-design.org/about/terms-of-use)页面上的“例外”部分（以及“allRightsReserved-UsedWithoutPermission”子部分）。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_03_2.jpg)

作者/版权持有者：Palm Inc.. 版权条款和许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因为无法获得许可）。请参阅[版权声明](https://www.interaction-design.org/about/terms-of-use)页面上的“例外”部分（以及“allRightsReserved-UsedWithoutPermission”子部分）。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_03_3.jpg)
作者/版权持有者：Psion. 版权条款和许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因为无法获得许可）。请参阅[版权声明](https://www.interaction-design.org/about/terms-of-use)页面上的“例外”部分（以及“allRightsReserved-UsedWithoutPermission”子部分）。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_03_4.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。

**图 9.3 A-B-C-D**：20 世纪 90 年代至 2000 年代的移动计算机：Apple Newton (1992), PalmPilot (1997), Psion 5 (1997), 以及 Compaq iPAQ (2000)

随着 PDA 的出现，也出现了专门为移动设备和用户开发的新类别应用程序。每款设备都有自己的操作系统，针对其特定的屏幕尺寸和输入能力进行了优化，并配备了一套用于日历、联系人、笔记和电子邮件的标准应用程序。此外，大量第三方应用程序很快便可购买，或者通过一种新方式——通过互联网下载。到 20 世纪 90 年代末，专门针对移动设备的应用程序开发已成为一个公认的研究领域和专业方向。1998 年，首届关于移动设备人机交互（Human-Computer Interaction with Mobile Devices, Mobile [HCI](https://www.interaction-design.org/literature/topics/human-computer-interaction)’98）的国际研讨会在 Glasgow 举行，专门探讨移动设备、系统和服务在交互设计和用户体验方面新兴的挑战。

### 9.2.3 连通性（Connectivity）

移动计算（Mobile Computing）的第三波浪潮起源于无线电信（Wireless Telecommunication）。早在 1973 年，由 Martin Cooper 领导的 Motorola 团队就开发并申请了一项手持移动电话的概念专利，这促成了 1983 年第一款体积小到可以携带的商业移动电话 DynaTAC 8000X 的问世。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_04.jpg)
作者/版权持有者：Motorola。版权条款和许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因为无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面上的“例外”部分（以及“allRightsReserved-UsedWithoutPermission”子节）。
**图 9.4**：第一款手持手机：Motorola DynaTAC 8000X (1983)

在 20 世纪 80 年代和 90 年代初，手机并不真正被视为计算机。然而，随着 1991 年数字全球移动通信系统（Global System for Mobile Communications, GSM）的引入（该系统还包含了短信服务（Short Message Service, SMS）通信组件），手机的复杂性和功能开始迅速演进。全球大众对手机技术的接纳程度也随之提高。这意味着手机开发人员突然面临着巨大的交互设计（Interaction Design）挑战，不仅要设计通话功能，还要处理联系人、日历、文本消息以及浏览互联网。在 90 年代后期，手机的交互设计无疑由 Nokia 主导，该公司推出了一系列具有开创性的手机。当时的挑战在于如何为极小的低分辨率显示屏以及仅限于 12 键数字键盘（以及少量功能键和导航键）的输入能力进行设计。在 90 年代，第一批明确经过严谨交互设计流程而产生的手机之一便是 Nokia 3110。它引入了简单的图形化菜单系统和用于简化用户交互的“Navi-key”概念——这一交互设计通过随后的 Nokia 手机触达了超过 3 亿用户（Lindholm and Keinonen 2003）。1999 年，Nokia 3110 的基础交互设计在极其成功的 Nokia 3210 中得到了扩展，增加了用于短信发送的 T9 预测文本（T9 Predictive Text）、游戏、可自定义的铃声以及可更换的外壳。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_05_1.jpg)
作者/版权持有者：Nokia。版权条款和许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因为无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面上的“例外”部分（以及“allRightsReserved-UsedWithoutPermission”子节）。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_05_2.jpg)
作者/版权持有者：Nokia。版权条款和许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因为无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面上的“例外”部分（以及“allRightsReserved-UsedWithoutPermission”子节）。
![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_05_3.jpg)
作者/版权持有者：Nokia。版权条款和许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因为无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面上的“例外”部分（以及“allRightsReserved-UsedWithoutPermission”子节）。
**图 9.5 A-B-C**：三个移动交互设计里程碑：Navi-key、T9 和 WAP：Nokia 3110 (1995)、Nokia 3210 (1999) 和 Nokia 7110 (1999)

在 90 年代后期，短信极其巨大且完全出乎意料的普及，激发了将互联网引入手机的尝试。这促成了无线应用协议（Wireless Application Protocol, WAP）的开发，使得简化版的网站可以在小屏幕上查看，为移动设备访问互联网铺平了道路。第一款配备 WAP 浏览器的手机是 Nokia 7110。为了满足滚动浏览长 WAP 页面的需求，它还配备了第一个“Navi-roller”拇指滚轮。作为一个有趣的交互设计案例，7110 还配备了一个*弹簧加载*的盖板来遮盖键盘，这受到了电影 *The Matrix* 的启发，片中主角使用的一款早期 Nokia 手机被剧组改装成了这种功能。你可以说这是“生活在模仿艺术”（Wilde 1889）。然而，由于数据传输缓慢且可用性（Usability）较差（Ramsay and Nielsen 2000; Nielsen 2000），WAP 始终未能达到预期，并很快被移动设备访问真实 Web 的方式所取代。尽管如此，90 年代的手机设计对未来的移动计算产生了根本性且深远的影响。

### 9.2.4 融合（Convergence）

移动计算最有趣的时代之一始于不同类型的专业化移动设备开始融合，形成了具有根本不同形态（form factors）和交互设计（interaction designs）的全新“混合（hybrid）”设备。第一阶段是“智能手机（smart phones）”的出现，它将个人数字助理（PDA）的功能与移动电话相结合。智能手机的发展涉及对多种形态和交互设计的探索，并产生了一系列创新方案。其中许多设计允许根据用户的用途改变设备的物理形状。其他设计，如 Blackberry，引入了“宽体手机”形态，采用 PDA 尺寸的显示屏，并用微型 QWERTY 键盘取代了传统的 12 键数字键盘。1992 年推出的 IBM Simon 是第一款除了通话外，还能用于日历、地址簿、笔记、电子邮件、传真和游戏的智能手机。它没有物理按钮，仅配备触控屏，可用手指或触控笔操作。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_06_1.jpg)
Author/Copyright holder: IBM. Copyright terms and licence: All Rights Reserved. Used without permission under the Fair Use Doctrine (as permission could not be obtained). See the "Exceptions" section (and subsection "allRightsReserved-UsedWithoutPermission") on the page [copyright notice](https://www.interaction-design.org/about/terms-of-use).

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_06_2.jpg)
Author/Copyright holder: Nokia. Copyright terms and licence: All Rights Reserved. Used without permission under the Fair Use Doctrine (as permission could not be obtained). See the "Exceptions" section (and subsection "allRightsReserved-UsedWithoutPermission") on the page [copyright notice](https://www.interaction-design.org/about/terms-of-use).

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_06_3.jpg)

Author/Copyright holder: Ericsson. Copyright terms and licence: All Rights Reserved. Used without permission under the Fair Use Doctrine (as permission could not be obtained). See the "Exceptions" section (and subsection "allRightsReserved-UsedWithoutPermission") on the page [copyright notice](https://www.interaction-design.org/about/terms-of-use).

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_06_4.jpg)
Author/Copyright holder: Blackberry. Copyright terms and licence: All Rights Reserved. Used without permission under the Fair Use Doctrine (as permission could not be obtained). See the "Exceptions" section (and subsection "allRightsReserved-UsedWithoutPermission") on the page [copyright notice](https://www.interaction-design.org/about/terms-of-use).

**图 9.6 A-B-C-D**：探索不同物理形态和交互风格的智能手机：IBM Simon (1992), Nokia 9000 (1996), Ericsson R380 (2000), 以及 Blackberry 5810 (2002)

第二阶段的融合将移动电话与各种富媒体能力（rich media capabilities）相结合，例如数字相机、音乐播放器、视频录制与回放，以及电视和广播接收。智能手机对商务人士的工作活动和生产力具有吸引力，而多媒体手机则吸引了普通大众的休闲、娱乐和社交。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_07_1.jpg)

作者/版权持有者：Sharp。版权条款与许可：保留所有权利（All Rights Reserved）。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用（因无法获得许可）。请参阅 [版权声明（copyright notice）](https://www.interaction-design.org/about/terms-of-use) 页面中的“例外（Exceptions）”章节（以及“allRightsReserved-UsedWithoutPermission”子章节）。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_07_2.jpg)
作者/版权持有者：Nokia。版权条款与许可：保留所有权利（All Rights Reserved）。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用（因无法获得许可）。请参阅 [版权声明（copyright notice）](https://www.interaction-design.org/about/terms-of-use) 页面中的“例外（Exceptions）”章节（以及“allRightsReserved-UsedWithoutPermission”子章节）。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_07_3.jpg)
作者/版权持有者：Nokia。版权条款与许可：保留所有权利（All Rights Reserved）。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用（因无法获得许可）。请参阅 [版权声明（copyright notice）](https://www.interaction-design.org/about/terms-of-use) 页面中的“例外（Exceptions）”章节（以及“allRightsReserved-UsedWithoutPermission”子章节）。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_07_4.jpg)

Author/Copyright holder: Sony Ericsson. Copyright terms and licence: All Rights Reserved. Used without permission under the Fair Use Doctrine (as permission could not be obtained). See the "Exceptions" section (and subsection "allRightsReserved-UsedWithoutPermission") on the page [copyright notice](https://www.interaction-design.org/about/terms-of-use).

**图 9.7 A-B-C-D**：融合的移动设备：拍照手机、游戏手机和随身听手机：Sharp J-SH04 (2001), Nokia N-Gage (2003), Nokia N90 (2005), 以及 Sony Ericsson W600 (2005)

休闲领域最显著的融合案例是拍照手机（camera phone）的发明。第一款配备数字相机的手机是 2001 年推出的 Sharp J-SH04。它当时仅在日本通过 i-mode 移动互联网服务提供，但世界其他地区很快便紧随其后。两年后，拍照手机的销量超过了数字相机；到 2006 年，全球一半的手机内置了相机——这使得 Nokia 成为了最大的数字相机品牌，并迫使 Minolta 和 Konica 等知名品牌退出相机市场。到 2009 年，拍照手机的数量已超过 19 亿部，通过在互联网上捕捉和分享照片的新方式，手机摄影已经产生了巨大的社会影响（参见 Kindberg et al. 2005; Gye 2007）。早期的拍照手机显然是“带有相机的手机”，但新颖的交互设计导致一些融合设备真正模糊了两者的界限（Murphy et al. 2005）。例如，很难分辨 Nokia N90 是一款手机还是一个摄像机。另一项在手机上广泛普及的融合功能是数字音乐播放能力。最显著的是，Sony 在 2005 年以融合设备 Sony Ericsson W600 的形式重新推出了其在 20 世纪 80 年代大获成功的 “Walkman” 品牌。在 2006 年的 W44 多媒体手机中，他们更进一步，在视频和音乐回放的基础上扩展了观看数字电视和收听数字广播的能力。融合还催生了像 Nokia N-Gage 这样形态类似于掌上游戏机的混合游戏手机（game-phones）。

融合趋势背后的根本驱动力在于，[移动用户体验（mobile user experience）](https://www.interaction-design.org/literature/topics/mobile-ux-design) 与交互式移动设备和系统的功能范围（functional scope）成正比：“越多意味着越好（more means more）”（Murphy et al. 2005）。因此，融合经常被批评为产生了可用性（usability）类似于“瑞士军刀”的低效通用方案：即一种功能广泛但没有任何一项功能在独立使用时达到理想状态的笨拙技术（参见 Norman 1998, Bergman 2000, Buxton 2001）。然而，在我看来，融合的真正优势不应仅仅追求在同一设备中简单地实现多种功能，而应在于创造出能够促进此前无法实现之用途的新型混合体，例如拍摄照片并立即与朋友分享、在手机上浏览互联网，或直接在 iPod 上购买音乐。

### 9.2.5 发散（Divergence）

与融合（Convergence）方法相反，**发散（Divergence）**趋势主张的是“单一功能/多种设备”或“信息专用设备（Information Appliance）”的方法，即每台设备都“旨在执行特定的活动，如音乐、摄影或写作”（Bergman 2000）。这一思路背后的驱动力在于，拥有大量优秀的专业化工具，比拥有一个在任何任务上都表现平平的通用工具更好。专业化工具有利于随着时间的推移优化功能，并完善已知的使用范式（Paradigms of use）。发散趋势所倡导的核心观点是，移动用户体验与移动交互设备及系统的功能范围成*反比*：“少即是多”（Murphy et al. 2005）。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_08_1.jpg)
作者/版权持有者：Apple Computer, Inc. 版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/mobile-computing#copyrightNotice) 页面上的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_08_2.jpg)
作者/版权持有者：Archos. 版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面上的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_08_3.jpg)
作者/版权持有者：Sony. 版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面上的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_08_4.jpg)

作者/版权持有者：Apple Computer, Inc. 版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面上的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

**图 9.8 A-B-C-D**：专业化移动媒体和游戏设备：Apple iPod (2001), Archos Gmini (2004), Sony PSP (2004), iPod Nano (2010)

21 世纪初出现了一系列旨在高效完成单一特定任务的发散式移动设备，尤其是移动音乐播放器、视频播放器和游戏机。当然，功能专用的移动设备并非新现象，例如，早期的口袋计算器、手机、[GPS](https://www.interaction-design.org/literature/topics/gps) 接收器、数字相机和 PDA 毫无疑问也可以被归类为信息专用设备。但 21 世纪初发散趋势的有趣之处在于，这是一种刻意的交互设计（Interaction Design）选择，而非技术上的必然。最具传奇色彩的信息专用设备例子可能是 2001 年的 Apple iPod。虽然它不是第一款移动数字音乐播放器，但其交互设计（包括与 iTunes 以及后来的 iTunes Music Store 的集成）从根本上改变了全球音乐的消费和购买行为。尽管 21 世纪中叶市场上的大多数手机都能播放 MP3 文件，但人们仍然倾向于携带另一台设备（iPod）来播放音乐，因为它在该特定任务上提供了更好的用户体验，且设备本身已成为一种流行的时尚单品。到 2010 年底，iPod 的总销量已超过 2.9 亿台。其他发散式移动设备包括 2004 年的 Archos Gmini 等视频播放器、Sony PSP 游戏和视频主机，以及后来增加了视频播放功能的 iPod 版本，但这些设备仍处于相同的基本信息专用设备交互设计框架内。

发散式移动设备的交互设计挑战与融合式设备截然不同，因为其功能范围要窄得多。然而，根据定义，发散式设备通常与设计师无法预知的众多其他交互设备和系统协同使用，因此，如何支持良好且灵活的集成以及“使用中的融合（Convergence-in-use）”构成了巨大的交互设计挑战 (Murphy et al. 2005)。

### 9.2.6 应用（Apps）

2007 年 6 月，Apple 推出了 iPhone。与当时许多同类产品一样，这是一款融合移动设备（Converged Mobile Device），集成了拍照手机、便携式媒体播放器以及具备电子邮件、网页浏览和高速无线网络连接能力的互联网客户端功能。然而，iPhone 并非仅仅是融合移动设备演进过程中的又一次渐进式提升，它代表了对移动交互设计（Mobile Interaction Design）的一次重大重新思考，并做出了一系列显著的交互设计选择。它配备了一个具有简单手势功能（Gesture Capabilities）——如滑动（Swiping）和捏合（Pinching）——的大尺寸高分辨率电容式多点触控显示屏（Capacitive Multi-touch Display），完全摒弃了当时主流的物理按键和用于文本输入与交互的触控笔。用户体验不再是导航于庞大且深层的菜单层级，而是变得更加流畅且具有[美感（Aesthetics）](https://www.interaction-design.org/literature/topics/aesthetics)，使得手机的使用变得极其简单且令人愉悦。iPhone 还配备了多个内置的上下文传感器（Context Sensors），能够根据持握方式改变显示屏的方向模式，这一设想最早由 Hinckley et al. (2000) 在 UIST 会议论文中提出；因此，在通话时将手机靠近面部，会改变手机应用的模式。随后加入的 GPS 和数字指南针将这种“上下文感知（Context-awareness）”能力扩展到了基于位置的服务（Location-based Services）。

在软件方面，iPhone 的网页浏览器首次让用户能够在移动设备上以良好的用户体验访问网络内容，许多人很快发现，与桌面端相比，在 iPhone 上处理电子邮件更加便捷。专用应用程序提供了直接观看 YouTube 视频内容和从 iTunes Store 购买音乐的途径。综合来看，这意味着人们实际上开始将移动设备作为*首选*的互联网入口，而非最后的无奈之选。因此，到 2009 年中期，iPhone OS 在全球移动网络流量总量中占据主导地位（Admob 2009）。此外，通过 MobileMe 等云计算服务，数据和媒体内容可以以前所未有的方式在用户的其他设备以及家中或办公室的计算机之间无缝集成，这展示了创建通过互联网连接的移动和固定计算机系统之*数字生态系统（Digital Ecosystems）*的初步尝试。

iPhone 完全重新定义了移动计算，并为移动交互设计和用户体验设定了新标准，以至于 Google 和 HTC 等公司在 4 年后推出 Android 开源移动操作系统及其相关的在线应用商店时，仍难以企及。在许多方面，iPhone 正是移动交互设计研究人员在过去十年中所构想的设备，而其在全球范围内的巨大普及率（截至 2010 年 9 月，iOS 设备销量超过 1.2 亿台）证实了我们对人们希望如何使用移动设备的推测确实是正确的——只要我们能为他们提供足够优秀的交互设计和用户体验。然而，iPhone 最大的影响不仅在于设备本身的交互设计及其原生应用（Native Applications）的高质量，而在于它创建了一种交互设计，让用户能够便捷地获取海量且前所未有的移动设备*应用程序（Applications）*。

2008 年，Apple 推出了在线的“App Store”，提供了一种机制，使 iPhone 用户可以直接从其移动设备上轻松下载并支付第三方应用内容。这些 App 涵盖了广泛的功能，包括社交网络、生产力工具、个人实用工具、游戏、导航以及电影和电视节目的广告。为了创建这些应用内容，Apple 免费发布了 iPhone OS 软件开发工具包（Software Development Kit, SDK），并采用了一种商业模式：由 Apple 处理支付和分发，而应用创建者可获得 70% 的利润。到 2012 年，从超过 50 万个应用中下载的次数已超过 250 亿次，这使得 Apple 和那些创作了极受欢迎应用的第三方开发者都获得了巨额利润，进而激励了更多应用内容的创建。为了说明这一业务的惊人规模，第三方移动软件开发者在不到三年的时间里，通过 Apple App Store 销售产品共创造了 20 亿美元的收入。与使用 Java 2 Platform, Micro Edition (J2ME) 或 Qualcomm 的 Binary Runtime Environment for Wireless (BREW) 开发移动应用不同，使用 iPhone SDK 开发无需为大量不同的手机型号定制应用，这意味着开发者可以将更多时间花在应用设计上。此外，与安装 J2ME 软件时通常极其糟糕的手机用户界面形成鲜明对比，iPhone 不仅提供了开箱即用的供应链和计费模式，还提供了一种*其本身就具有正向体验*的应用购物用户体验。因此，在 iPhone 出现之前，在手机或 PDA 上下载和安装软件是只有精通技术的人才会做的事情；而如今，无论年龄大小和计算经验如何，这已成为数百万用户的普遍习惯。

作为 iPhone 移动交互设计方法的一个有趣结果，提升设备硬件规格的重要性突然被提升软件质量所超越。这体现在软件开发和更新的速度与范围远超相应的硬件更新，这是移动交互设计中的一个重要转变。它表明，物理形态（Physical Form Factors）以及基础输入输出能力已经达到了某种稳定水平，重心已转向*应用与内容*。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_09_1.jpg)
作者/版权持有者：Apple Computer, Inc. 版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅[版权声明](https://www.interaction-design.org/about/terms-of-use)页面的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子节）。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_09_2.jpg)

作者/版权持有者：Apple Computer, Inc. 版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅[版权声明](https://www.interaction-design.org/about/terms-of-use)页面的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子节）。

**图 9.9 A-B**：Apple iPhone 和 iPad (2007 年和 2010 年)

Apple 在 iPhone 上的成功促成了移动计算领域的第三次尝试——iPad，它于 2010 年 4 月发布。最初的媒体反应褒贬不一，但商业接纳度却前所未有，iPad 在前两个月就售出了 200 多万台，到年底销量达到 1500 万台。虽然 Microsoft 对 PDA 和平板电脑的明确交互设计方法长期以来一直是复制 Windows 95 OS (Zuberec 2000)，但 Apple 在 iPad 平板电脑上采取了相反的方法，将其基于 iPhone OS 而非 MacOSX。这一举动令许多人（诚然包括我自己）感到惊讶，但它起到了重新诠释并随后重新定义的作用，将此前一直处于困境的“平板电脑”类别转化为一种新的*移动设备*类别，而不仅仅是没有键盘的笔记本电脑。尽管被批评为封闭系统（Closed System），但 iPad 的优势在于通过其精细的交互设计所创造的用户体验，这吸引了已经在增长的 iPhone 交互设计师和应用开发者社区去探索平板电脑的形态。在此之前，没有人关心为平板电脑创建网页或原生应用内容 (Chen 2010)，但有了 iPad，平板电脑突然成为了地球上最有趣且最有前景的移动平台之一，到 2011 年 3 月，已有超过 65,000 个可用作 iPad 的应用程序。

### 9.2.7 数字生态系统（Digital ecosystems）

随着我们进入新千年的第二个十年，移动计算（mobile computing）和交互设计（interaction design）所面临的挑战在不断演变。移动设备的硬件能力已显著提升，以至于屏幕空间（screen real estate）、输入能力、处理能力、网络速度和电池寿命等因素，已不再像五年前那样成为主要问题。与此同时，我们在针对相对较小的屏幕以及移动设备的不同输入能力进行设计方面，也已积累了足够的经验，使得数以百万计的普通用户能够下载并使用这些应用程序，甚至愿意为此付费。因此，在很大程度上，我们已经成功解决了过去移动交互研究人员和设计师所面临的大部分问题。然而，正如所有计算领域的发展历史所表明的那样，我们极不可能已经达到了终点。与过去一样，我们今天所见证的技术和交互设计，仅仅是未来技术和交互设计持续演进的起点。那么，未来的移动交互设计面临着怎样的挑战与机遇？下一波移动计算的浪潮将聚焦于什么？

在公众对智能手机和平板电脑等“后 PC 设备（post-PC devices）”的极大兴趣和广泛采用的推动下，推测一个远离桌面计算的重大平台转移（platform shift）即将到来并非没有道理。移动设备正变得越来越重要且普及。它们很快将成为访问互联网的主导入口，并且结合云计算（cloud computing）的增长，很快将主导人们对计算能力的利用。重要的是，我们在这里见证的不仅仅是开发出能力更强、能更好地模拟微型桌面 PC 的智能手机，而是一个主要计算平台的激进演进，它支持全新的应用，允许我们完成以前无法完成的事情。这很可能是一次移动计算和移动交互设计的真正范式转移（paradigm shift）。

观察当前的趋势，看来下一波移动计算和交互设计的浪潮将围绕着“数字生态系统（digital ecosystems）”（Miller et al. 2010）的创建展开，其中移动计算将与其他普适计算（ubiquitous computing）资源协同工作并发挥核心作用。这挑战我们不再将交互式移动设备、系统和服务视为可以脱离其所属的更大使用情境或人造物生态（artefact ecologies）（Jung et al. 2008, Bødker and Klokmose 2011）而独立设计和研究的实体。诚然，各种形式的移动计算机在大多数人的日常生活中扮演着极其重要的角色，但它们并不是我们在家中、工作中或两者之间所使用的唯一技术和人造物。大多数人出于不同目的使用多个移动设备，但他们同时也使用大量固定式或嵌入式计算机系统——在工作场所、在家里、在车里，或在周围的城市中。这些设备协同地构成了一个由交互式设备、系统和服务组成的丰富的数字生态系统，通常被称为普适计算或泛在计算（pervasive computing），其中移动计算是一个核心组件，但并非唯一组件。在这样一个普适且泛在的信息社会中，设计移动交互的挑战在于，如何促进创建能够良好融入这一设备、系统和服务生态系统的交互式设备、系统和服务，并使其适应由这些技术及其用户所创造的、用于工作和休闲的丰富新使用模式。

与任何其他类型的生态系统一样，理解、创建和维护数字生态系统需要对整个运行系统的总体性和生态性持有整体视角（holistic perspective），而不仅仅是对其每个单独组件进行详细分析。移动计算的数字生态浪潮将建立在硬件小型化、连接性、新形式因子（form factors）、输入设备、交互风格、应用程序、融合（convergence）、分化（divergence）和内容等先前时代的成就之上，但它将扩大范围，将更广泛的使用情境以及对影响用户体验（user experience）的上下文因素的明确[敏感度（sensitivity）](https://www.interaction-design.org/literature/topics/empathy)纳入其中。其核心将在于创建能够响应人类生活广泛且多样化方面的交互式设备、系统和服务，这些产品不仅要提供实用性且[易于使用（easy to use）](https://www.interaction-design.org/literature/topics/ease-of-use)，还要能提供愉悦感，并自然地融入人们在不断变化的环境和情境中复杂且动态的生活。

## 9.3 移动计算机的交互设计

交互设计（Interaction Design）这一术语由 Bill Moggridge 和 Bill Verplank 在 20 世纪 80 年代末提出，旨在“设计交互产品，以支持人们在日常生活和工作生活中的沟通与交互方式”（Sharp et al. 2007 p. 8），或者更广泛地定义为“对所有既是数字化又是交互式的事物的设计”（Moggridge 2007 p. 660），并特别关注其主观和[定性（Qualitative）](https://www.interaction-design.org/literature/topics/qualitative-research)方面。换句话说，它旨在通过对交互产品、设备、系统和服务的设计、开发、构建和实施，来创造能够提升生活和工作质量的用户体验（User Experiences）。

如今，交互产品通常基于计算机，这意味着交互设计与所有涉及为人类研究和设计基于计算机系统的学科、领域和方法都相关。因此，除了平面设计和工业设计等设计实践，心理学和社会学等学术学科，以及人机交互（Human-Computer Interaction）和信息系统（Information Systems）等多学科/跨学科领域外，交互设计还涉及计算机科学和工程等技术学术学科。然而，交互设计与这些实践、学科和领域的不同之处在于，它具有不同的整体关注点和目的。它关注的是交互产品用户体验的*整体性（Totality）*，以及所有可能有助于成功创建产品的因素。当我们设计基于计算机的交互系统时，我们不仅在设计它的外观，还在设计它的行为。我们是在设计人与技术如何交互（Moggridge 2007）。正如 Winograd (1996) 所述，进行交互设计在许多方面可以类比为进行建筑设计。建筑师关注的是人们及其在所创建的建筑内部的交互。例如，空间是否符合将要入住的家庭或企业的日常生活或工作方式？房间内部和房间之间的流动是否顺畅？功能相关的空间是否彼此接近？等等。为了支持建筑师的工作，工程师关注建筑的结构稳固性和施工方法，而来自其他学科（如人因工程（Human Factors）和社会科学）的知识也可能影响建筑师创建功能且宜居空间的能力。正如一名优秀的建筑师需要了解这些相关学科一样，一名优秀的交互设计师也是如此。然而，就像设计房子和建造房子之间存在区别一样，设计一个交互产品与对其软件进行工程实现之间也存在区别（Sharp et al. 2007 p. 9）。

移动交互设计（Mobile Interaction Design）是交互设计的一个分支，专门关注非固定式、可随身携带的交互产品、设备、系统和服务的用户体验创建。这得益于前文所述的移动计算（Mobile Computing）的进步，使设计师和系统开发人员能够构思出足够小以至于可以携带、手持甚至佩戴的交互产品，同时提供足够的计算能力和网络能力，以实现有用且具有吸引力的交互系统和服务。这包括手持设备和可穿戴设备、PDA、手机、智能手机、便携式数字媒体播放器、手持游戏机等，以及在这些设备上运行或可通过这些设备访问的软件应用程序和服务。然而，移动交互设计不仅是由计算机科学和工程的进步所促进和驱动的，它还日益得益于我们开发移动计算新使用实践的能力，以及将现有和新兴的移动计算机与网络技术适配并利用（Appropriate）到创新交互产品和解决方案中的能力。因此，我们早已超越了 20 世纪 90 年代末“随时随地（anytime anywhere）”的移动计算炒作，而产生了更理性的愿景，即开发“在正确的时间发挥作用，且懂得其所处环境——能够融入环境的移动设备”（Jones and Marsden 2006）。

随着新技术的开发和新使用实践的出现，移动交互设计的挑战随时间而变化和演进。早期的移动交互设计处理的是便携式计算机的物理设计。随后，重点演变为适用于手持操作和移动使用的输入设备和交互风格（Interaction Styles）。对于手机而言，交互设计的挑战主要在于减小物理尺寸，同时优化有限的屏幕空间（Display Real Estate）和标准 12 键数字键盘，以支持越来越多的潜在应用。随着功能混合且更复杂的设备的出现，交互设计的挑战变成了开发设备的新形式和形状，以及开发可在其上运行的新类型应用，且不增加设备的使用难度。对于日益增多的功能专用移动设备（如数字相机和媒体播放器），交互设计的挑战则变成了如何促进人们在日益复杂的交互计算机系统和数字数据生态系统中，对所有这些设备及其内容进行“编排（Orchestration）”。

如今，设计移动交互的挑战在很大程度上在于*软件应用（Software Applications）*的开发。物理设备的尺寸规格（Form Factor）在一段时间内似乎已经稳定在 2007 年 Apple iPhone 引入的基本尺寸、形状和交互能力上，这一形态在四年多时间里保持不变，并被所有主要手机制造商效仿。这使得关注点转移到了这些设备上可下载和购买的第三方应用内容上，这些内容以功能高度专业化的相对较小的“App”形式存在，不仅由大型软件公司设计，还由小公司甚至个人（包括学生）设计。到 2010 年底，Apple App Store 提供了超过 300,000 个第三方应用程序，Google 的 Android Market 提供了超过 80,000 个。在不到三年的时间里，iPhone 和 iPod Touch 的 App 下载量超过了 100 亿次。然而，尽管每天在 Google 和 Apple 的在线商店中都会出现许多有趣且创新的新移动应用，且全球的应用开发人员和交互设计师正在推高移动计算机设备用途的边界，但当前移动应用设计的状态可以类比为 20 世纪 90 年代中期的 Web 状态。人们对此充满热情和兴趣，开发工具易于获取，且拥有庞大的潜在用户群体。甚至超越了 90 年代中期 Web 的潜力，现在已经有了成熟的数字供应链和微支付（Micro-payments）机制。但就像 15 年前的 Web 一样，我们尚未看到或理解为移动设备设计的第三方应用将对我们生活、工作以及休闲的所有方面产生怎样的深远影响和范围。

### 9.3.1 上下文（Context）的作用

自移动计算（Mobile Computing）和移动人机交互（Mobile Human-Computer Interaction）早期以来，交互式移动系统和设备的“使用上下文（Use Contexts）”一直被强调为系统开发人员在设计、构建交互式移动系统以及评估和研究其使用情况时，必须“意识到”并“考虑到”的关键因素（参见 Johnson 1998, Rodden et al. 1998, Brown et al. 2000）。由于移动使用上下文具有高度动态性、复杂性且确实具有移动性的特质，因此与传统的固定办公系统（Stationary Office Systems）的使用上下文相比，它被认为更具挑战性。此外，人们经常指出，在使用交互式移动计算机系统时，周围上下文中的其他活动往往比与系统本身的实际交互和使用更为重要——例如在街上行走、在酒吧或咖啡馆社交，或者在医院照顾病人。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_10_1.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_10_2.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_10_3.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

**图 9.10 A-B-C**：上下文中的移动计算 (Kjeldskov and Paay 2010)

关于上下文有许多不同的定义，而关于移动计算中上下文的构成及其作用的争论仍在继续。移动计算的早期研究将上下文主要定义为人员和物体的位置（Schilit and Theimer 1994）。在较近期的研究中，上下文被扩展到包含更广泛的因素，例如环境的物理和 [社会方面（Social Aspects）](https://www.interaction-design.org/literature/topics/social-aspects)（McCullough 2004, Dourish 2004, Bradley and Dunlop 2002, Agre 2001, Dey 2001, Abowd and Mynatt 2000, Schmidt et al. 1999a, Crabtree and Rhodes 1998）。Dey (2001) 将上下文定义为“任何可用于表征实体状态的信息。实体是指与用户和应用程序之间的交互相关的个人、地点或物体，包括用户和应用程序本身”。虽然这个定义相当完整，但它对于究竟可以使用哪类信息来表征这种状态并没有给出非常具体的说明。与此相反，Schmidt et al. (1999a) 提出了一个包含两个截然不同类别的上下文模型：人类因素（Human Factors）和物理环境（Physical Environment）。人类因素由三个类别组成：关于用户的信息（画像、情绪状态等）、用户的社会环境（其他人的存在、群体动态等）以及用户的任务（当前活动、目标等）。物理环境由三个类别组成：位置（绝对位置和相对位置等）、基础设施（计算资源等）以及物理条件（噪音、光线等）。该模型提供了一个具体的上下文因素清单，可以补充像 Dey (2001) 那样较为宽泛的定义。其他研究在覆盖不同上下文因素方面可能不够全面，但会对其中一个或几个因素进行详细探讨。在 Agre (2001) 和 McCullough (2004) 的研究中，物理上下文（Physical Context）被赋予了特别的重要性，它由建筑结构和建成环境的元素（例如地标和路径）组成。在 Dourish (Dourish 2001, Dourish 2004) 的研究中，社会上下文（Social Context）被重点关注，包括与环境中人员的交互及其行为。Dourish (2004) 还指出，上下文不能被定义为对环境的稳定描述，而是产生于人们的活动并由其维持。因此，它在行动过程中不断地被重新协商和重新定义。这些研究为我们提供了与上下文中的移动计算特别相关的额外上下文因素，并让我们意识到，定义上下文的因素本身就取决于上下文。

移动计算的上下文是移动交互设计中多个独立学科共同关注的问题，它影响了该领域内部及跨学科边界的方法论、技术和理论的塑造。这些不同的学科对上下文挑战的应对方式各异，并产生了不同类型的响应。

在移动计算的领域研究（Domain Studies）中，上下文作为被审查的核心现象扮演着显而易见的中心角色。其挑战一方面在于从理论上理解什么是使用上下文以及如何描述它们，另一方面在于通过实证研究探讨特定感兴趣的使用上下文的特征，以及如何通过能够产生此类理解的方式来研究和分析上下文现象。这产生了一系列主要基于社会学、人类学和 [现象学（Phenomenology）](https://www.interaction-design.org/literature/topics/phenomenology) 方法和理论的理论及社会技术研究（Socio-technical Research）（例如 Luff and Heath 1998, Dourish 2001, Dourish 2004, Dey 2001, Ling 2001, Perry et al. 2001, Fortunati 2001, Green et al. 2001, Agre 2001, McCullough 2004, Chalmers 2004, Aoki et al. 2009, Kostakos et al. 2009），以及我自己在该领域的工作（Paay and Kjeldskov 2005, Paay and Kjeldskov 2008a, Kjeldskov et al. 2004, Kjeldskov and Stage 2006）。

在移动计算的系统开发和设计中，上下文的挑战主要在于如何创建系统与上下文之间的适当适配（Appropriate Fit），以及如何通过新的或改进的系统开发和设计方法在结构上支持这种适配。虽然关于这个话题的公开出版物相对较少，但目前出现了一批主要基于信息系统、软件工程和人机交互方法与理论的方法论研究（例如 Sharples et al. 2002, Mikkonen et al. 2002, Hosbond 2005, Paay 2008, de Sá and Carrico 2009, Paay et al. 2009a），以及我自己的工作（Kjeldskov and Howard 2004, Paay et al. 2009b, Vetere et al. 2005, Kjeldskov and Stage 2012）。

在移动计算的可用性评估（Usability Evaluation）中，上下文的挑战主要在于理解它与实证结果的范围、丰富度和有效性之间的关系，以及如何通过使用新的或改进的方法和技术，在具有上下文真实性的设置中进行可用性测试。这导致了大量基于可用性工程（Usability Engineering）方法和理论的实证研究的增加。这些研究包括（例如 Brewster 2002, Betiol and Cybis 2005, Hagen et al. 2005, Kaikkonen et al. 2005, Nielsen et al. 2006, Rogers et al. 2007, Reichl et al. 2007, Oulasvirta 2009, Oulasvirta and Nyyssonen 2009, de Sá and Carrico 2010），以及我的贡献（Kjeldskov and Stage 2004, Kjeldskov et al. 2004, Kjeldskov et al. 2005, Kjeldskov and Skov 2007a, Høegh et al. 2008）。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_11.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

**图 9.11：在上下文中评估移动计算**

在移动计算的实现中，上下文的挑战主要在于如何在计算数据模型中捕获、形式化（Formalizing）和建模这一属性，如何从这些模型中获取意义，以及如何利用它们构建能够响应周围环境的 *上下文感知（Context-aware）* 移动系统。这产生了一系列广泛的、主要基于计算机科学方法和理论的技术研究（例如 Schilit and Theimer 1994, Crabtree and Rhodes 1998, Schmidt et al. 1999a, Schimdt et al. 1999b, Cheverst et al. 2001, Dix et al. 2000, Chen and Kotz 2000, Hinckley and Horvitz 2001, Dey 2001, Jameson 2001, Jones et al. 2004, Edwards 2005, Hinckley et al. 2005），以及我的贡献（Kjeldskov and Skov 2007b, Kjeldskov and Paay 2005, Kjeldskov and Paay 2006, Kjeldskov et al. 2010, Skov et al. 2012, Kjeldskov et al. 2012）。

在移动计算的用户体验（User Experience, UX）研究中，上下文的挑战在于理解丰富且动态的用户上下文如何影响人们使用技术的体验，并描述如何改善这种用户体验。这产生了一系列基于社会学、心理学、认知科学、计算机科学、人机交互以及计算机支持的协同工作（Computer-Supported Cooperative Work）等广泛学科方法和理论的理论、概念和设计导向研究。这些研究包括（例如 Abowd and Mynatt 2000, Cheverst et al. 2001, Palen et al. 2000, Weilenmann 2001, Bradley and Dunlop 2002, Brown and Randell 2004, Little and Briggs 2009, Benford et al. 2009, Karapanos et al. 2009, Lindley et al. 2009, Rowland et al. 2009），以及我的贡献（Paay and Kjeldskov 2008b, Kjeldskov and Paay 2010, O’Hara et al. 2011, Murphy et al. 2005）。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_12_1.jpg)

作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_12_2.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_12_3.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_12_4.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_12_5.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

**图 9.12**：使用格式塔理论（Gestalt Theory）的五个知觉组织（Perceptual Organisation）原则来解释上下文中的移动用户体验 (Paay and Kjeldskov 2008b)

这并不是说上下文是一个随着 *移动* 计算的出现才进入研究议程的新现象。事实上，自人机交互的 *第二波（Second Wave）* 或 *范式（Paradigm）* 以来，上下文一直是人机交互和交互设计中的一个重要概念（Bødker 2006, Harrison et al. 2007）。第一波 HCI 是工程学和人因工程的结合，专注于优化人机适配（Human-machine Fit）。第二波主要基于认知科学，专注于机器和人类思维中信息的同步处理，但这也涉及对工作场所上下文中交互式计算系统使用的强烈关注。然而，正如 Bødker (2006) 所指出的，虽然在第二波 HCI 中关于复杂的上下文概念有很多讨论，但在将其定义并操作化（Operationalising）为对 HCI 和交互设计具有实际显著价值的方式方面，这些研究取得的成果很少。在 *第三波* 中，关注点进一步扩大到后 PC 时代的普适与泛在信息社会（Ubiquitous and Pervasive Information Society），计算机技术已经从“工作场所扩展到我们的家庭、日常生活和文化中”（Bødker 2006）。这意味着上下文现在是一个 *基础性（Elemental）* 概念，我们不仅需要对其进行良好的 *定义*，还需要在复杂性、重要性以及对人们使用技术体验的影响方面更好地 *理解* 它，以便更好地指导技术设计。

移动交互设计处于 HCI 的第二波和第三波之间。它成长于第二波，但随后普通大众对移动计算的巨大接纳，通过启用我们今天在全球范围内见证的一些全新的计算技术使用潜力和模式，成为了推动第三波创建、增强其力量和速度的促成因素。

### 9.3.2 研究对实践的影响

此前预想的移动计算（mobile computing）的大部分未来影响，将由具有创业精神的开发人员和设计师通过巧妙且富有创造力的移动交互（mobile interactions）设计来驱动。这些从业者深谙如何创造出符合用户需求、欲望以及[使用情境（contexts of use）](https://www.interaction-design.org/literature/topics/contexts-of-use)的实用且愉悦的效用（utility）与用户体验（user experience）。然而遗憾的是，目前基于研究的移动交互设计文献，既未能为这些开发人员和设计师在进行创新和交互设计时提供足够的理论基础，也未能就如何开展设计过程提供多少方法论指导。虽然关于桌面应用程序和网站的[用户界面（user interface）](https://www.interaction-design.org/literature/topics/ui-design)和交互设计（interaction design）已有大量基于研究的著作，但关于移动交互设计的对等文献仍然匮乏。尽管移动计算已有约三十年的历史，且交互设计在其中约三分之二的时间里扮演了重要角色，但迄今为止，该领域仅出版了一本优秀的通用教科书，即 Jones and Marsden (2006) 的著作。虽然这本书确实是应对*移动*交互设计特定挑战的绝佳起点，但其完整性和深度仍不及同类的人机交互（human-computer interaction）和交互设计入门教材，例如 Laurel (1990), Shneiderman (1997), Preece et al. (1994), Winograd (1996), Raskin (2000), Dix et al. (2004), Benyon et al. (2005), Lauesen (2005), Bagnara and Smith (2006), Preece et al. (2002), 以及 Rogers et al. (2011)。考虑到过去十五年里该领域已开展了大量优秀的交互设计研究，这在很大程度上意味着移动交互设计*实践*错失了一个实现大规模现实影响的机会。虽然这可能表明移动交互设计领域尚未稳定到足以演化出通用指南、原则、方法和技术的程度，但同时也表明了一个机会和需求，即需要进一步推动此类基础性工作的开发。

在现有的关于移动设备、系统和服务交互设计的几本教科书中，如 Helal et al. (1998), Weiss (2002), Ballard (2007), Fling (2009) 以及 Frederick and Lal (2010)，其核心目标基本上是针对特定且非常具体的设备类别和软件平台的应用开发，并解决了瞬时的技术限制（ephemeral technical limitations），例如特定的操作系统、低屏幕分辨率、处理能力不足、内存有限以及带宽较低等问题。虽然在针对这些具体平台进行设计时，这些著作无疑非常有用，但此类作品的弱点在于它们*过于*实用。它们极易受到技术进步的影响，因此随着新设备和新平台的出现而迅速失效。结果，它们通常最终变成了与特定时间点绑定的、生命周期短且过于具体的用户界面指南，而非具有普适性和永恒性的交互设计原则。提炼这些作品的精华——即适用于特定设备和平台之外的高层挑战与解决方案——将有助于推动移动交互设计领域的发展。但此类工作尚未得到系统且深入的开展。

![](https://public-media.interaction-design.org/images/encyclopedia/mobile_computing/figure_13.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。
**图 9.13**：部分建议阅读书目

不过，作为朝着正确方向迈出的一步，另一类移动交互设计教科书是对成功且具有影响力的设计方案进行类似案例研究（case study）的叙述，例如 Eric Bergman 的 “Information Appliances and Beyond” (Bergman 2000), Lindholm and Keinonen 的 “Mobile Usability: how Nokia changed the face of the mobile phone” (Lindholm and Keinonen 2003), Bill Moggridge 的 “Designing Interactions” (Moggridge 2007) 的部分章节，以及 Bondo et al 的 “iPhone User Interface Design Projects” (Bondo et al. 2009)。这些著作旨在捕捉从实际移动交互设计师经验中学习到的具有普适重要性的教训。它们提供了关于影响力方案及其产生过程的交互设计洞察和方法论洞察。然而，*这些*作品的潜在弱点在于，它们很容易变成轶事性的（anecdotal）描述，难以迁移到当下的设计挑战中。为了支持这种知识的迁移与升华，我们不仅需要提供案例研究的叙述，还需要对这些案例进行跨案例分析，从而将我们的学习从具体且特定的层面提升到抽象且普适的层面。

## 9.4 前行之路：迈向数字生态

那么，我们接下来的方向是什么？正如我此前所讨论的，移动计算领域目前出现的一种趋势是创建数字生态系统（digital ecosystems），在这种视角下，交互式移动系统和设备不再被视为孤立的个体，而更多地被视为更广泛的使用情境（use contexts）或人造物生态（artefact ecologies）的一部分（例如，参见 Jung et al. 2008, Bødker and Klokmose 2011）。在我看来，这是一个极具吸引力的进一步研究和设计的途径，也是我个人期待深入参与的方向。

作为起点，我认为我们需要开发能够更广泛地关注“整体”的交互设计方法，并且这些方法应具备一种内在的敏感性，以应对此类生态系统和生态中系统及其情境持续出现（emergence）和融合（convergence）的特性。当代的交互式移动系统、服务和设备已成为我们深切关注的普适计算（ubiquitous computing）环境不可或缺的一部分。然而，尽管我们在将这些设备与大量其他计算技术协同编排时，其外观、触感和功能会影响我们的日常生活，但这些人造物和生态系统无法通过传统的以用户为中心的设计（user-centred design）和可用性工程（usability engineering）方法得到充分的理解或创建。与传统的 IT 人造物不同，它们构成了具有价值和愉悦感的整体用户体验（holistic user experiences），这要求我们密切关注其使用的多样性、复杂性和动态性。因此，我们需要进一步开发理论和概念视角，以便我们能够以一种能够启发设计和深化思考的方式，来观察、处理和描述这一新兴现象。这项工作可以从近年来出现的一些概念性更强、技术性较低的普适计算和泛在计算（pervasive computing）文献中寻找灵感和动力，例如 Adam Greenfield 的著作 *“Everyware”* (Greenfield 2006)。

为了概括和定义这项工作，我建议使用并发展“数字生态（digital ecology）”这一术语。生态学是对构成生态系统的元素的研究，广义上是指理解生物与其环境之间的相互作用。它具有内在的整体性（holistic）和跨学科性质，且并不等同于“环境”或“环保主义”。生态思维也不局限于生物学领域。例如，“工业生态学（industrial ecology）”研究工业过程网络中的物质和能量流，而“人类生态学（human ecology）”则是一个跨学科研究领域，为理解和研究人类社会交互提供了框架。同样地，我认为“数字生态”可能是描述数字生态系统构成元素的研究，以及对这些元素与其环境之间相互作用的整体性理解的一种有效方式。因此，数字生态是指对相互关联的数字系统（例如移动计算和泛在计算）及其工作和交互过程，以及这些系统的构思、出现、融合和演进过程的研究。它旨在理解我们周围数字生态系统和人造物生态的功能、使用和体验，以及创建和推进它们的设计过程。

## 9.5 更多学习资源

有多种在线资源可供获取更多信息。部分资源免费，而另一些则需要订阅或通过已订阅大学的网络访问。

### 9.5.1 会议

Mobile HCI 系列会议是获取更多信息的核心渠道。该系列会议的论文集（Proceedings）可通过 Springer 和 ACM 以电子形式获取。该系列会议的发起人之一 Mark Dunlop 维护了一个关于该会议的通用页面 [on the conference](http://all.mobilehci.org/)，此外，Wikipedia 上的页面 [http://en.wikipedia.org/wiki/MobileHCI](http://en.wikipedia.org/wiki/MobileHCI) 也是一个值得访问的入口。

此外，ACM CHI 系列会议的论文集中包含大量关于移动计算系统人机交互（Human-Computer Interaction, HCI）的文章。这些论文集可通过 [http://dl.acm.org/](http://dl.acm.org/) 访问。

除此之外，浏览 [UbiComp conference series](http://www.ubicomp.org/ubicomp2012/)、[MobiCom conference series](http://www.sigmobile.org/mobicom/) 以及 [Pervasive conference series](http://pervasiveconference.org/)) 的论文集也具有很高的价值。

### 9.5.2 期刊

许多人机交互（Human-Computer Interaction, HCI）领域的期刊都发表过关于移动计算（Mobile Computing）的文章。其中专注于该主题的期刊包括：
- [*Personal and Ubiquitous Computing*](http://www.springer.com/computer/hci/journal/779)
- [Pervasive and Mobile Computing](http://www.journals.elsevier.com/pervasive-and-mobile-computing/)
- [*International Journal of Mobile Human Computer Interaction*](http://www.igi-global.com/journal/international-journal-mobile-human-computer/1126)

### 9.5.3 推荐阅读

在下方的参考文献（References）中，我特别推荐以下文章和书籍。

- Atkinson, P. (2005) Man in a Briefcase - The Social Construction of the Laptop Computer and the Emergence of a Type Form. *Journal of *[*Design History*](https://www.interaction-design.org/literature/topics/design-history)*,* 18(2), 191-205.
- Bergman E. (Ed.) (2000) *Information Appliances and Beyond*. San Francisco: Morgan Kaufmann Publishers.
- Greenfield, A. (2006) *Everyware: the dawning age of ubiquitous computing.* Berkeley: New Riders.
- Hinckley, K., Pierce, J., Sinclair, M. and Horvitz, E. (2000) Sensing techniques for mobile interaction. In *Proceedings of UIST 2000* (pp. 91-100). New York: ACM.
- Johnson, P. (1998) Usability and Mobility; Interactions on the move. In *Proceedings of the First Workshop on Human-Computer Interaction with Mobile Devices*, Glasgow, Scotland (GIST Technical Report G98-1).
- Jones, M. and Marsden, G. (2006) *Mobile Interaction Design.* Glasgow: John Wiley and Sons, Ltd.
- Kay, Alan (1972). A Personal Computer for Children of All Ages. In *Proceedings of ACM National Conference*. Boston: New York: ACM.
- Paay, J., (2008) From ethnography to interface design. In J. Lumsden (Ed.), *Handbook of Research on User Interface Design and Evaluation for Mobile Technology* (pp. 1-15). PA, USA: Idea Group Inc (IGI).

- Perry, M., O'Hara, K., Sellen, A., Brown, B. and Harper, R. (2001) 处理移动性（Mobility）：理解随时随地的访问。*ACM Transactions on Computer-Human Interaction, 8*(4), 323-347.
- Rogers, Y., Connelly, K., Tedesco, L., Hazlewood, W., Kurtz, A., Hall, R. E., Hursey, J. and Toscos, T. (2007) 为什么值得如此费力：在设计普适计算（Ubicomp）时原位研究（in-situ studies）的价值。In *Proceedings UbiComp 2007*, LNCS (pp. 336-353). Berlin: Springer-Verlag.
- Weiser, M. (1991) 21世纪的计算机。*Scientific American, 265*(3), 94-104.

### 9.5.4 基于我个人相关出版物的推荐

可在 [people.cs.aau.dk/~jesper/](http://people.cs.aau.dk/~jesper/) 获取
- Kjeldskov J. (2012) Designing mobile interactions — the continual convergence of form and context. Volume 1 and 2 (forthcoming) [移动交互设计——形式与上下文（Context）的持续融合。第1卷和第2卷（即将出版）]
- Kjeldskov, J., Skov, M. B., Nielsen, G. W., Thorup, S. and Vestergaard, M. (2012)
Digital Urban Ambience: Mediating Context on Mobile Devices in the City. *Journal of Pervasive and Mobile Computing* (in press). [数字城市氛围：在城市移动设备上对上下文进行中介。*Journal of Pervasive and Mobile Computing*（出版中）]
- Kjeldskov J., Cheverst K., de Sá M., Jones M., and Murray -Smith R. (2012)
Research Methods in Mobile HCI: Trends and Opportunities. *Proceedings of Mobile HCI 2012 (vol. 2),* September 21-24, San Francisco, USA. ACM Press, pp. 255-260. [移动人机交互（Mobile HCI）研究方法：趋势与机遇。*Proceedings of Mobile HCI 2012 (vol. 2)*]
- Kjeldskov J. and Paay J (2012) A longitudinal review of Mobile HCI research Methods. *Proceedings of Mobile HCI 2012,* September 21-24, San Francisco, USA. ACM Press, pp. 69-78. [移动人机交互研究方法的纵向综述（Longitudinal review）。*Proceedings of Mobile HCI 2012*]
- Kjeldskov, J. and Paay, J. (2010) Indexicality: understanding mobile human-computer interaction in context. *ACM Transactions on Computer-Human Interaction (TOCHI). 17*(4) [指示性（Indexicality）：在上下文中理解移动人机交互。*ACM Transactions on Computer-Human Interaction (TOCHI)*]

- Kjeldskov, J. and Paay, J. (2006) Public Pervasive Computing in the City: Making the Invisible Visible. *IEEE Computer, 39*(9), 60-65. [城市中的公共普适计算（Pervasive Computing）：让不可见变为可见。*IEEE Computer*]
- Kjeldskov, J. and Paay, J. (2005) Just-for-Us: A Context-Aware Mobile Information System Facilitating Sociality. In *Proceedings of Mobile HCI 2005*, Salzburg, Austria (pp. 23-30). New York: ACM. [Just-for-Us：一个促进社交的上下文感知（Context-Aware）移动信息系统。*Proceedings of Mobile HCI 2005*]
- Kjeldskov, J., Graham, C., Pedell, S., Vetere, F., Howard, S., Balbo, S. and
Davies, J. (2005) Evaluating the Usability of a Mobile Guide: The
influence of Location, Participants and Resources. *Behaviour and Information Technology, 24*(1), 51-65. [移动导览系统的可用性（Usability）评估：位置、参与者和资源的影响。*Behaviour and Information Technology*]
- Kjeldskov, J., Skov, M. B., Als, B. S. and Høegh, R. T. (2004a) Is it Worth the
Hassle? Exploring the Added Value of Evaluating the Usability of
Context-Aware Mobile Systems in the Field. In *Proceedings of MobileHCI 2004*, Glasgow, Scotland, LNCS (pp. 61-73). Berlin: Springer-Verlag. [值得如此费力吗？探讨在实地（In the Field）评估上下文感知移动系统可用性的附加价值。*Proceedings of MobileHCI 2004*]
- Kjeldskov, J. and Stage, J. (2004) New Techniques for Usability Evaluation of Mobile Systems. *International Journal of Human-Computer Studies, 60*(2004), 599-620. [移动系统可用性评估的新技术。*International Journal of Human-Computer Studies*]

- Kjeldskov, J. and Graham, C. (2003) A Review of MobileHCI Research Methods. In *Proceedings of the 5th International Mobile HCI 2003 conference*, Udine, Italy, LNCS (pp. 317-335). Berlin: Springer-Verlag. [移动人机交互研究方法综述。*Proceedings of the 5th International Mobile HCI 2003 conference*]
- Paay, J., Kjeldskov, J., Howard S. and Dave, B. (2009) Out on the town: a
socio-physical approach to the design of a context aware urban guide. *Transactions on Computer-Human Interaction, 16*(2), 7-34. [走进城市：一种设计上下文感知城市导览的社会-物理方法（Socio-physical approach）。*Transactions on Computer-Human Interaction*]
- Paay, J. and Kjeldskov, J. (2008) Understanding the user experience of
location based services: five principles of perceptual organization
applied. *Journal of Location-Based Services, 2*(4), 267-286 [理解基于位置的服务（Location Based Services, LBS）的用户体验（User Experience）：感知组织五原则的应用。*Journal of Location-Based Services*]

## 9.6 References

[Abowd](https://www.interaction-design.org/references/authors/gregory_d__abowd.html), Gregory D. and [Mynatt](https://www.interaction-design.org/references/authors/elizabeth_d__mynatt.html), Elizabeth D. (2000): *Charting Past, Present, and Future Research in Ubiquitous Computing*. In [ACM Transactions on Computer-Human Interaction](https://www.interaction-design.org/references/periodicals/acm_transactions_on_computer-human_interaction.html), 7 (1) pp. 29-58
[Agre](https://www.interaction-design.org/references/authors/philip_e__agre.html), Philip E. (2001): *Changing Places: Contexts of Awareness in Computing*. In [Human-Computer Interaction](https://www.interaction-design.org/references/periodicals/human-computer_interaction.html), 16 (2) pp. 177-192

[Aoki](https://www.interaction-design.org/references/authors/paul_m__aoki.html), Paul M., [Honicky](https://www.interaction-design.org/references/authors/r__j__honicky.html), R. J., [Mainwaring](https://www.interaction-design.org/references/authors/alan_mainwaring.html), Alan, [Myers](https://www.interaction-design.org/references/authors/chris_myers.html), Chris, [Paulos](https://www.interaction-design.org/references/authors/eric_paulos.html), Eric, [Subramanian](https://www.interaction-design.org/references/authors/sushmita_subramanian.html), Sushmita and [Woodruff](https://www.interaction-design.org/references/authors/allison_woodruff.html), Allison (2009): A vehicle for research: using street sweepers to explore the landscape of environmental community action. In: [Proceedings of ACM CHI 2009 Conference on Human Factors in Computing Systems](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2009_conference_on_human_factors_in_computing_systems.html)2009. pp. 375-384
[Atkinson](https://www.interaction-design.org/references/authors/p__atkinson.html), P. (2005): *Man in a briefcase: the social construction of the laptop computer and the emergence of a type form*. In [Journal of Design History](https://www.interaction-design.org/references/periodicals/journal_of_design_history.html), 18 (2) pp. 191-205

[Bagnara](https://www.interaction-design.org/references/authors/sebastiano_bagnara.html), Sebastiano and [Smith](https://www.interaction-design.org/references/authors/gillian_crampton_smith.html), Gillian Crampton (2006): *Theories and Practice in Interaction Design (Human Factors and Ergonomics Series).* Lawrence Erlbaum Associates
[Balakrishnan](https://www.interaction-design.org/references/authors/ravin_balakrishnan.html), Ravin, [Fitzmaurice](https://www.interaction-design.org/references/authors/george_w__fitzmaurice.html), George W., [Kurtenbach](https://www.interaction-design.org/references/authors/gordon_kurtenbach.html), Gordon and [Singh](https://www.interaction-design.org/references/authors/karan_singh.html), Karan (1999): Exploring interactive curve and surface manipulation using a bend and twist sensitive input strip. In: [SI3D 1999](https://www.interaction-design.org/references/conferences/si3d_1999.html) 1999. pp. 111-118
[Ballard](https://www.interaction-design.org/references/authors/barbara_ballard.html), Barbara (2007): *Designing the Mobile User Experience.* Wiley

[Benford](https://www.interaction-design.org/references/authors/steve_benford.html), Steve, [Giannachi](https://www.interaction-design.org/references/authors/gabriella_giannachi.html), Gabriella, [Koleva](https://www.interaction-design.org/references/authors/boriana_koleva.html), Boriana and [Rodden](https://www.interaction-design.org/references/authors/tom_rodden.html), Tom (2009): From interaction to trajectories: designing coherent journeys through user experiences. In: [Proceedings of ACM CHI 2009 Conference on Human Factors in Computing Systems](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2009_conference_on_human_factors_in_computing_systems.html) 2009. pp. 709-718
[Benyon](https://www.interaction-design.org/references/authors/david_benyon.html), David, [Turner](https://www.interaction-design.org/references/authors/phil_turner.html), Phil and [Turner](https://www.interaction-design.org/references/authors/susan_turner.html), Susan (2005): *Designing interactive systems : people, activities, contexts, technologies.* Addison-Wesley
[Bergman](https://www.interaction-design.org/references/authors/eric_bergman.html), Eric (2000): *Information Appliances and Beyond: Interaction Design for Consumer Products (Interactive Technologies).* Morgan Kaufmann

[Bergman](https://www.interaction-design.org/references/authors/eric_bergman.html), Eric and [Haitani](https://www.interaction-design.org/references/authors/rob_haitani.html), Rob (2000): Designing the PalmPilot: a Conversation with Rob Haitani. In: [Bergman](https://www.interaction-design.org/references/authors/eric_bergman.html),
 Eric (ed.). "Information Appliances and Beyond: Interaction Design for 
Consumer Products (Interactive Technologies)". Morgan Kaufmann
[Betiol](https://www.interaction-design.org/references/authors/a__h__betiol.html), A. H. and [Cybis](https://www.interaction-design.org/references/authors/w__de_abreu_cybis.html), W. de Abreu (2005): [Usability Testing](https://www.interaction-design.org/literature/topics/usability-testing) of Mobile Devices: A Comparison of Three Approaches. In: [Proceedings of IFIP INTERACT05: Human-Computer Interaction](https://www.interaction-design.org/references/conferences/proceedings_of_ifip_interact05-_human-computer_interaction.html) 2005. pp. 470-481

[Bondo](https://www.interaction-design.org/references/authors/joachim_bondo.html), Joachim, [Barnard](https://www.interaction-design.org/references/authors/david_barnard.html), David, [Wilson](https://www.interaction-design.org/references/authors/eddie_wilson.html), Eddie, [Peters](https://www.interaction-design.org/references/authors/keith_peters.html), Keith, [Kemper](https://www.interaction-design.org/references/authors/craig_kemper.html), Craig, [Burcaw](https://www.interaction-design.org/references/authors/dan_burcaw.html), Dan, [Novikoff](https://www.interaction-design.org/references/authors/tim_novikoff.html), Tim and[Parrish](https://www.interaction-design.org/references/authors/chris_parrish.html), Chris (2009): *iPhone User Interface Design Projects.* Apress
[Bradley](https://www.interaction-design.org/references/authors/nicholas_a__bradley.html), Nicholas A. and [Dunlop](https://www.interaction-design.org/references/authors/mark_d__dunlop.html), Mark D. (2002): Understanding Contextual Interactions to Design Navigational Context-Aware Applications. In: [Paterno](https://www.interaction-design.org/references/authors/fabio_paterno.html), Fabio (ed.) [Mobile Human-Computer Interaction - 4th International Symposium - Mobile HCI 2002](https://www.interaction-design.org/references/conferences/mobile_human-computer_interaction_-_4th_international_symposium_-_mobile_hci_2002.html) September 18-20, 2002, Pisa, Italy. pp. 349-353

[Brewster](https://www.interaction-design.org/references/authors/stephen_a__brewster.html), Stephen A. (2002): *Overcoming the Lack of Screen Space on Mobile Computers*. In [Personal and Ubiquitous Computing](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing.html), 6 (3) pp. 188-205
[Brown](https://www.interaction-design.org/references/authors/barry_brown.html), Barry (2004): *Building a Context Sensitive Telephone: Some Hopes and Pitfalls for Context Sensitive Computing*. In [Computer Supported Cooperative Work](https://www.interaction-design.org/references/periodicals/computer_supported_cooperative_work.html), 13 (3) pp. 329-345

[Brown](https://www.interaction-design.org/references/authors/barry_brown.html), Barry, [Sellen](https://www.interaction-design.org/references/authors/abigail_sellen.html), Abigail and [O'Hara](https://www.interaction-design.org/references/authors/kenton_p__o%27hara.html), Kenton P. (2000): A Diary Study of Information Capture in Working Life. In: [Turner](https://www.interaction-design.org/references/authors/thea_turner.html), Thea, [Szwillus](https://www.interaction-design.org/references/authors/gerd_szwillus.html), Gerd, [Czerwinski](https://www.interaction-design.org/references/authors/mary_czerwinski.html), Mary, [Peterno](https://www.interaction-design.org/references/authors/fabio_peterno.html), Fabio and [Pemberton](https://www.interaction-design.org/references/authors/steven_pemberton.html), Steven (eds.) [Proceedings of the ACM CHI 2000 Human Factors in Computing Systems Conference](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_2000_human_factors_in_computing_systems_conference.html) April 1-6, 2000, The Hague, The Netherlands. pp. 438-445
[Buxton](https://www.interaction-design.org/references/authors/bill_buxton.html), Bill (2001): Less is More (More or Less): Uncommon Sense and the Design of Computers. In: [Denning](https://www.interaction-design.org/references/authors/peter_j__denning.html), Peter J. (ed.). "The Invisible Future: The Seamless Integration of Technology Into Everyday Life". McGraw-Hill Companies

[Bødker](https://www.interaction-design.org/references/authors/susanne_b%F8dker.html), Susanne (2006): When second wave HCI meets third wave challenges. In: [Proceedings of the Fourth Nordic Conference on Human-Computer Interaction](https://www.interaction-design.org/references/conferences/proceedings_of_the_fourth_nordic_conference_on_human-computer_interaction.html) 2006. pp. 1-8
[Bødker](https://www.interaction-design.org/references/authors/susanne_b%F8dker.html), Susanne (2006): When second wave HCI meets third wave challenges. In: [Mørch](https://www.interaction-design.org/references/authors/anders_m%F8rch.html), Anders, [Morgan](https://www.interaction-design.org/references/authors/konrad_morgan.html), Konrad,[Bratteteig](https://www.interaction-design.org/references/authors/tone_bratteteig.html), Tone, [Ghosh](https://www.interaction-design.org/references/authors/gautam_ghosh.html), Gautam and [Svanaes](https://www.interaction-design.org/references/authors/dag_svanaes.html), Dag (eds.) [NordiCHI Nordic Conference on Human-Computer Interaction](https://www.interaction-design.org/references/conferences/nordichi_nordic_conference_on_human-computer_interaction.html) October 14-18, 2006, Oslo, Norway. pp. 1-8

[Bødker](https://www.interaction-design.org/references/authors/susanne_b%F8dker.html), Susanne and [Klokmose](https://www.interaction-design.org/references/authors/clemens_n__klokmose.html), Clemens N. (2011): *The Human-Artifact Model: An Activity Theoretical Approach to Artifact Ecologies*. In [Human–Computer Interaction](https://www.interaction-design.org/references/periodicals/human%96computer_interaction.html), 26 (4) pp. 315-371
[Chalmers](https://www.interaction-design.org/references/authors/matthew_chalmers.html), Matthew (2004): *A Historical View of Context*. In [Computer Supported Cooperative Work](https://www.interaction-design.org/references/periodicals/computer_supported_cooperative_work.html), 13 (3) pp. 223-247
[Chen](https://www.interaction-design.org/references/authors/brian_x__chen.html), Brian X. (2010). *What the iPad means for the future of computing*. Retrieved 8 November 2012 from wired.com: [http://www.wired.com/gadgetlab/2010/02/ipad-future...](http://www.wired.com/gadgetlab/2010/02/ipad-future/)
[Chen](https://www.interaction-design.org/references/authors/guanling_chen.html), Guanling and [Kotz](https://www.interaction-design.org/references/authors/david_kotz.html), David (2000). *A survey of context-aware mobile computing research*. Dartmouth College Hanover [http://dl.acm.org/citation.cfm?id=867843](http://dl.acm.org/citation.cfm?id=867843)

[Cheverst](https://www.interaction-design.org/references/authors/keith_cheverst.html), Keith, [Davies](https://www.interaction-design.org/references/authors/nigel_davies.html), Nigel, [Mitchell](https://www.interaction-design.org/references/authors/keith_mitchell.html), Keith, [Friday](https://www.interaction-design.org/references/authors/adrian_friday.html), Adrian and [Efstratiou](https://www.interaction-design.org/references/authors/christos_efstratiou.html), Christos (2000): Developing a Context-Aware Electronic Tourist Guide: Some Issues and Experiences. In: [Turner](https://www.interaction-design.org/references/authors/thea_turner.html), Thea, [Szwillus](https://www.interaction-design.org/references/authors/gerd_szwillus.html), Gerd, [Czerwinski](https://www.interaction-design.org/references/authors/mary_czerwinski.html), Mary, [Peterno](https://www.interaction-design.org/references/authors/fabio_peterno.html), Fabio and [Pemberton](https://www.interaction-design.org/references/authors/steven_pemberton.html), Steven (eds.) [Proceedings of the ACM CHI 2000 Human Factors in Computing Systems Conference](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_2000_human_factors_in_computing_systems_conference.html) April 1-6, 2000, The Hague, The Netherlands. pp. 17-24

[Cheverst](https://www.interaction-design.org/references/authors/keith_cheverst.html), Keith, [Davies](https://www.interaction-design.org/references/authors/nigel_davies.html), Nigel, [Mitchell](https://www.interaction-design.org/references/authors/keith_mitchell.html), Keith and [Efstratiou](https://www.interaction-design.org/references/authors/christos_efstratiou.html), Christos (2001): *Using Context as a Crystal Ball: Rewards and Pitfalls*. In [Personal and Ubiquitous Computing](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing.html), 5 (1) pp. 8-11
[Crabtree](https://www.interaction-design.org/references/authors/isac_b__crabtree.html), Isac B. and [Rhodes](https://www.interaction-design.org/references/authors/bradley_j__rhodes.html), Bradley J. (1998): *Wearable Computing and the Remembrance Agent*. In [BT Technology Journal](https://www.interaction-design.org/references/periodicals/bt_technology_journal.html), 16 (3) pp. 118-124

[de Sá](https://www.interaction-design.org/references/authors/marco_de_s%E1.html), Marco and [Carrico](https://www.interaction-design.org/references/authors/luis_carrico.html), Luis (2009): A mobile tool for in-situ [prototyping](https://www.interaction-design.org/literature/topics/prototyping). In: [Proceedings of 11th Conference on Human-computer interaction with mobile devices and services](https://www.interaction-design.org/references/conferences/proceedings_of_11th_conference_on_human-computer_interaction_with_mobile_devices_and_services.html) 2009. p. 20
[Dey](https://www.interaction-design.org/references/authors/anind_k__dey.html), Anind K. (2001): *Understanding and Using Context*. In [Personal and Ubiquitous Computing](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing.html), 5 (1) pp. 4-7

[Dix](https://www.interaction-design.org/references/authors/alan_j__dix.html), Alan J., [Rodden](https://www.interaction-design.org/references/authors/tom_rodden.html), Tom, [Davies](https://www.interaction-design.org/references/authors/nigel_davies.html), Nigel, [Trevor](https://www.interaction-design.org/references/authors/jonathan_trevor.html), Jonathan, [Friday](https://www.interaction-design.org/references/authors/adrian_friday.html), Adrian and [Palfreyman](https://www.interaction-design.org/references/authors/kevin_palfreyman.html), Kevin (2000):*Exploiting Space and Location as a Design Framework for Interactive Mobile Systems*. In [ACM Transactions on Computer-Human Interaction](https://www.interaction-design.org/references/periodicals/acm_transactions_on_computer-human_interaction.html), 7 (3) pp. 285-321
[Dix](https://www.interaction-design.org/references/authors/alan_j__dix.html), Alan J., [Finlay](https://www.interaction-design.org/references/authors/janet_e__finlay.html), Janet E., [Abowd](https://www.interaction-design.org/references/authors/gregory_d__abowd.html), Gregory D. and [Beale](https://www.interaction-design.org/references/authors/russell_beale.html), Russell (2004): *Human-Computer Interaction (3rd Edition).* Prentice Hall

[Dourish](https://www.interaction-design.org/references/authors/paul_dourish.html), Paul (2004): *What we talk about when we talk about context*. In [Personal and Ubiquitous Computing](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing.html), 8 (1) pp. 19-30
[Dourish](https://www.interaction-design.org/references/authors/paul_dourish.html), Paul (2001): *Seeking a Foundation for Context-Aware Computing*. In [Human-Computer Interaction](https://www.interaction-design.org/references/periodicals/human-computer_interaction.html), 16 (2) pp. 229-241
[Edwards](https://www.interaction-design.org/references/authors/w__keith_edwards.html), W. Keith (2005): *Putting computing in context: An infrastructure to support extensible context-enhanced collaborative applications*. In [ACM Trans. Comput.-Hum. Interact.](https://www.interaction-design.org/references/periodicals/acm_trans__comput-dot--hum__interact-dot-.html), 12 (4) pp. 446-474

[Feiner](https://www.interaction-design.org/references/authors/steven_k__feiner.html), Steven K., [MacIntyre](https://www.interaction-design.org/references/authors/blair_macintyre.html), Blair and [Seligmann](https://www.interaction-design.org/references/authors/doree_duncan_seligmann.html), Doree Duncan (1992): Annotating the real world with knowledge--based graphics on a see--through head--mounted display. In: [Graphics Interface 92](https://www.interaction-design.org/references/conferences/graphics_interface_92.html) May 11-15, 1992, Vancouver, British Columbia, Canada. pp. 78-85
[Fling](https://www.interaction-design.org/references/authors/brian_fling.html), Brian (2009): *Mobile Design and Development: Practical concepts and techniques for creating mobile sites and web apps (Animal Guide).* OReilly Media
[Fortunati](https://www.interaction-design.org/references/authors/leopoldina_fortunati.html), Leopoldina (2001): *The Mobile Phone: An Identity on the Move*. In [Personal and Ubiquitous Computing](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing.html), 5 (2) pp. 85-98
[Frederick](https://www.interaction-design.org/references/authors/gail_frederick.html), Gail and [Lal](https://www.interaction-design.org/references/authors/rajesh_lal.html), Rajesh (2010): *Beginning
 Smartphone Web Development: Building JavaScript, CSS, HTML and 
Ajax-based Applications for iPhone, Android, Palm Pre, BlackBerry,

Windows Mobile and Nokia S60.*Apress
[Green](https://www.interaction-design.org/references/authors/nicola_green.html), Nicola, [Harper](https://www.interaction-design.org/references/authors/richard_h__r__harper.html), Richard H. R., [Murtagh](https://www.interaction-design.org/references/authors/gerald_murtagh.html), Gerald and [Cooper](https://www.interaction-design.org/references/authors/geoff_cooper.html), Geoff (2001): *Configuring the Mobile User: Sociological and Industry Views*. In [Personal and Ubiquitous Computing](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing.html), 5 (2) pp. 146-156
[Greenfield](https://www.interaction-design.org/references/authors/adam_greenfield.html), Adam (2006): *Everyware: The Dawning Age of Ubiquitous Computing.* New Riders Publishing
[Gye](https://www.interaction-design.org/references/authors/lisa_gye.html), Lisa (2007): *Picture this: the impact of mobile camera phones on personal photographic practices*. In [Journal of Media and Cultural Studies](https://www.interaction-design.org/references/periodicals/journal_of_media_and_cultural_studies.html), 21 (2) pp. 279-288

[Hagen](https://www.interaction-design.org/references/authors/penny_hagen.html), Penny, [Robertson](https://www.interaction-design.org/references/authors/toni_robertson.html), Toni, [Kan](https://www.interaction-design.org/references/authors/melanie_kan.html), Melanie and [Sadler](https://www.interaction-design.org/references/authors/kirsten_sadler.html), Kirsten (2005): Emerging research methods for understanding mobile technology use. In: [Proceedings of OZCHI05, the CHISIG Annual Conference on Human-Computer Interaction](https://www.interaction-design.org/references/conferences/proceedings_of_ozchi05%2C_the_chisig_annual_conference_on_human-computer_interaction.html) 2005. pp. 1-10

[Harrison](https://www.interaction-design.org/references/authors/steve_harrison.html), Steve, [Art](https://www.interaction-design.org/references/authors/courtesy_art.html), Courtesy, [Tatar](https://www.interaction-design.org/references/authors/deborah_tatar.html), Deborah and [Sengers](https://www.interaction-design.org/references/authors/phoebe_sengers.html), Phoebe (2007): The Three Paradigms of HCI. In: [Begole](https://www.interaction-design.org/references/authors/bo_begole.html), Bo, [Payne](https://www.interaction-design.org/references/authors/stephen_payne.html), Stephen, [Churchill](https://www.interaction-design.org/references/authors/elizabeth_churchill.html), Elizabeth, [Amant](https://www.interaction-design.org/references/authors/rob_st__amant.html), Rob St., [Gilmore](https://www.interaction-design.org/references/authors/david_gilmore.html), David and [Rosson](https://www.interaction-design.org/references/authors/mary_b__rosson.html), Mary B. (eds.)[Proceedings of Computer/Human Interaction 2007](https://www.interaction-design.org/references/conferences/proceedings_of_computer%2Fhuman_interaction_2007.html) April 28 – May 3, 2007, San Jose, USA. pp. 1-18

[Helal](https://www.interaction-design.org/references/authors/abdelsalam_a__helal.html), Abdelsalam A., [Haskell](https://www.interaction-design.org/references/authors/bert_haskell.html), Bert, [Carter](https://www.interaction-design.org/references/authors/jeffery_l__carter.html), Jeffery L., [Brice](https://www.interaction-design.org/references/authors/richard_brice.html), Richard, [Woelk](https://www.interaction-design.org/references/authors/darrell_woelk.html), Darrell and [Rusinkiewicz](https://www.interaction-design.org/references/authors/marek_rusinkiewicz.html), Marek (1999): *Any
 Time, Anywhere Computing: Mobile Computing Concepts and Technology (The
 Springer International Series in Engineering and Computer Science).* Springer
[Hinckley](https://www.interaction-design.org/references/authors/ken_hinckley.html), Ken and [Horvitz](https://www.interaction-design.org/references/authors/eric_horvitz.html), Eric (2001): Toward more sensitive mobile phones. In: [Marks](https://www.interaction-design.org/references/authors/joe_marks.html), Joe and [Mynatt](https://www.interaction-design.org/references/authors/elizabeth_d__mynatt.html), Elizabeth D. (eds.) [Proceedings of the 14th annual ACM symposium on User interface software and technology](https://www.interaction-design.org/references/conferences/proceedings_of_the_14th_annual_acm_symposium_on_user_interface_software_and_technology.html) November 11 - 14, 2001, Orlando, Florida. pp. 191-192

[Hinckley](https://www.interaction-design.org/references/authors/ken_hinckley.html), Ken, [Pierce](https://www.interaction-design.org/references/authors/jeffrey_s__pierce.html), Jeffrey S., [Horvitz](https://www.interaction-design.org/references/authors/eric_horvitz.html), Eric and [Sinclair](https://www.interaction-design.org/references/authors/mike_sinclair.html), Mike (2005): *Foreground and background interaction with sensor-enhanced mobile devices*. In [ACM Trans. Comput.-Hum. Interact.](https://www.interaction-design.org/references/periodicals/acm_trans__comput-dot--hum__interact-dot-.html), 12 (1) pp. 31-52

[Hinckley](https://www.interaction-design.org/references/authors/ken_hinckley.html), Ken, [Pierce](https://www.interaction-design.org/references/authors/jeff_pierce.html), Jeff, [Sinclair](https://www.interaction-design.org/references/authors/mike_sinclair.html), Mike and [Horvitz](https://www.interaction-design.org/references/authors/eric_horvitz.html), Eric (2000): Sensing Techniques for Mobile Interaction. In:[Ackerman](https://www.interaction-design.org/references/authors/mark_s__ackerman.html), Mark S. and [Edwards](https://www.interaction-design.org/references/authors/keith_edwards.html), Keith (eds.) [Proceedings of the 13th annual ACM symposium on User interface software and technology](https://www.interaction-design.org/references/conferences/proceedings_of_the_13th_annual_acm_symposium_on_user_interface_software_and_technology.html) November 06 - 08, 2000, San Diego, California, United States. pp. 91-100

[Hosbond](https://www.interaction-design.org/references/authors/jens_henrik_hosbond.html), Jens Henrik (2005): Mobile Systems Development Challenges, Implications and Issues. In: [Krogstie](https://www.interaction-design.org/references/authors/john_krogstie.html), John,[Kautz](https://www.interaction-design.org/references/authors/karlheinz_kautz.html), Karlheinz and [Allen](https://www.interaction-design.org/references/authors/david_allen.html), David (eds.) [IFIP International Working Conference on Mobile Information Systems](https://www.interaction-design.org/references/conferences/ifip_international_working_conference_on_mobile_information_systems.html)December 6-7, 2005, Leeds, United Kingdom . pp. 279-286

[Høegh](https://www.interaction-design.org/references/authors/rune_t__h%F8egh.html), Rune T., [Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper, [Skov](https://www.interaction-design.org/references/authors/mikael_b__skov.html), Mikael B. and [Stage](https://www.interaction-design.org/references/authors/jan_stage.html), Jan (2008): A Field Laboratory for Evaluating In Situ. In: [Klinger](https://www.interaction-design.org/references/authors/kristin_klinger.html), Kristin, [Roth](https://www.interaction-design.org/references/authors/kristin_roth.html), Kristin, [Neidig](https://www.interaction-design.org/references/authors/jennifer_neidig.html), Jennifer, [Reed](https://www.interaction-design.org/references/authors/sara_reed.html), Sara, [Langel](https://www.interaction-design.org/references/authors/joy_langel.html), Joy, [Smalley](https://www.interaction-design.org/references/authors/katie_smalley.html), Katie and [Thor](https://www.interaction-design.org/references/authors/angela_thor.html), Angela (eds.). "Handbook of Research on User Interface Design and Evaluation for Mobile Technology". IGI Globalpp. 982-996
[Jameson](https://www.interaction-design.org/references/authors/anthony_jameson.html), Anthony (2001): *Modeling both the Context and the User*. In [Personal and Ubiquitous Computing](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing.html), 5 (1) pp. 29-33

[Johnson](https://www.interaction-design.org/references/authors/peter_johnson.html), Peter (1998). *Usability and Mobility; Interactions on the move*. Department of Computing Science[http://www.dcs.gla.ac.uk/~johnson/papers/mobile/HCIMD1.html](http://www.dcs.gla.ac.uk/~johnson/papers/mobile/HCIMD1.html)
[Jones](https://www.interaction-design.org/references/authors/matt_jones.html), Matt and [Marsden](https://www.interaction-design.org/references/authors/gary_marsden.html), Gary (2006): *Mobile interaction design.* John Wiley and Sons
[Jones](https://www.interaction-design.org/references/authors/quentin_jones.html), Quentin, [Grandhi](https://www.interaction-design.org/references/authors/sukeshini_a__grandhi.html), Sukeshini A., [Terveen](https://www.interaction-design.org/references/authors/loren_terveen.html), Loren and [Whittaker](https://www.interaction-design.org/references/authors/steve_whittaker.html), Steve (2004): *People-to-People-to-Geographical-Places: The P3 Framework for Location-Based Community Systems*. In [Computer Supported Cooperative Work](https://www.interaction-design.org/references/periodicals/computer_supported_cooperative_work.html), 13 (3) pp. 249-282

[Jung](https://www.interaction-design.org/references/authors/heekyoung_jung.html), Heekyoung, [Stolterman](https://www.interaction-design.org/references/authors/erik_a__stolterman.html), Erik A., [Ryan](https://www.interaction-design.org/references/authors/will_ryan.html), Will, [Thompson](https://www.interaction-design.org/references/authors/tonya_thompson.html), Tonya and [Siegel](https://www.interaction-design.org/references/authors/marty_siegel.html),
 Marty (2008): Toward a framework for ecologies of artifacts: how are 
digital artifacts interconnected within a personal life?. In: [Proceedings of the Fifth Nordic Conference on Human-Computer Interaction](https://www.interaction-design.org/references/conferences/proceedings_of_the_fifth_nordic_conference_on_human-computer_interaction.html) 2008. pp. 201-210

[Kaikkonen](https://www.interaction-design.org/references/authors/anne_kaikkonen.html), Anne, [Kekäläinen](https://www.interaction-design.org/references/authors/aki_kek%E4l%E4inen.html), Aki, [Cankar](https://www.interaction-design.org/references/authors/mihael_cankar.html), Mihael, [Kallio](https://www.interaction-design.org/references/authors/titti_kallio.html), Titti and [Kankainen](https://www.interaction-design.org/references/authors/anu_kankainen.html), Anu (2005): *Usability Testing of Mobile Applications: A Comparison between Laboratory and Field Testing*. In [Journal of Usability Studies](https://www.interaction-design.org/references/periodicals/journal_of_usability_studies.html), 1 (1) pp. 4-17
[Karapanos](https://www.interaction-design.org/references/authors/evangelos_karapanos.html), Evangelos, [Zimmerman](https://www.interaction-design.org/references/authors/john_zimmerman.html), John, [Forlizzi](https://www.interaction-design.org/references/authors/jodi_forlizzi.html), Jodi and [Martens](https://www.interaction-design.org/references/authors/jean-bernard_martens.html), Jean-Bernard (2009): User experience over time: an initial framework. In: [Proceedings of ACM CHI 2009 Conference on Human Factors in Computing Systems](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2009_conference_on_human_factors_in_computing_systems.html) 2009. pp. 729-738

[Kay](https://www.interaction-design.org/references/authors/alan_c__kay.html), Alan C. (1972): *A Personal Computer for Children of All Ages*. In [Proceedings of the ACM national conference](https://www.interaction-design.org/references/periodicals/proceedings_of_the_acm_national_conference.html),
[Kindberg](https://www.interaction-design.org/references/authors/tim_kindberg.html), Tim, [Spasojevic](https://www.interaction-design.org/references/authors/mirjana_spasojevic.html), Mirjana, [Fleck](https://www.interaction-design.org/references/authors/rowanne_fleck.html), Rowanne and [Sellen](https://www.interaction-design.org/references/authors/abigail_sellen.html), Abigail (2005): *The ubiquitous camera: an in-depth study of camera phone use*. In [IEEE Pervasive Computing](https://www.interaction-design.org/references/periodicals/ieee_pervasive_computing.html), 4 (2) pp. 42-50

[Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper and [Howard](https://www.interaction-design.org/references/authors/steve_howard.html), Steve (2004): Envisioning Mobile Information Services: Combining User- and Technology-Centered Design. In: [Masoodian](https://www.interaction-design.org/references/authors/masood_masoodian.html), Masood, [Jones](https://www.interaction-design.org/references/authors/steve_jones.html), Steve and [Rogers](https://www.interaction-design.org/references/authors/bill_rogers.html), Bill (eds.) [Computer Human Interaction 6th Asia Pacific Conference - APCHI 2004](https://www.interaction-design.org/references/conferences/computer_human_interaction_6th_asia_pacific_conference_-_apchi_2004.html) June 29 - July 2, 2004, Rotorua, New Zealand. pp. 180-190
[Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper and [Paay](https://www.interaction-design.org/references/authors/jeni_paay.html), Jeni (2005): Just-for-us: a context-aware mobile information system facilitating sociality. In: [Proceedings of 7th conference on Human-computer interaction with mobile devices and services](https://www.interaction-design.org/references/conferences/proceedings_of_7th_conference_on_human-computer_interaction_with_mobile_devices_and_services.html) 2005. pp. 23-30

[Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper and [Paay](https://www.interaction-design.org/references/authors/jeni_paay.html), Jeni (2010): *Indexicality: Understanding mobile human-computer interaction in context*. In [ACM Transactions on Computer-Human Interaction](https://www.interaction-design.org/references/periodicals/acm_transactions_on_computer-human_interaction.html), 17 (4) p. 14
[Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper and [Paay](https://www.interaction-design.org/references/authors/jeni_paay.html), Jeni (2006): *Public Pervasive Computing: Making the Invisible Visible*. In [IEEE Computer](https://www.interaction-design.org/references/periodicals/ieee_computer.html), 39 (9) pp. 60-65
[Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper and [Skov](https://www.interaction-design.org/references/authors/mikael_b__skov.html), Mikael B. (2007b): *Studying Usability In Sitro: Simulating Real World Phenomena in Controlled Environments*. In [International Journal of Human-Computer Interaction](https://www.interaction-design.org/references/periodicals/international_journal_of_human-computer_interaction.html), 22 (1) pp. 7-36

[Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper and [Skov](https://www.interaction-design.org/references/authors/mikael_b__skov.html), Mikael B. (2007a): *Exploring context-awareness for ubiquitous computing in the healthcare domain*. In [Personal and Ubiquitous Computing](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing.html), 11 (7) pp. 549-562
[Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper and [Stage](https://www.interaction-design.org/references/authors/jan_stage.html), Jan (2012): *Combining ethnography and object-orientation for mobile interaction design: Contextual richness and abstract models*. In [International Journal of Human-Computer Studies](https://www.interaction-design.org/references/periodicals/international_journal_of_human-computer_studies.html), 70 (3) pp. 197-217
[Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper and [Stage](https://www.interaction-design.org/references/authors/jan_stage.html), Jan (2006): *Exploring 'Canned Communication' for coordinating distributed mobile work activities*. In [Interacting with Computers](https://www.interaction-design.org/references/periodicals/interacting_with_computers.html), 18 (6) pp. 1310-133

[Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper and [Stage](https://www.interaction-design.org/references/authors/jan_stage.html), Jan (2004): *New techniques for usability evaluation of mobile systems*. In [International Journal of Human-Computer Studies](https://www.interaction-design.org/references/periodicals/international_journal_of_human-computer_studies.html), 60 (5) pp. 599-620
[Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper, [Skov](https://www.interaction-design.org/references/authors/mikael_b__skov.html), Mikael B., [Als](https://www.interaction-design.org/references/authors/benedikte_s__als.html), Benedikte S. and [Høegh](https://www.interaction-design.org/references/authors/rune_thaarup_h%F8egh.html),
 Rune Thaarup (2004): Is It Worth the Hassle? Exploring the Added Value 
of Evaluating the Usability of Context-Aware Mobile Systems in the 
Field. In:[Brewster](https://www.interaction-design.org/references/authors/stephen_a__brewster.html), Stephen A. and [Dunlop](https://www.interaction-design.org/references/authors/mark_d__dunlop.html), Mark D. (eds.) [Mobile Human-Computer Interaction - Mobile HCI 2004 - 6th International Symposium](https://www.interaction-design.org/references/conferences/mobile_human-computer_interaction_-_mobile_hci_2004_-_6th_international_symposium.html) September 13-16, 2004, Glasgow, UK. pp. 61-73

[Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper, [Skov](https://www.interaction-design.org/references/authors/mikael_b__skov.html), Mikael B., [Paay](https://www.interaction-design.org/references/authors/jeni_paay.html), Jeni and [Pathmanathan](https://www.interaction-design.org/references/authors/rahuvaran_pathmanathan.html), Rahuvaran (2012): Using Mobile Phones to Support Sustainability: A Field Study of Residential Electricity Consumption. In: [Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper and [Skov](https://www.interaction-design.org/references/authors/mikael_b__skov.html), Mikael B. (eds.) [Proceedings of the ACM CHI 2012 Conference on Human Factors in Computing Systems](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_2012_conference_on_human_factors_in_computing_systems.html) 2012, Austin, Texas. pp. 2347-2356

[Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper, [Gibbs](https://www.interaction-design.org/references/authors/martin_r__gibbs.html), Martin R., [Vetere](https://www.interaction-design.org/references/authors/franks_vetere.html), Franks, [Howard](https://www.interaction-design.org/references/authors/steve_howard.html), Steve, [Pedell](https://www.interaction-design.org/references/authors/sonja_pedell.html), Sonja, [Mecoles](https://www.interaction-design.org/references/authors/karen_mecoles.html), Karen and [Bunyan](https://www.interaction-design.org/references/authors/marcus_bunyan.html), Marcus (2004b): *Using *[*Cultural Probes*](https://www.interaction-design.org/literature/topics/cultural-probes)* to Explore Mediated Intimacy*. In [Australasian Journal of Information Systems](https://www.interaction-design.org/references/periodicals/australasian_journal_of_information_systems.html), 11 (2) pp. 102-115

[Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper, [Graham](https://www.interaction-design.org/references/authors/connor_graham.html), Connor, [Pedell](https://www.interaction-design.org/references/authors/sonja_pedell.html), Sonja, [Vetere](https://www.interaction-design.org/references/authors/frank_vetere.html), Frank, [Howard](https://www.interaction-design.org/references/authors/steve_howard.html), Steve, [Balbo](https://www.interaction-design.org/references/authors/s__balbo.html), S. and [Davies](https://www.interaction-design.org/references/authors/j__davies.html), J. (2005):*Evaluating the usability of a mobile guide: the influence of location, participants and resources*. In [Behaviour & IT](https://www.interaction-design.org/references/periodicals/behaviour_%26_it.html), 24 (1) pp. 51-65
[Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper, [Christensen](https://www.interaction-design.org/references/authors/claus_m__christensen.html), Claus M. and [Rasmussen](https://www.interaction-design.org/references/authors/klaus_k__rasmussen.html), Klaus K. (2010): *GeoHealth: a location-based service for home healthcare workers*. In [J. Location Based Services](https://www.interaction-design.org/references/periodicals/j__location_based_services.html), 4 (1) pp. 3-27

[Kostakos](https://www.interaction-design.org/references/authors/vassilis_kostakos.html), Vassilis, [Nicolai](https://www.interaction-design.org/references/authors/tom_nicolai.html), Tom, [Yoneki](https://www.interaction-design.org/references/authors/eiko_yoneki.html), Eiko, [O'Neill](https://www.interaction-design.org/references/authors/eamonn_o%27neill.html), Eamonn, [Kenn](https://www.interaction-design.org/references/authors/holger_kenn.html), Holger and [Crowcroft](https://www.interaction-design.org/references/authors/jon_crowcroft.html), Jon (2009):*Understanding and measuring the urban pervasive infrastructure*. In [Personal and Ubiquitous Computing](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing.html), 13 (5) pp. 355-364
[Lauesen](https://www.interaction-design.org/references/authors/soren_lauesen.html), Soren (2004): *User Interface Design: A Software Engineering Perspective.* Addison-Wesley
[Laurel](https://www.interaction-design.org/references/authors/brenda_k__laurel.html), Brenda K. (ed.) (1990): *The Art of Human-Computer Interface Design.* Reading, MA, Addison-Wesley Publishing
[Lindholm](https://www.interaction-design.org/references/authors/christian_lindholm.html), Christian and [Keinonen](https://www.interaction-design.org/references/authors/turkka_keinonen.html), Turkka (2003): *Mobile Usability: How Nokia Changed the Face of the Mobile Phone.* McGraw-Hill Professional

[Lindley](https://www.interaction-design.org/references/authors/sian_e__lindley.html), Sian E., [Harper](https://www.interaction-design.org/references/authors/richard_harper.html), Richard, [Randall](https://www.interaction-design.org/references/authors/dave_randall.html), Dave, [Glancy](https://www.interaction-design.org/references/authors/maxine_glancy.html), Maxine and [Smyth](https://www.interaction-design.org/references/authors/nicola_smyth.html), Nicola (2009): Fixed in time and "time in motion": mobility of vision through a SenseCam lens. In: [Proceedings of 11th Conference on Human-computer interaction with mobile devices and services](https://www.interaction-design.org/references/conferences/proceedings_of_11th_conference_on_human-computer_interaction_with_mobile_devices_and_services.html) 2009. p. 2
[Ling](https://www.interaction-design.org/references/authors/rich_ling.html), Rich (2001): *"We Release Them Little by Little": Maturation and Gender Identity as Seen in the Use of Mobile Telephony*. In [Personal and Ubiquitous Computing](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing.html), 5 (2) pp. 123-136

[Little](https://www.interaction-design.org/references/authors/linda_little.html), Linda and [Briggs](https://www.interaction-design.org/references/authors/pam_briggs.html), Pam (2009): *Private whispers/public eyes: Is receiving highly personal information in a public place stressful?*. In [Interacting with Computers](https://www.interaction-design.org/references/periodicals/interacting_with_computers.html), 21 (4) pp. 316-322
[Luff](https://www.interaction-design.org/references/authors/paul_luff.html), Paul and [Heath](https://www.interaction-design.org/references/authors/christian_heath.html), Christian (1998): Mobility in Collaboration. In: [Poltrock](https://www.interaction-design.org/references/authors/steven_poltrock.html), Steven and [Grudin](https://www.interaction-design.org/references/authors/jonathan_grudin.html), Jonathan (eds.)[Proceedings of the 1998 ACM conference on Computer supported cooperative work](https://www.interaction-design.org/references/conferences/proceedings_of_the_1998_acm_conference_on_computer_supported_cooperative_work.html) November 14 - 18, 1998, Seattle, Washington, United States. pp. 305-314
[McCullough](https://www.interaction-design.org/references/authors/malcolm_mccullough.html), Malcolm (2005): *Digital Ground: Architecture, Pervasive Computing, and Environmental Knowing.*The MIT Press

[McCullough](https://www.interaction-design.org/references/authors/malcolm_mccullough.html), Malcolm (2004): *Digital Ground: Architecture, Pervasive Computing, and Environmental Knowing.*The MIT Press
[Mikkonen](https://www.interaction-design.org/references/authors/m__mikkonen.html), M., [Väyrynen](https://www.interaction-design.org/references/authors/s__v%E4yrynen.html), S., [Ikonen](https://www.interaction-design.org/references/authors/v__ikonen.html), V. and [Heikkilä](https://www.interaction-design.org/references/authors/m__o__heikkil%E4.html), M. O. (2002): *User and Concept Studies as Tools in Developing Mobile Communication Services for the Elderly*. In [Personal and Ubiquitous Computing](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing.html), 6 (2) pp. 113-124
[Miller](https://www.interaction-design.org/references/authors/frederic_p_miller.html), Frederic P, [Vendome](https://www.interaction-design.org/references/authors/agnes_f__vendome.html), Agnes F. and [McBrewster](https://www.interaction-design.org/references/authors/john_mcbrewster.html), John (2010): *Digital Ecosystem.* Beau-Bassin, Mauritius, Alphascript Publishing
[Moggridge](https://www.interaction-design.org/references/authors/bill_moggridge.html), Bill (2007): *Designing Interactions.* The MIT Press

[Murphy](https://www.interaction-design.org/references/authors/john_murphy.html), John, [Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper, [Howard](https://www.interaction-design.org/references/authors/steve_howard.html), Steve, [Shanks](https://www.interaction-design.org/references/authors/graeme_shanks.html), Graeme and [Hartnell-Young](https://www.interaction-design.org/references/authors/elizabeth_hartnell-young.html), Elizabeth (2005): The converged appliance: "I love it... but I hate it". In: [Proceedings of OZCHI05, the CHISIG Annual Conference on Human-Computer Interaction](https://www.interaction-design.org/references/conferences/proceedings_of_ozchi05%2C_the_chisig_annual_conference_on_human-computer_interaction.html) 2005. pp. 1-10
[Nielsen](https://www.interaction-design.org/references/authors/jakob_nielsen.html), Jakob (2000). *WAP Field Study Findings*. Retrieved 8 November 2012 from useit.com: [http://www.useit.com/alertbox/20001210.html](http://www.useit.com/alertbox/20001210.html)

[Nielsen](https://www.interaction-design.org/references/authors/christian_monrad_nielsen.html), Christian Monrad, [Overgaard](https://www.interaction-design.org/references/authors/michael_overgaard.html), Michael, [Pedersen](https://www.interaction-design.org/references/authors/michael_bach_pedersen.html), Michael Bach, [Stage](https://www.interaction-design.org/references/authors/jan_stage.html), Jan and [Stenild](https://www.interaction-design.org/references/authors/sigge_stenild.html), Sigge (2006): It's worth the hassle!: the added value of evaluating the usability of mobile systems in the field. In: [Mørch](https://www.interaction-design.org/references/authors/anders_i__m%F8rch.html), Anders I.,[Morgan](https://www.interaction-design.org/references/authors/konrad_morgan.html), Konrad, [Bratteteig](https://www.interaction-design.org/references/authors/tone_bratteteig.html), Tone, [Ghosh](https://www.interaction-design.org/references/authors/gautam_ghosh.html), Gautam and [Svanaes](https://www.interaction-design.org/references/authors/dag_svanaes.html), Dag (eds.) [Proceedings of the 4th Nordic Conference on Human-Computer Interaction 2006, Oslo, Norway, October 14-18, 2006](https://www.interaction-design.org/references/conferences/proceedings_of_the_4th_nordic_conference_on_human-computer_interaction_2006%2C_oslo%2C_norway%2C_october_14-18%2C_2006.html) 2006. pp. 272-280

[Norman](https://www.interaction-design.org/references/authors/donald_a__norman.html), Donald A. (1998): *The
 Invisible Computer: Why Good Products Can Fail, the Personal Computer 
Is So Complex and Information Appliances Are the Solution.* MIT Press
[O'Hara](https://www.interaction-design.org/references/authors/kenton_o%27hara.html), Kenton, [Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper and [Paay](https://www.interaction-design.org/references/authors/jeni_paay.html), Jeni (2011): *Blended interaction spaces for distributed team collaboration*. In [ACM Transactions on Computer-Human Interaction (TOCHI)](https://www.interaction-design.org/references/periodicals/acm_transactions_on_computer-human_interaction_%28tochi%29.html), 18 (1) pp. 3:1-3:28
[Oulasvirta](https://www.interaction-design.org/references/authors/antti_oulasvirta.html), Antti (2009): Field Experiments in HCI: Promises and Challenges. In: [Saariluoma](https://www.interaction-design.org/references/authors/pertti_saariluoma.html), Pertti and [Isomäki](https://www.interaction-design.org/references/authors/hannakaisa_isom%E4ki.html), Hannakaisa (eds.). "Future Interaction Design II". London, United Kingdom: pp. 87-111

[Oulasvirta](https://www.interaction-design.org/references/authors/antti_oulasvirta.html), Antti and [Nyyssönen](https://www.interaction-design.org/references/authors/tuomo_nyyss%F6nen.html), Tuomo (2009): *Flexible Hardware Configurations for Studying Mobile Usability*. In [Journal of Usability Studies](https://www.interaction-design.org/references/periodicals/journal_of_usability_studies.html), 4 (2) pp. 93-105
[Paay](https://www.interaction-design.org/references/authors/jeni_paay.html), Jeni (2008): From ethnography to interface design. In: [Klinger](https://www.interaction-design.org/references/authors/kristin_klinger.html), Kristin, [Roth](https://www.interaction-design.org/references/authors/kristin_roth.html), Kristin, [Neidig](https://www.interaction-design.org/references/authors/jennifer_neidig.html), Jennifer, [Reed](https://www.interaction-design.org/references/authors/sara_reed.html), Sara, [Langel](https://www.interaction-design.org/references/authors/joy_langel.html), Joy, [Smalley](https://www.interaction-design.org/references/authors/katie_smalley.html), Katie and [Thor](https://www.interaction-design.org/references/authors/angela_thor.html), Angela (eds.). "Handbook of Research on User Interface Design and Evaluation for Mobile Technology". IGI Global

[Paay](https://www.interaction-design.org/references/authors/jeni_paay.html), Jeni and [Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper (2008b): *Understanding the user experience of location-based services: five principles of perceptual organisation applied*. In [Journal of Location Based Services](https://www.interaction-design.org/references/periodicals/journal_of_location_based_services.html), 2 (4) pp. 267-286
[Paay](https://www.interaction-design.org/references/authors/jeni_paay.html), Jeni and [Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper (2005): *Understanding and modelling built environments for mobile guide interface design*. In [Behaviour and Information Technology](https://www.interaction-design.org/references/periodicals/behaviour_and_information_technology.html), 24 (1) pp. 21-35
[Paay](https://www.interaction-design.org/references/authors/jeni_paay.html), Jeni and [Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper (2008a): *Situated Social Interactions: A Case Study of Public Places in the City*. In[Computer Supported Cooperative Work](https://www.interaction-design.org/references/periodicals/computer_supported_cooperative_work.html), 17 (2) pp. 275-290

[Paay](https://www.interaction-design.org/references/authors/jeni_paay.html), Jeni, [Sterling](https://www.interaction-design.org/references/authors/leon_sterling.html), Leon, [Vetere](https://www.interaction-design.org/references/authors/frank_vetere.html), Frank, [Howard](https://www.interaction-design.org/references/authors/steve_howard.html), Steve and [Boettcher](https://www.interaction-design.org/references/authors/anne_boettcher.html), Anne (2009b): *Engineering the social: The role of shared artifacts*. In [International Journal of Human-Computer Studies](https://www.interaction-design.org/references/periodicals/international_journal_of_human-computer_studies.html), 67 (5) pp. 437-454
[Paay](https://www.interaction-design.org/references/authors/jeni_paay.html), Jeni, [Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper, [Howard](https://www.interaction-design.org/references/authors/steve_howard.html), Steve and [Dave](https://www.interaction-design.org/references/authors/bharat_dave.html), Bharat (2009a): *Out on the town: A socio-physical approach to the design of a context-aware urban guide*. In [ACM Transactions on Computer-Human Interaction](https://www.interaction-design.org/references/periodicals/acm_transactions_on_computer-human_interaction.html), 16 (2) p. 7

[Palen](https://www.interaction-design.org/references/authors/leysia_palen.html), Leysia, [Salzman](https://www.interaction-design.org/references/authors/marilyn_c__salzman.html), Marilyn C. and [Youngs](https://www.interaction-design.org/references/authors/ed_youngs.html), Ed (2000): Going Wireless: Behavior & Practice of New Mobile Phone Users. In: [Kellogg](https://www.interaction-design.org/references/authors/wendy_a__kellogg.html), Wendy A. and [Whittaker](https://www.interaction-design.org/references/authors/steve_whittaker.html), Steve (eds.) [Proceedings of the 2000 ACM conference on Computer supported cooperative work](https://www.interaction-design.org/references/conferences/proceedings_of_the_2000_acm_conference_on_computer_supported_cooperative_work.html) 2000, Philadelphia, Pennsylvania, United States. pp. 201-210

[Perry](https://www.interaction-design.org/references/authors/mark_perry.html), Mark, [O'Hara](https://www.interaction-design.org/references/authors/kenton_p__o%27hara.html), Kenton P., [Sellen](https://www.interaction-design.org/references/authors/abigail_sellen.html), Abigail, [Brown](https://www.interaction-design.org/references/authors/barry_brown.html), Barry and [Harper](https://www.interaction-design.org/references/authors/richard_harper.html), Richard (2001): *Dealing with mobility: understanding access anytime, anywhere*. In [ACM Transactions on Computer-Human Interaction](https://www.interaction-design.org/references/periodicals/acm_transactions_on_computer-human_interaction.html), 8 (4) pp. 323-347
[Preece](https://www.interaction-design.org/references/authors/jennifer_j__preece.html), Jennifer J., [Rogers](https://www.interaction-design.org/references/authors/yvonne_rogers.html), Yvonne, [Sharp](https://www.interaction-design.org/references/authors/helen_sharp.html), Helen, [Benyon](https://www.interaction-design.org/references/authors/david_benyon.html), David, [Holland](https://www.interaction-design.org/references/authors/simon_holland.html), Simon and [Carey](https://www.interaction-design.org/references/authors/tom_carey.html), Tom (1994): *Human-Computer Interaction.* Reading, Mass., Addison-Wesley Publishing

[Preece](https://www.interaction-design.org/references/authors/jennifer_j__preece.html), Jennifer J., [Rogers](https://www.interaction-design.org/references/authors/yvonne_rogers.html), Yvonne and [Sharp](https://www.interaction-design.org/references/authors/helen_sharp.html), Helen (2002): *Interaction Design: Beyond Human-Computer Interaction.* John Wiley and Sons
[Ramsay](https://www.interaction-design.org/references/authors/marc_ramsay.html), Marc and [Nielsen](https://www.interaction-design.org/references/authors/jakob_nielsen.html), Jakob (2000). *WAP Usability: Déjà Vu: 1994 All Over Again*. Nielsen Norman Group[http://www.nngroup.com/reports/wap/WAP_usability.pdf](http://www.nngroup.com/reports/wap/WAP_usability.pdf)
[Raskin](https://www.interaction-design.org/references/authors/jef_raskin.html), Jef (2000): *The Humane Interface: New Directions for Designing Interactive Systems.* Addison-Wesley Publishing
[Reichl](https://www.interaction-design.org/references/authors/peter_reichl.html), Peter, [Fröhlich](https://www.interaction-design.org/references/authors/peter_fr%F6hlich.html), Peter, [Baillie](https://www.interaction-design.org/references/authors/lynne_baillie.html), Lynne, [Schatz](https://www.interaction-design.org/references/authors/raimund_schatz.html), Raimund and [Dantcheva](https://www.interaction-design.org/references/authors/antitza_dantcheva.html),
 Antitza (2007): The LiLiPUT prototype: a wearable lab environment for

user tests of mobile telecommunication applications. In: [Rosson](https://www.interaction-design.org/references/authors/mary_beth_rosson.html), Mary Beth and [Gilmore](https://www.interaction-design.org/references/authors/david_j__gilmore.html), David J. (eds.) [Extended
 Abstracts Proceedings of the 2007 Conference on Human Factors in 
Computing Systems, CHI 2007, San Jose, California, USA, April 28 - May 
3, 2007](https://www.interaction-design.org/literature/conference/extended-abstracts-proceedings-of-the-2007-conference-on-human-factors-in-computing-systems-chi-2007-san-jose-california-usa-april-28-may-3-2007) 2007. pp. 1833-1838
[Rodden](https://www.interaction-design.org/references/authors/tom_rodden.html), Tom, [Chervest](https://www.interaction-design.org/references/authors/keith_chervest.html), Keith, [Davies](https://www.interaction-design.org/references/authors/nigel_davies.html), Nigel and [Dix](https://www.interaction-design.org/references/authors/alan_dix.html), Alan (1998). *Exploiting Context in HCI Design for Mobile Systems*. ACM [http://www.dcs.gla.ac.uk/~johnson/papers/mobile/HCIMD1.html](http://www.dcs.gla.ac.uk/~johnson/papers/mobile/HCIMD1.html)

[Rogers](https://www.interaction-design.org/references/authors/yvonne_rogers.html), Yvonne, [Sharp](https://www.interaction-design.org/references/authors/helen_sharp.html), Helen and [Preece](https://www.interaction-design.org/references/authors/jenny_preece.html), Jenny (2011): *Interaction Design: Beyond Human - Computer Interaction - third edition.* Wiley

[Rogers](https://www.interaction-design.org/references/authors/yvonne_rogers.html), Yvonne, [Connelly](https://www.interaction-design.org/references/authors/kay_connelly.html), Kay, [Tedesco](https://www.interaction-design.org/references/authors/lenore_tedesco.html), Lenore, [Hazlewood](https://www.interaction-design.org/references/authors/william_r__hazlewood.html), William R., [Kurtz](https://www.interaction-design.org/references/authors/andrew_kurtz.html), Andrew, [Hall](https://www.interaction-design.org/references/authors/robert_e__hall.html), Robert E., [Hursey](https://www.interaction-design.org/references/authors/josh_hursey.html), Josh and [Toscos](https://www.interaction-design.org/references/authors/tammy_toscos.html), Tammy (2007): Why It's Worth the Hassle: The Value of In-Situ Studies When Designing Ubicomp. In: [Krumm](https://www.interaction-design.org/references/authors/john_krumm.html), John, [Abowd](https://www.interaction-design.org/references/authors/gregory_d__abowd.html), Gregory D., [Seneviratne](https://www.interaction-design.org/references/authors/aruna_seneviratne.html), Aruna and [Strang](https://www.interaction-design.org/references/authors/thomas_strang.html), Thomas (eds.) [UbiComp 2007 Ubiquitous Computing - 9th International Conference](https://www.interaction-design.org/references/conferences/ubicomp_2007_ubiquitous_computing_-_9th_international_conference.html) September 16-19, 2007, Innsbruck, Austria. pp. 336-353

[Rowland](https://www.interaction-design.org/references/authors/duncan_rowland.html), Duncan, [Flintham](https://www.interaction-design.org/references/authors/martin_flintham.html), Martin, [Oppermann](https://www.interaction-design.org/references/authors/leif_oppermann.html), Leif, [Marshall](https://www.interaction-design.org/references/authors/joe_marshall.html), Joe, [Chamberlain](https://www.interaction-design.org/references/authors/alan_chamberlain.html), Alan, [Koleva](https://www.interaction-design.org/references/authors/boriana_koleva.html), Boriana, [Benford](https://www.interaction-design.org/references/authors/steve_benford.html), Steve and [Perez](https://www.interaction-design.org/references/authors/citlali_perez.html), Citlali (2009): Ubikequitous computing: designing interactive experiences for cyclists. In:[Proceedings of 11th Conference on Human-computer interaction with mobile devices and services](https://www.interaction-design.org/references/conferences/proceedings_of_11th_conference_on_human-computer_interaction_with_mobile_devices_and_services.html) 2009. p. 21
[Schilit](https://www.interaction-design.org/references/authors/bill_n__schilit.html), Bill N. and [Theimer](https://www.interaction-design.org/references/authors/marvin_m__theimer.html), Marvin M. (1994): *Disseminating active map information to mobile hosts*. In [IEEE Network](https://www.interaction-design.org/references/periodicals/ieee_network.html), 8 (5) pp. 22-32

[Schmidt](https://www.interaction-design.org/references/authors/albrecht_schmidt.html), Albrecht, [Beigl](https://www.interaction-design.org/references/authors/michael_beigl.html), Michael and [Gellersen](https://www.interaction-design.org/references/authors/hans-werner_gellersen.html), Hans-Werner (1999b): *There is more to context than location*. In[Computers & Graphics](https://www.interaction-design.org/references/periodicals/computers_%26_graphics.html), 23 (6) pp. 893-901

[Schmidt](https://www.interaction-design.org/references/authors/albrecht_schmidt.html), Albrecht, [Aidoo](https://www.interaction-design.org/references/authors/kofi_asante_aidoo.html), Kofi Asante, [Takaluoma](https://www.interaction-design.org/references/authors/antti_takaluoma.html), Antti, [Tuomela](https://www.interaction-design.org/references/authors/urpo_tuomela.html), Urpo, [Laerhoven](https://www.interaction-design.org/references/authors/kristof_van_laerhoven.html), Kristof van and [Velde](https://www.interaction-design.org/references/authors/walter_van_de_velde.html), Walter van de (1999): Advanced Interaction in Context. In: [Gellersen](https://www.interaction-design.org/references/authors/hans-werner_gellersen.html), Hans-Werner (ed.) [Handheld and Ubiquitous Computing - First International Symposium - HUC99](https://www.interaction-design.org/references/conferences/handheld_and_ubiquitous_computing_-_first_international_symposium_-_huc99.html) September 27-29, 1999, Karlsruhe, Germany. pp. 89-101
[Sharp](https://www.interaction-design.org/references/authors/helen_sharp.html), Helen, [Rogers](https://www.interaction-design.org/references/authors/yvonne_rogers.html), Yvonne and [Preece](https://www.interaction-design.org/references/authors/jennifer_j__preece.html), Jennifer J. (2007): *Interaction Design: Beyond Human-Computer Interaction.* John Wiley and Sons

[Sharples](https://www.interaction-design.org/references/authors/mike_sharples.html), Mike, [Corlett](https://www.interaction-design.org/references/authors/dan_corlett.html), Dan and [Westmancott](https://www.interaction-design.org/references/authors/oliver_westmancott.html), Oliver (2002): *The Design and Implementation of a Mobile Learning Resource*. In [Personal and Ubiquitous Computing](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing.html), 6 (3) pp. 220-234
[Shneiderman](https://www.interaction-design.org/references/authors/ben_shneiderman.html), Ben (1997): *Designing the User Interface: Strategies for Effective Human-Computer Interaction. (3rd ed.).* Boston, MA, Addison-Wesley Publishing

[Skov](https://www.interaction-design.org/references/authors/mikael_b__skov.html), Mikael B., [Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper, [Paay](https://www.interaction-design.org/references/authors/jeni_paay.html), Jeni, [Husted](https://www.interaction-design.org/references/authors/niels_husted.html), Niels, [Nørskov](https://www.interaction-design.org/references/authors/jacob_n%F8rskov.html), Jacob and [Pedersen](https://www.interaction-design.org/references/authors/kenneth_pedersen.html), Kenneth (2012):*Designing on-site: Facilitating Participatory Contextual Architecture with Mobile Phones*. In [Journal of Pervasive and Mobile Computing](https://www.interaction-design.org/references/periodicals/journal_of_pervasive_and_mobile_computing.html), 8 (6)

[Vetere](https://www.interaction-design.org/references/authors/frank_vetere.html), Frank, [Gibbs](https://www.interaction-design.org/references/authors/martin_r__gibbs.html), Martin R., [Kjeldskov](https://www.interaction-design.org/references/authors/jesper_kjeldskov.html), Jesper, [Howard](https://www.interaction-design.org/references/authors/steve_howard.html), Steve, [Mueller](https://www.interaction-design.org/references/authors/florian_mueller.html), Florian, [Pedell](https://www.interaction-design.org/references/authors/sonja_pedell.html), Sonja, [Mecoles](https://www.interaction-design.org/references/authors/karen_mecoles.html), Karen and [Bunyan](https://www.interaction-design.org/references/authors/marcus_bunyan.html), Marcus (2005): Mediating intimacy: designing technologies to support strong-tie relationships. In:[Proceedings of ACM CHI 2005 Conference on Human Factors in Computing Systems](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2005_conference_on_human_factors_in_computing_systems.html) 2005. pp. 471-480
[Weilenmann](https://www.interaction-design.org/references/authors/alexandra_weilenmann.html), Alexandra (2001): *Negotiating Use: Making Sense of Mobile Technology*. In [Personal and Ubiquitous Computing](https://www.interaction-design.org/references/periodicals/personal_and_ubiquitous_computing.html), 5 (2) pp. 137-145

[Weiser](https://www.interaction-design.org/references/authors/mark_weiser.html), Mark (1991): *The Computer for the 21st Century*. In [Scientific American](https://www.interaction-design.org/references/periodicals/scientific_american.html), 265 (3) pp. 94-104
[Weiss](https://www.interaction-design.org/references/authors/scott_weiss.html), Scott (2002): *Handheld Usability.* John Wiley and Sons
[Wilde](https://www.interaction-design.org/references/authors/oscar_wilde.html), Oscar (2010): *The Decay Of Lying.* Kessinger Publishing, LLC
[Winograd](https://www.interaction-design.org/references/authors/terry_winograd.html), Terry (1996): *Bringing Design to Software.* ACM Press
[Zuberec](https://www.interaction-design.org/references/authors/sarah_zuberec.html), Sarah (2000): The interaction design of Microsoft Windows CE. In: [Bergman](https://www.interaction-design.org/references/authors/eric_bergman.html),
 Eric (ed.). "Information Appliances and Beyond: Interaction Design for 
Consumer Products (Interactive Technologies)". Morgan Kaufmann

## 本书章节涵盖的主题：

[移动计算 (Mobile Computing)](https://www.interaction-design.org/literature/topics/mobile-computing)[
                        用户体验 (User Experience, UX) 设计](https://www.interaction-design.org/literature/topics/ux-design)[
                        人机交互 (Human-Computer Interaction, HCI)](https://www.interaction-design.org/literature/topics/human-computer-interaction)[
                        设计史 (Design History)](https://www.interaction-design.org/literature/topics/design-history)
