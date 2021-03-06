---
layout: post
title: (논문) HST
---
### About this document 
- 이건 HST논문의 Draft버전이다. HST는 궁극적으로 두 자료사이의 거리를 새롭게 정의하고 그것들을 바탕으로 주어진 자료를 다양항 방식으로 재해석하는 방법이다. 두 자료간의 유사성을 정의하고 그것을 유클리드 공간에 뿌리는 수도 있고 두 자료간의 유사성을 정의하고 그것을 그래프형태로 재 구성할 수도 있다. (토폴로지컬 데이터 어날리시스 처럼) 

- 결국 HST의 2가지 버전이 있을 수 있다. (1) 우리가 링크에 대한 정보를 알고 있을 경우 분석법 (2) 우리가 링크자체를 새로 구성해야 하는 경우 

### 서론 
- 이 논문에서는 두 자료 ${\bf x}$와 ${\bf x}^* $사이의 **similarity**를 정의하기 위한 새로운 measure를 정의한다. 자료간의 **similarity**를 정의하는 방법은 여러가지가 있지만 일반적으로 자료간의 **distance**의 반대개념으로 정의하곤 한다. In the context of cluster analysis, Frey and Dueck suggest defining a similarity measure 
\begin{align}
sim_1 ({\bf x},{\bf x^* } )=-\\|{\bf x}-{\bf x^* }\\|_ {2}^{2}
\end{align}
where $\\|{\bf x}-{\bf x^* } \\|$ is the squared Euclidean distance. 이것은 자료간의 **distance**를 유클리드 거리로 생각한 것이다. Ng, A (2000)은 자료간의 **distance**를 아래와 같은 방식으로 정의하였다. 
\begin{align}
sim_2 ({\bf x},{\bf x^* },\sigma )=\exp \left(\frac{ -\\|{\bf x}-{\bf x^* }\\|_ {2}^{2}}{2\sigma^2} \right) 
\end{align}
이것은 유클리디안 거리를 살짝 변형한 방법이다. **가우스유사도** 라고도 불리며 **RBF kernel**이라고 불리기도 한다. 그 외에 **cosine similarity** 혹은 **correalation**과 같은것도 **similarity**를 측정하는 방법이라고 볼 수 있다. 또한 두 집합사이의 **similarity**를 측정하는 **Jaccard similarity**도 있다. $k$-최근접 이웃 유사도 혹은 국소척도유사도 (통통머신러닝 p151) 역시 많이 쓰이는 measure of **similarity** 이다. 

- 이렇게 많은 메져가 존재함에도 불구하고 본 논문에서 굳이 **similarity**를 측정하는 새로운 **measure**를 제안하는 이유는 이러한 메저들이 자료들간의 link를 고려하지 않고 **similarity**를 측정했다는 한계가 있기 때문이다. 여기에서 자료간의 link를 고려한다는 것은 index set의 스트럭처를 고려한다는 의미이다. 가령 다음과 같은 자료를 생각하여 보자. 
\begin{align}
\\{x_i\\}_ {i=1}^{20}=\\{1,1,1,1,5,1,1,1,1,1,5,5,5,5,5\\}
\end{align}
만약에 자료간의 link 즉 index set의 structure를 고려하지 않는다면 $x_5$는 $\\{x_i\\}_ {i=11}^{20}$와 비슷한 자료라고 느껴질 것이다. 하지만 자료간의 link 즉 index set의 structure를 고려한다면 $x_5$가 $\\{x_i\\}_ {i=11}^{20}$와 비슷하다고 느끼지 않을 것이다. 

- 이처럼 자료간의 link를 고려하게 되면 **similarity**의 개념이 달라지게 된다. 

- 자료간의 link를 고려하면 비유사성의 개념이 조금 달라지는 또 다른 예는 xxx에 설명되어 있다. 그림 XX는 논문에서 발췌한 것인데 링크를 어떻게 거느냐에 따라서 비유사성이 달라지는 상황을 나타낸다. 

- 본 논문에서는 이처럼 index set의 스트럭쳐를 고려하여 자료간의 비유사성을 측정할 수 있는 메져를 쌓인눈 변환을 이용하여 새롭게 제시하고자 한다. 자료간의 link를 고려한다는 점에서 이는 논문 xx에서 제시한 방법들과 매우 유사하다. (관련분야 공부할것) 제안된 방법이 이러한 방법들과 가지는 차이점은 (1) 제시된 방법이 멀티스케일방법이라는 점이다. 즉 눈이 내리는 양에 따라서 index set의 스트럭처를 얼마나 강하게 고려할것인지 결정할 수 있다. 제안된 방법의 두번째 차이점은 (2) 제시된 방법으로 인하여 linked data에서의 이상점탐지를 마치 unlinked data에서의 이상점탐지처럼 수행할 수 있다는 것이다. 이는 section xxx에서 자세히 설명할 것이다. (3) 제안된 방법은 observation각각의 이상치를 measure할수 있지만 XX의 방법은 데이터 전체의 smoothness를 메져한다. 


---
***LOF: identifying density-based local outliers***

