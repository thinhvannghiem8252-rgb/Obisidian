# Math1212 概率论与数理统计 I (Probability and Statistics I)

## 第四章：随机变量的数字特征 课程讲义全景精要与深度解析笔记

> **课件来源**：`week7_1.pdf`，*Numerical Characteristics of Random Variables — Chapter 4*，共 94 页。  
> **编排方式**：按知识点及其逻辑联系重组，不按课件页码逐页复述。  
> **笔记格式**：沿用第二章笔记的中英双语标题、分级编号、定义与定理引用块、详细证明、案例解析、深度辨析和公式速查结构。  
> **内容边界**：标注“深度补充”的内容用于解释或连接知识点，不表示课件已完整讲授。课件目录列出 4.4 二维正态分布，但第 73—74 页主要是引入性应用，随后进入条件期望。  
> **参考教材（按本章课件第 2 页）**：
> 1. Robert V. Hogg, Elliot A. Tanis, Dale Zimmerman, *Probability and Statistical Inference* (9th/10th ed.), Sections 2.2, 3.1, 4.2, 5.3, 5.4, 5.5。
> 2. 魏宗舒 等，《概率论与数理统计教程》（第三版），Sections 2.4, 2.5, 2.6, 3.5。

---

## 目录与知识架构

1. **引言：为什么要研究数字特征？(Motivation & Conceptual Framework)**
   - 1.1 从完整分布到关键数值
   - 1.2 本章的知识联系与统一记号
   - 1.3 参数约定、存在条件与“几乎必然”
2. **数学期望及其运算法则 (Expectation & Its Properties)**
   - 2.1 期望的定义、直观意义与存在条件
   - 2.2 随机变量函数的期望：定理 4.1
   - 2.3 示性变量：概率就是一种期望
   - 2.4 线性性与独立乘积公式：定理 4.3—4.4
   - 2.5 二元函数的期望与交叉矩
3. **方差、标准差与矩 (Variance, Standard Deviation & Moments)**
   - 3.1 方差与标准差的定义
   - 3.2 方差计算公式与线性变换：定理 4.5
   - 3.3 原点矩、中心矩与存在性关系
   - 3.4 常见分布的均值与方差推导
   - 3.5 分布参数与数字特征速查表
4. **矩母函数：生成矩与识别分布 (Moment-generating Functions, MGF)**
   - 4.1 定义与零点邻域的存在条件
   - 4.2 求导生成矩：定理 4.6
   - 4.3 泊松、指数、正态与二项分布的 MGF
   - 4.4 唯一性定理：定理 4.7
   - 4.5 仿射变换与独立和：定理 4.8 及推论 4.8A
5. **分布运算：独立和、最小值与平方变换 (Distributional Operations)**
   - 5.1 分布可加性的统一证明方法
   - 5.2 伯努利、二项、泊松、Gamma 与卡方的可加性
   - 5.3 指数变量之和与最小值的本质区别
   - 5.4 独立正态变量的线性组合
   - 5.5 正态标准化与标准正态平方
6. **协方差与相关系数 (Covariance & Correlation)**
   - 6.1 协方差的定义、意义与双线性性
   - 6.2 一般线性组合的方差：推论 4.11
   - 6.3 相关系数的界与等号条件
   - 6.4 例 4.8：联合分布表求相关系数
   - 6.5 独立与不相关：离散、连续两个反例
7. **正态模型与联合正态的作用 (Normal Models & Joint Normality)**
   - 7.1 正态概率计算与分位数
   - 7.2 灌装量质量控制例题
   - 7.3 边缘正态不足以确定联合关系
   - 7.4 相关正态变量的线性组合例题
   - 7.5 深度补充：二维正态的结构与条件分布
8. **条件期望与全期望公式 (Conditional & Total Expectation)**
   - 8.1 普通期望、给定取值的条件期望、随机条件期望
   - 8.2 离散型与连续型计算流程
   - 8.3 条件期望的代数性质
   - 8.4 全期望公式及证明
   - 8.5 两台机器与离散联合分布的完整案例
9. **条件方差、全方差与分层模型 (Conditional Variance & Hierarchical Models)**
   - 9.1 条件方差与全方差公式
   - 9.2 两阶段均匀模型的完整计算
   - 9.3 随机成功概率二项模型的均值、方差和边缘分布
   - 9.4 条件独立与无条件依赖的区别
10. **最优预测：线性预测与条件期望 (Optimal Prediction)**
    - 10.1 最佳线性预测的公式与配方证明
    - 10.2 相关系数与最小均方误差
    - 10.3 二元离散预测案例
    - 10.4 深度补充：条件期望是最佳一般均方预测
11. **核心公式速查与易错知识点深度辨析 (Summary & Pitfalls)**
    - 11.1 公式、条件和用途对照表
    - 11.2 高频错误与概念边界
    - 11.3 按题型选择方法
    - 11.4 自测题与答案核对

---

## 1. 引言：为什么要研究数字特征？(Motivation & Conceptual Framework)

### 1.1 从完整分布到关键数值

第二章主要解决“随机变量服从什么分布”，通过 PMF、PDF 和 CDF 描述全部概率信息。本章进一步研究：能否用几个重要数值，概括分布最值得关注的特征？

- **数学期望 (Expectation)**：取值的平均水平在哪里？
- **方差与标准差 (Variance & Standard Deviation)**：取值围绕平均水平波动多大？
- **矩 (Moments)**：如何用更一般的幂次平均描述分布？
- **协方差与相关系数 (Covariance & Correlation)**：两个变量是否有同向或反向的线性变化倾向？
- **条件期望与条件方差 (Conditional Expectation & Variance)**：已知额外信息后，平均值和剩余波动如何改变？

> **【核心概念辨析：数字特征不等于完整分布】**  
> 均值、方差相同的变量，可以具有完全不同的分布。仅凭 $E(X)$ 和 $\operatorname{Var}(X)$，一般无法计算任意区间概率。只有在分布族等额外信息已知时，参数才能进一步确定分布。例如，已知属于正态分布族后，均值与方差才确定该正态分布。

### 1.2 本章的知识联系与统一记号

本章的主要联系为：

$$\text{分布}\longrightarrow\text{期望}\longrightarrow\text{矩、方差、协方差}$$

$$\text{MGF}\longrightarrow\text{生成矩、识别分布、研究独立和}$$

$$\text{条件分布}\longrightarrow\text{条件期望与条件方差}\longrightarrow\text{总体特征与预测}$$

统一使用：

$$\mu_X=E(X),\qquad \sigma_X^2=\operatorname{Var}(X)=D(X),\qquad \sigma_X=\operatorname{sd}(X).$$

离散概率质量函数记为 $p_X(x)$，连续概率密度记为 $f_X(x)$，避免混淆单点概率与密度。

### 1.3 参数约定、存在条件与“几乎必然”

课件第 4 页明确规定：

1. 有限期望要求绝对可积：$E|X|<\infty$。
2. 方差、协方差公式在有关二阶矩有限时使用。
3. 几何分布取值为 $1,2,\ldots$，表示首次成功所需的**总试验次数**。
4. 指数分布、Gamma 分布均采用**速率参数** $\lambda$。
5. 讨论高斯向量时，方差为零的正态分布解释为点质量，即常数随机变量。

> **【参数衔接：第二章笔记与本章 Gamma 记号】**  
> 第二章笔记的不同案例出现了尺度参数 $\theta$ 与速率参数 $\lambda$。二者满足 $\theta=1/\lambda$。本章统一写作 $\operatorname{Gamma}(\alpha,\lambda)$，密度为
> $$f(x)=\frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\lambda x},\qquad x>0.$$
> 因此 $E(X)=\alpha/\lambda$、$\operatorname{Var}(X)=\alpha/\lambda^2$；若使用尺度参数，则对应 $\alpha\theta$、$\alpha\theta^2$。

“几乎必然 (Almost Surely, a.s.)”表示以概率 $1$ 成立。例如 $X=c$ a.s. 表示 $P(X=c)=1$，允许在零概率事件上有不同取值。

---

## 2. 数学期望及其运算法则 (Expectation & Its Properties)

### 2.1 期望的定义、直观意义与存在条件

对应课件第 6 页。

> **定义（数学期望, Expectation）**：设 $E|X|<\infty$。离散型与连续型随机变量的数学期望分别为：
> $$E(X)=\sum_x x p_X(x),\qquad E(X)=\int_{\mathbb R}x f_X(x)\,dx.$$

**直观意义**：按取值出现的概率对取值加权平均。

例如公平骰子：

$$E(X)=\sum_{k=1}^{6}k\frac16=\frac72.$$

虽然骰子不会出现 $3.5$ 点，但期望可以是 $3.5$。因此，期望不必属于随机变量的取值集合，也不等于最可能出现的取值。

#### 为什么要求绝对可积？

连续型要求：

$$\int_{\mathbb R}|x|f_X(x)\,dx<\infty.$$

离散型要求：

$$\sum_x|x|p_X(x)<\infty.$$

绝对可积保证正负部分都有限，防止出现 $\infty-\infty$；离散型的绝对收敛还使求和结果不依赖排列顺序。

> **【深度辨析：对称不自动意味着均值为零】**  
> 关于零对称且可积的分布，均值才为零。标准柯西密度 $1/[\pi(1+x^2)]$ 虽然对称，但 $\int |x|/[\pi(1+x^2)]\,dx$ 发散，所以普通意义下的期望不存在。对称截断积分为零只说明柯西主值为零，不能替代期望的存在性。

### 2.2 随机变量函数的期望：定理 4.1

对应课件第 7 页。

