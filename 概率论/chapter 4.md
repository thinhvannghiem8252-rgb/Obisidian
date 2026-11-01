# 第四章：随机变量的数字特征

> [!abstract] 本章主线
> 从一个随机变量的平均位置和波动出发，用矩与矩母函数研究分布；再通过协方差描述多个变量的关系，用条件期望刻画信息带来的变化，最终建立平方损失下的最优预测方法。

## 目录

- [[#0. 知识地图与基本约定|0. 知识地图与基本约定]]
- [[#1. 期望与方差：描述位置和波动|1. 期望与方差：描述位置和波动]]
- [[#2. 矩与矩母函数：从数字特征到分布|2. 矩与矩母函数：从数字特征到分布]]
- [[#3. 协方差与相关性：刻画变量间的关系|3. 协方差与相关性：刻画变量间的关系]]
- [[#4. 条件期望与方差分解：信息如何改变平均与波动|4. 条件期望与方差分解：信息如何改变平均与波动]]
- [[#5. 联合正态模型：连接分布、相关与条件信息|5. 联合正态模型：连接分布、相关与条件信息]]
- [[#6. 最优预测：从常数到线性函数再到条件期望|6. 最优预测：从常数到线性函数再到条件期望]]
- [[#7. 解题方法与易错点|7. 解题方法与易错点]]
- [[#8. 核心公式速查|8. 核心公式速查]]
- [[#9. 自测题与参考解答|9. 自测题与参考解答]]
- [[#10. 掌握程度检查|10. 掌握程度检查]]

## 0. 知识地图与基本约定

本章围绕三个问题展开：怎样概括一个分布，怎样描述变量之间的关系，以及怎样利用已知信息进行预测。各部分并非互不相干的公式集合，而是对期望运算的逐层扩展。

### 0.1 本章到底研究什么

分布描述随机变量“可能取什么值，以及各个值有多大可能”。数字特征则用少量数字概括分布的重要性质。

| 对象 | 回答的问题 | 主要工具 |
|---|---|---|
| 位置 | 随机变量平均在什么位置？ | 期望 $E(X)$ |
| 波动 | 随机变量偏离平均值有多大？ | 方差、标准差 |
| 更高阶形态 | 分布是否偏斜、尾部如何？ | 高阶矩、偏度与峰度 |
| 分布识别 | 能否把分布编码成一个函数？ | 矩母函数 MGF |
| 共同变化 | 两个变量是否具有线性同向或反向变化？ | 协方差、相关系数 |
| 预测 | 已知一个变量，怎样估计另一个？ | 最佳线性预测、条件期望 |
| 信息分解 | 总体波动由哪些部分构成？ | 全期望、全方差公式 |

本章的逻辑链为：

$$
\text{分布}
\longrightarrow \text{期望与矩}
\longrightarrow \text{方差、协方差}
\longrightarrow \text{预测与条件分解}.
$$

MGF 提供另一条计算路径：

$$
\text{分布}\longrightarrow M_X(t)
\longrightarrow
\begin{cases}
\text{求导得到矩},\\
\text{利用乘法求独立和的分布}.
\end{cases}
$$

**必须区分**：知道均值、方差通常不能确定分布；知道一个在零点邻域有限的完整 MGF，则可以唯一确定分布。

### 0.2 符号与参数约定

| 符号 | 含义 |
|---|---|
| $E(X)$、$\mu_X$ | 期望、均值 |
| $\operatorname{Var}(X)$、$\sigma_X^2$ | 方差 |
| $\operatorname{sd}(X)$、$\sigma_X$ | 标准差 |
| $\operatorname{Cov}(X,Y)$ | 协方差 |
| $\rho_{X,Y}$ | 相关系数 |
| $p_X(x)$ | 离散型随机变量的概率质量函数 |
| $f_X(x)$ | 连续型随机变量的概率密度 |
| $M_X(t)$ | 矩母函数，$E(e^{tX})$ |
| $\Phi(z)$、$\phi(z)$ | 标准正态分布函数、密度函数 |
| $\mathbf1_A$ | 事件 $A$ 的示性随机变量 |
| a.s. | almost surely，几乎必然，即以概率 1 成立 |

统一使用以下符号与参数约定：

1. **有限期望要求绝对可积**：$E|X|<\infty$。
2. 方差和协方差的通常运算在**二阶矩有限**的条件下使用。
3. 几何分布取值为 $1,2,\ldots$，表示“直到首次成功所需的试验总次数”。
4. 指数分布和 Gamma 分布中的 $\lambda$ 是**率参数**，不是尺度参数。
5. $N(\mu,\sigma^2)$ 的第二个参数是**方差**，不是标准差。
6. 讨论高斯向量时允许“方差为零的正态分布”，其含义为集中在一个点上的退化分布。

### 0.3 存在性条件的层次

$$
\boxed{
\text{MGF 在零点某邻域有限}
\Longrightarrow \text{所有阶绝对矩有限}
\Longrightarrow E(X^2)<\infty
\Longrightarrow E|X|<\infty
}
$$

这里中间一项指所有正整数阶绝对矩均有限。反方向一般都不能成立。

- $E(X^2)<\infty\Rightarrow E|X|<\infty$ 可由 Cauchy–Schwarz 不等式推出：$E|X|\le\sqrt{E(X^2)}$。
- 对 $0<k\le r$，有 $|x|^k\le 1+|x|^r$，所以高阶绝对矩有限推出低阶绝对矩有限。
- 存在均值不代表存在有限方差；存在全部矩也不代表 MGF 在零点邻域有限，后文给出反例。

### 0.4 知识之间的依赖关系

| 学习阶段 | 核心问题 | 与后续知识的联系 |
|---|---|---|
| 期望与方差 | 如何描述一个变量的位置和波动？ | 二阶矩产生方差，中心化乘积产生协方差 |
| 矩与矩母函数 | 如何计算高阶特征、识别分布和独立和？ | 为正态线性组合与分布可加性提供统一证明 |
| 协方差与相关性 | 两个变量如何共同变化？ | 决定线性组合的方差与线性预测的斜率 |
| 条件期望与条件方差 | 知道信息后，平均与波动如何变化？ | 导出全期望、全方差以及最优预测 |
| 联合正态 | 哪种模型把分布结构和线性关系统一起来？ | 不相关等价于独立，条件均值恰为线性预测 |
| 最优预测 | 如何将信息转化为最小误差的估计？ | 统一常数预测、线性预测与任意函数预测 |

理解各公式时，始终同时回答三个问题：**它描述什么、它需要什么条件、它能解决什么问题**。

## 1. 期望与方差：描述位置和波动

先定义期望，再把期望作用于中心化后的平方得到方差。线性性是整章计算的基础，而独立性主要用于拆分乘积与消去交叉项。

### 1.1 数学期望的定义

对于离散型随机变量，

$$
\boxed{E(X)=\sum_x x\,p_X(x)}.
$$

对于有密度的连续型随机变量，

$$
\boxed{E(X)=\int_{-\infty}^{\infty}x f_X(x)\,dx}.
$$

求和或积分实际上只需在分布的支持集上进行。有限期望的前提是

$$
\sum_x |x|p_X(x)<\infty
\quad\text{或}\quad
\int_{-\infty}^{\infty}|x|f_X(x)\,dx<\infty.
$$

#### 直观解释：概率加权的“重心”

若 $X$ 以概率 $0.2$ 取 $0$，以概率 $0.8$ 取 $10$，则

$$
E(X)=0\times0.2+10\times0.8=8.
$$

==期望可以不是随机变量能取到的==值==。本例中 $X$ 从不等于 $8$，但它的平均位置为 $8$。

**直观理解**：在独立同分布、可积等适当条件下，大数定律把期望与大量重复观测的样本平均联系起来；“长期平均”是解释，不是期望定义本身。

#### 为什么强调绝对可积

令 $X^+=\max(X,0)$、$X^-=\max(-X,0)$，则 $X=X^+-X^-$、$|X|=X^++X^-$。

若 $E|X|<\infty$，则 $E(X^+)$、$E(X^-)$ 都有限，因而

$$
E(X)=E(X^+)-E(X^-)
$$

不会出现 $\infty-\infty$。离散情形下，绝对收敛还保证求和顺序不影响结果。

**反例：对称不必有均值。** 标准 Cauchy 分布密度为

$$
f(x)=\frac{1}{\pi(1+x^2)}.
$$

尽管对称积分 $\int_{-A}^{A}xf(x)\,dx=0$，但 $E|X|=\infty$，正负部分的积分均发散，故其期望不存在。不能以“对称”为由直接写出 $E(X)=0$。

### 1.2 随机变量函数的期望

若 $g$ 可测且 $E|g(X)|<\infty$，则

$$
\boxed{
E[g(X)]=
\begin{cases}
\displaystyle\sum_x g(x)p_X(x),&X\text{ 离散},\\[6pt]
\displaystyle\int_{\mathbb R}g(x)f_X(x)\,dx,&X\text{ 有密度}.
\end{cases}}
$$

**核心价值**：求 $g(X)$ 的期望时，不必先求 $g(X)$ 的分布。这条公式也常称 LOTUS。

例如 $X\sim\operatorname{Unif}(0,1)$，直接得到

$$
E(X^2)=\int_0^1x^2\,dx=\frac13.
$$

但

$$
[E(X)]^2=\left(\frac12\right)^2=\frac14.
$$

所以一般有

$$
E[g(X)]\ne g(E(X)).
$$

只有在某些特殊情形下二者相等，例如 $g(x)=ax+b$ 为仿射函数。

### 1.3 概率是示性变量的期望

对事件 $A$，定义

$$
\mathbf1_A=
\begin{cases}
1,&A\text{ 发生},\\
0,&A\text{ 不发生}.
\end{cases}
$$

于是

$$
\boxed{E(\mathbf1_A)=P(A)}.
$$

若事件写作 $\{X\in B\}$，连续情形下

$$
E[\mathbf1_B(X)]
=\int_{\mathbb R}\mathbf1_B(x)f_X(x)\,dx
=\int_Bf_X(x)\,dx
=P(X\in B).
$$

离散情形则将积分换为对 $x\in B$ 的求和。

**应用：计数问题。** 若 $N=\sum_{i=1}^n\mathbf1_{A_i}$ 为发生的事件个数，则

$$
E(N)=\sum_{i=1}^nP(A_i).
$$

这些事件可以相互依赖；计算期望不要求独立。比如从含 $K$ 件次品的 $N$ 件产品中不放回抽取 $m$ 件，次品数的期望为 $mK/N$。

### 1.4 期望的运算性质

#### 1.4.1 线性性：不要求独立

对可积随机变量 $X_1,\ldots,X_n$ 及常数 $a_i,b$，

$$
\boxed{E\left(b+\sum_{i=1}^na_iX_i\right)=b+\sum_{i=1}^na_iE(X_i)}.
$$

更一般地，有

$$
E\left[\sum_{i=1}^ng_i(X_i)\right]
=\sum_{i=1}^nE[g_i(X_i)],
$$

前提是各项可积。这是积分或求和的线性性。

#### 1.4.2 独立时的乘法公式

若 $X_1,\ldots,X_n$ **相互独立**，且各 $g_i(X_i)$ 可积，则

$$
\boxed{E\left[\prod_{i=1}^ng_i(X_i)\right]=\prod_{i=1}^nE[g_i(X_i)]}.
$$

两个变量有联合密度时，证明的关键是

$$
\begin{aligned}
E[g(X)h(Y)]
&=\iint g(x)h(y)f_X(x)f_Y(y)\,dx\,dy\\
&=\left(\int g(x)f_X(x)\,dx\right)
\left(\int h(y)f_Y(y)\,dy\right).
\end{aligned}
$$

独立性使联合分布可以分解，并保证绝对值乘积的积分也可分解。

**区别要记牢**：

| 公式 | 是否一般成立 | 条件 |
|---|---|---|
| $E(X+Y)=E(X)+E(Y)$ | 是 | 两者可积 |
| $E(XY)=E(X)E(Y)$ | 否 | 独立且可积是充分条件 |
| $E[g(X)]=g(E(X))$ | 否 | 不能对非线性函数直接使用 |

即使恰好有 $E(XY)=E(X)E(Y)$，也不能反推独立。对三个及以上变量，要把整个乘积的期望拆开，通常需要相互独立，仅两两独立不够。

#### 1.4.3 常用辅助性质

在相关期望存在时：

- 若 $X\ge0$ a.s.，则 $E(X)\ge0$。
- 若 $X\le Y$ a.s.，则 $E(X)\le E(Y)$。
- $|E(X)|\le E|X|$。
- 若 $X\ge0$ a.s. 且 $E(X)=0$，则 $X=0$ a.s.

这些性质是判断答案符号、证明方差非负和处理“等号成立条件”的基础。

### 1.5 方差与标准差

设 $E(X^2)<\infty$，记 $\mu=E(X)$。定义

$$
\boxed{\operatorname{Var}(X)=E[(X-\mu)^2]},
\qquad
\boxed{\operatorname{sd}(X)=\sqrt{\operatorname{Var}(X)}}.
$$

**为什么平方？** 因为 $E(X-\mu)=0$，直接平均偏差会使正负抵消。平方既避免抵消，也赋予较大偏差更高权重。

**单位区别**：若 $X$ 以 mL 为单位，方差以 mL$^2$ 为单位，标准差仍以 mL 为单位。因此标准差更容易直接解释。

基本性质：

$$
\operatorname{Var}(X)\ge0,
\qquad
\operatorname{Var}(X)=0\iff X=E(X)\text{ a.s.}
$$

后者由非负随机变量 $(X-\mu)^2$ 的期望为零得到。

### 1.6 方差计算公式与变换性质

#### 1.6.1 “二阶矩减去均值平方”

$$
\boxed{\operatorname{Var}(X)=E(X^2)-[E(X)]^2}.
$$

证明：

$$
\begin{aligned}
E[(X-\mu)^2]
&=E(X^2)-2\mu E(X)+\mu^2\\
&=E(X^2)-\mu^2.
\end{aligned}
$$

因此 $E(X^2)\ge[E(X)]^2$，但 $E(X^2)$ 本身通常不是方差。

#### 1.6.2 仿射变换

$$
\boxed{\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)},
\qquad
\boxed{\operatorname{sd}(aX+b)=|a|\operatorname{sd}(X)}.
$$

因为

$$
aX+b-E(aX+b)=a(X-\mu).
$$

平移不改变分布的波动；放大 $a$ 倍会把平方偏差放大 $a^2$ 倍。标准差前必须是 $|a|$，不能是可能为负的 $a$。

#### 1.6.3 独立和的方差

若 $X_1,\ldots,X_n$ 独立且二阶矩有限，则

$$
\boxed{\operatorname{Var}\left(\sum_{i=1}^na_iX_i\right)
=\sum_{i=1}^na_i^2\operatorname{Var}(X_i)}.
$$

证明的要点：展开中心化后的平方，交叉项为

$$
E[(X_i-E X_i)(X_j-E X_j)]=0\quad(i\ne j),
$$

所以仅剩平方项。**条件辨析**：这一方差公式只需要两两不相关，不必要求独立；一般情形需加协方差项，见第 3 节。

### 1.7 五种分布的均值与方差

#### 1.7.1 Bernoulli 分布

若 $X\sim\operatorname{Bernoulli}(p)$，则 $P(X=1)=p$、$P(X=0)=1-p$。

$$
E(X)=p.
$$

由于 $X^2=X$，有 $E(X^2)=p$，所以

$$
\boxed{\operatorname{Var}(X)=p(1-p)}.
$$

当 $p=0$ 或 $1$ 时变量为常数，方差为零；当 $p=1/2$ 时方差最大，为 $1/4$。

#### 1.7.2 二项分布

若 $X\sim\operatorname{Binomial}(n,p)$，可在其试验模型中写成

$$
X=I_1+\cdots+I_n,
\qquad I_i\overset{\mathrm{iid}}\sim\operatorname{Bernoulli}(p).
$$

由线性性和独立和的方差公式，

$$
\boxed{E(X)=np},\qquad
\boxed{\operatorname{Var}(X)=np(1-p)}.
$$

这里均值的相加用不到独立性，但二项模型本身包含独立、同成功概率这两个条件。

#### 1.7.3 几何分布

设 $0<p<1$，令 $q=1-p$。采用从首次试验开始计数的约定：

$$
P(X=k)=p q^{k-1},\qquad k=1,2,\ldots.
$$

利用几何级数

$$
\sum_{k=0}^\infty q^k=\frac{1}{1-q},\qquad |q|<1,
$$

在收敛区间内逐项求导：

$$
\sum_{k=1}^{\infty}kq^{k-1}=\frac{1}{(1-q)^2}.
$$

所以

$$
E(X)=p\sum_{k=1}^{\infty}kq^{k-1}=\frac{p}{(1-q)^2}=\frac1p.
$$

再求一次导数，并乘上 $pq$：

$$
\begin{aligned}
E[X(X-1)]
&=p\sum_{k=2}^{\infty}k(k-1)q^{k-1}\\
&=pq\frac{2}{(1-q)^3}=\frac{2q}{p^2}.
\end{aligned}
$$

由 $X^2=X(X-1)+X$ 得

$$
E(X^2)=\frac{2q}{p^2}+\frac1p=\frac{2-p}{p^2},
$$

从而

$$
\boxed{\operatorname{Var}(X)=\frac{1-p}{p^2}}.
$$

$p=1$ 时 $X=1$ a.s.，上述均值、方差公式仍成立。

**易混淆的另一种定义**：若 $W=X-1$ 表示首次成功前的失败次数，则支持集从 $0$ 开始，

$$
E(W)=\frac{1-p}{p},\qquad \operatorname{Var}(W)=\frac{1-p}{p^2}.
$$

均值改变，方差不变，因为只是平移。

#### 1.7.4 指数分布

若 $X\sim\operatorname{Exp}(\lambda)$，$\lambda>0$，则

$$
f_X(x)=\lambda e^{-\lambda x},\qquad x>0.
$$

分部积分得到

$$
\begin{aligned}
E(X)
&=\int_0^\infty x\lambda e^{-\lambda x}\,dx\\
&=[-xe^{-\lambda x}]_0^\infty+\int_0^\infty e^{-\lambda x}\,dx
=\frac1\lambda.
\end{aligned}
$$

同理，

$$
E(X^2)
=[-x^2e^{-\lambda x}]_0^\infty
+2\int_0^\infty xe^{-\lambda x}\,dx
=\frac2{\lambda^2}.
$$

因此

$$
\boxed{\operatorname{Var}(X)=\frac1{\lambda^2}}.
$$

指数衰减快于多项式增长，故边界项为零。率 $\lambda$ 越大，平均等待时间 $1/\lambda$ 越短。

#### 1.7.5 正态分布

设 $X\sim N(\mu,\sigma^2)$、$\sigma>0$，写成 $X=\mu+\sigma Z$，其中 $Z\sim N(0,1)$。

标准正态密度

$$
\phi(z)=\frac{1}{\sqrt{2\pi}}e^{-z^2/2}
$$

关于零对称且一阶绝对矩有限，所以 $E(Z)=0$。又有 $\phi'(z)=-z\phi(z)$，故

$$
\begin{aligned}
E(Z^2)
&=\int_{\mathbb R}z^2\phi(z)\,dz
=-\int_{\mathbb R}z\phi'(z)\,dz\\
&=[-z\phi(z)]_{-\infty}^{\infty}+\int_{\mathbb R}\phi(z)\,dz=1.
\end{aligned}
$$

于是

$$
\boxed{E(X)=\mu},\qquad
\boxed{\operatorname{Var}(X)=\sigma^2}.
$$

### 1.8 常见分布的均值、方差与参数

| 分布 | 参数或支持集 | 均值 | 方差 |
|---|---|---|---|
| 点质量 $X=a$ | a.s. | $a$ | $0$ |
| Bernoulli$(p)$ | $0\le p\le1$ | $p$ | $p(1-p)$ |
| Binomial$(n,p)$ | $0,\ldots,n$ | $np$ | $np(1-p)$ |
| Geometric$(p)$ | $1,2,\ldots$ | $1/p$ | $(1-p)/p^2$ |
| Poisson$(\lambda)$ | $0,1,\ldots$ | $\lambda$ | $\lambda$ |
| Unif$(a,b)$ | $a<b$ | $(a+b)/2$ | $(b-a)^2/12$ |
| Exp$(\lambda)$ | 率 $\lambda>0$ | $1/\lambda$ | $1/\lambda^2$ |
| Gamma$(\alpha,\lambda)$ | 形状 $\alpha>0$、率 $\lambda>0$ | $\alpha/\lambda$ | $\alpha/\lambda^2$ |
| $\chi^2(\nu)$ | 自由度 $\nu>0$ | $\nu$ | $2\nu$ |
| $N(\mu,\sigma^2)$ | $\sigma^2>0$；可另作退化扩展 | $\mu$ | $\sigma^2$ |
| Student $t(\nu)$ | $\nu>0$ | $0$，要求 $\nu>1$ | $\nu/(\nu-2)$，要求 $\nu>2$ |

**Student $t$ 的边界条件**：$\nu\le1$ 时均值未定义；$1<\nu\le2$ 时均值存在而二阶矩发散，没有有限方差。不能把 $\nu\le2$ 直接代入方差公式。

常见连续分布的密度为

$$
\begin{aligned}
\operatorname{Unif}(a,b):\quad&f(x)=\frac1{b-a},&&a<x<b;\\
\operatorname{Exp}(\lambda):\quad&f(x)=\lambda e^{-\lambda x},&&x>0;\\
\operatorname{Gamma}(\alpha,\lambda):\quad&f(x)=\frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\lambda x},&&x>0;\\
N(\mu,\sigma^2):\quad&f(x)=\frac1{\sigma\sqrt{2\pi}}
e^{-(x-\mu)^2/(2\sigma^2)},&&x\in\mathbb R.
\end{aligned}
$$

密度在相应支持集外为零。Gamma 函数为

$$
\Gamma(\alpha)=\int_0^\infty u^{\alpha-1}e^{-u}\,du,
\qquad \Gamma(\alpha+1)=\alpha\Gamma(\alpha).
$$

**推导**：若 $X\sim\operatorname{Gamma}(\alpha,\lambda)$，则对非负整数 $r$，

$$
E(X^r)=\frac{\Gamma(\alpha+r)}{\Gamma(\alpha)\lambda^r}.
$$

取 $r=1,2$ 得 $E(X)=\alpha/\lambda$、$E(X^2)=\alpha(\alpha+1)/\lambda^2$，因而方差为 $\alpha/\lambda^2$。

若使用尺度参数 $\theta=1/\lambda$，同一分布的均值、方差则写为 $\alpha\theta$、$\alpha\theta^2$。读题时先确定参数约定。

## 2. 矩与矩母函数：从数字特征到分布

均值与方差只能概括部分分布特征。矩将这一描述扩展到更高阶；矩母函数则把各阶矩编码为一个函数，使计算矩、识别分布和研究独立和使用同一套工具。

### 2.1 原点矩、中心矩与绝对矩

对正整数 $r$，在相应绝对矩有限时：

$$
\text{$r$ 阶原点矩：}\quad m_r'=E(X^r),
$$

$$
\text{$r$ 阶中心矩：}\quad m_r=E[(X-\mu)^r].
$$

其中 $\mu=E(X)$。具体来说：

| 阶数 | 原点矩 | 中心矩 |
|---|---|---|
| 一阶 | $E(X)=\mu$ | $E(X-\mu)=0$ |
| 二阶 | $E(X^2)$ | $E[(X-\mu)^2]=\operatorname{Var}(X)$ |
| 三阶 | $E(X^3)$ | $E[(X-\mu)^3]$ |
| 四阶 | $E(X^4)$ | $E[(X-\mu)^4]$ |

进一步理解：当标准差为正且所需矩有限时，偏度为 $E[(X-\mu)^3]/\sigma^3$，峰度为 $E[(X-\mu)^4]/\sigma^4$。偏度描述分布的不对称性；峰度对极端偏离较敏感，但仅凭峰度并不能完整描述尾部。

### 2.2 矩母函数的定义与存在性

定义

$$
\boxed{M_X(t)=E(e^{tX})}.
$$

这里“MGF 存在”指存在 $h>0$，使

$$
M_X(t)<\infty,\qquad \forall t\in(-h,h).
$$

因此必须在零点的**一个双侧开邻域**内有限，仅知道 $M_X(0)=1$ 并不够。

离散与连续计算式分别为

$$
M_X(t)=\sum_xe^{tx}p_X(x),
\qquad
M_X(t)=\int_{\mathbb R}e^{tx}f_X(x)\,dx.
$$

基本性质：

1. $M_X(0)=1$。
2. 若在零点邻域有限，则零点附近可以任意次求导，特别地在零点连续。
3. 不要求对所有实数 $t$ 都有限。例如指数分布只在 $t<\lambda$ 时有限，但这已经包含零点邻域。

**为什么要写定义域？** 积分计算可能得到一个代数表达式，但该表达式只在积分收敛的参数范围内代表 MGF。例如 $\lambda/(\lambda-t)$ 在 $t>\lambda$ 时虽然仍可写出，却为负数，不可能等于正随机变量 $e^{tX}$ 的期望。

#### 为什么 MGF 存在能控制所有矩

取 $\delta>0$，使 $M_X(\delta)$ 和 $M_X(-\delta)$ 都有限。由

$$
e^{\delta|X|}\le e^{\delta X}+e^{-\delta X}
$$

可知 $E(e^{\delta|X|})<\infty$。而指数函数的级数给出

$$
|X|^r\le\frac{r!}{\delta^r}e^{\delta|X|},
$$

所以所有正整数阶绝对矩都有限。

反过来不成立。**反例**：若 $Z\sim N(0,1)$、$X=e^Z$，则 $E(X^r)=e^{r^2/2}$ 对每个正整数 $r$ 都有限，但任意 $t>0$ 时

$$
E(e^{tX})=\frac1{\sqrt{2\pi}}\int_{\mathbb R}
\exp(te^z-z^2/2)\,dz=\infty.
$$

因为 $z\to\infty$ 时 $te^z$ 的增长超过 $z^2/2$。因此对数正态变量没有在零点双侧邻域有限的 MGF。

### 2.3 利用 MGF 生成矩

若 MGF 在零点邻域有限，则

$$
\boxed{M_X^{(r)}(0)=E(X^r)}.
$$

特别地，

$$
\boxed{E(X)=M_X'(0)},\qquad
\boxed{\operatorname{Var}(X)=M_X''(0)-[M_X'(0)]^2}.
$$

#### 证明与交换次序的条件

对于固定 $x$，

$$
\frac{d^r}{dt^r}e^{tx}=x^re^{tx}.
$$

在 MGF 有限的开区间内部，可以把求导移入期望，得到

$$
M_X^{(r)}(t)=E(X^re^{tX}).
$$

令 $t=0$ 即得结论。

这里“可交换求导与积分”不是无条件成立。**条件说明**：对零点附近的 $t$，可以用一个可积的指数函数控制 $|X|^re^{tX}$，从而使用控制收敛一类结论。这就是零点邻域有限条件的实际作用。

另一个理解方式是零点附近的展开式：

$$
M_X(t)=\sum_{r=0}^{\infty}\frac{E(X^r)}{r!}t^r.
$$

MGF 把各阶原点矩编码为 Taylor 系数，因此称“矩母函数”。注意生成的是**原点矩**，二阶导数不是方差。

### 2.4 三个核心例子：Poisson、指数、正态

#### 2.4.1 Poisson 分布

若 $X\sim\operatorname{Poisson}(\lambda)$，则

$$
\begin{aligned}
M_X(t)
&=\sum_{k=0}^{\infty}e^{tk}e^{-\lambda}\frac{\lambda^k}{k!}\\
&=e^{-\lambda}\sum_{k=0}^{\infty}\frac{(\lambda e^t)^k}{k!}\\
&=\boxed{\exp[\lambda(e^t-1)]},\qquad t\in\mathbb R.
\end{aligned}
$$

求导：

$$
M_X'(t)=\lambda e^tM_X(t),
$$

$$
M_X''(t)=(\lambda e^t+\lambda^2e^{2t})M_X(t).
$$

所以

$$
E(X)=\lambda,\qquad E(X^2)=\lambda+\lambda^2,
\qquad\boxed{\operatorname{Var}(X)=\lambda}.
$$

#### 2.4.2 指数分布

若 $X\sim\operatorname{Exp}(\lambda)$，则当 $t<\lambda$ 时，

$$
M_X(t)=\int_0^\infty\lambda e^{-(\lambda-t)x}\,dx
=\boxed{\frac\lambda{\lambda-t}}.
$$

当 $t\ge\lambda$ 时积分发散。

$$
M_X'(t)=\frac\lambda{(\lambda-t)^2},\qquad
M_X''(t)=\frac{2\lambda}{(\lambda-t)^3}.
$$

从而

$$
E(X)=\frac1\lambda,\quad E(X^2)=\frac2{\lambda^2},\quad
\operatorname{Var}(X)=\frac1{\lambda^2}.
$$

进一步理解：一般有 $M_X^{(r)}(0)=r!/\lambda^r$，即 $E(X^r)=r!/\lambda^r$。

#### 2.4.3 正态分布：配方是关键

若 $X\sim N(\mu,\sigma^2)$、$\sigma>0$，则

$$
M_X(t)=\int_{\mathbb R}\frac1{\sigma\sqrt{2\pi}}
\exp\left(tx-\frac{(x-\mu)^2}{2\sigma^2}\right)dx.
$$

对指数中的二次式配方：

$$
tx-\frac{(x-\mu)^2}{2\sigma^2}
=-\frac{[x-(\mu+\sigma^2t)]^2}{2\sigma^2}
+\mu t+\frac12\sigma^2t^2.
$$

于是

$$
\begin{aligned}
M_X(t)
&=e^{\mu t+\sigma^2t^2/2}
\int_{\mathbb R}\frac1{\sigma\sqrt{2\pi}}
e^{-[x-(\mu+\sigma^2t)]^2/(2\sigma^2)}\,dx\\
&=\boxed{e^{\mu t+\sigma^2t^2/2}},\qquad t\in\mathbb R.
\end{aligned}
$$

积分等于 1，因为积分中的函数是均值为 $\mu+\sigma^2t$、方差为 $\sigma^2$ 的正态密度。

求导得

$$
M_X'(t)=(\mu+\sigma^2t)M_X(t),
$$

$$
M_X''(t)=[(\mu+\sigma^2t)^2+\sigma^2]M_X(t).
$$

因此

$$
E(X)=\mu,\quad E(X^2)=\mu^2+\sigma^2,\quad
\operatorname{Var}(X)=\sigma^2.
$$

### 2.5 MGF 的唯一性

若 $M_X$、$M_Y$ 在某个共同的开区间 $(-h,h)$ 上有限，而且

$$
M_X(t)=M_Y(t),\qquad\forall t\in(-h,h),
$$

则

$$
\boxed{X\overset d=Y}.
$$

$\overset d=$ 表示**同分布**，不表示二者是同一个随机变量，也不表示逐次取值相等。

唯一性是变换理论的基本结论；此处着重掌握其条件与应用，不展开一般变换唯一性证明。

**典型解题链**：

1. 根据定义或性质求目标变量的 MGF。
2. 写出其有限的区间，确认包含零点邻域。
3. 与某个已知分布的 MGF 比较。
4. 用唯一性说明目标变量服从该分布。

仅比较前两个导数，只能证明均值和二阶矩相同，不能证明同分布。

### 2.6 独立线性组合与仿射变换

若 $X_1,\ldots,X_n$ 相互独立且 MGF 在零点邻域有限，令

$$
Y=b+\sum_{k=1}^na_kX_k,
$$

则在各因子均有限时，

$$
\boxed{M_Y(t)=e^{bt}\prod_{k=1}^nM_{X_k}(a_kt)}.
$$

证明：

$$
\begin{aligned}
M_Y(t)
&=E\left[e^{bt}\prod_{k=1}^ne^{ta_kX_k}\right]\\
&=e^{bt}\prod_{k=1}^nE(e^{ta_kX_k})
=e^{bt}\prod_{k=1}^nM_{X_k}(a_kt).
\end{aligned}
$$

将期望中的乘积拆开的一步使用了相互独立性。

两个常用特例：

$$
\boxed{M_{aX+b}(t)=e^{bt}M_X(at)},
$$

$$
\boxed{M_{X+Y}(t)=M_X(t)M_Y(t)\quad(X\perp Y)}.
$$

单变量仿射变换公式无需独立性；多个变量的乘法公式才需要。

### 2.7 二项分布及其可加性

#### 二项分布的 MGF

若 $Y\sim\operatorname{Binomial}(n,p)$，则由二项式定理，

$$
\begin{aligned}
M_Y(t)
&=\sum_{y=0}^ne^{ty}\binom ny p^y(1-p)^{n-y}\\
&=\sum_{y=0}^n\binom ny(pe^t)^y(1-p)^{n-y}\\
&=\boxed{(1-p+pe^t)^n},\qquad t\in\mathbb R.
\end{aligned}
$$

#### 独立同参数 Bernoulli 之和

若 $X_k\overset{\mathrm{iid}}\sim\operatorname{Bernoulli}(p)$，则

$$
M_{X_k}(t)=1-p+pe^t.
$$

令 $Y=\sum_{k=1}^nX_k$，由独立性，

$$
M_Y(t)=\prod_{k=1}^n(1-p+pe^t)=(1-p+pe^t)^n.
$$

与二项分布的 MGF 相同，故由唯一性，

$$
\boxed{Y\sim\operatorname{Binomial}(n,p)}.
$$

#### 独立同成功概率的二项分布之和

设 $X_k\sim\operatorname{Binomial}(n_k,p)$，$k=1,\ldots,m$，相互独立。则

$$
M_{\sum X_k}(t)
=\prod_{k=1}^m(1-p+pe^t)^{n_k}
=(1-p+pe^t)^{\sum_{k=1}^mn_k}.
$$

所以

$$
\boxed{\sum_{k=1}^mX_k\sim\operatorname{Binomial}\left(\sum_{k=1}^mn_k,p\right)}.
$$

**必须同一个 $p$。** 若成功概率不同，独立 Bernoulli 之和一般是 Poisson-binomial 分布，不能直接套普通二项分布公式。

### 2.8 正态变量线性组合、标准化与卡方

#### 2.8.1 独立正态线性组合

设 $X_k\sim N(\mu_k,\sigma_k^2)$ 相互独立，令 $Y=\sum_ka_kX_k$。则

$$
\begin{aligned}
M_Y(t)
&=\prod_k\exp\left(a_k\mu_kt+\frac12a_k^2\sigma_k^2t^2\right)\\
&=\exp\left[t\sum_ka_k\mu_k+\frac{t^2}{2}\sum_ka_k^2\sigma_k^2\right].
\end{aligned}
$$

这是正态分布的 MGF，所以

$$
\boxed{\sum_ka_kX_k\sim
N\left(\sum_ka_k\mu_k,\sum_ka_k^2\sigma_k^2\right)}.
$$

若方差为零，则 $Y$ 几乎必然等于其均值。

**边界提醒**：仅知道每个 $X_k$ 的边缘分布是正态，不足以推出线性组合正态。独立正态是充分条件；更一般的充分条件是这些变量联合正态，后者的方差可能含非零协方差项。

#### 2.8.2 正态标准化

若 $X\sim N(\mu,\sigma^2)$ 且 $\sigma>0$，令 $Z=(X-\mu)/\sigma$。由仿射变换公式，

$$
M_Z(t)=e^{-\mu t/\sigma}M_X(t/\sigma)=e^{t^2/2}.
$$

因此

$$
\boxed{\frac{X-\mu}{\sigma}\sim N(0,1)}.
$$

**重要区别**：任何正方差变量都可“减均值、除标准差”，得到均值 0、方差 1 的变量；只有原变量正态时，才能进一步断言标准化结果服从标准正态。

#### 2.8.3 标准正态的平方

若 $Z\sim N(0,1)$，当 $t<1/2$ 时，

$$
\begin{aligned}
M_{Z^2}(t)
&=\frac1{\sqrt{2\pi}}\int_{\mathbb R}
e^{-(1-2t)z^2/2}\,dz\\
&=(1-2t)^{-1/2}.
\end{aligned}
$$

这是 $\chi^2(1)$ 的 MGF，所以

$$
\boxed{Z^2\sim\chi^2(1)}.
$$

积分可通过 $u=\sqrt{1-2t}\,z$ 化为标准正态积分。若 $t\ge1/2$，该积分发散。

若 $Z_1,\ldots,Z_n$ 独立且均为标准正态，则

$$
\boxed{\sum_{k=1}^nZ_k^2\sim\chi^2(n)}.
$$

### 2.9 常见 MGF 汇总

下表汇总常见分布的 MGF 与收敛范围，用于识别分布和计算矩。

| 分布 | $M_X(t)$ | 有限的 $t$ 范围 |
|---|---|---|
| 点质量 $X=a$ | $e^{at}$ | $\mathbb R$ |
| Bernoulli$(p)$ | $1-p+pe^t$ | $\mathbb R$ |
| Binomial$(n,p)$ | $(1-p+pe^t)^n$ | $\mathbb R$ |
| Poisson$(\lambda)$ | $e^{\lambda(e^t-1)}$ | $\mathbb R$ |
| Geometric$(p)$，$0<p<1$ | $pe^t/[1-(1-p)e^t]$ | $t<-\log(1-p)$ |
| Unif$(a,b)$ | $(e^{bt}-e^{at})/[(b-a)t]$，$t=0$ 处取 $1$ | $\mathbb R$ |
| Exp$(\lambda)$ | $\lambda/(\lambda-t)$ | $t<\lambda$ |
| Gamma$(\alpha,\lambda)$ | $(\lambda/(\lambda-t))^\alpha$ | $t<\lambda$ |
| $\chi^2(\nu)$ | $(1-2t)^{-\nu/2}$ | $t<1/2$ |
| $N(\mu,\sigma^2)$ | $e^{\mu t+\sigma^2t^2/2}$ | $\mathbb R$ |

几何分布公式来自

$$
\sum_{k=1}^\infty e^{tk}p(1-p)^{k-1}
=pe^t\sum_{j=0}^\infty[(1-p)e^t]^j.
$$

当 $p=1$ 时是点质量 $X=1$，MGF 为 $e^t$，对所有 $t$ 有限。

Gamma 的 MGF 可通过替换率参数推得：

$$
\begin{aligned}
M_X(t)
&=\frac{\lambda^\alpha}{\Gamma(\alpha)}
\int_0^\infty x^{\alpha-1}e^{-(\lambda-t)x}\,dx\\
&=\frac{\lambda^\alpha}{(\lambda-t)^\alpha},\qquad t<\lambda.
\end{aligned}
$$

并且

$$
\chi^2(\nu)=\operatorname{Gamma}\left(\frac\nu2,\frac12\right)
\quad\text{（此处第二个参数是率）}.
$$

### 2.10 分布的可加性

下表每一行的随机变量都要求相互独立。

| 各项分布 | 和的分布 | 额外条件 |
|---|---|---|
| $X_k\sim\operatorname{Poisson}(\lambda_k)$ | $\operatorname{Poisson}(\sum_k\lambda_k)$ | 无需各率相同 |
| $X_k\sim\operatorname{Binomial}(n_k,p)$ | $\operatorname{Binomial}(\sum_kn_k,p)$ | 同一个 $p$ |
| $X_k\sim\operatorname{Gamma}(\alpha_k,\lambda)$ | $\operatorname{Gamma}(\sum_k\alpha_k,\lambda)$ | 同一个率 $\lambda$ |
| $X_k\sim\chi^2(\nu_k)$ | $\chi^2(\sum_k\nu_k)$ | 自由度相加 |
| $X_k\sim N(\mu_k,\sigma_k^2)$ | $N(\sum_k\mu_k,\sum_k\sigma_k^2)$ | 均值、方差分别相加 |

证明都遵循“MGF 相乘，再使用唯一性”。例如

$$
\prod_ke^{\lambda_k(e^t-1)}
=e^{(\sum_k\lambda_k)(e^t-1)},
$$

$$
\prod_k\left(\frac\lambda{\lambda-t}\right)^{\alpha_k}
=\left(\frac\lambda{\lambda-t}\right)^{\sum_k\alpha_k},
$$

$$
\prod_k(1-2t)^{-\nu_k/2}
=(1-2t)^{-(\sum_k\nu_k)/2}.
$$

“参数相加”有不同含义：Poisson 加的是率；Gamma 在同率下加的是形状；正态加的是方差，不能把标准差直接相加。

### 2.11 指数变量之和与最小值：容易混淆的两个结论

#### 2.11.1 同率独立指数变量之和

若 $X_1,\ldots,X_n\overset{\mathrm{iid}}\sim\operatorname{Exp}(\lambda)$，则

$$
M_{\sum X_k}(t)=\left(\frac\lambda{\lambda-t}\right)^n,
\qquad t<\lambda.
$$

所以

$$
\boxed{\sum_{k=1}^nX_k\sim\operatorname{Gamma}(n,\lambda)}.
$$

整数形状的 Gamma 也称 Erlang 分布。$n>1$ 时通常不是指数分布。

直观解释：若每个 $X_k$ 是相邻事件之间的等待时间，则总和是等到第 $n$ 个事件的时间。

#### 2.11.2 不同率独立指数变量的最小值

若 $X_k\sim\operatorname{Exp}(\lambda_k)$ 相互独立，令 $W=\min_kX_k$。对 $x\ge0$，

$$
\begin{aligned}
P(W>x)
&=P(X_1>x,\ldots,X_n>x)\\
&=\prod_{k=1}^nP(X_k>x)\\
&=\prod_{k=1}^ne^{-\lambda_kx}
=e^{-x\sum_k\lambda_k}.
\end{aligned}
$$

对 $x<0$，$P(W>x)=1$。这正是指数分布的生存函数，故

$$
\boxed{\min_kX_k\sim\operatorname{Exp}\left(\sum_k\lambda_k\right)}.
$$

直观解释：几个独立“时钟”同时运行，只等最先响的一个，等待时间更短，因而率相加。

| 操作 | 自然方法 | 结果 |
|---|---|---|
| 同率独立指数变量求和 | MGF 相乘 | Gamma |
| 独立指数变量取最小值 | 生存函数相乘 | 指数，率相加 |

不要把“每个变量都服从指数分布”误读成“它们的和也服从指数分布”。

## 3. 协方差与相关性：刻画变量间的关系

从联合分布计算二元函数的期望，再定义协方差。先掌握协方差的运算与线性组合方差，再讨论标准化后的相关系数、独立性及反例。

### 3.1 两个随机变量的函数的期望

若 $g(X,Y)$ 可积，离散情形下

$$
\boxed{E[g(X,Y)]=\sum_x\sum_y g(x,y)p_{X,Y}(x,y)};
$$

有联合密度时

$$
\boxed{E[g(X,Y)]=\iint_{\mathbb R^2}g(x,y)f_{X,Y}(x,y)\,dx\,dy}.
$$

积分区域要服从联合支持集，而不一定是矩形。例如支持集为 $0<x<y<1$，就可写成 $\int_0^1\int_0^y(\cdots)\,dx\,dy$。

特别地，求 $E(XY)$ 应使用联合分布：

$$
E(XY)=\sum_x\sum_yxy\,p_{X,Y}(x,y)
$$

或对应的二重积分。仅有两个边缘分布通常不足以确定 $E(XY)$。

### 3.2 协方差的定义与意义

若 $E(X^2),E(Y^2)<\infty$，定义

$$
\boxed{\operatorname{Cov}(X,Y)
=E[(X-\mu_X)(Y-\mu_Y)]}.
$$

展开可得

$$
\boxed{\operatorname{Cov}(X,Y)=E(XY)-E(X)E(Y)}.
$$

二阶矩有限足以保证乘积可积，因为

$$
E|XY|\le\sqrt{E(X^2)E(Y^2)}<\infty.
$$

直观上：

- 两个变量经常同时高于各自均值、同时低于各自均值，中心化乘积偏正，协方差可能为正。
- 一个高于均值时另一个倾向低于均值，中心化乘积偏负，协方差可能为负。
- 协方差为零，表示这些中心化乘积平均抵消，不能排除其他依赖形式。

协方差的单位是两个变量单位的乘积，大小受单位影响。例如把 m 换成 cm，相关协方差会相应放大。

基本性质：

$$
\operatorname{Cov}(X,X)=\operatorname{Var}(X),
\qquad
\operatorname{Cov}(X,Y)=\operatorname{Cov}(Y,X).
$$

常数与任何二阶矩有限变量的协方差为零。

### 3.3 协方差的双线性

对二阶矩有限的随机变量，

$$
\boxed{
\operatorname{Cov}\left(\sum_i a_iX_i,\sum_jb_jY_j\right)
=\sum_i\sum_ja_ib_j\operatorname{Cov}(X_i,Y_j)
}.
$$

证明：对两组线性组合分别减去均值，乘积展开后取期望，即得右边。

常用特例：

$$
\operatorname{Cov}(aX+b,cY+d)=ac\operatorname{Cov}(X,Y),
$$

$$
\operatorname{Cov}(X+Y,Z)=\operatorname{Cov}(X,Z)+\operatorname{Cov}(Y,Z).
$$

上述性质都**不要求独立**。常数平移不影响协方差，缩放系数分别出现一次。

### 3.4 一般线性组合的方差

$$
\boxed{
\operatorname{Var}\left(\sum_i a_iX_i\right)
=\sum_i a_i^2\operatorname{Var}(X_i)
+2\sum_{i<j}a_ia_j\operatorname{Cov}(X_i,X_j)
}.
$$

推导：

$$
\operatorname{Var}(U)=\operatorname{Cov}(U,U)
=\sum_i\sum_ja_ia_j\operatorname{Cov}(X_i,X_j).
$$

将对角项 $i=j$ 分离，并将两个相同的非对角项合并，就出现系数 2。

特别地，

$$
\boxed{\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y)},
$$

$$
\boxed{\operatorname{Var}(X-Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)-2\operatorname{Cov}(X,Y)}.
$$

即使两个变量相减，各自方差仍是相加；改变符号的是协方差项。

**解释**：正相关变量相加时，波动会相互加强；相减时，共同变化会部分抵消。负相关情形则相反。

#### 矩阵写法

若 $\mathbf X=(X_1,\ldots,X_n)^\mathsf T$，协方差矩阵 $\Sigma$ 的第 $(i,j)$ 元为 $\operatorname{Cov}(X_i,X_j)$，则

$$
\operatorname{Var}(\mathbf a^\mathsf T\mathbf X)=\mathbf a^\mathsf T\Sigma\mathbf a\ge0.
$$

因此协方差矩阵必为对称半正定矩阵。这一形式将一维方差公式与多维正态模型联系起来。

### 3.5 相关系数：标准化的协方差

若 $0<\sigma_X,\sigma_Y<\infty$，定义

$$
\boxed{\rho_{X,Y}=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}}.
$$

也可以写成

$$
\rho_{X,Y}=E\left[
\frac{X-\mu_X}{\sigma_X}
\frac{Y-\mu_Y}{\sigma_Y}
\right].
$$

相关系数没有单位，衡量的是**线性关联**。如果任一变量方差为零，分母为零，通常的相关系数未定义，不能写成零。

进一步理解：若 $a,c\ne0$ 且原相关系数存在，则

$$
\operatorname{Corr}(aX+b,cY+d)=\operatorname{sgn}(ac)\operatorname{Corr}(X,Y).
$$

因此正向换单位不改变相关系数；反转其中一个变量的方向会改变相关系数的符号。

### 3.6 相关系数的界与等号条件

$$
\boxed{-1\le\rho_{X,Y}\le1}.
$$

证明：令 $U=X-\mu_X$、$V=Y-\mu_Y$，由 Cauchy–Schwarz，

$$
[E(UV)]^2\le E(U^2)E(V^2)=\sigma_X^2\sigma_Y^2.
$$

两边除以正数 $\sigma_X^2\sigma_Y^2$，得到 $\rho^2\le1$。

等号成立当且仅当中心化变量线性相关：

$$
V=aU\quad\text{a.s.}
$$

由于两者方差为正，$a\ne0$，故

$$
\boxed{|\rho|=1\iff Y=aX+b\text{ a.s.，其中 }a\ne0}.
$$

- $a>0$ 时，$\rho=1$。
- $a<0$ 时，$\rho=-1$。

“完全相关”要求几乎必然落在同一条非水平直线上，并非“有某种确定关系”就够了。例如 $Y=X^2$ 是确定关系，但通常不是完全线性相关。

### 3.7 独立与不相关：方向不能颠倒

在二阶矩有限时，

$$
X\perp Y\Longrightarrow E(XY)=E(X)E(Y)
\Longrightarrow\operatorname{Cov}(X,Y)=0.
$$

反方向一般不成立。

| 概念 | 含义 |
|---|---|
| 独立 | 联合分布完全分解；知道一个变量不会改变另一个变量的分布 |
| 不相关 | 协方差为零；中心化后的乘积期望为零 |

#### 3.7.1 离散反例

三点 $(0,1),(1,0),(2,1)$ 各以概率 $1/3$ 出现。

$$
E(X)=1,\qquad E(Y)=\frac23,\qquad E(XY)=\frac23.
$$

所以

$$
\operatorname{Cov}(X,Y)=\frac23-1\cdot\frac23=0.
$$

但

$$
P(X=0,Y=0)=0\ne\frac13\cdot\frac13=P(X=0)P(Y=0).
$$

因此不独立。事实上 $Y=(X-1)^2$，呈非线性依赖。

#### 3.7.2 连续边缘的反例：$Y=X^2$

令 $X\sim\operatorname{Unif}(-1,1)$，$Y=X^2$。由对称性及可积性，

$$
E(X)=0,\qquad E(XY)=E(X^3)=0,
$$

因此 $\operatorname{Cov}(X,Y)=0$。

令

$$
A=\{|X|\le1/2\},\qquad B=\{Y\le1/4\}.
$$

因为 $Y=X^2$，实际上 $A=B$。所以

$$
P(A\cap B)=\frac12,
\qquad P(A)P(B)=\frac14,
$$

二者不相等，故 $X,Y$ 不独立。

**进一步解释**：这里 $Y$ 完全由 $X$ 决定，但相关系数为零。这说明相关系数无法检测全部非线性依赖。

**特殊例外**：如果 $(X,Y)$ 联合正态，则不相关可以推出独立。条件必须是“联合正态”，而非“两个边缘都正态”。

### 3.8 从联合概率表计算相关系数

给定

$$
p_{X,Y}(x,y)=\frac{x+2y}{18},\qquad x,y\in\{1,2\}.
$$

先列联合表及边缘分布：

| $X\backslash Y$ | $Y=1$ | $Y=2$ | $p_X(x)$ |
|---|---|---|---|
| $X=1$ | $3/18$ | $5/18$ | $8/18=4/9$ |
| $X=2$ | $4/18$ | $6/18$ | $10/18=5/9$ |
| $p_Y(y)$ | $7/18$ | $11/18$ | $1$ |

#### 第一步：分别计算边缘矩

$$
E(X)=1\cdot\frac49+2\cdot\frac59=\frac{14}{9},
$$

$$
E(X^2)=1\cdot\frac49+4\cdot\frac59=\frac83.
$$

所以

$$
\operatorname{Var}(X)=\frac83-\left(\frac{14}{9}\right)^2=\frac{20}{81}.
$$

同理，

$$
E(Y)=\frac{29}{18},\qquad E(Y^2)=\frac{17}{6},
$$

$$
\operatorname{Var}(Y)=\frac{17}{6}-\left(\frac{29}{18}\right)^2=\frac{77}{324}.
$$

#### 第二步：计算交叉矩

$$
\begin{aligned}
E(XY)
&=1\cdot1\cdot\frac3{18}
+1\cdot2\cdot\frac5{18}
+2\cdot1\cdot\frac4{18}
+2\cdot2\cdot\frac6{18}\\
&=\frac{3+10+8+24}{18}=\frac52.
\end{aligned}
$$

于是

$$
\operatorname{Cov}(X,Y)
=\frac52-\frac{14}{9}\frac{29}{18}
=-\frac1{162}.
$$

#### 第三步：标准化

$$
\boxed{\rho_{X,Y}
=\frac{-1/162}{\sqrt{(20/81)(77/324)}}
=-\frac1{\sqrt{1540}}\approx-0.0255}.
$$

**解释**：二者的线性相关很弱且略为负，但“接近零”不能当作独立证据。这里联合概率也确实不等于边缘概率的乘积。

## 4. 条件期望与方差分解：信息如何改变平均与波动

条件期望把“一个总体平均”细化为“随已知信息变化的组内平均”。先掌握数与随机变量的区别，再学习全期望和全方差，最后将它们用于分层模型。

### 4.1 动机：知道信息后，平均值会改变

某工厂使用机器 $A,B$，令 $X$ 表示产品来自哪台机器，$Y$ 为次品示性变量：

$$
Y=
\begin{cases}1,&\text{次品},\\0,&\text{合格品}.\end{cases}
$$

给定

$$
P(X=A)=0.7,\qquad P(X=B)=0.3,
$$

$$
P(Y=1\mid X=A)=0.02,\qquad
P(Y=1\mid X=B)=0.08.
$$

因为 $Y$ 为示性变量，知道机器后，

$$
E(Y\mid X=A)=0.02,\qquad E(Y\mid X=B)=0.08.
$$

在不知道机器时，整体次品率为

$$
\boxed{E(Y)=0.7\times0.02+0.3\times0.08=0.038}.
$$

#### 三个记号，三种对象

| 表达式 | 类型 | 本例含义 |
|---|---|---|
| $E(Y)$ | 固定数 | 总体次品率 $0.038$ |
| $E(Y\mid X=A)$ | 固定数 | 已指定机器 $A$ 后，组内次品率 $0.02$ |
| $E(Y\mid X)$ | 随机变量 | 根据随机的机器来源，取 $0.02$ 或 $0.08$ |

具体地，

$$
\boxed{E(Y\mid X)=
\begin{cases}
0.02,&X=A,\\
0.08,&X=B.
\end{cases}}
$$

**理解要点**：对已知值 $x$，条件均值是一个数；在尚未固定 $X$ 时，条件均值随 $X$ 变化，因此是随机变量。不要把大写 $X$ 和小写 $x$ 混用。

### 4.2 给定取值的条件期望

#### 4.2.1 离散情形

当 $p_X(x)>0$ 时，

$$
p_{Y\mid X}(y\mid x)=\frac{p_{X,Y}(x,y)}{p_X(x)},
$$

$$
\boxed{E(Y\mid X=x)=\sum_y y\,p_{Y\mid X}(y\mid x)}.
$$

它就是在条件分布下计算普通期望。

#### 4.2.2 有联合密度的情形

当 $f_X(x)>0$ 时，可以通过密度比定义条件密度版本：

$$
f_{Y\mid X}(y\mid x)=\frac{f_{X,Y}(x,y)}{f_X(x)},
$$

$$
\boxed{E(Y\mid X=x)=\int_{\mathbb R}y f_{Y\mid X}(y\mid x)\,dy}.
$$

积分区间应由给定 $x$ 后 $Y$ 的条件支持集决定。

**关键解释**：连续型 $X$ 通常有 $P(X=x)=0$，不能把条件概率机械写成“两个零概率相除”。这里使用的是条件密度，它是条件分布的一种表示。条件分布和条件期望的值只需在相应边缘分布下几乎处处确定。

如果联合分布是混合型或集中在曲线上，未必存在通常的联合密度；条件期望本身仍可定义，只是不能套用不适用的密度比公式。

### 4.3 将条件均值视为随机变量

先定义函数

$$
g(x)=E(Y\mid X=x),
$$

再令

$$
\boxed{E(Y\mid X)=g(X)}.
$$

条件期望由 $X$ 决定，只使用 $X$ 所提供的信息。

“定义到零概率事件为止”的含义是：如果两个版本只在一个概率为零的集合上不同，它们代表同一个条件期望。后续的期望、方差等不受该差异影响。

**更一般的刻画。** 对可积 $Y$，$m(X)=E(Y\mid X)$ 是一个可积的、由 $X$ 决定的随机变量，并满足对任意有界可测函数 $h$，

$$
E[h(X)m(X)]=E[h(X)Y].
$$

这条刻画说明：在任何由 $X$ 划定的子群体中，$m(X)$ 与 $Y$ 的总平均保持一致。入门计算时通常直接用条件分布即可。

### 4.4 条件期望的基本性质

以下等式在相关可积性条件下几乎必然成立。

#### 4.4.1 线性性

$$
\boxed{E(aY+bZ\mid X)=aE(Y\mid X)+bE(Z\mid X)}.
$$

$a,b$ 为常数，不要求变量独立。

#### 4.4.2 已知量可以提出

$$
\boxed{E[h(X)Y\mid X]=h(X)E(Y\mid X)}.
$$

给定 $X$ 后，$h(X)$ 是已知量，作用类似常数。例如

$$
E(XY\mid X)=X E(Y\mid X).
$$

严谨使用时，要保证涉及的乘积可积；当 $h$ 有界且 $Y$ 可积时条件自动满足。

#### 4.4.3 已知量的条件期望是其本身

$$
\boxed{E[h(X)\mid X]=h(X)}.
$$

特别地，$E(X\mid X)=X$，而不是 $E(X)$。

#### 4.4.4 独立变量的信息无关性

若 $Y$ 独立于 $X$，则

$$
\boxed{E(Y\mid X)=E(Y)}.
$$

**注意：反过来不成立。** 条件均值恒定只表示 $X$ 不改变 $Y$ 的均值，仍可能改变其方差或其他分布特征。例如令 $U$ 为独立的等概率正负号，$X$ 以正概率分别取 $1,2$，设 $Y=XU$。则

$$
E(Y\mid X)=0=E(Y),\qquad \operatorname{Var}(Y\mid X)=X^2.
$$

$|Y|=X$，所以二者依赖。

#### 4.4.5 不可任意拆乘积

一般不能写成

$$
E(YZ\mid X)=E(Y\mid X)E(Z\mid X).
$$

给定 $X$ 后 $Y,Z$ 条件独立是使该分解成立的一种充分条件，仍需相应可积性。

### 4.5 全期望公式：先分组平均，再总体平均

若 $E|Y|<\infty$，则

$$
\boxed{E[E(Y\mid X)]=E(Y)}.
$$

离散情形：

$$
\boxed{E(Y)=\sum_xE(Y\mid X=x)p_X(x)}.
$$

连续情形：

$$
\boxed{E(Y)=\int_{\mathbb R}E(Y\mid X=x)f_X(x)\,dx}.
$$

分组均值必须按组的概率加权，不能对各组均值简单取平均，除非各组等概率。

#### 离散证明

$$
\begin{aligned}
E[E(Y\mid X)]
&=\sum_x\left[\sum_y y p_{Y\mid X}(y\mid x)\right]p_X(x)\\
&=\sum_x\sum_y y p_{X,Y}(x,y)\\
&=\sum_y y\sum_xp_{X,Y}(x,y)\\
&=\sum_y y p_Y(y)=E(Y).
\end{aligned}
$$

绝对可积保证交换求和合法。连续证明将求和换为积分，并使用相同的联合密度分解。

#### 概率版与更一般的塔式性质

令 $Y=\mathbf1_A$，则

$$
P(A)=E[P(A\mid X)],
$$

即全概率公式是全期望公式的一个特例。

若信息 $\mathcal G$ 包含在 $\mathcal H$ 中，则

$$
E[E(Y\mid\mathcal H)\mid\mathcal G]=E(Y\mid\mathcal G).
$$

先用更详细的信息求均值，再按较少信息平均，等于直接用较少信息求均值。信息必须具有相应嵌套关系，不能随意交换或删除条件。

### 4.6 例题：离散条件期望

给定

$$
p_{X,Y}(x,y)=\frac{x+y}{4},\qquad x,y\in\{0,1\}.
$$

联合表为

| $X\backslash Y$ | $Y=0$ | $Y=1$ | $p_X(x)$ |
|---|---|---|---|
| $X=0$ | $0$ | $1/4$ | $1/4$ |
| $X=1$ | $1/4$ | $1/2$ | $3/4$ |
| $p_Y(y)$ | $1/4$ | $3/4$ | $1$ |

给定 $X=0$，$Y=1$ 的条件概率为 1，因此

$$
E(Y\mid X=0)=1.
$$

给定 $X=1$，

$$
P(Y=1\mid X=1)=\frac{1/2}{3/4}=\frac23,
$$

因此 $E(Y\mid X=1)=2/3$。写成随机变量形式：

$$
\boxed{E(Y\mid X)=1-\frac X3}.
$$

外层期望为

$$
E[E(Y\mid X)]
=1\cdot\frac14+\frac23\cdot\frac34
=\boxed{\frac34}.
$$

另一方面 $Y\sim\operatorname{Bernoulli}(3/4)$，所以 $E(Y)=3/4$，全期望公式得到验证。

**容易写错的地方**：求外层期望时，权重是 $X$ 的边缘分布 $1/4,3/4$，不是 $Y$ 的条件概率，也不是各乘 $1/2$。

### 4.7 条件方差

若 $E(Y^2)<\infty$，定义

$$
\boxed{\operatorname{Var}(Y\mid X)
=E[(Y-E(Y\mid X))^2\mid X]}.
$$

计算公式为

$$
\boxed{\operatorname{Var}(Y\mid X)
=E(Y^2\mid X)-[E(Y\mid X)]^2}.
$$

推导与普通方差公式类似，但要把 $E(Y\mid X)$ 当作“给定 $X$ 后已知的量”提出条件期望。

**三个不同对象**：

| 对象 | 含义 |
|---|---|
| $\operatorname{Var}(Y\mid X=x)$ | 指定一组后，组内方差；是数 |
| $\operatorname{Var}(Y\mid X)$ | 随组别变化的组内方差；是随机变量 |
| $\operatorname{Var}(E(Y\mid X))$ | 各组均值的总体波动；是数 |

条件方差的中心是条件均值 $E(Y\mid X)$，不是总体均值 $E(Y)$。

### 4.8 全方差公式

若 $E(Y^2)<\infty$，则

$$
\boxed{\operatorname{Var}(Y)
=E[\operatorname{Var}(Y\mid X)]
+\operatorname{Var}(E(Y\mid X))}.
$$

其含义是

$$
\boxed{\text{总体波动}=\text{平均组内波动}+\text{组间均值波动}}.
$$

#### 4.8.1 代数证明

由条件方差公式和全期望公式，

$$
E[\operatorname{Var}(Y\mid X)]
=E(Y^2)-E\{[E(Y\mid X)]^2\}.
$$

另一方面，

$$
\operatorname{Var}(E(Y\mid X))
=E\{[E(Y\mid X)]^2\}-[E(Y)]^2.
$$

两式相加，中间项抵消，得到 $E(Y^2)-[E(Y)]^2$。

#### 4.8.2 为什么两部分可以相加

令 $m(X)=E(Y\mid X)$，分解

$$
Y-E(Y)=[Y-m(X)]+[m(X)-E(Y)].
$$

第一项是“组内残差”，第二项是“组均值相对总体均值的偏移”。交叉项的期望为零：

$$
\begin{aligned}
E\{[Y-m(X)][m(X)-E(Y)]\}
&=E\{[m(X)-E(Y)]E[Y-m(X)\mid X]\}\\
&=0.
\end{aligned}
$$

平方后取期望便得到全方差公式。

#### 4.8.3 重要推论与边界

$$
\operatorname{Var}(E(Y\mid X))\le\operatorname{Var}(Y),
$$

$$
E[\operatorname{Var}(Y\mid X)]\le\operatorname{Var}(Y).
$$

这些是总体或平均意义上的比较。**不能据此断言每个 $x$ 都满足** $\operatorname{Var}(Y\mid X=x)\le\operatorname{Var}(Y)$；某个特定组的方差可以更大。

### 4.9 应用：机器次品例子的方差分解

总体 $Y\sim\operatorname{Bernoulli}(0.038)$，所以

$$
\operatorname{Var}(Y)=0.038(1-0.038)=0.036556.
$$

组内方差平均：

$$
E[\operatorname{Var}(Y\mid X)]
=0.7(0.02\times0.98)+0.3(0.08\times0.92)
=0.0358.
$$

组间均值方差：

$$
\begin{aligned}
\operatorname{Var}(E(Y\mid X))
&=0.7(0.02-0.038)^2+0.3(0.08-0.038)^2\\
&=0.000756.
\end{aligned}
$$

两者相加确为 $0.036556$。这个例子把“组内随机性”与“机器质量差异”分开了。

### 4.10 全协方差公式

若 $Y,Z$ 二阶矩有限，则

$$
\boxed{
\operatorname{Cov}(Y,Z)
=E[\operatorname{Cov}(Y,Z\mid X)]
+\operatorname{Cov}(E(Y\mid X),E(Z\mid X))
}.
$$

其中

$$
\operatorname{Cov}(Y,Z\mid X)
=E(YZ\mid X)-E(Y\mid X)E(Z\mid X).
$$

对其取期望并加上条件均值之间的协方差，即可消去中间乘积项，得到公式。取 $Z=Y$，就是全方差公式。

设 $I_i,I_j$ 是共享随机成功概率 $Q$ 的两个示性变量，给定 $Q$ 后条件独立，且条件均值都为 $Q$。此时公式的第一项为零，第二项为 $\operatorname{Var}(Q)$。这说明共同随机环境可以诱导总体依赖；后面的分层二项模型将给出具体计算。

### 4.11 例题：两阶段均匀模型

首先抽取

$$
X\sim\operatorname{Unif}(0,1),
$$

再在给定 $X=x$ 后抽取

$$
Y\mid X=x\sim\operatorname{Unif}(x,1).
$$

要求 $E(Y\mid X)$、$\operatorname{Var}(Y\mid X)$、$E(Y)$、$\operatorname{Var}(Y)$。

#### 第一步：直接使用条件均匀分布

对 $0<x<1$，均匀区间的中点和长度分别为 $(x+1)/2$、$1-x$，所以

$$
\boxed{E(Y\mid X)=\frac{X+1}{2}},
\qquad
\boxed{\operatorname{Var}(Y\mid X)=\frac{(1-X)^2}{12}}.
$$

#### 第二步：全期望公式

$$
\boxed{E(Y)=E\left(\frac{X+1}{2}\right)=\frac{1/2+1}{2}=\frac34}.
$$

#### 第三步：全方差公式

$$
\begin{aligned}
E[\operatorname{Var}(Y\mid X)]
&=\frac1{12}E[(1-X)^2]\\
&=\frac1{12}\int_0^1(1-x)^2\,dx=\frac1{36}.
\end{aligned}
$$

$$
\operatorname{Var}(E(Y\mid X))
=\operatorname{Var}\left(\frac{X+1}{2}\right)
=\frac14\cdot\frac1{12}=\frac1{48}.
$$

所以

$$
\boxed{\operatorname{Var}(Y)=\frac1{36}+\frac1{48}=\frac7{144}}.
$$

#### 进一步分析：为什么 $Y$ 不是 Unif$(0,1)$

虽然 $Y$ 的取值范围也在 $(0,1)$ 内，但较大的 $Y$ 可以出现在更多的条件区间中，混合后的密度不均匀。

由生成方式，

$$
f_{X,Y}(x,y)=f_X(x)f_{Y\mid X}(y\mid x)
=\frac1{1-x},\qquad0<x<y<1.
$$

故

$$
\boxed{f_Y(y)=\int_0^y\frac1{1-x}\,dx=-\log(1-y)},
\qquad0<y<1.
$$

密度在靠近 1 时较大，与 $E(Y)=3/4>1/2$ 一致。也可由条件二阶矩

$$
E(Y^2\mid X=x)=\frac{1+x+x^2}{3}
$$

得到 $E(Y^2)=11/18$，进而验证 $11/18-(3/4)^2=7/144$。

#### 等价表示：一种等价构造

取独立的 $X,U\sim\operatorname{Unif}(0,1)$，令

$$
Y=X+(1-X)U.
$$

给定 $X=x$ 后，$Y=x+(1-x)U$ 均匀落在 $(x,1)$，这与原模型完全一致。

注意它不同于“在三角形 $0<x<y<1$ 中按面积均匀抽点”；后者的联合密度是常数 2，而本模型联合密度为 $1/(1-x)$。

### 4.12 例题：随机患病率的分层二项模型

考虑一个随机环境下的计数模型：先随机选取一个地区，其患病率为

$$
Q\sim\operatorname{Unif}(0,1).
$$

给定 $Q=q$ 后，抽取 $n$ 个在此条件下相互独立的个体，令 $X$ 为患病人数：

$$
X\mid Q=q\sim\operatorname{Binomial}(n,q).
$$

#### 4.12.1 均值

条件均值为 $E(X\mid Q)=nQ$，由全期望，

$$
\boxed{E(X)=nE(Q)=\frac n2}.
$$

#### 4.12.2 方差

条件方差为

$$
\operatorname{Var}(X\mid Q)=nQ(1-Q).
$$

因为

$$
E(Q)=\frac12,\quad E(Q^2)=\frac13,\quad\operatorname{Var}(Q)=\frac1{12},
$$

所以

$$
\begin{aligned}
\operatorname{Var}(X)
&=E[nQ(1-Q)]+\operatorname{Var}(nQ)\\
&=n\left(\frac12-\frac13\right)+n^2\frac1{12}\\
&=\boxed{\frac{n(n+2)}{12}}.
\end{aligned}
$$

第一部分是同一地区内抽样带来的平均波动，第二部分是地区患病率不同造成的波动。

#### 4.12.3 边缘分布

对 $k=0,1,\ldots,n$，使用全概率公式：

$$
\begin{aligned}
P(X=k)
&=\int_0^1\binom nk q^k(1-q)^{n-k}\,dq\\
&=\binom nk B(k+1,n-k+1).
\end{aligned}
$$

其中 Beta 积分为

$$
B(a,b)=\int_0^1q^{a-1}(1-q)^{b-1}\,dq
=\frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}.
$$

对整数参数，

$$
B(k+1,n-k+1)=\frac{k!(n-k)!}{(n+1)!}.
$$

于是

$$
\boxed{P(X=k)=\frac1{n+1},\qquad k=0,\ldots,n}.
$$

因此 $X$ 在 $\{0,1,\ldots,n\}$ 上服从**离散均匀分布**。

若不熟悉 Beta 函数，可对 $\int_0^1q^k(1-q)^{n-k}\,dq$ 反复分部积分：每一步把 $q$ 的次数降低 1，最终得到相同的阶乘比值。

#### 4.12.4 关键辨析：为什么不能代入平均参数得到 Binomial$(n,1/2)$

虽然每个个体无条件患病概率都是 $E(Q)=1/2$，但他们共享同一个随机 $Q$，无条件下通常不独立。

令 $I_i$ 为第 $i$ 人是否患病的示性变量。对于 $i\ne j$，由条件独立，

$$
E(I_iI_j\mid Q)=Q^2.
$$

因此

$$
E(I_iI_j)=E(Q^2)=\frac13,
\qquad E(I_i)E(I_j)=\frac14,
$$

$$
\boxed{\operatorname{Cov}(I_i,I_j)=\frac1{12}>0}.
$$

各自方差为 $1/4$，所以两人的相关系数为 $1/3$。共同环境使他们在总体上正相关。

于是也可从协方差公式验证：

$$
\begin{aligned}
\operatorname{Var}\left(\sum_{i=1}^nI_i\right)
&=\frac n4+2\binom n2\frac1{12}\\
&=\frac{n(n+2)}{12}.
\end{aligned}
$$

与 Binomial$(n,1/2)$ 的方差 $n/4$ 相比，增加了 $n(n-1)/12$，在 $n>1$ 时严格更大。

**结论**：条件独立不等于无条件独立；“先随机选共同参数，再按这个参数抽样”与“每人使用一个独立随机参数”是不同模型。

## 5. 联合正态模型：连接分布、相关与条件信息

在掌握边缘分布、协方差和条件期望后，可以系统理解联合正态模型。本节先说明为什么需要联合模型，再介绍定义、构造、线性组合与条件分布，最后处理概率计算。

### 5.1 建模动机：两个边缘分布为什么不够

以两个测量指标为例，设

$$
X\sim N(120,15^2),\qquad Y\sim N(200,30^2).
$$

研究两个指标同时偏高的概率，以及线性组合

$$
R=X+0.5Y.
$$

仅凭两个边缘分布，可以算

$$
E(R)=120+0.5\times200=220,
$$

但不能确定联合超限概率，也不能确定 $\operatorname{Var}(R)$，因为还缺少依赖关系。

若进一步假设 $(X,Y)$ **联合正态**且 $\rho=0.6$，则

$$
\operatorname{Cov}(X,Y)=0.6\times15\times30=270.
$$

于是

$$
\begin{aligned}
\operatorname{Var}(R)
&=15^2+0.5^2\times30^2+2\times0.5\times270\\
&=225+225+270=720.
\end{aligned}
$$

由于联合正态变量的线性组合仍为正态，

$$
\boxed{R\sim N(220,720)}.
$$

这里 $720$ 是方差，标准差为 $\sqrt{720}\approx26.83$。

**严谨区分**：

- 边缘分布加协方差足以算线性组合的均值、方差。
- 要判定线性组合为正态，还需要联合正态等分布结构条件。
- 一般情况下，即使知道边缘分布和相关系数，也不能唯一确定联合分布。
- 在二维正态这一模型族内，均值、方差、相关系数才足以确定联合分布。

### 5.2 二维正态的定义与参数

称 $(X,Y)$ **联合正态**，若对任意实数 $a,b$，线性组合 $aX+bY$ 都服从正态分布，允许方差为零的退化情形。

其参数可写为均值向量和协方差矩阵：

$$
\boldsymbol\mu=
\begin{pmatrix}\mu_X\\\mu_Y\end{pmatrix},
\qquad
\Sigma=
\begin{pmatrix}
\sigma_X^2&\rho\sigma_X\sigma_Y\\
\rho\sigma_X\sigma_Y&\sigma_Y^2
\end{pmatrix}.
$$

若 $\sigma_X,\sigma_Y>0$ 且 $|\rho|<1$，则它有二维密度

$$
\boxed{
f_{X,Y}(x,y)=\frac{1}{2\pi\sigma_X\sigma_Y\sqrt{1-\rho^2}}
\exp\left\{-\frac{1}{2(1-\rho^2)}
\left[u^2-2\rho uv+v^2\right]\right\}
}
$$

其中

$$
u=\frac{x-\mu_X}{\sigma_X},\qquad v=\frac{y-\mu_Y}{\sigma_Y}.
$$

边缘分布分别为 $N(\mu_X,\sigma_X^2)$ 与 $N(\mu_Y,\sigma_Y^2)$。密度的等高线是椭圆；正相关时通常沿左下到右上的方向延伸，负相关时沿相反方向延伸。

**退化边界**：$|\rho|=1$ 时，概率集中在一条直线上，没有上述对二维面积的密度。此时应使用线性关系或退化高斯分布描述，不能将 $\rho=\pm1$ 直接代入密度公式。

### 5.3 构造、联合 MGF 与独立性

取独立的 $Z_1,Z_2\sim N(0,1)$，可以构造

$$
X=\mu_X+\sigma_XZ_1,
$$

$$
Y=\mu_Y+\sigma_Y\left(\rho Z_1+\sqrt{1-\rho^2}\,Z_2\right).
$$

这里 $|\rho|\le1$；当 $|\rho|=1$ 时第二个随机项消失。

构造直接表明：

$$
\operatorname{Var}(Y)=\sigma_Y^2[\rho^2+(1-\rho^2)]=\sigma_Y^2,
$$

$$
\operatorname{Cov}(X,Y)=\sigma_X\sigma_Y\rho.
$$

并且任意线性组合都是独立标准正态变量的线性组合，因而正态。

联合 MGF 为

$$
\boxed{M_{X,Y}(s,t)=E(e^{sX+tY})
=\exp\left[s\mu_X+t\mu_Y+\frac12
\left(s^2\sigma_X^2+2st\rho\sigma_X\sigma_Y+t^2\sigma_Y^2\right)\right]}.
$$

当 $\rho=0$ 时，

$$
M_{X,Y}(s,t)=M_X(s)M_Y(t).
$$

右侧是具有相同边缘分布的一对独立变量的联合 MGF。利用多元 MGF 唯一性，得到独立性。因此对于联合正态且方差为正的二元组，

$$
\boxed{X\perp Y\iff\operatorname{Cov}(X,Y)=0\iff\rho=0}.
$$

也可在非退化密度中令 $\rho=0$，直接验证 $f_{X,Y}(x,y)=f_X(x)f_Y(y)$。

#### 为什么“边缘都正态”仍不够：一个明确反例

令 $Z\sim N(0,1)$，$S$ 独立于 $Z$，且 $P(S=1)=P(S=-1)=1/2$。设

$$
X=Z,\qquad Y=SZ.
$$

由于正态分布对称，$X$、$Y$ 的边缘分布均为 $N(0,1)$。而且

$$
E(XY)=E(SZ^2)=E(S)E(Z^2)=0.
$$

二者不相关，但满足 $|X|=|Y|$ a.s.，显然存在依赖。更严格地，事件 $\{|X|\le1\}$ 和 $\{|Y|\le1\}$ 相同，概率在 0 与 1 之间，因此不独立。

它们也不联合正态：$X+Y$ 以概率 $1/2$ 恰好为零，另有一个非退化连续部分，不是任何正态分布。

### 5.4 联合正态下的线性组合

若 $(X,Y)$ 联合正态，则

$$
\boxed{
aX+bY+c\sim N\left(
a\mu_X+b\mu_Y+c,
a^2\sigma_X^2+b^2\sigma_Y^2+2ab\rho\sigma_X\sigma_Y
\right)
}.
$$

与独立正态的结论相比，增加了协方差项；只有当 $\rho=0$ 时该项消失。

由联合 MGF 也可直接证明：

$$
M_{aX+bY+c}(t)=e^{ct}M_{X,Y}(at,bt).
$$

### 5.5 二维正态的条件分布

在 $\sigma_X,\sigma_Y>0$、$|\rho|<1$ 时，

$$
\boxed{
Y\mid X=x\sim N\left(
\mu_Y+\rho\frac{\sigma_Y}{\sigma_X}(x-\mu_X),
\sigma_Y^2(1-\rho^2)
\right)
}.
$$

可用前面给出的独立标准正态构造理解：知道 $X=x$，等于知道 $Z_1=(x-\mu_X)/\sigma_X$，剩余随机性仅来自独立的 $Z_2$。

因此

$$
\boxed{E(Y\mid X)
=\mu_Y+\rho\frac{\sigma_Y}{\sigma_X}(X-\mu_X)},
$$

$$
\boxed{\operatorname{Var}(Y\mid X)=\sigma_Y^2(1-\rho^2)}.
$$

这说明联合正态模型中：

1. 条件均值恰好是 $X$ 的仿射函数。
2. 条件方差不随观察到的 $x$ 改变。
3. 最佳线性预测等于所有平方损失预测中的最佳预测。

对于本节开头的两个测量指标，代入模型参数得

$$
E(Y\mid X)=200+1.2(X-120),
$$

$$
\operatorname{Var}(Y\mid X)=30^2(1-0.6^2)=576.
$$

条件分布中的均值随观察值改变，而条件方差保持不变；这是该联合正态模型的结构性质。

### 5.6 怎样计算两个指标同时偏高

联合超限概率取决于两个阈值与联合分布。若阈值为 $u,v$，则

$$
P(X>u,Y>v)
=\int_u^\infty P(Y>v\mid X=x)f_X(x)\,dx.
$$

在非退化二维正态模型下，令

$$
m(x)=\mu_Y+\rho\frac{\sigma_Y}{\sigma_X}(x-\mu_X),
\qquad s=\sigma_Y\sqrt{1-\rho^2},
$$

则

$$
\boxed{P(X>u,Y>v)=\int_u^\infty
\left[1-\Phi\left(\frac{v-m(x)}s\right)\right]f_X(x)\,dx}.
$$

一般不能写成两个边缘尾概率的乘积；只有独立时才能这样处理。

### 5.7 应用：正态模型下的质量控制

某灌装机装液体积为

$$
X\sim N(500,10^2),
$$

单位为 mL。因此均值为 $500$ mL，标准差为 $10$ mL，而非 $100$ mL。

#### 问题一：低于 485 mL 的概率

标准化：

$$
Z=\frac{X-500}{10}\sim N(0,1).
$$

所以

$$
\boxed{P(X<485)=\Phi(-1.5)\approx0.0668}.
$$

#### 问题二：落在规格区间内的比例

$$
\begin{aligned}
P(485\le X\le515)
&=P(-1.5\le Z\le1.5)\\
&=\Phi(1.5)-\Phi(-1.5)\\
&\approx\boxed{0.8664}.
\end{aligned}
$$

正态变量为连续型，端点是否包含不影响概率。

#### 问题三：仅 5% 的瓶子会超过的容量

令 $P(X>c)=0.05$，等价于 $P(X\le c)=0.95$。

$$
\frac{c-500}{10}=\Phi^{-1}(0.95)\approx1.645.
$$

因此

$$
\boxed{c\approx500+10(1.645)=516.45\text{ mL}}.
$$

**易错点**：上尾 5% 对应左侧累计概率 95% 的分位数，不是 $\Phi^{-1}(0.05)$。

## 6. 最优预测：从常数到线性函数再到条件期望

预测的目标不仅是给出一个数，还要明确“最佳”的评价标准。本节统一使用平方损失，并逐步扩大允许的预测函数范围：常数、仿射函数、任意由已知变量决定的函数。

### 6.1 只用常数预测：总体均值最优

设 $E(Y^2)<\infty$，希望选择常数 $a$，使 $E[(Y-a)^2]$ 最小。分解

$$
Y-a=(Y-E(Y))+(E(Y)-a),
$$

平方并取期望，利用 $E[Y-E(Y)]=0$，得到

$$
\boxed{E[(Y-a)^2]=\operatorname{Var}(Y)+[E(Y)-a]^2}.
$$

因此最优常数为 $a^*=E(Y)$，最小误差为 $\operatorname{Var}(Y)$。这是没有利用额外信息时的预测基准。

如果现在能观察到另一个变量 $X$，就可以让预测值随 $X$ 改变。问题转变为：只允许线性变化时怎样最优；允许任意函数时又怎样最优？

### 6.2 最佳线性预测

设 $X,Y$ 二阶矩有限且 $\operatorname{Var}(X)>0$。希望用

$$
\widehat Y=a+bX
$$

预测 $Y$，使均方误差

$$
\operatorname{MSE}(a,b)=E[(Y-a-bX)^2]
$$

最小。

#### 6.2.1 完整推导

中心化后展开：

$$
\begin{aligned}
E[(Y-a-bX)^2]
&=(\mu_Y-a-b\mu_X)^2\\
&\quad+\sigma_Y^2+b^2\sigma_X^2-2b\operatorname{Cov}(X,Y).
\end{aligned}
$$

固定 $b$ 时，第一项在

$$
a=\mu_Y-b\mu_X
$$

处达到最小值零。再对 $b$ 配方：

$$
\begin{aligned}
\sigma_Y^2+b^2\sigma_X^2-2b\operatorname{Cov}(X,Y)
&=\sigma_X^2\left(b-\frac{\operatorname{Cov}(X,Y)}{\sigma_X^2}\right)^2\\
&\quad+\sigma_Y^2-\frac{\operatorname{Cov}(X,Y)^2}{\sigma_X^2}.
\end{aligned}
$$

所以

$$
b^*=\frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(X)},
\qquad
a^*=\mu_Y-b^*\mu_X.
$$

最终得到

$$
\boxed{\widehat Y
=\mu_Y+\frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(X)}(X-\mu_X)}.
$$

若 $\sigma_Y>0$，还可写为

$$
\boxed{\widehat Y-\mu_Y=\rho\frac{\sigma_Y}{\sigma_X}(X-\mu_X)},
$$

$$
\boxed{\operatorname{MSE}_{\min}=\sigma_Y^2(1-\rho^2)}.
$$

如果 $Y$ 为常数，前面的协方差形式仍适用，最小误差为零，但不能使用未定义的 $\rho$。

#### 6.2.2 怎样理解这条直线

1. 直线经过总体均值点 $(\mu_X,\mu_Y)$。
2. 斜率取决于相关系数，还取决于两个变量的尺度比。
3. $\rho=0$ 时，最佳线性预测是常数 $\mu_Y$；这不表示 $X$ 无法提供非线性预测信息。
4. $|\rho|=1$ 时，最小误差为零。
5. 最小化的是 **$Y$ 方向的残差平方**，不是点到直线的垂直距离平方。

进一步理解：残差 $R=Y-\widehat Y$ 满足

$$
E(R)=0,\qquad \operatorname{Cov}(R,X)=0.
$$

这叫正交性；它通常不意味着残差与 $X$ 独立。

### 6.3 例题：相关性与预测

联合分布为

| $X\backslash Y$ | $Y=0$ | $Y=1$ |
|---|---|---|
| $X=0$ | $0.4$ | $0.1$ |
| $X=1$ | $0.1$ | $0.4$ |

两者的边缘分布均为 Bernoulli$(1/2)$，所以

$$
E(X)=E(Y)=\frac12,\qquad
\operatorname{Var}(X)=\operatorname{Var}(Y)=\frac14.
$$

仅当 $X=Y=1$ 时 $XY=1$，故

$$
E(XY)=0.4,\qquad
\operatorname{Cov}(X,Y)=0.4-0.25=0.15.
$$

$$
\rho=\frac{0.15}{\sqrt{(1/4)(1/4)}}=0.6.
$$

最佳线性预测为

$$
\boxed{\widehat Y=0.5+0.6(X-0.5)=0.2+0.6X},
$$

最小均方误差为

$$
\boxed{\operatorname{MSE}_{\min}=0.25(1-0.6^2)=0.16}.
$$

与条件期望的联系：$P(Y=1\mid X=0)=0.2$、$P(Y=1\mid X=1)=0.8$，所以此例中 $E(Y\mid X)=0.2+0.6X$，恰好等于最佳线性预测。本节后面的最优性定理将说明原因。

### 6.4 条件期望是最优平方损失预测

在常数与线性预测的基础上，进一步允许任意函数形式，可以得到统一的最优性结论。

设 $E(Y^2)<\infty$，令 $m(X)=E(Y\mid X)$。对任意满足二阶可积条件的预测函数 $g(X)$，

$$
\boxed{
E[(Y-g(X))^2]
=E[\operatorname{Var}(Y\mid X)]
+E[(m(X)-g(X))^2]
}.
$$

证明：写成

$$
Y-g(X)=[Y-m(X)]+[m(X)-g(X)],
$$

展开平方；交叉项通过条件期望等于零。第一项为平均条件方差，第二项非负。

因此最优预测为

$$
\boxed{g^*(X)=E(Y\mid X)},
\qquad
\boxed{\operatorname{MSE}_{\min,\text{任意函数}}
=E[\operatorname{Var}(Y\mid X)]}.
$$

| 最优化范围 | 最优解 | 最小误差 |
|---|---|---|
| 所有常数预测 | $E(Y)$ | $\operatorname{Var}(Y)$ |
| 所有仿射预测 $a+bX$ | 最佳线性预测 | $\sigma_Y^2(1-\rho^2)$，方差均为正时 |
| 所有由 $X$ 决定的平方可积预测 | $E(Y\mid X)$ | $E[\operatorname{Var}(Y\mid X)]$ |

允许使用的预测函数越丰富，最小误差不会增大。因此，在相关系数存在时，

$$
E[\operatorname{Var}(Y\mid X)]
\le\sigma_Y^2(1-\rho^2)
\le\sigma_Y^2.
$$

两种预测何时一致？当 $E(Y\mid X)$ 恰好是 $X$ 的仿射函数时，例如联合正态模型；当 $X$ 只有两个不同可能取值时，任何 $X$ 的函数在其支持集上也能用仿射函数表达。

**非线性反例的预测含义**：若 $X\sim\operatorname{Unif}(-1,1)$、$Y=X^2$，则最佳线性预测为常数 $E(Y)=1/3$，误差为

$$
\operatorname{Var}(Y)=\frac15-\frac19=\frac4{45}.
$$

但条件期望为 $E(Y\mid X)=X^2$，可以精确预测，误差为零。

### 6.5 一条统一的理解：信息、函数范围与误差

三种预测都是在寻找对 $Y$ 最合适的近似，区别在于允许使用的函数范围。

1. **不使用 $X$**：只能选常数，答案是总体均值。
2. **只用 $X$ 的线性信息**：只能选 $a+bX$，答案由协方差与方差决定。
3. **使用 $X$ 的全部信息**：可以选任意合适的 $g(X)$，答案是条件期望。

当条件均值非线性时，最佳线性预测可能遗漏重要信息；当条件均值恰为仿射函数时，线性预测已经达到全部函数中的最优。这也是联合正态模型特别便利的原因。

全方差公式在此具有预测解释：

$$
\underbrace{\operatorname{Var}(Y)}_{\text{只用常数时的误差}}
=\underbrace{E[\operatorname{Var}(Y\mid X)]}_{\text{使用全部 }X\text{ 信息后的最小误差}}
+\underbrace{\operatorname{Var}(E(Y\mid X))}_{\text{利用 }X\text{ 可以减少的误差}}.
$$

这种解释针对平方损失；不能直接推广为其他损失函数下的最优结论。

## 7. 解题方法与易错点

### 7.1 题型一：求期望、方差

建议顺序：

1. 明确支持集、分布参数及参数约定。
2. 检查相关矩是否存在，尤其注意重尾分布。
3. 优先使用结构：线性分解、示性变量、已知分布公式或条件期望。
4. 若无现成结构，计算 $E(X)$ 与 $E(X^2)$。
5. 用 $\operatorname{Var}(X)=E(X^2)-[E(X)]^2$。
6. 核查结果是否非负、单位是否正确、极端参数是否合理。

例如算几何分布二阶矩时，先算 $E[X(X-1)]$ 往往比直接算 $E(X^2)$ 更容易；算二项分布均值时，分解为示性变量比展开求和更简洁。

### 7.2 题型二：用 MGF 求分布

写完整的论证链：

$$
\text{定义目标变量}
\to\text{利用独立性或变换公式}
\to\text{求 MGF 及有效范围}
\to\text{匹配已知 MGF}
\to\text{唯一性得分布}.
$$

检查四件事：

- 拆乘积时是否真的独立？
- 缩放 $aX$ 时，是否写成 $M_X(at)$？
- 平移 $X+b$ 时，是否乘上 $e^{bt}$？
- 所得函数是否在零点开邻域有限，且 $M(0)=1$？

若只是需要均值和方差，不一定值得先求 MGF；根据题目结构选择计算量较小的方法。

### 7.3 题型三：由联合表求相关系数

建议按下面的顺序，避免中途反复计算：

$$
\text{联合概率表}
\to p_X,p_Y
\to E(X),E(Y),E(X^2),E(Y^2)
\to E(XY)
\to\operatorname{Cov}(X,Y)
\to\rho.
$$

核对：

- 联合表总和为 1，所有概率非负。
- 行、列和分别给出正确边缘分布。
- 求 $E(XY)$ 时遍历联合格子，不能只看两个边缘均值。
- 两个方差严格为正时才算通常的相关系数。
- 最后 $|\rho|\le1$；若超出这个范围，必有计算或模型错误。

### 7.4 题型四：判断独立或不相关

**证明独立**：验证整个联合分布可分解，或使用适用的结构定理。

$$
p_{X,Y}(x,y)=p_X(x)p_Y(y)
$$

在所有支持点成立；有密度时要求相应密度分解几乎处处成立。

**否定独立**：只需找出一个反例事件或一个支持点，使联合概率不等于乘积。

**判断不相关**：在二阶矩有限时计算 $E(XY)-E(X)E(Y)$。

一般不能以“协方差等于零”完成独立性证明；如果使用正态例外，必须明确写出联合正态条件。

### 7.5 题型五：求线性组合的分布或波动

设 $L=\sum_i a_iX_i+b$，先计算

$$
E(L)=\sum_i a_iE(X_i)+b,
$$

再使用包含协方差项的一般方差公式。只有确认不相关后，才能去掉交叉项。

最后才判断分布形状：

- 独立正态或联合正态：$L$ 为正态。
- 其他分布：仅凭均值、方差通常不能确定 $L$ 的分布。
- 方差为零：$L$ 为几乎必然常数。

### 7.6 题型六：分层随机模型

模型通常写成“先抽参数 $Q$，再给定 $Q$ 抽结果 $X$”。优先计算

$$
m(Q)=E(X\mid Q),\qquad v(Q)=\operatorname{Var}(X\mid Q).
$$

然后

$$
E(X)=E[m(Q)],
$$

$$
\operatorname{Var}(X)=E[v(Q)]+\operatorname{Var}[m(Q)].
$$

如果还要求边缘分布，再做混合：

$$
p_X(k)=\int p_{X\mid Q}(k\mid q)f_Q(q)\,dq
$$

或相应求和。不能普遍用“把随机参数替换成其平均值”的方式求边缘分布。

### 7.7 题型七：预测

先识别题目限定的预测范围：

- 只允许常数：使用 $E(Y)$。
- 只允许 $a+bX$：使用最佳线性预测。
- 允许任意 $g(X)$，目标为平方损失：使用 $E(Y\mid X)$。

“最佳”必须依赖损失函数与允许的预测函数范围。本章的最佳性均针对均方误差；若损失改为绝对误差等，答案一般会改变。

### 7.8 重点易错点汇总

| 容易出错的说法 | 严谨表述 |
|---|---|
| 期望就是最可能出现的值 | 期望是概率加权平均，不一定是众数，也不一定能取到 |
| 分布对称，所以均值一定为 0 | 先确认均值存在；对称中心为 0 且可积才可如此判断 |
| $E[g(X)]=g(E(X))$ | 一般不成立；仿射函数是重要特例 |
| 期望相加需要独立 | 不需要，相关可积性足够 |
| 乘积期望总能拆开 | 一般不能，独立是常用充分条件 |
| $E(XY)=E(X)E(Y)$ 推出独立 | 不能，只能在二阶矩条件下推出不相关 |
| $\operatorname{Var}(aX+b)=a\operatorname{Var}(X)$ | 系数应为 $a^2$ |
| $\operatorname{sd}(aX+b)=a\operatorname{sd}(X)$ | 系数应为 $\lvert a\rvert$ |
| $\operatorname{Var}(X-Y)=\operatorname{Var}(X)-\operatorname{Var}(Y)$ | 应为两方差相加再减去两倍协方差 |
| $M_X''(0)$ 就是方差 | 它是 $E(X^2)$，还需减 $[E(X)]^2$ |
| $M_X(0)=1$ 就说明 MGF 存在 | 必须在零点某双侧开邻域有限 |
| 有全部矩就必有 MGF | 不成立，对数正态是反例 |
| 前两阶矩相同就同分布 | 不成立；MGF 唯一性要求函数在邻域上相同 |
| 几何分布总从 0 开始 | 本文从 1 开始，两种定义的均值不同 |
| Gamma 的第二参数总是尺度 | 本文用率；先检查约定 |
| 指数变量相加仍为指数 | 同率独立和为 Gamma；独立最小值才是率相加的指数 |
| 二项变量相加总为二项 | 除独立外，还要求成功概率相同 |
| $\rho=0$ 表示没有任何依赖 | 只排除线性协方差，不排除非线性依赖 |
| $\lvert\rho\rvert=1$ 表示任意确定函数关系 | 必须是非零斜率的仿射关系，几乎必然成立 |
| 方差为零的变量与其他变量相关系数为 0 | 普通相关系数未定义 |
| 两个变量分别正态，就联合正态 | 不成立 |
| 两个正态边缘不相关，就独立 | 必须补上联合正态条件 |
| $E(Y\mid X)$ 是常数 | 通常是 $X$ 的函数，是随机变量 |
| 连续条件密度是 $P(X=x)$ 的比值 | 使用联合密度与边缘密度的比，而非零概率相除 |
| 条件方差围绕总体均值计算 | 应围绕条件均值 $E(Y\mid X)$ 计算 |
| 总方差只有平均条件方差 | 还要加条件均值的方差 |
| 知道条件后，每个组的方差都更小 | 只保证平均条件方差不超过总方差 |
| 条件独立意味着总体独立 | 不成立，共同随机参数可诱导总体依赖 |
| 最佳线性预测永远等于条件期望 | 只有条件均值在支持集上为仿射函数时成立 |

## 8. 核心公式速查

> 本节用于复习，不能代替前文的条件说明。方差、协方差运算默认二阶矩有限；相关系数要求双方方差为正；MGF 结论要求零点邻域有限。

### 8.1 期望与方差

$$
E(aX+bY+c)=aE(X)+bE(Y)+c.
$$

$$
E(XY)=E(X)E(Y)\quad\text{若独立且可积}.
$$

$$
E(\mathbf1_A)=P(A).
$$

$$
\operatorname{Var}(X)=E(X^2)-[E(X)]^2.
$$

$$
\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X).
$$

$$
\operatorname{Var}\left(\sum_i a_iX_i\right)
=\sum_i a_i^2\operatorname{Var}(X_i)
+2\sum_{i<j}a_ia_j\operatorname{Cov}(X_i,X_j).
$$

### 8.2 MGF

$$
M_X(t)=E(e^{tX}),\qquad M_X^{(r)}(0)=E(X^r).
$$

$$
E(X)=M_X'(0),\qquad
\operatorname{Var}(X)=M_X''(0)-[M_X'(0)]^2.
$$

$$
M_{aX+b}(t)=e^{bt}M_X(at).
$$

$$
M_{b+\sum_ka_kX_k}(t)=e^{bt}\prod_kM_{X_k}(a_kt)
\quad\text{若相互独立}.
$$

### 8.3 协方差、相关与线性预测

$$
\operatorname{Cov}(X,Y)=E(XY)-E(X)E(Y).
$$

$$
\rho=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y},\qquad -1\le\rho\le1.
$$

$$
\operatorname{Cov}(aX+b,cY+d)=ac\operatorname{Cov}(X,Y).
$$

$$
\widehat Y=\mu_Y+\frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(X)}(X-\mu_X).
$$

$$
\operatorname{MSE}_{\min,\text{线性}}=\sigma_Y^2(1-\rho^2).
$$

### 8.4 条件公式

$$
E[h(X)Y\mid X]=h(X)E(Y\mid X).
$$

$$
E[E(Y\mid X)]=E(Y).
$$

$$
\operatorname{Var}(Y\mid X)=E(Y^2\mid X)-[E(Y\mid X)]^2.
$$

$$
\operatorname{Var}(Y)=E[\operatorname{Var}(Y\mid X)]+\operatorname{Var}(E(Y\mid X)).
$$

$$
\widehat Y_{\text{任意函数最优}}=E(Y\mid X),\qquad
\operatorname{MSE}_{\min}=E[\operatorname{Var}(Y\mid X)].
$$

### 8.5 分布关系

$$
X\sim N(\mu,\sigma^2),\ \sigma>0
\quad\Longrightarrow\quad\frac{X-\mu}{\sigma}\sim N(0,1).
$$

$$
Z_i\overset{\mathrm{iid}}\sim N(0,1)
\quad\Longrightarrow\quad\sum_{i=1}^nZ_i^2\sim\chi^2(n).
$$

$$
\chi^2(\nu)=\operatorname{Gamma}(\nu/2,1/2)
\quad\text{（形状、率参数）}.
$$

$$
X_i\overset{\mathrm{iid}}\sim\operatorname{Exp}(\lambda)
\quad\Longrightarrow\quad\sum_{i=1}^nX_i\sim\operatorname{Gamma}(n,\lambda).
$$

$$
X_i\sim\operatorname{Exp}(\lambda_i)\text{ 相互独立}
\quad\Longrightarrow\quad\min_iX_i\sim\operatorname{Exp}\left(\sum_i\lambda_i\right).
$$

## 9. 自测题与参考解答

> 建议先遮住解答独立完成。除了算出结果，还应说明每一步使用的条件。

### 题 1：标准化是否必然得到正态

设 $X\sim\operatorname{Unif}(0,1)$，令 $Z=(X-1/2)/\sqrt{1/12}$。是否有 $Z\sim N(0,1)$？

**解答**：没有。$E(Z)=0$、$\operatorname{Var}(Z)=1$，但

$$
Z\sim\operatorname{Unif}(-\sqrt3,\sqrt3).
$$

均值为 0、方差为 1 只是数字特征，不能确定分布为标准正态。

### 题 2：MGF 的仿射变换

设 $X\sim\operatorname{Exp}(2)$，$Y=3X-1$，求 $M_Y(t)$、$E(Y)$、$\operatorname{Var}(Y)$。

**解答**：

$$
M_Y(t)=e^{-t}M_X(3t)=e^{-t}\frac2{2-3t},\qquad t<\frac23.
$$

$$
E(Y)=3\cdot\frac12-1=\frac12,
\qquad\operatorname{Var}(Y)=9\cdot\frac14=\frac94.
$$

检查：平移不影响方差，缩放系数需平方。

### 题 3：同率指数变量的和与最小值

设 $X_1,X_2$ 独立且均服从 Exp$(3)$，求 $S=X_1+X_2$ 与 $W=\min(X_1,X_2)$ 的分布和均值。

**解答**：

$$
S\sim\operatorname{Gamma}(2,3),\qquad E(S)=\frac23.
$$

$$
W\sim\operatorname{Exp}(6),\qquad E(W)=\frac16.
$$

和与最小值采用不同分布规则。

### 题 4：含相关性的线性组合

设 $\operatorname{Var}(X)=4$、$\operatorname{Var}(Y)=9$、$\rho_{X,Y}=1/2$，求 $\operatorname{Var}(2X-Y)$。

**解答**：先算

$$
\operatorname{Cov}(X,Y)=\frac12\times2\times3=3.
$$

然后

$$
\operatorname{Var}(2X-Y)=4\times4+9-4\times3=\boxed{13}.
$$

这里不需要正态假设；若还要求 $2X-Y$ 的具体分布，则现有信息不够。

### 题 5：两个无关的平均数是否决定独立性

已知 $E(X)=E(Y)=0$ 且 $E(XY)=0$，能否推出 $X,Y$ 独立？

**解答**：不能。令 $X\sim\operatorname{Unif}(-1,1)$，$Y=X^2-1/3$，则

$$
E(Y)=0,\qquad E(XY)=E(X^3)-\frac13E(X)=0,
$$

但 $Y$ 为 $X$ 的非恒定确定函数。知道 $X$ 可以确定 $Y$，二者不独立。

### 题 6：随机参数二项分布的一般方差

设 $0\le Q\le1$，$E(Q)=m$、$\operatorname{Var}(Q)=v$，且 $X\mid Q\sim\operatorname{Binomial}(n,Q)$。求 $E(X)$ 与 $\operatorname{Var}(X)$。

**解答**：

$$
E(X)=nm.
$$

由于 $E(Q^2)=m^2+v$，

$$
\begin{aligned}
\operatorname{Var}(X)
&=nE[Q(1-Q)]+n^2v\\
&=n[m-m^2-v]+n^2v\\
&=\boxed{nm(1-m)+n(n-1)v}.
\end{aligned}
$$

随机参数的变异在 $n>1$ 时增加总体方差。若 $v=0$，参数几乎必然固定，就退回普通二项模型。

### 题 7：条件均值与最佳线性预测

设 $X$ 等概率取 $-1,0,1$，$Y=X^2$。求 $E(Y\mid X)$、最佳线性预测及两者的最小均方误差。

**解答**：

$$
E(Y\mid X)=X^2,
$$

故任意函数预测的最小误差为零。另一方面，

$$
E(X)=0,\quad E(Y)=\frac23,\quad E(XY)=E(X^3)=0.
$$

所以协方差为零，最佳线性预测为常数 $2/3$。又因 $Y^2=Y$，

$$
\operatorname{MSE}_{\min,\text{线性}}
=\operatorname{Var}(Y)=\frac23-\frac49=\boxed{\frac29}.
$$

### 题 8：二维正态的条件分布与全方差

设 $(X,Y)$ 联合正态，参数为 $\mu_X=1$、$\mu_Y=2$、$\sigma_X=2$、$\sigma_Y=3$、$\rho=1/2$。求 $Y\mid X=x$ 的分布，并验证全方差公式。

**解答**：

$$
Y\mid X=x\sim N\left(2+\frac34(x-1),\frac{27}{4}\right).
$$

因此

$$
E[\operatorname{Var}(Y\mid X)]=\frac{27}{4},
$$

$$
\operatorname{Var}(E(Y\mid X))
=\left(\frac34\right)^2\operatorname{Var}(X)=\frac94.
$$

两者相加为 $9=\operatorname{Var}(Y)$。

## 10. 掌握程度检查

完成本章后，应能不依赖公式表解释和推导以下结论。

- [ ] 解释绝对可积的意义，说明对称分布为什么可能没有均值。
- [ ] 熟练使用函数期望与示性变量，不为求期望而不必要地求新分布。
- [ ] 推导方差计算公式、仿射变换公式和一般线性组合方差公式。
- [ ] 区分几何分布的两种支持集与 Gamma 的率、尺度参数。
- [ ] 从定义推导 Poisson、指数、正态和二项分布的 MGF。
- [ ] 说明 MGF 的存在范围、生成矩条件及唯一性应用的完整逻辑。
- [ ] 证明独立变量的分布可加性，并识别需要同参数的情况。
- [ ] 区分指数变量求和与取最小值，选择合适方法。
- [ ] 从联合概率表计算边缘矩、交叉矩、协方差及相关系数。
- [ ] 证明相关系数界，解释等号成立与线性关系。
- [ ] 推导最佳线性预测及最小均方误差。
- [ ] 给出至少一个“不相关但依赖”的反例。
- [ ] 区分边缘正态与联合正态，解释正态独立性判据的前提。
- [ ] 清楚区分 $E(Y)$、$E(Y\mid X=x)$、$E(Y\mid X)$。
- [ ] 用全期望和全方差处理两阶段或随机参数模型。
- [ ] 解释分层模型中的条件独立为什么不推出总体独立。
- [ ] 说明条件期望与最佳线性预测各自在什么范围内最优。
