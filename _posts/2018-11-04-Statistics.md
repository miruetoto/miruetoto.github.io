---
layout: post
title: (매우 얕은) 통계학
---
본 포스팅에서는 통계학에 대한 전반적인 내용을 소개한다. 매우 많은 범위를 가볍게만 훑을 생각이라 제목은 매우 얕은 통계학이다. 본 포스팅에 포함되는 내용의 범위는 1) 통계학과라면 응당 알아야할 내용 (기본 교양같은거) 2) 그중에서 이론통계(=수리통계)와 확률론계열을 제외한 부분이다. 따라서 회귀분석류를 포함한 대학원 응용통계 혹은 대학원 고급통계의 내용을 커버한다고 보면 될것이다. 

### 통계학의 과제
통계를 통하여 해결하고자 하는 문제는 아래와 같은 것들이 있다. 

***Regression***
- $y_i=f(x_i)+\epsilon_i$형태의 모델임. 
- $\\{(x_i,y_i)\\}_ {i=1}^{n}$에서 $f$를 학습하는 방식임. 
- 회귀는 결국 function estimation. 

***Classification***
- $y_i=f(x_i)+\epsilon_i$형태의 자료에서 $y_i=0$ 또는 $1$인 형태이므로 회귀모델로 볼 수 있음. 

***Anomaly detection***
- 주어진 입력표본 $\\{x_i\\}_ {i=1}^{n}$에 포함된 비정상적인 값을 발견하는 문제이다. 
- 밀집해있는 자료를 정상으로 간주하고 그 군집으로부터 멀리 떨어진 자료를 비정상으로 간주한다. (Line형태로 군집이 이루어지면 어쩔꺼야? ㅋㅋ) 

***Clustering*** 
- 표본간의 유사도를 측정하는 방법을 적절히 선택하는 것이 중요하다. 
- 이때 그래프라플라시안을 활용하면 좋을듯? smoothness개념 
- hst에서도 전체 smoothness를 정의하는 어떠한 방법이 있으면 좋겠네. Total variation의 개념과도 연결되는것 같다? 

