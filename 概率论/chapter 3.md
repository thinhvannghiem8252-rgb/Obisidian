# Chapter 3: 多维随机变量及其分布（Multi-dimensional Random Variables and Distributions）深度精讲笔记

> **课程来源与参考教材**
>
> * **英文主教材**：Robert V. Hogg, Elliot A. Tanis, Dale Zimmerman, *Probability and Statistical Inference* (9th / 10th Edition), **Chapters 4.1–4.4, 5.2**
>
> * **中文参考教材**：魏宗舒《概率论与数理统计教程》（第三版），**第 2.2、2.6、3.3、3.6 节**
>
> * **核心关键词**：联合分布（Joint Distribution）、边缘分布（Marginal Distribution）、条件分布（Conditional Distribution）、相互独立性（Mutual Independence）、多维随机变量变换（Change of Multivariate Variables）、雅可比行列式（Jacobian Determinant）、三大导出抽样分布（$t$ 分布、$\chi^2$ 分布、$F$ 分布）

## 一、全章知识脉络与核心对比总览

本章将一维随机变量的概率分布理论全面推广至**多维（**$n$ **维，重点是二维）随机向量**。无论离散型还是连续型，其核心逻辑均围绕“联合 $\to$ 边缘 $\to$ 条件 $\to$ 独立性 $\to$ 函数变换”五条主线展开。

### 离散型与连续型多维随机变量核心公式对照表

| 核心概念 | 多维离散型随机变量 $(X_1, \dots, X_n)$ | 多维连续型随机变量 $(X_1, \dots, X_n)$ | 核心操作转换 | 
| ----- | ----- | ----- | ----- | 
| **基本描述工具** | 联合概率质量函数（Joint PMF）  $f(x_1,\dots,x_n) = P(X_1=x_1,\dots,X_n=x_n)$ | 联合概率密度函数（Joint PDF）  $f(x_1,\dots,x_n)$ | 概率点质量 $\leftrightarrow$ 概率微元密度 | 
| **非负性** | $0 \le f(x_1,\dots,x_n) \le 1$ | $f(x_1,\dots,x_n) \ge 0$（注意：可大于 $1$） | 概率值有上界 $1$，密度值无上界 $1$ | 
| **规范性（归一性）** | $\sum_{(x_1,\dots,x_n)\in\mathbb{S}} f(x_1,\dots,x_n) = 1$ | $\int_{\mathbb{R}^n} f(x_1,\dots,x_n)\,dx_1\cdots dx_n = 1$ | 离散求和 $\sum \leftrightarrow$ 连续积分 $\int$ | 
| **事件概率计算** | $P(\mathbf{X}\in A) = \sum_{\mathbf{x}\in A} f(x_1,\dots,x_n)$ | $P(\mathbf{X}\in A) = \int_{A} f(x_1,\dots,x_n)\,dx_1\cdots dx_n$ | 对事件区域 $A$ 求和 / 多重积分 | 
| **边缘分布（以** $X_j$ **为例）** | $f_{X_j}(x_j) = \sum_{\tilde{x}_{-j}\in\mathbb{S}_{-j}} f(x_1,\dots,x_n)$ | $f_{X_j}(x_j) = \int_{\mathbb{R}^{n-1}} f(x_1,\dots,x_n)\,d\tilde{x}_{-j}$ | **消元降维**：对除 $x_j$ 外的所有其余变量求和/积分 | 
| **条件分布（给定** $\tilde{X}_{-j}=\tilde{x}_{-j}$**）** | $f_{X_j\mid\tilde{X}_{-j}}(x_j\mid\tilde{x}_{-j}) = \frac{f(x_1,\dots,x_n)}{f_{\tilde{X}_{-j}}(\tilde{x}_{-j})}$ | $f_{X_j\mid\tilde{X}_{-j}}(x_j\mid\tilde{x}_{-j}) = \frac{f(x_1,\dots,x_n)}{f_{\tilde{X}_{-j}}(\tilde{x}_{-j})}$ | **联合除以边缘**（形式完全一致，前提是分母 $>0$） | 
| **相互独立性充要条件** | $\forall \mathbf{x}\in\mathbb{S},\; f(x_1,\dots,x_n) = \prod_{i=1}^n f_{X_i}(x_i)$ | $\forall \mathbf{x}\in\mathbb{R}^n,\; f(x_1,\dots,x_n) = \prod_{i=1}^n f_{X_i}(x_i)$ | **联合分布等于边缘分布的乘积** | 

## 二、3.1 多维离散型随机变量（Discrete Type）

### 1. 联合概率质量函数（Joint PMF, Slide P4）

#### （1）定义与符号说明

设 $X_1, \dots, X_n$ 是定义在离散样本空间上的一组随机变量：

* 记每个分量 $X_j$ 的取值空间（支撑集，Support）为 $\mathbb{X}_j$（$j = 1, \dots, n$）。

* 记随机向量 $(X_1, \dots, X_n)$ 的联合取值空间为笛卡尔积 $\mathbb{S} = \mathbb{X}_1 \times \dots \times \mathbb{X}_n$（注：若变量间存在取值约束，实际有效支撑集为 $\mathbb{S}$ 的子集）。

* 事件 $\{X_1 = x_1, \dots, X_n = x_n\}$ 同时发生的概率定义为**联合概率质量函数（Joint PMF）**： 

  $$
  f(x_1, \dots, x_n) = P(X_1 = x_1, \dots, X_n = x_n)
  $$

#### （2）三条基本性质

* **(a) 有界非负性**：$0 \le f(x_1, \dots, x_n) \le 1, \quad \forall (x_1, \dots, x_n) \in \mathbb{S}$

* **(b) 归一性（规范性）**：$\sum_{(x_1, \dots, x_n) \in \mathbb{S}} f(x_1, \dots, x_n) = 1$

* **(c) 任意区域概率可加性**：对任意子集 $A \subset \mathbb{S}$，随机向量落入 $A$ 的概率为： 

  $$
  P\big((X_1, \dots, X_n) \in A\big) = \sum_{(x_1, \dots, x_n) \in A} f(x_1, \dots, x_n)
  $$

  > **【课件细节注记】** Slide P4 性质 (c) 左端写作 $P((x_1, \dots, x_n) \in A)$，在严格概率论记号中，大写字母代表随机变量，小写字母代表确定取值，因此规范写法应为 $P\big((X_1, \dots, X_n) \in A\big)$。

### 2. 边缘概率质量函数（Marginal PMF, Slide P5–P6）

#### （1）二维情形与联合分布表（Slide P5）

设 $X_1$ 的可能取值为 $a_1, a_2, \dots$，$X_2$ 的可能取值为 $b_1, b_2, \dots$，记联合概率 $p_{ij} = P(X_1 = a_i, X_2 = b_j)$。二维联合分布可用如下列联表直观表示：

| $X_1 \backslash X_2$ | $b_1$ | $b_2$ | $\cdots$ | $b_j$ | $\cdots$ | **行求和（**$X_1$ **的边缘分布** $p_{i\cdot}$**）** | 
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | 
| $a_1$ | $p_{11}$ | $p_{12}$ | $\cdots$ | $p_{1j}$ | $\cdots$ | $p_{1\cdot} = \sum_j p_{1j}$ | 
| $a_2$ | $p_{21}$ | $p_{22}$ | $\cdots$ | $p_{2j}$ | $\cdots$ | $p_{2\cdot} = \sum_j p_{2j}$ | 
| $\vdots$ | $\vdots$ | $\vdots$ | $\ddots$ | $\vdots$ | $\ddots$ | $\vdots$ | 
| $a_i$ | $p_{i1}$ | $p_{i2}$ | $\cdots$ | $p_{ij}$ | $\cdots$ | $p_{i\cdot} = \sum_j p_{ij}$ | 
| $\vdots$ | $\vdots$ | $\vdots$ | $\ddots$ | $\vdots$ | $\ddots$ | $\vdots$ | 
| **列求和（**$X_2$ **的边缘分布** $p_{\cdot j}$**）** | $p_{\cdot 1} = \sum_i p_{i1}$ | $p_{\cdot 2} = \sum_i p_{i2}$ | $\cdots$ | $p_{\cdot j} = \sum_i p_{ij}$ | $\cdots$ | **总和** $\sum_i \sum_j p_{ij} = 1$ | 

* $X_1$ **的边缘 PMF（按行求和，消去** $X_2$**）**： 

  $$
  f_{X_1}(a_i) = P(X_1 = a_i) = \sum_j P(X_1 = a_i, X_2 = b_j) = \sum_j p_{ij} = p_{i\cdot}
  $$

* $X_2$ **的边缘 PMF（按列求和，消去** $X_1$**）**： 

  $$
  f_{X_2}(b_j) = P(X_2 = b_j) = \sum_i P(X_1 = a_i, X_2 = b_j) = \sum_i p_{ij} = p_{\cdot j}
  $$

> **【课件勘误提醒（Slide P5）】**
>
> * 在 Slide P5 倒数第三行求 $X_2$ 的边缘分布时，课件写成了： 
>
>   $$
>   f_{X_2}(b_j) = P(X_2 = b_j) = \sum_i P(X_1 = a_i, X_2 = b_j) = \sum_j p_{ij} = p_{\cdot j}
>   $$
>
> * 其中第二个求和号下标 $\sum_j p_{ij}$ 属于**笔误**，正确写法应为对行标 $i$ 求和：$\sum_i p_{ij} = p_{\cdot j}$（固定列标 $j$，遍历所有行 $i$）。
>
> * **为什么叫“边缘（Marginal）”分布？** 因为在二维表格中，$X_1$ 和 $X_2$ 各自的分布恰好写在表格的最右侧边缘列和最底部边缘行，故得名“边缘分布”。

#### （2）$n$ 维一般情形与去一向量记号（Slide P6）

为了简洁书写 $n$ 维情形，课件引入了非常实用的**去第** $j$ **分量记号（Leave-one-out Notation）**：

