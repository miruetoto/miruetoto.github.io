---
layout: post 
title: (믿거나 말거나) 딥러닝 
---

딥러닝에 대해서 잘 모른다. 그래서 공부한다. 공부한 내용을 정리하는데 틀린내용이 있을 수 있다. 그래서 제목은 믿거나 말거나 딥러닝이다. 

### GAN 
- 우리가 관측한 자료 $\\{x_i\\}_ {i=1}^{n}$가 평균이 $500$이고 분산이 $5^2$인 정규분포 생성된다고 가정하자. 

- 제너레이터는 주어진 자료 $\\{x_i\\}_ {i=1}^{n}$로부터 generator's distribution $p_g(x)$를 알고 싶다. 즉 제너레이터의 목적은 
\begin{align}
p_g(x)=\frac{1}{\sqrt{5\times 2\pi}}\exp\left(\frac{-(x-500)^2}{2\times 5^2}\right)
\end{align}
를 학습하는 것이다. $G$는 이러한 목적을 달성하기 위해서 평균이 0이고 분산이 1인 정규분포 $p_z(z)$에서 *노이즈* $\\{z_i\\}_ {i=1}^{n}$를 발생시키고 *노이즈* 로 부터 $x_i$를 학습하는 MLP를 쌓는다. 즉 아래를 만족하는 적당한 함수 $G$를 학습한다.  
\begin{align}
x_i \approx G(z_i; {\bf \theta_g})
\end{align}
당연히 $G(z_i)=5\times z_i + 500$이 되도록 학습이 될 것이고 이때 ${\bf \theta_g}=(500,5)$가 된다. 

- 제너레이터와 별도로 디스크리미네이터는 입력으로 $\\{x_i\\}$ 혹은 $\\{G(z_i;{\bf \theta_g})\\}$를 받는다. 그리고 입력이 $\\{x_i\\}$일 경우에는 1을 출력하고 입력이 $\\{G(z_i;{\bf \theta_g})\\}$일 경우에는 0을 출력하는 MLP를 쌓아 함수 $D$학습한다. 따라서 제너레이터가 학습한 함수 $D$는 아래와 같은 성질을 가진다. 
\begin{align}
\begin{cases}
D(x) \approx 1, ~x \in \\{x_i\\} \\ 
D(x) \approx 0, ~x \in \\{G(z_i;{\bf \theta_g})\\}
\end{cases
\end{align}
