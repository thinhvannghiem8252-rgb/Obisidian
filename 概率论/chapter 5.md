# 第五章　大数定律与中心极限定理：教材式复习讲义

> 依据 chapter 5.pdf 的全部 80 个 PDF 页面整理。正文按“矩给出概率界 → 收敛的含义 → 样本平均的稳定性 → 误差的分布 → 变换后的误差”展开。课件例题均给出计算过程，额外推导、反例和练习标为“补充”。
>
> 原课件：[chapter 5.pdf](<C:/Users/yang/Desktop/大四/概率论/chapter 5.pdf>)。本文页码指 PDF 阅读器从 1 开始计算的实际页码。第 46–50 页重复引入大数定律并重述部分定理，正文合并讲解。

## 导论　本章怎样承接第四章

[[chapter 4|第四章]]用期望描述中心，用方差描述波动，用协方差描述变量的共同变化。本章把这些数字特征用于一列随样本量 $n$ 改变的随机变量。记

$$S_n=\sum_{i=1}^nX_i,\qquad \bar X_n=\frac{S_n}{n}.$$

- **知道均值或方差，能把尾概率压到多小？** Markov 和 Chebyshev 给出上界。
- **样本均值会靠近什么？** 大数定律说明它向总体均值 $\mu$ 收敛。
- **有限样本的误差通常有多大？** 中心极限定理描述放大 $\sqrt n$ 倍后的误差形状。
- **若报告 $\log\bar X_n$ 或 $e^{\bar X_n}$ 呢？** 连续映射定理给出收敛目标，Delta 方法给出变换后的渐近波动。

全文以 $E|X|<\infty$ 表示有限均值所需的绝对可积条件。$N(m,v)$ 的第二个参数 $v$ 是方差，$\Phi(z)=P(Z\le z)$ 为标准正态 CDF，$z_q=\Phi^{-1}(q)$ 为其下侧 $q$ 分位数。符号 $\xrightarrow{d}$ 表示分布极限，$\approx$ 用于有限样本近似。

### 课件与本文对应关系

| PDF 页码 | 课件内容 | 本文位置 |
|---|---|---|
| 1–5 | 章节导览、记号、研究问题 | 导论 |
| 6–11 | Markov、Chebyshev 不等式与证明 | 第一节 |
| 12–19 | 例 5.1–5.4 | 第二节 |
| 20–33 | 三种收敛、关系及反例 | 第三、四节 |
| 34–38 | 连续映射、Slutsky、边缘与联合 | 第五节 |
| 39–51 | 样本均值、弱律、方差判据、强律 | 第六节 |
| 52–53 | 例 5.5 样本比例、例 5.6 Monte Carlo 积分 | 第七节 |
| 54–56、59–62 | LLN 与 CLT、MGF 收敛、标准化与连续性修正 | 第八节 |
| 57–58、63–64 | 二项的 Poisson 极限、另一道例 5.6、例 5.7 | 第九节 |
| 65–68 | 例 5.8 与例 5.9(a)–(c) | 第十节 |
| 69–75 | Delta 方法、例 5.11、对数例题 | 第十一、十二节 |
| 76–80 | 全章总结、自查与结束页 | 第十三节及附录 |

---

## 第一节　从矩到尾概率：Markov 与 Chebyshev

### 1.1 Markov 不等式（定理 5.1，PDF 第 8–9 页）

若 $X\ge0$ 几乎处处、$E(X)<\infty$，则对 $a>0$，

$$\boxed{P(X\ge a)\le \frac{E(X)}a.}$$

证明用到第四章的指示变量。对几乎每个结果，$X\ge a\,1_{\{X\ge a\}}$。在事件上，$X$ 至少为 $a$；在事件外，右边为 $0$，仍由非负性保证不等式。取期望得到 $E(X)\ge aP(X\ge a)$。算出的上界若超过 $1$，可截到 $1$。

**补充：带符号变量的处理。** 若 $X$ 有正有负，可以对 $|X|$、$X^+=\max(X,0)$ 或 $X^2$ 应用 Markov。直接把 $E(X)$ 当成右尾上界会让正负贡献抵消。例如 $X=\pm1$ 各以 $1/2$ 的概率出现，$E(X)=0$，但 $P(X\ge1)=1/2$。

### 1.2 Chebyshev 不等式（推论 5.2，PDF 第 10–11 页）

设 $E(X)=\mu$、$\operatorname{Var}(X)=\sigma^2<\infty$。对 $a>0$，

$$\boxed{P(|X-\mu|\ge a)\le\frac{\sigma^2}{a^2}.}$$

令 $Y=(X-\mu)^2\ge0$。由于 $\{|X-\mu|\ge a\}=\{Y\ge a^2\}$ 且 $E(Y)=\sigma^2$，把 $Y$ 和阈值 $a^2$ 代入 Markov 即得。若 $\sigma>0$，取 $a=k\sigma$ 得

$$P(|X-\mu|\ge k\sigma)\le\frac1{k^2},\qquad
P(|X-\mu|<k\sigma)\ge1-\frac1{k^2}.$$

取补集时，外侧的 $\ge$ 对应内侧的 $<$。若 $\sigma=0$，则 $E[(X-\mu)^2]=0$，所以 $X=\mu$ 几乎处处，任何正阈值的偏差概率都为零。

**补充：界可以取到。** 给定 $k\ge1$，令 $X$ 在 $\pm k$ 处各有概率 $1/(2k^2)$，在 $0$ 处有余下的概率。此时 $E(X)=0$、$\operatorname{Var}(X)=1$，而 $P(|X|\ge k)=1/k^2$。只知道均值与方差时，不能普遍把这个上界调低。

---

## 第二节　不等式的课件例题

### 2.1 例 5.1　给定均值与方差（PDF 第 12–13 页）

$E(X)=25$、$\operatorname{Var}(X)=16$，所以 $\sigma=4$。区间 $(17,33)$ 是以 $25$ 为中心、半径 $8=2\sigma$ 的开区间。

$$P(17<X<33)=1-P(|X-25|\ge8)\ge1-\frac{16}{8^2}=\frac34.$$

阈值 $12=3\sigma$ 给出 $P(|X-25|\ge12)\le16/12^2=1/9$。两问的结果分别是**下界**和**上界**。

### 2.2 例 5.2　二项比例（PDF 第 14–15 页）

$Y\sim\operatorname{Bin}(n,p)$，令 $\hat p_n=Y/n$。用第四章的仿射变换公式，

$$E(\hat p_n)=p,\qquad
\operatorname{Var}(\hat p_n)=\frac{np(1-p)}{n^2}=\frac{p(1-p)}n.$$