* 记去除第 $j$ 个随机变量后的 $(n-1)$ 维随机向量为： 

  $$
  \tilde{X}_{-j} = (X_1, \dots, X_{j-1}, X_{j+1}, \dots, X_n)
  $$

* 其对应的取值与状态空间分别为： 

  $$
  \tilde{x}_{-j} = (x_1, \dots, x_{j-1}, x_{j+1}, \dots, x_n) \in \mathbb{S}_{-j} = \mathbb{X}_1 \times \dots \times \mathbb{X}_{j-1} \times \mathbb{X}_{j+1} \times \dots \times \mathbb{X}_n
  $$

* 则 $X_j$ 的**边缘 PMF** 定义为对所有其余 $(n-1)$ 个变量取值的多重求和： 

  $$
  f_{X_j}(x_j) = P(X_j = x_j) = \sum_{\tilde{x}_{-j} \in \mathbb{S}_{-j}} f(x_1, \dots, x_n)
  $$

### 3. 离散型随机变量的相互独立性（Mutual Independence, Slide P6）

#### （1）定义

随机变量 $X_1, \dots, X_n$ 称为**相互独立（Mutually Independent）**，当且仅当对联合空间中的**任意**取值点 $\forall (x_1, \dots, x_n) \in \mathbb{S}$，都有： 

$$
P(X_1 = x_1, \dots, X_n = x_n) = \prod_{i=1}^n P(X_i = x_i) \quad \Longleftrightarrow \quad f(x_1, \dots, x_n) = \prod_{i=1}^n f_{X_i}(x_i)
$$

#### （2）疑难深度剖析：判断独立性的三大核心要点

1. **证伪只需一个反例，证明必须遍历全空间**：

   * 要说明 $X, Y$ **不独立**，只需找到**一对**具体数值 $(x_0, y_0)$，使得 $f(x_0, y_0) \ne f_X(x_0)f_Y(y_0)$ 即可（如 Example 3.1 与 Example 3.2）。

   * 要证明 $X, Y$ **独立**，则必须对所有可能的 $(x, y)$ 验证等式恒成立。

2. **支撑集（Support）几何判别法（秒杀技巧）**：

   * 若 $X_1, \dots, X_n$ 相互独立，则其联合支撑集 $\{(x_1,\dots,x_n): f(x_1,\dots,x_n) > 0\}$ **必然是各变量边缘支撑集的笛卡尔积（即二维下的矩形区域或网格点阵）**。

   * **推论**：只要有效取值的边界满足类似 $x \le y$、$x + y \le 1$ 等变量间相互制约的不等式（即非矩形支撑集），则变量**一定不独立**！

3. **两两独立（Pairwise Independence）**$\ne$ **相互独立（Mutual Independence）**：

   * 当 $n \ge 3$ 时，任意两个变量独立并不能推出全体相互独立；而Slide P6 定义的 $f(x_1,\dots,x_n) = \prod_{i=1}^n f_{X_i}(x_i)$ 是最强的**相互独立**，它自动蕴含任意子集之间的独立性。

### 4. 条件概率质量函数（Conditional PMF, Slide P7）

#### （1）定义

设 $(X_1, \dots, X_n)$ 的联合 PMF 为 $f(x_1, \dots, x_n)$。在给定其余变量取值 $\tilde{X}_{-j} = \tilde{x}_{-j}$ 且满足边缘概率 $f_{\tilde{X}_{-j}}(\tilde{x}_{-j}) > 0$ 的条件下，$X_j$ 的**条件 PMF** 定义为： 

$$
f_{X_j \mid \tilde{X}_{-j} = \tilde{x}_{-j}}\left(x_j \mid \tilde{X}_{-j} = \tilde{x}_{-j}\right) = \frac{f(x_1, \dots, x_n)}{f_{\tilde{X}_{-j}}(\tilde{x}_{-j})} = \frac{f(x_1, \dots, x_n)}{\sum_{x_j \in \mathbb{X}_j} f(x_1, \dots, x_n)}
$$

#### （2）本质理解

* **来自条件概率公式**：在二维情形下，即 $f_{X\mid Y}(x\mid y) = P(X=x \mid Y=y) = \frac{P(X=x, Y=y)}{P(Y=y)} = \frac{f(x,y)}{f_Y(y)}$。

* **截面归一化视角**：固定条件变量 $\tilde{x}_{-j}$ 后，分子 $f(x_1, \dots, x_n)$ 只是 $x_j$ 的一元函数，而分母 $f_{\tilde{X}_{-j}}(\tilde{x}_{-j}) = \sum_{x_j} f(x_1, \dots, x_n)$ 是一个与 $x_j$ 无关的**归一化常数**，确保条件概率关于 $x_j$ 求和等于 $1$。

### 5. 经典例题深度精讲：Example 3.1（Slide P8–P10）

> **题目（Example 3.1）**：投掷一对均匀的六面骰子，共有 36 个等可能样本点（每个样本点概率为 $1/36$）。设 $X$ 表示两枚骰子中较小的点数，$Y$ 表示较大的点数（即 $X = \min(D_1, D_2), Y = \max(D_1, D_2)$）。
>
> * (a) 求 $(X, Y)$ 的联合 PMF，并由联合 PMF 推导 $X$ 和 $Y$ 的边缘 PMF；
>
> * (b) 判断 $X, Y$ 是否相互独立；
>
> * (c) 求给定 $Y = 4$ 条件下 $X$ 的条件 PMF。

#### 【完整解析与拓展】

##### (a) 联合 PMF 与边缘 PMF 推导

设第一枚骰子点数为 $D_1$，第二枚为 $D_2$，样本点 $(D_1, D_2) \in \{1,2,3,4,5,6\}^2$。 由于 $X = \min(D_1, D_2)$，$Y = \max(D_1, D_2)$，必然有 $1 \le x \le y \le 6$（若 $x > y$，概率必为 $0$）。

* **情形 1：当** $x = y$ **时**（两枚骰子点数相同）： 事件 $\{X=x, Y=x\}$ 仅对应唯一样本点 $\{(x, x)\}$，故： 

  $$
  f(x, x) = P(\{(x, x)\}) = \frac{1}{36}, \quad x = 1, 2, \dots, 6
  $$

* **情形 2：当** $1 \le x < y \le 6$ **时**（两枚骰子点数不同）： 事件 $\{X=x, Y=y\}$ 对应两个对称样本点 $\{(x, y), (y, x)\}$（即第一枚掷出 $x$ 第二枚掷出 $y$，或反之），故： 

  $$
  f(x, y) = P(\{(x, y), (y, x)\}) = \frac{2}{36}, \quad 1 \le x < y \le 6
  $$

汇总得联合 PMF： 

$$
f(x, y) = P(X = x, Y = y) = \begin{cases} \dfrac{1}{36}, & \text{if } 1 \le x = y \le 6 \\ \dfrac{2}{36}, & \text{if } 1 \le x < y \le 6 \\ 0, & \text{otherwise} \end{cases}
$$

**【直观补充：**$(X,Y)$ **的** $6\times 6$ **联合分布与边缘分布全表】**

| $X \backslash Y$ | $y=1$ | $y=2$ | $y=3$ | $y=4$ | $y=5$ | $y=6$ | **行和** $f_X(x)$ | 
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | 
| $x=1$ | $1/36$ | $2/36$ | $2/36$ | $2/36$ | $2/36$ | $2/36$ | $11/36$ | 
| $x=2$ | $0$ | $1/36$ | $2/36$ | $2/36$ | $2/36$ | $2/36$ | $9/36$ | 
| $x=3$ | $0$ | $0$ | $1/36$ | $2/36$ | $2/36$ | $2/36$ | $7/36$ | 
| $x=4$ | $0$ | $0$ | $0$ | $1/36$ | $2/36$ | $2/36$ | $5/36$ | 
| $x=5$ | $0$ | $0$ | $0$ | $0$ | $1/36$ | $2/36$ | $3/36$ | 
| $x=6$ | $0$ | $0$ | $0$ | $0$ | $0$ | $1/36$ | $1/36$ | 
| **列和** $f_Y(y)$ | $1/36$ | $3/36$ | $5/36$ | $7/36$ | $9/36$ | $11/36$ | **总和** $36/36 = 1$ | 

* **求** $X$ **的边缘 PMF** $f_X(x)$（固定行 $x$，对 $y$ 从 $x$ 到 $6$ 求和）： 其中 $y = x$ 这一项为 $1/36$，而 $y \in \{x+1, \dots, 6\}$ 共 $(6-x)$ 项均为 $2/36$： 

  $$
  f_X(x) = \sum_{y=x}^6 f(x, y) = f(x, x) + \sum_{y=x+1}^6 f(x, y) = \frac{1}{36} + \frac{2(6 - x)}{36} = \frac{13 - 2x}{36}, \quad x = 1, \dots, 6
  $$

* **求** $Y$ **的边缘 PMF** $f_Y(y)$（固定列 $y$，对 $x$ 从 $1$ 到 $y$ 求和）： 其中 $x = y$ 这一项为 $1/36$，而 $x \in \{1, \dots, y-1\}$ 共 $(y-1)$ 项均为 $2/36$： 

  $$
  f_Y(y) = \sum_{x=1}^y f(x, y) = \sum_{x=1}^{y-1} f(x, y) + f(y, y) = \frac{2(y - 1)}{36} + \frac{1}{36} = \frac{2y - 1}{36}, \quad y = 1, \dots, 6
  $$

##### (b) 独立性判定与课件笔误修正

* **方法一（课件反例法 + 勘误）**：
  取 $x = 1, y = 2$，由联合分布知 $f(1, 2) = \frac{2}{36}$。
  而边缘概率分别为 $f_X(1) = \frac{13-2(1)}{36} = \frac{11}{36}$，$f_Y(2) = \frac{2(2)-1}{36} = \frac{3}{36}$。

  > **【课件勘误提醒（Slide P9）】** 课件在计算 $f_X(1)f_Y(2)$ 时写成了 $\frac{11}{36} \times \frac{1}{36} \ne \frac{2}{36}$（把 $f_Y(1)=\frac{1}{36}$ 误代入了 $f_Y(2)$）。准确数值应为：
  > 
  >
  > $$
  > f_X(1)f_Y(2) = \frac{11}{36} \times \frac{3}{36} = \frac{33}{1296} \ne \frac{2}{36}
  > $$
  >
  > 
  > 结论不变，$X$ 与 $Y$ **不独立**。

