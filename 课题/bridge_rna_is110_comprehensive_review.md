# Bridge RNA与IS110家族插入序列研究进展深度综述：从微生物双特异性RNA引导重组机制到人类兆碱基级基因组重排与合成微生物组学

## 1. 引言：可编程基因组工程的范式演进与IS110家族的破局

生命科学对遗传信息的精确操纵能力，在过去二十年间经历了三次深刻的范式演进。第一代靶向基因组修饰依赖于蛋白质与DNA的特异性氨基酸-碱基相互作用，以锌指核酸酶（ZFNs）、转录激活因子样效应物核酸酶（TALENs）以及经典位点特异性重组酶（如Cre、Flp和噬菌体整合酶Bxb1、$\phi$C31）为代表。尽管位点特异性重组酶具备在不引入游离DNA双链断裂（Double-Strand Breaks, DSBs）的前提下介导大片段插入、切除与倒位的能力，但其DNA序列识别完全由蛋白质构象决定，针对全新内源基因组位点的定向进化耗时费力，且通常需要预先在宿主基因组中植入固定的识别靶标（如loxP或attB/attP着陆垫），限制了其在任意原位基因座上的直接应用（[Durrant et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208160/)）。

第二代范式由核酸引导的核酸内切酶系统开启，核心代表为原核适应性免疫系统CRISPR-Cas（如Cas9、Cas12a）及其转座子祖先蛋白TnpB、IscB与真核同源物Fanzor（[Hiraizumi et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208158/)）。通过单一引导RNA（gRNA）与靶DNA的Watson-Crick碱基配对，CRISPR系统彻底解决了靶位点的可编程性难题。然而，天然CRISPR效应蛋白的直接酶学活性局限于核酸切割（核酸内切酶或切口酶活性）。无论是依赖内源同源定向修复（HDR）或非同源末端连接（NHEJ）的传统CRISPR编辑，还是融合了脱氨酶的碱基编辑器（Base Editors）与融合了逆转录酶的先导编辑器（Prime Editors），本质上均需要将外源切割/切口事件与复杂的宿主细胞DNA损伤修复通路相偶联。当面对数千碱基（kilobase, kb）乃至兆碱基（megabase, Mb）尺度的基因载荷整合、大片段致病序列切除或染色体尺度倒位时，传统CRISPR衍生工具常受限于非分裂细胞HDR活性低下、多组分融合蛋白体积庞大（如PASTE或CRISPR相关转座酶CAST系统）以及潜在的双链断裂基因毒性与染色体易位风险（[Programmable RNA-Guided DNA Recombination, MDPI](https://www.mdpi.com/2227-9059/14/9/2008)）。

2024年6月，[Arc研究所（Arc Institute）](https://arcinstitute.org/news/bridge)的Patrick D. Hsu团队、东京大学的Hiroshi Nishimasu团队以及悉尼大学的Sandro F. Ataide团队分别在《Nature》与《Nature Communications》发表里程碑式研究，共同揭开了原核生物**IS110家族插入序列（IS110 Insertion Sequence Family）**及其近缘**IS1111亚家族**的神秘面纱（[Durrant et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208160/)；[Hiraizumi et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208158/)；[Siddiquee et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11187229/)）。研究证实，IS110家族转座子编码一种结构紧凑的**桥接RNA（Bridge RNA，简称bRNA，在IS1111/IS110部分研究中亦称为seekRNA）**，作为自然界首个被发现的**天然双特异性引导RNA（bispecific guide RNA）**，能够通过两个独立可编程的内部环——靶标结合环（Target-Binding Loop, TBL）和供体结合环（Donor-Binding Loop, DBL）——同时与靶标基因组DNA（Target DNA, tDNA）和供体DNA（Donor DNA, dDNA）双链发生碱基配对，直接招募并激活单一的IS110重组酶催化位点特异性重组。


*图1.1：新兴RNA引导转座元件的作用机制对比。（a）真核Fanzor通过$\omega$RNA引导切割DNA；（b）IS110通过Bridge RNA（bRNA）与桥接重组酶直接识别靶DNA和供体DNA这四种组分，在不产生游离双链断裂的前提下完成可编程DNA重组；（c）工程化R2逆转录转座子引导靶向整合（图片来源：[Mechanisms of RNA-guided TE insertion, ResearchGate](https://www.researchgate.net/figure/Mechanisms-of-RNA-guided-TE-insertion-a-Fanzor-cuts-DNA-in-eukaryotic-cells-at-locations_fig4_398002795)）。*

这一发现标志着第三代可编程RNA引导技术——**RNA引导的DNA重组系统（RNA-guided DNA Recombination）**的诞生。不同于CRISPR-Cas的“切割后修复”逻辑，IS110/Bridge RNA系统将RNA的可编程序列识别能力与重组酶自主催化链切割、交换及重新连接（无需宿主修复通路、无游离DSB产生、无PAM序列限制、无痕重组）的生物化学特性合二为一，为单基因座精准替换、超大片段基因写入及全基因组三维构象重排提供了统一的分子引擎。

| 技术维度 | IS110 / Bridge RNA 桥接重组系统 | 传统位点特异性重组酶 (Cre / Bxb1) | CRISPR-Cas9 / HDR 系统 | 先导编辑与双先导编辑 (PE / TwinPE / PASTE) | CRISPR相关转座酶 (CAST) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **核心催化组件** | 单一DEDD-Ser重组酶（~300–460 aa，极简型201 aa）+ 单一双特异性bRNA（~150–250 nt，独立DBL仅90 nt）（[Durrant et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208160/)） | 单一酪氨酸或大丝氨酸重组酶（无RNA组分） | Cas9核酸内切酶（~1,368 aa）+ sgRNA（~100 nt）+ 外源同源供体 | nCas9-RT融合蛋白（>2,000 aa）+ pegRNA（± Bxb1整合酶） | 多亚基Cascade/Cas12k + TnsA/B/C/TniQ多蛋白复合体 |
| **靶标与供体识别机制** | bRNA的TBL与DBL分别通过双链交错碱基配对识别靶DNA和供体DNA（[Hiraizumi et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208158/)） | 蛋白质氨基酸侧链直接识别固定DNA序列（如loxP、attB/attP） | sgRNA识别靶DNA单链，供体依赖长同源臂 | pegRNA识别靶DNA并逆转录合成短序列或attB位点 | crRNA识别靶DNA，转座酶蛋白识别供体末端反向重复（TIR） |
| **可编程性维度** | **靶DNA与供体DNA双端独立可编程**（[Durrant et al., 2024](https://pubmed.ncbi.nlm.nih.gov/38926615/)） | 不可直接重编程，需定向进化或预先植入着陆垫 | 仅靶位点可编程 | 靶位点与短逆转录模板可编程 | 仅靶位点可编程，供体末端序列固定并产生转座印记 |
| **DNA双链断裂（DSB）与宿主修复依赖** | **不产生游离DSB**，经5'-磷酸丝氨酸共价中间体与霍利迪交叉自主完成重连，不依赖HDR/NHEJ，可在非分裂细胞中工作（[Hiraizumi et al., 2024](https://pubmed.ncbi.nlm.nih.gov/38926616/)；[MDPI, 2026](https://www.mdpi.com/2227-9059/14/9/2008)） | 不产生游离DSB，自主完成链交换与连接 | 产生游离DSB，严格依赖宿主HDR（限于分裂期细胞）或NHEJ | 产生单链切口（Nick），依赖宿主襟翼（flap）修复与连接机制 | 靶向整合伴随靶位点重复（TSD）及宿主修复填补 |
| **支持的基因组重排类型** | 单一系统统一实现**插入（>140 kb）、切除（>130 kb）、倒位（0.93–2.3 Mb）、TRADE单步替换及跨门HGT**（[Perry et al., 2025](https://www.biorxiv.org/content/10.1101/2025.05.14.653916v2.full-text)；[Patel et al., 2026](https://www.biorxiv.org/content/10.64898/2026.04.29.721476v2.full-text)） | 插入、切除、倒位（必须在预设的固定识别位点之间进行） | 主要用于小片段敲除（Indel）或有限长度的同源重组敲入 | 碱基替换、小片段插入/缺失；大片段整合需偶联Bxb1分步进行（[MDPI, 2026](https://www.mdpi.com/2227-9059/14/9/2008)） | 主要局限于单向DNA插入，无法直接催化无痕切除或倒位 |
| **载荷容量与实测效率** | 细菌中高达142 kb无衰减插入（>90%）及2.3 Mb倒位；人类细胞中高达0.93 Mb倒位与20.2%–27.75%原位整合（[Perry et al., 2025](https://www.biorxiv.org/content/10.1101/2025.05.14.653916v2.full-text)；[Guo et al., 2026](https://pubmed.ncbi.nlm.nih.gov/42251048/)） | 容量大（数十至数百kb），配合着陆垫效率可达40%–75%，但需两步法 | HDR效率随插入片段增大急剧下降（通常限于<3–5 kb） | 纯PE限于数十bp；TwinPE+Bxb1可达5.6 kb插入与40 kb倒位 | 细菌中可达数十kb，但在哺乳动物细胞中多亚基递送复杂且效率受限 |

## 2. IS110与IS1111家族的基因组结构、分类学与演化起源

### 2.1 IS110家族的经典特征与长期未解之谜

插入序列（Insertion Sequences, IS）是细菌和古菌基因组中最简化的自主移动遗传元件（Mobile Genetic Elements, MGEs），通常仅包含编码自身移动所需转座酶的开放阅读框（ORF）以及两端的顺式作用序列（[Siguier et al., 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC7190074/)）。在ISfinder数据库收录的约28至30个IS家族中，绝大多数家族编码典型的DDE催化基序转座酶（如IS1、IS3、IS4、IS5等）或HUH核酸内切酶家族转座酶（如IS91、IS200/IS605），通过蛋白质直接识别元件两端的末端反向重复序列（Terminal Inverted Repeats, TIRs）完成剪切或复制转座，并在靶位点两侧留下特征性的靶位点重复（Target Site Duplications, TSDs）（[ASM Journals, 2015](https://journals.asm.org/doi/10.1128/microbiolspec.mdna3-0030-2014)）。


*图2.1：原核生物各插入序列（IS）家族的元件大小、末端反向重复（IR）、靶位点重复（DR/TSD）及转座酶催化化学分类总览表，其中IS110/IS1111家族独树一帜地采用DEDD催化基序并经历环状中间体（图片来源：[Siguier et al., Everyman's Guide to Bacterial Insertion Sequences, ResearchGate](https://www.researchgate.net/figure/Characteristics-of-insertion-sequence-families_tbl1_275827944)）。*

相比之下，首次在天蓝色链霉菌（*Streptomyces coelicolor*）温和噬菌体$\phi$C31衍生物中鉴定出的[IS110元件](https://pmc.ncbi.nlm.nih.gov/articles/PMC306192/)及其家族成员（如大肠杆菌中的IS621、假交替单胞菌中的IS492、恶臭假单胞菌中的ISPpu9和ISPpu10），展现出一系列截然不同的反常生物学特征：
1. **末端结构异常**：经典的IS110亚群元件完全缺乏末端反向重复序列（TIRs），或者仅具有极短的（2–3 bp）亚末端反向重复（STIRs）；而其姊妹分支IS1111亚群则具有长约7–17 bp的亚末端反向重复序列（STIRs）（[Durrant et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208160/)）。
2. **无痕切除与环状中间体**：IS110元件在从宿主基因组中切除时，不会在原位留下任何外源序列或缺失印记（即“无痕切除”，scarless excision），并且其左右两端会在核心双核苷酸序列（Core sequence，如`CT`）处精准拼接，形成共价闭合的双链环状DNA中间体（dsDNA minicircle）（[Durrant et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208160/)）。
3. **高度特异性的靶位点选择**：不同于随机或半随机整合的转座子，天然IS110和IS1111元件表现出极强的基因组靶位点专一性，常精准插入宿主基因组中的保守重复序列，如大肠杆菌的重复基因外回文序列（REP elements）、整合子（integron）的*attC*重组位点或其他转座子的TIR区域（[PMC2447020](https://pmc.ncbi.nlm.nih.gov/articles/PMC2447020/)；[Durrant et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208160/)）。
4. **独特的复合型DEDD-丝氨酸重组酶**：IS110家族是唯一使用**DEDD催化基序**的插入序列家族。其编码的单一重组酶（长约300–460个氨基酸）在N端具有一个与RuvC霍利迪交叉解离酶（Holliday junction resolvase）同源的**DEDD结构域（Pfam ID: PF01548）**，通过一段含两个$\alpha$-螺旋的卷曲螺旋（coiled-coil, CC）结构域连接至C端特有的**Tnp结构域（Pfam ID: PF02371）**，后者包含一个高度保守的催化丝氨酸残基（如IS621中的S241）（[Durrant et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208160/)；[Hiraizumi et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208158/)）。


*图2.2：IS110重组酶家族的序列保守性图谱（Durrant et al., 2024, Extended Data Fig. 1）。（a）基于213,171条比对序列生成的N端RuvC样结构域（PF01548）序列Logo图，箭头指示高度保守的DEDD四联体催化残基；（b）基于208,634条比对序列生成的C端Tnp结构域（PF02371）序列Logo图，箭头指示高度保守的催化丝氨酸（S）残基（图片来源：[Durrant et al., Nature 2024 / ResearchGate](https://www.researchgate.net/figure/Conserved-residues-in-the-RuvC-like-and-Tnp-domains-of-IS110-a-Sequence-logo-of-213-171_fig1_381737633)）。*

在长达数十年的时间里，由于研究人员无法在体外用纯化的IS110重组酶和DNA底物重构出转座活性，IS110究竟如何识别缺乏明显反向重复的自身末端以及高度特异性的宿主基因组靶标，一直是转座子生物学中的核心谜团（[Durrant et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208160/)）。

### 2.2 IS110与IS1111两大亚群的非编码区（LE/RE）不对称性与进化分化

通过对涵盖37,067个宏基因组、超过113万个细菌与古菌基因组及ISfinder数据库的系统挖掘（[Durrant et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208160/)），研究团队对28个IS家族的非编码末端长度分布进行了横向比较（对应原文**Fig. 1d**与**Extended Data Fig. 2**）。分析揭示，IS110家族拥有所有IS家族中最长的中位非编码末端（Non-coding ends，即重组酶CDS两侧的左端LE和右端RE），且分布范围极为紧凑，暗示这段非编码区承载着保守且不可或缺的遗传功能。


*图2.3：28个原核生物IS家族的最大非编码末端（RE–LE）长度分布箱线图（Durrant et al., 2024, Extended Data Fig. 2）。IS110家族具有显著长于其他家族且分布高度集中的非编码区，为编码结构化Bridge RNA提供了序列空间（图片来源：[Durrant et al., Nature 2024 / ResearchGate](https://www.researchgate.net/figure/Maximum-non-coding-end-length-distribution-of-28-IS-families-Distribution-of-non-coding_fig2_381737633)）。*

进一步对IS110与IS1111两大亚群进行比较基因组学与系统发育重建（对应[Durrant et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208160/)的**Fig. 6a–d**及**Extended Data Fig. 10a–c**），揭示了两者在结构组织上的镜像演化关系：

| 亚群分类 | 左端非编码区 (LE) 长度 | 右端非编码区 (RE) 长度 | 亚末端反向重复 (STIR) 特征 | Bridge RNA 编码位置与检出率 | 二级结构特征与代表性元件 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **IS110 亚群** | **显著长于 RE**（通常约150–250 bp） | 较短（通常约50–100 bp，含启动子-35区） | 极短，供体序列两侧仅存2–3 bp保守共变信号（如ATA/TAT） | 编码于 **LE 区**（共变模型预测检出率 **85.7%**） | 经典双内部环结构（5'茎环 + TBL茎环 + DBL茎环）；代表元件：IS621、IS622 (ISCro4)、ISPpu10、ISAar29、ISHne5（[Durrant et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208160/)） |
| **IS1111 亚群** | 较短 | **显著长于 LE** | 具有长约 **7–17 bp** 的典型STIR序列 | 编码于 **RE 区**（共变模型预测检出率 **93.0%**） | 供体结合核苷酸常位于复杂的多分支环（multi-loop）结构中，或形成紧凑型seekRNA（~70–100 nt，引导序列顺序与IS110相反）；代表元件：ISCARN28、ISAzs32、ISPa11、ISKpn4、ISEc11（[Durrant et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208160/)；[Siddiquee et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11187229/)） |


*图2.4：IS110与IS1111两大亚家族编码多样化Bridge RNA二级结构（Durrant et al., 2024, Fig. 6）。（a）IS110亚群LE显著长于RE，而IS1111亚群RE显著长于LE；（b）Bridge RNA在IS110（85.7%位于LE）和IS1111（93.0%位于RE）中的预测位置分布；（c）ISfinder中274个IS110/IS1111重组酶的系统发育树；（d）6个代表性元件（ISPpu10、ISAar29、ISHne5、ISCARN28、ISAzs32、ISPa11）的bRNA共识二级结构，蓝色标示靶标配对环，橙色标示供体配对环，绿色标示核心配对碱基（图片来源：[Durrant et al., Nature 2024 / ResearchGate](https://www.researchgate.net/figure/IS110-subfamilies-encode-distinct-and-diverse-bridge-RNA-secondary-structures-in_fig16_381737633)）。*


*图2.5：IS110/IS1111亚群序列特征与6种不同Bridge RNA的靶标/供体配对细节（Durrant et al., 2024, Extended Data Fig. 10）。（a）IS110供体序列共变分析揭示侧翼短3 bp STIR信号（ATA/TAT）；（b）IS110（长LE、短RE、短STIR）与IS1111（短LE、长RE、长STIR）元件架构对比；（c）6个代表性元件bRNA内部环与各自靶标（Target）和供体（Donor）围绕核心序列（下划线）的精确碱基配对对齐图（图片来源：[Durrant et al., Nature 2024 / ResearchGate](https://www.researchgate.net/figure/Detailed-analysis-of-diverse-bridge-RNA-sequences-and-their-predicted-targetanddonor_fig10_381737633)）。*

这一镜像分布表明，IS110与IS1111起源于共同的远古祖先，在演化分化过程中发生了Bridge RNA编码区在元件左端（LE）与右端（RE）之间的易位，并伴随亚末端反向重复序列（STIR）长度的扩张或缩减（[Durrant et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208160/)）。

### 2.3 从极简元件到100 kb级巨型基因货物平台的认知扩展（2026）

尽管早期研究将IS110定义为长约1.2–1.5 kb、仅编码单一重组酶和Bridge RNA的“极简”插入序列，但2026年8月发表的一项高通量连接图谱与大规模比较基因组学研究（[bioRxiv 2026.08.14.744561v2](https://www.biorxiv.org/content/10.64898/2026.08.14.744561v2.full-text)）彻底重塑了对自然界IS110尺度边界的认知：
* **微型极限的突破（843 bp极简活性元件）**：研究人员在自然界中鉴定出了一批远小于已知标准的微型IS110元件，包括缺失5'非翻译区但保留完整重组酶编码序列的~800 bp元件（由反式Bridge RNA驱动），并在无细胞体外转录-翻译（IVTT）系统中实验验证了一个**仅843 bp长、编码201个氨基酸微型重组酶**的天然IS110元件（原文**Fig. 1E, Fig. S3**）。该微型元件具有较长的引导-DNA配对区（LTG 10 bp、RTG 9 bp、LDG 9 bp、RDG 8 bp），能够高效完成供体环化与靶向整合。
* **巨型扩张连续体（高达~100 kb的抗生素耐药基因散播平台）**：在尺度谱系的另一端，自然界中的IS110位点可通过对侧翼序列的“半匹配（half-matches）”容忍度以及渐进式的DNA载荷捕获与串联重复，扩张形成延伸至**约100 kb**的巨型复合转座单元（原文**Fig. 1D**）。这些巨型IS110系统主要富集了源自质粒的DNA，其中以**抗菌药物耐药基因（AMR genes）**最为显著。这一发现证明IS110不仅是一种极简自私遗传元件，更是自然界微生物群落中散播适应性基因载荷的动态平台。

### 2.4 深层演化起源：从原核IS110转座子到古菌与真核生物snoRNP及剪接体（2025）

IS110系统的科学意义远超细菌转座本身。2025年1月发表于《Nature Microbiology》的一项演化生物学研究（[Nat Microbiol, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11930352/)）通过结构比对工具HHpred和Foldseek，揭示了细菌IS110重组酶与古菌/真核生物**Nop5家族蛋白（包括古菌Nop5、真核生物Nop56/Nop58）**以及**剪接体蛋白Prp31**之间惊人的同源性（对应其原文**Fig. 1a–e, Fig. 2a–c**及**Extended Data Figs. 1, 5–7**）：
1. **蛋白质三维结构与结构域同源**：IS110重组酶（PDB: 8WT7）、古菌Nop5（PDB: 7XPL）和真核Prp31（PDB: 2OZB）共享完全一致的三模块化拓扑结构——N端RuvC样结构域、中间卷曲螺旋（coiled-coil）二聚化结构域以及富含$\alpha$-螺旋的C端结构域（在Nop5和Prp31中被称为Nop结构域，对应IS110的Tnp结构域）。
2. **非编码引导RNA的构象趋同**：驱动RNA 2'-O-甲基化修饰的**C/D-box核仁小RNA（snoRNAs）**与IS110的**Bridge RNA**均具有标志性的大型凸出内部环（bulged-out internal loops），且均以成对引导序列（paired guide sequences）的方式在二聚体蛋白骨架上识别靶核酸（IS110识别DNA，snoRNP识别RNA）。
3. **跨界驯化（Exaptation）模型**：系统发育树拓扑结构表明，IS110重组酶与Nop5蛋白是RuvC超家族中的姊妹演化支。在细菌与古菌的最后共同祖先或早期古菌中，一个类似IS110重组酶的祖先蛋白经历了分子驯化——其N端RuvC样结构域丧失了DEDD核酸酶催化活性，转而演化出招募纤维蛋白（fibrillarin，甲基转移酶）和L7Ae（真核中为15.5 kDa/Snu13p）的蛋白互作界面，从而将原本用于**RNA引导的DNA重组**的IS110机器，改造为古菌和真核生物中负责**RNA引导的RNA修饰（snoRNP）**的核心机器；随后在早期真核生物中，Nop56/Nop58发生基因复制并演化出**Prp31**，结合U4/U6 snRNA参与真核生物**前体mRNA剪接（RNA splicing）**（[PMC11930352](https://pmc.ncbi.nlm.nih.gov/articles/PMC11930352/)）。这一发现与“IS200/IS605转座子TnpB/IscB演化为CRISPR-Cas9/Cas12”共同证明，原核生物转座子是生命演化史上复杂RNA引导机制的终极摇篮。


*图2.6：细菌IS110转座酶（IS110 Tnp）、古菌Nop5与真核剪接体蛋白Prp31的功能与三维结构相似性（Nat. Microbiol. 2025, Fig. 1）。（a）IS110 bRNA与古菌/真核C/D-box snoRNA及U4 snRNA二级结构对比；（b–d）IS110 Tnp（PDB: 8WT7）、Nop5（PDB: 7XPL）与Prp31（PDB: 2OZB）高度一致的“RuvC样结构域 + 卷曲螺旋 + C端$\alpha$-螺旋Nop/Tnp结构域”三维架构；（e）二聚体表面构象与引导RNA结合模式对比（图片来源：[Nat. Microbiol. 2025 / ResearchGate](https://www.researchgate.net/publication/387672972_Evolutionary_origins_of_archaeal_and_eukaryotic_RNA-guided_RNA_modification_in_bacterial_IS110_transposons)）。*


*图2.7：IS110家族转座酶与Nop5/Prp31家族共享共同演化祖先（Nat. Microbiol. 2025, Fig. 2）。系统发育树与简约演化模型展示了从远古IS110样RNA引导DNA重组机器，到古菌/真核C/D-box snoRNP（RNA 2'-O-甲基化修饰），再到真核U4/U6 snRNP剪接体组分Prp31的演化路径（图片来源：[Nat. Microbiol. 2025 / ResearchGate](https://www.researchgate.net/figure/IS110-family-transposases-share-a-common-evolutionary-ancestor-with-Nop5-family-proteins_fig2_387672972)）。*

## 3. 核心文献与关键图谱深度解析（2024–2026）

为全面梳理Bridge RNA与IS110领域自诞生以来的实验证据链，以下结合2024至2026年间发表的多项核心代表性研究及其文中的关键图表数据，对系统的发现、原子结构、哺乳动物工程化、反应方向性调控以及微生物组重写进行逐图剖析。

### 3.1 奠基之作（一）：Bridge RNA的发现、共变图谱与可编程三元重排（Durrant et al., *Nature* 2024）

在[Durrant et al., *Nature* 2024 (630: 984–993)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208160/)中，研究团队以大肠杆菌天然IS621元件为模型，完成了从计算预测到体外重构及体内全基因组重排的完整闭环验证：

* **Fig. 1 & Extended Data Figs. 1–3（IS110环化重构启动子并表达高亲和力ncRNA）**：
  * **蛋白与生命周期表征（Fig. 1a–c）**：展示IS621重组酶的N端DEDD RuvC样结构域与C端含催化S241的Tnp结构域，以及构建自1,054条非冗余IS110重组酶序列的系统发育树。当IS621从基因组切除形成环状中间体时，原本位于右端（RE）的`-35`区与位于左端（LE）的`-10`区跨越中央`CT`核心双核苷酸拼接，重构出一个经典的$\sigma^{70}$细菌启动子（$P_{\text{junc}}$）。
  * **小RNA测序与结合亲和力验证（Fig. 1e–g）**：在携带拼接RE–LE序列质粒的大肠杆菌中进行小RNA测序（small RNA-seq），在IS621及其5个近缘同源物的LE区检测到从预测转录起始位点（TSS）延伸约177 bp的连续高丰度转录峰（**Fig. 1e**）。利用微量热泳动（MST）测定体外转录的177 nt ncRNA与纯化IS621重组酶的结合能力，证实两者具有极高的特异性结合亲和力，平衡解离常数达到 **$K_D = 2.1 \pm 0.2\text{ nM}$**，而打乱序列的对照RNA则完全不结合（**Fig. 1f**）。对103个同源物LE序列的二级结构共识预测（ConsAlifold）显示，该ncRNA折叠为一个5'茎环以及两个带有显著内部环的发夹茎环（**Fig. 1g**，其中第一内部环序列保守性低，信息量仅$0.48 \pm 0.09$ bits，暗示其负责识别多变的宿主靶位点；第二内部环保守性较高，信息量为$0.93 \pm 0.11$ bits，对应**Extended Data Fig. 3c**）。


*图3.1：IS110移动遗传元件表达与其编码重组酶特异性结合的非编码RNA（Durrant et al., 2024, Fig. 1）。（a）IS110重组酶结构域示意图；（b）IS621元件生命周期：从基因组切除形成环状中间体，在RE–LE连接处跨越核心序列（绿色菱形）重构$\sigma^{70}$启动子驱动LE区转录ncRNA；（c）1,054条IS110重组酶的系统发育树；（d）8个IS家族非编码末端长度对比；（e）IS621及5个同源物RE–LE区域的small RNA-seq转录峰；（f）MST测定IS621重组酶与WT ncRNA的高亲和力结合（$K_D = 2.1 \pm 0.2\text{ nM}$）；（g）103个IS110 LE序列的ncRNA共识二级结构（图片来源：[Durrant et al., Nature 2024 / ResearchGate](https://www.researchgate.net/figure/IS110-mobile-genetic-elements-express-a-ncRNA-that-is-bound-by-its-encoded-recombinase-a_fig11_381737633)）。*

* **Fig. 2 & Extended Data Figs. 4–5（共变矩阵揭示双环分别配对靶DNA与供体DNA，实现体外四组分重构）**：
  * **大规模核苷酸共变分析（Fig. 2a,b）**：研究团队开发了类似MGEfinder的36轮迭代边界搜索算法，从宏基因组中重构了数千个IS110插入前后的靶位点与环状供体序列，并对**5,511对ncRNA-靶DNA（target–ncRNA）**和**2,201对ncRNA-供体DNA（donor–ncRNA）**进行了CCMpred伪似然耦合与碱基配对一致性分析（**Fig. 2b**）。热图矩阵中清晰浮现出四条强共变对角线信号：第一内部环（**靶标结合环，TBL**）的5'侧（8–9 nt）与11 bp靶位点的底链左侧（LT）互补（红色信号，$+1$），3'侧（4–7 nt）与靶位点顶链右侧（RT）互补（蓝色信号，$-1$）；第二内部环（**供体结合环，DBL**）的5'侧与22 bp供体DNA的底链左侧（LD）互补，3'侧与供体顶链右侧（RD，呈现9个RNA碱基非连续配对7个DNA碱基的特征）互补（**Fig. 2g,h**）。
  * **首次体外重组重构（In Vitro Recombination, Fig. 2c–f）**：将体外转录的177 nt Bridge RNA、纯化的IS621重组酶与含靶序列和供体序列的双链DNA寡核苷酸混合孵育，首次在体外成功检测并测序证实了预期的`LT–RD`和`LD–RT`重组产物（**Fig. 2d,e**），证明**这四种组分（重组酶、bRNA、靶DNA、供体DNA）是催化DNA重组的必要且充分条件**。MST实验进一步测得IS621 RNP复合体对野生型靶DNA的结合亲和力为 **$K_D = 13 \pm 6\text{ nM}$**，对野生型供体DNA为 **$K_D = 77 \pm 3\text{ nM}$**（**Fig. 2f**）。


*图3.2：鉴定IS621 Bridge RNA特异性识别靶DNA和供体DNA的双结合环（Durrant et al., 2024, Fig. 2）。（a,b）5,511对靶点-ncRNA与2,201对供体-ncRNA的共变矩阵，红色对角线代表与DNA底链互补，蓝色对角线代表与DNA顶链互补；（c–e）体外重组（IVR）实验证明重组酶、ncRNA、靶DNA与供体DNA四组分足以在体外生成LD–RT与LT–RD重组产物；（f）MST测定IS621 RNP对靶DNA（$K_D = 13\text{ nM}$）和供体DNA（$K_D = 77\text{ nM}$）的特异性结合；（g,h）Bridge RNA的靶标结合环（TBL：LTG/RTG，蓝色）与供体结合环（DBL：LDG/RDG，橙色）同靶DNA及供体DNA的双链交错配对模型（图片来源：[Durrant et al., Nature 2024 / ResearchGate](https://www.researchgate.net/figure/Identification-of-IS621-bridge-RNA-binding-loops-with-sequence-specific-recognition-of_fig12_381737633)）。*

* **Fig. 3 & Extended Data Fig. 6（靶位点的独立重编程与反式bRNA表达）**：
  * **大肠杆菌双质粒GFP报告系统（Fig. 3a–d）**：构建pTarget（含重组酶、50 bp靶位点及启动子）与pDonor（含RE–LE及无启动子*gfp*）。将野生型靶位点替换为7个全新的正交靶序列（T1–T7），并同步重编程bRNA的TBL，流式细胞术显示重编程bRNA完全消除了对WT靶标的活性，而在各自对应的T1–T7靶标上实现了**13.8%–59.5%**的阳性细胞重组率（**Fig. 3d**）；而将DEDD基序或S241突变为丙氨酸则彻底丧失活性（**Fig. 3b**）。
  * **顺式与反式解耦（Fig. 3e,f）**：将pDonor上的298 bp全长RE–LE截短为仅围绕核心序列的**22 bp极简供体序列**（去除了天然启动子`-35`区），并在质粒另一位置由合成启动子（J23119）以**反式（in trans）**独立表达bRNA，不仅完全恢复了重组活性，而且总GFP荧光强度比天然顺式启动子提高了近**2倍**（**Fig. 3f**）。


*图3.3：IS621靶位点可由Bridge RNA独立指定并重编程（Durrant et al., 2024, Fig. 3）。（a,b）大肠杆菌双质粒重组GFP流式报告系统及催化残基突变体（D11A、E60A、D102A、D105A、S241A）失活验证；（c,d）针对WT及T1–T7七个合成靶位点重编程TBL的正交重组矩阵，展现极高的序列专一性；（e,f）将298 bp RE–LE简化为22 bp供体序列并反式（in trans）表达bRNA，重组荧光信号较顺式（in cis）提升近2倍（图片来源：[Durrant et al., Nature 2024 / ResearchGate](https://www.researchgate.net/figure/The-IS621-target-site-is-reprogrammable-and-is-specified-by-the-bridge-RNA-a-Schematic_fig13_381737633)）。*

* **Fig. 4 & Extended Data Fig. 7（高通量文库筛选靶标特异性法则与RTG延伸提升全基因组精准度）**：
  * **万级条形码文库错配耐受度扫描（Fig. 4a–e）**：通过包含10,656个单错配、3,600个双错配及1,610个核心序列突变的寡核苷酸文库（偶联卡那霉素抗性筛选），证明`CT`核心双核苷酸的碱基配对受到极强选择偏好，且非核心的9个可编程位置（LT 1–7位，RT 10–11位）高度排斥单错配和双错配，同时在完美配对前提下具备广泛的序列可编程性（**Fig. 4b–e**）。
  * **大肠杆菌全基因组插入图谱与延伸RTG优化（Fig. 4f–i）**：利用温敏型单拷贝供体质粒（4.85 kb）进行大肠杆菌全基因组插入与纳米孔长读长测序，WT IS621在全基因组产生173个独特插入位点，其中144个位于天然REP重复元件内，**96.21%**的插入读长精确落在预期的`ATCAGGCCTAC`（允许第4位形成非经典rG:dT摆动配对）或完全匹配的`ATCGGGCCTAC`位点上（**Fig. 4g,h**）。针对大肠杆菌基因组中仅出现一次的4个独特内源位点进行重编程时，将RTG-RT配对长度从天然的**4 bp延伸至7 bp（Extended RTG）**，使全基因组靶向插入的中位平均特异性从**69.4%（范围51.2%–89.4%）显著提升至84.9%（范围65.4%–94.0%）**，并消除了大量脱靶位点（如bRNA 2消除了45个脱靶中的18个，bRNA 3消除了25个中的14个，对应**Fig. 4i**与**Extended Data Fig. 7e**）。
* **Fig. 5 & Extended Data Figs. 8–9（供体环重编程与插入、切除、倒位三元操作统一验证）**：
  * **供体序列高通量筛选与正交组合（Fig. 5a–g）**：通过包含13,593个单错配和5,000个完全随机供体引导序列的UMI文库，证明供体结合环（DBL）同样支持全面重编程（除LD第7位强烈排斥胞嘧啶C外，其余位置均严格要求碱基互补，**Fig. 5b–e**）。此外，在7 bp延伸RTG的辅助下，核心双核苷酸可从天然`CT`重编程为`AT`、`GT`或`TT`（**Extended Data Fig. 8a–d**）。针对9个与WT差异巨大的合成供体序列（D1–D9）重编程DBL，在对应供体上实现了**26.9%–95.0%**的细胞重组率且与WT供体完全正交（**Fig. 5f,g**）。
  * **可编程切除与倒位（Fig. 5h–k）**：当靶位点与供体位点位于同一DNA分子且**同向排列**（LD与LT位于同一链）时，系统高效介导两识别位点间1 kb转录终止子序列的**可编程切除（Excision，效率32.2%–98.9%，Fig. 5h,j）**；当两识别位点位于同一分子但**反向排列**（位于相反链）时，系统高效介导约900 bp *gfp*编码区的**可编程倒位（Inversion，效率4.54%–98.2%，Fig. 5i,k）**。


*图3.4：Bridge RNA供体编码区的重编程赋能完全可编程的DNA插入、倒位与切除（Durrant et al., 2024, Fig. 5）。（a–e）UMI高通量文库筛选揭示DBL在7 bp LD与2 bp RD位置的可编程性与错配敏感度；（f,g）D1–D9九组重编程供体与对应DBL的正交重组矩阵；（h–k）通过改变同一DNA分子上靶序列与供体序列的相对取向（同向或反向），高效实现可编程DNA切除（h,j）与可编程DNA倒位（i,k）（图片来源：[Durrant et al., Nature 2024 / ResearchGate](https://www.researchgate.net/figure/Bridge-RNA-donor-recoding-enables-fully-programmable-insertion-inversion-and-excision-a_fig15_381737633)）。*


*图3.5：IS621桥接重组系统介导插入（Insertion）、切除（Excision）与倒位（Inversion）的拓扑逻辑及大肠杆菌流式细胞术门控数据（Durrant et al., 2024, Extended Data Fig. 9）（图片来源：[Durrant et al., Nature 2024 / ResearchGate](https://www.researchgate.net/figure/Insertion-excision-and-inversion-using-the-IS621-bridge-recombination-system-a_fig9_381737633)）。*

### 3.2 奠基之作（二）：IS621突触复合体的四态冷冻电镜结构与“握手配对”催化机制（Hiraizumi et al., *Nature* 2024）

在同期背靠背发表的[Hiraizumi et al., *Nature* 2024 (630: 994–1002)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208158/)中，Hiroshi Nishimasu团队与Patrick Hsu团队合作，利用单颗粒冷冻电镜（Cryo-EM）解析了IS621重组酶-bRNA-靶DNA-供体DNA突触复合体（synaptic complex）在反应循环四个关键状态的原子分辨率结构：**链交换前状态（Pre-strand exchange state，2.52 Å，PDB: 8WT6 / EMD-37827）**、**链交换前锁定状态（Pre-HSB locked state，2.72 Å，PDB: 8WT7 / EMD-37828）**、**链交换后霍利迪交叉中间体状态（Post-strand exchange State 1 / HJ intermediate，2.88 Å，PDB: 8WT8 / EMD-37829）**以及**霍利迪交叉解离状态（Post-strand exchange State 2 / HJ resolution，2.73 Å，PDB: 8WT9 / EMD-37830）**：

* **Fig. 1 & Extended Data Figs. 1–3（四聚体突触复合体架构与两条独立bRNA的跨分子组装）**：
  * **结构域精确划分（Fig. 1b,h）**：326个氨基酸的IS621重组酶单体由N端**RuvC结构域（残基1–122，含D11、E60、D102、D105构成的DEDD基序，呈5股$\beta$-折叠夹4个$\alpha$-螺旋的RNase H折叠）**、中间双股$\alpha$-螺旋**卷曲螺旋二聚化结构域（CC，残基123–188）**以及C端由7个$\alpha$-螺旋组成的独特**Tnp结构域（残基189–326，催化残基S241位于$\alpha 3$与$\alpha 4$之间的环区，Dali搜索证实该折叠在已知蛋白质结构库中无任何同源物）**构成。
  * **双二聚体X型架构与双bRNA分子来源（Fig. 1e–g & Extended Data Fig. 2k）**：突触复合体由四个IS621原聚体（IS621.1–4）组成两个二聚体：IS621.1/2二聚体结合bRNA的TBL与38 bp靶DNA（tDNA），IS621.3/4二聚体结合DBL与44 bp供体DNA（dDNA）；tDNA与dDNA在中央催化中心周围强烈弯曲，呈X型交叉架构。电镜密度图揭示了一个意想不到的关键事实：在单个突触复合体中，TBL的3'端（C95）与DBL的5'端（A110）相距约**80 Å**（建模显示即使算上无序连接区U96–A109，C98与C99仍相距约40 Å，**Extended Data Fig. 2k**）。这表明**单个四聚体突触复合体中的TBL和DBL实际上分别来自两条不同的bRNA分子**（2D分类中亦观察到由两条bRNA串联起的突触复合体二聚体，且体外将TBL与DBL拆分为两条独立RNA分子同样支持高效重组，**Extended Data Fig. 6e**）。


*图3.6：IS621四聚体突触复合体的整体冷冻电镜结构（Hiraizumi et al., 2024, Fig. 1）。（a,b）IS621元件与重组酶结构域（RuvC、CC、Tnp）划分；（c,d）bRNA引导识别tDNA与dDNA的配对示意图及切割位点（黄色三角）；（e,f）IS621–bRNA–dDNA–tDNA突触复合体及核酸骨架三维结构，红色实心圆圈标示有序的复合活性位点（含形成5'-磷酸丝氨酸共价键的S241.2和S241.4），红色虚线圆圈标示无序位点；（g,h）IS621四聚体与单体的晶体学/电镜拓扑模型（图片来源：[Hiraizumi et al., Nature 2024 / ResearchGate](https://www.researchgate.net/figure/IS621-synaptic-complex-structure-a-Schematic-of-the-IS621-insertion-sequence-element_fig11_381737551)）。*


*图3.7：IS621突触复合体的冷冻电镜重构与跨分子bRNA组装证据（Hiraizumi et al., 2024, Extended Data Fig. 2）。（a,b）SEC纯化与SDS-PAGE显示共价IS621–DNA中间体慢迁移条带；（c–h）2.52 Å电镜重构流程与局部密度图，其中（d）的2D分类图像清晰捕捉到由两条bRNA分子连接而成的突触复合体二聚体；（i,j）5'茎环缺失对结合与重组活性的影响；（k）结构建模显示同一复合体内的TBL 3'端与DBL 5'端相距约40–80 Å，证实单个突触复合体中的TBL和DBL来自两条不同的bRNA分子（图片来源：[Hiraizumi et al., Nature 2024 / ResearchGate](https://www.researchgate.net/figure/Cryo-EM-analysis-of-the-IS621-synaptic-complex-a-Preparation-of-the_fig2_381737551)）。*


*图3.8：IS621重组酶单体与四聚体结构细节（Hiraizumi et al., 2024, Extended Data Fig. 3）。（a）IS621 RuvC结构域（结合单$\text{Mg}^{2+}$稳定5'-磷酸丝氨酸中间体）与Cas9 RuvC结构域（PDB: 7S4X，结合双$\text{Mg}^{2+}$催化水解）的对比；（b,c）四个IS621原聚体构象对比，显示IS621.2/4中S241环有序，而IS621.1/3中S241环无序；（d）四聚体中跨二聚体拼合的RuvC.1–Tnp.4（蓝圈）与RuvC.3–Tnp.2（品红圈）复合活性位点（图片来源：[Hiraizumi et al., Nature 2024 / ResearchGate](https://www.researchgate.net/figure/IS621-recombinase-structure-a-Structural-comparison-of-the-RuvC-domains-of-IS621-and_fig3_381737551)）。*

* **Fig. 2 & Extended Data Figs. 4–5（bRNA赝对称识别、疏水楔解旋与CT核心双核苷酸识别机制）**：
  * **TBL与DBL的赝对称构象与保守翻转碱基（Fig. 2a–c）**：TBL（nt 34–98）与DBL（nt 110–177）采用高度相似的H型赝对称三级结构，均包含标志性的外翻腺嘌呤（TBL中的A43/A67，DBL中的A116/A150）和采取*syn*（顺式）构象的鸟嘌呤（TBL中的G48/G72，DBL中的G121/G155），这些高度保守的碱基被四个原聚体的Tnp结构域以完全相同的方式特异性识别（**Extended Data Fig. 4**）。
  * **疏水楔（Hydrophobic Wedge）解旋双链DNA（Extended Data Fig. 5h–j）**：四个Tnp结构域中的保守疏水残基 **Y264、M265和M268** 像楔子一样直接插入tDNA（tA1–tT14\*与tA14–tT1\*之间）和dDNA（dA1–dT14\*与dT14–dA1\*之间）的双螺旋末端，破坏DNA碱基配对并促使其解旋，从而使LTG（A50–U58）/RTG（G77–G80）和LDG（A123–C130）/RDG（A157–U158/C162–G165）顺利侵入并形成RNA-DNA杂合双链。将这三个残基突变为丙氨酸（dWED: Y264A/M265A/M268A）导致大肠杆菌内重组活性急剧下降。
  * **CT核心双核苷酸的原子级识别（Extended Data Fig. 5c–g）**：解释了为何核心序列（第8、9位）偏好`CT`且第9位`T`几乎不可变：tDNA的tT9和dDNA的dT9碱基直接与RuvC.1和RuvC.3结构域中G63的主链酰胺基团形成特异性氢键；而第8位的tC8和dC8本身不直接接触蛋白，但与其配对的引导RNA碱基G80（RTG）和G165（RDG）与RuvC.1/RuvC.3的A61主链羰基形成氢键，且底链互补碱基tG7\*和dG7\*被RuvC.2/RuvC.4的N84侧链识别。


*图3.9：IS621重组酶与核酸（bRNA、tDNA、dDNA）的原子级相互作用全景图（Hiraizumi et al., 2024, Extended Data Fig. 4）。粗体标示TBL与DBL共有的外翻腺嘌呤（A43/A67/A116/A150）、顺式构象鸟嘌呤（G48/G72/G121/G155）以及CT核心核苷酸，青色圆圈代表催化位点中的$\text{Mg}^{2+}$离子（图片来源：[Hiraizumi et al., Nature 2024 / ResearchGate](https://www.researchgate.net/figure/Schematic-of-interactions-between-IS621-and-nucleic-acids-A43-A67-A116-A150-and_fig4_381737551)）。*


*图3.10：IS621的DNA双链解旋与核心序列识别机制（Hiraizumi et al., 2024, Extended Data Fig. 5）。（a,b）TBL–tDNA与DBL–dDNA复合物结构；（c–g）RuvC结构域中G63、A61和N84对CT核心双核苷酸及其互补碱基的氢键识别；（h–j）Tnp结构域疏水楔（Y264、M265、M268）插入DNA双螺旋末端促进解旋，突变疏水楔（dWED）使细菌内重组活性显著丧失（图片来源：[Hiraizumi et al., Nature 2024 / ResearchGate](https://www.researchgate.net/figure/DNA-recognition-mechanism-a-b-Structures-of-TBL-tDNA-a-and-DBL-dDNA-b-c-d_fig5_381737551)）。*

* **Fig. 3 & Extended Data Fig. 6（跨二聚体RuvC–Tnp复合活性中心与不对称界面防止靶-靶错误重组）**：
  * **“借刀催化”的跨二聚体复合活性中心（Fig. 3c–h）**：不同于Cas9中RuvC结构域独立利用双$\text{Mg}^{2+}$催化水解切割，IS621的RuvC结构域和Tnp结构域单独均无活性。唯有当两个二聚体通过RuvC–RuvC界面组装成四聚体突触复合体时，**Tnp.4的S241催化环穿过DBL伸入RuvC.1的活性口袋（构成RuvC.1–Tnp.4复合活性位点，切割tDNA顶链tT9与tA10之间）**，而**Tnp.2的S241催化环穿过TBL伸入RuvC.3的活性口袋（构成RuvC.3–Tnp.2复合活性位点，切割dDNA顶链dT9与dA10/dT10之间）**。在活性中心内，RuvC.1/RuvC.3的D102与Tnp.4/Tnp.2的G242形成氢键以稳定S241环构象，而D11、E60和D105配位一个**单$\text{Mg}^{2+}$离子**及两个水分子，稳定S241亲核进攻形成的**5'-磷酸丝氨酸共价中间体（5'-phosphoserine intermediate）**和游离3'-OH末端（**Fig. 3f,g**）。此时另外两个原聚体（Tnp.1和Tnp.3）的S241环处于无序状态，远离各自的RuvC伙伴。这种精妙的“跨二聚体授权（licensing）”机制确保了DNA切割绝不会在完整的四聚体突触复合体组装完成前发生。
  * **DBL茎环（DBL-SL）的不对称稳定作用（Extended Data Fig. 6b–d & Supplementary Fig. 3）**：DBL特有的长茎环（DBL-SL）中的U142、U143和C144与对侧二聚体RuvC.1的T30、H28和R27形成碱基特异性接触；而TBL的对应茎环（TBL-SL）较短，无法接触RuvC.3。这完美解释了为何两个IS621–TBL–tDNA二聚体无法组装成四聚体（因缺乏DBL-SL–RuvC互作），从而在天然状态下**完全阻止了危险的基因组靶位点-靶位点（target–target）错误重组**，而两个IS621–DBL–dDNA二聚体则能通过双侧DBL-SL互作介导供体-供体（donor–donor）重组。
* **Fig. 4, Fig. 5 & Extended Data Figs. 7–10（握手引导配对驱动链交换与霍利迪交叉解离的完整循环）**：
  * **握手引导序列（Handshake Guides, HSGs）的发现与功能验证（Extended Data Figs. 7–8）**：共变分析在bRNA的RTG紧邻区（第81–82位）和RDG紧邻区（第166–167位）发现了神秘的跨环共变信号——它们不与各自原本结合的DNA配对，而是分别与**交换过来的对侧DNA顶链第6–7位（Handshake Bases, HSB）**互补。研究团队将其命名为**握手引导序列（HSGs）**。体外与体内实验及电镜结构（PDB: 8WT7）证实：若将HSG突变为与自身原配DNA互补（pre-HSB bRNA），复合体虽能切割顶链，但会被死死锁在链交换前状态（Pre-strand exchange locked state），无法产生重组产物；反之，设计HSG使其与交换后的非原配DNA顶链互补（post-HSB bRNA），则能通过形成新的Watson-Crick碱基对，像热力学棘轮一样驱动切割后的顶链跨越活性中心发生交换并重新连接（**Fig. 4d–f**，State 1，2.88 Å，形成霍利迪交叉中间体）。


*图3.11：共变分析揭示握手引导序列（HSGs）的跨环配对潜能（Hiraizumi et al., 2024, Extended Data Fig. 7）。（a）红色箭头与橙色箭头分别指示TBL-HSG（P81）与供体DNA第7位（dDNA P7）、以及DBL-HSG（P166）与靶DNA第7位（tDNA P7）之间的跨环共变信号；（b）顶链交换前后TBL–tDNA与DBL–dDNA碱基配对模式重排示意图（图片来源：[Hiraizumi et al., Nature 2024 / ResearchGate](https://www.researchgate.net/figure/Covariation-analysis-a-Nucleotide-covariation-and-base-pairing-potential-between-bRNAs_fig7_381737551)）。*


*图3.12：握手碱基配对（Handshake Base-Pairing）对链交换的决定性影响（Hiraizumi et al., 2024, Extended Data Fig. 8）。（a,b）与链交换前原配DNA互补的pre-HSB bRNA虽能切割顶链，但将复合体死锁在切割态而无法生成重组产物；而与交换后对侧DNA互补的post-HSB bRNA则大幅提升体外重组产物比例并消除切割副产物；（c）大肠杆菌内验证DBL-HSG配对对重组效率的调控（图片来源：[Hiraizumi et al., Nature 2024 / ResearchGate](https://www.researchgate.net/figure/Effects-of-handshake-base-pairing-a-Schematics-of-the-TBL-DBL-and-tDNA-dDNA-sequences_fig8_381737551)）。*

  * **构象切换与底链切割解离（Fig. 4g–i & Fig. 5a,b）**：在随后的霍利迪交叉解离状态（State 2，2.73 Å，PDB: 8WT9）中，原本无序的**Tnp.1和Tnp.3的S241催化环变为有序状态**，分别与RuvC.4和RuvC.2组装成新的复合活性中心（RuvC.2–Tnp.3和RuvC.4–Tnp.1），在tC9\*–tC10\*和dT9\*–dA10\*之间切割tDNA和dDNA的底链（S241.3和S241.1分别与tC10\*和dA10\*形成5'-磷酸丝氨酸共价键），从而解离霍利迪交叉并完成整个重组反应（**Fig. 5b**）。此外，与经典酪氨酸重组酶Cre（PDB: 1CRX/3CRX）相比，IS621突触复合体中两条DNA分子的相对夹角相差约$180^\circ$，导致IS621形成**平行（parallel）**取向的霍利迪交叉中间体，而Cre形成反平行（antiparallel）取向（**Extended Data Fig. 10**）。


*图3.13：IS621介导的链交换与霍利迪交叉形成/解离机制（Hiraizumi et al., 2024, Fig. 4）。（a–c）链交换前状态（Pre-strand exchange，PDB: 8WT6）：顶链在黄色三角处被切割形成5'-磷酸丝氨酸中间体；（d–f）链交换后状态1——霍利迪交叉中间体（State 1，2.88 Å，PDB: 8WT8）：顶链跨越中心交换并在绿色/青色三角处重新连接，HSG（第81–82位与166–167位）与交换过来的DNA顶链第6–7位配对；（g–i）链交换后状态2——霍利迪交叉解离态（State 2，2.73 Å，PDB: 8WT9）：第二组复合活性位点有序化并切割底链（图片来源：[Hiraizumi et al., Nature 2024 / ResearchGate](https://www.researchgate.net/figure/Strand-exchange-mechanism-a-i-Schematics-of-TBL-tDNAandDBL-dDNA-and-the-structures-of_fig14_381737551)）。*


*图3.14：链交换后State 1与State 2的活性中心接力切换（Hiraizumi et al., 2024, Extended Data Fig. 9）。（a,b）在State 1中仅RuvC.1–Tnp.4与RuvC.3–Tnp.2有序（红实心圈），而在State 2中Tnp.1与Tnp.3的S241环也变为有序（四个红实心圈），激活RuvC.2–Tnp.3与RuvC.4–Tnp.1底链切割位点；（c–j）顶链重连与底链切割位点的局部冷冻电镜密度图（图片来源：[Hiraizumi et al., Nature 2024 / ResearchGate](https://www.researchgate.net/figure/Structures-of-the-IS621-synaptic-complexes-in-the-post-strand-exchange-states-a-b_fig9_381737551)）。*


*图3.15：Bridge RNA引导的DNA重组完整分子机制总结图（Hiraizumi et al., 2024, Fig. 5）。（a）两个IS621二聚体分别结合来自两条不同bRNA的TBL和DBL，各自识别tDNA与dDNA后组装为四聚体突触复合体；（b）从顶链切割（5'-磷酸丝氨酸中间体）、HSG驱动的顶链交换与重连（形成霍利迪交叉中间体），到底链切割与重组完成的完整催化循环（图片来源：[Hiraizumi et al., Nature 2024 / ResearchGate](https://www.researchgate.net/figure/Bridge-recombination-mechanism-a-b-Proposed-mechanisms-of-the-IS621-synaptic-complex_fig15_381737551)）。*


*图3.16：IS621与经典酪氨酸重组酶Cre（PDB: 1CRX/3CRX）的对比（Hiraizumi et al., 2024, Extended Data Fig. 10）。IS621利用bRNA识别DNA并形成5'-磷酸丝氨酸中间体，且两条DNA分子夹角与Cre相差约$180^\circ$，生成平行（parallel）霍利迪交叉；而Cre通过蛋白质直接识别loxP序列，形成3'-磷酸酪氨酸中间体与反平行（antiparallel）霍利迪交叉（图片来源：[Hiraizumi et al., Nature 2024 / ResearchGate](https://www.researchgate.net/figure/Comparison-of-IS621-and-Cre-Comparison-of-the-synaptic-complex-structures-DNA_fig10_381737551)）。*

### 3.3 独立平行突破：IS1111与IS110家族的seekRNA引导靶向机制（Siddiquee et al., *Nature Communications* 2024）

几乎在Arc研究所发表Bridge RNA的同时，悉尼大学Sandro F. Ataide团队联合Ruth M. Hall等学者在《Nature Communications》发表了关于IS1111和IS110家族转座机制的独立研究（[Siddiquee et al., 2024, PMC11187229](https://pmc.ncbi.nlm.nih.gov/articles/PMC11187229/)）：
* **跨亚群功能验证**：该研究选取了4个靶向不同序列的IS1111家族成员（包括靶向整合子*attC*位点或Tn21转座子TIR的成员，如ISKpn4、ISPa11、ISEc11等）和1个IS110家族成员（ISEc21），证明其非编码区（NCR）转录出一段长约**70–100 nt**的紧凑型搜寻RNA——被命名为**seeker RNA（seekRNA）**。
* **双向链识别与引导顺序反转**：与Bridge RNA一致，seekRNA与约350 aa的DEDD转座酶共纯化，并通过内部的靶标序列和供体序列分别识别靶标双链的顶链和底链，在无需宿主因子的情况下实现大片段DNA货物的位点特异性无痕插入。尤为关键的是，该研究发现IS1111家族（NCR位于转座酶基因下游RE区）与IS110家族（NCR位于转座酶基因上游LE区）中匹配靶DNA顶链与底链的短序列排列顺序恰好**相反（reversed）**，这两项背靠背的独立工作相互印证，确立了IS110/IS1111超家族普适的RNA引导DNA重组法则。


*图3.17：IS1111与IS110家族成员的基因组组织特征对比（Siddiquee et al., 2024, Fig. 1）。展示IS1111家族（具有亚末端反向重复sTIR，非编码区NCR位于转座酶基因下游RE端）与IS110家族（无明显sTIR，NCR位于转座酶基因上游LE端）的结构差异及靶位点对齐关系（图片来源：[Siddiquee et al., Nat. Commun. 2024 / ResearchGate](https://www.researchgate.net/figure/IS1111-and-IS110-family-features-a-Organisation-of-IS1111-and-IS110-family-members_fig1_381549892)）。*


*图3.18：IS1111家族成员ISEc11转座所需的环状中间体、启动子及seekRNA二级结构特征（Siddiquee et al., 2024, Fig. 2）（图片来源：[Siddiquee et al., Nat. Commun. 2024 / ResearchGate](https://www.researchgate.net/figure/Features-of-the-IS1111-family-member-ISEc11-required-for-transposition-a-Circular_fig2_381549892)）。*


*图3.19：IS110家族成员ISEc21的微环（Minicircle）连接序列、seekRNA结构与转座活性验证（Siddiquee et al., 2024, Fig. 6）（图片来源：[Siddiquee et al., Nat. Commun. 2024 / ResearchGate](https://www.researchgate.net/figure/Features-of-the-IS110-family-member-ISEc21-required-for-transposition-a-Minicircle_fig6_381549892)）。*


*图3.20：seekRNA引导IS1111与IS110家族转座酶进行靶向选址与转座的分子机制模型（Siddiquee et al., 2024, Fig. 7）（图片来源：[Siddiquee et al., Nat. Commun. 2024 / PMC11187229](https://pmc.ncbi.nlm.nih.gov/articles/PMC11187229/)）。*

### 3.4 人类细胞工程化里程碑：IS622（ISCro4）与enIS621–tebRNA实现哺乳动物基因组重排（2025–2026）

将原核IS110系统转化为哺乳动物及人类细胞基因组编辑工具，是该领域走向临床转化的核心一步。2025年9月至2026年7月间，多支国际团队相继报道了人类细胞桥接重组系统的重大工程化突破（[Perry et al., *Science* 2025](https://arcinstitute.org/news/bridge-recombinases-human-cells)；[Guo et al., *Nat. Commun.* 2026](https://pubmed.ncbi.nlm.nih.gov/42251048/)；[Pelea et al., 2026](https://www.researchgate.net/publication/400507050_Programmable_genome_editing_in_human_cells_using_RNA-guided_bridge_recombinases)）：

* **Fig. 1 & Figs. S1–S4（72个天然同源物高通量筛选鉴定出高活性正交物IS622 / ISCro4）**：
  * Patrick Hsu、Silvana Konermann与Hiroshi Nishimasu团队从细菌基因组中挖掘并合成了**72种不同的天然桥接重组酶系统**，在人类细胞（HEK293FT和K562）中进行活性筛选（[Perry et al., 2025](https://www.biorxiv.org/content/10.1101/2025.05.14.653916v2.full-text)）。虽然约25%的系统显示出微弱活性，但唯有源自啮齿类柠檬酸杆菌（*Citrobacter rodentium*）的**ISCro4**（被命名为**IS622**，其重组酶与IS621具有88%氨基酸序列一致性，bRNA具有86.6%序列一致性，AlphaFold3模型与IS621冷冻电镜结构的$\text{C}\alpha$ RMSD仅为2.5 Å，**Fig. 1H,I & Figs. S2–S3**）表现出高出背景4倍以上的显著天然重组活性。IS622–bRNA复合体能够识别靶DNA和供体DNA中各**14 bp**的序列，并通过HSG与HSB的链交换后配对推动反应正向进行。
* **Fig. 2 & Fig. S5（bRNA理性工程化与分裂双环机制验证）**：
  * 通过对IS622 bRNA进行系统的点突变、茎环稳定化改造以及删除未配对冗余碱基（例如稳定TBL构象并消除TBL与DBL之间的连接区），理性设计的**增强型bRNA支架（enhanced bRNA scaffolds）**将重组活性提升了**3.5倍至6.4倍**（**Fig. 2B–E**）。
  * 更重要的是，受IS621结构中“两个二聚体分别结合不同bRNA分子的TBL和DBL”以及“DBL茎环（DBL-SL）单独即可稳定四聚体”的启发，研究团队测试了**拆分式设计（split bRNA design）**，证实仅递送一段**90 nt的独立DBL分子**即可高效驱动供体-供体（donor–donor）重组，甚至在同向重复序列切除中表现出比全长单分子bRNA更高的活性（**Fig. 2D, Fig. 3E,F**）。
* **Fig. 3 & Fig. S7（揭秘“DBL靶向基因组 + 正交供体”的高特异性黄金法则）**：
  * 在早期原核实验中，人们习惯按照自然界转座子的分工，用TBL识别基因组靶位点、用DBL识别外源供体质粒。然而在人类基因组（30亿碱基对）中，由于DBL-DBL四聚体具有完整的催化活性而TBL-TBL四聚体无活性，当外源质粒使用天然供体序列时，DBL极易在人类基因组中寻找类似供体的序列发生“donor–donor”脱靶整合。
  * **Fig. 3D–O**揭示了颠覆性的工程化策略：（1）在外源供体质粒上编码一段**人类基因组中完全不存在的正交识别序列（genome-orthogonal sequence）**，由TBL去识别该外源质粒；（2）反过来**编程DBL去识别人类内源基因组靶位点**。这一“角色互换”策略彻底消除了质粒诱导的脱靶，使人类全基因组靶向整合的特异性在*SBF2*位点高达**82%**，在*ANP32A*位点达到**9.8%**的初始效率（**Fig. 3H,N,O & Fig. S7H**）。
* **Fig. 4 & Fig. S9（人类细胞内深度突变扫描构建三突变增强型IS622重组酶）**：
  * 为了直接在人类染色质环境中进化蛋白质，研究团队将326 aa的IS622划分为65 aa的片段，直接在人类细胞内进行了全序列**深度突变扫描（Deep Mutational Scanning, DMS，Fig. 4A–D）**。
  * 结构映射显示（**Fig. 4G,H**），位于催化位点S241紧邻处的**S243H突变**能够通过组氨酸侧链与DNA磷酸骨架形成一个全新的氢键；同时，位于RuvC结构域、负责识别DBL茎环U142的残基优化（如T30S相关互作）显著增强了突触复合体稳定性。将筛选出的有益突变组合构建为**三突变增强型IS622重组酶（enhanced IS622 triple mutant）**，并与增强型bRNA支架及最优环取向联用，使跨位点的整合活性比原始WT系统提升了**9.8倍**，在人类基因组内源基因座（如*SBF2*）实现了高达**20.2%的无筛选原位整合效率**（**Fig. 4E,I–K**）。
* **Fig. 5（兆碱基尺度人类染色体重排与弗里德赖希共济失调/镰刀型细胞贫血治疗概念验证）**：
  * **兆碱基级倒位与切除**：利用增强型IS622系统，研究团队在人类细胞染色体内部实现了高达**0.93 Mb（93万碱基对）的精准倒位**和高达**0.13 Mb（13万碱基对）的精准切除**，且在测试尺度范围内未表现出明显的距离衰减效应。
  * **镰刀型细胞贫血（BCL11A增强子切除，Fig. 5D–F）**：针对红系前体细胞中调控胎儿血红蛋白表达的*BCL11A*基因增强子（DHS h+58中的GATA基序区域），编程bRNA介导区间精准切除，实现了高达**18.7%**的无DSB精准切除效率。
  * **弗里德赖希共济失调（Friedreich's ataxia致病GAA三核苷酸重复切除，Fig. 5H–J）**：针对导致神经退行性病变的*FXN*基因内源性GAA三核苷酸重复扩增，利用仅包含326 aa重组酶（976 nt mRNA）和**90 nt独立DBL**的极简组合，成功切除了8至35个重复单元；在发生切除的底物中，**40%的分子被切除了超过80%（>29个重复拷贝）的致病扩增序列**，且全程仅需递送RNA分子，无需任何外源供体DNA（[Perry et al., 2025](https://www.biorxiv.org/content/10.1101/2025.05.14.653916v2.full-text)）。
* **enIS621–tebRNA与Pelea et al.的平行验证（2026）**：
  * 2026年6月，Guo等人在《Nature Communications》（[Nat. Commun. 17: 7234, PubMed: 42251048](https://pubmed.ncbi.nlm.nih.gov/42251048/)）发表了对原始大肠杆菌IS621系统的理性改造，构建了**enIS621–tebRNA**系统。该系统在多种人类细胞系中对千碱基级（kb-scale）环状DNA供体实现了最高达**27.75%**的无痕整合效率（对10 kb大片段供体仍保持2.53%活性），并成功在T细胞治疗相关基因座完成了**CD19-CAR**的功能性整合，以及针对B型血友病的人凝血因子IX（**Factor IX, F9**）基因原位敲入。与此同时，Pelea等人（[ResearchGate, 2026](https://www.researchgate.net/publication/400507050_Programmable_genome_editing_in_human_cells_using_RNA-guided_bridge_recombinases)）亦独立利用冷冻电镜解析了ISCro4在人类细胞中的高活性结构决定簇，证实了基于全RNA递送（all-RNA delivery）的多千碱基切除、倒位与>6%的供体整合。


*图3.21：可编程RNA引导DNA重组（seekRNA与bridgeRNA）的作用机制概览图（图片来源：[Programmable RNA-Guided DNA Recombination, MDPI Biomedicines 2026](https://www.mdpi.com/2227-9059/14/9/2008)）。*

### 3.5 攻克天然“插入偏好”与方向性控制：切除效率暴增13,000倍（Hiraizumi et al., *Nature* 2026）

尽管桥接重组酶能够通过改变bRNA结合位点的相对取向来指定插入、切除或倒位，但研究人员发现天然IS110系统存在严重的**方向性不对称（directional asymmetry）**：在体外定量测定中，天然IS621催化正向DNA插入（Insertion）的效率高达**63%**，而催化逆向DNA切除（Excision）的效率却仅有**0.03%**（相差超过2,000倍，[MDPI, 2026](https://www.mdpi.com/2227-9059/14/9/2008)）。从演化角度看，这种“重插入、轻切除”的偏好有利于自私转座子在宿主基因组中稳定驻留并扩增，但却制约了其在致病序列清除等基因治疗场景中的应用。

2026年8月，Hiroshi Nishimasu与Patrick Hsu团队再次在《Nature》发表合作研究 *"Structural mechanism governing the directionality of bridge recombination"*（[Hiraizumi et al., *Nature* 2026, doi: 10.1038/s41586-026-10903-y](https://arcinstitute.org/news/bridge-recombinase-excision)），通过捕获IS621正在进行切除反应的冷冻电镜结构快照，从生物物理学和热力学层面彻底解开了这一谜题，并实现了对反应方向的人工逆转：

* **DNA几何构象的“弹簧效应”差异（U型高应变 vs. X型松弛态）**：
  * 冷冻电镜结构对比显示，切除绝非插入反应的简单逆过程。在**插入反应（Insertion）**中，靶DNA和供体DNA进入突触复合体时均被强烈弯曲成**高度应变的“U型（U-shape）”构象**，宛如两根被强行弯折的干意大利面（或上紧发条的弹簧）；一旦顶链被S241切割，积蓄的巨大机械应变能会驱动断裂的DNA链迅速向外弹开并跨越中心完成链交换。
  * 相反，在**切除反应（Excision）**中，由于插入后形成的左、右嵌合连接点（LH和RH chimeric junctions，各自包含一半靶序列和一半供体序列）需要由TBL和DBL跨两个位点识别，DNA双链在复合体中呈现出**松弛的线性交叉“X型（X-shape）”构象**。虽然复合活性中心依然能有效切割顶链，但缺乏机械弯曲势能的推动，切割后的DNA链难以自发交换位置，且容易组装出无催化活性的TBL-TBL死端复合体（[Arc Institute, 2026](https://arcinstitute.org/news/bridge-recombinase-excision)）。
* **握手引导序列（HSGs）的天然热力学棘轮与人工重写（13,000倍效率跃升）**：
  * 结构与生化分析揭示，天然IS621的bRNA握手引导序列（HSGs）被演化精心“做手脚（rigged）”以偏向插入：在插入反应中，HSG在顶链交换前（pre-TSE）仅与DNA形成**1个碱基对**，而在顶链交换后（post-TSE）立即与交换过来的DNA链形成**3个碱基对**。这种从“1 bp到3 bp”的自由能下降构建了一个强力的**热力学棘轮（thermodynamic ratchet）**，将插入反应拉向产物端，同时使逆向的切除反应面临巨大的热力学能垒。
  * 基于这一原理，研究团队提出了**确定性方向工程化法则（Deterministic Directionality Engineering）**：通过重写bRNA上的HSG双核苷酸序列，人为最大化切除路径中链交换后状态（post-TSE excision state）的碱基配对数量，利用碱基配对自由能补偿X型DNA构象的几何劣势。实验结果显示，在大肠杆菌中，经HSG重写优化的bRNA使**可编程DNA切除效率暴增了13,000倍**（[Arc Institute, 2026](https://arcinstitute.org/news/bridge-recombinase-excision)），真正实现了对基因组重排方向（插入或切除）的随心调控。

### 3.6 微生物组学与合成生物学突破：全基因组尺度重写、TRADE替换与可编程水平基因转移（Patel et al., 2026）

在原核生物与微生物组工程领域，2026年5月加州大学伯克利分校创新基因组研究所（IGI）Brady F. Cress、Jennifer Doudna等团队发表了题为 *"Bridge recombinase enables versatile rewriting of bacterial genomes"* 的系统性研究（[Patel et al., 2026, bioRxiv 2026.04.29.721476v2](https://www.biorxiv.org/content/10.64898/2026.04.29.721476v2.full-text)），将IS621桥接重组酶的应用推向了全染色体尺度与复杂肠道菌群原位编辑：

* **Fig. 1（大肠杆菌142 kb超大载荷无衰减插入、50 kb基因簇切除与2.3 Mb半染色体倒位）**：
  * **尺寸无关的超高载荷整合（Fig. 1A–F）**：在大肠杆菌中测试了从13.8 kb到**141.6 kb（近142 kb）**的一系列细菌人工染色体（BAC）载荷整合，惊人地发现整合效率在跨越一个数量级的载荷尺寸范围内始终维持在**>90%（最高达90.9%）**，完全没有传统转座子或CRISPR系统的尺寸衰减效应。
  * **全基因组尺度切除与倒位（Fig. 1G–K）**：利用靶向单一bRNA实现了对大肠杆菌Nissle 1917中长达**50 kb的致癌大肠杆菌素（colibactin）生物合成基因簇（BGC）**的精准无痕切除（71.4%–100.0%的基因型鉴定菌落为精准切除）；并通过将固定内源基因*galK*与随机转座的*hsvTK*配对，在全基因组范围内实现了高达**2.3 Mb的染色体大倒位**——相当于将整个大肠杆菌染色体翻转了一半，达到了环形细菌染色体倒位的理论物理极限。
* **Fig. 2 & Fig. 3（单一bRNA跨5个细菌门通用编辑与人类肠道微生物组原位靶向）**：
  * **跨门通用靶向（Fig. 2A–E）**：利用一条靶向细菌普遍保守的**16S rRNA基因**内14 nt序列的通用bRNA，配合复制型pEdit载体，在无需针对每个物种重新设计引导序列的情况下，成功编辑了横跨**5个细菌门（Phyla）的11种不同细菌分离株**（包括枯草芽孢杆菌 *Bacillus subtilis*、多形拟杆菌 *Bacteroides thetaiotaomicron*、谷氨酸棒杆菌 *Corynebacterium glutamicum* 等），转化子菌落中的16S位点整合率接近**100%**。
  * **复杂人类肠道菌群原位宏基因组编辑（Fig. 3A–E）**：在无需预先分离培养单菌株的情况下，直接对富集的婴儿粪便菌群和成人回肠菌群进行原位编辑，成功实现了婴儿菌群中全部11种可培养肠杆菌科（Enterobacteriaceae）物种（如弗氏柠檬酸杆菌、肺炎克雷伯菌、产气克雷伯菌等）以及成人菌群中大肠杆菌与多形拟杆菌的直接编辑，其中肠杆菌科的16S靶向准确率**>99.9%**（菌落抽检为100%）。
* **Fig. 4（正交核心双bRNA驱动的TRADE单步“搜索-替换”编辑）**：
  * 当同时共表达两条bRNA以期直接用外源供体替换基因组大片段时，若两条bRNA使用相同的`CT`核心双核苷酸，会发生严重的交叉反应（cross-reactivity）和单次重组质粒骨架整合。
  * 研究团队开发了**靶向重组酶辅助DNA交换技术（Targetable Recombinase Assisted DNA Exchange, TRADE，Fig. 4A–K）**：通过为两条bRNA分配**正交的核心双核苷酸（orthogonal cores）**彻底消除交叉反应，并在质粒骨架中引入反筛选标记*hsvTK*（配合核苷类似物dP淘汰单次重组中间体），将双重组替换效率推升至近100%。利用TRADE技术，团队一步完成了大肠杆菌Nissle 1917中**~50.4 kb大肠杆菌素BGC基因簇**的原位精准替换，阳性率**>85.7%**。
* **Fig. 5（可编程水平基因转移 Programmable HGT：跨门捕获与功能代谢通路移植）**：
  * 将TRADE策略反向应用于“基因捕获”，在无需同源重组（HR-independent）且无需体外分子克隆的条件下，直接从供体细菌染色体上精准捕获功能性基因簇（如荧光报告簇或乳糖代谢操纵子*lacZY*）至移动质粒，并跨门（interphylum）转移整合至密歇根克雷伯菌（*K. michiganensis*）、胡萝卜软腐假单胞菌（*P. simiae*）和谷氨酸棒杆菌（*C. glutamicum*）中，赋予受体菌全新的碳源利用能力（如以乳糖作为唯一碳源生长，**Fig. 5F–H**），奠定了“合成微生物组学（Synthetic Microbiomics）”的技术基石。

### 3.7 机制精修与全谱系图谱：双转座路径、序列-结构双重匹配门控与Evo-PIN大数据挖掘（2025–2026）

除上述核心进展外，2025年底至2026年10月期间发表的多项机制与计算研究进一步丰富了IS110家族的理论大厦：

1. **双独立转座路径的揭示（Sun et al., *bioRxiv* 2025.10.25）**：
   针对嗜热厌氧菌（*Caloranaerobacter azorensis*）IS110元件的研究发现，IS110转座子在体内实际上可利用两条机制截然不同的RNA引导转座路径（[Sun et al., 2025](https://www.biorxiv.org/content/10.1101/2025.10.25.684509.full)）：
   * **路径一（bRNA依赖的复制脱出-粘贴插入，Copy-out-paste-in）**：通过顶链切除与重连生成单链（ssDNA）或双链（dsDNA）环状中间体，保留原位转座子拷贝；其中dsDNA环状中间体主要通过顶链整合，效率比底链高出**>1,300倍**，提示宿主体内存在辅助因子或DNA复制过程参与后续单链插入向双链产物的转化。
   * **路径二（绕过环状中间体的直接顶链转移，Direct Top-Strand Transfer）**：由一条截短的仅含靶标结合环的RNA（TBL-only RNA）与全长bRNA协同作用，通过两步连续反应（先转移`LT–RD`，再由全长bRNA完成`LD–RT`转移）直接将转座子转移至新靶位点，无需形成游离的环状中间体。
2. **序列-结构双重匹配门控逻辑（ISPpu10，*bioRxiv* 2026.03 / 2026.09）**：
   在对恶臭假单胞菌（*Pseudomonas putida*）适应性实验室进化中介导>100 kb片段扩增的**ISPpu10**元件进行研究时，科学家发现其靶位点识别不仅依赖bRNA与靶DNA的碱基配对，还依赖靶DNA 5'端延伸区编码的一个富含GC的**发夹茎环结构（target-encoded stem-loop）**（[bioRxiv 2026.03.19.712850v2](https://www.biorxiv.org/content/10.64898/2026.03.19.712850v2.full-text)）。系统错配与补偿突变扫描（原文**Fig. 4B–G**）证实了**“序列-结构双重匹配（sequence–structure dual-match）”逻辑**：其中LTG–LT界面仅要求维持碱基互补即可容忍序列变化（如第5位C–G替换为U–A甚至将活性提升至WT的138.58%），而RTG–RT界面除第3位外兼具严格的序列特异性；更重要的是，将靶DNA上的这个5'发夹茎环作为一个**可移植的结构门控元件（portable structural gate）**移植到大肠杆菌靶位点旁，显著提高了靶向整合效率并大幅降低了全基因组脱靶。
3. **原核非编码序列空间的系统性挖掘与Evo-PIN嵌入（*bioRxiv* 2026.10.21）**：
   2026年10月最新发布的预印本（[bioRxiv 2026.10.21.760802v1](https://www.biorxiv.org/content/10.64898/2026.10.21.760802v1.full.pdf)）利用基因组基础模型与Evo-PIN嵌入（Evo-PIN embeddings）对原核生物非编码序列空间进行了全谱系映射（原文**Fig. 1A,B**），建立了自动提取重组酶邻近非编码簇、构建精修共变模型、重构靶点/供体边界并自动判定引导区长度的计算流水线，揭示了自然界中远超此前认知的bRNA结构多样性。

| 发表时间 | 代表性文献与研究团队 | 核心研究对象 | 关键技术突破与核心定量指标 | 核心图表涵盖内容 |
| :--- | :--- | :--- | :--- | :--- |
| **2024年6月** | [Durrant et al., *Nature* 630: 984–993](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208160/) (Arc Institute / Patrick Hsu) | 大肠杆菌 IS621 及 28 个 IS 家族宏基因组 | 首次发现并命名 Bridge RNA；证实四组分体外重构；反式表达与双环独立重编程；延伸 RTG（7 bp）将大肠杆菌全基因组靶向特异性从 **69.4% 提升至 84.9%**；实现可编程插入、切除（32.2%–98.9%）与倒位（4.54%–98.2%） | Fig. 1–6 & Ext. Data Fig. 1–10：系统发育树、小RNA-seq、MST亲和力（$K_D=2.1\text{ nM}$）、5,511/2,201对共变热图、万级文库错配扫描、全基因组纳米孔测序、IS110/IS1111镜像演化 |
| **2024年6月** | [Hiraizumi et al., *Nature* 630: 994–1002](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208158/) (东京大学 Hiroshi Nishimasu / Arc Institute) | IS621–bRNA–tDNA–dDNA 突触复合体 | 解析 4 个反应状态冷冻电镜结构（2.52–2.88 Å，PDB: 8WT6–8WT9）；揭示双 bRNA 跨分子组装、疏水楔解旋、跨二聚体 RuvC–Tnp 复合活性位点（5'-磷酸丝氨酸中间体）及握手引导序列（HSG）促链交换机制 | Fig. 1–5 & Ext. Data Fig. 1–10：四聚体结构、TBL/DBL赝对称与翻转碱基、RuvC.1–Tnp.4活性中心、HSG体外/体内验证、霍利迪交叉形成与解离、与Cre重组酶对比 |
| **2024年6月** | [Siddiquee et al., *Nat. Commun.* 15: 5235](https://pmc.ncbi.nlm.nih.gov/articles/PMC11187229/) (悉尼大学 Sandro Ataide / Ruth Hall) | 4 个 IS1111 成员与 1 个 IS110 成员 (ISEc21) | 独立鉴定出 70–100 nt 的紧凑型搜寻 RNA（seekRNA），阐明 IS1111 家族 RE 区编码引导 RNA 识别双链靶点的共性机制及与 IS110 相反的引导区排列顺序 | Fig. 1–7：IS1111 与 IS110 结构对比、微环形成、seekRNA 二级结构与靶向转座验证 |
| **2025年1月** | [Nat. Microbiol. 10: 20–27](https://pmc.ncbi.nlm.nih.gov/articles/PMC11930352/) (Pasteur Institute 等) | 细菌 IS110 Tnp、古菌/真核 Nop5 (Nop56/58) 与剪接体 Prp31 | 揭示真核 C/D-box snoRNP（指导 RNA 2'-O-甲基化）与剪接体蛋白 Prp31 起源于远古原核 IS110 转座酶与 Bridge RNA 的跨界分子驯化 | Fig. 1–2 & Ext. Data Fig. 1–7：IS110 Tnp（PDB: 8WT7）与 Nop5（PDB: 7XPL）、Prp31（PDB: 2OZB）三维结构叠合及演化树 |
| **2025年9月** | [Perry et al., *Science*](https://arcinstitute.org/news/bridge-recombinases-human-cells) / [bioRxiv](https://www.biorxiv.org/content/10.1101/2025.05.14.653916v2.full-text) (Arc Institute / Hsu & Konermann) | 柠檬酸杆菌源 IS622 (ISCro4) 及人类细胞 (HEK293FT, K562) | 筛选 72 个同源物获 IS622；通过 bRNA 支架改造、蛋白质深度突变扫描（三突变体）及“DBL 靶向基因组 + 正交供体”策略，在人类细胞实现 **20.2% 插入效率**、**82% 特异性**、**0.93 Mb 倒位**、**0.13 Mb 切除**，以及 *BCL11A* 增强子（18.7%）与弗里德赖希共济失调 GAA 重复序列切除 | Fig. 1–5 & Fig. S1–S9：72同源物筛选、AlphaFold3建模、bRNA支架工程、90 nt独立DBL、DMS突变热图、S243H氢键模型、人类全基因组特异性与疾病模型验证 |
| **2026年5月** | [Patel et al., *bioRxiv*](https://www.biorxiv.org/content/10.64898/2026.04.29.721476v2.full-text) (UC Berkeley IGI / Brady Cress) | IS621、跨 5 门 11 种细菌及人类肠道微生物组 | 大肠杆菌中实现 **142 kb 载荷 >90% 效率无衰减插入**、**50 kb BGC 切除**、**2.3 Mb 半染色体倒位**；单 bRNA 跨 5 门 11 物种通用编辑及肠道菌群原位编辑；开发正交核心双 bRNA **TRADE 替换技术（>85.7% 效率）** 与可编程跨门水平基因转移（HGT） | Fig. 1–5 & Fig. S1–S22：BAC大片段插入曲线、全基因组倒位图谱、跨门16S靶向、婴儿/成人肠道宏基因组编辑、TRADE正交核心设计、跨门通路捕获与代谢表型恢复 |
| **2026年6月** | [Guo et al., *Nat. Commun.* 17: 7234](https://pubmed.ncbi.nlm.nih.gov/42251048/) (西北农林/南京大学等) | 工程化 enIS621–tebRNA 与人类细胞 | 理性改造大肠杆菌 IS621 及其 bRNA，在人类细胞实现最高 **27.75%** 的 kb 级供体无痕整合（10 kb 供体达 2.53%），完成 **CD19-CAR** 与人凝血因子 IX（**F9**）基因原位整合 | enIS621 蛋白突变与 tebRNA 支架优化图谱、人类细胞系整合效率对比、CAR-T 及血友病 B 基因治疗模型验证 |
| **2026年8月** | [Hiraizumi et al., *Nature*](https://arcinstitute.org/news/bridge-recombinase-excision) (东京大学 Nishimasu / Arc Institute Hsu) | IS621 插入与切除突触复合体 | 解析切除复合体冷冻电镜结构；揭示插入（U型高应变DNA + HSG 1 bp→3 bp热力学棘轮，体外63%）与切除（X型松弛DNA，体外0.03%）的生物物理不对称性；通过工程化重写 HSG 使大肠杆菌中 **DNA 切除效率提升 13,000 倍** | 插入（U型）与切除（X型）电镜结构对比图、嵌合位点（LH/RH）识别模型、HSG热力学棘轮与工程化切除效率柱状图 |
| **2026年8–10月** | [bioRxiv 744561](https://www.biorxiv.org/content/10.64898/2026.08.14.744561v2.full-text) / [bioRxiv 712850](https://www.biorxiv.org/content/10.64898/2026.03.19.712850v2.full-text) / [bioRxiv 760802](https://www.biorxiv.org/content/10.64898/2026.10.21.760802v1.full.pdf) | 843 bp极简元件、~100 kb巨型元件、ISPpu10 等 | 验证 **843 bp（201 aa）极简活性元件**并发现延伸至 **~100 kb 的耐药基因散播连续体**；揭示 ISPpu10 的“序列-结构（5'发夹茎环）双重匹配门控”逻辑；利用 Evo-PIN 映射原核非编码 bRNA 空间 | 尺度连续体分布图、ISPpu10 错配与补偿突变柔韧性图谱（Fig. 4B–G）、Evo-PIN 聚类图 |

## 4. 分子架构与生物物理催化机制综合剖析

综合上述结构生物学、生物化学与计算生物学证据，IS110桥接重组系统的分子运行机制可以归纳为四个严密偶联的生物物理层级：

### 4.1 环化诱导的顺式转录门控（Lifecycle Transcriptional Gating）

在宿主染色体上处于整合状态的IS110元件是转录沉默或低本底表达的，因为其启动子的`-35`区位于元件右端（RE，重组酶终止密码子下游），而`-10`区与转录起始位点（TSS）位于元件左端（LE，重组酶起始密码子上游）。只有当元件通过低本底表达或复制脱出形成共价闭合的环状中间体（RE–Core–LE连接）时，强效的接合启动子（$P_{\text{junc}}$）才被物理拼接完整，驱动下游LE区（IS110亚群）或RE区（IS1111亚群）转录出全长Bridge RNA（[Durrant et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208160/)）。这一机制在天然状态下充当了精密的“生命周期安全阀”：未脱离基因组的线性IS110拷贝不会大量表达bRNA，从而避免了在原位引发持续的基因组不稳定；而在人工工程化应用中，研究人员只需将bRNA置于外源组成型或诱导型启动子（如大肠杆菌J23119或哺乳动物U6启动子）下进行**反式表达（in trans）**，并将供体序列缩减至22 bp（甚至14 bp识别区），即可完全绕过环化步骤，直接驱动外源环状质粒或内源染色体位点之间的重组（[Durrant et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208160/)；[Perry et al., 2025](https://www.biorxiv.org/content/10.1101/2025.05.14.653916v2.full-text)）。

### 4.2 双链交错碱基配对（Dual-Strand Staggered Base-Pairing）与跨分子四聚体组装

不同于CRISPR-Cas9或Argonaute仅使用单链引导区识别靶DNA的一条链（形成单一R-loop并置换出非靶标链），Bridge RNA的TBL和DBL内部环采用独特的**双链交错识别模式**：
* **底链左侧配对（LTG–LT 与 LDG–LD）**：每个内部环的5'侧引导段（长约8–10 nt）与靶DNA或供体DNA核心序列左侧的**底链（bottom strand）**互补配对，且配对延伸覆盖核心双核苷酸的互补位点（如`3'-GA-5'`）。
* **顶链右侧配对（RTG–RT 与 RDG–RD）**：每个内部环的3'侧引导段（天然长约4–9 nt，可通过工程化延伸至7–9 nt）与靶DNA或供体DNA核心序列右侧的**顶链（top strand）**互补配对，同样延伸覆盖核心双核苷酸（如`5'-CT-3'`）。
* **核心双核苷酸重叠（Core Overlap）**：由于左引导区与底链的核心互补、右引导区与顶链的核心互补，核心双核苷酸（第8、9位）实际上同时参与了底链与顶链的RNA-DNA杂合配对。
* **两条bRNA分子协同构建突触四聚体**：在三维空间中，一个IS621/IS622二聚体结合一条bRNA的TBL并利用Tnp疏水楔（Y264/M265/M268）解旋tDNA，另一个二聚体结合**第二条bRNA分子**的DBL并解旋dDNA。随后，两个负载了DNA的RNP二聚体通过RuvC结构域界面相互靠拢，并依赖**DBL特有长茎环（DBL-SL，U142/U143/C144）与对侧RuvC.1（T30/H28/R27）的特异性相互作用**锁紧形成完整的四聚体突触复合体（[Hiraizumi et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208158/)）。

### 4.3 跨亚基RuvC–Tnp复合活性中心与分步霍利迪交叉催化循环

IS110重组酶在演化上巧妙融合了RuvC核酸酶的金属离子配位能力与丝氨酸重组酶的共价转酯化机制，其催化循环严格遵循四步有序列构象转换：
1. **复合活性位点跨二聚体拼合与顶链亲核切割**：四聚体组装后，Tnp.4的S241环穿过DBL插入RuvC.1口袋，Tnp.2的S241环穿过TBL插入RuvC.3口袋。在单$\text{Mg}^{2+}$离子（由RuvC的D11、E60、D105及水分子配位）的极化作用下，S241羟基对tDNA（tT9–tA10磷酸二酯键）和dDNA（dT9–dT10/dA10磷酸二酯键）发起亲核进攻，切断顶链并在5'端形成**共价5'-磷酸丝氨酸中间体（S241.4–tA10 与 S241.2–dT10）**，同时在tT9和dT9上释放出游离的3'-OH基团（[Hiraizumi et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208158/)）。
2. **U型机械应变释放与握手引导配对（HSG-HSB）驱动的顶链交换**：在插入反应中，处于U型高应变弯曲状态的tDNA和dDNA在顶链断裂后释放弹性能，携带5'-磷酸丝氨酸共价键的右半段顶链跨越中央通道交换至对侧二聚体。此时，对侧bRNA环上的**握手引导序列（HSGs，如TBL的81–82位与DBL的166–167位）**立即与交换过来的DNA顶链第6–7位（HSB）以及第8–9位核心序列形成新的Watson-Crick碱基对（从交换前的1 bp增加至交换后的3 bp），在热力学上锁定交换后的构象（[Hiraizumi et al., 2026](https://arcinstitute.org/news/bridge-recombinase-excision)）。
3. **顶链重连接与平行霍利迪交叉中间体形成（State 1）**：游离的dT9 3'-OH和tT9 3'-OH分别亲核进攻交换过来的tA10–S241.4和dT10–S241.2磷酸丝氨酸键，形成新的磷酸二酯键（`dT9–tA10`和`tT9–dT10`），释放出S241.4和S241.2，生成共价闭合的**平行霍利迪交叉中间体（Parallel Holliday Junction Intermediate）**（[Hiraizumi et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208158/)）。
4. **活性中心接力切换与底链切割解离（State 2）**：霍利迪交叉的形成触发四聚体内部的变构调节——原本无序的**Tnp.1和Tnp.3的S241催化环折叠有序**，分别与RuvC.4和RuvC.2构建出第二组复合活性中心（RuvC.2–Tnp.3和RuvC.4–Tnp.1），精准切割tDNA底链（tC9\*–tC10\*之间）和dDNA底链（dT9\*–dA10\*之间），形成S241.3–tC10\*和S241.1–dA10\*共价中间体，随后通过底链交换与重连（或在细胞内伴随错配修复与复制解离）彻底完成双链重组（[Hiraizumi et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208158/)）。

## 5. 理性工程化策略与设计法则总结

经过2024至2026年的密集攻关，研究界已建立起一套完整的Bridge RNA与IS110重组酶工程化设计准则（并集成于Arc研究所开源的[BridgeRNADesigner工具](https://github.com/hsulab-arc/BridgeRNADesigner)与[Cress实验室BridgeEvaluator工具](https://github.com/cress-lab/)中）：

| 工程化靶点与策略 | 具体分子改造手段 | 解决的核心瓶颈 | 实测性能提升效果 | 代表性文献依据 |
| :--- | :--- | :--- | :--- | :--- |
| **1. RTG 延伸策略 (Extended RTG)** | 将bRNA靶标结合环中的右靶标引导区（RTG）与靶DNA顶链的配对长度从天然4 bp扩展至 **7 bp（甚至9 bp）** | 天然短RTG在大基因组中识别特异性不足、脱靶率偏高；非CT核心活性低 | 大肠杆菌全基因组靶向特异性从平均 **69.4% 提升至 84.9%**，最高达 **94.0%**；赋能非经典核心（AT/GT/TT）的高效重组 | [Durrant et al., *Nature* 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208160/) (Fig. 4i, Ext. Data Fig. 7, 8) |
| **2. 握手引导序列 (HSG) 定向重写** | 重编程TBL（第81–82位）与DBL（第166–167位）的HSG碱基，消除链交换前（pre-TSE）配对，最大化链交换后（post-TSE）与对侧DNA第6–7位（HSB）的配对 | 天然系统存在强烈的“插入偏好”（体外插入63% vs 切除0.03%），导致逆向切除因X型松弛DNA构象而效率极低 | 消除体外切割副产物；在大肠杆菌中使可编程 **DNA切除效率暴增 13,000 倍**，实现插入/切除方向的可控切换 | [Hiraizumi et al., *Nature* 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208158/) (Ext. Data Fig. 8)；[Hiraizumi et al., *Nature* 2026](https://arcinstitute.org/news/bridge-recombinase-excision) |
| **3. “DBL靶向基因组 + 正交供体”反置法则** | 在外源供体质粒上使用人类基因组正交序列（由TBL识别），反过来**用DBL识别人类内源基因组位点** | 人类细胞中DBL-DBL四聚体活性导致外源供体与基因组内类供体序列发生“donor–donor”脱靶 | 在人类细胞（K562/HEK293FT）中全面消除质粒样脱靶，实现高达 **82% 的全基因组靶向特异性** | [Perry et al., *Science* 2025](https://www.biorxiv.org/content/10.1101/2025.05.14.653916v2.full-text) (Fig. 3D–O, Fig. S7H) |
| **4. bRNA 支架理性精简与独立 DBL 拆分** | 删除TBL茎环起始处未配对冗余碱基以稳定构象；或在同向重复切除中直接递送 **90 nt 独立 DBL RNA** | 全长bRNA在哺乳动物细胞内折叠效率受限；单分子双环在重复序列切除中存在空间位阻 | 增强型bRNA支架活性提升 **3.5–6.4 倍**；90 nt独立DBL在弗里德赖希共济失调GAA重复切除中实现40%分子清除>80%重复 | [Perry et al., *Science* 2025](https://www.biorxiv.org/content/10.1101/2025.05.14.653916v2.full-text) (Fig. 2B–E, Fig. 5H–J) |
| **5. 重组酶深度突变扫描 (DMS) 与活性口袋氢键强化** | 在IS622中引入 **S243H**（与DNA磷酸骨架形成新氢键）及RuvC–DBL互作界面突变，构建三突变增强型IS622；或构建工程化 **enIS621–tebRNA** | 细菌源天然重组酶在人类染色质微环境中催化效率不足 | 增强型IS622较原始系统活性提升 **9.8 倍**，人类内源位点无筛选插入率达 **20.2%**；enIS621–tebRNA在人类细胞实现最高 **27.75%** 整合率 | [Perry et al., *Science* 2025](https://www.biorxiv.org/content/10.1101/2025.05.14.653916v2.full-text) (Fig. 4A–K)；[Guo et al., 2026](https://pubmed.ncbi.nlm.nih.gov/42251048/) |
| **6. 正交核心双 bRNA 策略 (TRADE)** | 在双bRNA共表达系统中为两条bRNA分配不同的正交核心双核苷酸（如CT与非CT核心），配合质粒骨架*hsvTK*反筛选 | 共表达双bRNA进行片段替换时发生交叉反应（cross-reactivity）及单次重组质粒整合 | 完全消除双bRNA交叉副产物，实现50.4 kb生物合成基因簇的单步无HR原位替换，准确度 **>85.7%（最高近100%）** | [Patel et al., *bioRxiv* 2026](https://www.biorxiv.org/content/10.64898/2026.04.29.721476v2.full-text) (Fig. 4A–K) |
| **7. 靶标 5' 结构门控元件移植 (Structural Gate)** | 在靶位点5'延伸区引入或保留富含GC的发夹茎环结构（源自ISPpu10的双重匹配机制） | 单纯依赖14 bp RNA–DNA碱基配对在复杂基因组中仍存在一定错配容忍度 | 作为可移植的结构门控（portable structural gate），显著提升靶向整合率并抑制全基因组脱靶 | [bioRxiv 2026.03.19.712850v2](https://www.biorxiv.org/content/10.64898/2026.03.19.712850v2.full-text) (Fig. 4B–G) |

## 6. 当前技术局限、转化挑战与未来展望

尽管Bridge RNA与IS110重组酶系统在短短两年多时间内完成了从原核基础机制解析到人类兆碱基级基因组重排及微生物组工程的跨越，但作为一项新兴的基因组工程平台，其在迈向临床转化与工业级合成生物学应用的过程中仍面临若干关键挑战（[MDPI, 2026](https://www.mdpi.com/2227-9059/14/9/2008)）：

1. **序列容忍度与全基因组脱靶控制（Specificity vs. Plasticity）**：
   尽管IS621和IS622分别通过延伸RTG和“DBL靶向基因组”策略将大肠杆菌和人类细胞中的靶向特异性提升至84.9%–94.0%和82%，但由于Bridge RNA总识别长度约为11–14 bp（加上2 bp HSG），相比CRISPR-Cas9的20 nt间隔序列，其理论信息量仍相对偏小。高通量筛选表明，部分位置（如IS621靶位点第4位的rG:dT摆动配对、供体LD第7位，以及ISPpu10的LTG–LT界面）对单碱基错配具有一定容忍度（[Durrant et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208160/)；[bioRxiv 2026.03.19.712850v2](https://www.biorxiv.org/content/10.64898/2026.03.19.712850v2.full-text)）。在30亿碱基对的人类基因组中，这种单错配或半匹配（half-match）容忍度仍可能导致低频的脱靶插入或预期外的供体-供体（donor–donor）重排。未来结合具有更长天然引导区的新型IS110同源物（如2026年发现的含19 bp靶配对区的843 bp极简元件，[bioRxiv 2026.08.14.744561v2](https://www.biorxiv.org/content/10.64898/2026.08.14.744561v2.full-text)）或引入5'结构门控机制，将是进一步提升保真度的关键路径。
2. **原代人类细胞验证、大载荷效率衰减与体内递送（Primary Cells & In Vivo Delivery）**：
   目前人类细胞中的高效整合（20.2%–27.75%）与兆碱基重排主要在转化细胞系（HEK293FT和K562）中得到验证，且在人类细胞中当环状DNA供体从数kb增大至10 kb时，enIS621–tebRNA的整合效率从27.75%下降至2.53%（[Perry et al., 2025](https://www.biorxiv.org/content/10.1101/2025.05.14.653916v2.full-text)；[MDPI, 2026](https://www.mdpi.com/2227-9059/14/9/2008)）。在临床高度相关的原代人类T细胞、造血干细胞（HSCs）以及体内非分裂组织（如神经元、心肌细胞）中的编辑效率、细胞毒性及免疫原性仍有待全面评估。值得期待的是，由于IS110不依赖仅在分裂期活跃的宿主HDR通路，它在细胞周期阻滞（非分裂）的人类细胞中依然保持催化活性；特别是针对致病重复序列切除（如亨延顿舞蹈症、弗里德赖希共济失调、ALS）或染色体内调控元件倒位/切除（如*BCL11A*增强子），**完全无需递送外源DNA供体**，仅需通过脂质纳米颗粒（LNP）瞬时递送编码326 aa重组酶的mRNA（<1 kb）和90–180 nt的合成bRNA，即可实现“全RNA递送（all-RNA delivery）”的无痕基因组治疗（[Perry et al., 2025](https://www.biorxiv.org/content/10.1101/2025.05.14.653916v2.full-text)）。
3. **AI生成式设计与合成基因组学（AI-Guided Genome Design）**：
   随着Evo等基因组基础模型（Genomic Foundation Models）与Evo-PIN非编码RNA结构嵌入技术的成熟（[bioRxiv 2026.10.21.760802v1](https://www.biorxiv.org/content/10.64898/2026.10.21.760802v1.full.pdf)），研究人员已能够从头生成具有极高复杂度的合成基因簇与定制化Bridge RNA。将AI设计的百万碱基级合成DNA载荷与IS110桥接重组酶的超大片段无痕操纵能力相结合，正推动生命科学从“逐个碱基修补基因缺陷”迈向“在染色体与生态群落尺度上按需编写基因组”的全新纪元。

## 7. 参考文献与数据资源列表

1. **Durrant, M. G., Perry, N. T., Pai, J. J., Jangid, A. R., Athukoralage, J. S., Hiraizumi, M., McSpedon, J. P., Pawluk, A., Nishimasu, H., Konermann, S., & Hsu, P. D.** (2024). Bridge RNAs direct programmable recombination of target and donor DNA. *Nature*, 630(8018), 984–993. [PMC11208160](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208160/) | [PubMed: 38926615](https://pubmed.ncbi.nlm.nih.gov/38926615/)
2. **Hiraizumi, M., Perry, N. T., Durrant, M. G., Soma, T., Nagahata, N., Okazaki, S., Athukoralage, J. S., Isayama, Y., Pai, J. J., Pawluk, A., Konermann, S., Yamashita, K., Hsu, P. D., & Nishimasu, H.** (2024). Structural mechanism of bridge RNA-guided recombination. *Nature*, 630(8018), 994–1002. [PMC11208158](https://pmc.ncbi.nlm.nih.gov/articles/PMC11208158/) | [PubMed: 38926616](https://pubmed.ncbi.nlm.nih.gov/38926616/)
3. **Siddiquee, R., Pong, C. H., Hall, R. M., & Ataide, S. F.** (2024). A programmable seekRNA guides target selection by IS1111 and IS110 type insertion sequences. *Nature Communications*, 15, 5235. [PMC11187229](https://pmc.ncbi.nlm.nih.gov/articles/PMC11187229/) | [University of Sydney News](https://www.sydney.edu.au/news-opinion/news/2024/06/25/beyond-crispr-seekrna-delivers-new-pathway-accurate-gene-editing.html)
4. **Perry, N. T., Bartie, L. J., Katrekar, D., Gonzalez, G. A., Durrant, M. G., Pai, J. J., Fanton, A., Martins, J. Q., Hiraizumi, M., Ricci-Tam, C., Nishimasu, H., Konermann, S., & Hsu, P. D.** (2025). Megabase-scale human genome rearrangement with programmable bridge recombinases. *Science* (2025) / *bioRxiv*. [Arc Institute Release](https://arcinstitute.org/news/bridge-recombinases-human-cells) | [bioRxiv Full Text](https://www.biorxiv.org/content/10.1101/2025.05.14.653916v2.full-text)
5. **Hiraizumi, M., Athukoralage, J. S., Perry, N. T., Tsujimoto, E., Shiojiri, N., Nagahata, N., Lee, L., Sun, G., Durrant, M. G., Chandrasekaran, S. S., Konermann, S., Yamashita, K., Hsu, P. D., & Nishimasu, H.** (2026). Structural mechanism governing the directionality of bridge recombination. *Nature* (2026). [Arc Institute Release](https://arcinstitute.org/news/bridge-recombinase-excision)
6. **Patel, J. R., Swartz, S. E., Oromí-Bosch, A., et al., & Cress, B. F.** (2026). Bridge recombinase enables versatile rewriting of bacterial genomes. *bioRxiv* (2026). [bioRxiv Full Text](https://www.biorxiv.org/content/10.64898/2026.04.29.721476v2.full-text)
7. **Evolutionary origins of archaeal and eukaryotic RNA-guided RNA modification in bacterial IS110 transposons.** (2025). *Nature Microbiology*, 10(1), 20–27. [PMC11930352](https://pmc.ncbi.nlm.nih.gov/articles/PMC11930352/) | [PubMed: 39747689](https://pubmed.ncbi.nlm.nih.gov/39747689/)
8. **Guo, et al.** (2026). Optimization of IS621 recombinase/bridge RNA-directed recombination for precise insertion of large DNA fragments in human cells. *Nature Communications*, 17(1), 7234. [PubMed: 42251048](https://pubmed.ncbi.nlm.nih.gov/42251048/) | [MDPI Review](https://www.mdpi.com/2227-9059/14/9/2008)
9. **Pelea, et al.** (2026). Programmable genome editing in human cells using RNA-guided bridge recombinases. [ResearchGate](https://www.researchgate.net/publication/400507050_Programmable_genome_editing_in_human_cells_using_RNA-guided_bridge_recombinases)
10. **Sun, et al.** (2025). IS110 transposon utilizes two mechanistically distinct RNA-guided transposition pathways. *bioRxiv*. [bioRxiv Full Text](https://www.biorxiv.org/content/10.1101/2025.10.25.684509.full)
11. **A sequence–structure dual-match logic enables target recognition by an IS110 element (ISPpu10).** (2026). *bioRxiv*. [bioRxiv Full Text](https://www.biorxiv.org/content/10.64898/2026.03.19.712850v2.full-text)
12. **Canonically minimal RNA-guided insertion sequences expand into ~100 kb cargo platforms.** (2026). *bioRxiv*. [bioRxiv Full Text](https://www.biorxiv.org/content/10.64898/2026.08.14.744561v2.full-text)
13. **Systematic mapping of the prokaryotic noncoding sequence space (Evo-PIN bridge recombinase mining).** (2026). *bioRxiv*. [bioRxiv PDF](https://www.biorxiv.org/content/10.64898/2026.10.21.760802v1.full.pdf)
14. **Siguier, P., Gourbeyre, E., & Chandler, M.** (2014). Bacterial insertion sequences: their genomic impact and diversity. *FEMS Microbiology Reviews*, 38(5), 865–891. [PMC7190074](https://pmc.ncbi.nlm.nih.gov/articles/PMC7190074/)
15. **Bruton, C. J., & Chater, K. F.** (1987). Nucleotide sequence of IS110, an insertion sequence of *Streptomyces coelicolor* A3(2). *Nucleic Acids Research*, 15(17), 7053–7065. [PMC306192](https://pmc.ncbi.nlm.nih.gov/articles/PMC306192/)
