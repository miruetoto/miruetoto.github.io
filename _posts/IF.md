--- 
title: (정리) The IF for TS
layout: post
---

### About this doc 

- 이 문서는 헴펠의 **8.3b. The Influence Function for Time Series 를 요약한 것이다.** <br/>
Hampel, F. R., Ronchetti, E. M., Rousseeuw, P. J., & Stahel, W. A. (2011). Robust statistics: the approach based on influence functions (Vol. 196). John Wiley & Sons. 

- 해당내용은 교재 p.417 에 있다. 중간중간에 필요한 부분은 앞의 내용을 참고해가면서 정리하였다. 참고로 이 책은 엄청 어렵다. 그래서 중간중간 송문섭교수님이 쓰신 로버스트통계를 참고하였다. 또한 종종 임요한 교수님의 강의노트도 참고하였다. 

### Prepare

- 회귀분석은 보통 제곱합을 최소화 시키는 $\boldsymbol\beta$ 를 찾는 방법이므로 하나의 아웃라이어가 만드는 ***gross error*** 에 심각한 영향을 받는다. 여기에서 gross error 는 나중에 더 엄밀하게 정의할 것이다. 한글로 번역하면 **대형오차** 정도의 느낌이다. 

- 우리의 목적은 어떠한 ***estimator*** 가 가지는 성질을 규명하기 위함이다. 특히 극한적 성질을 규명할 일이 많은데 이때 estimator 를 만들어 내는 $X_1,\dots,X_n$ 의 극한적 성질을 다루기 보다 sample $(X_1,\dots,X_n)$의 ***empirical distribution*** $G_n$의 극한적 성질을 다루는 것이 더 편리하다. (글리벤코-칸텔리 정리 같은것을 쓸 수 있기 때문) 

- 그래서 우리는 $\theta$ 와 $\hat \theta$ 을 아래와 같은 ***functional*** 의 형태로 표현하고 싶다. 
\begin{align}
\begin{cases}
\theta=T(G) \\\\ \\
\hat{\theta}=\theta_n=T_n(G_n)=T_n(X_1,\dots,X_n)=T_n
\end{cases}
\end{align}
여기에서 $G$는 cdf를 의미하고 $G_n$은 sample $(X_1,\dots,X_n)$의 empirical distribution 이다. 그리고 $\hat\theta=\theta_n$ 은 sample $(X_1,\dots,X_n)$ 으로 만든 통계량이다. 


### The Influence Function for Time Series 

- ${\boldsymbol X}$를 ***timeseries*** 라고 하자. 즉 ${\boldsymbol X}$는 $(\Omega,{\cal F})$ 에서 $(\mathbb{R}^{\mathbb{N}},{\cal R}^{\mathbb{N}})$으로 가는 메저러블맵핑이다. 타임시리즈 ${\boldsymbol X}$ 에서 추출한 finite sample $(X_1,\dots,X_n)$ 을 살펴보자. 타임시리즈 ${\boldsymbol X}$의 cdf 를 $F$라고 하자. 그리고 확률벡터 $(X_1,\dots,X_n)$의 cdf 를 $F_n$ 이라고 하자. 여기에서 $F$가 ***stationary ergodic distribution*** 이라면 적당한 mild regularity condition 하에서 $T_n$이 $T(F^{(m)})$로 수렴한다. 여기에서 $F^{(m)}$ 은 차원이 $m$ 인 $F$ 의 마지날이다. $T$는 $m$ 차원 프로덕트 스페이스에서 정의되는 probability measure 처럼 행동한다. 즉 
\begin{align}
\int \psi(x_m,\dots,x_1 ; T(G)) dG(x_1,\dots,x_m)=0
\end{align}
이다. 이때 $G$는 $T$의 도메인에서 정의되는 임의의 함수이다. 이제 IF를 정의하여 보자. ***i.i.d.*** case 와 유사하게 아래와 같이 정의할 수 있다.
\begin{align}
IF(x_m,\dots,x_1; T, F^{(m)})=
\lim_{h\downarrow 0} \frac{T\Big((1-h)F^{(m)}+h\Delta_{(x_1,\dots,x_m)}\Big)-T(F^{(m)})}{h}
\end{align}
여기에서 $\Delta_{(x_1,\dots,x_m)}$ 는 $(X_1,\dots,X_m)=(x_1,\dots,x_m)$에서 point mass 1 을 가진다. 
