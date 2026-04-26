# 32. 三维用户界面 (3D User Interfaces)

**来源**：The Encyclopedia of Human-Computer Interaction, 2nd Ed.
**Notion 原页面**：https://www.notion.so/be2ba0263ae7404183fede7ce0e9d876

---

[Doug A. Bowman](https://www.interaction-design.org/literature/author/doug-a-bowman)
自从计算机鼠标以及基于窗口、图标、菜单和指针（Windows, Icons, Menus, and Pointer, WIMP）范式的图形用户界面（Graphical User Interface, GUI）出现以来，人们一直在探讨用户界面的下一个范式转移（Paradigm Shift）将是什么（van Dam, 1997; Rekimoto, 1998）。基于鼠标的 GUI 已证明具有极高的灵活性、鲁棒性（Robust）和通用性，但我们终于看到向“自然”用户界面（Natural User Interfaces, NUIs）的重大转变，这不仅体现在研究实验室中，也体现在面向广大消费者的商业产品中。在 NUI 的范畴下，界面可分为两大类：一类是基于直接触摸（Direct Touch）的界面，如多点触控平板电脑（Wigdor & Wixon, 2011）；另一类是基于三维空间输入（Three-dimensional Spatial Input）的界面（Bowman et al., 2005），如基于动作的游戏。本章将重点讨论后一类界面，即我们所称的三维用户界面（3D UIs）。

## 32.1 什么是三维用户界面？

就像我们领域中的许多高层描述性术语（high-level descriptive terms）（例如“[虚拟现实（Virtual Reality）](https://www.interaction-design.org/literature/topics/virtual-reality)”和“多媒体（Multimedia）”）一样，给“三维用户界面（3D User Interface, 3D UI）”这个词下一个精确的定义出人意料地困难。尽管大多数从业者和研究人员会说“我一看就知道它是不是”，但要准确阐明三维用户界面的构成，以及哪些界面应被包含在内、哪些应被排除在外，是非常棘手的。

[*3D User Interfaces: Theory and Practice*](https://www.interaction-design.org/literature/topics/3d-user-interfaces) (Bowman et al., 2005) 将三维用户界面简单地定义为“涉及三维交互（3D interaction）的 UI”。这只是推迟了不可避免的问题，因为我们现在必须定义什么是三维交互。该书指出，三维交互是指“用户在三维空间上下文（3D spatial context）中直接执行任务的人机交互（Human-Computer Interaction, HCI）”。

该定义中的一个关键词是“直接地（directly）”。一些交互式计算机系统虽然显示虚拟三维空间（virtual 3D space），但用户仅与该空间进行间接交互——例如，通过操作二维控件（2D widgets）、输入坐标或从菜单中选择项目。这些并不属于三维用户界面。

另一个核心概念是“三维空间上下文”。该书进一步明确，这种空间上下文可以是物理的、虚拟的，或者两者兼有。最主要的三维用户界面类型涉及物理三维空间

……（的）语境，用于输入。用户通过在物理三维空间（physical 3D space）中进行移动，或操作三维空间中的工具、传感器或设备来向系统提供输入，而无需关注该输入被用于执行或控制什么。当然，从某种意义上说，所有的输入/交互都处于物理三维空间语境中（例如鼠标和键盘就存在于三维物理空间中），但此处旨在强调，用户提供的是涉及三维位置（3D position, x, y, z）和/或朝向（Orientation, yaw, pitch, roll）的空间输入（Spatial Input），且这种空间输入对系统具有语义意义。

因此，此类三维用户界面（3D UIs）的关键技术支撑是空间追踪（Spatial Tracking）（Meyer et al., 1992; Welch & Foxlin, 2002）。系统必须能够追踪用户的位置、朝向和/或运动，才能使该输入用于三维交互。例如，Microsoft Kinect 通过追踪多个身体部位的三维位置来实现 3D UI，而 Apple iPhone 则通过追踪自身的三维朝向来允许三维交互。空间追踪采用了许多不同的技术，我们将在后续章节中详细介绍。

这种被追踪的空间输入可用于具象手势（Iconic Gestures）、直接指向（Direct Pointing）菜单项、控制游戏中的角色、指定三维形状以及许多其他用途。基于空间输入的 3D UI 可以应用于各种……

应用场景：游戏系统、建模应用、虚拟与[增强现实](https://www.interaction-design.org/literature/topics/augmented-reality)（Augmented Reality, AR）系统、大屏可视化装置以及艺术装置，仅举几例。

另一种[类型](https://www.interaction-design.org/literature/topics/type)的 3D 用户界面（3D UI）涉及在虚拟 3D 空间语境下的[直接交互](https://www.interaction-design.org/literature/topics/direct-interaction)（Direct Interaction）。在这种类型中，用户可能会使用传统的（非 3D）输入设备或动作作为输入，但如果这些输入被直接转化为虚拟 3D 空间中的动作，我们仍然将其视为 3D 交互（3D Interaction）。例如，用户可能会在 3D 模型上拖动鼠标以将其涂成某种[颜色](https://www.interaction-design.org/literature/topics/color)，或者用户可能会使用触摸输入在 3D 世界中绘制一条路径。

在本节中，我们将重点讨论第一类 3D UI，即基于 3D 空间输入（3D Spatial Input）的界面。虽然这两类界面都很重要且有广泛的应用，但在很大程度上，它们涉及的研究问题和技术截然不同。3D 空间追踪（3D Spatial Tracking）技术在近期已趋于成熟，在这一技术驱动力的推动下，具有空间输入的 3D UI 应用呈现出爆发式增长。我们将在下一节中更详细地讨论其中一些应用。

## 32.2 3D UI 的应用

为什么理解和研究 3D 用户界面（3D User Interfaces, 3D UIs）至关重要？多年来，3D UI 的主要应用集中在高端虚拟现实（Virtual Reality, VR）和增强现实（Augmented Reality, AR）系统中。由于这些系统的用户通常处于站立或走动状态，且其对真实世界的视野受限，传统的基于鼠标和键盘的交互方式并不实用。这些系统已经采用了对用户头部的空间追踪（Spatial Tracking）以确保虚拟世界的视角正确，因此，设计同样利用空间追踪的 UI 也就顺理成章。然而，正如我们此前所述，近年来空间输入（Spatial Input）在游戏机和智能手机等消费级系统中呈现爆发式增长。因此，现在理解优秀的 3D UI 设计原则比以往任何时候都更加重要。

为了进一步阐明 3D UI 研究的重要性，让我们详细探讨一些 3D UI 正在对实际应用产生影响的重要技术领域。

### 32.2.1 视频游戏（Video Gaming）

正如我们之前提到的，如今大多数人之所以了解 3D 用户界面（3D User Interfaces），是因为像 Nintendo Wii、Microsoft Kinect 和 Sony Move 这样“体感游戏（motion gaming）”系统的巨大成功。所有这些系统都使用空间追踪（spatial tracking）技术，允许用户通过指向（pointing）、手势（gestures）以及最关键的自然动作（natural movements），而非通过按钮和摇杆与游戏进行交互。例如，在射箭游戏中，用户可以持有两个被追踪的设备——一个代表弓柄，另一个代表箭和弓弦——并使用与现实世界射箭非常相似的动作来拉箭、瞄准和释放。

Wii 和 Move 都使用带有按钮和摇杆的追踪手持设备，而 Kinect 则直接追踪用户的身体。这里存在一个明显的权衡（tradeoff）：按钮和摇杆对于离散操作（discrete actions）仍然很有用，例如确认选择、开火或切换视角；而另一方面，消除用户的束缚（encumbrances）可以使体验显得更加自然。

3D 用户界面非常适合视频游戏 (LaViola, 2008; Wingrave et al., 2010)，因为其[重点](https://www.interaction-design.org/literature/topics/emphasis)在于创造一种极具吸引力的体验（compelling experience），而这种体验可以通过自然动作来增强，使玩家感觉自己仿佛是行动的一部分，而不仅仅是在间接控制一个远程角色的行为。

### 32.2.2 超大型显示器（Very Large Displays）

近年来，显示器的尺寸、分辨率和普及程度呈爆炸式增长。所谓的“显示墙（Display Walls）”出现在购物中心、会议室，甚至人们的家中。其中许多显示器是被动的，仅向观众呈现预设信息（Canned information），但越来越多的显示器具备了交互能力。

那么，人们应该如何与这些大型显示器进行交互呢？传统的鼠标和键盘仍然适用，但在这种场景下难以使用，因为用户希望在显示器前走动，且此类大型显示器通常支持多用户共同使用 (Ball and North, 2005)。触摸屏是另一种选择，但这意味着用户必须站在手臂可及的范围内才能与显示器交互，从而限制了可见的显示区域。

3D 交互（3D Interaction）是大型显示场景下的自然选择。追踪式手持设备（Tracked handheld device）、手部本身或全身都可以作为便携式输入方式，它们可以在任何位置工作，且适用于多用户场景。最简单的例子是*远距离指向（Distal pointing）*，即用户直接指向显示器上的某个位置（类似于使用激光笔）来进行交互 (Vogel & Balakrishnan, 2005; Kopper et al., 2010)，此外还可以使用全身手势（Full-body gestures）或视点依赖型显示（Viewpoint-dependent display）等其他技术。

### 32.2.3 移动应用程序（Mobile Applications）

如今的移动设备（如智能手机和平板电脑）是交互设计师的乐园，这不仅是因为多点触控输入（multi-touch input）提供了丰富的设计空间，还因为这些设备内置了一些相当强大的 3D 空间输入（3D spatial input）传感器。加速度计（accelerometers）、陀螺仪（gyroscopes）和电子罗盘（compass）的结合，使这些设备能够相当准确地追踪自身的姿态（orientation）。基于 [GPS](https://www.interaction-design.org/literature/topics/gps) 和加速度计的位置信息虽然准确度较低，但依然可用。然而，这些设备为 3D [交互设计](https://www.interaction-design.org/literature/topics/interaction-design)（interaction design）提供了关键机遇，因为它们具有普及性（ubiquitous），拥有独立的显示屏，且无需任何外部追踪基础设施（external tracking infrastructure，如摄像头、基站等）即可实现空间输入。

许多移动游戏正在利用这些功能。例如，赛车游戏使用了“倾斜转向”（tilt to steer）的隐喻（metaphor）。音乐游戏可以感知用户何时在敲击虚拟鼓。而高尔夫游戏则可以将玩家真实的挥杆动作融入其中。

但“严肃”应用（"serious" applications）同样可以利用移动设备的 3D 输入。每个人都熟悉通过倾斜设备将界面从纵向（portrait）切换到横向（landscape）模式，但这仅仅是冰山一角。一个为业余天文学家设计的工具可以使用

GPS 和方向信息（orientation information）可帮助用户识别设备所指向的恒星和行星。相机应用程序不仅可以记录照片拍摄的位置，还可以追踪相机的移动，以辅助 3D 场景的重建（reconstruction of a 3D scene）。

移动设备 3D 交互最显著的例子或许在于移动增强现实（mobile AR）。在移动 AR 中，智能手机成为了一个窗口，用户不仅可以通过它看到现实世界，还能看到虚拟对象和信息 (Höllerer et al., 1999; Ashley, 2008)。因此，用户只需移动设备以查看现实世界场景的不同部分，即可浏览信息。移动 AR 正被应用于娱乐、[导航（navigation）](https://www.interaction-design.org/literature/topics/navigation-1)、社交网络、旅游以及更多领域。例如，学生可以学习某个地区的历史；朋友们可以寻找周围的餐厅并查看评论；游客则可以沿着虚拟路径前往最近的地铁站。诸如 MIT 的 SixthSense (Mistry & Maes, 2009) 和 Google 的 Project Glass (Google, 2012) 等知名项目，极大地提升了移动 AR 的可见度。而优秀的 3D 用户界面（3D UI）设计对于实现这些愿景至关重要。

## 32.3 3D 用户界面技术 (3D UI Technologies)

正如上文所述，空间追踪技术 (spatial tracking technologies) 与 3D 用户界面 (3D UI) 密切相关。因此，为了设计出具有可用性 (usable) 的 3D 用户界面，必须对空间追踪有基础的了解。此外，其他输入技术 (input technologies) 和显示设备 (display devices) 在 3D 用户界面设计中也起着至关重要的作用。

### 32.3.1 追踪系统与传感器（Tracking Systems and Sensors）

空间追踪系统（Spatial Tracking Systems）用于感知一个或多个对象的位置、朝向（Orientation）、线速度或角速度，以及/或线加速度或角加速度。传统上，3D 用户界面（3D UIs）基于六自由度（Six-Degree-of-Freedom, 6-DOF）位置追踪器，这些追踪器可检测对象的绝对 3D 位置（在固定 XYZ 坐标系中的位置）和朝向（在固定坐标系中的翻滚、俯仰和偏航 [Roll, Pitch, and Yaw]），该对象通常安装在头部或由手持。

这些 6-DOF 位置追踪器可基于多种不同的技术，例如使用电磁场（Electromagnetic Fields，如 Polhemus Liberty）、光学追踪（Optical Tracking，如 NaturalPoint OptiTrack）或超声波/惯性混合追踪（Hybrid Ultrasonic/Inertial Tracking，如 Intersense IS900）。然而，所有这些技术都有一个共同的局限性，即必须使用某种外部固定参考物，例如基站（Base Station）、摄像头阵列（Camera Array）、一组可见标记（Visible Markers）或发射器（Emitter）[网格](https://www.interaction-design.org/literature/topics/grid-systems)。因此，绝对 6-DOF 位置追踪通常只能在经过准备的空间中进行。

另一方面，惯性追踪系统（Inertial Tracking Systems）可以是自包含的，不需要外部参考。它们使用加速度计（Accelerometers）、陀螺仪（Gyros）、磁力计（Magnetometers，即指南针）或视频摄像头等技术来感知自身的运动——即位置或朝向的变化。由于它们测量的是相对位置和朝向，惯性系统无法告知其

...绝对位置，且测量误差往往随时间累积，从而产生漂移（drift）。

空间追踪（spatial tracking）的“圣杯”是一个独立的六自由度（6-DOF, Degrees of Freedom）系统，能够以极高的准确度（accuracy）和精密度（precision）追踪自身的绝对位置和朝向（orientation）。我们正逐步接近这一愿景。例如，智能手机可以使用其加速度计（accelerometers）、陀螺仪（gyros）和磁力计（magnetometer）来追踪其绝对朝向（相对于重力和地球磁场），并利用其 GPS 接收器来追踪其在地球表面的二维位置。然而，GPS 定位在最好的情况下误差也在几英尺之内，且目前无法准确追踪手机的高度（altitude）。因此，目前智能手机本身还不能被用作通用的六自由度输入设备。

一个安装要求极低的六自由度追踪器是 Sony Move 系统。Move 是为 PlayStation 游戏机设计的“动作控制器（motion controller）”（尽管它实际上感知的是位置），它使用典型的加速度计和陀螺仪来感知三维朝向，并使用单个摄像头来追踪设备顶部发光球的三维位置。这一方案的效果出奇地好，其准确度接近于昂贵且复杂的追踪系统，但确实存在局限性：用户必须面向摄像头，且不能遮挡摄像头对发光球的视线。此外，深度维度（depth dimension）的准确度低于水平和垂直维度。

对于独立式六自由度（6-DOF, 6 Degrees of Freedom）追踪而言，最理想的方案可能是由内而外的基于视觉的追踪（inside-out vision-based tracking）。在这种方案中，被追踪对象使用摄像头观察周围环境，并通过分析该视图随时间的变化来理解自身的运动（包括平移和旋转）。尽管这种方法本质上是相对的，但此类系统可以通过追踪场景中的“特征点（feature points）”，在与场景关联的固定坐标系中实现某种形式的绝对追踪（absolute tracking）。例如并行追踪与建图（PTAM, Parallel Tracking and Mapping）(Klein & Murray, 2007) 等算法，正使这一目标逐渐成为现实。

近期有三项追踪技术的发展值得特别提及，因为它们正吸引许多新的设计师和研究人员进入 3D 用户界面（3D UIs, 3D User Interfaces）领域。第一项是 Nintendo Wii Remote。这款游戏外设虽然不提供六自由度追踪，但除了一个可用于在屏幕上移动光标的简单光学追踪器外，还包含多个惯性传感器（inertial sensors）。Wingrave 及其同事 (Wingrave et al, 2010) 深入探讨了 Wii Remote 与传统追踪器的区别，以及它如何被应用于 3D UIs 中。

第二项是 Microsoft Kinect（图 1），它以一种截然不同的方式实现追踪。它并非追踪手持设备或用户头部的单个点，而是使用深度摄像头（depth camera）来追踪用户的整个身体（一个包含约 20 个点的骨架）。系统会测量每个点的三自由度（3-DOF）位置，但

方向无法被检测。而且由于它直接追踪身体，因此不需要“控制器”。研究人员利用 Kinect 设计了一些有趣的 3D 交互（例如 Wilson & Benko, 2010），但这些交互必然与基于单点 6 自由度（6-DOF, 6 Degrees of Freedom）追踪的交互截然不同。

![](https://public-media.interaction-design.org/images/encyclopedia/3d_user_interfaces/fig1_3d_user_interfaces.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”部分。
**图 32.1**：使用 Microsoft Kinect 的 3D 交互

第三，Leap Motion 设备（在本文撰写时已公布但尚未上市）有望在小型工作空间内实现对双手、手指和工具极其精确的 3D 追踪（3D tracking）。它有可能使 3D 交互成为桌面计算体验的标准组成部分，但我们仍需观察如何为该设备设计最佳的交互技术（interaction techniques）。它将具有与 Kinect 许多相似的优点和缺点，且尽管其设计旨在支持“自然”交互（natural interaction），但自然主义（naturalism）并非总是可行，也并非总是最佳解决方案（我们将在下文讨论）。

对于 3D 交互而言，空间追踪器（spatial trackers）最常被集成在手持设备（handheld devices）中。这些设备通常还包含其他输入方式，例如按钮，

摇杆（joysticks）或轨迹球（trackballs），使其类似于一种“3D 鼠标”。与桌面鼠标类似，这些设备可用于指向、操纵对象、选择菜单项等操作。追踪器（Trackers）还被用于测量用户的头部位置与朝向（orientation）。头部追踪（Head tracking）能够以自然的方式修改 3D 环境的视角。

3D 用户界面（3D UI）中所采用的空间追踪器（spatial tracker）类型对其[可用性（usability）](https://www.interaction-design.org/literature/topics/usability)有重大影响，且不同的追踪器可能需要不同的 UI 设计。例如，具有较高延迟（latency）的追踪器可能不适用于精确的对象操纵任务；而使用 3 自由度（3-DOF）朝向追踪器的界面则需要额外的手段来平移（translating）3D 环境中的视点，因为它无法追踪用户的位置。

这一简短的章节无法详尽地阐述空间追踪这一复杂课题。关于追踪技术及其相关问题的综述，可以参考 Welch 的论文（Welch & Foxlin, 2002），虽然该文发表时间较早，但质量极高。

### 32.3.2 其他输入设备

虽然空间追踪（Spatial Tracking）是 3D 用户界面（3D UIs）的基础输入设备，但它通常不足以独立完成所有任务。如前所述，大多数手持追踪器（Handheld Trackers）都包含其他类型的输入，因为很难将所有的界面操作都映射到追踪器的位置、方向或运动上。例如，为了确认选择操作，需要一个离散事件或命令（Discrete Event or Command），在这种情况下，按钮比手势动作要合适得多。Intersense IS900 操纵杆（wand）是这类手持追踪器的典型代表；它在手持式外形设计中包含了四个标准按钮、一个“触发”按钮以及一个 2 自由度（2-DOF）模拟摇杆（该摇杆同时也是一个按钮）。Kinect 由于采用了“无控制器（Controller-less）”设计，因此面临缺乏按钮等离散输入的困扰。

推广这一观点，我们可以看到，几乎任何类型的输入设备都可以通过对其进行追踪而变成空间输入设备（Spatial Input Device）。这通常需要向设备添加一些硬件，例如光学追踪标记（Optical Tracking Markers）。这扩展了追踪器的能力和表达能力（Expressiveness），并允许根据设备的位置和方向，对来自设备的输入进行不同的解释。例如，在我的实验室中，我们尝试对多点触控智能手机（Multi-touch Smartphones）进行追踪，并将多点触控输入与空间输入相结合，用于构建复杂的对象操纵界面（Complex Object Manipulation Interfaces）（Wilkes et al., 2012）。其他有趣的设备，例如弯曲敏感带（Bend-sensitive Tape），可以被

被追踪以提供额外的自由度（Degrees of Freedom, DoF）(Balakrishnan et al., 1999)。

手套（Gloves，或手指追踪器 Finger Trackers）是另一种经常与空间追踪器（Spatial Trackers）结合使用的输入设备。捏合手套（Pinch Gloves）用于检测手指之间的接触，而数据手套（Data Gloves）和手指追踪器则用于测量手指的关节角度。将这些设备与追踪器结合，可以实现有趣、自然且具有表现力的手势操作，例如空中打字（In-air Typing）(Bowman et al., 2002)、书写 (Ni et al., 2011) 或手语输入（Sign Language Input）(Fels & Hinton, 1997)。

### 32.3.3 显示设备（Displays）

早期关于 3D 用户界面（3D User Interfaces, 3D UIs）的大量研究是在与虚拟现实（Virtual Reality, VR）系统的交互背景下进行的，这些系统使用某种形式的“沉浸式（immersive）”显示设备，例如头戴式显示器（Head-Mounted Displays, HMDs）、环绕屏显示器（surround-screen displays，如 CAVEs）或墙面大小的立体显示器（wall-sized stereoscopic displays）。然而，由于面向游戏的消费级追踪设备（tracking devices）的普及，3D 交互越来越多地在电视甚至桌面显示器上进行。显示配置和特性的差异会对 3D UI 的设计和可用性（usability）产生重大影响。

HMDs（图 2）可提供 360 度的全方位环绕（当与头部追踪相结合时），并且能够遮挡用户对现实世界的视野，或者在增强现实（Augmented Reality, AR）系统中使用时增强对现实世界的视野。在 VR 应用中，HMDs 会导致用户无法看到自己的双手或身体其他部位，这意味着设备必须能够在无需视觉引导（eyes-free）的情况下使用，且用户在物理环境中移动时可能会有所顾虑。HMDs 的视场角（Field of View, FOV）也存在很大差异。当 FOV 较低时，3D UI 设计师必须谨慎地利用有限的屏幕空间（screen real estate）。

![](https://public-media.interaction-design.org/images/encyclopedia/3d_user_interfaces/fig2_3d_user_interfaces.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”部分。

**图 32.2**：佩戴头戴式显示器（Head-Mounted Display, HMD）使用 3D 用户界面（3D UI）。背景中的电视显示了 HMD 中呈现的图像。

类 CAVE 显示系统（CAVE-like displays, Cruz-Neira et al., 1993）可以提供全方位环绕，但更常见的是使用两到四个屏幕来部分环绕用户。在其他考虑因素中，对于 3D UI 而言，这意味着设计者必须为用户提供一种旋转世界（rotate the world）的方法。物理视角旋转与虚拟视角旋转的混合可能会令人困惑，并降低在视觉搜索（visual search, McMahan, 2011）等任务中的表现。

在电视等较小显示设备上的 3D UI 也会带来一些有趣的挑战。在 HMD 和 CAVE 中，软件视场（software field of view，即虚拟相机的 FOV）通常与显示设备的物理视场（physical FOV）相匹配，从而使视角显得真实，仿佛是通过窗户观察虚拟世界一样。然而，对于桌面显示器和电视，我们可能不知道显示器的尺寸或用户相对于显示器的位置，因此很难确定合适的软件视场。这反过来可能会影响用户理解所显示对象尺度（scale）的能力。

最后，我们已知显示特性会影响 3D 交互性能。例如，我实验室之前的研究表明，立体显示（stereoscopic display, Narayan et al., 2005）可以提高困难操纵任务（manipulation tasks）的性能，但对较简单的操纵任务（McMahan et al., 2006）则没有显著提升。

## 32.4 设计可用的 3D UI

作为[人机交互（HCI, Human-Computer Interaction）](https://www.interaction-design.org/literature/topics/human-computer-interaction)领域的一个重要课题，3D 交互出现的时间并不长。该领域的开创性论文直到 20 世纪 90 年代中后期才出现，引用次数最多的书籍出版于 2005 年，而 IEEE Symposium on 3D User Interfaces 直到 2006 年才开始举办。

因此，3D UI [设计原则（design principles）](https://www.interaction-design.org/literature/topics/design-principles)的成熟度落后于标准图形用户界面（GUIs）的设计原则。目前不存在标准的 3D UI（而且考虑到输入设备、显示设备和交互技术的多样性，尚不清楚是否可能存在标准），且缺乏成熟的 3D UI 设计指南。虽然像 Nielsen 的[启发式原则（heuristics）](https://www.interaction-design.org/literature/topics/heuristics)（Nielsen & Molich, 1990）等通用人机交互原则仍然适用，但它们不足以让我们理解如何设计一个可用的（usable）3D UI。

因此，制定针对 3D 交互的特定设计原则至关重要。虽然 3D UI 相关书籍（Bowman et al., 2005）以及其他几项研究（Kulik, 2009; Gabbard, 1997; Kaur, 1999）提供了详尽的[指南列表（lists）](https://www.interaction-design.org/literature/topics/lists)，但在这里，我尝试提炼出我认为关于优秀 3D UI 设计最重要的经验教训。

### 32.4.1 理解设计空间（Design Space）

尽管该领域尚处于起步阶段，但针对所谓的“通用任务（universal tasks）”——即移动（travel）、选择（selection）、操作（manipulation）和系统控制（system control）——已经存在大量的 3D 交互技术（3D interaction techniques）。在许多情况下，这些技术可以直接在新的应用中复用，或在稍作修改后使用。3D UI 书籍 (Bowman et al., 2005) 中的技术列表是一个很好的起点；更近期的技术可以在 IEEE 3DUI 和 VR、ACM CHI 和 UIST 以及其他主要会议的论文集中找到。

当现有技术不足以满足需求时，有时可以通过组合现有的技术组件（technique components）来生成新技术。技术组件的分类法（taxonomies of technique components）(Bowman et al., 2001) 可为此目的作为设计空间（design spaces）使用。

### 32.4.2 创新空间依然存在

目前已经存在极其丰富的技术，因此有人认为 3D 用户界面（3D UI）设计已无创新空间。一方面，大多数针对通用任务（universal tasks）的基础隐喻（primary metaphors）可能已经被发明了。但另一方面，有几个理由让我们相信，仍然存在与目前截然不同的新型隐喻。

首先，由于可用设备和映射（mappings）的数量众多，我们知道 3D 交互的设计空间（design space）非常广阔。其次，3D 交互设计可以是神奇的——其上限仅取决于设计者的想象力。第三，具有新交互形式潜力的各种新技术（如 Leap Motion 设备）在不断出现。例如，在我们实验室最近的一个项目中，学生们结合了多种新技术（多点触控平板、3D 重建、基于标记的 AR 跟踪以及拉伸传感器），实现了“AR 愤怒的小鸟（AR Angry Birds）”——这是一种在增强现实（AR）中与真实对象和虚拟对象进行物理交互（physical interaction）的新形式（图 3）。最后，可以针对各个应用领域中的专业任务设计特定的技术。例如，我们为建筑和施工领域的对象克隆（object cloning）设计了特定领域的交互技术 (Chen and Bowman, 2009)。

![](https://public-media.interaction-design.org/images/encyclopedia/3d_user_interfaces/fig3_3d_user_interfaces.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：

未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

**图 32.3**：具有实体弹弓并能“破坏”现实世界物体的 AR（增强现实，Augmented Reality）版《Angry Birds》原型——这是 3D 用户界面（User Interface, UI）设计中[创新（Innovation）](https://www.interaction-design.org/literature/topics/innovation)的一个示例。

### 32.4.3 注意映射与自由度（DOFs）

3D 用户界面（UI）设计中最常见的问题之一，是输入设备与界面操作之间使用了不恰当的映射（Mappings）。例如，Zhai & Milgram (1993) 表明，弹性传感器（Elastic sensors，如摇杆）和等长传感器（Isometric sensors，如 SpaceBall）非常适合映射到速率控制运动（Rate-controlled movements）——即传感器测得的位移或力被映射为虚拟世界中物体（包括视点）的速度；而等张传感器（Isotonic sensors，如位置追踪器）则非常适合映射到位置控制运动（Position-controlled movements）——即传感器测得的位置被映射为物体的位置。当违反这一原则时，操作性能会下降。

同样地，输入自由度（Degrees of Freedom, DOFs）与操作之间的映射也经常存在问题。当使用高自由度输入来执行仅需要低自由度的任务时，任务执行可能会变得异常困难。例如，选择菜单项本质上是一个一维任务。如果用户需要将虚拟手精准地放置在菜单项内才能进行选择（这属于 3-DOF 输入），那么该界面将要求用户付出过多的努力。

另一个关于自由度的问题是整体自由度（Integral DOFs）与可分自由度（Separable DOFs）的误用。Jacob & Sibert (1992) 表明，具有整体自由度的输入设备（即那些被统一控制的设备，如 6-DOF 追踪器）应当映射到用户感知为整体的任务中（例如 6-DOF 物体操纵）；而具有可分自由度的输入设备（即那些可以...

（例如一组滑块）应被映射到那些用户认为其子任务可分离的任务中（例如设置颜色的色相、饱和度和明度）。例如，违背这一原则的情况是使用六自由度（6-DOF, Degrees of Freedom）追踪器同时控制对象的 3D 位置和音频剪辑的音量，因为用户无法将这些任务整合在一起。

通常，3D 用户界面（3D UI）设计师应寻求减少用户需要控制的自由度数量。这可以通过使用低自由度输入设备、忽略部分输入自由度，或使用物理或虚拟约束（Constraints）来实现。例如，将虚拟 2D 界面放置在物理平板道具（Schmalstieg et al., 1999）上，提供了一种约束，使用户能够轻松地将 6-DOF 追踪器输入用于 2D 交互。

### 32.4.4 保持简单（Keep it simple）

虽然 3D 用户界面（3D User Interfaces, 3D UIs）具有很强的表现力（expressive）且能支持复杂任务，但并非 3D UI 中的所有任务都需要使用完全通用的交互技术（interaction techniques）。当用户的目标简单时，设计者应提供简单且毫不费力的技术。例如，有许多通用的移动技术（travel techniques）允许用户连续控制视点（viewpoint）的位置和方向，但如果用户只是想移动到某个已知的地标，那么简单的基于目标的技术（target-based technique）（例如，指向地标对象）将具有更高的可用性。

如前所述，减少自由度（Degrees of Freedom, DOFs）的数量是简化 3D UI 的另一种方法。例如，如果启用了地形跟随（terrain following），移动技术可能仅需要两个自由度。

最后，在使用物理按钮或手势映射（mapping）到命令/功能时，应避免为每个新命令都增加一个按钮或手势的倾向。用户通常无法记住大量的手势，而且在使用了 2-3 个按钮后，记住按钮与功能之间的映射关系就会变得困难。

### 32.4.5 针对硬件的设计（Design for the hardware）

在传统用户界面（User Interfaces, UIs）中，我们通常尝试在设计时不考虑显示器或输入设备（即显示与设备独立性 [display- and device-independence]）。无论用户使用的是大显示器还是小型笔记本电脑，使用鼠标还是触控板，UI 都应当具有相同的可用性。当然，这并不总是完全成立——例如，当你拥有一个非常大的多显示器设置时。但在 3D UI 中，在某种显示器或设备上有效的方法，极少能在不同的系统上以完全相同的方式运作。

我们称之为*迁移（migration）*问题。当迁移到不同的显示器或设备时，UI 和交互技术通常需要进行修改。换句话说，我们需要特定于显示和设备的 3D UI。

例如，微缩世界（World-in-Miniature, WIM）技术 (Stoakley et al., 1995) 允许用户通过操作对象的微小“娃娃屋”式表示（"dollhouse" representations）来移动全尺寸虚拟环境中的虚拟对象，该技术最初是为配备两个手持追踪器作为输入的头戴式显示器（Head-Mounted Display, HMD）而设计的。当我们尝试将 WIM 迁移到 CAVE (Bowman et al., 2007) 时，我们发现性能显著下降，这可能是因为当虚拟 WIM 靠近眼睛时，用户发现很难融合立体图像（stereo imagery）。此外，由于 CAVE 缺少后墙，我们不得不增加旋转世界的控制项。最近，我们尝试

将 WIM 迁移至使用 Kinect，但未能找到*任何*合理的映射（mapping）方式，能让用户轻松地以六自由度（six DOFs）操纵 WIM 和虚拟手。

### 32.4.6 您可能仍需对用户进行培训，但少量的培训也能产生显著效果

3D 交互（3D interaction）通常被认为是“自然的”，但对于许多初学者来说，有效地操作 3D 用户界面（3D User Interfaces, 3D UIs）绝非自然之举。使用头戴式显示器（Head-Mounted Displays, HMDs）的用户不愿转头，更不用说移动身体了。在二维平面（与屏幕平行）移动手部是没有问题的，但向屏幕靠近或远离的动作则并不自然。在使用 3D 移动技术（3D travel techniques）时，用户往往不会利用飞行、侧向移动或穿墙而过等能力 (Bowman et al., 1999)。

因此，我们发现，即使是设计良好的 3D UI，在用户能够熟练使用之前，通常也需要对其进行培训。在大多数人机交互（Human-Computer Interaction, HCI）社区中，需要培训或指导被视为[糟糕设计](https://www.interaction-design.org/literature/topics/bad-design)的标志，但在上述示例中，高效的使用要求用户违背其本能和直觉。如果一个极短的（一分钟）培训环节能让用户显著提高其操作表现，我们认为这既是务实的，也是积极的。

### 32.4.7 始终进行评估

最后，我们建议所有的 3D UI 设计都应针对目标用户群体进行形成性（formative）、实证的（empirical）[可用性评估（usability evaluation）](https://www.interaction-design.org/literature/topics/usability-evaluation)。虽然这一准则可能适用于所有用户界面，但 3D UI 尤其难以仅凭理论、原则和直觉就设计得完善。许多可用性问题直到用户实际尝试 3D UI 时才会显现。请尽早且频繁地进行评估。

## 32.5 当前 3D UI 研究

在最后一个章节中，我想重点介绍当前 3D UI 研究人员正在解决的两个有趣的问题。

### 32.5.1 现实主义与魔幻主义——交互保真度问题

3D UI 设计中的一个核心问题是现实交互（Realistic Interaction）与魔幻交互（Magical Interaction）之间的张力。许多人认为 3D 交互应当尽可能地“自然”，通过复用和模拟现实世界中的交互方式，使用户能够利用其既有技能，从而清楚地知道该做什么以及如何操作。另一方面，3D UI 主要允许用户与虚拟对象和环境进行交互，而这些对象的唯一限制在于程序员的技巧和技术的局限性。因此，“魔幻”交互成为可能，它能让用户超越人类[感知（Perception）](https://www.interaction-design.org/literature/topics/perception)和行动的局限，减少或消除体力消耗和冗长的操作，甚至执行在现实世界中无法完成的任务。

这个问题与*交互保真度（Interaction Fidelity）*的概念相关。我们将交互保真度定义为：在 UI 中执行某项任务时所采取的动作（以动作、力度、使用的身体部位等为特征）与在现实世界中执行该任务时所采取的动作之间相对应的客观程度 (Bowman et al., 2012)。通过讨论保真度的*程度*，我们强调讨论的不仅是“现实”与“非现实”的交互，而是一个现实主义的连续体（Continuum of Realism），且该连续体本身包含多个不同的维度。

考虑一个例子。对于

针对将一本虚拟书籍从桌面上的一个位置移动到另一个位置的任务，在众多选项中，我们可以：a) 精确映射用户真实手部和手指的动作，要求精确的放置、抓取和释放；b) 将 3D 光标（3D cursor）置于书籍上方，按下按钮，将光标移动到目标位置，然后松开按钮；或者 c) 从菜单中选择“移动”，然后使用激光指针（laser pointer）来指示书籍和目标位置。显然，选项 a) 是最自然的，选项 b) 使用了自然隐喻（natural metaphor）但省略了现实世界交互中一些不那么必要的细节，而选项 c) 的交互保真度（interaction fidelity）非常低。只要设计者能够足够好地复制现实世界中的动作和感知线索（perceptual cues），选项 a) 对新手用户来说可能最容易学习和使用，尽管选项 b) 最简单且可能同样有效。

某些任务在现实世界中非常困难（或不可能）完成。如果我想从一座城市中移除一座建筑会怎样？一个高度自然的 3D 用户界面（3D UI）将要求用户获取一些虚拟炸药或带有拆除球的虚拟起重机，并在较长时间内操作这些设备。在这种情况下，一种“魔法”技术（"magic" technique）——例如允许用户“擦除”建筑，或者选择建筑并通过语音调用“删除”命令——显然更加实用且高效。

在许多困难任务的情况下，问题不在于我们应该使用自然还是魔法的 3D

UI，因为纯自然交互技术（purely natural technique）并不实用。

相反，问题在于是否应该使用一种自然*隐喻*（natural metaphor）。例如，在现实世界中，我无法拿起手臂触及范围之外的物体，但在虚拟世界中我可以。我应该采用伸手抓取隐喻（reaching and grasping metaphor）来实现吗？例如 Go-Go 技术 (Poupyrev et al., 1996)，该技术基于自然动作将用户的虚拟手延伸到环境深处。还是应该通过激光指针隐喻（laser pointer metaphor）指向物体来将其拿起，如 HOMER 技术 (Bowman & Hodges, 1997) 所采用的方式？在这种情况下，虽然自然度较低的激光指针隐喻在用户绩效（user performance）方面更有效，但增强的自然隐喻在许多场景下更容易学习且具有极高的可用性（usability）。

由于像 Go-Go 这样的技术利用自然隐喻将用户的能力扩展到超出现实世界的可能范围，我们将此类技术称为*超自然*（hyper-natural）。对于应该选择自然、超自然还是非自然魔法技术（non-natural magic techniques）这个问题，并没有统一的答案，但总体而言，研究表明自然和超自然的设计方法具有显著的优势 (Bowman et al., 2012)。

### 32.5.2 提高精密度（Increasing Precision）

基于空间追踪系统（spatial tracking systems）的 3D 用户界面（3D UIs）的一个主要缺点是难以提供精确的 3D 空间输入。现代鼠标是一种高度精密、准确且响应迅速的 2D 空间输入设备——用户可以快速且准确地指向屏幕上的元素，甚至是单个像素。在精密度（precision，指抖动/jitter）、报告值的准确度（accuracy）以及响应速度（responsiveness，指延迟/latency）方面，3D 空间追踪系统远落后于鼠标，这使得将它们用于需要高精度的任务变得十分困难 (Teather et al., 2009)。

但即便 3D 空间追踪系统的技术指标提升到能与当今的鼠标相媲美，3D 用户界面仍然会面临精密度问题，原因如下：

- 3D 交互是在空中进行的，而非在平面上。由于缺乏摩擦力或物理支撑，使得动作难以更加可控且精确。
- 人类天生具有手部震颤（hand tremor），这会导致在空中的动作出现抖动。
- 基于光线投射（ray-casting，即激光笔隐喻/laser pointer metaphor）的 3D 指向界面会放大这种手部震颤，且沿着光线延伸越远，情况就越严重。
- 3D 空间追踪器不像鼠标那样具有“可停靠性（parkable）”——用户无法在松开它们后确保它们仍保持在同一位置。

那么，能够用于精密工作的 3D 用户界面是否还有希望？一个部分解决方案是对 3D 空间追踪器的输出进行滤波（filter）以减少噪声，但滤波...

可能会导致其他问题，例如延迟（Latency）增加。目前的研究正采用几种不同的策略来解决精确度问题（Precision problem）。

一种方法是修改控制/显示比（Control/Display ratio, C/D ratio）。其核心思路是在输入设备（控制端）的移动与系统（显示端）的移动之间使用 N:1 的映射（Mapping），其中 N 大于 1。换句话说，如果 C/D 比为 5，那么追踪器（Tracker）移动 5 厘米（或旋转 5 度）将导致虚拟世界（Virtual world）中 1 厘米的移动（或 1 度的旋转）。这赋予了用户更高程度的控制力以及实现更高精确度的能力，但代价是增加了体力消耗和时间成本。一些技术（例如 Frees et al., 2007）会动态地修改 C/D 比，从而仅在必要时（例如用户移动缓慢时）增加精确度。

第二种策略是确保用户不需要达到超出绝对必要范围的精确度。例如，如果用户在稀疏环境中选择一个非常小的对象，则无需要求用户精确地触摸或指向该对象。相反，光标可以具有面积或体积（例如圆形或球体），而不是一个点（例如 Liang & Green, 1994），或者光标可以吸附（Snap）到最近的对象（例如 de Haan et al., 2005）。

最后，一种被称为 *渐进式细化（Progressive refinement）* 的极具前景的方法将交互过程在时间上展开，而不是要求一次性

精确操作。一系列粗略且不精确的操作可以用来实现精确的结果，而无需用户付出过多努力。例如，SQUAD 技术 (Kopper et al., 2011) 允许用户在杂乱的环境中选择小型对象，其方法是先进行体积选择（Volume Selection），然后通过一系列快速的菜单选择来细化所选对象的集合。在极困难的情况下，该技术甚至比光线投射（Ray-casting）更快，而后者使用的是单次精确选择；并且在所有情况下，SQUAD 导致的选择错误都更少。这种渐进式细化方法（Progressive Refinement Approach）应广泛适用于许多类型的困难 3D 交互任务。

## 32.6 延伸阅读

- 若要了解 3D 用户界面（3D User Interfaces, 3D UIs）领域的概况，以及关于设备和交互技术（interaction techniques）的全面综述，请参阅 *3D User Interfaces: Theory and Practice* (Bowman et al., 2005)。
- 该领域目前最前沿的研究可见于 *IEEE Symposium on 3D User Interfaces* 的论文集（proceedings）。
- 关于如何在 3D UI 设计中运用真实感（realism）与魔幻感（magic），请参阅 *IEEE Computer Graphics & Applications* 中近期的一篇教程 (Kulik, 2009)。
- Wolfgang Stuerzlinger 在近期的一篇综述论文 (Bowman et al., 2008) 中，基于其在 3D UI 设计方面的多年经验，提供了一套实用指南。
- 若想进一步了解关于 3D UI 中交互保真度（interaction fidelity）影响的实验结果，请参阅我近期发表在 *Communications of the ACM* 上的论文 (Bowman et al., 2012)。

## 32.7 References

[Ashley](https://www.interaction-design.org/references/authors/steven_ashley.html), Steven (2008): *Annotating the Real World: Augmented Reality Makes Commercial Headway*. In [Scientific American](https://www.interaction-design.org/references/periodicals/scientific_american.html), 299 (4) pp. 27-28
[Balakrishnan](https://www.interaction-design.org/references/authors/ravin_balakrishnan.html), Ravin, [Fitzmaurice](https://www.interaction-design.org/references/authors/george_w__fitzmaurice.html), George W., [Kurtenbach](https://www.interaction-design.org/references/authors/gordon_kurtenbach.html), Gordon and [Singh](https://www.interaction-design.org/references/authors/karan_singh.html), Karan (1999): Exploring interactive curve and surface manipulation using a bend and twist sensitive input strip. In: [SI3D 1999](https://www.interaction-design.org/references/conferences/si3d_1999.html) 1999. pp. 111-118
[Bowman](https://www.interaction-design.org/references/authors/doug_a__bowman.html), Doug A. and [Hodges](https://www.interaction-design.org/references/authors/larry_f__hodges.html),
 Larry F. (1997): An Evaluation of Techniques for Grabbing and 
Manipulating Remote Objects in Immersive Virtual Environments. In: [SI3D 1997](https://www.interaction-design.org/references/conferences/si3d_1997.html) 1997. pp. 35-38,182

[Bowman](https://www.interaction-design.org/references/authors/doug_a__bowman.html), Doug A., [McMahan](https://www.interaction-design.org/references/authors/ryan_p__mcmahan.html), Ryan P. and [Ragan](https://www.interaction-design.org/references/authors/eric_d__ragan.html), Eric D. (2012): *Questioning naturalism in 3D user interfaces*. In[Communications of the ACM](https://www.interaction-design.org/references/periodicals/communications_of_the_acm.html), 55 (9) pp. 78-88
[Bowman](https://www.interaction-design.org/references/authors/doug_a__bowman.html), Doug A., [Johnson](https://www.interaction-design.org/references/authors/donald_b__johnson.html), Donald B. and [Hodges](https://www.interaction-design.org/references/authors/larry_f__hodges.html), Larry F. (2001): *Testbed Evaluation of Virtual Environment Interaction Techniques*. In [Presence: Teleoperators and Virtual Environments](https://www.interaction-design.org/references/periodicals/presence-_teleoperators_and_virtual_environments.html), 10 (1) pp. 75-95
[Bowman](https://www.interaction-design.org/references/authors/doug_a__bowman.html), Doug A., [Kruijff](https://www.interaction-design.org/references/authors/ernst_kruijff.html), Ernst, [LaViola](https://www.interaction-design.org/references/authors/joseph_j__laviola.html), Joseph J. and [Poupyrev](https://www.interaction-design.org/references/authors/ivan_poupyrev.html), Ivan (2005): *3D User Interfaces: Theory and Practice.* Addison-Wesley Professional

[Bowman](https://www.interaction-design.org/references/authors/doug_a__bowman.html), Doug A., [Wingrave](https://www.interaction-design.org/references/authors/chadwick_a__wingrave.html), Chadwick A., [Campbell](https://www.interaction-design.org/references/authors/j__m__campbell.html), J. M., [Ly](https://www.interaction-design.org/references/authors/v__q__ly.html), V. Q. and [Rhoton](https://www.interaction-design.org/references/authors/c__j__rhoton.html), C. J. (2002): *Novel Uses of Pinch GlovesTM for Virtual Environment Interaction Techniques*. In [Virtual Reality](https://www.interaction-design.org/references/periodicals/virtual_reality.html), 6 (3) pp. 122-129
[Bowman](https://www.interaction-design.org/references/authors/doug_a__bowman.html), Doug A., [Davis](https://www.interaction-design.org/references/authors/elizabeth_thorpe_davis.html), Elizabeth Thorpe, [Hodges](https://www.interaction-design.org/references/authors/larry_f__hodges.html), Larry F. and [Badre](https://www.interaction-design.org/references/authors/albert_n__badre.html), Albert N. (1999): *Maintaining Spatial Orientation during Travel in an Immersive Virtual Environment*. In [Presence: Teleoperators and Virtual Environments](https://www.interaction-design.org/references/periodicals/presence-_teleoperators_and_virtual_environments.html), 8 (6) pp. 618-631

[Bowman](https://www.interaction-design.org/references/authors/doug_a__bowman.html), Doug A., [Coquillart](https://www.interaction-design.org/references/authors/sabine_coquillart.html), Sabine, [Froehlich](https://www.interaction-design.org/references/authors/bernd_froehlich.html), Bernd, [Hirose](https://www.interaction-design.org/references/authors/michitaka_hirose.html), Michitaka, [Kitamura](https://www.interaction-design.org/references/authors/yoshifumi_kitamura.html), Yoshifumi, [Kiyokawa](https://www.interaction-design.org/references/authors/kiyoshi_kiyokawa.html), Kiyoshi and [Stürzlinger](https://www.interaction-design.org/references/authors/wolfgang_st%FCrzlinger.html), Wolfgang (2008): *3D User Interfaces: New Directions and Perspectives*. In [IEEE Computer Graphics and Applications](https://www.interaction-design.org/references/periodicals/ieee_computer_graphics_and_applications.html), 28 (6) pp. 20-36

[Bowman](https://www.interaction-design.org/references/authors/doug_a__bowman.html), Doug A., [Badillo](https://www.interaction-design.org/references/authors/brian_badillo.html), Brian and [Manek](https://www.interaction-design.org/references/authors/dhruv_manek.html), Dhruv (2007): Evaluating the Need for Display-Specific and Device-Specific 3D Interaction Techniques. In: [Shumaker](https://www.interaction-design.org/references/authors/randall_shumaker.html), Randall (ed.) [ICVR 2007 - Virtual Reality - Second International Conference - Part 1](https://www.interaction-design.org/references/conferences/icvr_2007_-_virtual_reality_-_second_international_conference_-_part_1.html) July 22-27, 2007, Beijing, China. pp. 195-204
[Chen](https://www.interaction-design.org/references/authors/jian_chen.html), Jian and [Bowman](https://www.interaction-design.org/references/authors/doug_a__bowman.html), Doug A. (2009): *Domain-Specific Design of 3D Interaction Techniques: An Approach for Designing Useful Virtual Environment Applications*. In [Presence: Teleoperators and Virtual Environments](https://www.interaction-design.org/references/periodicals/presence-_teleoperators_and_virtual_environments.html), 18 (5) pp. 370-386

[Cruz-Neira](https://www.interaction-design.org/references/authors/carolina_cruz-neira.html), Carolina, [Sandin](https://www.interaction-design.org/references/authors/daniel_j__sandin.html), Daniel J. and [DeFanti](https://www.interaction-design.org/references/authors/thomas_a__defanti.html), Thomas A. (1993): Surround-screen projection-based virtual reality: the design and implementation of the CAVE. In: [Proceedings of the 20st Annual Conference on Computer Graphics and Interactive Techniques, SIGGRAPH 1993](https://www.interaction-design.org/references/conferences/proceedings_of_the_20st_annual_conference_on_computer_graphics_and_interactive_techniques%2C_siggraph_1993.html) 1993. pp. 135-142
[Feiner](https://www.interaction-design.org/references/authors/steven_k__feiner.html), Steven K., [MacIntyre](https://www.interaction-design.org/references/authors/blair_macintyre.html), Blair and [Seligmann](https://www.interaction-design.org/references/authors/doree_duncan_seligmann.html), Doree Duncan (1992): Annotating the real world with knowledge--based graphics on a see--through head--mounted display. In: [Graphics Interface 92](https://www.interaction-design.org/references/conferences/graphics_interface_92.html) May 11-15, 1992, Vancouver, British Columbia, Canada. pp. 78-85

[Fels](https://www.interaction-design.org/references/authors/s__s__fels.html), S. S. and [Hinton](https://www.interaction-design.org/references/authors/g__e__hinton.html), G. E. (1997): *Glove-talk II - a neural-network interface which maps gestures to parallel formant speech synthesizer controls*. In [IEEE Transactions on Neural Networks](https://www.interaction-design.org/references/periodicals/ieee_transactions_on_neural_networks.html), 8 (5) pp. 977-984
[Frees](https://www.interaction-design.org/references/authors/scott_frees.html), Scott, [Kessler](https://www.interaction-design.org/references/authors/g__drew_kessler.html), G. Drew and [Kay](https://www.interaction-design.org/references/authors/edwin_kay.html), Edwin (2007): *PRISM interaction for enhancing control in immersive virtual environments*. In [ACM Transactions on Computer-Human Interaction](https://www.interaction-design.org/references/periodicals/acm_transactions_on_computer-human_interaction.html), 14 (1) p. 2
[Gabbard](https://www.interaction-design.org/references/authors/joseph_l__gabbard.html), Joseph L. (1997). *Taxonomy of Usability Characteristics in Virtual Environments. (M.S. Thesis)*. Virginia Tech.
Google (2012). *Project Glass*. Retrieved 7 November 2012 from Google: https://plus.google.com/+projectglass/posts.

[Haan](https://www.interaction-design.org/references/authors/gerwin_de_haan.html), Gerwin de, [Koutek](https://www.interaction-design.org/references/authors/michal_koutek.html), Michal and [Post](https://www.interaction-design.org/references/authors/frits_h__post.html), Frits H. (2005): IntenSelect: Using Dynamic Object Rating for Assisting 3D Object Selection. In: [Kjems](https://www.interaction-design.org/references/authors/eric_kjems.html), Eric and [Blach](https://www.interaction-design.org/references/authors/roland_blach.html), Roland (eds.) [Proceedings
 of the 9th Int. Workshop on Immersive Projection Technology - 11th 
Eurographics Workshop on Virtual Environments - IPT-EGVE 2005](https://www.interaction-design.org/references/conferences/proceedings_of_the_9th_int__workshop_on_immersive_projection_technology_-_11th_eurographics_workshop_on_virtual_environments_-_ipt-egve_2005.html)2005, Aalborg, Denmark. pp. 201-209

[Höllerer](https://www.interaction-design.org/references/authors/tobias_h%F6llerer.html), Tobias, [Feiner](https://www.interaction-design.org/references/authors/steven_feiner.html), Steven, [Terauchi](https://www.interaction-design.org/references/authors/tachio_terauchi.html), Tachio, [Rashid](https://www.interaction-design.org/references/authors/gus_rashid.html), Gus and [Hallaway](https://www.interaction-design.org/references/authors/drexel_hallaway.html), Drexel (1999): *Exploring MARS: developing indoor and outdoor user interfaces to a mobile augmented reality system*. In [Computers & Graphics](https://www.interaction-design.org/references/periodicals/computers_%26_graphics.html), 23 (6) pp. 779-785

[Jacob](https://www.interaction-design.org/references/authors/robert_j__k__jacob.html), Robert J. K. and [Sibert](https://www.interaction-design.org/references/authors/linda_e__sibert.html), Linda E. (1992): The Perceptual Structure of Multidimensional Input Device Selection. In: [Bauersfeld](https://www.interaction-design.org/references/authors/penny_bauersfeld.html), Penny, [Bennett](https://www.interaction-design.org/references/authors/john_bennett.html), John and [Lynch](https://www.interaction-design.org/references/authors/gene_lynch.html), Gene (eds.) [Proceedings of the ACM CHI 92 Human Factors in Computing Systems Conference](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_92_human_factors_in_computing_systems_conference.html) June 3-7, 1992, Monterey, California. pp. 211-218
[Kaur](https://www.interaction-design.org/references/authors/k__kaur.html), K. (1999). *Designing Virtual Environments for Usability. Doctoral Dissertation*. University College, London

[Klein](https://www.interaction-design.org/references/authors/georg_klein.html), Georg and [Murray](https://www.interaction-design.org/references/authors/david_w__murray.html), David W. (2007): Parallel Tracking and Mapping for Small AR Workspaces. In: [Sixth IEEE/ACM International Symposium on Mixed and Augmented Reality, ISMAR 2007, 13-16 November 2007, Nara, Japan](https://www.interaction-design.org/references/conferences/sixth_ieee%2Facm_international_symposium_on_mixed_and_augmented_reality%2C_ismar_2007%2C_13-16_november_2007%2C_nara%2C_japan.html) 2007. pp. 225-234
[Kopper](https://www.interaction-design.org/references/authors/regis_kopper.html), Regis, [Bowman](https://www.interaction-design.org/references/authors/doug_a__bowman.html), Doug A., [Silva](https://www.interaction-design.org/references/authors/mara_g__silva.html), Mara G. and [McMahan](https://www.interaction-design.org/references/authors/ryan_p__mcmahan.html), Ryan P. (2010): *A human motor behavior model for distal pointing tasks*. In [International Journal of Human-Computer Studies](https://www.interaction-design.org/references/periodicals/international_journal_of_human-computer_studies.html), 68 (10) pp. 603-615

[Kopper](https://www.interaction-design.org/references/authors/regis_kopper.html), Regis, [Bacim](https://www.interaction-design.org/references/authors/felipe_bacim.html), Felipe and [Bowman](https://www.interaction-design.org/references/authors/doug_a__bowman.html), Doug A. (2011): Rapid and accurate 3D selection by progressive refinement. In: [Proceedings of the 2011 IEEE Symposium on 3D User Interfaces](https://www.interaction-design.org/references/conferences/proceedings_of_the_2011_ieee_symposium_on_3d_user_interfaces.html) 2011. pp. 67-74
[Kulik](https://www.interaction-design.org/references/authors/alexander_kulik.html), Alexander (2009): *Building on Realism and Magic for Designing 3D Interaction Techniques*. In [IEEE Computer Graphics and Applications](https://www.interaction-design.org/references/periodicals/ieee_computer_graphics_and_applications.html), 29 (6) pp. 22-33
[LaViola](https://www.interaction-design.org/references/authors/joseph_j__laviola.html), Joseph J. (2008): *Bringing VR and Spatial 3D Interaction to the Masses through Video Games*. In [IEEE Computer Graphics and Applications](https://www.interaction-design.org/references/periodicals/ieee_computer_graphics_and_applications.html), 28 (5) pp. 10-15

[Liang](https://www.interaction-design.org/references/authors/jiandong_liang.html), Jiandong and [Green](https://www.interaction-design.org/references/authors/mark_green.html), Mark (1994): *JDCAD: A highly interactive 3D modeling system*. In [Computers & Graphics](https://www.interaction-design.org/references/periodicals/computers_%26_graphics.html), 18 (4) pp. 499-506
[McMahan](https://www.interaction-design.org/references/authors/ryan_patrick_mcmahan.html), Ryan Patrick (2011). *Exploring the Effects of Higher-Fidelity Display and Interaction for Virtual Reality Games. (Ph.D. dissertation)*. Virginia Tech.

[McMahan](https://www.interaction-design.org/references/authors/ryan_p__mcmahan.html), Ryan P., [Gorton](https://www.interaction-design.org/references/authors/doug_gorton.html), Doug, [Gresock](https://www.interaction-design.org/references/authors/joe_gresock.html), Joe, [McConnell](https://www.interaction-design.org/references/authors/will_mcconnell.html), Will and [Bowman](https://www.interaction-design.org/references/authors/doug_a__bowman.html), Doug A. (2006): Separating the effects of level of immersion and 3D interaction techniques. In: [Slater](https://www.interaction-design.org/references/authors/mel_slater.html), Mel, [Kitamura](https://www.interaction-design.org/references/authors/yoshifumi_kitamura.html), Yoshifumi, [Tal](https://www.interaction-design.org/references/authors/ayellet_tal.html), Ayellet,[Amditis](https://www.interaction-design.org/references/authors/angelos_amditis.html), Angelos and [Chrysanthou](https://www.interaction-design.org/references/authors/yiorgos_chrysanthou.html), Yiorgos (eds.) [VRST 2006 - Proceedings of the ACM Symposium on Virtual Reality Software and Technology](https://www.interaction-design.org/references/conferences/vrst_2006_-_proceedings_of_the_acm_symposium_on_virtual_reality_software_and_technology.html) November 1-3, 2006, Limassol, Cyprus. pp. 108-111

[Meyer](https://www.interaction-design.org/references/authors/kenneth_meyer.html), Kenneth, [Applewhite](https://www.interaction-design.org/references/authors/hugh_l__applewhite.html), Hugh L. and [Biocca](https://www.interaction-design.org/references/authors/frank_a__biocca.html), Frank A. (1992): *A Survey of Position Trackers*. In [Presence: Teleoperators and Virtual Environments](https://www.interaction-design.org/references/periodicals/presence-_teleoperators_and_virtual_environments.html), 1 (2) pp. 173-200
[Mistry](https://www.interaction-design.org/references/authors/pranav_mistry.html), Pranav and [Maes](https://www.interaction-design.org/references/authors/pattie_maes.html), Pattie (2009): SixthSense: a wearable gestural interface. In: [Oda](https://www.interaction-design.org/references/authors/yuko_oda.html), Yuko and [Tanaka](https://www.interaction-design.org/references/authors/mariko_tanaka.html), Mariko (eds.) [International
 Conference on Computer Graphics and Interactive Techniques, SIGGRAPH 
ASIA 2009, Yokohama, Japan, December 16-19, 2009, Art Gallery and 
Emerging Technologies Adaptation](https://www.interaction-design.org/references/conferences/international_conference_on_computer_graphics_and_interactive_techniques%2C_siggraph_asia_2009%2C_yokohama%2C_japan%2C_december_16-19%2C_2009%2C_art_gallery_and_emerging_technologies_adaptation.html) 2009. p. 85

[Narayan](https://www.interaction-design.org/references/authors/michael_narayan.html), Michael, [Waugh](https://www.interaction-design.org/references/authors/leo_waugh.html), Leo, [Zhang](https://www.interaction-design.org/references/authors/xiaoyu_zhang.html), Xiaoyu, [Bafna](https://www.interaction-design.org/references/authors/pradyut_bafna.html), Pradyut and [Bowman](https://www.interaction-design.org/references/authors/doug_a__bowman.html), Doug A. (2005): Quantifying the benefits of immersion for [collaboration](https://www.interaction-design.org/literature/topics/collaboration) in virtual environments. In: [Singh](https://www.interaction-design.org/references/authors/gurminder_singh.html), Gurminder, [Lau](https://www.interaction-design.org/references/authors/rynson_w__h__lau.html), Rynson W. H.,[Chrysanthou](https://www.interaction-design.org/references/authors/yiorgos_chrysanthou.html), Yiorgos and [Darken](https://www.interaction-design.org/references/authors/rudolph_p__darken.html), Rudolph P. (eds.) [VRST 2005 - Proceedings of the ACM Symposium on Virtual Reality Software and Technology](https://www.interaction-design.org/references/conferences/vrst_2005_-_proceedings_of_the_acm_symposium_on_virtual_reality_software_and_technology.html) November 7-9, 2005, Monterey, CA, USA. pp. 78-81

[Ni](https://www.interaction-design.org/references/authors/tao_ni.html), Tao, [Bowman](https://www.interaction-design.org/references/authors/doug_a__bowman.html), Doug A. and [North](https://www.interaction-design.org/references/authors/chris_north.html), Chris (2011): AirStroke: bringing unistroke text entry to freehand gesture interfaces. In: [Proceedings of ACM CHI 2011 Conference on Human Factors in Computing Systems](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2011_conference_on_human_factors_in_computing_systems.html) 2011. pp. 2473-2476
[Nielsen](https://www.interaction-design.org/references/authors/jakob_nielsen.html), Jakob and [Molich](https://www.interaction-design.org/references/authors/rolf_molich.html), Rolf (1990): [Heuristic evaluation](https://www.interaction-design.org/literature/topics/heuristic-evaluation) of user interfaces. In: [Carrasco](https://www.interaction-design.org/references/authors/jane_carrasco.html), Jane and [Whiteside](https://www.interaction-design.org/references/authors/john_whiteside.html), John (eds.) [Proceedings of the ACM CHI 90 Human Factors in Computing Systems Conference](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_90_human_factors_in_computing_systems_conference.html) 1990, Seattle, Washington,USA. pp. 249-256

[Poupyrev](https://www.interaction-design.org/references/authors/ivan_poupyrev.html), Ivan, [Billinghurst](https://www.interaction-design.org/references/authors/mark_billinghurst.html), Mark, [Weghorst](https://www.interaction-design.org/references/authors/suzanne_weghorst.html), Suzanne and [Ichikawa](https://www.interaction-design.org/references/authors/tadao_ichikawa.html), Tadao (1996): The Go-Go Interaction Technique: Non-Linear Mapping for Direct Manipulation in VR. In: [Kurlander](https://www.interaction-design.org/references/authors/david_kurlander.html), David, [Brown](https://www.interaction-design.org/references/authors/marc_brown.html), Marc and [Rao](https://www.interaction-design.org/references/authors/ramana_rao.html), Ramana (eds.) [Proceedings of the 9th annual ACM symposium on User interface software and technology](https://www.interaction-design.org/references/conferences/proceedings_of_the_9th_annual_acm_symposium_on_user_interface_software_and_technology.html)November 06 - 08, 1996, Seattle, Washington, United States. pp. 79-80

[Rekimoto](https://www.interaction-design.org/references/authors/jun_rekimoto.html), Jun (1998): Multiple-Computer User Interfaces: A Cooperative Environment Consisting of Multiple Digital Devices. In: [Streitz](https://www.interaction-design.org/references/authors/norbert_a__streitz.html), Norbert A., [Konomi](https://www.interaction-design.org/references/authors/shin%27ichi_konomi.html), Shin'ichi and [Burkhardt](https://www.interaction-design.org/references/authors/heinz_j%FCrgen_burkhardt.html), Heinz Jürgen (eds.) [Cooperative
 Buildings, Integrating Information, Organization, and Architecture, 
First International Workshop, CoBuild98, Darmstadt, Germany, February 
1998, Proceedings](https://www.interaction-design.org/literature/conference/cooperative-buildings-integrating-information-organization-and-architecture-first-international-workshop-cobuild98-darmstadt-germany-february-1998-proceedings) 1998. pp. 33-40
[Schmalstieg](https://www.interaction-design.org/references/authors/dieter_schmalstieg.html), Dieter, [Encarnacao](https://www.interaction-design.org/references/authors/l__miguel_encarnacao.html), L. Miguel and [Szalavári](https://www.interaction-design.org/references/authors/zsolt_szalav%E1ri.html), Zsolt (1999): Using transparent props for interaction with the virtual table. In: [SI3D 1999](https://www.interaction-design.org/references/conferences/si3d_1999.html) 1999. pp. 147-153

[Stoakley](https://www.interaction-design.org/references/authors/richard_stoakley.html), Richard, [Conway](https://www.interaction-design.org/references/authors/matthew_conway.html), Matthew and [Pausch](https://www.interaction-design.org/references/authors/randy_pausch.html), Randy (1995): Virtual Reality on a WIM: Interactive Worlds in Miniature. In: [Katz](https://www.interaction-design.org/references/authors/irvin_r__katz.html), Irvin R., [Mack](https://www.interaction-design.org/references/authors/robert_l__mack.html), Robert L., [Marks](https://www.interaction-design.org/references/authors/linn_marks.html), Linn, [Rosson](https://www.interaction-design.org/references/authors/mary_beth_rosson.html), Mary Beth and [Nielsen](https://www.interaction-design.org/references/authors/jakob_nielsen.html), Jakob (eds.)[Proceedings of the ACM CHI 95 Human Factors in Computing Systems Conference](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_95_human_factors_in_computing_systems_conference.html) May 7-11, 1995, Denver, Colorado. pp. 265-272

[Teather](https://www.interaction-design.org/references/authors/robert_j__teather.html), Robert J., [Pavlovych](https://www.interaction-design.org/references/authors/andriy_pavlovych.html), Andriy, [Stuerzlinger](https://www.interaction-design.org/references/authors/wolfgang_stuerzlinger.html), Wolfgang and [MacKenzie](https://www.interaction-design.org/references/authors/i__scott_mackenzie.html), I. Scott (2009): Effects of tracking technology, latency, and spatial jitter on object movement. In: [Proceedings of the 2009 IEEE Symposium on 3D User Interfaces](https://www.interaction-design.org/references/conferences/proceedings_of_the_2009_ieee_symposium_on_3d_user_interfaces.html) 2009. pp. 43-50
[van Dam](https://www.interaction-design.org/references/authors/andries_van_dam.html), Andries (1997): *Post-WIMP User Interfaces*. In [Communications of the ACM](https://www.interaction-design.org/references/periodicals/communications_of_the_acm.html), 40 (2) pp. 63-67

[Vogel](https://www.interaction-design.org/references/authors/daniel_vogel.html), Daniel and [Balakrishnan](https://www.interaction-design.org/references/authors/ravin_balakrishnan.html), Ravin (2005): Distant freehand pointing and clicking on very large, high resolution displays. In: [Proceedings of the 2005 ACM Symposium on User Interface Software and Technology](https://www.interaction-design.org/references/conferences/proceedings_of_the_2005_acm_symposium_on_user_interface_software_and_technology.html) 2005. pp. 33-42
[Welch](https://www.interaction-design.org/references/authors/greg_welch.html), Greg and [Foxlin](https://www.interaction-design.org/references/authors/eric_foxlin.html), Eric (2002): *Motion Tracking: No Silver Bullet, but a Respectable Arsenal*. In [IEEE Computer Graphics and Applications](https://www.interaction-design.org/references/periodicals/ieee_computer_graphics_and_applications.html), 22 (6) pp. 24-38
[Wigdor](https://www.interaction-design.org/references/authors/daniel_wigdor.html), Daniel and [Wixon](https://www.interaction-design.org/references/authors/dennis_wixon.html), Dennis (2011): *Brave NUI World: Designing *[*Natural User Interfaces*](https://www.interaction-design.org/literature/topics/natural-user-interfaces)* for Touch and Gesture.* Morgan Kaufmann

[Wilkes](https://www.interaction-design.org/references/authors/curtis_b__wilkes.html), Curtis B., [Tilden](https://www.interaction-design.org/references/authors/dan_tilden.html), Dan and [Bowman](https://www.interaction-design.org/references/authors/doug_a__bowman.html), Doug A. (2012): 3D User Interfaces Using Tracked Multi-touch Mobile Devices. In: [Joint Virtual Reality Conference of ICAT - EGVE - EuroVR 2012](https://www.interaction-design.org/references/conferences/joint_virtual_reality_conference_of_icat_-_egve_-_eurovr_2012.html) 2012.
[Wilson](https://www.interaction-design.org/references/authors/andrew_d__wilson.html), Andrew D. and [Benko](https://www.interaction-design.org/references/authors/hrvoje_benko.html), Hrvoje (2010): Combining multiple depth cameras and projectors for interactions on, above and between surfaces. In: [Proceedings of the 2010 ACM Symposium on User Interface Software and Technology](https://www.interaction-design.org/references/conferences/proceedings_of_the_2010_acm_symposium_on_user_interface_software_and_technology.html) 2010. pp. 273-282

[Wingrave](https://www.interaction-design.org/references/authors/chadwick_a__wingrave.html), Chadwick A., [Williamson](https://www.interaction-design.org/references/authors/brian_williamson.html), Brian, [Varcholik](https://www.interaction-design.org/references/authors/paul_varcholik.html), Paul, [Rose](https://www.interaction-design.org/references/authors/jeremy_rose.html), Jeremy, [Miller](https://www.interaction-design.org/references/authors/andrew_miller.html), Andrew, [Charbonneau](https://www.interaction-design.org/references/authors/emiko_charbonneau.html), Emiko,[Bott](https://www.interaction-design.org/references/authors/jared_n__bott.html), Jared N. and [LaViola](https://www.interaction-design.org/references/authors/joseph_j__laviola.html), Joseph J. (2010): *The Wiimote and Beyond: Spatially Convenient Devices for 3D User Interfaces*. In [IEEE Computer Graphics and Applications](https://www.interaction-design.org/references/periodicals/ieee_computer_graphics_and_applications.html), 30 (2) pp. 71-85
[Zhai](https://www.interaction-design.org/references/authors/shumin_zhai.html), Shumin and [Milgram](https://www.interaction-design.org/references/authors/paul_milgram.html), Paul (1993): Human Performance Evaluation of Manipulation Schemes in Virtual Environments. In: [VR 1993](https://www.interaction-design.org/references/conferences/vr_1993.html) 1993. pp. 155-161
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

加入 **314,524 位设计师** 的行列，通过我们的时事通讯（Newsletter）获取实用的用户体验（User Experience, UX）技巧。
需要提供有效的电子邮件地址。

## 本书章节涵盖的主题：

[3D 用户界面（3D User Interfaces）](https://www.interaction-design.org/literature/topics/3d-user-interfaces)
[人机交互（Human-Computer Interaction, HCI）](https://www.interaction-design.org/literature/topics/human-computer-interaction)
[用户体验（User Experience, UX）设计](https://www.interaction-design.org/literature/topics/ux-design)