于是

$$P(|\hat p_n-p|\ge\varepsilon)\le
\frac{p(1-p)}{n\varepsilon^2}\le\frac{1}{4n\varepsilon^2},$$

其中 $p(1-p)=1/4-(p-1/2)^2$。对每个**固定** $\varepsilon>0$，上界趋于零。第二个界在 $p$ 未知时仍能直接使用。若把阈值取成 $\varepsilon_n=1/\sqrt n$，代入后上界为常数，这就引出了 CLT 所关注的误差尺度。

### 2.3 例 5.3　正态精确尾概率与通用界（PDF 第 16–17 页）

对 $Z\sim N(0,1)$，用对称性得 $P(|Z|\ge k)=2[1-\Phi(k)]$。

| $k$ | 正态精确尾概率（舍入） | Chebyshev 上界 |
|---:|---:|---:|
| 1 | 0.31731 | 1 |
| 2 | 0.04550 | 0.25 |
| 3 | 0.00270 | 0.11111 |

第 17 页已指出，$k=2$ 时把精确概率写成小于 $0.04$ 是错误的。已知正态分布时可直接用 $\Phi$。只有矩信息时，Chebyshev 仍可量化偏差，尤其适合证明收敛。

### 2.4 例 5.4　标准正态样本的平均（PDF 第 18–19 页）

$Z_i$ 独立且均为 $N(0,1)$，由独立正态的线性组合性质，

$$\bar Z_n\sim N(0,1/n),\qquad \sqrt n\,\bar Z_n\sim N(0,1).$$

因此 $P(|\bar Z_n|\ge1)=2[1-\Phi(\sqrt n)]$，Chebyshev 则给出 $P(|\bar Z_n|\ge1)\le1/n$。精确式来自正态可加性，对每个 $n$ 都成立。两个结果都说明，平均值偏离零至少一个单位的概率趋于零。

---

## 第三节　三种收敛：看路径、误差概率或分布函数

### 3.1 依概率收敛（PDF 第 22–23 页）

$$X_n\xrightarrow{p}X
\quad\Longleftrightarrow\quad
\forall\varepsilon>0,\quad P(|X_n-X|>\varepsilon)\longrightarrow0.$$

使用 $\ge\varepsilon$ 也给出同一个定义，因为 $\{|X_n-X|\ge\varepsilon\}\subseteq\{|X_n-X|>\varepsilon/2\}$。估计量 $T_n$ 依概率趋于真值 $\theta$ 时，称其为 $\theta$ 的一致估计量。

**课件例。** 若 $T_n=\theta+Z_n/\sqrt n$，且每个 $Z_n$ 均值为 $0$、方差为 $1$，则

$$P(|T_n-\theta|>\varepsilon)=P(|Z_n|>\sqrt n\,\varepsilon)\le\frac{1}{n\varepsilon^2}\longrightarrow0.$$

这是逐个 $n$ 使用 Chebyshev，所以 $Z_n$ 之间可有依赖。

### 3.2 依分布收敛（PDF 第 24–25 页）

设 $F_n,F$ 分别是 $X_n,X$ 的 CDF，则 $X_n\xrightarrow d X$ 的定义是 $F_n(x)\to F(x)$ 对 $F$ 的**每个连续点** $x$ 成立。只比较各自的分布，因此 $X_n$ 和 $X$ 可以定义在不同概率空间上。

**课件例。** 若 $X_n\sim N(0,1+1/n)$，则

$$F_n(x)=\Phi\!\left(\frac{x}{\sqrt{1+1/n}}\right)\longrightarrow\Phi(x),$$

故 $X_n\xrightarrow d N(0,1)$。**补充：** $X_n=1/n$ 时，$X_n\xrightarrow d0$，但 $F_n(0)=0$，而常数 $0$ 的 CDF 在 $0$ 处取 $1$。这个跳点在定义里无需检查。

### 3.3 几乎处处收敛（PDF 第 26–27 页）

$$X_n\xrightarrow{\mathrm{a.s.}}X
\quad\Longleftrightarrow\quad
P\{\omega:X_n(\omega)\to X(\omega)\}=1.$$

固定一个结果 $\omega$，观察整条数列。可以有概率为零的例外。依概率和几乎处处收敛都需要在同一概率空间上比较 $X_n$ 与 $X$。

**课件例。** 对同一个 $U\sim U(0,1)$，定义 $X_n=U^n$。当 $U<1$，$U^n\to0$；唯一可能的端点例外 $U=1$ 的概率为零，所以 $X_n\xrightarrow{\mathrm{a.s.}}0$。

---

## 第四节　收敛关系与反例（定理 5.6，PDF 第 28–33 页）

$$\boxed{X_n\xrightarrow{\mathrm{a.s.}}X\ \Longrightarrow\
X_n\xrightarrow p X\ \Longrightarrow\ X_n\xrightarrow d X.}$$

极限为常数 $c$ 时，$X_n\xrightarrow d c$ 也能推出 $X_n\xrightarrow p c$。

### 4.1 补充：三个箭头的证明

1. **几乎处处 $\Rightarrow$ 依概率。** 固定 $\varepsilon>0$，定义 $A_m=\bigcup_{n\ge m}\{|X_n-X|>\varepsilon\}$。几乎处处收敛意味着 $\bigcap_m A_m$ 的概率为零。事件 $A_m$ 递减，故 $P(A_m)\to0$，而 $P(|X_m-X|>\varepsilon)\le P(A_m)$。
2. **依概率 $\Rightarrow$ 依分布。** 固定 $F$ 的连续点 $x$。在 $|X_n-X|\le\delta$ 上，$X\le x-\delta$ 推出 $X_n\le x$，而 $X_n\le x$ 推出 $X\le x+\delta$。因此

   $$F(x-\delta)-P(|X_n-X|>\delta)\le F_n(x)\le
   F(x+\delta)+P(|X_n-X|>\delta).$$

   先让 $n\to\infty$ 消掉误差概率，再让 $\delta\downarrow0$，由连续性得到 $F_n(x)\to F(x)$。
3. **常数极限的反向箭头。** $c-\varepsilon$ 和 $c+\varepsilon$ 都是常数 $c$ 的 CDF 的连续点。因此

   $$P(|X_n-c|>\varepsilon)\le F_n(c-\varepsilon)+1-F_n(c+\varepsilon)\longrightarrow0+1-1=0.$$

### 4.2 课件反例：同分布的两条路径可以相差很远

取 $X\sim N(0,1)$，每个 $X_n=-X$。正态对称性给出 $X_n\stackrel d=X$，自然有 $X_n\xrightarrow d X$。但

