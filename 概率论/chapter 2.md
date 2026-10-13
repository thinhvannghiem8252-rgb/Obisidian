# Math1212 概率论与数理统计 I (Probability and Statistics I)
## 第二章：一维随机变量及其分布 课程讲义全景精要与深度解析笔记

> **课程信息**：Math1212 Probability and Statistics I (Fall 2025/2026)  
> **授课机构**：上海科技大学 数学科学学院 (Institute of Mathematical Sciences, ShanghaiTech University)  
> **主讲教师**：王世家 (Shijia Wang)  
> **参考教材**：
> 1. Robert V. Hogg, Elliot A. Tanis, Dale Zimmerman, *Probability and Statistical Inference* (9th/10th ed.), Ch. 2.1, 2.4–2.6, 3.1–3.3, 5.1
> 2. 魏宗舒 等，《概率论与数理统计教程》（第三版），高等教育出版社，Ch. 2.1, 2.3, 3.1, 3.4
> 3. Larry Wasserman, *All of Statistics*, Springer, Ch. 2.1, 2.2

---

## 目录与知识架构

1. **引言：为什么需要随机变量？(Motivation & Philosophical Foundation)**
   - 1.1 从样本空间到实数轴的映射
   - 1.2 随机变量的严格数学定义与测度论可测性
   - 1.3 随机变量的代数运算与代数封闭性
2. **累积分布函数 (Cumulative Distribution Function, CDF)**
   - 2.1 CDF 的定义与直观意义
   - 2.2 CDF 的充要公理化性质 (定理 2.3)
   - 2.3 定理 2.3 的严格测度连续性证明
   - 2.4 随机变量的两大基本类型：离散型与连续型
3. **第一节：一维离散型随机变量与概率质量函数 (2.1 Discrete Random Variables & PMF)**
   - 3.1 概率质量函数 (PMF) 的定义与公理化性质
   - 3.2 PMF 与 CDF 的阶梯对应关系
   - 3.3 经典案例剖析：双骰子极大值分布的推导与图示
   - 3.4 离散分布的可视化：折线图 (Line Graph) 与概率直方图 (Histogram)
4. **第二节：一维连续型随机变量与概率密度函数 (2.2 Continuous Random Variables & PDF)**
   - 4.1 概率密度函数 (PDF) 的严格定义与物理意义
   - 4.2 微积分基本定理下的 PDF 与 CDF 对偶关系
   - 4.3 核心本质辨析：为什么连续型 PDF 的值不是概率？
   - 4.4 连续均匀分布与三角/多项式密度典型案例
5. **第三节：随机变量函数的分布 (2.3 Distributions of Functions of Random Variables)**
   - 5.1 变量代换方法论：CDF 法 (Distribution Function Technique)
   - 5.2 单调可逆变换定理 (定理 2.4, 2.5, 2.6) 与雅可比因子 (Jacobian)
   - 5.3 经典连续代换案例深度解析：
     - Gamma 到 Loggamma 的指数变换
     - 旋转指针与标准柯西分布 (Cauchy) 的几何生成
     - 非单调变换：平方变换 $Y = X^2$ 与两分支求和法
   - 5.4 概率积分变换与逆变换抽样定理 (Theorems 2.7 & 2.8)
   - 5.5 离散型随机变量的代换技巧及与连续型的关键差异
6. **第四节：常见离散型随机变量分布 (2.4.1 Common Discrete Distributions)**
   - 6.1 离散均匀分布 (Discrete Uniform Distribution)
   - 6.2 伯努利分布 (Bernoulli Distribution)
   - 6.3 二项分布 (Binomial Distribution) 及其偏度形态
   - 6.4 负二项分布 (Negative Binomial) 与几何分布 (Geometric)
   - 6.5 泊松分布 (Poisson Distribution) 与发生率模型
   - 6.6 泊松极限定理 (Poisson Theorem / 稀有事件定律) 的严格证明与近似分析
7. **第五节：常见连续型随机变量分布 (2.4.2 Common Continuous Distributions)**
   - 7.1 连续均匀分布 (Continuous Uniform Distribution)
   - 7.2 柯西分布 (Cauchy Distribution)：厚尾特性与矩不存在悖论
   - 7.3 指数分布 (Exponential Distribution) 与无记忆性 (Memoryless Property) 的唯一定理
   - 7.4 伽马分布 (Gamma Distribution) 与不完全 Gamma 函数
   - 7.5 卡方分布 (Chi-square Distribution) 作为 Gamma 分布的特例
   - 7.6 正态分布 (Normal Distribution) 与标准化变换定理
8. **核心公式速查与易错知识点深度辨析 (Summary & Pitfalls)**

---

## 1. 引言：为什么需要随机变量？(Motivation & Philosophical Foundation)

### 1.1 从样本空间到实数轴的映射
在第一章中，我们建立了概率空间 $(\Omega, \mathcal{F}, P)$。然而在实际随机试验中，样本点 $\omega \in \Omega$ 往往是**非数值化的定性描述**。例如：
- 抛硬币：$\omega \in \{\text{"Head"}, \text{"Tail"}\}$；
- 医疗诊断：$\omega \in \{\text{"治愈"}, \text{"复发"}, \text{"死亡"}\}$；
- 产品质检：$\omega \in \{\text{"合格品"}, \text{"次品"}\}$。

若直接使用样本点集合来描述复杂的复合事件（如 $n$ 重伯努利试验中“正面次数总和大于 5”），只能依靠穷举枚举法或文字长句，无法借助微积分、线性代数和函数分析等强大的现代数学工具。  
因此，必须在样本空间 $\Omega$ 与实数集 $\mathbb{R}$ 之间建立一座数学桥梁——**将抽象的定性结果数值化**。

### 1.2 随机变量的严格数学定义与可测性
课件第 6 页给出了随机变量的标准定义：

> **定义（随机变量, Random Variable, 简记 r.v.）**：  
> 设给定随机试验的样本空间为 $\Omega$。一个将样本空间中每个元素 $\omega \in \Omega$ **单值映射**到唯一实数 $X(\omega) = x \in \mathbb{R}$ 的实值函数：
> $$X: \Omega \to \mathbb{R}$$
> 称为**随机变量 (Random Variable)**。

