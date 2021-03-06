---
title: (정리) Graph-Laplacian에 대한 점근적성질 
layout: post 
---

### About this doc

- 논문연구 

- 대학원 1-2학년 수준 

- 이 포스팅에서는 그래프라플라시안의 점근적 성질에 대한 포스팅을 하겠다. 

- 아래의 논문을 위주로 정리할 생각이지만 다른논문들도 참고할 것이다.  <br/>
Belkin, M., & Niyogi, P. (2008). Towards a theoretical foundation for Laplacian-based manifold methods. Journal of Computer and System Sciences, 74(8), 1289-1308.

### Basic objects

- ${\cal M}$은 어떤 $\mathbb{R}^{N}$공간에 isometrically embedded 되어 있다고 가정한다. 즉 ${\cal M} \subset \mathbb{R}^N$ 이다. 만약에 3차원 공간에 존재하는 구의 표면에 관심이 있다면 아래와 같이 설정할 수 있다. <br/><br/>
  - $\mathbb{R}^3$ : 3차원 유클리드 공간 
  - ${\cal M}$ : 3차원 유클리드 공간에 존재하는 구의 표면을 나타내는 매니폴드 
  
- 일반적인 라플라스 오퍼레이터는 아래와 같이 정의한다. 
\begin{align}
\triangledown^2 = -\mbox{div} \triangledown
\end{align}
리만 매니폴드 ${\cal M}$위에 있는 라플라스 오퍼레이터는 아래와 같이 표현한다. 
\begin{align}
\triangledown_{\cal M}^2 = -\mbox{div} \triangledown_{\cal M}
\end{align}
그리고 리만매니폴드 위에서 정의되는 라플라스 오퍼레이터를 특별히 라플라스-벨트라미 오퍼레이터라 부르기도 한다. 

- 라플라스 오퍼레이터와 라플라스 벨트라미 오퍼레이터는 다르다. 아까와 같이 $\mathbb{R}^3$ 에 존재하는 구형의 매니폴드 ${\cal M}$ 를 생각해보자. 쉽게 생각해서 ${\cal M}$을 지구의 표면이라고 생각하면 된다. 지구의 모든 표면위에 높이가 100m 인 눈을 쌓는다고 가정하자. (바다든 뭐든 일단 쌓인다고 가정하자..) 이 눈들의 표면을 $h: {\cal M} \to \mathbb{R}$ 이라는 함수를 나타내었다고 하자. 당연히 모든 $v \in {\cal M}$ 에 대하여 
\begin{align}
h(v)=100
\end{align}
가 성립한다. 아무튼 이러한 함수에 $\triangledown^2$ 와 $\triangledown_{\cal M}^2$ 을 각각 적용한다고 생각해보자. 모든 $v \in {\cal M}$ 에 대하여 
\begin{align}
\triangledown_{\cal M}^2 h(v) =0
\end{align} 
이지만 $\triangledown^2 h(v)=0$ 이 성립하지는 않는다. 

- 매니폴드 ${\cal M}$ 위의 특정한 점 $v$에 대한 tangent space를 아래와 같이 표현한다. 
\begin{align}
T_p{\cal M}
\end{align}
 
- $V:{\cal V} \to {\cal M}$ 을 랜덤변수라고 하자. 여기에서 ${\cal V}$는 모든 vertex 의 집합을 의미한다. 편의상 ${\cal V}$의 원소들을 $\nu_1,\nu_2,\dots $ 와 같이 나타내기로 하자. 어벤져스 자료를 예를들면 ${\cal V}$ 는 MCU의 모든 영화(이미만든것+만들어질것)라고 생각할 수 있다. 또한 $V:{\cal V} \to \mathbb{N}$ 인 랜덤변수라고 볼 수 있다. 만약에 Iron man, Avengers: Endgame 2개의 영화가 만들어 졌다고 가정하면 
\begin{align}
v_1 &= V(\nu_1)=V(\mbox{Iron man}) = 1 \\\\ \\
v_2 &= V(\nu_2)=V(\mbox{Avengers: Endgame}) = 2
\end{align}
와 같이 나타낼 수 있다. 확률변수 $V$에 대응하는 probability measure 를 $P_v:{\cal V} \to [0,1] $ distribution function 을 $\mu_v: 2^{\mathbb{N} } \to [0,1]$ 라고 하자. 단 $\mu_v: 2^{\mathbb{N} } \to [0,1]$ 인 이유는 $V:{\cal V} \to \mathbb{N}$ 이기 때문이고 보통 일반적인 $V:{\cal V} \to {\cal M}$ 과 같은 상황이라면 $\mu_v: 2^{\cal M} \to [0,1]$ 와 같이 쓰는것이 맞다. 

