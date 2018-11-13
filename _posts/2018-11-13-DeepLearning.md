---
layout: post 
title: (믿거나 말거나) 딥러닝 
---

딥러닝에 대해서 잘 모른다. 그래서 공부한다. 공부한 내용을 정리하는데 틀린내용이 있을 수 있다. 그래서 제목은 믿거나 말거나 딥러닝이다. 

### GAN 
- 우리가 관측한 자료 $\\{x_i\\}_ {i=1}^{n}$가 평균이 $500$이고 분산이 $5^2$인 정규분포 생성된다고 가정하자. 

- 제너레이터는 주어진 자료 $\\{x_i\\}_ {i=1}^{n}$로부터 generator's distribution $p_g(x)$를 알고 싶다. 즉 제너레이터의 목적은 
\begin{align}
p_g(x) \approx \frac{1}{\sqrt{5\times 2\pi}}\exp\left(\frac{-(x-500)^2}{2\times 5^2}\right)
\end{align}
가 되도록 $p_g(x)$를 학습하는 것이다. 제너레이터는 이러한 목적을 달성하기 위해서 평균이 0이고 분산이 1인 정규분포 $p_z(z)$에서 노이즈 $\\{z_i\\}_ {i=1}^{n}$를 발생시키고 노이즈로부터 $x_i$를 학습하는 MLP를 쌓는다. 즉 아래를 만족하는 적당한 함수 $G_{\theta_g}(z_i)$를 학습한다.  
\begin{align}
x_i \approx G_{\bf \theta_g}(z_i)
\end{align}
당연히 학습을 잘 했다면 $G_{\bf \theta_g}(z_i)=5\times z_i + 500$이 되도록 학습이 될 것이고 이때 ${\bf \theta_g}=(500,5)$가 된다. 

- 제너레이터와 별도로 디스크리미네이터는 입력으로 $\\{x_i\\}$ 혹은 $\\{G_{\bf \theta_g}(z_i)\\}$를 받는다. 편의상 이러한 자료를 $\\{y_i\\}$라고 하자. 즉 
\begin{align}
\\{y_i\\}:=\\{x_i\\} \cup \\{G_{\bf \theta_g}(z_i)\\}
\end{align}
$\\{x_i\\}$는 총 $n$개 있고, $\\{G(z_i;{\bf \theta_g})\\}$역시 총 $n$개가 있으므로 $\\{y_i\\}$는 $2n$개가 있을 것이다. 디스크리미네이터는 입력이 $\\{x_i\\}$일 경우에는 1을 출력하고 입력이 $\\{G_{\bf \theta_g}(z_i)\\}$일 경우에는 0을 출력하는 함수 $D_{\bf \theta_d}(y_i)$를 학습한다. 따라서 $D_{\bf \theta_d}(y_i)$가 자료 $\\{y_i\\}:=\\{x_i\\} \cup \\{G_{\bf \theta_g}(z_i)\\}$으로부터 파라메터 $\theta_d$를 잘 학습했다면 $D_{\bf \theta_d}(y_i)$는 아래와 같은 성질을 가져야 한다. <br/><br/>
> $y_i \in \\{x_i\\}$이면 $D_{\bf \theta_d}(y_i) \approx 1$이다. <br/><br/>
> $y_i \in \\{G_{\bf \theta_g}(z_i)\\}$이면 $D_{\bf \theta_d}(y_i) \approx 0$이다. 

- 디스크리미네이터의 관점에서 보자. 디스크리미네이터는 1) $D_{\bf \theta_d}(G_{\bf \theta_g}(x_i))$의 값들이 작을 수록 2) $D_{\bf \theta_d}(G_{\bf \theta_g}(z_i))$의 값들이 클수록 학습이 잘 되었다고 볼 수 있다. 따라서 디스크리미네이터는 아래식을 만족하는 $\bf \theta_d$를 찾고 싶어한다. 이때 $\bf \theta_g$는 고정된 값이다. 
\begin{align}
\underset{\bf \theta_d}{\operatorname{argmin}}\frac{1}{n}\sum_{i=1}^{n} \left[ \log D_{\bf \theta_d}(x_i) +\log \left(1- D_{\bf \theta_d}(G_{\bf \theta_g}(z_i)) \right) \right] 
\end{align}

- 반면에 제너레이터는 $D_{\bf \theta_d}(G_{\bf \theta_g}(z_i))$값들이 커야지 학습이 잘 된 것이고 볼 수 있다. 즉 제너레이터는 아래식을 만족하는 $\bf \theta_g$를 찾고 싶어한다. 이때도 $\bf \theta_d$는 고정된 값이다.  
\begin{align}
\underset{\bf \theta_d}{\operatorname{argmin}}\frac{1}{n}\sum_{i=1}^{n} \log \left(1-D_ {\bf \theta_d}(G_{\bf \theta_g}(z_i))\right)
\end{align}

- 우리가 원하는 것은 <br/><br/>
***"굉장히 성능이 좋은 디스크리미네이터조차도 구분하기가 쉽지않은 가짜 샘플을 만드는 제너레이너를 찾는 것"***<br/><br/>
이다. 따라서 요걸 달성하기 위해서는 아래를 구하면 된다.    
\begin{align}
\underset{G_{\bf \theta_g}}{\operatorname{argmin}} \max_{D_{\bf \theta_d}} V(D_{\bf \theta_d},G_{\bf \theta_g})
\end{align}
여기에서  
\begin{align}
V(D_{\bf \theta_d},G_{\bf \theta_g})=E_{x \sim p_{data}}[\log D_{\bf \theta_d}(x)] + E_{z \sim p_z(z)}[\log (1-D_{\bf \theta_d}(G_{\bf \theta_g}(z))]
\end{align}
이다. 

- 보면 알겠지만 $\frac{1}{n} \sum_{i=1}^{n}\log D_{\bf \theta_d}(x_i)$는 $E_{x \sim p_{data}}[\log D_{\bf \theta_d}(x)]$ 의 샘플버전이고 $\frac{1}{n} \sum_{i=1}^{n} \log \left(1- D_{\bf \theta_d}(G_{\bf \theta_g}(z_i)) \right)$은 $ E_{z \sim p_z(z)}[\log (1-D_{\bf \theta_d}(G_{\bf \theta_g}(z))]
\end{align}$의 샘플버전이다. 

- 




- 이 식이 생각보다 오묘하다. $\max_{D} V(D,G)$가 어떻게 달성되는지 생각하여보자. 사실상 $\max_{D} V(D,G)$는 오로지 디스크리미네이터의 입장에서 본 로스함수이다. 디스크리미네이터는 1) 매우 일을 잘하는 경우: 즉 진짜 데이터와 가짜 데이터를 너무 잘 구분하는 경우 2) 일을 안하는 경우: 진짜 데이터와 가짜데이터를 전혀 구분하지 못하는 경우 그니까 그냥 랜덤으로 찍는다든가.. 3) 매우 일을 못하는 경우: 진짜 데이터와 가짜 데이터를 완벽하게 반대로 구분하고 있는 경우가 있을 수 있다. 다시 $V(D,G)$함수를 살펴보자. 
\begin{align}
V(D,G)=E_{x \sim p_{data}}[\log D(x)] + E_{z \sim p_z(z)}[\log (1-D(G(x))]
\end{align}
$V(D,G)$ 최대가 되는 경우는 1) 과 3)이다. 