> **定理 4.1（随机变量函数的期望）**：若 $g$ 可测且 $E|g(X)|<\infty$，则：
> $$E[g(X)]=\begin{cases}\displaystyle\sum_x g(x)p_X(x),&X\text{ 离散},\\[5pt]\displaystyle\int_{\mathbb R}g(x)f_X(x)\,dx,&X\text{ 连续}.\end{cases}$$

**实际价值**：求 $E[g(X)]$ 时，不必先求新变量 $g(X)$ 的分布。

例如 $X\sim U(0,1)$：

$$E(X^2)=\int_0^1x^2\,dx=\frac13.$$

而：

$$[E(X)]^2=\left(\int_0^1x\,dx\right)^2=\frac14.$$

因此一般有 $E[g(X)]\ne g(E(X))$。只有线性函数等特定情形才可直接交换。

### 2.3 示性变量：概率就是一种期望

对应课件第 8—9 页，推论 4.2。

定义事件 $A$ 的示性变量：

$$I_A=\begin{cases}1,&A\text{ 发生},\\0,&A\text{ 不发生}.\end{cases}$$

由期望定义：

$$\boxed{E(I_A)=P(A).}$$

课件的写法 $\mathbf1_A(X)$ 表示判断 $X$ 是否落在集合 $A$ 中，于是：

$$E[\mathbf1_A(X)]=P(X\in A).$$

连续型证明：

$$E[\mathbf1_A(X)]=\int_{\mathbb R}\mathbf1_A(x)f_X(x)\,dx=\int_Af_X(x)\,dx=P(X\in A).\quad\blacksquare$$

**计数问题的应用**：若 $N=\sum_{i=1}^nI_{A_i}$ 统计事件发生总次数，则：

$$\boxed{E(N)=\sum_{i=1}^nP(A_i).}$$

不要求这些事件独立。复杂计数问题若难以求出 $N$ 的分布，先拆成示性变量往往更容易。

### 2.4 线性性与独立乘积公式：定理 4.3—4.4

对应课件第 10 页。

> **定理 4.3（期望的线性性）**：对可积随机变量和常数 $a_i,b$，
> $$E\left(b+\sum_{i=1}^na_iX_i\right)=b+\sum_{i=1}^na_iE(X_i).$$
> **不要求独立。**

> **定理 4.4（独立变量的乘积期望）**：若 $X_1,\ldots,X_n$ 相互独立，且各 $g_i(X_i)$ 可积，则：
> $$E\left[\prod_{i=1}^ng_i(X_i)\right]=\prod_{i=1}^nE[g_i(X_i)].$$

对两个离散型独立变量，证明为：

$$\begin{aligned}E[g(X)h(Y)]&=\sum_x\sum_y g(x)h(y)p_{X,Y}(x,y)\\&=\sum_x\sum_y g(x)h(y)p_X(x)p_Y(y)\\&=\left[\sum_xg(x)p_X(x)\right]\left[\sum_yh(y)p_Y(y)\right].\end{aligned}$$

关键一步是独立性给出的联合分布分解。连续型将求和换成积分即可。

> **【核心辨析：加法与乘法的条件不同】**  
> $E(X+Y)=E(X)+E(Y)$ 在可积时总成立；$E(XY)=E(X)E(Y)$ 一般不能直接使用，独立是保证它成立的充分条件。反过来，仅一个乘积期望等式成立，并不能推出独立。

### 2.5 二元函数的期望与交叉矩

对应课件第 51 页。

当 $g(X,Y)$ 可积时：

$$E[g(X,Y)]=\sum_x\sum_y g(x,y)p_{X,Y}(x,y)$$

或：

$$E[g(X,Y)]=\iint_{\mathbb R^2}g(x,y)f_{X,Y}(x,y)\,dx\,dy.$$

特别地，取 $g(x,y)=xy$ 得交叉矩：

$$E(XY)=\sum_x\sum_yxy\,p_{X,Y}(x,y).$$

这是协方差计算的关键中间量。仅有边缘分布通常无法确定 $E(XY)$，因为它还反映变量之间的依赖。

---

## 3. 方差、标准差与矩 (Variance, Standard Deviation & Moments)

### 3.1 方差与标准差的定义

对应课件第 11 页。

> **定义（方差与标准差）**：设 $E(X^2)<\infty$，$\mu=E(X)$，则：
> $$\operatorname{Var}(X)=E[(X-\mu)^2],\qquad \operatorname{sd}(X)=\sqrt{\operatorname{Var}(X)}.$$

偏差直接求平均得到零：$E(X-\mu)=0$，因此采用平方偏差衡量波动。平方避免正负抵消，并使较大偏差获得更大权重。

例如 $X$ 等概率取 $49,51$，$Y$ 等概率取 $0,100$。二者均值都为 $50$，但：

$$\operatorname{Var}(X)=1,\qquad \operatorname{Var}(Y)=2500.$$

若原变量以 mL 计量，方差单位是 $\text{mL}^2$，标准差单位仍是 mL。

### 3.2 方差计算公式与线性变换：定理 4.5

对应课件第 11—12 页。

> **定理 4.5**：
> $$\boxed{\operatorname{Var}(X)=E(X^2)-[E(X)]^2}$$
> $$\boxed{\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X).}$$

#### (1) 方差计算公式的证明

$$\begin{aligned}E[(X-\mu)^2]&=E(X^2)-2\mu E(X)+\mu^2\\&=E(X^2)-\mu^2.\end{aligned}\quad\blacksquare$$

#### (2) 线性变换的证明

$$aX+b-E(aX+b)=a(X-\mu).$$

两边平方再取期望即得方差公式。相应地：

$$\operatorname{sd}(aX+b)=|a|\operatorname{sd}(X).$$

**直观解释**：平移不改变离散程度；放大 $a$ 倍使平方偏差放大 $a^2$ 倍。

#### (3) 零方差与常数变量

非负随机变量 $(X-\mu)^2$ 的期望为零，当且仅当它几乎必然为零。因此：

$$\boxed{\operatorname{Var}(X)=0\iff X=E(X)\text{ a.s.}}$$

### 3.3 原点矩、中心矩与存在性关系

对应课件第 22—23 页。

> **定义（矩, Moments）**：当相应绝对矩有限时，$r$ 阶原点矩为 $E(X^r)$，$r$ 阶中心矩为 $E[(X-\mu)^r]$。

| 名称 | 公式 | 含义 |
| :--- | :--- | :--- |
| 一阶原点矩 | $E(X)$ | 均值 |
| 二阶原点矩 | $E(X^2)$ | 计算方差的基础 |
| 一阶中心矩 | $E(X-\mu)=0$ | 平均偏差为零 |
| 二阶中心矩 | $E[(X-\mu)^2]$ | 方差 |

若 $0<k<r$，因为 $|x|^k\le1+|x|^r$，所以：

$$\boxed{E|X|^r<\infty\implies E|X|^k<\infty.}$$

特别地，有限二阶矩保证有限一阶绝对矩。反向推理一般不成立。

### 3.4 常见分布的均值与方差推导

对应课件练习 4.1，第 13—17 页。

#### (1) 伯努利分布：利用 $X^2=X$

若 $X\sim\operatorname{Bernoulli}(p)$，则：

$$E(X)=0(1-p)+1p=p.$$

由于 $X\in\{0,1\}$，有 $X^2=X$，故：

$$\boxed{\operatorname{Var}(X)=p-p^2=p(1-p).}$$

#### (2) 二项分布：利用示性变量分解

若 $X=\sum_{i=1}^nX_i$，其中 $X_i$ 相互独立且均服从 $\operatorname{Bernoulli}(p)$，则：

$$E(X)=\sum_{i=1}^nE(X_i)=np.$$

独立使协方差为零，因此：

$$\boxed{\operatorname{Var}(X)=\sum_{i=1}^n\operatorname{Var}(X_i)=np(1-p).}$$

注意期望相加本身不需要独立，而上述方差简化使用了独立性。

#### (3) 几何分布：对几何级数求导

设 $0<p<1$，$q=1-p$，$P(X=k)=pq^{k-1}$，$k\ge1$。由：

$$\sum_{k=0}^\infty q^k=\frac1{1-q},$$

对 $q$ 求导：

$$E(X)=p\sum_{k=1}^\infty kq^{k-1}=p\frac{d}{dq}\frac1{1-q}=\frac1p.$$

求二阶矩时，先计算阶乘形式：

$$E[X(X-1)]=pq\frac{d^2}{dq^2}\frac1{1-q}=\frac{2q}{p^2}.$$

利用 $X^2=X(X-1)+X$：

$$E(X^2)=\frac{2q}{p^2}+\frac1p=\frac{2-p}{p^2}.$$

最终：

$$\boxed{\operatorname{Var}(X)=\frac{2-p}{p^2}-\frac1{p^2}=\frac{1-p}{p^2}.}$$

$p=1$ 时 $X=1$ a.s.，上述均值和方差公式仍成立；$p=0$ 时不能作为有限首次成功时间的这一几何模型。

#### (4) 指数分布：分部积分

若 $X\sim\operatorname{Exp}(\lambda)$，$\lambda>0$，则：

$$\begin{aligned}E(X)&=\int_0^\infty x\lambda e^{-\lambda x}\,dx\\&=[-xe^{-\lambda x}]_0^\infty+\int_0^\infty e^{-\lambda x}\,dx=\frac1\lambda.\end{aligned}$$

同理：

$$E(X^2)=[-x^2e^{-\lambda x}]_0^\infty+2\int_0^\infty xe^{-\lambda x}\,dx=\frac2{\lambda^2}.$$

所以：

$$\boxed{\operatorname{Var}(X)=\frac1{\lambda^2}.}$$

#### (5) 正态分布：标准化与分部积分

写作 $X=\mu+\sigma Z$，其中 $Z\sim N(0,1)$。设标准正态密度为 $\phi(z)$，则：