- **定义域 (Domain)**：试验的样本空间 $\Omega$；
- **值域 / 支撑集 (Range / Support / Space)**：随机变量所有可能取值的实数集合，记作 $\mathbb{X} = \{x \in \mathbb{R} : X(\omega) = x, \omega \in \Omega\}$。

> **【深度补充解释 1：测度论视角下的“可测函数 (Measurable Function)”】**  
> 为什么一个普通的实值函数被称为“随机变量”而不是“函数”？  
> 在严谨的现代测度论概率体系中，不能随便抓一个映射就叫随机变量。为了能够对形如 $P(X \le x)$ 或 $P(X \in B)$ 的事件计算概率，**原像必须是概率空间中的合法可测事件**！  
> 即：对实数轴 Borel $\sigma$-代数中的任意集合 $B \in \mathcal{B}(\mathbb{R})$，其原像集合必须属于事件域 $\mathcal{F}$：
> $$X^{-1}(B) = \{\omega \in \Omega : X(\omega) \in B\} \in \mathcal{F}$$
> 因此，**随机变量的严格数学本质是可测空间 $(\Omega, \mathcal{F})$ 到 $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ 上的可测函数 (Measurable Function)**。

### 1.3 随机变量的代数运算与代数封闭性
课件第 7 页给出了随机变量的代数性质（命题 2.1 与 2.2）：
- **命题 2.1**：若 $X, Y$ 是随机变量，则对任意实数常数 $a, b \in \mathbb{R}$，下列运算生成的对象依然是良定义的随机变量：
  $$X + Y, \quad X - Y, \quad XY, \quad \frac{X}{Y} \; (Y \ne 0), \quad aX + bY$$
- **命题 2.2**：若 $X, Y$ 是随机变量，$\phi: \mathbb{R}^2 \to \mathbb{R}$ 是二元可测函数，则复合映射 $\phi(X, Y)$ 亦为随机变量。

---

## 2. 累积分布函数 (Cumulative Distribution Function, CDF)

### 2.1 CDF 的定义与直观意义
虽然随机变量本身是一个映射，但统计学关心的是其取值落在某个区间的可能性大小。

> **定义（累积分布函数, CDF）**：  
> 对于概率空间 $(\Omega, \mathcal{F}, P)$ 上的任意随机变量 $X$，定义在整个实数轴 $\mathbb{R} = (-\infty, +\infty)$ 上的函数：
> $$F(x) = P(X \le x) = P(\{\omega \in \Omega : X(\omega) \le x\})$$
> 称为随机变量 $X$ 的**累积分布函数 (Cumulative Distribution Function, CDF)**，或简称为**分布函数**。

- **物理直观**：$F(x)$ 描述了随机变量落在区间 $(-\infty, x]$ 内的总累积概率质量。
- **区间概率计算公式**：
  $$P(a < X \le b) = F(b) - F(a)$$
  $$P(X = x) = F(x) - F(x^-)$$
  $$P(X > x) = 1 - F(x)$$

---

### 2.2 CDF 的充要公理化性质 (定理 2.3)
课件第 9 页指出了判定一个函数是否为合法 CDF 的三条充要条件：

> **定理 2.3**：实函数 $F(x)$ 是某个随机变量的累积分布函数 (CDF) 的**充分必要条件**是满足以下三条性质：
> 1. **极限边界性 (Boundary Limits)**：
>    $$\lim_{x \to -\infty} F(x) = 0, \quad \lim_{x \to +\infty} F(x) = 1$$
> 2. **右连续性 (Right-continuity)**：$F(x)$ 处处右连续，即对任意 $x \in \mathbb{R}$：
>    $$F(x^+) = \lim_{y \downarrow x} F(y) = F(x)$$
> 3. **单调不减性 (Non-decreasing)**：若 $x_1 < x_2$，则 $F(x_1) \le F(x_2)$。

---

### 2.3 定理 2.3 的严格测度连续性证明
课件第 10~11 页给出了极其优美的测度连续性证明，完美衔接了第一章的理论：

#### (1) 右连续性证明：
- 设 $x$ 为任意实数，取严格递减收敛到 $x$ 的实数数列 $\{y_n\}$，即 $y_1 > y_2 > \dots > x$ 且 $\lim_{n \to \infty} y_n = x$；
- 构造单调递减的事件序列 $A_n = \{\omega : X(\omega) \le y_n\} = (-\infty, y_n]$；
- 显然 $A_1 \supset A_2 \supset A_3 \dots$，且其交集为：
  $$A = \bigcap_{n=1}^\infty A_n = \bigcap_{n=1}^\infty (-\infty, y_n] = (-\infty, x] = \{\omega : X(\omega) \le x\}$$
- 由第一章**概率测度的下连续性（定理 1.1.7 / 推论 1.1.9）**：
  $$\lim_{n \to \infty} P(A_n) = P(A)$$
- 将 CDF 定义代入：
  $$\lim_{n \to \infty} F(y_n) = F(x)$$
  因数列 $\{y_n\}$ 的任意性，即证明了右极限 $F(x^+) = F(x)$。 $\blacksquare$

#### (2) 极限边界性证明：
- **上极限**：取单调增序列 $A_n = (-\infty, n]$，$A_1 \subset A_2 \subset \dots$。由可数并性质：
  $$\bigcup_{n=1}^\infty A_n = (-\infty, +\infty) = \Omega$$
  由概率测度的上连续性：$\lim_{n \to \infty} F(n) = \lim_{n \to \infty} P(A_n) = P(\Omega) = 1$。
- **下极限**：取单调减序列 $B_n = (-\infty, -n]$，$B_1 \supset B_2 \supset \dots$。其交集为：
  $$\bigcap_{n=1}^\infty B_n = \emptyset$$
  由概率测度的下连续性：$\lim_{n \to \infty} F(-n) = \lim_{n \to \infty} P(B_n) = P(\emptyset) = 0$。 $\blacksquare$

#### (3) 单调不减性证明：
若 $x_1 < x_2$，则事件包含关系 $(-\infty, x_1] \subset (-\infty, x_2]$。由第一章概率单调性定理：
$$P(X \le x_1) \le P(X \le x_2) \iff F(x_1) \le F(x_2) \quad \blacksquare$$

---

