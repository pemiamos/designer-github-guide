# 7. 双焦显示（Bifocal Display）

**来源**：The Encyclopedia of Human-Computer Interaction, 2nd Ed.
**Notion 原页面**：https://www.notion.so/c91ce21fa61b4d6389f8f4bdfde97cfb

---

 [Robert Spence](https://www.interaction-design.org/literature/author/robert-spence) 和 [Mark Apperley](https://www.interaction-design.org/literature/author/mark-apperley)
[双焦显示（Bifocal Display）](https://www.interaction-design.org/literature/topics/bifocal-display) 是一种信息呈现技术（information presentation technique），它允许用户将庞大的数据空间作为一个整体进行查看，同时能够以完整细节观察其中的一部分。细节部分是在概览的上下文（context）中呈现的，且在边界处保持连续，而非存在于一个离散的窗口中（见图 1）。

![](https://public-media.interaction-design.org/images/encyclopedia/bifocal_display/bifocal_display_world_map_distortion_visualization_focus_plus_context.jpg)
作者/版权持有者：Robert Spence 和 Prentice Hall。版权条款和许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。

**图 7.1**：伦敦地铁图的双焦表示法，显示中心区域的完整细节，同时保留整个网络的上下文。需要注意的是，尽管放大倍数不同，聚焦区域与上下文区域之间的线路依然保持连续。

William Farrand (Farrand 1973) 观察到，“有效的[数据]变换必须在提供细节的同时，以某种方式维持全局意识（global awareness）”，这反映了一个长期存在的问题，即用户需要感知上下文，以及“数据过多而屏幕太小”的问题。虽然地理学领域已经存在静态解决方案，但一种能够满足 Farrand 的要求且能维持信息空间（information space）连续性的交互式控制变换，由 Robert Spence (Imperial College London) 和 Mark Apperley (University of Waikato, New Zealand) 在 1980 年发明，并将其命名为“双焦显示（Bifocal Display）”。自此，该技术得到了实现、泛化、评估并被广泛应用。如今，双焦显示的概念在许多应用中得到了使用；例如，Mac OSX (Modine 2008) 操作系统中非常熟悉的、可伸缩的应用图标 Dock 栏（图 2）。

![](https://public-media.interaction-design.org/images/encyclopedia/bifocal_display/mac-osx-dock-bifocal-display.jpg)
作者/版权持有者：Apple Computer, Inc. 版权条款和许可：保留所有权利。根据公平使用原则（Fair Use Doctrine）在未获得许可的情况下使用（因为无法获得许可）。请参阅[版权声明](https://www.interaction-design.org/about/terms-of-use)页面上的“例外”部分（以及“allRightsReserved-UsedWithoutPermission”小节）。

**图 7.2**：双焦概念的一个非常熟悉的例子；2001 年发布的 Macintosh OSX 应用“Dock”栏。

作者/版权持有者：由 Rikke Friis Dam 和 Mads Soegaard 提供。版权条款和许可：CC-Att-ND (Creative Commons Attribution-NoDerivs 3.0 Unported)。
双焦显示简介

作者/版权持有者：由 Rikke Friis Dam 和 Mads Soegaard 提供。版权条款和许可：CC-Att-ND (Creative Commons Attribution-NoDerivs 3.0 Unported)。
主要指南与未来方向

作者/版权持有者：由 Rikke Friis Dam 和 Mads Soegaard 提供。版权条款和许可：CC-Att-ND (Creative Commons Attribution-NoDerivs 3.0 Unported)。
双焦显示是如何被发明和推出的

作者/版权持有者：Mark Apperley 和 Robert Spence。版权条款和许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。
1980 年的双焦显示概念视频

## 7.1 双焦点显示（Bifocal Display）详解

双焦点显示（Bifocal Display）的概念可以通过图 3、4 和 5 所示的物理类比来阐述。在图 3 中，我们看到一张代表信息空间（Information Space）的纸页，其中包含许多项目：例如文档、草图、电子邮件和手稿。如图 3 所示，信息空间可能过于庞大，无法通过一个窗口完整地查看，因此需要通过滚动来检查所有信息项。然而，如果将代表信息空间的纸页像图 4 那样包裹在两根立柱上，并将其两端以适当的角度倾斜，用户在图 5 中将能看到信息空间的一部分以其原始细节呈现，此外还能看到其余信息空间的“压缩视图（Squashed View）”。虽然压缩视图可能无法分辨细节，但通过适当的编码（Encoding）（例如颜色、垂直位置），用户可以解读出焦点区域（Focus Region）之外项目的存在及其*性质*。如果在上下文区域（Context Region）中注意到某个项目并认为其具有潜在价值，可以通过手动滚动整个信息空间，将该项目带入焦点区域以查看细节。

图 3、4 和 5 强调了信息空间的“拉伸（Stretching）”或“扭曲（Distorting）”是双焦点显示概念的核心。焦点区域与上下文区域之间信息空间的连续性（Continuity）是一项至关重要的特性，在地图表示（Map Representation）的语境下尤为具有价值（见下文）。

![](https://public-media.interaction-design.org/images/encyclopedia/bifocal_display/metaphor-of-the-bifocal-display_03.jpg)
作者/版权持有者：Courtesy of Mark D. Apperley and Robert Spence. 版权条款与许可：CC-Att-ND-3 (Creative Commons Attribution-NoDerivs 3.0 Unported).
**图 7.3**：包含文档、电子邮件等的信息空间。

![](https://public-media.interaction-design.org/images/encyclopedia/bifocal_display/metaphor-of-the-bifocal-display_07.jpg)
作者/版权持有者：Courtesy of Mark D. Apperley and Robert Spence. 版权条款与许可：CC-Att-ND-3 (Creative Commons Attribution-NoDerivs 3.0 Unported).
**图 7.4**：同一空间包裹在两根立柱上的样子。

![](https://public-media.interaction-design.org/images/encyclopedia/bifocal_display/metaphor-of-the-bifocal-display_09.jpg)
作者/版权持有者：Courtesy of Mark D. Apperley and Robert Spence. 版权条款与许可：CC-Att-ND-3 (Creative Commons Attribution-NoDerivs 3.0 Unported).
**图 7.5**：从适当方向观察时信息空间的外观。

在 1980 年发明后，双焦点显示的概念立即在一篇基于（首个！）设想视频（Envisionment Video）(Apperley and Spence 1980) 的新闻稿中得到了展示，该视频将其应用于一个未来主义办公室的场景中。1981 年，该概念被介绍给[办公自动化（Office Automation）](https://www.interaction-design.org/literature/topics/automation)领域的专家 (Apperley and Spence 1981a; Apperley and Spence 1981b)，而潜在实现的具体技术细节 (Apperley et al. 1982) 则在 1982 年进行了讨论，同年，一篇描述双焦点显示的正式期刊论文 (Spence and Apperley 1982) 也随之发表。

双焦点显示具有以下几个显著特点：

### 7.1.1 连续性（Continuity）

在双焦点表示（bifocal representation）中，焦点区域与上下文区域（context regions）之间的连续性（Continuity）是一个重要且强大的特性，它通过“拉伸（stretching）”或“扭曲（distorting）”信息空间的概念来实现。从形式上讲，为了使连续性可见，空间的变换在两个维度上必须是单调的（monotonic）（实际上是指在同一方向上移动）。事实上，拉伸的概念可以被推广。如果将图 5、6 和 7 中所示的拉伸称为 X 轴扭曲（X-distortion），那么在两个方向上进行拉伸（XY 轴扭曲，XY-distortion）在某些场景下会更有优势，例如日历（图 6）和地铁图（图 1）的显示：在这两种应用中，信息空间的连续性是一个显著的优势。“橡胶片拉伸（rubber-sheet stretching）”这一术语（Tobler 1973; Mackinlay et al. 1991; Sarkar et al. 1993）被认为能够简洁地解释焦点+上下文呈现（focus-plus-context presentations）在图形/拓扑扭曲（graphical/topological distortion）和连续性方面的特性。这种后者的灵活性可能导致了“鱼眼显示（fish-eye display）”一词被用作“双焦点显示（bifocal display）”的同义词。请注意，Ying Leung 和 Apperley 开发的分类法（taxonomy）（Leung and Apperley 1993a; Leung and Apperley 1993b）讨论了双焦点概念与鱼眼概念之间的关系和区别。

![](https://public-media.interaction-design.org/images/encyclopedia/bifocal_display/calendar-distortion-visualization.jpg)
作者/版权持有者：Courtesy of Bob Spence. 版权条款和许可：CC-Att-ND-3 (Creative Commons Attribution-NoDerivs 3.0 Unported).

**图 7.6**：X 轴和 Y 轴的组合扭曲提供了一个便捷的日历界面

### 7.1.2 细节抑制（Detail Suppression）

双焦点显示（bifocal display）的第二个重要特性是能够自定义项目在上下文区域（context region）中出现时的表征（representation），因为在这些区域中，精细的细节是不相关甚至是不合适的（例如，参见图 1 的伦敦地铁图，其中并未尝试在上下文区域中提供车站细节）。由 George Furnas (Furnas 1986) 随后正式提出的“感兴趣程度（degree of interest）”概念，例如可能会导致文本的抑制，并可能引入替代的 [视觉线索（visual cues）](https://www.interaction-design.org/literature/topics/visual-cues)（如形状和颜色），旨在使项目在上下文区域中更容易被区分。虽然双焦点概念主要被解释为一种呈现技术（presentation technique），但显而易见的是，通过利用焦点区域（focus region）和上下文区域中隐含的感兴趣程度，并对表征进行相应的变化，可以增强呈现的效果。

### 7.1.3 交互：滚动/平移（Interaction: scrolling/panning）

双焦点概念（Bifocal concept）的第三个特性涉及通过手动交互来实现滚动（scrolling）或平移（panning）。在设想视频（envisionment video, Apperley and Spence 1980）中，可以看到用户通过触控进行滚动，即时的视觉反馈确保了能够轻松地将所需项目定位在焦点区域（focus region）中（见图 7）。像触控那样真正的直接操纵（Direct Manipulation）对于在扭曲空间（distorted space）中实现可预测的[导航](https://www.interaction-design.org/literature/topics/navigation-1)至关重要，并且克服了通常与平移和缩放（panning and zooming）组合操作相关的尺度和速度问题（Guiard and Beaudouin-Lafon 2004）。多点触控界面（multi-touch interfaces）在这种交互中的影响和潜力将在稍后讨论。

![](https://public-media.interaction-design.org/images/encyclopedia/bifocal_display/bifocal-display-touch-interaction.jpg)
作者/版权持有者：Courtesy of Robert Spence, with the assistance of Colin Grimshaw of the Imperial College TV studio. 版权条款和许可：CC-Att-ND (Creative Commons Attribution-NoDerivs 3.0 Unported)
**图 7.7**：与双焦点显示器的[直接交互](https://www.interaction-design.org/literature/topics/direct-interaction)允许将特定项目或区域拖入焦点区域（摘自视频 5）

![](https://public-media.interaction-design.org/images/encyclopedia/bifocal_display/perspective_wall.jpg)
作者/版权持有者：Courtesy of Inxight Software, Inc (screenshot of Perspective Wall). 版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。
**图 7.8**：1991 年的 Perspective Wall 与双焦点显示器有许多共同之处。

![](https://public-media.interaction-design.org/images/encyclopedia/bifocal_display/neighbourhood-explorer.jpg)
作者/版权持有者：Courtesy of Mark D. Apperley and Robert Spence. 版权条款和许可：CC-Att-ND (Creative Commons Attribution-NoDerivs 3.0 Unported).
**图 7.9**：Neighbourhood Explorer (Spence 2001; Apperley et al. 2001)。在每个轴上距离目标对象较远的属性以细节较少的图标形式显示。

Apperley 和 Spence 及其同事随后的工作描述了双焦点显示器概念的泛化（generalizations）以及一个有用的分类法（taxonomy）（Leung and Apperley 1993a,b,c,d; Leung et al. 1995）。1991 年，一种被称为 Perspective Wall（图 8）的双焦点显示器的三维实现（three-dimensional realization）被提出（Mackinlay et al. 1991）。在 Neighbourhood Explorer（图 9）中，Apperley 和 Spence 将双焦点显示器概念应用于多轴表示（multi-axis representation）中的寻屋任务（home-finding）（Spence 2001, page 85; Apperley et al. 2001）。John Lamping 和 Ramana Rao (Lamping and Rao 1994) 描述了将双焦点概念有效地应用于层级结构数据（hierarchically structured data）交互的方法，他们采用了双曲变换（hyperbolic transformation）以确保从理论上讲，整个树结构都能映射到显示器上（图 10）。同年，Rao 和 Stuart Card (Rao and Card 1994) 描述了 Table Lens（图 12），该工具同样采用了拉伸（stretching）的概念。

![](https://public-media.interaction-design.org/images/encyclopedia/bifocal_display/hyperbolic-browser-representation-of-tree.jpg)
作者/版权持有者：Courtesy of Robert Spence. 版权条款和许可：CC-Att-ND (Creative Commons Attribution-NoDerivs 3.0 Unported).
**图 7.10**：双曲浏览器（hyperbolic browser）树形表示的草图[插图](https://www.interaction-design.org/literature/topics/illustration)。节点距离根节点（root node）越远，它就越靠近其上级节点（superordinate node），且其占据的区域越小（Spence 2001）。

![](https://public-media.interaction-design.org/images/encyclopedia/bifocal_display/continuity-detail-suppression-scrolling-panning-idelix.jpg)
作者/版权持有者：David Baar, IDELIX Software Inc. 版权条款和许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。
**图 7.11**：PDA 上的扭曲地图，显示了交通线路的连续性。

![](https://public-media.interaction-design.org/images/encyclopedia/bifocal_display/tablelens_visualizing_tabular_datasets_inxight.jpg)
作者/版权持有者：Courtesy of Inxight Software, Inc (screenshot of Table Lens). 版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。
**图 7.12**：Table Lens 的截图。Table Lens 在 X 轴和 Y 轴维度上都结合了拉伸概念，以提供焦点加上下文（focus plus context）（Rao and Card 1994）。

IDELIX 对实现双焦点显示器概念的软件进行了商业开发（commercial development），使该公司能够在多个应用中演示该概念。其中一个应用是通过适当的手动平移和可变拉伸（variable stretching）控制，在 PDA 有限的显示区域内检查波士顿地区的交通地图（图 11）；该应用采用了自动感兴趣程度调节（degree-of-interest adjustment）以充分利用可用显示区域。相比之下，另一个应用（图 13 和 14）采用了桌面显示器（table-top display），四名用户可同时独立控制地图不同区域的拉伸以检查细节。Ben Bederson, Aaron Clamage, Mary Czerwinski 和 George Robertson (Bederson et al 2004) 演示了双焦点显示器概念在用户与日历交互中的价值——见图 15。

在双焦点概念的一项医学应用中，大脑一部分的 3D 图像被扭曲，以聚焦于动脉瘤（aneurysm）周围区域，而周围的动脉网络则作为上下文（Cohen et al. 2005）——见图 16 和图 17。

![](https://public-media.interaction-design.org/images/encyclopedia/bifocal_display/continuity-detail-suppression-scrolling-panning-idelix-distorted-map.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。
**图 7.13**：桌面上的扭曲地图（2005 年）

![](https://public-media.interaction-design.org/images/encyclopedia/bifocal_display/continuity-detail-suppression-scrolling-panning-idelix-distorted-map-2.jpg)
作者/版权持有者：Clifton Forlines, Chia Shen, and Mitsubishi Electric Research Labs. 版权条款和许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。
**图 7.14**：桌面上的扭曲地图（2005 年）

![](https://public-media.interaction-design.org/images/encyclopedia/bifocal_display/bifocal-display-concept-pda-calendar-.jpg)
作者/版权持有者：Bederson et al. 版权条款和许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。
**图 7.15**：双焦点显示器概念在基于 PDA 的日历中的应用（Bederson et al. 2004）

![](https://public-media.interaction-design.org/images/encyclopedia/bifocal_display/bifocal_distortion_3d_medical_imaging_no_distortion.jpg)
作者/版权持有者：IEEE, Marcelo Cohen, Ken Brodlie, and Nick Phillips. 版权条款和许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。
**图 7.16**：未进行双焦点扭曲的大脑动脉瘤 3D 医学数据集（Cohen et al. 2005）

![](https://public-media.interaction-design.org/images/encyclopedia/bifocal_display/bifocal_distortion_3d_medical_imaging.jpg)
作者/版权持有者：IEEE, Marcelo Cohen, Ken Brodlie, and Nick Phillips. 版权条款和许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。
**图 7.17**：应用于该数据集的双焦点扭曲（Cohen et al. 2005）

## 7.2 未来展望

需要针对为什么以及在何种情况下，上下文意识（awareness of context）会特别有用，其背后的基础认知和感知原因进行研究，以便能够针对特定应用评估双焦点（Bifocal）、兴趣度（Degree-of-Interest）以及其他焦点+上下文（Focus+Context）技术（无论是单独使用还是协同使用）的潜力。多点触控屏幕（Multi-touch screens）及其相关的（极端）直接操纵（Direct Manipulation）的出现，为改进在大空间中导航的交互技术提供了巨大的机遇。多点触控显示器支持的单个手势结合平移-缩放（pan-zoom）操作，为双焦点概念的进一步开发和利用提供了令人兴奋的可能性 (Forlines and Shen 2005)。

## 7.3 更多学习资源

Bill Buxton 的书 (Buxton 2007) 中有一章专门讨论双焦点显示 (Bifocal Display)。双焦点概念在许多与人机交互 (Human-computer Interaction) 相关的文献中也有探讨，并采用了多种不同的索引词：畸变 (distortion) (Ware 2007)、双焦点显示 (bifocal display) (Spence 2007; Mazza 2009)，以及焦点+上下文 (focus+context) Tidwell (Tidwell 2005)。

## 7.4 视频

通过观看视频演示，可以更好地理解双焦点显示（Bifocal Display）的概念。以下是精选视频列表。

作者/版权持有者：未知（待调查）。版权条款与许可：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”章节。
双焦点显示（The Bifocal Display）

作者/版权持有者：Robert Spence。版权条款与许可：版权所有（All Rights Reserved）。经许可转载。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”章节。
双焦点显示（The Bifocal Display）

作者/版权持有者：IDELIX Software。版权条款与许可：版权所有（All Rights Reserved）。经许可转载。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”章节。
PDA 上的变形地图（Distorted map on a PDA）（52 秒，无声）

作者/版权持有者：Clifton Forlines, Chia Shen 以及 Mitsubishi Electric Research Labs。版权条款与许可：版权所有（All Rights Reserved）。经许可转载。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”章节。
桌上的可弯曲显示技术（Pliable display Technology）（3 分钟）

作者/版权持有者：IDELIX Software。版权条款与许可：版权所有（All Rights Reserved）。经许可转载。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”章节。
橡胶片地图变形（Rubber sheet map distortion）（33 秒，无声）

作者/版权持有者：Jock D. Mackinlay, George D. Robertson 以及 Stuart K. Card。版权条款与许可：版权所有（All Rights Reserved）。经许可转载。请参阅下方 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外（Exceptions）”章节。
透视墙（The Perspective Wall）（54 秒）

## 7.5 参考文献 (References)

[Apperley](https://www.interaction-design.org/references/authors/mark_apperley.html), Mark and [Leung](https://www.interaction-design.org/references/authors/y__k__leung.html), Y. K. (1993b): 数据呈现中面向失真技术（Distortion-oriented techniques）的分类学 (A taxonomy of distortion-oriented techniques for data presentation). In:[Salvendy](https://www.interaction-design.org/references/authors/gavriel_salvendy.html), Gavriel and [Smith](https://www.interaction-design.org/references/authors/m__j__smith.html), M. J. (eds.). "Advances in [Human Factors](https://www.interaction-design.org/literature/topics/human-factors)/Ergonomics Vol 19B, Human-Computer Interaction: Software and Hardware Interfaces". Amsterdam, Holland: Elsevier Science Publisherspp. 105-109
[Apperley](https://www.interaction-design.org/references/authors/mark_apperley.html), Mark and [Leung](https://www.interaction-design.org/references/authors/y__k__leung.html), Y. K. (1993a). *面向失真呈现技术的统一理论 (A Unified Theory of Distortion-Oriented Presentation Techniques)*. Massey University
[Apperley](https://www.interaction-design.org/references/authors/mark_apperley.html), Mark and [Spence](https://www.interaction-design.org/references/authors/robert_spence.html), Robert (1980). *视频：双焦点显示概念视频 (Video: bifocal display concept video)*. Retrieved 4 November 2013 from [https://www.interaction-design.org/tv/bifocal_displ...](https://www.interaction-design.org/tv/bifocal_display_concept_video.html)
[Apperley](https://www.interaction-design.org/references/authors/mark_apperley.html), Mark and [Spence](https://www.interaction-design.org/references/authors/robert_spence.html), Robert (1981): 使用双焦点显示器的专业人员界面 (A Professional's Interface Using the Bifocal Display). In: [Proceedings of the 1981 Office Automation Conference](https://www.interaction-design.org/references/conferences/proceedings_of_the_1981_office_automation_conference.html) 1981. pp. 313-315
[Apperley](https://www.interaction-design.org/references/authors/mark_apperley.html), Mark, [Spence](https://www.interaction-design.org/references/authors/robert_spence.html), Robert and [Wittenburg](https://www.interaction-design.org/references/authors/kent_wittenburg.html), Kent (2001): 从众多中择一：可扩展可视化工具的开发 (Selecting One from Many: The Development of a Scalable Visualization Tool). In: [HCC 2001 - IEEE CS International Symposium on Human-Centric Computing Languages and Environments ](https://www.interaction-design.org/references/conferences/hcc_2001_-_ieee_cs_international_symposium_on_human-centric_computing_languages_and_environments.html)September 5-7, 2001, Stresa, Italy. pp. 366-372
[Apperley](https://www.interaction-design.org/references/authors/mark_apperley.html), Mark, [Tzavaras](https://www.interaction-design.org/references/authors/i__tzavaras.html), I. and [Spence](https://www.interaction-design.org/references/authors/robert_spence.html), Robert (1982): 一种用于数据呈现的双焦点显示技术 (A Bifocal Display Technique for Data Presentation). In:[Eurographics 82 Proceedings](https://www.interaction-design.org/references/conferences/eurographics_82_proceedings.html) 1982, Amsterdam. pp. 27-43
[Bederson](https://www.interaction-design.org/references/authors/benjamin_b__bederson.html), Benjamin B., [Clamage](https://www.interaction-design.org/references/authors/aaron_clamage.html), Aaron, [Czerwinski](https://www.interaction-design.org/references/authors/mary_czerwinski.html), Mary and [Robertson](https://www.interaction-design.org/references/authors/george_g__robertson.html), George G. (2004): *DateLens：一种用于 PDA 的鱼眼日历界面 (DateLens: A fisheye calendar interface for PDAs)*. In [ACM Transactions on Computer-Human Interaction](https://www.interaction-design.org/references/periodicals/acm_transactions_on_computer-human_interaction.html), 11 (1) pp. 90-119
[Buxton](https://www.interaction-design.org/references/authors/bill_buxton.html), Bill (2007): [*绘制用户体验：确保设计正确且设计得恰到好处 (Sketching User Experiences: Getting the Design Right and the Right Design)*](https://www.interaction-design.org/literature/topics/sketching). Morgan Kaufmann
[Cohen](https://www.interaction-design.org/references/authors/marcelo_cohen.html), Marcelo, [Brodlie](https://www.interaction-design.org/references/authors/ken_brodlie.html), Ken and [Phillips](https://www.interaction-design.org/references/authors/nick_phillips.html), Nick (): 医学中用于体积可视化（Volume visualisation）的硬件加速失真 (Hardware-accelerated distortion for volume visualisation in medicine). In: [Proceedings of the 4th IEEE EMBSS UKRI PG Conference on Biomedical Engineering and Medical Physics 2005](https://www.interaction-design.org/references/conferences/proceedings_of_the_4th_ieee_embss_ukri_pg_conference_on_biomedical_engineering_and_medical_physics_2005.html) . pp. 29-30
[Farrand](https://www.interaction-design.org/references/authors/william_a__farrand.html), William A. (1973). *交互设计中的信息显示 (Information display in interactive design), 博士论文*. University of California at Los Angeles
[Forlines](https://www.interaction-design.org/references/authors/clifton_forlines.html), Clifton and [Shen](https://www.interaction-design.org/references/authors/chia_shen.html), Chia (2005): DTLens：多用户桌面空间数据探索 (DTLens: multi-user tabletop spatial data exploration). In: [Proceedings of the 2005 ACM Symposium on User Interface Software and Technology](https://www.interaction-design.org/references/conferences/proceedings_of_the_2005_acm_symposium_on_user_interface_software_and_technology.html) 2005. pp. 119-122
[Furnas](https://www.interaction-design.org/references/authors/george_w__furnas.html), George W. (1986): 广义鱼眼视图 (Generalized Fisheye Views). In: [Mantei](https://www.interaction-design.org/references/authors/marilyn_mantei.html), Marilyn and [Orbeton](https://www.interaction-design.org/references/authors/peter_orbeton.html), Peter (eds.) [Proceedings of the ACM CHI 86 Human Factors in Computing Systems Conference](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_86_human_factors_in_computing_systems_conference.html) April 13-17, 1986, Boston, Massachusetts. pp. 16-23
[Guiard](https://www.interaction-design.org/references/authors/yves_guiard.html), Yves and [Beaudouin-Lafon](https://www.interaction-design.org/references/authors/michel_beaudouin-lafon.html), Michel (2004): *多尺度电子世界中的目标获取 (Target acquisition in multiscale electronic worlds)*. In[International Journal of Human-Computer Studies](https://www.interaction-design.org/references/periodicals/international_journal_of_human-computer_studies.html), 61 (6) pp. 875-905
[Lamping](https://www.interaction-design.org/references/authors/john_lamping.html), John and [Rao](https://www.interaction-design.org/references/authors/ramana_rao.html), Ramana (1994): 使用双曲空间（Hyperbolic Space）布局和可视化大型树结构 (Laying Out and Visualizing Large Trees Using a Hyperbolic Space). In:[Szekely](https://www.interaction-design.org/references/authors/pedro_szekely.html), Pedro (ed.) [Proceedings of the 7th annual ACM symposium on User interface software and technology](https://www.interaction-design.org/references/conferences/proceedings_of_the_7th_annual_acm_symposium_on_user_interface_software_and_technology.html)November 02 - 04, 1994, Marina del Rey, California, United States. pp. 13-14
[Leung](https://www.interaction-design.org/references/authors/ying_k__leung.html), Ying K. and [Apperley](https://www.interaction-design.org/references/authors/mark_apperley.html), Mark (1993): E{cubed}：迈向大型数据集图形呈现技术的量化 (E{cubed}: Towards the Metrication of Graphical Presentation Techniques for Large Data Sets). In: [East-West International Conference on Human-Computer Interaction: Proceedings of the EWHCI93](https://www.interaction-design.org/references/conferences/east-west_international_conference_on_human-computer_interaction-_proceedings_of_the_ewhci93.html) 1993. pp. 9-26
[Leung](https://www.interaction-design.org/references/authors/ying_k__leung.html), Ying K. and [Apperley](https://www.interaction-design.org/references/authors/mark_apperley.html), Mark (1993): 扩展透视墙 (Extending the Perspective Wall). In: [Proceedings of OZCHI93, the CHISIG Annual Conference on Human-Computer Interaction](https://www.interaction-design.org/references/conferences/proceedings_of_ozchi93%2C_the_chisig_annual_conference_on_human-computer_interaction.html) 1993. pp. 110-120
[Leung](https://www.interaction-design.org/references/authors/y__w__leung.html), Y. W. and [Apperley](https://www.interaction-design.org/references/authors/mark_apperley.html), Mark (1994): *面向失真呈现技术的综述与分类学 (A Review and Taxonomy of Distortion-Oriented Presentation Techniques)*. In [ACM Transactions on Computer-Human Interaction](https://www.interaction-design.org/references/periodicals/acm_transactions_on_computer-human_interaction.html), 1 (2) pp. 126-160
[Leung](https://www.interaction-design.org/references/authors/ying_k__leung.html), Ying K., [Spence](https://www.interaction-design.org/references/authors/robert_spence.html), Robert and [Apperley](https://www.interaction-design.org/references/authors/mark_apperley.html), Mark (1995): *将双焦点显示器应用于拓扑地图 (Applying Bifocal Displays to Topological Maps)*. In[International Journal of Human-Computer Interaction](https://www.interaction-design.org/references/periodicals/international_journal_of_human-computer_interaction.html), 7 (1) pp. 79-98
[Mackinlay](https://www.interaction-design.org/references/authors/jock_d__mackinlay.html), Jock D., [Robertson](https://www.interaction-design.org/references/authors/george_g__robertson.html), George G. and [Card](https://www.interaction-design.org/references/authors/stuart_k__card.html), Stuart K. (1991): 透视墙：细节与上下文的平滑集成 (The Perspective Wall: Detail and Context Smoothly Integrated). In: [Robertson](https://www.interaction-design.org/references/authors/scott_p__robertson.html), Scott P., [Olson](https://www.interaction-design.org/references/authors/gary_m__olson.html), Gary M. and [Olson](https://www.interaction-design.org/references/authors/judith_s__olson.html), Judith S. (eds.) [Proceedings of the ACM CHI 91 Human Factors in Computing Systems Conference](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_91_human_factors_in_computing_systems_conference.html) April 28 - June 5, 1991, New Orleans, Louisiana. pp. 173-179
[Mazza](https://www.interaction-design.org/references/authors/riccardo_mazza.html), Riccardo (2009): *[信息可视化 (Information Visualization)](https://www.interaction-design.org/literature/topics/information-visualization) 导论 (Introduction to Information Visualization)*. Springer
[Modine](https://www.interaction-design.org/references/authors/austin_modine.html), Austin (2008). *苹果获得 OS X Dock 专利 (Apple patents OS X Dock)*. Retrieved 9 November 2010 from The Register: [http://www.theregister.co.uk/2008/10/08/apple_pate...](http://www.theregister.co.uk/2008/10/08/apple_patents_osx_dock/)
[Rao](https://www.interaction-design.org/references/authors/ramana_rao.html), Ramana and [Card](https://www.interaction-design.org/references/authors/stuart_k__card.html), Stuart K. (1994): Table Lens：在表格信息的交互式聚焦+上下文可视化（Focus+Context Visualization）中融合图形与符号表示 (The Table Lens: Merging Graphical and Symbolic Representations in an Interactive Focus+Context Visualization for Tabular Information). In: [Adelson](https://www.interaction-design.org/references/authors/beth_adelson.html), Beth, [Dumais](https://www.interaction-design.org/references/authors/susan_dumais.html), Susan and [Olson](https://www.interaction-design.org/references/authors/judith_s__olson.html), Judith S. (eds.) [Proceedings of the ACM CHI 94 Human Factors in Computing Systems Conference](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_94_human_factors_in_computing_systems_conference.html) April 24-28, 1994, Boston, Massachusetts. pp. 318-322
[Sarkar](https://www.interaction-design.org/references/authors/manojit_sarkar.html), Manojit, [Snibbe](https://www.interaction-design.org/references/authors/scott_s__snibbe.html), Scott S., [Tversky](https://www.interaction-design.org/references/authors/oren_j__tversky.html), Oren J. and [Reiss](https://www.interaction-design.org/references/authors/steven_p__reiss.html), Steven P. (1993): 拉伸橡胶片：在小屏幕上可视化大型布局的一种隐喻 (Stretching the Rubber Sheet: A Metaphor for Visualizing Large Layouts on Small Screens). In: [Hudson](https://www.interaction-design.org/references/authors/scott_e__hudson.html), Scott E., [Pausch](https://www.interaction-design.org/references/authors/randy_pausch.html), Randy, [Zanden](https://www.interaction-design.org/references/authors/brad_vander_zanden.html), Brad Vander and [Foley](https://www.interaction-design.org/references/authors/james_d__foley.html), James D. (eds.) [Proceedings of the 6th annual ACM symposium on User interface software and technology](https://www.interaction-design.org/references/conferences/proceedings_of_the_6th_annual_acm_symposium_on_user_interface_software_and_technology.html) 1993, Atlanta, Georgia, United States. pp. 81-91
[Spence](https://www.interaction-design.org/references/authors/robert_spence.html), Robert (2007): *信息可视化：交互设计 (Information Visualization: Design for Interaction) (第 2 版)*. Prentice Hall
[Spence](https://www.interaction-design.org/references/authors/robert_spence.html), Robert (2001): *信息可视化 (Information Visualization)*. Addison Wesley
[Spence](https://www.interaction-design.org/references/authors/robert_spence.html), Robert and [Apperley](https://www.interaction-design.org/references/authors/mark_apperley.html), Mark (1982): *数据库导航：面向专业人员的办公环境 (Data Base Navigation: An Office Environment for the Professional)*. In[Behaviour and Information Technology](https://www.interaction-design.org/references/periodicals/behaviour_and_information_technology.html), 1 (1) pp. 43-54
[Tidwell](https://www.interaction-design.org/references/authors/jenifer_tidwell.html), Jenifer (2005): *界面设计：高效[交互设计 (Interaction Design)](https://www.interaction-design.org/literature/topics/interaction-design) 的模式 (Designing Interfaces: Patterns for Effective Interaction Design)*. O'Reilly and Associates
[Tobler](https://www.interaction-design.org/references/authors/w__r__tobler.html), W. R. (1973): *一种用于分区划分的连续变换 (A continuous transformation useful for districting)*. In [Annals of the New York Academy of Sciences](https://www.interaction-design.org/references/periodicals/annals_of_the_new_york_academy_of_sciences.html), 219 p. 215–220
[Ware](https://www.interaction-design.org/references/authors/colin_ware.html), Colin (2004): *信息可视化：面向[感知 (Perception)](https://www.interaction-design.org/literature/topics/perception) 的设计 (Information Visualization: Perception for Design), 第 2 版*. San Francisco, Morgan Kaufman

**章节目录 (Chapter TOC)**
[**人机交互：UX 设计基础 (Human-Computer Interaction: The Foundations of UX Design)**](https://www.interaction-design.org/courses/hci-foundations-of-ux-design)
![](https://public-media.interaction-design.org/images/courses/hds/course_72--square_thumbnail.jpg?tr=fo-auto)
人机交互：UX 设计基础 (Human-Computer Interaction: The Foundations of UX Design)
将在 10 天后关闭
已预约
查看课程

## 获取每周用户体验洞察（UX Insights）

加入 **314,536 位设计师** 的行列，通过我们的时事通讯（newsletter）获取实用的 UX 技巧。
需要提供有效的电子邮件地址。

# 7.5 Stuart K. Card 的评述（Commentary）

### 7.5.0.1 焦点+上下文显示的设计空间（The Design Space of Focus + Context Displays）

Robert Spence 和 Mark Apperley 在介绍双焦点显示（Bifocal display）及其后续探索方面做了出色的工作。在本评论中，我想阐明已经形成的设计空间结构并捕捉其中的一些抽象概念。随后，我想就我们从焦点+上下文（Focus + Context）显示中学到了什么提出一些推测。

双焦点显示旨在解决一个通用问题：世界提供的信息量超过了人类在有限的处理带宽下所能处理的极限。Resnikoff (1987) 提出的“信息的选择性省略与重编码（selective omission and recoding of information）”原则为该问题提供了一个务实的解决方案——即忽略部分信息，同时将其他信息重新编码为更紧凑、更标准化的形式。双焦点显示正是这一原则的体现，它将信息分为两部分：一个宽泛但简化的*上下文概览部分（contextual overview part）*和一个狭窄但详细的*焦点部分（focal part）*。在上下文概览部分中，详细信息被忽略或被重编码为简化的视觉形式；而在焦点部分中，则包含更多细节，甚至可能经过增强。这大致模拟了人类感知系统的策略，该系统实际上采用了由视网膜（retina）、黄斑中心凹（fovea）和周边视觉（periphery）组成的三级分层组织，以在感知视觉环境时，在对高空间分辨率和宽视野（wide aperture）的冲突需求之间分配有限的带宽（Resnikoff, 1987）。周边视觉捕捉到的视觉特征（例如，某个移动的物体）会引导可定向的高分辨率黄斑中心凹/视网膜以及注意力转向该感兴趣区域，从而将其解析（例如，解析为一只正在冲过来的狮子）。

Imperial College London 的 Spence 和 Apperley 认为，这种焦点+上下文的原则不仅可以应用于感知主体，也可以应用于数据本身的显示。Spence 和 Apperley 面对的具体问题是如何组织电子工作区（electronic workspace）的动态可视化。在他们的解决方案中，焦点部分的文档或期刊文章以详细形式呈现，而上下文部分的文档则被缩短或以其他方式聚合，以占用更少的空间并显示更少的细节（图 7.1）。显示的详细部分可以围绕上下文区域中的不同位置重新聚焦，使其成为新的焦点。Spence 和 Apperley 的方法为有限屏幕空间的使用提供了一种动态解决方案，这让人联想到双焦点眼镜的动态特性，因此得名*双焦点显示（bifocal display）*。他们的贡献在于提出了双焦点显示的概念模型，阐明了如何通过该技术使工作区在效果上变得更大且更高效，以及如何将此技术应用于更广泛的任务。该技术的首次记录是一段拍摄于 1980 年 12 月（1981 年 1 月编辑）的概念视频。随后，相关记录在 1982 年的一篇期刊论文中发表（Spence and Apperley, 1982）。

![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/metaphor-of-the-bifocal-display_03.jpg)
Courtesy of Mark D. Apperley and Robert Spence. 
Copyright: CC-Att-ND-3 (Creative Commons Attribution-NoDerivs 3.0 
Unported).
![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/metaphor-of-the-bifocal-display_09.jpg)
Courtesy of Mark D. Apperley and Robert Spence. 
Copyright: CC-Att-ND-3 (Creative Commons Attribution-NoDerivs 3.0 
Unported).
图 7.1 A-B：应用于桌面工作区的双焦点显示（摘自 Spence and Apperley 论文的图 7.3 和 7.5）。a) 工作区 b) 工作区的双焦点表示

大约在同一时间，Bell Labs 的 George Furnas 提出了一个相关的想法。Furnas 面对的具体问题是如何访问长计算机程序列表中的语句。程序员需要能够在上下文中查看代码行，例如，变量声明可能在代码当前关注点之前的好几页之前。他注意到，在日常生活中可以找到针对这一问题的有趣响应。一个著名的例子是 *New Yorker Magazine* 封面上的 Steinberg 漫画，它展示了一个纽约人对第 9 大道的感知：细节随着与第 9 大道距离的增加而减少，但对于拉斯维加斯以及其他几个对第 9 大道纽约人感兴趣的地点，其细节却比预期要丰富。另一个生活中的例子是照相机的鱼眼镜头（fisheye lens），它会对中心图像进行扭曲放大，而对图像边缘进行缩小渲染。Furnas 的贡献是发明了一种计算性的感兴趣程度（Degree-of-Interest, DOI）函数，用于动态分配用户对数据结构不同部分的相对兴趣程度。随后，他能够使用 DOI 函数将信息划分为更偏向焦点和更偏向周边的部分。他的函数包含两项：一项表示某事物的内在重要性，另一项表示与关注点距离的影响。在许多情况下，该函数似乎创造了一种自然的信息压缩方式。例如，图 7.2（摘自他 1982 年的原始备忘录）展示了当用户焦点在第 39 行时的计算机程序片段。在计算程序每行的 DOI 函数值后，DOI 低于阈值的行被过滤掉，从而产生了图 7.3 中更紧凑的*鱼眼视图（fisheye view）*。

鱼眼视图版本更好地利用了程序列表的空间。它将此时对程序员高度相关的信息引入列表空间，例如 `includes` 语句、变量声明语句、控制 `while` 循环语句和条件语句。它通过省略此时与程序员无关的细节（例如某些 `case` 语句）来为这些信息腾出空间。该技术的首次记录是 1982 年 10 月的一份 Bell Labs 内部备忘录（Furnas, 1982），当时在研究社区广泛传阅，但直到 1999 年才正式发表（Furnas, 1982/1999）。第一篇正式发表的论文是 (Furnas G., 1986)。

```plain text
   28 			t[0] = (t[0] + 10000)
   29 				   - x[0];
   30 			for(i=1;i<k;i++){
   31 			t[i] = (t[i] + 10000)
   32 				   - x[i]
   33 				   - (1 - t[i-1]/10000);
   34 			t[i-1] %= 10000;
   35 			}
   36 			t[k-1] %= 10000;
   37 			break;
   38 		case 'e':
 >>39			for(i=0;i<k;i++) t[i] = x[i];
   40 			break;
   41 		case 'q':
   42 			exit(0);
   43 		default:
   44 			noprint = 1;
   45 			break;
   46 	}
   47 	if(!noprint){
   48 		for(i=k - 1;t[i] <= 0 && i &rt; 0;i--);
   49 		printf("%d",t[i]);
   50 		if(i &rt; 0) {

```
图 7.2：应用鱼眼视图之前的程序列表片段。程序列表的鱼眼视图。第 39 行（红色）为焦点。

```plain text
   1 #define DIG 40
   2 #include
...4 main()
   5 {
   6      int c, i, x[DIG/4], t[DIG/4], k = DIG/4, noprint = 0;
...8      while((c=getchar()) != EOF){
   9           if(c >= '0' && c <= '9'){
...16           } else {
   17                switch(c){
   18                     case '+':
...27                     case '-':
...38                    case 'e':
 >>39                         for(i=0;i<k;i++) t[i] = x[i];
   40                          break;
   41                     case 'q':
...43                     default:
...46                }
   47                if(!noprint){
...57               }
   58           }
   59           noprint = 0;
   60      }
   61 }


```
图 7.3：C 程序的鱼眼视图。行号在左边距。 “...” 表示缺失的行。请注意，变量声明和 `while` 循环初始化现在在同一页上。第 39 行（红色）为焦点。

将双焦点显示或鱼眼视图与另一种访问上下文和焦点信息的方法——*概览+细节（Overview + Detail）*进行对比会很有帮助。图 7.4 将 Spence 和 Apperley 双焦点显示的数据以概览+细节显示的方式呈现。概览+细节的优点是简单直接；缺点是需要眼睛在两个不同的显示区域之间来回移动。双焦点显示本质上是寻求将细节显示拟合在上下文显示之中，从而避免这种协调工作及其隐含的视觉搜索。

![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image5.jpg)
Copyright status: Unknown (pending investigation). See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image8.jpg)
Copyright status: Unknown (pending investigation). See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
图 7.4 A-B：概览+细节显示。a) 概览 b) 细节

尽管最初被命名为“双焦点显示”或“鱼眼视图”，但源自这些开创性论文的一系列技术（无论是作者本人还是他人开发的）已经远远超出了鱼眼所暗示的视觉变换，也超出了双焦点所暗示的两级表示。这些显示方式可以被称为*注意力感知显示（Attention-aware displays）*，因为它们利用用户注意力的代理（proxies）来动态重新分配显示空间和细节。在实际操作中，我将这一通用类别称为*焦点+上下文技术（Focus + Context techniques）*，以强调其在视觉之外与用户注意力的联系，并避免重复使用“双焦点显示或鱼眼视图”这一措辞。

### 7.5.0.2 作为可视化变换的聚焦+上下文显示（Focus + Context Displays as Visualization Transformations）

聚焦+上下文（Focus + context）技术本质上是动态的，这引导我们将信息显示视为空间 $\times$ 时间 $\times$ 表示变换（representation transformations）。可用的表示类别可以通过图 7.5 所示的 *信息可视化参考模型（information visualization reference model）*（Card, Mackinlay, & Shneiderman, 1999）来理解。该框架追踪了从原始数据到可视化的路径：数据首先被转换为归一化形式（normalized form），然后映射到视觉结构（visual structures），最后再重新映射为衍生视觉形式（derivative visual forms）。图中的下方箭头描绘了信息可视化是动态的这一事实。用户可以修改其当前所见可视化的变换参数。

![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image3.jpg)
版权状态：未知（待调查）。详见下文 [版权条款](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) 中的“例外”部分。
图 7.5：信息可视化参考模型（Card, Mackinlay, and Shneiderman, 1999）

聚焦+上下文显示混合了信息可视化参考模型中两种变换的效果：*视图变换（view transformations）*和*视觉映射（visual mappings）*。
视图变换使用一种从空间到空间的映射，以某种方式扭曲可视化结果。其中一些变换可以用*视觉传输函数（visual transfer function）*来便捷地描述，以实现聚焦+上下文效果。双焦点显示（bifocal display）是其中最早出现的技术，并启发了后续的工作。

视觉映射关注的是从数据到视觉表示的映射，包括过滤掉较低层级的细节。关于过滤的视觉映射设计空间，通常可以用应用于数据结构或内容的*感兴趣程度函数（degree-of-interest functions）*的选择，以及如何使用这些函数来过滤细节层次（level of detail）来便捷地描述。这也启发了后续的工作。

然而，这种在几何导向技术（如双焦点显示）与数据导向的细节层次过滤/感兴趣程度技术之间的便捷的历史关联，无论在分析上还是在历史上，都未能触及这些技术的本质。即使在最初的论文中，Spence 和 Apperley 也不仅仅是应用几何变换，他们还意识到在显示的上下文部分和聚焦部分改变数据表示的优势，正如其原论文中的图 6 所示：显示中上下文部分的月份简单表示被扩展为聚焦部分中每日预约的详细表示。相反，Furnas 在关于鱼眼视图（fisheye view）的第一份备忘录中，就包含了一个关于“欧几里得空间的鱼眼视图”的章节，因此他也理解其技术在视觉变换中的潜在用途。这些技术并未穷尽动态聚焦+上下文映射的所有可能性。

![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/calendar-distortion-visualization.jpg)
courtesy of Bob Spence. 版权：CC-Att-ND-3 (Creative Commons Attribution-NoDerivs 3.0 Unported).
图 7.6：双焦点显示语义表示变更示例（源自 Spence and Apperley 的图 7.6）。

双焦点显示和鱼眼视图的本质在于，视图变换和视觉映射变换能够主动且持续地改变显示中的细节位置（locus of detail），以支持当前的任务。各种可能变换的组合为聚焦+上下文显示生成了一个设计空间。为了体会由 Spence & Apperley 以及 Furnas 的开创性思想所产生的这一设计空间的丰富性，我们将探讨视觉传输函数和感兴趣程度函数的几种参数化变体。

### 7.5.0.3 将视图变换视为视觉传递函数

视图变换（View Transformations）改变了空间的几何结构。双焦点显示（Bifocal Display）工作区具有两个放大级别，如图 7.7.B 所示。根据代表这两个放大级别的函数，我们可以推导出图 7.7.C 中的视觉传递函数（Visual Transfer Function），该函数展示了图像中的点是如何被变换的。放大函数中两个恒定的放大级别（一个用于外围上下文区域 Peripheral Context Region，另一个用于焦点区域 Focal Region）产生了一个视觉传递函数（本质上是放大函数的积分）。将此变换应用于原图（图 7.7.A）的结果即为图 7.7.D 所示的图像，其两侧被透视缩短（Foreshortening）。

![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/metaphor-of-the-bifocal-display_03.jpg)
Courtesy of Mark D. Apperley and Robert Spence. 
Copyright: CC-Att-ND-3 (Creative Commons Attribution-NoDerivs 3.0 
Unported).
![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image6.jpg)
Courtesy of Stuart Card. Copyright: CC-Att-SA-3 (Creative Commons Attribution-ShareAlike 3.0).
![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image7.jpg)
Courtesy of Stuart Card. Copyright: CC-Att-SA-3 (Creative Commons Attribution-ShareAlike 3.0).
![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/metaphor-of-the-bifocal-display_09.jpg)
Courtesy of Mark D. Apperley and Robert Spence. 
Copyright: CC-Att-ND-3 (Creative Commons Attribution-NoDerivs 3.0 
Unported).
图 7.7 A-B-C-D：双焦点显示的视觉传递函数：(a) 原始图像 (b) 放大函数 (c) 视觉传递函数 (d) 变换后的工作区

*橡胶几何：替代性的视觉传递函数（Rubber Geometry: Alternate Visual Transfer Functions）。* 显然，视觉传递函数可以被泛化，以提供许多替代的“焦点+上下文（Focus + Context）”显示方式。Leung and Apperley (1994) 很早就意识到，视觉传递函数是对这类显示方式的多种变体进行分类的一种有效方法，并付诸实践。具有讽刺意味的是，Leung and Apperley (1994) 最早处理的函数之一是真实的（光学）鱼眼镜头（Fisheye Lens）的视觉传递函数，而此前 Furnas (1982) 讨论该镜头大多是基于隐喻的。鱼眼放大函数（图 7.8.A）及其产生的视觉传递函数（图 7.8.B）导致了图 7.8.C 中的变换工作区，图中通过展示网格线的畸变来对其进行描述。

![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image9.jpg)
Copyright © Mark Apperley, Ying Leung. All 
Rights Reserved. Reproduced with permission. See section "Exceptions" in
 the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image10.jpg)
Copyright © Mark Apperley, Ying Leung. All 
Rights Reserved. Reproduced with permission. See section "Exceptions" in
 the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image11.jpg)
Copyright © Mark Apperley, Ying Leung. All 
Rights Reserved. Reproduced with permission. See section "Exceptions" in
 the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
图 7.8 A-B-C：鱼眼镜头的视觉传递函数 (Leung and Apperley, 1994)：(a) 放大函数 (b) 视觉传递函数 (c) 变换后的工作区

请注意，在图 7.8.A 中，放大级别不再仅仅是两个，而是一个连续函数。同时请注意，图 7.7.C 描述的是一维函数，而图 7.8.B 则是二维函数的简写，这在图 7.8.B 中显而易见。

视觉传递函数可以采取多种形式。其中一个有趣的子集被称为橡胶片传递函数（Rubber Sheet Transfer Functions），之所以如此命名，是因为它们看起来就像是在拉伸一张连续的橡胶片。图 7.9 展示了其中的几种。

![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image12.jpg)
Copyright © Sheelagh Carpendale. All Rights 
Reserved. Reproduced with permission. See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image13.jpg)
Copyright © Sheelagh Carpendale. All Rights 
Reserved. Reproduced with permission. See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image14.jpg)
Copyright © Sheelagh Carpendale. All Rights 
Reserved. Reproduced with permission. See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
图 7.9 A-B-C：橡胶片视觉变换函数 (Carpendale, 2001)。(a) 高斯传递函数 (b) 余弦传递函数 (c) 线性传递函数

*自然透视视觉传递函数（Natural Perspective Visual Transfer Functions）。* 橡胶片视觉传递函数的一个问题是，其畸变可能较为难以解读，如图 7.10.A（原图）到图 7.10.B（变换图）的映射所示，尽管可以通过在视觉传递函数的中心设置一个平坦区域来减轻这一问题。

![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image15.jpg)
Copyright © Sheelagh Carpendale. All Rights 
Reserved. Reproduced with permission. See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image16.jpg)
Copyright © Sheelagh Carpendale. All Rights 
Reserved. Reproduced with permission. See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
图 7.10 A-B：某些视觉传递函数引起的畸变示例 (Carpendale, 2006/2012)。(a) 原始图像 (b) 变换后的图像

一个有趣的替代方案是使用自然透视视觉传递函数。这些函数实现了两个区域之间所需的放大对比度，但巧妙之处在于显示效果看起来并不畸变。透视墙（Perspective Wall，图 7.11.C）就是这样一种显示方式。从放大函数（图 7.11.A）可以看出，放大函数的一部分是平坦的，从而解决了畸变问题，但侧边的部分是弯曲的。然而，弯曲的侧边看起来并不畸变，因为该曲线符合自然透视，因此能被观察者的感知系统有效地抵消（尽管比较判断仍可能受到不利影响）。触摸侧边面板上的某个元素，会导致被触摸的“带状”部分滑动到前方，从而实现图 7.11.A 中放大函数的放大效果，并将上下文信息移动到焦点位置。关键在于，通过使用自然透视视觉传递函数，我们获得了“焦点+上下文”显示的节省空间特性，但用户不会将其视为畸变，而会觉得它是自然的。

![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image17.jpg)
Copyright © Mark Apperley, Ying Leung. All 
Rights Reserved. Reproduced with permission. See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image18.jpg)
Copyright © Mark Apperley, Ying Leung. All 
Rights Reserved. Reproduced with permission. See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image19.jpg)
Copyright © Jock Mackinlay, George Robertson, 
Stuart Card. All Rights Reserved. Reproduced with permission. See 
section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
图 7.11 A-B-C：透视墙 (Mackinlay, Robertson, and Card, 1991)：(a) 放大函数 (b) 视觉传递函数 (c) 变换后的工作区

*三维视觉传递函数（Three-Dimensional Visual Transfer Functions）。* 透视墙引入了另一种变化元素：视觉传递函数可以是三维的。图 7.12 展示了另一种此类可视化方式——文档透镜（Document Lens, Robertson & Mackinlay, 1993）。文档透镜用于书籍或报告 (Card, Robertson, & York, 1996)。用户命令书籍将其转换为所有页面的网格。搜索会点亮所有感兴趣的短语，并明确哪些页面最值得详细查看。随后用户伸手将某些页面向前拉出，结果如图 7.12 所示。

尽管用户在详细区域阅读一页（或一组页面），但所有页面作为上下文仍然可见。此外，由于这是一种感知变换，上下文页面不会被感知为畸变。

![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image20.jpg)
Copyright status: Unknown (pending investigation). See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
图 7.12：文档透镜 (Robertson and Mackinlay, 1993)

自然透视视觉传递函数几乎可以无缝地融入强有力的视觉隐喻中，因此可以用来产生“焦点+上下文”效果，而不会将其作为一种独立的视觉化方式而吸引注意力。图 7.13.A 展示了 3Book (Card, Hong and Mackinlay, 2004)，这是一款 3D 电子书。屏幕上没有空间显示打开的双页书，因此视图缩放到了左上页（焦点），而右页向后弯曲但未完全弯曲，因此其内容仍然可见（上下文）。读者可以看到右页上有一幅插图，点击该插图会使书籍摇摆到图 7.13.B 所示的位置，从而使右页成为焦点，左页成为上下文。通过这种方式，摇摆页（Rocker Page）焦点+上下文技术能够在适应可用空间资源的同时，为读者保留更多的上下文。

![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image21.jpg)
Copyright © Stuart Card, Lichen Hong, Jock 
Mackinlay. All Rights Reserved. Reproduced with permission. See section 
"Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image22.jpg)
Copyright © Stuart Card, Lichen Hong, Jock 
Mackinlay. All Rights Reserved. Reproduced with permission. See section 
"Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
图 7.13 A-B：书籍中使用摇摆页焦点+上下文效果 (Card, Hong, and Mackinlay, 2004)：(a) 左页为焦点。右页部分向后弯曲，形成上下文。(b) 书籍摇摆导致左页变为上下文，右页变为焦点

*双曲视觉传递函数（Hyperbolic Visual Transfer Functions）。* 一种被尝试过的特别有趣的视觉传递函数是双曲映射（Hyperbolic Mapping）。通过双曲函数，可以通过缩小投影图表的尺寸空间，来补偿图表的指数级增长。这是因为无限的双曲空间可以被投影到欧几里得空间（Euclidean Space）的一个有限部分中。与所有“焦点+上下文”技术一样，作为焦点的图表部分可以移动，并相应地调整尺寸。图 7.14 展示了双曲视觉传递函数的示例。图 7.14.A 是图 7.9 的双曲等效形式。图 7.14.B 展示了一个双曲树 (Lamping, Rao, and Pirolli, 1995)。请注意，当空间足够大时，节点如何被重新表示为小型文档。图 7.14.C 给出了一个 3D 版本 (Munzner & Burchard, 1995; Munzner, 1998)。有趣的是，图 7.14.D 展示了如何使用更极端的双曲投影（在这种情况下，是通过精巧的编织构建的，Tallmina, 1997）将这一想法进一步延伸，它可以作为图 7.14.B 或 7.14.C 中树结构的替代基质。

![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image12.jpg)
Copyright © Sheelagh Carpendale. All Rights 
Reserved. Reproduced with permission. See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image24.jpg)
Copyright © . All Rights Reserved. Reproduced with permission. See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image25.jpg)
Copyright © Tamara Munzner Paul Burchard. All 
Rights Reserved. Reproduced with permission. See section "Exceptions" in
 the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image26.jpg)
Copyright © Daina Taimina. All Rights Reserved. 
Reproduced with permission. See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
图 7.14 A-B-C-D：双曲视觉传递函数：(a) 双曲视觉变换函数 (Carpendale, 2001)。(b) 双曲树 (Lamping, Rao, and Pirolli, 1995) (c) 3D 双曲 (Munzner and Burchard, 1995; Munzner, 1998)。(d) 3D 双曲曲面 (Tallmina, 1997)

*复杂视觉传递函数（Complex Visual Transfer Functions）。* 一些视觉传递函数甚至更加复杂。图 7.15 展示了一个以 3D 圆锥树（Cone Tree, Robertson, Mackinlay, & Card, 1991）形式可视化的树，其中每个节点下方都有一个中空的、3D 的、可旋转的节点圆环。图 7.15.A 展示了一个倾斜放置的小型树，图 7.15.B 展示了一个从侧面看到的更大规模的树。触摸这些树中的一个元素，会导致该树中持有标签的圆环以及所有上层圆环向用户旋转。结果是，用户能够阅读兴趣点周围的标签，而自然透视和遮挡（Occlusion）会将树的背景节点更多地推入上下文。该视觉变换利用透视和遮挡来达到“焦点+上下文”的效果。从焦点到上下文的切换完全是通过几何视图变换完成的，但这些变换不再能被描述为图 7.1.C 那种简单的视觉传递。

![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image27.jpg)
Copyright © Stuart Card, George Robertson, Jock 
Mackinlay. All Rights Reserved. Reproduced with permission. See section 
"Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image28.jpg)
Copyright © Stuart Card, George Robertson, Jock 
Mackinlay. All Rights Reserved. Reproduced with permission. See section 
"Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
图 7.15 A-B：圆锥树：(b) 从侧面看的大型圆锥树。(a) 展示透视的小型圆锥树。

### 7.5.0.4 作为视觉映射变换的兴趣度函数

与视图变换（view transforms）不同，视觉映射变换（visual mapping transforms）利用数据的内容来生成物理形式。兴趣度（Degree-of-Interest, DOI）函数为数据的每个部分分配一个对用户的瞬时相关性估计值。该值随后被用于动态地修改显示效果。假设我们有一个取自 Roget’s Thesaurus 的类别树，并且我们正在与其中一个类别“Hardness”进行交互（图 7.16.A）。在焦点位于节点 **Hardness** 的情况下，我们为树中的每个项目计算一个兴趣度（DOI）。

为了实现这一点，我们将 DOI 分为内在部分和随当前兴趣中心距离而变化的部分，并采用了 Furnas (1982) 的公式。通过使用 DOI 函数，原始树可以被折叠成一个小得多的树（图 7.16.B），从而保留焦点及其相关的上下文部分。结果树的紧凑程度取决于一个兴趣阈值函数（interest threshold function）。该阈值可以是一个固定数值，也可以是可变的，以便结果树能够适应一个固定大小的矩形。通过这种方式，DOI 树可以获得用户界面中一个重要的属性——空间模块化（spatial modularity）。它们可以被分配屏幕资源中的特定大小区域，并被限制在该空间内运行。

| Matter
   ORGANIC vitality
      Vitality in general
      Specific vitality
         Sensation in general
         Specific sensation
INORGANIC Solid
   **Hardness**
   Softness
      Fluid
         Fluid in general
         Specific fluid
 | Matter
   ORGANIC vitality
   INORGANIC solid
      **Hardness**
      Softness
         Fluid
 |
|---|---|
| *(a) 来自 Roget’s Thesaurus 的类别。* | *(b) 当兴趣点集中在类别 ****Hardness**** 时，类别的鱼眼视图（Fisheye view）。* |
Figure 7.16: 使用兴趣度函数进行过滤

当然，这只是一个用于演示的小例子。代表程序列表、计算机目录或分类法的树很容易拥有数千行；这个数量将大大超过显示屏能够容纳的范围。

*DOI* = *内在兴趣度 (Intrinsic DOI)* + *距离兴趣度 (Distance DOI)*

图 7.17 示意性地展示了如何为我们的示例执行此计算。向上箭头表示预设的兴趣点。我们假设节点的内在 DOI 仅为其到根节点的距离（图 7.17.A）。DOI 的距离部分则是从当前焦点节点到该节点的遍历距离（图 7.17.B）；在这种计算中使用负数被证明是非常方便的，这样最大兴趣量是有界的，而最小兴趣量则不受限。我们将这两个数值相加（图 7.17.C），从而获得树中每个节点的 DOI。然后，我们应用一个最小兴趣阈值，仅显示比该阈值更具“兴趣”的节点。结果即为图 7.17.D 中的简化树。这就是图 7.16.D 背后的计算方式。

简化树提供了焦点节点周围的局部上下文，并且随着距离的增加，细节逐渐减少。但它确实提供了重要的上下文信息。

![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image29.jpg)
Copyright © Stuart Card, Ben Shneiderman, 
Morgan-Kaufmann, Jock Mackinlay. All Rights Reserved. Reproduced with 
permission. See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
Figure 7.17: 树的兴趣度计算。(a) 内在兴趣函数。(b) 距离函数。(c) (a) 与 (b) 之和。(d) 对 (c) 应用基于阈值的过滤函数。

*基于兴趣度函数的多焦点细节水平过滤（Level-of-Detail Filtering）。* 图 7.18 将这些计算的一个版本应用于一个包含超过 600,000 个节点且具有多个兴趣焦点的树。这证明了通过将缓存机制与 DOI 计算相结合，可以在极短的时间内对极大型的树进行计算，从而允许将 DOI 树作为动画界面的组件，用于显示大型数据集的上下文相关且经过细节过滤的视图，使其能够适应屏幕。如果我们假设该技术至少能处理一百万个节点，且一次屏幕显示约 50 个节点，那么这证明了我们可以获得比屏幕容量大 20,000 倍的树的深刻且近乎瞬时的视图——这很好地验证了最初的双焦点显示（bifocal display）直觉。

![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image31.jpg)
Copyright © Jeffrey Heer, Stuart Card. All 
Rights Reserved. Reproduced with permission. See section "Exceptions" in
 the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
Figure 7.18: TreeBlock，一种能够以动画速度计算和布局极大型树的兴趣度树算法。此处显示的树在 600,000 个节点上具有多个焦点，并混合了从右至左和从左至右的文本 (Heer and Card, 2004)。

*通过语义缩放和聚合 DOI 函数进行重新表示（Re-Representation）。* 除了细节水平过滤外，还可以通过多种方式利用兴趣度信息。在图 7.19 中，它被用于 (a) 如前所述的节点细节水平过滤，(b) 调整节点本身的大小，(c) 选择在节点上显示多少个属性，以及 (d) 语义缩放（semantic zooming）。语义缩放是指当节点较小时，使用语义含义相近但表示形式更小的替代方案。例如，图 7.19 中的术语 “Manager” 在节点较小时可能会变为 “Mgr.”。

![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image32.jpg)
Copyright © Stuart Card. All Rights Reserved. 
Reproduced with permission. See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
Figure 7.19: 使用兴趣度计算创建的 PARC 组织结构图（2000 年代初）。触摸一个方框会使该方框以及计算出的兴趣度增加的方框增大并改变其内容；其他方框则会变小。进行搜索可能会产生多个命中结果，导致多个方框增大。

*将视觉变换与兴趣度函数相结合。* 当然，我们讨论的这两种技术可以结合使用。图 7.20 展示了一个包含 Unix 中所有文件的锥形树（cone tree）与兴趣度函数的结合。图 7.20.A 显示了完整的文件树。图 7.20.A 和 7.20.B 显示了对不同文件的选择焦点。由于 Unix 是一个庞大的系统，这可能是人们第一次真正“看到” *Unix* 的全貌。

![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image37.jpg)
Copyright © Stuart Card, Ben Shneiderman, Jock 
Mackinlay. All Rights Reserved. Reproduced with permission. See section 
"Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image38.jpg)
Copyright © Stuart Card, Ben Shneiderman, Jock 
Mackinlay. All Rights Reserved. Reproduced with permission. See section 
"Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/image39.jpg)
Copyright © Stuart Card, Ben Shneiderman, Jock 
Mackinlay. All Rights Reserved. Reproduced with permission. See section 
"Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
Figure 7.20: 使用锥形树结合兴趣度函数可视化的 Unix 文件。(a) Unix 所有文件的锥形树。(b) 使用兴趣度算法选择文件子集。(c) 选择另一组文件。

### 7.5.0.5 聚焦+上下文显示技术的现状

聚焦+上下文（Focus + Context）技术受到 Spence, Apperley 和 Furnas 早期工作的启发，已成为通过在全局信息结构（global information structure）的上下文中处理局部信息，从而应对信息过载（information overload）的丰富灵感来源。Spence 和 Apperley 提出了一些未来的发展方向。我同意他们的建议，并想就我们已有的认知以及潜在的机会提出几点观察。首先是观察结果：

1. *产生了两种可重复利用的抽象方法来生成聚焦+上下文效果：（1）视觉传输函数（visual transfer functions）和（2）感兴趣程度函数（degree-of-interest functions）*。它们构建了大部分的设计空间，并有助于我们生成新的设计。
2. *但这些原则可能会受到低层视觉现象（low-level vision phenomena）的干扰*。例如，平行线的畸变可能会增加任务难度。为了补偿这种畸变，视觉传输函数可以被赋予平坦区域（flat regions）。平坦区域虽然有效，但反过来可能会在聚焦区域（focal areas）和上下文区域（context areas）之间产生一个中间区域，从而在关键的近聚焦区域（near-focal region）创建一个难以阅读的区域。另一个例子是，树形结构的上下文部分可能会形成视觉斑块（visual blobs），而眼睛会被视觉斑块吸引，导致用户在树的非生产性部分浪费时间进行搜索 (Pirolli, Card, & Van der Wege, 2003; Budiu, Pirolli, & Fleetwood, 2006)。这些不可控的效果可能会干扰任务。我们需要更好地理解聚焦+上下文显示中的低层视觉效果。
3. *总的来说，我们需要理解聚焦+上下文显示如何为任务中的行动线索（cues to action）或意义构建（sensemaking）提供引导*。汽车后视鱼眼镜中的畸变是可以接受的，因为其行动线索是镜像视野中某些对象的出现、消失或移动，这预示着不安全的情况。但如果鱼眼显示被用作地图查看器的一部分，道路的畸变弯曲可能不利于导航引导。其区别在于任务。实际上，我们需要进行认知任务分析（cognitive task analysis），询问我们究竟试图从这些显示中获得什么，以及为什么我们预期它们能起作用。我们必须更好地理解聚焦+上下文显示在任务流（flow of the task）中是如何运作的。
4. *在大的放大倍率（magnification ratios）下，当不同聚合层级（aggregation levels）存在一组涌现的表示（emergent set of representations）时，聚焦+上下文显示的效果最好*。在适度的放大倍率下，仅使用放大（magnification）即可奏效。而 DOI 过滤在大的放大倍率下有效，是因为其算法有效地转换到了一种更高层级的聚合。但聚焦+上下文显示的强大之处在于，它们能够将跨聚合层级的表示联系在一起。

实际上，这些观察反映了一组更深层次的问题。聚焦+上下文显示利用了用户自动的、面向感知（perceptually-oriented）的机制与用户更费力的、面向认知（cognitively-oriented）的机制之间微妙的交互——有时被称为系统 1 和 系统 2 (Kahneman, 2012)，以及这两个系统与任务需求之间的微妙交互。这些机制与聚焦+上下文可视化设计之间的交互需要被更好地理解。这些显示技术开发的新机会包括：与多点触控输入设备或多组显示器的集成，或者在汽车或医疗手术室中的应用。聚焦+上下文显示的核心在于带宽（bandwidth）和注意力（attention）的动态划分。针对问题的新信息流以及用于控制的新输入设备，应确保这一领域依然充满活力。

### 7.5.0.6 参考文献 (References)

1. Budiu, Raluca, Pirolli, Peter, & Fleetwood, Michael (2006). 在兴趣度树（degree of interest trees）中进行导航（Navigation）. *AVI 2006, Proceedings of the working conference on Advanced Visual Interfaces,* 457-462. New York: ACM.
1. Card, Stuart K., Hong, Lichen, Mackinlay, Jock D. (2004). 3Book：一种 3D 电子智能书（electronic smart Book）. *AVI 2004, Proceedings of the conference on Advanced Visual Interfaces:* 303-307.
1. Card, S. K., Mackinlay, J. D., & Shneiderman, B. (1999). *Readings in Information Visualization.* San Francisco, CA: Morgan-Kaufmann.
1. Card, Stuart K. and Nation, David (2002). 兴趣度树：一种注意力响应式用户界面（attention-reactive user interface）的组件. *AVI 2002, Proceeding of the Conference on Advanced Visual Interfaces (Trento, Italy, May 22-24, 2002)*, 231-245.
1. Card, S. K., Robertson, G. G., and York, W. (1996). WebBook 与 Web Forager：一个面向万维网（World-Wide Web）的信息工作空间（information workspace）. *Proceedings of CHI ‘96, ACM Conference on Human Factors in Software*, New York: ACM, 111–117.
1. Carpendale, M.S.T. and Montagnese, Catherine (2001). 橡胶片视觉变换函数（Rubber sheet visual transform functions）. In *UIST 2001, Proceedings of the ACM Symposium on User Interface Software and Technology (Orlando, FL).* New York: ACM, 61-70.
1. Carpendale (2006/2012, December 6). 弹性呈现（Elastic Presentation）. *Sheelagh Carpenter.* Retrieved June 24, 2012 from [http://pages.cpsc.ucalgary.ca/~sheelagh/wiki/pmwiki.php?n=Main.Presentation](http://pages.cpsc.ucalgary.ca/~sheelagh/wiki/pmwiki.php?n=Main.Presentation) .
1. Furnas, G. (1986). 广义鱼眼视图（fisheye views）. *CHI '86, Proceeding of the Conference on Human Factors in Computing Systems* (Boston). New York: ACM, 16-23.
1. Furnas, G. W. (1982). 鱼眼视图：结构化文件的一种新视角. Technical Memorandum #82-11221-22, Bell Laboratories, Oct. 18.
1. Furnas, G. W. (1992/1999). 鱼眼视图：结构化文件的一种新视角. In Stuart. K. Card, Jock D. Mackinlay, & Ben Shneiderman, *Readings in Information Visualization* (pp. 312-330). San Francisco, CA: Morgan-Kaufmann.
1. Heer, Jeffrey and Card, Stuart K. (2003). 信息可视化（Information visualization）与导航：鱼眼视图中高效的用户兴趣估计. *CHI ’03 Extended Abstracts on Human Factors in Computing Systems,* 836-837.
1. Heer, Jeffrey & Card, Stuart K. (2004). 重新审视 DOITrees：层次化数据（hierarchical data）的可扩展且空间受限的可视化. *AVI 2004. Proceeding of the Conference on Advanced Visual Interfaces (Trento, Italy)*.
1. Kahneman, Daniel (2011). *Thinking, Fast and Slow.* New York: Farrar, Straus and Giroux.
1. Lamping, J., Rao, R. and Pirolli, P. 一种基于双曲几何（hyperbolic geometry）的“焦点+上下文（focus + context）”技术，用于可视化大型层次结构. *CHI '95 Proceedings of the SIGCHI Conference on Human factors in Computing Systems.*
1. [Leung](https://www.interaction-design.org/references/authors/y__w__leung.html), Y. W. and [Apperley](https://www.interaction-design.org/references/authors/mark_apperley.html), Mark (1994). 失真导向呈现技术（Distortion-Oriented Presentation Techniques）的综述与分类学（Taxonomy）. In *ACM Transactions on Computer-Human Interaction*, 1(2): 126-160.
1. Mackinlay, Jock D., Robertson, George G., & Card, Stuart K. (1991). 透视墙（perspective wall）：细节与上下文的平滑过渡. In *CHI ‘91, ACM Conference on Human Factors in Computing Systems.* New York: ACM, 173–179.
1. Munzner, Tamara, and Burchard, Paul (1995). 在 3D 双曲空间（hyperbolic space）中可视化万维网的结构. *Proceedings of VRML ’95, (San Diego, California, December 14-15)* and special issue of *Computer Graphics*, New York: ACM SIGGRAPH, pp. 33-38.
1. Munzner, Tamara (1998). 在 3D 超空间（hyperspace）中探索大型图. *IEEE Computer Graphics and Applications* 18(4):18-23.
1. Pirolli, Peter, Card, Stuart K., a& Van Der Wege, Mija M. (2003). 信息气味（information scent）在双曲树浏览器中对视觉搜索的影响. *ACM Transactions on Computer-Human Interaction (TOCHI): 10*(1). New York: ACM.
1. Resnikoff, H. L. (1987). *The Illusion of Reality.* New York: Springer-Verlag.
1. Robertson, George G., Mackinlay, Jock D. (1993). 文档透镜（document lens）. In *ACM UIST ’93, Proceedings of the 6th Annual ACM Symposium on User Interface Software and Technology*. New York: ACM, 101-108.
1. Robertson, George G., Mackinlay, Jock D., & Card, Stuart K. (1991). 锥形树（Cone trees）：层次化信息的动态 3D 可视化. *CHI ‘91 ACM Conference on Human Factors in Computing Systems,* 189–194. New York: ACM.
1. Sarkar, M. and Brown, M.H. (1994). 图形化鱼眼视图. *CACM* 37(12): 73-84.
1. Spence, R. (1982). 双焦点显示（Bifocal Display）. Video, Imperial College London.
1. Tallmina, Daina (1997). 双曲平面（hyperbolic plane）的钩编模型. Fig, The Institute for Figuring. Taken from web page [http://www.theiff.org/oexhibits/oe1e.html](http://www.theiff.org/oexhibits/oe1e.html) on June 14, 2012.

# 7.6 Lars Erik Holmquist 的评论

在重新审视 Spence 和 Apperley 的原始视频时，令人惊叹的是他们的想法至今依然如此前卫且实用——这不仅体现在双焦点显示（Bifocal display）本身的原理上，还体现在他们所构想的人机交互（human-computer interaction）环境之中。几年前，我组织了一场经典研究视频的会议放映，其中包括 Spence 和 Apperley 对未来“专业人士办公室（Office of the Professional）”的设想。为了增加趣味性，放映结束后我们观看了 Steven Spielberg 的科幻电影《少数报告》（MINORITY REPORT）。在这部虚构电影中，我们可以看到主角（由 Tom Cruise 饰演）与信息交互的方式似乎远远超出了我们今天的桌面计算机，但在许多方面又与 Spence 和 Apperley 对未来办公室的愿景非常相似。这些研究者的思想如此超前，以至于当这些作品被对照放映时，人们立刻就能发现 1981 年研究中的许多想法被直接反映在 20 多年后好莱坞一个华丽的未来愿景之中！

现在我们很难想象，但曾经桌面计算范式（desktop computing paradigm），也被称为 Windows-图标-鼠标-指针（Windows-Icons-Mouse-Pointers，简称 WIMP），仅仅是关于未来如何与数字数据进行最佳交互的众多竞争方案之一。Spence 和 Apperley 想象的交互方式更符合我们与现实世界物体交互的方式——直接指向它们、在屏幕上触摸它们、发出自然的口头指令，而不是使用像鼠标这样脱节且间接的设备进行点选。在他们探索的众多想法中，一个共同的主题是以比在普通计算机屏幕上查看更自然的方式与大量信息进行交互——他们将后者比作透过一个小窗户窥视，只能揭示海量底层数据中的极小一部分。

双焦点显示基于一些非常简单但强大的原理。通过观察人们在真实的物理世界中如何处理大量数据，发明者们想出了在虚拟领域缓解同一问题的解决方案。在这种特定情况下，他们借鉴了对人类视觉系统的观察——即我们如何在保持少数事物处于焦点（focus）的同时，将许多事物保留在注意力的边缘（periphery）——并将其通过电子方式实现。他们还利用了一个简单的光学现象，即透视（perspective）：远处的物体比近处的物体小。后来，其他物理特性也被应用于实现类似效果，例如像“橡胶片（rubber sheet）”一样拉伸并适应外部力量的想法，或者像摄像机镜头一样创建场景的“鱼眼（fisheye）”视图（例如 Sarkar and Brown 1994）。

所有这些技术都可以归类在“焦点+上下文可视化（focus+context visualizations）”这一通用术语下。这些可视化技术有潜力使计算机屏幕上的大量数据变得易于理解，而计算机屏幕由于尺寸和分辨率等因素，在本质上限制了其能呈现的数据量。然而，尽管这些技术功能强大，但其中许多也存在一些固有问题。原始的双焦点显示假设被查看的材料排列在 一维布局（1-dimensional layout）中，这对于许多重要的数据集（如地图和图像）来说可能并不适用。其他鱼眼和橡胶片技术将这些原理扩展到了二维数据，但仍然要求基于固定空间关系而非基于逻辑关系（如图表）的排列。这一点在后来的可视化技术中得到了解决，这些技术允许数据集中的单个元素（例如图中的节点）在二维空间中更自由地移动，同时保持其逻辑排列（例如 Lamping et al 1995）。

此外，为了使这些技术奏效，必须假设焦点之外的材料对失真缩减（distortion shrinking）不 overly 敏感，或者至少在应用某些失真时仍能辨认。但这并非总是成立；例如，如果文本承受过多的失真和/或缩减，可能会变得无法阅读。在这种情况下，可能需要采用除纯视觉之外的其他方法来减小焦点之外材料的尺寸。实现这一目标的一个例子是语义缩放（semantic zooming），它可以衍生自 Furnas 通用鱼眼视图中的“感兴趣程度（Degree of Interest）”函数（Frunas 1986）。在语义缩放中，与其在图形上缩减或扭曲焦点之外的材料，不如提取并显示重要的语义特征。一个典型的应用是显示报纸文章的标题，而不是整个文本的缩略图。语义缩放现在在地图中很常见，当用户放大时，更多的细节（如地名和小路）会逐渐显现。

人们尝试缓解这些问题的方法有很多。在我的研究工作中，采用了与 Spence 和 Apperley 类似的起点，并受到 Furnas、Card 等人的启发，我设想了一张铺满重要文件的办公桌。其中一两张文件在被处理时处于注意力的中心，其余的则散布在周围。然而，与其他双焦点显示不同，它们不会形成一个连续的显示，而是由离散的对象组成。在计算机屏幕上，其类比是在中间放置一个可读尺寸的对象，而将其他对象缩减为较小尺寸并排列在周围区域。通过将单个页面按从左到右、从上到下的方式排列，可以呈现较长的文本，如报纸文章或书籍（见图 1）。用户随后可以点击相关页面将其聚焦，或使用键盘翻页（图 2）。这种技术被称为翻页缩放（Flip Zooming），因为它模拟了翻书的过程。最初的应用是一个用于网页浏览的 Java 应用程序，称为缩放浏览器（Zoom Browser）（Holmquist 1997）。后来，我们致力于将同一原理适配到更小的显示设备中，如掌上电脑。由于这些设备的屏幕空间（screen real-estate）更小，仅仅缩减焦点之外的页面是不可行的——它们会变得太小而无法阅读。相反，我们应用了计算语言学原理（computational linguistics principles）来提取每个部分最重要的关键词，并将其呈现给观看者，以提供材料的概览。这被实现为一个用于小型终端的 Web 浏览器，是如何在此类设备上处理大量数据的首批示例之一（Björk et al. 1999）。

![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/browser_unzoomed_screen_real-estate.jpg)
Copyright © Lars Erik Holmquist. All Rights Reserved. Reproduced with permission. See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
图 7.1：大型文档的翻页缩放视图，无页面放大

![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/browser_zoomed_screen_real-estate.jpg)
Copyright © Lars Erik Holmquist. All Rights Reserved. Reproduced with permission. See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
图 7.2：翻页缩放且有页面放大的情况。注意页面之间的线条用于表示顺序！

可视化大量数据的另一个问题是尺寸与分辨率（size versus resolution）的关系。即使是非常大的显示设备，如投影仪或大屏幕等离子屏，其像素数量也与普通计算机终端大致相同。这意味着虽然我们可以将焦点+上下文显示扩大到墙壁大小，但显示设备可能没有足够的细节来正确显示焦点中的重要信息（如文本）。几个项目尝试将不同尺寸和分辨率的显示器结合起来，以便同时显示细节和上下文。例如，焦点+上下文屏幕（Focus Plus Context Screen）将一个高分辨率屏幕放置在大投影显示屏的中心（Baudisch et al 2005）。该系统能够提供大图像（如地图）的低分辨率概览，并在中间提供一个高分辨率区域；用户随后可以滚动图像以寻找感兴趣的区域。在普适图形（Ubiquitous Graphics）项目中也发现了类似的方法，我们将位置感知（position-aware）的掌上显示设备与大型投影显示屏相结合。用户不再是在静态定位的显示器上滚动图像，而是可以将高分辨率显示器作为一个窗口或“魔镜（magic lens）”，以显示大屏幕上任意部分的细节（见图 3）。这些以及其他几个项目指向了一种设备生态（device ecology），其中多个屏幕协同工作作为输入/输出设备。这将允许以比单用户桌面工作站更自然的方式进行协作工作，这让我们想起了 Spence 和 Apperley 最初的愿景。

![](https://www.interaction-design.org/images/encyclopedia/bifocal_display/ubiquitous_graphics_magic_lens_wimp.jpg)
Copyright © Lars Erik Holmquist. All Rights Reserved. Reproduced with permission. See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/bifocal-display#copyrightNotice) below.
图 7.3：普适图形系统提供了一个可自由移动的高分辨率显示器，它充当交互式“魔镜”，以揭示大显示器上任何位置的详细信息

在经历了 20 多年的 WIMP 桌面计算之后，双焦点显示及其衍生想法在许多方面比以往任何时候都更具相关性。我们生活在一个不同分辨率和尺寸的多个显示器并存的世界中，非常像 Spence 和 Apperley 对未来办公室的愿景。新的交互模型为缩放和基于焦点+上下文的显示开辟了新的可能性。例如，智能手机和平板电脑等多点触控设备（multitouch devices）使得直接在屏幕上拖动和拉伸虚拟“橡胶片”变得完全直观，而不再是鼠标那种单点、间接的交互风格。我相信，这批新设备为重新审视并构建基于 Spence 文本中提出的原始可视化想法提供了绝佳的机会，而我们可能才刚刚看到它们在实际应用中的起步。

### 参考文献

- Björk, S., Holmquist, L.E., Redström, J., Bretan, I., Danielsson, R., Karlgren, J. and Franzén, K. *WEST：一种用于小型终端 (Small Terminals) 的网页浏览器 (Web Browser)*. Proc. ACM Conference on User Interface Software and Technology (UIST) '99, ACM Press, 1999.
- Baudisch, P., Good, N., and Stewart, P. *焦点+上下文屏幕 (Focus Plus Context Screens)：将显示技术与可视化技术 (Visualization Techniques) 相结合*. In Proceedings of [UIST 2001](http://www.acm.org/uist/uist2001/), Orlando, FL, November 2001, pp.31-40.
- Furnas, G.W. *广义鱼眼视图 (Generalized fisheye views)*. CHI '86 Proceedings of the SIGCHI conference on Human factors in computing systems.
- Holmquist, L.E. *基于翻转缩放 (flip zooming) 和缩放浏览器 (zoom browser) 的焦点+上下文可视化 (Focus+context visualization)*. CHI '97 extended abstracts on Human factors in computing systems.
- Lamping, J., Rao, R. and Pirolli, P. *一种基于双曲几何 (hyperbolic geometry) 用于可视化大型层级结构 (large hierarchies) 的焦点+上下文技术*. CHI '95 Proceedings of the SIGCHI conference on Human factors in computing systems.
- Sanneblad, J. and Holmquist, L.E. *普适图形 (Ubiquitous graphics)：结合手持设备与墙面尺寸显示器 (wall-size displays) 以进行大图交互*. AVI '06 Proceedings of the working conference on Advanced visual interfaces.
- Sarkar, M. and Brown, M.H. *图形化鱼眼视图 (Graphical Fisheye Views)*. Commun. ACM 37(12): 73-84 (1994)

## 本书章节涵盖的主题：

[双焦点显示 (Bifocal Display)](https://www.interaction-design.org/literature/topics/bifocal-display)
[用户体验 (User Experience, UX) 设计](https://www.interaction-design.org/literature/topics/ux-design)
[人机交互 (Human-Computer Interaction, HCI)](https://www.interaction-design.org/literature/topics/human-computer-interaction)
