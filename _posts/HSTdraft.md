---
title : (논문) HST 
layout: post 
---

### About this doc

- 이 문서는 HST에 대한 드래프트이다. 

### Definition of HST 

- 그래프형태의 자료 $(V,E,f(V))$에서의 hst를 $(V,E,\boldsymbol{h}(V))$라고 정의하자. 각각의 $i=1,\dots,n$에 대하여 $\boldsymbol{h}(v_i)$ 는 크기가 $1\times (\tau+1)$인 벡터이다. 각각의 $i,j \in \\{1,\dots,n\\}$ 에 대하여 노드 $v_i$, $v_j$ 간의 snow-dist 는 아래와 같이 정의한다. 
\begin{align}
d_1(v_i,v_j) := \\|\boldsymbol{h}(v_i)-\boldsymbol{h}(v_j) \\|_ 2
\end{align}
각각의 노드에 새롭게 쌓인 눈의 양만을 알고 싶다면 아래를 살펴보는 것도 좋다. 
\begin{align}
\boldsymbol{\dot h}(v_1), \dots, \boldsymbol{\dot h}(v_n).
\end{align}
이것은 각각 $\boldsymbol{h}(v_1),\dots,\boldsymbol{h}(v_n)$ 을 차분해서 얻을 수 있는 길이가 $1\times \tau$ 벡터이다. 이것을 이용하여 아래와 같이 snow-dist 를 정의할 수도 있다. 
\begin{align}
d_2(v_i,v_j) :=  \\|\boldsymbol{\dot h}(v_i)-\boldsymbol{\dot h}(v_j) \\|_ 2
\end{align}

- 각 노드에 내리는 눈의 양을 $\epsilon_i=\epsilon(v_i)$ 라고 하자. 눈이 내린 횟수 $\ell$ 을 고정하였을때, $v_i$ 지역으로 눈을 흘려보낼 수 있는 지역들의 모임을 ${\cal U}_ {i,\ell}$ 라고 하고 엄밀하게는 아래와 같이 정의하자. 
\begin{align}
{\cal U}_ {i,\ell} := \Big\\{j:(i,j)\in E , ~ h^{\ell}(v_i)+\epsilon(v_i) \leq h^{\ell}(v_j) \Big\\} 
\end{align}
이때 ${\cal U}_ {i,\ell}$ 은 ${\cal N}_ {v_i}:={\cal N}_ i:=\\{j: (i,j)\in E \\}$ 와는 다름을 유의하라. 각 노드에 쌓인 눈의 양을 아래와 같이 정의할 수 있다. 
\begin{align}
h^{\ell}(v_i)&=h^{\ell-1}(v_i)+ \sum_{j \in {\cal U}_ {i,\ell} }\Big( \frac{\epsilon(v_j)}{\|{\cal N}_ j \| }+\frac{\epsilon(v_i)}{\|{\cal N}_ i \| }\Big)  \\\\ \\ 
&= h^{\ell-1}(v_i)+ \frac{\epsilon(v_i)}{\|{\cal N}_ i \| }\|{\cal U}_ {i,\ell}\|+ \sum_{j \in {\cal U}_ {i,\ell} } \frac{\epsilon(v_j)}{\|{\cal N}_ j \| }
\end{align}
맨 마지막 수식에서 첫번째 항은 이전에 쌓여있었던 눈의 양을 나타내고 두번째 항은 $i$번째 노드에 내린눈이 다른 노드로 이동하지 못하고 (다른 노드의 값이 더 높기 때문) 그대로 쌓인양을 의미한다. 마지막항은 $i$와 인접한 다른노드에 쌓인눈이 $i$번째 노드로 흘러들어온 양을 의미한다. 위의 수식대신에 아래와 같이 간단한 수식을 고려할수도있다. 
\begin{align}
h^{\ell}(v_i)&=h^{\ell-1}(v_i)+ \sum_{j \in {\cal U}_ {i,\ell} } \epsilon(v_j)
\end{align}