### 2.4 随机变量的两大基本类型
根据值域与 CDF 的形态，随机变量分为：
1. **离散型 (Discrete Type)**：
   - 支撑集 $\mathbb{X}$ 最多包含**可数个**数值；
   - 其 CDF 表现为**阶梯函数 (Step Function)**，在每一个可能取值点处发生跳跃，跳跃高度等于该点的概率质量；
2. **连续型 (Continuous Type)**：
   - 支撑集 $\mathbb{X}$ 为一个区间或若干区间的并集；
   - 其 CDF 是**连续函数**（处处连续，无跳跃）。

---

## 3. 第一节：一维离散型随机变量与概率质量函数 (2.1 Discrete Random Variables & PMF)

### 3.1 概率质量函数 (PMF) 的定义与公理化性质
对于离散型随机变量 $X$，直接研究单点概率是最自然的途径。

> **定义（概率质量函数, PMF）**：  
> 离散型随机变量 $X$ 的概率质量函数 $f(x)$（课件常用记号，国内教材常记为 $p(x)$ 或 $P(X = x_i)$）定义为：
> $$f(x) = P(X = x)$$

#### PMF 的充要性质：
1. **非负性**：$f(x) \ge 0, \quad \forall x \in \mathbb{X}$；
2. **归一性 (Normed)**：$\sum_{x \in \mathbb{X}} f(x) = 1$；
3. **可加性**：对任意子集 $A \subset \mathbb{X}$，有 $P(X \in A) = \sum_{x \in A} f(x)$。

### 3.2 PMF 与 CDF 的对应关系
已知 PMF 求 CDF：
$$F(x) = \sum_{y \le x} f(y)$$
已知 CDF 求单点 PMF：在跳跃点 $x$ 处，PMF 等于跳跃高度：
$$f(x) = F(x) - F(x^-)$$

---

### 3.3 经典案例剖析：双骰子极大值分布（例 2.2）
掷两颗均匀六面骰子，样本空间 $\Omega^2 = \{(\omega_1, \omega_2) : \omega_i \in \{1, \dots, 6\}\}$，总可能数 $|\Omega| = 36$。  
令随机变量 $X = \max(\omega_1, \omega_2)$ 为两颗骰子朝上面点数的较大者。求 $X$ 的分布。

#### 严谨推导与思维模型：
- **方法一：直接穷举枚举法**
  - $X = 1$：仅 $(1, 1)$，共 1 种，故 $f(1) = 1/36$；
  - $X = 2$：$(1, 2), (2, 1), (2, 2)$，共 3 种，故 $f(2) = 3/36$；
  - $X = 3$：$(3, 1), (1, 3), (3, 2), (2, 3), (3, 3)$，共 5 种，故 $f(3) = 5/36$；
  - $X = 4$：共 7 种，故 $f(4) = 7/36$；
  - $X = 5$：共 9 种，故 $f(5) = 9/36$；
  - $X = 6$：共 11 种，故 $f(6) = 11/36$。

- **方法二：CDF 差分转化法（推荐高级解法）**  
  事件 $\{\max(\omega_1, \omega_2) \le k\} \iff \{\omega_1 \le k \text{ 且 } \omega_2 \le k\}$。  
  由于两颗骰子独立：
  $$P(X \le k) = P(\omega_1 \le k) P(\omega_2 \le k) = \frac{k}{6} \times \frac{k}{6} = \frac{k^2}{36}$$
  由此可直接写出阶梯状 CDF：
  $$F(x) = \begin{cases} 0, & x < 1 \\ \frac{k^2}{36}, & k \le x < k + 1, \quad k = 1, 2, 3, 4, 5 \\ 1, & x \ge 6 \end{cases}$$
  而单点 PMF 即为相邻平方差：
  $$f(k) = F(k) - F(k-1) = \frac{k^2 - (k-1)^2}{36} = \frac{2k - 1}{36}, \quad k = 1, 2, \dots, 6$$

---

### 3.4 离散分布的可视化表示
课件第 22~23 页展示了离散分布的两种主流图形化工具：
1. **折线针状图 (Line Graph / Spike Plot)**：在横轴每个取值点 $x$ 处作垂直线段，高度为 $f(x)$；
2. **概率直方图 (Probability Histogram)**：在横轴以每个取值点 $x$ 为中心，以底边宽度为 1（若间距为 1）、高度为 $f(x)$ 绘制矩形柱。  
   - 核心几何特性：每个矩形的底宽为 1，因而每个小矩形的面积严格等于该点的概率质量 $f(x)$；
   - **所有矩形的总面积严格等于 1**。这一设计在直观上将离散的概率质量平滑过渡到了连续型的概率密度面积概念。

---

## 4. 第二节：一维连续型随机变量与概率密度函数 (2.2 Continuous Random Variables & Pdf)

### 4.1 概率密度函数 (PDF) 的严格定义与性质

> **定义（概率密度函数, Probability Density Function, PDF）**：  
> 设 $X$ 为连续型随机变量，其累积分布函数为 $F(x)$。在 $F(x)$ 可导（即 $f(x)$ 连续）的每一个实数点上，CDF 的一阶导数称为 $X$ 的**概率密度函数**：
> $$f(x) = \frac{dF(x)}{dx}$$

#### PDF 的充要公理化性质：
1. **非负性**：$f(x) \ge 0, \quad \forall x \in \mathbb{X}$；
2. **全积分归一性**：$\int_{-\infty}^{+\infty} f(x) dx = 1$；
3. **区间测度性**：对任意实数子集 $A \in \mathcal{B}(\mathbb{R})$：
   $$P(X \in A) = \int_A f(x) dx$$

---

### 4.2 微积分基本定理下的 PDF 与 CDF 对偶关系
- **由密度求分布（积分累积）**：
  $$F(x) = \int_{-\infty}^x f(s) ds, \quad \forall x \in (-\infty, +\infty)$$
- **由分布求密度（微分斜率）**：
  $$f(x) = F'(x) = \frac{d}{dx} \int_{-\infty}^x f(s) ds$$

---

### 4.3 核心本质辨析：为什么连续型 PDF 的值不是概率？
这是概率论教学中最关键的认知飞跃：

1. **单点概率恒为 0**：  
   对于连续型随机变量，由积分性质：
   $$P(X = c) = \int_c^c f(x) dx = 0$$
   因此：$P(a < X < b) = P(a \le X < b) = P(a < X \le b) = P(a \le X \le b) = F(b) - F(a)$。是否包含端点不影响区间概率。