***Dimensionality reduction***
- 입력차원 $\\{ cbind(x_{i1},\dots,x_{ip}) \\}_ {i=1}^{n}$의 차원이 매우 클때 그것을 낮은차원의 자료들 $\\{ cbind(z_ {i1},\dots,z_{ip'}) \\}_ {i=1}^{n}$로 바꾸는 방법
- 차원축소를 수행하는 연산이 선형이면 적당한 행렬 ${\bf T}_ {p \times p'}$를 사용하여 $cbind(z_{i1}, \dots, z_{ip'})=cbind(x_{i1},\dots,x_{ip'}){\bf T}$와 같은 방식으로 쓸 수 있음.

---

### 통계학의 계파 
위에 제시된 문제를 해결하는데에는 다양한 철학을 가진 학파가 있다. 

***Generative model vs Discriminative model***
- $28\times 28$-pixel 의 이미지자료가 있다고 하자. 따라서 이 경우 ${\bf X}_ {n\times 784}$가 된다. 
- $y_{n\times 1}$이라고 하고, $y \in \\{0,\dots,9\\}$라고 하자. 
- 어쨋든 ${\bf X}$와 $y$를 통하여 conditional pdf $f(y|{\bf X})$를 알 수 있다. 결국 분류문제는 아래식을 풀어서 $\hat{y}$을 구하는 과정으로 이해할 수 있다. 
  \begin{align}
  \hat{y}=\underset{y}{\operatorname{argmax}} f(y|{\bf X})
  \end{align}
- 그런데 위에서 $f(y|{\bf X})$를 최대화하는 대신에 $f({\bf X},y)$를 최대화해도 문제없는데 그 이유는 아래식이 성립하기 때문이다. 
  \begin{align}
  f(y|{\bf X})=\frac{f({\bf X},y)}{f({\bf X})} \propto f({\bf X},y)
  \end{align}
  이처럼 $\hat{y}$는 $f({\bf X},y)$를 최대화 하거나 $f(y|{\bf X})$를 최대화 함으로써 구할 수 있는데 $f({\bf X},y)$를 최대화 하여 구하자는 주의가 *Generative model*을 지지하는 사람들이고  $f(y|{\bf X})$를 최대화 하여 구하자는 사람들은 *Discriminative model*을 지지하는 사람들이다.  
- 일반적으로 $f({\bf X},y)$를 알면 $f(y|{\bf X})$를 쉽게 계산할 수 있지만(아래식참고) 반대는 불가능하므로 $f({\bf X},y)$를 아는게 더 어려운 일이다. 
  \begin{align}
  f(y|{\bf X})=\frac{f({\bf X},y)}{f({\bf X})}=\frac{f({\bf X},y)}{\sum_y f({\bf X},y)}
  \end{align}
- 따라서 더 구하기 힘든함수 $f({\bf X},y)$를 알아내서 $\hat{y}$를 구하는 것보다는 좀 더 구하기 쉬운 함수 $f(y \vert {\bf X})$ 를 알아낸 다음에 $\hat{y}$을 구하는 것이 더 효과적이다. 이것이 SVM을 창시한 뱁닉(Vapnik)의 아이디어이다. 


***Frequentis vs Bayesian***
- Frequentist는 $\theta$를 확률변수로 보지 않는다. (fixed paramater라고 생각함.)
- Bayesian은 $\theta$를 확률변수라고 생각한다. 
- 따라서 Frequentist는 $\theta$의 값을 MLE와 같은 방법으로 구하려고 하지만 Bayesian는 $\theta$의 (posterior) distribution 관심이 있다. 

---

### (선형) 모델링하는 방법
- $\\{(x_i,y_i)\\}_ {i=1}^{n}$을 관측하였다고 하자. 우리가 풀고 싶은 문제는
\begin{align}
y_i=f(x_i)+\epsilon_i
\end{align}
로 표현했을때 어색하지 않은 underlying function $f(x)$를 찾아내는 것이다. 이러한 $f(x)$를 찾으면 모델이 만들어 지고 결국 새로운 관측치 $x_{i^* }$에 대한 prediction을 할 수 있다. 

- 가장 기본적인 모델인 1차원 회귀식으로 부터 시작하자. 
\begin{align}
y_i=f(x_i)+\epsilon_i, ~~~ f(x)=\beta_0+x\beta_1
\end{align}
위의 모델은 디자인매트릭스를 $f(x)$를 설명하기 위한 basis를 $[1,x]$로 선택하였다. 

- 위의 모델을 좀 더 개신시켜 basis를 $[1,\cos x, \sin x, \cos 2x, \sin 2x, \dots, ]$와 같이 확장해볼 수도 있을 것이다. 이때 각각의 basis는 오소고날하다. 

- 위의 2가지 방법은 각각 어떠한 가정을 내포한다. 가령 
''$f(x)$는 $x$에 선형변환으로 만들어질 수 있다. (즉 $f(x)=\beta_0+\beta_1x$)'' 
라든가 하는식으로 말이다. 이말은 
\begin{align}
y_i=f(x_i)+\epsilon, 
\end{align}
와 같은 모델에서 $f$가 어떠한 형태를 가질것인지 미리 알고 있다고 생각한다는 말과 같다. 이처럼 $f$가 어떤 모양인지 미리 알고 접근하는 방법을 파라메트릭 모델이라고 한다. 그리고 보통 $f$의 모양을 결정하는 과정(즉 적절한 basis를 선택하는 과정)을 모델링이라고 한다. 

- $f$를 어떻게 모델링할지 감이 안 올 수도 있다. 즉 자료를 봤는데 선형의 모양을 가지는지 어떤지 감을 못잡겠는 경우이다. 이것을 바꾸어 말하면 $\\{y_i\\}$가 $\\{x_i\\}$의 어떤 space에 있는지 감을 못 잡겠다는 뜻이다. 혹은 모델링이 귀찮을 수도 있다. 이럴 경우 $f(x)$가 $x$의 어떤 특정스페이스 $\cal A$의 부분공간에 존재한다고 가정하고 그 특정스페이스 $\cal A$를 expansion할 수 있는 베이시스를 선택하여 문제를 풀 수 있다. 가령 예를들면
''$f(x)$가 어떤 공간에 있는지 모르겠는데 최소한 비숍스페이스의 부분공간에 있는것 같아'' 
라고 생각한다면 웨이블릿 베이시스를 선택하여 모델링 하는 것이다. 

- 보통위와 같은 접근법은 무한대의 basis를 활용한다. 많은 수학자들이 
"이런식으로 무한개의 basis를 활용하면 특정공간에 있는 어떠한 함수도 표현할 수 있어요~"
라는 식의 증명을 많이 해놓았는데 이러한 증명결과들을 적극적으로 활용하는 셈이다. 요렇게 $f$를 표현하는데 무한개의 basis를 활용하는 모델링을 semi-parametric이라고 한다. 

- 커널모델을 사용하여 자료를 표현하는 경우는 어떤가? 커널모델은 $f(x)$를 아래와 같이 가정하는 것으로 이해할 수 있다. 
\begin{align}
f(x)=\theta_1K_h(x,x_i)+\dots+\theta_n K_h(x,x_n)
\end{align}
특이한것은 $f(x)$를 설계할때 관측자료 $x_i$를 사용하였다는 점이다. 퓨리에 변환이 $f(x)$를 가정하는 방식
\begin{align}
f(x)=\sum_{k =0}^{\infty}\theta_k e^{i\omega kx}
\end{align}
과 비교하여 보면 퓨리에변환은 $f(x)$를 표현하는데 무한대에 가까운 숫자의 basis를 사용하였지만 입력자료 $x_i$를 basis에 활용하지는 않았다. 이처럼 입력값 $x_i$를 직접 basis를 설계하는데 활용하는 방식을 non-parametric이라고 한다. 

- 지금까지 살펴본 것은 모두 입력변수가 1차원일 경우에 basis를 선택하는 방법이었다. 즉 
\begin{align}
y_i=f(x_i)+\epsilon_i
\end{align}
와 같은 모형이었다. 입력변수가 2개일 경우는 어떻게 basis를 선택해야 하는가? 예를들어 ${\bf x}$가 $2\times2$ pixel로 이루어 졌다고 하자. 각각의 픽셀값은 ${\bf x}=[x11,x12,x21,x22]$으로 정의된다고 하자. 여기에서 $x11$은 왼쪽위의 pixel이라는 뜻이다. 모형은 아래와 같을 것이다. 

\begin{align}
y_i=f({\bf x}_ i) +\epsilon_i
\end{align}

- 이와 같은 경우 기저를 어떻게 잡아야 할까? 보통 이런 경우는 1) 일차원 기저를 적당히 확장하여 고차원 기저를 만들거나 2) 커널처럼 자료 $\\{x_i\\}$를 활용하여 의 고차원의 기저를 구하는 방법이 있다. 

- 여기에서 첫번째 방법(1차원 basis를 적당히 확장하는 경우)은 다시 아래와 같은 예가 있을 수 있다.
    - (multiplicative model) 고차원베이시스를 1차원베이시스들의 product로 표현할 수 있다는 관점임.

    - (additive model) 고차원베이시스를 1차원베이시스의 합으로 표현할 수 있다는 관점임. 
  
- 이때 multiplicative model이 골때린다. 이 모델은 쉽게 말하면 교호작용을 고려하는 모델로 볼 수있다. 예를들어 입력변수 ${\bf x}$가 4차원이고 각 차원을 2개의 파라메터(예를들면 $[1,x]$)로 표현하고 있으면 전체 필요한 파라메터 수는 $2^4$이다. 만약에 입력변수의 차원이 $10$이라고 하면 각 변수당 2개의 파라메터를 쓸때 $2^{10}=1024$개의 파라메터가 필요하다. 한마디로 망한 모델이라는 소리이다. 이처럼 입력변수의 차원에 대하여 파라메터의 수가 지수적으로 증가하는 현상을 차원의 저주라고 부른다. 그래서 일반적으로 Multiplicative model보다 Additive model을 고려하는 것이 좋다. 

- 이처럼 일반적으로 입력변수가 고차원일때에는 커널과 같은 넌파라메트릭 모델을 고려하는것이 차원의 저주를 피하기에 유리하다. 커널과 같은 경우를 예로 들어보자. $\\{ {\bf x} \\}_ {i=1}^{n}$를 관측하였다면, 
\begin{align}
f({\bf x})=\sum_{i=1}^{n} \theta_i K_h({\bf x},{\bf x}_ i)
\end{align}
와 같이 쓸 수 있다. 이때 
\begin{align}
{\bf x}_ i=[x11_i,x12_i,x21_i,x22_i]
\end{align}
이다. 입력변수의 차원에 상관없이 $n$개의 basis만 가지고서 $f({\bf x})$를 표현 할 수 있다. 

- 커널방법의 또 다른 장점은 $K({\bf x},{\bf x}_ i)$만 잘정의하면 어떠한 입력형태 $\bf x$에서도 동작한다는 것이다. 예를들면 입력 $\bf x$가 문자열, 트리, 그래프등인 경우에도 동작한다. 

- 지금까지 살펴본 모델은 모두 선형모델이다. 선형모델이라는 뜻은 $f(x)$를 아래와 같은 방식으로 표현한다는 의미이다. 
\begin{align}
f(x)=\sum coef \times basis 
\end{align}
여기에서 coef는 parameter로 이해해도 된다. 왜 우리는 선형모델을 가정할까? 선형모델을 가정하면 최소제곱법과 같은 방법을 활용하여 parameter를 매우 쉬운 연산만으로 구할 수 있다는 장점이 있다. 앞에서 살펴본 커널의 경우도 밴드윗을 $h$로 고정하고 중심도 $x_i$로 고정된 상태에서 $\theta_i$를 구하는것은 선형모델이다. (하지만 만약에 커널모델에서 $h$와 $\theta_i$를 동시에 구해야 한다면 이것은 비선형 방정식을 풀어야한다.)  

---

### (선형모델에서) Basis의 Coef를 구하기 
- 회귀분석류의 대부분의 방식은 본질적으로 2가지 단계로 귀결된다. 
  1. 모델링을 한다. (=basis를 선택한다) 
  
  2. 각 basis의 coef를 구한다. 
  
- 위의 1. 의 과정이 끝나면 즉 (선형) 모델링이 끝나면 아래와 같이 자료가 표현될것이다. 
\begin{align}
y_i=f(x_i)+\epsilon_i=\sum coef \times basis +\epsilon_i= \sum_{j=1}^{p} \theta_j B_j(x_i)+\epsilon_i
\end{align}
여기에서 $B_j(x)$는 원래 데이터를 가지고 만든 어떠한 basis이다. 그리고 $\theta_j$는 그러한 basis에 해당하는 coef이다. 귀찮으니까 그냥 앞으로 $B_j(x)=X[,j]$라고 생각하고 $\theta_j=\beta_j$라고 생각하자. 그러면 모든 (선형)모델은 아래와 같이 쓸 수 있다. 
\begin{align}
{\bf y}={\bf X\beta} +{\bf \epsilon}
\end{align}

- 이제 남은것은 2.의 과정 즉 coef $\bf \beta$를 구하는 것이다. 보통 LS방법으로 구하면 
\begin{align}
\bf \hat{\beta}=(X'X)^{-1}X'y
\end{align}
와 같이 된다. 

- 가끔 가다가 오차항의 분산이 일정하지 않을수도있다. 예를들어서 $i \in \\{1,\dots,500\\}$에서는 분산이 $1$인 정규분포를 따르고 $i \in \\{501,\dots,1000\\}$에서는 분산이 $2$인 정규분포를 따른다고 하자. 이 경우에도 
\begin{align}
\sum_{i=1}^{1000}(y_i-\hat{y}_ i)^2
\end{align}
을 최소화하는 아이디어는 좀 곤란하다. 기본적으로 $i=1,\dots,500$에서 $E(y_i-\hat{y}_ i)^2$와 $i=501,\dots,1000$에서 $E(y_i-\hat{y}_ i)^2$의 값은 다르기 때문이다. 뒤에 값이 앞의 값보다 2배정도 크기 때문에 뒤의 값의 loss를 우선적으로 줄이는 쪽으로 LSE가 구해질 가능성이 높다. 따라서 $i=501,\dots,1000$에 해당하는 loss를 구할때는 $\frac{1}{2}$씩 곱해보는 것이 더 현명할 수 있다. 이것이 WLS의 핵심아이디어이다. 

- 좀 더 살펴보자. 위의 예제에서 오차항의 분산은 $V({\bf \epsilon})=diag(1,\dots,1,2,\dots,2)$와 같은 형태가 된다. 적당한 행렬 ${\bf P}=diag(1,\dots,1,\frac{1}{\sqrt{2}},\dots,\frac{1}{\sqrt{2}})$을 가져와서 $\bf y=X \beta +\epsilon$의 양변에 곱하면 
\begin{align}
\bf Py=PX\beta+P\epsilon
\end{align}
이 된다. 그럼 이때 $V({\bf P \epsilon})=I$ 이다. 이제 분산이 똑같아 졌으니까 LSE를 써도 괜찮을 것 같다. LSE를 쓰면 
\begin{align}
\bf \hat{\beta}=(X'P'PX)^{-1}X'P'Py  
\end{align}
가 된다. ${\bf P'P}={\bf P^2}=diag(1,\dots,1,\frac{1}{2},\dots,\frac{1}{2})$가 된다. 이는 결국 loss함수를 
\begin{align}
\sum_{i=1}^{500} (y_i-\hat{y}_ i)^2+ \frac{1}{2} \sum_{i=501}^{1000} (y_i-\hat{y}_ i)^2
\end{align}
와 같이 설정하는 것과 동일한 효과를 준다. 

- 좀 더 일반적으로 $V({\bf \epsilon})={\bf \Sigma}$인 경우를 살펴보아도 $\bf y=X\beta + \epsilon$의 양변에 ${\bf \Sigma}^{-\frac{1}{2}}$를 곱해주면 문제가 간단하다. 문제는 ${\bf \Sigma}^{-\frac{1}{2}}$이 존재하느냐는 것이다. 이것은 잘 생각해보면 당연하다는 것을 알 수 있다. 우선 $\Sigma$는 *(real, symm,) positive definite*이다. 이러한 행렬을 편의상 *(real-symm)-pd* 행렬이라고 하자. 아래와 같은 사실이 있다.
<br/><br/>
***모든 (real-symm)-pd 행렬 $A_ {n \times n}$은 고유치가 모두 양수이고 고유벡터가 서로 정규직교하도록 분해할 수 있다. (그리고 역도 성립한다.)***<br/><br/>
이걸 잘 이용하면 1) $\Sigma$의 역행렬 $\Sigma^{-1}$이 존재한다. 2) $\Sigma^{-1}$역시 real-symm-pd이다. 3) $\Sigma^{-1}=\Sigma^{-\frac{1}{2}}\Sigma^{-\frac{1}{2}}$를 만족하는 $\Sigma^{-\frac{1}{2}}$이 존재함을 순차적으로 (매우쉽게) 보일 수 있다. 

- 즉 $\epsilon$의 분산구조가 어떠한 형태를 가지든 간에 그것이 *(real-symm)-pd*이기만 하면 위와 같은 방법으로 LSE를 구할 수 있다는 것을 의미한다.  이때 *(real-symm)*은 분산의 정의상 무조건 성립하는 것이고 가끔씩 $\epsilon$의 공분산행렬이 *pd*가 아니고 *semi_pd*가 되는 경우가 가끔 있는데 ($\epsilon$이 랜덤변수가 아니고 상수라든가 하는 경우) 이러한 경우만 조심하면 된다. 통계학에서는 그냥 분산이 *semi_pd*인 경우는 없다고 생각하는게 정신건강에 좋다. 

- 만약에 $\bf (X'X)^{-1}$가 존재하지 않는다면 어떻게 되는가? 본질적으로 이런 경우는 $\bf X$의 랭크가 $p$보다 작은 경우, 그래서 결국 $\bf X'X$의 랭크가 $p$보다 작게되어 역행렬을 못구하는 경우에 생긴다. 이러한 일은 1) $n<p$ 이거나 2) $\bf X$중에서 선형적으로 종속된 변수들이 있을 경우 자주 발생한다. 


