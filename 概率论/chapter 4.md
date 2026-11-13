# 第四章　随机变量的数字特征：教材式复习讲义

> 依据 chapter 4.pdf 的全部 120 个 PDF 页面整理。正文按知识依赖关系展开：期望 → 方差 → 矩与矩母函数 → 协方差与相关 → 线性预测 → 二元正态 → 条件期望与全方差。课件中的习题、例题和应用均给出推导；额外解释与练习标为“补充”。本文页码均为 PDF 的物理页码，原课件页脚的总页数“123”与文件实际页数不一致。
>
> 原课件：[chapter 4.pdf](<C:/Users/yang/Desktop/大四/概率论/chapter 4.pdf>)。离散 PMF 记为 $p$，连续 PDF 记为 $f$；$N(\mu,\sigma^2)$ 的第二个参数是方差。几何分布取值为 $1,2,\ldots$；Gamma 与指数分布一律使用**速率参数** $\lambda$。

## 导论　本章怎样承接前面三章

前三章研究“概率规律的完整描述”：事件概率、一元分布、联合分布。本章进一步问：如果不想每次携带整个分布，能否用几个数概括它的重要性质？

期望描述平均位置，方差描述离散程度，协方差与相关系数描述两个变量的线性共同变化。矩母函数把一系列矩编码到一个函数里，既能求矩，也能识别分布。条件期望则把“一个总体平均值”扩展为“根据已知信息变化的平均值”。

需要始终记住：**少量数字特征通常不能决定整个分布。** 两个变量均值、方差相同，不代表同分布；两个边缘都正态且相关系数给定，也不代表已经确定联合分布，除非额外假设联合正态。

本章可以沿着五个问题复习：

1. **平均在什么位置？** ——期望及其线性性质。
2. **围绕平均值波动多大？** ——方差、标准差、矩。
3. **组合后是什么分布？** ——矩母函数与独立和。
4. **两个变量怎样共同变化？** ——协方差、相关、二元正态。
5. **掌握信息后怎样预测？** ——条件期望、全期望、全方差。

### 课件与本文对应关系

| PDF 页码 | 课件内容 | 本文位置 |
|---|---|---|
| 4、6—10 | 可积性、期望、函数期望、指示变量、期望性质 | 第一、二节 |
| 11—19 | 方差及常见分布的均值方差，习题 4.1 | 第三、四节 |
| 21—24、30—34 | 矩母函数、矩、唯一性、独立和及仿射变换 | 第五节 |
| 25—29、35—44 | Poisson、指数、正态的 MGF；习题 4.4—4.6；正态组合、标准化、平方 | 第六、七节 |
| 45—49 | 可加性、指数和与最小值 | 第七节 |
| 51—57、62—70 | 协方差、相关、例 4.8、例 4.10、不相关反例、双线性、和的方差 | 第八至十节 |
| 58—61 | 最佳线性预测与离散表格例题 | 第十一节 |
| 71—74 | 灌装质量控制、两项健康测量的建模 | 第十二节 |
| 76—85 | 二元正态的构造、密度、边缘与联合 MGF | 第十三节 |
| 86—97 | 正态线性组合、独立性、反例、条件分布及计算 | 第十四、十五节 |
| 99—108 | 机器次品率、条件期望、全期望及离散例题 | 第十六、十七节 |
| 109—114 | 条件方差、全方差、两阶段均匀模型 | 第十八节 |
| 115—117 | 分层患病率模型 | 第十九节 |
| 118—119 | 总结公式及 Gaussian 结论 | 第二十节及附录 |

---

## 第一节　数学期望：按概率加权的平均

### 1.1 定义与直觉

若 $X$ 为离散变量，取值为 $x$ 的概率是 $p_X(x)$，定义

$$\boxed{E(X)=\sum_x x\,p_X(x).}$$

若 $X$ 有密度 $f_X$，则

$$\boxed{E(X)=\int_{-\infty}^{\infty}x f_X(x)\,dx.}$$

离散情形的“取值乘权重再相加”，在连续情形变成积分。权重由分布决定，不是把所有可能取值等权平均。例如 $P(X=0)=0.9,P(X=10)=0.1$，则 $E(X)=1$，不是 5。

期望也不必是可能取到的值。公平骰子的期望为 $3.5$，而骰子不会掷出 $3.5$。在适当的重复试验条件下，样本平均值会趋近总体期望；这一长期解释依赖后续的大数定律，不能当作期望的定义。

### 1.2 先判断有限期望是否存在

本章的普通有限期望以**绝对可积**为前提：

$$\boxed{E|X|<\infty.}$$

对应地，离散情形要求 $\sum_x|x|p_X(x)<\infty$，连续情形要求 $\int|x|f_X(x)dx<\infty$。

令 $X^+=\max(X,0),X^-=\max(-X,0)$，则

$$X=X^+-X^-,\qquad |X|=X^++X^-.$$

若两部分的期望都有限，$E(X)=E(X^+)-E(X^-)$ 是有限数；若一边无限、另一边有限，可以谈 $+\infty$ 或 $-\infty$ 的扩展期望；若两边都无限，就出现没有定义的“$\infty-\infty$”。本章的线性、协方差等常规运算应在相应有限性条件下使用。

**补充反例：对称不保证期望为 0。** 标准柯西密度为

$$f(x)=\frac1{\pi(1+x^2)},\qquad x\in\mathbb R.$$

虽然关于 0 对称，但

$$\int_0^A\frac{x}{\pi(1+x^2)}dx=\frac1{2\pi}\log(1+A^2)\longrightarrow\infty.$$

负半轴也有无限的绝对贡献，因此 $E(X)$ 不存在。对称截断 $\lim_{A\to\infty}\int_{-A}^Axf(x)dx=0$ 是主值，不是期望。**先验证可积，再使用对称性。**

### 1.3 函数的期望：不必先求新变量的分布

课件定理 4.1：若 $g$ 可测且 $E|g(X)|<\infty$，则

$$\boxed{E[g(X)]=\sum_xg(x)p_X(x)}$$

或

$$\boxed{E[g(X)]=\int_{-\infty}^{\infty}g(x)f_X(x)dx.}$$

例如求 $E(X^2)$，直接把公式中的 $x$ 换成 $x^2$；求 $E(e^{tX})$，直接积分 $e^{tx}f_X(x)$。这条公式常称 LOTUS：知道输入变量分布，就能求输出函数的平均。

为什么成立？离散时，同一输出值 $z$ 的概率应把所有满足 $g(x)=z$ 的输入概率加起来，再把求和重新归类：

$$\sum_z zP(g(X)=z)
=\sum_z\sum_{x:g(x)=z}g(x)p_X(x)
=\sum_xg(x)p_X(x).$$

连续情形可由指示函数、简单函数逐步推广得到；它不要求 $g$ 单调或一一对应。

**补充例：** $X\sim U(-1,1)$ 时，

$$E(X^2)=\int_{-1}^1x^2\frac12dx=\frac13.$$

无需先用第三章的方法求 $X^2$ 的密度。但如果题目要求 $X^2$ 的完整分布，仍需做分布变换。注意 $E[g(X)]$ 一般不等于 $g(E(X))$，这里 $E(X^2)=1/3$，而 $[E(X)]^2=0$。

### 1.4 二元函数的期望

课件第 51 页将同一原理推广为

$$E[g(X,Y)]=\sum_x\sum_y g(x,y)p_{X,Y}(x,y),$$

或

$$E[g(X,Y)]=\iint_Dg(x,y)f_{X,Y}(x,y)\,dx\,dy.$$

仍要先写支持集 $D$，并要求相应绝对期望有限。特别地，$E(XY)$ 用联合分布计算，通常不能只靠两个边缘计算。

---

## 第二节　期望的性质与指示变量

### 2.1 概率也是一种期望

对事件 $A$ 定义指示变量

$$I_A=\begin{cases}1,&A\text{ 发生},\\0,&A\text{ 不发生}.\end{cases}$$

于是课件推论 4.2 给出

$$\boxed{E(I_A)=1\cdot P(A)+0\cdot P(A^c)=P(A).}$$

写成 $1_B(X)$ 时，它指事件 $\{X\in B\}$ 的指示变量，因此 $E[1_B(X)]=P(X\in B)$。

这条公式把计数题变成期望题：若总数 $N=\sum_{i=1}^nI_{A_i}$，则

$$E(N)=\sum_{i=1}^nP(A_i).$$

事件之间可以相关。**计算期望人数、次数时，往往先拆成若干个 0—1 变量。**

**补充例：随机排列的固定点。** 把 $n$ 封信随机放进 $n$ 个信封。令 $I_i$ 表示第 $i$ 封信进入正确的信封。每个 $P(I_i=1)=1/n$，故正确配对数 $N$ 满足 $E(N)=n\cdot1/n=1$。这些指示变量并不独立，但不影响此期望计算。

### 2.2 线性性质：不要求独立

对可积随机变量和常数 $a_i,b$，课件定理 4.3 给出

$$\boxed{E\left(b+\sum_{i=1}^na_iX_i\right)=b+\sum_{i=1}^na_iE(X_i).}$$

理由是求和或积分的线性。例如在联合密度情形，

$$\iint(ax+by)f(x,y)dxdy
=a\iint xf(x,y)dxdy+b\iint yf(x,y)dxdy.$$

这里没有把联合密度分解，所以不需要独立性。若 $Y=X$，仍有 $E(X+Y)=2E(X)$。

课件用 $g_i(X_i)$ 表述同一性质：只要每一项可积，有限和的期望就是期望之和。

### 2.3 独立时乘积期望可以分解

课件定理 4.4：若 $X_1,\ldots,X_n$ **相互独立**，且各 $g_i(X_i)$ 可积，则

$$\boxed{E\left[\prod_{i=1}^ng_i(X_i)\right]=\prod_{i=1}^nE[g_i(X_i)].}$$

例如 $X,Y$ 独立时，$E(XY)=E(X)E(Y)$。连续情形的证明是

$$\begin{aligned}
E[g(X)h(Y)]
&=\iint g(x)h(y)f_X(x)f_Y(y)dxdy\\
&=\left[\int g(x)f_X(x)dx\right]
  \left[\int h(y)f_Y(y)dy\right].
\end{aligned}$$

独立性保证联合密度或联合分布能够分解，也保证乘积的绝对可积性。

反方向要小心：**仅有 $E(XY)=E(X)E(Y)$ 不能推出独立。** 它只约束一个乘积平均值；独立性要求所有有关事件的概率分解，强得多。第十节会给出反例。

### 2.4 三条辅助性质（补充）

在相应期望存在时：若 $X\le Y$ 几乎处处，则 $E(X)\le E(Y)$；若 $X\ge0$，则 $E(X)\ge0$；总有 $|E(X)|\le E|X|$。

“几乎处处”或“几乎必然”表示允许在概率为 0 的事件上不成立。对于非负变量，$E(X)=0$ 等价于 $X=0$ 几乎必然。这一点将用于理解零方差。

---

## 第三节　方差与标准差：位置以外的第二个特征

### 3.1 为什么用平方偏差

设 $\mu=E(X)$，且 $E(X^2)<\infty$。定义

$$\boxed{\operatorname{Var}(X)=E[(X-\mu)^2],\qquad
\operatorname{sd}(X)=\sqrt{\operatorname{Var}(X)}.}$$

普通偏差的平均恒为 $E(X-\mu)=0$，正负偏差会抵消；平方使不同方向的偏离都产生非负贡献。方差的单位是原单位的平方，标准差与 $X$ 同单位。例如身高用 cm 表示，方差用 $\mathrm{cm}^2$，标准差用 cm。

二阶矩有限自动推出一阶绝对矩有限，因为 $|x|\le1+x^2$。因此这一前提足以保证均值与方差公式中的每一项有限。

### 3.2 计算公式与证明

展开平方并使用线性性质：

$$\begin{aligned}
\operatorname{Var}(X)
&=E(X^2-2\mu X+\mu^2)\\
&=E(X^2)-2\mu E(X)+\mu^2\\
&=\boxed{E(X^2)-[E(X)]^2}.
\end{aligned}$$

实战中常先求 $E(X),E(X^2)$，再相减。**$E(X^2)$ 是二阶原点矩，不能直接当作方差。** 若算得方差为负数，说明计算或舍入有问题。

### 3.3 平移与缩放

课件定理 4.5：

$$\boxed{\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X),\qquad
\operatorname{sd}(aX+b)=|a|\operatorname{sd}(X).}$$

证明只需注意

$$aX+b-E(aX+b)=a(X-\mu).$$

平移改变中心，不改变围绕自身中心的波动；缩放后的偏差变为 $a$ 倍，平方偏差变为 $a^2$ 倍。负号也必须平方，标准差则乘 $|a|$。

### 3.4 方差为零是什么意思

