---
layout: post 
title: (얕은) 딥러닝 
---

### About this document
- 이 포스트는 딥러닝에 대하여 다룬다. 
- 이 포스트는 계속 작성중인 문서이다. 

### Overview
***신경망의 역사***
- 1943년에 최초의 신경망이 매컬럭(Maculloch)과 피츠(Pits)에 의해 제안되었다.  
- 1958년에 로젠블(Rosenblatt)이 퍼셉트론을 제안하였다. 
- 1960년대에는 신경망으로 모든 문제를 해결할것처럼 과장되어 학계와 매스컴의 주목을 받았다. 
- 1969년에 민스키(Minky)와 페퍼트(Papert)는 퍼셉트론의 한계를 수학적으로 증명하였다. 퍼셉트론은 선형분류기에 불과하므로 XOR 분류도 하지 못한다고 하였다. 이후에 신경망 연구는 크게 퇴조하였다. 
- 1986년에 루멜하트(Rumelhart)와 동료들이 은닉층을 가진 다층 퍼셉트론과 오류 역전파알고리즘을 제안하였다. 이 신경망이 필기숫자인식과 같은 문제를 훌륭하게 해결하여 이후에 다시 신경망연구가 활기를 찾았다. 하지만 역전파알고리즘은 층수가 많은 깊은 신경망일수록 학습이 되지 않는 문제가 생겼다. 정확히 말하면 트레이닝에러는 줄어들지만 테스트에러는 줄어들지않는 과적합 문제가 생겼다. 
- 1990년대에 들어 SVM이 신경망보다 좋은 성능을 보여 신경망은 잠시 SVM에 밀리는 형국이 되었다. 
- 현재는 다시 신경망이 기계학습의 주류로 자리잡았다. 

***신경망의 종류***
- 앞먹임신경망과 순환신경망: DNN(=DMLP)과 CNN과 같은것을 feedforword 신경망이라 하며 RNN이나 LSTM과 같은것을 순환신경망이라고 한다. 
- 얕은신경망과 깊은신경망: 층이 1~2개정도를 얕은신경망이라 하며 은닉층이 두꺼운 것을 깊은신경망이라고 한다. 
- 결정론신경망과 스토캐스틱신경망: 결정론 신경망에서는 입력이 같으면 항상 같은 출력이 나온다. 계산식에 임의성이 없다. 스토캐스틱신경망은 계산식에 난수가 들어가 입력이 같아도 매번 다른 출력이 나온다. RBM과 DBN이 대표적인 스토캐스틱신경망이다. 결정론적신경망은 분류나 회귀와 같은 예측만 가능하지만 스토캐스틱신경망은 예측뿐아니라 유사한 패턴을 생성하는 생성모델로도 활용가능하다. 

### DNN 
- DMLP라 부르기도 한다. 

- 앞먹임신경망에 대하여 논의하기 전에 유닛이 무엇인지 아는게 편함. 
하나의 obs $x[i,]$이 있다고 하자. 여기에서 $x[i,]$는 3개의 성분을 가지고 있다고 하자. 즉 $$x[i,]=[x[i,1],x[i,2],x[i,3]].$$ 
유닛을 하나만 생각하자. (\textcolor{red}{유닛이 하나라는 것은 $y_i$의 차원이 1차원이라는것임!!})
하나의 유닛은 입력 $u[i,1]$와 출력 $z[i,1]$로 이루어져 있음. 여기에서 1은 첫번째 유닛이라는 소리임.
$$u[i,1]=x[i,1]w[1,1]+x[i,2]w[2,1]+x[i,3]w[3,1]+b[1]$$
와 같이 이루어져 있고 출력은
$$z[i,1]=f(u[i,1])$$
와 같은 형태임. 

- 유닛이 2개면 어떻게 생겼을까? (일단 유닛이 2개라는것은 출력의 차원이 2차원이라는 의미이다)
$$u[i,1]=x[i,1]w[1,1]+x[i,2]w[2,1]+x[i,3]w[3,1]+b[1]$$
$$u[i,2]=x[i,1]w[1,2]+x[i,2]w[2,2]+x[i,3]w[3,2]+b[2]$$
유닛을 일렬로 세우면 층이라고함. 즉 위에서 $u[1,1],u[2,1]$를 일렬로 세우면 이것이 층이된다. 

- 관측치가 $n$개이고 $X$의 feature가 1024개 있다고 하자. $Y$의 feature는 10개 있다고 하자. 층은 1개만 쌓자. $X$의 차원은 $n\times 1024$임. $W$의 차원은 $1024 \times 10$이고 $U$의 차원은 $n \times 10$이 된다. 식으로는 아래와 같이 된다.
$$U_{n\times 10}=X_{n\times 1024}W_{1024\times 10}$$
이때 $u[i,]$는 가로로 10개의 값이 들어가 있는 메트릭스이다.