2. **密度 (Density) vs 质量 (Mass)**：  
   在物理学中，质量密度 $\rho(x) = \frac{dm}{dx}$ 的量纲是“质量 / 长度”。同理，概率密度 $f(x)$ 的量纲是“概率 / 长度”。
3. **微元法诠释**：在微小区间 $[x, x + dx]$ 上：
   $$P(x \le X \le x + dx) \approx f(x) dx$$
4. **$f(x)$ 可以大于 1**：  
   因为 $f(x)$ 不是概率，只要总积分等于 1，$f(x)$ 在局部完全可以大于 1，甚至在奇点处趋向无穷大！例如 $X \sim U(0, 0.1)$，其密度为 $f(x) = 10 > 1$。

---

### 4.4 连续分布计算典型案例
- **例 2.3（连续均匀分布）**：$X \sim U(1, 2)$，$f(x) = 1$ ($1 \le x \le 2$)。  
  积分求得 CDF：
  $$F(x) = \begin{cases} 0, & x < 1 \\ x - 1, & 1 \le x \le 2 \\ 1, & x > 2 \end{cases}$$
- **例 2.4（线性三角密度）**：$f(x) = 2x$ ($0 \le x \le 1$)。  
  积分求得 CDF：
  $$F(x) = \int_0^x 2s ds = x^2, \quad 0 \le x \le 1$$
  图像上：$f(x)$ 是一条斜率为 2 的上升线段，其 CDF 是一段顶点在原点的抛物线，在 $x=1$ 处平滑过渡到常数 1。

---

## 5. 第三节：随机变量函数的分布 (2.3 Distributions of Functions of Random Variables)

在工程信号处理、统计建模与机器学习中，常常需要对已知随机变量 $X$ 进行非线性变换得到新的随机变量 $Y = g(X)$。如何严谨求解 $Y$ 的分布？

### 5.1 变量代换方法论：CDF 法 (Distribution Function Technique)
CDF 法是最本质、最稳健的基础方法，其标准解题流水线分为三步：
1. **确定 $Y$ 的支撑集 $\mathbb{Y}$**；
2. **写出 $Y$ 的累积分布函数定义**：
   $$F_Y(y) = P(Y \le y) = P(g(X) \le y)$$
   通过不等式变换，将 $g(X) \le y$ 解出关于 $X$ 的等价取值区间；
3. **代入 $X$ 的分布积分，并对 $y$ 求导得到密度 $f_Y(y) = F_Y'(y)$**。

---

### 5.2 单调可逆变换定理与雅可比公式

#### (1) 严格单调递增情形 (定理 2.4)
若 $g(x)$ 严格单调递增且可导，其反函数为 $x = g^{-1}(y)$：
$$F_Y(y) = P(g(X) \le y) = P(X \le g^{-1}(y)) = F_X(g^{-1}(y))$$
两边对 $y$ 应用链式求导法则：
$$f_Y(y) = \frac{d}{dy} F_X(g^{-1}(y)) = f_X(g^{-1}(y)) \cdot \frac{dg^{-1}(y)}{dy}$$

#### (2) 严格单调递减情形 (定理 2.5)
若 $g(x)$ 严格单调递减且可导：
$$F_Y(y) = P(g(X) \le y) = P(X \ge g^{-1}(y)) = 1 - F_X(g^{-1}(y))$$
两边对 $y$ 求导：
$$f_Y(y) = - f_X(g^{-1}(y)) \cdot \frac{dg^{-1}(y)}{dy}$$
注意：因为 $g(x)$ 递减，其反函数导数 $\frac{dg^{-1}(y)}{dy} < 0$，负负得正，保证了 $f_Y(y) \ge 0$。

#### (3) 统一定理：雅可比单调变换公式 (定理 2.6)

> **定理 2.6（单调代换通用定理）**：  
> 设 $X$ 为连续型随机变量，其密度为 $f_X(x)$。设 $y = g(x)$ 是严格单调且处处可导的可逆变换，反函数为 $x = g^{-1}(y)$。则 $Y = g(X)$ 的概率密度函数为：
> $$f_Y(y) = f_X(g^{-1}(y)) \cdot \left| \frac{dg^{-1}(y)}{dy} \right|, \quad y \in \mathbb{Y}$$

其中因子 $\left| \frac{dg^{-1}(y)}{dy} \right| = \left| \frac{dx}{dy} \right|$ 称为**一维变换的雅可比行列式 (Jacobian)**。

---

### 5.3 经典连续代换案例深度解析

#### 案例 1：Gamma 分布到 Loggamma 分布（例 2.5）
设 $X \sim \text{Gamma}(\alpha, \theta)$，其密度为 $f_X(x) = \frac{1}{\Gamma(\alpha)\theta^\alpha} x^{\alpha-1} e^{-x/\theta}, x > 0$。  
作指数变换 $Y = g(X) = e^X$。
- **确定支撑集**：$x \in (0, \infty) \implies y = e^x \in (1, \infty)$；
- **反函数与导数**：$x = g^{-1}(y) = \ln y$，$\frac{dx}{dy} = \frac{1}{y} > 0$；
- **代入雅可比公式**：
  $$f_Y(y) = f_X(\ln y) \left| \frac{dx}{dy} \right| = \frac{1}{\Gamma(\alpha)\theta^\alpha} (\ln y)^{\alpha-1} e^{-\frac{\ln y}{\theta}} \cdot \frac{1}{y}$$
  由于 $e^{-\frac{\ln y}{\theta}} = (e^{\ln y})^{-1/\theta} = y^{-1/\theta}$，合并同类项：
  $$f_Y(y) = \frac{1}{\Gamma(\alpha)\theta^\alpha} (\ln y)^{\alpha-1} y^{-(1 + 1/\theta)}, \quad 1 < y < \infty$$
  该分布被称为 **Loggamma 分布**。