$$\operatorname{Var}(X)=0\quad\Longleftrightarrow\quad X=E(X)\ \text{几乎必然}.$$

因为平方偏差非负，期望为零意味着平方偏差几乎必然为零。零方差变量是常数变量；它与任何变量独立，但其 Pearson 相关系数通常没有定义，因为分母为零。

### 3.5 独立和的方差与样本平均（后者为补充）

若 $X_i$ 相互独立且二阶矩有限，则

$$\boxed{\operatorname{Var}\left(\sum_i a_iX_i\right)
=\sum_i a_i^2\operatorname{Var}(X_i).}$$

展开中心化和的平方后，交叉项为

$$E[(X_i-\mu_i)(X_j-\mu_j)]
=E(X_i-\mu_i)E(X_j-\mu_j)=0.$$

事实上，两两不相关已经足够让交叉项为零；独立是充分条件。没有这些条件时应使用第八节的完整公式。

例如独立同分布的 $X_1,\ldots,X_n$ 满足 $E(X_i)=\mu,\operatorname{Var}(X_i)=\sigma^2$，则

$$E(\bar X)=\mu,\qquad \operatorname{Var}(\bar X)=\frac{\sigma^2}{n},\qquad
\operatorname{sd}(\bar X)=\frac\sigma{\sqrt n}.$$

期望中系数 $1/n$ 乘一次，方差中系数必须平方，再累加 $n$ 项。这是常见的系数错误来源。

### 3.6 均值是最佳常数预测（补充）

对任意常数 $c$，

$$E[(X-c)^2]=\operatorname{Var}(X)+(\mu-c)^2.$$

因此在所有常数中，用 $\mu$ 预测 $X$ 的均方误差最小，最小值就是方差。这是第十一节线性预测和第十七节条件期望预测的起点。

---

## 第四节　课件习题 4.1：常见分布均值、方差的推导

### 4.1 Bernoulli 分布

若 $X\sim\operatorname{Bernoulli}(p)$，则 $X\in\{0,1\}$，且 $X^2=X$，所以

$$E(X)=p,\qquad E(X^2)=p,\qquad
\boxed{\operatorname{Var}(X)=p(1-p).}$$

任何事件的指示变量都是 Bernoulli 变量，因而 $\operatorname{Var}(I_A)=P(A)[1-P(A)]$。

### 4.2 Binomial 分布

若 $X\sim\operatorname{Binomial}(n,p)$，可以表示为 $n$ 个相互独立的 Bernoulli 变量之和：$X=\sum_{i=1}^nI_i$。于是

$$\boxed{E(X)=np,\qquad \operatorname{Var}(X)=np(1-p).}$$

期望相加使用线性；方差相加使用独立性。两步依据不同，不能混为一谈。

### 4.3 Geometric 分布：第一次成功所在的试验次数

令 $q=1-p$，其中 $0<p\le1$，课件约定

$$P(X=k)=pq^{k-1},\qquad k=1,2,\ldots.$$

从几何级数 $\sum_{k=0}^\infty q^k=1/(1-q)$ 出发，在 $0\le q<1$ 的范围内逐项求导，得到

$$\sum_{k=1}^\infty kq^{k-1}=\frac1{(1-q)^2}.$$

因此

$$E(X)=p\sum_{k=1}^\infty kq^{k-1}=\frac1p.$$

再求一次导数，并乘 $pq$：

$$E[X(X-1)]
=p\sum_{k=2}^\infty k(k-1)q^{k-1}
=\frac{2pq}{(1-q)^3}=\frac{2q}{p^2}.$$

由 $X^2=X(X-1)+X$，

$$E(X^2)=\frac{2q}{p^2}+\frac1p=\frac{2-p}{p^2},$$

$$\boxed{\operatorname{Var}(X)=\frac{1-p}{p^2}.}$$

如果改为“成功前失败的次数” $W=X-1$，其均值为 $(1-p)/p$，方差不变。看到 Geometric，第一步先确认支持集从 0 还是 1 开始。

### 4.4 指数分布：用分部积分

若 $X\sim\operatorname{Exp}(\lambda)$，$\lambda>0$，密度为 $\lambda e^{-\lambda x}$，$x>0$。有

$$\begin{aligned}
E(X)&=\int_0^\infty x\lambda e^{-\lambda x}dx\\
&=[-xe^{-\lambda x}]_0^\infty+\int_0^\infty e^{-\lambda x}dx=\frac1\lambda,
\end{aligned}$$

$$E(X^2)=[-x^2e^{-\lambda x}]_0^\infty
+2\int_0^\infty xe^{-\lambda x}dx=\frac2{\lambda^2}.$$

于是

$$\boxed{E(X)=\frac1\lambda,\qquad\operatorname{Var}(X)=\frac1{\lambda^2}.}$$

边界项为零，是因为指数衰减快于这些多项式的增长。速率越大，平均等待越短。

### 4.5 正态分布：标准化后用对称性与分部积分

设 $Z\sim N(0,1)$，密度 $\phi(z)=e^{-z^2/2}/\sqrt{2\pi}$。由于 $z\phi(z)$ 为奇函数且绝对可积，$E(Z)=0$。

利用 $\phi'(z)=-z\phi(z)$，

$$\begin{aligned}
E(Z^2)&=-\int_{-\infty}^{\infty}z\phi'(z)dz\\
&=[-z\phi(z)]_{-\infty}^{\infty}+\int_{-\infty}^{\infty}\phi(z)dz=1.
\end{aligned}$$

对 $X=\mu+\sigma Z$，$\sigma>0$，得到

$$\boxed{E(X)=\mu,\qquad\operatorname{Var}(X)=\sigma^2.}$$

### 4.6 常见分布速查及条件

| 分布与参数约定 | 期望 | 方差 |
|---|---|---|
| 点质量 $P(X=a)=1$ | $a$ | $0$ |
| Bernoulli$(p)$ | $p$ | $p(1-p)$ |
| Binomial$(n,p)$ | $np$ | $np(1-p)$ |
| Geometric$(p)$，取值 $1,2,\ldots$ | $1/p$ | $(1-p)/p^2$ |
| Poisson$(\lambda)$ | $\lambda$ | $\lambda$ |
| $U(a,b)$，$a<b$ | $(a+b)/2$ | $(b-a)^2/12$ |
| Exp$(\lambda)$，速率 | $1/\lambda$ | $1/\lambda^2$ |
| Gamma$(\alpha,\lambda)$，形状—速率 | $\alpha/\lambda$ | $\alpha/\lambda^2$ |
| $\chi^2(\nu)$ | $\nu$ | $2\nu$ |
| $N(\mu,\sigma^2)$ | $\mu$ | $\sigma^2$ |
| $t(\nu)$ | $0$，要求 $\nu>1$ | $\nu/(\nu-2)$，要求 $\nu>2$ |

Poisson 的推导见第六节；Gamma 与卡方由 MGF 得到。均匀分布可用 $X=a+(b-a)U$、$U\sim U(0,1)$，结合 $E(U)=1/2,E(U^2)=1/3$ 推出。

对 $t$ 分布，$\nu\le1$ 时均值不存在；$1<\nu\le2$ 时均值为 0，但二阶矩无限，方差无有限值；均值不存在时，不应直接套用以均值为中心的方差定义。F 分布的矩及条件在第三章讲义中已列出，本章不要求据此扩展课件范围。

---

## 第五节　矩与矩母函数：从数字特征走回分布

### 5.1 原点矩与中心矩

对正整数 $r$，在相应绝对矩有限时，定义

$$\mu'_r=E(X^r)\quad\text{为 $r$ 阶原点矩},$$

$$\mu_r=E[(X-E(X))^r]\quad\text{为 $r$ 阶中心矩}.$$

第一阶原点矩是均值，第一阶中心矩是 0，第二阶中心矩是方差。不要把 $E(X^2)$ 与 $E[(X-\mu)^2]$ 混淆。

若 $E|X|^r<\infty$，则对 $0<k<r$ 有

$$|X|^k\le1+|X|^r\quad\Longrightarrow\quad E|X|^k<\infty.$$

高阶绝对矩有限推出低阶有限；反方向一般不成立。

### 5.2 MGF 的定义与存在范围

课件定义矩母函数为

$$\boxed{M_X(t)=E(e^{tX}),}$$

并要求它在 0 的某个开邻域 $(-h,h)$ 内均有限。具体计算为

$$M_X(t)=\sum_xe^{tx}p_X(x)
\quad\text{或}\quad
M_X(t)=\int_{-\infty}^{\infty}e^{tx}f_X(x)dx.$$

“在 0 附近存在”不等于“对所有实数 $t$ 都有限”。指数分布的 MGF 只在 $t<\lambda$ 时有限，但由于 $\lambda>0$，仍包含 0 的一个双侧邻域。

任何随机变量都有 $E(e^{0X})=1$，因此仅有 $M_X(0)=1$ 不能证明 MGF 在本章意义下存在。计算时应同时写出**表达式与有限域**。

### 5.3 为什么 MGF 能产生矩

对固定的 $x$，$d^re^{tx}/dt^r=x^re^{tx}$。MGF 在 0 附近有限时，可以在该邻域内把求导移入期望，于是课件定理 4.6 给出

$$M_X^{(r)}(t)=E(X^re^{tX}),\qquad
\boxed{M_X^{(r)}(0)=E(X^r).}$$

特别地，