- HST를 매트릭스를 이용하여 정의하여 보자. $\ell = 0,1,2,\dots $ 에 대하여 ${\boldsymbol h}^{\ell}$ 을 각각 길이가 $n$인 벡터라고 하자. 그리고 $n\times n$ 매트릭스 ${\bf S}^{(\ell)}$ 를 아래와 같이 정의하자. 
\begin{align}
{\bf S}^{(\ell)}_ {ij}=
\begin{cases} 
\frac{ 1_ { {\cal N}(i,\ell-1) }(j)}{\|{\cal N}_ j\|}  & i \neq j  \\\\ \\
\frac{\|{\cal N}(i,\ell-1)\|}{\|{\cal N}_ i\|} & i=j
\end{cases} 
\end{align}
여기에서 
\begin{align}
1_A(x)=
\begin{cases}
1 & x \in A \\\\ \\
0 & x \notin A 
\end{cases}
\end{align} 
이다. 이제 $\ell = 1,2,\dots $ 에 대하여 ${\boldsymbol f}=(f(v_1),\dots,f(v_n))'$ 의 HST 를 아래와 같이 정의할 수 있다. 
\begin{align}
{\boldsymbol h}^{\ell}= {\bf S}^{(\ell)} {\boldsymbol \epsilon}+ {\boldsymbol h}^{\ell-1} 
\end{align}

### Basic Assumptions and Properties. 

- HST에서 ${\boldsymbol h}$는 우리가 데이터로 부터 얻어낼 수 있는 모든 정보를 포함하고 있다고 볼 수 있다. 따라서 스무딩이나 클러스터링등은 모두 ${\boldsymbol h}$에서 얻어지는 통계량으로 정의가능하다. 이러한 통계량은 아래와 같은 ***functional*** $T:{\cal A} \to \mathbb{R}$ 로 표현가능하다. 
\begin{align}
T(F;\tau):=\int g({\boldsymbol h}) dF({\boldsymbol h})
\end{align}
여기에서 $F({\boldsymbol h})=\mu_1(-\infty,h_1]\times \dots \times \mu_{\tau+1}(-\infty,h_{\tau+1}]$ , $\mu:=P \circ {\boldsymbol h}^{-1}$ 이고 ${\cal A}$ 는 $(\Omega,{\cal F})$ 에서 정의가능한 모든 ***finited-signed measure*** 들의 집합 혹은 그것의 convex subset 이다. 이때 $T$ 에 대한 ***($\tau+1$)-dimensional influence function*** 은 아래와 같이 정의한다. 
\begin{align}
IF({\boldsymbol h}; T,F,\tau)= \lim_{t\downarrow 0}\frac{T\Big((1-t)F(\boldsymbol{h}) + t \delta(\boldsymbol{h}) \Big)-T(F(\boldsymbol{h}))}{t}
\end{align}
우리는 아래와 같이 $IF({\boldsymbol h}; T,F,\tau)$의 ***sample version*** 을 생각해 볼 수 있다. 
\begin{align}
SC_{n}({\boldsymbol h};\tau)= \frac{T\Big((1-1/n)F_{n-1}(\boldsymbol{h}) + 1/n ~ \delta(\boldsymbol{h}) \Big)-T(F_{n-1}(\boldsymbol{h}))}{1/n}
\end{align}
보는것처럼 $SC_{n}$은 $IF({\boldsymbol h}; T,F,\tau)$ 의 정의에서 $t$ 대신에 $1/n$을, $F$ 대신에 $F_{n-1}$을 대입하여 얻을 수 있다. 보통 $SC_{n}$ 를 ***sensitivity curve*** 라고 부른다. 