#### 案例 2：旋转指针与标准柯西分布的物理生成（例 2.6）
在平面笛卡尔坐标系中，点 $(0, 1)$ 处安装一个可自由旋转的发光探针。探针与 $y$ 轴负方向的夹角 $W$ 服从对称均匀分布 $W \sim U(-\pi/2, \pi/2)$。  
光线射向 $x$ 轴的交点坐标为 $X$。由三角几何关系，$X = \tan W$。求 $X$ 的概率分布。
- $W$ 的 CDF 为：$F_W(w) = \frac{w - (-\pi/2)}{\pi} = \frac{w + \pi/2}{\pi}, \quad w \in (-\pi/2, \pi/2)$；
- $X = \tan W$ 在 $(-\pi/2, \pi/2)$ 上严格单调递增，值域为 $(-\infty, +\infty)$；
- $X$ 的 CDF：
  $$F_X(x) = P(\tan W \le x) = P(W \le \arctan x) = F_W(\arctan x) = \frac{\arctan x + \pi/2}{\pi}$$
- 求导得 PDF：
  $$f_X(x) = \frac{d}{dx} \left( \frac{\arctan x}{\pi} + \frac{1}{2} \right) = \frac{1}{\pi (1 + x^2)}, \quad -\infty < x < \infty$$
- **结论**：这就是著名的**标准柯西分布 (Standard Cauchy Distribution)**！这一几何光学模型揭示了柯西分布的物理来源。

#### 案例 3：非单调变换：$Y = X^2$ 的两分支求和法（例 2.7）
若 $X \sim \text{Cauchy}(1, 0)$，求 $Y = X^2$ 的分布。
- **问题特征**：函数 $y = x^2$ 在整个定义域 $(-\infty, +\infty)$ 上**不是单调函数**（两边平方对称），无法直接应用定理 2.6。
- **CDF 分支展开**：$y \ge 0$ 时：
  $$F_Y(y) = P(X^2 \le y) = P(-\sqrt{y} \le X \le \sqrt{y}) = F_X(\sqrt{y}) - F_X(-\sqrt{y})$$
- **求导并结合对称性**：
  $$f_Y(y) = \frac{d}{dy} [F_X(\sqrt{y}) - F_X(-\sqrt{y})] = f_X(\sqrt{y}) \cdot \frac{1}{2\sqrt{y}} - f_X(-\sqrt{y}) \cdot \left(-\frac{1}{2\sqrt{y}}\right)$$
  $$f_Y(y) = \frac{1}{2\sqrt{y}} [f_X(\sqrt{y}) + f_X(-\sqrt{y})]$$
  因为柯西密度是偶函数 $f_X(x) = f_X(-x) = \frac{1}{\pi(1+x^2)}$：
  $$f_Y(y) = \frac{1}{\sqrt{y}} f_X(\sqrt{y}) = \frac{1}{\pi (1 + y)\sqrt{y}}, \quad y \in [0, \infty)$$

---

### 5.4 概率积分变换与逆变换抽样定理 (Theorems 2.7 & 2.8)
课件第 42~43 页给出了计算统计学与蒙特卡洛随机模拟的理论奠基定理：

#### 定理 2.7（逆变换采样定理 / Inverse Transform Sampling）
设随机变量 $U \sim U(0, 1)$。若 $F_Y(y)$ 是任意连续且严格单调递增的累积分布函数，反函数为 $F_Y^{-1}$。  
定义随机变量 $Y = F_Y^{-1}(U)$，则 **$Y$ 的分布函数恰好就是 $F_Y(y)$**！
- *证明*：
  $$P(Y \le y) = P(F_Y^{-1}(U) \le y) = P(U \le F_Y(y))$$
  因为 $U \sim U(0, 1)$，对任意 $u \in (0, 1)$ 有 $P(U \le u) = u$。取 $u = F_Y(y) \in (0, 1)$，即得：
  $$P(Y \le y) = F_Y(y) \quad \blacksquare$$
- **计算机模拟的核心价值**：计算机伪随机数生成器只能产生标准的均匀分布伪随机数 $U(0, 1)$。利用该定理，只要算出目标分布的逆 CDF，就能将均匀随机数转化为任意指定连续分布的样本点！

#### 定理 2.8（概率积分变换 / Probability Integral Transform）
若连续型随机变量 $X$ 的 CDF $F_X(x)$ 严格单调递增，则构造的复合随机变量：
$$Y = F_X(X) \sim U(0, 1)$$
恒服从标准均匀分布。
- *证明*：对 $y \in (0, 1)$，$P(Y \le y) = P(F_X(X) \le y) = P(X \le F_X^{-1}(y)) = F_X(F_X^{-1}(y)) = y$。

---

### 5.5 离散型随机变量的代换技巧及与连续型的关键差异
课件第 46~48 页特别指出了离散型变量代换与连续型的本质差异：

- **核心差异**：离散型的 PMF $f_X(x) = P(X = x)$ **本身就是一个真实的概率值**，而不是单位区间的密度。因此在单调代换中，**完全不需要乘以导数/雅可比因子**！
- **单调变换公式**：若 $Y = g(X)$ 是一对一单射，反函数为 $X = g^{-1}(Y)$，则：
  $$f_Y(y) = P(Y = y) = P(X = g^{-1}(y)) = f_X(g^{-1}(y))$$
- **案例 2.8**：$X \sim \text{Poisson}(4)$，PMF 为 $f_X(x) = \frac{4^x e^{-4}}{x!}, x = 0, 1, 2, \dots$  
  令 $Y = \sqrt{X}$，则反函数为 $X = Y^2$。  
  $Y$ 的支撑集为 $\mathbb{Y} = \{0, 1, \sqrt{2}, \sqrt{3}, \dots\}$，其 PMF 直接为：
  $$f_Y(y) = f_X(y^2) = \frac{4^{y^2} e^{-4}}{(y^2)!}, \quad y \in \{0, 1, \sqrt{2}, \dots\}$$

---

## 6. 第四节：常见离散型随机变量分布 (2.4.1 Common Discrete Distributions)

### 6.1 离散均匀分布 (Discrete Uniform Distribution)
- **支撑集**：有限个等可能点 $\mathbb{X} = \{c_1, c_2, \dots, c_m\}$；
- **PMF**：$f(x) = \frac{1}{m}, \quad x \in \mathbb{X}$；
- **CDF**：$F(x) = \begin{cases} 0, & x < c_1 \\ \frac{k}{m}, & c_k \le x < c_{k+1} \\ 1, & x \ge c_m \end{cases}$。

---

### 6.2 伯努利分布 (Bernoulli Distribution)
- **记号**：$X \sim \text{Bernoulli}(p)$，参数 $p \in [0, 1]$；
- **试验模型**：单次二值试验（成功 1，失败 0）；
- **PMF 紧凑表达**：
  $$f(x) = p^x (1 - p)^{1 - x}, \quad x \in \{0, 1\}$$