$$\boxed{E(X)=M'_X(0),\qquad
\operatorname{Var}(X)=M''_X(0)-[M'_X(0)]^2.}$$

注意二阶导数产生的是 $E(X^2)$，还需要减去均值平方。

**补充：存在性条件在证明中的作用。** 取足够小的 $\delta>0$，有

$$E(e^{\delta|X|})\le M_X(\delta)+M_X(-\delta)<\infty.$$

多项式 $|X|^r$ 及较小邻域中的求导项可以用一个可积的指数函数控制，这就为交换微分与期望提供依据。不能仅凭形式求导就跳过有限性检查。

由此也得到：MGF 在 0 附近存在，则所有阶绝对矩均有限。**补充辨析：反方向不成立。** 例如非退化对数正态变量 $X=e^Z$、$Z\sim N(0,1)$，所有正整数阶矩都有限，但任意 $t>0$ 的 $E(e^{tX})$ 都无限，故没有这样的双侧 MGF。它说明“有很多矩”和“具有 MGF”是不同条件。

### 5.4 唯一性：相同 MGF 意味着同分布

课件定理 4.7：若 $M_X,M_Y$ 在共同邻域 $(-h,h)$ 都有限，且该区间内

$$M_X(t)=M_Y(t),$$

则 $X,Y$ 同分布，记为 $X\overset d=Y$。课件将变换唯一性定理作为已知结果，本文亦不把它误当成一个简单的代数恒等式来证明。

常用步骤是：

1. 计算待研究变量的 MGF，并写出有效区间。
2. 整理成已知分布的 MGF。
3. 确认共同区间包含 0 的邻域。
4. 由唯一性宣布同分布。

只比较前两个矩不够；只看到形式像某个 MGF，也应检查参数和有效区间。

### 5.5 仿射变换

课件推论 4.8A：若 $Y=aX+b$，则

$$\boxed{M_Y(t)=e^{bt}M_X(at).}$$

证明为 $E(e^{t(aX+b)})=e^{bt}E(e^{atX})$。常数平移在外面乘 $e^{bt}$，缩放改变自变量为 $at$，不能写成 $aM_X(t)+b$。

当 $a\ne0$ 时有限域满足 $at$ 落入 $M_X$ 的有限域；若 $a=0$，则 $Y=b$，直接有 $M_Y(t)=e^{bt}$，对所有实数有限。

### 5.6 独立和的 MGF

课件定理 4.8：若 $X_1,\ldots,X_n$ 相互独立，各 MGF 在 0 附近有限，$Y=b+\sum_ka_kX_k$，则

$$\boxed{M_Y(t)=e^{bt}\prod_{k=1}^nM_{X_k}(a_kt).}$$

因为

$$E\left[e^{t\sum_ka_kX_k}\right]
=E\left[\prod_ke^{ta_kX_k}\right]
=\prod_kE(e^{ta_kX_k}).$$

第二个等号使用相互独立性；有限域由所有非零系数对应的 $a_kt$ 条件共同决定。若变量相关，就不能一般地把和的 MGF 写成边缘 MGF 的乘积。

---

## 第六节　课件 MGF 例题：Poisson、指数、正态与二项

### 6.1 Poisson 分布：识别指数级数

若 $X\sim\operatorname{Poisson}(\lambda)$，则

$$\begin{aligned}
M_X(t)&=\sum_{k=0}^\infty e^{tk}e^{-\lambda}\frac{\lambda^k}{k!}\\
&=e^{-\lambda}\sum_{k=0}^\infty\frac{(\lambda e^t)^k}{k!}\\
&=\boxed{\exp[\lambda(e^t-1)]},\qquad t\in\mathbb R.
\end{aligned}$$

求导得

$$M'_X(t)=\lambda e^tM_X(t),$$

$$M''_X(t)=(\lambda e^t+\lambda^2e^{2t})M_X(t).$$

所以 $E(X)=\lambda$，$E(X^2)=\lambda+\lambda^2$，$\operatorname{Var}(X)=\lambda$。

### 6.2 指数分布：积分的收敛条件必须写出来

$$M_X(t)=\int_0^\infty\lambda e^{-(\lambda-t)x}dx
=\boxed{\frac\lambda{\lambda-t}},\qquad t<\lambda.$$

若 $t=\lambda$，被积函数为正的常数；若 $t>\lambda$，被积函数指数增长，因此都发散。

$$M'_X(t)=\frac\lambda{(\lambda-t)^2},\qquad
M''_X(t)=\frac{2\lambda}{(\lambda-t)^3}.$$

代 $t=0$ 得到 $E(X)=1/\lambda$、$E(X^2)=2/\lambda^2$、$\operatorname{Var}(X)=1/\lambda^2$，与第四节分部积分相互核对。

### 6.3 正态分布：核心技巧是配方

对 $X\sim N(\mu,\sigma^2)$、$\sigma>0$，

$$M_X(t)=\int_{\mathbb R}\frac1{\sqrt{2\pi}\sigma}
\exp\left[tx-\frac{(x-\mu)^2}{2\sigma^2}\right]dx.$$

配方得到

$$tx-\frac{(x-\mu)^2}{2\sigma^2}
=-\frac{[x-(\mu+\sigma^2t)]^2}{2\sigma^2}
+\mu t+\frac{\sigma^2t^2}2.$$

提取与 $x$ 无关的部分后，剩余积分是均值为 $\mu+\sigma^2t$、方差为 $\sigma^2$ 的正态密度的积分，等于 1。因此

$$\boxed{M_X(t)=\exp\left(\mu t+\frac{\sigma^2t^2}2\right),\qquad t\in\mathbb R.}$$

$$M'_X(t)=(\mu+\sigma^2t)M_X(t),$$

$$M''_X(t)=[(\mu+\sigma^2t)^2+\sigma^2]M_X(t).$$

所以 $E(X)=\mu$，$E(X^2)=\mu^2+\sigma^2$，方差为 $\sigma^2$。记忆时注意：指数中 $t$ 的系数是均值，$t^2$ 的系数是**方差的一半**。

### 6.4 习题 4.4：二项分布的 MGF

若 $Y\sim\operatorname{Binomial}(n,p)$，由二项式定理，

$$\begin{aligned}
M_Y(t)&=\sum_{y=0}^ne^{ty}\binom ny p^y(1-p)^{n-y}\\
&=\sum_{y=0}^n\binom ny(pe^t)^y(1-p)^{n-y}\\
&=\boxed{(1-p+pe^t)^n},\qquad t\in\mathbb R.
\end{aligned}$$

这是有限和，对每个实数 $t$ 都有限。取 $n=1$ 就得到 Bernoulli 的 MGF：$1-p+pe^t$。

### 6.5 Gamma 分布的 MGF（课件可加性证明的补充步骤）

课件第 46 页直接使用 Gamma 的 MGF，这里补出积分。若

$$f(x)=\frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\lambda x},\qquad x>0,$$

则对 $t<\lambda$，

$$\begin{aligned}
M_X(t)&=\frac{\lambda^\alpha}{\Gamma(\alpha)}
\int_0^\infty x^{\alpha-1}e^{-(\lambda-t)x}dx\\
&=\boxed{\left(\frac\lambda{\lambda-t}\right)^\alpha}.
\end{aligned}$$

第二步令 $u=(\lambda-t)x$，使用 Gamma 积分；$t\ge\lambda$ 时发散。求导得

$$E(X)=\frac\alpha\lambda,\qquad
E(X^2)=\frac{\alpha(\alpha+1)}{\lambda^2},\qquad
\operatorname{Var}(X)=\frac\alpha{\lambda^2}.$$

卡方为 $\operatorname{Gamma}(\nu/2,1/2)$，所以

$$M_{\chi^2(\nu)}(t)=(1-2t)^{-\nu/2},\qquad t<1/2.$$

---

## 第七节　用 MGF 识别和的分布

### 7.1 习题 4.5：独立 Bernoulli 之和

若 $X_k\sim\operatorname{Bernoulli}(p)$ 相互独立，$Y=\sum_{k=1}^nX_k$，则

$$M_Y(t)=\prod_{k=1}^n(1-p+pe^t)=(1-p+pe^t)^n.$$

它与第 6.4 小节的二项 MGF 相同，在整个实轴有限，由唯一性，

$$\boxed{Y\sim\operatorname{Binomial}(n,p).}$$

若各成功概率不同，则 MGF 为 $\prod_k(1-p_k+p_ke^t)$，一般不能合并成同一个二项分布。

### 7.2 习题 4.6：独立同成功概率的二项之和

为避免课件中“求和项数 $n$”与“各二项试验次数 $n_k$”混淆，令共有 $m$ 项。若 $X_k\sim\operatorname{Binomial}(n_k,p)$ 相互独立，则

$$M_{\sum_kX_k}(t)=\prod_{k=1}^m(1-p+pe^t)^{n_k}
=(1-p+pe^t)^{\sum_kn_k}.$$

故

$$\boxed{\sum_{k=1}^mX_k\sim\operatorname{Binomial}\left(\sum_{k=1}^mn_k,p\right).}$$

必须共享同一个 $p$；独立本身不足以推出此结论。

### 7.3 课件练习：独立正态的线性组合

若 $X_k\sim N(\mu_k,\sigma_k^2)$ 相互独立，令 $Y=\sum_ka_kX_k$，则

$$\begin{aligned}
M_Y(t)&=\prod_k\exp\left(a_k\mu_kt+\frac{a_k^2\sigma_k^2t^2}2\right)\\
&=\exp\left[t\sum_ka_k\mu_k+\frac{t^2}2\sum_ka_k^2\sigma_k^2\right].
\end{aligned}$$

所以

$$\boxed{Y\sim N\left(\sum_ka_k\mu_k,\ \sum_ka_k^2\sigma_k^2\right).}$$

系数在均值中保持原符号，在方差中平方。若所得方差为 0，$Y$ 是常数，按课件约定理解为退化正态。对有关联的联合正态，仍有线性组合正态，但方差需要协方差项，见第十四节。

### 7.4 标准化与标准正态平方

对 $X\sim N(\mu,\sigma^2)$、$\sigma>0$，$Z=(X-\mu)/\sigma$ 满足

$$M_Z(t)=e^{-\mu t/\sigma}M_X(t/\sigma)=e^{t^2/2},$$

故 $Z\sim N(0,1)$。

若 $Z\sim N(0,1)$，令 $Q=Z^2$，不能使用仿射公式，而应从函数期望积分：

$$\begin{aligned}
M_Q(t)&=E(e^{tZ^2})
=\frac1{\sqrt{2\pi}}\int_{\mathbb R}e^{-(1-2t)z^2/2}dz\\
&=\frac1{\sqrt{1-2t}},\qquad t<1/2.
\end{aligned}$$

这是 $\chi^2(1)$ 的 MGF，因此 $Z^2\sim\chi^2(1)$。若 $Z_1,\ldots,Z_n$ 相互独立，则平方后仍相互独立，于是 $\sum_iZ_i^2\sim\chi^2(n)$，与第三章的构造一致。

### 7.5 定理 4.9：五类分布的可加性

以下每一行都假设各变量相互独立：

| 各变量分布 | 和的分布 | 参数限制 |
|---|---|---|
| Poisson$(\lambda_k)$ | Poisson$(\sum_k\lambda_k)$ | 无须各速率相同 |
| Binomial$(n_k,p)$ | Binomial$(\sum_kn_k,p)$ | 同一个 $p$ |
| Gamma$(\alpha_k,\lambda)$ | Gamma$(\sum_k\alpha_k,\lambda)$ | 同一个速率 $\lambda$ |
| $\chi^2(\nu_k)$ | $\chi^2(\sum_k\nu_k)$ | 自由度相加 |
| $N(\mu_k,\sigma_k^2)$ | $N(\sum_k\mu_k,\sum_k\sigma_k^2)$ | 方差相加 |

证明都采用“MGF 相乘，再由唯一性识别”。尚未展开的三行分别为

$$\prod_ke^{\lambda_k(e^t-1)}=e^{(\sum_k\lambda_k)(e^t-1)},$$

$$\prod_k\left(\frac\lambda{\lambda-t}\right)^{\alpha_k}
=\left(\frac\lambda{\lambda-t}\right)^{\sum_k\alpha_k},$$

$$\prod_k(1-2t)^{-\nu_k/2}=(1-2t)^{-(\sum_k\nu_k)/2}.$$

“和属于同一分布族”不是所有分布都有的性质。例如两个独立均匀变量的和一般不是均匀分布。

### 7.6 指数变量：和与最小值必须区分

**同速率独立和。** 若 $X_1,\ldots,X_n$ 独立且均为 Exp$(\lambda)$，则

$$M_{\sum_kX_k}(t)=\left(\frac\lambda{\lambda-t}\right)^n,$$

所以

$$\boxed{\sum_kX_k\sim\operatorname{Gamma}(n,\lambda).}$$

当 $n>1$ 时通常不是指数分布；这里和表示依次完成若干阶段所需总时间。

**可以不同速率的独立最小值。** 若 $X_k\sim\operatorname{Exp}(\lambda_k)$ 相互独立，$W=\min_kX_k$，则对 $x\ge0$，

$$\begin{aligned}
P(W>x)&=P(X_1>x,\ldots,X_n>x)\\
&=\prod_ke^{-\lambda_kx}=e^{-x\sum_k\lambda_k}.
\end{aligned}$$

故

$$\boxed{W\sim\operatorname{Exp}\left(\sum_k\lambda_k\right).}$$

这里用生存函数最方便，独立性用于联合事件概率分解。它表示多个机制并行工作时，首次发生事件的等待时间。最小值结论允许速率不同；Gamma 和的结论则需要同速率。

---

## 第八节　协方差：两个变量的中心化乘积平均

### 8.1 定义及正负含义

设 $E(X^2),E(Y^2)<\infty$，记 $\mu_X=E(X),\mu_Y=E(Y)$。定义

$$\boxed{\operatorname{Cov}(X,Y)=E[(X-\mu_X)(Y-\mu_Y)].}$$

二阶矩有限通过 Cauchy–Schwarz 保证这里的乘积绝对可积。若两个变量常在各自均值的同侧，中心化乘积常为正；若常在均值的相反侧，乘积常为负。协方差总结这种**线性共同变化**，正负项也可能相互抵消。

展开得最常用的计算式：

$$\boxed{\operatorname{Cov}(X,Y)=E(XY)-E(X)E(Y).}$$

同时

$$\operatorname{Cov}(X,Y)=\operatorname{Cov}(Y,X),\qquad
\operatorname{Cov}(X,X)=\operatorname{Var}(X).$$

协方差有单位，改变测量单位会改变数值，因此不适宜直接比较不同量纲的数据关系强弱。

### 8.2 双线性：常数项不产生协方差

课件定理 4.10 给出

$$\boxed{\operatorname{Cov}(aX+b,cY+d)=ac\operatorname{Cov}(X,Y),}$$

以及

$$\boxed{\operatorname{Cov}\left(\sum_ia_iX_i,\sum_jb_jY_j\right)
=\sum_i\sum_ja_ib_j\operatorname{Cov}(X_i,Y_j).}$$

证明是先把和减去其均值，再展开中心化乘积，最后应用期望线性。这里**不要求独立性**。

例如

$$\begin{aligned}
\operatorname{Cov}(X+Y,X-Y)
&=\operatorname{Var}(X)-\operatorname{Cov}(X,Y)\\
&\quad+\operatorname{Cov}(Y,X)-\operatorname{Var}(Y)\\
&=\operatorname{Var}(X)-\operatorname{Var}(Y).
\end{aligned}$$

两个交叉协方差自动抵消，不需要先假设 $X,Y$ 独立。

### 8.3 和的方差：完整公式

使用 $\operatorname{Var}(U)=\operatorname{Cov}(U,U)$，课件推论 4.11 得到

$$\boxed{\operatorname{Var}\left(\sum_ia_iX_i\right)
=\sum_ia_i^2\operatorname{Var}(X_i)
+2\sum_{i<j}a_ia_j\operatorname{Cov}(X_i,X_j).}$$

其中对角项是方差；非对角项按对称性两两合并，产生系数 2。特别地，

$$\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y),$$

$$\operatorname{Var}(X-Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)-2\operatorname{Cov}(X,Y).$$

即使独立，差的方差仍然是两个方差相加，不是相减。