* **方法二（零概率点/支撑集秒杀法）**：
  直接取下三角区域的点，例如 $x = 2, y = 1$：由于最小值不可能大于最大值，必有 $f(2, 1) = 0$；但 $f_X(2) = \frac{9}{36} > 0, f_Y(1) = \frac{1}{36} > 0$，显然 $0 \ne \frac{9}{36} \times \frac{1}{36}$，一秒证伪！

##### (c) 给定 $Y = 4$ 下 $X$ 的条件 PMF（Slide P10）

1. 先求条件事件的分母边缘概率：
   

   $$
   f_Y(4) = \frac{2(4) - 1}{36} = \frac{7}{36}
   $$

2. 再列出 $Y = 4$ 这一列的联合概率截面 $f(x, 4)$：
   

   $$
   f(x, 4) = P(X = x, Y = 4) = \begin{cases} 1/36, & \text{if } x = 4 \\ 2/36, & \text{if } x = 1, 2, 3 \\ 0, & \text{otherwise} \end{cases}
   $$

3. 相除即得条件 PMF：
   

   $$
   f_{X\mid Y=4}(x \mid Y = 4) = \frac{f(x, 4)}{f_Y(4)} = \begin{cases} 1/7, & \text{if } x = 4 \\ 2/7, & \text{if } x = 1, 2, 3 \\ 0, & \text{otherwise} \end{cases}
   $$

   
   *检验归一性*：$\frac{2}{7} \times 3 + \frac{1}{7} = \frac{7}{7} = 1$，完全正确。

## 三、3.2 多维连续型随机变量（Continuous Type）

### 1. 联合、边缘与条件概率密度函数（Slide P12–P15）

#### （1）联合概率密度函数（Joint PDF, Slide P12）

设 $X_1, \dots, X_n$ 为连续型随机变量，若存在非负可积函数 $f(x_1, \dots, x_n)$，使得对任意区域 $A \subset \mathbb{R}^n$ 有：

$$
P\big((X_1, \dots, X_n) \in A\big) = \int \dots \int_{(x_1, \dots, x_n) \in A} f(x_1, \dots, x_n)\,dx_1 \dots dx_n
$$


则称 $f(x_1, \dots, x_n)$ 为联合 PDF。它满足：

* **(a)** $f(x_1, \dots, x_n) \ge 0, \quad \forall (x_1, \dots, x_n) \in \mathbb{R}^n$

* **(b)** $\int_{\mathbb{R}^n} f(x_1, \dots, x_n)\,d(x_1, \dots, x_n) = 1$

> **【疑难辨析：密度的值为什么可以大于 1？】**
> 概率是体积（面积），而密度 $f(x_1,\dots,x_n)$ 是“单位体积上的概率高度”，只有乘以无穷小体积微元后才是概率：
> 
>
> $$
> P(x_1 \le X_1 \le x_1 + dx_1, \dots, x_n \le X_n \le x_n + dx_n) \approx f(x_1, \dots, x_n)\,dx_1 \dots dx_n
> $$
>
> 
> 例如后面 Example 3.3 中 $f(1,1) = \frac{30}{7} > 1$，完全合法，只要全空间积分为 $1$ 即可。

#### （2）边缘概率密度函数（Marginal PDF, Slide P13）

记 $\tilde{X}_{-j} = (X_1, \dots, X_{j-1}, X_{j+1}, \dots, X_n)$，则 $X_j$ 的边缘 PDF 通过对所有其余 $(n-1)$ 个变量在 $\mathbb{R}^{n-1}$ 上积分得到：

$$
f_{X_j}(x_j) = \int_{\tilde{x}_{-j} \in \mathbb{R}^{n-1}} f(x_1, \dots, x_n)\,d\tilde{x}_{-j}
$$

* **二维特例**（最常用）：
  

  $$
  f_X(x) = \int_{-\infty}^{+\infty} f(x, y)\,dy \quad (\text{消去 } y), \qquad f_Y(y) = \int_{-\infty}^{+\infty} f(x, y)\,dx \quad (\text{消去 } x)
  $$

#### （3）连续型随机变量的相互独立性（Slide P14）

$X_1, \dots, X_n$ 相互独立 $\Longleftrightarrow \forall (x_1, \dots, x_n) \in \mathbb{R}^n$（除零测度集外），联合 PDF 可分解为边缘 PDF 的乘积：

$$
f(x_1, \dots, x_n) = \prod_{i=1}^n f_{X_i}(x_i)
$$

> **【实用定理：可分离变量判据（Factorization Criterion）】**
> 在做题时，无需先求边缘分布即可直接判断独立性：$X, Y$ 相互独立的充要条件是：
>
> 1. **联合支撑集是矩形区域**（即 $a \le x \le b,\; c \le y \le d$，上下限互不含对方变量）；
>
> 2. **在支撑集内部，联合密度可拆成纯** $x$ **函数与纯** $y$ **函数的乘积**：$f(x, y) = g(x)h(y)$。

#### （4）条件概率密度函数（Conditional PDF, Slide P15）

当给定条件点的边缘密度 $f_{\tilde{X}_{-j}}(\tilde{x}_{-j}) > 0$ 时，$X_j$ 的条件 PDF 为：

$$
f_{X_j \mid \tilde{X}_{-j} = \tilde{x}_{-j}}\left(x_j \mid \tilde{X}_{-j} = \tilde{x}_{-j}\right) = \frac{f(x_1, \dots, x_n)}{f_{\tilde{X}_{-j}}(\tilde{x}_{-j})} = \frac{f(x_1, \dots, x_n)}{\int_{x_j \in \mathbb{R}} f(x_1, \dots, x_n)\,dx_j}
$$

> **【深度原理解析：连续型随机变量单点概率** $P(Y=y)=0$**，为什么还能定义给定** $Y=y$ **的条件分布？】**
> 初学者常困惑：在初等条件概率 $P(A\mid B) = \frac{P(AB)}{P(B)}$ 中，若 $B = \{Y = y\}$，则分母 $P(Y=y)=0$，公式直接失效！
> **严格数学解释**：连续型的条件分布是通过无穷小区间 $\{y \le Y \le y + \Delta y\}$ 取极限定义的：
> 
>
> $$
> F_{X\mid Y}(x \mid y) = \lim_{\Delta y \to 0^+} P(X \le x \mid y \le Y \le y + \Delta y) = \lim_{\Delta y \to 0^+} \frac{\int_{-\infty}^x \left[\int_y^{y+\Delta y} f(u, v)\,dv\right] du}{\int_y^{y+\Delta y} f_Y(v)\,dv}
> $$
>
> 
> 当 $f$ 与 $f_Y$ 连续且 $f_Y(y) > 0$ 时，由积分中值定理，分子约为 $\left(\int_{-\infty}^x f(u, y)\,du\right) \Delta y$，分母约为 $f_Y(y)\Delta y$，约去微元 $\Delta y$ 后对 $x$ 求导，便得到了 $f_{X\mid Y}(x\mid y) = \frac{f(x,y)}{f_Y(y)}$！

### 2. 经典例题深度精讲：Example 3.2 & Example 3.3（Slide P16–P21）

#### 例题 3.2：矩形支撑集上的多项式密度（Slide P16–P18）

> **题目（Example 3.2）**：设 $X, Y$ 的联合 PDF 为 $f(x, y) = \frac{4}{3}(1 - xy), \quad \forall x \in [0, 1],\; y \in [0, 1]$（其余区域为 $0$）。
>
> * (a) 求 $X, Y$ 的边缘 PDF；
>
> * (b) 判断 $X, Y$ 是否独立；
>
> * (c) 求给定 $Y = 1$ 时 $X$ 的条件 PDF。

**【完整解析】**

* **(a) 求边缘 PDF**：

  * 对 $\forall x \in [0, 1]$，把 $x$ 看作常数，对 $y$ 在 $[0, 1]$ 上积分：
    

    $$
    f_X(x) = \int_0^1 \frac{4}{3}(1 - xy)\,dy = \frac{4}{3}\left[y - \frac{1}{2}xy^2\right]_{y=0}^{y=1} = \frac{4}{3}\left(1 - \frac{x}{2}\right), \quad x \in [0, 1]
    $$

  * 由对称性，对 $\forall y \in [0, 1]$：
    

    $$
    f_Y(y) = \int_0^1 \frac{4}{3}(1 - xy)\,dx = \frac{4}{3}\left(1 - \frac{y}{2}\right), \quad y \in [0, 1]
    $$

  > **【书写规范提醒】** 考试答题时务必注明定义域（即当 $x \notin [0,1]$ 时 $f_X(x) = 0$）。

* **(b) 独立性判定**：
  虽然支撑集 $[0,1]\times[0,1]$ 是矩形，但 $1 - xy$ 无法分解为 $g(x)h(y)$。取特殊点 $x = 1, y = 1$：
  

  $$
  f(1, 1) = \frac{4}{3}(1 - 1\times 1) = 0, \qquad f_X(1) = f_Y(1) = \frac{4}{3}\left(1 - \frac{1}{2}\right) = \frac{2}{3}
  $$

  
  显然 $f(1, 1) = 0 \ne f_X(1)f_Y(1) = \frac{4}{9}$，故 $X, Y$ **不独立**。

* **(c) 条件 PDF** $f_{X\mid Y=1}(x\mid Y=1)$：
  已知 $f_Y(1) = \frac{2}{3}$，$f(x, 1) = \frac{4}{3}(1 - x)$，故：
  

  $$
  f_{X\mid Y=1}(x \mid Y = 1) = \frac{f(x, 1)}{f_Y(1)} = \frac{\frac{4}{3}(1 - x)}{2/3} = \begin{cases} 2(1 - x), & \text{if } x \in [0, 1] \\ 0, & \text{otherwise} \end{cases}
  $$