- ***claim 1.*** **(1)** 각각의 노드 $v_i$에서 정의된 확률변수 $f(v_i)$가 서로 독립이고 같은분포를 가진다고 하자. 그리고 **(2)** 각 노드에 연결된 edge의 수가 동일하다고 하자(이런 그래프를 ***regular graph*** 라고 함). 그러면 $\boldsymbol{h}(v_i)$ 역시 서로 독립이고 같은 분포를 가질것이다. $F_n$을 $\boldsymbol{h}(v_1),\dots,\boldsymbol{\dot h}(v_n)$에 대응하는 empirical-cdf 라고 하자. 글리벤코-칸텔리정리는 $F_n \to F$ 임을 보여준다. 따라서 적당히 큰 $n$에 대하여 $F_n$은 $F$의 neighborhood에 속한다고 볼 수 있다. 따라서 
\begin{align}
T(F_n) & \approx  T(F)+\int IF(\boldsymbol{h},T,F)d(F_n-F)(\boldsymbol{h}) \\\\ \\ 
& = T(F)+\int IF(\boldsymbol{h},T,F) dF_n(\boldsymbol{h}) 
\end{align}
이다. 여기에서 $\int IF(\boldsymbol{h},T,F)dF(\boldsymbol{h})=0$ 임이 사용되었다. 따라서 
\begin{align}
\sqrt{n}\Big(T(F_n)-T(F) \Big) \to N(0,V(T,F))
\end{align}
이다. 여기에서 $V(T,F)=\int IF(\boldsymbol{h},T,F)^2 dF(\boldsymbol{h})$ 이다. 

- ***claim 2.*** claim 1에서 $V(T,F)$ 는 $\tau \to \infty$ 일 경우 $0$ 으로 수렴한다. 왜냐하면 $\tau$ 가 커질수록 
\begin{align}
\boldsymbol{h}(v_1)\approx \boldsymbol{h}(v_2) \approx \dots \approx \boldsymbol{h}(v_n)
\end{align}
와 같이 되기 때문이다. 

- claim 1에서 **(2)** 의 조건은 생략불가능하다. 즉 $f(v_i)$가 서로 독립이고 같은 분포를 가진다는 것이 반드시 $\boldsymbol{h}(v_i)$ 들이 서로 독립이고 같은분포를 따른다는 것을 임플라이 하지는 않는다. 

- 노드간의 snow-dist 역시 $\boldsymbol{h}(v_i)$ 의 함수이므로 $T$로 표현가능하다. 따라서 (1),(2) 를 가정하면 노드간의 snow-dist 역시 $N(0,V(T,F))$ 를 따른다. 즉 (1),(2) 아래에서 노드간의 snow-distance 를 히스토그램으로 그려보면 정규분포와 비슷한 모양이 된다. 이때 snow-dist들의 평균거리가 0으로 수렴한다는 조건이 추가적으로 있으면 claim2 에 의해서 모든 노드들이 한점으로 뭉쳐버리게 된다. 

- 거리들의 히스토그램이 정규분포처럼 보이지 않는 경우는 (1) 이 성립하지 않거나 (2) 가 성립하지 않기 때문이다. 그렇다면 각각의 거리가 정규분포처럼 보이는 그룹이 2개가 있다면 이것은 (1) 혹은 (2) 가 성립하는 그룹이 2개 있다고 해석해도 될까? 아래가 성립하면 이렇게 주장할 수 있을것이다. 

- ***claim 3.*** 모든 $\tau$에 대하여 아래를 만족하는 거리 (혹은 유사거리) $d^* $ 가 존재한다. 
\begin{align}
d_1 \big(\boldsymbol{h}(v_i),\boldsymbol{h}(v_j)\big) = d^* \big(F^* (f(v_i)),F^* (f(v_j))\big)
\end{align}
여기에서 $F^* (x) :=\mu_1(-\infty,x]\times \mu_1(-\infty,\infty] \dots \times \mu_{\tau+1}(-\infty,\infty]$ 이고 $\mu:=P \circ {\boldsymbol h}^{-1}$ 이다. 