**补充自检：** 若 $Y=X$，则 $\operatorname{Var}(X+Y)=4\operatorname{Var}(X)$、$\operatorname{Var}(X-Y)=0$。如果忽略协方差项，两式都会算错。

### 8.4 用矩阵压缩公式（补充）

随机向量 $\boldsymbol X$ 的协方差矩阵为 $\Sigma=(\operatorname{Cov}(X_i,X_j))$。则

$$\operatorname{Var}(\boldsymbol a^T\boldsymbol X)=\boldsymbol a^T\Sigma\boldsymbol a\ge0.$$

因此协方差矩阵一定对称且半正定。二维时

$$\Sigma=\begin{pmatrix}
\sigma_X^2&\operatorname{Cov}(X,Y)\\
\operatorname{Cov}(X,Y)&\sigma_Y^2
\end{pmatrix}.$$

矩阵只是完整展开公式的简写，不能取代对各项含义的理解。

---

## 第九节　相关系数与课件例 4.8

### 9.1 用标准差消去量纲

当 $0<\sigma_X,\sigma_Y<\infty$ 时，定义 Pearson 相关系数

$$\boxed{\rho_{X,Y}=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}.}$$

它等于标准化变量 $U=(X-\mu_X)/\sigma_X$ 与 $V=(Y-\mu_Y)/\sigma_Y$ 的乘积期望：$\rho=E(UV)$。相关系数无量纲，但只描述线性关系，不能概括全部依赖。

### 9.2 为什么相关系数在 $[-1,1]$ 内

对中心化变量使用 Cauchy–Schwarz 不等式：

$$\{E[(X-\mu_X)(Y-\mu_Y)]\}^2
\le E[(X-\mu_X)^2]E[(Y-\mu_Y)^2].$$

除以正的 $\sigma_X^2\sigma_Y^2$，得到

$$\boxed{-1\le\rho\le1.}$$

等号成立恰好在两个中心化变量成确定比例时：

$$Y-\mu_Y=a(X-\mu_X)\quad\text{几乎必然},\qquad a\ne0.$$

因此

$$\boxed{|\rho|=1\ \Longleftrightarrow\ Y=aX+b\ \text{几乎必然},\ a\ne0.}$$

斜率为正时 $\rho=1$，斜率为负时 $\rho=-1$。“完全相关”在这里指精确的仿射关系；$Y=X^2$ 这样的精确非线性关系不必有 $|\rho|=1$。

### 9.3 单位变化与符号（补充）

对非零 $a,c$，

$$\rho_{aX+b,cY+d}=\frac{ac}{|a||c|}\rho_{X,Y}.$$

平移与正比例单位换算不改变相关系数；仅把一个轴反向会翻转符号。若缩放系数为 0，所得变量为常数，相关系数无定义。

### 9.4 例 4.8：从联合 PMF 算相关

**题目（第 53—55 页）。** 已知

$$p(x,y)=\frac{x+2y}{18},\qquad x,y\in\{1,2\}.$$

将表列全，避免漏项：

| $X\backslash Y$ | $1$ | $2$ | $p_X(x)$ |
|---|---|---|---|
| $1$ | $3/18$ | $5/18$ | $4/9$ |
| $2$ | $4/18$ | $6/18$ | $5/9$ |
| $p_Y(y)$ | $7/18$ | $11/18$ | $1$ |

先求边缘矩：

$$E(X)=\frac49+2\frac59=\frac{14}9,\qquad
E(X^2)=\frac49+4\frac59=\frac83,$$

$$E(Y)=\frac7{18}+2\frac{11}{18}=\frac{29}{18},\qquad
E(Y^2)=\frac7{18}+4\frac{11}{18}=\frac{17}6.$$

因此

$$\operatorname{Var}(X)=\frac83-\left(\frac{14}9\right)^2=\frac{20}{81},$$

$$\operatorname{Var}(Y)=\frac{17}6-\left(\frac{29}{18}\right)^2=\frac{77}{324}.$$

再用联合 PMF 求交叉矩：

$$E(XY)=\frac{1\cdot1\cdot3+1\cdot2\cdot5+2\cdot1\cdot4+2\cdot2\cdot6}{18}
=\frac52.$$

于是

$$\operatorname{Cov}(X,Y)=\frac52-\frac{14}9\frac{29}{18}=-\frac1{162},$$

$$\boxed{\rho=\frac{-1/162}{\sqrt{(20/81)(77/324)}}
=-\frac1{\sqrt{1540}}\approx-0.0255.}$$

虽然 PMF 的表达式随 $x,y$ 增大而增大，但相关系数仍略为负。不能根据密度或 PMF 的局部增减来直接猜相关符号；需要比较“相对于各自均值的共同偏离”。非零协方差也直接说明二者不独立。

---

## 第十节　独立、不相关与非线性依赖

### 10.1 正确的逻辑方向

在二阶矩有限的前提下，

$$X\perp Y\ \Longrightarrow\ E(XY)=E(X)E(Y)
\ \Longrightarrow\ \operatorname{Cov}(X,Y)=0.$$

“不相关”就是协方差为 0；当两个方差都为正时，也等价于相关系数为 0。一般不能反推独立。

独立要求联合概率结构完整分解；不相关仅是一条关于二阶混合矩的等式。若其中某个变量是常数，协方差为 0，且它与另一个变量独立，但相关系数没有定义。

### 10.2 例 4.10：离散的不相关但依赖

**题目（第 64 页）。** 三个点 $(0,1),(1,0),(2,1)$ 各以概率 $1/3$ 出现。

直接算得

$$E(X)=1,\qquad E(Y)=\frac23,\qquad
E(XY)=\frac{0+0+2}3=\frac23.$$

故 $\operatorname{Cov}(X,Y)=0$。但

$$P(X=0,Y=0)=0,\qquad
P(X=0)P(Y=0)=\frac13\frac13=\frac19.$$

所以不独立。实际上 $Y=(X-1)^2$，知道 $X$ 就完全知道 $Y$，只是这种依赖不表现为非零线性相关。

### 10.3 连续反例：$Y=X^2$

**题目（第 65—66 页）。** $X\sim U(-1,1)$，$Y=X^2$。对称性给出

$$E(X)=0,\quad E(XY)=E(X^3)=0,\quad E(Y)=E(X^2)=\frac13,$$

因此 $\operatorname{Cov}(X,Y)=0$。

取 $A=\{|X|\le1/2\}$、$B=\{Y\le1/4\}$。由于 $Y=X^2$，$A=B$，所以

$$P(A\cap B)=\frac12\ne\frac14=P(A)P(B).$$

这用事件概率严格证明不独立。两个边缘都连续，并不保证存在普通二维联合密度；本例全部概率集中在抛物线 $y=x^2$ 上。

![线性相关与依赖的区别](<C:/Users/yang/Documents/ChatGPT/概率论/output/chapter4_dependence.png>)

*补充示意图：每幅为固定随机种子生成的样本，只辅助理解；图中 $\rho$ 指理论相关系数。独立与不相关的结论由公式及事件概率证明，不能仅靠散点图判定。第四幅将在第十四节解释。*

### 10.4 三个不能混用的判断

| 已知信息 | 可以推出 | 不能一般推出 |
|---|---|---|
| 独立且二阶矩有限 | 协方差为 0 | 变量之间存在确定关系 |
| 协方差为 0 | 不相关、和的方差可直接相加 | 独立 |
| 相关系数绝对值为 1 | 几乎必然存在非零斜率的直线关系 | 一般非线性关系都能被这种相关系数识别 |
| 联合正态且协方差为 0 | 独立 | 把“联合正态”弱化成“两个边缘正态” |

---

## 第十一节　最佳线性预测：用 $X$ 预测 $Y$

### 11.1 最小化的是什么

课件第 58—59 页考虑：在所有 $\widehat Y=a+bX$ 中，找到使

$$\operatorname{MSE}(a,b)=E[(Y-a-bX)^2]$$

最小的系数。假设 $X,Y$ 二阶矩有限且 $\operatorname{Var}(X)>0$。这里最小化的是 **$Y$ 方向的预测残差平方**，不是点到直线的垂直几何距离，也不是用样本估计回归系数的过程。

### 11.2 配方推导

将均值部分和中心化部分拆开：

$$\begin{aligned}
E[(Y-a-bX)^2]
={}&(\mu_Y-a-b\mu_X)^2\\
&+\sigma_Y^2+b^2\sigma_X^2-2b\operatorname{Cov}(X,Y).
\end{aligned}$$

对给定 $b$，第一项在 $a=\mu_Y-b\mu_X$ 时为零。剩下部分对 $b$ 配方：

$$\begin{aligned}
&\sigma_Y^2+b^2\sigma_X^2-2b\operatorname{Cov}(X,Y)\\
&=\sigma_X^2\left[b-\frac{\operatorname{Cov}(X,Y)}{\sigma_X^2}\right]^2
+\sigma_Y^2-\frac{\operatorname{Cov}(X,Y)^2}{\sigma_X^2}.
\end{aligned}$$

因此

$$\boxed{\widehat Y=\mu_Y+\frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(X)}(X-\mu_X).}$$

若 $\sigma_Y>0$，可写为

$$\widehat Y=\mu_Y+\rho\frac{\sigma_Y}{\sigma_X}(X-\mu_X),$$

$$\boxed{\operatorname{MSE}_{\min}=\sigma_Y^2(1-\rho^2).}$$

若 $Y$ 为常数，直接预测该常数，最小误差为 0；此时不使用含 $\rho$ 的表达式。

### 11.3 解释与限制

斜率为 $\rho\sigma_Y/\sigma_X$，一般不等于 $\rho$，因为预测斜率有单位。若先把两个变量都标准化，预测斜率才是 $\rho$。

当 $\rho=0$，最佳线性预测为常数 $\mu_Y$。这并不说明 $X$ 完全没有预测价值。例如 $Y=X^2$ 且 $X\sim U(-1,1)$ 时，最佳线性预测是 $1/3$，但知道 $X$ 后，用非线性函数 $X^2$ 可以实现零误差。

对于二元正态，条件均值恰好是上述直线；一般模型中的 $E(Y\mid X)$ 则可能弯曲。第十七节会解释为什么条件期望是允许任意函数时的最佳预测。

### 11.4 课件离散表格例题

**题目（第 60—61 页）。** 联合分布为

| $X\backslash Y$ | $0$ | $1$ |
|---|---|---|
| $0$ | $0.4$ | $0.1$ |
| $1$ | $0.1$ | $0.4$ |

两个边缘均为 Bernoulli$(1/2)$，所以

$$E(X)=E(Y)=\frac12,\qquad\operatorname{Var}(X)=\operatorname{Var}(Y)=\frac14.$$

只有 $(1,1)$ 对 $XY$ 有非零贡献，故

$$E(XY)=0.4,\qquad\operatorname{Cov}(X,Y)=0.4-0.25=0.15,$$

$$\rho=\frac{0.15}{0.25}=0.6.$$

于是

$$\boxed{\widehat Y=0.5+0.6(X-0.5)=0.2+0.6X,}$$

$$\boxed{\operatorname{MSE}_{\min}=0.25(1-0.6^2)=0.16.}$$

还可以直接核对：给定 $X=0$，$P(Y=1\mid X=0)=0.1/0.5=0.2$；给定 $X=1$，该概率为 $0.4/0.5=0.8$。因此本例 $E(Y\mid X)$ 恰好是 $0.2+0.6X$，而且两组条件方差均为 $0.2\cdot0.8=0.16$。此处线性与条件预测一致，是因为条件均值在两个可能的 $X$ 值上可以用直线连接，不要求正态。

---

## 第十二节　课件应用：一元正态计算与联合建模的必要性

### 12.1 灌装质量控制

**题目（第 71—72 页）。** 灌装体积 $X\sim N(500,10^2)$，单位 mL。求少于 485 mL 的概率、在 $[485,515]$ 内的比例，以及只有 5% 瓶子会超过的体积。

先统一标准化：$Z=(X-500)/10\sim N(0,1)$。记 $\Phi$ 为标准正态 CDF，则

$$P(X<485)=\Phi(-1.5)\approx\boxed{0.0668},$$

$$P(485\le X\le515)=\Phi(1.5)-\Phi(-1.5)
\approx\boxed{0.8664}.$$

令上侧 5% 分位点为 $c$，则 $P(X\le c)=0.95$，所以

$$\frac{c-500}{10}=\Phi^{-1}(0.95)\approx1.64485,$$

$$\boxed{c\approx516.45\ \mathrm{mL}.}$$

上侧 5% 对应 CDF 的 95% 分位点，不能误用 $\Phi^{-1}(0.05)$。正态分布连续，因此这里端点的开闭不改变概率。

### 12.2 两项健康测量：边缘还缺什么

