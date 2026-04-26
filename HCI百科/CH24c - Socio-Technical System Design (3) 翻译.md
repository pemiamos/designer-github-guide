# 24. 社会技术系统设计 (Socio-Technical System Design) (3)

**来源**：The Encyclopedia of Human-Computer Interaction, 2nd Ed.
**Notion 原页面**：https://www.notion.so/c0b0dc5308c142ca95fafa659036e731

---

[Brian Whitworth](https://www.interaction-design.org/literature/author/brian-whitworth) 和 [Adnan Ahmad](https://www.interaction-design.org/literature/author/adnan-ahmad)

### 24.4.14 实现（Implementation）

传统的访问控制执行（Access Control Enforcement）是通过安全内核（Security Kernel）机制实现的。安全内核是一个可信的软件模块，它拦截提交给系统的每一个访问请求调用，并根据特定的访问策略模型（Access Policy Model）决定该请求应被允许还是拒绝。通常，系统采用集中式方法，由一个策略决策点（Policy Decision Point）处理所有资源请求。用户看到的要么是执行动作的结果，要么是权限被拒绝的消息。由于社交网络系统（SNSs）拥有数百万用户，因此集中式或半去中心化的证书（Certificates）会成为瓶颈。这一点，加上内容贡献者对本地所有权（Local Ownership）的社交需求，表明应采用分布式证书策略来实现此处概述的 ACS 策略模型。允许本地策略决策点处理资源请求，也能确保本地用户对资源的控制权。如果分布式证书存储在利益相关者的命名空间（Namespace）中，则只有该用户才能访问和修改它们（图 20）。

![](https://public-media.interaction-design.org/images/encyclopedia/socio-technical_system_design/Distributed_access_control_model_architecture.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

**图 24.20**：分布式访问控制模型架构

### 24.4.15 总结

一个合法的 ACS 模型可以通过为对象（Objects）和空间（Spaces）分配所有者（Owner）、父级（Parent）、祖先（Ancestor）、后代（Offspring）以及本地公共角色（Local Public Roles）来管理权限（Rights）。推导出的 ACS 公理如下：

1. *所有非空实体权限都应分配给参与者（Actors）*。
2. *一个 Persona（人格/角色）应当由其自身所有*。
3. *每个实体都有一个父级空间，最高至系统空间（System Space）*。
4. *任何使用对象的权限都隐含了查看该对象的权限*。
5. *任何通信行为都应事先获得相互同意*。
6. *角色（Role）是以通用形式表达的权限，表现为指针或集合*。
7. *空间所有者可以在无需其所有者许可的情况下，禁止或允许某个 Persona 进入*。
8. *元权限（Meta-right）是指分配任何实体权限（包括其自身）的权限*。
9. *创建始终是对空间的某种行为，最高至系统空间*。
10. *新实体的创建者应立即获得该实体的所有权限*。
11. *一个人可以提前查看任何可能适用于他们的权限*。
12. *空间所有者应具有查看任何后代（Offspring）的权限*。
13. *实体所有者应能够进入任何祖先空间（Ancestor Space）*。
14. *在空间中展示实体需要 Persona 和空间所有者的共同同意*。
15. *为了在空间中展示实体，实体所有者需向空间所有者授予查看元权限（View Meta-rights）*。
16. *委派（Delegating）并不赋予进一步委派的权限*。
17. *将现有的对象使用权限分配给某人需要其同意*。
18. *为现有对象分配空权限（Null Rights）或分配创建权限不需要同意*。

以上是社会性要求（social requirements）而非技术必要性（technical necessities），旨在实现社会可持续性（social sustainability）。我们目前正在将该模型形式化（formalizing），以将其作为任何社会技术系统（socio-technical system）的社会交互标准（social interaction standard）。

### 24.4.16 讨论问题

请从以下列表中选择部分问题进行研究。如果您是在大学或商业课程的课堂上阅读本章，可以两人一组研究这些问题，并向全班汇报，同时提供理由和示例。

1. 什么是访问控制（Access Control）？哪些类型的计算机系统使用了它？哪些没有？它在传统上是如何运作的？社交网络如何对此提出挑战？访问控制又是如何应对的？
2. 从人类的角度来看，什么是权利（Right）？它是一种指令（Directive）吗？权利是如何作为信息被表示的？请举例说明。传递的权利称作什么？请举例说明。
3. 用户（User）和行动者（Actor）之间有什么区别？对比用户目标和行动者目标。为什么行动者对于在线社区的演化至关重要？
4. 一个人总是公民（Citizen）吗？社区如何要求公民承担责任（Accountability）？如果一辆车撞死了一只狗，车需要承担责任吗？那么为什么驾驶员需要承担责任？如果在线软件欺骗了用户，软件需要承担责任吗？如果不需要，那么谁需要？请举例说明。如果自动竞价程序导致股市崩盘并使数百万人失业，谁应该承担责任？我们可以将此归咎于技术吗？
5. 对比实体（Entity）和操作（Operation）。什么是社会实体（Social Entity）？在线人格（Online Persona）是一个人吗？人格是如何被激活的？这是否是在“占据”一个在线身体？人格“真正”是你吗？如果一个程序激活了一个...

人格面具 (Persona) 是一种在线僵尸 (online zombie) 吗？哪些在线程序会用你的名字向你问好？你喜欢这样吗？如果一个网上银行网站每次都用你的名字欢迎你，这是否建立了一种关系？你是在与谁建立关系？

1. 估算你每天与技术交互 (interact) 的时长。请诚实回答。其中，与在线程序交互的时间与与人交互的时间分别是多少？你更倾向于哪一种？有任何在线程序是你的朋友吗？尝试使用可以对话的手机助手（如 Siri）。要求它成为你的*私人*朋友，并记录这次对话。如果 AI 得到了提升，你会想要一个个人 AI 朋友吗？

1. 是否所有的权利 (rights) 都必须被分配？哪些权利必须被分配？为什么？谁来管理在线权利？AI 程序是否对其被分配的权利承担问责 (accountable)？在 USS Vincennes 悲剧中，击落伊朗民航客机的计算机程序是否被追究责任？为什么没有？导致错误的原因是什么？之后发生了什么变化？

1. 谁应该拥有一个人格面具 (persona)，为什么？针对三个社会技术系统 (Social-Technical Systems, STSs)，创建一个新的人格面具，使用它进行连接，尝试编辑它，然后将其删除。比较你可以更改和不能更改的属性。如果你将其完全删除，还剩下什么？你能将其恢复 (resurrect) 吗？描述两种加入在线社区的方式。哪一种更简单？哪一种更安全？

1. 请举例说明目前针对人格面具的遗弃 (abandonment)、转移 (transfer)、委派 (delegation) 和孤立 (orphaning) 等社会问题的技术应对方案。在每种情况下，你有什么建议？

1. 为什么选择如何向他人展示自己对于社交 [此处原文中断] 如此重要？

...生物？这种控制权称作什么？谁有权在电话簿列表中显示你的姓名？谁有权将其删除？同样的情况是否适用于在线注册列表（Online Registry Listing）？调研三个在线案例并报告其处理方式。

1. 信息实体（Information Entities）与对象（Objects）有何不同？空间（Spaces）与项目（Items）有何不同？对象层级（Object Hierarchy）是什么，它是如何产生的？第一个空间是什么？哪些操作（Operations）适用于空间而不适用于项目？哪些操作适用于项目而不适用于空间？项目能变成空间吗？空间能变成项目吗？请举例说明。

1. 评论（Comments）与消息（Messages）有何不同？将评论权定义为一个 AEO 三元组（AEO Triad）。如果一个评论变成了空间，它称作什么？请通过三个评论类社会技术系统（STSs）进行演示。对于允许“深度”评论（评论的评论的评论，以此类推）的系统，其内部机制是怎样的？（观察谁添加了内容）。聊天式的对话功能是否会比如此多的缩进（Indents）更简单？

1. 对于以下每个操作集（Operation Set），请解释其区别，给出示例，并提供另一种变体：
  - *删除（Delete）*：删除（Delete）、撤销删除（Undelete）、销毁（Destroy）。
  - *编辑（Edit）*：编辑（Edit）、追加（Append）、版本化（Version）、回滚（Revert）。
  - *创建（Create）*：创建（Create）。
  创建与编辑之间有什么区别？请定义第四个操作集。

1. 查看一个对象是否是对该对象的一种操作？查看一个人是否是对该人的一种操作？查看如何成为一种社会行为（Social Act）？查看在线对象能成为一种社会行为吗？为什么查看对于社会问责（Social Accountability）是必要的？

1. 什么是通信（Communication）？信息传输是否属于通信，例如下载（Download）？为什么通信需要相互同意（Mutual consent）？如果不是相互的会发生什么？开启通道（Opening a channel）与发送消息有何不同？发送者对接收者可以是匿名的吗？接收者对发送者可以是匿名的吗？发送者或接收者对传输系统（Transmission system）可以是匿名的吗？请描述能够实现通道控制（Channel control）的在线系统。

1. 请针对固定电话（Landline phone）、移动电话（Mobile phone）和 Skype 回答以下问题：通信请求是如何呈现的？接收者会获得哪些信息，他们有哪些选择？匿名发送者的情况如何？如何创建地址簿（Address list）？还有哪些其他不同之处？

1. 什么是角色（Role）？角色可以是空的（Empty）或无效的（Null）吗？角色在何方面类似于数学变量（Maths variable）或计算指针（Computing pointer）？请举出三个流行的社会技术系统（Socio-Technical Systems, STSs）中的角色示例。为每个示例提供 ACS 三元组（ACS triad），并说明哪些值是可变的。还有哪些其他值可能发生变化？基于此建议一些新的有用角色。

1. 根据定义，角色是如何变化的？针对三个不同的 STSs，描述每种角色变体类型（Role variation type）是如何运作的。请给出三个已实现角色的不同示例，并建议三个未来的发展方向。

1. 如果你删除一个人的好友关系（Unfriend），对方应该被通知吗？请 [测试](https://www.interaction-design.org/literature/topics/test) 并报告在三个常见的社交网络（Social Networks, SNs）中实际发生了什么。被禁言的公告板“挑衅者”（Flamer）必须被通知吗？被踢出聊天室的人又如何？这里的一般原则是什么？

1. 什么是元权利（meta-right）？请给出物理环境和在线环境的示例。它与其他权利有何不同？它仍然是一种权利吗？ACS 能在元权利上执行操作吗？是否存在 ACS 的元元权利（meta-meta-rights）？如果不存在，原因是什么？那么，“拥有（own）”一个实体意味着什么？

2. 为什么 ACS 创建一个项目的行为不能被视为是对该项目的操作？为什么它不能是对“无（nothing）”的操作？那么，它究竟是对什么的执行操作？请用在线示例进行说明。

3. 谁拥有一个新创建的信息实体（information entity）？依据什么样的社会原则？这种情况是否必然如此？请寻找一些你在网上创建了某个东西但并不完全拥有它的在线案例。

4. 在一个空间（space）中，最初谁拥有在该空间内创建的权利？随后，其他人如何在该空间中创建？什么是创建条件（creation conditions）？其合理性依据是什么？请阐述对象（object）、操作（operation）、访问（access）、可见性（visibility）和编辑条件（edit conditions）。透明度（transparency）在此如何适用？

5. 给出在空间中创建实体的三个示例。对于每个示例，请明确所有者（owner）、父级（parent）、祖先（ancestors）、后代（offspring）和局部公众（local public）。所有者可以更改哪些角色？

6. 针对五种不同的社会技术系统（Social-Technical Systems, STS）体裁，给出在线创建条件的示例。在每种体裁中创建一些内容。结果是否具有透明度？请寻找两个非透明创建的示例。

7. 针对以下情况，解释原因（为什么可以或不可以）。假设你是一个拥有多个分论坛（tracks）的计算机会议的主席。分论坛主席是否应该能够将你排除在外，或者向你隐藏某篇论文？你是否应该能够

能否从其分会场（track）中删除一篇论文？他们能否查看其他分会场的论文？分会场主席（track chair）是否应该能够将误提交至其分会场的论文移动到另一个分会场？调研并报告你在学术会议管理在线系统中发现的相关评论。

1. 一个在线社区将一个议题提交给成员投票。请评估以下社会技术系统（Social Technical Systems, STS）选项：
  1. 投票者在投票前可以看到其他人的投票情况（包括姓名）。
  2. 投票者在投票前可以看到投票平均值。
  3. 投票者仅在投票后、但所有投票结束前，可以看到投票平均值。
  4. 投票者仅在所有投票结束后，才能看到投票平均值。
  寻找在线投票案例进行说明。针对以下投票选项执行相同操作：
  1. 投票者无需注册，因此一个人可以多次投票。
  2. 投票者已注册，但可以随时更改其唯一的一次投票。
  3. 投票者已注册，且只能投票一次，不可编辑。
  发起投票的人是否有权合法地定义这些投票条件？如果他们设定诸如所有投票必须签名且将公开等条件，情况会如何？

1. 在线发布视频是否类似于在当地商店橱窗中张贴通知？请解释，涵盖发布权限（permission to post）、展示权限（permission to display）、撤回权限（permission to withdraw）和删除权限（permission to delete）。帖子可以被删除吗？可以被拒绝吗？请解释两者的区别。提供在线示例。

1. 请给出权利重新分配（rights re-allocations）的物理示例和在线示例。明确区分权利（rights）和元权利（meta-rights）。如果四位作者在线发表一篇论文，请列出...

所有权选项（Ownership options）。讨论每种选项在实践中如何运作。你更倾向于哪一种，为什么？

1. 委派（Delegating）是否应该赋予进一步委派的权利？请结合物理世界和在线环境的示例进行解释。如果被委派者（Delegatees）可以继续委派，所有权（Ownership）和问责制（Accountability）会发生什么变化？讨论一种最坏的情况。

1. 如果一份遗嘱将财产留给了你，你可以拒绝拥有它，还是它自动归你所有？哪些权利在没有同意（Consent）的情况下不能被分配？哪些可以？在以下权利中，哪些可以被自由分配：论文作者（Paper author）、论文共同作者（Paper co-author）、分会主席（Track chair）、被添加为好友（Being friended）、被封禁（Being banned）、公告板成员（Bulletin board member）、登录 ID（Logon ID）、公告板版主（Bulletin board moderator）、在线圣诞卡访问权限（Online Christmas card access）？其中哪些需要接收者的同意？

1. 调研社交网络（Social Network, SN）连接是如何呈倍数增长的。列出你和四个朋友的朋友数量及其平均值。基于此，估算一般情况下潜在的“朋友的朋友”总数。通过查看你朋友的朋友列表，给出在你个人情况下的实际“朋友的朋友”数量。估算你每周从所有朋友那里收到多少条消息或通知。据此，估算每位朋友每天发送消息的平均数量。那么，如果你将所有“朋友的朋友”都添加为好友，潜在地，你预计每天会收到多少条消息？如果你把“朋友的朋友的朋友”也添加为好友会怎样？为什么这个数字如此之大？讨论电影 *Six Degrees of Separation*。

1. 演示如何在三个社交网络（Social Networks）中“取消好友（unfriend）”一个人。对方会收到通知吗？“取消好友”是否等同于“关系破裂（breaking up）”？“反好友（anti-friend）”即敌人这一观点，启发了“反 Facebook（anti-Facebook）”类网站的出现。调研针对讨厌的人（例如名人或前任）的技术支持（Technology support）。尝试访问反组织网站（Anti-organization sites），例如 [sickfacebook.com](http://sickfacebook.com/)。针对“反友谊（anti-friendship）”的技术支持可能具有什么样的目的？

## 24.5 第 5 部分：未来

> 未来并非仅是技术性的（technical）或社会性的（social），而是两者的结合。

### 24.5.1 技术乌托邦主义（Technology utopianism）

技术乌托邦主义（Technology utopianism）是一种认为仅凭技术就能创造未来的信念。这种观点在虚构作品中非常流行，例如 *The Jetsons* 中的 Rosie、*Star Wars* 中的 C-3PO 以及 *Star Trek* 中的 Data，这些机器人都能阅读、说话、行走、交谈、思考和感受。既然我们能如此轻松地完成这些事情，那么（让机器人实现）会有多难呢？在电影中，机器人可以学习（*Short Circuit*）、繁衍（*Stargate* 中的复制者）、思考（*The Hitchhiker's Guide* 中的 Marvin）、产生自我意识（self-aware，*I, Robot*），并最终取代人类（*The Terminator*，*The Matrix*）。在这种视角下，计算机被视为一种不可阻挡的进化巨轮（evolutionary juggernaut，图 21），但就目前而言，它们甚至无法征服一个充满蟑螂的星球。

![](https://public-media.interaction-design.org/images/encyclopedia/socio-technical_system_design/fig16_The_technical_vision_utopia.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。
**图 24.21**：技术乌托邦主义

尽管有动画片和科幻小说的描绘，但如今的家务机器人（housework robot）是 Roomba（图 24.22）。它能清理灰尘，但用户遇到的问题包括原地打转、瘫痪、线头和头发堵塞以及卡住。甚至用水清洗它都会导致其损坏。毋庸置疑，这是一个聪明的机器人，

然而，它仍需要帮助才能在*地形平坦、没有敌人且食物充足的房屋中*生存。(脚注 93) 若被置于室外或被单独留下，它将无法生存。甚至昆虫的生存能力都更强。

![](https://public-media.interaction-design.org/images/encyclopedia/socio-technical_system_design/robot_and_superman.jpg)
作者/版权持有者：由 Fleischer Brothers production 提供。版权条款与许可：pd (Public Domain (公有领域 (属于公共财产且不含原创作者身份的信息)))。

![](https://public-media.interaction-design.org/images/encyclopedia/socio-technical_system_design/robot_r2d2.jpg)
作者/版权持有者：由 Brayon Michael Pieske 提供。版权条款与许可：pd (Public Domain (公有领域 (属于公共财产且不含原创作者身份的信息)))。

![](https://public-media.interaction-design.org/images/encyclopedia/socio-technical_system_design/robot_Roomba_original.jpg)
作者/版权持有者：由 Larry D. Moore 提供。版权条款与许可：CC-Att-SA-3 (Creative Commons Attribution-ShareAlike 3.0 (知识共享-署名-相同方式共享 3.0))。

**图 24.22 A-B-C**：机器人助手分别出现在：a. Superman，b. Star Wars，c. 现实（第一代 iRobot Roomba 版本）

对话（Conversation）的情况亦然。人们可以轻松地聊很多话题，但我们身边的计算机却出奇地沉默。相关技术已经存在，那么为什么汽车不能像 Knight Rider 中的 [KITT](http://www.youtube.com/watch?v=rGT-6nRREQI) 那样与我们交谈呢？是因为计算机对话令人尴尬吗？(脚注 94)

空间协调性（Spatial coordination）的情况也是如此。比较一下 [机器人世界杯](http://www.robocup.org/) 和人类的 [世界杯](http://www.fifa.com/worldcup/index.html)。[人工智能](https://www.interaction-design.org/literature/topics/ai)（Artificial Intelligence, AI）的拥护者声称机器人将在四十年内超越人类，但他们在四十年之前也是这么说的。就像海市蜃楼一样，AI 的突破似乎永远在四十年之后——或者应该是四万年之后？在视觉方面，计算机在处理视网膜活动（retinal activity）时依然困难重重，更不用说皮层活动（cortical activity）了：

> 在视觉、听觉、模式识别（pattern recognition）和学习等领域，计算机根本无法与人类大脑竞争。……而谈到运行效率（operational efficiency），则完全没有可比性。一台典型的房间大小的超级计算机，其重量约为人类大脑的 1,000 倍，占用空间为 10,000 倍，功耗则高出一百万倍……
> 
> —— Boahen, 2005

问题的关键不在于计算机不能做什么，而在于说话、行走和思考这些任务并不像看起来那么简单。技术乌托邦主义（Technology utopianism）基于 Moore's law（摩尔定律）预言了一个“奇点（singularity）”，即计算机的处理能力每十八个月就会翻一番（脚注 95）。该观点认为，超级智能计算机很快就会取代人类（Kurzweil, 1999）。这种被视为“大谎言（big lie）”（脚注 96）的幻想，将未来仅仅看作是计算机现有处理能力的简单叠加。然而，进化绝非简单的重复，而大脑也不仅仅是一台巨大的计算机。

![](https://public-media.interaction-design.org/images/encyclopedia/socio-technical_system_design/fig17_letraset_page.jpg)
**图 24.23**：字母 'A' 的 Letraset 页面

计算机的计算能力比人类强，正如汽车行驶得更快，起重机起吊得更多，但计算并非大脑功能的全部。简单处理（Simple processing）（脚注 97）适用于简单的情况，但视觉、听觉、思考和交谈等真实任务具有“生产性（productive）”，即其信息量随规模呈几何级数增长（脚注 98）。语言的生产性体现在，五岁儿童能说出的句子数量，超过了他们以每秒一句的速度在终身学习中能学到的数量 (Chomsky, 2006)。儿童能轻易看出 Letraset 页面（图 23）上全是字母“A”，但计算机在处理这种生产性变化（productive variation）时却十分吃力。使用像素级处理（pixel level processing）来进行模式识别（pattern recognition）就“*像是试图仅通过研究羽毛来理解鸟类的飞行。这根本无法实现*” (Norman, 1990)。那些能看穿炒作（hype）的 AI 专家在几十年前就意识到，像语言这样具有生产性的任务在短期内无法被解决 (Copeland, 1993)。

![](https://public-media.interaction-design.org/images/encyclopedia/socio-technical_system_design/The_exponential_growth_of_simple_process_power.jpg)
作者/版权持有者：Courtesy of Ray Kurzweil and Kurzweil Technologies, Inc. 
版权条款与许可：CC-Att-SA-1 (Creative Commons Attribution-ShareAlike 1.0 Unported)。

**图 24.24**：简单处理能力的指数级增长

简单处理（Simple Processing）的底线是 *99% 门槛（the 99% barrier）*。例如，准确率 99% 的计算机语音识别（Computer Voice Recognition）每 100 个单词就会出现一个错误，但每分钟一个错误远低于对话标准。对于计算机自动驾驶汽车（Computer Auto-drive Cars）而言，99% 的准确率意味着每天都会发生一次事故！在 2005 年的 DARPA Grand Challenge 中，23 辆自动驾驶车辆（Autonomous Vehicles）中仅有 5 辆完成了简单的赛道（Miller et al, 2006）。2007 年，11 辆资金更充足的车辆中，有 6 辆完成了城市赛道（Urban Track），最高平均时速为 14 英里/小时。然而，熟练的驾驶者在更复杂的道路上、更恶劣的天气中、更拥挤的交通环境下，以更快的速度驾驶数十年而 *没有* 发生事故。（脚注 99）大脑并非仅仅通过增加简单处理能力就跨越了 99% 的性能门槛。

![](https://public-media.interaction-design.org/images/encyclopedia/socio-technical_system_design/fig18a_Kim_Peek_memory.jpg)
作者/版权持有者：由 Dmadeo 提供。版权条款和许可：CC-Att-SA-3 (Creative Commons Attribution-ShareAlike 3.0)。

![](https://public-media.interaction-design.org/images/encyclopedia/socio-technical_system_design/fig18a_rain-man-trailer.jpg)
作者/版权持有者：MGM。版权条款和许可：保留所有权利（All Rights Reserved）。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因为无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面上的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

**图 24.25 A-B**：最左侧：Kim Peek 是电影 *Rain Man* 的灵感来源。最右侧：饰演 *Rain Man* 的 Dustin Hoffman。

大脑如何处理那些“不可计算（incalculable）”的任务？它本身就是一个信息处理器（information processor）。其数以万亿（$10^{12}$）计的神经元（neurons）是由电力驱动的生物开关设备，能够实现逻辑门（logic gates）（McCulloch and Pitts, 1943），也就是说，在原理上与晶体管（transistors）没有区别。如果处理能力（processing power）真的取决于神经元或晶体管的数量，那么计算机很快就能达到大脑的潜力。图 24.24 表明，计算机在 2000 年的处理能力相当于昆虫，2010 年相当于小鼠，2020 年将相当于人类，并在 2045 年超越所有人类。当然，这简直是胡说八道，因为目前的计算机甚至无法完成蚂蚁所能做的事情，而蚂蚁仅凭极少量的神经元就能做到。无论是蜜蜂、蟑螂还是飞行甲虫亦然。那么，计算机如何在短短几十年内就跃升到能够进行对话、模式识别（pattern recognition）和学习的程度？原因在于，正如我们大脑在进化过程中所发现的那样，计算能力（calculating power）并不是解决不可计算任务（incalculable tasks）的答案。在*学者综合征（savant syndrome）*中，那些能在脑中计算 20 位素数的人需要全天候的照顾才能在社会中生存。例如，启发了电影 *Rain Man* 的 Kim Peek，他能回忆起 9,000 多本书中每一页的每一个字，包括所有的 Shakespeare 作品和《圣经》，但必须由他的父亲照顾（图 25）。他患有神经功能障碍（neurologically disabled），因为他大脑中较晚演化出的部分未能发育。

因此，学者（savants）的大脑是在缺失较新子系统（sub-systems）的情况下运作的。他们计算能力*更强*这一事实表明，大脑曾尝试过简单的处理能力，但随后进化并超越了它。相比之下，技术乌托邦主义者（technology utopians）仍然没有意识到，单纯的量变（more of the same）并不等同于进化。

计算机就是*电子学者（electronic savants）*，它们是计算奇才，但需要看护者才能在现实世界中生存。如果计算机擅长的是大脑在一百万年前就已经超越的那种处理方式，那么它们如何能代表未来？如果由并行运行的 PC 显卡构建的超级计算机是计算的未来，那么更大的耕牛就是农业的未来！如果人工智能（AI, Artificial Intelligence）甚至没有朝着相同的方向演进，它又如何能超越人类智能（HI, Human Intelligence）？

一个系统的性能不仅取决于其组成部分，还取决于这些部分是如何连接的。

如今的计算机遵循冯·诺依曼架构（von Neumann's architecture），但大脑并非如此，例如，它没有中央处理器（CPU）(Sperry and Gazzaniga, 1967)。大脑通过采取冯·诺依曼所避开的设计风险，突破了 99% 的性能壁垒 (Whitworth, 2009c)。计算机科学避开了「对处理过程的处理（processing of processing）」，因为这会导致死循环（infinite loops），但这种机制却实现了符号化（symbolism）——即将大脑的一个神经组件（neural assembly，即一个符号）与另一个组件（即一种[感知（perception）](https://www.interaction-design.org/literature/topics/perception)）联系起来。

这是意义和语言的基础。处理过程会改变信息，因此它预设了一个语境（context）。(footnote 100) 只有通过对处理过程的处理，我们才能修改语境，也就是说，才能进行学习。剥夺计算机这一选项，也就剥夺了它们理解意义的能力。

大脑并非现代计算机的低劣生物版本，而是一种*完全不同的处理器*。它通过处理自身的处理过程，从而产生了语言、数学和哲学。解决生产力问题的答案并非增加更多的处理能力，而是实现对处理过程的处理。通过这一冒险的步骤，大脑能够感知到“自我”、“他人”、“朋友”和“社区”，而这些构建（constructs）正是人类和计算机专家们难以攻克的难题。如果如今的超级计算机在处理量级上甚至无法与大脑相提并论 (footnote 101)，那么那些技术乌托邦主义者不过是伪装成未来主义者的计算传统主义者。

### 24.5.2 社会技术愿景（Socio-technical vision）

![](https://public-media.interaction-design.org/images/encyclopedia/socio-technical_system_design/fig19_mr_clippy.jpg)
作者/版权持有者：未知（待调查）。版权条款与许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。
**图 24.26**：掌控局面的 Clippy 先生

计算技术面临的问题并非它何时会取代人类，而是人类何时能看清它的本质，例如 Office 97 的回形针助手 Clippy 先生（图 26）：
> 当你希望它消失时，它并不离开。它粗鲁地打断你，并破坏了你的思路（train of thought）。
> —— Pratley, 2004

用户的反应包括“死吧，Clippy，死吧！”（Gauze, 2006），但其 Microsoft 的设计师仍然好奇：“如果你认为‘助手’这个想法很糟糕，那么具体原因是什么？”
具体答案是：因为它认为自己才是掌控者。在 Windows XP 中，Clippy 先生被足够聪明、懂得自己定位的标签（tags）所取代。试图独立变得“智能”的软件，很快就会像那个“魔法师的学徒（sorcerer's apprentice）”一样失控。

为什么要耗费价值两千万美元的超级计算机，去尝试完成大脑已经能够完成的事情——而大脑已经经历了数百万年的现实生活 Beta 测试（beta-testing）？即使我们将计算机重新设计成像大脑一样工作，例如采用神经网络（neural nets），谁能保证它们不会继承同样的弱点？如果大脑已经解决了生产力问题，那么...

正如预期的那样，让我们将计算的目标从模拟人类（human mimicry）转变为辅助人类（human assistance）。

这种情况已经在发生了。无人驾驶汽车仍是一个梦想，但响应式定速巡航（reactive cruise control）、距离感测（range sensing）和辅助平行泊车（assisted parallel parking）已经存在 (Miller et al, 2006)。计算机独立手术仍面临困难，但计算机支持的远程手术（computer-supported remote surgery）和计算机辅助手术（computer-assisted surgery）在今天已经成为现实。机器人的行走还很笨拙，但安装了机器人肢体（robotic limbs）的人们却能应对自如。计算机自动驾驶的无人机可能带来风险，而远程驾驶的无人机则是极大的助力。计算机生成的动画虽然出色，但像 $\textit{Avatar}$ 这样顶尖的动画作品则是将人类演员与计算机相结合。在计算机建议下下棋的棋手，其表现比单独的棋手或单独的计算机都要好。(footnote 102) 在过去十年的杀手级应用（killer applications）中，从 email 到 Facebook，人们在做他们最擅长的事，而技术在做它最擅长的事。例如，email 传输信息，而人类创造意义（meaning）。因此，“术业有专攻（horses for courses）”意味着让计算机处理信息（process information），而让人类处理意义（process meaning）。意义比信息处于更高的维度，这意味着人类应该“监督（mind）”计算机，而计算机不应控制人类。

![](https://public-media.interaction-design.org/images/encyclopedia/socio-technical_system_design/fig20_The_socio-technical_vision.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：

未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 24.27**：社会技术愿景（The socio-technical vision）

社会技术（Socio-technology）关注的是技术*与*人，且后者是更高级的（"elder"）系统（图 27）。如果由人引导技术，*可能会*出错；但如果由技术引导人，则*必然*出错。高级层面引导低级层面是进化（evolution），而低级层面引导高级层面则是退化（devolution）。仅仅因为低级层面更容易处理而将其作为关注重点，并不等同于进步。（脚注 103）再次强调，如果仅从技术角度看待互联网，是对它的低估！正如普适计算（pervasive computing）和泛在计算（ubiquitous computing）理论所主张的，应让计算机成为背景而非前景。技术应当与人融合，而非相反。脱离了人文语境（human context）的技术甚至称不上是无用——而是毫无意义。如果“技术就是未来”，那么掌控我们的将是某种无心且无情的存在。因此，未来应该是社会技术，而非单纯的技术。

有人说互联网让我们变得愚蠢（脚注 104），但镜子仅仅是反射。在线媒体所展示的人类残暴、腐败或愚蠢，仅仅揭示了现状。互联网如同观察人类的显微镜和望远镜，*正将我们自己呈现给我们看*。它虽然不是物理实体，但思想引发言行，正如枪支发射子弹一样。人类的思想现在就在线上，供我们选择。我们人类正在选择自己的思考方式，而我们的思考现在也呈现在线上，伴随着...

网页计数器（web-counters）记录着这一切。互联网这面“电子镜像（electronic mirror）”所呈现的景象并非总是美好，但它是真实的；而一个人若要改变，必须首先审视自身。计算的演进（evolution of computing）是人类演进的一部分，是一场已持续数千年的社会实验（social experiment）。唯有通过个体的演进，通过超越自我，我们才能助力这一进程取得成功。

### 24.5.3 讨论问题

请从以下列表中选择部分问题进行研究。如果你是在大学或商业课程的课堂上阅读本章，可以两人一组研究这些问题，并向全班汇报，同时提供理由和示例。

1. 什么是技术乌托邦主义（Technology Utopianism）？请举出电影中的例子。什么是技术奇点（Technology Singularity）？在这种观点中，为什么计算机必然会取代人类？这里存在什么样的错误假设？
2. 上个世纪的人们预期到 2000 年会实现哪些技术进步？其中哪些我们仍在等待？人们预期机器人到 2050 年会做什么？哪些是现实的？像 Sony dog 这样的机器人成就处于什么水平？社会技术设计（Socio-technical design）如何改进 Sony dog？在社会技术范式（Socio-technical paradigm）中，机器人将如何演进？请举例说明。
3. 如果超级计算机达到了一个人类大脑的处理能力，那么在拥有多个大脑的情况下，许多人在一起是否比一个人更聪明？回顾“群体疯狂（Madness of Crowds）”理论，即人们在一起时智力会下降。请举例说明。为什么给项目增加更多的程序员并不总是能更快地完成项目？通常情况下，什么因素会影响各部分协同工作的效果？如果一台超级计算机拥有的晶体管数量与大脑拥有的神经元数量相同，其处理能力是否相等？请解释。

1. 如今的超级计算机（Supercomputers）如何提高处理能力（Processing power）？请列出 [Top500](http://www.top500.org/) 前十名的处理器核心（Processor cores）。其中哪些使用了 NVIDIA 个人电脑显卡核心（NVidia PC graphic board cores）？这种能力在实际计算任务中是如何利用的？处理器核心的串行（Sequence）或并行（Parallel）运行如何影响性能（Performance）？在实践中是如何决定采用哪种方式的？（仅限计算机科学专业学生）。
1. 评述自动化车辆（Automated vehicles，无论是汽车、飞机还是火车等）目前的最新技术状态（State-of-the-art）。目前是否有完全“无驾驶员（Pilotless）”的车辆在投入使用？远程驾驶车辆（Remotely piloted vehicles）的情况如何？全计算机控制在何时有效？在何时无效？（提示：考虑主动帮助系统 [Active help systems]）。全计算机控制车辆在什么情况下会有用？请举例说明车辆的计算机控制将如何演进。
1. 什么是 99% 障碍（99% barrier）？为什么最后 1% 的准确率（Accuracy）对于生产性任务（Productive tasks）来说是一个问题？请分别从语言、逻辑、艺术、音乐、诗歌、驾驶以及另一个领域给出示例。这类任务在现实世界中有多普遍？大脑是如何处理这些任务的？
1. 什么是人类学者综合征者（Human savant）？请举出过去和现在的例子。学者综合征者能轻松完成哪些任务？他们能与现代计算机竞争吗？学者综合征者觉得哪些任务困难？区别在哪里？为什么学者综合征者需要支持（Support）？如果计算机类似于学者综合征者，它们需要什么样的支持？
1. 寻找三个像 Mr. Clippy 那样自以为是的软件示例。请分别给出以下示例：1. 未经询问便采取行动；2. 唠叨；3. 秘密更改；4. 增加用户工作量。
1. 想想一个你经历过的个人冲突（Personal conflict）

...想要获得建议。请保持简单清晰。现在尝试以下三种方案。在每种情况下，请以相同的方式解释并提出问题：
1. 独自进入卧室，将一张你喜欢的家庭成员的照片放在枕头上。大声地解释并提出问题，然后想象他们的回应。
2. 访问一个在线计算机程序，如 [http://cleverbot.com/](http://cleverbot.com/)，并执行相同的操作。
3. 拨打一个匿名求助热线（anonymous help line）并执行相同的操作。
比较并对比结果。哪一个最有帮助？

1. 一种理性的决策方式（rational way to decide）是列出所有选项，评估每一个选项并选择最佳方案。在以下竞赛中，分别有多少种选项：1. 国际跳棋（Checkers），2. 国际象棋（Chess），3. 《文明》（Civilization，一款策略游戏），4. 一款 MMORPG（大规模多人在线角色扮演游戏），5. 一场辩论。计算机擅长其中的哪些？如果人们无法计算所有选项，他们会怎么做？程序能够实现这一点吗？在线游戏玩家如何评价人类对手和 AI 对手？为什么？这种情况会一直持续下去吗？

1. Mr. Clippy 是基于贝叶斯逻辑（Bayesian logic）构建的。什么样的驱动数据决定了他的决策？哪些内容被忽略了？为什么用户觉得他很粗鲁？为什么他无法识别拒绝（rejection）？什么样的用户喜欢 Mr. Clippy？在 Word 中开启自动更正（auto-correct）功能，并尝试编写等式：i = 1。为什么 Word 会出错？在不关闭自动更正的情况下，你该如何修复它？请提供关于“推荐（recommending）”与“主导（taking charge）”的在线示例。

1. 语言中的句法（syntax）和语义（semantics）之间有什么区别？程序擅长处理什么？

请观察文本转语音系统（Text-to-Speech, TTS），例如[这里](http://imtranslator.net/translate-and-speak/#window)，或者翻译系统[这里](http://www.oddcast.com/home/demos/tts/tts_tran_example.php)。它们的成效如何？计算机是否在执行人类所做的事情？翻译发生在哪个层面？它们是否属于语义层面的转换（semantic level transformations）？请讨论 John Searle 的[中文屋（Chinese room）](http://en.wikipedia.org/wiki/Chinese_room) 思想实验。

## 24.6 致谢

感谢第一作者的妻子提供的宝贵建议，感谢 Massey University 158729 (STS Design) 课程的学生们参与问题的测试。同时，感谢 Yijing Qian 提供图 2 和图 9。

## 24.7 References

[Ackerman](https://www.interaction-design.org/references/authors/mark_s__ackerman.html), Mark S. (2000): *The Intellectual Challenge of CSCW: The Gap Between Social Requirements and Technical Feasibility*. In [Human-Computer Interaction](https://www.interaction-design.org/references/periodicals/human-computer_interaction.html), 15 (2) pp. 181-203
[Ahmad](https://www.interaction-design.org/references/authors/adnan_ahmad.html), Adnan and [Whitworth](https://www.interaction-design.org/references/authors/brian_whitworth.html), Brian (2011): *Distributed access control for social networks*. In [2011 7th International Conference on Information Assurance and Security IAS](https://www.interaction-design.org/references/periodicals/2011_7th_international_conference_on_information_assurance_and_security_ias.html), pp. 68-73
[Alberts](https://www.interaction-design.org/references/authors/bruce_alberts.html), Bruce, [Bray](https://www.interaction-design.org/references/authors/dennis_bray.html), Dennis, [Lewis](https://www.interaction-design.org/references/authors/julian_lewis.html), Julian, [Raff](https://www.interaction-design.org/references/authors/martin_raff.html), Martin, [Roberts](https://www.interaction-design.org/references/authors/keith_roberts.html), Keith and [Watson](https://www.interaction-design.org/references/authors/james_d__watson.html), James D. (1994): *Molecular Biology of the Cell 3E.* Garland Science

[Alexander](https://www.interaction-design.org/references/authors/christopher_alexander.html), Christopher (1964): *Notes on the Synthesis of Form.* Harvard University Press
[Alter](https://www.interaction-design.org/references/authors/steven_alter.html), Steven (1999): *A general, yet useful theory of information systems*. In [Communications of the AIS](https://www.interaction-design.org/references/periodicals/communications_of_the_ais.html), 1 (3)
[Beer](https://www.interaction-design.org/references/authors/david_beer.html), David and [Burrows](https://www.interaction-design.org/references/authors/roger_burrows.html), Roger (2007): *Sociology and, of and in Web 2.0: Some Initial Considerations*. In[Sociological Research Online](https://www.interaction-design.org/references/periodicals/sociological_research_online.html), 12 (5) pp. 1-15
[Benkler](https://www.interaction-design.org/references/authors/yochai_benkler.html), Yochai (2002): *Coase's Penguin, or, Linux and "The Nature of the Firm*. In [Yale Law Journal](https://www.interaction-design.org/references/periodicals/yale_law_journal.html), 112 (3) pp. 369-446
[Berners-Lee](https://www.interaction-design.org/references/authors/tim_berners-lee.html), Tim (2000): *Weaving the Web: The Original Design and Ultimate Destiny of the World Wide Web.*HarperBusiness

[Bertalanffy](https://www.interaction-design.org/references/authors/ludwig_von_bertalanffy.html), Ludwig Von (1968): *General System Theory: Foundations, Development, Applications (Revised Edition).* George Braziller Inc
[Boahen](https://www.interaction-design.org/references/authors/kwabena_boahen.html), Kwabena (2005): *Neuromorphic Microchips*. In [Scientific American](https://www.interaction-design.org/references/periodicals/scientific_american.html), 292 (5) pp. 56-63
[Borenstein](https://www.interaction-design.org/references/authors/nathaniel_s__borenstein.html), Nathaniel S. and [Thyberg](https://www.interaction-design.org/references/authors/chris_a__thyberg.html), Chris A. (1991): *Power, Ease of Use and Cooperative Work in a Practical Multimedia Message System*. In [International Journal of Man-Machine Studies](https://www.interaction-design.org/references/periodicals/international_journal_of_man-machine_studies.html), 34 (2) pp. 229-259
[Boutin](https://www.interaction-design.org/references/authors/paul_boutin.html), Paul (2004): *Can e-mail be saved*. In [Infoworld](https://www.interaction-design.org/references/periodicals/infoworld.html), 14
[Burk](https://www.interaction-design.org/references/authors/dan_l__burk.html), Dan L. (2001): *Copyrightable functions and patentable speech*. In [Communications of the ACM](https://www.interaction-design.org/references/periodicals/communications_of_the_acm.html), 44 (2) pp. 69-75

[Callahan](https://www.interaction-design.org/references/authors/david_callahan.html), David (2004): *The Cheating Culture: Why More Americans Are Doing Wrong to Get Ahead.* Mariner Books
[Campbell-Kelly](https://www.interaction-design.org/references/authors/martin_campbell-kelly.html), Martin (2008): *Historical reflections: Will the future of software be open source?*. In[Communications of the ACM](https://www.interaction-design.org/references/periodicals/communications_of_the_acm.html), 51 (10) pp. 21-23
[Chomsky](https://www.interaction-design.org/references/authors/noam_chomsky.html), Noam (2006): *Language and Mind.* Cambridge University Press
[Chung](https://www.interaction-design.org/references/authors/lawrence_chung.html), Lawrence, [Nixon](https://www.interaction-design.org/references/authors/brian_a__nixon.html), Brian A., [Yu](https://www.interaction-design.org/references/authors/eric_yu.html), Eric and [Mylopoulos](https://www.interaction-design.org/references/authors/john_mylopoulos.html), John (1999): *Non-Functional Requirements in Software Engineering (THE KLUWER INTERNATIONAL SERIES IN SOFTWARE ENGINEERING Volume 5).*Springer

[Clark](https://www.interaction-design.org/references/authors/d__d__clark.html), D. D. and [Wilson](https://www.interaction-design.org/references/authors/d__r__wilson.html), D. R. (1987): A Comparison of Commercial and Military Computer Security Policies. In:[IEEE Symposium on Security and Privacy 1987](https://www.interaction-design.org/references/conferences/ieee_symposium_on_security_and_privacy_1987.html) 1987. pp. 184-195
[Cohen](https://www.interaction-design.org/references/authors/bram_cohen.html), Bram (2003): *Incentives Build Robustness in BitTorrent*. In [Workshop on Economics of PeertoPeer systems](https://www.interaction-design.org/references/periodicals/workshop_on_economics_of_peertopeer_systems.html), 6 (22)
[Copeland](https://www.interaction-design.org/references/authors/jack_copeland.html), Jack (1993): *Artificial Intelligence: A Philosophical Introduction.* Wiley-Blackwell
[Cysneiros](https://www.interaction-design.org/references/authors/l__m__cysneiros.html), L. M. and [Leite](https://www.interaction-design.org/references/authors/julio_cesar_sampaio_do_prado_leite.html), Julio Cesar Sampaio do Prado (2002): *Non-functional requirements:from Elicitation to modeling languages*. In [Computer](https://www.interaction-design.org/references/periodicals/computer.html), 35 (3) pp. 8-9

[David](https://www.interaction-design.org/references/authors/julie_smith_david.html), Julie Smith, [McCarthy](https://www.interaction-design.org/references/authors/william_e__mccarthy.html), William E. and [Sommer](https://www.interaction-design.org/references/authors/brian_s__sommer.html), Brian S. (2003): *Agility: the key to survival of the fittest in the software market*. In [Communications of the ACM](https://www.interaction-design.org/references/periodicals/communications_of_the_acm.html), 46 (5) pp. 65-69
[Davis](https://www.interaction-design.org/references/authors/fred_d__davis.html), Fred D. (1989): *Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology*. In [MIS Quarterly](https://www.interaction-design.org/references/periodicals/mis_quarterly.html), 13 (3) pp. 319-340
Department of Defense (1985). *TCSEC - Trusted Computer Security Evaluation Criteria (TCSEC), DOD 5200.28-STD*. Retrieved 19 May 2012 from Department of Defense:
[Diamond](https://www.interaction-design.org/references/authors/jared_m__diamond.html), Jared M. (1998): *Guns, Germs, and Steel: The Fates of Human Societies.* W. W. Norton and Company
[Esfeld](https://www.interaction-design.org/references/authors/michael_esfeld.html), Michael (1998): *Holism and analytic philosophy*. In [Mind](https://www.interaction-design.org/references/periodicals/mind.html), 107 (426) pp. 365-380

[Ferraiolo](https://www.interaction-design.org/references/authors/david_f__ferraiolo.html), David F. and [Kuhn](https://www.interaction-design.org/references/authors/d__richard_kuhn.html), D. Richard (2004): *Role Based Access Control*. In [Review Literature And Arts Of The Americas](https://www.interaction-design.org/references/periodicals/review_literature_and_arts_of_the_americas.html), 14 (5) pp. 554-563
[Figart](https://www.interaction-design.org/references/authors/deborah_m__figart.html), Deborah M. and [Golden](https://www.interaction-design.org/references/authors/lonnie_golden.html), Lonnie (eds.) (2000): *Working Time: International Trends, Theory and Policy Perspectives (Routledge Advances in Social Economics).* Routledge
[Forman](https://www.interaction-design.org/references/authors/bruce_jay_forman.html), Bruce Jay and [Whitworth](https://www.interaction-design.org/references/authors/brian_whitworth.html), Brian (2007): Information Disclosure and the Online Customer Relationship. In:[Quality, Values and Choice Workshop, Computer Human Interaction](https://www.interaction-design.org/references/conferences/quality%2C_values_and_choice_workshop%2C_computer_human_interaction.html) 2007, Portland, Oregon, USA. pp. 1-7
[Freeden](https://www.interaction-design.org/references/authors/michael_freeden.html), Michael (1991): *Rights (Concepts in Social Thought).*

[Freudenthal](https://www.interaction-design.org/references/authors/eric_freudenthal.html), Eric, [Pesin](https://www.interaction-design.org/references/authors/tracy_pesin.html), Tracy, [Port](https://www.interaction-design.org/references/authors/lawrence_port.html), Lawrence, [Keenan](https://www.interaction-design.org/references/authors/edward_keenan.html), Edward and [Karamcheti](https://www.interaction-design.org/references/authors/vijay_karamcheti.html), Vijay (2002): *dRBAC: distributed role-based access control for dynamic coalition environments*. In [Proceedings 22nd International Conference on Distributed Computing Systems](https://www.interaction-design.org/references/periodicals/proceedings_22nd_international_conference_on_distributed_computing_systems.html), pp. 411-420
[G.](https://www.interaction-design.org/references/authors/geen%2C_r__g-dot-.html), Geen, R. and [Gange](https://www.interaction-design.org/references/authors/j__j__gange.html), J. J. (1983): Social facilitation: Drive theory and beyond. In: [Blumberg](https://www.interaction-design.org/references/authors/herbert_h__blumberg.html),
 Herbert H. (ed.). "Small Groups and Social Interaction: v. 2 (Small 
Groups & Social Interactions)". John Wiley and Sons Ltdp. 141–153

[Gediga](https://www.interaction-design.org/references/authors/gunther_gediga.html), Gunther, [Hamborg](https://www.interaction-design.org/references/authors/kai-christoph_hamborg.html), Kai-Christoph and [Duntsch](https://www.interaction-design.org/references/authors/ivo_duntsch.html), Ivo (1999): *The
 IsoMetrics Usability Inventory: An Operationalization Of ISO 9241-10 
supporting summative and formative evaluation of software systems*. In[Behaviour and Information Technology](https://www.interaction-design.org/references/periodicals/behaviour_and_information_technology.html), 18 (3) pp. 151-164
[Hoffman](https://www.interaction-design.org/references/authors/l__r__hoffman.html), L. R. and [Maier](https://www.interaction-design.org/references/authors/n__r__f__maier.html), N. R. F. (1961): *Quality and acceptance of problem solutions by members of homogenous and heterogenous groups*. In [Journal of Abnormal and Social Psychology](https://www.interaction-design.org/references/periodicals/journal_of_abnormal_and_social_psychology.html), 62 pp. 401-407
[Johnson](https://www.interaction-design.org/references/authors/deborah_g__johnson.html), Deborah G. (2001): *Computer Ethics (3rd Edition).* Prentice Hall

[Jonsson](https://www.interaction-design.org/references/authors/erland_jonsson.html), Erland (1998): *An integrated Framework for Security and Dependability*. In [Information Security](https://www.interaction-design.org/references/periodicals/information_security.html), pp. 22-29
[Kant](https://www.interaction-design.org/references/authors/immanuel_kant.html), Immanuel (1999): *Critique of Pure Reason (The Cambridge Edition of the Works of Immanuel Kant).*Cambridge University Press
[Karp](https://www.interaction-design.org/references/authors/alan_h__karp.html), Alan H., [Haury](https://www.interaction-design.org/references/authors/harry_haury.html), Harry and [Davis](https://www.interaction-design.org/references/authors/michael_h__davis.html), Michael H. (2009): *From ABAC to ZBAC : The Evolution of Access Control Models From ABAC to ZBAC : The Evolution of Access Control Models*. In [Control](https://www.interaction-design.org/references/periodicals/control.html), (0) pp. 22-30
[Keeney](https://www.interaction-design.org/references/authors/ralph_l__keeney.html), Ralph L. and [Raiffa](https://www.interaction-design.org/references/authors/howard_raiffa.html), Howard (1976): *Decisions with Multiple Objectives: Preferences and Value Tradeoffs.*Cambridge University Press
[Kelly](https://www.interaction-design.org/references/authors/erin_kelly.html), Erin (ed.) (2001): *Justice as Fairness: A Restatement.* Belknap Press of Harvard University Press

[Kienzle](https://www.interaction-design.org/references/authors/darrell_m__kienzle.html), Darrell M. and [Wulf](https://www.interaction-design.org/references/authors/william_a__wulf.html), William A. (1998): A practical approach to security assessment. In: [Proceedings of the 1997 workshop on New security paradigms](https://www.interaction-design.org/references/conferences/proceedings_of_the_1997_workshop_on_new_security_paradigms.html) 1998. pp. 5-16
[Knoll](https://www.interaction-design.org/references/authors/kathleen_knoll.html), Kathleen and [Jarvenpaa](https://www.interaction-design.org/references/authors/sirkka_l__jarvenpaa.html),
 Sirkka L. (1994): Information technology alignment or â€œfitâ€� in 
highly turbulent environments: the concept of flexibility. In: [Proceedings
 of the 1994 computer personnel research conference on Reinventing IS 
managing information technology in changing organizations managing 
information technology in changing organizations](https://www.interaction-design.org/references/conferences/proceedings_of_the_1994_computer_personnel_research_conference_on_reinventing_is_managing_information_technology_in_changing_organizations_managing_information_technology_in_changing_organizations.html) 1994. pp. 1-14
[Kurzweil](https://www.interaction-design.org/references/authors/ray_kurzweil.html), Ray (1999): *The Age of Spiritual Machines: When Computers Exceed Human Intelligence.* Viking Adult

[Lampson](https://www.interaction-design.org/references/authors/b__w__lampson.html), B. W. (1969): Dynamic protection structures. In: [Proceedings of the November 18-20, 1969, fall joint computer conference](https://www.interaction-design.org/references/conferences/proceedings_of_the_november_18-20%2C_1969%2C_fall_joint_computer_conference.html) 1969. pp. 27-38
[Lessig](https://www.interaction-design.org/references/authors/lawrence_lessig.html), Lawrence (1999): *Code and Other Laws of Cyberspace.* Basic Books
[Lindquist](https://www.interaction-design.org/references/authors/christopher_lindquist.html), Christopher (2005): *Fixing the requirements mess*. In [CIO](https://www.interaction-design.org/references/periodicals/cio.html), 0
[Locke](https://www.interaction-design.org/references/authors/john_locke.html),
 John (1963): An essay concerning the true original extent and end of 
civil government: Second of "Two Treatises on Government" (1690). In: [Somerville](https://www.interaction-design.org/references/authors/john_somerville.html), John and [Santoni](https://www.interaction-design.org/references/authors/ronald_santoni.html), Ronald (eds.). "Social and Political Philosophy: Readings From Plato to Gandhi". Anchorp. 169–204

[Lorenz](https://www.interaction-design.org/references/authors/e__n__lorenz.html), E. N. (1963): *Deterministic Nonperiodic Flow*. In [Journal of the Atmospheric Sciences](https://www.interaction-design.org/references/periodicals/journal_of_the_atmospheric_sciences.html), 20 (2) pp. 130-141
[Losavio](https://www.interaction-design.org/references/authors/francisca_losavio.html), Francisca, [Chirinos](https://www.interaction-design.org/references/authors/ledis_chirinos.html), Ledis, [Matteo](https://www.interaction-design.org/references/authors/alfredo_matteo.html), Alfredo, [Levy](https://www.interaction-design.org/references/authors/nicole_levy.html), Nicole and [Ramdane-Cherif](https://www.interaction-design.org/references/authors/amar_ramdane-cherif.html), Amar (2004): *Designing Quality Architecture: Incorporating ISO Standards into the Unified Process*. In [IS Management](https://www.interaction-design.org/references/periodicals/is_management.html), 21 (1) pp. 27-44
[Mandelbaum](https://www.interaction-design.org/references/authors/michael_mandelbaum.html), Michael (2002): *The Ideas that Conquered the World: Peace, Democracy, and Free Markets in the Twenty-first Century.* PublicAffairs

[McCulloch](https://www.interaction-design.org/references/authors/warren_s__mcculloch.html), Warren S. and [Pitts](https://www.interaction-design.org/references/authors/walter_h__pitts.html), Walter H. (1943): *A logical calculus of the ideas immanent in nervous activity*. In[Bulletin of Mathematical Biophysics](https://www.interaction-design.org/references/periodicals/bulletin_of_mathematical_biophysics.html), 5 (4) pp. 115-133
MessageLabs (2006). *The year spam raised its game; 2007 predictions*. Retrieved 19 May 2012 from MessageLabs:
MessageLabs (2010). *Intelligence Annual Security Report, 2010*. Retrieved 19 May 2012 from MessageLabs:
[Meyrowitz](https://www.interaction-design.org/references/authors/joshua_meyrowitz.html), Joshua (1985): *No Sense of Place: The Impact of Electronic Media on Social Behavior.* Oxford University Press, USA
[Miller](https://www.interaction-design.org/references/authors/george_a__miller.html), George A. (1956): *The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information*. In [Psychological Review](https://www.interaction-design.org/references/periodicals/psychological_review.html), 63 pp. 81-97

[Miller](https://www.interaction-design.org/references/authors/isaac_miller.html), Isaac, [Garcia](https://www.interaction-design.org/references/authors/ephrahim_garcia.html), Ephrahim and [Campbell](https://www.interaction-design.org/references/authors/mark_campbell.html), Mark (2006): *To Drive Is Human*. In [IEEE Computer](https://www.interaction-design.org/references/periodicals/ieee_computer.html), 39 (12) pp. 52-56
[Mitchell](https://www.interaction-design.org/references/authors/william_j__mitchell.html), William J. (1995): *City of Bits: Space, Place, and the Infobahn (On Architecture).* The MIT Press
[Moreira](https://www.interaction-design.org/references/authors/ana_moreira.html), Ana, [Araújo](https://www.interaction-design.org/references/authors/jo%E3o_ara%FAjo.html), João and [Brito](https://www.interaction-design.org/references/authors/isabel_brito.html), Isabel (2002): *Crosscutting quality attributes for requirements engineering*. In [Proceedings of the 14th international conference on Software engineering and knowledge engineering SEKE 02](https://www.interaction-design.org/references/periodicals/proceedings_of_the_14th_international_conference_on_software_engineering_and_knowledge_engineering_seke_02.html), (0)
[Norman](https://www.interaction-design.org/references/authors/donald_a__norman.html), Donald A. (1990): *The Design of Everyday Things.* New York, Doubleday

[Nuseibeh](https://www.interaction-design.org/references/authors/bashar_nuseibeh.html), Bashar and [Easterbrook](https://www.interaction-design.org/references/authors/steve_easterbrook.html), Steve (2000): Requirements engineering: a roadmap. In: [Proceedings of the Conference on The Future of Software Engineering](https://www.interaction-design.org/references/conferences/proceedings_of_the_conference_on_the_future_of_software_engineering.html) 2000. pp. 35-46
OECD (1996). *Guidelines for the Security of Information Systems*. Retrieved 19 May 2012 from OECD:
[Penrose](https://www.interaction-design.org/references/authors/roger_penrose.html), Roger (2005): *The Road to Reality : A Complete Guide to the Laws of the Universe.* Knopf
[Pinto](https://www.interaction-design.org/references/authors/jeffrey_k__pinto.html), Jeffrey K. (2002): [*Project Management*](https://www.interaction-design.org/literature/topics/project-management)* 2002*. In [Research Technology Management](https://www.interaction-design.org/references/periodicals/research_technology_management.html), 45 (2) p. 22–37

[Porra](https://www.interaction-design.org/references/authors/jaana_porra.html), Jaana and [Hirschheim](https://www.interaction-design.org/references/authors/rudy_hirschheim.html), Rudy (2007): *A Lifetime of Theory and Action on the Ethical Use of Computers: A Dialogue with Enid Mumford*. In [Journal of the Association for Information Systems](https://www.interaction-design.org/references/periodicals/journal_of_the_association_for_information_systems.html), 8 (9) pp. 467-478
[Poundstone](https://www.interaction-design.org/references/authors/william_poundstone.html), William (1992): *Prisoner's Dilemma.* Anchor
[Raymond](https://www.interaction-design.org/references/authors/eric_s__raymond.html), Eric S. (1999): *The Cathedral & the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary.* OReilly Media
[Regan](https://www.interaction-design.org/references/authors/priscilla_m__regan.html), Priscilla M. (1995): *Legislating Privacy: Technology, Social Values, and Public Policy.* University of North Carolina Press

[Reid](https://www.interaction-design.org/references/authors/fraser_j__m__reid.html), Fraser J. M., [Malinek](https://www.interaction-design.org/references/authors/vlastimil_malinek.html), Vlastimil, [Stott](https://www.interaction-design.org/references/authors/clifford_j__t__stott.html), Clifford J. T. and [Evans](https://www.interaction-design.org/references/authors/jonathan_st__b__t__evans.html), Jonathan ST. B. T. (1996): *The messaging threshold in computer-mediated communication*. In [Ergonomics](https://www.interaction-design.org/references/periodicals/ergonomics.html), 39 (8) pp. 1017-1037
[Ridley](https://www.interaction-design.org/references/authors/matt_ridley.html), Matt (2010): *The Rational Optimist: How Prosperity Evolves.* Harper
[Rosa](https://www.interaction-design.org/references/authors/nelson_s__rosa.html), Nelson S., [Justo](https://www.interaction-design.org/references/authors/george_r__r__justo.html), George R. R. and [Cunha](https://www.interaction-design.org/references/authors/paulo_r__f__cunha.html), Paulo R. F. (2001): *A framework for building non-functional software architectures*. In [Parallel Computing](https://www.interaction-design.org/references/periodicals/parallel_computing.html), pp. 141-147

[Rose](https://www.interaction-design.org/references/authors/e__rose.html), E. (2000): *Balancing internet marketing needs with consumer concerns: a property rights framework*. In[ACM SIGCAS Computers and Society](https://www.interaction-design.org/references/periodicals/acm_sigcas_computers_and_society.html), 30 (2) pp. 20-24
[Samuelson](https://www.interaction-design.org/references/authors/pamela_samuelson.html), Pamela (2003): *Unsolicited communications as trespass?*. In [Communications of the ACM](https://www.interaction-design.org/references/periodicals/communications_of_the_acm.html), 46 (10) pp. 15-20
[Sanai](https://www.interaction-design.org/references/authors/hakim_abu_l_majd_madud_sanai.html), Hakim Abu L Majd Madud (1968): *The Enclosed Garden of Truth.* Theophania Publishing
[Sanders](https://www.interaction-design.org/references/authors/mark_s__sanders.html), Mark S. and [McCormick](https://www.interaction-design.org/references/authors/ernest_j__mccormick.html), Ernest J. (1993): *Human Factors In Engineering and Design.* McGraw-Hill Science
[Seabold](https://www.interaction-design.org/references/authors/daniel_e__seabold.html), Daniel E., [Honemann](https://www.interaction-design.org/references/authors/daniel_h__honemann.html), Daniel H. and [Balch](https://www.interaction-design.org/references/authors/thomas_j__balch.html), Thomas J. (eds.) (1993): *Robert's Rules of Order Newly Revised, 11th edition.* Da Capo Press

[Shannon](https://www.interaction-design.org/references/authors/claude_e__shannon.html), Claude E. and [Weaver](https://www.interaction-design.org/references/authors/warren_weaver.html), Warren (1949): *The Mathematical Theory of Communication.* University of Illinois Press
[Shannon](https://www.interaction-design.org/references/authors/claude_e__shannon.html), Claude E. and [Weaver](https://www.interaction-design.org/references/authors/warren_weaver.html), Warren (1971): *The Mathematical Theory of Communication.* University of Illinois Press
[Shirky](https://www.interaction-design.org/references/authors/clay_shirky.html), Clay (2008): *Here Comes Everybody: The Power of Organizing Without Organizations.* Penguin Press
[Short](https://www.interaction-design.org/references/authors/john_short.html), John, [Williams](https://www.interaction-design.org/references/authors/ederyn_williams.html), Ederyn and [Christie](https://www.interaction-design.org/references/authors/bruce_christie.html), Bruce (1976): *Visual communication and social interaction - The role of 'medium' in the communication process*. In [The Social Psychology of Telecommunications](https://www.interaction-design.org/references/periodicals/the_social_psychology_of_telecommunications.html), pp. 43-60

[Simone](https://www.interaction-design.org/references/authors/mauricio_de_simone.html), Mauricio De and [Kazman](https://www.interaction-design.org/references/authors/rick_kazman.html), Rick (1995): *Software architectural analysis: an experience report*. In [CASCON 95 Proceedings of the 1995 conference of the Centre for Advanced Studies on Collaborative research](https://www.interaction-design.org/references/periodicals/cascon_95_proceedings_of_the_1995_conference_of_the_centre_for_advanced_studies_on_collaborative_research.html),
[Skinner](https://www.interaction-design.org/references/authors/burrhus_f__skinner.html), Burrhus F. (1948): *'Superstition' in the pigeon*. In [Journal of Experimental Psychology](https://www.interaction-design.org/references/periodicals/journal_of_experimental_psychology.html), 38 (2) pp. 168-172
[Smith](https://www.interaction-design.org/references/authors/heather_a__smith.html), Heather A., [Kulatilaka](https://www.interaction-design.org/references/authors/nalin_kulatilaka.html), Nalin and [Venkatramen](https://www.interaction-design.org/references/authors/n__venkatramen.html), N. (2002): *Developments in IS practice III: Riding the wave: extracting value from mobile technology*. In [Communications of the Association for Information Systems](https://www.interaction-design.org/references/periodicals/communications_of_the_association_for_information_systems.html), 8 (0) pp. 467-481

[Sommerville](https://www.interaction-design.org/references/authors/ian_sommerville.html), Ian (2004): *Software Engineering (9th Edition).* Addison Wesley
[Spence](https://www.interaction-design.org/references/authors/robert_spence.html), Robert and [Apperley](https://www.interaction-design.org/references/authors/mark_apperley.html), Mark (2011). *Bifocal Display*. Retrieved 4 November 2013 from [URL to be defined - in press]
[Sperry](https://www.interaction-design.org/references/authors/r__w__sperry.html), R. W. and [Gazzaniga](https://www.interaction-design.org/references/authors/m__s__gazzaniga.html), M. S. (1967): Language following surgical disconnexion of the hemispheres. In:[Millikan](https://www.interaction-design.org/references/authors/darley_millikan.html), Darley (ed.). "Brain Mechanism Underlying Speech and Language". Grune and Stratton
[Tenner](https://www.interaction-design.org/references/authors/edward_tenner.html), Edward (1997): *Why Things Bite Back: Technology and the Revenge of Unintended Consequences (Vintage).* Vintage

[Thompson](https://www.interaction-design.org/references/authors/mary_thompson.html), Mary, [Johnston](https://www.interaction-design.org/references/authors/william_johnston.html), William, [Mudumbai](https://www.interaction-design.org/references/authors/srilekha_mudumbai.html), Srilekha, [Hoo](https://www.interaction-design.org/references/authors/gary_hoo.html), Gary, [Jackson](https://www.interaction-design.org/references/authors/keith_jackson.html), Keith and [Essiari](https://www.interaction-design.org/references/authors/abdelilah_essiari.html), Abdelilah (1999):*Certificate-based Access Control for Widely Distributed Resources*. In [Proceedings of 8th USENIX Security Symposium](https://www.interaction-design.org/references/periodicals/proceedings_of_8th_usenix_security_symposium.html), pp. 215-228
[Toffler](https://www.interaction-design.org/references/authors/alvin_toffler.html), Alvin (1980): *The Third Wave.* Bantam
[Weiss](https://www.interaction-design.org/references/authors/aaron_weiss.html), Aaron (2003): *Ending spam's free ride*. In [netWorker](https://www.interaction-design.org/references/periodicals/networker.html), 7 (2) pp. 18-24
[Whitworth](https://www.interaction-design.org/references/authors/brian_whitworth.html), Brian (2009b): The social requirements of technical systems. In: [Whitworth](https://www.interaction-design.org/references/authors/brian_whitworth.html), Brian and [Moor](https://www.interaction-design.org/references/authors/aldo_de_moor.html),

 Aldo de (eds.). "Handbook of Research on Socio-Technical Design and 
Social Networking Systems (2-Volumes)". Information Science Reference
[Whitworth](https://www.interaction-design.org/references/authors/brian_whitworth.html), Brian (2011): *The Virtual Reality Conjecture*. In [Prespacetime Journal](https://www.interaction-design.org/references/periodicals/prespacetime_journal.html), 2 (9) p. 1404–1433
[Whitworth](https://www.interaction-design.org/references/authors/brian_whitworth.html), Brian (2009a): A Comparison of Human and Computer Information Processing. In: [Pagani](https://www.interaction-design.org/references/authors/margherita_pagani.html), Margherita (ed.). "Encyclopedia of Multimedia Technology and Networking (2 Volume Set)". Idea Group Publishingp. 230–239
[Whitworth](https://www.interaction-design.org/references/authors/brian_whitworth.html), Brian (2006): Measuring disagreement. In: [Reynolds](https://www.interaction-design.org/references/authors/rodney_a__reynolds.html), Rodney A., [Woods](https://www.interaction-design.org/references/authors/robert_woods.html), Robert and [Baker](https://www.interaction-design.org/references/authors/jason_d__baker.html), Jason D. (eds.). "Handbook of Research on Electronic Surveys and Measurements".

[Whitworth](https://www.interaction-design.org/references/authors/brian_whitworth.html), Brian and [Bieber](https://www.interaction-design.org/references/authors/michael_bieber.html), Michael (2002): Legitimate [Navigation](https://www.interaction-design.org/literature/topics/navigation-1) Links. In: [ACM Hypertext 2002, Demonstrations and Posters](https://www.interaction-design.org/references/conferences/acm_hypertext_2002%2C_demonstrations_and_posters.html) 2002, Maryland, USA. pp. 26-27
[Whitworth](https://www.interaction-design.org/references/authors/brian_whitworth.html), Brian and [Friedman](https://www.interaction-design.org/references/authors/robert_s__friedman.html), Robert S. (2009): *Reinventing Academic Publishing Online. Part I: Rigor, Relevance and Practice*. In [First Monday](https://www.interaction-design.org/references/periodicals/first_monday.html), 14 (8)
[Whitworth](https://www.interaction-design.org/references/authors/brian_whitworth.html), Brian and [Liu](https://www.interaction-design.org/references/authors/tong_liu.html), Tong (2008): Politeness as a Social Computing Requirement. In: [Luppicini](https://www.interaction-design.org/references/authors/rocci_luppicini.html),
 Rocci (ed.). "Handbook of Conversation Design for Instructional 
Applications (Premier Reference Source)". Information Science 
Referencepp. 419-436

[Whitworth](https://www.interaction-design.org/references/authors/brian_whitworth.html), Brian and [Liu](https://www.interaction-design.org/references/authors/tong_liu.html), Tong (2009): *Channel E-mail: A Sociotechnical Response to Spam*. In [IEEE Computer](https://www.interaction-design.org/references/periodicals/ieee_computer.html), 42 (7) pp. 63-72
[Whitworth](https://www.interaction-design.org/references/authors/brian_whitworth.html), Brian and [Moor](https://www.interaction-design.org/references/authors/aldo_de_moor.html), Aldo de (2002): Legitimate by Design: Towards Trusted Virtual Community Environments. In: [HICSS 2002](https://www.interaction-design.org/references/conferences/hicss_2002.html) 2002. p. 213
[Whitworth](https://www.interaction-design.org/references/authors/brian_whitworth.html), Brian and [Whitworth](https://www.interaction-design.org/references/authors/alex_p__whitworth.html), Alex P. (2010): *The social environment model: Small heroes and the evolution of human society*. In [First Monday](https://www.interaction-design.org/references/periodicals/first_monday.html), 15 (11)
[Whitworth](https://www.interaction-design.org/references/authors/brian_whitworth.html), Brian and [Whitworth](https://www.interaction-design.org/references/authors/elizabeth_whitworth.html), Elizabeth (2004): *Spam and the Social-Technical Gap*. In [Computer](https://www.interaction-design.org/references/periodicals/computer.html), 37 (10) pp. 38-45

[Whitworth](https://www.interaction-design.org/references/authors/brian_whitworth.html), Brian, [Bañuls](https://www.interaction-design.org/references/authors/victor_ba%F1uls.html), Victor, [Sylla](https://www.interaction-design.org/references/authors/cheickna_sylla.html), Cheickna and [Mahinda](https://www.interaction-design.org/references/authors/edward_mahinda.html), Edward (2008): *Expanding the Criteria for Evaluating Socio-Technical Software*. In [IEEE Transactions on Systems, Man, and Cybernetics](https://www.interaction-design.org/references/periodicals/ieee_transactions_on_systems%2C_man%2C_and_cybernetics.html), 38 (4) pp. 777-790
[Whitworth](https://www.interaction-design.org/references/authors/brian_whitworth.html), Brian, [Gallupe](https://www.interaction-design.org/references/authors/brent_gallupe.html), Brent and [McQueen](https://www.interaction-design.org/references/authors/robert_mcqueen.html), Robert (2000): *A cognitive three-process model of computer-mediated group interaction*. In [Group Decision and Negotiation](https://www.interaction-design.org/references/periodicals/group_decision_and_negotiation.html), 9 (5) pp. 431-456

[Whitworth](https://www.interaction-design.org/references/authors/brian_whitworth.html), Brian, [Gallupe](https://www.interaction-design.org/references/authors/brent_gallupe.html), Brent and [McQueen](https://www.interaction-design.org/references/authors/robert_mcqueen.html), Robert (2001): *Generating agreement in computer-mediated groups*. In [Small Group Research](https://www.interaction-design.org/references/periodicals/small_group_research.html), 32 (5) pp. 625-665
[Wright](https://www.interaction-design.org/references/authors/robert_wright.html), Robert (2001): *Nonzero: The Logic of Human Destiny.* Vintage
**Chapter TOC**
[**Human-Computer Interaction: The Foundations of UX Design**](https://www.interaction-design.org/courses/hci-foundations-of-ux-design)
![](https://public-media.interaction-design.org/images/courses/hds/course_72--square_thumbnail.jpg?tr=fo-auto)
Human-Computer Interaction: The Foundations of UX Design
Closes in
10
days
booked
View Course

## 获取每周 UX 洞察

加入 **314,337 位设计师** 的行列，通过我们的时事通讯（Newsletter）获取实用的用户体验（User Experience, UX）技巧。
需要提供有效的电子邮件地址。

## 本书章节涵盖的主题：

[社会技术系统（Socio-Technical Systems）](https://www.interaction-design.org/literature/topics/socio-technical-systems)
[用户体验（User Experience, UX）设计](https://www.interaction-design.org/literature/topics/ux-design)
[人机交互（Human-Computer Interaction, HCI）](https://www.interaction-design.org/literature/topics/human-computer-interaction)
[设计史（Design History）](https://www.interaction-design.org/literature/topics/design-history)
[社会结构（Social Structures）](https://www.interaction-design.org/literature/topics/social-structures)
[社会计算（Social Computing）](https://www.interaction-design.org/literature/topics/social-computing)
