# Math1212 概率论与数理统计 I (Probability and Statistics I)

## 第五章：不等式、随机变量收敛与大数定律——全景精要与深度解析笔记

> **课件来源**：`Week8_1.pdf`，共 45 个实际 PDF 页面，页脚总页数标为 86。本文件只整理所提供的 1—45 页，不能据此推断后续页面的内容。
> **编排方式**：参照 chapter 4，以知识点及逻辑联系组织；采用中英标题、分级编号、定义与定理引用块、详细证明、案例解析、概念辨析、公式速查及自测题。
> **内容边界**：目录包含 5.4 中心极限定理及 5.5 Delta 方法，但本 PDF 正文止于大数定律的方差判据。涉及中心极限定理的公式只在收敛应用中简要出现。下文标为“深度补充”的证明、反例与应用是辅助理解，不代表课件已完整讲授。
> **参考教材（课件第 2 页）**：Hogg、Tanis、Zimmerman，*Probability and Statistical Inference*，第 9/10 版，5.6—5.9 节；魏宗舒等，《概率论与数理统计教程》第三版，3.5、4.1—4.4 节。

---

## 目录与知识架构

1. 从数字特征走向概率极限 (Motivation & Notation)
2. Markov 与 Chebyshev 不等式 (Probability Inequalities)
3. 概率界的完整案例与样本量应用 (Bounds & Applications)
4. 三种随机变量收敛 (Modes of Convergence)
5. 收敛之间的关系与反例 (Implications & Counterexamples)
6. 连续映射、运算规则与 Slutsky 定理 (Limit Tools)
7. 弱大数定律及其证明 (Weak Laws of Large Numbers)
8. 大数定律的应用、边界及与 CLT 的联系 (Applications & Scope)
9. 公式速查、解题路线与易错辨析 (Summary & Pitfalls)
10. 自测题与完整答案 (Practice & Solutions)

本课件的推导主线是：

$$\text{有限矩}\longrightarrow\text{概率上界}\longrightarrow\text{误差概率趋于零}\longrightarrow\text{依概率收敛}\longrightarrow\text{平均值的一致性}.$$

另一条应用主线是：

$$\text{已有极限}\xrightarrow{\text{连续映射、Slutsky}}\text{新统计量的极限}.$$

---

## 1. 从数字特征走向概率极限 (Motivation & Notation)

### 1.1 本章解决什么问题？

第四章研究均值、方差等数字特征。本章进一步问：

1. 只知道均值或方差，能否控制某个事件的概率？
2. 为什么反复观测后的平均值能估计总体均值？
3. “随机变量越来越接近”究竟如何定义？
4. 已知一个统计量收敛，取平方、倒数或替换未知参数后，是否仍收敛？

前两个问题由概率不等式和大数定律连接起来；第三、四个问题由收敛概念与极限定理工具解决。

### 1.2 统一记号与存在条件

$$\bar X_n=\frac1n\sum_{i=1}^nX_i,\qquad \mu=E(X_1),\qquad \sigma^2=\operatorname{Var}(X_1).$$

- $\bar X_n$ 是前 $n$ 次观测的平均值，$X_n$ 是第 $n$ 次观测；二者不能混淆。
- i.i.d. 表示相互独立且同分布。
- 有限均值指 $E|X|<\infty$；有限方差指 $E(X^2)<\infty$。
- 正态分布写作 $N(\mu,\sigma^2)$，第二个参数为方差。
- $\Phi$ 为标准正态 CDF；$z_q=\Phi^{-1}(q)$。
- $\xrightarrow{d}$ 表示极限分布；$\approx$ 表示有限样本近似。二者表达的结论不同。

### 1.3 三种概率计算结论

| 类型 | 例子 | 能说明什么 |
|---|---|---|
| 精确值 | $P(|Z|\ge2)=2[1-\Phi(2)]$ | 给定分布下真实概率 |
| 严格界 | $P(|X-\mu|\ge2\sigma)\le1/4$ | 概率不会超过该值 |
| 渐近结论 | $\bar X_n\xrightarrow p\mu$ | 固定误差阈值下，误差概率趋于零 |

概率上界不等于真实概率；渐近收敛也不自动提供给定 $n$ 的误差数值。

---

## 2. Markov 与 Chebyshev 不等式 (Probability Inequalities)

对应课件第 7—11 页。

### 2.1 Markov 不等式：非负变量的右尾界

> **定理 5.1（Markov's Inequality）**：若 $X\ge0$ a.s.，且 $E(X)<\infty$，则对每个 $a>0$，
> $$\boxed{P(X\ge a)\le\frac{E(X)}a.}$$
> 考虑概率本身不超过 1，也可写成 $\min\{1,E(X)/a\}$。

**直观解释**：每当 $X\ge a$，就至少给总体期望贡献 $a$。如果这种事件频繁发生，期望就不可能很小。

**证明**：逐点有

$$X\ge a\mathbf1_{\{X\ge a\}}.$$

因为事件内右边为 $a\le X$，事件外右边为零，而 $X\ge0$。取期望：

$$E(X)\ge aE[\mathbf1_{\{X\ge a\}}]=aP(X\ge a).$$

除以正数 $a$ 即得结论。示性变量证明同时适用于离散、连续和混合分布。