$$P(|X_n-X|>\varepsilon)=2[1-\Phi(\varepsilon/2)]>0,$$

与 $n$ 无关，所以 $X_n$ 不依概率收敛到这个 $X$。同一个序列其实几乎处处收敛到 $-X$。分布极限只确定分布，路径极限还涉及随机变量之间的配对方式。

### 4.3 补充反例：依概率收敛而路径反复跳动

在 $[0,1)$ 上取一个均匀的 $U$。第 $m$ 层把区间分成 $2^m$ 个半开区间，依次令 $X_{2^m+k}=1_{\{k/2^m\le U<(k+1)/2^m\}}$，其中 $0\le k<2^m$。

每个 $X_{2^m+k}$ 取 $1$ 的概率是 $2^{-m}$，所以 $X_n\xrightarrow p0$。然而每个固定的 $U$ 在每层恰好落入一个区间，整条序列有无穷多个 $1$ 和 $0$，所以不存在逐点极限。逐次错误越来越少见，仍可能在整条路径上反复出现。

---

## 第五节　连续映射、Slutsky 与联合收敛（定理 5.7，PDF 第 34–38 页）

### 5.1 连续映射定理

若 $g$ 在极限随机变量取值处几乎必然连续，则 $X_n\xrightarrow p X$ 推出 $g(X_n)\xrightarrow p g(X)$，$X_n\xrightarrow d X$ 推出 $g(X_n)\xrightarrow d g(X)$。几乎处处收敛时，可以沿每条收敛路径直接应用连续性。

课件例中，$X_n\xrightarrow p\mu$ 时有 $X_n^2\xrightarrow p\mu^2$、$e^{X_n}\xrightarrow p e^\mu$。若 $\mu\ne0$，还有 $1/X_n\xrightarrow p1/\mu$。因为 $P(X_n=0)\le P(|X_n-\mu|>|\mu|/2)\to0$，可以在分母为零的事件上任意定义估计量。若 $X_n\xrightarrow d X$，则 $|X_n|\xrightarrow d|X|$。

对同一概率空间上的 $X_n\xrightarrow p X$ 和 $Y_n\xrightarrow p Y$，用并集界可得 $(X_n,Y_n)\xrightarrow p(X,Y)$，再用二元连续函数得到和与积的依概率收敛。

### 5.2 Slutsky 定理：用一致估计量替换未知常数

若 $X_n\xrightarrow d X$ 且 $Y_n\xrightarrow p c$，其中 $c$ 是常数，则

$$X_n+Y_n\xrightarrow d X+c,\qquad X_nY_n\xrightarrow d cX,\qquad
\frac{X_n}{Y_n}\xrightarrow d\frac Xc\quad(c\ne0).$$

常数极限使 $(X_n,Y_n)\xrightarrow d(X,c)$，因此可以用连续映射取和、积和比。$X_n$ 和 $Y_n$ 可以来自同一批样本。商式在分母为零的事件上可以用任意值补定义，该事件概率趋于零。

**课件应用：估计标准差后的标准化。** 若 $\sqrt n(\hat\theta_n-\theta)/\sigma\xrightarrow d N(0,1)$ 且 $s_n\xrightarrow p\sigma>0$，则

$$\frac{\sqrt n(\hat\theta_n-\theta)}{s_n}
=\frac{\sqrt n(\hat\theta_n-\theta)}{\sigma}\frac{\sigma}{s_n}
\xrightarrow d N(0,1).$$

极限成立需要 $s_n$ 一致。有限样本下用估计标准差得到的统计量是否有精确分布，需要另外的模型条件。

### 5.3 边缘的分布极限不足以计算和的极限

课件取 $X_n=Z$、$Y_n=-Z$，其中 $Z\sim N(0,1)$。两者各自的边缘都是标准正态，但和恒为 $0$。若极限对被选成两个独立标准正态，它们的和却服从 $N(0,2)$。两个边缘无法确定极限对的依赖关系。

**补充：和甚至可以没有分布极限。** 令 $X_n=Z$、$Y_n=(-1)^nZ$。奇数项的和恒为零，偶数项的和服从 $N(0,4)$，两条子列的分布极限不同。遇到两个随机极限，先论证联合收敛，再使用二元连续映射。

---

## 第六节　大数定律：样本平均为何稳定

### 6.1 i.i.d. 有限方差弱律（定理 5.3，PDF 第 40–42、47–48 页）

设 $X_1,X_2,\ldots$ 独立同分布（i.i.d.），$E(X_i)=\mu$、$\operatorname{Var}(X_i)=\sigma^2<\infty$。期望的线性与独立时方差可加给出

$$E(\bar X_n)=\mu,\qquad
\operatorname{Var}(\bar X_n)=\frac{1}{n^2}\sum_{i=1}^n\sigma^2=\frac{\sigma^2}{n}.$$

于是对每个固定 $\varepsilon>0$，

$$P(|\bar X_n-\mu|\ge\varepsilon)\le
\frac{\sigma^2}{n\varepsilon^2}\longrightarrow0,\qquad
\boxed{\bar X_n\xrightarrow p\mu.}$$

方差随 $1/n$ 下降，标准差随 $1/\sqrt n$ 下降。若只有 $E|X_1|<\infty$，i.i.d. 弱律仍然成立，可由下述强律推出。

### 6.2 独立但不同分布的 Chebyshev 弱律（定理 5.4，PDF 第 43–44、49 页）

设 $X_i$ 独立、$E(X_i)=\mu_i$，且有一个与 $i$ 无关的有限常数 $C$ 使 $\operatorname{Var}(X_i)\le C$。则

$$\operatorname{Var}(\bar X_n)\le C/n,\qquad
P\!\left(\left|\frac1n\sum_{i=1}^n(X_i-\mu_i)\right|>\varepsilon\right)\le\frac{C}{n\varepsilon^2}.$$

故 $\bar X_n-\frac1n\sum_{i=1}^n\mu_i\xrightarrow p0$。中心是随 $n$ 变化的平均期望。若该确定性序列另有极限 $\mu$，才可得到 $\bar X_n\xrightarrow p\mu$。

### 6.3 方差判据（定理 5.5，PDF 第 45、50 页）

只要 $X_i$ 有有限二阶矩，且

$$\frac{\operatorname{Var}(S_n)}{n^2}=\operatorname{Var}(\bar X_n)\to0,$$

就有 $\bar X_n-E(\bar X_n)\xrightarrow p0$。证明是把 $\operatorname{Var}(\bar X_n)/\varepsilon^2$ 代入 Chebyshev。存在依赖时，用第四章的公式计算

