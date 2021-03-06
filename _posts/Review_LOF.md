---
layout: post 
title: (리뷰) LOF
---

### About this document 

- 논문리뷰

- 학부수준 

- 여기서는 아래의 논문을 요약하였다. <br/>
***REF***: Breunig, M. M., Kriegel, H. P., Ng, R. T., & Sander, J. (2000, May). LOF: identifying density-based local outliers. In ACM sigmod record (Vol. 29, No. 2, pp. 93-104). ACM.

- 위의 논문에서는 **리처빌리티-디스턴스*(Reachability Distance)*** 라는 개념이 나오는데 이것이 HST에서 제안하는 dissimilarity와 유사하다. 이 논문에서 제시한 anormally detection방법과 우리의 방법을 비교해보면 매우 유익할것이다. 

- 가급적 논문에 나오는 노테이션을 따라갈것이다. 하지만 도저히 못따라가겠는 노테이션이 있는데 바로 **하이픈** 이다. 저자들은 $k-distance(p)$와 같이 자꾸 변수에 하이픈을 넣는데 이러한 노테이션은 마치 $k$ **minus** $distance(p)$ 와 같이 이해된다. 어지간하면 참고 쓰려고 했는데 가독성이 너무 떨어져서 도저히 쓸 수 없다. 왜 이런 노테이션을 쓰는지 도저히 이해할 수 없다. 그래서 변수에 정의된 하이픈은 모두 닷으로 바꾸겠다. 즉 $k-distance(p)$를 $k.distance(p)$와 같이 변경하겠다. 

- 이거는 HST를 쓰기위해서 어쩔수 없이 잘 읽어봐야 한다. 

### 4. Formal definition of local outliers 
- **(Definition 3)** 여기에서는 **점 $p$와 $k$번째로 가까운 점사이의 거리*$k.distance(p)$*** 라는 것을 정의한다. $p$와 가장 가까운 점은 자기자신이므로 $k=1$이면 $k.distance(p)=0$이다. 즉 모든 경우에 클리어하게 아래가 정의된다. 
\begin{align}
1.distance(p)=d(p-p)=0
\end{align}
그런데 만약에 점 $p$로부터 $k$번째로 가까운 점이 2개면 정의가 애매해진다. 이때는 그냥 동점자끼리는 같은 거리를 가진다고 생각하고 정의해버린다. 예를 들어보자. 하나의 수직선위에 점 $\\{-1,0,1,2,3,4\\}$가 있다고 하자. 편의상 $p=0$이라고 하자. 일단 언급한바와 같이 아래가 성립한다. 
\begin{align}
1.distance(0)=0
\end{align}
이다. $k=2$인 경우를 살펴보자. 점 $\\{0\\}$과 두번째로 가까운 점은 $\\{-1,1\\}$ 이런경우는 아래와 같이 정의한다. 
\begin{align}
2.distance(0)=3.distance(0)=1
\end{align}
**앞으로는 논의를 빠르게 하고 논문의 이해를 돕기위해서 위와같은 상황은 없다고 가정하자.**

- **(Definition 4)** 여기에서는 **점 $p$의 $k.distance$ 이웃들*($k.distance$ neighborhood of $p$)*** 이라는 개념이 나온다. 요거는 기호로 $N_{k.distance(p)}(p)$라고 표현하고 아래와 같이 정의한다.
\begin{align}
N_{k.distance(p)}(p)=\\{q \in D- \\{p\\} | d(p,q) \leq k.distance(p) \\} 
\end{align}
여기에서 $D$는 전체 데이터셋을 의미한다. 쉽게 말하면 $p$의 $k.distance$ 이웃들 점 $p$와 가까운 점 $k-1$개를 의미한다. (자기자신을 빼므로 $k$개가 아니라 $k-1$개임). 이것을 줄여서 $N_k(p)$라고도 쓴다. 