**题目（第 73—74 页）。** 已知 $X\sim N(120,15^2)$、$Y\sim N(200,30^2)$，希望研究二者同时偏高的概率及组合指标 $R=X+0.5Y$。

仅由边缘可以知道

$$E(R)=120+0.5\cdot200=220,$$

但其方差还需要协方差：

$$\operatorname{Var}(R)=225+0.25\cdot900+\operatorname{Cov}(X,Y).$$

同时偏高的概率更需要联合分布。单独添加一个相关系数，通常仍不足以确定所有联合概率；课件接着采用**二元联合正态模型**，再给定 $\rho=0.6$。于是

$$\operatorname{Cov}(X,Y)=0.6\cdot15\cdot30=270,$$

$$\operatorname{Var}(R)=225+225+270=720,$$

$$\boxed{R\sim N(220,720).}$$

注意 $\sqrt{720}$ 才是该指标的标准差。原题没有指定“偏高”的两个阈值，因此不能给出唯一数值概率；设阈值为 $a,b$，联合正态模型下可写为

$$P(X>a,Y>b)=\int_a^\infty
\left[1-\Phi\left(\frac{b-\mu_Y-\rho(\sigma_Y/\sigma_X)(x-\mu_X)}{\sigma_Y\sqrt{1-\rho^2}}\right)\right]f_X(x)dx.$$

这是后面条件正态与全概率思想的应用，不需要擅自补出题目未给的阈值。上述为课件中的数学建模示例，并非对真实人群分布的实证结论。

---

## 第十三节　二元正态：从独立正态构造相关正态

### 13.1 构造比长密度更容易理解

课件第 76 页：令 $Z_1,Z_2$ 相互独立且都为 $N(0,1)$。对 $\sigma_X,\sigma_Y>0$、$-1\le\rho\le1$，定义

$$\boxed{\begin{aligned}
X&=\mu_X+\sigma_XZ_1,\\
Y&=\mu_Y+\sigma_Y\bigl(\rho Z_1+\sqrt{1-\rho^2}Z_2\bigr).
\end{aligned}}$$

二者共享 $Z_1$ 带来的波动，$Y$ 还含有独立来源 $Z_2$。系数 $\rho$ 控制共享部分的方向与大小，$\sqrt{1-\rho^2}$ 保证标准化后的 $Y$ 总方差为 1。

**补充等价定义：** 一个向量称为联合正态，如果它的每个实系数线性组合都为一元正态，允许零方差的常数情形。上述构造满足这个定义；“每个分量分别正态”则是更弱的条件。

### 13.2 均值、方差与协方差

由构造和 $\operatorname{Cov}(Z_1,Z_2)=0$，

$$E(X)=\mu_X,\quad E(Y)=\mu_Y,\quad\operatorname{Var}(X)=\sigma_X^2,$$

$$\operatorname{Var}(Y)=\sigma_Y^2[\rho^2+(1-\rho^2)]=\sigma_Y^2,$$

$$\operatorname{Cov}(X,Y)
=\sigma_X\sigma_Y[\rho\operatorname{Var}(Z_1)+\sqrt{1-\rho^2}\operatorname{Cov}(Z_1,Z_2)]
=\rho\sigma_X\sigma_Y.$$

所以构造中的 $\rho$ 正是 Pearson 相关系数，协方差矩阵为

$$\boxed{\Sigma=\begin{pmatrix}
\sigma_X^2&\rho\sigma_X\sigma_Y\\
\rho\sigma_X\sigma_Y&\sigma_Y^2
\end{pmatrix}.}$$

在联合正态模型内，两个均值、两个方差及一个相关系数共五个参数决定联合分布。

### 13.3 非退化与退化：为什么要求 $|\rho|<1$

若 $|\rho|<1$，两条独立噪声方向都存在，$\det\Sigma=\sigma_X^2\sigma_Y^2(1-\rho^2)>0$，分布有普通二维密度，支持为整个平面。

若 $|\rho|=1$，$Z_2$ 项消失，

$$Y=\mu_Y+\rho\frac{\sigma_Y}{\sigma_X}(X-\mu_X)\quad\text{几乎必然}.$$

全部概率集中在一条直线上，没有普通二维面积密度。边缘、联合 MGF、线性组合结论仍成立，但不能将 $\rho=\pm1$ 直接代入含 $\sqrt{1-\rho^2}$ 分母的密度公式。

### 13.4 密度的完整推导：连接第三章换元

假设 $|\rho|<1$，令

$$u=\frac{x-\mu_X}{\sigma_X},\qquad v=\frac{y-\mu_Y}{\sigma_Y}.$$

逆变换为

$$z_1=u,\qquad z_2=\frac{v-\rho u}{\sqrt{1-\rho^2}}.$$

逆雅可比矩阵为

$$\frac{\partial(z_1,z_2)}{\partial(x,y)}
=\begin{pmatrix}
1/\sigma_X&0\\
-\rho/(\sigma_X\sqrt{1-\rho^2})&1/(\sigma_Y\sqrt{1-\rho^2})
\end{pmatrix},$$

故绝对行列式为 $1/[\sigma_X\sigma_Y\sqrt{1-\rho^2}]$。两个独立标准正态的联合密度为 $e^{-(z_1^2+z_2^2)/2}/(2\pi)$，于是

$$f_{X,Y}(x,y)=\frac{\exp\left[-\frac12\left(u^2+\frac{(v-\rho u)^2}{1-\rho^2}\right)\right]}
{2\pi\sigma_X\sigma_Y\sqrt{1-\rho^2}}.$$

使用恒等式

$$u^2+\frac{(v-\rho u)^2}{1-\rho^2}
=\frac{u^2-2\rho uv+v^2}{1-\rho^2},$$

得到标准形式

$$\boxed{f_{X,Y}(x,y)=\frac1{2\pi\sigma_X\sigma_Y\sqrt{1-\rho^2}}
\exp\left[-\frac{u^2-2\rho uv+v^2}{2(1-\rho^2)}\right],\quad (x,y)\in\mathbb R^2.}$$

与其死背长公式，更应记住构造、逆变换与这条配方恒等式。

### 13.5 边缘分布：构造与积分的两种证明

由构造，$X$ 显然为 $N(\mu_X,\sigma_X^2)$；$Y$ 是独立正态的线性组合，均值和方差如上，也为 $N(\mu_Y,\sigma_Y^2)$。

对非退化情形，配方为

$$u^2-2\rho uv+v^2=(1-\rho^2)u^2+(v-\rho u)^2.$$

固定 $x$，以 $dy=\sigma_Ydv$ 积分：

$$\begin{aligned}
f_X(x)&=\frac{e^{-u^2/2}}{2\pi\sigma_X\sqrt{1-\rho^2}}
\int_{\mathbb R}e^{-(v-\rho u)^2/[2(1-\rho^2)]}dv\\
&=\frac{e^{-u^2/2}}{2\pi\sigma_X\sqrt{1-\rho^2}}
\sqrt{2\pi(1-\rho^2)}\\
&=\frac1{\sqrt{2\pi}\sigma_X}e^{-u^2/2}.
\end{aligned}$$

交换 $X,Y$ 得另一边缘。积分证明只用于 $|\rho|<1$；退化情形直接用构造。

### 13.6 联合矩母函数

定义 $M_{X,Y}(s,t)=E(e^{sX+tY})$。由构造，

$$sX+tY=s\mu_X+t\mu_Y+(s\sigma_X+t\rho\sigma_Y)Z_1
+t\sigma_Y\sqrt{1-\rho^2}Z_2.$$

用独立性和标准正态 MGF 得

$$\begin{aligned}
M_{X,Y}(s,t)
&=e^{s\mu_X+t\mu_Y}
e^{(s\sigma_X+t\rho\sigma_Y)^2/2}
e^{t^2\sigma_Y^2(1-\rho^2)/2}\\
&=\boxed{\exp\left[\mu_Xs+\mu_Yt+
\frac12(\sigma_X^2s^2+2\rho\sigma_X\sigma_Yst+\sigma_Y^2t^2)\right]}.
\end{aligned}$$

它对所有实数 $s,t$ 有限，包括 $|\rho|=1$ 的退化情况。联合 MGF 中的混合项编码了协方差；把 $t=0$ 或 $s=0$ 就恢复边缘 MGF。

---

## 第十四节　联合正态的线性组合与独立性

### 14.1 有关也可以相加后仍然正态

若 $(X,Y)$ 联合正态，令 $W=aX+bY$，则

$$M_W(r)=M_{X,Y}(ar,br).$$

代入上式可识别出

$$\boxed{aX+bY\sim N\left(a\mu_X+b\mu_Y,
a^2\sigma_X^2+b^2\sigma_Y^2+2ab\rho\sigma_X\sigma_Y\right).}$$

此处不要求 $X,Y$ 独立，前提是联合正态；协方差项不能略去。若计算出的方差为零，就将该分布理解为点质量。

“边缘都正态”并不足以使和正态；第 14.3 小节将直接展示一个含点质量的和。

### 14.2 联合正态中，不相关等价于独立

独立推出协方差为零，是一般性质。反过来，在联合正态模型中，若 $\operatorname{Cov}(X,Y)=0$，联合 MGF 分解为

$$M_{X,Y}(s,t)=e^{\mu_Xs+\sigma_X^2s^2/2}
e^{\mu_Yt+\sigma_Y^2t^2/2}=M_X(s)M_Y(t).$$

右侧是具有给定边缘的独立变量对的联合 MGF，由多元唯一性得到联合分布为乘积分布，即独立。

$$\boxed{(X,Y)\text{ 联合正态}\quad\Longrightarrow\quad
X\perp Y\ \Longleftrightarrow\ \operatorname{Cov}(X,Y)=0.}$$

若两个方差为正，也等价于 $\rho=0$。如果有零方差分量，直接用其为常数的性质处理；不勉强定义相关系数。

### 14.3 课件反例：两个边缘正态、零协方差，但仍然依赖

**题目（第 90—91 页）。** 设 $Z\sim N(0,1)$，$S$ 独立于 $Z$，且 $P(S=1)=P(S=-1)=1/2$。令

$$X=Z,\qquad Y=SZ.$$

由于 $Z$ 与 $-Z$ 同分布，$Y$ 的分布是两个相同标准正态分布的等权混合，因此 $Y\sim N(0,1)$；$X$ 也标准正态。

同时

$$E(XY)=E(SZ^2)=E(S)E(Z^2)=0,$$

故协方差和相关系数都为 0。但 $|X|=|Y|$ 几乎必然。选取 $c>0$，令 $q=P(|Z|\le c)\in(0,1)$，有

$$P(|X|\le c,|Y|\le c)=q\ne q^2.$$

因此二者依赖，不可能联合正态。图中样本集中在两条交叉直线上，而不是一个非退化二维高斯云团。

**补充直接检验：** $X+Y=(1+S)Z$，有一半概率等于 0，另一半为 $2Z$。它既不是有正方差的连续正态，也不是常数，所以不服从一元正态。这直接否定“所有线性组合正态”，并表明仅由正态边缘不能推断和正态。

### 14.4 课件例题：和与差相互独立

**题目（第 96—97 页）。** $(X,Y)$ 联合正态，均值为 0、方差都为 1、相关系数为 $\rho\in(-1,1)$。令 $U=X+Y,V=X-Y$。

均值都为 0，并且

$$\operatorname{Var}(U)=2+2\rho=2(1+\rho),$$

$$\operatorname{Var}(V)=2-2\rho=2(1-\rho).$$

所以

$$\boxed{U\sim N(0,2(1+\rho)),\qquad V\sim N(0,2(1-\rho)).}$$

再算 $\operatorname{Cov}(U,V)=\operatorname{Var}(X)-\operatorname{Var}(Y)=0$。

关键的最后一步不能省：$(U,V)$ 是联合正态向量的线性变换，因此**它们也是联合正态**。于是由零协方差推出 $U,V$ 独立。

为什么线性变换保持联合正态？任意 $cU+dV=(c+d)X+(c-d)Y$ 仍为原联合正态向量的线性组合，所以服从正态。若原变量不联合正态，仅有相等方差，最多能得到和与差不相关，不能保证独立。

---

## 第十五节　二元正态的条件分布

### 15.1 核心公式与条件

对 $\sigma_X,\sigma_Y>0$、$|\rho|<1$ 的联合正态，

$$\boxed{Y\mid X=x\sim N\left(
\mu_Y+\rho\frac{\sigma_Y}{\sigma_X}(x-\mu_X),\quad
\sigma_Y^2(1-\rho^2)\right).}$$

所以条件均值是关于 $x$ 的仿射函数，条件方差不随 $x$ 改变。交换变量即可写出 $X\mid Y=y$：均值中的标准差比也要一起交换。

给定 $X=x$ 后，$x$ 是确定参数。连续情况下这通过条件密度定义，不是把普通条件概率写成一个分母为 $P(X=x)=0$ 的比值。