> **【条件辨析】** 非负性是核心条件。若 $P(X=1)=P(X=-1)=1/2$，则 $E(X)=0$，但 $P(X\ge1)=1/2$；直接使用 Markov 将得到错误上界 0。负值会抵消正值的期望贡献。

### 2.2 深度补充：对非负变换使用 Markov

一般变量 $X$ 不一定非负，但 $|X|^r$ 非负。若 $r>0$ 且 $E|X|^r<\infty$，则

$$\boxed{P(|X|\ge a)\le\frac{E|X|^r}{a^r}},\qquad a>0.$$

证明只需把事件改写为 $\{|X|^r\ge a^r\}$。因此，Markov 的真正用途常常是先选择恰当的非负随机变量，再应用不等式。

### 2.3 Chebyshev 不等式：围绕均值的双侧界

> **推论 5.2（Chebyshev's Inequality）**：若 $E(X)=\mu$、$\operatorname{Var}(X)=\sigma^2<\infty$，则对每个 $a>0$，
> $$\boxed{P(|X-\mu|\ge a)\le\frac{\sigma^2}{a^2}.}$$

**证明**：令 $Y=(X-\mu)^2\ge0$，则 $E(Y)=\sigma^2$，所以

$$P(|X-\mu|\ge a)=P(Y\ge a^2)\le\frac{E(Y)}{a^2}=\frac{\sigma^2}{a^2}.$$

这说明 Chebyshev 是 Markov 用于“平方偏差”的结果，而不是完全独立的一条技巧。

若 $\sigma>0$，令 $a=k\sigma$：

$$\boxed{P(|X-\mu|\ge k\sigma)\le\frac1{k^2}},\qquad k>0.$$

取补集得到

$$\boxed{P(|X-\mu|<k\sigma)\ge1-\frac1{k^2}}.$$

注意 $\{|X-\mu|\ge a\}$ 的补集是 $\{|X-\mu|<a\}$。对于有原子的离散分布，不能随意交换严格和非严格端点。若 $k\le1$，下界可能非正，此时只给出平凡信息；若 $\sigma=0$，则 $X=\mu$ a.s.，不要再除以 $\sigma$。

### 2.4 深度补充：为什么普适概率界可能很松？

Chebyshev 对所有有限方差分布同时有效，无法利用正态性、对称性或具体尾部形状。它牺牲了对特定分布的精度，换来普适性。

但“普遍有效”并不意味着“永远不精确”。对固定 $k\ge1$，令

$$P(X=\mu-k\sigma)=P(X=\mu+k\sigma)=\frac1{2k^2},$$
$$P(X=\mu)=1-\frac1{k^2},\qquad \sigma>0.$$

容易核实 $E(X)=\mu$、$\operatorname{Var}(X)=\sigma^2$，并且

$$P(|X-\mu|\ge k\sigma)=\frac1{k^2}.$$

因此仅知道均值与方差时，不能对所有分布都把这个界改小。

---

## 3. 概率界的完整案例与样本量应用 (Bounds & Applications)

### 3.1 例 5.1：由均值和方差估计概率

对应第 12—13 页。已知 $E(X)=25$、$\operatorname{Var}(X)=16$，所以 $\sigma=4$。

**问题一：求 $P(17<X<33)$ 的下界。**

先写成以均值为中心的区间：

$$\{17<X<33\}=\{|X-25|<8\}=\{|X-25|<2\sigma\}.$$

因此

$$\boxed{P(17<X<33)\ge1-\frac{16}{8^2}=\frac34.}$$

**问题二：求 $P(|X-25|\ge12)$ 的上界。**

$$\boxed{P(|X-25|\ge12)\le\frac{16}{12^2}=\frac19.}$$

不能把以上不等号写成等号，也不能因为只知道两个数字特征，就擅自把 $X$ 当作正态变量。

### 3.2 例 5.2：二项比例集中在成功概率附近

对应第 14—15 页。设 $Y\sim\operatorname{Bin}(n,p)$，样本成功比例为 $\hat p=Y/n$。由第四章公式：

$$E(\hat p)=p,\qquad \operatorname{Var}(\hat p)=\frac{p(1-p)}n.$$

所以对固定 $\varepsilon>0$，

$$\boxed{P(|\hat p-p|\ge\varepsilon)\le\frac{p(1-p)}{n\varepsilon^2}\le\frac1{4n\varepsilon^2}.}$$

最后一步来自 $p(1-p)=1/4-(p-1/2)^2\le1/4$。若右端大于 1，应再与 1 取最小值。

**核心含义**：随着 $n$ 增大，偏差超过任意固定容许值的概率趋于零。这是从一个具体比例模型走向依概率收敛的桥梁。

### 3.3 深度补充：反推保守样本量

希望确保

$$P(|\hat p-p|<\varepsilon)\ge1-\alpha,\qquad 0<\alpha<1.$$

只需使上界不超过 $\alpha$，即

$$\boxed{n\ge\frac1{4\alpha\varepsilon^2}.}$$

例如容许误差 $0.05$、要求概率至少 $0.95$，取 $\alpha=0.05$，得到 $n\ge2000$。

这是对未知 $p$ 统一有效的**充分样本量**。它不是实际所需的最小样本量；使用具体分布信息通常能得到更精细的计算。

### 3.4 例 5.3：正态精确尾概率与 Chebyshev 界