- 활성화 함수 $f$는 벡터 $[u[i,1]\dots,u[i,10]$와 벡터 $[z[i,1],\dots,z[i,10]]$사이의 맵핑을 정의하는 함수이다. 즉 $f:\mathbb{R}^{10} -\rightarrow \mathbb{R}^{10}$임. 하지만 보통 벡터에서 벡터로 맵핑되는 경우는 거의 없으며 스칼라에서 스칼라로 맵핑되거나 (항등함수, 로지스틱함수, 렐루) 벡터에서 스칼라로 맵핑(맥스아웃함수,소프트맥스)된다. 
	1. 항등함수: $z[i,1]=u[i,1]$. 
	2. 로지스틱함수: $z[i,1]=\frac{1}{1+e^{-u[i,1]}}$. 
	3. 소프트맥스함수: $z[i,1]=\frac{e^{-u[i,1]}}{sum(e^{-u[i,]})}$

- 다시한번 말하지만 항등함수와 로지스틱함수는 $z[i,1]$의 값을 구하는 오직 $u[i,1]$값만을 필요로 하지만 소프트맥스함수는 $z[i,1]$의 값을 구하는데 $u[i,1],\dots u[i,10]$의 값을 모두 필요로 한다. 즉 항등함수와 로지스틱 함수는 모두 $f:\mathbb{R} \rightarrow \mathbb{R}$이고, 소프트맥스함수는 $f:\mathbb{R}^{10}\rightarrow \mathbb{R}$이다. 

- 층이 여러층 있을경우 층마다 다른활성화함수를 쓰는건 가능하다. 예를들어 1층에서 시그모이드를 쓰고 2층에서 렐루를 쓸 수 있음. 

- 앞먹임 신경망의 정의는 아래와 같음. 

1. 유닛은 인접한 층에서만 결합한다 : 즉 1층의 유닛은 2층의 유닛과 결합할수 있지, 1층과 3층이 바로 결합할 수 없다.

2. 정보는 입력에서 출력으로만 흐른다 : 1층의 유닛 $u_1$과 $u_2$간의 정보교환은 없다. 이게 있으면 RNN임. 

- 잉여성에 대하여 설명하겠음. 잉여성은 함수의 입력이 바뀌어도 출력이 변하지 않는 현상을 이야기함. 무슨소리냐. 이해를 위해서 다클래스를 분류하는 예제를 생각하겠음. 
38*38픽셀을 가진 MNIST 자료를 상상하여 보자. class가 10개인 분류문제이므로, $y_i$는 길이가 10인 벡터이다. $L$개의 층을 쌓았다고 가정하자. 
$$x[i,]=[x[i,1],\dots,x[i,32*32]]$$
$$y[i,]=[y[i,1],y[i,2],\dots,y[i,10]]=[z^{(L)}[i,1],\dots,z^{(L)}[i,10]]$$
활성화함수를 소프트맥스라고 가정하면 
$$z^{(L)}[i,1]=\frac{\exp\left(-u^{(L)}[i,1]\right)}{sum\left(\exp\left(-u^{(L)}[i,]\right)\right)}$$
와 같이 된다. 이 함수는 특이하게도 
$$u^{(L)}[i,] \leftarrow u^{(L)}[i,]+777$$
과 같이 하여도 출력 $z^{(L)}[i,1]$의 값이 변하지 않는데 이러한 성질을 잉여성이라고 한다. (함수의 입력이 바뀌어도 출력이 바뀌지 않음.)
\memo (잉여성)
$$z^{(L)}[i,1]
=\frac{\exp\left(-u^{(L)}[i,1]\right)}{sum\left(\exp\left(-u^{(L)}[i,]\right)\right)}
=\frac{\exp\left(-u^{(L)}[i,1]+777\right)}{sum\left(\exp\left(-u^{(L)}[i,]+777\right)\right)}$$

- 잉여성이 왜 문제임? 잉여성이 있으면 $W^{(L)}$을 구하기가 어려움. 왜냐하면 로칼미니멈에 빠지기 쉽기 때문임. 이러한 잉여성을 해결하는 방법은 1) 가중치 $W$에 제약을 주거나 2) 유닛의 입력 $u[i,k]$의 값을 임의로 0으로 만드는것임(이러면 로칼미니멈에서 탈출가능). 


### 딥러닝기초  
- 


### 딥러닝 최적화



### 순환신경망 

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

- 디스크리미네이터의 관점에서 보자. 디스크리미네이터는 1) $D_{\bf \theta_d}(G_{\bf \theta_g}(z_i))$의 값들이 작을 수록 2) $D_{\bf \theta_d}(x_i)$의 값들이 클수록 학습이 잘 되었다고 볼 수 있다. 따라서 디스크리미네이터는 아래식을 만족하는 $\bf \theta_d$를 찾고 싶어한다. 이때 $\bf \theta_g$는 고정된 값이다. 
\begin{align}
\underset{\bf \theta_d}{\operatorname{argmin}}\frac{1}{n}\sum_{i=1}^{n} \left[ \log D_{\bf \theta_d}(x_i) +\log \left(1- D_{\bf \theta_d}(G_{\bf \theta_g}(z_i)) \right) \right] 
\end{align}

