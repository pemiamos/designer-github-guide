# 39. 用户界面设计适配（User Interface Design Adaptation）

**来源**：The Encyclopedia of Human-Computer Interaction, 2nd Ed.
**Notion 原页面**：https://www.notion.so/e805d3b5cca944ddb4030727ca105397

---

[Fabio Paterno](https://www.interaction-design.org/literature/author/fabio-paterno)
本章旨在帮助[用户界面](https://www.interaction-design.org/literature/topics/ui-design)（User Interface）设计师和开发人员理解多设备交互应用（multi-device interactive applications）中所涉及的问题。这些应用可以通过移动设备（mobile devices）和固定设备（stationary devices）访问，甚至可以利用不同的交互模态（interaction modalities）（如图形化、语音等）。本章从概念、技术、语言和工具等方面讨论了可能的解决方案，并特别关注 Web 环境。本章探讨了根据使用情境（context of use）对用户界面进行适配（adapting）、分发（distributing）和迁移（migrating）的各种策略。它研究了在构建（authoring）多设备界面时，以及在针对不同设备的界面进行动态适配、分发，甚至为了跟随移动用户而跨设备无缝迁移时，应如何解决这些问题。因此，本章讨论了迁移界面（migratory interfaces）中跨设备任务连续性（task continuity）以及相关的[可用性](https://www.interaction-design.org/literature/topics/usability)（usability）问题。

## 39.1 引言 (Introduction)

自适应（Adaptation）重要性日益增加的主要原因之一是，随着移动技术和智能环境的出现，我们与应用程序交互的[使用情境（contexts of use）](https://www.interaction-design.org/literature/topics/contexts-of-use)变得越来越多样化。
各种因素都可以成为可能的使用情境的一部分，并可分为四个维度（见图 1）：
- *用户相关维度（user-related aspects）*：偏好、目标与任务、生理状态（如位置）、情绪状态等；
- *技术相关维度（technology-related aspects）*：屏幕分辨率、连接性、浏览器、电池等；
- *环境相关维度（environment-related aspects）*：位置、光线、噪音等；
- [*社会维度（social aspects）*](https://www.interaction-design.org/literature/topics/social-aspects)：隐私规则、[协作（collaboration）](https://www.interaction-design.org/literature/topics/collaboration)等。

根据使用情境中这些维度的变化，用户界面的任何特征都可以被修改。因此，用户界面可以在以下方面进行自适应：*呈现（presentation）*——可感知方面，包括媒介与交互技术、布局、图形属性；*动态行为（dynamic behaviour）*——包括[导航（navigation）](https://www.interaction-design.org/literature/topics/navigation-1)结构、交互技术的动态激活与去激活；以及*内容（content）*——包括文本、标签和图像。

各种适配策略（adaptation strategies）都是可能的，可以根据它们对用户界面（user interface, UI）的影响进行分类：*保留（conservation）*，例如 UI 元素的简单缩放；*重排（rearrangement）*，例如更改布局；*简化（simplification）* / *放大（magnification）*，即相同的 UI 元素但修改了呈现方式；以及在 UI 元素方面的*增加（increase）*（也称为*渐进增强（progressive enhancement）*）/ *减少（reduction）*（也称为*优雅降级（graceful degradation）*）。

![](https://public-media.interaction-design.org/images/encyclopedia/user_interface_design_adaptation/user_interface_design_adaptation.001.jpg)
作者/版权持有者：Courtesy of Fabio Paterno。版权条款和许可：CC-Att-ND-3 (Creative Commons Attribution-NoDerivs 3.0 Unported)。
**图 39.1**：使用情境（The Context of Use）

用户界面适配日益受到关注的主要原因之一是技术演进（尤其是移动设备）所引发的设备碎片化（device fragmentation）。设备碎片化涉及硬件以及对格式、浏览器、音频/视频播放/流媒体等支持的情况。例如，在屏幕方面，我们可以注意到个人计算机（PC）的屏幕分辨率（screen resolution）通常在 800x600 到 1920x1200 像素之间，而移动设备的屏幕分辨率则在 320x240 到 1136x640 像素（iPhone 5）之间，最高可达 1920×1080（Galaxy S 4）。因此，移动设备的屏幕分辨率波动比桌面设备更大。有趣的一点是

摩尔定律（Moore’s Law）不断地改变着这些数值，我们可以预见在不久的将来会出现更大的波动。近年来，移动技术发生了显著演进。观察智能手机中交互方式的变化，我们很容易意识到这一点。最早期的设备采用的是*基于焦点的交互（focus-based interactions）*，在这种模式下，浏览器焦点（browser focus）在各个元素之间循环切换；由于当前处于焦点状态的元素会被高亮显示，因此可以轻松确定页面的当前焦点，且焦点在可选元素（selectable element）之间（例如从一个链接到另一个链接）仅能按顺序移动，即使元素之间距离较远（这可能会耗费一些时间）。随后，人们提出了支持*基于指针的交互（pointer-based interaction）*的设备，在这种设备中，*基于按键的（key-based）*导航可以控制一个能够覆盖屏幕任何部分的指针。在这种方案中，可选元素需要足够大，以便于

[它们]很容易被选中，因为指针通常以 5-10 像素为步长移动，且可选中元素应具有悬停效果（Rollovers），以便在指针进入其激活区域时清晰地告知用户。在基于指针的交互之后，现在是*基于触摸的交互*（*Touch-based interaction*）大获成功，在这种交互中，事件直接与手指或触控笔在屏幕上的触摸位置相关联；可选中元素应保持较大的间距，以便用户能够精确地选择它们（研究建议间距在 7mm 到 9.6mm 之间），且可选中元素必须足够大以便于选择；在被选中之前，没有任何元素处于焦点状态（In focus），因此无法向用户传递额外信息（例如，悬停效果失效）。

多种设计考量有助于提升移动交互的可用性（Usability）。我们必须考虑到用户可能处于移动状态，且能投入在交互上的注意力有限。因此，尽量减少文本输入、保持平台之间的一致性（Consistency）以使通过桌面交互获得的应用程序知识能够在移动访问中复用从而防止用户错误、避免用户界面因元素过多而过载、限制缩放（Zooming）需求，以及防止触摸选择时偏离预期目标，这些都至关重要。总的来说，我们必须考虑到移动用户可用的访问时间通常较短，因此他们更倾向于获取碎片化的信息。

更广泛地说，我们必须考虑到我们的生活正变成一种多设备[用户体验（User Experience, UX）](https://www.interaction-design.org/literature/topics/ux-design)。事实上，一项最近的研究（Google, 2012）发现，我们的在线时间分布在四类设备中（智能手机、平板电脑、个人电脑/笔记本电脑、电视）。使用这些设备有两种模式：*顺序使用（sequential usage）*，即在不同时间从一台设备转移到另一台设备以完成一项任务；以及*同时使用（simultaneous usage）*，即在同一时间使用多台设备来执行相关或不相关的活动。在此类设备之间管理信息是使用多设备的一个具有挑战性的方面。总的来说，多设备用户界面（multi-device User Interfaces, UIs）的主要问题在于：对使用情境（context of use）的适应性较差，通过不同设备执行的任务之间缺乏协调，以及对无缝跨设备任务执行（seamless cross-device task performance）的支持不足。

一些研究已开始探讨跨设备应用程序访问（cross-device application access）中用户体验的特征。例如，在 Waljas et al. (2010) 中，作者确定了提升跨设备用户体验的三个重要维度：*任务执行的适当性（appropriateness for task performance）*，旨在使交互应用程序的结构能够提供一个

与用户在每种设备[类型](https://www.interaction-design.org/literature/topics/type)中期望执行的操作具有良好的适配性（effective fit）；*连续性（continuity）*，使设备内及跨设备的交互流（flow of interaction）被感知为流畅且连贯；*一致性（consistency）*，即各种设备类型的用户界面应被感知为具有统一性（coherent），且仍属于同一个应用程序。

## 39.2 用户界面/任务/平台关系（User Interface/Task/Platform Relations）

在本节中，我们将讨论一个逻辑框架（Logical framework），该框架允许设计者思考待执行的任务、用户界面（User Interface, UI）以及可用平台（Platform）之间各种可能的关系。我们所指的平台是指共享相似交互资源（Interaction resources）的一组设备，例如台式机、智能手机和平板电脑。具体而言，我们确定了五种可能的关系：

- 在不同平台上使用相同的用户界面执行相同的任务
- 在不同平台上使用不同的用户界面执行相同的任务
- 在不同平台上执行相同的主任务，但具有不同层级的子任务（Subtasks）
- 在不同平台上执行的不同任务之间的依赖关系（Dependencies）
- 仅在某些平台类型上才有意义的任务（例如，因为它们需要极长时间的访问，或者与移动位置或特定设备如摄像头相关）。

由于移动技术的种类迅速增加，不同平台之间确实存在显著差异。其结果是，对于同一个任务，有时根据平台的不同，不同的用户界面更为合适；而某些特定任务则仅在特定平台上才真正合适。例如，通过智能手机观看足球比赛是没有意义的，即使在技术上可行，因为小屏幕不适合在九十分钟的时间段内使用，且比赛的许多细节无法被

……值得赞赏。另一方面，在舒适地坐在沙发上，面前放置一个距离适中的大屏幕时，进行这项活动是非常愉快的。

图 2 展示了在不同平台（platforms）上使用不同用户界面（User Interfaces, UI）执行同一任务的示例。该任务是展示空间信息（spatial information）。左侧是桌面设备（desktop device）版本，它覆盖了更广的空间区域，并提供了一个概览图，用以突出显示细节视图（detail view）所在的位置。右侧是移动设备（mobile device）版本，它突出了移动用户的当前位置，显示较小的区域，并可通过触控操作来更改缩放级别（zoom level）。

![](https://public-media.interaction-design.org/images/encyclopedia/user_interface_design_adaptation/user_interface_design_adaptation.002.jpg)
作者/版权持有者：Google Maps。版权条款与许可：保留所有权利（All Rights Reserved）。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用（因为无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面中的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

![](https://public-media.interaction-design.org/images/encyclopedia/user_interface_design_adaptation/user_interface_design_adaptation.003.jpg)
作者/版权持有者：Google Maps。版权条款与许可：保留所有权利。根据公平使用原则在未经许可的情况下使用（因为无法获得许可）。

（无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面中的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

**图 39.2 A-B**：相同任务在不同用户界面（User Interface, UI）下的示例

图 3 展示了同一主任务在不同用户界面以及部分不同子任务（Subtasks）下的第二个示例。在本例中，主任务是展示某航空公司的航班信息。我们可以注意到，两种 UI 都支持搜索航班和预订机票的功能，但采用了不同的呈现方式和布局；在移动端版本中，交互元素（Interactive elements）更大，以方便触控交互（Touch interaction）；而在桌面端版本中，用户还可以访问额外的信息，例如促销活动。

![](https://public-media.interaction-design.org/images/encyclopedia/user_interface_design_adaptation/user_interface_design_adaptation.004.jpg)

作者/版权持有者：Air France。版权条款与许可：保留所有权利（All Rights Reserved）。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用（因无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面中的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

![](https://public-media.interaction-design.org/images/encyclopedia/user_interface_design_adaptation/user_interface_design_adaptation.005.jpg)

作者/版权

持有者：Air France。版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面中的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

**图 39.3 A-B**：同一任务在不同用户界面（User Interfaces）下的示例

下图展示了两个应用程序的示例，其移动端版本支持一些仅在该平台上有意义的任务。顶部是一个使用关键词“restaurant”进行搜索的示例：移动端版本在地图和列表中显示一组附近餐厅，其中每个条目都包含一个按钮，用于立即向相应的餐厅拨打电话。在右下方，我们可以看到 Flickr 的移动端版本如何实现显示在当前移动位置附近拍摄的照片。

![](https://public-media.interaction-design.org/images/encyclopedia/user_interface_design_adaptation/user_interface_design_adaptation.006.jpg)

作者/版权持有者：Google Maps。版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面中的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

![](https://public-media.interaction-design.org/images/encyclopedia/user_interface_design_adaptation/user_interface_design_adaptation.007.jpg)
作者/版权持有者：Google Maps。版权条款与许可：保留所有权利（All Rights Reserved）。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用（由于无法获得许可）。请参阅 [版权声明（copyright notice）](https://www.interaction-design.org/about/terms-of-use) 页面中的“例外（Exceptions）”章节（以及“allRightsReserved-UsedWithoutPermission”小节）。

![](https://public-media.interaction-design.org/images/encyclopedia/user_interface_design_adaptation/user_interface_design_adaptation.008.jpg)
作者/版权持有者：Flickr。版权条款与许可：保留所有权利（All Rights Reserved）。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用（由于无法获得许可）。请参阅 [版权声明（copyright notice）](https://www.interaction-design.org/about/terms-of-use) 页面中的“例外（Exceptions）”章节（以及“allRightsReserved-UsedWithoutPermission”小节）。

![](https://public-media.interaction-design.org/images/encyclopedia/user_interface_design_adaptation/user_interface_design_adaptation.009.jpg)
作者/版权持有者：Flickr。版权条款与许可：保留所有权利（All Rights Reserved）。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用（由于无法获得许可）。请参阅 [版权声明（copyright notice）](https://www.interaction-design.org/about/terms-of-use) 页面中的“例外（Exceptions）”章节（以及“allRightsReserved-UsedWithoutPermission”小节）。

**图 39.4 A-B-C-D**：仅在某些平台（Platform）上具有意义的任务示例

## 39.3 构建多设备交互应用（Authoring Multi-Device Interactive Applications）

构建多设备交互应用需要改变传统的交互应用开发方式。解决这一问题有多种方法。最简单的方法是为每个目标平台（Target Platform）分别开发特定版本。通过这种方式，开发者可以完全控制每个版本的具体细节。然而，这意味着开发交互应用的工作量将随着目标平台数量的增加而倍增。因此，这会导致开发和维护成本的增加。事实上，如果应用需要进行任何更改，则每个版本都需要同步更新。

另一种方法是开发一个具有流式布局（Fluid Layout）的主版本及其子版本。这就是响应式 [Web 设计](https://www.interaction-design.org/literature/topics/web-design)（Responsive Web Design）的实现方式，作者通过实现流体布局（Liquid Layouts）并利用媒体查询（Media Query）支持来识别不同类型的设备。针对识别出的每种设备类型，他们提供相应的样式表（Stylesheets），通过样式表可以更改某些属性的值，或者显示或隐藏某些元素。这可能是解决该问题的一种相对低成本的方法，但在某些情况下，它会限制不同版本之间能实现的差异，因为样式表不允许对交互应用的结构进行深层更改。

另一种方法是单一创作（Single Authoring），在这种方法中，一个关于...的概念描述（Conceptual Description）...

交互式应用程序被开发，并从中获得针对各种目标平台（target platforms）进行优化的不同版本。另一种解决方案是自动重构（automatic reauthoring），其起点是针对特定平台的实现，然后通过适当的转换（transformations）推导出适配于不同平台的实现。

研究界为此提出了多种解决方案。其中一个例子是 SUPPLE (Gajos, Weld, and Wobbrock, 2010)，它采用了接口的功能规范（functional specification）、设备特定约束（device-specific constraints）、典型的使用轨迹（usage trace）以及一个代价函数（cost function）。该代价函数基于用户偏好和预期的操作速度。SUPPLE 的优化算法旨在寻找一个既能使代价函数最小化，又能满足所有设备约束的用户界面。

![](https://public-media.interaction-design.org/images/encyclopedia/user_interface_design_adaptation/user_interface_design_adaptation.010.jpg)
作者/版权持有者：SUPPLE (Gajos, Weld, and Wobbrock)。版权条款和许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 39.5**：SUPPLE 环境 (Gajos, Weld, and Wobbrock, 2010)

随后，SUPPLE 的作者专注于如何利用 SUPPLE 来支持残障用户，例如通过自动生成用户

基于用户实际运动能力（motor abilities）模型的接口，旨在服务于灵活性受损（impaired dexterity）的用户。更广泛地说，我们可以认为自适应（adaptation）对于永久性和暂时性障碍（permanent and temporary disabilities）都具有实用价值。暂时性障碍的一个例子是，当用户需要快速移动并与图形化移动设备进行交互时，其视觉注意力（visual attention）无法完全分配给交互过程。构建多设备用户界面（multi-device user interfaces）的最早方法之一是 Damask (Lin and Landay, 2008)，它支持三种平台类型的构建：桌面端、智能手机和语音端。Damask 基于三个方面：草图（sketches）、图层（layers）和模式（patterns）。草图用于便捷地指示用户界面的外观。图层用于指示用户界面的某个部分应当分配给所有设备，还是仅分配给某个特定的平台。模式则用于识别

为了便于在不同应用程序中实现复用（Reuse），针对重复出现的问题所提出的解决方案。

![](https://public-media.interaction-design.org/images/encyclopedia/user_interface_design_adaptation/user_interface_design_adaptation.011.jpg)
作者/版权持有者：Damask (Lin and Landay)。版权条款与许可：保留所有权利。经许可转载。请参阅下文[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 39.6**：Damask 创作环境（Authoring Environment）(Lin and Landay, 2008)

## 39.4 适配规则（Adaptation Rules）

用户界面如何适配使用情境（context of use）可以通过一系列规则来描述，而这些规则可以根据其所能实现的效用类型进行分类。

部分适配由*替换规则（replacement rules）*组成：它们规定了如何根据当前平台替换某些元素。待替换的元素可以是单个用户界面元素，如图 7 所示。在图底部，我们可以看到一个用于查询火车时刻表的应用程序：其桌面版本通过一个较长的下拉菜单（drop-down menu）来实现小时选择，而移动版本则使用选项数量有限的单选按钮（radio button），因为可选的小时已被分组。

![](https://public-media.interaction-design.org/images/encyclopedia/user_interface_design_adaptation/user_interface_design_adaptation.012.jpg)
作者/版权持有者：Courtesy of TrenItalia, ViaggiaTreno (AllRightsRerserved, FairUse)。版权条款与许可：compositeWorkWithMultipleCopyrightTerms（由具有不同版权条款和/或版权持有者的多个作品衍生或组成的作品）。

**图 39.7**：单个元素替换规则的示例

图 8 展示了替换规则如何应用于一组元素而非单个元素。在此示例中，分组是指针对特定地点的酒店查询结果（query results）。桌面版本（左侧）展示结果组的方式旨在提供额外的

信息（例如之前访客的评论），而移动端版本（右图）仅在请求时显示详情，通过易于触控选择的元素来实现。
![](https://public-media.interaction-design.org/images/encyclopedia/user_interface_design_adaptation/user_interface_design_adaptation.013.jpg)
作者/版权持有者：TripAdvisor。版权条款和许可：保留所有权利。根据合理使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面中的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。
**图 39.8**：一组元素的替换规则（replacement rule）示例。

另一种类型的规则是将用户界面（User Interface, UI）*拆分（splitting）*为两个或多个独立的呈现方式。可以通过两种方式获得新界面：一种是创建独立的界面，另一种是通过动态地显示和隐藏元素以达到类似的效果。图 9 展示了页面拆分（page splitting）的一个示例。这里以著名的 PacMan 游戏为例：左侧是单页呈现方式，右侧是针对小屏幕的版本，其中包含两种呈现方式：一种用于进行游戏，另一种用于定义各种设置。
![](https://public-media.interaction-design.org/images/encyclopedia/user_interface_design_adaptation/user_interface_design_adaptation.014.jpg)
作者/版权

持有者：PacMan 的各种实现版本（版权归 Namco Limited 所有）。
版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面中的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

**图 39.9**：页面拆分（Page splitting）示例

在其他情况下，适配（Adaptation）需要移除规则（Removal rules）。其目的是移除被认为与目标设备（Target device）无关的内容。造成这种情况的原因可能有多种：技术限制或厂商选择（例如，iPhone 不支持 Flash 视频）；由于在新型设备中消耗的资源过高而被移除的对象；以及支持被认为与目标设备无关的任务的元素。需要注意的是，移除元素可能会对脚本执行（Script execution）产生影响，因为脚本可能会引用这些元素，如果它们被移除，脚本可能无法正常运行。

最常用的适配规则是旨在更改某些用户界面属性（User interface properties）的规则。在这种情况下，UI 元素保持不变，但其呈现方式在以下方面发生变化：其属性（例如颜色、尺寸等）；它们在 UI 中的位置；它们之间的间距；以及整体的用户界面结构。

适配规则可以用以下格式表示：事件 / 条件 / 动作（Event / Condition / Action）。事件的发生会触发...

规则的评估。基础事件（Elementary events）发生在交互式应用程序（interactive application）中、使用情境（context of use）中，或者是这些事件的组合。条件（condition，可选）是一个需要满足的布尔条件（Boolean condition），以便执行相关的动作；它可能与之前发生的事情或某种状态条件相关。动作（action）指明了交互式应用程序的抽象/具体/实现描述应如何更改，以执行请求的自适应（adaptation）。它可以在不同的粒度（granularities）上更改用户界面（User Interface, UI）：完全更改 UI、更改部分 UI 模块、更改 UI 元素，或更改特定 UI 元素的属性。以下是一些自适应规则的示例：

- 事件（用户选择了打印机描述的链接）；条件（用户选择了三个以上的打印机描述链接）；动作（显示销量最高的五款打印机）
- 事件（电池电量变化）；条件（如果电池电量低于给定阈值）；动作（更改屏幕亮度）
- 事件（用户访问应用程序）；条件（用户为老年人）；动作（将字体大小增加 10%）
- 事件（（用户在户外）且（正值午餐时间））；条件（附近有餐厅）；动作（显示附近餐厅列表）
- 事件（访问应用程序）；条件（设备为手机）；动作（在不同的呈现方式中显示主视图和详情视图）

如果我们要考虑[无障碍性（Accessibility）](https://www.interaction-design.org/literature/topics/accessibility)是一个重要方面的应用程序，我们可以参考以下不同适配规则（Adaptation rules）的示例 (Minon et al. 2013)：

- 事件（Event）：环境噪音变化至 25 分贝以上；条件（Condition）：用户患有轻度听力障碍（Hearing impairment）；动作（Action）：所有视频必须显示字幕。
- 事件（Event）：用户访问一个包含许多交互元素（Interaction elements）的应用程序；条件（Condition）：用户失明；动作（Action）：创建应用程序目录（Table of content），以便于访问每个交互元素。
- 事件（Event）：用户界面（User Interface, UI）被激活；条件（Condition）：用户是色盲（Colour-blind）；动作（Action）：将前景色改为黑色，背景色改为白色，以提供高对比度 UI（High-contrast UI）。
- 事件（Event）：UI 包含一个带有超时（Timeout）设置的元素；条件（Condition）：用户患有认知障碍（Cognitive disability）；动作（Action）：移除超时设置，或在必要时大幅增加时间限制。
- 事件（Event）：用户界面被激活；条件（Condition）：用户视力不佳（Poor vision）；动作（Action）：激活屏幕放大镜（Screen magnifier）。
- 事件（Event）：用户开始移动；条件（Condition）：用户患有下半身瘫痪（Paraplegia）且 UI 未以语音模态（Vocal modality）呈现；动作（Action）：将用户界面切换为语音模态。
- 事件（Event）：应用程序包含许多不同的交互元素，用于同时执行不同的任务；条件（Condition）：用户在维持...方面存在问题

注意力；操作（Action）：用户界面（User Interface, UI）的组织方式使得一次只能支持一项任务。

另一个需要考虑的重要方面是，运行在移动设备上的应用程序通常需要适应上下文事件（Contextual events）。因此，人们对于提供能够让非编程人员也能定义其上下文相关应用（Context-dependent applications）的环境产生了越来越浓厚的兴趣。Tasker (footnote 1) 是一款 Android 应用程序，它允许用户基于简单的事件触发规则（Event-trigger rules）执行上下文敏感操作（Context-sensitive actions）。用户可以在用户定义的配置文件（Profiles）中，根据上下文（Contexts，取决于应用程序、时间、日期、位置、事件、手势、状态等因素）创建以任务（Tasks，即一组操作，可以是激活警报或应用程序，更改音频或显示属性等）为形式的上下文敏感规则。尽管 Tasker 在可开发的应用类型方面仍有局限，但它无论如何是一个开始，并且进一步证明了此类贡献的实用性。Locale (footnote 2) 是另一款 Android 应用程序，它允许用户创建“情境”（Situations），并指定在何种条件下应更改用户的手机设置。使用此类工具可以实现的一条规则示例为：下午 4 点后，如果电池电量低于 20% 且 WiFi 已启用，则禁用 WiFi 并降低屏幕亮度（Luminosity）。

## 39.5 多设备上下文中的基于模型的 UI 设计（Model-based UI Design in Multi-Device Contexts）

模型（Models）是真实实体的抽象。我们在生活中使用模型的频率比通常认为的要高。例如，我们经常在早晨思考当天要执行的主要活动，从而创建了一个关于这一天的模型。

在基于模型的方法（model-based approaches）中，其核心思想是使用以概念化术语（conceptual terms）描述主要方面的语言，以便让设计者和开发人员能够专注于主要的语义方面，而无需学习大量的实现语言（implementation languages）。通过这种方式，还可以将语义信息与实现元素联系起来。这里指的是交互语义（interaction semantics），它定义了用户界面元素的用途。这使得通过多种可能的实现语言来实现设备互操作性（device interoperability）成为可能，因为可以通过实现生成器（implementation generators）从逻辑描述中导出各种适配的实现。语义化描述的另一个优势是，由于每个元素的用途定义得更清晰，因此有利于[辅助技术（assistive technology）](https://www.interaction-design.org/literature/topics/assistive-technology)的支持。

从事基于模型方法研究的社区已就描述交互式应用程序时可考虑的若干抽象级别（abstraction levels）达成共识，它们分别是：

- *任务与领域对象（Tasks and domain objects）*：此层级的目的是描述为了实现用户目标而应执行的活动，以及为此目的需要操作的对象。该层级的一个概念示例是“我想选择一件艺术品”。用于表示此类描述的符号系统包括 ConcurTaskTrees (Paterno, 2000) 或 GOMS (John and Kieras, 1996)。
- *抽象交互应用（Abstract Interactive Application）*：此层级的重点转移到应用的交互部分，旨在提供一种独立于所采用的交互模态（Interaction modality）的描述方式。该层级的一个概念示例是“具有高基数（High cardinality）的单选对象”。这里需要一个能够实现此效果的交互对象，而无需指定任何依赖于模态的细节；因此，它并不指明该对象是通过图形交互、语音命令还是手势来选择的。
- *具体交互应用（Concrete Interactive Application）*：其描述依赖于模态，但独立于实现语言（Implementation language）。一个概念示例是“包含 X 个元素的列表交互对象”。其假设是使用了图形模态且需要一个列表元素。然而，这种列表元素可以通过多种不同的实现语言来获取。

- *交互式应用程序实现（Interactive Application Implementation）*：此处是指使用某种实现语言进行的实际开发。例如，列表对象（List object）可以在 Java 用户界面工具包（如 AWT）、HTML 或其他用户界面库中实现。

图 10 展示了一个通过基于模型的方法（model-based approach）构建的多设备用户界面的简例。在左上部分，有一个由两个元素组成的抽象描述（abstract description）：一个用于进行选择，另一个用于提供一个范围值。随后，我们可以看到针对移动设备、桌面设备和家用电器的三种可能实现方式。其中，“选择”在移动设备中通过单选按钮（radio button）实现，在桌面设备中通过两个按钮实现，在物理设备中通过开关（switch）实现；而“范围值”在移动设备中通过滑块（slider）获取，在桌面设备中通过数值调节框（spin-box）获取，在电器中则通过杠杆（lever）获取。

![](https://public-media.interaction-design.org/images/encyclopedia/user_interface_design_adaptation/user_interface_design_adaptation.015.jpg)
作者/版权持有者：Fabio Paterno。版权条款与许可：保留所有权利。经许可转载。详见下文 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”章节。

**图 39.10**：多设备用户界面的基于模型描述示例

目前 W3C 成立了一个关于基于模型的用户界面（Model-based UI）的工作组，正在基于这些概念开发相关标准（详见 [http://www.w3.org/2011/mbui/](http://www.w3.org/2011/mbui/)）。此外，这些概念已被证明对可访问性（Accessibility）非常有益。事实上，最近 W3C 又成立了另一个小组——独立用户界面（Independent User Interface, IndieUI）小组 ([http://www.w3.org/WAI/intro/indieui](http://www.w3.org/WAI/intro/indieui))。该小组旨在使 Web 应用程序能够更轻松地在广泛的场景（Contexts）中运行，包括不同的设备、不同的辅助技术（Assistive Technologies, AT）以及不同的[用户需求](https://www.interaction-design.org/literature/topics/user-needs)。

图 11 展示了一个示例，说明应用程序如何以一种独立于具体触发技术的方式来管理一个事件（Event，例如“向下滚动”）。

![](https://public-media.interaction-design.org/images/encyclopedia/user_interface_design_adaptation/user_interface_design_adaptation.016.jpg)
作者/版权持有者：Fabio Paterno。版权条款和许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 39.11**：抽象事件（Abstract Event）示例

基于模型的方法存在的一个问题是，模型的开发有时会产生设计师无法解决的需求。为了部分地

为了解决这个问题，人们开发了[逆向工程（Reverse Engineering）](https://www.interaction-design.org/literature/topics/reverse-engineering)的方法和工具。其基本思路是，此类工具能够分析用户界面（User Interface）的实现，并构建相应的底层模型（Underlying model）。Bellucci et al. (2012) 描述了一个示例，其中介绍的工具能够分析网页（包括相关的样式表），并构建相应的逻辑描述，从而保留原始脚本。

最成熟的基于模型的语言（Model-based languages）之一是 MARIA (Paterno et al., 2009)，它包括：对数据模型（Data Model）的支持，用于指定输入值的格式，以及将各种数据对象与各种交互组件（Interactors）相关联；一个事件模型（Event Model），它将每个交互组件与一组事件相关联，这些事件可以是属性变更事件（Property change events）或激活事件（Activation events）（例如，访问 Web 服务或数据库）；一个对话模型（Dialogue Model），用于指定动态行为（即在给定时间可以触发哪些事件）。对话表达式使用 CTT 算子（CTT operators）连接，以定义它们的时间关系；能够支持包含复杂 Ajax 脚本的用户界面，这些脚本可以通过调用外部函数（可实现为 Web 服务）在无需用户明确请求的情况下持续更新字段；以及动态的用户界面元素集，可以通过...

呈现方式（Presentations）之间的条件连接，或者仅更改 UI 部分的可能性。值得注意的是，HTML 5 也在朝着同样的方向演进，它引入了许多更具语义化的标签（Semantic Tags，如 `navbar`、`article` 等），这些标签为相关元素的用途提供了更明确的提示。然而，HTML 5 主要局限于基于图形和表单的用户界面。因此，它无法应对日益增多的各种交互模态（Interaction Modalities）。MARIA 还由一个创作环境（Authoring Environment）MARIAE（MARIA Environment，公开访问地址为 [http://giove.isti.cnr.it/tools/MARIAE/home]）提供支持，该环境提供了图形化的直接操纵（Direct Manipulation）支持，用于在不同的抽象层级（Abstraction Levels）上编辑交互式应用程序并生成...

针对各种平台相应的实现，并采用了不同的交互模态（Interaction Modalities）。图 12 展示了该工具如何支持编辑逻辑描述（Logical Description）；左侧是代表应用程序结构的交互式树（Interactive Tree），中间区域是所选呈现（Presentation）的图形化表示（Graphical Representation），用户可以将右侧动态显示的相应元素通过拖拽（Drag-and-drop）方式移入。

![](https://public-media.interaction-design.org/images/encyclopedia/user_interface_design_adaptation/user_interface_design_adaptation.017.jpg)

作者/版权持有者：HIIS Laboratory。版权条款与许可：保留所有权利（All Rights Reserved）。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用（因无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面上的“例外（Exceptions）”章节（以及“allRightsReserved-UsedWithoutPermission”小节）。

**图 39.12**：MARIAE 创作环境（Authoring Environment）

## 39.6 适配阶段的技术

在自动适配（automatic adaptation）中，我们可以识别出三个主要阶段：设备识别（device identification）、交互资源识别（interaction resources identification）以及适配（adaptation）。

*设备识别* 可以在服务端（server-side）或客户端（client-side）执行。在服务端的情况下，通常会执行 HTTP 协议中的用户代理检测（user agent detection）。它通常指示：([系统和浏览器信息]) [平台] ([平台详情]) [扩展]，例如：Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405。在客户端的情况下，可以通过标记语言（markup）在一定程度上识别当前设备的主要特征（例如，srcset 属性能够根据设备的主要特征指示使用哪个版本的图像）；或者通过使用样式表（stylesheets），利用媒体查询（media queries）将样式表与不同设备相关联；或者通过使用特定的脚本（scripts）（例如，jQueryMobile 为此提供了支持）。

*交互资源识别* 适用于需要获取当前可用交互资源的更详细信息的情况。此时，环境应通过设备描述仓库（Device Description Repository, DDRs）来访问这些资源。DDRs 的一种格式是 UAProf（User Agent Profile，用户代理配置文件），它描述了移动手持设备的各项能力，包括屏幕尺寸。

以及多媒体能力。移动设备在 HTTP 请求中发送一个标头（通常为 "x-wap-profile"），其中包含指向其用户代理配置文件（User Agent Profile, UAProf）的 URL。为设备制作该配置文件是自愿的。它基于 World Wide Web Consortium (W3C) 制定的复合能力/偏好配置文件规范（Composite Capability/Preference Profiles Specification, CC/PP）。设备描述资源（Device Description Resources, DDRs）的另一种格式是 WURFL，它是一个可以本地存储的 XML 配置文件，包含了各种移动设备的能力和特性信息。这些信息源自不同的渠道：可用的 UAProf、公开文档、开发者报告以及实际测试。它具有分层且可扩展的结构。它最初是一个开源项目 [http://wurfl.sourceforge.net/](http://wurfl.sourceforge.net/)，现在由 WURFL 团队创立的 ScientiaMobile 为这些 API 提供商业支持，同时也提供云服务。该领域的其他商业工具还包括 Device Atlas ([http://deviceatlas.com](http://deviceatlas.com/)) 和 DetectRight ([http://www.detectright.com](http://www.detectright.com/))。

通常，设备属性可分为静态属性（Static properties）和动态属性（Dynamic properties）。静态属性在应用程序执行期间无法更改，例如操作系统、RAM 大小、可用存储空间、显示尺寸、输入设备、标记语言支持、CSS 支持、图像格式支持、脚本支持等；动态属性则包括设备倾斜、当前使用的网络技术、...

连接、电池电量、位置、方向、加速度、光线、噪声等。媒体查询（Media Queries）能够检测一组有限的媒体特性（Media Features）：宽度、高度、设备宽度、设备高度、方向、宽高比、设备宽高比、[颜色](https://www.interaction-design.org/literature/topics/color)、颜色索引、单色、分辨率。

第三阶段是*适配（Adaptation）*。自动重构（Automatic Re-authoring）可以有多种实现方法：
- *缩放（Scaling）*：仅根据可用设备的交互资源进行线性缩放，例如 iPhone 上的 Safari 在加载为桌面系统开发的网页时所采取的方式；
- *转换（Transducing）*：保留初始结构并将元素转换为其他格式，同时压缩并转换图像以匹配设备特性；
- *变换（Transforming）*：进一步修改最初为桌面系统设计的内容和结构，使其更适合在小屏幕上显示。

要解决将桌面版本自动适配为能够改变用户界面结构（User Interface Structure）的移动版本的问题，可以首先计算各种元素所需的屏幕空间成本：即文本所需的垂直和水平空间、图像尺寸、行间距值、交互组件类型等。接下来，在计算目标设备中用户界面所需的空间时，还应考虑允许多少滚动容差，以及多少额外的

应当为表格及类似内容预留空间。如果结果高于目标设备的可持续成本（sustainable cost），则应考虑对用户界面元素进行适配（adaptation）（例如，使用较小的图像，或将交互元素替换为占用空间更少的等效元素）。如果最终的整体成本对于目标设备屏幕而言仍然过高，则应考虑将用户界面拆分为多个呈现形式（presentations）。为了决定如何进行拆分，可以将用户界面视为一组元素组（groups of elements），且这些组内部不可进一步拆分。因此，决策的核心在于如何分布这些组，以获得目标设备能够承载的呈现形式。拆分可以通过创建独立的移动端呈现形式，或通过动态地（dynamically）显示相关元素来实现。这一适配过程可以根据特定的参数和规则进行定制，例如目标设备允许的滚动程度，或在目标设备中分布元素组时应遵循的策略。在此适配过程中，表格有时是关键元素，因为当它们在小屏幕设备上显示时，往往占用空间过大。针对此类问题，已有学者提出了一些技术，例如 Tajima and Ohnishi (2008) 引入了动态脚本，允许部分列和/或行被折叠（collapsed）。

……以交互方式进行，从而使用户能够更好地关联表格中感兴趣的元素。

另一种有趣的适配技术（Adaptation Technique）是页面摘要（Page Summarization），其目的是自动减少内容，使其更适合小屏幕。针对这一问题有两种处理方法：基于抽象的方法（Abstraction-based approach）采用句子操纵（Sentence Manipulation）技术，如削减（Reduction）、压缩（Compression）和重构（Reformulation）；基于提取的方法（Extraction-based approach）则通过为句子评分，以筛选出能更好地代表全文的句子，该方法可以是基于特征的（例如词频 Term Frequency、句子位置、属性等），也可以利用 [机器学习（Machine Learning）](https://www.interaction-design.org/literature/topics/ai) 或基于图（Graph-based）的技术。页面摘要的一个示例是 PowerBrowser 所支持的功能。

(Buyukkokten et al., 2002)。其基本思想是，关键词（keyword）的重要性取决于它在单篇文本以及更大规模语料库（collection）中出现的频率。如果一个词在给定文本中出现频率较高，但在更大规模的语料库中出现频率较低，则该词被认为是最重要的。句子的显著性因子（significance factor）是通过对其组成词进行分析而得出的。如果一个句子中包含数量最多且分布最紧凑的高频独立词（distinct words），那么该句子很可能是重要的。对此类技术感兴趣的人可以使用 MEAD，这是一个公开的多文档摘要系统（multi-document summarization system），在该领域提供了更灵活的支持（参见 [http://www.summarization.com/mead/](http://www.summarization.com/mead/)）。

众包（Crowd-sourcing）技术基于通过公开征集来分配某些执行任务的想法。这些技术正变得日益重要，并且同样可以应用于适配（adaptation）。例如，Nebeling 和 Norrie 已将这些技术应用于网页的适配。其目标是支持开发人员定义能够适配各种设备及其日益增加的多样性的 Web 界面（Web interfaces）。为此，他们引入了一种工具来增强 Web 页面，允许用户针对特定设备自定义 Web 页面的布局（layout）。设备根据窗口大小（window size）、屏幕分辨率（screen resolution）和方向（orientation）进行分类。这样就可以共享适配方案，以便其他具有相同

设备以及具有相似偏好的用户可以直接从中受益。同一个研究团队 (Nebeling et al, 2013) 开发了一个名为 W3Touch 的工具，其目的是根据各项指标（metrics）支持触控适配（adaptation for touch）。该工具生成用户交互分析（analytics of the user interaction），以帮助设计者检测并定位移动触控设备的潜在设计问题。为此，该工具考虑了两个指标：链接误触率（Missed links ratio），用于追踪触控错过预期目标的频率；以及缩放级别（Zoom level），用于考量用户在访问 Web 界面不同组件时平均需要缩放的程度。

另一个需要考虑的重要方面是如何评估适配。为此，Manca et al. (2013) 提出了一组相关的评估标准（criteria）：
- *用户对适配的感知度（User’s awareness of adaptation）*：用户在多大程度上能够意识到 UI 的变化是由适配引起的；
- *适配的恰当性（Appropriateness of adaptation）*：系统是否选择了良好/恰当的适配策略；
- *适配的过渡性（Transition of adaptation）*：适配过程在多大程度上允许用户意识到适配期间发生了什么；
- *适配的连续性（Continuity of adaptation）*：在适配之后，继续交互的便捷程度如何；
- *适配在降低交互复杂度方面的影响（Impact of adaptation in decreasing interaction complexity）*：系统的交互复杂度是否有所降低；
- *适配在提高用户满意度方面的影响（Impact of adaptation in increasing user satisfaction）*：适配在多大程度上提高了用户的满意度。

## 39.7 语音界面（Vocal Interfaces）

语音界面（Vocal Interfaces）在多种场景中发挥着重要作用：例如针对视障用户；当用户在移动中时；以及更广泛地，当视觉通道（Visual Channel）被占用时。可能的应用示例包括预订服务、航班信息、天气信息、电话簿和新闻。然而，语音交互应用具有特定的特征，使其与[图形用户界面（Graphical User Interfaces）](https://www.interaction-design.org/literature/topics/graphical-user-interfaces)有所不同。语音界面是线性的（Linear）且具有非持久性（Non-persistent），而图形界面则支持并发交互（Concurrent Interactions）且具有持久性（Persistent）。语音界面的优势在于，对于某些操作而言，它们可以更加快速且自然。

近年来，随着语音技术的提升，人们对语音界面的关注日益增加。该技术正变得更加鲁棒（Robust）且具有即时性（Immediate），无需长时间的训练，因此在消费市场中出现了各种应用，例如 Google 的语音搜索和地图导航，以及 iPhone 上的 Siri。这得益于一种实现方式：允许输入语音指令，将音频存储在本地，随后发送至服务器进行语音识别（Speech Recognition）。基于菜单的语音导航（Vocal Menu-based Navigation）必须经过精心设计：需要持续的反馈（Feedback）以检查应用状态，且应提供简短的提示（Prompts）和选项[列表（Lists）](https://www.interaction-design.org/literature/topics/lists)。

以减轻记忆负担，并且应当支持对特定事件（如无输入 [no-input]、无匹配 [no-match]、帮助 [help]）的管理。尽管图形页面的逻辑结构是一棵树，但其深度和宽度对于语音浏览（Vocal Browsing）来说过大。图 13 展示了一个图形用户界面（Graphical User Interface, GUI）的示例，并使用实线边框的多边形来表示主区域，使用虚线边框来表示其中的子区域，从而呈现其逻辑结构。

![](https://public-media.interaction-design.org/images/encyclopedia/user_interface_design_adaptation/user_interface_design_adaptation.018.jpg)
作者/版权持有者：W3C。版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因无法获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面中的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子节）。

**图 39.13**：图形用户界面的逻辑结构

图 14 左侧显示了一个根据算法（Paterno and Sisti, 2011）自动生成的相应语音菜单（Vocal Menu），其中语音菜单项的文本源自元素 ID（elements id）或区域内容（section contents）。图 14 右侧则是一个通过此类语音界面可实现的语音对话（Vocal Dialogue）示例。

![](https://public-media.interaction-design.org/images/encyclopedia/user_interface_design_adaptation/user_interface_design_adaptation.019.jpg)
作者/版权持有者：Paterno and Sisti。版权条款与许可：保留所有权利（All Rights Reserved）。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。
**图 39.14**：示例用户界面（User Interface）的语音版本

## 39.8 多模态用户界面（Multimodal User Interfaces）

多模态性（Multimodality）关注于确定各种交互模态（interaction modalities）最有效的组合方式。为此，Coutaz et al. (1995) 提出了一个简单的术语集，即 CARE 属性（CARE properties）：*互补性（complementarity）*，指界面的相关部分由一种模态部分支持，由另一种模态部分支持；*分配性（assignment）*，指界面的相关部分由一个指定的模态支持；*冗余性（redundancy）*，指界面的相关部分由两种模态共同支持；*等价性（equivalence）*，指界面的相关部分可由其中任何一种模态支持。在 Manca et al. (2013) 中，作者详细描述了如何利用这些属性来设计和开发多模态用户界面：它们可以应用于组合算子（composition operators）、交互元素（interaction elements）以及仅输出元素（output-only elements）。对于交互元素，可以将其进一步分解为三个部分：提示（prompt）、输入（input）和反馈（feedback），这三个部分可以与不同的 CARE 属性相关联。在这种方法中，等价性仅能应用于输入元素，因为只有在输入时，用户才能选择使用哪种方式进行输入；而冗余性可以应用于提示和反馈，但不能应用于输入，因为一旦通过某种模态完成了输入，再次通过另一种模态输入便没有意义。

图 15 展示了一个支持自适应多模态用户界面（adaptive multimodal user interfaces）的通用架构。

接口。系统中包含一个能够检测与用户、技术、环境及社会方面相关事件的上下文管理器（Context Manager）。随后，适配引擎（Adaptation Engine）接收用户界面（User Interface）的描述以及可能的适配规则。用户界面的描述可以通过设计时（Design Time）的创作环境（Authoring Environments）获取，或在运行时（Run-time）通过逆向工程工具（Reverse Engineering Tools）自动生成。当与任何适配规则相关的事件发生时，应执行相应的动作部分。为此，有三种可选方案：

- **交互模态（Interaction Modality）的完全变更**：应调用相应的适配器（Adapter）以完成向新模态的完整适配，随后生成新的用户界面；
- **对当前用户界面结构进行部分变更**：修改其逻辑描述，并生成新的实现；
- **对当前用户界面进行微调**：例如更改某些元素的某些属性；此类变更可以通过适配脚本（Adaptation Scripts）直接在实现层完成。

![](https://public-media.interaction-design.org/images/encyclopedia/user_interface_design_adaptation/user_interface_design_adaptation.020.jpg)
作者/版权持有者：HIIS Laboratory。版权条款与许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未经许可的情况下使用（as

（未能获得许可）。请参阅 [版权声明](https://www.interaction-design.org/about/terms-of-use) 页面中的“例外（Exceptions）”部分（以及“allRightsReserved-UsedWithoutPermission”子章节）。

**图 39.15**：多模态自适应（Multimodal Adaptation）的通用架构

现在在 Web 端实现多模态应用也已成为可能。最初的实现方案是由 X+V 提供的，这是一种整合了 HTML 和 VoiceXML 的语言。然而，目前的浏览器已不再支持该语言。

Manca et al. (2013) 提出了一种新颖的解决方案，通过扩展 HTML 和 CSS 来调用 Google 对语音部分的支撑（通过由特定 Javascripts 解析的 CSS 注释来实现）。桌面应用程序可以通过 Javascripts 利用 Chrome 扩展程序，根据这些 CSS 注释来访问 Google 的自动语音识别（ASR, Automatic Speech Recognition）和文本转语音（TTS, Text-to-Speech）API。这种实现方式在 Chrome 移动版中仍然无法实现。因此，移动应用程序需要创建 Web View 组件实例，以便能够加载 Web 页面并通过 Java 访问 ASR 和 TTS API。在针对这种上下文相关多模态自适应（Context-dependent Multimodal Adaptation）方案的初步实证测试中，结果令人鼓舞。用户反馈指出，用户希望能够控制模态分布（Modality Distribution），以支持个人偏好。结果还表明，模态的选择除了要考虑当前的运行上下文（Context of Use）外，还应考虑需要支持的任务，例如显示较长的...

查询结果本质上更适合以图形化方式呈现，因为语音模态（Vocal Modality）不具备持久性，当最后的结果以语音形式呈现时，用户可能已经忘记了最初的结果。另一个方面是，在单个 UI 元素（UI elements）的部分组件这一粒度（Granularity）上混合模态并不总是被认为是合适的；例如，对于一个必须通过图形化方式选中的单个文本字段（Text field），此时要求以语音方式输入数值被认为是没有意义的。

## 39.9 分布式用户界面（Distributed User Interfaces）

在考虑多设备环境（Multi-device environments）中的用户访问时，我们可以识别出多种可能性：
- 在不同时间通过不同设备访问应用程序（每次仅使用一台设备）；
- 分布式用户界面（Distributed User Interfaces）：应用程序逻辑接收来自多个设备的输入；
- 在交互设备之间移动对象（例如，通过“拾取并投放（Pick-and-drop）” (Rekimoto, 87)）；
- 迁移式用户界面（Migratory User Interfaces）：设备变更，且界面迁移时能够实现状态保存（State preservation）。

分布式 UI 和迁移式 UI 是两个独立的概念。事实上，可能存在既是分布式又能够迁移的 UI，但同时也存在仅为分布式（完全不迁移）的用户界面，或者是不分布在多个设备上的迁移式 UI。

多设备支持正出现在各种环境中。OS X Lion Resume (footnote 3) 提供了“Resume”功能，允许用户在离开应用程序及其用户界面后，从上次停止的地方继续操作。Chrome-to-phone (footnote 4) 允许用户将链接从 Chrome 桌面浏览器发送到 Android 设备上的 App。Chrome-to-mobile (footnote 5) 将页面从计算机的 Chrome 浏览器发送到在移动设备上运行的 Chrome 浏览器。Firefox (footnote 6) 在桌面端和移动端 Firefox 客户端之间同步书签、[标签页（Tabs）](https://www.interaction-design.org/literature/topics/tabs)和网页历史记录。

在研究层面，Myngle (Sohn et al., 2011) 提供了来自多个个人设备的统一 Web 历史记录，并允许用户根据高级类别对其历史记录进行过滤。

在具体考虑分布式用户界面（Distributed User Interfaces）时，需要注意的是，有三类关键信息需要指定 (Frosini et al., 2013)：*哪些*界面组件需要被分布；*是否*在这些组件上启用输入；以及*目标设备（Target device(s)）*，即应当接收这些分布组件的设备（可以通过设备类型、ID 或与设备相关的角色来标识）。

一般而言，分布可以通过不同的方式定义：
- 在交互式应用程序的描述中，通过初始应用程序规范进行定义（设计时 Design-time）；
- 通过交互式应用程序规范中指明的分布事件处理器来定义分布（设计时定义 + 运行时执行 Run-time execution）；
- 通过动态定制工具（Dynamic customization tools）实现的分布（完全在运行时），这允许用户获得在设计时未曾规划的分布方案。

Manca and Paterno (2013) 展示了一个通过动态定制工具实现分布的示例。该示例使用 CARE 属性在基于 MARIA 的描述中指定分布。当应用程序生成后，最终用户仍然可以通过一个交互式工具来定制其在各种设备上的分布，以便

以应对在设计阶段（Design Time）未预见的需求。图 16 展示了一个示例：起初，用户界面（User Interface, UI）完全分配给一个移动设备；随后，通过交互式定制工具（Interactive Customization Tool），部分元素被分配到大屏幕上，而其他元素则在两个设备之间冗余（Redundant）分布。

![](https://public-media.interaction-design.org/images/encyclopedia/user_interface_design_adaptation/user_interface_design_adaptation.021.jpg)

作者/版权持有者：Manca and Paterno。版权条款与许可：保留所有权利。经许可转载。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”章节。

**图 39.16**：动态用户界面分布（Dynamic User Interface Distribution）的示例

## 39.10 迁移式交互应用程序（Migratory Interactive Applications）

当前普适环境（Ubiquitous Environments）中主要的挫败感来源之一是，用户在每次更换设备时都需要重新启动应用程序。为了充分利用当前的技术能力，需要能够跨多种设备连续访问交互式服务。迁移式用户界面（Migratory User Interfaces）可以在不同设备之间（从“源设备（Source Devices）”到“目标设备（Target Devices）”）进行转移，从而允许用户继续执行其任务。研究人员已经探索了多种实现方法（如像素复制（Pixel Replication）、交互式应用程序、虚拟机等）。购物、在线拍卖、游戏、预订等多个应用领域可以从中受益。其特点是能够保存交互部分的状态（State of the interactive part），其中可能包括用户输入、焦点元素（Focus Elements）、Cookie、会话（Sessions）、历史书签等。

支持迁移式用户界面的一种解决方案示例是 DeepShot (Chang and Li, 2011)。它通过摄像头识别用户正在查看的应用程序，恢复其状态，并将其迁移到手机上，状态信息被编码为统一资源标识符（Uniform Resource Identifier, URI）。相关视频可见于

EU OPEN 项目 (http://saturno.isti.cnr.it:88/) 研究了多种交互式应用程序迁移的解决方案，并已应用于各种场景（游戏、应急、社交网络）。其详细

相关描述见于一本关于普适环境（Ubiquitous Environments）中迁移式交互应用（Migratory Interactive Applications）的书籍 ([http://www.springer.com/computer/information+systems+and+applications/book/978-0-85729-249-0](http://www.springer.com/computer/information+systems+and+applications/book/978-0-85729-249-0))。

其中一种解决方案专注于支持网页迁移的环境。这是通过一个能够注入脚本的代理服务器（Proxy server）实现的；当通过迁移客户端（Migration client）触发迁移时，该脚本能够发送页面的 DOM（文档对象模型）及其当前状态。迁移客户端是一个独立的 Web 应用程序，能够与迁移服务器（Migration server）及相关应用进行通信。在此类环境中，可用性（Usability）具有一些特定的特征。它们与连续性（Continuity）相关，例如所需的时间

……由源设备（source device）上的触发机制到目标设备（target device）上的用户界面呈现的迁移过程。这种转换应当对用户而言是可理解的，也就是说，用户应当能够意识到迁移正在发生。适配结果（adaptation result）不应增加用户理解后续操作步骤的难度。另一个重要方面是可预测性（predictability）：用户应当能够预测目标设备、哪些 UI 部分将被迁移，以及迁移后用户交互的结果将出现在何处。

为了提高迁移环境的灵活性，我们可以引入部分迁移（partial migration）的可能性，即用户可以通过交互方式选择想要迁移到目标设备的部分。例如，在从桌面端到移动端的迁移中，如果用户希望限制迁移的部分以避免目标设备有限的屏幕空间过载，这种方式将非常有用。Web 应用程序迁移的一个问题是 JavaScript 的状态（state）。事实上，如果与 JavaScript 变量相关的状态没有被正确地保存和恢复，可能会出现不一致的情况：某些变量在上传的新版本中不再存在，或者某些变量可能持有错误的值。

无论如何，迁移界面（migratory interfaces）在多用户环境下也能提供有用的支持。在 Ghiani et al. (2012) 中，讨论了一个有趣的场景，即计划出差的同事们在其中利用了……

以便推送或拉取包含其旅途有用信息和数据的网页。展示该场景的视频可见于 [http://www.youtube.com/watch?feature=player_embedded&v=0cOlm28n_YE](http://www.youtube.com/watch?feature=player_embedded&v=0cOlm28n_YE)。

这种类型的环境可能会引发一系列隐私问题（Privacy issues），需要通过赋予用户控制权来解决，包括：每个设备是否对他人可见、在设备上浏览的页面是否可被他人检测到，以及设备是否可以作为迁移（Migration）的目标。这些权限可以仅分配给特定的用户或用户组。

在安全性（Security）方面可能会产生进一步的问题，包括从迁移后的用户界面（Migrated UIs）中窃取私密信息，例如用户输入的数据（信用卡、密码等）、页面中包含的数据（银行概况等），或存储在表单、会话（Sessions）和 Cookie 中的信息。其他风险可能源于通过身份验证攻击（Authentication attack）来冒充用户。其中一些问题可以通过自动分析交互式表单（Interactive forms）中的元素来解决，以识别其是否包含机密数据（Confidential data）；在这种情况下，即使原始应用程序中未使用安全协议（Secure protocols），也可以在迁移过程中使用安全协议来处理其内容。

## 39.11 结论

综上所述，为了更好地利用多设备环境（multi-device environments），人们已经开发了多种解决方案。建立一套逻辑维度（logical dimensions）以便设计者和开发人员对这些方案进行比较将是非常有用的。Paterno and Santoro (2012) 提供了一组此类维度及其用于区分方案的具体取值，具体如下：

- *分布（Distribution）*：是静态的还是动态的；
- *迁移（Migration）*：根据其能够保留的状态组件（state components）而定：如表单状态（form state）、功能状态（function state）、会话（sessions）、历史记录（history）、书签（bookmarks）等；
- *粒度（Granularity）*：方案是涉及整个用户界面（UI）、界面组、单个 UI 元素，还是 UI 元素的局部；
- *触发激活类型（Trigger Activation type）*：可以是按需（on demand）、自动（automatic）或混合（mixed）；
- *交互模态（Interaction modalities）*：方案是单模态（monomodal）、跨模态（transmodal）还是多模态（multimodal）；
- *激活的 UI 类型（Type of UIs activated）*：是预计算（precomputed）、运行时生成（generated at runtime）还是混合方案；
- *多用户间的设备共享（Device sharing between multiple users）*：共享是指在同一设备中移动元素，还是用户可以与同一设备进行交互；
- *时机（Timing）*：用户界面的更改是即时的（immediate）、延迟的（deferred）还是混合的；
- *适配方法（Adaptation Approach）*：是采用缩放（scaling）、传导（transducing）还是变换（transforming）方法；
- *架构（Architecture）*：架构方案是基于服务器（server-based）还是点对点（peer-to-peer）。

当然，我们距离解决所有具有挑战性的问题还很遥远。

这些特征定义了多设备环境（multi-device environments）。仍有多个方面值得进一步研究，例如为适配多种 Post-WIMP 交互技术提供集成支持，或者为在迁移过程中保持[功能（functionality）](https://www.interaction-design.org/literature/topics/functionality)状态提供更通用的解决方案。到目前为止，多设备到多设备的迁移以及群源适配（crowd-sourced adaptation）都较少受到关注。针对上下文相关应用的最终用户开发（End-User Development, EUD）环境需要更有效的隐喻（metaphors）和解决方案，且目前仍缺乏在分布式与迁移式用户界面（distributed and migratory user interfaces）中利用点对点通信（peer-to-peer communication）的通用解决方案。

## 39.12 References

[Arthur](https://www.interaction-design.org/references/authors/richard_arthur.html), Richard and [Jr.](https://www.interaction-design.org/references/authors/dan_r__olsen%2C_jr-dot-.html), Dan R. Olsen, (2011): *XICE windowing toolkit: Seamless display annexation*. In [ACM Transactions on Computer-Human Interaction](https://www.interaction-design.org/references/periodicals/acm_transactions_on_computer-human_interaction.html), 18 (3) p. 14
[Bellucci](https://www.interaction-design.org/references/authors/federico_bellucci.html), Federico, [Ghiani](https://www.interaction-design.org/references/authors/giuseppe_ghiani.html), Giuseppe, [Paterno](https://www.interaction-design.org/references/authors/fabio_paterno.html), Fabio and [Porta](https://www.interaction-design.org/references/authors/claudio_porta.html),
 Claudio (2012): Automatic reverse engineering of interactive dynamic 
web applications to support adaptation across platforms. In: [Proceedings of the 2012 International Conference on Intelligent User Interfaces](https://www.interaction-design.org/references/conferences/proceedings_of_the_2012_international_conference_on_intelligent_user_interfaces.html) 2012. pp. 217-226

[Buyukkokten](https://www.interaction-design.org/references/authors/orkut_buyukkokten.html), Orkut, [Kaljuvee](https://www.interaction-design.org/references/authors/oliver_kaljuvee.html), Oliver, [Garcia-Molina](https://www.interaction-design.org/references/authors/hector_garcia-molina.html), Hector, [Paepcke](https://www.interaction-design.org/references/authors/andreas_paepcke.html), Andreas and [Winograd](https://www.interaction-design.org/references/authors/terry_winograd.html), Terry (2002):*Efficient web browsing on handheld devices using page and form summarization*. In [ACM Transactions on Information Systems](https://www.interaction-design.org/references/periodicals/acm_transactions_on_information_systems.html), 20 (1) pp. 82-115
[Chang](https://www.interaction-design.org/references/authors/tsung-hsiang_chang.html), Tsung-Hsiang and [Li](https://www.interaction-design.org/references/authors/yang_li.html), Yang (2011): Deep shot: a framework for migrating tasks across devices using mobile phone cameras. In: [Proceedings of ACM CHI 2011 Conference on Human Factors in Computing Systems](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2011_conference_on_human_factors_in_computing_systems.html) 2011. pp. 2163-2172

[Frosini](https://www.interaction-design.org/references/authors/luca_frosini.html), Luca, [Manca](https://www.interaction-design.org/references/authors/marco_manca.html), Marco and [Paterno](https://www.interaction-design.org/references/authors/fabio_paterno.html), Fabio (2013): A Framework for the Development of Distributed Interactive Applications. In: [EICS 13 Proceedings of the 5th ACM SIGCHI symposium on Engineering interactive computing systems](https://www.interaction-design.org/references/conferences/eics_13_proceedings_of_the_5th_acm_sigchi_symposium_on_engineering_interactive_computing_systems.html) June 24-27, 2013, London, United Kingdom. pp. 249-254
[Gajos](https://www.interaction-design.org/references/authors/krzysztof_z__gajos.html), Krzysztof Z., [Weld](https://www.interaction-design.org/references/authors/daniel_s__weld.html), Daniel S. and [Wobbrock](https://www.interaction-design.org/references/authors/jacob_o__wobbrock.html), Jacob O. (2010): *Automatically generating personalized user interfaces with Supple*. In [Artificial Intelligence](https://www.interaction-design.org/references/periodicals/artificial_intelligence.html), 174 (12) pp. 910-950

[Gajos](https://www.interaction-design.org/references/authors/krzysztof_z__gajos.html), Krzysztof Z., [Hurst](https://www.interaction-design.org/references/authors/amy_hurst.html), Amy and [Findlater](https://www.interaction-design.org/references/authors/leah_findlater.html), Leah (2012): *Personalized dynamic accessibility*. In [Interactions](https://www.interaction-design.org/references/periodicals/interactions.html), 19 (2) pp. 69-73
[Ghiani](https://www.interaction-design.org/references/authors/giuseppe_ghiani.html), Giuseppe, [Paterno](https://www.interaction-design.org/references/authors/fabio_paterno.html), Fabio and [Santoro](https://www.interaction-design.org/references/authors/carmen_santoro.html), Carmen (2013): *Interactive customization of ubiquitous Web applications*. In [Journal of Visual Languages & Computing](https://www.interaction-design.org/references/periodicals/journal_of_visual_languages_%26_computing.html), 24 (1) pp. 37-52

[Ghiani](https://www.interaction-design.org/references/authors/giuseppe_ghiani.html), Giuseppe, [Paterno](https://www.interaction-design.org/references/authors/fabio_paterno.html), Fabio and [Santoro](https://www.interaction-design.org/references/authors/carmen_santoro.html), Carmen (2012): Push and pull of web user interfaces in multi-device environments. In: [Proceedings of the 2012 International Conference on Advanced Visual Interfaces](https://www.interaction-design.org/references/conferences/proceedings_of_the_2012_international_conference_on_advanced_visual_interfaces.html) 2012. pp. 10-17
[Ghiani](https://www.interaction-design.org/references/authors/giuseppe_ghiani.html), Giuseppe, [Paterno](https://www.interaction-design.org/references/authors/fabio_paterno.html), Fabio and [Isoni](https://www.interaction-design.org/references/authors/lorenzo_isoni.html), Lorenzo (2012): Security in migratory interactive web applications. In:[Proceedings of the 11th International Conference on Mobile and Ubiquitous Multimedia MUM](https://www.interaction-design.org/references/conferences/proceedings_of_the_11th_international_conference_on_mobile_and_ubiquitous_multimedia_mum.html) December 4-6, 2012, Ulm, Germany.

[John](https://www.interaction-design.org/references/authors/bonnie_e__john.html), Bonnie E. and [Kieras](https://www.interaction-design.org/references/authors/david_e__kieras.html), David E. (1996): *The GOMS Family of User Interface Analysis Techniques: Comparison and Contrast*. In [ACM Transactions on Computer-Human Interaction](https://www.interaction-design.org/references/periodicals/acm_transactions_on_computer-human_interaction.html), 3 (4) pp. 320-351
[Lin](https://www.interaction-design.org/references/authors/james_lin.html), James and [Landay](https://www.interaction-design.org/references/authors/james_a__landay.html), James A. (2008): Employing patterns and layers for early-stage design and [prototyping](https://www.interaction-design.org/literature/topics/prototyping) of cross-device user interfaces. In: [Proceedings of ACM CHI 2008 Conference on Human Factors in Computing Systems](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2008_conference_on_human_factors_in_computing_systems.html) April 5-10, 2008. pp. 1313-1322

[Manca](https://www.interaction-design.org/references/authors/marco_manca.html), Marco and [Paterno](https://www.interaction-design.org/references/authors/fabio_paterno.html), Fabio (2011): Flexible support for distributing user interfaces across multiple devices. In:[Proceedings of CHI 2011 Conference on Human Factors in Computing](https://www.interaction-design.org/references/conferences/proceedings_of_chi_2011_conference_on_human_factors_in_computing.html) May 7-12, 2011, Vancouver, Canada. pp. 191-195
[Manca](https://www.interaction-design.org/references/authors/marco_manca.html), Marco, [Paterno](https://www.interaction-design.org/references/authors/fabio_paterno.html), Fabio, [Santoro](https://www.interaction-design.org/references/authors/carmen_santoro.html), Carmen and [Spano](https://www.interaction-design.org/references/authors/lucio_d__spano.html), Lucio D. (2013): Generation of Multi-Device Adaptive MultiModal Web Applications. In: [Proceedings of 10th International Conference on Mobile Web Information Systems MobiWIS 2013](https://www.interaction-design.org/references/conferences/proceedings_of_10th_international_conference_on_mobile_web_information_systems_mobiwis_2013.html) August 26-29, 2013, Paphos, Cyprus. pp. 218-232

[MiÃ±Ã³n](https://www.interaction-design.org/references/authors/ra%C3%BAl_mi%C3%B1%C3%B3n.html), RaÃºl, [PaternÃ²](https://www.interaction-design.org/references/authors/fabio_patern%C3%B2.html), Fabio and [Arrue](https://www.interaction-design.org/references/authors/myriam_arrue.html), Myriam (2013): An environment for designing and sharing adaptation rules for accessible applications. In: [Proceedings of the 5th ACM SIGCHI Symposium on Engineering Interactive Computing Systems EICS 2013](https://www.interaction-design.org/references/conferences/proceedings_of_the_5th_acm_sigchi_symposium_on_engineering_interactive_computing_systems_eics_2013.html) June 24-27, 2013, London, United Kingdom. pp. 43-48
[Nebeling](https://www.interaction-design.org/references/authors/michael_nebeling.html), Michael, [Speicher](https://www.interaction-design.org/references/authors/maximilian_speicher.html), Maximilian and [Norrie](https://www.interaction-design.org/references/authors/moira_c__norrie.html), Moira C. (2013): CrowdAdapt: Enabling Crowdsourced Web Page Adaptation for Individual Viewing Conditions and Preferences. In: [Proceedings of the 5th ACM SIGCHI Symposium on Engineering Interactive Computing Systems EICS 2013](https://www.interaction-design.org/references/conferences/proceedings_of_the_5th_acm_sigchi_symposium_on_engineering_interactive_computing_systems_eics_2013.html) June 24-27, 2013, London, United Kingdom.

[Nebeling](https://www.interaction-design.org/references/authors/michael_nebeling.html), Michael, [Speicher](https://www.interaction-design.org/references/authors/maximilian_speicher.html), Maximilian and [Norrie](https://www.interaction-design.org/references/authors/moira_c__norrie.html), Moira C. (2013): W3touch: metrics-based web page adaptation for touch. In: [Proceedings of CHI 2013 Conference on Human Factors in Computing](https://www.interaction-design.org/references/conferences/proceedings_of_chi_2013_conference_on_human_factors_in_computing.html) April 27-May 2, 2013, Paris, France. pp. 2311-2320

[Nigay](https://www.interaction-design.org/references/authors/laurence_nigay.html), Laurence, [Coutaz](https://www.interaction-design.org/references/authors/jo%EBlle_coutaz.html), Joëlle, [Salber](https://www.interaction-design.org/references/authors/daniel_salber.html), Daniel, [Blandford](https://www.interaction-design.org/references/authors/ann_blandford.html), Ann, [May](https://www.interaction-design.org/references/authors/jon_may.html), Jon and [Young](https://www.interaction-design.org/references/authors/richard_m__young.html), Richard M. (1995): Four Easy Pieces for Assessing the Usability of Multimodal Interaction: the CARE Properties. In: [Nordby](https://www.interaction-design.org/references/authors/knut_nordby.html), Knut (ed.)[Proceedings of INTERACT 95 - IFIP TC13 Fifth International Conference on Human-Computer Interaction](https://www.interaction-design.org/references/conferences/proceedings_of_interact_95_-_ifip_tc13_fifth_international_conference_on_human-computer_interaction.html) June 25-29, 1995, Lillehammer, Norway. pp. 115-120
[Paterno](https://www.interaction-design.org/references/authors/fabio_paterno.html), Fabio (1999): *Model-Based Design and Evaluation of Interactive Application.* London, United Kingdom,

[Paterno](https://www.interaction-design.org/references/authors/fabio_paterno.html), Fabio and [Santoro](https://www.interaction-design.org/references/authors/carmen_santoro.html), Carmen (2012): A logical framework for multi-device user interfaces. In: [ACM SIGCHI 2012 Symposium on Engineering Interactive Computing Systems](https://www.interaction-design.org/references/conferences/acm_sigchi_2012_symposium_on_engineering_interactive_computing_systems.html) 2012. pp. 45-50
[Paterno](https://www.interaction-design.org/references/authors/fabio_paterno.html), Fabio, [Santoro](https://www.interaction-design.org/references/authors/carmen_santoro.html), Carmen and [Spano](https://www.interaction-design.org/references/authors/lucio_davide_spano.html), Lucio Davide (2009): *MARIA:
 A universal, declarative, multiple abstraction-level language for 
service-oriented applications in ubiquitous environments*. In [ACM Transactions on Computer-Human Interaction](https://www.interaction-design.org/references/periodicals/acm_transactions_on_computer-human_interaction.html), 16 (4) p. 19
[Patern](https://www.interaction-design.org/references/authors/fabio_patern%C3%B2.html)o, Fabio (2013): [*End User Development*](https://www.interaction-design.org/literature/topics/end-user-development)*: Survey of an Emerging Field for Empowering People*. In [ISRN Software Engineering](https://www.interaction-design.org/references/periodicals/isrn_software_engineering.html), p. 11

[Patern](https://www.interaction-design.org/references/authors/fabio_patern%C3%B2.html)o, Fabio and [Sisti](https://www.interaction-design.org/references/authors/christian_sisti.html), Christian (2011): Model-based customizable adaptation of web applications for vocal browsing. In: [Proceedings of the 29th ACM international conference on Design of communication SIGDOC 11](https://www.interaction-design.org/references/conferences/proceedings_of_the_29th_acm_international_conference_on_design_of_communication_sigdoc_11.html)October 3-5, 2011, Pisa,Italy. pp. 83-90
[Rekimoto](https://www.interaction-design.org/references/authors/jun_rekimoto.html), Jun (1997): Pick-and-Drop: A Direct Manipulation Technique for Multiple Computer Environments. In:[Robertson](https://www.interaction-design.org/references/authors/george_g__robertson.html), George G. and [Schmandt](https://www.interaction-design.org/references/authors/chris_schmandt.html), Chris (eds.) [Proceedings of the 10th annual ACM symposium on User interface software and technology](https://www.interaction-design.org/references/conferences/proceedings_of_the_10th_annual_acm_symposium_on_user_interface_software_and_technology.html) October 14 - 17, 1997, Banff, Alberta, Canada. pp. 31-39

[Sohn](https://www.interaction-design.org/references/authors/timothy_sohn.html), Timothy, [Li](https://www.interaction-design.org/references/authors/frank_chun_yat_li.html), Frank Chun Yat, [Battestini](https://www.interaction-design.org/references/authors/agathe_battestini.html), Agathe, [Setlur](https://www.interaction-design.org/references/authors/vidya_setlur.html), Vidya, [Mori](https://www.interaction-design.org/references/authors/koichi_mori.html), Koichi and [Horii](https://www.interaction-design.org/references/authors/hiroshi_horii.html), Hiroshi (2011): Myngle: unifying and filtering web content for unplanned access between multiple personal devices. In: [Proceedings of the 2011 International Conference on Uniquitous Computing](https://www.interaction-design.org/references/conferences/proceedings_of_the_2011_international_conference_on_uniquitous_computing.html) 2011. pp. 257-266

[Tajima](https://www.interaction-design.org/references/authors/keishi_tajima.html), Keishi and [Ohnishi](https://www.interaction-design.org/references/authors/kaori_ohnishi.html), Kaori (2008): Browsing large HTML tables on small screens. In: [Cousins](https://www.interaction-design.org/references/authors/steve_b__cousins.html), Steve B. and[Beaudouin-Lafon](https://www.interaction-design.org/references/authors/michel_beaudouin-lafon.html), Michel (eds.) [Proceedings of the 21st Annual ACM Symposium on User Interface Software and Technology](https://www.interaction-design.org/references/conferences/proceedings_of_the_21st_annual_acm_symposium_on_user_interface_software_and_technology.html) October 19-22, 2008, Monterey, CA, USA. pp. 259-268

[Wäljas](https://www.interaction-design.org/references/authors/minna_w%E4ljas.html), Minna, [Segerståhl](https://www.interaction-design.org/references/authors/katarina_segerst%E5hl.html), Katarina, [Väänänen-Vainio-Mattila](https://www.interaction-design.org/references/authors/kaisa_v%E4%E4n%E4nen-vainio-mattila.html), Kaisa and [Oinas-Kukkonen](https://www.interaction-design.org/references/authors/harri_oinas-kukkonen.html), Harri (2010): Cross-platform service user experience: a field study and an initial framework. In: [Proceedings of 12th Conference on Human-computer interaction with mobile devices and services](https://www.interaction-design.org/references/conferences/proceedings_of_12th_conference_on_human-computer_interaction_with_mobile_devices_and_services.html) 2010. pp. 219-228
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

加入 **314,322 位设计师** 的行列，通过我们的时事通讯获取实用的 UX 技巧。
需要提供有效的电子邮件地址。

## 本书章节涵盖的主题：

[适应性设计（Adaptive Design）](https://www.interaction-design.org/literature/topics/adaptive-design)
[用户体验（User Experience, UX）设计](https://www.interaction-design.org/literature/topics/ux-design)
[移动端用户体验（Mobile UX）设计](https://www.interaction-design.org/literature/topics/mobile-ux-design)
[用户界面（User Interface, UI）设计](https://www.interaction-design.org/literature/topics/ui-design)
[人机交互（Human-Computer Interaction, HCI）](https://www.interaction-design.org/literature/topics/human-computer-interaction)