#### 例题 3.3：非矩形（梯形）支撑集与分段边缘积分（Slide P19–P21，本章高频易错核心题！）

> **题目（Example 3.3）**：设 $X, Y$ 的联合 PDF 为：
> 
>
> $$
> f(x, y) = \begin{cases} c x^2 y, & \text{if } 0 \le y \le 1,\; -y \le x \le 1 \\ 0, & \text{otherwise} \end{cases}
> $$
>
> * (a) 求归一化常数 $c$；
>
> * (b) 求 $X, Y$ 的边缘 PDF；
>
> * (c) 判断 $X, Y$ 是否独立；
>
> * (d) 求给定 $Y = 1/2$ 时 $X$ 的条件 PDF。

**【疑难拆解与完整解析】**

##### 第一步：画出支撑集几何图形（做非矩形区域题目的灵魂！）

不等式组 $\begin{cases} 0 \le y \le 1 \\ -y \le x \le 1 \end{cases}$ 在 $(x, y)$ 平面上围成一个**直角梯形区域**（见 Slide P21 右上角 Figure 1）：

* 上底：$y = 1$（从 $(-1, 1)$ 到 $(1, 1)$，长度为 $2$）

* 下底：$y = 0$（从 $(0, 0)$ 到 $(1, 0)$，长度为 $1$）

* 左斜边：$x = -y \Longleftrightarrow y = -x$（连接 $(-1, 1)$ 与 $(0, 0)$）

* 右直边：$x = 1$（连接 $(1, 0)$ 与 $(1, 1)$）

##### (a) 求常数 $c$（利用归一性二重积分）

由于 $y$ 的范围是常数区间 $[0, 1]$，而 $x$ 的范围 $[-y, 1]$ 依赖于 $y$，因此**先对** $x$ **积分、后对** $y$ **积分**不用分段（注意 Slide P20 第一行积分上限写成了 $-y \le x \le 1-$，末尾多了一个横杠，属于排版小笔误）：

$$
\int_{\mathbb{R}^2} f(x, y)\,dx\,dy = \int_0^1 \left(\int_{-y}^1 c x^2 y\,dx\right) dy = \int_0^1 c y \left[\frac{x^3}{3}\right]_{x=-y}^{x=1} dy = \int_0^1 \frac{c}{3} y (1 + y^3)\,dy
$$

$$
= \frac{c}{3} \int_0^1 (y + y^4)\,dy = \frac{c}{3}\left[\frac{y^2}{2} + \frac{y^5}{5}\right]_0^1 = \frac{c}{3} \cdot \frac{7}{10} = \frac{7c}{30} = 1 \implies c = \frac{30}{7}
$$

##### (b) 求边缘 PDF（重点攻克：为什么求 $f_X(x)$ 必须分成两段？）

* **求** $f_X(x) = \int_{-\infty}^{+\infty} f(x, y)\,dy$**（固定横坐标** $x$**，作一条竖直线向上穿过阴影梯形）**：
  观察梯形的下边界：

  * **当** $x \in [-1, 0]$ **时**：竖直线从左斜边 $y = -x$ 进入阴影区，从上边界 $y = 1$ 穿出！因此 $y$ 的积分区间为 $[-x, 1]$：
    

    $$
    f_X(x) = \int_{-x}^1 \frac{30}{7} x^2 y\,dy = \frac{30}{7} x^2 \left[\frac{y^2}{2}\right]_{y=-x}^{y=1} = \frac{15}{7} x^2 (1 - x^2), \quad x \in [-1, 0]
    $$

  * **当** $x \in [0, 1]$ **时**：竖直线从横轴 $y = 0$ 进入阴影区，从上边界 $y = 1$ 穿出！因此 $y$ 的积分区间为 $[0, 1]$：
    

    $$
    f_X(x) = \int_0^1 \frac{30}{7} x^2 y\,dy = \frac{30}{7} x^2 \left[\frac{y^2}{2}\right]_{y=0}^{y=1} = \frac{15}{7} x^2, \quad x \in [0, 1]
    $$

  * 汇总得 $X$ 的分段边缘 PDF：
    

    $$
    f_X(x) = \begin{cases} \dfrac{15}{7}x^2(1 - x^2), & \text{if } x \in [-1, 0] \\[6pt] \dfrac{15}{7}x^2, & \text{if } x \in [0, 1] \\[6pt] 0, & \text{otherwise} \end{cases}
    $$

* **求** $f_Y(y) = \int_{-\infty}^{+\infty} f(x, y)\,dx$**（固定纵坐标** $y \in [0, 1]$**，作一条水平线向右穿过阴影梯形）**：
  无论 $y$ 在 $[0, 1]$ 何处，水平线始终从左斜边 $x = -y$ 进入，从右边界 $x = 1$ 穿出，无需分段：
  

  $$
  f_Y(y) = \begin{cases} \displaystyle\int_{-y}^1 \frac{30}{7} x^2 y\,dx = \frac{10}{7}(y + y^4), & \text{if } y \in [0, 1] \\[8pt] 0, & \text{otherwise} \end{cases}
  $$

##### (c) 独立性判定

* **课件反例法**：取 $x = 1, y = 1$，有 $f(1, 1) = \frac{30}{7}$，$f_X(1) = \frac{15}{7}$，$f_Y(1) = \frac{20}{7}$。因为 $\frac{30}{7} \ne \frac{15}{7} \times \frac{20}{7}$，所以 $X, Y$ **不独立**。

* **支撑集直观结论**：因为支撑集是梯形（非矩形），例えば取点 $(-0.5, 0.2)$，此时 $x \in [-1,1], y \in [0,1]$ 使得 $f_X(-0.5)>0, f_Y(0.2)>0$，但因 $x < -y$ 在梯形外，故 $f(-0.5, 0.2) = 0$，必然不独立。

##### (d) 求给定 $Y = 1/2$ 时 $X$ 的条件 PDF（含课件勘误与速算技巧）

* **常规代公式法**：

  1. 先计算 $y = 1/2$ 处的边缘密度：
     

     $$
     f_Y\left(\frac{1}{2}\right) = \frac{10}{7}\left(\frac{1}{2} + \left(\frac{1}{2}\right)^4\right) = \frac{10}{7} \times \frac{9}{16} = \frac{45}{56}
     $$

  2. 当 $Y = 1/2$ 时，由 $-y \le x \le 1$ 知 $x$ 的有效支撑集变为 $x \in [-1/2, 1]$，且分子为：
     

     $$
     f\left(x, \frac{1}{2}\right) = \frac{30}{7} x^2 \left(\frac{1}{2}\right) = \frac{15}{7} x^2, \quad x \in \left[-\frac{1}{2}, 1\right]
     $$

  3. 相除得条件 PDF：
     

     $$
     f_{X\mid Y=1/2}\left(x \;\middle|\; Y = \frac{1}{2}\right) = \frac{f(x, 1/2)}{f_Y(1/2)} = \frac{\frac{15}{7}x^2}{\frac{45}{56}} = \begin{cases} \dfrac{8}{3}x^2, & \text{if } x \in \left[-\dfrac{1}{2}, 1\right] \\[6pt] 0, & \text{otherwise} \end{cases}
     $$

> **【课件勘误提醒（Slide P21 (d)）】**
> Slide P21 最后一行在书写公式左端与中间分式时，误将 $Y = 1/2$ 写成了 $Y = 1$（印成了 $f_{X\mid Y=1}(x\mid Y=1) = \frac{f(x,1)}{f_Y(1)}$），但右端计算结果 $\frac{8}{3}x^2, x \in [-1/2, 1]$ 实际上对应的是正确的 $Y = 1/2$（若真是 $Y=1$，结果应为 $\frac{30/7 x^2}{20/7} = \frac{3}{2}x^2, x \in [-1, 1]$）。复习时务必修正左端记号！

> **【秒杀技巧：条件密度“核函数（Kernel）归一化法”】**
> 观察联合密度 $f(x, y) = \frac{30}{7} x^2 y$，当固定 $Y = 1/2$ 时，关于变量 $x$ 的函数形状（核，Kernel）正比于 $x^2$，且支撑集为 $x \in [-1/2, 1]$。
> 因此 $f_{X\mid Y=1/2}(x \mid 1/2) = k \cdot x^2$。由 $\int_{-1/2}^1 k x^2\,dx = k \left[\frac{x^3}{3}\right]_{-1/2}^1 = k \cdot \frac{1 + 1/8}{3} = \frac{3}{8}k = 1 \implies k = \frac{8}{3}$，无需先算 $f_Y(1/2)$ 即可直接秒出答案并用于验算！

## 四、3.3 多维随机变量的函数变换与三大导出分布（Change of Variables & Derived Distributions）

### 1. 多维连续型随机变量变换公式与雅可比行列式（Slide P23–P24）

#### （1）定理与公式表述

设 $\mathbf{X} = (X_1, \dots, X_n)^T$ 为连续型随机向量，联合 PDF 为 $f_{\mathbf{X}}(\mathbf{x})$，支撑集为 $S_X \subset \mathbb{R}^n$。
设变换 $\mathbf{Y} = g(\mathbf{X})$ 将 $S_X$ 一一映射（可逆映射，Invertible Mapping）到 $S_Y \subset \mathbb{R}^n$，其逆变换为 $\mathbf{X} = g^{-1}(\mathbf{Y})$ 且连续可微。

* **正向雅可比矩阵（Slide P24）**：
  

  $$
  J_{x \to y} \stackrel{\text{def}}{=} \frac{\partial(y_1, \dots, y_n)}{\partial(x_1, \dots, x_n)} = \begin{bmatrix} \dfrac{\partial y_1}{\partial x_1} & \cdots & \dfrac{\partial y_1}{\partial x_n} \\ \vdots & \ddots & \vdots \\ \dfrac{\partial y_n}{\partial x_1} & \cdots & \dfrac{\partial y_n}{\partial x_n} \end{bmatrix}
  $$

  
  *(注：Slide P24 分子写成* $\partial(y_1,\dots,y_m)$*，其中* $m$ *应为* $n$*，因为可逆方阵要求维数相同)*。