$$\phi'(z)=-z\phi(z).$$

对称性与可积性给出 $E(Z)=0$。再由分部积分：

$$\begin{aligned}E(Z^2)&=\int_{\mathbb R}z^2\phi(z)\,dz=-\int_{\mathbb R}z\phi'(z)\,dz\\&=[-z\phi(z)]_{-\infty}^{+\infty}+\int_{\mathbb R}\phi(z)\,dz=1.\end{aligned}$$

因此：

$$\boxed{E(X)=\mu,\qquad \operatorname{Var}(X)=\sigma^2.}$$

### 3.5 分布参数与数字特征速查表

对应课件第 14、18—19 页。

| 分布 | 参数与约定 | 期望 | 方差 |
| :--- | :--- | :--- | :--- |
| 点质量 $X=a$ | 常数 $a$ | $a$ | $0$ |
| $\operatorname{Bernoulli}(p)$ | $0\le p\le1$ | $p$ | $p(1-p)$ |
| $\operatorname{Binomial}(n,p)$ | $n$ 次独立同成功率试验 | $np$ | $np(1-p)$ |
| $\operatorname{Geometric}(p)$ | $0<p\le1$，支撑从 $1$ 开始 | $1/p$ | $(1-p)/p^2$ |
| $\operatorname{Poisson}(\lambda)$ | $\lambda>0$ | $\lambda$ | $\lambda$ |
| $U(a,b)$ | $a<b$ | $(a+b)/2$ | $(b-a)^2/12$ |
| $\operatorname{Exp}(\lambda)$ | 速率 $\lambda>0$ | $1/\lambda$ | $1/\lambda^2$ |
| $\operatorname{Gamma}(\alpha,\lambda)$ | 形状、速率均为正 | $\alpha/\lambda$ | $\alpha/\lambda^2$ |
| $N(\mu,\sigma^2)$ | 第二参数为方差 | $\mu$ | $\sigma^2$ |
| $\chi^2(n)$ | 自由度 $n$ | $n$ | $2n$ |
| $t(\nu)$ | 自由度 $\nu>0$ | $0$，要求 $\nu>1$ | $\nu/(\nu-2)$，要求 $\nu>2$ |

> **【存在条件不能漏记】**  
> $t$ 分布在 $\nu\le1$ 时均值不存在，在 $\nu\le2$ 时没有有限方差。不能忽略条件后机械代入 $\nu/(\nu-2)$，得到负数“方差”。

---

## 4. 矩母函数：生成矩与识别分布 (Moment-generating Functions, MGF)

### 4.1 定义与零点邻域的存在条件

对应课件第 21—22 页。

> **定义（矩母函数, MGF）**：
> $$M_X(t)=E(e^{tX}).$$
> 本章所用的 MGF 理论要求存在 $h>0$，使得 $M_X(t)$ 在整个 $(-h,h)$ 内有限。

离散与连续表达式：

$$M_X(t)=\sum_xe^{tx}p_X(x),\qquad M_X(t)=\int_{\mathbb R}e^{tx}f_X(x)\,dx.$$

任何随机变量均满足 $E(e^{0X})=1$，但这不足以保证 MGF 在零点邻域有限。另一方面，MGF 不必在整个实数轴上有限。

> **【深度补充：MGF 为什么能同时管理很多矩？】**  
> $e^{tx}$ 的幂级数为 $1+tx+t^2x^2/2!+\cdots$。在零点附近具有足够可积性时，$M_X(t)$ 的导数提取相应的幂次平均。严格论证不能只形式化地交换无穷求和、积分与求导；零点邻域内的有限性提供了相应控制。

### 4.2 求导生成矩：定理 4.6

对应课件第 23—24 页。

> **定理 4.6（Generating Moments）**：若 MGF 在零点邻域内有限，则各阶原点矩存在，并且：
> $$\boxed{M_X^{(r)}(0)=E(X^r).}$$

**证明思路**：

$$\frac{d^r}{dt^r}e^{tx}=x^re^{tx}.$$

在可交换求导与期望的条件下：

$$M_X^{(r)}(t)=E(X^re^{tX}).$$

令 $t=0$，即得结论。$\blacksquare$

因此：