对应第 16—17 页。若 $Z\sim N(0,1)$，由对称性：

$$P(|Z|\ge k)=2[1-\Phi(k)].$$

| $k$ | 精确正态尾概率（近似值） | Chebyshev 上界 |
|---:|---:|---:|
| 1 | 0.31731 | 1 |
| 2 | 0.04550 | 0.25 |
| 3 | 0.00270 | 0.11111 |

课件第 17 页明确指出，原先的说法 $P(|Z|\ge2)<0.04$ 是错误的；真实值约为 $0.04550$。

**复习意义**：已知正态分布且要求数值概率时，优先标准化并查 $\Phi$；只知道方差或要证明收敛时，Chebyshev 往往更方便。

### 3.5 例 5.4：独立标准正态变量的平均值

对应第 18—19 页。若 $Z_1,Z_2,\ldots$ 相互独立且均为 $N(0,1)$，则由独立正态线性组合性质，

$$\boxed{\bar Z_n\sim N(0,1/n).}$$

标准化时除以的是标准差 $1/\sqrt n$：

$$P(|\bar Z_n|\ge1)=P(|\sqrt n\bar Z_n|\ge\sqrt n)=\boxed{2[1-\Phi(\sqrt n)]}.$$

Chebyshev 则给出

$$\boxed{P(|\bar Z_n|\ge1)\le1/n.}$$

二者都趋于零；正态精确尾概率衰减更快。这里平均值对每个 $n$ 都精确服从正态分布，所用的是第四章正态可加性，不需要先使用中心极限定理。

---

## 4. 三种随机变量收敛 (Modes of Convergence)

对应课件第 21—30 页。

### 4.1 依概率收敛 (Convergence in Probability)

> **定义**：若对每个 $\varepsilon>0$，都有
> $$P(|X_n-X|>\varepsilon)\longrightarrow0,$$
> 则称 $X_n$ 依概率收敛到 $X$，记作 $X_n\xrightarrow pX$。

等价地，对每个 $\varepsilon>0$，$P(|X_n-X|\le\varepsilon)\to1$。定义中把 $>$ 换成 $\ge$ 也等价，因为它要求对**所有正阈值**成立；例如 $P(|X_n-X|\ge\varepsilon)\le P(|X_n-X|>\varepsilon/2)$。

**直观解释**：选定一个容许误差，样本量足够大时，超出它的概率很小。它没有要求误差在每条样本路径上单调减少。

**课件例子**：

$$T_n=\theta+\frac{Z_n}{\sqrt n},\qquad E(Z_n)=0,\quad\operatorname{Var}(Z_n)=1.$$

因此

$$P(|T_n-\theta|>\varepsilon)\le\frac1{n\varepsilon^2}\to0,$$

即 $\boxed{T_n\xrightarrow p\theta}$。这里不要求 $Z_n$ 正态，也不要求各个 $Z_n$ 彼此独立。

> **一致性 (Consistency)**：估计量 $T_n$ 若满足 $T_n\xrightarrow p\theta$，称其为 $\theta$ 的一致估计量。一致性控制大样本误差概率；无偏性 $E(T_n)=\theta$ 控制平均偏差，两者不等价。

### 4.2 依分布收敛 (Convergence in Distribution)

> **定义**：设 $F_n,F$ 分别为 $X_n,X$ 的 CDF。若在 $F$ 的每个连续点 $x$ 上，
> $$F_n(x)\longrightarrow F(x),$$
> 则记为 $X_n\xrightarrow dX$。

它比较的是分布，不要求 $X_n$ 与 $X$ 在同一个随机结果下取值接近，甚至不要求定义在同一概率空间。

**课件例子**：若 $X_n\sim N(0,1+1/n)$，则

$$F_n(x)=\Phi\!\left(\frac{x}{\sqrt{1+1/n}}\right)\longrightarrow\Phi(x),$$

所以 $X_n\xrightarrow dN(0,1)$。

**为什么只要求连续点？深度补充。** 取 $X_n=1/n$、$X=0$，显然确定性取值趋于零。然而 $F_n(0)=0$，$F(0)=1$。极限 CDF 在零点跳跃，这不妨碍依分布收敛。要求所有点收敛会错误排除这个最简单的例子。

### 4.3 几乎必然收敛 (Almost Sure Convergence)

> **定义**：若
> $$P\bigl(\{\omega:X_n(\omega)\to X(\omega)\}\bigr)=1,$$
> 则记作 $X_n\xrightarrow{a.s.}X$。

固定一个随机结果 $\omega$ 后，就得到一条数列 $X_1(\omega),X_2(\omega),\ldots$。几乎必然收敛要求这些数列在一个共同的概率 1 集合上收敛。

**课件例子**：设同一个 $U\sim U(0,1)$，令 $X_n=U^n$。只要 $0\le U<1$，就有 $U^n\to0$；端点 $U=1$ 的概率为零，故

$$\boxed{U^n\xrightarrow{a.s.}0.}$$

要注意这里各项共享同一个 $U$。若每个 $n$ 都重新生成变量，就改变了随机序列的联合结构，不能照搬这条逐路径论证。

### 4.4 用量词理解二者的差别

依概率收敛关心“第 $n$ 次误差大的概率”是否趋于零。几乎必然收敛关心“对几乎每一条路径，误差是否最终一直小下去”。