- 그리고 편의상 앞으로 $N_k(p)$의 원소들을 $p$의 $k$-1차이웃 혹은 줄여서 1차이웃이라고 하자. 요런 정의를 바탕으로 하면 $k.distance(p)$는 $p$의 $k$-1차이웃들중 $p$와 가장 멀리떨어진 점과의 거리를 의미한다. 편의상 이걸 *최대 $k$-1차이웃거리* 혹은 *최대 1차이웃거리* 라고 하자. 이런 용어는 논문에 없는 용어이다. 비슷한 방식으로 1차이웃들의 1차이웃들을 정의할수 있는데, 이를 2차이웃으로 정의하자. 앞으로 혼란을 피하기 위해서 (1) $p$는 target point (2) $q$는 $p$의 1차이웃 (3) $o$는 $q$의 1차이웃 즉 $p$의 2차이웃으로 정의하자. 즉 아래와 같은 인덱스로 정리하자. 
\begin{align}
q \in {\cal N}_ p :=\\{q \in D- \\{p\\} | d(p,q) \leq k.distance(p) \\} \\\\ \\ 
\forall q: ~ o \in {\cal N}_ q :=\\{o \in D- \\{q\\} | d(q,o) \leq k.distance(q) \\} 
\end{align}
따라서 $p$의 2차이웃에 $p$ 자신이 포함될 수도 아닐수도 있다. 

- **(Definition 5)** 여기에서는 $q$에서 $p$까지의 **리처빌리티-디스턴스*(Reachability Distance, RD)*** 를 정의한다. RD는 기호로 $reach.dist_{k}(p,q)$라고 쓰고 아래와 같이 정의한다. 
\begin{align}
reach.dist_{k}(p,q)= \max (k.distance(q) ,d(p,q)) 
\end{align}

- 잘 살펴보면 이 논문에서 RD는 $q$ 주변의 점들의 **조밀함** 을 반영한 거리라고 볼 수 있다. 무슨 말인지 예를 들어 설명해보도록 하자. 점 $p$와 유클리드 거리상으로 똑같은 거리에 있는 두점 $q_1$과 $q_2$가 있다고 생각하자. 그런데 점 $q_1$ 주변에는 다른점들이 엄청 조밀하게 있고 점 $q_2$ 주변에는 다른점들이 듬성듬성 있다고 하자. 중심이 $q_1$ 이고 반지름이 $k.distance(q_1)$ 인 원을 하나 그리고 중심이 $q_2$ 이고 반지름이 $k.distance(q_2)$ 인 원을 하나 그려보자. 당연히 $q_1$에는 작은 점선원이 $q_2$에는 큰 점선원이 그려질 것이다. <br/>
(1) $p$가 $q_1$의 점선원과 $q_2$의 점선원에 모두 포함될 경우: 
\begin{align}
reach.dist(p,q_1)<reach.dist(p,q_2).
\end{align}
(2) $p$가 $q_1$의 점선원에는 포함되지 않지만 $q_2$의 점선원에는 포함되는 경우:
\begin{align}
reach.dist(p,q_1) \leq reach.dist(p,q_2).
\end{align}
(3) $p$가 $q_1$과 $q_2$의 점선원에 모두 포함되지 않는 경우:
\begin{align}
reach.dist(p,q_1)=reach.dist(p,q_2).
\end{align}
따라서 실제 유클리드 거리는 같음에도 불구하고 RD의 관점에서 보면 $q_1$보다 $q_2$가 더 떨어져있다. 

- 저자들은 어느순간부터  $k$를 Minpts라고 표현한다. 정확한 의미는 모르겠지만 ***minimal number of points***의 약자인것 같다. 여기에서는 그냥 계속 $k$라고 표현하겠다. 