### 15.2 从联合密度配方得到条件密度

由第三章公式，

$$f_{Y\mid X}(y\mid x)=\frac{f_{X,Y}(x,y)}{f_X(x)}.$$

利用第十三节的配方，除去 $X$ 的边缘密度后，剩下

$$f_{Y\mid X}(y\mid x)=\frac1{\sqrt{2\pi}\sigma_Y\sqrt{1-\rho^2}}
\exp\left[-\frac{(v-\rho u)^2}{2(1-\rho^2)}\right].$$

又因为

$$v-\rho u=\frac{y-\mu_Y-\rho(\sigma_Y/\sigma_X)(x-\mu_X)}{\sigma_Y},$$

这正是上述均值与方差的正态密度。

### 15.3 构造给出的预测与残差解释

原构造可重写为

$$Y=\underbrace{\mu_Y+\rho\frac{\sigma_Y}{\sigma_X}(X-\mu_X)}_{\text{由 }X\text{ 决定的部分}}
+\underbrace{\sigma_Y\sqrt{1-\rho^2}Z_2}_{\text{独立于 }X\text{ 的残差}}.$$

因此给定 $X$ 后只剩下独立残差的随机性。条件方差为 $\sigma_Y^2(1-\rho^2)$，与 $x$ 无关。

当 $\rho=0$，条件分布等于原来的边缘分布；当 $|\rho|$ 越接近 1，给定 $X$ 后剩余波动越小；当 $|\rho|=1$，条件分布退化为预测直线上的点质量，不能再用非退化密度公式。

### 15.4 课件综合计算例题

**题目（第 94—95 页）。** $(X,Y)$ 联合正态，参数为

$$\mu_X=1,\quad\mu_Y=2,\quad\sigma_X=2,\quad\sigma_Y=3,\quad\rho=\frac12.$$

**(1) 求 $X+Y$ 的分布。** 先算协方差 $\rho\sigma_X\sigma_Y=3$，故

$$\boxed{X+Y\sim N(1+2,\ 4+9+2\cdot3)=N(3,19).}$$

**(2) 求 $Y\mid X=3$ 的分布。** 条件均值

$$m=2+\frac12\frac32(3-1)=3.5,$$

条件方差

$$s^2=9\left(1-\frac14\right)=\frac{27}4=6.75.$$

因此

$$\boxed{Y\mid X=3\sim N(3.5,6.75).}$$

**(3) 求条件右尾概率。** 必须使用条件均值与条件标准差：

$$\begin{aligned}
P(Y>5\mid X=3)
&=1-\Phi\left(\frac{5-3.5}{\sqrt{6.75}}\right)\\
&=\boxed{1-\Phi(1/\sqrt3)\approx0.2819}.
\end{aligned}$$

不能仍然用边缘的 $\mu_Y=2,\sigma_Y=3$ 标准化，也不能把条件方差 $6.75$ 直接当作标准差。

---

## 第十六节　条件期望：信息改变时，平均值也改变

### 16.1 机器次品率：先从分组平均理解

**课件例题（第 99—101 页）。** 用 $X$ 标识产品来自机器 A 或 B，用 $Y$ 表示是否次品。已知

$$P(X=A)=0.7,\quad P(X=B)=0.3,$$

$$P(Y=1\mid X=A)=0.02,\quad P(Y=1\mid X=B)=0.08.$$

由于 $Y$ 是指示变量，

$$E(Y\mid X=A)=0.02,\qquad E(Y\mid X=B)=0.08.$$

在不知道机器前，对分组平均按组概率加权：

$$\boxed{E(Y)=0.7\cdot0.02+0.3\cdot0.08=0.038.}$$

不能把两个次品率等权平均为 0.05，因为两台机器贡献的产品比例不同。

### 16.2 三种记号对应三种对象

| 记号 | 数学对象 | 机器例子的意义 |
|---|---|---|
| $E(Y)$ | 一个确定数 | 总体次品率 $0.038$ |
| $E(Y\mid X=x)$ | 给定 $x$ 后的确定数 | 指定机器的次品率 |
| $E(Y\mid X)$ | $X$ 的函数，是随机变量 | 根据实际机器选出 $0.02$ 或 $0.08$ |

定义 $g(x)=E(Y\mid X=x)$，则

$$\boxed{E(Y\mid X)=g(X).}$$

本例具体为

$$E(Y\mid X)=\begin{cases}0.02,&X=A,\\0.08,&X=B.\end{cases}$$

这个随机变量有自己的分布：以概率 0.7 取 0.02，以概率 0.3 取 0.08。把它再求一次期望，才恢复总体平均。

### 16.3 从条件分布计算条件期望

对离散联合分布，在 $p_X(x)>0$ 时，

$$\boxed{E(Y\mid X=x)=\sum_y y\,p_{Y\mid X}(y\mid x)
=\frac{\sum_y y\,p_{X,Y}(x,y)}{p_X(x)}.}$$

对具有联合密度的连续分布，在 $f_X(x)>0$ 且相应条件绝对矩有限时，

$$\boxed{E(Y\mid X=x)=\int y\,f_{Y\mid X}(y\mid x)dy
=\frac{\int y\,f_{X,Y}(x,y)dy}{f_X(x)}.}$$

步骤是：固定 $x$ → 写出条件支持 → 求条件分布并归一化 → 对 $y$ 求平均 → 最后把 $x$ 换成 $X$。

如果直接给出了 $Y\mid X=x$ 的已知分布，就直接用该分布均值，无需先恢复联合密度。

条件期望作为随机变量只在“几乎必然”的意义下唯一；在 $X$ 不会取到的值上可以任意定义。连续模型中单个条件点的条件分布通常选用由密度比给出的自然版本，这不是给零概率事件套普通概率比值。

### 16.4 条件期望的基本性质

课件第 104 页的恒等式均在有关可积条件下几乎必然成立：

$$\boxed{E(aY+bZ\mid X)=aE(Y\mid X)+bE(Z\mid X).}$$

$$\boxed{E[h(X)Y\mid X]=h(X)E(Y\mid X).}$$

$$\boxed{E[h(X)\mid X]=h(X).}$$

第二条叫“把已知量提出”：给定 $X$ 后，$h(X)$ 已经确定。它不要求 $h(X)$ 与 $Y$ 独立。对于无界 $h$，需保证涉及的乘积可积；不能忽略这些条件随意运算。

若 $Y$ 独立于 $X$，则

$$\boxed{E(Y\mid X)=E(Y).}$$

独立意味着条件分布不变，自然使均值不变。但反方向一般不成立，见第 17.4 小节。

---

## 第十七节　全期望公式与预测

### 17.1 全期望：先在组内平均，再跨组平均

课件第 105 页：若 $E|Y|<\infty$，

$$\boxed{E[E(Y\mid X)]=E(Y).}$$

离散情形为

$$E(Y)=\sum_x E(Y\mid X=x)p_X(x),$$

连续情形为

$$E(Y)=\int_{-\infty}^{\infty}E(Y\mid X=x)f_X(x)dx.$$

外层使用的是**条件变量 $X$ 的分布**，不是 $Y$ 的分布。条件均值函数并不是密度，不需要积分为 1。

离散证明是

$$\begin{aligned}
E[E(Y\mid X)]
&=\sum_x\left[\sum_y yp_{Y\mid X}(y\mid x)\right]p_X(x)\\
&=\sum_x\sum_y yp_{X,Y}(x,y)\\
&=\sum_y y\left[\sum_xp_{X,Y}(x,y)\right]=E(Y).
\end{aligned}$$

连续证明把求和替换为积分；绝对可积条件支持交换次序。

### 17.2 课件离散条件期望例题

**题目（第 107—108 页）。** $X,Y\in\{0,1\}$，联合 PMF 为 $p(x,y)=(x+y)/4$。

| $X\backslash Y$ | $0$ | $1$ | $p_X$ |
|---|---|---|---|
| $0$ | $0$ | $1/4$ | $1/4$ |
| $1$ | $1/4$ | $1/2$ | $3/4$ |

当 $X=0$ 时，$Y=1$ 的条件概率为 1，所以 $E(Y\mid X=0)=1$。当 $X=1$ 时，

$$P(Y=1\mid X=1)=\frac{1/2}{3/4}=\frac23,$$

故 $E(Y\mid X=1)=2/3$。将两个值写为 $X$ 的函数：

$$\boxed{E(Y\mid X)=1-\frac X3.}$$

再平均得

$$E[E(Y\mid X)]=1\cdot\frac14+\frac23\cdot\frac34
=\boxed{\frac34}.$$

由于边缘 $P(Y=1)=3/4$，也有 $E(Y)=3/4$，全期望验证成立。条件均值随机变量的两个值不是 $0,1$，而是 $1,2/3$。

### 17.3 条件期望是允许任意函数时的最佳预测（补充）

假设 $E(Y^2)<\infty$，令 $m(X)=E(Y\mid X)$。对任意满足平方可积要求的预测函数 $h(X)$，

$$Y-h(X)=[Y-m(X)]+[m(X)-h(X)].$$

交叉项的期望为零，因为

$$E\{[Y-m(X)][m(X)-h(X)]\}
=E\{[m(X)-h(X)]E[Y-m(X)\mid X]\}=0.$$

于是

$$\boxed{E[(Y-h(X))^2]
=E[(Y-m(X))^2]+E[(m(X)-h(X))^2].}$$

第二项非负，所以最优预测为 $h(X)=E(Y\mid X)$，最小均方误差为 $E[\operatorname{Var}(Y\mid X)]$。

这把三种预测连成一条线：无信息时最优常数为 $E(Y)$；限于仿射函数时得到第十一节的最佳线性预测；允许任意平方可积函数时得到条件期望。二元正态中，条件期望恰好为仿射函数，因此后两者一致。

### 17.4 条件均值不变仍不等于独立（补充）

使用第 14.3 小节的 $X=Z,Y=SZ$：给定 $X=x$，$Y$ 以各一半概率取 $x$ 与 $-x$，因此

$$E(Y\mid X=x)=0,\qquad E(Y\mid X)=0=E(Y).$$

但其条件方差为 $x^2$，且 $|Y|=|X|$，所以仍然依赖。条件**均值**不变只说明一个平均值不变；独立要求条件**分布**不变。

在 $X,Y$ 平方可积时，$E(Y\mid X)=E(Y)$ 可以推出不相关：

$$E(XY)=E[XE(Y\mid X)]=E(X)E(Y).$$

这也是“独立 → 条件均值不变 → 不相关”的逻辑链；一般不能把箭头倒转。

---

## 第十八节　条件方差与全方差：波动从哪里来

### 18.1 条件方差本身也是随机变量

若 $E(Y^2)<\infty$，定义

$$\boxed{\operatorname{Var}(Y\mid X)
=E\bigl([Y-E(Y\mid X)]^2\mid X\bigr).}$$

利用条件期望线性与把已知量提出，得到计算式

$$\boxed{\operatorname{Var}(Y\mid X)
=E(Y^2\mid X)-[E(Y\mid X)]^2.}$$

给定 $X=x$ 时，$\operatorname{Var}(Y\mid X=x)$ 是一个数；将 $x$ 换为 $X$，条件方差则是依赖于 $X$ 的随机变量。

### 18.2 全方差公式与代数证明

课件第 110—111 页：

$$\boxed{\operatorname{Var}(Y)
=E[\operatorname{Var}(Y\mid X)]
+\operatorname{Var}[E(Y\mid X)].}$$

第一项是**组内方差的平均**，第二项是**各组均值之间的方差**。前者先给定 $X$ 看剩余波动，再取平均；后者关注由 $X$ 带来的均值差异。

设 $m(X)=E(Y\mid X)$。分别展开：

$$E[\operatorname{Var}(Y\mid X)]=E(Y^2)-E[m(X)^2],$$

$$\operatorname{Var}[E(Y\mid X)]=E[m(X)^2]-[E(Y)]^2.$$

相加后中间项消去，恰好得到 $\operatorname{Var}(Y)$。

全方差不是 $\operatorname{Var}(Y)=\operatorname{Var}(E(Y\mid X))$，后者漏掉组内波动；也不是把两个方差都先取方差。两项的运算顺序应读成“**方差的期望＋期望的方差**”。

### 18.3 用二元正态核对

二元正态中

$$E[\operatorname{Var}(Y\mid X)]=\sigma_Y^2(1-\rho^2),$$

$$\operatorname{Var}[E(Y\mid X)]
=\operatorname{Var}\left[\mu_Y+\rho\frac{\sigma_Y}{\sigma_X}(X-\mu_X)\right]
=\rho^2\sigma_Y^2.$$

两项相加为 $\sigma_Y^2$。因此 $\rho^2$ 在此模型中是由条件均值解释的总体方差比例；这一解释依赖条件均值为线性，不能把一般非线性依赖全部归入 Pearson 相关。