| 模式 | 比较对象 | 核心问题 |
|---|---|---|
| 依概率 | 同一空间中的误差 $|X_n-X|$ | 某个大 $n$ 时，大误差有多可能？ |
| 几乎必然 | 整条无限样本路径 | 大误差会不会沿路径无穷次出现？ |
| 依分布 | CDF | 分布形状是否趋于目标分布？ |

---

## 5. 收敛之间的关系与反例 (Implications & Counterexamples)

### 5.1 定理 5.6：强弱关系

对应第 28—33 页。

$$\boxed{X_n\xrightarrow{a.s.}X\ \Longrightarrow\ X_n\xrightarrow pX\ \Longrightarrow\ X_n\xrightarrow dX.}$$

一般不能反向推导；但常数极限有特殊性质：

$$\boxed{X_n\xrightarrow dc\iff X_n\xrightarrow pc,\qquad c\text{ 为常数}.}$$

### 5.2 深度补充：依概率收敛为什么推出依分布收敛？

对任意 $\delta>0$，利用事件包含关系：

$$P(X\le x-\delta)-P(|X_n-X|>\delta)\le F_n(x)$$
$$\le P(X\le x+\delta)+P(|X_n-X|>\delta).$$

先令 $n\to\infty$，误差概率趋于零；再令 $\delta\downarrow0$。若 $F$ 在 $x$ 连续，两侧都趋于 $F(x)$，故 $F_n(x)\to F(x)$。

这也说明定义中“极限 CDF 的连续点”为何自然出现。

### 5.3 深度补充：几乎必然收敛为什么推出依概率收敛？

固定 $\varepsilon>0$，记

$$A_m=\bigcup_{n\ge m}\{|X_n-X|>\varepsilon\}.$$

集合 $A_m$ 随 $m$ 递减，其交集表示“大于 $\varepsilon$ 的误差发生无穷多次”。几乎必然收敛保证该交集概率为零，因此由概率对递减集合的连续性，$P(A_m)\downarrow0$。而 $P(|X_m-X|>\varepsilon)\le P(A_m)$，结论成立。

### 5.4 课件反例：依分布不推出依概率

设 $X\sim N(0,1)$，令每个 $X_n=-X$。对称性保证 $X_n$ 与 $X$ 同分布，所以 $F_n=F$，从而

$$X_n\xrightarrow dX.$$

但对任意 $\varepsilon>0$，

$$P(|X_n-X|>\varepsilon)=P(2|X|>\varepsilon)=P(|X|>\varepsilon/2)>0,$$

其值不随 $n$ 改变，故不依概率收敛到 $X$。

这个序列事实上几乎必然收敛到 $-X$。矛盾并不存在：依概率极限比较随机变量本身，依分布极限只识别它的分布。

### 5.5 深度补充：依概率不推出几乎必然的完整反例

令 $U\sim U([0,1))$。把所有二进区间逐层排列：

$$X_{2^k+j}=\mathbf1_{\{j/2^k\le U<(j+1)/2^k\}},\qquad k=0,1,\ldots,\quad j=0,\ldots,2^k-1.$$

第 $k$ 层共有 $2^k$ 项，每一项取 1 的概率为 $2^{-k}$。当 $n\to\infty$，相应的层数 $k\to\infty$，所以对 $0<\varepsilon<1$，

$$P(|X_n|>\varepsilon)=2^{-k}\to0.$$

故 $X_n\xrightarrow p0$。但对每个 $U\in[0,1)$，每层恰有一项为 1，从第二层起每层也有取 0 的项。沿每条路径都出现无穷多个 1 和无穷多个 0，因此路径不收敛。

它体现的正是：单次错误越来越罕见，错误仍可能沿无限序列不断出现。

### 5.6 深度补充：常数极限为何特殊？

若 $X_n\xrightarrow dc$，固定 $\varepsilon>0$，取 $\delta=\varepsilon/2$。常数分布在 $c-\delta,c+\delta$ 连续，因此

$$P(|X_n-c|>\varepsilon)\le F_n(c-\delta)+1-F_n(c+\delta)\to0.$$

常数分布的所有质量集中在一点，分布接近它就迫使随机取值以高概率接近该点；非退化极限没有这个性质。

---

## 6. 连续映射、运算规则与 Slutsky 定理 (Limit Tools)

对应第 34—38 页。课件将连续映射与 Slutsky 都标为 Theorem 5.7，复习时按定理名称区分。

### 6.1 连续映射定理 (Continuous Mapping Theorem)

> 若 $X_n\xrightarrow pX$，且 $g$ 在 $X$ 几乎必然取到的位置连续，则
> $$g(X_n)\xrightarrow pg(X).$$
> 若 $X_n\xrightarrow dX$，在同样连续性条件下，
> $$g(X_n)\xrightarrow dg(X).$$

例如，若 $X_n\xrightarrow p\mu$，则 $X_n^2\xrightarrow p\mu^2$、$e^{X_n}\xrightarrow pe^\mu$。若 $\mu\ne0$，还可得到 $1/X_n\xrightarrow p1/\mu$，前提是比值有定义，或在趋于零概率的未定义事件上作任意扩展。