- 반면에 제너레이터는 $D_{\bf \theta_d}(G_{\bf \theta_g}(z_i))$값들이 커야지 학습이 잘 된 것이고 볼 수 있다. 즉 제너레이터는 아래식을 만족하는 $\bf \theta_g$를 찾고 싶어한다. 이때 $\bf \theta_d$는 고정된 값이다.  
\begin{align}
\underset{\bf \theta_d}{\operatorname{argmin}}\frac{1}{n}\sum_{i=1}^{n} \log \left(1-D_ {\bf \theta_d}(G_{\bf \theta_g}(z_i))\right)
\end{align}

- 우리가 원하는 것은 <br/><br/>
***"굉장히 성능이 좋은 디스크리미네이터조차도 구분하기가 쉽지않은 가짜 샘플을 만드는 제너레이너를 찾는 것"***<br/><br/>
이다. 이안굿펠로우는 요걸 달성하기 위해서 아래를 구하면 된다고 주장한다.     
\begin{align}
\underset{G_{\bf \theta_g}}{\operatorname{argmin}} \max_{D_{\bf \theta_d}} V(D_{\bf \theta_d},G_{\bf \theta_g})
\end{align}
여기에서  
\begin{align}
V(D_{\bf \theta_d},G_{\bf \theta_g})=E_{x \sim p_{data}}[\log D_{\bf \theta_d}(x)] + E_{z \sim p_z(z)}[\log (1-D_{\bf \theta_d}(G_{\bf \theta_g}(z))]
\end{align}
이다. 보면 알겠지만 <br/><br/>
1) $\frac{1}{n} \sum_{i=1}^{n}\log D_{\bf \theta_d}(x_i)$는 $E_{x \sim p_{data}}[\log D_{\bf \theta_d}(x)]$ 의 샘플버전이고<br/><br/>
2) $\frac{1}{n} \sum_{i=1}^{n} \log \left(1- D_{\bf \theta_d}(G_{\bf \theta_g}(z_i)) \right)$는 $ E_{z \sim p_z(z)}[\log (1-D_{\bf \theta_d}(G_{\bf \theta_g}(z))]$의 샘플버전이다. 따라서 이안굿펠로우의 주장은 매우 타당하다. 

- 즉 <br/><br/>
1) $\underset{\bf \theta_d}{\operatorname{argmin}}\frac{1}{n}\sum_{i=1}^{n} \left[ \log D_{\bf \theta_d}(x_i) +\log \left(1- D_{\bf \theta_d}(G_{\bf \theta_g}(z_i)) \right) \right]$ <br/><br/>
2) $\underset{\bf \theta_d}{\operatorname{argmin}}\frac{1}{n}\sum_{i=1}^{n} \log \left(1-D_ {\bf \theta_d}(G_{\bf \theta_g}(z_i))\right)$ <br/><br/>
를 최소화하는 $\bf \theta_d$, $\bf \theta_g$를 반복적으로 찾아가면서 업데이트하면 쉽게 문제를 해결할 수 있다. 

### BEGAN 
- BEGAN을 이해하기 전에 Wasserstein-디스턴스를 먼저 이해해야 한다. Wasserstein-디스턴스는 두 분포함수 $F_{X}(x)$와 $G_{Y}(x)$가 얼마나 유사한지를 측정하는 함수이다. 여기에서 분포함수 $F_X(x)$란 확률변수 $X$가 정의되었을 경우 $F_X(x)=P(X\leq x)$를 만족하는 $\mathbb{R} \rightarrow [0,1]$인 함수이다. 참고로 임의의 확률변수 $X$에 대한 분포함수는 항상 존재한다(확률분포함수는 항상 존재하지는 않음).  

- 각설하고 $X \sim N(0,1)$이고 $Y \sim N(300,5)$이라고 하자. 확률변수 $X$와 $Y$에 의해서 유도된 분포함수를 $F_X(x)$, $F_Y(y)$라고 하자. 두분포함수 $F_X(x)$, $F_Y(y)$의 와썰스테인-디스턴스는 아래와 같이 정의된다. 
\begin{align}
W(F_X(x),F_Y(y)):= \inf_ {F_{XY}} E_{F_{XY}}\|X-Y\|.  
\end{align}
여기에서 $F_{X,Y}(x,y)$는 확률벡터 $c(X,Y)$의 결합확률 밀도함수이다. $F_{X,Y}(x,y)$는 다양한 형태를 가질수 있다. 왜냐하면 $c(X,Y)$의 분포가 다양한 모양을 가질 수 있기 때문이다. 만약에 $X$와 $Y$가 독립이면 
\begin{align}
c(X,Y) \sim N\left(\begin{bmatrix} 0 \\\\ 300 \end{bmatrix}, \begin{bmatrix}1 & 0 \\\\ 0 & 25 \end{bmatrix} \right)
\end{align}
이 될 것이다. 독립이 아니면 $\rho$값에 따라서 아래와 같은 형태를 가질것이다. 
\begin{align}
c(X,Y) \sim N\left(\begin{bmatrix} 0 \\\\ 300 \end{bmatrix}, \begin{bmatrix}1 & 5\rho \\\\ 5\rho & 25 \end{bmatrix} \right)
\end{align}
따라서 $