- 잠시 RD와 HST의 **쌓인눈거리*(snow-dist)*** 를 비교하여 보자. <br/><br/>
(1) RD에서는 점선원안에 들어오는것을 이웃으로 생각하는데 HST에서는 링크된 점들을 이웃으로 생각한다. 즉 RD에서는 target point와 가장 가까운 유클리드 거리를 가지는 몇개의 점들을 이웃으로 생각하고 HST는 target point와 링크된 점들을 이웃으로 생각한다. HST에서는 다른 링크를 줄 수 있으므로 이웃의 정의를 전혀 다르게 가져갈 수 있다. <br/> 
(2) 이 논문에 나오는 산점자료들을 굳이 HST에 때려맞춰서 그래프시그널 형태로 표현한다면, 점 $(1,1)$은 위치가 $(1,1)$에서 그 크기로 $\sqrt{2}$를 가지는 신호로 표현가능하다. <br/>
(3) RD는 주변점들의 국소적 특징들을 반영한다는 점에서 HST의 snow-dist와 비슷하다. 그리고 둘다 기본적으로 유클리드 거리를 반영한다는 점에서 비슷하다. 다만 RD는 주변값들이 얼마나 조밀한지 그렇지 않은지를 추가적으로 반영하고 snow-dist는 주변값들보다 상대적으로 낮은지 높은지, 낮아지다가 높아지는지 등등을 반영할 수 있다. 하트모양으로 point를 scattering 한다고 할때 하트의 꼭지점을 찾을 수 있다. 비유를하면 RD는 주변점들의 밀도를 느낄 수 있으며 snow-dist 모양을 느낄 수 있다!!!! <br/>
(4) snow-dist 로 RD 와 비슷한 역할을 하게 만들수 없을까?? 밀도가 높은곳이라면 연결이 많이 되어있을테고 링크가 많을수록 수렴하는 느낌이 다를텐데 이걸 이용해서 먼가 할 수 있을까?? 

- **(Definition 6)** 이제 **로칼-리처빌리티-덴시티*(Local Reachability Density,LRD)*** 에 대하여 알아보자. 점 $p$에서의 LRD는 아래와 같이 정의한다. 
\begin{align}
lrd_{k}(p)=\left(\frac{1}{\|N_{k}(p)\|} \sum_{q \in N_{k}(p)} reach.dist_k(p,q)\right)^{-1}
\end{align}

- LRD의 정의에서 RD대신에 유클리드거리를 쓰면 그냥 **평균거리의 역수**가 되어서 빼도박도 못하고 그냥 밀도개념이 된다. 유클리드 거리 대신에 RD를 쓰면 $p$의 밀도를 구할때 $p$ 밀도 뿐만 아니라 $q$의 밀도도 함께 고려한 메져가 된다. 

- **(Definition 7)** 이제 대망의 **LOF(local outlier factor)** 를 정의하여보자. LOF는 아래와 같이 정의한다. 
\begin{align}
LOF_{k}(p)=\frac{1}{\|N_{k}(p)\|} \sum_{q \in N_{k}(p)} \frac{lrd_k(q)}{lrd_k(p)}
\end{align}
이건 그냥 너무 클리어한 정의이다. $p$근처에는 점이 하나도 없고 $p$의 이웃들은 다 모여있는 경우 $p$의 LOF가 가장 크게 나타난다. 하지만 그냥
\begin{align}
LOF_{k}(p)=\frac{1}{lrd_k(p)}
\end{align}
와 같이 간편하게 정의해도 괜찮치 않나? 왜 밀도역수가 아니라 밀도비로 정의했을까? 

### Properties of local outliers 

- 이제 LOF에 대한 성질을 알아보자. LOF는 $p$가 얼마나 outlier 인지를 메져하는데, 반대로 말하면 $p$가 어떠한 그룹이 속해있는지 아닌지를 메져하는것고 ㅏ같다. 점 $p$가 클러스터 안에 폭 파묻혀 있다면 $p$의 LOF값은 1에 가까울 것이다. 즉 $LOF_{k}(p) \approx 1$ 이다. 