* **逆向雅可比矩阵（实际代入公式所使用的矩阵！）**：
  

  $$
  J_{y \to x} \stackrel{\text{def}}{=} \frac{\partial(x_1, \dots, x_n)}{\partial(y_1, \dots, y_n)} = \begin{bmatrix} \dfrac{\partial x_1}{\partial y_1} & \cdots & \dfrac{\partial x_1}{\partial y_n} \\ \vdots & \ddots & \vdots \\ \dfrac{\partial x_n}{\partial y_1} & \cdots & \dfrac{\partial x_n}{\partial y_n} \end{bmatrix} = \left(J_{x \to y}\right)^{-1}
  $$

* **变换后的联合概率密度公式**：
  

  $$
  f_{\mathbf{Y}}(\mathbf{y}) = \begin{cases} f_{\mathbf{X}}\big(g^{-1}(\mathbf{y})\big) \cdot \left|\det J_{y \to x}\right|, & \mathbf{y} \in S_Y \\ 0, & \text{otherwise} \end{cases}
  $$

#### （2）核心疑难解析：为什么乘的是 $\left|\det J_{y \to x}\right|$ 且要加绝对值？

1. **源于多元微积分换元法**：
   在计算区域概率 $\int_A f_{\mathbf{X}}(\mathbf{x})\,d\mathbf{x}$ 时，将积分变量从 $\mathbf{x}$ 换为 $\mathbf{y}$，微元体积（面积）的缩放关系为：
   

   $$
   dx_1 \dots dx_n = \left|\det \frac{\partial(x_1, \dots, x_n)}{\partial(y_1, \dots, y_n)}\right| dy_1 \dots dy_n = \left|\det J_{y \to x}\right| dy_1 \dots dy_n
   $$

2. **为什么要加绝对值** $|\cdot|$**？**
   行列式的正负号代表坐标变换是否翻转了空间定向（如镜像反射会使行列式为负），而概率密度和体积微元必须始终**非负**，因此必须取绝对值。

3. **如果直接求** $J_{x \to y}$ **更容易怎么办？**
   由逆矩阵行列式性质，有 $\det J_{y \to x} = \frac{1}{\det J_{x \to y}}$。若反解 $x = g^{-1}(y)$ 后的偏导不好算，也可以先算 $\det J_{x \to y}$ 再取倒数！

#### （3）降维变换的“辅助变量法（Auxiliary Variable Method）”标准五步流程

在实际问题中（如求 $T = \frac{X}{\sqrt{Y/\nu}}$ 或 $F = \frac{X/u}{Y/v}$ 的一维分布），已知的是**二维**随机变量 $(X, Y)$，要求的只是**一维**目标变量 $T = h(X, Y)$ 的分布。为了使用可逆变换公式，标准操作五步法如下：

1. **引入辅助变量**：设目标变量为 $U = h(X, Y)$，人为补充一个简单的辅助变量 $W = Y$（或 $W = X$），凑成 $\mathbb{R}^2 \to \mathbb{R}^2$ 的双射 $(X, Y) \mapsto (U, W)$。

2. **反解原变量并确定新支撑集**：用 $(U, W)$ 表示 $(X, Y)$，即写出 $X = x(U, W), Y = W$，并由 $(X, Y)$ 的原取值范围推导出 $(U, W)$ 的取值范围 $S_{U,W}$。

3. **计算雅可比行列式**：因为 $Y = W$，二阶雅可比矩阵的第二行必为 $\begin{bmatrix} \frac{\partial Y}{\partial U} & \frac{\partial Y}{\partial W} \end{bmatrix} = \begin{bmatrix} 0 & 1 \end{bmatrix}$，从而行列式极易计算：
   

   $$
   |J| = \left|\det \begin{bmatrix} \dfrac{\partial X}{\partial U} & \dfrac{\partial X}{\partial W} \\ 0 & 1 \end{bmatrix}\right| = \left|\frac{\partial X}{\partial U}\right|
   $$

4. **写出联合 PDF**：$f_{U,W}(u, w) = f_{X,Y}\big(x(u, w), w\big) \cdot |J|$。

5. **积分消去辅助变量** $W$：求边缘密度 $f_U(u) = \int_{-\infty}^{+\infty} f_{U,W}(u, w)\,dw$。

### 2. 推导 $t$ 分布与 $F$ 分布的终极武器：凑 Gamma 密度积分法（Gamma Trick）

在 Slide P30–P31（推导 $t$ 分布）和 Slide P42–P43（推导 $F$ 分布）中，最核心的计算难点都是第 5 步对辅助变量 $w \in (0, \infty)$ 的积分。掌握以下**Gamma 分布核积分公式**，所有推导将迎刃而解！

* **Gamma 分布** $\text{Gam}(a, b)$ **的概率密度函数**（采用形状参数 $a > 0$，速率参数 $b > 0$）：
  

  $$
  f(w; a, b) = \frac{b^a}{\Gamma(a)} w^{a-1} e^{-b w}, \quad w > 0
  $$

* **利用归一性** $\int_0^\infty f(w; a, b)\,dw = 1$**，移项即得万能积分恒等式**：
  

  $$
  \boxed{\int_0^\infty w^{a-1} e^{-b w}\,dw = \frac{\Gamma(a)}{b^a}}
  $$

* **考场速记口诀**：看到 $\int_0^\infty w^{\text{幂次}-1} e^{-\text{系数}\cdot w}\,dw$，无需分部积分，直接套用 $\frac{\Gamma(\text{幂次})}{(\text{系数})^{\text{幂次}}}$！

### 3. 三大统计导出分布深度推导与剖析（Slide P25–P43）

#### （1）Student's $t$ 分布（Slide P26–P31）

##### ① 定义（Slide P26）

设 $X \sim N(0, 1)$（标准正态分布），$Y \sim \chi^2(\nu)$（自由度为 $\nu$ 的卡方分布），且 $X$ **与** $Y$ **相互独立**。定义随机变量：

$$
T = \frac{X}{\sqrt{Y / \nu}}
$$


则称 $T$ 服从自由度为 $\nu$ 的 $t$ **分布（Student's** $t$**-distribution）**，记作 $T \sim t(\nu)$。

##### ② Example 3.4：推导 $T \sim t(\nu)$ 的概率密度函数（Slide P27–P31）

* **已知条件**：

  * $X \sim N(0,1)$ 的 PDF：$f_X(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}, \quad x \in \mathbb{R}$

  * $Y \sim \chi^2(\nu)$ 的 PDF：$f_Y(y) = \frac{1}{\Gamma(\nu/2) 2^{\nu/2}} y^{\frac{\nu}{2}-1} e^{-\frac{y}{2}}, \quad y \ge 0$

  * 由 $X \perp Y$，联合 PDF 为 $f_{X,Y}(x, y) = f_X(x) f_Y(y)$。

* **Step 1 & 2（引入辅助变量与求逆变换）**：
  令：
  

  $$
  \begin{cases} T = X \sqrt{\dfrac{\nu}{Y}} \\[6pt] W = Y \end{cases} \quad \Longleftrightarrow \quad \begin{cases} X = T \sqrt{\dfrac{W}{\nu}} \\[6pt] Y = W \end{cases}, \quad (t \in \mathbb{R},\; w > 0)
  $$

* **Step 3（计算雅可比行列式）**：
  

  $$
  J = \begin{bmatrix} \dfrac{\partial X}{\partial T} & \dfrac{\partial X}{\partial W} \\[8pt] \dfrac{\partial Y}{\partial T} & \dfrac{\partial Y}{\partial W} \end{bmatrix} = \begin{bmatrix} \sqrt{\dfrac{w}{\nu}} & \dfrac{t}{2\nu\sqrt{w/\nu}} \\[8pt] 0 & 1 \end{bmatrix} \implies |J| = \sqrt{\frac{w}{\nu}} = \nu^{-1/2} w^{1/2}
  $$

* **Step 4（写出** $(T, W)$ **的联合 PDF）**：
  

  $$
  f_{T,W}(t, w) = f_X\left(t\sqrt{\frac{w}{\nu}}\right) \cdot f_Y(w) \cdot |J|
  $$

  $$
  = \frac{1}{\sqrt{2\pi}} e^{-\frac{t^2 w}{2\nu}} \cdot \frac{1}{\Gamma(\nu/2) 2^{\nu/2}} w^{\frac{\nu}{2}-1} e^{-\frac{w}{2}} \cdot \frac{w^{1/2}}{\sqrt{\nu}}
  $$

  
  合并常数项与关于 $w$ 的幂次项、指数项：
  

  $$
  f_{T,W}(t, w) = \frac{1}{\sqrt{2\pi\nu}\,\Gamma(\nu/2) 2^{\nu/2}} \cdot w^{\frac{\nu+1}{2}-1} \cdot \exp\left[-\frac{1}{2}\left(\frac{t^2}{\nu} + 1\right)w\right]
  $$