$$\operatorname{Var}(S_n)=\sum_{i=1}^n\operatorname{Var}(X_i)
+2\sum_{i<j}\operatorname{Cov}(X_i,X_j).$$

**补充对照。** 若 $X_i=Z$ 对所有 $i$ 成立，且 $Z$ 非退化，则 $\bar X_n=Z$，方差一直不变。若 $X_i=Z_i+Z_{i+1}$，其中 $Z_i$ 独立同分布、均值零、方差 $1$，则相邻 $X_i$ 相关，且

$$S_n=Z_1+2\sum_{i=2}^nZ_i+Z_{n+1},\qquad
\operatorname{Var}(S_n)=4n-2.$$

后一例的 $\operatorname{Var}(S_n)/n^2\to0$，所以相关性并未妨碍该平均值依概率收敛。

### 6.4 i.i.d. 强大数定律（定理 5.8，PDF 第 51 页）

若 $X_1,X_2,\ldots$ i.i.d.，且 $E|X_1|<\infty$、$\mu=E(X_1)$，则

$$\boxed{\bar X_n\xrightarrow{\mathrm{a.s.}}\mu.}$$

在概率为 $1$ 的一组完整样本序列上，对每个给定容忍度，平均值从某一步开始一直落在容忍范围内。起始步可以随样本序列而变。课件直接使用强律。上面的 Chebyshev 证明只得到弱律，不能从单个 $n$ 的界直接推到整条路径收敛。

---

## 第七节　大数定律的课件应用

### 7.1 例 5.5　次品率的一致估计（PDF 第 52 页）

令 $X_i=1_{\{\text{第 }i\text{ 件为次品}\}}$。在独立且次品概率同为 $p$ 的模型里，$X_i\sim\operatorname{Bernoulli}(p)$，$E(X_i)=p$。观测比例是 $\hat p_n=\bar X_n$。由弱律 $\hat p_n\xrightarrow p p$，由强律还可得 $\hat p_n\xrightarrow{\mathrm{a.s.}}p$。例如 $p=0.02$ 时，对每个固定 $\varepsilon>0$，$P(|\hat p_n-0.02|>\varepsilon)\to0$。

### 7.2 例 5.6　Monte Carlo 积分（PDF 第 53 页）

抽取 $U_1,\ldots,U_n$ i.i.d. $U(0,1)$，令 $Y_i=4\sqrt{1-U_i^2}$。用均匀分布的密度，

$$E(Y_i)=4\int_0^1\sqrt{1-u^2}\,du=4\cdot\frac\pi4=\pi.$$

积分是单位圆在第一象限的面积。每个 $Y_i$ 有界且同分布，所以 $\hat\pi_n=n^{-1}\sum_iY_i$ 依概率并且几乎处处趋于 $\pi$。

**补充：模拟误差。** $E(Y_i^2)=16\int_0^1(1-u^2)du=32/3$，所以

$$\operatorname{Var}(\hat\pi_n)=\frac{32/3-\pi^2}{n},\qquad
\operatorname{SD}(\hat\pi_n)=\frac{\sqrt{32/3-\pi^2}}{\sqrt n}.$$

要把标准差降到原来的一半，需要把独立抽样次数增加到原来的四倍。

---

## 第八节　中心极限定理：误差放大后呈现什么形状

### 8.1 i.i.d. CLT（定理 5.9，PDF 第 55、59–60 页）

设 $X_1,X_2,\ldots$ i.i.d.，$E(X_i)=\mu$、$0<\operatorname{Var}(X_i)=\sigma^2<\infty$。则

$$\boxed{\frac{S_n-n\mu}{\sigma\sqrt n}
=\frac{\bar X_n-\mu}{\sigma/\sqrt n}
\xrightarrow d N(0,1).}$$

等价地，$\sqrt n(\bar X_n-\mu)\xrightarrow d N(0,\sigma^2)$。大数定律看固定容忍度下误差是否消失，CLT 看缩到 $1/\sqrt n$ 尺度后剩下多少误差。例如对固定 $a>0$，

$$P\!\left(|\bar X_n-\mu|\le\frac{a\sigma}{\sqrt n}\right)
\longrightarrow 2\Phi(a)-1.$$

这也解释了一个常见现象：增加样本会缩小标准误，但把误差除以自己的标准误之后，其分布逐渐稳定在标准正态。

在有限样本题中，常用以下近似：

$$\bar X_n\approx N(\mu,\sigma^2/n),\qquad
\bar X_n-\mu\approx N(0,\sigma^2/n),\qquad
S_n\approx N(n\mu,n\sigma^2).$$

三个正态分布的参数均对应当前样本量。写分布收敛时，右边应是一个固定分布。例如 $\bar X_n\xrightarrow d\mu$ 是大数定律的推论，而放大后的误差有非退化的正态极限。

### 8.2 矩母函数收敛与 CLT 的证明思路（引理 5.9A，PDF 第 56 页）

若 $M_{X_n}$ 和 $M_X$ 在包含 $0$ 的同一开区间内有限，且 $M_{X_n}(t)\to M_X(t)$ 对该区间内每个 $t$ 成立，则 $X_n\xrightarrow d X$。第四章的 MGF 唯一性是“函数相等则分布相等”，此处的连续性引理允许用函数的极限识别分布的极限。

**补充推导：额外假定 MGF 在零点附近有限。** 设 $W_i=(X_i-\mu)/\sigma$，则 $M_W(u)=1+u^2/2+o(u^2)$，一次项消失是因为 $E(W_i)=0$，二次项来自 $E(W_i^2)=1$。独立性给出

$$M_{\frac1{\sqrt n}\sum_iW_i}(t)
=\left[M_W\left(\frac{t}{\sqrt n}\right)\right]^n
=\left[1+\frac{t^2}{2n}+o(n^{-1})\right]^n
\longrightarrow e^{t^2/2}.$$

最后的函数是标准正态的 MGF。一般 i.i.d. CLT 只需要有限的非零方差，证明可对特征函数使用类似的二阶展开。这里的 MGF 推导解释了为何中心化和标准化后只有二次项保留。

### 8.3 标准化的做题顺序（PDF 第 61 页）

先确定题目要的是总和还是平均值，再分别算其均值 $m$ 与标准差 $s$。例如

$$P(S_n\le b)\approx\Phi\!\left(\frac{b-n\mu}{\sigma\sqrt n}\right),$$

$$P(a\le\bar X_n\le b)\approx
\Phi\!\left(\frac{b-\mu}{\sigma/\sqrt n}\right)-
\Phi\!\left(\frac{a-\mu}{\sigma/\sqrt n}\right).$$