### Visualizing Examples of Importance 

- 이 챕터에서는 공통적으로 (1) HST를 활용해 거리를 정의하고 (2) 그것을 통하여 중요성을 정의 한 뒤 (3) 적당한 visualization 테크닉을 사용하여 시각화를 한다. 

- 이 챕터에서 사용되는 시각화의 종류는 (1) importance coloring (2) 주성분 분석을 활용한 3-dim 시각화 (3) 다양한 scale 에 대한 정보를 요약할 수 있는 시각화를 제시한다. 이중에서 (1)은 원래 자료와 가장 직관적으로 연결가능하다는 장점이 있다. (2) 는 자료의 특징을 토폴로지컬한 모양을 통하여 직관적으로 파악가능하다는 장점이 있다. 하지만 (1) 과 (2) 는 공통적으로 특정 scale 이 fix 되어 있어야하는 단점이 있다. 반면에 (3)은 (1),(2) 의 장점은 없지만 다양한 스케일에서 자료의 변화를 한번에 살펴볼 수 있다는 장점이 있다. 이것은 분석에 유리한 ***scale*** 을 찾는데 도움을 준다. 

- 이론적인 부분은 전혀없지만 우리가 정의한것이 매우 다양한 셋팅에서 유용하게 활용될 수 있다는 것을 보여주는 챕터가 될것 이다. 

#### Example 1. 스트럭처가 없는 1차원자료에서 평균이 다른 자료

- 그래프자료에서 모든 스트럭처간에 눈이 이동할수 있다고 생각하고 중요성을 정의한 뒤 보여준다.
- 포인트1. 그룹간의 평균차이를 멀티스케일하게 나타낸다. (평균이 1인그룹 평균이 2인그룹 평균이 5인그룹) 
- 포인트2. 자료의 희소성 

#### Example 2. 값이 없는 자료에서 (그냥 그래프자료) 스트럭처를 포착하여 보여준다. 

- 그래프자료에서 신호값에 해당하는 것을 모두 0으로 두고 HST를 적용한다음 중요성을 보여준다. 소셜네트워크에서 중요한사람? 을 나타내준다. 

#### Example 3. 똑같은 함수값과 다른 given structure를 통하여 중요성을 포착 

- 논문 EF of SP on G 에서 Example 1 과 같은 예제를 분석하면 좋아보인다. 

#### Example 4. 엣지가 주어지지 않은 자료에서 토폴로지컬 스트럭처를 파악함. 

- Hst 가 모양을 잘 찾을 수 있음을 보여준다. 
- 십자가 형태의 분포
- 도넛형태의 분포 
- 지하철역의 위치

#### Example 5. 토폴로지컬 도메인 + 값

- 지하철역의 위치 + 탑승인원 

#### Example 6. 토폴로지컬 도메인 + 값의 변동 

- 지하철역의 위치 + 탑승인원 + 시간 
- 그냥 HST를 적용하고 보여주기만 하면 된다. 지하철자료가 좋은 예가 될 수 있다. (강남역 vs 신림역 / 요일별 특이점 / 지역별특이점) 

#### Example 7. 방향성그래프 (마블) 

- 마블영화관의 관계를 파악함. 

#### Example 8. 시간에 따라서 언더라잉 스트럭처가 변화하는 경우. 

- 소셜네트워크에서 메신저를 보낸 횟수의 변화를 포착함. 
- 지진, 태풍경로? 

--- 
---
---

### Smoothing 