* **Step 5（对** $w$ **积分求** $T$ **的边缘密度，使用 Gamma 积分公式）**：
  

  $$
  f_T(t) = \int_0^\infty f_{T,W}(t, w)\,dw = \frac{1}{\sqrt{2\pi\nu}\,\Gamma(\nu/2) 2^{\nu/2}} \int_0^\infty w^{\frac{\nu+1}{2}-1} \exp\left[-\frac{1}{2}\left(\frac{t^2}{\nu} + 1\right)w\right] dw
  $$

  
  识别被积函数为 Gamma 分布 $\text{Gam}(a, b)$ 的核，其中参数为：
  

  $$
  a = \frac{\nu + 1}{2}, \qquad b = \frac{1}{2}\left(\frac{t^2}{\nu} + 1\right)
  $$

  
  代入 $\int_0^\infty w^{a-1} e^{-bw}\,dw = \frac{\Gamma(a)}{b^a}$：
  

  $$
  f_T(t) = \frac{1}{\sqrt{2\pi\nu}\,\Gamma(\nu/2) 2^{\nu/2}} \cdot \frac{\Gamma\left(\frac{\nu+1}{2}\right)}{\left[\frac{1}{2}\left(\frac{t^2}{\nu} + 1\right)\right]^{\frac{\nu+1}{2}}}
  $$

  
  注意到分母中 $\sqrt{2} \cdot 2^{\nu/2} \cdot \left(\frac{1}{2}\right)^{\frac{\nu+1}{2}} = 2^{\frac{\nu+1}{2}} \cdot 2^{-\frac{\nu+1}{2}} = 1$，化简得到 $t(\nu)$ **的标准 PDF**：
  

  $$
  \boxed{f_T(t) = \frac{\Gamma\left(\frac{\nu+1}{2}\right)}{\Gamma\left(\frac{\nu}{2}\right)\sqrt{\nu\pi}} \left(1 + \frac{t^2}{\nu}\right)^{-\frac{\nu+1}{2}}, \quad t \in \mathbb{R}}
  $$

> **【补充拓展：**$t$ **分布的重要性质】**
>
> 1. **偶函数对称性**：$f_T(-t) = f_T(t)$，关于 $t = 0$ 对称（当 $\nu > 1$ 时 $E(T) = 0$；当 $\nu > 2$ 时 $\text{Var}(T) = \frac{\nu}{\nu-2}$）。
>
> 2. **厚尾特性与正态极限**：相比于 $N(0,1)$，$t$ 分布尾部更厚；当自由度 $\nu \to \infty$ 时，由 $\lim_{\nu\to\infty}(1 + \frac{t^2}{\nu})^{-\frac{\nu+1}{2}} = e^{-t^2/2}$，有 $t(\nu) \xrightarrow{d} N(0, 1)$。
>
> 3. **特例** $\nu = 1$：$t(1)$ 的密度为 $f(t) = \frac{1}{\pi(1+t^2)}$，即著名的**标准柯西分布（Cauchy Distribution）**，其数学期望与方差均不存在。

#### （2）卡方分布 $\chi^2(k)$（Slide P32–P36）

##### ① 定义与 Gamma 分布的关系（Slide P32）

* **定义**：设 $X_1, \dots, X_k \stackrel{\text{i.i.d.}}{\sim} N(0, 1)$（相互独立的标准正态随机变量），则它们的平方和：
  

  $$
  Y = \sum_{i=1}^k X_i^2 \sim \chi^2(k)
  $$

  
  服从自由度为 $k$ 的**卡方分布（Chi-squared Distribution）**。

* **与 Gamma 分布的等价关系**：自由度为 $k$ 的 $\chi^2(k)$ 分布，本质上就是形状参数为 $\alpha = \frac{k}{2}$、速率参数为 $\beta = \frac{1}{2}$ 的 Gamma 分布：
  

  $$
  Y \sim \chi^2(k) \Longleftrightarrow Y \sim \text{Gam}\left(\frac{k}{2}, \frac{1}{2}\right), \qquad f_Y(y) = \frac{1}{2^{k/2}\Gamma(k/2)} y^{\frac{k}{2}-1} e^{-\frac{y}{2}}, \quad y > 0
  $$

##### ② Example 3.5（第一部分）：推导 $\chi^2(k)$ 的概率密度函数（Slide P33–P36）

> **【核心疑难解析：为什么课件说“这里直接用多维变量代换并不容易”，而采用了** $k$ **维超球壳体积微元法？】**
> 如果对 $Y = \sum_{i=1}^k X_i^2$ 强行使用雅可比变换，需要引入 $k-1$ 个辅助变量（即 $k$ 维广义球坐标变换 $r, \theta_1, \dots, \theta_{k-1}$），不仅由于平方项 $X_i^2$ 在正负半轴上**不是一一映射**（$2^k$ 对 $1$），而且 $k$ 维球坐标雅可比行列式的积分推导极为繁琐。因此，课件巧妙地采用了**几何微元法（超球壳体积法，Elemental Shell Volume Method）**！

* **超球壳体积微元法逐步拆解（Slide P34–P36）**：

  1. **微分关系（附 Slide P34 勘误）**：
     设 $Y = \sum_{i=1}^k X_i^2$ 的 CDF 为 $F_Y(y) = P(Y \le y)$，PDF 为 $f_Y(y) = F_Y'(y)$。
     当 $Y$ 落在无穷小区间 $[y, y + dy]$ 内时，概率微元为：
     

     $$
     dF_Y(y) = \frac{dF_Y(y)}{dy}\,dy = f_Y(y)\,dy
     $$

     
     *(注：Slide P34 第 6 行印成了* $F_Y(y) = \frac{F_Y(y)}{dy}dy = f_Y(y)dy$*，左端和分子漏写了微分算子* $d$*，正确写法如上)*。

  2. **转化为** $k$ **维球壳** $V$ **上的重积分**：
     满足 $y \le x_1^2 + \dots + x_k^2 \le y + dy$ 的点集 $\mathbf{x} = (x_1, \dots, x_k) \in \mathbb{R}^k$ 构成一个半径为 $r = \sqrt{y}$、厚度为 $dr$ 的$k$ 维无穷薄球壳 $V$。
     由于 $X_1, \dots, X_k \stackrel{\text{i.i.d.}}{\sim} N(0, 1)$，其联合密度在球壳 $V$ 上的积分为：
     

     $$
     f_Y(y)\,dy = \int_V \prod_{i=1}^k \left(\frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}x_i^2}\,dx_i\right) = \int_V \frac{1}{(2\pi)^{k/2}} \exp\left[-\frac{1}{2}(x_1^2 + \dots + x_k^2)\right] dx_1 \dots dx_k
     $$

  3. **利用球面上** $\sum_{i=1}^k x_i^2 = y$ **为常数提出指数项**：
     在无穷薄球壳 $V$ 上，$x_1^2 + \dots + x_k^2 = y$ 是常数，可直接提到积分号外：
     

     $$
     f_Y(y)\,dy = \frac{e^{-y/2}}{(2\pi)^{k/2}} \underbrace{\int_V dx_1 \dots dx_k}_{\text{球壳 } V \text{ 的体积 } dV} \qquad \text{--- 式 (2)}
     $$

  4. **计算球壳体积** $dV = \text{球面表面积 } A \times \text{球壳厚度 } dr$：

     * 半径为 $r = \sqrt{y}$ 的 $k$ 维球体，其边界（即 $(k-1)$ 维超球面）的表面积公式为：
       

       $$
       A = \frac{2\pi^{k/2}}{\Gamma(k/2)} r^{k-1} \qquad \text{--- 式 (3)}
       $$

       
       *(验证特例：当* $k=2$ *时，圆周长* $A = \frac{2\pi^1}{\Gamma(1)}r^1 = 2\pi r$*；当* $k=3$ *时，球表面积* $A = \frac{2\pi^{3/2}}{\Gamma(3/2)}r^2 = \frac{2\pi^{3/2}}{\frac{1}{2}\sqrt{\pi}}r^2 = 4\pi r^2$*，完全吻合！)*

     * 由 $r = y^{1/2}$ 求微分，得球壳厚度：
       

       $$
       \frac{dr}{dy} = \frac{1}{2}y^{-1/2} \iff dr = \frac{dy}{2\sqrt{y}} \qquad \text{--- 式 (4)}
       $$

  5. **回代化简得出最终结果（Slide P36）**：
     将式 (3)、式 (4) 及 $r = \sqrt{y}$ 代入式 (2)：
     

     $$
     f_Y(y)\,dy = \frac{e^{-y/2}}{(2\pi)^{k/2}} \cdot A\,dr = \frac{e^{-y/2}}{2^{k/2}\pi^{k/2}} \cdot \left(2 (\sqrt{y})^{k-1} \frac{\pi^{k/2}}{\Gamma(k/2)}\right) \cdot \frac{dy}{2\sqrt{y}}
     $$

     
     约去 $\pi^{k/2}$ 和常数 $2$，并合并 $\frac{(\sqrt{y})^{k-1}}{\sqrt{y}} = (\sqrt{y})^{k-2} = y^{\frac{k}{2}-1}$：
     

     $$
     f_Y(y)\,dy = \frac{1}{2^{k/2}\Gamma(k/2)} y^{\frac{k}{2}-1} e^{-y/2}\,dy \implies \boxed{f_Y(y) = \frac{1}{2^{k/2}\Gamma(k/2)} y^{\frac{k}{2}-1} e^{-y/2}, \quad y > 0}
     $$

> **【补充：考场上更简单的替代证法——单变量变换 + Gamma 可加性 / 矩母函数法】**
> 如果考试不强制要求使用超球面面积公式，可通过以下两步轻松推导：
>
> 1. **先证** $k=1$ **时** $Z = X_1^2 \sim \chi^2(1) = \text{Gam}\left(\frac{1}{2}, \frac{1}{2}\right)$：
>    对 $z > 0$，$F_Z(z) = P(-\sqrt{z} \le X_1 \le \sqrt{z}) = 2\Phi(\sqrt{z}) - 1$。求导得：
>    
>
>    $$
>    f_Z(z) = 2\phi(\sqrt{z}) \cdot \frac{1}{2\sqrt{z}} = \frac{1}{\sqrt{2\pi}} z^{-\frac{1}{2}} e^{-\frac{z}{2}} = \frac{(1/2)^{1/2}}{\Gamma(1/2)} z^{\frac{1}{2}-1} e^{-\frac{1}{2}z} \sim \text{Gam}\left(\frac{1}{2}, \frac{1}{2}\right)
>    $$
>
>    
>    （这里用到了欧拉余元公式结论 $\Gamma(1/2) = \sqrt{\pi}$）。
>
> 2. **再利用独立同速率 Gamma 分布的可加性（或 MGF 乘积性质）**：
>    因为 $X_i^2 \stackrel{\text{i.i.d.}}{\sim} \text{Gam}\left(\frac{1}{2}, \frac{1}{2}\right)$，其矩母函数为 $M_{X_i^2}(t) = (1 - 2t)^{-1/2}$。
>    故 $Y = \sum_{i=1}^k X_i^2$ 的矩母函数为 $M_Y(t) = \prod_{i=1}^k (1 - 2t)^{-1/2} = (1 - 2t)^{-k/2}$，唯一对应 $\text{Gam}\left(\frac{k}{2}, \frac{1}{2}\right) = \chi^2(k)$！