- 어떤 클러스터 $C$에 속한 임의의 점들 $c_1,c_2,\dots,$를 생각하자. 즉 $c_i \in C$ 이면 $LOF_k(c_i) \approx 1$이 성립하게끔 하는것이 우리의 목표다. 우리가 정의한 LOF가 과연 이러한 성질을 만족할까? Lemma1은 $C$에 존재하는 모든 점들은 아웃라이어가 아니라는 결론을 주는(정말?? 좀 애매한데? ㅋㅋ) 레마이다. 

- **(Lemma 1)** $C$를 임의의 클러스터라고 하자. $reach.dist.min$ 이라는 것을 정의할 것인데 이것은 $C$내에 있는 모든 자료의 **리치어빌리티-디스턴스**의 최소값을 의미한다. 즉 클러스터 $C$내에서 가장 가까이 붙어있는 두점사이의 거리를 의미한다. 식으로 쓰면 아래와 같다. 
\begin{align}
reach.dist.min=\min \\{ reach.dist(c_i,c_j): c_i,c_j \in C \\}
\end{align}
이와 유사하게 $reach.dist.max$ 도 정의할 수 있다. 이제 $\epsilon$을 아래와 같이 정의하자. 
\begin{align}
\epsilon=\frac{reach.dist.max}{reach.dist.min}-1
\end{align}
쉽게 생각해서 $C$안의 대부분의 점들의 엄청 모여있으면 $\epsilon \approx 0$ 와 같이 된다. 저자들은 클러스터 $C$에 속하는 임의의 점 $p$에 대하여 $p$가 다음의 3가지 성질 (i) $p$의 $k$-근접이웃들이 모두 $C$의 원소이고(ii) $p$의 $k$-근접이웃들 각각의 $k$-근접이웃들까지 모두 $C$의 원소이면 
\begin{align}
\frac{1}{1+\epsilon}\leq LOF(p) \leq 1+\epsilon
\end{align}
이 성립한다고 주장한다. 

- 증명은 다음과 같다. 모든 $q \in N_k(p)$에 대하여 아래가 성립한다. 
\begin{align}
dist(p,q) \geq reach.dist.min
\end{align}
따라서 아래가 성립한다. 
\begin{align}
lrd_k(p) \leq \frac{1}{reach.dist.min}
\end{align}
이거랑 비슷한 논리로 아래가 성립한다. 
\begin{align}
lrd_k(p) \geq \frac{1}{reach.dist.max} 
\end{align}
위의 논쟁에서 $p$를 $q$로 바꾸고 $q$를 $o$로 바꾸면 아래 역시 증명된다. 
\begin{align}
\frac{1}{reach.dist.max} \leq lrd_k(q) \leq \frac{1}{reach.dist.min}
\end{align}
따라서 원하는것이 증명된다. 

- Lemma 1 의 조건 (i), (ii)는 점 $p$가 클러스터안에 **"포오옥~"** 파묻혀있어야 함을 의미한다. 

- Lemma 1 에서 $\epsilon$은 클러스터의 tightness를 결정한다. 

- 이것을 이용하면 HST 에서 $\tau \to \infty$일때 $\epsilon_{\tau} \to 0$으로 감을 증명할 수 있을것 같다. 즉 클러스터가 하나의 클러스터로 되고 그 것들이 점점 ***tight*** 해짐을 증명할 수 있을것 같다. 이를 위해서는 논문에서 처럼 $p$ 가 얼마나 클러스터에 포오옥 파묻혀있는지 메져하는 것이 필요하다. 
 
#### A General Upper and Lower Bound on LOF 

- Lemma 1 은 (i), (ii)가 만족되는 $p \in C$에 대한 성질만 밝혔다. 좀더 일반적인 $p$에 대한 성질을 밝히기 위하여 Theorem 1을 만들었다. Theorem 1 은 두가지 측면에서 Lemma 1의 업그레이드 버전이라고 볼 수 있다. 첫째 Theorem 1 은 언급한데로 일반적인 $p$에 대하여 $LOF_k(p)$의 bound를 준다. 둘째 Theorem 1 은 Lemma 1 보다 더 타이트한 bound를 제시할 수 있다. 

