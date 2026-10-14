# Math1212 概率论与数理统计 I (Probability and Statistics I)
## 第一章：概率论基础 课程讲义全景精要与深度解析笔记

> **课程信息**：Math1212 Probability and Statistics I (Fall 2026)  
> **参考教材**：
> 1. Robert V. Hogg, Elliot A. Tanis, Dale Zimmerman, *Probability and Statistical Inference* (9th/10th ed.)
> 2. 魏宗舒 等，《概率论与数理统计教程》（第三版），高等教育出版社
> 3. Morris H. DeGroot, Mark J. Schervish, *Probability and Statistics* (4th ed.)
> 4. 陈希孺，《概率论与数理统计》（第一版），中国科学技术大学出版社

---

## 目录与知识架构

1. **课程概貌与概率统计学科全景 (Overview & Big Picture)**
2. **第一节：概率的基本概念 (1.1 Concept of Probability)**
   - 2.1 随机现象、随机试验与样本空间
   - 2.2 随机事件与集合代数
   - 2.3 集合系与 $\sigma$-代数 ($\sigma$-Algebra) 深度辨析
   - 2.4 [补充专题] 集合序列的极限 (Set Limits - Loeve 理论)
   - 2.5 频率与公理化概率定义 (Kolmogorov Axioms)
   - 2.6 概率的基本性质与定理严谨证明
   - 2.7 概率测度的连续性定理 (Continuity of Probability Measures)
   - 2.8 邦弗朗尼不等式 (Bonferroni's Inequality) 与布尔不等式
3. **第二节：古典概型与几何概型 (1.2 Classical & Geometric Probability)**
   - 3.1 古典概型与排列组合计算
   - 3.2 进阶案例分析：Tom & Jerry 抛硬币的对称性妙解
   - 3.3 几何概型（1维、2维、3维空间中的测度模型）
   - 3.4 [补充证明] 独立重复试验中互斥事件“先发生”定理
4. **第三节：条件概率 (1.3 Conditional Probability)**
   - 4.1 条件概率的公理化定义与测度性质
   - 4.2 乘法法则 (Multiplication Rule) 与链式法则
   - 4.3 综合应用案例分析
5. **第四节：事件的独立性 (1.4 Independent Events)**
   - 5.1 相互独立的数学定义与直观意义
   - 5.2 零概率事件的独立性与代数性质
   - 5.3 直觉的陷阱：家庭多孩性别分布中的独立性反转
6. **第五节：全概率公式与贝叶斯定理 (1.5 Bayes' Theorem)**
   - 6.1 样本空间的划分 (Partition)
   - 6.2 全概率公式 (Law of Total Probability)
   - 6.3 贝叶斯定理 (Bayes' Theorem) 与后验概率更新
   - 6.4 深度剖析：医学筛查中的“假阳性悖论”与基础比率谬误 (Base Rate Fallacy)
7. **第六节：伯努利试验 (1.6 Bernoulli Trials)**
   - 7.1 伯努利试验与独立试验序列
   - 7.2 二项概率模型与分布性质
   - 7.3 典型案例计算
8. **核心公式速查与易错知识点辨析 (Summary & Pitfalls)**

---

## 1. 课程概貌与概率统计学科全景 (Overview & Big Picture)

### 1.1 概率与数理统计的研究对象
- **概率与数理统计 (Probability and Statistics)**：数学的一个重要分支，专门研究==**随机现象的统计规律性== (Statistical Law of Random Phenomena)**。
- ==🔴**随机现象 (Random Phenomenon) 与随机试验 (Random Experiment)**：==
  - 在个别试验中，结果呈现出不确定性（无法在试验前准确预测）；
  - 但在相同条件下大量重复试验时，其所有可能结果呈现出固有的统计规律性。

### 1.2 概率论 (Probability) 与数理统计 (Statistics) 的对偶关系
课件第 4 页与第 5 页揭示了概率与统计两者的宏观思维闭环：

```
                【概率论 (Probability)】
          基于模型推演数据分布 (Deductive / Forward)
   ┌───────────────────────────────────────────────┐
   │                                               │
   ▼                                               │
真实随机现象 ────────── 观察/采集 (Observe) ─────────► 数据 (Data)
(Random Phenomenon)                                │
   ▲                                               │
   │                                               │
   └───────────────────────────────────────────────┘
                【数理统计 (Statistics)】
          基于观测数据反推系统模型 (Inductive / Inverse)
```

- **概率论（从模型到数据）**：假设已知随机现象背后的总体分布与物理/数学机制（例如已知骰子是均匀的），通过演绎推理研究随机变量、极限定理及各种事件发生的概率；
- **数理统计（从数据到模型）**：现实世界中总体的真实规律是未知的，我们仅能通过抽样获取有限的观测数据（Data），通过归纳推理与推断（Inference）去估计未知参数、检验科学假设并揭示底层机制。

### 1.3 现代数据科学与 AI 背景下的现实意义
课件第 7 页特别强调：在当今海量数据与人工智能时代，概率统计构成了以下关键技术的最底层数理基石：
1. **推荐算法（如短视频/电商推荐系统）**：基于用户历史交互与协同过滤，通过贝叶斯更新与概率图模型估计用户对特定内容的点击率 (CTR) 与兴趣概率分布；
2. **大语言模型 (LLMs, 如 ChatGPT)**：生成式模型的本质是对自然语言序列的联合概率分布 $P(w_1, w_2, \dots, w_n) = \prod_{i=1}^n P(w_i \mid w_1, \dots, w_{i-1})$ 进行自回归建模与采样；
3. **生物信息学与基因组学**：在人体的 30 亿个碱基对中，通过多重假设检验 (Multiple Hypothesis Testing) 筛选出与阿尔茨海默病、帕金森病显著相关的致病单核苷酸多态性 (SNP) 位点。

---

## 2. 第一节：概率的基本概念 (1.1 Concept of Probability)

### 2.1 随机现象、样本空间与样本点

#### (1) 基本定义
- **样本空间 (Sample Space, $\Omega$)**：随机试验的所有可能结果所构成的集合。
- **样本点 / 基本事件 (Element / Sample Point / Elementary Event, $\omega$)**：随机试验的每一个具体单次可能结果，满足 $\omega \in \Omega$。
- **随机事件 (Random Event, $A$)**：样本空间 $\Omega$ 的子集，记作 $A \subset \Omega$。
  - 当试验结果 $\omega \in A$ 时，称“事件 $A$ 发生”；
  - **必然事件 (Certain Event)**：<font color="#ff0000">全集 $\Omega$ </font>本身，每次试验必定发生；
  - **不可能事件 (Impossible Event)**：<font color="#ff0000">空集 $\emptyset$，</font>任何一次试验都不可能发生。

#### (2) 样本空间的分类与典型实例
1. **离散有限样本空间**：
   - 抛一枚硬币：$\Omega = \{\text{正面 (Head)}, \text{反面 (Tail)}\}$，元素个数 $|\Omega| = 2$；
   - 掷一颗六面骰子：$\Omega = \{1, 2, 3, 4, 5, 6\}$，基本事件 $\omega_i = \{i\}$。
2. **连续不可数样本空间**：
   - 在区间 $[0, 1]$ 内随机选取一个实数：$\Omega = [0, 1]$，<u>每一个实数 $\omega \in [0, 1]$ 都是一个基本事件，样本点个数不可数无穷。</u>

---

### 2.2 随机事件的集合代数与运算规则

由于事件是样本空间的子集，概率论中的事件运算完全等价于**集合论代数 (Algebra of Sets)**：

| 概率论术语              | 集合论记号                                                         | 数学定义 / 元素刻画                                                         | 实际物理含义                   |
| :----------------- | :------------------------------------------------------------ | :------------------------------------------------------------------ | :----------------------- |
| **包含 / 蕴涵**        | $A \subset B$                                                 | $\forall \omega \in A \implies \omega \in B$                        | 若事件 $A$ 发生，则事件 $B$ 必发生   |
| **事件相等**           | $A = B$                                                       | $A \subset B$ 且 $B \subset A$                                       | 事件 $A$ 与事件 $B$ 同生同灭      |
| **和事件 / 并**        | $A \cup B$                                                    | $\{\omega : \omega \in A \text{ 或 } \omega \in B\}$                 | 事件 $A$ 与事件 $B$ 至少有一个发生   |
| **积事件 / 交**        | $A \cap B$ 或 $AB$                                             | $\{\omega : \omega \in A \text{ 且 } \omega \in B\}$                 | 事件 $A$ 与事件 $B$ 同时发生      |
| ==**差事件**==        | $A \setminus B$ 或 $A - B$                                     | $\{\omega : \omega \in A \text{ 且 } \omega \notin B\} = A \cap B^c$ | ==事件 $A$ 发生且事件 $B$ 不发生== |
| **对立事件 / 补集**      | $A'$ 或 $A^c$                                                  | $\{\omega : \omega \in \Omega \setminus A\}$                        | 事件 $A$ 不发生               |
| **互斥 / exclusive** | $A \cap B = \emptyset$                                        | $AB = \emptyset$                                                    | 事件 $A$ 与事件 $B$ 不可能同时发生   |
| **完备事件群**          | $\bigcup_{i=1}^n A_i = \Omega$                                | 至少有一个 $A_i$ 发生                                                      | 试验结果必落在某个 $A_i$ 中        |
| **样本空间划分**         | $A_i \cap A_j = \emptyset (i \ne j)$ 且 $\bigcup A_i = \Omega$ | 两两互斥(exclusive)且完全覆盖(exhaustive)                                    | 每次试验有且仅有一个 $A_i$ 发生      |

#### 常用集合运算定律：
1. **交换律 (Commutative Laws)**：$A \cup B = B \cup A,\quad A \cap B = B \cap A$
2. **结合律 (Associative Laws)**：$(A \cup B) \cup C = A \cup (B \cup C),\quad (AB)C = A(BC)$
3. **分配律 (Distributive Laws)**：
   $$A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$$
   $$A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$$
4. **德摩根律 / 对偶原则 (De Morgan's Laws)**：
   $$(A \cup B)^c = A^c \cap B^c,\quad (A \cap B)^c = A^c \cup B^c$$
   推广至有限/可数无限个事件：
   $$\left( \bigcup_{i} A_i \right)^c = \bigcap_{i} A_i^c, \quad \left( \bigcap_{i} A_i \right)^c = \bigcup_{i} A_i^c$$

#### 复合事件的集合语言表述规范：
- “事件 $A_1, \dots, A_n$ 中至少有一个发生” $\iff \bigcup_{i=1}^n A_i$
- “事件 $A_1, \dots, A_n$ 全部发生” $\iff \bigcap_{i=1}^n A_i$
- “事件 $A_1, \dots, A_n$ 都不发生” $\iff \left(\bigcup_{i=1}^n A_i\right)^c = \bigcap_{i=1}^n A_i^c$
- “事件 $A_1, \dots, A_n$ 中至少有一个不发生” $\iff \left(\bigcap_{i=1}^n A_i\right)^c = \bigcup_{i=1}^n A_i^c$

---

### 2.3 集合系与 $\sigma$-代数 ($\sigma$-Algebra) 深度辨析

在现代测度论概率体系中，不能随意将样本空间 $\Omega$ 的“任意子集”都定义为事件。必须明确定义一个由子集构成的集合系（代数与 $\sigma$-代数）。

#### (1) 代数 (Algebra / Field)
设 $\Omega$ 是样本空间，$\mathcal{A}$ 是 $\Omega$ 的某些子集组成的集类。若满足：
1. $\Omega \in \mathcal{A}$；
2. 若 $A \in \mathcal{A}$，则 $A^c \in \mathcal{A}$（对补运算封闭）；
3. 若 $A, B \in \mathcal{A}$，则 $A \cup B \in \mathcal{A}$（对**有限**并运算封闭）。
则称 $\mathcal{A}$ 为 $\Omega$ 上的一个**代数 (Algebra)**。

#### (2) $\sigma$-代数 ($\sigma$-Algebra / $\sigma$-Field)
若集类 $\mathcal{F}$ 在有限并封闭的基础上，进一步对**可数无限并**运算封闭，即满足：
1. $\emptyset \in \mathcal{F}$（或等价地 $\Omega \in \mathcal{F}$）；
2. 若 $A \in \mathcal{F}$，则 $A^c \in \mathcal{F}$（对余集/补集封闭）；
3. 若序列 $A_1, A_2, \dots \in \mathcal{F}$，则可数并 $\bigcup_{i=1}^\infty A_i \in \mathcal{F}$（对**可数并**封闭）。

> **【深度补充解释 1：为什么概率论需要引入 $\sigma$-代数？】**  
> 很多初学者会疑惑：为什么不直接把 $\Omega$ 的所有子集构成的幂集 $\mathcal{P}(\Omega)$ 作为事件域？  
> - **对于离散有限或可数样本空间**（如抛硬币、掷骰子）：其幂集 $\mathcal{P}(\Omega)$ 的子集数目为有限或可数个，确实可以直接将 $\mathcal{F} = \mathcal{P}(\Omega)$ 作为 $\sigma$-代数。若 $|\Omega| = n$，则 $\mathcal{F}$ 包含 $2^n$ 个子集。
> - **对于不可数连续样本空间**（如区间 $[0, 1]$ 或实数轴 $\mathbb{R}$）：在实分析与测度论中，著名的 **Vitali 不可测集定理 (Vitali Vitali Non-measurable Set)** 和 **Banach-Tarski 悖论**证明了：在选择公理 (Axiom of Choice) 下，**不存在一个既满足平移不变性、又满足非负性与可数可加性的测度，能够赋予 $\mathbb{R}$ 的所有子集**！也就是说，存在一些“极其病态”的病态子集，根本无法合理定义其“长度”或“概率”。  
> 因此，数学家必须退而求其次，划定一个足够大、在可数集合运算下封闭、且每个集合都能严谨测量概率的良态子集类——这便是 $\sigma$-代数。在实数轴 $\mathbb{R}$ 上，由所有区间 $[a, b], (a, b), [a, b), (a, b]$ 生成的最小 $\sigma$-代数称为 **Borel $\sigma$-代数**，记作 $\mathcal{B}(\mathbb{R})$。

#### (3) 两个极端的 $\sigma$-代数
1. **平凡 $\sigma$-代数 (Trivial $\sigma$-algebra)**：$\mathcal{F} = \{\emptyset, \Omega\}$。这是最小的 $\sigma$-代数，完全不包含任何细节信息；
2. **全子集幂集 (Power Set)**：$\mathcal{F} = 2^\Omega = \mathcal{P}(\Omega)$。这是最大的 $\sigma$-代数。

---

### 2.4 [补充专题] 集合序列的极限 (Set Limits - Loeve 理论)

课件第 44~47 页专门引入了著名概率论家 M. Loeve 的集合序列极限定理，这是概率论收敛性证明的核心工具：

设集合序列 $\{A_n\}_{n \ge 1}$，其中每个 $A_n \subset \Omega$。

#### (1) 下极限 (Inferior Limit / $\liminf$)
$$\liminf_{n \to \infty} A_n = \bigcup_{n=1}^\infty \bigcap_{k=n}^\infty A_k$$
- **元素特征刻画**：$\omega \in \liminf A_n \iff \omega$ 属于**除有限个之外的几乎所有 $A_n$** (belongs to all but finitely many $A_n$)。
- **物理含义**：从某一项 $N$ 开始，事件 $A_n$ 恒发生。

#### (2) 上极限 (Superior Limit / $\limsup$)
$$\limsup_{n \to \infty} A_n = \bigcap_{n=1}^\infty \bigcup_{k=n}^\infty A_k$$
- **元素特征刻画**：$\omega \in \limsup A_n \iff \omega$ 属于**无限多个 $A_n$** (belongs to infinitely many $A_n$)。
- **物理含义**：事件 $A_n$ 发生无穷多次（经常记为 $A_n \text{ i.o.}$，即 infinitely often）。

#### (3) 包含关系与极限存在性
- **基本包含关系**：
  $$\liminf_{n \to \infty} A_n \subset \limsup_{n \to \infty} A_n$$
  *解释*：如果一个点属于几乎所有集合，则它必然属于无限多个集合。
- **极限存在的充要条件**：
  若 $\liminf_{n \to \infty} A_n = \limsup_{n \to \infty} A_n = A$，则称集合序列 $\{A_n\}$ **收敛于极限集 $A$**，记作 $\lim_{n \to \infty} A_n = A$。

#### (4) 单调集合序列的收敛性定理
单调集合序列构成了一类必然收敛的基本集合系：
1. **单调递增序列 (Non-decreasing, $A_n \uparrow$)**：$A_n \subset A_{n+1}, \forall n$。其极限必然存在且等于其可数并：
   $$\lim_{n \to \infty} A_n = \bigcup_{n=1}^\infty A_n$$
2. **单调递减序列 (Non-increasing, $A_n \downarrow$)**：$A_{n+1} \subset A_n, \forall n$。其极限必然存在且等于其可数交：
   $$\lim_{n \to \infty} A_n = \bigcap_{n=1}^\infty A_n$$

---

### 2.5 频率与公理化概率定义 (Kolmogorov Axioms)

#### (1) 相对频率 (Relative Frequency)
在 $n$ 次重复试验中，事件 $A$ 发生的频数记为 $N(A)$，其相对频率为：
$$f_n(A) = \frac{N(A)}{n}$$
相对频率满足以下直观性质：
1. **非负性**：$f_n(A) \ge 0$；
2. **规范性**：$f_n(\Omega) = \frac{n}{n} = 1$；
3. **有限可加性**：若 $A \cap B = \emptyset$，则 $f_n(A \cup B) = f_n(A) + f_n(B)$。

#### (2) 概率的公理化定义 (Колмогоров, 1933)
柯尔莫哥洛夫摆脱了历史上古典概型“循环定义”与几何概型“贝特朗悖论”的泥潭，基于测度论建立了概率公理体系：

**定义**：设 $\Omega$ 是样本空间，$\mathcal{F}$ 是 $\Omega$ 的一个 $\sigma$-代数。若映射 $P: \mathcal{F} \to [0, 1]$ 满足以下三条公理：
- **公理 1（非负性, Non-negativity）**：$\forall A \in \mathcal{F},\quad P(A) \ge 0$；
- **公理 2（规范性, Normed Property）**：$P(\Omega) = 1$；
- **公理 3（可数可加性 / $\sigma$-可加性, Countable Additivity）**：若事件序列 $A_1, A_2, \dots \in \mathcal{F}$ 两两互斥（即 $A_i \cap A_j = \emptyset, \forall i \ne j$），则：
  $$P\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty P(A_i)$$

称 $P$ 为定义在 $(\Omega, \mathcal{F})$ 上的**概率测度 (Probability Measure)**，二元组 $(\mathcal{F}, P)$ 称为**概率域 (Probability Field)**，三元组 $(\Omega, \mathcal{F}, P)$ 称为**概率空间 (Probability Space)**。

---

### 2.6 概率的基本性质与定理证明

从三条公理出发，可以推导出一系列重要的性质定理（课件第 53~65 页）：

#### 定理 1.1.1（对立事件概率）
对于任意事件 $A \in \mathcal{F}$，有：
$$P(A) = 1 - P(A^c)$$
*证明*：因为 $A \cup A^c = \Omega$ 且 $A \cap A^c = \emptyset$。根据可加性与规范性：
$$P(A) + P(A^c) = P(A \cup A^c) = P(\Omega) = 1 \implies P(A) = 1 - P(A^c) \quad \blacksquare$$

#### 定理 1.1.2（不可能事件概率为 0）
$$P(\emptyset) = 0$$
*证明*：在定理 1.1.1 中取 $A = \emptyset$，则 $A^c = \Omega$，得 $P(\emptyset) = 1 - P(\Omega) = 1 - 1 = 0$。 $\blacksquare$

> **【重要辨析】**：“$P(A) = 0$” 与 “$A = \emptyset$” 并不等价！在连续型样本空间中，单点集的概率往往为 0，但单点集并非空集。

#### 定理 1.1.3（单调性定理）
若 $A, B \in \mathcal{F}$ 且 $A \subset B$，则：
$$P(A) \le P(B), \quad \text{且 } P(B \setminus A) = P(B) - P(A)$$
*证明*：将 $B$ 分解为两两互斥的部分：$B = A \cup (B \cap A^c) = A \cup (B \setminus A)$。因为 $A \cap (B \setminus A) = \emptyset$，由可加性公理：
$$P(B) = P(A) + P(B \setminus A)$$
由非负性公理，$P(B \setminus A) \ge 0$，因此 $P(B) \ge P(A)$。 $\blacksquare$

#### 定理 1.1.4（概率的有界性）
对于任意事件 $A \in \mathcal{F}$，均有：
$$0 \le P(A) \le 1$$
*证明*：由公理 1 可知 $P(A) \ge 0$。由 $A \subset \Omega$ 及定理 1.1.3 单调性可知 $P(A) \le P(\Omega) = 1$。 $\blacksquare$

#### 定理 1.1.5（两事件加法公式 / 容斥原理）
对任意两个事件 $A, B \in \mathcal{F}$：
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
*证明*：将 $A \cup B$ 与 $B$ 分解为不相交并集：
$$A \cup B = A \cup (A^c \cap B), \quad \text{其中 } A \cap (A^c \cap B) = \emptyset$$
$$B = (A \cap B) \cup (A^c \cap B), \quad \text{其中 } (A \cap B) \cap (A^c \cap B) = \emptyset$$
由可加性：
$$P(A \cup B) = P(A) + P(A^c \cap B)$$
$$P(B) = P(A \cap B) + P(A^c \cap B) \implies P(A^c \cap B) = P(B) - P(A \cap B)$$
代入前式即得：
$$P(A \cup B) = P(A) + P(B) - P(A \cap B) \quad \blacksquare$$

#### 定理 1.1.6（三事件加法公式）
对任意三个事件 $A, B, C \in \mathcal{F}$：
$$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(AB) - P(AC) - P(BC) + P(ABC)$$
*证明思路*：将 $B \cup C$ 视为一个整体事件 $D$，应用定理 1.1.5 展开 $P(A \cup D)$，并利用集合分配律 $A \cap (B \cup C) = (AB) \cup (AC)$ 再次应用加法定理展开即可。

---

### 2.7 概率测度的连续性定理 (Continuity of Probability Measures)

课件第 66~73 页给出了概率测度的连续性定理及其极具数学美感的不相交化证明：

#### 定理 1.1.7（概率测度的连续性）
设序列 $\{A_i\}_{i \ge 1} \subset \mathcal{F}$，则：
$$P\left(\bigcup_{i=1}^\infty A_i\right) = \lim_{m \to \infty} P\left(\bigcup_{i=1}^m A_i\right)$$
对交集利用德摩根律亦有：
$$P\left(\bigcap_{i=1}^\infty A_i\right) = \lim_{m \to \infty} P\left(\bigcap_{i=1}^m A_i\right)$$

#### 核心证明技术：不相交化构造法 (Disjointification)
*严谨证明*：
1. **构造两两不交的新事件列 $\{B_n\}$**：
   令：
   $$B_1 = A_1$$
   $$B_2 = A_2 \setminus A_1$$
   $$\dots$$
   $$B_n = A_n \setminus \left(\bigcup_{i=1}^{n-1} A_i\right) = A_n \cap \left(\bigcup_{i=1}^{n-1} A_i\right)^c$$
2. **验证性质**：
   - **性质 1**：$B_i \cap B_j = \emptyset, \forall i \ne j$（两两互斥）；
   - **性质 2**：对任意有限正整数 $m$，$\bigcup_{i=1}^m B_i = \bigcup_{i=1}^m A_i$；
   - **性质 3**：无穷并相等，$\bigcup_{i=1}^\infty B_i = \bigcup_{i=1}^\infty A_i$。
3. **结合级数定义与公理 3**：
   $$P\left(\bigcup_{i=1}^\infty A_i\right) = P\left(\bigcup_{i=1}^\infty B_i\right) = \sum_{i=1}^\infty P(B_i) \quad (\text{由可数可加性})$$
   根据无穷级数收敛的本质定义，无穷级数的和就是其部分和序列的极限：
   $$\sum_{i=1}^\infty P(B_i) = \lim_{m \to \infty} \sum_{i=1}^m P(B_i)$$
   又因有限个 $B_i$ 互斥：
   $$\sum_{i=1}^m P(B_i) = P\left(\bigcup_{i=1}^m B_i\right) = P\left(\bigcup_{i=1}^m A_i\right)$$
   故：
   $$P\left(\bigcup_{i=1}^\infty A_i\right) = \lim_{m \to \infty} P\left(\bigcup_{i=1}^m A_i\right) \quad \blacksquare$$

#### 推论 1.1.8 & 1.1.9（单调列的连续性）
- **单调增列上连续性**：若 $A_n \uparrow A$（即 $A_1 \subset A_2 \subset \dots$ 且 $A = \bigcup_{n=1}^\infty A_n$），则：
  $$P(A) = \lim_{n \to \infty} P(A_n)$$
- **单调减列下连续性**：若 $A_n \downarrow A$（即 $A_1 \supset A_2 \supset \dots$ 且 $A = \bigcap_{n=1}^\infty A_n$），则：
  $$P(A) = \lim_{n \to \infty} P(A_n)$$

> **【深度数学洞见】**：在现代测度论中，**可数可加性 (Countable Additivity)** 等价于 **有限可加性 (Finite Additivity) + 测度的单调连续性 (Continuity)**。定理 1.1.7 保证了极限运算与概率计算可以自由交换顺序，即 $\lim P(A_n) = P(\lim A_n)$。

---

### 2.8 邦弗朗尼不等式 (Bonferroni's Inequality) 与布尔不等式

在复杂联合事件中，直接计算交集或并集的概率通常非常困难。邦弗朗尼不等式提供了极具实用价值的上下界估计。

#### (1) 定理表述
设 $A_1, A_2, \dots, A_n \in \mathcal{F}$，则：
1. **布尔不等式 (Boole's Inequality / 并集上界 / Union Bound)**：
   $$P\left(\bigcup_{i=1}^n A_i\right) \le \sum_{i=1}^n P(A_i)$$
2. **邦弗朗尼不等式 (Bonferroni's Inequality / 交集下界)**：
   $$P\left(\bigcap_{i=1}^n A_i\right) \ge 1 - \sum_{i=1}^n P(A_i^c) = \sum_{i=1}^n P(A_i) - (n - 1)$$
   上述两个不等式对 $n \to \infty$ 可数无穷情形同样成立。

#### (2) 严谨证明
1. 证明布尔不等式：利用不相交化序列 $B_i \subset A_i$：
   $$P\left(\bigcup_{i=1}^n A_i\right) = P\left(\bigcup_{i=1}^n B_i\right) = \sum_{i=1}^n P(B_i) \le \sum_{i=1}^n P(A_i) \quad (\text{因 } B_i \subset A_i \implies P(B_i) \le P(A_i))$$
2. 证明邦弗朗尼不等式：对交集的对立事件应用德摩根律与布尔不等式：
   $$P\left(\bigcap_{i=1}^n A_i\right) = 1 - P\left(\left(\bigcap_{i=1}^n A_i\right)^c\right) = 1 - P\left(\bigcup_{i=1}^n A_i^c\right)$$
   由布尔不等式，$P\left(\bigcup_{i=1}^n A_i^c\right) \le \sum_{i=1}^n P(A_i^c)$，代入得：
   $$P\left(\bigcap_{i=1}^n A_i\right) \ge 1 - \sum_{i=1}^n P(A_i^c)$$
   因为 $P(A_i^c) = 1 - P(A_i)$，所以：
   $$1 - \sum_{i=1}^n [1 - P(A_i)] = 1 - [n - \sum_{i=1}^n P(A_i)] = \sum_{i=1}^n P(A_i) - (n - 1) \quad \blacksquare$$

#### (3) 实际应用与局限性分析（课件第 77 页）
- **高概率事件的有效下界**：  
  设 $P(A) = 0.95, P(B) = 0.95$。两者同时发生的概率下界为：
  $$P(A \cap B) \ge 0.95 + 0.95 - 1 = 0.90$$
  即使完全不知道 $A$ 与 $B$ 的相关性结构，也能保证其交集概率至少为 $90\%$。
- **局限性（失效边界）**：  
  若单个事件的概率不够大，例如 $P(A) = 0.4, P(B) = 0.4$，则：
  $$P(A \cap B) \ge 0.4 + 0.4 - 1 = -0.2$$
  由于任何事件概率平凡地大于等于 0，负数下界虽然在数学上完全正确，但**没有任何信息量 (Useless though correct)**。
- **统计学拓展**：在多重假设检验中，著名的 **Bonferroni 校正 (Bonferroni Correction)** 即基于此原理，控制总体第一类错误率 (Family-Wise Error Rate, FWER)。

---

## 3. 第二节：古典概型与几何概型 (1.2 Classical & Geometric Probability)

### 3.1 古典概型 (Classical Probability)

#### (1) 基本特征
随机试验必须满足两个苛刻的前提条件：
1. **有限性**：样本空间 $\Omega$ 包含有限个基本事件，即 $|\Omega| < \infty$；
2. **等可能性**：每个基本事件出现的可能性均等（物理上的对称性，如均匀骰子、完全洗匀的纸牌）。

#### (2) 计算公式
设事件 $A$ 包含 $|A|$ 个基本事件，则古典概率为：
$$P(A) = \frac{|A|}{|\Omega|} = \frac{A \text{ 包含的基本事件数}}{\Omega \text{ 包含的总基本事件数}}$$

#### (3) 常用计数原理：笛卡尔积与乘法法则 (Multiplication Rule)
若两个有限集合 $A, B$，其笛卡尔积为 $A \times B = \{(a, b): a \in A, b \in B\}$，则元素个数满足：
$$|A \times B| = |A| \times |B|$$
推广至 $k$ 步试验序列，总结果数为 $|\Omega_1 \times \dots \times \Omega_k| = \prod_{i=1}^k |\Omega_i|$。

#### (4) 经典例题回顾
- **例 1.2.1（52 张扑克牌抽一张）**：$|\Omega| = 52$。抽到一张老 K (King) 的概率为 $P(A) = \frac{4}{52} = \frac{1}{13}$。
- **例 1.2.2（掷两颗均匀六面骰子）**：$|\Omega| = 6 \times 6 = 36$。
  - 掷出两个 6：$A = \{(6,6)\}$，$P(A) = 1/36$；
  - 掷出一个 6 和一个 4：$A = \{(4,6), (6,4)\}$，$P(A) = 2/36 = 1/18$；
  - 掷出两个相同点数：$A = \{(1,1), \dots, (6,6)\}$，$P(A) = 6/36 = 1/6$。

---

### 3.2 进阶案例分析：Tom & Jerry 抛硬币的对称性妙解

课件第 85~87 页展示了一个极其优美且体现深厚数学直觉的题目（例 1.2.3）：

#### 问题描述
Tom 和 Jerry 抛一枚均匀硬币。Tom 抛 $n + 1$ 次，Jerry 抛 $n$ 次。求 **Tom 获得的正面次数多于 Jerry 获得正面次数的概率**。

#### 深度解析：暴力代数法 vs 巧妙对称性法

##### 方法一：代数求和法（繁琐复杂）
设 Tom 掷出 $X$ 个正面，$X \sim \text{Binomial}(n+1, 0.5)$；Jerry 掷出 $Y$ 个正面，$Y \sim \text{Binomial}(n, 0.5)$。
由于试验独立，需要计算双重组合数求和：
$$P(X > Y) = \sum_{k=0}^n P(Y = k) P(X > k) = \sum_{k=0}^n \binom{n}{k} \left(\frac{1}{2}\right)^n \sum_{j=k+1}^{n+1} \binom{n+1}{j} \left(\frac{1}{2}\right)^{n+1}$$
该式化简极其耗时且容易出错。

##### 方法二：对称性分析法（课件推荐解法，优雅严谨）
设 Tom 掷出的正面数为 $H_T$，反面数为 $T_T$；Jerry 掷出的正面数为 $H_J$，反面数为 $T_J$。
注意试验的总约束：
$$H_T + T_T = n + 1, \quad H_J + T_J = n$$
将两个方程相减：
$$(H_T - H_J) + (T_T - T_J) = (n + 1) - n = 1$$
这一等式是整个解题的题眼！它表明：
$$(H_T - H_J) + (T_T - T_J) = 1$$
由于硬币只有正面和反面，这两个差值都是整数。因此：
- 若 $H_T > H_J$（即 $H_T - H_J \ge 1$），则必然有 $T_T - T_J = 1 - (H_T - H_J) \le 0$，即 $T_T \le T_J$（Tom 的反面数不大于 Jerry 的反面数）；
- 若 $H_T \le H_J$（即 $H_T - H_J \le 0$），则必然有 $T_T - T_J = 1 - (H_T - H_J) \ge 1$，即 $T_T > T_J$（Tom 的反面数严格多于 Jerry 的反面数）。

由于两者的并集构成了整个样本空间 $\Omega$，且两者互斥，因此：
$$\{H_T > H_J\} = \{T_T \le T_J\}^c = \{T_T > T_J\}$$
又因为硬币是完全对称且均匀的（抛正面与抛反面的概率严格相同），所以“Tom 的正面数多于 Jerry”与“Tom 的反面数多于 Jerry”这两个事件的发生概率必然完全相同：
$$P(H_T > H_J) = P(T_T > T_J)$$
而这两个事件不仅互斥，而且其并集恰好是整个样本空间 $\Omega$：
$$\{H_T > H_J\} \cup \{T_T > T_J\} = \Omega, \quad \{H_T > H_J\} \cap \{T_T > T_J\} = \emptyset$$
由规范性与可加性：
$$P(H_T > H_J) + P(T_T > T_J) = 1$$
$$2 P(H_T > H_J) = 1 \implies P(H_T > H_J) = \frac{1}{2}$$
无论 $n$ 取得多大（$n=10, 100, 10^{10}$），Tom 正面数多于 Jerry 的概率**恒等于 $1/2$**！

---

### 3.3 几何概型 (Geometric Probability)

#### (1) 基本特征
当样本空间包含**不可数无限多个基本事件**，但仍然满足“等可能性”假设时，古典概型推广为几何概型：
1. **无限性**：样本空间 $\Omega$ 对应欧氏空间 $\mathbb{R}^k$ 中的某个几何区域（长度、面积或体积有限且大于 0）；
2. **等可能性**：试验中点落在某个子区域 $A$ 的可能性大小只与该子区域的几何测度（长度/面积/体积）成正比，而与位置和形状无关。

#### (2) 计算公式
$$P(A) = \frac{S_A}{S_\Omega} = \frac{\text{区域 } A \text{ 的测度 (Measure)}}{\text{样本空间 } \Omega \text{ 的测度}}$$
- 1 维空间：测度为长度 (Length)；
- 2 维空间：测度为面积 (Area)；
- 3 维空间：测度为体积 (Volume)。

#### (3) 经典维度案例解析
- **1维案例（例 1.2.4）**：在 $[0, 1]$ 上随机取数，落入 $[0, 1/3]$ 的概率：
  $$P(A) = \frac{1/3 - 0}{1 - 0} = \frac{1}{3}$$
- **2维案例（例 1.2.5）**：在矩形区域 $[0, 2] \times [0, 3]$ 内随机选点，求落入以 $(1, 1)$ 为圆心的单位圆（半径 $r=1$）内的概率：
  - 样本空间面积：$S_\Omega = 2 \times 3 = 6$；
  - 单位圆完全内切在矩形下方（圆在 $x \in [0, 2], y \in [0, 2]$ 内），面积：$S_A = \pi r^2 = \pi$；
  - 概率：$P(A) = \frac{S_A}{S_\Omega} = \frac{\pi}{6}$。
- **3维案例（例 1.2.6）**：在立方体 $[0, 4]^3$ 中随机取点，落入子立方体 $[2, 4]^3$ 的概率：
  - $S_\Omega = 4^3 = 64$，$S_A = (4 - 2)^3 = 2^3 = 8$；
  - 概率：$P(A) = \frac{8}{64} = \frac{1}{8}$。
- **3维条件几何概率（例 1.2.6 续）**：
  已知点落入立方体 $A = [2, 4] \times [2, 4] \times [2, 4]$，求该点落入长方体 $B = [1, 4] \times [1, 4] \times [0, 3]$ 的条件概率 $P(B \mid A)$：
  - 交集区域 $B \cap A$：
    $x \in [2, 4] \cap [1, 4] = [2, 4]$（长为 2）；
    $y \in [2, 4] \cap [1, 4] = [2, 4]$（宽为 2）；
    $z \in [2, 4] \cap [0, 3] = [2, 3]$（高为 1）；
  - 测度比值计算：
    $$S_{B \cap A} = 2 \times 2 \times 1 = 4, \quad S_A = 2 \times 2 \times 2 = 8$$
    $$P(B \mid A) = \frac{S_{B \cap A}}{S_A} = \frac{4}{8} = \frac{1}{2}$$

---

### 3.4 [补充证明] 独立重复试验中互斥事件“先发生”定理

课件第 99 页给出了一个极高频的经典理论问题：

#### 定理表述
设 $\Omega$ 是单次试验的样本空间，独立无限次重复该试验。设 $A, B$ 是单次试验中的两个互斥事件（$A \cap B = \emptyset$），且 $P(A \cup B) > 0$。  
证明：**在试验序列中，事件 $A$ 比事件 $B$ 先发生的概率等于条件概率 $P(A \mid A \cup B)$**，即：
$$P(A \text{ happens earlier than } B) = \frac{P(A)}{P(A \cup B)} = P(A \mid A \cup B)$$

#### 严谨数学证明
1. **事件定义**：
   - 令 $C = \Omega \setminus (A \cup B)$ 为“单次试验中 $A$ 和 $B$ 均未发生”的事件。由加法定理与互斥性，其概率为 $P(C) = 1 - P(A \cup B) = 1 - P(A) - P(B)$；
   - 设 $D$ 为事件“$A$ 比 $B$ 先发生”；
   - 设 $D_j$ 为事件“在前 $j-1$ 次试验中，$A$ 和 $B$ 均未发生，而在第 $j$ 次试验中事件 $A$ 首次发生”，$j = 1, 2, \dots$。
2. **互斥分解与级数展开**：
   显然事件列 $\{D_j\}_{j \ge 1}$ 两两互斥，且 $D = \bigcup_{j=1}^\infty D_j$。  
   由于每次试验相互独立，根据独立性乘法法则：
   $$P(D_j) = [P(C)]^{j-1} P(A)$$
3. **几何级数（等比数列求和）**：
   $$P(D) = \sum_{j=1}^\infty P(D_j) = \sum_{j=1}^\infty [P(C)]^{j-1} P(A) = P(A) \sum_{k=0}^\infty [P(C)]^k$$
   因为 $P(A \cup B) > 0$，所以公比 $P(C) = 1 - P(A \cup B) < 1$。应用无穷等比级数求和公式 $\sum_{k=0}^\infty q^k = \frac{1}{1 - q}$：
   $$P(D) = P(A) \cdot \frac{1}{1 - P(C)} = \frac{P(A)}{1 - [1 - P(A \cup B)]} = \frac{P(A)}{P(A \cup B)}$$
   又因 $A \cap B = \emptyset \implies A \cap (A \cup B) = A$，故：
   $$\frac{P(A)}{P(A \cup B)} = \frac{P(A \cap (A \cup B))}{P(A \cup B)} = P(A \mid A \cup B) \quad \blacksquare$$

> **【直观物理诠释】**：  
> 每次试验中，如果出现既非 $A$ 也非 $B$ 的结果（事件 $C$），这一轮试验对“决出胜负”毫无贡献，相当于“平局并重新开局”。由于试验无记忆性，比赛直到出现 $A$ 或 $B$ 为止才宣告结束。因此，在最终决出胜负的那一次试验中，发生 $A$ 的概率就是只在有效结果集合 $A \cup B$ 中 $A$ 所占的比重！

---

## 4. 第三节：条件概率 (1.3 Conditional Probability)

### 4.1 条件概率的定义与测度性质

#### (1) 定义
设 $A, B$ 是概率空间 $(\Omega, \mathcal{F}, P)$ 中的两个事件，且 $P(B) > 0$。称：
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$
为在“事件 $B$ 已经发生”的条件下，事件 $A$ 发生的**条件概率 (Conditional Probability)**。

#### (2) 条件概率本身是一个合法的概率测度
很多学生误以为条件概率只是一个普通比例，但定理表明：**固定条件事件 $B$（$P(B)>0$），映射 $P(\cdot \mid B): \mathcal{F} \to [0, 1]$ 严格满足柯尔莫哥洛夫的三条公理**：
1. **非负性**：因为 $P(AB) \ge 0, P(B) > 0$，故 $P(A \mid B) = \frac{P(AB)}{P(B)} \ge 0$；
2. **规范性**：
   $$P(\Omega \mid B) = \frac{P(\Omega \cap B)}{P(B)} = \frac{P(B)}{P(B)} = 1, \quad P(B \mid B) = \frac{P(B \cap B)}{P(B)} = 1$$
3. **可数可加性**：若 $A_1, A_2, \dots$ 两两互斥，则 $(A_i \cap B)$ 亦两两互斥：
   $$P\left(\bigcup_{i=1}^\infty A_i \;\Big|\; B\right) = \frac{P\left((\bigcup A_i) \cap B\right)}{P(B)} = \frac{P\left(\bigcup (A_i \cap B)\right)}{P(B)} = \frac{\sum_{i=1}^\infty P(A_i \cap B)}{P(B)} = \sum_{i=1}^\infty P(A_i \mid B)$$

> **【核心结论】**：所有对普通概率测度 $P(\cdot)$ 成立的定理与性质（如对立事件公式、加法公式、单调性、容斥原理等），在条件概率 $P(\cdot \mid B)$ 下**无一例外全部成立**！

---

### 4.2 概率乘法法则 (Multiplication Rule) 与链式法则

由条件概率定义可直接导出计算交集概率的乘法公式：
- 对两个事件：
  $$P(A \cap B) = P(B) P(A \mid B) = P(A) P(B \mid A) \quad (\text{当 } P(B)>0 \text{ 或 } P(A)>0)$$
- **链式法则 (Chain Rule)** 推广至 $n$ 个事件：
  若 $P(A_1 A_2 \dots A_{n-1}) > 0$，则：
  $$P(A_1 A_2 A_3 \dots A_n) = P(A_1) P(A_2 \mid A_1) P(A_3 \mid A_1 A_2) \dots P(A_n \mid A_1 A_2 \dots A_{n-1})$$

---

### 4.3 综合应用案例解析

#### 案例 1：四面体骰子掷出 3 先于 5（例 1.3.1）
掷一对均匀的四面体骰子（点数为 1, 2, 3, 4），点数和记为 $S$。
- 样本空间总数：$4 \times 4 = 16$；
- 事件 $A$：点数和为 3，可能结果为 $(1,2), (2,1)$，共 2 种；$P(A) = 2/16 = 1/8$；
- 事件 $C$：点数和为 5，可能结果为 $(1,4), (2,3), (3,2), (4,1)$，共 4 种；$P(C) = 4/16 = 1/4$；
- 事件 $B$：点数和为 3 或 5，由于互斥，$P(B) = P(A) + P(C) = 2/16 + 4/16 = 6/16 = 3/8$。
在序列投掷中，点数和 3 先于 5 出现的概率根据前述定理：
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{P(A)}{P(B)} = \frac{2/16}{6/16} = \frac{1}{3}$$

#### 案例 2：多险种保单续保概率（例 1.3.2）
- 投保人群划分：
  - $A_1$：仅汽车险，$P(A_1) = 0.3$，续保条件概率 $P(B \mid A_1) = 0.6$；
  - $A_2$：仅房屋险，$P(A_2) = 0.2$，续保条件概率 $P(B \mid A_2) = 0.7$；
  - $A_3$：同时有汽车和房屋险，$P(A_3) = 0.2$，续保条件概率 $P(B \mid A_3) = 0.8$；
- 已知某人随机选自持有上述保险之一的客户，求其至少续保一份保单的概率 $P(B \mid A_1 \cup A_2 \cup A_3)$：
  - 分母：$P(A_1 \cup A_2 \cup A_3) = 0.3 + 0.2 + 0.2 = 0.7$；
  - 分子：$P(B \cap (A_1 \cup A_2 \cup A_3)) = \sum_{i=1}^3 P(A_i) P(B \mid A_i) = 0.3(0.6) + 0.2(0.7) + 0.2(0.8) = 0.18 + 0.14 + 0.16 = 0.48$；
  - 条件概率：
    $$P(B \mid A_1 \cup A_2 \cup A_3) = \frac{0.48}{0.7} = \frac{48}{70} \approx 0.686$$

---

## 5. 第四节：事件的独立性 (1.4 Independent Events)

### 5.1 相互独立的数学定义与直观意义

#### (1) 直观含义
若事件 $A$ 的发生对事件 $B$ 发生的概率没有任何影响，反之亦然，即信息量不改变先验判断：
$$P(B \mid A) = P(B) \quad \text{或} \quad P(A \mid B) = P(A)$$

#### (2) 严格公理化定义
上述条件概率形式必须要求 $P(A) > 0$ 或 $P(B) > 0$。为了消除条件为 0 的病态限制，数学上采用积事件形式作为统一定义：

**定义 4.1**：称事件 $A$ 与事件 $B$ **相互独立 (Independent)**，当且仅当：
$$P(A \cap B) = P(A) P(B)$$
若该等式不成立，则称事件 $A$ 与 $B$ 为**相依事件 / 相关事件 (Dependent Events)**。

---

### 5.2 零概率事件的独立性与重要代数定理

#### (1) 零概率事件的独立性
若 $P(A) = 0$，因为 $A \cap B \subset A$，由单调性与非负性得 $0 \le P(A \cap B) \le P(A) = 0$，即 $P(A \cap B) = 0$。  
同时 $P(A) P(B) = 0 \times P(B) = 0$。  
因此恒有 $P(A \cap B) = P(A) P(B)$。  
**结论**：**概率为 0（或概率为 1）的事件与样本空间中的任意事件相互独立**。

#### (2) 对立事件的独立性传递定理
若事件 $A$ 与 $B$ 独立，则下列事件对也必然相互独立：
1. $A$ 与 $B^c$
2. $A^c$ 与 $B$
3. $A^c$ 与 $B^c$

*简要证明 $A$ 与 $B^c$ 独立*：
因为 $A = (A \cap B) \cup (A \cap B^c)$ 且两部分互斥，故：
$$P(A) = P(AB) + P(AB^c) = P(A)P(B) + P(AB^c)$$
$$P(AB^c) = P(A) - P(A)P(B) = P(A)[1 - P(B)] = P(A)P(B^c) \quad \blacksquare$$

---

### 5.3 直觉的陷阱：家庭多孩性别分布中的独立性反转

课件第 118~120 页设计了一个极为震撼的经典反直觉案例（例 1.4.4），深刻展示了“纯凭直觉判断独立性是多么危险”：

#### 问题设置
假设生男孩与生女孩的概率各为 $1/2$ 且各胎性别独立。定义两个事件：
- 事件 $A$：该家庭**既有男孩又有女孩** (Both boys and girls)；
- 事件 $B$：该家庭**至多有一个女孩** (At most one girl)。
考察在以下两种情况下，$A$ 与 $B$ 是否独立？
- **场景 1**：家庭总共有 **2 个孩子**；
- **场景 2**：家庭总共有 **3 个孩子**。

#### (1) 场景 1：家庭有 2 个孩子
- 样本空间：$\Omega = \{(B,B), (B,G), (G,B), (G,G)\}$，$|\Omega| = 4$，每个样本点概率 $1/4$。
- 事件 $A = \{(B,G), (G,B)\}$，包含 2 个元素：
  $$P(A) = \frac{2}{4} = \frac{1}{2}$$
- 事件 $B = \{(B,B), (B,G), (G,B)\}$（女孩数为 0 或 1），包含 3 个元素：
  $$P(B) = \frac{3}{4}$$
- 乘积：$P(A) P(B) = \frac{1}{2} \times \frac{3}{4} = \frac{3}{8}$。
- 交集事件 $A \cap B = \{(B,G), (G,B)\}$，包含 2 个元素：
  $$P(A \cap B) = \frac{2}{4} = \frac{1}{2}$$
- 结论：
  $$P(A \cap B) = \frac{1}{2} \ne \frac{3}{8} = P(A) P(B)$$
  **事件 $A$ 与 $B$ 不独立（显著相依）**！

#### (2) 场景 2：家庭有 3 个孩子
- 样本空间：$|\Omega| = 2^3 = 8$：
  $$\Omega = \{(B,B,B), (B,B,G), (B,G,B), (G,B,B), (B,G,G), (G,B,G), (G,G,B), (G,G,G)\}$$
- 事件 $A$：既有男又有女，排除全男 $(B,B,B)$ 和全女 $(G,G,G)$，共 6 个元素：
  $$P(A) = \frac{6}{8} = \frac{3}{4}$$
- 事件 $B$：至多一个女孩（0个女孩或1个女孩）：
  - 0个女孩：$(B,B,B)$（1种）
  - 1个女孩：$(B,B,G), (B,G,B), (G,B,B)$（3种）
  共 4 个元素：
  $$P(B) = \frac{4}{8} = \frac{1}{2}$$
- 乘积：$P(A) P(B) = \frac{3}{4} \times \frac{1}{2} = \frac{3}{8}$。
- 交集事件 $A \cap B$：既有男又有女，且至多一个女孩 $\iff$ 恰好有 1 个女孩：
  $$A \cap B = \{(B,B,G), (B,G,B), (G,B,B)\}$$
  共 3 个元素：
  $$P(A \cap B) = \frac{3}{8}$$
- 结论：
  $$P(A \cap B) = \frac{3}{8} = P(A) P(B)$$
  **事件 $A$ 与 $B$ 竟然严格统计独立 (Statistically Independent)**！

> **【深度思维启示】**：  
> 人类直觉往往认为，“既有男又有女”与“女孩数量”天然存在因果牵连，在两孩时确实相依。然而，当孩子数量增加到 3 时，概率测度在对称样本点之间的重新分配恰好使得边缘概率的乘积与交集概率严格吻合。这证明了**统计独立性是一个纯粹的代数与测度性质，绝不能单凭因果直觉妄下断言**！

---

## 6. 第五节：全概率公式与贝叶斯定理 (1.5 Bayes' Theorem)

### 6.1 样本空间的划分 (Partition)

设 $\Omega$ 为试验的样本空间。若事件组 $A_1, A_2, \dots, A_n$ 满足：
1. **两两互斥**：$A_i \cap A_j = \emptyset, \forall i \ne j$；
2. **完全穷尽**：$\bigcup_{i=1}^n A_i = \Omega$；
3. **正测度**：$P(A_i) > 0, \forall i = 1, \dots, n$。
则称 $A_1, A_2, \dots, A_n$ 为样本空间 $\Omega$ 的一个**划分 (Partition)** 或**完备事件群**。

---

### 6.2 全概率公式 (Law of Total Probability)

#### (1) 定理表述
设 $A_1, \dots, A_n$ 是样本空间 $\Omega$ 的一个划分，则对任意事件 $B$，有：
$$P(B) = \sum_{i=1}^n P(A_i) P(B \mid A_i)$$

#### (2) 证明
因为 $\Omega = \bigcup_{i=1}^n A_i$，故：
$$B = B \cap \Omega = B \cap \left(\bigcup_{i=1}^n A_i\right) = \bigcup_{i=1}^n (B \cap A_i)$$
由于 $A_i$ 两两互斥，故 $(B \cap A_i)$ 亦两两互斥。由有限可加性：
$$P(B) = \sum_{i=1}^n P(B \cap A_i)$$
再应用条件概率乘法法则 $P(B \cap A_i) = P(A_i) P(B \mid A_i)$，即得证。 $\blacksquare$

- **思想精髓**：“**化整为零，分而治之**”。当复杂事件 $B$ 的概率无法直接求解时，通过全面考察导致 $B$ 发生的各种可能“原因”或“情境” $A_i$，先求出各情境下的条件概率，再以先验概率为权重做加权平均。

---

### 6.3 贝叶斯定理 (Bayes' Theorem) 与后验概率更新

#### (1) 定理表述
设 $A_1, \dots, A_n$ 为样本空间 $\Omega$ 的划分，$B$ 为某一观测事件且 $P(B) > 0$。则对任意 $k \in \{1, \dots, n\}$：
$$P(A_k \mid B) = \frac{P(A_k \cap B)}{P(B)} = \frac{P(A_k) P(B \mid A_k)}{\sum_{i=1}^n P(A_i) P(B \mid A_i)}$$

#### (2) 贝叶斯思维的认知闭环
- **先验概率 (Prior Probability, $P(A_k)$)**：在观测到新证据/新数据 $B$ 之前，我们对原因 $A_k$ 发生可能性的初始信念；
- **似然度 (Likelihood, $P(B \mid A_k)$)**：如果原因 $A_k$ 确实发生，出现观测结果 $B$ 的条件可能性；
- **后验概率 (Posterior Probability, $P(A_k \mid B)$)**：在观测到新证据 $B$ 出现之后，对原因 $A_k$ 发生可能性的更新信念。

$$\text{后验概率 (Posterior)} \propto \text{先验概率 (Prior)} \times \text{似然度 (Likelihood)}$$

---

### 6.4 深度剖析：医学筛查中的“假阳性悖论”与基础比率谬误 (Base Rate Fallacy)

课件第 129~131 页给出的宫颈癌 Pap smear 筛查案例（例 1.5.3）是现代概率论中最具社会与临床价值的经典问题：

#### (1) 题目数据与事件设定
- 设 $C^+$ 为患病（Cancer），$C^-$ 为未患病（Not Cancer）；
- 设 $T^+$ 为检测阳性（Test Positive），$T^-$ 为检测阴性（Test Negative）；
- **基础患病率 (Prior / Prevalence)**：全美每 10 万名女性中约 8 人患病：
  $$P(C^+) = \frac{8}{100,000} = 0.00008, \quad P(C^-) = 1 - 0.00008 = 0.99992$$
- **假阴性率 (False Negative Rate)**：患病女性中检测为阴性的概率为 $16\%$：
  $$P(T^- \mid C^+) = 0.16 \implies \text{灵敏度 (Sensitivity)} = P(T^+ \mid C^+) = 1 - 0.16 = 0.84$$
- **假阳性率 (False Positive Rate)**：未患病女性中检测为阳性的概率为 $10\%$：
  $$P(T^+ \mid C^-) = 0.10 \implies \text{特异度 (Specificity)} = P(T^- \mid C^-) = 1 - 0.10 = 0.90$$

#### (2) 贝叶斯计算：检测阳性者真患病的概率
现有一名女性检测结果呈阳性 ($T^+$)，求她真正患病的概率 $P(C^+ \mid T^+)$：

1. **计算全人群的检测阳性率 $P(T^+)$（全概率公式）**：
   $$P(T^+) = P(C^+) P(T^+ \mid C^+) + P(C^-) P(T^+ \mid C^-)$$
   $$P(T^+) = (0.00008 \times 0.84) + (0.99992 \times 0.10)$$
   $$P(T^+) = 0.0000672 + 0.099992 = 0.1000592 \approx 10.01\%$$
2. **应用贝叶斯定理计算后验概率**：
   $$P(C^+ \mid T^+) = \frac{P(C^+) P(T^+ \mid C^+)}{P(T^+)} = \frac{0.0000672}{0.1000592} \approx 0.0006716 \approx 0.0672\%$$

#### (3) 结果解读与“假阳性悖论”深度剖析
- **惊人事实**：一个灵敏度高达 $84\%$、特异度高达 $90\%$ 的医学筛查，**当检测结果呈阳性时，受检者真正患病的概率竟然只有不到 $0.07\%$**（约千分之零点六七）！这意味着每 100 万个阳性检测者中，仅有 672 人是真正的患者，其余 999,328 人全是被误诊的健康人（假阳性）！
- **为什么会出现这种反直觉的现象？——基础比率谬误 (Base Rate Fallacy)**：  
  因为该疾病本身是极度罕见的（先验概率只有 $0.008\%$），而健康人群的基数庞大到占据了 $99.992\%$。即使健康人群被误诊的假阳性率只有 $10\%$，这 $10\%$ 乘上庞大的健康基数，所产生的假阳性绝对人数（约 10 万人）也远远压倒了真正患病且被检出的真阳性人数（约 67 人）！
- **测试是否有价值？**：  
  课件精辟地指出：从信息更新角度看，该测试绝非毫无用处。受检者在测试前的患病概率是 $0.008\%$，阳性后概率提升到 $0.0672\%$，**后验概率是先验概率的 8.4 倍**！它起到了重要的初筛分流作用，只是在面对罕见疾病时，不能单凭单次普筛阳性直接确诊，必须配合高特异度的二次复查（如活检穿刺）。

---

## 7. 第六节：伯努利试验 (1.6 Bernoulli Trials)

### 7.1 伯努利试验与独立试验序列

#### (1) 伯努利试验 (Bernoulli Experiment)
结果只有两种可能、相互对立且完备的随机试验：
$$\Omega = \{\text{成功 (Success, 1)}, \text{失败 (Failure, 0)}\}$$
成功概率记为 $p$ ($0 < p < 1$)，失败概率记为 $q = 1 - p$。

#### (2) $n$ 重伯努利试验序列 (Sequence of $n$ Bernoulli Trials)
将同一个伯努利试验独立重复进行 $n$ 次，满足：
1. **独立性**：各次试验的结果互不影响；
2. **齐次性 (Homogeneity)**：每次试验中成功的概率恒为 $p$，保持不变。

- **样本空间结构**：
  $$\Omega^n = \Omega_1 \times \Omega_2 \times \dots \times \Omega_n = \{0, 1\}^n$$
  样本空间中总共包含 $2^n$ 个基本事件。每一个具体的基本事件形如 $\omega = (e_1, e_2, \dots, e_n)$，其中 $e_i \in \{0, 1\}$。

---

### 7.2 二项概率模型与分布性质

若在 $n$ 重伯努利试验中，关注“成功出现的总次数”记为随机变量 $X$：
- 某一特定的、包含 $k$ 次成功与 $n-k$ 次失败的序列（例如前 $k$ 次成功后 $n-k$ 次失败），由独立性，其发生概率为：
  $$p^k (1-p)^{n-k}$$
- 在 $n$ 次试验中，恰好出现 $k$ 次成功的不同序列排列方式共有组合数 $\binom{n}{k} = C_n^k$ 种；
- 因此，$n$ 次试验中恰好成功 $k$ 次的概率为经典的**二项概率公式 (Binomial Formula)**：
  $$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, 2, \dots, n$$

---

### 7.3 典型案例计算（例 1.6.1：甜菜种子发芽问题）

#### 题目背景
甜菜种子单颗发芽概率 $p = 0.8$。各种子发芽独立。播种 $n = 10$ 颗种子，构成 10 重伯努利试验，单次失败（不发芽）概率 $q = 1 - 0.8 = 0.2$。

#### (a) 至少有一颗种子发芽的概率
- “至少一颗发芽”的对立事件是“全部没有发芽”（0 颗发芽）：
  $$P(X \ge 1) = 1 - P(X = 0) = 1 - \binom{10}{0} (0.8)^0 (0.2)^{10} = 1 - (0.2)^{10} = 1 - 1.024 \times 10^{-7} \approx 0.9999998976$$

#### (b) 恰好有两颗种子发芽的概率
- 代入二项公式，$k = 2$：
  $$P(X = 2) = \binom{10}{2} (0.8)^2 (0.2)^8 = \frac{10 \times 9}{2} \times 0.64 \times (0.2)^8 = 45 \times 0.64 \times 0.00000256 \approx 7.3728 \times 10^{-5}$$

#### (c) 至多有九颗种子发芽的概率
- “至多九颗发芽”的对立事件是“全部 10 颗均发芽”：
  $$P(X \le 9) = 1 - P(X = 10) = 1 - \binom{10}{10} (0.8)^{10} (0.2)^0 = 1 - (0.8)^{10} \approx 1 - 0.107374 = 0.892626$$

---

## 8. 核心公式速查与易错知识点辨析 (Summary & Pitfalls)

### 8.1 第一章核心公式一览表

| 核心公式 / 定理 | 数学表达式 | 关键适用条件 / 备注 |
| :--- | :--- | :--- |
| **加法公式（两事件）** | $P(A \cup B) = P(A) + P(B) - P(AB)$ | 任意两事件均适用 |
| **互斥事件加法** | $P(A \cup B) = P(A) + P(B)$ | 充要条件：$A \cap B = \emptyset$ |
| **测度连续性定理** | $P(\lim A_n) = \lim P(A_n)$ | 对单调递增/递减集合序列恒成立 |
| **布尔不等式 (Union Bound)** | $P(\bigcup_{i=1}^n A_i) \le \sum_{i=1}^n P(A_i)$ | 提供了并集概率的天然上界 |
| **邦弗朗尼不等式** | $P(\bigcap_{i=1}^n A_i) \ge \sum P(A_i) - (n-1)$ | 适用于高概率事件交集的下界估计 |
| **古典概型** | $P(A) = |A| / |\Omega|$ | 有限样本空间 + 各样本点等可能 |
| **几何概型** | $P(A) = S_A / S_\Omega$ | 连续样本空间 + 几何测度均匀分布 |
| **条件概率定义** | $P(A \mid B) = \frac{P(AB)}{P(B)}$ | 必须保证 $P(B) > 0$ |
| **事件独立性定义** | $P(AB) = P(A)P(B)$ | 对包括零概率在内的任意事件通用 |
| **全概率公式** | $P(B) = \sum_{i=1}^n P(A_i) P(B \mid A_i)$ | $A_1, \dots, A_n$ 构成 $\Omega$ 的划分 |
| **贝叶斯定理** | $P(A_k \mid B) = \frac{P(A_k) P(B \mid A_k)}{\sum_{i=1}^n P(A_i) P(B \mid A_i)}$ | 后验概率更新公式 |
| **二项分布概率公式** | $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$ | $n$ 重独立伯努利试验序列 |

---

### 8.2 易错知识点深度辨析矩阵

#### 辨析 1：“互斥 (Mutually Exclusive)” vs “独立 (Independent)”
这是概率论初学者最常混淆的一对概念：
- **互斥是集合结构关系**：$A \cap B = \emptyset$。意味着 $A$ 与 $B$ 不能同时发生。若 $A$ 发生，$B$ 一定不发生（信息量极大相关！）；
- **独立是概率测度关系**：$P(AB) = P(A)P(B)$。意味着 $A$ 发不发生完全不影响 $B$ 的概率；
- **核心定理**：设 $P(A) > 0$ 且 $P(B) > 0$：
  - 若 $A$ 与 $B$ 互斥，则 $P(AB) = 0 \ne P(A)P(B) > 0$，因此**互斥事件绝不可能独立**！
  - 反之，若 $A$ 与 $B$ 独立，则 $P(AB) = P(A)P(B) > 0$，因此**独立事件绝不可能互斥**！

#### 辨析 2：“条件概率 $P(A \mid B)$” vs “积事件概率 $P(AB)$”
- **样本空间基准不同**：
  - $P(AB)$ 是以原样本空间 $\Omega$ 为基准，衡量 $A$ 和 $B$ 同时落入的概率；
  - $P(A \mid B)$ 是以压缩后的新样本空间 $B$ 为基准，衡量在已知 $B$ 的前提下 $A$ 的占比。
- **比值关系**：$P(AB) = P(A \mid B) \cdot P(B)$。因为 $P(B) \le 1$，通常有 $P(AB) \le P(A \mid B)$。

#### 辨析 3：“零概率事件” vs “不可能事件”
- 不可能事件一定是空集 $\emptyset$，其概率严格为 0；
- 但概率为 0 的事件不一定是空集。例如在 $[0, 1]$ 上的几何概型中，取到具体某一个单点数 $\{0.5\}$ 的概率为 $\frac{0}{1} = 0$，但该点属于样本空间，是可能被取到的样本点。