--- 
***On spectral clustering: Analysis and an algorithm***
- 여기서는 아래의 논문을 요약하였다. <br/>
***REF***: Ng, A. Y., Jordan, M. I., & Weiss, Y. (2002). On spectral clustering: Analysis and an algorithm. In Advances in neural information processing systems (pp. 849-856).

- 위의 논문에서는 두 벡터 ${\bf x}$와 ${\bf x^* }$의 거리를 단순한 유클리드 거리가 아니라 아래와 같이 정의하였다. 
\begin{align}
dist({\bf x},{\bf x}^* )= 
\end{align}
라는 개념이 나오는데 이것이 우리가 제안하는 dissimilarity와 유사하다. 이 논문에서는 위와같은 유사도를 바탕으로 Spectral Clustering을 제안한다. Spectral Clustering은 국소적보존사영을 수행한뒤에 $k$-평균 클러스터링을 수행하는 기법이다. 이 결과와 우리의 방법을 비교하면 매우 흥미로울 것으로 예상된다. 

--- 
***밀도비***
- 비유사성은 정보이론에서 상호정보량으로도 이해할 수 있다. 상호정보량은 두 자료가 얼마나 독립인지를 메져한다. KL-괴리도 설명.  
- P140 / P160 에 관련내용이 있으니까 공부해볼것. (밀도비 기반 이상치 검출과 스펙트럴-클러스터링에서 파라메터를 자동 결정하는 내용임) 

--- 
***공변량쉬프트*** 
- 이상도 역시 비유사성만큼 통계학에서 중요한 의미를 가진다. 이상도를 활용한 다양한 통계적 분석방법이 존재한다. 공변량쉬프트상황에서의 중요도 가중학습, 상대중요도가중학습.. (KL괴리도와 비슷함) 

--- 
### Definitions
***Definition of heavy-snow transform***  

***Definition of dissimilarity***  

***Definition of Global smoothness of graph*** 

- Let $(V,E,f(V))$ be the given data. Let $(V,E,{\boldsymbol h}^{\tau}(V))$ be the hst of given data. Define
\begin{align}
T_n^{\tau}=\sum_{(i,j) \in E}\big\\|{\boldsymbol h}(v_i)- {\boldsymbol h}(v_j)\big\\|^2. 
\end{align}

- $T_n^{\tau}$을 일단 위와 같이 정의하긴 했는데 이런정의로 우리가 원하는것을 이끌어 낼지는 모르겠음. 

- $x_i:=f(v_i) \sim ~ i.i.d. ~ F$ 라고 하자. 벌티스 $v_i$에 대한 importance 아래와 같이 정의한다. 
\begin{align}
Imp(x_i):=IF(x_i;T_n^{\tau},F)=\lim_{t \downarrow 0} \frac{T_n^{\tau}\Big((1-t)F+t\delta_x\Big)-T_n^{\tau}(F)}{t}
\end{align}
왜인지는 알 수 없지만 이것은 given $F,T$ 에서 특정한 point $x_0$이 얼마나 $T$를 흔들 수 있느냐를 measure 한다. 


### Robustness 

- beakdown pt : Let $(V,E,f(V))$ be the given data. Let $T_n^{\tau}$ be measure of total smoothness of graph. Then 
\begin{align}
T_n^{\tau} \to 0?, 1?, n? 
\end{align}
as  $\tau \to \infty$. 

### Thm with some specified application 

#### properties for super global scael 

- 눈이 많이 내리면 결국 모든 자료는 비슷해진다. 

#### 이상점에 대한 성질 

- 이상점에 대한 성질을 증명하자. 아웃라이어는 생각보다 중요한데 함수의 local smoothness 역시 같이 정의할 수 있다. 따라서 함수의 local variance 역시 같이 정의할 수 있다. 그리고 이것은 뒤에 denoising,approximation 으로도 이어진다. (prediction은 어쩌지?) 

***link 가 정의된 자료*** 

- $(t,X_t)$를 관측했다고 하자. 하나의 자료 $x^* =X_{t^* }$ 를 제외한 다른 모든 자료가 똑같은 값을 가지고 있다고 가정하자. 이러한 자료위에 눈을 쌓았다고 생각하자. (1) $x^* $와 가까운 점일수록 importance가 높아진다. (2) 눈이 쌓여가면서 $x^* $와 함께 importance 가 높아지는 점이 발견된다. (3) 결국은 모든 점들이 다시 평범해 진다. 

- 

#### 변화점에 대한 성질 

- $\\{x_i\\}$와 $\\{y_i\\}$가 서로 다른분포에서 추출된 집단이라고 하자. 두 집단의 평균이 다른지 같은지 test하고 싶다고 하자. 
- 평균이 다르다면 두 집단의 observation을 odering 한 뒤에 눈을 쌓아보면 변화가 느껴질 것이다. 
- 두 집단의 분산이 다를때 이를 검출하고 싶다고 하자. 
- 하나의 시계열에서 평균이 변화할때 이를 검출하고 싶다고 하자. 
- 하나의 시계열에서 분산이 변화할때 이를 검출하고 싶다고 하자. 
- 하나의 시계열모델에서 파라메터의 변화를 검출하고 싶다고 하자. (1) AR모델의 파라메터를 local 하게 찾는다. (2) 이걸 HST로 detect한다. 