---

### 비지도 기반 차원축소기법

- 차원축소란 입력차원 $\\{ {\bf x}_ i\\}_ {i=1}^{n}$의 차원이 매우 클때 그것을 낮은차원의 자료들 $\\{ {\bf z}_ i\\}_ {i=1}^{n}$로 바꾸는 방법을 말한다. 

- 차원축소를 수행하는 연산이 선형이면 적당한 행렬 ${\bf T}$를 사용하여 ${\bf z}_ i={\bf x}_ i{\bf T}$와 같은 방식으로 쓸 수 있다. 가령 예를 들어서 ${\bf x}_ i=[1,2,4,5,8]$과 같은 자료가 있다고 하자. 이때 ${\bf x}_ i$의 차원은 $1\times 5$이다. 그러면 ${\bf T}$를 $5\times 2$와 같은 행렬을 잡아와서 ${\bf z}_ i={\bf x}_ i{\bf T}$와 같이 쓸 수 있는데 이러면 ${\bf z}_ i$의 차원은 $1 \times 2$가 되고 ${\bf T}$는 5차원자료를 2차원으로 줄이는 변환이 된다. 좀 더 일반적으로는 아래와 같이 선형변환을 표현할 수 있다. 
\begin{align}
{\bf Z}_ {n\times p'} = {\bf X}_ {n \times p} {\bf T}_ {p \times p'} 
\end{align}