$$\boxed{E(X)=M_X'(0),\qquad E(X^2)=M_X''(0)}$$

$$\boxed{\operatorname{Var}(X)=M_X''(0)-[M_X'(0)]^2.}$$

计算前可用 $M_X(0)=1$ 检查表达式；若不等于 $1$，则一定有误，但等于 $1$ 并不能证明全部计算正确。

### 4.3 泊松、指数、正态与二项分布的 MGF

#### (1) 泊松分布：识别指数函数级数

对应课件第 25—26 页。若 $X\sim\operatorname{Poisson}(\lambda)$：

$$\begin{aligned}M_X(t)&=\sum_{k=0}^\infty e^{tk}e^{-\lambda}\frac{\lambda^k}{k!}\\&=e^{-\lambda}\sum_{k=0}^\infty\frac{(\lambda e^t)^k}{k!}\\&=\boxed{\exp[\lambda(e^t-1)]},\qquad t\in\mathbb R.\end{aligned}$$

求导：

$$M_X'(t)=\lambda e^tM_X(t),\qquad M_X''(t)=(\lambda e^t+\lambda^2e^{2t})M_X(t).$$

所以：

$$E(X)=\lambda,\quad E(X^2)=\lambda+\lambda^2,\quad \operatorname{Var}(X)=\lambda.$$

#### (2) 指数分布：必须注明收敛范围

对应课件第 27 页。

$$M_X(t)=\lambda\int_0^\infty e^{-(\lambda-t)x}\,dx=\boxed{\frac{\lambda}{\lambda-t}},\qquad t<\lambda.$$

当 $t\ge\lambda$ 时积分发散。求导得到：

$$M_X'(t)=\frac{\lambda}{(\lambda-t)^2},\qquad M_X''(t)=\frac{2\lambda}{(\lambda-t)^3}.$$

于是 $E(X)=1/\lambda$，$E(X^2)=2/\lambda^2$，$\operatorname{Var}(X)=1/\lambda^2$。

#### (3) 正态分布：配方后识别一个密度积分

对应课件第 28—29 页。若 $X\sim N(\mu,\sigma^2)$，$\sigma>0$，配方：

$$tx-\frac{(x-\mu)^2}{2\sigma^2}=-\frac{[x-(\mu+\sigma^2t)]^2}{2\sigma^2}+\mu t+\frac{\sigma^2t^2}{2}.$$

因此：

$$M_X(t)=e^{\mu t+\sigma^2t^2/2}\int_{\mathbb R}\frac1{\sqrt{2\pi}\sigma}e^{-[x-(\mu+\sigma^2t)]^2/(2\sigma^2)}\,dx.$$

积分内是均值为 $\mu+\sigma^2t$、方差为 $\sigma^2$ 的正态密度，其全积分等于 $1$：

$$\boxed{M_X(t)=e^{\mu t+\sigma^2t^2/2},\qquad t\in\mathbb R.}$$

求导：

$$M_X'(t)=(\mu+\sigma^2t)M_X(t),$$

$$M_X''(t)=[(\mu+\sigma^2t)^2+\sigma^2]M_X(t).$$

于是：

$$E(X)=\mu,\qquad E(X^2)=\mu^2+\sigma^2,\qquad \operatorname{Var}(X)=\sigma^2.$$

#### (4) 二项分布：使用二项式定理

对应练习 4.4，第 35—36 页。若 $Y\sim\operatorname{Binomial}(n,p)$：

$$\begin{aligned}M_Y(t)&=\sum_{y=0}^ne^{ty}\binom ny p^y(1-p)^{n-y}\\&=\sum_{y=0}^n\binom ny(pe^t)^y(1-p)^{n-y}\\&=\boxed{(1-p+pe^t)^n},\qquad t\in\mathbb R.\end{aligned}$$

当 $n=1$ 时，得到伯努利 MGF：$1-p+pe^t$。

### 4.4 唯一性定理：定理 4.7

对应课件第 30 页。

> **定理 4.7（Uniqueness）**：设 $M_X,M_Y$ 在某个共同区间 $(-h,h)$ 内有限，且该区间中处处有 $M_X(t)=M_Y(t)$，则 $X,Y$ 同分布。

**方法论**：先求未知变量的 MGF，再与熟悉分布的 MGF 匹配，最后引用唯一性。

**注意**：同分布不等于 $X=Y$，也不意味着独立；只表示两者具有相同的概率分布。

### 4.5 仿射变换与独立和：定理 4.8 及推论 4.8A

对应课件第 31—34 页。

> **推论 4.8A（仿射变换）**：若 $Y=aX+b$，则：
> $$\boxed{M_Y(t)=e^{bt}M_X(at).}$$

证明：$E[e^{t(aX+b)}]=e^{bt}E(e^{atX})$。$\blacksquare$

> **定理 4.8（独立线性组合）**：若 $X_1,\ldots,X_n$ 相互独立且 MGF 在零点附近有限，则在各因子有限的范围内：
> $$\boxed{M_{b+\sum_ia_iX_i}(t)=e^{bt}\prod_iM_{X_i}(a_it).}$$

证明的核心：

$$E\left[e^{t\sum_i a_iX_i}\right]=E\left[\prod_i e^{ta_iX_i}\right]=\prod_iE(e^{ta_iX_i}).$$

最后一步使用相互独立，不能只凭两两不相关使用此公式。

---

## 5. 分布运算：独立和、最小值与平方变换 (Distributional Operations)

### 5.1 分布可加性的统一证明方法

对应课件第 37—46 页。

设 $S=\sum_iX_i$，变量相互独立。步骤为：

1. 写出每个 $M_{X_i}(t)$ 与其有限范围。
2. 用独立性得到 $M_S(t)=\prod_iM_{X_i}(t)$。
3. 整理成某个已知分布的 MGF。
4. 说明零点附近有限，并引用唯一性。

这比仅计算均值、方差更强：它确定了 $S$ 的完整分布。

### 5.2 伯努利、二项、泊松、Gamma 与卡方的可加性

#### (1) 练习 4.5：独立同参数伯努利变量之和

若 $X_i\sim\operatorname{Bernoulli}(p)$ 相互独立：

$$M_S(t)=\prod_{i=1}^n(1-p+pe^t)=(1-p+pe^t)^n.$$

所以：

$$\boxed{S\sim\operatorname{Binomial}(n,p).}$$

#### (2) 练习 4.6：同成功率二项变量之和

若 $X_i\sim\operatorname{Binomial}(n_i,p)$ 相互独立：

$$M_S(t)=\prod_i(1-p+pe^t)^{n_i}=(1-p+pe^t)^{\sum_i n_i}.$$

所以：

$$\boxed{S\sim\operatorname{Binomial}\left(\sum_i n_i,p\right).}$$

不同成功概率时，该乘积通常无法合并为单一二项分布形式。

#### (3) 定理 4.9：独立和的分布汇总

| 各变量分布 | 和的分布 | 必要使用条件 |
| :--- | :--- | :--- |
| $\operatorname{Poisson}(\lambda_i)$ | $\operatorname{Poisson}(\sum_i\lambda_i)$ | 相互独立 |
| $\operatorname{Binomial}(n_i,p)$ | $\operatorname{Binomial}(\sum_i n_i,p)$ | 相互独立、相同 $p$ |
| $\operatorname{Gamma}(\alpha_i,\lambda)$ | $\operatorname{Gamma}(\sum_i\alpha_i,\lambda)$ | 相互独立、相同速率 |
| $\chi^2(n_i)$ | $\chi^2(\sum_i n_i)$ | 相互独立 |
| $N(\mu_i,\sigma_i^2)$ | $N(\sum_i\mu_i,\sum_i\sigma_i^2)$ | 相互独立 |

例如 Gamma 一行的计算是：

$$\prod_i\left(\frac\lambda{\lambda-t}\right)^{\alpha_i}=\left(\frac\lambda{\lambda-t}\right)^{\sum_i\alpha_i},\qquad t<\lambda.$$

卡方分布是 $\operatorname{Gamma}(n/2,1/2)$，所以自由度相加来自形状参数相加。

### 5.3 指数变量之和与最小值的本质区别

对应课件第 47—49 页。

#### (1) 相同速率的和：Gamma 分布

若 $X_1,\ldots,X_n\overset{\mathrm{iid}}\sim\operatorname{Exp}(\lambda)$，则：

$$M_{\sum_iX_i}(t)=\left(\frac\lambda{\lambda-t}\right)^n.$$

由唯一性：

$$\boxed{\sum_{i=1}^nX_i\sim\operatorname{Gamma}(n,\lambda).}$$

因此均值为 $n/\lambda$，方差为 $n/\lambda^2$。除单个变量等特殊情形外，和不再是指数分布。

#### (2) 不同速率的最小值：速率相加

若 $X_i\sim\operatorname{Exp}(\lambda_i)$ 相互独立，令 $W=\min_iX_i$。当 $w\ge0$：

$$\begin{aligned}P(W>w)&=P(X_1>w,\ldots,X_n>w)\\&=\prod_iP(X_i>w)\\&=\prod_i e^{-\lambda_iw}=e^{-w\sum_i\lambda_i}.\end{aligned}$$

故：

$$\boxed{W\sim\operatorname{Exp}\left(\sum_i\lambda_i\right).}$$

当 $w<0$ 时，$P(W>w)=1$，与非负支撑一致。

> **【模型辨析：依次完成与最先发生】**  
> 求和对应依次经历多个等待阶段；最小值对应同时等待多个事件中最先发生的那个。相同速率的独立和改变 Gamma 的形状参数；独立最小值将指数速率相加。两种规则不能交换使用。

### 5.4 独立正态变量的线性组合

对应课件第 41—42 页。

若 $X_i\sim N(\mu_i,\sigma_i^2)$ 相互独立，令 $Y=b+\sum_i a_iX_i$，则：

$$\begin{aligned}M_Y(t)&=e^{bt}\prod_i\exp\left(a_i\mu_it+\frac12a_i^2\sigma_i^2t^2\right)\\&=\exp\left[\left(b+\sum_i a_i\mu_i\right)t+\frac12\left(\sum_i a_i^2\sigma_i^2\right)t^2\right].\end{aligned}$$

识别为正态 MGF：

$$\boxed{Y\sim N\left(b+\sum_i a_i\mu_i,\sum_i a_i^2\sigma_i^2\right).}$$

特别地，独立正态变量相减时：

$$X-Y\sim N(\mu_X-\mu_Y,\sigma_X^2+\sigma_Y^2).$$

均值相减，方差仍相加。若结果方差为零，$Y$ 为常数变量。

### 5.5 正态标准化与标准正态平方

对应课件第 43—44 页。

#### (1) 标准化的 MGF 证明

若 $X\sim N(\mu,\sigma^2)$，$\sigma>0$，令 $Z=(X-\mu)/\sigma$：

$$M_Z(t)=e^{-\mu t/\sigma}M_X(t/\sigma)=e^{t^2/2}.$$

所以：

$$\boxed{Z\sim N(0,1).}$$

仅使均值为零、方差为一，不能保证一般变量变成正态；这里还使用了原变量正态。

#### (2) 标准正态平方的分布

若 $Z\sim N(0,1)$，则当 $t<1/2$：

$$E(e^{tZ^2})=\frac1{\sqrt{2\pi}}\int_{\mathbb R}e^{-(1-2t)z^2/2}\,dz=(1-2t)^{-1/2}.$$

这正是 $\chi^2(1)$ 的 MGF：

$$\boxed{Z^2\sim\chi^2(1).}$$

因此独立标准正态平方和满足：

$$\boxed{Z_1,\ldots,Z_n\overset{\mathrm{iid}}\sim N(0,1)\implies\sum_{i=1}^nZ_i^2\sim\chi^2(n).}$$

---

## 6. 协方差与相关系数 (Covariance & Correlation)

### 6.1 协方差的定义、意义与双线性性

对应课件第 52、67—68 页。

> **定义（协方差, Covariance）**：在二阶矩有限时：
> $$\boxed{\operatorname{Cov}(X,Y)=E[(X-\mu_X)(Y-\mu_Y)]=E(XY)-E(X)E(Y).}$$

同向偏离各自均值时，偏差乘积为正；反向偏离时为负。协方差是这些乘积的平均，反映整体的线性共同变化倾向，而不是每次观测都满足的单调规律。

基本性质：

$$\operatorname{Cov}(X,X)=\operatorname{Var}(X),\qquad \operatorname{Cov}(X,Y)=\operatorname{Cov}(Y,X).$$

> **定理 4.10（双线性性, Bilinearity）**：
> $$\boxed{\operatorname{Cov}\left(\sum_i a_iX_i,\sum_j b_jY_j\right)=\sum_i\sum_j a_ib_j\operatorname{Cov}(X_i,Y_j).}$$

证明：将两边变量分别减去其均值，展开乘积，再利用期望线性性。整个过程不需要独立。

特别地：

$$\operatorname{Cov}(aX+b,cY+d)=ac\operatorname{Cov}(X,Y),$$

$$\operatorname{Cov}(X+Y,Z)=\operatorname{Cov}(X,Z)+\operatorname{Cov}(Y,Z).$$

常数平移不改变协方差，倍乘系数保留符号。

### 6.2 一般线性组合的方差：推论 4.11

对应课件第 69—70 页。

> **推论 4.11**：
> $$\boxed{\operatorname{Var}\left(\sum_i a_iX_i\right)=\sum_i a_i^2\operatorname{Var}(X_i)+2\sum_{i<j}a_ia_j\operatorname{Cov}(X_i,X_j).}$$

证明：令 $U=\sum_i a_iX_i$，由 $\operatorname{Var}(U)=\operatorname{Cov}(U,U)$ 与双线性性：

$$\operatorname{Var}(U)=\sum_i\sum_j a_ia_j\operatorname{Cov}(X_i,X_j).$$

其中 $i=j$ 为方差项；$i\ne j$ 的对称项两两合并，得到系数 $2$。$\blacksquare$

两个变量时：

$$\boxed{\operatorname{Var}(aX+bY)=a^2\sigma_X^2+b^2\sigma_Y^2+2ab\operatorname{Cov}(X,Y).}$$

因此：

$$\operatorname{Var}(X\pm Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)\pm2\operatorname{Cov}(X,Y).$$

若变量两两不相关，交叉项消失；独立是保证这种简化成立的充分条件，但不是必要条件。

### 6.3 相关系数的界与等号条件

对应课件第 52、56—57 页。

> **定义（相关系数, Correlation）**：当 $0<\sigma_X,\sigma_Y<\infty$ 时：
> $$\boxed{\rho_{X,Y}=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}.}$$

协方差随单位变化，相关系数除去两个标准差后没有量纲。若一个变量方差为零，该公式下的相关系数没有定义。

#### (1) 相关系数的范围

设 $U=X-\mu_X$，$V=Y-\mu_Y$。Cauchy–Schwarz 不等式给出：

$$[E(UV)]^2\le E(U^2)E(V^2)=\sigma_X^2\sigma_Y^2.$$

故：

$$\boxed{-1\le\rho_{X,Y}\le1.}$$

#### (2) 什么时候达到等号？

等号成立当且仅当 $V=aU$ a.s.。由于两个方差为正，$a\ne0$。因此：

$$\boxed{|\rho|=1\iff Y=aX+b\text{ a.s.},\quad a\ne0.}$$

$a>0$ 对应 $\rho=1$；$a<0$ 对应 $\rho=-1$。一般非线性函数关系并不能保证 $|\rho|=1$。

### 6.4 例 4.8：联合分布表求相关系数

对应课件第 53—55 页。

已知：

$$p_{X,Y}(x,y)=\frac{x+2y}{18},\qquad x,y\in\{1,2\}.$$

#### 第一步：求联合与边缘分布

| $X\backslash Y$ | $Y=1$ | $Y=2$ | $p_X(x)$ |
| :--- | :--- | :--- | :--- |
| $X=1$ | $3/18$ | $5/18$ | $4/9$ |
| $X=2$ | $4/18$ | $6/18$ | $5/9$ |
| $p_Y(y)$ | $7/18$ | $11/18$ | $1$ |

#### 第二步：求一、二阶矩

$$E(X)=\frac{14}{9},\quad E(X^2)=\frac83,\quad E(Y)=\frac{29}{18},\quad E(Y^2)=\frac{17}{6}.$$

因此：

$$\operatorname{Var}(X)=\frac83-\left(\frac{14}{9}\right)^2=\frac{20}{81},$$

$$\operatorname{Var}(Y)=\frac{17}{6}-\left(\frac{29}{18}\right)^2=\frac{77}{324}.$$

#### 第三步：求交叉矩与协方差

$$E(XY)=\sum_x\sum_yxy\frac{x+2y}{18}=\frac{3+10+8+24}{18}=\frac52.$$

$$\operatorname{Cov}(X,Y)=\frac52-\frac{14}{9}\frac{29}{18}=-\frac1{162}.$$

#### 第四步：标准化为相关系数

$$\boxed{\rho=\frac{-1/162}{\sqrt{(20/81)(77/324)}}=-\frac1{\sqrt{1540}}\approx-0.0255.}$$

说明二者只有很弱的负线性相关，不能据此断定独立。

### 6.5 独立与不相关：离散、连续两个反例

对应课件第 62—66 页。

若独立，则 $E(XY)=E(X)E(Y)$，故：

$$\boxed{X\perp Y\implies\operatorname{Cov}(X,Y)=0.}$$

反向推理一般不成立。

#### (1) 例 4.10：离散反例

$(X,Y)$ 在 $(0,1),(1,0),(2,1)$ 上各有概率 $1/3$。于是：

$$E(X)=1,\quad E(Y)=\frac23,\quad E(XY)=\frac23.$$

所以 $\operatorname{Cov}(X,Y)=0$。但是：

$$P(X=0,Y=0)=0\ne P(X=0)P(Y=0)=\frac19.$$

故二者不相关但不独立。

#### (2) 连续反例：$Y=X^2$

设 $X\sim U(-1,1)$，$Y=X^2$。由对称性：

$$E(X)=0,\qquad E(XY)=E(X^3)=0,$$

从而协方差为零。为严格证明不独立，考虑：

$$A=\{|X|\le1/2\},\qquad B=\{Y\le1/4\}.$$

因 $Y=X^2$，有 $A=B$，所以：

$$P(A\cap B)=\frac12,\qquad P(A)P(B)=\frac14.$$

事件不独立，故随机变量也不独立。

> **【核心逻辑】**  
> 独立排除所有可测事件层面的依赖；不相关只约束一个二阶交叉矩。独立比不相关强得多。只有加入联合正态等额外结构，才可以从不相关推出独立。

---

## 7. 正态模型与联合正态的作用 (Normal Models & Joint Normality)

### 7.1 正态概率计算与分位数

设 $X\sim N(\mu,\sigma^2)$，$\sigma>0$，标准正态 CDF 为 $\Phi$。标准化后：

$$P(X\le x)=\Phi\left(\frac{x-\mu}{\sigma}\right),$$

$$\boxed{P(a\le X\le b)=\Phi\left(\frac{b-\mu}{\sigma}\right)-\Phi\left(\frac{a-\mu}{\sigma}\right).}$$

若 $z_p$ 满足 $\Phi(z_p)=p$，则 $X$ 的 $p$ 分位数为：

$$\boxed{x_p=\mu+\sigma z_p.}$$

使用对称性可减少查表：$\Phi(-z)=1-\Phi(z)$。

### 7.2 灌装量质量控制例题

对应课件第 71—72 页。设瓶中液体体积：

$$X\sim N(500,10^2).$$

#### (1) 少于 $485$ mL 的概率

$$P(X<485)=\Phi\left(\frac{485-500}{10}\right)=\Phi(-1.5)\approx\boxed{0.0668}.$$

#### (2) 满足 $485\le X\le515$ 的比例

$$P(485\le X\le515)=\Phi(1.5)-\Phi(-1.5)\approx\boxed{0.8664}.$$

#### (3) 仅有 $5\%$ 的瓶子超过的体积

令 $P(X>c)=0.05$，等价于 $P(X\le c)=0.95$：

$$\frac{c-500}{10}=z_{0.95}\approx1.645.$$

所以：

$$\boxed{c\approx516.45\text{ mL}.}$$

**方向辨析**：“只有 $5\%$ 超过”对应第 $95\%$ 分位数，不是第 $5\%$ 分位数。

### 7.3 边缘正态不足以确定联合关系

对应课件第 73—74 页。

已知 $X,Y$ 各自的正态分布，不能单独确定 $P(X>a,Y>b)$ 或 $X+Y$ 的完整分布。还需要描述依赖结构。

> **【深度补充：联合正态的定义性特征】**  
> 若对任意常数 $a,b$，$aX+bY$ 都是正态变量（允许退化情形），则称 $(X,Y)$ 联合正态。联合正态保证边缘正态；边缘正态本身一般不能推出联合正态。

仅给出两个边缘分布和一个相关系数，对一般分布仍不足以唯一确定联合分布；在**联合正态假设下**，均值、方差、相关系数才确定二维正态模型。

### 7.4 相关正态变量的线性组合例题

课件设：

$$X\sim N(120,15^2),\quad Y\sim N(200,30^2),\quad \rho=0.6,$$

且 $(X,Y)$ 联合正态。令 $R=X+0.5Y$。

首先：

$$\operatorname{Cov}(X,Y)=0.6\times15\times30=270.$$

均值：

$$E(R)=120+0.5\times200=220.$$

方差：

$$\begin{aligned}\operatorname{Var}(R)&=15^2+0.5^2\times30^2+2(1)(0.5)(270)\\&=225+225+270=720.\end{aligned}$$

由联合正态性：

$$\boxed{R\sim N(220,720).}$$

**三个层次要分清**：均值计算只需线性性；方差计算需要协方差；完整分布为正态使用联合正态假设。

### 7.5 深度补充：二维正态的结构与条件分布

本节用于补全课件引入例子与后续条件期望之间的联系，不属于课件已经完整展开的证明内容。

#### (1) 一个可解释的构造

取独立标准正态 $U,V$，令 $\sigma_X,\sigma_Y>0$，$-1\le\rho\le1$：

$$X=\mu_X+\sigma_XU,$$

$$Y=\mu_Y+\sigma_Y\left(\rho U+\sqrt{1-\rho^2}\,V\right).$$

则 $X,Y$ 联合正态，且：

$$\operatorname{Cov}(X,Y)=\rho\sigma_X\sigma_Y.$$

$U$ 是二者共享的随机来源，$V$ 是 $Y$ 独有的随机来源。当 $\rho=0$ 时共享项消失，$X,Y$ 独立。

#### (2) 非退化二维正态密度

当 $|\rho|<1$ 时，令 $u=(x-\mu_X)/\sigma_X$，$v=(y-\mu_Y)/\sigma_Y$，有：

$$f_{X,Y}(x,y)=\frac1{2\pi\sigma_X\sigma_Y\sqrt{1-\rho^2}}\exp\left[-\frac{u^2-2\rho uv+v^2}{2(1-\rho^2)}\right].$$

当 $\rho=0$ 时，密度分解为 $f_X(x)f_Y(y)$，可直接看出独立。

当 $|\rho|=1$ 时，分布集中在一条直线上，不能继续使用上面的二维密度公式。

#### (3) 条件分布与条件均值

给定 $X=x$ 后，构造中的 $U=(x-\mu_X)/\sigma_X$ 已经确定，而独立的 $V$ 保持标准正态。所以当 $|\rho|<1$：

$$\boxed{Y\mid X=x\sim N\left(\mu_Y+\rho\frac{\sigma_Y}{\sigma_X}(x-\mu_X),\ \sigma_Y^2(1-\rho^2)\right).}$$

因此条件期望是线性的，条件方差与 $x$ 无关。$|\rho|=1$ 时，相应条件分布退化为确定值。

---

## 8. 条件期望与全期望公式 (Conditional & Total Expectation)

### 8.1 普通期望、给定取值的条件期望、随机条件期望

对应课件第 76—80 页。

条件期望回答：**知道额外信息后，应如何更新对随机变量平均值的判断？**

| 对象 | 数学含义 | 类型 |
| :--- | :--- | :--- |
| $E(Y)$ | 总体平均 | 常数 |
| $E(Y\mid X=x)$ | 固定 $x$ 对应条件组的平均 | 对该 $x$ 而言是一个数 |
| $E(Y\mid X)$ | 由随机 $X$ 决定的条件平均 | 随机变量，可能为常数 |

定义函数：

$$g(x)=E(Y\mid X=x).$$

然后：

$$\boxed{E(Y\mid X)=g(X).}$$

这解释了为什么条件期望外面还可以再求期望或方差。

### 8.2 离散型与连续型计算流程

对应课件第 79—80 页。

#### (1) 离散型

先求条件概率，要求 $p_X(x)>0$：

$$p_{Y\mid X}(y\mid x)=\frac{p_{X,Y}(x,y)}{p_X(x)},\qquad p_X(x)=\sum_y p_{X,Y}(x,y).$$

再求条件平均：

$$\boxed{E(Y\mid X=x)=\sum_y y p_{Y\mid X}(y\mid x)=\frac{\sum_y y p_{X,Y}(x,y)}{\sum_y p_{X,Y}(x,y)}.}$$

固定 $x$，对 $y$ 求和，最后按需要将 $x$ 换回 $X$。

#### (2) 连续型

先求：

$$f_X(x)=\int_{\mathbb R}f_{X,Y}(x,y)\,dy.$$

当 $f_X(x)>0$ 时：

$$f_{Y\mid X}(y\mid x)=\frac{f_{X,Y}(x,y)}{f_X(x)}.$$

于是：

$$\boxed{E(Y\mid X=x)=\int_{\mathbb R}y f_{Y\mid X}(y\mid x)\,dy=\frac{\int y f_{X,Y}(x,y)\,dy}{\int f_{X,Y}(x,y)\,dy}.}$$

#### (3) 取值区域与零概率条件

如果支撑集为 $0<x<y<1$，固定 $x$ 后，$y$ 必须从 $x$ 积到 $1$，不能写成与支撑无关的 $0$ 到 $1$。

连续型通常有 $P(X=x)=0$，不能直接使用两个单点事件概率相除。条件密度是在联合密度框架下定义的对象。条件期望只需在 $X$ 的分布意义下几乎处处确定。

> **【条件方向辨析】**  
> 求 $E(Y\mid X)$：固定 $X$，求 $Y$ 的条件分布；求 $E(X\mid Y)$：固定 $Y$，求 $X$ 的条件分布。两者一般不对称，积分范围和分母也不同。

### 8.3 条件期望的代数性质

对应课件第 81 页。以下在有关可积性条件下几乎必然成立。

#### (1) 线性性

$$E(aY+bZ\mid X)=aE(Y\mid X)+bE(Z\mid X).$$

不要求 $Y,Z$ 独立。

#### (2) 已知量可以提出

$$\boxed{E[h(X)Y\mid X]=h(X)E(Y\mid X).}$$

因为知道 $X$ 就知道 $h(X)$。特别地：

$$E[h(X)\mid X]=h(X).$$

例如 $E(XY+X^2\mid X)=XE(Y\mid X)+X^2$。

#### (3) 独立时不更新均值

$$Y\perp X\implies E(Y\mid X)=E(Y).$$

反过来不一定成立：条件均值不变并不能保证条件分布整体不变。

### 8.4 全期望公式及证明

对应课件第 82—83 页。

> **全期望公式（Law of Total Expectation）**：若 $Y$ 可积，则：
> $$\boxed{E[E(Y\mid X)]=E(Y).}$$

离散型展开：

$$E(Y)=\sum_x E(Y\mid X=x)p_X(x).$$

连续型展开：

$$E(Y)=\int E(Y\mid X=x)f_X(x)\,dx.$$

**直观意义**：先求每个条件组的平均，再按组出现的概率加权平均。

**离散型证明**：

$$\begin{aligned}E[E(Y\mid X)]&=\sum_x\left[\sum_y y p_{Y\mid X}(y\mid x)\right]p_X(x)\\&=\sum_x\sum_y y p_{X,Y}(x,y)\\&=\sum_y y\sum_xp_{X,Y}(x,y)\\&=\sum_y y p_Y(y)=E(Y).\end{aligned}\quad\blacksquare$$

连续型将求和换成积分即可。各组概率不相同时，不可将条件均值直接做等权算术平均。

### 8.5 两台机器与离散联合分布的完整案例

#### 案例 1：两台机器的总体次品率

对应课件第 76—78 页。设机器来源 $X\in\{A,B\}$，次品示性变量为 $Y$。已知：

$$P(X=A)=0.7,\quad P(X=B)=0.3,$$

$$P(Y=1\mid X=A)=0.02,\quad P(Y=1\mid X=B)=0.08.$$

由于 $Y$ 为示性变量：

$$E(Y\mid X)=\begin{cases}0.02,&X=A,\\0.08,&X=B.\end{cases}$$

因此：

$$\boxed{E(Y)=0.7(0.02)+0.3(0.08)=0.038.}$$

总体次品率为 $3.8\%$。这也说明全概率公式是全期望公式用于示性变量的特殊情形。

#### 案例 2：离散条件期望的完整计算

对应课件第 84—85 页。设：

$$p_{X,Y}(x,y)=\frac{x+y}{4},\qquad x,y\in\{0,1\}.$$

| $X\backslash Y$ | $Y=0$ | $Y=1$ | $p_X(x)$ |
| :--- | :--- | :--- | :--- |
| $X=0$ | $0$ | $1/4$ | $1/4$ |
| $X=1$ | $1/4$ | $1/2$ | $3/4$ |

当 $X=0$，$Y=1$ 的条件概率为 $1$：

$$E(Y\mid X=0)=1.$$

当 $X=1$：

$$P(Y=1\mid X=1)=\frac{1/2}{3/4}=\frac23,$$

所以 $E(Y\mid X=1)=2/3$。将两种情况合并为随机变量：

$$\boxed{E(Y\mid X)=1-\frac X3.}$$

再求期望：

$$E[E(Y\mid X)]=1\frac14+\frac23\frac34=\frac34.$$

直接从边缘分布也有 $P(Y=1)=3/4$，故 $E(Y)=3/4$，验证全期望公式。

---

## 9. 条件方差、全方差与分层模型 (Conditional Variance & Hierarchical Models)

### 9.1 条件方差与全方差公式

对应课件第 86—88 页。

> **定义（条件方差）**：若 $E(Y^2)<\infty$，则：
> $$\operatorname{Var}(Y\mid X)=E\left[(Y-E(Y\mid X))^2\mid X\right].$$
> 计算公式为：
> $$\boxed{\operatorname{Var}(Y\mid X)=E(Y^2\mid X)-[E(Y\mid X)]^2.}$$

它描述知道 $X$ 之后，$Y$ 围绕**条件均值**的剩余波动，也是由 $X$ 决定的随机变量。

> **全方差公式（Law of Total Variance）**：
> $$\boxed{\operatorname{Var}(Y)=E[\operatorname{Var}(Y\mid X)]+\operatorname{Var}[E(Y\mid X)].}$$

两部分含义：

- $E[\operatorname{Var}(Y\mid X)]$：平均组内波动。
- $\operatorname{Var}[E(Y\mid X)]$：不同条件组均值之间的波动。

#### 证明

对条件方差取期望：

$$E[\operatorname{Var}(Y\mid X)]=E(Y^2)-E\{[E(Y\mid X)]^2\}.$$

另一方面：

$$\operatorname{Var}[E(Y\mid X)]=E\{[E(Y\mid X)]^2\}-[E(Y)]^2.$$

相加后中间项消去，得到 $E(Y^2)-[E(Y)]^2=\operatorname{Var}(Y)$。$\blacksquare$

> **【易错辨析：非线性运算不能直接穿过期望】**  
> $E([E(Y\mid X)]^2)$ 通常不等于 $[E(Y)]^2$，两者之差恰好为条件均值的方差。忽略这一差别就会漏掉全方差中的组间波动项。

### 9.2 两阶段均匀模型的完整计算

对应课件第 89—91 页。

先抽取 $X\sim U(0,1)$；给定 $X=x$ 后，再抽取：

$$Y\mid X=x\sim U(x,1).$$

求条件均值、条件方差以及无条件均值、方差。

#### 第一步：识别条件分布

均匀分布 $U(a,b)$ 的均值为 $(a+b)/2$，方差为 $(b-a)^2/12$，所以：

$$\boxed{E(Y\mid X)=\frac{X+1}{2},\qquad \operatorname{Var}(Y\mid X)=\frac{(1-X)^2}{12}.}$$

#### 第二步：使用全期望

$$E(Y)=E\left(\frac{X+1}{2}\right)=\frac{E(X)+1}{2}=\boxed{\frac34}.$$

#### 第三步：计算平均组内方差

$$E[\operatorname{Var}(Y\mid X)]=\frac1{12}\int_0^1(1-x)^2\,dx=\frac1{36}.$$

#### 第四步：计算条件均值的方差

$$\operatorname{Var}[E(Y\mid X)]=\operatorname{Var}\left(\frac{X+1}{2}\right)=\frac14\operatorname{Var}(X)=\frac1{48}.$$

#### 第五步：相加得到总方差

$$\boxed{\operatorname{Var}(Y)=\frac1{36}+\frac1{48}=\frac7{144}.}$$

**方法价值**：无需先推导 $Y$ 的边缘密度，即可得到均值和方差。

> **【深度补充：相同取值区域不等于相同分布】**  
> 此模型的联合密度为 $f_{X,Y}(x,y)=f_X(x)f_{Y\mid X}(y\mid x)=1/(1-x)$，区域为 $0<x<y<1$。它不是在三角形上取常数密度 $2$ 的均匀模型。两者虽然有相同的区域，边缘分布却不同，不能互相套用结果。

**边缘分布核对（补充）**：对 $0<y<1$：

$$f_Y(y)=\int_0^y\frac1{1-x}\,dx=-\ln(1-y).$$

该密度不是常数，说明条件上均匀不意味着无条件下仍均匀。

### 9.3 随机成功概率二项模型的均值、方差和边缘分布

对应课件第 92—94 页。

设随机选取地区的患病率 $Q\sim U(0,1)$。给定 $Q=q$ 后抽取 $n$ 个条件独立个体，患病人数满足：

$$X\mid Q=q\sim\operatorname{Binomial}(n,q).$$

#### (1) 条件均值与条件方差

$$E(X\mid Q)=nQ,\qquad \operatorname{Var}(X\mid Q)=nQ(1-Q).$$

#### (2) 无条件均值

$$\boxed{E(X)=nE(Q)=\frac n2.}$$

#### (3) 无条件方差

$$\begin{aligned}\operatorname{Var}(X)&=E[nQ(1-Q)]+\operatorname{Var}(nQ)\\&=n[E(Q)-E(Q^2)]+n^2\operatorname{Var}(Q)\\&=n\left(\frac12-\frac13\right)+\frac{n^2}{12}\\&=\boxed{\frac{n(n+2)}{12}}.\end{aligned}$$

#### (4) 边缘分布

对 $k=0,1,\ldots,n$，由条件概率积分：

$$P(X=k)=\int_0^1\binom nkq^k(1-q)^{n-k}\,dq.$$

利用 Beta 积分：

$$\int_0^1q^k(1-q)^{n-k}\,dq=B(k+1,n-k+1)=\frac{k!(n-k)!}{(n+1)!}.$$

因此：

$$\boxed{P(X=k)=\frac1{n+1},\qquad k=0,1,\ldots,n.}$$

无条件的 $X$ 服从 $\{0,1,\ldots,n\}$ 上的离散均匀分布。

#### (5) 为什么不能把 $Q$ 替换成 $E(Q)$？

误写为 $\operatorname{Binomial}(n,1/2)$，会得到方差 $n/4$，而真实方差为 $n(n+2)/12$。二者相差：

$$\frac{n(n+2)}{12}-\frac n4=\frac{n(n-1)}{12}.$$

当 $n>1$ 时有额外波动，来自所有个体共享的随机成功概率。

### 9.4 条件独立与无条件依赖的区别

以下为帮助理解上题的深度补充。

设 $I_i$ 表示第 $i$ 个个体是否患病。给定 $Q$ 后，$I_i$ 条件独立，但无条件下：

$$E(I_i)=E(Q)=\frac12,$$

$$E(I_iI_j)=E[E(I_iI_j\mid Q)]=E(Q^2)=\frac13,\qquad i\ne j.$$

所以：

$$\operatorname{Cov}(I_i,I_j)=\frac13-\frac14=\frac1{12}>0.$$

因此：

$$\operatorname{Var}\left(\sum_{i=1}^nI_i\right)=\frac n4+2\binom n2\frac1{12}=\frac{n(n+2)}{12}.$$

这从协方差角度再次验证了全方差的答案。

> **【知识连接】**  
> 同一个随机参数使不同个体共享了信息，从而产生无条件依赖。全方差中的组间波动，与变量和公式中的交叉协方差，是这一现象的两种数学表达。

---

## 10. 最优预测：线性预测与条件期望 (Optimal Prediction)

### 10.1 最佳线性预测的公式与配方证明

对应课件第 58—59 页。已知 $X$，用 $\widehat Y=a+bX$ 预测 $Y$，要求最小化：

$$E[(Y-a-bX)^2].$$

假设二阶矩有限且 $\operatorname{Var}(X)>0$。

> **最佳线性预测（Best Linear Predictor）**：
> $$\boxed{\widehat Y=\mu_Y+\frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(X)}(X-\mu_X).}$$
> 对应斜率与截距为：
> $$b=\frac{\operatorname{Cov}(X,Y)}{\sigma_X^2},\qquad a=\mu_Y-b\mu_X.$$

#### 严谨推导

先分解均值与中心化部分：

$$\begin{aligned}E[(Y-a-bX)^2]&=(\mu_Y-a-b\mu_X)^2\\&\quad+\sigma_Y^2+b^2\sigma_X^2-2b\operatorname{Cov}(X,Y).\end{aligned}$$

对固定 $b$，取 $a=\mu_Y-b\mu_X$，使第一项为零。再对剩余项配方：

$$\begin{aligned}&\sigma_Y^2+b^2\sigma_X^2-2b\operatorname{Cov}(X,Y)\\&=\sigma_X^2\left(b-\frac{\operatorname{Cov}(X,Y)}{\sigma_X^2}\right)^2+\sigma_Y^2-\frac{\operatorname{Cov}(X,Y)^2}{\sigma_X^2}.\end{aligned}$$

第一项在所给斜率处为零，得最优解。预测直线经过 $(\mu_X,\mu_Y)$。

注意误差是 $Y-a-bX$，即固定 $X$ 时的纵向残差，不是点到直线的垂直距离。

### 10.2 相关系数与最小均方误差

最小均方误差为：

$$\boxed{\operatorname{MSE}_{\min}=\sigma_Y^2-\frac{\operatorname{Cov}(X,Y)^2}{\sigma_X^2}.}$$

若 $\sigma_Y>0$，可写成：

$$\boxed{\widehat Y=\mu_Y+\rho\frac{\sigma_Y}{\sigma_X}(X-\mu_X),\qquad \operatorname{MSE}_{\min}=\sigma_Y^2(1-\rho^2).}$$

不用 $X$ 时，最佳常数预测为 $\mu_Y$，误差为 $\sigma_Y^2$。因此 $\rho^2$ 表示使用最佳线性预测后相对减少的均方误差比例。

- $\rho=0$：在直线预测范围内，$X$ 不改善预测。
- $|\rho|=1$：线性预测误差为零。
- $0<|\rho|<1$：仍存在无法被最佳直线解释的波动。

### 10.3 二元离散预测案例

对应课件第 60—61 页。

| $X\backslash Y$ | $Y=0$ | $Y=1$ |
| :--- | :--- | :--- |
| $X=0$ | $0.4$ | $0.1$ |
| $X=1$ | $0.1$ | $0.4$ |

两边边缘均为 $\operatorname{Bernoulli}(1/2)$，故：

$$E(X)=E(Y)=\frac12,\qquad \operatorname{Var}(X)=\operatorname{Var}(Y)=\frac14.$$

因 $XY=1$ 仅在 $(1,1)$ 发生：

$$E(XY)=0.4,\quad \operatorname{Cov}(X,Y)=0.4-0.25=0.15,\quad \rho=0.6.$$

最佳线性预测：

$$\widehat Y=0.5+0.6(X-0.5)=\boxed{0.2+0.6X}.$$

最小误差：

$$\boxed{\operatorname{MSE}_{\min}=0.25(1-0.6^2)=0.16.}$$

**与条件期望连接**：$E(Y\mid X=0)=0.1/0.5=0.2$，$E(Y\mid X=1)=0.4/0.5=0.8$，因此本例中 $E(Y\mid X)=0.2+0.6X$，恰好与最佳线性预测一致。

### 10.4 深度补充：条件期望是最佳一般均方预测

课件详细证明了最佳线性预测；下面解释它与条件期望的关系。

如果不把预测限制为 $a+bX$，而允许任意平方可积的 $g(X)$，令：

$$m(X)=E(Y\mid X).$$

分解误差：

$$Y-g(X)=[Y-m(X)]+[m(X)-g(X)].$$

由于：

$$E[Y-m(X)\mid X]=0,$$

交叉项的期望为零：

$$E\{[Y-m(X)][m(X)-g(X)]\}=0.$$

所以：

$$\boxed{E[(Y-g(X))^2]=E[\operatorname{Var}(Y\mid X)]+E[(m(X)-g(X))^2].}$$

第二项非负，故最优解为：

$$\boxed{\widehat Y_{\mathrm{opt}}=E(Y\mid X),\qquad \min_gE[(Y-g(X))^2]=E[\operatorname{Var}(Y\mid X)].}$$

| 预测问题 | 允许的函数 | 最优结果 |
| :--- | :--- | :--- |
| 最佳常数预测 | 常数 $c$ | $E(Y)$ |
| 最佳线性预测 | $a+bX$ | 均值、方差与协方差决定的直线 |
| 最佳一般均方预测 | 任意合适的 $g(X)$ | $E(Y\mid X)$ |

例如 $X\sim U(-1,1)$、$Y=X^2$ 时，相关系数为零，最佳线性预测只能使用常数 $E(Y)=1/3$；但非线性预测 $g(X)=X^2$ 没有误差。

在联合正态情况下，条件期望本身是线性的，因此最佳一般预测与最佳线性预测相同。这解释了二维正态条件均值公式与最佳直线公式具有相同形式。

---

## 11. 核心公式速查与易错知识点深度辨析 (Summary & Pitfalls)

### 11.1 公式、条件和用途对照表

#### (1) 核心公式

| 知识点 | 公式 | 条件或用途 |
| :--- | :--- | :--- |
| 函数期望 | $E[g(X)]=\sum g(x)p_X(x)$ 或 $\int g(x)f_X(x)\,dx$ | $g(X)$ 可积，不必先求新分布 |
| 期望线性性 | $E(\sum a_iX_i)=\sum a_iE(X_i)$ | 不要求独立 |
| 独立乘积 | $E(\prod g_i(X_i))=\prod E[g_i(X_i)]$ | 相互独立，各项可积 |
| 方差 | $\operatorname{Var}(X)=E(X^2)-[E(X)]^2$ | 二阶矩有限 |
| 方差变换 | $\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$ | 标准差缩放为 $\lvert a\rvert$ 倍 |
| 协方差 | $\operatorname{Cov}(X,Y)=E(XY)-E(X)E(Y)$ | 计算线性共同变化 |
| 相关系数 | $\rho=\operatorname{Cov}(X,Y)/(\sigma_X\sigma_Y)$ | 两方差正且有限 |
| 线性组合方差 | $a^2\sigma_X^2+b^2\sigma_Y^2+2ab\operatorname{Cov}(X,Y)$ | 不要求独立 |
| MGF 生成矩 | $M_X^{(r)}(0)=E(X^r)$ | MGF 零点邻域有限 |
| 仿射 MGF | $M_{aX+b}(t)=e^{bt}M_X(at)$ | 识别变换后分布 |
| 独立和 MGF | $M_{\sum a_iX_i}(t)=\prod M_{X_i}(a_it)$ | 相互独立 |
| 全期望 | $E[E(Y\mid X)]=E(Y)$ | $Y$ 可积 |
| 条件方差 | $E(Y^2\mid X)-[E(Y\mid X)]^2$ | 中心是条件均值 |
| 全方差 | $E[\operatorname{Var}(Y\mid X)]+\operatorname{Var}[E(Y\mid X)]$ | 等于 $\operatorname{Var}(Y)$，二阶矩有限 |
| 最佳线性预测 | $\mu_Y+\operatorname{Cov}(X,Y)(X-\mu_X)/\sigma_X^2$ | $\sigma_X^2>0$ |
| 最佳一般预测 | $E(Y\mid X)$ | 均方误差准则，二阶矩有限 |

#### (2) MGF 速查

| 分布 | MGF | 有限范围 |
| :--- | :--- | :--- |
| $\operatorname{Bernoulli}(p)$ | $1-p+pe^t$ | $t\in\mathbb R$ |
| $\operatorname{Binomial}(n,p)$ | $(1-p+pe^t)^n$ | $t\in\mathbb R$ |
| $\operatorname{Poisson}(\lambda)$ | $e^{\lambda(e^t-1)}$ | $t\in\mathbb R$ |
| $\operatorname{Exp}(\lambda)$ | $\lambda/(\lambda-t)$ | $t<\lambda$ |
| $\operatorname{Gamma}(\alpha,\lambda)$ | $(\lambda/(\lambda-t))^\alpha$ | $t<\lambda$ |
| $\chi^2(n)$ | $(1-2t)^{-n/2}$ | $t<1/2$ |
| $N(\mu,\sigma^2)$ | $e^{\mu t+\sigma^2t^2/2}$ | $t\in\mathbb R$ |

### 11.2 高频错误与概念边界

#### 辨析 1：把期望的规则套到方差上

- **错误**：$\operatorname{Var}(aX+bY)=a\operatorname{Var}(X)+b\operatorname{Var}(Y)$。
- **正确**：系数要平方，还需保留 $2ab\operatorname{Cov}(X,Y)$。
- **检查方法**：令 $Y=X$ 或 $Y=-X$ 代入，常可立即发现不合理结果。

#### 辨析 2：独立、不相关、均值独立混为一谈

- 独立推出不相关（在二阶矩有限时）。
- $E(Y\mid X)=E(Y)$ 表示条件均值不变，但仍可能存在条件方差等方面的依赖。
- 零协方差更不能推出独立。
- 联合正态是可将不相关提升为独立的重要附加条件。

#### 辨析 3：MGF 二阶导数与方差混淆

$$M_X''(0)=E(X^2),\qquad \operatorname{Var}(X)=M_X''(0)-[M_X'(0)]^2.$$

例如正态分布有 $M_X''(0)=\mu^2+\sigma^2$，不能把它直接写成 $\sigma^2$。

#### 辨析 4：忽略分布可加性的参数要求

二项和要求相同成功率；Gamma 和要求相同速率；整个 MGF 乘积法还要求相互独立。只写“分布名称相同”不足以使用可加性。

#### 辨析 5：条件期望的对象类型不清楚

$E(Y\mid X=x)$ 对固定 $x$ 是数，$E(Y\mid X)$ 是 $X$ 的函数。前者换回随机变量后，才能按 $X$ 的分布进一步求期望或方差。

#### 辨析 6：全方差漏掉条件均值的方差

知道组别后仍有组内波动，不同组的均值也可能不同；总体方差必须计入两者。只有条件均值几乎必然为常数时，组间项才为零。

#### 辨析 7：条件模型中的随机参数直接换成平均数

一般不能把 $X\mid Q\sim\operatorname{Binomial}(n,Q)$ 改为 $X\sim\operatorname{Binomial}(n,E(Q))$。需要对整个条件分布按 $Q$ 积分，或使用全期望、全方差。

#### 辨析 8：正态边缘、联合正态与相关信息混淆

两个正态边缘并不能保证联合正态。均值、方差、相关系数通常只描述部分联合信息；在联合正态模型内，它们才足以确定联合分布。

#### 辨析 9：最佳线性预测被误认为任意意义上的最佳预测

最佳线性预测只在直线函数类中最优。均方误差意义下的一般最优预测是条件期望；它可能是非线性的。

### 11.3 按题型选择方法

| 题型信号 | 优先方法 | 最后检查 |
| :--- | :--- | :--- |
| 已知密度求 $E[g(X)]$ | 直接积分 $g(x)f_X(x)$ | 支撑范围与可积性 |
| 计算复杂计数的均值 | 拆成示性变量 | 不要误加独立条件 |
| 求变量和的均值、方差 | 线性性与完整方差公式 | 协方差是否已知或为零 |
| 求独立和的完整分布 | MGF 相乘、唯一性 | 同参数要求与收敛范围 |
| 独立指数变量的最小值 | 生存函数相乘 | 求的是最小值还是和 |
| 联合概率表求相关系数 | 边缘矩、交叉矩、标准化 | $\lvert\rho\rvert\le1$ |
| 联合密度求条件期望 | 边缘密度、条件密度、积分 | 固定哪个变量、积分哪个变量 |
| 直接给出条件分布 | 全期望与全方差 | 全方差的两项是否齐全 |
| 给出随机成功率 | 分层模型计算 | 条件独立不等于无条件独立 |
| 预测直线 | 协方差除以自变量方差 | 回归方向、截距与误差 |

### 11.4 自测题与答案核对

以下为复习补充题，用于检查公式是否真正会用。

#### 自测 1：相关变量的线性组合

已知 $\operatorname{Var}(X)=4$、$\operatorname{Var}(Y)=9$、$\operatorname{Cov}(X,Y)=1$，求 $\operatorname{Var}(2X-Y)$。

**答案**：

$$4\cdot4+9+2(2)(-1)(1)=\boxed{21}.$$

#### 自测 2：从 MGF 识别分布

已知 $M_X(t)=\exp(3t+2t^2)$，求分布、均值与方差。

**答案**：与 $\exp(\mu t+\sigma^2t^2/2)$ 比较，$X\sim N(3,4)$；均值为 $3$，方差为 $4$，二阶原点矩为 $13$。

#### 自测 3：指数最小值

独立的 $X\sim\operatorname{Exp}(2)$、$Y\sim\operatorname{Exp}(3)$，求 $W=\min(X,Y)$ 的分布和均值。

**答案**：$W\sim\operatorname{Exp}(5)$，$E(W)=1/5$。不能据此把 $X+Y$ 也写成 $\operatorname{Exp}(5)$。

#### 自测 4：全期望与全方差

已知 $E(Y\mid X)=2X+1$、$\operatorname{Var}(Y\mid X)=3$，且 $E(X)=0$、$\operatorname{Var}(X)=2$。求 $E(Y)$、$\operatorname{Var}(Y)$。

**答案**：

$$E(Y)=1,\qquad \operatorname{Var}(Y)=3+\operatorname{Var}(2X+1)=3+8=11.$$

#### 自测 5：不相关是否意味着不可预测？

若 $X\sim U(-1,1)$，$Y=X^2$，比较最佳线性预测与最佳一般预测。

**答案**：协方差为零，最佳线性预测为 $1/3$。由 $E(X^4)=1/5$，其最小均方误差为 $1/5-1/9=4/45$。一般最优预测为 $X^2$，误差为零。

#### 自测 6：随机成功率模型

若 $Q\sim U(0,1)$，$X\mid Q\sim\operatorname{Binomial}(4,Q)$，求 $P(X=0)$、$E(X)$、$\operatorname{Var}(X)$。

**答案**：$X$ 在 $\{0,1,2,3,4\}$ 上等概率，故 $P(X=0)=1/5$、$E(X)=2$、$\operatorname{Var}(X)=2$。

---

## 课件与笔记模块对应索引

| 课件内容 | PDF 页码 | 本笔记位置 |
| :--- | :--- | :--- |
| 期望、函数期望、示性变量、线性性 | 6—10 | 第 2 节 |
| 方差、标准差、分布均值方差练习 | 11—19 | 第 3 节 |
| MGF 定义、生成矩、分布 MGF | 21—29 | 第 4 节 |
| MGF 唯一性、独立和、仿射变换 | 30—34 | 第 4—5 节 |
| 二项、正态线性组合、标准化与卡方 | 35—44 | 第 4—5 节 |
| 可加性、指数和与最小值 | 45—49 | 第 5 节 |
| 二元函数期望、协方差与相关系数 | 51—57 | 第 2、6 节 |
| 最佳线性预测及例题 | 58—61 | 第 10 节 |
| 独立与不相关、协方差双线性、组合方差 | 62—70 | 第 6 节 |
| 正态质量控制、二维正态引入 | 71—74 | 第 7 节 |
| 条件期望、性质、全期望与例题 | 76—85 | 第 8 节 |
| 条件方差与全方差 | 86—88 | 第 9 节 |
| 两阶段均匀模型 | 89—91 | 第 9 节 |
| 随机成功率二项模型 | 92—94 | 第 9 节 |

**复习使用建议**：第一遍按知识模块理解定义和条件；第二遍遮住答案独立完成课件案例；考前用第 11 节核对公式、适用前提和易错点。遇到忘记的推导，再通过页码索引回到原课件。
