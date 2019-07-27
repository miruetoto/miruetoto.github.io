---
title: (정리) Began
layout: post 
--- 

### About this doc 

- 이건 BEGAN 을 이해하기 위한 포스트이다. 

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