**深度补充：不连续处不能直接使用。** 令确定性 $X_n=1/n\to0$，而 $g(x)=\mathbf1_{\{x>0\}}$。则 $g(X_n)=1$，但 $g(0)=0$。由于 $g$ 在极限点不连续，不能套用定理。

### 6.2 依概率收敛的四则运算

若 $X_n\xrightarrow pX$、$Y_n\xrightarrow pY$，则

$$X_n+Y_n\xrightarrow pX+Y,\qquad X_nY_n\xrightarrow pXY.$$

若 $P(Y=0)=0$，比值在有定义或适当扩展后也有 $X_n/Y_n\xrightarrow pX/Y$。

这里不要求 $X_n,Y_n$ 独立。和的结论可由

$$P(|(X_n+Y_n)-(X+Y)|>\varepsilon)$$
$$\le P(|X_n-X|>\varepsilon/2)+P(|Y_n-Y|>\varepsilon/2)\to0$$

直接证明；乘积则还需要控制变量取值过大的事件，不能把它当成和的同一条估计。

### 6.3 Slutsky 定理：把收敛到常数的量代入极限分布

> 若 $X_n\xrightarrow dX$、$Y_n\xrightarrow pc$，其中 $c$ 为常数，则
> $$X_n+Y_n\xrightarrow dX+c,\qquad X_nY_n\xrightarrow dcX.$$
> 若 $c\ne0$，则 $X_n/Y_n\xrightarrow dX/c$，并注意比值的定义。

**关键条件**：一个量有分布极限，另一个量依概率趋于常数。二者之间无需独立。

### 6.4 课件应用：用一致估计替换未知标准差

假设已经证明

$$\frac{\sqrt n(\hat\theta_n-\theta)}\sigma\xrightarrow dN(0,1),\qquad S_n\xrightarrow p\sigma>0.$$

则 $\sigma/S_n\xrightarrow p1$，于是

$$\frac{\sqrt n(\hat\theta_n-\theta)}{S_n}=\frac{\sqrt n(\hat\theta_n-\theta)}\sigma\frac\sigma{S_n}\xrightarrow dN(0,1).$$

这个结果说明为何大样本推断常可以用估计的标准差代替未知真值；它不意味着替换后的统计量在有限样本下精确服从标准正态分布。

### 6.5 警告：边缘依分布收敛不保证和的极限

单独知道 $X_n\xrightarrow dX$、$Y_n\xrightarrow dY$，不能直接写出 $X_n+Y_n\xrightarrow dX+Y$。还需要正确的联合收敛信息。

课件例子令 $Z\sim N(0,1)$，$X_n=Z$、$Y_n=-Z$。两个边缘分布始终为标准正态，但和恒为零。因此不能把它们擅自当成两个独立标准正态变量，其和应为 $N(0,2)$。

**更精确地说**：如果目标对是 $(Z,-Z)$，和的目标就是零；如果目标对是两个独立标准正态，和的目标是 $N(0,2)$。相同的两个边缘分布，没有指定相同的联合关系。

---

## 7. 弱大数定律及其证明 (Weak Laws of Large Numbers)

对应第 39—45 页。

### 7.1 样本均值为何越来越稳定？

若 $X_i$ i.i.d.，且 $E(X_i)=\mu$、$\operatorname{Var}(X_i)=\sigma^2<\infty$，则

$$E(\bar X_n)=\frac1n\sum_{i=1}^nE(X_i)=\mu,$$

$$\operatorname{Var}(\bar X_n)=\frac1{n^2}\sum_{i=1}^n\operatorname{Var}(X_i)=\frac{\sigma^2}n.$$

第一式仅使用期望线性性；第二式还使用独立性使交叉协方差为零。随着 $n$ 增大，均值不变、波动收缩。

### 7.2 定理 5.3：i.i.d. 弱大数定律

> 设 $X_1,X_2,\ldots$ i.i.d.，有有限均值 $\mu$ 和有限方差 $\sigma^2$，则
> $$\boxed{\bar X_n\xrightarrow p\mu.}$$

**完整证明**：对任意固定 $\varepsilon>0$，由 Chebyshev，

$$0\le P(|\bar X_n-\mu|\ge\varepsilon)\le\frac{\operatorname{Var}(\bar X_n)}{\varepsilon^2}=\frac{\sigma^2}{n\varepsilon^2}\to0.$$

根据依概率收敛定义，结论成立。

课件同时说明：i.i.d. 弱大数定律在更弱条件 $E|X_1|<\infty$ 下也成立；有限方差便于使用这里的简短证明。不能把“此证明需要有限方差”误读为“大数定律成立必须有有限方差”。

### 7.3 定理 5.4：独立、不必同分布的 Chebyshev 大数定律

> 设 $X_i$ 相互独立，$E(X_i)=\mu_i$，且存在与 $i$ 无关的有限常数 $C$，使 $\operatorname{Var}(X_i)\le C$。则
> $$\boxed{\frac1n\sum_{i=1}^n(X_i-\mu_i)\xrightarrow p0.}$$

**证明**：令 $T_n=n^{-1}\sum_i(X_i-\mu_i)$，则 $E(T_n)=0$，且

$$\operatorname{Var}(T_n)=\frac1{n^2}\sum_{i=1}^n\operatorname{Var}(X_i)\le\frac Cn.$$