#### （3）Snedecor's $F$ 分布（Slide P37–P43）

##### ① 定义（Slide P37）

设 $X_1 \sim \chi^2(d_1)$，$X_2 \sim \chi^2(d_2)$，且 $X_1$ **与** $X_2$ **相互独立**。则它们各自除以自身自由度之比：

$$
Y = \frac{X_1 / d_1}{X_2 / d_2} \sim F(d_1, d_2) \quad (d_1, d_2 > 0)
$$


称为服从第一自由度（分子自由度）为 $d_1$、第二自由度（分母自由度）为 $d_2$ 的 $F$ **分布**（又称 Snedecor's $F$-distribution 或 Fisher–Snedecor distribution）。

##### ② Theorem 3.1：核心性质与证明（Slide P38）

* **性质 (a)（倒数对称性）**：若 $X \sim F(d_1, d_2)$，则 $\dfrac{1}{X} \sim F(d_2, d_1)$。

  * **证明**：设 $X = \frac{U_1/d_1}{U_2/d_2}$，其中 $U_1 \sim \chi^2(d_1) \perp U_2 \sim \chi^2(d_2)$。则：
    

    $$
    \frac{1}{X} = \frac{U_2 / d_2}{U_1 / d_1}
    $$

    
    分子是自由度为 $d_2$ 的卡方除以 $d_2$，分母是独立的自由度为 $d_1$ 的卡方除以 $d_1$，由定义直接有 $\frac{1}{X} \sim F(d_2, d_1)$。

  * **【重要推论：分位数倒数公式】**：在查 $F$ 分布表时，左侧下分位数通常不印在表上，需用此性质转换：
    

    $$
    F_{1-\alpha}(d_1, d_2) = \frac{1}{F_\alpha(d_2, d_1)}
    $$

* **性质 (b)（与** $t$ **分布的平方关系）**：若 $X \sim t(\nu)$，则 $X^2 \sim F(1, \nu)$。

  * **证明**：由 $t(\nu)$ 定义，可设 $X = \frac{Z}{\sqrt{V/\nu}}$，其中 $Z \sim N(0, 1) \perp V \sim \chi^2(\nu)$。
    两边平方得：
    

    $$
    X^2 = \frac{Z^2 / 1}{V / \nu}
    $$

    
    由于 $Z \sim N(0, 1) \implies Z^2 \sim \chi^2(1)$，且 $Z^2$ 与 $V \sim \chi^2(\nu)$ 相互独立，故由 $F$ 分布定义立得 $X^2 \sim F(1, \nu)$。

##### ③ Example 3.5（第二部分）：推导 $F(u, v)$ 的概率密度函数（Slide P39–P43）

*(注：课件将 P33 和 P39 两个例题都编号为 Example 3.5，这里自由度记为* $u, v$*)*。

* **已知条件**：$X \sim \chi^2(u)$，$Y \sim \chi^2(v)$，且 $X \perp Y$。
  

  $$
  f_X(x) = \frac{1}{\Gamma(u/2) 2^{u/2}} x^{\frac{u}{2}-1} e^{-\frac{x}{2}}, \quad f_Y(y) = \frac{1}{\Gamma(v/2) 2^{v/2}} y^{\frac{v}{2}-1} e^{-\frac{y}{2}}, \quad (x > 0, y > 0)
  $$

* **Step 1 & 2（引入辅助变量与求逆变换）**：
  

  $$
  \begin{cases} F = \dfrac{X / u}{Y / v} \\[8pt] W = Y \end{cases} \quad \Longleftrightarrow \quad \begin{cases} X = \dfrac{u}{v} F W \\[6pt] Y = W \end{cases}, \quad (f > 0,\; w > 0)
  $$

* **Step 3（计算雅可比行列式）**：
  

  $$
  J = \begin{bmatrix} \dfrac{\partial X}{\partial F} & \dfrac{\partial X}{\partial W} \\[8pt] \dfrac{\partial Y}{\partial F} & \dfrac{\partial Y}{\partial W} \end{bmatrix} = \begin{bmatrix} \dfrac{u}{v}W & \dfrac{u}{v}F \\[6pt] 0 & 1 \end{bmatrix} \implies |J| = \frac{u}{v}w \quad (w > 0)
  $$

* **Step 4（写出** $(F, W)$ **的联合 PDF）**：
  

  $$
  f_{F,W}(f, w) = f_X\left(\frac{u}{v}fw\right) \cdot f_Y(w) \cdot |J|
  $$

  $$
  = \frac{1}{\Gamma(u/2) 2^{u/2}} \left(\frac{u}{v}fw\right)^{\frac{u}{2}-1} e^{-\frac{1}{2}\left(\frac{u}{v}fw\right)} \cdot \frac{1}{\Gamma(v/2) 2^{v/2}} w^{\frac{v}{2}-1} e^{-\frac{w}{2}} \cdot \frac{u}{v}w
  $$

  
  整理关于 $f$ 的因式和关于 $w$ 的幂次与指数（注意 $\left(\frac{u}{v}\right)^{\frac{u}{2}-1} \cdot \frac{u}{v} = \left(\frac{u}{v}\right)^{\frac{u}{2}}$，且 $w^{\frac{u}{2}-1} \cdot w^{\frac{v}{2}-1} \cdot w = w^{\frac{u+v}{2}-1}$）：
  

  $$
  f_{F,W}(f, w) = \frac{\left(\frac{u}{v}\right)^{u/2} f^{\frac{u}{2}-1}}{\Gamma(u/2)\Gamma(v/2) 2^{(u+v)/2}} \cdot w^{\frac{u+v}{2}-1} \exp\left[-\frac{1}{2}\left(\frac{u}{v}f + 1\right)w\right]
  $$

* **Step 5（对** $w$ **积分求** $F$ **的边缘密度，再次使用 Gamma 积分公式）**：
  

  $$
  f_F(f) = \int_0^\infty f_{F,W}(f, w)\,dw = \frac{\left(\frac{u}{v}\right)^{u/2} f^{\frac{u}{2}-1}}{\Gamma(u/2)\Gamma(v/2) 2^{(u+v)/2}} \int_0^\infty w^{\frac{u+v}{2}-1} \exp\left[-\frac{1}{2}\left(\frac{u}{v}f + 1\right)w\right] dw
  $$

  
  识别被积函数为 $\text{Gam}(a, b)$ 的核，其中：
  

  $$
  a = \frac{u + v}{2}, \qquad b = \frac{1}{2}\left(\frac{u}{v}f + 1\right)
  $$

  
  代入 $\int_0^\infty w^{a-1} e^{-bw}\,dw = \frac{\Gamma(a)}{b^a}$，约去分母中的 $2^{(u+v)/2}$，即得 $F(u, v)$ **的标准 PDF**：
  

  $$
  \boxed{f_F(f) = \frac{\Gamma\left(\frac{u+v}{2}\right)}{\Gamma\left(\frac{u}{2}\right)\Gamma\left(\frac{v}{2}\right)} \left(\frac{u}{v}\right)^{\frac{u}{2}} f^{\frac{u}{2}-1} \left(\frac{u}{v}f + 1\right)^{-\frac{u+v}{2}}, \quad f > 0}
  $$

  
  *(注：利用 Beta 函数* $B\left(\frac{u}{2}, \frac{v}{2}\right) = \frac{\Gamma(u/2)\Gamma(v/2)}{\Gamma((u+v)/2)}$*，前置常数项也常简写为* $\frac{1}{B(u/2, v/2)}$*)*。

### 4. 经典例题深度精讲：Example 3.6（区域边界映射与“算术依赖但概率独立”现象，Slide P44–P46）

> **题目（Example 3.6，源自 Hogg 教材 Section 5.2 Example 1）**：
> 设 $X_1, X_2$ 的联合 PDF 为：
> 
>
> $$
> f(x_1, x_2) = 2, \quad 0 < x_1 < x_2 < 1 \quad (\text{其余区域为 } 0)
> $$
>
> 
> 考虑变换：$Y_1 = \dfrac{X_1}{X_2}, \quad Y_2 = X_2$。求 $(Y_1, Y_2)$ 的联合 PDF，并讨论其独立性。

#### 【深度解析与三大疑难突破】

##### 1. 逆变换与雅可比行列式计算

由 $\begin{cases} y_1 = x_1 / x_2 \\ y_2 = x_2 \end{cases}$ 反解得逆变换：

$$
x_1 = y_1 y_2, \qquad x_2 = y_2
$$


计算逆向雅可比行列式：

$$
J = \det \begin{bmatrix} \dfrac{\partial x_1}{\partial y_1} & \dfrac{\partial x_1}{\partial y_2} \\[8pt] \dfrac{\partial x_2}{\partial y_1} & \dfrac{\partial x_2}{\partial y_2} \end{bmatrix} = \det \begin{bmatrix} y_2 & y_1 \\ 0 & 1 \end{bmatrix} = y_2
$$

##### 2. 疑难一：三角形支撑集 $S_X$ 是如何变成正方形支撑集 $S_Y$ 的？