- 또한 일반적으로 probability measure 와 distribution function 은 $\mu_v:= P_v \circ V^{-1}$ 의 관계가 있다. 그런데 벨킨의 논문에서는 둘을 같다고 생각한다. 즉 
\begin{align}
\mu_v=P_v \circ V^{-1} = P_v 
\end{align}
가 성립한다고 가정한다. 

- $F_v: {\cal M} \to [0,1]$를 $V$의 distribution function이라고 한다. 따라서 
\begin{align}
F_v(v)=\mu_v((-\infty,v])=P_v(\\{\nu:V(\nu)\leq v\\})
\end{align}
가 성립한다.

- 확률변수 $V$에 대한 probability density function 을 $p_v: {\cal M} \to \mathbb{R}^+$ 라고 정의하자. 이는 $F_v(v)$의 라돈니코딤 도함수로 정의된다. 벨킨의 논문에서는 이것을 $P:{\cal M} \to \mathbb{R}^+$ 로 표현하였다. 

- 벨킨의 논문에서는 쓰는 몇가지 표현을 우리의 방식으로 변경하면 아래와 같다. 
\begin{align}
\mbox{vol}(v)&=dv \\\\ \\
\int_{\cal M} f(v)\mu(dv)&=\int_{\cal M} f(v)p(v)dv =\int_{\cal M} f(v)p(v)\mbox{vol}(v) \\\\ \\
\int_{\cal M} p(v)dv&=\int_{\cal M} p(v)\mbox{vol}(v)=1
\end{align}
벨킨의 논문은 $\int_{\cal M} f(v)\mu(dv)$ 을 $\int_{\cal M} f(v)d\mu(v)$ 로 표현했는데 이것은 틀린표현이다. 
${\cal M}$ 에 존재하는 임의의 sub-manifold ${\cal M}^* $ 에 대하여 아래가 성립한다. 
\begin{align}
\int_{v \in {\cal M}^* } \mu(dv) = \int_{v \in {\cal M}^* } p(v)dv = P({\cal V}^* ) 
\end{align}
여기에서 ${\cal V}^* $ 는 ${\cal M}^* $ 에 대한 inverse image, 즉 ${\cal V}^* = \\{\nu: V(\nu) \in {\cal M}^* \\} $ 이다. 

- $v_1,\dots,v_n$ 이 어떤 랜덤변수 $X_1,\dots,X_n$ 의 realization 이라고 하자. 그리고 $v_1,\dots,v_n$ 이 어떠한 리만매니폴드 ${\cal M}$ 에 존재한다고 하자. (화산자료로 예를들면 $v_1=(latitude, longitude)$ 임) 이때 $v_i, v_j$ 사이에 유클리드 거리(매니폴드내의 최단거리를 의미하는게 아님)를 $w_{ij}$라고 하고 아래와 같이 정의한다. 
\begin{align}
w_{ij}=e^{-\\|v_i-v_j\\|^2/4t_n}
\end{align}
여기에서 $t_n=n^{-\frac{1}{\kappa+2+\alpha} }$ 이다. 여기에서 $\kappa$는 매니폴드의 디멘젼이다. 즉 3차원 매니폴드에 임베딩된 구표면이라면 $\kappa=2$이다. $\alpha$는 적당한 양수이다. 따라서 $t_n$은 $n$이 커질수록 점점 작아지는 어떠한 값이다. 벨킨의 논문에서는 $i=j$ 일 경우 $w_{ij}=0$ 이라는 내용이 없는데 깜빡하고 빼먹은것인지 아니면 의도한 것인지 확실히 알 수 없다. 응의 논문에서는 $w_{ii}=0$ 을 가정하였긴 했지만 무조건 $w_{ii}=0$ 으로 정의하는게 맞는것은 아니다. 참고로 데이비드의 논문은
\begin{align}
w_{ij}=e^{-\\|v_i-v_j\\|^2/2\theta^2}
\end{align}
으로 정의하였다. 그리고 보통의 다른논문들은 $\theta$ 대신에 정규분포 pdf처럼 $\sigma$를 주로 사용한다. 정규분포 pdf와 비교해보면 벨킨의 파라메터 $t_n$과 우리가 일반적으로 생각하는 분산 $\sigma^2$은 아래의 관계가 있다.
\begin{align}
4t_n \sim 2\sigma^2 
\end{align}
따라서 대충 아래의 관계가 성립한다. 
\begin{align}
2 n^{-\frac{1}{\kappa+2+\alpha} }= \frac{1}{\sqrt{n} } 2n^{-\frac{1}{\kappa+\alpha} } \sim \sigma^2 
\end{align}