所以 $P(|T_n|>\varepsilon)\le C/(n\varepsilon^2)\to0$。

**结论应如何读？**

$$\bar X_n-\frac1n\sum_{i=1}^n\mu_i\xrightarrow p0.$$

平均值接近的是“各自均值的平均”，这个中心本身可能随 $n$ 变化。只有进一步知道 $n^{-1}\sum_i\mu_i\to\mu$，才能推得 $\bar X_n\xrightarrow p\mu$。

### 7.4 定理 5.5：一般方差判据

> 设各 $X_i$ 有有限二阶矩。若
> $$\boxed{\frac1{n^2}\operatorname{Var}\!\left(\sum_{i=1}^nX_i\right)\longrightarrow0,}$$
> 则
> $$\boxed{\frac1n\sum_{i=1}^n(X_i-E X_i)\xrightarrow p0.}$$

课件说明该结果在来源课件中称为 “Markov's LLN”。为避免名称差异，复习时优先记住方差条件及结论。

**证明（补齐第 45 页的推导）**：令 $T_n=n^{-1}\sum_i(X_i-E X_i)$，有 $E(T_n)=0$，

$$P(|T_n|>\varepsilon)\le\frac{\operatorname{Var}(T_n)}{\varepsilon^2}=\frac{\operatorname{Var}(\sum_iX_i)}{n^2\varepsilon^2}\to0.$$

它不要求独立或同分布。真正起作用的是总和的方差相对于 $n^2$ 足够小。

### 7.5 深度补充：协方差决定依赖是否妨碍平均

总和方差的完整展开为

$$\operatorname{Var}\!\left(\sum_{i=1}^nX_i\right)=\sum_{i=1}^n\operatorname{Var}(X_i)+2\sum_{i<j}\operatorname{Cov}(X_i,X_j).$$

因此独立性是消除协方差的一种充分条件，不是平均值收敛的唯一机制。

**可收敛的依赖例子**：令 $Z_1,Z_2,\ldots$ i.i.d.，均值为 0、方差为 1，设 $X_{2j-1}=X_{2j}=Z_j$。相邻两项完全相同，序列不独立，但

$$\sum_{i=1}^{2m}X_i=2\sum_{j=1}^mZ_j,\qquad \operatorname{Var}\!\left(\sum_{i=1}^{2m}X_i\right)=4m.$$

除以 $(2m)^2$ 得 $1/m\to0$；奇数项时方差为 $4m+1$，除以 $(2m+1)^2$ 也趋于零。故平均值依概率趋于零。

**失败的依赖例子**：若所有 $X_i=Z$，且 $\operatorname{Var}(Z)>0$，则 $\bar X_n=Z$ 始终不变，

$$\operatorname{Var}\!\left(\sum_{i=1}^nX_i\right)=n^2\operatorname{Var}(Z).$$

方差判据失败，而且平均值确实不依概率趋于 $E(Z)$。反复复制同一个随机结果，不会产生平均化效果。

### 7.6 三个大数定律版本如何选择？

| 版本 | 易检查的充分条件 | 结论中心 |
|---|---|---|
| i.i.d. 有限方差版 | 独立同分布、有限方差 | 共同均值 $\mu$ |
| Chebyshev 版 | 独立、方差统一有界 | 各均值的平均 |
| 一般方差判据 | $\operatorname{Var}(\sum_iX_i)/n^2\to0$ | 各均值的平均 |

前两者都能通过方差计算归入第三个判据。但更弱的 i.i.d. 有限一阶矩结论可能没有有限方差，不能硬套第三个判据。

---

## 8. 大数定律的应用、边界及与 CLT 的联系 (Applications & Scope)

本模块除课件已出现的一致性解释外，为深度补充。

### 8.1 频率为何趋于概率？

在独立重复试验中，设 $I_i=\mathbf1_{A_i}$，每次成功概率为 $p$。则 $I_i$ i.i.d. Bernoulli$(p)$，

$$\frac{\text{成功次数}}n=\frac1n\sum_{i=1}^nI_i\xrightarrow pp.$$

所以频率稳定性是样本均值大数定律在示性变量上的应用。它并未保证每次增加样本都会让频率更接近 $p$。

### 8.2 从样本均值推广到样本矩

若 $X_i$ i.i.d.，且 $E|g(X_1)|<\infty$，对 $g(X_i)$ 使用有限均值版弱大数定律：

$$\boxed{\frac1n\sum_{i=1}^ng(X_i)\xrightarrow pE[g(X_1)].}$$

例如若 $E(X_1^2)<\infty$，则 $n^{-1}\sum_iX_i^2\xrightarrow pE(X_1^2)$。再结合 $\bar X_n^2\xrightarrow p\mu^2$，得到

$$\frac1n\sum_{i=1}^n(X_i-\bar X_n)^2=\frac1n\sum_iX_i^2-\bar X_n^2\xrightarrow p\sigma^2.$$

乘以 $n/(n-1)\to1$，便得到通常样本方差 $S_n^2$ 的一致性；开平方又得到 $S_n\xrightarrow p\sigma$。

这里使用了有限均值版大数定律作用于 $X_i^2$。若坚持仅用有限方差版证明这个步骤，则通常需要更强的四阶矩条件；不要把证明方法额外需要的条件误当作结论本身必须的条件。

### 8.3 Monte Carlo 平均