---

### 6.3 二项分布 (Binomial Distribution)
- **记号**：$X \sim \text{Binomial}(n, p)$，参数 $n \in \mathbb{N}^+, p \in [0, 1]$；
- **物理模型**：$n$ 重独立伯努利试验中成功的总次数；
- **PMF 公式**：
  $$f(x) = \binom{n}{x} p^x (1 - p)^{n - x}, \quad x = 0, 1, 2, \dots, n$$
- **分布形态分析（课件图 12）**：
  - 当 $p = 0.5$ 时，二项分布呈现**关于中心点高度对称**的钟形；
  - 当 $p < 0.5$ 时，分布**右偏 (Right-skewed / 正偏)**，概率质量集中在左侧小数值区；
  - 当 $p > 0.5$ 时，分布**左偏 (Left-skewed / 负偏)**，概率质量集中在右侧大数值区。

---

### 6.4 负二项分布 (Negative Binomial) 与几何分布 (Geometric)
课件第 53 页给出了统计试验中“等待试验结束”的模型：

#### (1) 负二项分布（总试验次数定义）
- **物理模型**：在独立重复伯努利试验中，持续进行试验，**直到获得第 $r$ 次成功为止所需的总试验次数 $X$**；
- **支撑集**：$x = r, r+1, r+2, \dots$（至少需要做 $r$ 次试验）；
- **PMF 推导**：
  要在第 $x$ 次试验时恰好达成第 $r$ 次成功，必须满足：
  1. 前 $x - 1$ 次试验中恰好发生了 $r - 1$ 次成功（以及 $x - r$ 次失败），组合数方式为 $\binom{x-1}{r-1}$；
  2. 第 $x$ 次试验必定是成功（概率为 $p$）。
  结合独立性相乘：
  $$f(x) = \binom{x-1}{r-1} p^{r-1} (1-p)^{x-r} \times p = \binom{x-1}{r-1} p^r (1-p)^{x-r}, \quad x = r, r+1, \dots$$

> **【深度概念辨析：负二项分布的两种常见定义】**  
> - **定义 A（本课件采用）**：$X$ 为直到第 $r$ 次成功时的**总试验次数**，支撑集 $x \in \{r, r+1, \dots\}$；
> - **定义 B（部分教材与软件如 R/Python 采用）**：$Y$ 为直到第 $r$ 次成功前的**失败次数**，支撑集 $y \in \{0, 1, 2, \dots\}$，其关系为 $Y = X - r$。读者在查表或调用函数时务必注意区分！

#### (2) 几何分布 (Geometric Distribution)
- 当取 $r = 1$ 时，负二项分布退化为几何分布（等待第一次成功所需的试验次数）：
  $$f(x) = p (1 - p)^{x-1}, \quad x = 1, 2, 3, \dots$$

---

### 6.5 泊松分布 (Poisson Distribution)
- **记号**：$X \sim \text{Poisson}(\lambda)$，参数 $\lambda > 0$；
- **物理模型**：用于对在固定时间间隔或空间区域内稀疏随机事件的**发生次数 (Counts)** 建模（例如每小时到达售票处的顾客数、每卷铝合金表面的缺陷点数）；
- **PMF 公式**：
  $$f(k) = \frac{\lambda^k}{k!} e^{-\lambda}, \quad k = 0, 1, 2, \dots$$
- **归一化验证**：
  $$\sum_{k=0}^\infty f(k) = \sum_{k=0}^\infty \frac{\lambda^k}{k!} e^{-\lambda} = e^{-\lambda} \sum_{k=0}^\infty \frac{\lambda^k}{k!} = e^{-\lambda} \cdot e^\lambda = 1 \quad \blacksquare$$

---

### 6.6 泊松极限定理 (Poisson Theorem / 稀有事件定律)

#### (1) 定理表述 (定理 2.9)
设 $X_n \sim \text{Binomial}(n, p_n)$。若当试验次数 $n \to \infty$ 且单次成功率 $p_n \to 0$ 时，期望值保持收敛稳定：
$$\lim_{n \to \infty} n p_n = \lambda > 0$$
则对任意固定的非负整数 $k = 0, 1, 2, \dots$，二项分布概率逐点收敛于泊松分布概率：
$$\lim_{n \to \infty} \binom{n}{k} p_n^k (1 - p_n)^{n - k} = \frac{\lambda^k}{k!} e^{-\lambda}$$

#### (2) 严格数学证明
*严谨推导*：  
记 $p_n = \frac{\lambda_n}{n}$，其中 $\lim_{n \to \infty} \lambda_n = \lambda$。展开二项组合数：
$$\binom{n}{k} p_n^k (1 - p_n)^{n - k} = \frac{n(n-1)(n-2)\dots(n-k+1)}{k!} \left(\frac{\lambda_n}{n}\right)^k \left(1 - \frac{\lambda_n}{n}\right)^{n - k}$$
将其拆项重新组合：
$$= \frac{\lambda_n^k}{k!} \cdot \left[ \frac{n}{n} \cdot \frac{n-1}{n} \cdot \dots \cdot \frac{n-k+1}{n} \right] \cdot \left(1 - \frac{\lambda_n}{n}\right)^n \cdot \left(1 - \frac{\lambda_n}{n}\right)^{-k}$$
当 $n \to \infty$ 时分别考察各项极限（注意 $k$ 是固定的有限整数）：
1. $\lim_{n \to \infty} \frac{\lambda_n^k}{k!} = \frac{\lambda^k}{k!}$；
2. $\lim_{n \to \infty} \left[ 1 \cdot \left(1 - \frac{1}{n}\right) \dots \left(1 - \frac{k-1}{n}\right) \right] = 1 \times 1 \dots \times 1 = 1$；
3. 由重要微积分极限 $\lim_{n \to \infty} (1 - x/n)^n = e^{-x}$，得 $\lim_{n \to \infty} \left(1 - \frac{\lambda_n}{n}\right)^n = e^{-\lambda}$；
4. $\lim_{n \to \infty} \left(1 - \frac{\lambda_n}{n}\right)^{-k} = (1 - 0)^{-k} = 1$。
四项极限相乘，立即得到：
$$\lim_{n \to \infty} P(X_n = k) = \frac{\lambda^k}{k!} e^{-\lambda} \quad \blacksquare$$