右尾用 $1-\Phi$，近似的下侧 $q$ 分位数用 $m+s\,z_q$。近似误差与原分布偏斜程度、尾部及所求区域有关。同一个 $n$ 下，中心区域和很远尾部的准确度可以相差很大。

### 8.4 连续性修正（PDF 第 62 页）

整数 $k$ 上的质量用连续区间 $[k-0.5,k+0.5]$ 的面积近似。若 $Y$ 是整数变量且可用 $N(m,s^2)$ 近似，下表的阈值先按事件确定，再标准化。

| 原事件（$a,b,k$ 为整数） | 正态计算区间 |
|---|---|
| $Y\le k$ | $(-\infty,k+0.5]$ |
| $Y<k$ | $(-\infty,k-0.5]$ |
| $Y\ge k$ | $[k-0.5,\infty)$ |
| $Y>k$ | $[k+0.5,\infty)$ |
| $a\le Y\le b$ | $[a-0.5,b+0.5]$ |

例如 $P(a\le Y\le b)\approx\Phi((b+0.5-m)/s)-\Phi((a-0.5-m)/s)$。若题目给的是比例阈值，先换算成整数计数。若格点间距为 $h$，半格是 $h/2$，可以先把变量除以 $h$ 化为整数。修正处理格点边界，偏斜很严重时仍须检查正态近似的质量。

---

## 第九节　二项计数：Poisson 极限还是正态近似

### 9.1 稀有事件下的 Poisson 极限（PDF 第 56–57 页）

若 $Y_n\sim\operatorname{Bin}(n,p_n)$，$np_n\to\lambda\in(0,\infty)$，则 $p_n\to0$，且 $Y_n\xrightarrow d\operatorname{Poisson}(\lambda)$。例如取 $p_n=\lambda/n$。

**补充推导。** 由二项分布的 MGF，

$$M_{Y_n}(t)=[1+p_n(e^t-1)]^n.$$

固定 $t$，记 $u_n=p_n(e^t-1)$。则 $nu_n\to\lambda(e^t-1)$ 且 $nu_n^2\to0$，因此

$$n\log(1+u_n)=nu_n+O(nu_n^2)\to\lambda(e^t-1).$$

取指数得 $M_{Y_n}(t)\to\exp\{\lambda(e^t-1)\}$，正是 Poisson 的 MGF，应用引理 5.9A 即得结论。固定样本时常以 $\lambda=np$ 作近似参数。

### 9.2 例 5.6　同均值的三个二项分布（PDF 第 58 页）

三个二项分布的均值都为 $5$，所以与 $\operatorname{Poisson}(5)$ 对比。它们的方差都是 $5(1-p)$，与 Poisson 的方差 $5$ 相比，$p$ 越小越接近。直接计算部分概率如下：

| 分布 | 方差 | $P(Y=0)$ | $P(Y=5)$ |
|---|---:|---:|---:|
| $\operatorname{Bin}(50,0.1)$ | 4.50 | 0.005154 | 0.184925 |
| $\operatorname{Bin}(20,0.25)$ | 3.75 | 0.003171 | 0.202331 |
| $\operatorname{Bin}(10,0.5)$ | 2.50 | 0.000977 | 0.246094 |
| $\operatorname{Poisson}(5)$ | 5.00 | 0.006738 | 0.175467 |

其中 $\operatorname{Bin}(50,0.1)$ 最接近。**补充核对：** 用总变差距离 $\tfrac12\sum_{k\ge0}|p_{\mathrm{Bin}}(k)-p_{\mathrm{Pois}}(k)|$ 比较整个分布，三者依次约为 $0.0260$、$0.0714$、$0.1718$。

![同均值二项分布与 Poisson 分布的概率质量比较](<../img/chapter5_poisson_comparison.png>)

图中四个分布都以 $5$ 为均值。$p$ 较大的二项分布把更多概率质量集中到均值附近。

### 9.3 例 5.7　50 件物品的次品数（PDF 第 63 页）

每件独立地以概率 $0.01$ 成为次品，故 $Y\sim\operatorname{Bin}(50,0.01)$。题目求 $P(Y\le3)$。

1. **精确二项。**

   $$\sum_{j=0}^3\binom{50}{j}(0.01)^j(0.99)^{50-j}\approx0.99840383.$$

2. **Poisson。** $\lambda=50(0.01)=0.5$，所以 $e^{-0.5}\sum_{j=0}^3(0.5)^j/j!\approx0.99824838$。
3. **正态，不做连续性修正。** $m=0.5$，$s=\sqrt{50(0.01)(0.99)}=\sqrt{0.495}$，用 $\Phi((3-0.5)/s)\approx0.99980982$。
4. **正态，做连续性修正。** 用 $\Phi((3.5-0.5)/s)\approx0.99998996$。

四个答案看起来都接近 $1$，从右尾更容易看出差距。精确的 $P(Y>3)\approx0.00159617$，Poisson 给出约 $0.00175162$，修正后的正态只给出约 $0.00001004$。本题的 $np=0.5$，计数强烈偏右，Poisson 更贴合，半格修正无法解决形状差异。

### 9.4 选择近似的依据（PDF 第 64 页）

- 当 $p$ 很小、$np$ 适中时，Poisson 捕捉稀有事件计数。若 $1-p$ 很小，可先考虑失败次数 $n-Y$。
- 当 $p\in(0,1)$ 固定、$n$ 增大时，把二项计数写成 i.i.d. Bernoulli 的和，可用 CLT 得到 $(Y-np)/\sqrt{np(1-p)}\xrightarrow d N(0,1)$。有限样本中通常检查 $np$ 和 $n(1-p)$ 是否都足够大。
- “两者至少为 $5$”或“至少为 $10$”是经验检查。若结果依赖远尾小概率，能计算精确二项时可用它核对。

---

## 第十节　中心极限定理的课件例题

### 10.1 例 5.8　卡方的正态近似（PDF 第 65 页）

令 $Y_n\sim\chi^2(n)$。用第四章的正态平方与卡方可加性，可写 $Y_n\stackrel d=\sum_{i=1}^nZ_i^2$，其中 $Z_i$ 是独立标准正态。$E(Z_i^2)=1$，$E(Z_i^4)=3$，故 $\operatorname{Var}(Z_i^2)=2$。应用 i.i.d. CLT 得

$$\frac{Y_n-n}{\sqrt{2n}}\xrightarrow d N(0,1),\qquad
P(Y_n\le y)\approx\Phi\!\left(\frac{y-n}{\sqrt{2n}}\right).$$

卡方是连续分布，近似时不作半格修正。按精确支持集，$y\le0$ 时 $P(Y_n\le y)=0$。自由度较小时分布偏右，正态近似在尾部尤其需要核对。