* **代数不等式推导法（最快、最稳）**：
  将逆变换 $x_1 = y_1 y_2, x_2 = y_2$ 代入原支撑集不等式 $0 < x_1 < x_2 < 1$：
  

  $$
  0 < y_1 y_2 < y_2 < 1
  $$

  * 由右半部分 $0 < y_2 < 1$，知 $y_2 \in (0, 1)$ 且 $y_2 > 0$；

  * 将左半部分 $0 < y_1 y_2 < y_2$ 同时除以正数 $y_2$，立即得到 $0 < y_1 < 1$！

  * 因此，新支撑集为开正方形区域：$S_Y = \{(y_1, y_2) : 0 < y_1 < 1,\; 0 < y_2 < 1\}$。

* **边界线段几何映射追踪法（Slide P45 Figure 5.2-1 的直观含义）**：
  观察原三角形 $S_X$ 的三条边界在变换下的去向：

  1. 左竖直边 $x_1 = 0, 0 < x_2 < 1 \implies y_1 = 0, 0 < y_2 < 1$（正方形的左边界）；

  2. 上水平边 $x_2 = 1, 0 \le x_1 < 1 \implies y_2 = 1, 0 \le y_1 < 1$（正方形的上边界）；

  3. 斜边 $0 < x_1 = x_2 \le 1 \implies y_1 = 1, 0 < y_2 \le 1$（正方形的右边界）；

  4. **那正方形的下边界（**$y_2 = 0, 0 \le y_1 < 1$**）对应哪里？**
     当 $y_2 = 0$ 时，无论 $y_1 \in [0, 1)$ 取何值，都有 $x_1 = y_1 \cdot 0 = 0, x_2 = 0$！也就是说，**正方形底边整条线段上的无穷多个点** $(y_1, 0)$**，全部坍缩映射到了原平面的同一个原点** $(0, 0)$！

##### 3. 疑难二：既然在 $y_2 = 0$ 处是“多对一映射（Many-to-One）”，为什么还能用要求“一一映射”的雅可比定理？（Slide P46）

* **核心原因**：原支撑集 $S_X = \{(x_1, x_2) : 0 < x_1 < x_2 < 1\}$ 是一个**开集（不包含边界）**！

* 在开集内部（$y_2 > 0$），映射 $(x_1, x_2) \leftrightarrow (y_1, y_2)$ 是严格一一对应（双射）的；而发生坍缩的边界 $\{y_2 = 0\}$ 和 $\{x_1 = x_2 = 0\}$ 在二维平面上的面积（勒贝格测度）为 $0$，对连续型随机变量的积分概率没有任何影响！

##### 4. 疑难三：为什么 $Y_1 = X_1/X_2$ 在公式里明显含有 $Y_2 = X_2$，但 $Y_1$ 和 $Y_2$ 却相互独立？（Slide P46 结尾）

* **计算联合 PDF 与边缘 PDF**：
  

  $$
  g(y_1, y_2) = f(y_1 y_2, y_2) \cdot |J| = 2 y_2, \quad 0 < y_1 < 1,\; 0 < y_2 < 1
  $$

  
  求边缘密度：
  

  $$
  g_1(y_1) = \int_0^1 2y_2\,dy_2 = 1 \quad (0 < y_1 < 1, \text{ 即 } Y_1 \sim U(0, 1))
  $$

  $$
  g_2(y_2) = \int_0^1 2y_2\,dy_1 = 2y_2 \quad (0 < y_2 < 1)
  $$

  
  显然在 $S_Y = (0,1)\times(0,1)$ 上恒有 $g(y_1, y_2) = 1 \cdot 2y_2 = g_1(y_1)g_2(y_2)$，故 $Y_1$ **与** $Y_2$ **相互独立**！

* **物理与几何直观解释（消除反直觉感）**：

  * 原变量 $(X_1, X_2)$ 在三角形 $0 < x_1 < x_2 < 1$ 上服从**均匀分布**。

  * 当固定 $X_2 = y_2$ 时，$X_1$ 在区间 $(0, y_2)$ 上均匀分布，其绝对取值范围虽然受 $y_2$ 限制（所以 $X_1$ 与 $X_2$ 不独立），但**相对比例** $Y_1 = \frac{X_1}{X_2}$ 相当于把区间 $(0, y_2)$ 按比例缩放到标准区间 $(0, 1)$！

  * 无论 $Y_2 = y_2$ 是大是小，$X_1$ 占 $X_2$ 的相对百分比 $Y_1$ 永远在 $(0, 1)$ 上均匀分布，与 $Y_2$ 的具体数值毫无关系。这就是 Slide P46 所强调的：**“尽管** $Y_1$ **的代数计算依赖于** $Y_2$**，但在概率意义上** $Y_1$ **与** $Y_2$ **是完全独立的！”**

## 五、三大抽样分布（$\chi^2, t, F$）横向对比与全章课件勘误汇总

### 1. 三大导出抽样分布核心特征对比表

| 分布名称 | 记号与自由度 | 标准构造定义（前提：分子分母相互独立） | 支撑集（取值范围） | 概率密度函数（PDF）核心结构 | 典型关联性质 | 
| ----- | ----- | ----- | ----- | ----- | ----- | 
| **卡方分布**  ($\chi^2$-distribution) | $\chi^2(k)$  （自由度 $k$） | $Y = \sum_{i=1}^k X_i^2$  其中 $X_i \stackrel{\text{i.i.d.}}{\sim} N(0,1)$ | $y \in (0, +\infty)$ | $\frac{1}{2^{k/2}\Gamma(k/2)} y^{\frac{k}{2}-1} e^{-y/2}$ | 1\. 等价于 $\text{Gam}\left(\frac{k}{2}, \frac{1}{2}\right)$  2\. 独立可加性：$\chi^2(k_1)+\chi^2(k_2)=\chi^2(k_1+k_2)$ | 
| **学生** $t$ **分布**  (Student's $t$) | $t(\nu)$  （自由度 $\nu$） | $T = \dfrac{X}{\sqrt{Y/\nu}}$  其中 $X \sim N(0,1) \perp Y \sim \chi^2(\nu)$ | $t \in (-\infty, +\infty)$ | $\frac{\Gamma\left(\frac{\nu+1}{2}\right)}{\Gamma\left(\frac{\nu}{2}\right)\sqrt{\nu\pi}} \left(1 + \frac{t^2}{\nu}\right)^{-\frac{\nu+1}{2}}$ | 1\. 关于 $0$ 对称，$\nu\to\infty$ 趋于 $N(0,1)$  2\. $T \sim t(\nu) \implies T^2 \sim F(1, \nu)$ | 
| $F$ **分布**  (Snedecor's $F$) | $F(u, v)$  （自由度 $u, v$） | $F = \dfrac{X/u}{Y/v}$  其中 $X \sim \chi^2(u) \perp Y \sim \chi^2(v)$ | $f \in (0, +\infty)$ | $\frac{\Gamma\left(\frac{u+v}{2}\right)}{\Gamma\left(\frac{u}{2}\right)\Gamma\left(\frac{v}{2}\right)} \left(\frac{u}{v}\right)^{\frac{u}{2}} f^{\frac{u}{2}-1}\left(\frac{u}{v}f + 1\right)^{-\frac{u+v}{2}}$ | 1\. $X \sim F(u, v) \implies \frac{1}{X} \sim F(v, u)$  2\. 分位数：$F_{1-\alpha}(u,v) = \frac{1}{F_\alpha(v,u)}$ | 

### 2. 本课件（Chapter 3 Slides）公式笔误与易混点勘误汇总表

在复习原版课件时，以下 6 处排版或计算笔误需要特别留意，避免被误导：

| 课件页码 | 原课件内容（含笔误） | 修正后正确内容 | 原因说明 | 
| ----- | ----- | ----- | ----- | 
| **Slide P5** | $f_{X_2}(b_j) = \sum_i P(X_1=a_i, X_2=b_j) = \sum_j p_{ij} = p_{\cdot j}$ | $\dots = \sum_i p_{ij} = p_{\cdot j}$ | 求 $X_2$ 的边缘分布应固定列 $j$，对行标 $i$ 求和 | 
| **Slide P9 (b)** | $f_X(1)f_Y(2) = \frac{11}{36} \times \frac{1}{36} \ne \frac{2}{36}$ | $f_X(1)f_Y(2) = \frac{11}{36} \times \frac{3}{36} \ne \frac{2}{36}$ | 将 $f_Y(2) = \frac{2(2-1)+1}{36} = \frac{3}{36}$ 误写成了 $f_Y(1) = \frac{1}{36}$ | 
| **Slide P20 (a)** | $\int_{0\le y\le 1} \int_{-y\le x\le 1-} f(x,y)dxdy = 1$ | $\int_{0\le y\le 1} \int_{-y\le x\le 1} f(x,y)dxdy = 1$ | 内层积分上限 $1-$ 末尾多打了一个负号 | 
| **Slide P21 (d)** | $f_{X\mid Y=1}(x\mid Y=1) = \frac{f(x,1)}{f_Y(1)} = \begin{cases} \frac{8}{3}x^2, & x\in[-1/2, 1] \\ 0, & \text{otherwise} \end{cases}$ | $f_{X\mid Y=1/2}(x\mid Y=1/2) = \frac{f(x,1/2)}{f_Y(1/2)} = \dots$ | 题目要求给定 $Y=1/2$，右侧结果也是按 $Y=1/2$ 算的，仅左端符号误印成了 $Y=1$ | 
| **Slide P24** | $J_{x\to y} \stackrel{\text{def}}{=} \frac{\partial(y_1,\dots,y_m)}{\partial(x_1,\dots,x_n)}$ | $J_{x\to y} \stackrel{\text{def}}{=} \frac{\partial(y_1,\dots,y_n)}{\partial(x_1,\dots,x_n)}$ | 映射为 $\mathbb{R}^n \to \mathbb{R}^n$，分子分母变量个数均为 $n$ | 
| **Slide P34** | $F_Y(y) = \frac{F_Y(y)}{dy}dy = f_Y(y)dy$ | $dF_Y(y) = \frac{dF_Y(y)}{dy}dy = f_Y(y)dy$ | 概率微元等于分布函数的微分 $dF_Y(y)$，原式漏写了微分符号 $d$ | 