#### Clustering 

- cut: 변화점을 그룹에서 잘라버린다. 나머지 링크는 그대로 유지한다. 

- spectral clustering: 링크자체를 완전히 재배열한다. 


#### Subgroup detection 

- 우리의 목적에 맞는 subgroup을 잘 찾을 수 있는 $\tau$ 를 조정함. 기존의 거리들은 이런식으로 하기 어렵지만 우리는 $\tau$에 따라서 멀티스케일하게 거리를 재정의하는 능력이 있기 때문에 원하는 목적에 맞는 분석을 더 하기 쉽다. 멀티스케일의 장점은 하나의 스케일이 신호 전체의 효과를 도미네이트 할때 나타난다. 하나의 효과가 다른 효과를 도미네이트 할때면 그 효과에 가려진 숨겨진 의미를 꿰뚫기 힘들다. 하지만 이 분석법은 그것을 가능하게 한다. 

#### 독립성

- 두 자료가 독립인지 아닌지를 알기 위해서는 (1) link 정보를 주고 노드값을 예측하게 해보고, (2) link 정보를 주지 않고 노드값을 예측하게 해본뒤 두 결과를 비교해보면 좋을것 같다. 

---

### Data Analysis 

***measuring smoothness and anormally detection***
- 이상검출은 dissimilarity의 개념과 매우 밀접한 관련이 있다. (1) LOF의 경우 RD를 활용하여 두 자료사이의 비유사성을 측정하고 (2) 그것을 통하여 자료의 이상성을 측정한다. 우리의 방법은 (3) 이상성을 변화점으로 치환시킬수 있다. 따라서 변화점 탐지도 이상점 탐지처럼 할 수 있다. 

- 아이디어가 하나 있는데 적당한 $\tau$에 대하여 importance plot을 그리고 적당한 threshold $\lambda$를 설정하여 change-point를 원하는 수준으로 검출한다. 이렇게되면 change point detection 문제는 change를 잘 보여줄 수 있는 $(\tau, \lambda)$를 찾는문제로 생각할 수 있다. 즉 $(\tau,\lambda)$에 따른 적당한 loss function을 잘 설정하고 (loss function은 change point를 잘 못찾으면 크게 설정되도록 함) 그 loss function이 convex임을 보이면 매우 좋을것 같다. 

- 

***clustering***

***smoothing and prediction***

---

### Real-data analysis 

***measuring smoothness and anormally detection***

- 어떤역들은(쩌리역들) 시간별로 스무스한 반면 어떤역들은(신림,강남) 스무스하지 않음.

- 어떤 시간은 스무스 하지만 어떤 시간은 스무스 하지 않음. 

- 어떤 날은 스무스하지만 어떤 날은 특이함. (이런 요일이 있을까?? 주말?? 행사등이 있는날?? 지하철 무료탑승??) 

- 중요한 역, 중요한 시간, 중요한 요일을 알고 싶을 수 있다. 여기에서 중요하다는 의미는 다른 자료들과 비슷하지 않아 다른 자료들로 부터 쉽게 예측할수 없다는 의미이다.  

- 일반적인 anormally detection과의 차이는?? (아마 신림역보다 강남역이 더 anormallity가 크게 나올것임) 

***clustering***
- unsupervised and semi-supervised learning

- 요일을 고려하면 상업지역을 구분할 수 있다. 특정요일에만 활성화 되는 역들이 있다면 이 역들은 휴식 혹은 유흥등 사람들이 여가시간을 보내는 공간이라고 이해할수 있다. (1) 요일과 역들을 고정한 상태에서 each 요일 each 역들에 대한 모든 시간의 총합을 취한다. 

- 하나의 (공휴일이 아닌) 요일에 대하여 시간, station을 모두 고려하면 오피스지역, 비오피스지역을 구분할 수 있다. 

- 일반적인 clustering 방법과 차이점은? 상업지역과 비상업지역을 구분할 수 있을까?  


***smoothing and prediction***
- underlying function을 추론. 예측 

- 각각의 점마다 smoothness를 측정한다. 

- smoothness가 큰 곳 (=importance가 낮은곳) 은 노드를 넓게 연결하여 다음값을 예측한다. 

- smoothness가 작은곳 (=importance가 높은곳) 은 노드를 좁게 연결하여 다음값을 예측한다. 

- LSTM에서 기억을 잃어버리는 정도의 rate를 조절하는 방식이라고 볼 수 있다. 

---

### Conclusion


### Reference
- Ng, A. Y., Jordan, M. I., \& Weiss, Y. (2002). On spectral clustering: Analysis and an algorithm. In Advances in neural information processing systems (pp. 849-856).

- Breunig, M. M., Kriegel, H. P., Ng, R. T., \& Sander, J. (2000, May). LOF: identifying density-based local outliers. In ACM sigmod record (Vol. 29, No. 2, pp. 93-104). ACM.

- He, X., \& Niyogi, P. (2004). Locality preserving projections. In Advances in neural information processing systems (pp. 153-160).