### 10.2 例 5.9(a)　团体寿险赔付的 90% 分位数（PDF 第 66 页）

甲类有 $1000$ 人，每人的赔付额为 $20{,}000$ 美元，赔付概率 $0.01$。乙类有 $500$ 人，赔付额为 $10{,}000$ 美元，赔付概率 $0.03$。各人指示变量相互独立。设 $A\sim\operatorname{Bin}(1000,0.01)$、$B\sim\operatorname{Bin}(500,0.03)$ 为两类赔付件数，则总赔付 $L=20{,}000A+10{,}000B$。

$$\begin{aligned}
E(L)&=20{,}000(10)+10{,}000(15)=350{,}000,\\
\operatorname{Var}(L)&=20{,}000^2(1000)(0.01)(0.99)
+10{,}000^2(500)(0.03)(0.97)=5{,}415{,}000{,}000.
\end{aligned}$$

$\operatorname{SD}(L)\approx73{,}586.68$ 美元。令 $P(L\le q)\approx0.90$，连续正态近似给出

$$q\approx350{,}000+z_{0.90}(73{,}586.68)
\approx\boxed{444{,}305\text{ 美元}}.$$

两类赔付分布不同。可以分别近似两组独立二项，再用独立正态可加性；也可用独立非同分布 CLT 的条件解释。这里使用的是连续正态的分位数。若把问题改成求实际离散赔付的精确分位数，可以在 $10{,}000$ 美元格点上计算 $P(2A+B\le k)$。

### 10.3 例 5.9(b)　病假预算（PDF 第 67 页）

每人的年度病假均值为 $10$ 天、标准差为 $2$ 天，有 $20$ 位独立员工。设 $S$ 为总病假天数，则 $E(S)=200$，$\operatorname{Var}(S)=20\cdot2^2=80$。按课件采用总和的正态近似，超预算概率为 $1-\Phi((b-200)/\sqrt{80})$。

$$P(S>b)\lesssim0.20
\quad\Rightarrow\quad
b\gtrsim200+z_{0.80}\sqrt{80}\approx207.53.$$

按整天预算取 **208 天**。代回未作连续性修正的近似式，$b=207$ 时超出概率约为 $0.2169$，$b=208$ 时约为 $0.1855$。题目没有指定每人的完整分布或病假的记账粒度，因此结果按连续正态近似解释。

### 10.4 例 5.9(c)　肺炎病例（PDF 第 68 页）

设 $X\sim\operatorname{Bin}(84,0.7)$。题目求 $P(X\le52)$，计数阈值修正为 $52.5$。

$$m=84(0.7)=58.8,\qquad s=\sqrt{84(0.7)(0.3)}=4.2,$$

$$P(X\le52)\approx\Phi\!\left(\frac{52.5-58.8}{4.2}\right)
=\Phi(-1.5)\approx\boxed{0.06681}.$$

精确二项和 $\sum_{j=0}^{52}\binom{84}{j}(0.7)^j(0.3)^{84-j}\approx0.06899$，可用来衡量本题近似误差。

### 10.5 补充：如何落实第 79 页的 CLT 选用要求

1. **i.i.d. 且已知 $\sigma>0$。** 直接使用第八节的标准化。
2. **i.i.d. 且未知 $\sigma>0$。** 用样本标准差 $s_n$。由大数定律，$n^{-1}\sum_iX_i^2\to E(X^2)$ 且 $\bar X_n^2\to\mu^2$（依概率），所以

   $$s_n^2=\frac{n}{n-1}\left[\frac1n\sum_iX_i^2-\bar X_n^2\right]\xrightarrow p\sigma^2.$$

   取平方根后再用 Slutsky，得到 $\sqrt n(\bar X_n-\mu)/s_n\xrightarrow d N(0,1)$。
3. **独立但不同分布。** 以 $\sum_iE(X_i)$ 为中心，以 $s_n=\sqrt{\sum_i\operatorname{Var}(X_i)}$ 作分母，并检查有无个别项主导总波动。一个常见充分条件是 Lyapunov 条件：对某个 $\delta>0$，

   $$\frac{\sum_{i=1}^n E|X_i-E(X_i)|^{2+\delta}}{s_n^{2+\delta}}\to0.$$

   在寿险例按两类人数同比例扩大、赔付额和概率固定的序列中，每项赔付有统一上界，分子至多与人数同阶，总方差与人数同阶，因而比值趋零。有限样本的数值仍是近似。

---

## 第十一节　Delta 方法：用局部斜率传播误差

### 11.1 定理 5.12（PDF 第 70–73 页）

设 $\sqrt n(T_n-\theta)\xrightarrow d N(0,\tau^2)$，$g$ 在 $\theta$ 可微，且 $g(T_n)$ 已定义或可在概率趋零的事件上补定义。则