- 그래프라플라시안 ${\bf L}$ 은 아래와 같이 정의한다. 
\begin{align}
{\bf L}={\bf D}-{\bf W}
\end{align}
위의 노테이션은 데이비드의 표기법을 따랐는데 벨킨의경우도 같다. 아래의 식이 성립한다. 
\begin{align}
{\bf Lf} = rbind\Big( \sum_{j \in {\cal N}_ 1 } W_{1j}(f(v_1)-f(v_j)), \dots, \sum_{j \in {\cal N}_ n } w_{nj}(f(v_n)-f(v_j)) \Big)
\end{align}
보통은 연결이 되지 않으면 $w_{ij}=0$ 으로 표현할 수있으므로 ${\cal N}_ 1 ,\dots, {\cal N}_ n$ 와 같은 표현은 모두 생략가능하다. 따라서 아래와 같이 쓸 수 있다. 
\begin{align}
{\bf Lf} = rbind\Big( \sum_{j \in {\cal N}_ 1 } w_{1j}(f(v_1)-f(v_j)), \dots, \sum_{j \in {\cal N}_ n } w_{nj}(f(v_n)-f(v_j)) \Big)
\end{align}

- ${\bf Lf}$ 의 $i$번째 원소를 ${\cal L}f(v_i)$와 같이 정의하자. 즉 
\begin{align}
{\cal L}f(v_i):= \sum_{j=1}^{n}w_{ij}(f(v_i)-f(v_j))= \sum_{j=1}^{n}e^{-\\|v_i-v_j\\|^2/4t_n}(f(v_i)-f(v_j))
\end{align}
이다. 이를 일반화하면 임의의 $v \in {\cal M}$ 에 대하여서도 아래와 같은 정의가 가능하다. 
\begin{align}
{\cal L}f(v):= \sum_{j=1}^{n}w_{ij}(f(v)-f(v_j))= \sum_{j=1}^{n}e^{-\\|v-v_j\\|^2/4t_n}(f(v)-f(v_j))
\end{align}

- 그런데 $w_{ij}$ 의 값들은 표준화가 안되어 있으므로 $n \to \infty$ 이면 ${\cal L}f(v_i)$ 의 값이나 ${\cal L}f(v)$ 의 값도 발산한다. 그래서 벨킨은 아래와 같은 통계량을 고려한다. 
\begin{align}
\frac{1}{n} {\cal L}f(v) = f(v)\frac{1}{n}\sum_{j=1}^{n}e^{-\\|v-v_j\\|^2/4t_n} - \frac{1}{n} \sum_{j=1}^{n}f(v_j)e^{-\\|v-v_j\\|^2/4t_n}
\end{align}

- 벨킨외 다수는 아래의 정리를 증명했다. 

- ***(Thm 3.1.)*** $v_1,\dots,v_n$ 이 어떠한 매니폴드 ${\cal M}$에서 추출된 샘플이라고 하자. 그리고 $f$는 매니폴드 ${\cal M}$위에서 무한번 미분가능한 어떠한 함수라고 하자. 여기에서 미분은 유클리드 공간이 아닌 매니폴드 위에서의 미분을 의미한다. 즉 $\triangledown^2$ 이 아니라 $\triangledown_{\cal M}^2$ 을 의미한다. 이것을 기호로는 $f \in C^{\infty}({\cal M})$ 와 같이 나타낸다. 임의의 $v \in {\cal M}$에 대하여 아래가 성립한다. 
\begin{align}
\lim_{n\to\infty} \frac{1}{t_n (4\pi t_n)^{\kappa/2}}\frac{1}{n}{\cal L}f(v ) = \frac{1}{\mbox{vol}({\cal M})}\triangledown_{\cal M}f(v )
\end{align}
앞에붙은 텀과 $\kappa$-dimensional 정규분포의 앞에 붙은 factor 가 서로 비슷하다. 
\begin{align}
\frac{1}{t_n (4\pi t_n)^{\kappa/2}} \sim \frac{1}{(2\pi)^{\kappa/2}|\Sigma|} 
\end{align}