#### (3) 实际计算中的近似指导法则（课件图 15 & 16）
- 课件第 59~60 页通过海量数值模拟线图与散点对比图阐明：  
  当 $n$ 较大且 $p$ 极小时（工程惯用标准为 $n \ge 30, p \le 0.1$，或 $n \ge 100, np \le 10$），复杂的二项式高阶组合数可以用简洁的泊松概率极高精度地近似替代。散点图完全重合在对角线上！

---

## 7. 第五节：常见连续型随机变量分布 (2.4.2 Common Continuous Distributions)

### 7.1 连续均匀分布 (Continuous Uniform Distribution)
- **记号**：$X \sim U(a, b), \quad a < b$；
- **PDF 与 CDF**：
  $$f(x) = \begin{cases} \frac{1}{b-a}, & a < x < b \\ 0, & \text{其他} \end{cases}, \qquad F(x) = \begin{cases} 0, & x < a \\ \frac{x-a}{b-a}, & a \le x < b \\ 1, & x \ge b \end{cases}$$

---

### 7.2 柯西分布 (Cauchy Distribution)
- **标准柯西分布**：$X \sim \text{Cauchy}(1, 0)$，PDF 为 $f(x) = \frac{1}{\pi(1+x^2)}, x \in \mathbb{R}$；
- **一般柯西分布**：$Y = aX + b$（尺度参数 $a > 0$，位置参数 $b \in \mathbb{R}$），记作 $Y \sim \text{Cauchy}(a, b)$：
  $$f_Y(y) = \frac{1}{a\pi \left[1 + \left(\frac{y-b}{a}\right)^2\right]}, \qquad F_Y(y) = \frac{1}{2} + \frac{1}{\pi} \arctan\left(\frac{y-b}{a}\right)$$

> **【深度补充解释 2：柯西分布的“病态”厚尾与矩不存在悖论】**  
> 课件第 65 页将标准柯西分布与标准正态分布 $N(0, 1)$ 的密度曲线进行了同图对比：
> 1. **厚尾特性 (Heavy Tails)**：正态分布的尾部按指数二次方衰减 $e^{-x^2/2}$，极快趋向于 0；而柯西分布的尾部按代数多项式倒数衰减 $\sim 1/x^2$。这意味着在柯西分布下，**发生极端异常值的概率远比正态分布高得多**！
> 2. **数学期望不存在**：由于 $\int_{-\infty}^{+\infty} \frac{|x|}{\pi(1+x^2)} dx = \infty$（被积函数按 $1/|x|$ 衰减，调和发散），柯西分布**连一阶数学期望（均值）都不存在**，更遑论方差！
> 3. 它作为中心极限定理失效的著名反例，在物理学（共振谱线 Breit-Wigner 分布）与稳健统计学中扮演着核心角色。

---

### 7.3 指数分布 (Exponential Distribution) 与无记忆性

#### (1) 基本定义
- **记号**：$X \sim \text{Exp}(\lambda)$，参数 $\lambda > 0$（事件到达率）；
- **物理模型**：泊松流中连续两次事件发生的等待时间间隔；
- **PDF 与 CDF**：
  $$f(x) = \lambda e^{-\lambda x}, \quad x > 0; \qquad F(x) = 1 - e^{-\lambda x}, \quad x \ge 0$$
- **生存函数 / 尾概率 (Survival Function)**：
  $$P(X > x) = 1 - F(x) = e^{-\lambda x}, \quad x \ge 0$$

#### (2) 无记忆性定理 (Memoryless Property, 定理 2.10)
课件第 70~72 页重点讲解了电子元件寿命案例（例 2.8）与无记忆性证明：

> **定理 2.10**：若 $X \sim \text{Exp}(\lambda)$，则对任意 $a, x \ge 0$，有：
> $$P(X > a + x \mid X > a) = P(X > x)$$

*严谨证明*：由条件概率公式与生存函数：
$$P(X > a + x \mid X > a) = \frac{P(X > a + x \cap X > a)}{P(X > a)} = \frac{P(X > a + x)}{P(X > a)} = \frac{e^{-\lambda(a + x)}}{e^{-\lambda a}} = e^{-\lambda x} = P(X > x) \quad \blacksquare$$

- **物理含义**：若一个元件的寿命服从指数分布，假设它已经无故障运行了 $a = 300$ 小时，它“还能再继续工作至少 $x = 600$ 小时”的条件概率，与一个“全新元件从 0 开始能工作 600 小时”的概率**完全一样**！元件没有任何“老化”或“磨损记忆”。
- **唯一性**：**指数分布是整个连续型分布家族中唯一具备无记忆性的分布**！（几何分布是离散家族中的唯一代表）。

---

### 7.4 伽马分布 (Gamma Distribution)
- **物理模型**：泊松过程中直到**第 $\alpha$ 次事件发生所需的总等待时间**；
- **记号**：$X \sim \text{Gamma}(\alpha, \lambda)$（形状参数 $\alpha > 0$，率参数 $\lambda > 0$）；
- **Gamma 函数**：$\Gamma(\alpha) = \int_0^\infty y^{\alpha-1} e^{-y} dy$。重要性质：$\Gamma(\alpha) = (\alpha - 1)\Gamma(\alpha - 1)$，若 $n$ 为正整数则 $\Gamma(n) = (n - 1)!$；
- **PDF 公式**：
  $$f(x) = \frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\lambda x}, \quad x > 0$$
- **CDF 与不完全 Gamma 函数**：
  $$F(x) = \frac{\gamma(\alpha, \lambda x)}{\Gamma(\alpha)}, \quad \text{其中 } \gamma(s, x) = \int_0^x t^{s-1} e^{-t} dt$$
- **退化关系**：当 $\alpha = 1$ 时，$\text{Gamma}(1, \lambda)$ 退化为**指数分布 $\text{Exp}(\lambda)$**。

---

### 7.5 卡方分布 (Chi-square Distribution) 作为 Gamma 分布特例
课件第 75 页指出：
当 Gamma 分布的形状参数取自由度的一半 $\alpha = n/2$，率参数取 $\lambda = 1/2$（或尺度 $\beta = 1/\lambda = 2$）时：
$$X \sim \text{Gamma}(n/2, 1/2) \implies X \sim \chi^2(n)$$
称 $X$ 服从自由度为 $n$ 的**卡方分布**。卡方分布是后续数理统计中样本方差分布与拟合优度检验的基础。