$$\boxed{\sqrt n[g(T_n)-g(\theta)]\xrightarrow d
N\!\left(0,[g'(\theta)]^2\tau^2\right).}$$

对大样本，可把 $g(T_n)$ 近似为均值 $g(\theta)$、方差 $[g'(\theta)]^2\tau^2/n$ 的正态变量。近似标准误为 $|g'(\theta)|\tau/\sqrt n$。斜率的符号决定小误差的方向，斜率的绝对值决定标准误的倍数。若 $\tau>0$ 且 $g'(\theta)\ne0$，可用 $|g'(\theta)|\tau$ 标准化放大后的误差。

### 11.2 补充推导：Taylor 展开与 Slutsky

$\sqrt n(T_n-\theta)$ 依分布收敛，因此在概率意义下有界，即 $O_p(1)$。除以 $\sqrt n$ 得 $T_n\xrightarrow p\theta$。可微性给出

$$g(\theta+h)-g(\theta)=g'(\theta)h+h\,r(h),\qquad r(h)\to0.$$

令 $h=T_n-\theta$，并令 $r(0)=0$。由连续映射，$r(T_n-\theta)\xrightarrow p0$。于是

$$\sqrt n[g(T_n)-g(\theta)]
=\sqrt n(T_n-\theta)\,[g'(\theta)+r(T_n-\theta)]
\xrightarrow d g'(\theta)Z,\quad Z\sim N(0,\tau^2).$$

这说明连续映射负责传递估计目标，一阶展开负责传递误差，Slutsky 负责处理趋于常数的因子。

### 11.3 标准误的估计与零导数

若 $\hat\tau_n\xrightarrow p\tau$ 且 $g'$ 在 $\theta$ 连续，可用 $|g'(T_n)|\hat\tau_n/\sqrt n$ 估计标准误。若 $g'(\theta)=0$，一阶结论是 $\sqrt n[g(T_n)-g(\theta)]\xrightarrow p0$，此时一阶标准化的分母为零。

**补充例：** 取 $g(t)=t^2$、$\theta=0$，且 $\sqrt n T_n\xrightarrow d N(0,\tau^2)$。直接对放大后的量平方，

$$nT_n^2=(\sqrt nT_n)^2\xrightarrow d\tau^2\chi^2(1).$$

这个例子要放大 $n$ 倍才看到非退化波动。Delta 方法给出的近似中心也不能直接当作有限样本期望，非线性变换可能引入偏差。

---

## 第十二节　Delta 方法的课件例题

### 12.1 例 5.11　样本均值的指数（PDF 第 74 页）

$X_i$ i.i.d.，$E(X_i)=\mu$、$0<\operatorname{Var}(X_i)=\sigma^2<\infty$，令 $W_n=e^{\bar X_n}$。

1. 由 LLN 与连续映射，$W_n\xrightarrow p e^\mu$，同样也有几乎处处收敛。
2. 由 CLT，$\sqrt n(\bar X_n-\mu)\xrightarrow d N(0,\sigma^2)$。取 $g(x)=e^x$，$g'(\mu)=e^\mu$，于是

   $$\sqrt n(W_n-e^\mu)\xrightarrow d N(0,e^{2\mu}\sigma^2),\qquad
   W_n\approx N(e^\mu,e^{2\mu}\sigma^2/n).$$

近似标准误是 $e^\mu\sigma/\sqrt n$。**补充对照：** 若原样本本身正态，$W_n$ 的有限样本精确分布为对数正态，精确期望为 $\exp(\mu+\sigma^2/(2n))$。这时仍可以用 Delta 方法描述大样本下中心附近的波动。

### 12.2 课件补充例　样本均值的对数（PDF 第 75 页）

沿用 i.i.d. 抽样，并设 $X_i>0$ 几乎处处、$\mu>0$，方差 $\sigma^2$ 有限且为正。$\bar X_n>0$ 保证可以取对数。由 LLN 与连续映射，$\log\bar X_n\xrightarrow p\log\mu$。取 $g(x)=\log x$，$g'(\mu)=1/\mu$，得

$$\sqrt n(\log\bar X_n-\log\mu)\xrightarrow d N(0,\sigma^2/\mu^2).$$

理论标准误约为 $\sigma/(\mu\sqrt n)$。用样本标准差 $s_n$ 与样本均值替代未知量，得到

$$\widehat{\operatorname{se}}(\log\bar X_n)=\frac{s_n}{\bar X_n\sqrt n}.$$

当 $\mu>0$ 时，Slutsky 还给出 $\sqrt n(\log\bar X_n-\log\mu)/(s_n/\bar X_n)\xrightarrow d N(0,1)$，在 $s_n=0$ 时可按第五节补定义。

---

## 第十三节　公式速查、解题路线与自测

### 13.1 公式速查

| 已知条件或目标 | 可用公式或结论 |
|---|---|
| $X\ge0$，知道 $E(X)$ | $P(X\ge a)\le E(X)/a$，$a>0$ |
| 知道均值 $\mu$ 与方差 $\sigma^2$ | $P(\lvert X-\mu\rvert\ge a)\le\sigma^2/a^2$ |
| $\operatorname{Var}(\bar X_n)\to0$ | $\bar X_n-E(\bar X_n)\xrightarrow p0$ |
| i.i.d. 且 $E\lvert X_1\rvert<\infty$ | $\bar X_n\xrightarrow{\mathrm{a.s.}}\mu$，从而 $\bar X_n\xrightarrow p\mu$ |
| i.i.d. 且 $0<\sigma^2<\infty$ | $(S_n-n\mu)/(\sigma\sqrt n)\xrightarrow d N(0,1)$ |
| 总和和均值的标准差 | $\operatorname{SD}(S_n)=\sigma\sqrt n$，$\operatorname{SD}(\bar X_n)=\sigma/\sqrt n$ |
| $Y_n\sim\operatorname{Bin}(n,p_n)$，$np_n\to\lambda>0$ | $Y_n\xrightarrow d\operatorname{Poisson}(\lambda)$ |
| 整数 $Y$ 以 $N(m,s^2)$ 近似 | $P(Y\le k)\approx\Phi((k+0.5-m)/s)$ |
| $X_n\xrightarrow d X$、$Y_n\xrightarrow p c$ | 和、积、商可将 $Y_n$ 替为常数 $c$ 后取分布极限，取商要求 $c\ne0$ |
| $\sqrt n(T_n-\theta)\xrightarrow d N(0,\tau^2)$，$g$ 在 $\theta$ 可微 | $\sqrt n[g(T_n)-g(\theta)]\xrightarrow d N(0,[g'(\theta)]^2\tau^2)$ |

### 13.2 从题目关键词选择方法

1. **“至少”“至多”，只给出矩。** 先写所求事件，非负量用 Markov，离均值的距离用 Chebyshev。取补集前核对边界。
2. **“证明一致”或“平均值长期稳定”。** 先找 $E(\bar X_n)$ 的极限，再检查能否用弱律、强律或方差判据。
3. **“近似概率”“分位数”“预算”。** 先写目标随机量及其单位，求其均值与标准差。整数计数先确定是否需要半格修正，稀有事件先检查 Poisson 近似条件。
4. **“方差未知”。** 先证明用于标准化的估计量收敛到正的常数，再用 Slutsky。
5. **“非线性变换后求近似分布或标准误”。** 写出原始渐近分布，确定 $g$ 的定义域，算 $g'(\theta)$。若一阶导数为零，检查更高阶项。

### 13.3 补充自测

1. 非负随机变量 $X$ 满足 $E(X)=6$。给出 $P(X\ge24)$ 的上界，并构造一个达到该上界的分布。
2. $E(X)=10$、$\operatorname{Var}(X)=9$。给出 $P(4<X<16)$ 的下界。
3. 为了让 $P(|\hat p_n-p|\ge0.05)\le0.10$，用 Chebyshev 给出对所有 $p$ 有效的样本量。
4. 令 $X_n=1/n$。它以哪几种方式收敛到 $0$？为什么 $F_n(0)\ne F(0)$ 不妨碍分布收敛？
5. $X_n$ 与 $Y_n$ 各自依分布趋向标准正态。给出一个其和没有分布极限的构造。
6. $X_i$ 独立、$E(X_i)=(-1)^i$，且 $\operatorname{Var}(X_i)=i$。直接用 Chebyshev 的方差判据能否证明 $\bar X_n\xrightarrow p0$？
7. $\bar X_n$ 来自均值 $20$、方差 $25$ 的 i.i.d. 样本，$n=100$。用 CLT 近似 $P(\bar X_n>20.5)$。
8. $Y\sim\operatorname{Bin}(100,0.4)$。用带连续性修正的正态近似计算 $P(Y\le35)$。
9. 若 $Y_n\sim\operatorname{Bin}(n,2/n)$（$n\ge2$），求 $P(Y_n=0)$ 的极限，并用二项式公式核对。
10. 若 $\sqrt n(T_n-\theta)\xrightarrow d N(0,4)$、$\theta=2$，求 $\log T_n$ 的渐近分布和近似标准误。设 $T_n>0$。
11. 若 $\sqrt n T_n\xrightarrow d N(0,9)$，求 $\sqrt n T_n^2$ 与 $nT_n^2$ 的极限分布。
12. 模拟估计 $\pi$ 时，使用 $Y=4\sqrt{1-U^2}$ 与 $W=4\,1_{\{U^2+V^2\le1\}}$，其中 $U,V$ 独立且均匀。独立重复次数相同，哪个样本均值的方差较小？

### 13.4 自测解析

1. Markov 给出 $P(X\ge24)\le6/24=1/4$。取 $P(X=24)=1/4$，$P(X=0)=3/4$，均值为 $6$ 且尾概率为 $1/4$。
2. $P(4<X<16)=1-P(|X-10|\ge6)\ge1-9/36=3/4$。
3. $P(|\hat p_n-p|\ge0.05)\le1/[4n(0.05)^2]=100/n$。取 $n\ge1000$ 即可，这是由通用界得到的充分条件。
4. 常数序列逐点收敛，因此也几乎处处、依概率、依分布收敛。极限的 CDF 在 $0$ 处有跳跃，定义只检查其连续点。
5. 令 $X_n=Z$、$Y_n=(-1)^nZ$，$Z\sim N(0,1)$。和在奇数项恒为零，在偶数项服从 $N(0,4)$，所以不存在统一的分布极限。
6. 不能直接用此判据。虽然 $E(\bar X_n)\to0$，但 $\operatorname{Var}(\bar X_n)=n^{-2}\sum_{i=1}^ni=(n+1)/(2n)\to1/2$。仅凭给出的信息也不能保证收敛。例如各 $X_i\sim N((-1)^i,i)$ 且独立时，$\bar X_n$ 依分布趋向 $N(0,1/2)$。
7. 标准误为 $5/\sqrt{100}=0.5$，所以 $P(\bar X_n>20.5)\approx1-\Phi(1)=0.15866$。
8. $m=40$、$s=\sqrt{24}$。$P(Y\le35)\approx\Phi((35.5-40)/\sqrt{24})\approx0.1792$。
9. Poisson 极限是 $\operatorname{Poisson}(2)$，$0.5$ 是极限 CDF 的连续点，而 $\{Y_n=0\}=\{Y_n\le0.5\}$，故极限为 $e^{-2}$。直接计算 $(1-2/n)^n\to e^{-2}$。
10. $g'(2)=1/2$，所以 $\sqrt n(\log T_n-\log2)\xrightarrow d N(0,(1/2)^2\cdot4)=N(0,1)$，近似标准误为 $1/\sqrt n$。
11. 一阶导数为零，$\sqrt nT_n^2\xrightarrow p0$。而 $nT_n^2=(\sqrt nT_n)^2\xrightarrow d9\chi^2(1)$。
12. $E(Y)=E(W)=\pi$。由第七节，$\operatorname{Var}(Y)=32/3-\pi^2\approx0.7971$。单位正方形内落入四分之一圆的概率是 $\pi/4$，故 $\operatorname{Var}(W)=16(\pi/4)(1-\pi/4)=4\pi-\pi^2\approx2.6968$。各除以独立抽样次数即可比较，$Y$ 的样本均值方差更小。

---

## 附录 A　易错点与检查方法

| 容易写错的地方 | 检查方法 |
|---|---|
| 用 $E(X)$ 直接界定可取负值的 $X$ 的右尾 | 先变成 $X^+$、绝对值或平方，再检查阈值 |
| 把 Chebyshev 上界当成概率的等式 | 只有矩信息时保留不等号，已知分布时可直接算 |
| 交换 $\ge$ 与 $>$ 后取补集 | 特别检查离散分布在边界处是否有质量 |
| 分布收敛必须在所有 $x$ 点验证 | 只检查极限 CDF 的连续点 |
| 把依概率收敛直接当作逐路径收敛 | 区分单个时点的误差概率与未来所有时点的事件 |
| 看到两个边缘收敛就把它们相加 | 检查联合收敛，或确认一个极限是常数再用 Slutsky |
| 不同分布的观测一律围绕某个 $\mu$ | 先写出 $\frac1n\sum_iE(X_i)$，再检查该中心的极限 |
| 用 $\sigma^2$ 或 $\sigma^2/n$ 作标准化的分母 | 分母是目标变量的标准差，和为 $\sigma\sqrt n$，平均为 $\sigma/\sqrt n$ |
| 写成 $\bar X_n\xrightarrow d N(\mu,\sigma^2/n)$ | 有限样本写 $\approx$，极限写 $\sqrt n(\bar X_n-\mu)\xrightarrow d N(0,\sigma^2)$ |
| 连续性修正把两端都加 $0.5$ | 对闭区间 $a\le Y\le b$，左端减、右端加 |
| 看到 $n$ 大就使用正态近似 | 二项先检查成功和失败的期望计数，再考虑所求尾部 |
| Delta 方法的方差只乘 $g'(\theta)$ | 标准误乘 $\lvert g'(\theta)\rvert$，方差乘 $[g'(\theta)]^2$ |
| 导数为零时仍套用标准化 | 一阶极限退化，重新分析误差的尺度与主导项 |

## 附录 B　课件核对与阅读顺序

- PDF 实际为 80 页，前半段页脚标为总计 86 页，第 47 页起又出现类似“2/1”的编号。查找例题时请使用 PDF 阅读器的实际页码。
- 课件两次使用“例 5.6”。第 53 页是 Monte Carlo 积分，第 58 页是二项与 Poisson 的比较。讲义保留编号，并以标题和页码区分。
- 课件第 17 页已纠正正态尾概率 $P(|Z|\ge2)<0.04$ 的误写。正确值约为 $0.04550$。
- 第一遍可沿第 1、3、6、8、11 节掌握五个主干，再做第 2、7、9、10、12 节例题。第二遍用第 4、5 节的反例和第 13 节自测检查条件、尺度、边界与近似精度。