条件方差不一定在每一个 $x$ 处都小于总体方差；全方差保证的是平均意义下

$$E[\operatorname{Var}(Y\mid X)]\le\operatorname{Var}(Y).$$

### 18.4 课件两阶段均匀模型

**题目（第 112—114 页）。** 先取 $X\sim U(0,1)$；观察到 $X=x$ 后，再取 $Y\mid X=x\sim U(x,1)$。求条件均值、条件方差及 $Y$ 的总体均值、方差。

**第一步：直接使用均匀分布公式。**

$$E(Y\mid X=x)=\frac{x+1}2,\qquad
\operatorname{Var}(Y\mid X=x)=\frac{(1-x)^2}{12}.$$

所以

$$\boxed{E(Y\mid X)=\frac{X+1}2,\qquad
\operatorname{Var}(Y\mid X)=\frac{(1-X)^2}{12}.}$$

**第二步：全期望。**

$$\boxed{E(Y)=\frac{E(X)+1}2=\frac34.}$$

**第三步：全方差的组内项。**

$$E[\operatorname{Var}(Y\mid X)]
=\frac1{12}\int_0^1(1-x)^2dx=\frac1{36}.$$

**第四步：全方差的组间项。**

$$\operatorname{Var}[E(Y\mid X)]
=\frac14\operatorname{Var}(X)=\frac1{48}.$$

因此

$$\boxed{\operatorname{Var}(Y)=\frac1{36}+\frac1{48}=\frac7{144}.}$$

### 18.5 为什么该模型不是“在三角形内均匀取点”（补充）

其联合密度应由条件密度乘边缘得到：

$$\boxed{f_{X,Y}(x,y)=\frac1{1-x},\qquad0<x<y<1,}$$

区域外为 0。因为给定 $x$ 后，要在长度为 $1-x$ 的区间上归一化。它虽然支持于三角形内，密度却不是常数 2。

对 $x$ 积分可以验证边缘

$$f_Y(y)=\int_0^y\frac1{1-x}dx=-\log(1-y),\qquad0<y<1.$$

因此 $Y$ 不是 $U(0,1)$，它更倾向于靠近 1。若改成三角形上密度恒为 2，则 $f_X(x)=2(1-x)$，不再符合题设 $X\sim U(0,1)$。

用条件二阶矩还能独立核对：

$$E(Y^2\mid X=x)=\frac{x^2+x+1}3,$$

$$E(Y^2)=\frac{1/3+1/2+1}3=\frac{11}{18},\qquad
\frac{11}{18}-\left(\frac34\right)^2=\frac7{144}.$$

这个例子把第三章“由条件恢复联合”与本章“由条件恢复总体矩”连在一起。

---

## 第十九节　分层模型：随机参数带来额外波动

### 19.1 课件患病率模型的两层随机性

**题目（第 115—117 页）。** 随机选择一个地区，地区患病率 $Q\sim U(0,1)$。给定 $Q=q$ 后，抽取 $n$ 个条件独立的人，患病人数满足

$$X\mid Q=q\sim\operatorname{Binomial}(n,q).$$

求 $E(X)$、$\operatorname{Var}(X)$ 与 $X$ 的边缘分布。

这是课件设定的示范模型。随机性有两层：先决定地区患病率，再决定在该患病率下的个人结果；同一次抽样中的所有人共享同一个 $Q$。

### 19.2 先写条件矩，再求总体矩

由二项分布，

$$E(X\mid Q)=nQ,\qquad\operatorname{Var}(X\mid Q)=nQ(1-Q).$$

而 $E(Q)=1/2,E(Q^2)=1/3,\operatorname{Var}(Q)=1/12$。全期望得到

$$\boxed{E(X)=nE(Q)=\frac n2.}$$

全方差则给出

$$\begin{aligned}
\operatorname{Var}(X)
&=E[nQ(1-Q)]+\operatorname{Var}(nQ)\\
&=n\left(\frac12-\frac13\right)+\frac{n^2}{12}\\
&=\boxed{\frac{n(n+2)}{12}}.
\end{aligned}$$

第一项 $n/6$ 是组内二项波动的平均，第二项 $n^2/12$ 是地区患病率差异导致的波动。

### 19.3 边缘分布：二项分布的连续混合

对 $k=0,1,\ldots,n$，按全概率积分，

$$P(X=k)=\int_0^1\binom nkq^k(1-q)^{n-k}dq.$$

使用 Beta 积分

$$\int_0^1q^k(1-q)^{n-k}dq
=B(k+1,n-k+1)=\frac{k!(n-k)!}{(n+1)!},$$

得到

$$P(X=k)=\frac{n!}{k!(n-k)!}\frac{k!(n-k)!}{(n+1)!}
=\boxed{\frac1{n+1}}.$$

所以 $X$ 在 $\{0,1,\ldots,n\}$ 上服从**离散均匀分布**，不是一般的 Binomial$(n,1/2)$。用离散均匀公式也可验证均值 $n/2$、方差 $n(n+2)/12$。

### 19.4 为什么不能直接把 $Q$ 换成 $E(Q)$（补充）

把 $Q$ 替换为 $1/2$，会得到 Binomial$(n,1/2)$，其方差为 $n/4$；而实际方差为 $n(n+2)/12$。二者之差为

$$\frac{n(n+2)}{12}-\frac n4=\frac{n(n-1)}{12},$$

当 $n>1$ 时严格为正。只在 $n=1$ 这个特殊情形，两种边缘都是 Bernoulli$(1/2)$。

用个体指示变量可以看清原因。令 $I_i$ 表示第 $i$ 人患病，$X=\sum_iI_i$。给定 $Q$ 后它们独立，但不再对 $Q$ 条件化时，

$$E(I_i)=E(Q)=\frac12,$$

$$E(I_iI_j)=E[E(I_iI_j\mid Q)]=E(Q^2)=\frac13\quad(i\ne j),$$

$$\boxed{\operatorname{Cov}(I_i,I_j)=\frac13-\frac14=\frac1{12}>0.}$$

共享的随机环境造成正相关。用完整的和方差公式核对：

$$\operatorname{Var}(X)=\frac n4+2\binom n2\frac1{12}
=\frac{n(n+2)}{12}.$$

所以“给定 $Q$ 后相互独立”不等于“总体相互独立”。这也是混合模型相较固定参数模型波动更大的具体机制。

---

## 第二十节　公式速查、解题路线与自测

### 20.1 基本数字特征速查

| 内容 | 公式 | 使用条件或注意 |
|---|---|---|
| 函数期望 | $E[g(X)]=\sum g(x)p_X(x)$ 或 $\int g(x)f_X(x)dx$ | 对应绝对期望有限；无需先求 $g(X)$ 的分布 |
| 指示变量 | $E(I_A)=P(A)$ | 计数可拆为指示变量之和 |
| 线性 | $E(\sum a_iX_i+b)=\sum a_iE(X_i)+b$ | 可积，不要求独立 |
| 独立乘积 | $E(\prod g_i(X_i))=\prod E[g_i(X_i)]$ | 相互独立，各项可积 |
| 方差 | $E(X^2)-[E(X)]^2$ | 二阶矩有限 |
| 仿射方差 | $\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$ | 标准差乘 $|a|$ |
| 协方差 | $E(XY)-E(X)E(Y)$ | 本章取二阶矩有限 |
| 相关系数 | $\rho=\operatorname{Cov}(X,Y)/(\sigma_X\sigma_Y)$ | 两个标准差正且有限 |
| 一般和方差 | $\sum a_i^2\operatorname{Var}(X_i)+2\sum_{i<j}a_ia_j\operatorname{Cov}(X_i,X_j)$ | 不要求独立 |
| 线性预测 | $\mu_Y+\operatorname{Cov}(X,Y)(X-\mu_X)/\sigma_X^2$ | $\sigma_X^2>0$，最小化纵向均方误差 |
| 条件期望 | $E(Y\mid X)=g(X),\ g(x)=E(Y\mid X=x)$ | 是随机变量 |
| 全期望 | $E[E(Y\mid X)]=E(Y)$ | $Y$ 可积 |
| 条件方差 | $E(Y^2\mid X)-[E(Y\mid X)]^2$ | $Y$ 平方可积 |
| 全方差 | $E[\operatorname{Var}(Y\mid X)]+\operatorname{Var}[E(Y\mid X)]$ | 等于总体方差 |

### 20.2 MGF 速查

| 分布 | $M_X(t)$ | 有限域 |
|---|---|---|
| 常数 $c$ | $e^{ct}$ | $\mathbb R$ |
| Bernoulli$(p)$ | $1-p+pe^t$ | $\mathbb R$ |
| Binomial$(n,p)$ | $(1-p+pe^t)^n$ | $\mathbb R$ |
| Poisson$(\lambda)$ | $e^{\lambda(e^t-1)}$ | $\mathbb R$ |
| Exp$(\lambda)$ | $\lambda/(\lambda-t)$ | $t<\lambda$ |
| Gamma$(\alpha,\lambda)$ | $[\lambda/(\lambda-t)]^\alpha$ | $t<\lambda$ |
| $\chi^2(\nu)$ | $(1-2t)^{-\nu/2}$ | $t<1/2$ |
| $N(\mu,\sigma^2)$ | $e^{\mu t+\sigma^2t^2/2}$ | $\mathbb R$ |

配套三条：

$$M_X^{(r)}(0)=E(X^r),\qquad
M_{aX+b}(t)=e^{bt}M_X(at),\qquad
M_{\sum_ka_kX_k}(t)=\prod_kM_{X_k}(a_kt)\ \text{（相互独立）}.$$

MGF 的矩公式要求在 0 邻域存在；识别分布时还要使用唯一性。

### 20.3 二元正态最应熟练的三条

在联合正态前提下：

$$aX+bY\sim N\left(a\mu_X+b\mu_Y,
a^2\sigma_X^2+b^2\sigma_Y^2+2ab\rho\sigma_X\sigma_Y\right),$$

$$X\perp Y\quad\Longleftrightarrow\quad\operatorname{Cov}(X,Y)=0,$$

$$Y\mid X=x\sim N\left(\mu_Y+\rho\frac{\sigma_Y}{\sigma_X}(x-\mu_X),
\sigma_Y^2(1-\rho^2)\right).$$

最后一个普通条件密度公式要求 $|\rho|<1$ 且两个标准差正；退化情形用构造解释。不要在“各自正态”前提下直接使用这些联合结论。

### 20.4 看到题目先选择哪条路线

**求均值或方差：** 先检查支持与有限性，判断能否直接用已知分布的矩；若是函数期望，优先 LOTUS；若是和，优先线性与完整方差公式。

**求独立和的分布：** 写 MGF → 用独立性相乘 → 整理参数 → 写有效邻域 → 用唯一性识别。若是最小值，往往生存函数更直接。

**算相关系数：** 联合分布 → 边缘 → $E(X),E(Y),E(X^2),E(Y^2),E(XY)$ → 两个方差与协方差 → 归一化。不要提前舍入，否则小协方差可能被数值误差掩盖。

**判断独立：** 普通模型用联合分解或事件概率；联合正态模型先确认联合正态，再用零协方差。零协方差通常只能证明不相关。

**给定条件分布或分层生成过程：** 先求条件矩 → 全期望、全方差。若求边缘分布，才按条件分布对混合变量求和或积分。不要把随机参数直接换成它的均值。

### 20.5 自测题（均为补充练习）

建议先遮住解析。每题除结果外，至少说明一次“为什么可以使用这条公式”。

**习题 1：存在性。** 标准柯西变量关于 0 对称，能否推出 $E(X)=0$？若某随机变量只有 $M_X(0)=1$ 已知，能否直接使用 MGF 的矩公式？

**习题 2：函数期望与仿射变换。** $X\sim U(-1,1)$，求 $E(X^2)$、$\operatorname{Var}(X^2)$、$E(3X-2)$ 与 $\operatorname{Var}(3X-2)$。

**习题 3：和的方差。** 已知 $\operatorname{Var}(X)=4$、$\operatorname{Var}(Y)=9$、$\operatorname{Cov}(X,Y)=3$。求 $\rho$、$\operatorname{Var}(2X-Y)$ 与 $\operatorname{Cov}(X+Y,X-Y)$。这些条件能否保证 $2X-Y$ 正态？

**习题 4：MGF 识别。** 相互独立的 $X\sim\operatorname{Gamma}(2,3)$、$Y\sim\operatorname{Gamma}(4,3)$ 均采用速率参数。求 $S=X+Y$ 的分布、MGF 有限域、均值和方差。

**习题 5：系数改变 MGF 有限域。** $X\sim\operatorname{Exp}(2)$，$W=1-3X$。求 $M_W(t)$、有限域、均值和方差。

