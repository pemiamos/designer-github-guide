# 53. 服务设计 (Service Design)

**来源**：The Encyclopedia of Human-Computer Interaction, 2nd Ed.
**Notion 原页面**：https://www.notion.so/448baae89fa04d30b2cdbf272acab381

---

[John Zimmerman](https://www.interaction-design.org/literature/author/john-zimmerman-1) 和 [Jodi Forlizzi](https://www.interaction-design.org/literature/author/jodi-forlizzi-1)

# 引言

在过去的几十年里，全球大部分工业化经济体（industrialized economies）经历了从产品制造到服务交付的转型。科技产业在这一转型中扮演了重要角色，从硬件和软件产品转向了软件即服务（Software as a Service, SaaS），并将智能手机等硬件视为产品-服务系统（product-service systems, PSS）的组成部分。这种转型产生了对专注于服务的全新[创新（innovation）](https://www.interaction-design.org/literature/topics/innovation)流程的需求。这种被称为[服务设计（service design）](https://www.interaction-design.org/literature/topics/service-design)的新型创新实践源于商学院的研究，主要来自运营（operations）和[营销（marketing）](https://www.interaction-design.org/literature/topics/marketing)领域。

*运营*传统上侧重于降低制造成本并提高生产与交付效率。然而，这种关注点并不太适用于服务。同样，*营销*传统上侧重于了解客户的消费习惯和动机，以驱动更多的消费。同样，营销中对产品的关注也无法很好地映射到服务上。Vargo 和 Lusch 的一篇开创性论文捕捉到了这一转型，作者鼓励营销研究人员放弃基于制造产出的主导逻辑（dominant logic），并围绕*服务提供（service provisioning）*建立一种新的主导逻辑 (Vargo and Lusch, 2004)。

服务设计（Service design）作为一种设计实践出现，它与[产品设计（product design）](https://www.interaction-design.org/literature/topics/product-design)和[用户体验 (UX) 设计（user experience (UX) design）](https://www.interaction-design.org/literature/topics/ux-design)有所不同。传播与信息设计师、产品设计师以及[UX 设计师（UX designers）](https://www.interaction-design.org/literature/topics/ux-designers)开始与服务研究人员及企业合作，共同创建这一全新的实践。在此过程中，他们借鉴了传统实践中的方法和流程，同时也发明了更侧重于系统性（systemic）和生态（ecology）视角的新方法。这些设计师协助创建的最重要的两种方法包括*服务蓝图（service blueprinting）* (Bitner et al, 2008) 和*客户旅程地图（customer journey mapping）* (Samadzadeh, 2015)，这两者在 UX 设计中得到了日益广泛的应用。

大多数服务设计工作专注于对大型传统服务的创新，包括银行与金融、医疗保健、旅游、酒店业、零售、政府及公共服务。相关研究聚焦于一线员工（frontline employees）的工作、他们与客户之间的面对面交互，以及支持服务执行的后端流程（backend processes）。有趣的是，交互通信技术（interactive communication technologies, ICT）的飞速发展，包括个人计算机、互联网、万维网（World Wide Web）、社交计算（social computing）、云计算（cloud computing）、移动电话以及智能手机

而物联网（Internet of Things, IoT）日益推动服务研究和服务设计去探索数字化服务（digital services）。

数字化服务的增长使得服务研究与人机交互（[Human-Computer Interaction, HCI](https://www.interaction-design.org/literature/topics/human-computer-interaction)）研究之间，以及服务设计与用户体验（UX）实践之间产生了重叠。许多早期的数字化服务专注于创建*自助服务（self-service）*设备和界面。这些设备用计算机取代了前线员工，例如自动柜员机、交通售票机和航空公司值机自助终端（图 1）。它们同时也为 HCI 和 UX 设计带来了大量的[可用性（usability）](https://www.interaction-design.org/literature/topics/usability)挑战。

![](https://public-media.interaction-design.org/images/uploads/user-content/1445/fwTuWjbkGOSATS6xUASiZ399SIKgKM1e5PJmNPd8.jpeg)
作者 / 版权持有者：Wolfmann 提供。版权条款和许可：CC BY-SA 4.0 (Creative Commons Attribution-ShareAlike 4.0 International)

图 1. 顾客绕过售票窗口，使用自助终端购买火车票。随着许多顾客现在可以通过手机购买并出示交通票据，智能手机正开始对这些自助服务设备产生挑战。

下一波数字化服务将交互从实体服务场景（servicescapes）转移到了 Web 端，以及最近的移动设备上。这

这一趋势包括客服人员被 Wiki、常见问题解答（FAQs, lists of frequently asked questions）以及近期的聊天机器人（Chatbots）所取代（图 2）。

![](https://public-media.interaction-design.org/images/uploads/user-content/1445/fBi2kCdP9P6KkNvPCbHMV3TKk7Vk2vLp08uv2ERS.png)
*作者 / 版权持有者：Nike, Inc. 版权条款与许可：保留所有权利。根据合理使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。*

图 2. Nike 的这项在线服务允许客户设计自己的鞋子，将自助服务（Self-service）提升到了一个全新的水平。这一向个性化（Personalization）迈进的步骤模糊了客户与工业设计师之间的界限。

传统的、一线服务员工也被零工经济（Gig-economy）从业者所取代。这一现象的出现得益于智能手机、快速且泛在的网络（Ubiquitous networks）以及数据科学（Data science）的进步（图 3）。这种服务创新（Service innovation）既是技术性的，也是经济性的。服务设计师需要将两者都视为设计材料（Design materials），以便构思新的创新和新的生活方式。

![](https://public-media.interaction-design.org/images/uploads/user-content/1445/T2ywySTpEVWLZJ53jabNitl5v5ZdSYDzn4EyytQR.jpeg)
作者 / 版权持有者：由 shopblocks 提供。版权条款与许可：CC BY 2.0 (Creative Commons Attribution 2.0 Generic)

图 3. 为 Uber 提供外卖配送服务的零工经济从业者。

# 服务与服务设计（Services and Service Design）

服务与产品不同。“价值（Value）”是两者之间最显著的区别特征之一。当客户购买产品时，他们支付金钱并获得占有权和所有权（Possession and Ownership）；他们是用金钱交换一件物品。而当客户为服务付费时，他们获得的是一种服务行为（Performance）。即有人在为他们执行所需的操作。服务提供者通过其服务行为创造价值，但所有权并不发生转移。

Starbucks 提供了一个简单的例子。一杯 Starbucks 咖啡是一个产品。客户支付咖啡费用并获得占有权；他们拥有手中这杯咖啡。而 Starbucks 门店则充当一项服务。一线员工（Frontline employees）通过“履行”服务来提供价值；他们根据需求制作并交付咖啡。该服务通过饮料的销售间接产生收入。在交易结束时，客户并不拥有这家店，也不占有或拥有这些一线员工。Starbucks 以产品-服务系统（Product-Service System, Morelli, 2003）的方式运作。产品增强了服务，而服务也增强了产品。两者相辅相成。- 剩余 6 小时 25 分 53 秒：[ Gamification - How to Create Engaging User Experiences](https://www.interaction-design.org/courses/gamification-how-to-create-engaging-user-experiences)
- 剩余 1 天：[ Service Design: How to Design Integrated Service Experiences](https://www.interaction-design.org/courses/service-design-how-to-design-integrated-service-experiences)

自 20 世纪 50 年代以来，服务及其服务部门已逐渐主导工业化世界的经济 (Cox et al., 2013)。服务的重要性日益增加，是因为它们有助于加快金融交易的速度；它们利用了数字技术所提供的消除时间和空间限制的特性，而产品则难以轻易实现这一点 (Normann, 2001)。Normann 将此称为 *去物质化（Dematerialization）* 和 *流动化（Liquification）*。例如，随着货币日益去物质化，它增强了流动性；通过消除时间和空间的障碍，它减少了金融交易中的摩擦（Friction）。

去物质化是人机交互（Human-Computer Interaction, HCI）研究和用户体验（User Experience, UX）实践中非常熟悉的话题，它使商业运行得更快。服务通过去物质化和增加流动化来实现创新。它们通过 *解绑（Unbundling）* 和 *重新绑定（Rebundling）* 的过程来实现这一点。例如，一家杂货店可能会在其物理空间内集成一个银行分支机构。这解绑了银行作为客户访问的独立地点的属性，并将杂货店重新绑定为一个允许...

涵盖了购买杂货和银行交易。将银行设置在商店内缩短了顾客在这两个实体之间必须移动的物理距离，从而增加了他们选择这种“一站式商店”而非分别使用独立杂货店和银行的可能性。将此概念置于数字化语境中，像 Square 这样的系统将销售点（Point-of-Sale, POS）系统从笨重的收银机中“解绑”（unbundle），并将每部智能手机重新“绑定”（rebundle）为潜在的销售点系统（图 4）。

![](https://public-media.interaction-design.org/images/uploads/user-content/1445/hGJAJ6khgA0SToI4mEur8s9Ql4qDoxVZwGEcVm3o.jpeg)
Author / Copyright holder: Courtesy of Rosenfeld Media. Copyright terms and license: CC BY 2.0 (Creative Commons Attribution 2.0 Generic)

图 4. Square 的信用卡阅读器于 2009 年推出。这家硅谷初创公司让任何智能手机都能变成一台收银机。

服务研究人员将服务的兴起归功于信息通信技术（Information and Communication Technologies, ICTs）的进步 (Normann, 2001)。人机交互（Human-Computer Interaction, HCI）和用户体验（User Experience, UX）设计社区在推动这些技术的进步、创造新的产品/服务形式以及研究 ICTs 的进步如何影响人们的生活方面发挥了重要作用。然而有趣的是，HCI 和 UX 设计往往倾向于遵循以产品为中心（product-centric）的设计流程。它们专注于生产一个“东西”。其底层的心理模型（mental model）仍然集中在制造人们想要拥有和占有的东西上。

在一段时间内，硬件和软件都采用了以产品为中心的

经济模型。Microsoft 的 Office 软件套件提供了一个很好的例子（图 5）。在过去，客户可以前往商店，从货架上选择一个包含软件和手册的盒子，在收银台付款，然后拎着购物袋离开。客户最终将拥有这些实物材料，并获得在计算机上安装该软件的许可（License）。这种以产品为中心的模型（Product-centric model）不仅适用于硬件（例如台式机、打印机、消费电子产品），也适用于软件（例如操作系统、桌面出版 Desktop publishing、数据库）。

![](https://public-media.interaction-design.org/images/uploads/user-content/1445/ndneyCnKRTbTD8qc9Ei9iD0dN3jWiDMs0n1ThWCE.jpeg)
Author / Copyright holder: Courtesy of Long Zheng. Copyright terms and license: CC BY-SA 2.0 (Creative Commons Attribution-ShareAlike 2.0 Generic)

图 5. Microsoft Office，最初是人们在零售店货架上选择并付费购买的产品。客户拥有其购买的材料。

进入 21 世纪二十年后，许多（如果不是大多数）硬件和软件采用了基于服务（Services）的经济模型。Google Docs 提供了一个例子（图 6）。这个在线软件套件复制了 Microsoft Office 提供的许多功能。然而，服务化方法（Service approach）具有几个重要的区别和优势。Google Docs 是免费使用的。此外，用户永远不需要为升级付费。相反，每一次

当他们使用这些工具时，使用的是最新版本，从而消除了人们在尝试协作时因使用不同版本的软件产品而导致的大量问题。用户并不拥有 Google Docs 应用程序的所有权。该服务免费且不涉及所有权，这一事实与渗透在以用户为中心的设计（User-Centered Design）中隐含的“用户即付费客户”这一角色相矛盾。Google Docs 在 Google 与用户之间实现了价值共创（Value Co-creation）。用户可以免费使用软件，而 Google 则根据用户与软件的交互方式获取个人数据，并将其出售给其他公司。

![](https://public-media.interaction-design.org/images/uploads/user-content/1445/63xrhXjPfBvYhawRrPUSmZIxKqUYENoNJZaZAs0Q.jpeg)
作者/版权持有者：Google LLC, www.google.com/docs/about。版权条款与许可：保留所有权利。根据合理使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。

图 6. Google Docs 将生产力应用程序作为一种服务（as a service）提供，成为了 Microsoft Office 的替代方案。虽然 Docs 最初是作为面向个人用户的免费服务发布的，但 Google 现在向企业客户收取 Docs 特定版本的费用，并将所有信息保密在企业内部。

一个使情况复杂化的因素是，使用这些工具创建的文档的所有权仍然模糊不清。用户“拥有”这些文档，但他们并不具备完全的控制权，尤其是在删除方面。将 Google Docs 与...

……到 Microsoft Office 的例子阐明了“颠覆性创新（disruptive innovation）”的概念，这是服务领域一种常见的进步类型。在进行颠覆性创新时，服务提供商会为现有的产品或服务提供一种价格低得多的替代方案。新版本仅具备当前市场领导者部分的功能，而较低的价格点则将客户从市场领导者那里吸引过来 (Christensen and Raynor, 2003)。

如今，人机交互（HCI）和用户体验（UX）所开发、创新和研究的系统，其功能表现为“产品-服务系统（product-service systems）”——这类系统由人类参与者（human actors）、技术触点（technology touchpoints）、环境以及其他基础设施组成，旨在提供一种整体的使用体验。团队可以通过“产品化（productization）”进行创新，即在服务中创建新产品。例如，Amazon 的 Alexa 就是一个客户可以购买并拥有的产品，它提供了一种访问 Amazon 服务（如 Prime Music）以及多种其他服务的新方式。团队还可以通过“服务化（servitization）”进行创新，即创建围绕产品的新服务。例如，Apple 的 iCloud 服务被添加到其众多 iOS 和 Macintosh 产品中并对其进行了增强。

# 服务设计中的核心概念

服务设计（Service Design）提供了几个核心概念，这些概念影响了[设计思维（Design Thinking）](https://www.interaction-design.org/literature/topics/design-thinking)，并使得服务设计与产品设计截然不同。其中许多概念与人机交互（Human-Computer Interaction, HCI）研究和用户体验（User Experience, UX）设计实践密切相关。

## 53.1 服务概念（Service Concept）

服务设计流程（Service Design Process）最终会产生一个“服务概念（Service Concept）”(Goldstein et al., 2002)（图 7）。它包含四个不同的要素：

1. 客户的需求与愿望
1. 服务组织的战略意图（Strategic Intention）
1. 客户获得的收益（被称为 *what*，即“内容”）
1. 关于服务应如何交付的描述（被称为 *how*，即“方式”）

一个设计良好的服务概念应当缩小客户或利益相关者（Stakeholder）的预期与实际交付的服务之间的差距。一个沟通充分的服务概念应当在客户、利益相关者和服务提供者之间建立一致性。服务概念一旦创建，即可用于帮助构思新服务，细化一组新兴服务产品（Service Offerings）的细节，并指导新产品的部署与评估。在创建服务概念时，服务设计团队还将制定一套运作化（Operationalizing）该概念的策略，以引导服务组织从当前状态过渡到理想的未来状态。一旦完成，独立的创新团队可以将其作为指南来开发许多新产品，从而降低这些产品之间产生冲突的可能性。

![](https://public-media.interaction-design.org/images/uploads/user-content/1445/JaFfPm8mnxbYLrBruh8lngWHwyzv8g3opr5XITJl.png)
图 7. 服务概念，改编自 Goldstein et al., 2002

## 53.2 价值共创（Co-creation of Value）

服务设计（Service design）通过客户与服务提供者之间共同创造价值这一理念，将自身与产品设计（product design）区分开来（Prahalad and Ramaswamy, 2004; Payne et al., 2008）。为了使其有效运作，客户必须感知到通过参与服务能够获得价值，而服务提供者也必须感知到通过向客户提供服务能够获得价值。双方都必须感觉到他们获得的价值高于其投入的价值。以 Starbucks 为例，客户通过选择并前往某家 Starbucks 门店点咖啡来共创价值；而服务方则通过提供客户想要的产品以及选择便捷的营业时间和地点来共创价值。

点对点经济服务（peer-economy service）Waze 在数字化空间中提供了一个很好的示例（图 8）。Waze 为驾驶员提供免费的逐步导航系统（turn-by-turn navigation system），并增强了交通详情和其他信息。当驾驶员使用该系统时，Waze 会收集位置、方向和速度信息。通过聚合当前用户的数据，Waze 构建了当前交通状况的详细模型。为了收集较少行驶道路的数据，Waze 采用了[游戏化（gamification）](https://www.interaction-design.org/literature/topics/gamification)手段，当用户为了产生这些更有价值的数据而绕路行驶时，系统会为其提供勋章。此外，该应用程序允许用户添加他们自己的

地标以及他们遇到的情况描述。Waze 将交通信息出售给其他感兴趣的利益相关者（stakeholders），从而产生用于支付软件开发和维护费用的收入。客户通过生成 Waze 用于提供服务并出售给他人的数据来共同创造价值（co-create value）。而 Waze 则通过免费提供更新的分步导航（turn-by-turn navigation）来共同创造价值。

![](https://public-media.interaction-design.org/images/uploads/user-content/1445/VZDAy46ylTHuNnhIJxQTBHLfAasTHEYfKAmATXqj.jpeg)
作者 / 版权持有者：Waze。版权条款和许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。
图 8. Waze 是一款众包（crowdsources）交通信息的移动应用程序。该服务与客户共同创造价值。

价值共创（Co-creation of value）不仅涉及收入，还包括其他形式的价值。用户体验设计（UX design）几乎完全专注于用户的需求，而服务设计师（service designers）则关注一系列利益相关者，包括主要客户和服务提供者。他们利用价值共创的概念，构思一种在所有利益相关者之间交换价值的新生态系统。这项工作更具系统性（systemic）。服务设计师致力于识别每个利益相关者所追求的多种不同类型的价值，并研究哪些交互（interactions）能够产生对利益相关者有价值的内容。随着免费移动应用和在线...

服务驱动服务设计师在用户与服务提供者（user-to-service-provider）的交互之外，寻找来自其他利益相关者（stakeholders）的营收来源。这一挑战对于人机交互（Human-Computer Interaction, HCI）研究人员和用户体验（User Experience, UX）设计师来说变得日益重要。UX 设计团队面临的一个挑战是，这些为利益相关者共创价值（co-create value）的努力，往往迫使团队去考虑远超出人们与计算机交互范围的价值，因此可能会让人觉得这完全超出了 HCI 和 UX 的领域。

服务设计文献经常将 *价值共产（co-production of value）* 和 *价值共创（co-creation of value）* 作为同义词使用。关于服务主导逻辑（service dominant logic）的早期研究使用了“共产（co-production）”一词；然而，Lusch 和 Vargo 后来改为使用“共创（co-creation）”，因为有批评认为“共产”一词感觉过于接近于“生产产品”，而这正是其服务主导逻辑旨在克服的思维方式 (2006)。

## 53.3 客户能力（Customer Competence）

客户能力（Customer Competence）是指承认客户能够执行服务中具有价值的部分 (Prahalad and Ramaswamy, 2000)。服务设计师对这一概念的应用通常会带来自助服务创新（Self-service innovations）。一个经典的服务设计案例是对客户能够自行挑选杂货的认可，以及由此产生的转变：从由店员收集所有商品的传统杂货店，转变为客户将所需商品放入购物篮或购物车的现代超市。早期电话中拨号盘的加入代表了另一种更侧重于技术层面的对客户能力的认可；在这种情况下，即认可客户能够记住并拨打对方的电话号码，从而减少了由接线员连接每次通话的需求。

在开展设计项目时，设计团队不仅会考虑服务能为客户或用户提供什么，还会考虑客户能为自己做什么，以及他们能做哪些对服务提供者有价值的事情。软件公司将用户作为 Beta 测试员（Beta-testers）是一个极佳的例子。公司意识到，部分用户具备操作未完成软件以及识别并描述软件缺陷（Bugs）所需的技能。如此一来，客户能力便成为了价值共创（Value co-creation）的一个方面。在 Beta 测试的案例中，公司获得了改进软件的免费劳动力，而部分选定的客户则可以提前预览...

到来以及影响最终设计的机会。

Yelp 提供了一个与人机交互（Human-Computer Interaction, HCI）和用户体验（User Experience, UX）更为接近的客户能力（Customer Competence）示例 (www.yelp.com)。多年来，HCI 和普适计算（UbiComp）研究人员一直在构建基于位置的信息服务（location-based information services）原型。这些研究人员始终未能解决的一个难以逾越的问题是，如何为系统填充所需的基于位置的信息。Yelp 通过让用户生成他们自己想要的信息，解决了这一挑战。Yelp 的核心功能允许用户对当地餐厅和其他服务进行评分和评论。这些在线餐厅评论的影响力如此之大，以至于影响了更传统的声誉（reputation）形式 (Luca, 2011)。客户评分中餐厅星级的一次提升，可触发该餐厅收入 5–9% 的增长。在这个例子中，Yelp 提供了一个由用户生成其所需数据的平台。

## 53.4 服务接触与接触点

关于服务设计与创新的早期研究探讨了“服务接触（Service Encounters）”，即客户与一线员工（Frontline Employees）之间的面对面交互 (Bitner et al., 1990)。这些研究详细阐述了员工如何通过识别并满足客户需求、预判并超越客户需求，以及在服务故障（Service Breakdowns）后进行恢复，从而显著提升客户体验。随着信息与通信技术（ICTs）的发展，越来越多的一线员工被计算系统所取代，“服务接触”的含义也随之扩展，涵盖了客户与一线员工的交互以及客户与计算机系统的交互。

在开发服务设计方法的过程中，从业者和研究人员开始讨论“接触点（Touchpoints）”。接触点包括客户在完成一项任务或经历一次“客户旅程（Customer Journey）”期间，与服务提供者产生的每一个交互点。接触点不仅包括服务接触，还包括客户可能产生的其他交互，例如尝试停车、通过门禁、查看标识与寻路（Wayfinding）、使用餐巾纸分配器以及选择座位。在致力于创新客户体验时，服务设计师会尝试识别客户旅程中的所有接触点，随后寻找更高效的实现方式，或者探索增强或消除这些接触点的方法。

## 53.5 服务模式（Service Patterns）

随着互联网、云计算和物联网（Internet of Things）的兴起，如今的服务通常依赖于由其他服务产生的数据流（data streams）和结果（outcomes）。服务可以通过多种方式进行分组（Chai et al., 2005）。一个简单的例子是现在常见的在某个新服务中创建账户，并使用 Google 或 Facebook 的凭据（credentials）来验证用户身份的流程。服务设计社区（service design community）已经识别出几种服务模式（service patterns），其中包括捆绑（bundling）和提取（extraction），即对一组服务进行分组或取消分组。使用 Facebook 或 Google 凭据进行身份验证就是捆绑的一个例子。

在线旅行规划服务 Kayak 提供了另一个例子。他们在同一个规划工具中链接了关于酒店和航空公司的信息。为了提供自身的服务，他们依赖于其他服务提供的信息。Uber 乘客在乘坐 Uber 时可以使用其 Spotify 播放列表，但这并非行程中必须的一部分。乘客可以在许多机场使用通用自助终端（kiosk）办理航班登机手续，但办理登机服务并不依赖于航空公司的业务服务。

服务可以在时间或覆盖范围上进行扩展（scaled）。微服务（microservice）是指在短时间内或在局部环境下使用的服务——例如，包装圣诞礼物的服务，或报告社区内问题的本地服务。另一方面，宏服务（macroservice）则在全球范围内被使用，并且

在更长的时间段内。例如，全球每天有数十亿人在使用 Google 搜索。

## 53.6 客户的客户（The Customer’s Customer）

服务交付（Service delivery）通常涉及一组级联且互操作的人员，他们同时扮演着客户和服务提供者（Service provider）的角色。在这种情况下，“客户的客户”是指链条中的下一个人，当当前的客户转变为服务提供者的角色时，该人将接受服务。在药店取药是一个简单的例子：药剂师是在线订购系统的客户，使用该系统接收新订单的通知；在这种情况下，领取药物的人就是药剂师的客户。一个设计良好的服务设计（Service Design）会关注“客户的客户”的需求，以增加价值共创（Co-creation of value）。在用户体验设计（UX design）中，用户通常被认为是客户；然而，UX 设计领域往往较少关注“客户的客户”的需求 (Holmlid, 2009)。

# 服务设计流程（Service design process）

以用户为中心的设计流程（user-centered design process）描绘了世界的现状，并以新的计算人工制品（computational artifacts）的形式构思理想的未来状态。服务设计（Service design）依赖于一个类似的过程，但存在一些重要的区别。最重要的是，服务设计流程产生的是一个系统、一个服务概念（service concept）以及一套从当前系统过渡到理想系统的策略。与几乎完全关注用户的 [UCD](https://www.interaction-design.org/literature/topics/user-centered-design) 和 UX 不同，服务设计师在服务提供者与客户需求的交汇点寻找解决方案。因此，服务设计通过一系列模型来表达，这些模型描述了服务的定义、它如何满足客户的需求，以及它如何实现多个利益相关者（stakeholders）的目标和倡议 (Goldstein et al., 2002)。

在服务设计中，常用于描绘现状并探索理想未来的三种模型是：利益相关者模型（stakeholder model）、客户旅程图（customer journey map）和服务蓝图（service blueprint）。利益相关者模型详细描述了所有关系集，通常是从服务系统内单个利益相关者的视角出发。服务蓝图描绘了客户在服务中的轨迹，通常是为了完成某项任务，例如购买房屋 (Bitner et al., 2008)。它揭示了客户在这一系列...中所经历的交互顺序。

...触点（Touchpoints），随后记录客户与之交互的元素和资源，以及为了提供服务而必须协同工作的后台业务资源（Backstage business resources）。客户旅程图（Customer Journey Map）同样绘制了在服务过程中的轨迹，但其重点在于客户的动机、体验和情感 (Samadzadeh, 2015)。所有这些模型的目标是以一种能够通过重新排列或修改来揭示整个系统变化的方式来呈现元素 (Sevaldson, 2011)。产品、服务、人员和关系被整体地呈现出来。服务设计（Service Design）模型和计划成为了服务设计团队协作的基础。模型被用于确保所有团队...

达成一致的成员共同开发[场景（Scenarios）](https://www.interaction-design.org/literature/topics/user-scenarios)和概念，并考虑引入服务生态（Service Ecology）中的新产品、服务和系统的影响。他们支持一种迭代地且整体地（Iteratively and Holistically）开发、随时间推移而评估和完善，并最终充满信心地推向世界的解决方案。

在许多方面，服务设计（Service Design）与人机交互（Human-Computer Interaction, HCI）中的设计实践非常相似。两者都始于背景研究（Background Research），以了解现状并识别客户和用户的需求。服务设计的不同之处在于，它还致力于识别服务提供者的战略举措（Strategic Initiatives）。以用户为中心的设计（User-Centered Design, UCD）、用户体验（User Experience, UX）和服务设计都涉及原型设计（Prototyping）。在服务设计中，这通常包括构建或模拟客户与服务提供者相互交互的特定环境。这里的一个关键区别是，服务设计师通常会开发由人类服务提供者使用的脚本（Scripts）。服务设计团队创建所使用的工具和技术，以及支持该服务的工作流（Workflow）。相比之下，HCI 的工作通常仅关注客户和服务提供者所使用的计算设备（Computational Device）和界面（Interface）。HCI 和 UX 通常不会设计详细规定人们应如何开展工作的脚本。

为了降低部署那些在预期的[客户体验（customer experience）](https://www.interaction-design.org/literature/topics/customer-experience)以及服务提供者的服务执行能力方面均告失败的服务之风险，服务设计（service design）团队会对其服务设计进行原型制作（prototype），通过迭代地改进设计以降低或消除风险。在原型制作过程中，设计团队会评估并优化其设计，重点关注客户如何理解服务方案、设计如何满足客户需求，以及服务如何为客户和服务提供者双方创造价值 (Polaine, Løvlie and Reason, 2013)。服务原型制作通常始于需求验证（needs validation），即通过将初步的服务概念置于客户的显性或潜在需求（latent needs）框架下进行评估。随后，它将采取迭代原型（iterative prototypes）的形式，通过不断增加细节，以理解服务在物理和社会情境中是如何展开的，以及交付该服务需要哪些资源和接触点（touchpoints）。通常，体验原型（experience prototype）或用户演练（user enactment）——即一种旨在采样围绕服务的社会交互的构建原型——被用于评估拟议的服务 (Bucheneau and Fulton Suri, 2000; Odom et al., 2012)。

# 服务设计与 UX 设计的比较

服务设计（Service Design）与用户体验设计（UX Design）都关注于客户/用户体验。然而，服务设计明确的系统性方法（systemic approach）鼓励对问题空间（problem space）采取更整体的视角（holistic view），考虑更广泛的利益相关者（stakeholders），并处理远超数字系统交互范围的解决方案空间（solution space）。服务设计师致力于开发服务概念以及编排该策略的方案。相比之下，UX 设计师则专注于构建新系统或增强型计算系统（computational system）的原型。

UX 设计师在设计工作中具有强烈的技术导向（technology orientation），他们倾向于挑战可能性的边界。而服务设计师在选择使用何种技术时则显得更为保守。他们在工作中具有强烈的商业导向（business orientation），通常根据商业案例（business case）来选择技术。在实践中，UX 设计仅关注人们隐式或显式地与计算技术交互的触点。服务设计则没有这样的技术边界，其设计实践考虑了构成服务周围生态（ecology）的众多不同利益相关者的所有触点（touchpoints）。

分析-综合桥接模型（analysis-synthesis bridge model）（图 9）为讨论 UX 和服务设计提供了一个很好的框架。它将设计过程分为四个象限（Dubberly et al., 2008）。这两种设计实践都始于收集记录当前状态的数据...

这个世界。这包括调查用户/客户实践的实地研究（fieldwork），以及对详细记录用户/客户行为轨迹的计算机日志（computer logs）进行分析性研究。在此阶段，两种实践所采用的方法包括访谈（interviews）、观察（observations）、情境访谈（contextual inquiries）(Beyer and Holtzblatt, 1997)、定向[故事讲述](https://www.interaction-design.org/literature/topics/storytelling)（directed storytelling）(Evenson, 2006)、焦点小组（focus groups）、问卷调查（surveys）以及回顾性日志分析（retrospective log analysis）(Dumais et al., 2014)。

![](https://public-media.interaction-design.org/images/uploads/user-content/1445/K7yJcAkkJnR7zQhdem68UEHSqAmz6G0LMaQSap6R.png)
作者 / 版权持有者：Hugh Dubberly。版权条款和许可：保留所有权利。经许可转载。
图 9. 分析-综合桥接模型（Analysis-synthesis bridge model）。

这两种实践都涉及通过构建抽象模型来综合（synthesizing）收集到的数据，这些模型旨在描述世界的当前状态，并指出提升体验的机会。两者都涉及使用包含数百张便签的亲和图（affinity diagrams）(Hanington and Martin, 2012)。设计团队根据项目的亲和力对其进行聚类（cluster），以识别重要的主题。两者都涉及使用传统形式（如象限图 quadrant plots）来生成概念模型（conceptual models），并且两者都涉及创建全新的概念模型形式，以揭示数据中的重要关系 (Johnson and Henderson, 2002; Mendel, 2012)。两者都涉及使用流程图（flow diagrams）(Beyer and

(Holtzblatt, 1997) 详细描述了不同角色和任务之间的沟通模式（communication patterns）与失效（breakdowns），以及文化模型（cultural models, Beyer and Holtzblatt, 1997）的使用，后者展示了影响者（influencers）与被影响者（influencees），揭示了权力动态（power dynamics）中的问题与机遇。两者还涉及利益相关者地图（stakeholder maps, Hanington and Martin, 2012）的使用，用以捕捉系统中许多实体之间的关联关系。服务设计师几乎总是使用 [客户旅程图（customer journey maps）](https://www.interaction-design.org/literature/topics/customer-journey-map) (Nenonen et al., 2008) 和 [服务蓝图（service blueprints）](https://www.interaction-design.org/literature/topics/service-blueprint) (Bitner et al. 2008)，以便从客户的角度更好地理解服务的所有元素是如何连接的。UX 设计团队越来越多地采用这两种综合方法（synthesis methods）。诸如 IDEO 等 [交互设计（interaction design）](https://www.interaction-design.org/literature/topics/interaction-design) 机构推广这些方法的使用 (Richardson, 2010)，而 Cooper 甚至为 UX 设计师提供了详细的指导 (Samadzadeh, 2015)，具体阐述了 UX 设计师在何时以及如何使用这些方法。这两种实践都采用了多种方法来重新定义（Reframe）现状，为理想的未来设定目标，并构思旨在实现该目标的新产品和新服务供给（Service offerings）。它们的特点是使用了建模方法（Modeling approaches），例如展示未来系统的产品/服务路线图（Product/service roadmaps）或概念模型（Conceptual models）（Mendel, 2012）。两者都涉及使用[用户角色（Personas）](https://www.interaction-design.org/literature/topics/personas)来构思未来的用户/客户及其目标（Cooper, 1999）。此外，它们还包括创建情绪板（Mood boards），以挖掘用户/客户与未来产品之间可能存在的情感连接。

以及服务。它们还采用了[头脑风暴（brainstorming）](https://www.interaction-design.org/literature/topics/brainstorming)和身体风暴（bodystorming）来[构思（ideate）](https://www.interaction-design.org/literature/topics/ideation)许多可能的未来方案。两者还都涉及结合叙事（narrative）的[草图绘制（sketching）](https://www.interaction-design.org/literature/topics/sketching)，将故事讲述（storytelling）作为一种处理交互设计（interaction design）和服务执行（service performance）中时间维度的方法。

一旦确定了方向和目标，团队会同时利用这两者进行快速原型制作（rapid prototyping）；团队通过迭代地开发和评估设计想法，以降低产品和服务在发布时失败的风险。用户体验（User Experience, UX）中的原型制作通常要求关注可用性（usability），但它也包括对新技术的性能测试以及对用户体验的评估。服务的原型制作通常更为复杂、昂贵且耗时，因为设计往往涉及新的物理环境和新的员工执行表现。

当产品或服务从原型阶段过渡到发布阶段时，评估（evaluation）工作仍在继续。在此阶段，团队会制定衡量指标以追踪新设计的采用率（uptake），并经常采用 A/B 测试（A/B testing）对已发布的系统进行迭代修改，从而不断提升客户和用户体验。对于交互系统（interactive system）而言，这通常是指发布多个受控的

同一软件系统的不同版本。对于服务而言，这可能包括在特定区域对新产品进行[测试](https://www.interaction-design.org/literature/topics/test)发布。

这两种实践之间的一个重要区别在于设计过程的产出（output）。在用户体验设计（UX design）中，主要的交付物（deliverable）通常是一个可运行的原型（working prototype），用于演示技术并传达预期的用户体验。在服务设计（service design）中，主要的交付物通常表现为服务概念（service concept）以及一套服务组织在服务与客户之间共同创造价值（co-create value）的策略。这通常还包括一系列的人造物（artifacts），用以展示服务概念的不同具体体现（embodiments），以及将它们联系在一起的策略。服务概念提供了一个统一的愿景，有助于推动整个服务组织的决策和创新，使设计工作能够远远超出单个团队的范围。UX 设计师在工作时，通过想象交互系统的行为以及用户对此行为的反应，从而赋予这些行为具体的形式。而服务设计师在工作时，则通过想象客户与服务人员在触点（touchpoints）上的交互，从而赋予服务的执行（performance）具体的形式。在这两种实践中，设计师的大部分时间都花在想象和评估用户如何对系统行为做出反应，以及客户如何对服务执行做出反应。

## 技术导向与商业导向

UX 设计实践具有内在的强技术导向（technology orientation）。设计团队专门研究新兴技术如何满足或超越用户的需求与愿望。UX 社区的主要设计主题围绕着技术支柱展开，例如大数据（big data）、物联网（Internet of Things）、可穿戴设备（wearables）、量化自我（quantified self）、作为新 UX 的 AI、众包计算（crowd computing）和社会计算（social computing）。即使是 UX 设计中更偏向社会和群体导向的主题，如 HCI4D（面向发展中国家的人机交互）和可持续 UX（Sustainable UX），也涉及研究如何利用当前和新兴技术来应对这些大规模问题。新技术的发明仍然是 HCI 研究和 UX 设计实践的核心价值和驱动力。

相比之下，在服务设计（service design）中，人们会发现一种更为保守的技术使用方法。服务设计具有强烈的商业导向（business orientation），这要求在承担技术风险时需要更明确的理由。设计团队研究服务生态（service ecology）中不同利益相关者（stakeholders）之间的价值流动。设计师讨论并尝试不同的价值主张（value propositions），以激励他们期望的行为。虽然大多数 UX 设计流程很少将支付视为一种激励力量，但底层经济模型的设计仍然是服务设计的核心。服务设计师将当前和新兴技术视为一种颠覆性的

……力量。他们并不发明新技术，而是寻求部署已知技术的新方式，以及让这些系统转化为能够颠覆价值流（flow of value）的服务的新途径。他们将技术视为通过创建自助服务产品（self-service offerings）来降低服务交付成本（service delivery costs）的机会，同时也将其视为一种风险，因为他们注意到在服务接触（service encounters）过程中，与技术的交互可能会破坏客户与一线员工之间关系的建立（rapport building）(Giebelhausen et al., 2014)。

用户体验设计（UX design）旨在发明能够改善人们生活的新技术，而服务设计（service design）则旨在发明能够为客户和服务提升价值共创（value co-creation）的新商业模式。这两个领域的专业人士在探索过程中都极具创造力，但他们寻找解决方案的切入点不同。诸如 *免费增值（freemium）* 或 *应用内购买（in-app-purchase）* 等概念，更有可能产生于服务设计过程而非 UX 过程。而诸如在社交媒体发布的照片中自动标记好友，或移动设备上的文本自动纠错等想法，则更有可能源自 UX 设计过程而非服务设计过程。

这种导向上的差异可能源于 UX 和服务设计的起源。UX 源自人机交互（HCI），而 HCI 最初是计算机科学与心理学的协作产物。另一方面，服务设计则始于营销（marketing）与运营（operations）在……内部的协作。

商学院。尽管这两种设计实践在发展过程中已整合了许多其他学科视角，但其源自不同背景的取向（orientations）依然存在。

## 实践的重叠与边界

由于技术进步和经济模式的创新，服务设计（Service Design）与用户体验设计（UX Design）项目日益重叠。尽管如此，每项实践在边界上的差异使得两者易于区分。

服务设计与 UX 设计产生重叠的一个主要原因，在于服务环境（Service Environments）中技术应用的日益增加。早期的例子包括销售点系统（Point-of-Sale Systems），这些系统可以追踪购买记录、更新库存、检索之前的订单或预约，或者允许订购缺货商品。随后出现了一波自助服务系统（Self-service Systems），它们通常取代了前线服务员工（Frontline Service Employees），包括自动柜员机（ATM）、自助加油泵、航空公司自助值机亭以及交通票务自动售票机。在某些情况下，自助服务系统被整合到更大规模的服务重新设计项目中，而几乎没有考虑到 UX 设计。Norman 曾以那些令人沮丧且令人困惑的交通票务自动售票机为例，说明将自助服务系统置于服务环境中而缺乏 UX 考量的情况 (Norman, 1988)。虽然自助服务系统的经济层面和用户对效率的追求可能得到了充分考虑，但其 UX 层面却失败了。另一个重叠领域始于传统的实体服务（brick-and-mortar services）开始提供允许客户完成各种交易的网站。例如，零售店的在线订购、酒店的在线预订、航空公司的在线购票，以及政府机构提供的信息查询或许可证/准证申请。最初，这些项目主要被视为用户体验（User Experience, UX）项目来执行，且通常与服务的前线员工端（frontline employee side）运作得非常独立。然而，随着在线交互的数量及其复杂程度持续激增，近年来的项目在服务设计（service design）与 UX 之间变得更加集成。公司通常拥有一个与整体战略截然不同的数字化战略（digital strategy），甚至设有独立于其他服务设计活动的数字化设计团队。

截至...结束时（By the close of the）

进入 2010 年代，这种界限变得更加模糊。智能手机的快速普及、旨在增强顾客店内体验的应用程序（Apps）的近期发展，以及传统实体店（Brick-and-mortar）服务中自助服务终端（Kiosks）的日益增加，促使许多服务设计师（Service Designers）与用户体验（UX）设计师开展协作。此外，这一现象还见证了许多 UX 设计师向 UX 服务设计师的转型。Starbucks 的移动应用程序提供了一个很好的例子，展示了公司提供的各类店内服务，包括忠诚度计划（Loyalty programs）、产品描述、促销活动以及远程下单并在店内取货（图 10）。该应用甚至能提供店内当前播放的歌曲名称。

这些日益增加的重叠案例主要由新技术的能力提升所驱动，旨在提高顾客的效用（Utility）同时降低整体成本，例如用自助服务终端、网站或应用程序取代员工。许多公司现在采用了 *全渠道（Omni-channel）* 服务交付的概念，即顾客希望并期待能够利用服务提供的任何且所有渠道（包括店内、电话、网页和移动应用）来完成交易的任何部分 (Brynjolfsson et al., 2013)。

![](https://public-media.interaction-design.org/images/uploads/user-content/1445/BADGF9w0VFIIABXTnAa7kDqbqxNBgVlipbdLBdDP.png)
Author / Copyright holder: Starbucks Coffee Company. Copyright terms and

版权所有。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。

图 10. Starbucks 应用程序，包含店内功能，如支付、兑换忠诚度奖励（loyalty rewards）以及当前播放的歌曲名称。

点对点经济（Peer-economy）服务是服务设计（service design）与用户体验设计（UX design）之间日益增加的重叠的另一个例子。对于点对点经济而言，技术创新（智能手机的日益普及和移动网络速度的提升）与经济模式创新（颠覆传统服务的模式）起到了同等重要的作用。点对点服务——例如 KickStarter（针对从产品到电影等项目的众筹，挑战了银行和投资者的传统用途）；Airbnb（人们向旅行者出租房间，挑战了酒店的传统用途）；Uber（人们通过提供车辆接送来获利，挑战了出租车的传统用途）；以及 Mechanical Turk（由个人完成分布式微任务的众包，挑战了传统的员工雇佣方式）——都在挑战传统的服务模式。这些服务的成败取决于用户体验的质量，以及其底层经济模式创造价值的能力。与许多专注于单一消费者体验的 UX 项目不同，这些服务要求设计团队在创造价值的同时，构思出两个不同利益相关者（stakeholders）之间有效的交换生态（ecology of exchange）。

对于将这些利益相关者（Stakeholders）聚集在一起的服务提供者而言，只有当用户体验设计（UX Design）和服务设计（Service Design）有效地协同工作时，这些服务才能正常运作。

尽管 UX 设计和服务设计的重叠程度日益增加，但人们可以通过它们在实践边缘所设定的边界来轻松区分这两种实践。大多数 UX 设计师和 UX 项目将自身局限于与计算系统（Computational System）之间发生的交互。虽然设计团队会考虑该交互之外的许多因素，但他们实际设计的是计算系统的行为，从而形成了这一边界。服务设计师并不遵循任何技术边界，而是将工作范围限定在他们所负责的具体服务的边缘。再次以 Starbucks 为例，UX 设计团队会设计公司网站、移动应用程序以及一线员工使用的销售点系统（Point-of-Sale system）的行为。服务设计师则会额外设计一线员工的工作流程（Work routines），例如在杯子上写顾客的名字，或者将顾客的订单转化为一种统一的语言，以便点单员工进行标记，从而确保咖啡师（Barista）制作出正确的饮品。虽然 UX 团队设计员工使用的工具，但他们并没有设计员工应如何执行工作的历史。服务设计师还会考虑门店环境的设计，以及门店在不同地点的布局，例如

机场、酒店以及带状购物中心（strip malls）。这类工作远远超出了目前用户体验设计（User Experience design, UX design）的实践范畴。

# UX 实践中服务思维的机遇

多年来，UX 设计一直作为技术产品和服务设计的标准实践发挥着良好作用。HCI（人机交互）从狭隘地关注可用性（Usability）和易用性（Ease of Use）演变为对用户体验（User Experience）更广泛的考量，使其在技术开发社区中的影响力日益增强。然而，当前 UX 设计工作中的三个主题将从服务思维（Service Thinking）中获益：软件即服务（Software as a Service, SaaS）、社交计算（Social Computing）以及面向社会变革的设计（Design for Social Change）。

## 软件即服务（Software as a Service）

与其他行业一样，软件行业一直在改变其底层的经济模型。它正从“软件作为产品”转向“软件即服务（Software as a Service, SaaS）”。在这种新模型下，客户通常订阅他们想要使用的软件，并支付定期的月费或年费。许多服务模型还采用了基于客户软件使用量或相关底层资源的动态定价（variable pricing）。熟悉 Adobe 软件的设计师最近经历了从产品模型到服务模型的转变，因为 Adobe 开始对其创意软件套件（creative suite of software）收取月费。SaaS 具有多项优势，包括降低开始使用服务的成本，以及消除了软件作为产品销售时常见的版本管理问题（versioning problems）。它还能产生更强大的客户行为分析（analytics），从而使服务提供商获益。

绝大多数商业软件都采用了 SaaS 模型；因此，用户体验（UX）设计团队在根本上始终是在设计服务而非产品。对于在浏览器中运行的在线工具/服务，以及售价 99 美分或通常免费的移动应用程序而言，这一点尤为明显。免费在线工具的兴起以及智能手机和其他移动设备的飞速发展，加速了软件行业向服务模型的转型。此外，这增加了 UX 设计的复杂性，因为...的用户...

免费服务或 99 美分的应用程序几乎从未将用户视为客户（customer）；因为用户并不支付软件的开发与维护成本。在大多数情况下，用户实际上成为了软件公司向第三方（third parties）出售的产品。在设计实践（design practice）中，用户体验（UX）设计团队需要考虑这些第三方的需求，他们必须设计能够捕捉第三方感兴趣之行为的交互（interactions），或者传递第三方希望用户接收的信息。在此类情境下进行设计时，服务设计师（service designers）关注客户与服务提供者（service providers）之间的价值共创（co-creation of value），这有助于挖掘更合适的设计机会（design opportunities）。有证据表明，服务思维（service thinking）正逐渐融入到...

当前的 UX（User Experience）实践中，越来越多地使用诸如“引导（onboarding）”之类的术语——这是一个传统的商业术语，用于描述新员工接受公司实践和文化培训的过程 (Bradt and Vonnegut, 2009)。现在，UX 设计师通常用它来描述允许用户创建账户并开始使用新服务的交互设计 (Hess, 2010)。

![](https://public-media.interaction-design.org/images/uploads/user-content/1445/2qV4N2Q0VAhaHdfnNhsvBUmklF1N1JJ0MEx7aZLG.jpeg)
作者/版权持有者：Duolingo, Netflix, Inc 和 Uber Technologies, Inc。版权条款和许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。

图 11。这三个熟悉的移动应用服务（DuoLingo, Netflix 和 Uber）采用了三种不同但常见的经济模型。DuoLingo 采用的是*免费增值（freemium）*模型；包含一个带有广告的免费服务层级和一个不含广告的付费服务层级。Netflix 采用的是*分级固定定价（tiered, fixed pricing）*；客户为不同级别的服务支付固定的月费。Uber 采用的是*按量计费（usage）*模型；客户根据其使用的服务量支付费用。

## 社会计算（Social Computing）

社会计算（Social Computing）长期以来一直是人机交互（HCI）领域的一个研究课题。随着 Twitter, Facebook, Foursquare, Instagram 和 Snapchat 等社交媒体服务的极高普及率，以及从 Wikipedia（群众策展百科全书）、Yelp（基于位置的服务群众评论和评分）、Waze（群众生成的交通和驾驶信息）到 Mechanical Turk（全球群众工作场所）等群众驱动服务（Crowdpowered services）的兴起，社会计算服务的设计已成为 UX 设计实践的主流部分。

从事社会计算项目的 UX 设计师可以从服务设计（Service design）的系统化方法（Systemic approach）中获益。除了 UX 关注于满足并超越用户的需求和欲望之外，他们的工作实际上是构思一套利益相关者（Stakeholders）之间可持续的交换生态（Sustainable ecology of exchange）。例如，Instagram 需要内容创作者（制作并分享图像的名人、艺术家、家人和朋友）、内容消费者（查看并点赞图像的人）以及希望向内容消费者推广产品和服务的广告商。Yelp 需要源源不断地有想要获取本地化服务评论的用户、愿意生成这些服务评论的用户，以及在 Yelp 上购买广告以推广其服务的服务供应商。高效的 UX 设计团队致力于考虑该生态系统中所有组成部分的需要和欲望，并开发基于 Web 和 App 的界面，让他们能够查找信息、分享

信息，或监控服务的使用情况，以便对其进行调优（Tune），使其更加高效。

## 面向社会变革的设计（Design for Social Change）

在用户体验（UX）的 [设计教育](https://www.interaction-design.org/literature/topics/design-education)、研究和实践中，人们对面向社会变革的设计（Design for Social Change）产生了越来越浓厚的兴趣。设计团队越来越多地利用设计思维（Design Thinking）和通信技术的进步来应对社会层面的问题，包括可持续性（Sustainability）、公共卫生与健康、公民参与社区改善以及发展中国家面临的挑战。这些项目通常关注新技术的颠覆性力量（Disruptive power）如何为人们改善生活创造新机遇。由于 UX 设计与技术之间深厚的联系及其创新导向，它在这一领域发挥了核心作用。

从事此类项目的 UX 设计团队可以从服务设计（Service Design）的两个方面获益。对于其中许多（如果不是大多数）项目而言，其重点更多在于实现公共利益（Public good），而非关注寻求消费选择（Consumptive choice）的个体用户的需求和欲望。用户需求依然至关重要，但必须将其置于更大的项目目标背景之下。服务思维（Service thinking）能够使 UX 团队获益，因为它关注于众多利益相关者（Stakeholders）之间以及跨部门的价值共创（Co-creation of value）。此外，借助通信技术可以帮助应对这些大规模挑战；在大多数情况下，如果这些系统没有被整合到其他服务中，其影响力将十分有限。

……产品服务，或与政策变更相结合。服务设计（Service Design）能够突破个体与技术系统交互的边界，从而实现对解决方案更整体（holistic）的探索。

# 预测未来

下文中，我们对 UX/HCI（用户体验/人机交互）与服务设计（Service Design）之间的关系将如何继续演变与交互进行了推测。我们将从设计实践、设计教育和设计研究三个方面展开讨论。

## 未来的设计实践

UX 设计师在工作中已经经常像服务设计师一样思考，尤其是当他们使用服务蓝图（Service Blueprints）和用户旅程图（Customer Journey Maps）来综合分析数据时。这些工具迫使设计团队去考虑用户在整个服务过程中与非计算触点（Non-computational touchpoints）的交互。同时，这些工具也强化了对用户与服务之间相互作用的系统性视角（Systemic view）。在这种意义上，UX 设计师现在以及将来都将继续实践服务设计，即便他们不称自己为服务设计师，甚至没有意识到自己正日益深入地从事服务设计。

随着时间的推移，我们预计 UX 设计将成为服务设计的一个高度专业化的子学科（Sub-discipline）。我们认为这类似于建筑学（Architecture）与城市设计（Urban Design）之间的关系，其中城市设计已成为一个拥有特定关注点和技能集的高度专业化子学科。在这种对未来设计实践的推测中，几乎所有的项目都将是服务设计项目；而当团队开始勾勒并构建交互式计算系统的行为原型时，他们将依托于在 UX 实践方面拥有深厚经验的团队成员，由其主导并指导设计决策。

## 未来设计教育

用户体验设计（UX Design）在设计教育领域经历了巨大的增长。自 20 世纪 90 年代以来，许多新的交互设计（Interaction Design）硕士项目相继启动。近期，本科课程也开始提供 UX 设计学位，且许多在线教育和培训服务开始提供 UX 设计的课程和证书。这种增长似乎在很大程度上是由行业对具备这些技能的人才的需求所驱动的。服务设计（Service Design）自 20 世纪 90 年代以来也有所增长，但速度明显较慢。虽然有数百个 UX 项目可供选择，但提供服务设计学位的项目仅有 30 个左右。

我们预测这种情况可能会发生变化。如果行业需求发生变化，开始需要服务设计师，我们预计许多项目将重新调整其 UX 课程，以培养同时接受过服务设计和 UX 设计交叉培训（Cross-trained）的学生。再次强调，两者的方法和流程实际上非常相似。此外，我们推测商学院可能会进入这一领域，并开始提供更侧重于业务流程（Business Processes）的服务设计学位。在商学院或设计学院以外的部门中，已经出现了一些将设计思维（Design Thinking）与商业相结合的新项目。此外，商学院提供设计思维培训和课程的情况也日益增多。

## 未来设计研究

服务设计（Service Design）与用户体验设计（UX Design）正朝着同一个未来演进，这主要受到技术持续进步以及随之而来的社会变革的驱动。我们认为有几个研究重点将对这两个领域日益重要，具体包括：

**大数据与人工智能（Big Data and AI）**：大数据（Big Data）的收集与利用，结合人工智能（AI）的持续进步，引发了一系列设计研究课题。这些课题涵盖了从数据隐私、服务透明度、算法偏见（Algorithmic Bias）等伦理问题，到进行特定推断的伦理考量，例如利用性别、种族或社会阶层对特定群体进行负面定型。此外，还存在一些更基础的设计研究问题，例如如何利用数据进行设计，以及如何将 AI 作为一种设计材料（Design Material），从而构思出那些即便拥有[机器学习](https://www.interaction-design.org/literature/topics/ai)博士学位的人也难以想象的事物。

**社会设计（Social Design）**：社会正义与可持续性等大规模社会问题在设计研究中变得日益重要，且我们预计这一趋势将持续。技术进步将持续提供新的解决方案路径，但同时也会带来新的非预期后果（Unintended Consequences）；因此，我们认为在该领域采用服务设计中系统性视角（Systemic Perspective）的设计研究将继续增长。

**全球设计（Global Design）**：

随着应用程序和在线服务的增长，在全球规模（Global Scale）上进行设计正面临着日益严峻的挑战，即如何设计能够在全球范围内运行的产品和服务；这些产品和服务既要尊重当地规则、文化规范并符合当地法律，又要让用户在访问和使用一套熟悉且个性化的工具和服务时，能够无缝地在全球范围内活动。我们目前尚不清楚如何设计这类产品，并且我们预计这将成为设计研究的一个新课题，该课题将结合用户体验设计（UX Design）在技术方面的专业知识，以及服务设计（Service Design）的系统性视角（Systemic Perspective）及其对用户在多种触点（Touchpoints）中连续展开的体验的关注。

# 更多学习资源

有许多途径可以深入学习服务设计（Service Design）。

Andy Polaine, Lavrans Løvlie 和 Ben Reason 撰写了一本极佳的描述服务设计实践的著作：《Service Design: From Implementation to Practice》(Polaine et al., 2013)。

[Service Design Network](https://www.service-design-network.org/) 是获取信息以及结识服务设计从业者的绝佳渠道。他们举办年度会议，在世界各大城市开展活动，并出版专注于服务设计实践的期刊 *Touchpoint*。

[Journal of Service Research](https://journals.sagepub.com/home/jsr) 是一本探讨服务研究相关学术问题的学术期刊。

服务设计及其与用户体验（User Experience, UX）和人机交互（Human-Computer Interaction, HCI）的关系，也是 [Medium](https://medium.com/) 上设计类文章经常讨论的话题。

# References

Beyer, H., & Holtzblatt, K. (1997). *Contextual design: defining customer-centered systems*. Elsevier.
Bitner,
 M. J., Booms, B. H., & Tetreault, M. S. (1990). The service 
encounter: diagnosing favorable and unfavorable incidents. *The Journal of Marketing*, 71-84.
Bitner, M. J., Ostrom, A. L., & Morgan, F. N. (2008). Service blueprinting: a practical technique for service innovation. *California management review*, *50*(3), 66-94.
Bradt, G. B., & Vonnegut, M. (2009). *Onboarding: How to get your new employees up to speed in half the time*. John Wiley & Sons.
Buchenau,
 Marion, and Jane Fulton Suri. "Experience prototyping." In Proceedings 
of the 3rd conference on Designing interactive systems: processes, 
practices, methods, and techniques, pp. 424-433. ACM, 2000.
Brynjolfsson, Erik, Yu Jeffrey Hu, and Mohammad S. Rahman. *Competing in the Age of Omnichannel Retailing*. MIT, 2013.
Chai, K. H., Zhang, J., & Tan, K. C. (2005)*. *A TRIZ-based method for new service design*. Journal of Service Research*, 8(1), 48-66.
Christensen,
 CM., Raynor, ME. The Innovator's Solution: Creating and Sustaining 
Successful Growth, Harvard Business School Press, Cambridge, MA, USA, 
2003.
Cooper, A. (1999). *The inmates are running the asylum:(Why high-tech products drive us crazy and how to restore the sanity)* (Vol. 261). Indianapolis: Sams.
Cox,
 A., Duhigg, C., G.V. Xaquin, Grondahl, M., Park, H., Roberts, G, and

Russell, K. (2013). The iPhone Economy: A Shift From Manufacturing. New 
York Times, [http://www.nytimes.com/interactive/2012/01/20/business/the-iphone-economy.html?scp=51&sq=product+manufacture&st=nyt](https://www.google.com/url?q=http%3A%2F%2Fwww.nytimes.com%2Finteractive%2F2012%2F01%2F20%2Fbusiness%2Fthe-iphone-economy.html%3Fscp%3D51%26sq%3Dproduct%2Bmanufacture%26st%3Dnyt&sa=D&ust=1458840343329000&usg=AFQjCNEuPH2bNCoLT0Mfdq48JE1PERDDsQ), accessed September 15, 2014.
Dubberly, H., & Evenson, S. (2008). On modeling: The Analysis-synthesis Bridge Model. *Interactions*, 15(2), 57-61.
Dumais,
 S., Jeffries, R., Russell, D. M., Tang, D., & Teevan, J. (2014). 
Understanding user behavior through log data and analysis. In *Ways of Knowing in HCI* (pp. 349-372). Springer New York.
Evenson, S. (2006). Directed storytelling: Interpreting experience for design. *Design Studies—Theory and Research in *[*Graphic Design*](https://www.interaction-design.org/literature/topics/graphic-design)*, a Reader*, 231-240.
Giebelhausen,
 Michael, Stacey G. Robinson, Nancy J. Sirianni, and Michael K. Brady. 
"Touch versus tech: When technology functions as a barrier or a benefit 
to service encounters." *Journal of Marketing* 78, no. 4 (2014): 113-124.
Goldstein,
 Susan Meyer, Robert Johnston, JoAnn Duffy, and Jay Rao. "The service 
concept: the missing link in service design research?" *Journal of Operations management* 20, no. 2 (2002): 121-134.

Hanington, B., & Martin, B. (2012). *Universal methods of design: 100 ways to research complex problems, develop innovative ideas, and design effective solutions*. Rockport Publishers.
Hess,
 W. (February 16, 2010). Onboarding: Designing Welcoming First 
Experiences: You don't get a second chance to make a first impression. *UX Magazine*. Article No: 487. [https://uxmag.com/articles/onboarding-designing-welcoming-first-experiences](https://uxmag.com/articles/onboarding-designing-welcoming-first-experiences)
Holmlid, Stefan. "Interaction design and service design: Expanding a comparison of design disciplines." *Proceedings of NORDES* (2009).
Johnson, Jeff, and Austin Henderson. "Conceptual models: begin by designing what to design." *Interactions, 9*,1 (2002): 25-32.
Mendel, J. (2012). A taxonomy of models used in the design process. [http://www.dubberly.com/articles/taxonomy-of-models.html](http://www.dubberly.com/articles/taxonomy-of-models.html)
Luca, Michael. "Reviews, reputation, and revenue: The case of Yelp. com." (September 16, 2011). *Harvard Business School NOM Unit Working Paper 12-016*.
Lusch, Robert F., and Stephen L. Vargo. "Service-dominant logic: reactions, reflections and refinements." *Marketing theory* 6, no. 3 (2006): 281-288.
Morelli, Nicola. "Product-service systems, a perspective shift for designers: A case study: the design of a telecentre." *Design Studies* 24, no. 1 (2003): 73-99

Nenonen, S., Rasila, H., Junnonen, J. M., & Kärnä, S. (2008). Customer Journey–a method to investigate user experience. In *Proceedings of the Euro FM Conference Manchester* (pp. 54-63).
Norman, D. A. (1988). *The psychology of everyday things*. Basic books.
Normann, Richard. *Reframing business: When the map changes the landscape*. John Wiley & Sons, 2001.
Odom,
 William, John Zimmerman, Scott Davidoff, Jodi Forlizzi, Anind K. Dey, 
and Min Kyung Lee. "A fieldwork of the future with user enactments." In *Proceedings of the Designing Interactive Systems Conference*, pp. 338-347. ACM, 2012.
Payne, Adrian F., Kaj Storbacka, and Pennie Frow. "Managing the co-creation of value." *Journal of the academy of marketing science* 36, no. 1 (2008): 83-96.
Polaine, A., Løvlie, L., & Reason, B. (2013). *Service design. From Implementation to Practice*. New York: Reosenfeld Media.
Prahalad, Coimbatore K., and Venkatram Ramaswamy. "Co-opting customer competence." *Harvard Business Review* 78, no. 1 (2000): 79-90.
Prahalad, Coimbatore K., and Venkat Ramaswamy. "Co-creating unique value with customers." *Strategy & leadership* 32, no. 3 (2004): 4-9.
Richardson, Adam. 2010. “Using Customer Journey Maps to Improve Customer Experience.” *Harvard Business Review*. [https://hbr.org/2010/11/using-customer-journey-maps-to](https://hbr.org/2010/11/using-customer-journey-maps-to)

Samadzadeh, Shahrzad. 2015. “Customer Journey Map or Service Blueprint?” [http://www.cooper.com/journal/2015/5/journey-map-or-service-blueprint](http://www.cooper.com/journal/2015/5/journey-map-or-service-blueprint)
Sevaldson, B. (2011). “GIGA-Mapping: Visualisation for complexity and systems thinking in design.” Nordes, (4).
Vargo, Stephen L., and Robert F. Lusch. "Evolving to a new dominant logic for marketing." *Journal of Marketing* 68.1 (2004): 1-17.
**Chapter TOC**
[**Interaction Design for Usability**](https://www.interaction-design.org/courses/interaction-design-for-usability)
![](https://public-media.interaction-design.org/images/courses/hds/course_43--square_thumbnail.jpg?tr=fo-auto)
Interaction Design for Usability
Closes in
0
days
06
hrs
25
mins
54
secs
booked
View Course

## 获取每周用户体验（User Experience, UX）洞察

加入 **314,524 位设计师** 的行列，通过我们的时事通讯（Newsletter）获取实用的 UX 技巧。
需要提供有效的电子邮件地址。

## 本章涵盖的主题：

[服务设计（Service Design）](https://www.interaction-design.org/literature/topics/service-design)
