# 22. 卡片分类法（Card Sorting）

**来源**：The Encyclopedia of Human-Computer Interaction, 2nd Ed.
**Notion 原页面**：https://www.notion.so/7710eb7fef8a4bd0a856d0e169ce57be

---

[William Hudson](https://www.interaction-design.org/literature/author/william-hudson)

“卡片分类法（Card Sorting）”这一术语适用于涉及对象或概念的分组和/或命名的多种活动。这些对象或概念可以用实体卡片、计算机屏幕上的虚拟卡片，或者实体或数字形式的照片来表示。有时，对象本身也可以被分类。结果可以通过多种方式表达，其核心关注点在于参与者最频繁地将哪些项目分在一起，以及为生成的类别所赋予的名称。

在交互设计（Interaction Design）中，由交互方案的潜在用户执行的分类过程可以提供：
- 术语（Terminology）：即人们如何称呼事物
- 关系（Relationships）：如邻近性（Proximity）和相似性（Similarity）
- 类别（Categories）：即分组及其名称

我们可以利用这些信息来决定在界面显示中应将哪些项目分在一起；菜单内容应如何组织和标注；以及最根本地，我们应该使用什么样的词汇来描述用户关注的对象。

## 22.1 一个实际案例

想象一下，你负责设计如图 1 所示的、在大型超市中日益普及的计算机化触摸屏电子秤的[信息架构（Information Architecture）](https://www.interaction-design.org/literature/topics/information-architecture)。该屏幕一次显示 12 张图像及其标题。目前有一些投诉称，顾客在电子秤前停留时间过长，并且对类别的组织方式感到沮丧。表 1 显示了顾客需要查找的示例项目列表。这些项目被打印在带有条形码的卡片上，以便于数据采集（Data Capture）（见图 2 和 Syntagm 网站 [http://www.syntagm.co.uk/cardsorting](http://www.syntagm.co.uk/cardsorting)）。图 3 展示了将卡片组织成组的示例。由于这是一个“开放式”分类（Open Sort），用户可以自行创建组并为其命名。这种特定的分组代表了目前电子秤中实现的解决方案，被称为“参考分类（Reference Sort）”，将在本章后面讨论。

![](https://public-media.interaction-design.org/images/encyclopedia/card_sorting/supermarket_scale.jpg)
作者/版权持有者：William Hudson。版权条款和许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。

![](https://public-media.interaction-design.org/images/encyclopedia/card_sorting/card_sorting_categories_supermarket_scale.jpg)
作者/版权

版权持有者：William Hudson。版权条款与许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

**图 22.1 A-B**：显示水果和蔬菜类别的计算机化超市电子秤（触摸屏）

西兰花 / Calabrese
柠檬
胡萝卜
荔枝
辣椒
蘑菇
西葫芦 / Zucchini
洋葱
茴香（球茎）
橙子
大蒜
欧防风
生姜
土豆
葡萄柚
南瓜
葡萄
倭瓜 / Marrows
奇异果
芜菁 / Rutabaga
韭葱
芜菁

**表 22.1**：超市电子秤中可找到的项目示例列表（参见图 1）

![](https://public-media.interaction-design.org/images/encyclopedia/card_sorting/card_sorting_with_machine_readable_bar_codes.jpg)

版权持有者：William Hudson。版权条款与许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

**图 22.2**：带有条形码的示例卡片，用于简化数据采集（Data Capture）（条形码以机器可读的形式提供项目编号）

![](https://public-media.interaction-design.org/images/encyclopedia/card_sorting/sample_cards_for_card_sorting.jpg)

版权持有者：William Hudson。版权条款与许可：保留所有权利。

保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

**图 22.3**：分组排列的示例卡片

请花一点时间思考，如果你自己会如何组织这些项目。对大多数人来说，至少可以分为两组——水果和蔬菜。但在大型超市中，这两组将包含非常长的[列表（lists）](https://www.interaction-design.org/literature/topics/lists)，如果没有进一步的细分，将毫无帮助。此外，可能有一些你不熟悉的术语。Courgette 是英国超市中常见的那种长绿色西葫芦（squash）的法语名称，而 zucchini 则是美国使用的意大利语名称。相反，在美国被称为 rutabaga 的蔬菜在英国被称为 swede，因为它是由瑞典人引入苏格兰的。如果预先知道这类简单的语言差异，在同一张卡片上列出替代名称可能是一个令人满意的解决方案。然而，在全新的问题域（novel problem domains）或术语问题较为严重的多元文化/多语言环境下，让参与者对照片甚至实物（附带条形码标签）进行分类可能会更好。

无论你对什么进行分类，最终都会将一些项目（items）排列成组，理想情况下每组还应有组名。接下来的挑战是如何理解这些结果，特别是当你

拥有数十或数百名参与者。无论如何进行分析，我们至少想要了解两件事：
- 分组的名称是什么，以及每个组中包含哪些内容？
- 哪些项目最经常被分在同一组中？

请注意，这是两组独立的信息。在示例研究中，西柚和橙子总是被分在一起，这一事实不受所使用的不同分组名称的影响。此外，不出所料，其他项目也会与西柚和橙子分在一起——但这些项目的性质随参与者采取的方法而有所不同。如果该组被简单地命名为“水果（fruit）”，那么除了西柚和橙子，它还包含苹果、梨和其他水果。如果它被命名为“柑橘类（citrus）”，那么唯一增加的项目是柠檬。因此，为了深入了解分类（sort）结果向我们揭示的信息，我们需要使用不同类型的分析方法。前两种分析方法分别对应于我们想要了解的两件事：
- **项目-分组（items by groups）**图表显示了分组的名称及其包含的内容。
- **项目-项目（items by items）**图表显示了哪些项目最经常被分在一起。

### 22.1.1 元素分组图（Items by groups chart）

您可以使用铅笔和纸，或者电子表格和打印机自行制作这些图表的简单版本。首先是元素分组图（Items by groups chart）：

- 将所有被分类的元素列在页面的左侧。为了能够快速找到每个元素，建议按字母顺序排列（可以使用文字处理或电子表格软件辅助排序）。
- 浏览分类结果，为每个新组编写一个列标题。在属于该组的每个元素单元格中做标记。例如，如果第一个组名为“柑橘类水果（Citrus Fruit）”，我们就将其写为列标题，然后标记橙子、柠檬和葡萄柚的单元格。图 4 展示了该示例。

![](https://public-media.interaction-design.org/images/encyclopedia/card_sorting/groups_worksheet.jpg)
作者/版权持有者：William Hudson。版权条款和许可：保留所有权利。经许可转载。详见下文 [版权条款](https://www.interaction-design.org/about/terms-of-use) 中的“例外”部分。

**图 22.4**：部分完成的元素分组工作表（针对单个组——柑橘类水果）

- 如果另一位参与者使用了相同的组名（或者是在您已提供所有组名的“封闭式分类（Closed Sort）”中），您只需编写一次列标题。然而，对于“开放式分类（Open Sort）”，请做好面对拼写和措辞多样性的准备。例如，“软果类（soft fruit）”。

与“浆果（berries）”相对。通常最好的做法是在数据采集（Data Capture）过程中将这些不同的术语分开，并在稍后阶段决定是否合并结果。

- 如果我们使用聚类分析（Cluster Analysis，后文将讨论）来重新排列项目，将会得到一个类似于图 5 所示的图表。它的布局与图 4 中的工作表相同——项目列在左侧，分组排列在顶部。在图表的主体部分，方格单元格代表每个项目在指定分组中出现的次数，通过所选颜色的深浅来表示——这对应于你在手动生成版本中会做的标记数量。（在应用程序中，点击单元格即可查看百分比值；图中显示的是“胡萝卜（Carrots）”在“根茎类蔬菜（Root Veg）”组中的结果。）表 2 提供了关于所用阴影深浅的更多细节。

![](https://public-media.interaction-design.org/images/encyclopedia/card_sorting/groups_chart_26_participants.jpg)
作者/版权持有者：William Hudson。版权条款和许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 22.5**：包含 26 名参与者的水果和蔬菜样本的项目-分组图（Items by groups chart）（SynCaps V2）

![](https://public-media.interaction-design.org/images/encyclopedia/card_sorting/legend_items_charts_card_sorting.jpg)

**表 22.2**：包含 26 名参与者的水果与蔬菜样本的分组项目图表 (SynCaps V2)

### 22.1.2 项与项对照表（Items by items chart）

制作项与项对照表（Items by items chart）稍微具有挑战性：
- 将参与者分类的所有项目按字母顺序排列在页面的左侧。在页面顶部以相同的顺序重复该列表。现在你得到了一个项目矩阵（Matrix of items）。为了避免混淆和重复工作，请在对角线（Diagonal）——即每个项目与自身相交的位置——画一条线，从左上角延伸至右下角，并决定使用矩阵的哪一半。然后将另一半涂上阴影。这样可以强制你将“橙子”x“葡萄柚”与“葡萄柚”x“橙子”记录在同一个位置。最终你将得到一个类似于图 6 所示的工作表。矩阵的右上部分已置灰，将不被使用。

![](https://public-media.interaction-design.org/images/encyclopedia/card_sorting/worksheet_items_by_items_chart_created_with_MS_Excel.jpg)
作者/版权持有者：William Hudson。版权条款和许可：保留所有权利。经许可转载。详见下文[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。
**图 22.6**：项与项对照表工作表（使用 MS Excel 创建）

![](https://public-media.interaction-design.org/images/encyclopedia/card_sorting/Item_pairings.jpg)
作者/版权持有者：William Hudson。版权条款和许可：所有权利保留

保留所有权。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”部分。

**图 22.7**：一组 12 个项目（“蔬菜”）的项目配对（Item Pairings）

- 使用排序后的卡片（Sorted Cards），在每个单元格中为出现在同一组中的每对项目做一个标记。例如，如果我们遇到一个名为“柑橘类”的组，其中可能包含葡萄柚、橙子和柠檬，那么我们就需要标记“葡萄柚 x 橙子”、“葡萄柚 x 柠檬”以及“橙子 x 柠檬”这些单元格。这是一个简单的例子；对于较大的组，需要标记的数量很多：$(n^2 - n) / 2$。这是因为我们需要所有可能的配对 ($n^2$)，但要排除项目与自身的配对 ($-n$)，且我们不需要区分配对的顺序——因此“苹果 x 梨”与“梨 x 苹果”是相同的。这使得我们可以将矩阵（Matrix）减半，从而减少需要标记的数量（即公式中的 $/2$）。因此，如果你有一组 8 个项目，请准备好铅笔，准备在 28 个单元格中做标记。12 个项目则会产生 66 个标记，如图 7 所示。（请记住，这些是单个参与者的数值。你可以在每个单元格中保持累计总数，或者在处理后续参与者时添加额外的标记。或者，为每位参与者使用一张单独的表格，最后将结果相加。这种方法的明显优势在于允许你发现并修正...）

（错误，以及对参与者的分类方法进行视觉对比。）
- 对所有参与者重复此操作。完成后，每个单元格中的标记数量代表参与者将该项对（item pairs）分在同一组中的频率。这被称为“项与项”（items by items）图（或称“项对”图（pairs chart））。图 8 展示了一个计算机生成的版本，其中的项目使用了聚类分析（cluster analysis）进行了重新排序。项目名称显示在对角线上，而不是分别为行和列贴标签。请注意，由于我们移除了矩阵的一半，大多数项目在对角线处是折叠的。例如，“胡萝卜（Carrots）”开始于左侧的一行，然后在对角线处变为向下延伸的一列。图中的虚线将聚类（clusters）分开——这是基于参与者创建组的平均数量（四个）。
- 与“项与组”（items by groups）图（图 5）一样，正方形单元格通过所选颜色的深浅来表示参与者的百分比，详见表 2。然而，在“项与项”图中，每个单元格代表一对被分在同一组中的项目。

![](https://public-media.interaction-design.org/images/encyclopedia/card_sorting/sort_Items_by_items_chart_red_line.jpg)
作者/版权持有者：William Hudson。版权条款和许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。
**图 22.8**：

26 名参与者的水果与蔬菜样本逐项分析图 (Item-by-item chart) (SynCaps V2)（红色方框显示了“胡萝卜”的完整数据）

## 22.2 分析结果的含义

虽然人们很容易认为卡片分类（Card Sorting）项目能立即提供一个[导航层级（Navigation Hierarchy）](https://www.interaction-design.org/literature/topics/navigation-1)，但事实并非如此。分析结果是为[设计流程（Design Process）](https://www.interaction-design.org/literature/topics/design-process)提供参考，而非提供一个现成的解决方案。这里描述的水果和蔬菜示例项目提供了一个现实的案例——其结果远非定论。

从分析中我们可以确定什么？在继续之前，请回顾图 5 和图 8，看看你能得出什么结论。

两张图表都包含了将项目分为四个组的聚类分析（Cluster Analysis）结果。“按组划分的项目”图表（图 5）显示，这四个组最受欢迎的名称分别是“水果（Fruit）”、“香料（Spices）”、“蔬菜（Vegetables）”和“根茎类蔬菜（Root Veg）”。对于葡萄柚、橙子和柠檬，“柑橘类水果（Citrus Fruit）”是一个强有力的竞争名称，而一些参与者（约三分之一）没有区分“根茎类蔬菜”和“蔬菜”。

还有其他的吗？茴香（fennel）的情况如何？在两张图表中，应该可以看到茴香被分到了多种不同的项目中。尽管聚类分析将其归入名为“香料”的组，但几乎有 20% 的参与者将其分类到“蔬菜”组中。除在两个组中都提供进入茴香的路径外，我们可能对此无能为力——这在...上很容易实现

计算机量表或网站。

暂时关注于“项对项图表（items by items chart）”，我们可以发现项目本身的一个重要特征——这一特征独立于组名。极少有参与者尝试将水果与任何蔬菜归为一类。这表明参与者对这两个主类别有清晰的理解和区分，我们在设计合适的信息层级（Information Hierarchy）时，理应基于此点进行构建。相比之下，图表显示参与者在对待洋葱和韭葱时存在相当大的模糊性。这些项目经常被归入根茎类蔬菜，但项对项图表显示它们（尤其是洋葱）与最常被称为“香料（spices）”的组别具有关联性（Affinity）。

我们可以从这个例子中得出什么结论？首先，虽然我们深入了解了参与者对术语、类别和概念的认知，但由于本次练习的规模过于有限，其结果无法直接应用于更大的信息空间（Information Space）。具体而言，示例中提供的水果数量较少，这促使参与者将它们全部放入同一个组中。这在实践中可能并不现实，尽管我们确实有一些细化建议——例如图 5 中的“柑橘类水果（Citrus Fruits）”和“浆果（Berries）”。一种解决方案是为参与者提供更广泛的水果范围，包括我们预期类别的所谓典型样本（Exemplars，即代表性类型）。另一种方法则是简要地……

能够更密切地监测参与者。这在在线分类活动（online sorting activity）中很难实现——即使指导说明（briefing）非常详细，参与者也可能忽略、未阅读或未按照说明操作。这些问题在面对面分类（face-to-face sorting）中大多可以得到解决。如果引导者（facilitators）发现参与者创建的类别（categories）过少，他们可以简单地引导参与者创建更多类别。

到目前为止，我们已经触及了两种常用的卡片分类（card sorts）分析方法——其他方法将在稍后讨论。但首先，让我们了解一些背景知识……

## 22.3 卡片分类法的历史（The History of card sorting）

卡片分类法（Card Sorting）有着令人惊讶的悠久历史，尤其是如果将分类（Categorization）的概念包含在内的话。古希腊人被认为在类别的早期开发中做出了贡献，其中 [Aristotle](https://www.interaction-design.org/literature/topics/aristotle) 为我们今天用于动植物的分类方案奠定了基础 (Sachs 2002)。在社会科学中进行卡片分类的实践则相对较晚，但仍有 100 多年的历史。最初，印制的扑克牌被用于初创时期的心理学领域中的各种实验 (Jastrow 1886)，但很快，研究人员开始使用空白卡片，在上面写下单词，由受试者进行分类 (Bergström 1893)。早期的卡片分类活动主要关注于确定受试者的特征——例如，将分类速度作为[心理过程（Mental Processes）](https://www.interaction-design.org/literature/topics/mental-processes)和反应时间（Reaction Time）的指标 (Jastrow 1886; Jastrow 1898)；记忆功能（Memory Function）(Bergström 1893; Bergström 1894) 以及通过卡片上的墨迹（Inkblots）来测试想象力 (Dearborn 1898)。其中一些实验演变成了现在被认为是针对头部受伤患者神经损伤（Neurological Damage）的标准[测试（Test）](https://www.interaction-design.org/literature/topics/test)，即威斯康星卡片分类测试 (Wisconsin Card Sorting Test) (Eling et al. 2008)。事实上，卡片

卡片分类（Card Sorting）在心理学领域广受认可，早在 1914 年，*Science* 杂志就发表了一篇推崇各类基于卡片活动之优点的文章 (Kline and Kellogg 1914)。

卡片分类随后也被引入其他领域：犯罪学 (Galton 1891)、[市场研究（Market Research）](https://www.interaction-design.org/literature/topics/market-research) (Dubois 1949)、语义学 (Miller 1969)，并成为社会科学中一种标准的定性工具（Qualitative Tool） (Weller and Romney 1988; Bernard and Ryan 2009)。然而，直到 20 世纪 90 年代初万维网（World Wide Web）出现，卡片分类才被应用于组织信息空间（Information Spaces）的任务 (Nielsen and Sano 1995)；一个极少数的例外是 Tom Tullis 在 20 世纪 80 年代初将卡片分类应用于操作系统的菜单设计 (Tullis 1985)。

### 22.3.1 卡片分类法与交互产品设计

尽管 Web 如此普及，但卡片分类法（Card Sorting）在交互产品（Interactive Products）设计中仍然是一个使用不足的工具。在针对 2008 年 [Usability](https://www.interaction-design.org/literature/topics/usability) Week 217 位参会者的调查中，Nielsen Norman Group 报告称，每年进行的卡片分类平均次数仅为 2 次。虽然这一频率是该调查中眼动追踪研究（Eye-tracking studies，平均每年 1 次）的两倍，但考虑到该方法不需要大量的前期投入，这个数字低得令人惊讶。事实上，自诞生以来，卡片分类法在交互 [产品设计](https://www.interaction-design.org/literature/topics/product-design)（Product Design）中仅扮演了边缘角色——这或许反映了以用户为中心的设计（User-centred Design）方法在整体上的普及程度有限。Peter Morville 和 Louis Rosenfeld 在他们的开创性著作 *Information Architecture*（现已出到第三版，Morville and Rosenfeld 2006）中仅用了寥寥几页来讨论卡片分类法。且在撰写本文时，关于交互系统设计中卡片分类法的书籍仅有一本，即 Donna Spencer 的 *Card Sorting: Designing Usable Categories* (Spencer 2009)，该书在分析方面倾向于较为保守。

## 22.4 卡片分类法的优势

对于交互设计（Interaction Design）、[用户研究（Customer Research）](https://www.interaction-design.org/literature/topics/customer-research)或社会科学研究而言，在处理大量概念时，很少有调查技术能像卡片分类法（Card Sorting）那样有效。在面对面的场景中，操作和标注实体卡片是一个相当自然且无压力的过程：观察用户参与这一过程可以为研究人员带来许多洞察，并为关于所研究的问题域（Problem Domain）以及用户本身的提问和对话提供丰富的素材。这些成果和机会很难通过访谈、问卷和可用性评估（Usability Evaluations）来获得，尽管这些替代方案在范围较小的调查中各有其优势。例如，在可用性研究中，发现单个菜单项标注错误相对容易，但如果要检查几十个项目，其成本则高得令人难以承受。

## 22.5 定性与定量结果

在一个极端情况下，卡片分类法（Card Sorting）可以以一对一的方式进行，将其作为一种探索（知识提取，Knowledge Elicitation）的工具，以及在参与者和研究人员之间产生有意义讨论的手段 (Weller and Romney 1988; Bernard and Ryan 2009)。此类研究的结果通常是从用户的视角更好地理解问题域（Problem Domain），并通过最终形成的组别来表达术语、关系和类别。在另一个极端，组织数百名参与者进行在线分类（Online Sorts）则非常容易，以此来探索所呈现的术语和概念是否在广大用户群体中得到了充分理解 (Fincher and Tenenberg 2005)。虽然一对一方法的结果主要是[定性的（Qualitative）](http://en.wikipedia.org/wiki/Qualitative_research)，但大规模在线研究的结果则大多是[定量的（Quantitative）](http://en.wikipedia.org/wiki/Quantitative_research)。（请注意，从在线研究中获取定性信息并非不可能；只是说引导或允许在线参与者提供有用反馈的机会相对较少。）

## 22.6 分类内容的选取

不出所料，让参与者对什么内容进行分类，很大程度上取决于研究人员、信息架构师（Information Architect）或交互设计师（Interaction Designer）试图发现什么。对于“绿地项目（Green-field projects）”——即那些不受先前工作约束的全新项目——首要任务是建立一套词汇表（Vocabulary）。在这种情况下，可以让用户面对物体、图像或项目的描述，并要求他们为其命名。命名之后，可以将它们进行分组，并依次为这些组命名。这在面对面（Face-to-face）的场景中非常容易实现，可以通过在物体或照片上贴上编号或条形码标签来完成（例如，可参阅 [Syntagm 网站](http://www.syntagm.co.uk/cardsorting) 提供的 Microsoft Word 卡片分类模板）。请注意，一些基于 Web 的分类工具（如 [websort.net](http://www.websort.net/)）虽然允许对照片进行分类，但没有提供让用户为所描绘的项目命名的手段。

- **固定项目（Fixed Items）：** 如果术语已经确定且不可更改（例如产品名称），那么上述的基础研究就不是必要的。此时，分类活动的主要目标将是发现哪些项目应该被分在同一组，以及这些组应该如何命名。无论是采用面对面还是在线方法，这都是一项相对简单的任务。选择哪种方法很大程度上取决于是否需要定性反馈（Qualitative feedback）（为此，采用面对面分类...

（纸质卡片最为合适），或者是否需要通过增加参与者人数来获取有益的定性反馈（qualitative feedback）。在面对面的环境下，15-30 名参与者即可获得高质量的结果 (Nielsen 2004; Tullis and Wood 2004)，而在线分类（online sorts）则可以针对数百名参与者进行，除了招募成本外无需额外费用。此外，大规模研究有助于提高组织内部的参与度，或确保不同类型的用户对问题领域（problem domain）具有相似的理解。

- [**用户目标（User Goals）**](https://www.interaction-design.org/literature/topics/user-goals)**：卡片分类（Card sorting）经常被应用于导航设计（navigation design）。然而，仅仅列出解决方案中将包含的文档、页面或功能名称，并不能保证用户能够达成其目标，即使这些内容经过了最优化的组织。从用户目标入手有助于确保导航设计的有效性。因此，与其要求参与者对诸如“员工手册”、“员工政策”和“人力资源指南”（这些项之间存在令人困惑的重叠）等项目进行分类，不如考虑用户在访问这些文档时的目标，例如：“查询假期额度”、“我可以居家办公吗？”、“新生儿假可以请多久？”等等。(Tom Tullis 在其操作系统菜单设计中采用了用户目标 —— 参见 Tullis 1985)。服务器日志（Server logs），

特别是搜索词、内容审计以及[用户研究（User Research）](https://www.interaction-design.org/literature/topics/user-research)可用于构建用户目标列表，而卡片分类法（Card Sorting）则可提供分组和类别名称。
- **多级层级（Multilevel Hierarchies）：** 大多数分类和分析工具不支持除最简单的交互方案外，在几乎所有交互方案中都能见到的那种多级层级结构。即使是示例卡片分类法中使用的农产品秤（produce scales）也可以采用多级层级。例如，一个名为“水果”的顶层类别可能会引导至“柑橘类水果”、“苹果和梨”、“异域水果”等。然而，缺乏对多级层级的分析支持并不是一个无法解决的问题。事实上，在分析阶段采用多级层级会显著增加分类活动的复杂性，从而使许多参与者感到这项任务艰巨。相反，应开展多次单级分类活动。重点关注最低层级（即导航树的“叶子”节点），因为正如我们在示例中所见，参与者提供的类别名称在抽象层级（Levels of Abstraction）上往往存在显著差异。参与者的类别名称包括“水果”、“软果”和“浆果”，其中任何一个都可能适用于更高层级的导航标题。（多级分类在 *Section 9, Advanced analysis* 中有更详细的讨论。）

## 22.7 如何进行卡片分类（Card Sorting）

![](https://public-media.interaction-design.org/images/encyclopedia/card_sorting/card_sorting_1.jpg)
![](https://public-media.interaction-design.org/images/encyclopedia/card_sorting/card_sorting_2.jpg)
![](https://public-media.interaction-design.org/images/encyclopedia/card_sorting/card_sorting_3.jpg)
![](https://public-media.interaction-design.org/images/encyclopedia/card_sorting/card_sorting_4.jpg)

### 22.7.1 选择方法

面对面排序法（Face-to-face sorting methods）通常更适用于[定性研究（qualitative research）](https://www.interaction-design.org/literature/topics/qualitative-research)，而在线方法（基于 Web 或桌面端）则更适合获取[定量（quantitative）](https://www.interaction-design.org/literature/topics/quantitative-research)结果。然而，情况并非总是如此；例如，研究者可以在参与者进行在线排序时坐在他们身边，或者共享其桌面。这可能会产生高质量的定性数据，但会让参与者感到压力更大，且会增加引导者（facilitator）的工作难度。此外，远程桌面共享在技术上也具有挑战性，尤其是在存在公司防火墙和安全策略的情况下。

研究人员或交互设计师还可以在以下方案中进行选择：
- 开放式排序（open sorting）：用户自行创建类别
- 封闭式排序（closed sorting）：类别是预先定义的
- 混合式排序（hybrid sorting）：两者的某种结合

对于大多数目的而言，开放式排序是最佳选择，尽管提供一些预定义的类别总是对参与者有所帮助，且大多数排序和分析工具都支持这一操作。当试图确定现有结构需要做出哪些更改时，可以使用封闭式排序，特别是配合那些能够将“参考排序（reference sort）”（如现有方案或建议方案）与参与者结果进行对比的分析工具——见图 9。

![](https://public-media.interaction-design.org/images/encyclopedia/card_sorting/reference_sort.jpg)
作者/版权持有者：William Hudson。版权条款与许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/card-sorting#copyrightNotice)中的“例外（Exceptions）”部分。

**图 22.9**：显示现有解决方案（SynCaps V2）的参考分类（Reference Sort）水果与蔬菜示例

在这个项目-分组图表（Items by Groups Chart，见图 9）中，当前的解决方案由单元格中的黑色方块表示。因此，虽然大多数参与者选择将所有水果分在一起，但数字化秤（Computerized Scales）使用了两个不寻常的分组：“葡萄与柑橘类”和“异域水果”。然而，在某些方面存在一致性（Correspondence）：许多参与者认同图表底部中心位置的“根茎类蔬菜”组的当前设计。

### 22.7.2 招募与引导参与者

与任何其他形式的以用户为中心的设计（User-Centred Design）一样，卡片分类（Card Sorting）活动的参与者应具有代表性，能够代表该解决方案预想的目标用户。然而，考虑到某些人群在面对技术时可能遇到的困难（例如老年用户），对这些群体进行过采样（Over-sample）通常是有益的，以确保最终的设计能尽可能地服务于更广泛的用户群体。在可能的情况下，尽量选择那些除了纯粹的金钱报酬之外，还具有其他参与动机的参与者——例如现有的用户或客户。

在为分类活动的参与者提供引导（Briefing）时，陈述需求时不宜过于模糊。在导航设计（Navigation Design）中，一组项目所需的类别数量并非完全不可预知。通常需要在组的数量和规模之间取得平衡 (Kiger 1984)。因此，向参与者提供关于你所要求的组数量和层级的充分信息至关重要。如果你正尝试为我们的电脑化农产品秤设计菜单，而屏幕空间仅能容纳 12 个项目，那么请毫不犹豫地将此情况告知参与者。同样，网站或桌面应用程序的水平菜单栏很少有空间容纳超过 6 或 8 个项目。在这些情况下，如果允许参与者创建 20 或 30 个类别，可能会浪费参与者以及你的时间。

同样地，如果你已经知道，或者至少强烈怀疑需要某些组名（Group Names），请将这些组名提供给参与者。这在面对面和在线环境下均可实现。但如果参与者愿意，应鼓励他们自行创建组名。

此外，还应指导参与者如何处理他们不理解的项目。虽然一些研究人员或交互设计师（Interaction Designers）建议所有项目都应被分类——让参与者对不认识的项目进行猜测——但这可能会导致伪分组（Spurious Groupings）。可以考虑要求用户直接不对不认识的项目进行分类，或者创建一个专门的“未知”组来放置这些项目。随后可以将这些项目从结果中剔除。目前大多数在线分类工具都允许项目保持未分类状态。然而，请确保分析结果是基于参与者的人数，而非项目被分类的次数。

### 22.7.3 分类所需时间（Time to sort）

执行分类（sort）所需的时间因人而异，但很大程度上取决于需要分类的项目数量：
- 30 个项目约需 20 分钟
- 50 个项目约需 30 分钟
- 100 个项目约需 60 分钟

然而，其他影响因素还包括参与者对术语和概念的熟悉程度，以及他们认真提供结果的积极性。此外，在单次会话（single sessions）中最多可以对 150 张卡片进行分类，但通过将如此庞大的项目拆分为较小的部分，可能会获得更高质量的结果。

### 22.7.4 准备分类工作

对于面对面（基于纸质的）分类（face-to-face sorting），将项目和组名制作到卡片上可能是一项繁琐的任务。幸运的是，可以使用标准的邮件合并（mail-merge）软件来简化这项任务，这意味着项目可以直接打印在卡片或自粘标签上。在 [Syntagm 网站](http://www.syntagm.co.uk/cardsorting) 上可以找到适用于 Microsoft Word 的免费邮件合并模板，涵盖北美和欧洲的纸张尺寸。这些模板还包含可用于简化[数据收集（data collection）](https://www.interaction-design.org/literature/topics/data-collection)的条形码：通过简单的 USB 扫描仪直接读取条形码，而无需手动输入项目名称或编号。这比手动输入更快且更不容易出错——每分钟处理 120 张或更多卡片相对容易（详细说明请参阅上述网页）。

在线分类（online sorting）的准备工作相对简单，仅需上传项目列表和组名（如果有）即可。

然而，无论采用哪种分类方法，都要意识到所用名称的表层相似性（superficial similarities）可能会产生无益的结果。请考虑以下来自一个内网的菜单项名称：
- **管理（Manage）** 缺勤与假期
- **管理（Manage）** 难以相处的同事
- 变革**管理（management）**

如果面对大量需要分类的项目，参与者可能会简单地将名称相似的项目分在一起。这被称为表层匹配（superficial match）。

为了解决这个问题，可以考虑修改以下项目名称：
- 缺勤与假期（Absence and holidays）
- 与难以相处的同事共事（Coping with difficult colleagues）
- 变革管理（Change management）

在前两个项目中，“管理（manage）”一词并非名称的核心部分。将其删除或使用同义词可以避免不必要的分组（Grouping）。

### 22.7.5 选择名称

除了上述提到的表层相似性（superficial similarities）问题外，请务必选择通用名称，特别是当交互方案（interactive solutions）是为具有广泛能力范围的用户设计时。这不仅是常识，也是许多国家[残障歧视立法](https://www.interaction-design.org/literature/topics/accessibility)（disability discrimination legislation）的要求。简单来说，语言的复杂程度不应超过传达所需信息所必需的程度。在英语中，较长的单词（以音节衡量）的使用频率远低于较短的单词 (Klare 1963)。尽管卡片分类（card sort）的参与者可能会为项目或组建议一些不寻常的名称——例如“十字花科植物（brassicas）”——但大多数人在当地超市或蔬菜店购物时，会直接询问“卷心菜（cabbage）”，而不会使用其拉丁语属名（Latin genus）。如果有疑问，请参考常用词汇参考资料，如 [Corpus of Contemporary American English](http://corpus.byu.edu/)（现代美语语料库）、[British National Corpus](http://www.natcorp.ox.ac.uk/)（英国国家语料库）或其他语言的[类似来源](http://en.wikipedia.org/wiki/Word_lists_by_frequency)。

## 22.8 如何理解分析结果

对于规模非常小的项目，只需快速浏览排序后的卡片或在线结果列表，即可获得关于分组（groupings）的有用见解。然而，较大的项目则需要某种形式的分析，其范围从简单的制表汇总（tabulation）到聚类分析（cluster analysis）不等。请注意，虽然聚类分析可能是一个非常复杂的主题 (Romesburg 2004; Bernard and Ryan 2009)，但大多数卡片分类（card sorting）工具使用的是一种相当简单的聚类分析形式，可以通过手动方式轻松实现。这种方法被称为“层次聚类分析（hierarchical cluster analysis）”。在这种情况下，“层次”是指较小的簇（clusters）被聚合以形成较大簇，直到所有元素都被包含在内的方式。

### 22.8.1 简单分析

项目按组的简单汇总（Tabulation of items by groups）可以通过手动（如上所述）或使用电子表格软件来完成。然而，在线排序工具可以为你自动完成这项分析。对于使用前文所述 Microsoft Word 邮件合并模板的打印卡片，SynCaps V2 及更高版本可以生成项目间（items by items）、项目与组间（items by groups）以及树状图分析（Dendrogram analyses）。

![](https://public-media.interaction-design.org/images/encyclopedia/card_sorting/optimal_sort_items_by_groups_chart.jpg)
作者/版权持有者：William Hudson。版权条款和许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。

**图 22.10**：使用基于 Web 的最优排序（Optimal Sort）软件创建的内网导航项目与组关系图

图 10 是一个项目与组关系图，展示了与图 5 不同的另一种呈现方式。在这两种情况下，项目都列在图表的左侧，组名则分布在顶部。通过执行聚类分析（Cluster Analysis）来确定哪些项目之间关系最密切，从而产生一种从一个聚类移动到下一个聚类的项目排序。这两幅图之间唯一的显著区别在于，图 5 使用阴影来显示每种关系的相对强度（可以通过点击单元格查看具体数值），而图 10 则呈现...

带有蓝色底色的百分比数值仅用于突出最显著的结果。

### 22.8.2 聚类分析（Cluster Analysis）

大多数卡片分类工具所采用的聚类分析类型是「层级聚类分析（Hierarchical Cluster Analysis）」或 HCA。其通常的结果是一种被称为树状图（Dendrogram）的图形显示，该词在字面意义上源自希腊语中表示“树”的单词“dendron”。

![](https://public-media.interaction-design.org/images/encyclopedia/card_sorting/Dendrogram_of_Intranet_Navigation.jpg)
作者/版权持有者：William Hudson。版权条款和许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外”部分。

**图 22.11**：使用基于 Web 的 Websort 软件创建的内网导航（Intranet Navigation）树状图

图 11 以树状图的形式展示了层级聚类分析。该示例取自一项内网导航分类活动。树状图的层级特性与项目之间关系的强度相关，这种强度是通过它们出现在同一组中的频率来衡量的。正如真实的树木一样，分支越短，关系越强。在图 11 中，底部的六个项目都包含“leave”（请假）一词。然而，参与者主要将“领养假（Adoption Leave）”、“育儿假（Parental Leave）”和“特别假（Special Leave）”归类为密切相关，但较少

这与“产假与陪产假（Maternity & Paternity Leave）”、“年假（Annual Leave）”和“病假（Sick Leave）”保持一致。最后，“工作休息（Work Breaks）”有时被与请假项归为一类，但与其他项相比，这种关系相当弱。如果你想知道为什么“工作休息”项的关系较弱，则需要查阅项与项图表（items by items chart）、项与组图表（items by groups chart）或（如果可用的话）原始邻近矩阵（raw proximity matrix）——后者仅显示每对项在同一组中共同出现的次数。

树状图（Dendrogram）还揭示了聚类分析（Cluster Analysis）的工作方式。所使用的方法称为“凝聚聚类（Agglomerative Clustering）”，简单来说，就是我们自底向上地构建聚类。因此，在内网（intranet）示例中，第一个聚类将从最后三个“请假”项开始——它们的分支最短——随后将“产假与陪产假”归入其中。然后，再次观察图 11，接下来的最强关系出现在图表的顶部，即“辞职（Resignation）”和“离职人员调查政策（Survey of leavers policy）”。

当各项被凝聚成聚类时，会计算一个平均分（同样基于项对在同一组中共同出现的次数）。这在树状图中通过垂直连接线与标签之间的距离来表示。如前所述，生成的分支越短，反映的关系越强——也就是说，当垂直

连接线更靠近标签，如图 11 中底部的三个项目所示。

在树状图（Dendrogram）中，簇（Clusters）被合并成一个个分支（Branches），直到所有项目都被包含在内。这意味着最弱的关系——即不相似簇之间的关系——位于距离项目标签最远的地方。虽然图 11 没有显示完整的树状图，但它包含了三个向右延伸的长分支。这些分支代表三个不相似的簇；每个簇都需要自己的类别标签（Category labels）（这些标签可以从项目-组图表 [Items by groups chart] 中获取）。请注意，树状图不考虑组名（Group names）；即便 “Adoption -”、“Parental -” 和 “Special Leave” 被频繁地分在同一组，参与者可能为该分组赋予了多种不同的名称。同时请注意，在树状图中，项目只能出现在一个位置。因此，如果参与者将某个项目平均地分在两个不同的组中，该项目将仅在其中一组中表现为一种弱关系。你需要查看项目-组图表（Items by groups chart）才能注意到这一点。

## 22.9 高级分析（Advanced analysis）

在尝试理解卡片分类（Card Sorting）结果时，经常会出现两个重复出现的问题。第一个问题是，并非所有参与者都具有相同的[动机（Motivation）](https://www.interaction-design.org/literature/topics/motivation)、经验或需求。这意味着我们可能会遇到一些参与者，其分类结果纯粹是“噪声（Noise）”——尤其是在具有吸引力激励措施的在线分类中。在其他情况下，我们可能认为参与者是一个相对同质的群体（Homogenous group），但实际上包含多个群体。这可能是由经验等通用因素导致的——在这种情况下，我们需要在设计中兼顾这些不同的群体；或者可能是由于不同的[使用情境（Contexts of use）](https://www.interaction-design.org/literature/topics/contexts-of-use)导致的。在后一种情况下，我们应尝试理解这些差异，并决定是否需要采取独立的设计方案。不幸的是，传统的卡片分类分析工具在此方面帮助不大。但其中一些信息可以通过手动方式获取——例如，通过检查每位参与者创建的组数和组的大小：那些匆忙完成的人倾向于创建较少的组，并且在“不知道”或“杂项”等无用类别中放置大量项目；而那些对问题域（Problem domain）有截然不同看法的人，可能会创建数量异常的组（相对于平均值而言）。 [Optimal Workshop](http://www.optimalworkshop.com/)

在其基于 Web 的服务中增加了一些以参与者为导向的结果（participant-oriented results）。在所有版本的 [SynCaps](http://www.syntagm.co.uk/cardsorting) 中都可以找到相当详细的参与者和项目电子表格。

第二个经常出现的问题与聚类分析（cluster analysis）的基本原则有关：每个项目必须且只能被分配到一个簇（cluster）中。在一定程度上，可以通过仔细检查项目与项目分析（items by items analysis）和项目与组分析（items by groups analysis）来规避这一问题。例如，“黄瓜”这一项目可能会被平均地分在“绿色蔬菜”和“沙拉蔬菜”这两个组中。在树状图（dendrogram）中，它将出现在这两个组中的其中一个——如果分配比例恰好是 50:50，那么选择将是随机的——且其关联强度相当弱。然而，这种关联性的弱化并不是因为参与者对该项目应归入何处感到困惑，而仅仅是因为他们之间没有达成一致。项目与项目分析图和项目与组分析图可以清晰地展示这一点。然而，由于聚类分析的这一局限性，一些研究人员探索了其他高级统计技术，其中最显著的是因子分析（factor analysis）。参见 Capra 2005 和 Giovannini 2012。关于卡片分类（card sorting）分析方法的更详细描述可见于 (Corter 1996) 和 (Coxon 1999)。

### 22.9.1 多级分类（Multilevel sorting）

本章讨论的主要分类方法可以被描述为单层级或“扁平化（flat）”。参与者获得一组项目，并需将其分到单层级的组别中。因此，尽管人们可能会倾向于进行组别嵌套——例如，将“叶菜”嵌套在“绿色蔬菜”中，再将后者嵌套在“蔬菜”中——但需要注意两个问题：

- **分析的局限性（Limitations of analysis）**：最常用的分析方法使用单一的指标来衡量相关项目之间的亲近度（closeness）或邻近度（proximity）。这基于参与者将项目放在一起的频率。对多个组别层级进行聚类分析（cluster analysis）是不切实际的，但根据项目是出现在同一个组、子组（sub-group）、次级子组（sub-sub-group）还是更深层级中，来为项目邻近度分配权重（weightings）则相对简单。出现在同一个组中的项目将获得最高权重；被分在直接子组中的项目对权重稍低；而分在二阶子组（second-order sub-groups）中的项目权重则更低（以此类推）。例如，如果黄瓜和西葫芦（courgette/zucchini）都出现在“绿色蔬菜”组中，它们将获得最大权重；但如果西葫芦出现在名为“绿色蔬菜”的组中，而黄瓜出现在名为“沙拉蔬菜”的子组中，则权重较低（如图 12 所示，其中最大权重为 2）。这正是...所采取的方法

（现已停止运行的）EZsort/Usort (Dong et al. 2001) 以及免费的 SynCaps V1 软件包，在其匿名单层子组（anonymous single-level sub-groups）的实现中采用了这一方法。（匿名子组即简单地不命名。）这一功能已被 UXsort ([uxsort.com](http://www.uxsort.com/)) 和 SynCaps V3 ([Syntagm Ltd](http://www.syntagm.co.uk/cardsorting)) 等软件包扩展到了多层级（multiple levels）。SynCaps V3 还提供了对每个层级所使用的子组名称的分析。关于加权多层级排序（weighted multilevel sorts）的进一步讨论，请参阅 Harloff 2005。

![](https://public-media.interaction-design.org/images/encyclopedia/card_sorting/multilevel_weighting.jpg)
作者/版权持有者：William Hudson。版权条款与许可：保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外（Exceptions）”章节。

**图 22.12**：多层级加权示例

- **规模与复杂度（Scale and complexity）**：多层级卡片分类（multilevel card sorting）面临的最大挑战之一是待分类项目数量的显著增加，以及由此产生的解决方案数量的增加 (Wood and Wood 2008)。因此，不建议将大型内网或电子商务网站的整个导航层级（navigation hierarchy）交给参与者，并要求他们根据自己的意愿对其进行组织。卡片分类的参与者是用户，而非信息架构师（information architects）。当潜在解决方案被部分定义或...时，多层级卡片分类更有可能产生效果。

……受到限制。即便如此，在实际可行的情况下，研究人员和设计师通过开展一系列单层排序（single-level sorting）活动，或许能获取更有价值的信息。

## 22.10 树状排序（Tree Sorting）

树状排序（Tree Sorting，也称为“[树状测试（tree testing）](https://www.interaction-design.org/literature/topics/tree-testing)”和“反向卡片分类（reverse card sorting）”）是一个与卡片分类（card sorting）相关的概念，但在许多方面又截然不同。从本质上讲，它是对软件应用程序或网站中导航树（navigation tree）的一种模拟。在线参与者会收到具体的目标，然后被要求使用该树状模拟进行导航。图 13 展示了跨越多个屏幕的操作过程（步骤 1 为第一个屏幕，步骤 2 为第二个屏幕，依此类推）。在步骤 1 中，参与者选择了“水果（Fruit）”，而在步骤 2 中选择了“软果（Soft Fruit）”。如果选择了错误的选项，参与者需要回溯以寻找更合适的菜单。可以提供大量的任务，且如果需要，每位参与者仅看到其中的一个随机子集。

项目完成后，研究人员和设计师可以获得成功率（success rates）、错误率（error rates）和耗时（time taken）及其相关变体。虽然封闭式卡片分类（closed card sorting）在验证导航设计方面能提供一定的帮助，但在大多数情况下，树状排序是一种更有效的方法。（参见 [plainframe.com](http://www.plainframe.com/) 和 [optimalworkshop.com](http://www.optimalworkshop.com/)）

![](https://public-media.interaction-design.org/images/encyclopedia/card_sorting/Tree_sorting_example.jpg)
作者/版权持有者：William Hudson。版权条款和许可：保留所有权利（All Rights）

保留所有权利。经许可转载。请参阅下方[版权条款](https://www.interaction-design.org/about/terms-of-use)中的“例外情况（Exceptions）”章节。

**图 22.13**：来自 optimalworkshop.com 的树形分类（Tree Sorting）示例，其任务为“寻找橙子”。

## 22.11 更多学习资源

除了下面列出的参考文献，特别是 Donna Spencer 关于卡片分类法（Card Sorting）的著作 (Spencer 2009) 之外，还有许多有用的网页资源：
- [Card Sorting (Usability.gov)](http://www.usability.gov/methods/design_site/cardsort.html)
- [Card Sorting and Computer-Aided Paper Sorting (Syntagm Ltd)](http://www.syntagm.co.uk/design/cardsortintro.shtml)

## 22.12 References

[Bergström](https://www.interaction-design.org/references/authors/john_a__bergstr%F6m.html), John A. (0000b): *An Experimental Study of Some of the Conditions of Mental Activity*. In [The American Journal of Psychology](https://www.interaction-design.org/references/periodicals/the_american_journal_of_psychology.html), 6 (2) pp. 247-274
[Bergström](https://www.interaction-design.org/references/authors/john_a__bergstr%F6m.html), John A. (0000a): *Experiments upon Physiological Memory by Means of the Interference of Associations*. In [The American Journal of Psychology](https://www.interaction-design.org/references/periodicals/the_american_journal_of_psychology.html), pp. 356-369
[Bernard](https://www.interaction-design.org/references/authors/h__russell_bernard.html), H. Russell and [Ryan](https://www.interaction-design.org/references/authors/gery_w__ryan.html), Gery W. (2009): *Analyzing Qualitative Data: Systematic Approaches.* Sage Publications, Inc
[Capra](https://www.interaction-design.org/references/authors/miranda_g__capra.html), Miranda G. (2005): *Factor analysis of card sort data: an alternative to hierarchical cluster analysis*. In[Human Factors](https://www.interaction-design.org/references/periodicals/human_factors.html), 49 (5) pp. 691-695

[Corter](https://www.interaction-design.org/references/authors/james_e__corter.html), James E. (1996): *Tree Models of Similarity and Association (Quantitative Applications in the Social Sciences).* Sage Publications, Inc
[Coxon](https://www.interaction-design.org/references/authors/anthony_p__m__coxon.html), Anthony P. M. (1999): *Sorting Data: Collection and Analysis (Quantitative Applications in the Social Sciences).* Sage Publications, Inc
[Dong](https://www.interaction-design.org/references/authors/jianming_dong.html), Jianming, [Martin](https://www.interaction-design.org/references/authors/shirley_martin.html), Shirley and [Waldo](https://www.interaction-design.org/references/authors/paul_waldo.html), Paul (2001): *A user input and analysis tool for information architecture*. In [CHI 01 extended abstracts on Human factors in computing systems CHI 01](https://www.interaction-design.org/references/periodicals/chi_01_extended_abstracts_on_human_factors_in_computing_systems_chi_01.html),
[Dubois](https://www.interaction-design.org/references/authors/cornelius_dubois.html), Cornelius (1949): *The Card-Sorting or Psychophysical Interview*. In [Public Opinion Quarterly](https://www.interaction-design.org/references/periodicals/public_opinion_quarterly.html), 13 (4) pp. 619-628

[Eling](https://www.interaction-design.org/references/authors/paul_eling.html), Paul, [Derckx](https://www.interaction-design.org/references/authors/kristianne_derckx.html), Kristianne and [Maes](https://www.interaction-design.org/references/authors/roald_maes.html), Roald (2008): *On the historical and conceptual background of the Wisconsin Card Sorting Test*. In [Brain and Cognition](https://www.interaction-design.org/references/periodicals/brain_and_cognition.html), 67 (3) pp. 247-253
[Fincher](https://www.interaction-design.org/references/authors/sally_fincher.html), Sally and [Tenenberg](https://www.interaction-design.org/references/authors/josh_tenenberg.html), Josh (2005): *Making sense of card sorting data*. In [Expert Systems](https://www.interaction-design.org/references/periodicals/expert_systems.html), 22 (3) pp. 89-93
[Giovannini](https://www.interaction-design.org/references/authors/peter_giovannini.html), Peter (2012). *How to carry out pile sorting and how to analyse the data with Anthropac: a tutorial*. Retrieved 2 January 2012 from [http://petergiovannini.com/ethnobotany-methods/how...](http://petergiovannini.com/ethnobotany-methods/how-to-pile-sorting-with-anthropac-tutorial.html)

[Harloff](https://www.interaction-design.org/references/authors/joachim_harloff.html), Joachim (2005): *Multiple Level Weighted Card Sorting*. In [Methodology: European Journal of Research Methods for the Behavioral and Social Sciences](https://www.interaction-design.org/references/periodicals/methodology-_european_journal_of_research_methods_for_the_behavioral_and_social_sciences.html), 1 (4) pp. 119-128
[Jastrow](https://www.interaction-design.org/references/authors/joseph_jastrow.html), Joseph (0000): *A sorting apparatus for the study of reaction-times*. In [Psychological Review](https://www.interaction-design.org/references/periodicals/psychological_review.html), 5 (3) pp. 279-285
[Kiger](https://www.interaction-design.org/references/authors/john_i__kiger.html), John I. (1984): *The Depth/Breadth Trade-Off in the Design of Menu-Driven User Interfaces*. In [International Journal of Man-Machine Studies](https://www.interaction-design.org/references/periodicals/international_journal_of_man-machine_studies.html), 20 (2) pp. 201-213
[Klare](https://www.interaction-design.org/references/authors/george_r__klare.html), George R. (1963): *Measurement of Readability.* Umi Research Pr

[Kline](https://www.interaction-design.org/references/authors/linus_w__kline.html), Linus W. and [Kellogg](https://www.interaction-design.org/references/authors/chester_e__kellogg.html), Chester E. (1914): *Cards as Psychological Apparatus*. In [Science](https://www.interaction-design.org/references/periodicals/science.html), 39 pp. 657-659
[Miller](https://www.interaction-design.org/references/authors/george_a__miller.html), George A. (1969): *A psychological method to investigate verbal concepts*. In [Journal of Mathematical Psychology](https://www.interaction-design.org/references/periodicals/journal_of_mathematical_psychology.html), 6 (2) pp. 169-191
[Morville](https://www.interaction-design.org/references/authors/peter_morville.html), Peter and [Rosenfeld](https://www.interaction-design.org/references/authors/louis_rosenfeld.html), Louis (2006): *Information Architecture for the World Wide Web: Designing Large-Scale Web Sites.* OReilly Media
[Nielsen](https://www.interaction-design.org/references/authors/jakob_nielsen.html), Jakob (2004): *Card Sorting : How Many Users to Test*. In [Useit Alertbox](https://www.interaction-design.org/references/periodicals/useit_alertbox.html), (0) pp. 3-7

[Nielsen](https://www.interaction-design.org/references/authors/jakob_nielsen.html), Jakob and [Sano](https://www.interaction-design.org/references/authors/darrell_sano.html), Darrell (1995): *SunWeb: *[*user interface*](https://www.interaction-design.org/literature/topics/ui-design)* design for Sun Microsystem's internal Web*. In[Computer Networks and ISDN Systems](https://www.interaction-design.org/references/periodicals/computer_networks_and_isdn_systems.html), 28 (1) pp. 179-188
[Romesburg](https://www.interaction-design.org/references/authors/charles_romesburg.html), Charles (2004): *Cluster Analysis for Researchers.* Lulu.com
[Sachs](https://www.interaction-design.org/references/authors/joe_sachs.html), Joe (2002): *Aristotle's Metaphysics.* Green Lion Press
[Spencer](https://www.interaction-design.org/references/authors/donna_spencer.html), Donna (2009): *Card Sorting.* Rosenfeld Media

[Tullis](https://www.interaction-design.org/references/authors/thomas_s__tullis.html), Thomas S. (1985): Designing a Menu-Based Interface to an Operating System. In: [Borman](https://www.interaction-design.org/references/authors/lorraine_borman.html), Lorraine and[Curtis](https://www.interaction-design.org/references/authors/bill_curtis.html), Bill (eds.) [Proceedings of the ACM CHI 85 Human Factors in Computing Systems Conference](https://www.interaction-design.org/references/conferences/proceedings_of_the_acm_chi_85_human_factors_in_computing_systems_conference.html) April 14-18, 1985, San Francisco, California. pp. 79-84
[Tullis](https://www.interaction-design.org/references/authors/tom_tullis.html), Tom and [Wood](https://www.interaction-design.org/references/authors/larry_e__wood.html), Larry E. (2004): *How Many Users Are Enough for a Card-Sorting Study? The Card-sorting Study*. In [Learning](https://www.interaction-design.org/references/periodicals/learning.html), pp. 1-10
[Weller](https://www.interaction-design.org/references/authors/susan_c__weller.html), Susan C. and [Romney](https://www.interaction-design.org/references/authors/a__kimball_romney.html), A. Kimball (1988): *Systematic Data Collection (Qualitative Research Methods Series 10).* Sage Publications, Inc

[Wood](https://www.interaction-design.org/references/authors/jed_r__wood.html), Jed R. and [Wood](https://www.interaction-design.org/references/authors/larry_e__wood.html), Larry E. (2008): *Card Sorting: Current Practices and Beyond*. In [Journal of Usability Studies](https://www.interaction-design.org/references/periodicals/journal_of_usability_studies.html), 4 (1) pp. 1-6

# 22.12 Jeff Sauro 的点评

它是什么，如何使用，来源何处，以及如何解读结果？当你使用像卡片分类法（Card Sorting）这样的方法时，这些正是你想要了解的内容。Hudson 对这一关键的用户体验（UX）方法进行了简洁且全面的阐述。他准确地阐明了卡片分类法如何同时产生定性数据（qualitative data）和定量数据（quantitative data），并说明了在解读卡片分类法标志性图表之一——树状图（dendrogram）时，如何兼顾数据分析与主观判断。在对卡片分类的结果进行定量分析（quantifying）时，还有以下几点需要考虑。

## 22.12.1 置信区间（Confidence Intervals）

卡片分类（Card sorts）——与大多数用户研究（User Research）方法一样——涉及对更大规模用户总体（Population）中的一个样本（Sample）（通常是小样本）进行研究。任何样本都伴随着关于数据稳定性的不确定性。最有效的策略之一是在样本统计量（Sample statistics）周围添加置信区间（Confidence intervals）。置信区间告诉我们未知总体百分比最可能的范围。

例如，假设 26 位用户中有 20 位（77%）能够成功在“软果类（Soft Fruit）”类别下找到草莓（图 22.13）。即使没有测量所有用户，我们也可以在 95% 的置信水平下认为，所有用户中会有 58% 到 89% 能够成功定位草莓（假设我们的样本具有合理的代表性）。

![](https://www.interaction-design.org/images/encyclopedia/card_sorting/measuring_usability_quantifying_user_experience_1.jpg)
Copyright © Jeff Sauro. All Rights Reserved. 
Reproduced with permission. See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/card-sorting#copyrightNotice) below.

我们百分比周围的误差幅度（Margin of error）约为 +/- 16%。置信区间的下限告诉我们，我们可以 95% 地确信，有 58% **或更多** 的用户能够找到草莓的位置。如果我们的初步目标是让大多数用户能找到该水果，那么我们就有证据表明实现了这一目标。

我们可以将同样的方法应用于评估（qualifying）被放入某个类别的卡片百分比。例如，假设有 70 名参与者进行了图 22.10 所示的卡片分类（card-sort）。我们看到，46% 的参与者将“让新员工上手（Getting a New Person Started）”放入了“入职（Joining）”类别，而 39% 的参与者将该卡片放入了“招聘新员工（Hiring New People）”类别。

![](https://www.interaction-design.org/images/encyclopedia/card_sorting/measuring_usability_quantifying_user_experience_2.jpg)
Copyright © Jeff Sauro. All Rights Reserved. 
Reproduced with permission. See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/card-sorting#copyrightNotice) below.

“招聘新员工”类别的 95% 置信区间（confidence interval）在 35% 到 58% 之间，而“入职”类别的置信区间在 28% 到 50% 之间（见上图）。置信区间之间存在大量重叠，这意味着我们不应对这一差异持有太高的信心。可以使用 [http://www.measuringusability.com/wald.htm](http://www.measuringusability.com/wald.htm) 提供的在线计算器进行计算。

由于区间重叠较大，我们无法将这 5 个百分点的差异与抽样误差（sampling error）区分开来。如果必须选择一个，我们应该选择“入职”，但应将这两个类别都视为可行的选项。

## 22.12.2 样本量（Sample Sizes）

与大多数评估一样，在涉及用户时，首先被提出的问题之一就是“我需要多少名用户？”令人惊讶的是，除了 Tullis and Wood 在 2004 年发表的文章外，关于如何确定样本量的指导非常少。Tullis and Wood 进行了一项重采样研究（resampling study），其中包含一项涉及 168 名用户的大规模卡片分类（card sort），结果发现当样本量在 20-30 之间时，聚类结果（cluster results）会非常相似（相关性 correlations 在 0.93 以上）。

这一样本量是基于单项研究的具体情况（卡片放置的一致性以及 46 张卡片）以及对树状图（dendrogram）的观察得出的，因此，如果你的研究与他们的研究相似，该结果最为适用。

另一种样本量规划方法是基于将卡片放入每个类别图表（图 22.10）的用户百分比，或在树形测试（tree testing，图 22.13）中正确选择路径的用户百分比。这种方法是基于从置信区间（confidence intervals）反向推导，类似于前一节中生成的结果。在第一个示例中，关于能够正确找到“草莓”的用户百分比，我们的误差幅度（margin of error）为 16%。

如果我们想要获得更精确的估计，并将误差幅度减半至 +/- 8%，我们可以从置信区间反向推导，得出所需的样本量为 147。下表显示了在不同样本量下，95% 置信区间的预期误差幅度。

| **样本量（Sample Size）** | **误差幅度（Margin of Error +/-）** |
|---|---|
| 10 | 27% |

| 21 | 20% |
| 30 | 17% |
| 39 | 15% |
| 53 | 13% |
| 93 | 10% |
| 115 | 9% |
| 147 | 8% |
| 193 | 7% |
| 263 | 6% |
| 381 | 5% |
| 597 | 4% |
| 1064 | 3% |

具体的计算过程在 [Quantifying the User Experience](http://www.amazon.com/Quantifying-User-Experience-Practical-Statistics/dp/0123849683) 的第 3 章和第 6 章中进行了详细阐述。

# 22.13 David Travis 的评论

William Hudson 对卡片分类法（Card Sorting）的论述专业且深刻，这正符合人们对一位拥有十多年实践经验的专家的预期。William 在本百科全书中的章节将为那些初次接触卡片分类法、需要分步指南的读者提供极大的帮助。

对于已经具备一定卡片分类经验的人员，我想就在实际操作开放式卡片分类（Open Card Sorting）和封闭式卡片分类（Closed Card Sorting）时遇到的一些问题补充几点看法。首先，在进行开放式卡片分类时，面对一个包含数百个待分类项的大型网站，应当如何处理？其次，在进行封闭式卡片分类时，如何向客户呈现结果，才能让他们理解你所收集的复杂的定量数据（Quantitative Data）？

## 22.13.1 针对大型网站的开放式卡片分类法（Open Card Sort）

几年前，我曾与一家拍卖网站合作，帮助他们修订其在线帮助系统。该系统包含大量的帮助页面（超过 850 个），且这些页面的增长方式较为随意（ad hoc）。为了确保新的帮助系统能够实现预期的商业效益，客户需要在将其集成到新界面之前，对内容进行结构化处理和组织。然而，即使是最敬业的用户也不愿对 850 张内容卡片进行分类，因此我们必须首先采取措施，使这项任务变得可操作。

我们首先对在线帮助系统进行了内容清单（Content Inventory）盘点。这是描述不同页面之间关系的重要第一步，因为它能让我们回答诸如“哪些帮助页面被访问最频繁？”、“最常见的搜索词是什么？”以及“典型用户在一次会话中会查看多少个帮助页面？”等问题。这些问题的答案帮助我们将内容分为“关键（critical）”内容和“次要（secondary）”内容。我们还剔除了所谓的“ROT”内容，即冗余（Redundant）、过时（Outdated）或琐碎（Trivial）的内容。这些步骤帮助我们将海量的内容减少到了一个相对可控的规模。

我们的下一步是审查内容，看看是否存在任何明显、突出的主题或分组。在这个阶段，我们确实让几个人（包括我在内）对整个清单进行了分类，以观察是否能发现任何明显的类别。

通过这种方法，我们能够识别出那些大多数用户倾向于将其归为一类的卡片簇（Clusters）。例如，假设一个企业内网（Corporate Intranet）中包含数十项人事政策（HR Policies），如差旅政策、环境政策、产假政策等。显而易见，大多数用户会将这些政策归入同一组，因此，要求参与者对每一项政策进行分类的收益较低；相反，在卡片分类法（Card Sort）中，只需为每个组选取少量的典型样本（Exemplars）即可。

这两种技术帮助我们将项目数量缩减至 100 个左右，这在卡片分类法中是一个可接受的数量。

得益于此，新的信息架构（Information Architecture）减少了因用户无法找到或理解内容而产生的支持咨询（Support Enquiries）数量。用户现在能够自主解决问题，从而间接提升了商品上架量（Listings）、销售额和注册人数。

## 22.13.2 呈现封闭式卡片分类法的数据

去年，我与 Royal Bank of Scotland 的内网（Intranet）设计团队合作。该银行拥有超过 15 万名员工，设计团队当时正着手对包含约 50 万个页面的内网进行大规模重构。设计团队希望验证员工是否能在拥有近 1000 个节点（Nodes）的新结构中找到重要内容。

我们开展了一次封闭式卡片分类法（Closed Card Sort），其方法与 William 在其文章中所描述的非常相似。然而，我们希望确保能收集到来自美国、英国和印度等多个国家员工的意见。因此，我们决定采用远程、无引导的封闭式卡片分类法（Remote, Unmoderated Closed Card Sort）。我们邀请了一组具有代表性的银行员工样本访问一个网站，该网站以树状结构（Tree Structure）排列了内网的顶级导航术语（Top-level Navigation Terms）（这有助于我们专注于导航，而不会受到视觉美学的干扰）。参与者的任务是为各种具体任务选择正确的链接，例如“查找报销申请表”。共有 200 多名参与者参加了这项研究。

这类研究的挑战在于如何向设计团队呈现结果，使他们能够基于数据做出明智的决策。虽然有一些显而易见的统计数据可以使用——例如成功完成任务的参与者人数——但对于设计而言，同样有用的是理解参与者所选择的错误路径。

![](https://www.interaction-design.org/images/encyclopedia/card_sorting/card_sort_travis_2.jpg)
Copyright © David Travis. All Rights Reserved. 
Reproduced with permission. See section "Exceptions" in the [copyright terms](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/card-sorting#copyrightNotice) below.
图 22.1：我们选择呈现结果的一种示例（针对一项任务）。

图 1 展示了我们选择呈现结果的一种示例（针对一项任务）。请注意该图表的以下特征：
- “地铁图（tube map）”图表显示了参与者寻找答案所采取的主要路径。绿线表示正确路径，红线表示常见的错误路径。红色圆圈表示参与者选择错误路径的节点（Node）。
- “成功率（Success rate）”显示了找到正确答案的参与者百分比。误差线（Error bars）显示了 95% 置信区间（Confidence interval）。
- “成功率——详细细分（Detailed breakdown）”提供了关于成功率衡量指标的更多背景信息，显示了有多少参与者需要通过回溯（Backtrack）来寻找答案（即“间接成功 [Indirect success]”）。
- “直接度（Directness）”是指在任务过程中任何时间点都没有在树状结构中回溯的参与者百分比。该分数越高，我们越能确信参与者对其答案具有信心（即使答案是错误的）。误差线显示了 95% 置信区间。
- “耗时（Time taken）”显示了中位数时间（Median time）

参与者所花费的时间。误差棒（Error bar）表示上四分位数（Upper quartile）。您可以将所花费的时间视为完成任务时犹豫程度（Hesitation）的一种衡量标准。
- 我们还根据测得的成功率（Success rate），对该设计在这一任务中的表现给出了定性判断（Qualitative judgement）（从“非常差”到“优秀”），并包含了一个对研究结果进行解读并提供改进建议的章节。

除了地铁图可视化（Tube map visualisation）之外，我们能够从用于收集数据的在线工具 Treejack 中提取大部分这些指标（Metrics）。这使得分析和呈现过程相对简单直接。（非常感谢 RBS Group 的 Rebecca Shipp 允许我们描述这一案例研究）。

# 22.14 Chris Rourke 的评论

互联网的一个残酷讽刺在于，网站上的信息越多，寻找某一项具体信息的难度就越大。这就好比在更大的干草堆里寻找一根针。当然，这种趋势并非绝对，你至少可以通过高效地组织信息，尽力抵消这种倾向。将内容放入整洁且标签清晰的分组中，并使用嵌套层级（Nested Hierarchies），能让原本庞杂的信息变得有条理。

在 UX 设计师的工具箱中，卡片分类法（Card Sorting）是构建合理信息层级结构最有效的工具。而与其相辅相成的树状测试（Tree Testing）则是验证该结构鲁棒性（Robustness）的最佳手段。两者结合，是创建可用信息架构（Information Architecture）的核心工具，能够实现最优的信息组织方式，从而帮助用户高效地找到所需信息。

William Hudson 在卡片分类法领域被公认为领先的思想家和实践者，他开发的 SynCaps 软件在采集和分析卡片分类结果方面，为我以及 UX 领域的许多同行提供了极大的便利（并节省了大量时间）。

William 撰写的关于卡片分类法的章节内容全面且具有启发性，书中配有多张有益的图表，并采用了一个所有读者都能理解的简单场景——水果和蔬菜的世界。在此领域背景下，他清晰地阐述了：

- 卡片分类法的必要性

- 卡片分类法（Card Sorting）的规划者和参与者所遇到的各类困境（Dilemmas）（例如，同一种水果被赋予了两种不同的名称）
- 执行卡片分类法的流程
- 数据分析的方法

这是我读过关于卡片分类法最易懂且最具可读性的解释，将成为一个关键的学习资源（以及文中提到的 Donna Spencer 的出版物）。

特别是，它提供了极佳的可视化图表来解释卡片分类法的输出结果。令人欣慰的是，它不仅仅停留在展示树状图（Dendrogram）上——遗憾的是，一些从业者倾向于直接将树状图旋转 90 度，然后惊呼：“瞧！这就是我的新站点地图（Site map），大功告成了！”

经验较为丰富的从业者会知道，解读树状图还需要做大量其他工作。我非常感激作者清晰地解释了，仅凭树状图并不总能讲述最清晰的故事。例如，如果受试者在将某个项目归类时意见分歧严重（正好平分），那么一个可能与两个不同组别都有强亲和力（Affinities）的项目，最终看起来可能与这两个组别的关系都较为微弱。这是一个典型的案例，证明了在做出最佳决策时，需要通过与用户交谈来获取传统的定性信息（Qualitative information）。

根据我的经验，如何主持（Moderate）这些环节至关重要，并会影响结果。例如，我经常采用的一个技巧（在以下情况下非常有用...

（如上所述，当一张卡片具有两个或多个自然归属（natural homes）时），做法是要求参与者将该项目的打印卡片放置在他们认为最合适的地方；但如果他们觉得该项目也能非常自然地放入其他组，他们可以拿一张空白卡片，在上面写下该项目名称，并将其放置在他们认为可能所属的其他组中。在数据采集（data capture）过程中，所有卡片副本都将被处理，SynCaps V2 会将该项目分摊到所选的各个组中。正如 William 所提到的，树状图（dendrograms）仅支持每个项目对应一个位置，但这种分摊情况在“项目对项目（items by items）”和“项目对组（items by groups）”图表中会清晰可见。从业者在构建信息架构（Information Architecture）时可以参考这些分摊结果，将其作为设置交叉链接（cross links）的合适位置（例如引导访问者前往其他章节相关内容的“查看更多”类链接）。

另一个需要考虑的引导要点（moderating point）是参与者在环节中应提供多少口头反馈（verbal feedback）。用户体验（UX）的核心方法——可用性测试（usability testing），依赖于参与者在浏览网站路径时所产生的口头意识流（verbal stream of consciousness）。就个人而言，我认为这种方式并不适用于卡片分类（card sorting），尽管我承认口头反馈很重要，特别是对于理解类别名称以及哪些项目容易或难以分类而言。我通常建议他们将卡片铺开，以便对需要分类的内容有一个全局视角（bird's eye view），然后不要干扰...

当参与者发现模式并进入“状态（get in the zone）”时，他们会为解决这个特定的信息架构（Information Architecture）难题制定自己的策略。只有在他们分类了大约一半的卡片并贴上几个标签后，我才会尝试用温和的“进展如何？”这类探测性询问（probe）进行干预。主持人应该具备像理发师那样理想的“第六感”，能够判断参与者是否愿意交谈，如果他们不想说，不要强迫他们。一旦所有卡片都分类完毕（有些可能会被放在“不知道”堆中），那么绝对应该鼓励进行一次全面的事后访谈（debrief）。

William 对我认为卡片分类（Card Sorting）中最困难的部分给出了一些解释——即当你的信息域（information domain）是一个拥有数百个项目的网站时，该选择哪些项目进行分类。不可避免地，需要对项目进行一定的整合（consolidating），即从一个明显且广泛的项目组中仅选择 1 或 2 个代表性项目。这本身往往会引发争议或分散注意力，并且始终存在被用作淡化卡片分类结果理由的风险（“噢，没错，但你在分类中没有包含这 3 个项目，如果你包含了，结果可能会非常不同……”）。

最后，我倾向于始终尝试采用树形测试（Tree Testing，或称反向卡片分类 Reverse Card Sorting，或类别测试 Category Testing）的自顶向下（top-down）方法，来平衡卡片分类的自底向上（bottom-up）方法。我发现树形测试在让客户看到……方面至少同样有效。

一个优秀的、以用户为中心的信息架构（User-Centred Information Architecture）的重要性。毕竟，树形测试（Tree Testing）的过程与人们在网站导航时实际寻找信息（Information Foraging）的方式更为相似。此外，由此产生的定量和统计数据（Quantitative and Statistical Data）非常有说服力，尤其是当这些测试能在信息架构修订前后分别进行时（例如，“此前有 50% 的用户能无误地找到该主题，现在这一比例上升到了 75%”）。该测试也可以远程进行，除了本章中提到的资源外，其他可用资源还包括 NaviewApp 和 UserZoom。William 的核心研究领域是卡片分类（Card Sorting），但如果能增加关于自顶向下法（Top-down Method）的内容，或许可以将该章节重新命名为《卡片分类与信息架构研究》。

尽管如此，William Hudson 的这一章节内容详尽，能够满足卡片分类初学者以及具有一定经验者的需求。对于那些希望通过实施此类研究来优化网站导航和信息架构的人来说，这绝对是一份极具价值的参考资料。

## 本章主题：

[卡片分类 (Card Sorting)](https://www.interaction-design.org/literature/topics/card-sorting)[
                        用户体验 (User Experience, UX) 设计](https://www.interaction-design.org/literature/topics/ux-design)[
                        人机交互 (Human-Computer Interaction, HCI)](https://www.interaction-design.org/literature/topics/human-computer-interaction)[
                        交互设计 (Interaction Design)](https://www.interaction-design.org/literature/topics/interaction-design)[
                        信息架构 (Information Architecture)](https://www.interaction-design.org/literature/topics/information-architecture)[
                        设计史 (Design History)](https://www.interaction-design.org/literature/topics/design-history)[
                        定量研究 (Quantitative Research)](https://www.interaction-design.org/literature/topics/quantitative-research)[
                        定性研究 (Qualitative Research)](https://www.interaction-design.org/literature/topics/qualitative-research)[
                        客户研究 (Customer Research)](https://www.interaction-design.org/literature/topics/customer-research)