**习题 6：指数和与最小值。** $X_1\sim\operatorname{Exp}(2)$、$X_2\sim\operatorname{Exp}(5)$ 独立。求 $\min(X_1,X_2)$ 的分布及均值。$X_1+X_2$ 能否直接写为同速率 Gamma？求和的均值与方差。

**习题 7：最佳线性预测。** $E(X)=1,E(Y)=2$，方差分别为 4 和 9，协方差为 3。求用 $X$ 预测 $Y$ 的最佳仿射函数与最小均方误差。它是否必等于 $E(Y\mid X)$？

**习题 8：联合正态。** 在习题 7 的数值条件之外，增加 $(X,Y)$ 联合正态。求 $Y\mid X=3$ 的分布与 $P(Y>5\mid X=3)$，并用全方差检查总体方差。

**习题 9：零相关与信息。** $Z\sim N(0,1)$，$S$ 独立于 $Z$ 且等概率取 $\pm1$，令 $X=Z,Y=SZ$。求 $E(Y\mid X)$ 与 $\operatorname{Var}(Y\mid X)$。两个边缘是否正态？二者是否独立？

**习题 10：离散条件期望。** $p(x,y)=(x+y)/4$，$x,y\in\{0,1\}$。求 $\operatorname{Var}(Y\mid X)$、$E[\operatorname{Var}(Y\mid X)]$、$\operatorname{Var}[E(Y\mid X)]$，验证全方差。

**习题 11：反向的两阶段均匀模型。** $X\sim U(0,1)$，给定 $X=x$ 后 $Y\sim U(0,x)$。求 $E(Y\mid X)$、$\operatorname{Var}(Y\mid X)$、$E(Y)$、$\operatorname{Var}(Y)$，并写联合密度。

**习题 12：分层二项。** $Q\sim U(0,1)$，$X\mid Q\sim\operatorname{Binomial}(6,Q)$。求 $E(X)$、$\operatorname{Var}(X)$ 与 $P(X=0)$；和把 $Q$ 固定为 $1/2$ 的模型比较。

### 20.6 参考解析

**1.** 均不能。柯西变量的正负部分期望都无限，有限期望不存在，主值不能代替期望；仅有 $M_X(0)=1$ 不能证明 MGF 在 0 的邻域有限。

**2.** LOTUS 给出 $E(X^2)=1/3$、$E(X^4)=1/5$，因此

$$\operatorname{Var}(X^2)=\frac15-\frac19=\frac4{45}.$$

另有 $E(X)=0,\operatorname{Var}(X)=1/3$，故 $E(3X-2)=-2$、$\operatorname{Var}(3X-2)=9/3=3$。

**3.** $\rho=3/(2\cdot3)=1/2$。由完整方差公式，

$$\operatorname{Var}(2X-Y)=4\cdot4+9-4\cdot3=13.$$

双线性给出 $\operatorname{Cov}(X+Y,X-Y)=4-9=-5$。这些矩条件没有说明分布族，不能保证线性组合正态。

**4.**

$$M_S(t)=\left(\frac3{3-t}\right)^2\left(\frac3{3-t}\right)^4
=\left(\frac3{3-t}\right)^6,\qquad t<3.$$

由唯一性 $S\sim\operatorname{Gamma}(6,3)$，均值为 $6/3=2$，方差为 $6/9=2/3$。独立与同速率是关键。

**5.**

$$M_W(t)=e^tM_X(-3t)=\frac{2e^t}{2+3t},\qquad -3t<2\Longleftrightarrow t>-\frac23.$$

负系数使有限域方向翻转。$E(W)=1-3/2=-1/2$，$\operatorname{Var}(W)=9/4$。

**6.** 最小值为 Exp$(7)$，均值为 $1/7$。和的两个速率不同，不能用同速率 Gamma 可加性；其 MGF 为 $[2/(2-t)][5/(5-t)]$，并不具有单一 Gamma 的形式。由独立性，和的均值为 $1/2+1/5=7/10$，方差为 $1/4+1/25=29/100$。

**7.**

$$\widehat Y=2+\frac34(X-1)=\frac54+\frac34X,$$

$$\operatorname{MSE}_{\min}=9-\frac{3^2}4=\frac{27}4.$$

不必等于 $E(Y\mid X)$；还需要条件均值为仿射函数的条件，联合正态是保证它成立的一种情形。

**8.** 这里 $\rho=1/2$，所以 $Y\mid X=3\sim N(7/2,27/4)$，所求概率为 $1-\Phi(1/\sqrt3)\approx0.2819$。全方差的组内项为 $27/4$，组间项为 $(3/4)^2\cdot4=9/4$，相加为 9。

**9.** 给定 $X=x$ 后 $Y$ 等概率取 $x,-x$，故 $E(Y\mid X)=0$、$\operatorname{Var}(Y\mid X)=X^2$。两个边缘均为标准正态，但 $|X|=|Y|$，因此依赖，也非联合正态。全方差核对为 $E(X^2)+0=1$。

**10.** 已知 $E(Y\mid X)=1-X/3$。当 $X=0$ 时 $Y$ 为常数，条件方差为 0；当 $X=1$ 时 $Y\sim\operatorname{Bernoulli}(2/3)$，条件方差为 $2/9$。故

$$\operatorname{Var}(Y\mid X)=\frac{2X}9,\qquad
E[\operatorname{Var}(Y\mid X)]=\frac29\frac34=\frac16.$$

因 $X\sim\operatorname{Bernoulli}(3/4)$，

$$\operatorname{Var}[E(Y\mid X)]=\frac19\frac34\frac14=\frac1{48}.$$

两项和为 $1/6+1/48=3/16$，与边缘 Bernoulli$(3/4)$ 的方差一致。

**11.**

$$E(Y\mid X)=\frac X2,\qquad\operatorname{Var}(Y\mid X)=\frac{X^2}{12}.$$

因此 $E(Y)=1/4$，组内项为 $E(X^2)/12=1/36$，组间项为 $\operatorname{Var}(X)/4=1/48$，故 $\operatorname{Var}(Y)=7/144$。联合密度为 $1/x$，$0<y<x<1$，区域外为 0。不是三角形上的常数密度。

**12.** $X$ 在 $\{0,1,\ldots,6\}$ 上离散均匀，所以 $E(X)=3$、$\operatorname{Var}(X)=6\cdot8/12=4$、$P(X=0)=1/7$。固定 $Q=1/2$ 时 $X\sim\operatorname{Binomial}(6,1/2)$，均值仍为 3，但方差为 $3/2$，$P(X=0)=1/64$。随机环境同时改变总体方差和完整分布。

---

## 附录 A　高频错误与修正

| 常见错误 | 正确做法 |
|---|---|
| 分布对称就写期望等于中心 | 先验证绝对可积；柯西是典型反例 |
| 为求 $E[g(X)]$ 先机械地求 $g(X)$ 的密度 | 优先用 LOTUS |
| 写 $E[g(X)]=g(E(X))$ | 一般不成立，线性函数等特殊情形除外 |
| 期望相加时额外要求独立 | 有限和只要求各项可积 |
| 乘积期望随意分解 | 先确认独立或另有直接证明 |
| 把 $E(X^2)$ 当方差 | 还要减去 $[E(X)]^2$ |
| 缩放后的方差只乘 $a$ | 方差乘 $a^2$，标准差乘 $|a|$ |
| 差的方差等于方差之差 | 用 $\sigma_X^2+\sigma_Y^2-2\operatorname{Cov}(X,Y)$ |
| MGF 二阶导数直接等于方差 | 它等于二阶原点矩 |
| $M_X(0)=1$ 就认为可以求任意阶矩 | 确认 MGF 在 0 的一个双侧开邻域有限 |
| 改变变量系数后沿用原 MGF 有限域 | 检查 $at$ 的取值条件，负系数会翻转不等号 |
| 不同 $p$ 的二项和直接合并 | 同一个 $p$ 才能用对应可加性 |
| 不同速率 Gamma 之和直接合并 | 对应可加性要求同速率 |
| 指数和与指数最小值混淆 | 同速率和为 Gamma，独立最小值为速率和的指数 |
| 相关系数接近零就判“几乎独立” | 它只说明线性相关弱，非线性依赖可能很强 |
| 相关系数为 1 就说明两个变量相等 | 是正斜率仿射关系，斜率与截距不一定为 1、0 |
| 两个边缘正态就用零相关推出独立 | 必须先确认联合正态 |
| 和与差零协方差后直接判独立 | 加上它们联合正态等足够条件 |
| 认为 $\rho=\pm1$ 可直接代入二维密度 | 分布退化到直线，使用构造 |
| 条件正态概率仍用原边缘均值和标准差 | 先求条件均值与条件方差，再标准化 |
| 把 $E(Y\mid X)$ 当成单一确定数 | 它是 $X$ 的函数；给定 $X=x$ 后才是数 |
| 全期望对组均值等权平均 | 使用条件变量各组的实际概率或密度 |
| 全方差只保留条件方差平均 | 还要加条件均值的方差 |
| 条件均值恒定就判独立 | 条件分布可能仍改变，比如条件方差随 $X$ 变化 |
| 两阶段均匀抽样等同于区域上均匀 | 用 $f_{X,Y}=f_{Y\mid X}f_X$ 检查密度 |
| 条件独立就认为总体独立 | 共享随机参数可能造成总体依赖 |

## 附录 B　课件核对与阅读注意

本讲义按提取文字与页面图像核对。当前课件已经在多处明确补充可积性、几何支持、速率参数与联合正态条件；这些是正确前提，应保留，不应当作课件错误。

| PDF 页码 | 阅读时要注意的情况 | 本文处理 |
|---|---|---|
| 全篇 | 页脚显示总页数为 123，文件实际为 120 页 | 一律引用物理页码，不据页脚推断缺失内容 |
| 4、6、11、52 | 有限期望、方差、协方差各有有限性前提 | 各定理处明确标注，区分无限扩展期望与不存在 |
| 13—15 | Geometric 的支持从 1 开始 | 统一用首次成功的试验次数，补充从 0 开始时均值的变化 |
| 18 | $t$ 分布均值、方差只在部分自由度下成立 | 分别保留 $\nu>1$、$\nu>2$ 的条件 |
| 21—24 | $M(0)=1$ 是必要性质，真正前提是 0 邻域有限 | 不把所有矩有限与 MGF 存在混为一谈 |
| 30、89 | 使用一元及多元变换唯一性定理 | 说明其为课件引用的定理，避免把未证结论冒充初等代数证明 |
| 39—40 | 求和项数与二项参数同时使用 $n,n_k$ | 用 $m$ 表示求和项数，保留每项参数 $n_k$ |
| 45—49 | 同速率 Gamma 和与不同速率指数最小值的条件不同 | 分别陈述与推导 |
| 56—59 | 相关界与含 $\rho$ 的误差公式有正方差条件 | 分离常数变量情形，避免除以零 |
| 73—74 | “同时偏高”没有给出具体阈值 | 解释需要联合模型，并用符号阈值给公式，不虚构数值答案 |
| 76—93 | 构造允许 $|\rho|=1$，普通二维密度则不允许 | 区分非退化密度与退化点线分布 |
| 90—91 | 正态边缘不足以推出联合正态 | 完整保留随机符号反例，另用和带点质量核对 |
| 102—104 | 给定具体值的条件期望与条件期望随机变量是不同对象 | 单独解释 $g(x)$ 与 $g(X)$，保留几乎必然意义 |
| 112—117 | 两阶段均匀与随机参数二项均为条件生成模型 | 避免误用均匀区域密度或把随机参数直接替成平均值 |

课件编号从习题 4.1 跳到 4.4，并有例 4.8、例 4.10 等编号；本文保留原编号，不据此虚构文件中未出现的例题。

## 附录 C　复习顺序与达标要求

**第一轮：掌握均值与波动。** 阅读第一至四节，能说明期望为何要检查绝对可积，能用指示变量和函数期望简化问题，能独立推导五个基础分布的均值方差。

**第二轮：用 MGF 识别分布。** 阅读第五至七节，重做 Poisson、指数与正态的 MGF，能在证明中写出独立性、有限域与唯一性三个依据，理解同参数可加性。

**第三轮：区分线性关系与依赖。** 阅读第八至十一节，自己重算例 4.8；能够给出“不相关但依赖”的具体反例，能从均方误差推导最佳线性预测。

**第四轮：掌握联合正态。** 阅读第十二至十五节，先记构造，再由换元重建密度；掌握组合分布、零协方差与独立、条件分布三类题，并能识别退化边界。

**第五轮：用信息分解平均与波动。** 阅读第十六至十九节，先分清 $E(Y\mid X=x)$ 与 $E(Y\mid X)$，再独立完成离散条件期望、两阶段均匀、分层二项三类模型，能解释全方差的两个来源。

最终达标标准是：看到问题，能判断需要完整分布、几个矩、线性预测还是条件模型；写出公式时能同时说明其前提，而不是仅凭符号相似就套用。