- 증명을해보자. 여기에서 
\begin{align}
\frac{1}{n}{\cal L}f(v) = \frac{1}{n}\sum_{j=1}^{n}e^{-\\|v -v_j\\|^2/4t_n}(f(v )-f(v_j))
\end{align}
와 같이 쓸 수 있다. 아래가 성립한다. 
\begin{align}
\mathbb{E} \frac{1}{n} {\cal L}f(v ) =\int_{\xi \in{\cal M} } e^{-\\|v -\xi \\|^2/4t_n}(f(v)-f(\xi))\mu(d\xi)
\end{align}
호핑의 부등식(Hoeffding's inequality)을 쓰면 아래가 성립한다. 
\begin{align}
\mathbb{P} \bigg[\frac{1}{t_n(4\pi t_n)^{\kappa/2} } \Big|\frac{1}{n} {\cal L}f(v) -\mathbb{E} \frac{1}{n} {\cal L}f(v ) \Big| > \epsilon  \bigg]  \leq 2 e^{-1/2\epsilon^2n t_n (4\pi t_n)^{\kappa/2} }.
\end{align}
따라서 아래가 성립한다. 
\begin{align}
\frac{1}{t_n(4\pi t_n)^{\kappa/2} } \frac{1}{n} {\cal L}f(v) \overset{p}{\rightarrow} \frac{1}{t_n(4\pi t_n)^{\kappa/2} } \mathbb{E} \frac{1}{n} {\cal L}f(v ) 
\end{align}

- 지금까지의 결과를 해석해보자. $\frac{1}{t_n(4\pi t_n)^{\kappa/2} }$ 이 분산과 관련된 어떠한 항목이라는 점을 생각하면 결국 위는 
\begin{align}
\frac{1}{n} {\cal L}f(v) \overset{p}{\rightarrow} \mathbb{E} \frac{1}{n} {\cal L}f(v ) 
\end{align}
임을 보인것이다. 

- 이제 아래에 관심을 가져보자. 
\begin{align}
\frac{1}{t_n(4\pi t_n)^{\kappa/2} } \mathbb{E} \frac{1}{n} {\cal L}f(v ) = \frac{1}{t_n(4\pi t_n)^{\kappa/2} } \int_{\xi \in{\cal M} } e^{-\\|v -\xi \\|^2/4t_n}(f(v)-f(\xi))\mu(d\xi)
\end{align}
편의상 $t_n=h$라고 가정하자. 왜냐하면 이것이 결국 밴드윗을 의미하기 때문이다. 즉 
\begin{align}
\frac{1}{h(4\pi h)^{\kappa/2} } \mathbb{E} \frac{1}{n} {\cal L}f(v ) = \frac{1}{h(4\pi h)^{\kappa/2} } \int_{\xi \in{\cal M} } e^{-\\|v -\xi \\|^2/4h}(f(v)-f(\xi))\mu(d\xi)
\end{align}
에 관심을 가지자. 아래가 성립한다. 
\begin{align}
\Bigg \|\int_{\xi \in {\cal B} } e^{-\\|v -\xi \\|^2/4h}f(\xi)\mu(d\xi) - \int_{\xi \in {\cal M} } e^{-\\|v -\xi \\|^2/4h}f(\xi)\mu(d\xi) \Bigg \| \leq \mu({\cal M}-{\cal B}) \sup_{\xi \in {\cal M} }\big(\|f(\xi)\| \big)e^{-d^2/4t}
\end{align}
여기에서 $d=\inf_{\xi \notin {\cal B} } \\|v-\xi\\|^2$ 이다. 

- The Laplacian on a Riemannian manifold: an introduction to analysis on manifolds 를 참고하면 아래가 성립한다. 
\begin{align}
\triangledown_{\cal M} f(v) = \triangledown_{\mathbb{R}^m} f(\)
\end{align}