若可以独立抽取 $X_i$，则用 $n^{-1}\sum_i g(X_i)$ 估计 $E[g(X)]$。例如 $U_i$ i.i.d. $U(0,1)$，则

$$\frac1n\sum_i h(U_i)\xrightarrow p\int_0^1h(u)\,du,$$

前提是积分绝对可积。概率论中的平均值稳定性因此可以转化为数值积分方法。

### 8.4 弱大数定律与强大数定律

弱大数定律给出 $\bar X_n\xrightarrow p\mu$；强大数定律给出 $\bar X_n\xrightarrow{a.s.}\mu$。本 PDF 正文并未陈述、证明强大数定律，不应把它作为本课件已经完成的内容。

强结论强调一条无限样本路径的长期行为；弱结论强调大样本时误差概率小。

### 8.5 与中心极限定理的衔接：只作定位

对 i.i.d.、$0<\sigma^2<\infty$ 的情形，经典 CLT 描述

$$\frac{\sqrt n(\bar X_n-\mu)}\sigma\xrightarrow dN(0,1).$$

| 大数定律 | 中心极限定理 |
|---|---|
| 平均值趋向哪里？ | 放大后的误差如何分布？ |
| $\bar X_n\xrightarrow p\mu$ | $\sqrt n(\bar X_n-\mu)/\sigma\xrightarrow dN(0,1)$ |
| 固定误差阈值的偏离概率趋于零 | 刻画 $1/\sqrt n$ 尺度的随机波动 |

未经放大的均值趋于常数，与放大后的误差有非退化极限并不矛盾。完整 CLT 条件、正态近似计算、连续性修正及 Delta 方法需结合后续课件学习，不能视为这 45 页中已经覆盖的正文。

---

## 9. 公式速查、解题路线与易错辨析 (Summary & Pitfalls)

### 9.1 核心公式卡片

| 知识点 | 公式 | 使用条件 |
|---|---|---|
| Markov | $P(X\ge a)\le E(X)/a$ | $X\ge0$、有限期望、$a>0$ |
| Chebyshev | $P(|X-\mu|\ge a)\le\sigma^2/a^2$ | 有限方差、$a>0$ |
| 标准化界 | $P(|X-\mu|\ge k\sigma)\le1/k^2$ | $\sigma>0$ |
| i.i.d. 平均值 | $E(\bar X_n)=\mu$，$\operatorname{Var}(\bar X_n)=\sigma^2/n$ | i.i.d.、有限二阶矩 |
| 比例误差界 | $P(|Y/n-p|\ge\varepsilon)\le1/(4n\varepsilon^2)$ | $Y\sim\operatorname{Bin}(n,p)$ |
| 一般 LLN 判据 | $\operatorname{Var}(\sum_iX_i)/n^2\to0$ | 有限二阶矩，结论是中心化平均值依概率趋零 |
| 收敛关系 | a.s. $\Rightarrow p\Rightarrow d$ | 同一空间中比较前两者 |
| 常数极限 | $X_n\xrightarrow dc\iff X_n\xrightarrow pc$ | $c$ 为常数 |
| 连续映射 | $X_n\to X\Rightarrow g(X_n)\to g(X)$ | 保持相应收敛模式，检查连续性 |
| Slutsky | $X_n\xrightarrow dX,Y_n\xrightarrow pc\Rightarrow X_nY_n\xrightarrow dcX$ | $c$ 为常数；比值另需 $c\ne0$ |

### 9.2 按题型选择方法

1. **只给非负变量的期望，求右尾上界**：Markov。
2. **给均值、方差，求偏离概率**：先写成 $|X-\mu|$，再用 Chebyshev。
3. **求中心区间的概率下界**：先对补集求上界，再用 $1-$。
4. **证明依概率收敛到常数**：写出任意 $\varepsilon>0$ 的误差概率；优先检查方差是否趋零。
5. **证明依分布收敛**：计算 CDF，在极限 CDF 连续点处取极限。
6. **证明几乎必然收敛**：固定随机结果，研究整条数列，并说明例外集合的概率为零。
7. **求平方、指数或倒数的极限**：连续映射；检查倒数的极限是否为零。
8. **在分布极限中替换未知参数**：证明替换量一致，再用 Slutsky。
9. **非同分布或依赖序列的平均值**：先展开总和方差，检查是否为 $o(n^2)$，再看均值平均是否有极限。

### 9.3 高频易错点

| 容易写错的结论 | 正确理解 |
|---|---|
| Markov 可用于任意正均值变量 | 变量本身需要非负，或先进行非负变换 |
| Chebyshev 的结果就是实际概率 | 它提供普适界 |
| 两倍标准差外的概率必为约 4.55% | 这是正态概率；一般有限方差分布只保证上界 25% |
| 依概率收敛要求每一步误差都减少 | 只要求每个固定阈值的超限概率趋于零 |
| 几乎必然表示对所有结果成立 | 可排除概率零的共同例外集合 |
| 同分布意味着取值相同 | 仅意味着概率规律相同 |
| 依分布收敛要求每个点 CDF 都收敛 | 只要求极限 CDF 的连续点 |
| 两个依分布极限可以直接相加 | 还需要联合关系；Slutsky 的常数极限是重要特例 |
| Slutsky 需要两个统计量独立 | 不需要 |
| i.i.d. 平均值总能套用有限方差证明 | 必须检查矩条件 |
| 大数定律必须独立同分布 | 本课件给出非同分布和一般方差判据 |
| 有限方差是所有大数定律的必要条件 | i.i.d. 有限一阶矩也足够 |
| 非同分布平均值必趋于固定常数 | 还须检查均值平均本身是否收敛 |
| 方差判据不满足就一定不收敛 | 它是充分条件，不能一般性反推失败 |
| 依概率收敛自动推出期望收敛 | 错；还需额外条件 |
| 无偏就必然一致 | 若方差不收缩，可能不一致 |