- 여기에서는 헴펠교재 P.316 의 내용을 참고하였다. 선형모델에서 모수 $\boldsymbol{\beta}$의 추정량 $\boldsymbol{\beta}_ n$ 을 구하는 것은 아래를 푸는 것이고 
\begin{align}
\min_{\boldsymbol{\beta}_ n}\sum_{i=1}^{n}\rho(y_i-{\bf x}_ i \boldsymbol{\beta}_ n)
\end{align}
이것은 다시 아래의 방정식의 해를 푸는것과 같다. 
\begin{align}
\sum_{i=1}^{n}{\bf x}_ i^T\psi\big(y_i-{\bf x}_ i \boldsymbol{\beta}_ n\big)=0 
\end{align}
이런 추정량 $\boldsymbol{\beta}_ n$을 $M$-estimator라고 한다. 일반적인 회귀분석 모형에서는 $\psi(y)=y$ 가 되어 위의 식은 
\begin{align}
\sum_{i=1}^{n}{\bf x}_ i^T\big(y_i-{\bf x}_ i \boldsymbol{\beta}_ n\big)=\sum_{i=1}^{n}{\bf x}_ i^T y_i-\sum_{i=1}^{n}{\bf x}_ i^T {\bf x}_ i \boldsymbol{\beta}_ n= {\bf X}'{\bf y}-{\bf X}'{\bf X}\boldsymbol{\beta}_ n=0 
\end{align}
와 같이 정리된다. 따라서 $\boldsymbol{\beta}_ n = ({\bf X}'{\bf X})^{-1}{\bf X}'{\bf y}$ 와 같이 정리된다.

- 반면 generalized $M$-estimator 는 아래를 최소화하는 해이다. 
\begin{align}
\sum_{i=1}^{n}{\bf x}_ i \phi\big({\bf x}_ i , y_i-{\bf x}_ i \boldsymbol{\beta}_ n\big) =0 
\end{align}
여기에서 $\psi$는 $1\times p$ row-vector를 실수로 보내는 맵핑이다. 즉 $\psi:\mathbb{R}\times \mathbb{R}^p \to \mathbb{R}$ 이다. 만약에 
\begin{align}
\phi({\bf x},u)=\psi(u)
\end{align}
를 만족하면 이 경우 generalized $M$-estimator 는 classical $M$-estimator 와 같다. 

- 이때 $\sum_{i=1}^{n}{\bf x}_ i \phi\big({\bf x}_ i , y_i-{\bf x}_ i \boldsymbol{\beta}_ n\big) =0$ 은 아래와 같이 쓸 수 있다. 
\begin{align}
\int {\bf x} \phi\big({\bf x} , y-{\bf x} \boldsymbol{\beta}\big) dF_n=0 
\end{align}

- WLS의 경우 
\begin{align}
\boldsymbol{\beta}_ n = \big({\bf X}'{\bf W}^2{\bf X}\big)^{-1}{\bf X}'{\bf W}{\bf y}
\end{align}
와 같이 된다. 이런 경우는 $\psi(y;{\bf w}_ i {\bf X})= \pi({\bf w}_ i {\bf X}) $ 와 같이 선택되었다고 볼 수 있다. 

#### Maronna and Yohai (1981)

- 일반적인 셋팅은 아래와 같다. (1.1) 
\begin{align}
y_i={\bf x}_ i \boldsymbol{\beta}  +\epsilon_i 
\end{align}
여기에서 $\epsilon_i$ 의 분산은 편의상 $1$ 로 가정한다. 

- 아래를 만족하는 $\boldsymbol{\beta}$ 를 구한다. (1.2) 
\begin{align}
\sum_{i=1}^{n}{\bf x}_ i \phi\big({\bf x}_ i , y_i-{\bf x}_ i \boldsymbol{\beta}_ n\big) =0 
\end{align}
이런 추정량 $\boldsymbol{\beta}_ n$을 $M$-estimator라고 한다. 여기에서 $\psi$는 $p\times 1$ row-vector를 실수로 보내는 맵핑이다. 

- 우리는 $y_i$ 대신 $f(v_i)$ 를 대입하고 ${\bf x}_ i$ 대신 $f(v_j),~ j\in\\{1,2,\dots,i-1,i+1,\dots,n\\}$ 를 대입한 셋팅을 생각하면 된다. 

- 참고문헌: Maronna and Yohai (1981), Damien Garcia (2010) 

- 적용자료: 지진자료 혹은 기상자료의 smoothing 을 수행하면 의미가 있어보인다. (시공간이 동시에 변화하는 자료들) 

- $\tau$ 의 선택??

### Clustering 

- Spectral clustering 혹은 TDA식 클러스터링을 활용하거나 cut을 사용할 수 있다. 자료는 고민중.. 

- HST에 의한 라플라시안은 아래와 같이 정의할 수 있다. 
\begin{align}
{\bf L}_ {ij}^{(\tau)}=
\begin{cases} 
-w_{ij} & i\neq j \\\\ \\
\sum_k w_{ik} & i=j. 
\end{cases} 
\end{align} 
이때 
\begin{align}
w_{ij}=\begin{cases}
\exp \Big(-\frac{d_1^2(v_i,v_j)}{2b^2}\Big) & (i,j) \in E \\\\ \\
0 & o.w.
\end{cases}
\end{align}
이다. 여기에서 $b$는 bandwidth 를 의미한다. 눈이 올수록 점점 값이 커지니까 $b$를 $\tau$에 비례하여 증가시켜야 할것 같다. 

- 이제 $f(v_1),\dots,f(v_2)$ 에 대응하는 ***graph Laplacian quadratic form*** 은 아래와 같다. 
\begin{align}
s_2(f;\tau):=\sum_{(i,j)\in E} w_{ij} \big(f(v_i)-f(v_j)\big)^2={\bf f}^T {\bf L}^{(\tau)}{\bf f}
\end{align}
여기에서 ${\bf f}=(f(v_1),\dots,f(v_n))'$ 이다. 

- 만약에 $f(v_i)$가 랜덤이면 $W_{ij}$도 랜덤이 된다. 그리고 $S_2(f;\tau)$도 랜덤이 된다. 그리고 $f$ 와 $W$ 모두 ${\boldsymbol h}$ 가 정의되는 확률공간$(\Omega,{\cal F},P)$ 에서 정의할 수 있다. 참고로 ${\boldsymbol h}$ 에서 $f$, $W$, $S_2(f;\tau)$를 만드는 함수가 각각 연속함수가 되어 각각을 정의하는데 무리가 없다. 

### Spectral Decomposition 

- ㅇㅇ

### discussions 

- 그래프 $(V,W)$는 어떠한 매니폴드의 $({\cal M},{\cal W})$ 의 ***sample version*** 이라고 하자. 아래의 성질을 만족하는(이것이 맞는 표기법인지 모르겠다. 이런식으로 가정하는 논문을 찾아봐야 할것 같음) 상황에서만 이론을 전개할 것이다. 
\begin{align}
{\cal G} \to {\cal M} \quad as~ n\to \infty 
\end{align}
신호처리식 언어로 표현하면 샘플링 주기가 $0$에 가까워지면 distrcret signal 이 continuous signal 로 수렴한다는 의미이다. 이때 샘플링은 일정한 간격으로 할 수도 있지만 어떤 특정확률에 따라서 랜덤하게 샘플링할 수도 있다. 따라서 기븐 그래프 ${\cal G}=(V,E)$ 가 어떠한 매니폴드의 sample version 이라고 볼 수 도 있지만 어떠한 랜덤엘리먼트의 ***realization*** 이라고 볼 수 도 있다. 

- 우리의 정의에서 $b$는 밴드윗의 역할을 한다. ***asymptotic property*** 를 증명하기 위해서는 밴드윗이 0으로 간다는 조건이 필수적인데 HST의 아이디어로 비춰볼때 이 조건은 
\begin{align}
\|{\cal N}_ i\|\to \infty \quad \mbox{ for all } v_i \in V
\end{align}
와 비슷하다. 

- 벨킨의 논문에서 ${\cal M}$ 은 유클리드 스페이스 $\mathbb{R}^{N}$에 ***isometric*** 하게 임베딩된 ***compact and smooth*** 매니폴드라고 가정한다(벨킨, 2008, p.1290). 이러한 가정은 매니폴드에서 샘플된 자료들에 대한 엣지를 고려하지 않고 단순히 거리만으로 유사성을 따지기 위함이다. 심지어 유클리디안거리를 그대로 쓰기 위하여 아이소메트릭 가정을 하였다. (컴팩트 and 스무스 가정은 왜 했는지 잘 모르겠음 아마 벨트라미-라플라시안을 잘 정의하기 위함일것으로 추측됨) 아무튼 이러한 셋팅하에서 ${\cal G} \to {\cal M}$ 를 모순없이 가정할수 있는것 같다. 우리는 위의 가정들을 쓰지 않는 대신에 ${\cal M}$ 위에서 적당하게 샘플을 잘하면 그래프가 매니폴드를 근사한다고 직접 가정한다. 구체적으로는 아래와 같은 가정이 될것 같다. 
\begin{align}
\frac{\|{\cal N}_ i \|}{n} \overset{\operatorname{pr} }{\to} \int_{v \in {\cal N}(v_i)}dP_{\cal M}(v)
\end{align} 
여기에서 $P_{\cal M}$ 는 매니폴드 ${\cal M}$ 위에서 정의된 메져이다. 

- ***claim*** 여기서는 given ${\cal M}$ 에 대하여 특정한 확률로 ${\cal G}$ 가 뽑힌 경우를 고려한다. $f:{\cal M} \to \mathbb{R}$ 이라고 하자. $P_{\cal M}$ 를 ${\cal M}$ 에서 정의된 ***probability measure*** 라고 하고 $p_{\cal M}$ 을 $P_{\cal M}$ 에 대응하는 ***probability density function*** 이라고 하자. 이제 $v_1,\dots,v_n$을 $P_{\cal M}$에 따라 ${\cal M}$ 에서 추출된 어떠한 sample 이라고 하자. $f(v_i)$를  랜덤이 아니라고 하자. 
\begin{align}
{\bf Lf}(v_i):=\frac{1}{\|{\cal N}_ i\|}\sum_{j \in {\cal N}_ i} e^{ -\frac{d_1^2(v_i,v_j)}{2b^2} } \big(f(v_i)-f(v_j)\big)
\end{align}
이때 $v_i \in {\cal M}$ 주변의 점들을 ${\cal N}(v_i)$ 라고 하자(이것은 ${\cal N}_ i$의 continuous 버전이라고 볼 수 있음). 만약에 $\int_{v \in {\cal N}(v_i)} dP(v)>0$ 이면 $n \to \infty$ 일때 $\|{\cal N}_ i \| \to \infty$ 가 성립할것 같다. 이러한 조건하에서 아래가 성립할것 같다. 
\begin{align}
{\bf Lf}(v_i) \overset{\operatorname{pr}}{\rightarrow}\frac{1}{\mbox{something} }\int_{ {\cal N}(v_i)} e^{ -\frac{d_1^2(v_i,v)}{2b^2} } \big(f(v_i)-f(v)\big)dP_{\cal M}(v)
\end{align}
여기에서 someting은 bandwidth $b$와 관련있는 어떠한 상수일것같다. 만약에 ${\cal M}$이 유클리드공간에 임베딩된 매니폴드라면 우변이 ${\cal L}_ {\cal M}f(v_i)$ 와 관련이 있을 것이다. 여기에서 ${\cal L}_ {\cal M}$은 라플라스-벨트라미 연산자이다. 일단은 아래가 성립한다고 생각하자. 
\begin{align}
{\bf Lf}(v_i) \overset{\operatorname{pr}}{\rightarrow} {\cal L}_ {\cal M}f(v_i)
\end{align}