---

### 7.6 正态分布 (Normal Distribution) 与标准化变换

#### (1) 基本定义
- **记号**：$X \sim N(\mu, \sigma^2)$，位置参数（均值）$\mu \in \mathbb{R}$，尺度参数（标准差）$\sigma > 0$；
- **PDF 公式**：
  $$f(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x - \mu)^2}{2\sigma^2}}, \quad -\infty < x < \infty$$
- **标准正态分布**：当 $\mu = 0, \sigma = 1$ 时，记作 $Z \sim N(0, 1)$：
  $$\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}, \qquad \Phi(z) = \int_{-\infty}^z \phi(s) ds$$

#### (2) 标准化变换定理 (定理 2.11)

> **定理 2.11**：若 $X \sim N(\mu, \sigma^2)$，则线性变换：
> $$Z = \frac{X - \mu}{\sigma} \sim N(0, 1)$$
> 其 CDF 满足：$F_X(x) = \Phi\left(\frac{x - \mu}{\sigma}\right)$。

*严谨证明（利用定理 2.4 单调变量代换法）*：  
令 $Z = g(X) = \frac{X - \mu}{\sigma}$。  
反函数为 $x = g^{-1}(z) = \sigma z + \mu$，导数 $\frac{dx}{dz} = \sigma > 0$。  
由单调变换雅可比公式：
$$f_Z(z) = f_X(g^{-1}(z)) \left| \frac{dx}{dz} \right| = \left[ \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{((\sigma z + \mu) - \mu)^2}{2\sigma^2}} \right] \cdot \sigma = \frac{1}{\sqrt{2\pi}} e^{-z^2/2} = \phi(z) \quad \blacksquare$$

---

## 8. 核心公式速查与易错知识点深度辨析 (Summary & Pitfalls)

### 8.1 经典分布全景速查对照表

| 分布名称 | 类型 | 参数定义 | PMF / PDF 表达式 | 支撑集 $\mathbb{X}$ | 典型现实背景 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **离散均匀分布** | 离散 | $m$ 个点 | $f(x) = 1/m$ | $\{c_1, \dots, c_m\}$ | 掷骰子、抽签 |
| **伯努利分布** | 离散 | $p \in [0, 1]$ | $f(x) = p^x (1-p)^{1-x}$ | $\{0, 1\}$ | 单次抛硬币、质检 |
| **二项分布** | 离散 | $n \in \mathbb{N}^+, p$ | $f(x) = \binom{n}{x} p^x (1-p)^{n-x}$ | $\{0, 1, \dots, n\}$ | $n$ 重试验成功次数 |
| **负二项分布** | 离散 | $r \in \mathbb{N}^+, p$ | $f(x) = \binom{x-1}{r-1} p^r (1-p)^{x-r}$ | $\{r, r+1, \dots\}$ | 等待第 $r$ 次成功的试验次数 |
| **几何分布** | 离散 | $p \in [0, 1]$ | $f(x) = p(1-p)^{x-1}$ | $\{1, 2, \dots\}$ | 等待首次成功的试验次数 |
| **泊松分布** | 离散 | $\lambda > 0$ | $f(x) = \frac{\lambda^x}{x!} e^{-\lambda}$ | $\{0, 1, 2, \dots\}$ | 稀疏事件计数、排队论 |
| **连续均匀分布** | 连续 | $a < b$ | $f(x) = \frac{1}{b-a}$ | $(a, b)$ | 均匀误差、随机角 |
| **标准柯西分布** | 连续 | - | $f(x) = \frac{1}{\pi(1+x^2)}$ | $(-\infty, +\infty)$ | 旋转光斑、厚尾物理共振 |
| **指数分布** | 连续 | $\lambda > 0$ | $f(x) = \lambda e^{-\lambda x}$ | $(0, +\infty)$ | 电子元件寿命、无记忆等待 |
| **伽马分布** | 连续 | $\alpha, \lambda > 0$ | $f(x) = \frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\lambda x}$ | $(0, +\infty)$ | 等待第 $\alpha$ 次事件发生的时间 |
| **卡方分布** | 连续 | 自由度 $n$ | $\text{Gamma}(n/2, 1/2)$ | $(0, +\infty)$ | 样本方差分布、拟合优度 |
| **正态分布** | 连续 | $\mu, \sigma^2$ | $f(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $(-\infty, +\infty)$ | 测量误差、海量微小扰动叠加 |

---

### 8.2 核心易错点与解题陷阱深度辨析

#### 辨析 1：连续变量代换是否能直接代入？雅可比项的本质为何？
- **常见错误**：许多学生在求 $Y = g(X)$ 的密度时，直接把反函数代入原密度：$f_Y(y) = f_X(g^{-1}(y))$（遗漏了导数项！）；
- **正确法则**：根据概率守恒原理，微元区间内的概率必须相等：
  $$P(y \le Y \le y + dy) = P(x \le X \le x + dx) \implies f_Y(y) |dy| = f_X(x) |dx|$$
  所以必有 $f_Y(y) = f_X(x) \left|\frac{dx}{dy}\right|$！只有当 $X$ 是离散型时，因 $f(x)$ 是纯概率点质量，才可以直接代入。

#### 辨析 2：负二项分布定义混淆陷阱
- 考试中必须审清题目问的是**“总试验次数 $X$”** 还是 **“失败次数 $Y$”**：
  - 若为总次数，支撑集从 $r$ 开始，公式为 $\binom{x-1}{r-1} p^r (1-p)^{x-r}$；
  - 若为失败次数，支撑集从 $0$ 开始，公式为 $\binom{y+r-1}{y} p^r (1-p)^y$。

#### 辨析 3：连续型单点概率为 0 与可能发生的矛盾
- 在连续型分布中，$P(X = x_0) = 0$ 对任何确定的实数点 $x_0$ 均成立。但这绝不代表事件 $\{X = x_0\}$ 是不可能事件 $\emptyset$。
- 测度论解释：单点集的 Lebesgue 测度为 0，因而概率测度为 0。任何一次试验总会落出某个具体的实数点，这体现了“概率为 0 的事件依然可能发生”。