最后两点可用简单例子理解。令 $P(T_n=n)=1/n$、$P(T_n=0)=1-1/n$，则 $T_n\xrightarrow p0$，但 $E(T_n)=1$ 不趋于零。令 $T_n=\theta+Z$，其中同一个 $Z\sim N(0,1)$，则每个 $T_n$ 都无偏，但始终保留同样的随机误差，因而不一致。

---

## 10. 自测题与完整答案 (Practice & Solutions)

### 10.1 先独立尝试

1. 已知 $X\ge0$、$E(X)=6$，给出 $P(X\ge20)$ 的上界。
2. 已知 $E(X)=10$、$\operatorname{Var}(X)=9$，给出 $P(4<X<16)$ 的下界。
3. 设 i.i.d. 样本方差为 4，欲保证 $P(|\bar X_n-\mu|<0.2)\ge0.99$，Chebyshev 给出的充分样本量是多少？
4. 若 $E(T_n)=\theta+1/n$、$\operatorname{Var}(T_n)=2/n$，证明 $T_n$ 一致。
5. 若 $X_n\xrightarrow p2$，求 $X_n^2$ 与 $1/X_n$ 的依概率极限。
6. 若 $X_n\xrightarrow dN(0,1)$、$Y_n\xrightarrow p3$，求 $X_n/Y_n$ 的分布极限。
7. 若 $X_i$ 独立，$E(X_i)=i/n$ 是否适合直接当成一个固定无限序列的大数定律题？若改为固定序列 $E(X_i)=1/i$、方差不超过 1，平均值趋于什么？
8. 若有限二阶矩序列满足 $\operatorname{Var}(\sum_{i=1}^nX_i)=O(n^{3/2})$，可以得到什么大数定律结论？

### 10.2 答案与解析

**1.** Markov 给出 $P(X\ge20)\le6/20=0.3$。

**2.** 区间对应 $|X-10|<6$，所以概率至少 $1-9/36=3/4$。

**3.** 只需 $4/(n\cdot0.2^2)\le0.01$，故 $n\ge10000$。注意这是足够的样本量，未证明最小。

**4.** 相对于目标 $\theta$ 的均方误差为

$$E[(T_n-\theta)^2]=\operatorname{Var}(T_n)+[E(T_n)-\theta]^2=\frac2n+\frac1{n^2}\to0.$$

对非负变量 $(T_n-\theta)^2$ 使用 Markov：

$$P(|T_n-\theta|>\varepsilon)\le\frac{2/n+1/n^2}{\varepsilon^2}\to0.$$

故 $T_n\xrightarrow p\theta$。这也表明一致性不要求每个样本量都无偏。

**5.** 连续映射给出 $X_n^2\xrightarrow p4$、$1/X_n\xrightarrow p1/2$；若个别事件上 $X_n=0$，可先在这些事件上扩展定义，其概率趋于零。

**6.** Slutsky 给出 $X_n/Y_n\xrightarrow dZ/3\sim N(0,1/9)$，$Z\sim N(0,1)$。第二参数是方差，不能写成 $1/3$。

**7.** $i/n$ 同时依赖样本量 $n$，通常需要写作 $X_{n,i}$，属于三角阵形式，不能不加说明地套用固定无限序列记号。对于修改后的固定序列，由 Chebyshev 大数定律，

$$\bar X_n-\frac1n\sum_{i=1}^n\frac1i\xrightarrow p0.$$

又因 $\sum_{i=1}^n1/i\le1+\log n$，其均值平均趋于零，所以 $\bar X_n\xrightarrow p0$。

**8.** 方差比为 $O(n^{-1/2})\to0$，故

$$\frac1n\sum_{i=1}^n(X_i-E X_i)\xrightarrow p0.$$

若再知各均值的平均趋于 $\mu$，才可进一步写成 $\bar X_n\xrightarrow p\mu$。

---

## 课件覆盖范围核对

| PDF 页码 | 本笔记对应内容 |
|---|---|
| 1—5 | 标题、参考书、目录、记号、全章问题 |
| 6—11 | Markov、Chebyshev 及证明 |
| 12—19 | 例 5.1—5.4，全数整理并解释 |
| 20—30 | 三种收敛及关系、用途 |
| 31—33 | 反向推论失败的原因与正态反例 |
| 34—38 | 连续映射、Slutsky、边缘与联合收敛 |
| 39—45 | 样本均值、弱大数定律、Chebyshev 版、一般方差判据 |

**复习优先级**：先熟练推导 Markov → Chebyshev → 有限方差弱大数定律；再用反例区分三种收敛；最后训练连续映射与 Slutsky 的条件检查，以及非独立序列的总和方差计算。
