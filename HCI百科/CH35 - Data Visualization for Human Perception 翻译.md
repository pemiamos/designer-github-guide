# 35. 面向人类感知的数据可视化（Data Visualization for Human Perception）

**来源**：The Encyclopedia of Human-Computer Interaction, 2nd Ed.
**Notion 原页面**：https://www.notion.so/fed37581f3af40bf83c800ad0924c3ca

---

[Stephen Few](https://www.interaction-design.org/literature/author/stephen-few)
[数据可视化（Data visualization）](https://www.interaction-design.org/literature/topics/data-visualization) 是将抽象信息进行图形化展示（Graphical display），其目的有两个：意义构建（Sense-making，也称为数据分析）和沟通。我们的数据中蕴含着重要的故事，而数据可视化是发现并理解这些故事，进而将其呈现给他人的强大手段。这里的“信息”之所以是抽象的，是因为它描述的是非物理实体的事物。统计信息（Statistical information）就是抽象的。无论它涉及的是销售额、疾病发病率、运动表现还是其他任何内容，尽管它不属于物理世界，我们仍然可以将其视觉化地展示出来；但要实现这一点，我们必须找到一种方法，为那些没有形式的事物赋予形式。这种将抽象转化为物理形式的...

视觉属性（attributes of vision，例如长度、位置、大小、形状和[颜色](https://www.interaction-design.org/literature/topics/color)等）只有在我们对[视觉感知](https://www.interaction-design.org/literature/topics/visual-perception)（visual perception）和[认知](https://www.interaction-design.org/literature/topics/cognition)（cognition）有一定了解的情况下才能发挥作用。换句话说，为了有效地进行数据可视化（visualize data），我们必须遵循基于对人类[感知](https://www.interaction-design.org/literature/topics/perception)（perception）理解而制定的[设计原则](https://www.interaction-design.org/literature/topics/design-principles)（design principles）。

正如俗话所说，“一幅画胜过千言万语”——通常甚至更多——但这仅限于该故事最适合以图形而非文字的方式来讲述，且该图像经过精心设计的情况。你可能整天盯着一张数字表格看，却始终无法发现那些在同一组数字的优秀图表中能立即显现出的规律。请允许我举例说明。这里有一张简单的销售数据表——涵盖一整年的数据——分为两个区域：

![](https://public-media.interaction-design.org/images/encyclopedia/data_visualization_for_human_perception/sales-table-visualization.jpg)

作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 35.1**

这张表格在两方面表现得极其出色：它精确地表达了这些销售数值，并为查询特定区域和月份的数值提供了一种高效的手段。但如果我们试图在这些数值中寻找模式（Patterns）、趋势（Trends）或异常值（Exceptions），或者希望快速感知这些数字背后蕴含的故事，亦或是需要比较整组数字而非仅仅每次比较两个，那么这张表格就失效了。

现在请看下面这张以折线图（Line graph）形式呈现相同信息的图片：

![](https://public-media.interaction-design.org/images/encyclopedia/data_visualization_for_human_perception/sales-line-graph-visualization.jpg)

作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 35.2**

现在，几个事实一目了然：
- 国内销售额明显且持续地高于国际销售额。
- 总体而言，国内销售额在全年呈现上升趋势。
- 相比之下，国际销售额保持相对平稳，但有一个显著的异常：它们在 8 月份大幅下降。
- 国内销售额呈现出一种周期性模式（Cyclical pattern）——上升、上升、下降——这种模式按季度重复，总是在季度的最后一个月达到顶峰，然后在下个季度的第一个月剧烈下降。

当这些数字以文本形式呈现时，它们无法传达的信息是……

表格中的内容是通过大脑的语言处理（verbal processing）来解读的，而当通过视觉方式传达时，它变得直观且易于理解。这就是“数据可视化（data visualization）”的力量。

虽然数据可视化通常侧重于[定量值（quantitative values）](https://www.interaction-design.org/literature/topics/quantitative-research)之间的关系，但它也可以展示本质上非定量的关系。例如，Facebook 等社交网络网站上的用户之间，或疑似恐怖分子之间的联系，可以使用节点-链路可视化（node and link visualization）来展示。在接下来的示例中，人被定义为节点（nodes），以圆圈表示；而他们之间的关系则是链路（links），以连接他们的线段表示。

![](https://public-media.interaction-design.org/images/encyclopedia/data_visualization_for_human_perception/node-and-link-diagram-social-graph.jpg)
作者/版权持有者：Jeffrey Heer 和 Danah Boyd 使用 Vizster 提供。版权条款和许可：CC-Att-ND (Creative Commons Attribution-NoDerivs 3.0 Unported)。
**图 35.3**

刻画实体（entities）之间关系的可视化（如上述示例中的人物关系）也可以通过添加定量信息来进一步丰富。例如，任意两人之间互动的次数可以通过连接他们的线段粗细来表示。

## 35.1 历史背景下的数据可视化（Data Visualization）

人们至少从公元 2 世纪起就开始将数据排列成表格（行与列），但用图形表示定量信息（quantitative information）的想法直到 17 世纪才出现。这一[创新](https://www.interaction-design.org/literature/topics/innovation)要归功于法国哲学家和数学家 Rene Descartes。他开发了一种用于显示数值的二维坐标系（two-dimensional coordinate system），由一个代表一个变量的水平轴和一个代表另一个变量的垂直轴组成，主要将其作为执行数学运算的图形化手段。直到 18 世纪末，我们才开始挖掘图形在定量数据传递（communication of quantitative data）方面的潜力，这要归功于苏格兰人 William Playfair。Playfair 开创了许多如今常用的图表。他是第一个使用从左向右延伸且上下波动的线条来展示数值随时间变化的人，如下例所示。他还发明了柱状图（bar graph），并且在某次灵感迸发时发明了饼图（pie chart）。后来我们发现饼图相对低效，因为它将数值编码（encodes）为视觉属性（visual attributes）——主要是每个扇形的面积以及它在圆心形成的夹角——而这些属性是我们难以轻松感知和比较的。

![](https://public-media.interaction-design.org/images/encyclopedia/data_visualization_for_human_perception/playfair-visualization-national-debt-line-graph.jpg)
作者/版权持有者：William Playfair (1759-1823) 提供。
版权条款与许可：pd（公有领域（Public Domain），指共有财产且不含原始作者权的资料）。
**图 35.4**：Playfair 将此图表收录在其著作 *The Commercial and Political Atlas* (1786) 中，旨在反对英国通过国家债务为殖民战争融资的政策。

随着时间的推移，定量图表（Quantitative Graphs）的使用逐渐增加，但其方法和有效性直到 20 世纪下半叶才有了显著演进。Jacques Bertin 在 1967 年出版的 *Semiologie graphique* (*The Semiology of Graphics*, Bertin 1967) 一书，为过去半个世纪的大部分进展奠定了基础。他的工作至关重要，因为他发现视觉感知（Visual Perception）遵循一定的规则，而通过遵循这些规则，可以用直观、清晰、准确且高效的方式将信息进行视觉化表达。

真正向我们揭示数据可视化（Data Visualization）作为探索和理解定量数据手段之强大威力的人，是 Princeton 大学统计学教授 John Tukey。他在 1977 年提出了一种全新的统计方法，称为 *exploratory data analysis*（探索性数据分析）。

1983 年，如今在该领域工作且名为...的人

在所有相关人士中，Edward Tufte 最受推崇，他出版了开创性的著作 *The Visual Display of Quantitative Information*。在书中，他指出，虽然存在有效的数据可视化（Data Visualization）展示方式，但大多数人的做法却效果不佳。与此同时，William Cleveland 也在致力于改进数据可视化实践，他为统计学家扩展并完善了数据可视化技术。此后不久，学术界出现了一个新的研究领域，被命名为“[信息可视化（Information Visualization）](https://www.interaction-design.org/literature/topics/information-visualization)”。在 1999 年出版的 *Readings in Information Visualization: Using Vision to Think* 一书中，Stuart Card, Jock Mackinlay 和 Ben Shneiderman 汇集了最优秀的

将当时已完成的学术研究汇编成册，使其研究成果在学术界之外也变得[易于获取](https://www.interaction-design.org/literature/topics/accessibility)（Accessible）(Card et al 1999)。

自 21 世纪之交以来，数据可视化（Data Visualization）得到了普及，但由于其通过商业软件产品触达大众，其普及方式往往低效得令人遗憾。令人欣慰的是，在众多推崇表面[美学](https://www.interaction-design.org/literature/topics/aesthetics)（Aesthetics）而忽视实用且有效的数据探索（Data Exploration）、意义构建（Sense-making）和沟通的产品中，仍有少数值得关注的优秀产品，它们正以实用且强大的方式帮助我们发挥数据可视化的潜力。

![](https://public-media.interaction-design.org/images/encyclopedia/data_visualization_for_human_perception/tableau-visualization-example.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 35.5**：该显示界面由同一数据集的多个视图组成，是使用 Tableau Software 创建的，该厂商是目前少数真正理解数据可视化的软件供应商之一。

在那些为我们理解数据做出贡献的人之中...

在可视化（Visualization）领域，Colin Ware 为将其实践建立在对人类感知（Human Perception）的理解之上做出了最大贡献。Ware 的两部优秀著作——*Information Visualization: Perception for Design* (Ware, 2004) 和 *Visual Thinking for Design* (Ware 2008) —— 汇总、整理并阐释了我们从多个科学学科中获得的关于视觉思维（Visual Thinking）与认知（Cognition）的知识，并将这些知识应用于数据可视化（Data Visualization）。

## 35.2 视觉与心智的图像

数据可视化（Data visualization）能否成功，取决于它是否能以一种我们的眼睛可以辨识、大脑可以理解的方式对信息进行编码（encode）。做好这一点与其说是艺术，不如说更像是一门科学，而我们只能通过研究人类感知（human perception）来实现这一目标。其目标是将抽象信息转化为能够被轻松、高效、准确且有意义地解码（decode）的视觉表征（visual representations）。考虑这样一个案例：你需要帮助人们理解下表中所包含的美国主要死亡原因：

![](https://public-media.interaction-design.org/images/encyclopedia/data_visualization_for_human_perception/causes-of-death-table-visualization.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。
**图 35.6**

为了实现这一目标，展示方式应达到以下要求：
- 清晰地表明数值之间如何相互关联，在本例中是一种部分与整体的关系（part-to-whole relationship）——各项死因的死亡人数之和等于该年度的总死亡人数。
- 准确地表示数量。
- 使数量的比较变得简单。
- 使数值的排序（ranked order）一目了然，例如从最主要的死因到最次要的死因。

- 使人们能够清楚地知道如何使用这些信息——以及使用这些信息是为了达成什么目标——并鼓励他们这样做。

以图形方式展示此类信息的传统方法是使用饼图（Pie Chart），如下图所示。

![](https://public-media.interaction-design.org/images/encyclopedia/data_visualization_for_human_perception/pie-chart-distorted-causes-of-death.jpg)

作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

**图 35.7**

这个饼图在多大程度上满足了我们的有效性标准？让我们逐一分析各项要求。

- *是否清晰地表明了关系的性质？ 是。* 饼图的主要优势在于它能清晰地表明数值之间的部分-整体关系（part-to-whole relationship）。
- *是否准确地表示了数量？ 否。* 饼图通过三种视觉属性（visual attributes）对数值进行冗余编码：每个扇形的面积、每个扇形在圆心形成的夹角，以及每个扇形沿圆周的弧长。即使每个扇形的面积、角度和周长计算正确，它依然失效，因为我们无法准确地感知其中任何一项属性。人类的视觉感知（visual perception）在进化过程中并未形成对面积、角度或曲线距离进行精确解码（decoding）的能力。

- *是否易于比较数量？不。* 由于我们无法准确地感知（perceive）数值，因此也无法轻松或准确地对它们进行比较。此外，在这个特定的饼图（pie chart）中，由于使用了图例（legend）来标记扇区（slices），我们不得不反复通过寻找正确的颜色来查找想要比较的扇区的含义，而这些颜色往往难以区分（discriminate）。该饼图采用了 3D 渲染，这也使简单的比较行为变得复杂，因为透视（perspective）扭曲了扇区的相对大小和形状，使得底部的扇区看起来比顶部大小相近的扇区更大且更显著（salient）。
- *是否易于看出数值的排序（ranked order）？不。* 尽管扇区是按从最高值（心脏病）开始，顺时针排列至最小值（不包括最后的“所有其他原因”扇区），但这种排序并不明显，因为扇区之间难以比较。例如，由于 3D 效果赋予了其更多的视觉权重（visual weight），红色的癌症扇区看起来比蓝色的心脏病扇区更大。像这个饼图的 3D 渲染这样的效果，有时被用来故意误导。
- *是否明确了人们应如何使用这些信息？部分如此。* 虽然该饼图成功地引导人们通过比较扇区来理解各部分对整体的相对贡献（relative contributions），但它未能有效地支持这一操作。

鉴于这个饼图（Pie Chart）在匹配人类感知（Human Perception）方面的不足，让我们考虑另一种显示形式。下面的条形图（Bar Graph）显示了同一组数值，但其呈现方式更容易被感知。

![](https://public-media.interaction-design.org/images/encyclopedia/data_visualization_for_human_perception/causes-of-death-bar-chart-visualization.jpg)
Author/Copyright holder: Unknown (pending investigation). Copyright terms and licence: Unknown (pending investigation). See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/about/terms-of-use) below.

**Figure 35.8**

让我们使用之前的相同标准来评估这个条形图的有效性。

- *是否清晰地表明了关系的性质？ 是。* 条形图本身并不能声明这些数值之间部分与整体（Part-to-whole）的关系，因为与饼图不同，条形图也可以用来显示其他关系。然而，这个特定的条形图包含了使关系性质变得清晰的组件，包括标题（"Total Deaths..."）以及尤其是总计为 100% 的数值列。
- *是否准确地表示了数量？ 是。* 每个条形结束的水平位置以及相对于 x 轴定量刻度（Quantitative scale）的长度，都以一种能够被准确感知的方式对这些数值进行了编码（Encode）。与面积、角度以及...不同。

不共享共同基准线（Common baseline）的曲线长度、二维位置，以及像这些条形一样共享共同基准线且彼此平行的直线对象的长度，都是我们可以高精度感知的视觉属性（Visual attributes）。

- *是否易于比较数量？是的。* 因为当这些数值被编码为条形（Bars）时，我们可以准确地感知它们，因此比较起来也非常容易。请注意，这些条形长度的差异非常容易被察觉，而这在比较饼图的扇区（Slices of the pie）时则很难实现。同时请注意，当每个条形具有相同的颜色时（不同于颜色各异的饼图扇区），这种相似性会促使我们的眼睛去比较这些条形。此外，由于条形直接标注了死亡原因的名称，我们在比较数值时不再需要执行图例（Legend）所要求的认知操作。
- *是否易于查看数值的排序（Ranked order）？是的。* 由于条形长度的差异易于感知，因此除了最后一个“所有其他原因”条形外，它们按从高到低的顺序排列这一事实显而易见。通过将条形按排序排列，我们将数值最接近的死亡原因在图表中放置在一起，从而使比较变得更加容易。
- *是否明确了人们应如何使用这些信息？是的。* 事实是，这些条形应当被用来比较，以理解不同的...

这些死因在总死亡人数中所占的比例在直觉上是显而易见的。

比较饼图（Pie Chart）和条形图（Bar Graph）的感知效能（Perceptual Effectiveness）的目的，并非是为了论证饼图的不足（尽管这种论证是有必要的），而是为了说明：**我们应当始终根据能够多么轻松、高效、准确且有意义地感知信息所传达的故事，来评判一个可视化方案的优劣**。为此，我们必须了解各种图形手段在展示特定故事时的感知优势与劣势。而要做到这一点，我们必须理解感知（Perception）。

## 35.3 数据可视化与人类感知（Data Visualization and Human Perception）

数据可视化之所以有效，是因为它改变了感知（Perception）与认知（Cognition）之间的平衡，从而更充分地利用大脑的能力。视觉（即视觉感知 Visual Perception）由位于大脑后部的视觉皮层（Visual Cortex）处理，速度极快且效率极高。我们能够立即看到，且几乎不需要费力。而思考（即认知 Cognition）主要由大脑前部的大脑皮层（Cerebral Cortex）处理，速度要慢得多，效率也较低。传统的数据意义构建（Sensemaking）和呈现方法在几乎所有环节都需要有意识的思考。数据可视化将平衡点向更多地利用视觉感知方向转移，尽可能地发挥我们强大的视觉能力。

![](https://public-media.interaction-design.org/images/encyclopedia/data_visualization_for_human_perception/brain-balance-perception-cognition-horisontal.jpg)
作者/版权持有者：未知（待调查）。版权条款和许可：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。
**图 35.9**

对感知科学最早的贡献之一来自格式塔心理学派（Gestalt School of Psychology）。该研究始于 1912 年，其最初目的是揭示我们如何感知所见之物的模式（Pattern）、形式（Form）和组织（Organization）。创始人观察到我们

以特定的方式组织我们所看到的内容，旨在使其具有意义。这一努力的结果是一系列[格式塔原则（Gestalt principles）](https://www.interaction-design.org/literature/topics/gestalt-principles)的感知规律，这些原则至今仍被认为是对视觉行为的准确描述。以下是几个可以为我们的数据可视化（data visualization）工作提供参考的原则：

除了信息可视化（information visualization）之外，视觉感知（visual perception）和认知（cognition）的新见解正源于多个学科的研究，例如[人因工程（human factors）](https://www.interaction-design.org/literature/topics/human-factors)和人机交互（human-computer interaction），但其中最具有突破性的当属认知科学（cognitive sciences），尤其是[认知心理学（cognitive psychology）](https://www.interaction-design.org/literature/topics/cognitive-psychology)。如今，随着大脑探索技术和方法的更新与改进，提高数据可视化感知效能（perceptual effectiveness）的机会大量增加。其中，有两个研究领域尤为有用：

- 前注意视觉处理（preattentive visual processing）
- 注意力（attention）与记忆（memory）的机制及其局限性

数据可视化的一个巨大优势在于，我们处理视觉信息的能力远快于处理语言信息（verbal information）。前注意视觉处理是指在意识觉察（conscious awareness）之前，大脑中自动发生的部分。它由多个阶段组成，每个阶段由专门用于检测的特化神经元（specialized neurons）处理。

……光线从物体表面反射出的视觉信息中所包含的特定属性，随后这些属性在我们的心像（mind's eye）中被拼接成该物体的图像。我们可以将这些基础属性——如长度、尺寸、色调（hue）、颜色强度、角度、纹理、形状等——作为数据可视化（data visualization）的构建块。当我们以一种基于理论的方式（informed manner）这样做时，我们能够将解码视觉显示内容（如图表）的大部分工作，从大脑中较慢的、意识层面的、高能耗的部分，转移到较快且低能耗的部分，从而实现更高效的认知（cognition）。

关于注意力（attention）和记忆（memory）的研究表明，我们在意识中同时持有多个项目的能力出奇地有限。这一认知促使我们通过依赖外部信息存储形式来增强注意力与记忆。最有效的方法之一是将信息进行视觉编码（encode），这使得更多信息能够被组块化（chunked），从而填入工作记忆（working memory）中有限的槽位。另一种方法是同时将多个信息视图呈现在眼前，从而扩展我们从多维度和多视角探索数据的能力，以便进行比较并发现关联；由于工作记忆的限制，如果我们必须逐一查看这些视图，将无法达到这种程度。

优秀的数据可视化技术与手段（Data Visualization Techniques and Technologies）若能得到恰当运用，可以将我们的思维拓展至分析性意义构建（Analytical Sensemaking）的新领域，而我们目前才刚刚开始挖掘这一潜力。

## 35.4 未来方向

在数据可视化（data visualization）领域，与其他领域一样，最需要的并不总是最令人兴奋的，甚至不一定是特别具有创新性的。有时，我们只需要让那些行之有效的方法更容易实施。一个例子是少数软件供应商尝试将数据可视化的最佳实践（best practices）直接内置到工具中（例如以默认设置的形式），从而使有效的方法更易于实施且更节省时间，而使无效的方法变得更困难且成本更高。除了这些简单直接但经常被忽视的改进外，其他几个领域也具有进一步丰富和发展的潜力，例如：

- 将地理空间（geo-spatial）和网络显示（network displays，如节点-链路图 node and link diagrams）与其他形式的显示相结合，以实现无缝交互和同步使用。
- 为协作式数据意义构建（collaborative data sensemaking）提供技术支持，以汇聚多个大脑的互补优势。
- 将数据可视化的应用从描述性统计（descriptive statistics）扩展到预测分析（predictive analytics）领域，例如通过使用交互式预测视觉模型。
- 将用于发现有意义模式的数据挖掘（data mining）算法与数据可视化更紧密地结合，从而为审查和探索这些模式提供更好的方式。
- 改进人机交互界面（human-computer interface）设备，以便以更快速、更无缝的方式与数据可视化进行交互。

所有这些方向在某种程度上都在被探索，但可以

若有更多研究人员专注于解决当今世界面临的实际问题，[相关成果]将能得到更迅速的转化与应用。

## 35.5 更多学习资源

许多大学已经开设了专门致力于数据可视化（Data Visualization）研究与推进的研究生项目。University of Maryland, Stanford, University of North Carolina, University of California, Berkeley 以及 Georgia Tech 是其中最顶尖的几所院校。尽管在计算机图形学（Computer Graphics）和人机交互（Human-Computer Interaction）等更广泛领域的若干期刊中包含关于数据可视化的文章，但只有一本学术期刊专门关注该领域：由 Palgrave Macmillan 每季度出版的 *Information Visualization Journal*。此外，还有一些规模较小的出版物致力于提高数据可视化的实用性，使其能被更广泛的受众所接触，例如 *Visual Business Intelligence Newsletter*。

专门针对该领域的会议也相对较少。其中最古老的 IEEE *VisWeek* 包含完全致力于数据可视化的 InfoVis 和 VAST (Visual Analytics Science and Technology) 分会，它仍然是规模最大且或许是质量最高的会议；但该领域的许多重要成果也会出现在其他视角更宽泛的会议中，例如 [CHI](https://www.interaction-design.org/literature/topics/human-computer-interaction) (Computer-Human Interaction) 和 SIGGRAPH。

### 35.5.0.1 CHI - 计算系统中的人类因素 (Human Factors in Computing Systems)

[2011](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2011_conference_on_human_factors_in_computing_systems.html)[2010](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2010_conference_on_human_factors_in_computing_systems.html)[2009](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2009_conference_on_human_factors_in_computing_systems.html)[2008](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2008_conference_on_human_factors_in_computing_systems.html)[2007](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2007_conference_on_human_factors_in_computing_systems.html)[2006](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2006_conference_on_human_factors_in_computing_systems.html)[2005](https://www.interaction-design.org/references/conferences/proceeding_of_the_sigchi_2005_conference_on_human_factors_in_computing_systems.html)[2004](https://www.interaction-design.org/references/conferences/proceedings_of_acm_chi_2004_conference_on_human_factors_in_computing_systems.html)[2003](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_2003_human_factors_in_computing_systems_conference.html)[2002](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_2002_conference_on_human_factors_in_computing_systems_conference.html)[2001](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_2001_human_factors_in_computing_systems_conference.html)[2000](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_2000_human_factors_in_computing_systems_conference.html)[1999](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_99_human_factors_in_computing_systems_conference.html)[1998](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_98_human_factors_in_computing_systems_conference.html)[1997](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_97_human_factors_in_computing_systems_conference.html)[1996](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_96_human_factors_in_computing_systems_conference.html)[1995](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_95_human_factors_in_computing_systems_conference.html)[1994](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_94_human_factors_in_computing_systems_conference.html)[1993](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_93_human_factors_in_computing_systems_conference.html)[1992](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_92_human_factors_in_computing_systems_conference.html)[1991](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_91_human_factors_in_computing_systems_conference.html)[1990](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_90_human_factors_in_computing_systems_conference.html)[1989](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_89_human_factors_in_computing_systems_conference.html)[1988](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_88_human_factors_in_computing_systems_conference.html)[1987](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_87_human_factors_in_computing_systems_conference.html)[1986](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_86_human_factors_in_computing_systems_conference.html)[1985](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_85_human_factors_in_computing_systems_conference.html)[1983](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_83_human_factors_in_computing_systems_conferenc.html)[198](https://www.interaction-design.org/references/conferences/proceedings_of_the_sigchi_conference_on_human_factors_in_computing_systems.html)

### 35.5.0.2 SIGGRAPH - 计算机图形学与交互技术国际会议 (International Conference on Computer Graphics and Interactive Techniques)

[2002](https://www.interaction-design.org/references/conferences/proceedings_of_the_29th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[2001](https://www.interaction-design.org/references/conferences/proceedings_of_the_28th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[2000](https://www.interaction-design.org/references/conferences/proceedings_of_the_27th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1999](https://www.interaction-design.org/references/conferences/proceedings_of_the_26th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1998](https://www.interaction-design.org/references/conferences/proceedings_of_the_25th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1997](https://www.interaction-design.org/references/conferences/proceedings_of_the_24th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1996](https://www.interaction-design.org/references/conferences/proceedings_of_the_23rd_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1995](https://www.interaction-design.org/references/conferences/proceedings_of_the_22nd_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1994](https://www.interaction-design.org/references/conferences/proceedings_of_the_21st_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1993](https://www.interaction-design.org/references/conferences/proceedings_of_the_20th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1992](https://www.interaction-design.org/references/conferences/proceedings_of_the_19th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1991](https://www.interaction-design.org/references/conferences/proceedings_of_the_18th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1990](https://www.interaction-design.org/references/conferences/proceedings_of_the_17th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1989](https://www.interaction-design.org/references/conferences/proceedings_of_the_16th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1988](https://www.interaction-design.org/references/conferences/proceedings_of_the_15th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1987](https://www.interaction-design.org/references/conferences/proceedings_of_the_14th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1986](https://www.interaction-design.org/references/conferences/proceedings_of_the_13th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1985](https://www.interaction-design.org/references/conferences/proceedings_of_the_12th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1984](https://www.interaction-design.org/references/conferences/proceedings_of_the_11th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1983](https://www.interaction-design.org/references/conferences/proceedings_of_the_10th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1982](https://www.interaction-design.org/references/conferences/proceedings_of_the_9th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1981](https://www.interaction-design.org/references/conferences/proceedings_of_the_8th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1980](https://www.interaction-design.org/references/conferences/proceedings_of_the_7th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1979](https://www.interaction-design.org/references/conferences/proceedings_of_the_6th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1978](https://www.interaction-design.org/references/conferences/proceedings_of_the_5th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1977](https://www.interaction-design.org/references/conferences/proceedings_of_the_4th_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1976](https://www.interaction-design.org/references/conferences/proceedings_of_the_3rd_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1975](https://www.interaction-design.org/references/conferences/proceedings_of_the_2nd_annual_conference_on_computer_graphics_and_interactive_techniques.html)[1974](https://www.interaction-design.org/references/conferences/proceedings_of_the_1st_annual_conference_on_computer_graphics_and_interactive_techniques.html)

### 35.5.0.3 InfoVis - IEEE Symposium on Information Visualization

[2005](https://www.interaction-design.org/references/conferences/infovis_2005_-_ieee_symposium_on_information_visualization.html)[2004](https://www.interaction-design.org/references/conferences/infovis_2004_-_10th_ieee_symposium_on_information_visualization.html)[2003](https://www.interaction-design.org/references/conferences/infovis_2003_-_9th_ieee_symposium_on_information_visualization.html)[2002](https://www.interaction-design.org/references/conferences/infovis_2002_-_2002_ieee_symposium_on_information_visualization.html)[2001](https://www.interaction-design.org/references/conferences/infovis_2001.html)[2000](https://www.interaction-design.org/references/conferences/infovis_2000.html)[1999](https://www.interaction-design.org/references/conferences/infovis_1999.html)[1998](https://www.interaction-design.org/references/conferences/infovis_1998_-_ieee_symposium_on_information_visualization.html)[1997](https://www.interaction-design.org/references/conferences/infovis_1997_-_ieee_symposium_on_information_visualization.html)[1995](https://www.interaction-design.org/references/conferences/infovis_1995_-_ieee_symposium_on_information_visualization.html)
值得关注的例外包括 Tableau Software 和 TIBCO Spotfire（两者均为学术研究的衍生产品 spin-offs）、源于对统计学深刻理解的 SAS JMP，以及其他几家规模相对较小的供应商（vendors）。

它们正逐渐从主导市场的大型软件公司——尤其是商业智能（Business Intelligence, BI）供应商——那里夺回它们应得的关注。除了产品供应商外，一些研究实验室和咨询公司也在为该领域的发展和应用做出贡献，包括 Microsoft Research, Pacific Northwest National Laboratory, Flowing Media, Oculus Info 和 Perceptual Edge。

关于数据可视化（Data Visualization）已经有几本优秀的著作。以下书籍按时间顺序排列，对于概览该领域以及作为基础指导来源尤其有用：

| [Tufte](https://www.interaction-design.org/references/authors/edward_r__tufte.html), Edward R. (1983): *The Visual Display of Quantitative Information.* Cheshire, CT, Graphics Press | Tufte 的四本书都非常出色，但第一本是最优秀的。它为图表卓越性（graphical excellence）提供了极具启发性的论证。 |
|---|---|
| [Cleveland](https://www.interaction-design.org/references/authors/william_s__cleveland.html), William S. (1994): *The Elements of Graphing Data.* Hobart Press | 专注于统计学家需求的数据可视化实践。 |
| [Harris](https://www.interaction-design.org/references/authors/robert_l__harris.html), Robert L. (2000): *Information Graphics: A Comprehensive Illustrated Reference.* Oxford University Press, USA | 一本关于信息图形（Information Graphics）的百科全书式参考书。 |

| [Card](https://www.interaction-design.org/references/authors/stuart_k__card.html), Stuart K., [Mackinlay](https://www.interaction-design.org/references/authors/jock_d__mackinlay.html), Jock D. and [Shneiderman](https://www.interaction-design.org/references/authors/ben_shneiderman.html), Ben (eds.) (1999): *Readings in Information Visualization: Using Vision to Think.* Academic Press | 截至出版日期，该书对该领域最优秀的学术研究进行了综述。 |
| [Few](https://www.interaction-design.org/references/authors/stephen_few.html), Stephen (2004): *Show Me the Numbers: Designing Tables and Graphs to Enlighten.* Analytics Press | 一本易懂、实用且全面的表格与图表设计指南，旨在用于沟通交流。 |
| [Ware](https://www.interaction-design.org/references/authors/colin_ware.html), Colin (2008): *Visual Thinking: for Design.* Morgan Kaufmann | 一本关于视觉感知（Visual Perception）与认知（Cognition）及其与数据可视化（Data Visualization）关系的精彩介绍。 |
| [Few](https://www.interaction-design.org/references/authors/stephen_few.html), Stephen (2009): *Now You See It: Simple Visualization Techniques for Quantitative Analysis.* Analytics Press | 一本易懂且实用的面向分析的数据可视化指南。 |

许多博客和在线讨论论坛都涉及数据可视化——其中一些基于专业知识且思考深入，而另一些则带有互联网上常见的浅薄。以下是其中一些最优秀的资源：

- [Tufte.com](http://www.tufte.com/) (Edward Tufte)
- [Perceptual Edge](http://www.perceptualedge.com/) (Stephen Few)
- [Eager Eyes](http://eagereyes.org/) (Robert Kosara)
- [Visual Complexity](http://www.visualcomplexity.com/vc/) (Manuel Lima)
- [Flowing Data](http://flowingdata.com/) (Nathan Yau)
- [Pictures of Numbers](http://www.numberpix.com/) (Mike Dickison)
- [Instant Cognition](http://blog.instantcognition.com/) (Clint Ivy)

## 35.6 References

[Card](https://www.interaction-design.org/references/authors/stuart_k__card.html), Stuart K., [Mackinlay](https://www.interaction-design.org/references/authors/jock_d__mackinlay.html), Jock D. and [Shneiderman](https://www.interaction-design.org/references/authors/ben_shneiderman.html), Ben (eds.) (1999): *Readings in Information Visualization: Using Vision to Think.* Academic Press
[Cleveland](https://www.interaction-design.org/references/authors/william_s__cleveland.html), William S. (1994): *The Elements of Graphing Data.* Hobart Press
[Few](https://www.interaction-design.org/references/authors/stephen_few.html), Stephen (2009): *Now You See It: Simple Visualization Techniques for Quantitative Analysis.* Analytics Press
[Few](https://www.interaction-design.org/references/authors/stephen_few.html), Stephen (2004): *Show Me the Numbers: Designing Tables and Graphs to Enlighten.* Analytics Press
[Harris](https://www.interaction-design.org/references/authors/robert_l__harris.html), Robert L. (2000): *Information Graphics: A Comprehensive Illustrated Reference.* Oxford University Press, USA
[Tufte](https://www.interaction-design.org/references/authors/edward_r__tufte.html), Edward R. (1983): *The Visual Display of Quantitative Information.* Cheshire, CT, Graphics Press
[Ware](https://www.interaction-design.org/references/authors/colin_ware.html), Colin (2008): *Visual Thinking: for Design.* Morgan Kaufmann
**Chapter TOC**

[**Human-Computer Interaction: The Foundations of UX Design**](https://www.interaction-design.org/courses/hci-foundations-of-ux-design)
![](https://public-media.interaction-design.org/images/courses/hds/course_72--square_thumbnail.jpg?tr=fo-auto)
Human-Computer Interaction: The Foundations of UX Design
Closes in
10
days
booked
View Course

## 获取每周用户体验洞察 (UX Insights)

加入 **314,524 位设计师** 的行列，通过我们的时事通讯 (newsletter) 获取有用的用户体验技巧 (UX tips)。
需要提供有效的电子邮件地址。

# 35.6 Ronald A. Rensink 的评述 (Commentary)

## 35.6.1 四个未来与一段历史

Stephen Few 对我们为何应该设计高效的数据可视化（data visualizations），以及在设计过程中理解人类感知（human perception）为何至关重要，提供了一个很好的概述。事实上，他的论述非常详尽，以至于我无法在其中增加太多内容。然而，我可以将这一核心观点进一步延伸，探讨他所讨论的时间段之前和之后的情况。延伸到那些不那么为人所知或尚未充分开发的领域，那里可能潜藏着新的机遇与危险……

也许最好的开始方式就是从起点开始。讨论可视化的起源并非没有困难，即便仅仅是因为存在几种不同类型的可视化——例如，数据可视化（data visualization）、信息可视化（information visualization）和科学可视化（scientific visualization）。但无论使用何种形容词，我们通常会发现其历史比人们普遍想象的要悠久得多。例如，尽管 Descartes 在 17 世纪为定量数据的图形化展示（graphic display of quantitative data）做出了贡献，但在三个世纪前，图表就已经被用来表示温度和光强等指标。事实上，正如 Manfredo Massironi 在其著作中讨论的那样（Massironi, 2002; p. 131），早在 11 世纪，位移（displacement）等物理量就被绘制成时间的函数。虽然这些事实本身很有趣，但更重要的一点是，图形表示（graphic representation）的技术

这些技术在几个世纪中不断发展，其中许多随后被遗忘——或许是因为不再流行，或者从一开始就未被广泛使用。但它们被摒弃的原因在当今时代未必适用。事实上，某些技术可能非常适合现代技术，因此值得以某种形式重新挖掘。像 Massironi 的著作这类书籍有助于发现这些可能性。

接下来探讨未来。或者更准确地说，探讨如何进一步建立可视化（Visualization）与心理学之间有益的联系。首先，视觉（Vision）与可视化之间存在着比目前更深层次的整合潜力；更多的处理工作可以被转移（Offloaded）到观察者的视觉皮层（Visual Cortex）中。正如 Stephen Few 所提到的，实现这一点的一种方法是利用简单的前注意属性（Preattentive Properties），如长度、方向和色调。但视觉科学（Vision Science）最近的研究表明，前注意层级的视觉能力包含比这丰富得多的视觉智能（Visual Intelligence）。其中，前注意过程可以判定阴影、提取三维方向，并将图像中分散的元素链接成统一的组。这些能力可以在更高性能的可视化中得到利用。另一个近期取得进展的领域是我们对视觉注意（Visual Attention）和场景感知（Scene Perception）的理解。我们对世界的视觉感知似乎基于一个

一种即时架构（just-in-time architecture），在这种架构中，注意力在正确的时间被引导至正确的对象。如果相关的协调机制（co-ordination mechanisms）能够得到正确处理，那么将有望以一种与观察物理世界一样自然且毫不费力的方式，来“观察”抽象数据集。（关于这些进展及其影响的简要概述可见 Rensink, 2002。）

另一个相关的机遇是更广泛地使用视觉类比（visual analogy）或隐喻（metaphor）。在这里，重点不再是绕过意识思考，而是使用最适合对视觉空间（visuospatial）对象和过程进行推理的思考模式。例如，在对物理力进行推理时，一个非常有效的隐喻是有向线或箭头。一个更现代的例子是桌面（desktop），它允许用户对计算机上可能的操作进行推理。与视觉感知（visual perception）的情况一样，迄今为止的许多——如果不是大多数——进展都是基于对相关机制相对浅层的理解。但鉴于认知科学家已经对隐喻有了更深入的了解，现在可能是时候考虑以一种更成熟的方式来使用它了。最终，可视化可能能够创建出与任何过程或任务的结构自然对应的心理表象（mental images）。（关于对此问题的有趣讨论，请参阅 Paley, 2009。）

第三个具有潜在重要性的方向是创建更强大的评估方法（evaluation methods），这些方法基于在……中开发的方法论（methodologies）

实验心理学（Experimental Psychology）。几个世纪以来，心理学家们一直在研究如何（以及不应如何）获取人类行为各方面的精确测量。从中借鉴将大有裨益。当然，其中一些技术已经被应用于评估（Evaluation）。但正如在认知与感知机制（Cognitive and Perceptual Mechanisms）方面一样，这里的知识迁移远未完成，仍有许多工作有待开展。例如，考虑评估一个给定的散点图设计（Scatterplot Design）在传达数据集相关性（Correlation）方面的效果。过去，这种评估是通过向观察者展示散点图，并要求其对（感知到的）相关性给出数值估计来完成的。但一种更强大的方法是借鉴测量最小可觉差（Just Noticeable Differences, JNDs）的实验方法：向观察者展示两个并排的散点图，并要求其选择相关性更高的一张。基于该方法的结果表明，所有相关性的精确度（Precision）和准确度（Accuracy）都可以由仅由两个参数（Parameters）控制的两个函数来定义。因此，一个给定的散点图设计仅凭两次简单的测量即可完成全面评估。（详情请参阅 Rensink and Baldridge, 2010。）

最后一个需要考虑的方向——或许也是最具挑战性的——是开发一种系统化的方法，以确保可视化设计（Visualization Designs）能够最优地（或至少是良好地）利用人类的感知与认知。理论上，这

可能会导致一种“设计科学（science of design）”的产生。在实践中，这可能无法实现，即便仅仅是因为可能的设计数量如此庞大，而我们对人类认知（human cognition）的理解还如此不完整。但我们可以借鉴其他几个设计领域的经验，旨在建立一套原则，至少能够约束需要考虑的可能性空间（space of possibilities）。例如，基于物理力（physical forces）或材料属性（material properties）的约束可以应用于任何建筑设计，以确定其是否可行（viable）。没有先验的（*a priori*）理由认为类似的方法不能同样适用于可视化（visualization）。

Bertin 的努力或许是这一方向的开端，他针对不同类型的问题可以采用的图形表示（graphic representation）类型提出了建议。Tufte, Mackinlay, Ware 等人的工作进一步扩展了这一领域。但无论这些建议多么有用，我们距离建立一个思考有效可视化的坚实基础还很遥远。许多基础性问题（foundational issues）仍未被充分理解。在可视化过程中究竟发生了什么？是否有一种方法能够精确且客观地描述这一过程？从原理上讲，是否可能确定一个给定的可视化方案是否以最优方式利用了观察者的感知与认知资源（perceptual and cognitive resources）？这些问题以及类似问题的答案将难以寻找，但它们将决定我们在多大程度上能够

使人类与机器能够充分结合各自的优势。

## 35.6.2 References

- Massironi, M. (2002). *The Psychology of Graphic Images: Seeing Drawing, Communicating*. Matwah NJ: Erlbaum.
- Paley, W.B. (2009). Interface and mind. *it – Information Technology*, **51**: 131-141.
- Rensink, R.A. (2002). Internal vs. external information in visual perception. *Proceedings of the Second International Symposium on Smart Graphics*: 63-70. [Smart Graphics 2; Hawthorne, NY, USA.]
- Rensink R.A., and Baldridge G. (2010). The perception of correlation in scatterplots. *Computer Graphics Forum*, 29: 1203-1210.

# 35.7 Commentary by Naomi B. Robbins

Stephen
 Few wrote an excellent description of data visualization and the 
necessity for designing graphics to take advantage of our knowledge of 
human perception and cognition. In this commentary I question who is 
responsible for the myriad of visualizations that ignore this knowledge:
 the software vendors, the software users or others? In addition, I 
point out important work that deserves greater exposure on the 
integration of geo-spatial and other forms of data display, a topic on 
Few's most-needed list. I end with additional sources for learning more.

## 35.7.1 许多数据可视化中知觉问题的责任归属

Few 的文章指出：
**“**自 21 世纪之交以来，数据可视化（data visualization）得到了普及，但由于是通过商业软件产品触达大众，其方式往往极其低效，令人遗憾。**”**
诚然，软件供应商应承担责任，因为他们提供了许多阻碍而非有助于读者理解数据的图表形式。供应商提供这些图表是为了让观众感到惊艳，而非为了清晰地传达信息，从而创造了对低效图表的需求。但他们并非是产生大量具有知觉问题（perceptual problems）的图表的唯一责任方。人们通过观察来学习，而他们看到了许多低效的图表。随后，软件用户便要求软件能够让他们模仿这些低效的设计。这使我们陷入了一个“鸡生蛋，蛋生鸡”（chicken and egg situation）的困境：供应商是因为客户的需求而制作这些糟糕的可视化图表，还是客户在看到供应商的市场推广后才被其吸引？

低效方式的一个例子包括柱状图（bar charts）中的伪三维（pseudo-third dimensions）。图 1 展示了 Excel 中的一个伪三维柱状图。几乎没有人能正确地解读它。我在 *Creating More Effective Graphs* [1] 中描述了该图表的其他问题。

![](https://www.interaction-design.org/images/encyclopedia/data_visualization_for_human_perception/three-dimensional-bar-chart-user-interface.jpg)

版权状态：未知（待调查）。请参阅下方 [版权条款](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/data-visualization-for-human-perception#copyrightNotice) 中的“例外（Exceptions）”部分。

图 35.1：几乎没有人能正确阅读这张简单的图表。绘制的数值分别是 1、2 和 3。如果你不相信，可以用 Excel 自己画一遍。

许多图形艺术家为数据可视化（Data Visualization）领域做出了重大贡献。然而，也有一些图形艺术家对数字缺乏认知，没有意识到图表中数字的呈现应当与其代表的数值成比例。因此，经常可以看到一些未按比例绘制（not drawn to scale）的图表。

一些图表设计者希望营造出比实际情况更好的性能印象，并故意设计具有误导性的图表以达到这一目的。另一些设计者可能更关注于展示其技术能力或艺术能力，而非清晰、准确地传递信息。直到最近，我们的教育体系尚未提供关于数字传递（communicating numbers）的培训。如今，虽然大学层面出现了一些优秀的课程，但大多数人几乎没有接受过关于呈现数值信息的培训。因此，许多图表设计者并不了解高效图表的原则。其中一些

问题源于缺乏校对（Proofreading）和粗心导致的错误。

作为类比（Analogy），目前时尚界的一种流行风格是高跟鞋。快速搜索“高跟鞋的危险”发现，高跟鞋穿着者的拇趾外翻（Bunion）手术数量有所增加，同时还伴有足部疼痛、背部疼痛和颈部疼痛。在某些情况下，跟腱（Achilles tendon）会变短。平衡能力受到影响，从而增加了跌倒的风险。问题清单不胜枚举。那么，对于这些医疗问题的增加，应该是鞋类设计师、鞋类制造商、销售鞋子的零售店，还是购买鞋子的消费者负责？这种情况是否与数据可视化（Data visualization）的问题类似？两者都造成了严重的后果：前者导致糟糕的商业决策，而后者则导致身体痛苦以及不必要的医疗费用。我希望这些问题能激发有趣的讨论。

## 35.7.2 地理空间显示与其他形式显示的集成

在关于未来方向的章节中，Few 提到了一些具有增强潜力的领域，包括将地理空间显示（geo-spatial displays）与其他形式的显示相结合，以实现无缝交互（seamless interaction）和同步使用。几位研究人员在该领域取得了进展。例如，Dan Carr [1] 和 [2] 的微地图（micromap）设计为统计信息增加了地理上下文（geographic context），从而允许对数据中的统计模式和地理模式进行联合探索（joint exploration）。如图 2 所示，统计图形（此处为点）通过颜色与小地图相链接。在第一行中，我们可以看到马里兰州（Maryland）由红点表示，因此在右侧的地图中，马里兰州被涂成了红色。通过按贫困水平排序，我们可以发现，贫困与教育不仅呈反比关系，而且美国南部各州在这些变量上存在地理聚类（geographic clustering）现象。

![](https://www.interaction-design.org/images/encyclopedia/data_visualization_for_human_perception/geo-spatial_displays_statistical_computing.jpg)
Copyright © Taylor and Francis. All Rights Reserved. Reproduced with permission. See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/data-visualization-for-human-perception#copyrightNotice) below.
图 35.2：来自 Carr 和 Pickle [1] 的微地图设计示例

## 35.7.3 更多学习资源

数据可视化（Data Visualization）并不属于单一的学术学科。统计学家、计算机科学家、心理学家、平面设计师以及其他专业人士都在从事数据可视化并为其做出贡献。Few 提到的大学课程和资源在很大程度上倾向于计算机科学。George Mason University、Iowa State 和 University of Augsburg 提供了一些将统计图形（Statistical Graphics）与计算机科学相结合的优秀课程。此外还有许多其他课程，我将把补充认知心理学（Cognitive Psychology）和平面设计领域优秀课程的任务交给其他评论者。由 American Statistical Association、Institute of Mathematical Statistics 和 Interface Foundation of North America 联合出版的 *The Journal of Computational and Graphical Statistics* 是该主题的另一本学术期刊。*Statistical Computing Statistical Graphics Newsletter (SCGN)* 是另一份非正式出版物。尽管 Joint Statistical Meetings 并非专门致力于统计图形和数据可视化，但由 Statistical Graphics Section 赞助的分会场数量之多，足以抵得上许多小型会议的全部内容。

对于“需求清单”，我想补充的一点是：计算机科学家、平面设计师、心理学家和统计学家之间需要更好的沟通。增加联合会议以及参加彼此的会议，将有助于每个学科从其他学科的研究中获益。

## 35.7.4 References

1. Carr, Daniel B. and Linda Williams Pickle. 2010*. Visualizing Data Patterns with Micromaps. *Chapman and Hall/CRC, Boca Raton, FL.
1. Carr DB, Wallin JF and Carr DA. Two new templates for epidemiology
applications: Linked micromap plots and conditioned choropleth maps. *Statistics in Medicine* 19:2521-38, 2000.
1. Robbins, Naomi B. 2005. *Creating More Effective Graphs*. John Wiley and Sons, Hoboken, NJ.

# 35.8 Commentary by Robert Kosara

## 35.8.1 隐喻与交互（Metaphors and Interaction）

Stephen Few 在他那篇写得非常出色且详尽的文章中仅简要提及的一个重要话题是交互（Interaction）。虽然静态图表和可视化无疑是有用的，但它们几乎没有利用到我们今天可以轻易获得的强大计算能力。可视化中的交互能够让用户快速探索并发现那些甚至出乎其意料的数据模式（Data Patterns）。此外，交互还可以减少同时显示的数据量，从而提供更清晰的可视化效果，同时仍允许用户在任何时候按需（On demand）获取相关信息。

Ben Shneiderman 在他著名的视觉信息检索格言（Visual Information Seeking Mantra）中概括了交互的作用 (Shneiderman, 1996)：*先概览，再缩放与过滤，最后按需查看细节（overview first, zoom and filter, then details on demand）*。抽象信息空间（Abstract Information Spaces）需要一个概览，以便用户了解在哪里可以找到数据，但随后需要通过缩放（Zoom）来查看细节。在处理大规模数据集时，数据过滤（Filtering）至关重要。最后，用户可以根据需要检索关于已显示（以及未显示）内容的详细信息。所有这些步骤都需要交互，即用户告知可视化系统其想要看到的内容。

## 35.8.2 简单交互（Simple Interactions）

最简单的交互包括工具提示（Tooltips）或其他在用户指向可视化（Visualization）的某个部分时出现的数据显示（Data displays）。以 Few 上述文章中的死亡原因条形图（Bar chart）为例：数值可以完全按需（On demand）显示，且可能不仅包含百分比，还包含总数。此外，可以从激活条形（Active bar）的末端向顶部的刻度（Scale）绘制一条垂直线，以便在整体语境（Context）中更轻松地观察条形。

这种类型的交互毫不费力且易于发现：只需将鼠标移至显示区域，观察是否会发生某些变化即可。在图表中显示数值也非常普遍。但真正的强大之处在于更高级的交互。

## 35.8.3 联动与刷选（Linking and Brushing）

刷选（Brushing）允许用户选择数据点，并使这些点在同一数据的一个或多个视图中被高亮显示。当涉及多个视图时，所有视图都高亮显示相同数据点这一特性通常被称为联动（Linking）（而这些视图被称为协调多视图（Coordinated Multiple Views））。

请看这个关于泰坦尼克号乘客数据的联动柱状图示例。每个柱状图代表一个数据维度（Data Dimension）（如舱位等级、性别、年龄和是否生存），并以直方图（Histogram）的形式显示每个类别中的人数。

![](https://www.interaction-design.org/images/encyclopedia/data_visualization_for_human_perception/linked-barcharts-overview-first-zoom-and-filter-then-details-on-demand.jpg)
图片由 Robert Kosara 提供。版权状态：未知（待调查）。请参阅下方[版权条款](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/data-visualization-for-human-perception#copyrightNotice)中的“例外（Exceptions）”章节。
图 35.1

为了找出每个类别中生存的人数，我们将选择相关的柱条，这将对所有视图中的这些数据点进行刷选。现在，我们可以通过观察各自柱条的高亮程度，来比较不同性别、舱位等级等的生存率。

![](https://www.interaction-design.org/images/encyclopedia/data_visualization_for_human_perception/linked-barcharts-brushed-overview-first-zoom-and-filter-then-details-on-demand.jpg)
由 Robert Kosara 提供。版权状态：未知（待调查）。请参阅下方 [版权条款（copyright terms）](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/data-visualization-for-human-perception#copyrightNotice) 中的“例外（Exceptions）”章节。

图 35.2

对于单个数据点而非本例中的汇总数据（summary data），其机制非常相似。刷选与链接（Brushing and linking）使得通过尝试不同的可能性来发现数据中的高维关系（high-dimensional relationships）成为可能。

## 35.8.4 隐喻与结构（Metaphors and Structure）

隐喻在可视化（visualization）领域有着较为复杂的历史。甚至对于什么是“隐喻”，人们还没有达成清晰的共识：许多人在讨论视觉隐喻（visual metaphors）时，指的是描绘数据的不同方式；而另一些人则将其专门用于指代某种带有装饰性的可视化（例如，用花朵的生长来代表聊天室的流量等）。

我在这里想要探讨的是两者的结合，或许可以用“结构（structure）”来概括：可视化中元素之间的关系如何影响人们读取数据的方式？Caroline Ziemkiewicz 和我曾就这一主题开展研究，并发现宏观结构所起的作用比大多数人预想的要大。

在比较不同类型的树形可视化（tree visualizations）时，我们发现不同的研究对于哪种方法更有效得出了不同的结论，而这取决于问题中使用了哪种隐喻：是“A 被包含在 B 中”，还是“A 在层级（hierarchy）结构中位于 B 之下”。我们进行了一项研究，发现问题中使用的语言隐喻（linguistic metaphor）与可视化的视觉隐喻之间确实存在一种兼容性效应（compatibility effect）（Ziemkiewicz and Kosara, 2008）。

我们最近的研究表明，可视化对象之间存在一种明显的重力（gravity）效应，这可能会扭曲对距离的感知（Ziemkiewicz and Kosara, 2010）。

## 35.8.5 未来

虽然我们已经掌握了许多创建合理的可视化（Visualizations）的方法，但仍有许多我们未知或尚未意识到的领域。即使是像可视化布局（Layout）如何影响我们对数据的解读这样看似基础的知识，仍需要进一步研究，以便将其转化为有用的建议和最佳实践（Best Practices）。

交互（Interaction）在可视化研究中并非一个全新的课题，但在许多可视化和图表程序中，其实现仍然相当基础。为了真正释放可视化的潜力，这些程序需要更先进的功能，以及引导用户了解其交互特性的方法。可视化所能提供的价值远超大多数人目前的认知。

## 35.8.6 References

- Shneiderman, Ben (1996): The Eyes Have It: A Task by Data Type Taxonomy for Information Visualizations. In: [VL 1996](https://www.interaction-design.org/references/conferences/vl_1996.html) 1996. pp. 336-343.
- Caroline Ziemkiewicz, Robert Kosara, [The Shaping of Information by Visual Metaphors](http://kosara.net/papers/2008/Ziemkiewicz_InfoVis_2008.pdf), Transactions on Visualization and Computer Graphics (Proceedings InfoVis), vol. 14, no. 6, pp. 1269-1276, 2008.
- Caroline Ziemkiewicz, Robert Kosara, [Laws of Attraction: From Perceived Forces to Conceptual Similarity](http://kosara.net/papers/2010/Ziemkiewicz_InfoVis_2010.pdf), Transactions on Visualization and Computer Graphics (Proceedings InfoVis), vol. 16, no. 6, pp. 1009-1016, 2010.

## 本书章节涵盖的主题：

[数据可视化 (Data Visualization)](https://www.interaction-design.org/literature/topics/data-visualization)[
                        视觉感知 (Visual Perception)](https://www.interaction-design.org/literature/topics/visual-perception)[
                        用户体验 (User Experience, UX) 设计](https://www.interaction-design.org/literature/topics/ux-design)[
                        人机交互 (Human-Computer Interaction, HCI)](https://www.interaction-design.org/literature/topics/human-computer-interaction)[
                        设计史 (Design History)](https://www.interaction-design.org/literature/topics/design-history)[
                        视觉表征 (Visual Representation)](https://www.interaction-design.org/literature/topics/visual-representation)