***주성분분석***

- 주성분 분석은 (1) ${\bf z}_ i$가 ${\bf x}_ i$의 정사영이라는 제약아래에서 (2) ${\bf z}_ i \approx {\bf x}_ i$가 최대한 만족하도록 하는 선형변환 ${\bf T}$를 찾고자 하는 기법이다. 여기에서 (1)은  ${\bf T}'{\bf T}={\bf I}_ {p' \times p'}$이라는 조건과 동치이다(이게 이해안되면 선대다시공부해야함). 


- (2)를 만족하기 위해서는 $\sum_{i=1}^{n} \\| {\bf z}_ i - {\bf x}_ i \\|^2$을 최소화 하면 될것이다. 그런데 ${\bf z}_ i$와 ${\bf x}_ i$의 차원이 다르므로 직접거리를 잴 수 없다. 따라서 ${\bf z}_ i$에 ${\bf T'}$를 곱한 아래식을 최소화 한다. 
\begin{align}
\sum_{i=1}^{n} \\|{\bf z}_ i {\bf T'}-{\bf x}_ i \\|^2= \sum_ {i=1}^{n}  \\| {\bf x}_ i {\bf T} {\bf T'} - {\bf x}_ i \\|^2 
\end{align}
고정된 $i$에 대하여 $\\| {\bf x}_ i {\bf T} {\bf T'} - {\bf x}_ i \\|^2 $을 풀면 ${\bf x}_ i{\bf x}_ i' -{\bf x}_ i {\bf T}{\bf T'} {\bf x}_ i'$가 되어서 위의식은 아래와 같이 정리된다. 
\begin{align}
\sum_{i=1}^{n}  \\| {\bf x}_ i {\bf T} {\bf T'} - {\bf x}_ i \\|^2 = -tr({\bf T'}{\bf X'}{\bf X}{\bf T})+tr({\bf X'}{\bf X})
\end{align}
잠깐 세부계산을 살펴보자. 
1) $\\| {\bf x}_ i {\bf T} {\bf T'} - {\bf x}_ i \\|^2 $을 풀면 ${\bf x}_ i{\bf x}_ i' -{\bf x}_ i {\bf T}{\bf T'} {\bf x}_ i'$가 되는것은 ${\bf a}$가 row-vector일때 $\\|{\bf a}\\|^2={\bf a}{\bf a}'$임을 이용하면 쉽게 구할 수 있다. 
2) $\sum_{i=1}^{n}{\bf x}_ i {\bf x}_ i'=tr({\bf X}{\bf X}')=tr({\bf X}'{\bf X})$가 된다. 여기에서 두번째 등호가 성립하는 이유는 $tr({\bf A})=tr({\bf A}')$를 사용해도 되고 $tr({\bf A}{\bf B})=tr({\bf B}{\bf A})$를 사용해도 된다. 혹은 매트릭스쿡북 p6-(17) 공식 ${\bf a}'{\bf a}=tr({\bf a}{\bf a}')$를 이용할수도 있다. 그러면 $\sum_{i=1}^{n} {\bf x}_ i {\bf x}_ i ' =\sum_{i=1}^{n}tr({\bf x}_ i' {\bf x}_ i)=tr(\sum_{i=1}^{n}{\bf x}_ i' {\bf x}_ i)=tr({\bf X}'{\bf X})$가 된다.  
3) 위에서 언급한 ${\bf a}'{\bf a}=tr({\bf a}{\bf a}')$를 다시 이용하면 ${\bf x}_ i {\bf T}{\bf T'} {\bf x}_ i'=tr({\bf T'} {\bf x}_ i'{\bf x}_ i {\bf T})$가 된다. 따라서 $\sum_i^{n}{\bf x}_ i {\bf T}{\bf T'} {\bf x}_ i'=tr\left({\bf T}'\left(\sum_i^n {\bf x}_ i'{\bf x}_ i \right) {\bf T}\right)=tr({\bf T}'{\bf X}'{\bf X}{\bf T})$가 된다. 

여기에서 ${\bf X}$는 *given*되어 있으므로 결국 PCA는 아래식을 최대화하는 ${\bf T}$를 찾으면 된다. 
\begin{align}
tr({\bf T'}{\bf X'}{\bf X}{\bf T})+\lambda \left({\bf I}-{\bf T}{\bf T}'\right)
\end{align}