- Theorem 1 을 제시하기에 앞서 몇 가지 정의할 기호들이 있다. 
\begin{align}
\begin{cases}
direct_{min}(p):=\min \\{ reach.dist(p,q) : q \in N_k(p) \\} \\\\ \\
direct_{max}(p):=\max \\{ reach.dist(p,q) : q \in N_k(p) \\} \\\\ \\
indirect_{min}(p):=\min \\{ reach.dist(q,o) : q \in N_k(p), ~ o \in N_k(q) \\} \\\\ \\
indirect_{max}(p):=\max \\{ reach.dist(q,o) : q \in N_k(p), ~ o \in N_k(q) \\}
\end{cases}
\end{align}

- **(Theorem 1)** 아래식이 성립한다.
\begin{align}
\frac{direct_{min}(p)}{indirect_{max}(p)}\leq LOF_k(p) \leq \frac{direct_{max}(p)}{indirect_{min}(p)}
\end{align}

- 편의상 Theorem 1 에서 정리된 $LOF_k(p)$의 lower bound 를 $LOF_{min}$이라고 하고 그 max에 해당하는 것을 $LOF_{max}$라고 하자. 저자들은 $LOF_{max}-LOF_{min}$이 $\frac{direct}{indirect}$에 의존한다고 주정한다. 즉 
\begin{align}
LOF_{max}-LOF_{min} \propto \frac{direct}{indirect}=\frac{direct_{min}(p)+direct_{max}(p)}{indirect_{min}(p)+indirect_{max}(p)}
\end{align}
여기에서 
\begin{align}
\begin{cases}
direct(p):=direct=:\big(direct_{min}(p)+direct_{max}(p)\big)/2 \\\\ \\
indirect(p):=indirect=:\big(indirect_{min}(p)+indirect_{max}(p)\big)/2
\end{cases}
\end{align}
이다. 

- 아무튼 저자들이 주정하고 싶은것은 Theorem 1 에서 정리된 $LOF$의 경계값이 $\frac{direct}{indirect}$에 의존한다는것과 그 바운드가 상당히 작다는것 같다. (그림4에서 보면 진짜 작아보임) 

- 심지어 적당한 가정하에 아래와 같이 표현가능하다. 
\begin{align}
\begin{cases}
direct_{max}=direct\times (1+x\%) \\\\ \\
direct_{min}=direct\times (1-x\%) \\\\ \\
indirect_{max}=indirect\times (1+x\%) \\\\ \\
indirect_{min}=indirect\times (1-x\%)
\end{cases}
\end{align}
여기에서 적당한 가정이라는 것은 $k$의 직접이웃(direct-neighborhood)와 $k$의 간접이웃(indirect-neighborhood)의 출렁임(fluctuate)가 동일하다고 가정하는것과 같다. 즉 $k$의 직접이웃과 간접이웃의 분산구조가 같다고 가정한다는 의미이다. 즉 
\begin{align}
\frac{direct_{max}-direct_{min}}{direct}=\frac{indirect_{max}-indirect_{min}}{indirect}
\end{align}
을 가정한다. 아무튼 이러한 가정덕에 우린 $x\%$라는 하나의 파라메터로 직접 혹은 간접이웃들의 출렁임을 아래와 같이 표현할 수 있다. 그리고 여기에서 $x\%=pct$라고 정의한다. 

- 이전에서는 바운드의 tightness를 다루었고 그 바운드가 tight하기 위한 2가지 조건을 살펴보았다. 이제 우리의 질문은 "그럼 바운드가 타이트하지 않으면 어떻게 되는거야?"라는 것이다. 

### The impact of the parameter minpts 

