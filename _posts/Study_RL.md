---
layout: post
title: (정리) 강화학습 
---

### About this document

- 강화학습공부

- 학부수준 

- 이 포스팅은 아래의 교재를 참고하였다. <br/>
Sutton, R. S., & Barto, A. G. (2018). Reinforcement learning: An introduction. MIT press.

- 여기에서는 다이내믹프로그래밍과 템포랄디퍼런스러닝에 대한 내용을 다룬다. 

--- 

### 암기요소 

***some useful equations***

- 아래는 다양한 형태의 벨만이퀘이션을 모은것이다. <br/><br/>
**(1)** (Bellman equation), p.63, (3.12).
\begin{align}
v_{\pi}(s)=\sum_{a}\pi(a|s)\sum_{s',r}p(s',r|s,a)\Big[r+\gamma v_{\pi}(s')\Big] 
\end{align}
**(2)** (Bellman equation of $q$), p.83, (4.6). 
\begin{align}
q_{\pi}(s,a)=\sum_{s',r} p(s',r | s,a)\Big[r+\gamma v_{\pi}(s')\Big]
\end{align}
**(3)** (Bellman optimality equation), p.68, (3.17). 
\begin{align}
v_* (s)=\max_{a \in {\cal A}(s)}\sum_{s',r} p(s',r | s,a)[r+\gamma v_* (s')]. 
\end{align}
**(4)** (Bellman optimality equation for $q_* $), p.69. 
\begin{align}
q_* (s,a)=\sum_{s',r} p(s',r | s,a)\Big[r+\gamma \max_{a' \in {\cal A}(s')}q_* (s',a')\Big]. 
\end{align}

- 이때 optimal value function 와 optimal $q$-function 의 정의를 잘 생각해보면 아래와 같은 관계가 성립함을 알 수 있다. 
\begin{align}
q_{* }(s,a):= \mathbb{E} \Big(R_{t+1} + \gamma v_{* }(S_{t+1}) ~~ \Big\| ~~ S_t=s, A_t=a \Big). 
\end{align}
여기에서 $R_{t+1}$ 은 행동 $A_t=a$를 취했을 경우 즉시 얻어지는 보상이고 그 이후에 $S_{t+1}$ 상태로 이동한 후에는 계속 최적정책 $\pi^* $ 를 따를텐데 그것을 따름으로 인해서 얻어지는 보상은 $\gamma v_{* }(S_{t+1})$로 표현되었다. 

***algorithms***

- ***폴리시이터레이션 알고리즘*** <br/>
**(1)** (유저) $\pi^{(0)}(a\|s)$ 를 정한다. <br/>
**(2)** (유저) $v(s)$를 초기화 한다. <br/>
**(3)** (인간-인공환경) 각 상태를 순서대로 방문 하면서 아래의 벨만 이퀘이션을 한번씩 업데이트 한다. 
\begin{align}
v(s) \leftarrow \sum_{a}\pi(a|s)\sum_{s',r}p(s',r|s,a)\Big[r+\gamma v(s')\Big] 
\end{align}
**(4)** (인간) 수렴할때까지 (3)를 반복한다. 수렴값은 $v_{\pi^{(0)} }(s)$ 이다. <br/>
**(5)** (인간-인공환경) $v_{\pi^{(0)} }(s)$ 로부터 $q_{\pi^{(0)} }(s,a)$ 를 구한다. 이때 인간은 MDP 정보를 참조한다. <br/>
**(6)** (인간) 더 나은 정책 $\pi^{(1)}$을 찾는다. 이때 인간은 $q^{(0)}(s_1,a)$ 를 참조한다. <br/>
**(7)** 수렴할때까지 (3)-(6) 를 반복한다. 수렴된 정책이 최적의 정책 $\pi^* $ 이다. 

- ***밸류이터레이션 알고리즘*** <br/>
**(1)** (유저) $v(s)$ 를 초기화한다. <br/>
**(2)** (인간-인공환경) 각 상태를 순서대로 방문 하면서 아래의 벨만 옵티멀이퀘이션을 한번씩 업데이트 한다. <br/>
\begin{align}
v(s) \leftarrow \max_{a} \sum_{s',r}p(s',r|s,a)\Big[r+\gamma v(s')\Big] 
\end{align}
**(3)** (인간) 수렴할때까지 (2)를 반복한다. 수렴값은 $v_{\pi^* }(s)$ 이다. <br/>
**(4)** (인간) $V_{\pi^* }(s)$ 로부터 $q_{\pi^* }(s,a)$ 를 구한다. 이때 인간은 MDP 정보를 참조한다. <br/>
**(5)** (인간) 최적의 정책 $\pi^* $을 찾는다. 이때 인간은 $q_{\pi^* }(s,a)$ 를 참조한다. <br/>

- ***살사*** <br/>
**(1) $S$** (유저) 먼저 특정상태 $s_0$를 랜덤하게 생성한다. <br/>
**(2) $A$** (인간) $s_0$에 맞는 적당한 액션 $a_0$를 선택한다. 이때 인간은 $q^{(0)}(s_0,a)$ 를 참조한다. <br/>
**(3) $R$** (환경) $(s_0,a_0)$에 따른 보상 $R_1=r(S_0,A_0)$을 준다. 이때 환경은 $p(r\|S_0,A_0)$ 를 참고한다. (그리고 테이블 $p(r\|S_0,A_0)$ 의 값을 인간은 모른다.) <br/>
**(4) $S$** (환경) $(s_0,a_0)$에 따라 다음상태 $s_1$을 준다. 이때 환경은 $p(s\|s_0,a_0)$ 를 참고한다. (그리고 테이블 $p(s\|s_0,a_0)$ 의 값을 인간은 모른다.) <br/>
**(5) $A$** (인간) $s_1$에 맞는 적당한 액션 $a_1$을 선택한다. 이때 인간은 $q^{(0)}(s_1,a)$ 를 참조한다. <br/>
**(6)** 위의 결과로 샘플 $(s_0,a_0,r_1,s_1,a_1)$ 을 모으면 이것을 이용하여 아래와 같이 큐펑션을 업데이트 한다. 
\begin{align}
q(s_0,a_0) \leftarrow q(s_0,a_0) + \rho \left(r_1 + \gamma q(s_1,a_1)-q(s_0,a_0) \right)
\end{align}
**(7)** 에피소드가 끝날때까지 위의 과정을 반복한다. <br/>

- ***큐러닝*** <br/>
**(1) $S$** (유저) 먼저 특정상태 $s_0$를 랜덤하게 생성한다. <br/>
**(2) $A$** (인간) $s_0$에 맞는 적당한 액션 $a_0$를 선택한다. 이때 인간은 $q^{(0)}(s_0,a)$ 를 참조한다. <br/>
**(3) $R$** (환경) $(s_0,a_0)$에 따른 보상 $r_1=r(s_0,a_0)$을 준다. 이때 환경은 $p(r\|s_0,a_0)$ 를 참고한다. (그리고 테이블 $p(r\|s_0,a_0)$ 의 값을 인간은 모른다.) <br/>
**(4) $S$** (환경) $(s_0,a_0)$에 따라 다음상태 $s_1$을 준다. 이때 환경은 $p(s\|s_0,a_0)$ 를 참고한다. (그리고 테이블 $p(s\|s_0,a_0)$ 의 값을 인간은 모른다.) <br/>
**(5)** 샘플 $(s_0,a_0,r_1,s_1)$ 을 모으면 이것을 이용하여 아래와 같이 큐펑션을 업데이트 한다. 
\begin{align}
q(s_0,a_0) \leftarrow q(s_0,a_0) + \rho \left(r_1 + \gamma \max_{a \in {\cal A}(s_1)} q(s_1,a)-q(s_0,a_0) \right)
\end{align}
**(6)** 에피소드가 끝날때까지 위의 과정을 반복한다. <br/>

--- 

### Finite markov decision process 의 기본 구성 

- 설명의 편의를 위해서 아래그림과 같이 $4\times 4$개의 격자가 있는 세계에서 로봇이 움직이는 일반적인 예제를 특정하자. 음영처리된 부분에 도착하면 로봇이 더이상 움직이지 않는다고 가정하자. 참고로 이렇게 일정한 시간이 지나면 언제가 끝이나는 task 를 **에피소드-태스크** 라고 한다. 이 예제를 포함하여 바둑이나 장기와 같은것도 일정한 시간이 지나면 언젠가 끝나기 때문에 **에피소드-테스크** 의 한 예이다. 반대로 시간이 지나도 끝나지 않는 task 를 **컨티뉴잉-태스크** 라고 한다.
<center><img src="https://github.com/miruetoto/miruetoto.github.io/blob/master/fig/RL/RL_fig1.png?raw=true" height="60%" width="60%"></center>

- ***state***: $4\times 4$ 격자위에서 로봇이 움직이고 있으므로 로봇이 존재할 수 있는 all possible states 는 총 16개이다. 여기에서 음영처리된 부분에 로봇이 도착하면 task가 종료되는데 이런 특징을 가지는 상태를 *terminal-state* 라고 한다. 일반적으로 시점 $t$에서 가능한 state 들의 집합 ${\cal S}$은 terminal state를 제외한 집합을 고려한다. 즉 이 예제의 경우는 
\begin{align}
{\cal S}:=\Big\\{1,2,\dots,14\Big\\}
\end{align}
이다. 시점 $t+1$에서는 음영부분 즉 terminal-state 까지 고려한 집합을 생각해야 한다. 이런 집합을 기호로 ${\cal S}^+$ 로 표시한다. 이 예제에서는 
\begin{align}
{\cal S}^+:=\Big\\{0,1,2,\dots,14,15\Big\\}
\end{align}
가 된다. 여기에서 $s=0$ 이 나타내는 state는 $s=1$ 옆의 음영이고 $s=15$ 가 의미하는 state 는 $s=14$ 옆의 음영이다. (사실 이정도는 말안해도 센스로 알것이라 생각한다.) 강화학습에서는 주로 2개의 시점 $t$와 $t+1$을 많이 생각한다. 시점 $t$에서의 상태를 $S_t$ 라고 하고 시점 $t+1$에서의 상태를 $S_{t+1}$이라고 한다. 엄밀하게 말하면 $S_t, S_{t+1}$은 모두 확률변수이다. 확률변수의 realization은 $s_t$와 $s_{t+1}$로 표시하는 것이 마땅할것 같은데 편의상 $s,s'$으로 표시한다. 그리고 일반적으로 아래를 가정한다. 
\begin{align}
\begin{cases}
s \in {\cal S} \\\\ \\
s' \in {\cal S}^+
\end{cases}
\end{align}

- ***action***: 로봇이 취할 수 있는 액션을 정의하자. 본디 로봇은 동서남북으로 움직일수 있으므로 로봇이 취할 수 있는 all possible actions은 4가지 행동이다. 따라서 
\begin{align}
{\cal A}=\Big\\{\mbox{up, down, right, left} \Big\\}
\end{align}
다만 경우에 따라서 특정상태에서 취할수 있는 행동에 제약이 있을 수 있다. 가령 예를 들면 위의 예제에서 
\begin{align}
s \in \Big\\{1,2,3,4,7,8,11,12,13,14\Big\\}
\end{align}
인 경우와 같이 가장자리에 위치할 경우 그리드 밖으로 나가게 만드는 action 자체를 금지할 수 있다. 예를 들어서 $s=14$라면 $a=\mbox{down}$ 을 취할 수 없다는 식으로 의미이다. 이처럼 현재시점 $t$에서 가지는 상태 $S_t$에 따라서 액션이 달라질 수 있다. 이런 경우를 매 시점 매 상태마다 취할 수 있는 액션스페이스가 다르니까 ${\cal A}(S_t)$와 같은 기호를 고려 하는 것이 마땅하다. 여기에서 ${\cal A}(S_t)$ 는 상태 $S_t$에서 로봇이 가질 수 있는 모든 액션들의 집합을 의미한다. 즉 
\begin{align}
\begin{cases}
A_t \in {\cal A}(S_t) \\\\ \\
A_{t+1} \in {\cal A}(S_{t+1})
\end{cases}
\end{align}
이다. 혹은 아래처럼 표시하기도 한다. 
\begin{align}
\begin{cases}
a \in {\cal A}(s) \\\\ 
a' \in {\cal A}(s')
\end{cases}
\end{align}

- ***reward***: 액션 $A_t$로 부터 얻어지는 보상을 $R_{t+1}$라고 정의한다. 이 책에서 $t$시점의 행동에 대한 보상은 $t+1$ 에 주어진다고 가정하므로 $R_t$가 아니라 $R_{t+1}$ 로 정의하였다. 받을 수 있는 모든 보상의 집합을 ${\cal R}$이라고 정의하자. 예를 들어서 그리드 밖으로 나가면 $-1$점씩, 그리고 terminal-state에 도달하면 +100점씩, 그외에는 무조건 0점씩 준다고 하면 
\begin{align}
{\cal R}=\Big\\{-1,0,100\Big\\}
\end{align}
이다. 

- 그런데 같은 상태에서 같은 행동을 취해도 다른 보상을 줄 수 있다. (될놈될.. 잘 보면 $R_t$가 랜덤변수임..) 따라서 아래식과 같이 상태 $S_t=s$ 에서 행동 $A_t=a$를 취했을 때 얻는 보상 $R_{t+1}$의 평균과 같은 개념을 생각해 볼 수 있다. 
\begin{align}
r(s,a):= \mathbb{E} \Big( R_{t+1} ~ \Big\|~ S_t=s, A_t=a \Big)
\end{align}
이것을 *expected rewards for (state,action) pairs* 라고 한다. 

- 종종 헷갈리는 것이 $r$과 $r(s,a)$ 이다. 둘은 엄연히 다른데, $r$은 $t+1$시점에서의 보상 $R_{t+1}$의 실현값이고 $r(s,a)$는 given $(s,a)$에서 $R_{t+1}$의 평균값이라는 것이다. 아래식을 관찰하면 차이가 명확해 질 것이다. 
\begin{align}
r(s,a):= \sum_{r \in {\cal R}} r \sum_{s' \in {\cal S}}  p(s',r~\|~ s,a) 
\end{align}
여기에서 $p(s',r~ \| ~ s,a)$는 아래에서 좀더 자세히 설명할 것이다. 별로 어려운것은 없고 말 그대로 $(s,a)$가 given 일때 $(s',r)$가 일어날 확률을 의미한다. 보통 $r(s,a)$는 모두 클리어하게 정의 될 수 있는데 이것은 우리가 MDP를 가정하기 때문이다. 

- ***probability of $(s',r)$ given $(s,a)$***<br/><br/>
환경은 $(s,a)$가 정해지면 $(s',r)$을 던져준다. 이 확률을 $p(s',r ~ \| ~ s,a)$ 라고 한다. 즉 
\begin{align}
p(s',r ~ \| ~ s,a) := Pr\Big( S_{t+1}=s', R_{t+1}=r ~ \Big\| ~ S_t=s, A_t=a \Big).
\end{align}
이다. 위의 확률은 아래와 같은 함수로 해석가능하다. 
\begin{align}
{\bf\tilde  P}: {\cal S} \times {\cal A} \times {\cal R} \times {\cal S}^+  \to [0,1]
\end{align}
이다. 여기에서 **틸드**를 쓰는 이유는 conditionality를 강조하기 위함이다. 아무튼 ${\bf \tilde P}$를 정의하기 위해서는 크기가 
\begin{align}
\Big(\|{\cal S}\|,\|{\cal A}\|,\|{\cal R}\|,\|{\cal S}^+\|\Big)
\end{align}
인 4차원 어레이 혹은 텐서에 각각 $[0,1]$ 사이의 값을 코딩해야 한다. 편의상 이러한 어레이를 ${\bf\tilde  P}[s,a,r,s']$이라고 생각하자. 확률에 $0$값을 줄 수 있다는 것을 이용하면 
\begin{align}
{\bf\tilde  P}: {\cal S}^+ \times {\cal A} \times {\cal R} \times {\cal S}^+ \to [0,1]
\end{align}
이라고 정의해도 괜찮다. 따라서 일반성을 잃지 않고 ${\cal S}^+ = {\cal S}$ 라고 놓아도 무방하다. 
\begin{align}
{\bf\tilde  P}: {\cal S} \times {\cal A} \times {\cal R} \times {\cal S}  \to [0,1]
\end{align}
로 정의할 수 있고 ${\bf\tilde  P}[s,a,r,s']$ 의 차원을 $\Big(\|{\cal S}\|,\|{\cal A}\|,\|{\cal R}\|,\|{\cal S}\|\Big)$ 로 생각해도 무방하다. 그리고 당연하겠지만 given $(s,a)$ 일때 환경이 줄 수 있는 모든 경우의 수 $(r,s')$ 에 대한 확률의 총합은 1 이므로 ${\bf\tilde  P}[s,a,r,s']$ 에서 $(s,a)$를 고정시켜서 나오는 2차원 에러이의 총합도 1 이다. 

- 여기에서 ${\bf\tilde  P}[s,a,r,s']$ 은 **환경*(environment)*** 가 가지고 있는 궁극의 테이블 (혹은 비밀노트?) 라고 보면 된다. 환경이 에이전트에게 주는 모든 종류의 피드백은 ${\bf\tilde  P}[s,a,r,s']$ 에 근거한다. 예를들어 ${\bf\tilde  P}[s,a,r,s']$ 를 이용하면 아래와 같이 상태이동확률 *(state-transition probabilites)* 를 구할 수 있다. 
\begin{align}
p(s'|s,a):= Pr\Big(S_{t+1}=s'~  \Big\| ~ S_t=s, A_t=a \Big)= \sum_{r \in {\cal R}}p(s',r~|~s,a):=P_{ss'}^{a}.
\end{align}
위의 식은 그냥 에레이 ${\bf\tilde P}$ 에서 $r$ 차원을 marginally out 한 것이다. 또한 ${\bf\tilde P}[s,a,r,s']$ 로 부터 *expected rewards for (state,action,next-state) triples* 을 아래와 같이 구할 수 있다. 
\begin{align}
r(s,a,s'):=\mathbb{E}\Big( R_{t+1} ~~ \Big\|  ~~ S_t=s, A_t=a, S_{t+1}=s' \Big)=\frac{\sum_{r \in {\cal R}}rp(s',r|s,a)}{p(s'|s,a)}:=R_{ss'}^{a}.
\end{align}
위에서 정의된 $P_{ss'}^{a}$와 $R_{ss'}^{a}$를 ${\bf\tilde P}[s,a,r,s']$ 를 활용하여 얻어내는 방법 즉 코딩하는 방법도 생각해보자. 노동력 낭비라 생각해서 여기에 답을 쓰진 않겠다. 하지만 한번씩 이렇게 생각해보는 것이 내용을 이해하는데 도움이 될 것이다. (원래 책 읽으면서 자신만의 언어로 잘 바꾸면서 읽어야함) 

- ***policy*** : 환경이 가지고 있는 궁극의 테이블이 ${\bf\tilde P}[s,a,r,s']$ 이라고 언급하였다. 에이전트가 가지는 궁극의 테이블은 무엇인가? 그것은 바로 아래와 같이 정의되는 **폴리쉬*(policy)*** 이다. 
\begin{align}
\pi_t:=\pi_t(a|s):=\mathbb{P}\Big(A_t=a ~ \Big\| ~ S_t=s\Big) \in \Pi.
\end{align}
이건 간단하게 말해서 에이전트가 상태 $S_t=s$ 에서 액션 $A_t=a$ 을 취할 확률을 의미한다. (우리는 MDP를 가정하고 있으므로 앞으로 아래첨자는 생략하여 쓰겠다.) 따라서 polish는 차원이 ${\cal S} \times {\cal A}$ 인 ${\boldsymbol \Pi}[s,a]$ 와 같은 테이블에 $[0,1]$ 사이의 확률값들을 기록한 것으로 생각 할 수 있다. 포스팅 도입부에 소개한 $4\times 4$ 그리드가 있는 예제를 다시 떠올려보자. 에이전트가 $s$에 상관없이 로봇을 동서남북 아무방향이라 랜덤으로 움직이는 폴리쉬를 가지고 있다 가정하면 모든 $16\times 4$ 차원의 테이블에 모두 0.25의 값을 넣은 것과 같다. 즉 모든 $(s,a)$ 에 대하여 
\begin{align}
{\boldsymbol \Pi}[s,a] = 0.25 
\end{align}
와 같이 된다. 

--- 

### Polish Iteration 

- 특정 상태 $s \in {\cal S}$에 대하여 폴리쉬 $\pi^{(1)}(a|s)$가 좋은 폴리쉬인지 나쁜 폴리쉬인지 평가할 수 있다. 여기에서 숫자 1 은 첫번째 폴리쉬라는 의미이다. 엔바이러먼트가 가진 테이블 $p(s',r|s,a)$과는 다르게 에이전트가 가진 테이블 $\pi(a|s)$는 업데이트가 된다. 즉 
\begin{align}
\pi^{(1)}(a|s) \to \pi^{(2)}(a|s) \to .. 
\end{align}
이런식으로 업데이트 하면서 더 좋은 테이블로 점점 수정해 나간다. 폴리쉬 $\pi^{(1)}(a|s)$ 이 좋은 폴리쉬인지 나쁜폴리쉬인지는 어떻게 알 수 있을까? 폴리쉬 $\pi(a|s)$ 가 좋은 폴리쉬인지 나쁜폴리쉬인지 평가하기 위해서는 아래를 계산해야 한다. 
\begin{align}
v_{\pi}(s):=\mathbb{E}_ {\pi} \bigg( \sum_{k=0}^{\infty}\gamma^k R_{t+k+1} \bigg\| S_t=s\bigg).
\end{align}
요걸 **밸류펑션*(value function)*** 이라고 한다. 폴리쉬 $\pi(a|s)$에 대한 밸류펑션 $v_{\pi}(s)$은 폴리쉬 $\pi(a|s)$를 반복하여 썼을때 특정 상태 $s \in {\cal S}$에서 받게 될것이라고 기대되는 보상값(=단기+장기 합쳐서)이라고 해석 할 수 있다. 만약 모든 $s \in {\cal S}$에 대하여 아래가 성립한다면 
\begin{align}
v_{\pi'}(s) > v_{\pi}(s)
\end{align}
폴리쉬 $\pi'(a|s)$ 가 폴리쉬 $\pi(a|s)$ 보다 좋은 폴리쉬라고 생각할 수 있다. 이런식으로 확장하면 더 이상 개선할 수 없는 폴리쉬이 있을텐데 이를 **옵티멀폴리쉬*(optimal policy)*** 라고 하고 기호로는 $\pi^* (a|s)$ 와 같이 쓴다. 좀 더 엄밀하게는 가능한 모든 $\pi(a|s)$ 에 대하여 
\begin{align}
\forall s \in {\cal S}: v_{\pi^* }(s) \geq v_{\pi}(s)
\end{align}
이 성립할때 $\pi^* (a|s)$ 를 옵티멀폴리쉬라고 한다. 

- 앞으로 논의를 편하게 하기위해서 현재 폴리쉬를 $\pi(a|s)$라고 하고 나중 폴리쉬를 $\pi'(a|s)$ 이라고 하자. 그리고 아래를 가정하자. 
\begin{align}
\begin{cases}
\pi^{(1)}(a|s) = \pi(a|s) \\\\ \\ 
\pi^{(2)}(a|s) = \pi'(a|s) \\\\ 
\pi^{(\infty)}(a|s) = \pi^* (a|s) 
\end{cases}
\end{align}
지금까지의 논리를 종합하면 <br/><br/>
**step 1.** 특정 폴리쉬 $\pi$ 에 대한 벨류펑션 $v_{\pi}(s)$ 를 계산하고 (이걸 **폴리쉬-이벨류에이션*(policy evaluation)*** 이라함) <br/>
**step 2.** 폴리쉬 $\pi$를 $\pi'$ 로 업데이트 하는것을 반복하면 (이걸 **폴리쉬-인푸르브먼트*(policy improvement)*** 라고함) <br/><br/>
옵티멀폴리쉬 $\pi^* $ 를 쉽게 찾을 수 있을 것 같다. 이런식으로 폴리쉬-이벨류에이션과 폴리쉬-인푸릅먼트를 반복하여 $\pi^* $ 를 찾아내는 과정을 **폴리쉬-이터레이션 알고리즘*(polish iteration algorithm)*** 이라고 한다. 

- **step 1.** 이제 벨류펑션을 계산하는 방법에 대하여 알아보자. 밸류펑션 $v_{\pi}(s)$를 아날래틱하게 풀기 위해서는 모든 $s \in {\cal S}$에 대하여 아래의 식을 만족하는 $v_{\pi}(s)$ 값을 찾아야 한다. 
\begin{align}
v_{\pi}(s)=\sum_{a}\pi(a|s)\sum_{s',r}p(s',r|s,a)\Big[r+\gamma v_{\pi}(s')\Big] 
\end{align}
이것을 **벨만이퀘이션*(Bellman equation)*** 이라고 한다. 이 벨만이퀘이션은 벨류펑션의 정의로부터 유도가능한데 이 유도과정은 p.63에 나와있다. 식이 직관적으로 이해가능하여 굳이 여기에서 유도하진 않겠다. (심심할때 한번씩 풀어보면 좋을듯) 참고로 벨만방정식을 아날래틱하게 푸는것이 힘들어서 보통 알고리즘으로 풀어낸다. 알고리즘적으로 풀어내는 방법은 수렴할때까지 $k$를 증가시키면서 아래를 반복하는 것이다. 
\begin{align}
v_{\pi}^{(k+1)}(s) \leftarrow \sum_{a}\pi(a|s)\sum_{s',r}p(s',r|s,a)\Big[r+\gamma v_{\pi}^{(k)}(s')\Big] 
\end{align}
이렇게 하면 우리가 원하는 $v_{\pi}(s)$를 찾을 수 있다. 즉 $v_{\pi}^{(k)}(s) \to v_{\pi}(s)$ as $k \to \infty$ 가 성립한다. 요 내용은 Sutton p.78 에 있다. 

- 참고로 아래와 같은 벨만이퀘이션 에서 
\begin{align}
v_{\pi}(s)=\sum_{a}\pi(a|s)\sum_{s',r}p(s',r|s,a)\Big[r+\gamma v_{\pi}(s')\Big] 
\end{align}
뒷부분 $\sum_{s',r}p(s',r|s,a)\Big[r+\gamma v_{\pi}(s')\Big]$ 을 **큐펑션*($q$-function)*** 이라고 한다. 즉 $q_{\pi}(s,a)$는 아래와 같이 정의할 수 있다. 
\begin{align}
q_{\pi}(s,a)=:\mathbb{E}_ {\pi}\Big[R_{t+1}+\gamma v_{\pi} (S_{t+1}) ~\|~ S_t=s, A_t=a \Big] =\sum_{s',r}p(s',r|s,a)\Big[r+\gamma v_{\pi}(s')\Big] 
\end{align}
이것은 상태 $s$ 에서만 액션 $a$를 **강제적으로** 취하고 나머지 상태에서는 팔리쉬 $\pi$를 계속 따를 때 얻어지는 보상의 기대값으로 해석할 수 있다. 

- **step 2.** 이제 $\pi$로 부터 더 나은 팔리쉬 $\pi'$을 찾는 과정을 논의하여 보자. 편의상 $\pi$, $\pi'$ 이 모두 디터미니스틱-팔리쉬(deterministic policy) 라고 하자. 따라서 given $s$에 대하여 항상 같은 action을 취하게 된다. 이 경우 그냥 $\pi(s)=a$ 와 같은 식으로 정의할 수 있다. Sutton의 교재 p.82에 보면 ***policy improvement theorem*** 이라는 것이 있는데 이것은 임의의 두 디터미니스틱-팔리쉬 $\pi$ 와 $\pi'$ 에 대하여 
\begin{align}
\forall s \in {\cal S}: q_{\pi}(s,\pi'(s)) \geq v_{\pi}(s)
\end{align} 
이면 아래가 성립한다는 이론이다. 
\begin{align}
\forall s \in {\cal S}: v_{\pi'}(s) \geq v_{\pi}(s)
\end{align}
증명은 p.83 을 참고하자. 요 이론을 활용하면 $\pi$를 $\pi'$로 업데이트 하기 위해서 즉 $\pi$ 보다 더 나은 $\pi'$를 찾기위해서는 단지 아래를 수행하면 된다는 것을 알 수 있다. <br/><br/>
**(1)** given $\pi$ 일때 밸류펑션 $v_{\pi}(s)$ 을 계산하고 그것을 바탕으로 큐펑션 $q_{\pi}(s,a)$를 구함. <br/>
**(2)** 모든 $s \in {\cal S}$에 대하여 큐펑션을 최대화하는 액션을 구하고 이를 새로운 정책에 반영. 즉 
\begin{align}
\pi'(s) \leftarrow \underset{a}{\operatorname{argmax}} q_{\pi}(s,a).
\end{align}
이러한 방식으로 업데이트 된 팔리쉬 $\pi'$를 **$v_{\pi}$에 대한 그리디팔리쉬*(greedy policy with respect to $v_{\pi}$)*** 라고 한다. 

- 이 과정을 거치면 $\pi$ 보다 더 나은 $\pi'$를 찾을 수 있음은 알겠다. 그래서 위의 과정 step 1,2 를 반복해 더 이상 개선될 수 없는 팔리쉬 $\pi'$를 찾았다고 하자. 즉 모든 $s \in {\cal S}$ 에 대하여 $v_{\pi}(s)=v_{\pi'}(s)$ 가 성립한다고 하자. 이 $\pi'$ 가 옵티멀팔리쉬 $\pi^* $ 라고 주장할 수 있을까? 분명 $\pi' $는 초기 정책에 비해서 업데이트와 업데이트를 거듭하여 구해진 **나름 최적의 값**이지만 이것이 과연 모든 $\pi$ 를 고려하여도 최적일 수 있을까? 결론은 yes 이다. 보충 설명으로 Sutton p.83. 하단에 있는 내용을 풀어 쓰겠다. 우선 $v_{\pi'}(s)$ 는 아래와 같이 쓸 수 있다. 
\begin{align}
v_{\pi'}(s)=\sum_{a}\pi(a|s) q_{\pi'}(s,a)
\end{align}
지금은 디터미니스틱 팔리쉬만 고려하고 있음과 $\pi'(s) = \underset{a}{\operatorname{argmax}} q_{\pi}(s,a)$임을 고려하면 
\begin{align}
v_{\pi'}(s)=q_{\pi'}(s,\pi'(s))
\end{align}
이 된다. $\pi'=\pi$ 라는 사실과 $\pi'(s)$ 의 정의를 이용하면 
\begin{align}
v_{\pi'}(s)=q_{\pi'}(s,\pi'(s))=q_{\pi}(s,\pi'(s))= \max_a q_{\pi}(s,a) = \max_a q_{\pi'}(s,a) 
\end{align}
이 된다. 따라서 
\begin{align}
v_{\pi'}(s) = \max_a \sum_{s',r}p(s',r\|s,a)\Big[r+\gamma v_{\pi'}(s')\Big] 
\end{align}
이 되는데 이것은 Sutton p.68, (3.17) 에서 소개한 **벨만 옵티멀리티 이퀘이션*(Bellman optimality equation)*** 과 같다. 그래서 
\begin{align}
v_{\pi'}=v_{\pi^* }
\end{align}
이 성립한다. 

- 이제 다시 아래의 그리드예제로 돌아오자. 
<br/>
<figure>	
<center>	
<img src="https://github.com/miruetoto/miruetoto.github.io/blob/master/fig/RL/RLEX41.png?raw=true" height="70%" width="70%">
<figcaption> [Sutton, p.92] terminal state로 가기전까지 계속 음의보상값 $-1$ 을 받는다. </figcaption>	
</center>	
</figure>
<br/>

- 우선 이 예제의 경우 랜덤팔리쉬에 $\pi$ 에 대하여 폴리쉬-이벨류에이션 한번만 하면 끝난다. 처음에 모든 $s\in {\cal S}$ 에 대하여 $v_{\pi}(s)$ 값에 $0$ 을 넣고 시작하자. 이게 $k=0$ 상태이다. 벨만이퀘이션을 활용하여 한번 업데이트 하면 터미널스테이트를 제외하고 모두 $-1$의 값으로 업데이트 된다. (단기보상+장기보상에서 장기보상은 $0$이고 단기보상은 모두 $-1$ 이므로..) 이게 $k=1$의 상태이다. 이제 $k=2$에서 $s=1$ 에 해당하는 밸류펑션만 연습삼아 구해보자.
\begin{align}
v_{\pi}^{(2)}(1) \leftarrow  \sum_{a}\pi(a|s)\sum_{s',r}p(s',r|s,a)\Big[r+\gamma v_{\pi}^{(1)}(s')\Big] 
\end{align}
우선 상태 $s=1$ 에서 할 수 있는 액션은 $\{\mbox{up, down, left, right}\}$ 이고 그 액션에 대응하여 이동할 수 있는 상태는 $s'=\{1,5,0,2\}$ 이다. 각각의 액션을 할 확률은 모두 $\frac{1}{4}$ 이고 이때 주어지는 단기보상은 모두 $-1$ 장기보상은 
\begin{align}
\Big\\{\gamma v_{\pi}^{(1)}(1), \gamma v_{\pi}^{(1)}(5), \gamma v_{\pi}^{(1)}(0), \gamma v_{\pi}^{(1)}(2) \Big\\} 
\end{align}
가 되고 따라서 
\begin{align}
\\{ -\gamma, -\gamma , 0, -\gamma \\} 
\end{align}
이 된다. 감가율이 없다고 치면 $\gamma=1$로 볼 수 있는데 이때는 상태 $s=1$에서 액션 $\{\mbox{up, down, left, right}\}$ 을 하였을때 얻는 장기보상이 $\{-1,-1,0,-1\}$ 이다. 따라서 
\begin{align}
\sum_{a}\pi(a|s)\sum_{s',r}p(s',r|s,a)\Big[r+\gamma v_{\pi}^{(1)}(s')\Big]  = \frac{3}{4} (-2) + \frac{1}{4} (-1)  = -1.75
\end{align}
가 된다.

- 위의 그리드예제에 폴리쉬이터레이션을 수행한 결과를 살펴보자. 
<br/>
<figure>	
<center>	
<img src="https://github.com/miruetoto/miruetoto.github.io/blob/master/fig/RL/RL42.png?raw=true" height="70%" width="70%">
<figcaption> [Sutton, p.93, Fig 4.2]  </figcaption>	
</center>	
</figure>

- 왼쪽 컬럼은 랜덤 팔리쉬에 대한 평가를 위하여 $v_{\pi}(s)$를 업데이트하며 추론한 것이다. 왼쪽 컬럼을 쭉 따라서 내려오는 과정이 step 1. 폴리쉬-이벨류에이션 에 해당하는 것이다. 오른쪽은 그에 대응하는 그리디팔리쉬 이다. 왼쪽의 **맨마지막 로우 ($k=\infty$)** 에서 오른쪽을 구하는과정이 step 2. 폴리쉬-인프룹먼트 이다. 

- ***주의: 맨 마지막 로우를 계산한뒤에만 실제로 폴리쉬-인푸릅먼트를 한다. 그전에 $k=0,1,3,10$ 에 있는 오른쪽 칼럼은 그냥 $v_{\pi}^{(k)}$에 대한 그리디팔리쉬를 보여준것 뿐이지 실제로 업데이트는 하지 않는다. 처음에 이것때문에 헷갈려서 엄청 고생함.*** 

---

### Value Iteration 

- 폴리쉬-이터레이션-알고리즘 보다 빠른것이 **밸류-이터레이션-알고리즘*(value iteration algorithm)*** 이다. 이것은 옵티멀폴리쉬 $\pi^* $ 를 알고 있다면 그에 대응하는 $v_{\pi^* }(s)$를 유추할 수 있듯이 $v_{\pi^* }(s)$를 알면 그에 대응하는 optimal policy $\pi^* $ 를 쉽게 유추할 수 있다 는 점을 이용해서 $v_{\pi^* }$를 먼저 찾은 다음에  $\pi^* $ 를 찾는 전략이다. 이것은 밸류펑션이 폴리쉬를 결정하는데 필요한 모든 정보를 제공하기 때문에 가능한 것이다. 

- polish iteration algorithm 은 정책과 가치함수를 동시에 업데이트 하면서 $(\pi,v_{\pi}(s))$를 동시에 최적화 하지만 value iteration algorithm 은 $v_{\pi}(s)$ 를 먼저 최적화하고 그담에 $\pi$를 찾는다. 그래서 $v_{\pi}(s)$ 만 최적화 하면 되기 때문에 빠르다. 그럼 어떻게 $v_{\pi}(s)$를 최적화하는 것일까? 아이디어는 생각보다 간단하다. 실제예제로 바로 넘어가기 위해서 아까 탐구했던 그리드 예제로 다시 돌아가자. 
<br/>
<figure>	
<center>	
<img src="https://github.com/miruetoto/miruetoto.github.io/blob/master/fig/RL/RLEX41.png?raw=true" height="70%" width="70%">
<figcaption> [Sutton, p.92] terminal state로 가기전까지 계속 음의보상값 $-1$ 을 받는다.  </figcaption>	
</center>	
</figure>
<br/>

- 이전예제에서 임의의 랜덤폴리쉬 $\pi$에 대한 가치함수를 계산하였다. 이번 예제의 트릭은 가치함수를 한번 업데이트 할때마다 폴리쉬 $\pi$ 를 조금씩 수정해 나간다는 아이디어 이다. (물론 실제로 수정하진 않음) 우선 $k=0$, $k=1$일 경우는 위의 예제와 동일하다. $k=2$인 경우의 계산이 좀 달라진다. 상태 $s=1$에서 액션 $\{\mbox{up, down, left, right}\}$ 을 하였을때 얻는 장기보상이 $\{-1,-1,0,-1\}$ 이다. 따라서 기존에는 
\begin{align}
\sum_{a}\pi(a|s)\sum_{s',r}p(s',r|s,a)\Big[r+\gamma v_{\pi}^{(1)}(s')\Big]  = \frac{3}{4} (-2) + \frac{1}{4} (-1)  = -1.75
\end{align}
와 같이 업데이트 하였다. 그런데 우리는 이미 상태 $s=1$ 에서는 왼쪽으로 가야는 액션을 취해야 좋다는 것을 $v^{(1)}(s)$ 의 정보로 부터 알아낼 수 있다. 그래서  정책 $\pi$를 **따르지 않고** **(탐욕스럽게)**그 순간 이득을 최대화 하는 값으로 업데이트를 할 수 있다. 즉 
\begin{align}
v_{\pi}^{(2)}(s) \leftarrow \sum_{a}\pi(a|s)\sum_{s',r}p(s',r|s,a)\Big[r+\gamma v_{\pi}^{(1)}(s')\Big] 
\end{align}
가 아니라 
\begin{align}
v_{\pi}^{(2)}(s) \leftarrow \max_a \sum_{s',r}p(s',r|s,a)\Big[r+\gamma v_{\pi}^{(1)}(s')\Big] 
\end{align}
와 같이 업데이트 한다. 

- 여기에서 나같은 노테이션충은 '이건 사실 정책 $\pi$를 따르지 않았으므로 업데이트된 $v_{\pi}^{(2)}(s)$ 는 정책 $\pi$ 에 대한 가치함수가 아니라 그 순간 수정된 정책 (편의상 $\tilde{\pi}$ 라고 하자) 에 대한 가치함수가 된다' 고 주장할 수 있다. 타당한 주장이다. 따라서 굳이 표현하면 이 상황에서는 $v_{\tilde \pi}^{(2)}(s)$ 라고 표현하는것이 맞을것 같다. 즉 
\begin{align}
v_{\tilde\pi}^{(2)}(s) \leftarrow \max_a \sum_{s',r}p(s',r|s,a)\Big[r+\gamma v_{\pi}^{(1)}(s')\Big] 
\end{align}
라고 보는게 맞겠다. 물론 $k=0$일때와 $k=1$일때는 폴리쉬의 변화가 없으므로 그대로 $v_{\pi}^{(1)}(s')$은 맞는 표현이다. 하지만 보는 것 처럼 노테이션이 쓸대없이 엄밀하고 유용하지도 않아서 보통 교재에서는 정책을 특정짓지 않고 아래와 같이 쓰는것 같다. 
\begin{align}
v^{(2)}(s) \leftarrow \max_a \sum_{s',r}p(s',r|s,a)\Big[r+\gamma v_{\pi}^{(1)}(s')\Big] 
\end{align}
이게 훨씬 나은것 같다. 아무튼 이 방법으로 하면 $k=2$ 에서 이미 $s=1$에 대응하는 밸류펑션의 값은 $-1.75$ 이 아니라 $-1$로 바끼게 된다. 

- 이제 다시 헷갈렸던 그 그림으로 돌아와보자. 
<br/>
<figure>	
<center>	
<img src="https://github.com/miruetoto/miruetoto.github.io/blob/master/fig/RL/RL42.png?raw=true" height="70%" width="70%">
<figcaption> [Sutton, p.93, Fig 4.2]  </figcaption>	
</center>	
</figure>

- 이 그림에서 폴리쉬-이터레이션은 왼쪽위부터 아래로 쭉 계산하고 (step 1, 폴리쉬-이벨류에이션) 그리고 수렴한뒤에 $v_{\pi}^{(\infty)}$ 에 대한 그리피팔리쉬를 구했다. 즉 위의 그림에서 L형태로 계산이 진행된다. 내가 헷갈렸던 부분은 L형태로 계산을 하지 않고 지그재그식으로 계산하면 더 효율적이지 않나? 라고 생각했기 때문이다. 그리고 이렇게 하는 방식이 바로 벨류-이터레이션-알고리즘이다. 

- 이게 언뜻생각하면 밸류-이터레이션-알고리즘은 현재상태에서 max 가 되는 행동을 취하므로 순간의 이득만 최대화할 뿐 장기이득을 최대화 하지는 못할것 같다. 하지만 그전의 스텝까지 계산한 밸류펑션이 장기이득을 내포하고 있으므로 순간이득에 머물지많은 않는다는 사실을 알 수 있다. 

### Asynchronous Dynamic Programming 

- 벨류-이터레이션과 폴리쉬-이터레이션을 잘 살펴보면 다른 상태의 값을 보고 자신의 값을 업데이트 하는 방식이다. 예를들어서 $k=2$ 인 시점에서 하나의 상태값 $s=1$ 에 대한 밸류펑션을 알기 위해서는 $k=1$ 인 시점에서 $s=1$ 주변의 다른 상태들의 밸류펑션값들이 필요하다. 아무튼 이런 방식을 부스트랩방식이라고 한다. (왜??) 이러한 부스트랩방식에서 중요한것은 $k=2$인 시점을 업데이트 하기 위해서는 $k=1$인 시점에서의 배열만으로 계산해야 한다는 것이다. 따라서 밸류펑션을 저장할 배열이 2개가 필요하다. (과거,현재). 따라서 **인플레이스연산*(in-place)*** 을 하면 안된다. 

- 하지만 이런 규칙을 무시하고 인플레이스 연산을 해보면 어떨까? 이것이 바로 에이-싱크러너스-다이내믹-프로그래밍(Asynchronous Dynamic Programming) 의 아이디어이다. 에이싱크러너스-다이내믹-프로그래밍 에서는 하나의 밸류펑션만 메모리에 저장하고 계속 그걸 업데이트 한다고 보면 된다. 

- 요런방식이 수렴이 안될수도 있을것 같은데 일단 수렴한다고 책에 나와있다. 

### Temporal-Difference Learning 

- 잠깐 몬테카를로방법을 훑어보자. 몬테카를로 방법의 장점은 (1) 환경모델이 없어도 학습할수 있으며 (2) 환경모델이 마코프성질을 크게 벗어나는 경우에도 성능저하가 심하지 않다는 것이다. 또한 (3) 특정한 상태만 골라서 밸류펑션을 계산할 수 있어 계산량을 줄일 수 있다는 부수적인 장점도 있다. 몬테카를로 방법의 단점은 하나의 에피소드가 끝나서 보상이 결정될때까지 업데이트가 이루어지지 않는다는 단점이 있다. 그래서 에피소드-태스크가 아닌이상 이 방법을 쓸 수 없다. 

- 다이나믹-프로그래밍은 환경정보를 완벽하게 알고 있어야 사용가능한 방법이다. 환경에 대한 정보가 없다면 몬테카를로 방법을 써야한다. 하지만 몬테카를로 방식은 에피소드가 끝날때까지 업데이트가 이루어지지 않아서 컨티뉴잉-태스크에 적합하지 않다. 이 단점을 보완하여 에피소드가 끝나기 전에 업데이트를 하는 방법을 고안하면 좋겠다. 즉 몬테카를로 방식의 장점을 취한 새로운 다이나믹-프로그래밍 방식이 있으면 좋겠다. 이런 모티브에서 출발한 것이 **템포랄-디퍼런스-러닝*(temporal-difference learning)*** 이다. 

- 템포랄-디퍼런스-러닝 방식에는 **살사*(sarsa)*** 와 **큐러닝*($Q$-learning)*** 이 있다. 다이나믹-프로그래밍의 두 방법인 폴리쉬-이터레이션과 밸류-이터레이션은 밸류펑션을 업데이트 하는 공통점이 있었는데 템포럴-디퍼런스-러닝의 두 방식인 살사와 큐러닝은 큐함수를 업데이트하는 것을 공통점으로 가진다. 

- 이 챕터에서는 템포랄-디퍼런스-러닝 중 하나인 **살사*(sarsa)*** 에 대하여 알아볼 것이다. 살사의 알고리즘은 아래와 같이 동작한다. <br/>
(1) **s**: (유저) 먼저 특정상태 $s_0$를 랜덤하게 생성한다. <br/>
(2) **a**: (인간) $s_0$에 맞는 적당한 액션 $a_0$를 선택한다. 이때 인간은 $q^{(0)}(s_0,a)$ 를 참조한다. <br/>
(3) **r**: (환경) $(s_0,a_0)$에 따른 보상 $r_1=r(s_0,a_0)$을 준다. 이때 환경은 $p(r\|s_0,a_0)$ 를 참고한다. (그리고 테이블 $p(r\|s_0,a_0)$ 의 값을 인간은 모른다.) <br/>
(4) **s**: (환경) $(s_0,a_0)$에 따라 다음상태 $s_1$을 준다. 이때 환경은 $p(s\|s_0,a_0)$ 를 참고한다. (그리고 테이블 $p(s\|s_0,a_0)$ 의 값을 인간은 모른다.) <br/>
(5) **a**: (인간) $s_1$에 맞는 적당한 액션 $a_1$을 선택한다. 이때 인간은 $q^{(0)}(s_1,a)$ 를 참조한다. <br/>
(6) 위의 결과로 샘플 $(s_0,a_0,r_1,s_1,a_1)$ 을 모으면 이것을 이용하여 아래와 같이 큐펑션을 업데이트 한다. 
\begin{align}
q^{(1)}(s_0,a_0) = (1-\rho) q^{(0)}(s_0,a_0) + \rho \left(r_1 + \gamma q^{(0)}(s_1,a_1)\right)
\end{align}
교재에 따라서 위의 식을 아래와 같이 표현하기도 한다. 
\begin{align}
q^{(1)}(s_0,a_0) = q^{(0)}(s_0,a_0) + \rho \left(r_1 + \gamma q^{(0)}(s_1,a_1)-q^{(0)}(s_0,a_0) \right)
\end{align}
또는 아래와 같이 쓰기도 한다. 
\begin{align}
q(s_0,a_0) \leftarrow q(s_0,a_0) + \rho \left(r_1 + \gamma q(s_1,a_1)-q(s_0,a_0) \right)
\end{align}
(7) 에피소드가 끝날때까지 위의 과정을 반복한다. <br/>

- 위에서 (2),(5) 의 과정에서 $a$는 각각 
\begin{align}
a_0= \underset{a \in {\cal A}(s_0) }{\operatorname{argmax} }  q^{(0)}(s_1,a), \quad a_1= \underset{a \in {\cal A}(s_1) }{\operatorname{argmax} } q^{(0)}(s_1,a)
\end{align}
에 따라서 실현할 수도 있고 혹은 $\epsilon$-그리디로 실현할 수도 있다. 

- Q러닝은 살사와 거의 동일한데 $a_1$을 항상 아래와 같이 그리디로 선택한다는 것이 차이점이다. 
\begin{align}
a_1= \underset{a \in {\cal A}(s_1) }{\operatorname{argmax} } q^{(0)}(s_1,a)
\end{align}

- 따라서 Q러닝의 알고리즘은 살사와 똑같이 한뒤 스텝 (5) 만 바꾸면 된다. <br/>
(1) **s**: (유저) 먼저 특정상태 $s_0$를 랜덤하게 생성한다. <br/>
(2) **a**: (인간) $s_0$에 맞는 적당한 액션 $a_0$를 선택한다. 이때 인간은 $q^{(0)}(s_0,a)$ 를 참조한다. <br/>
(3) **r**: (환경) $(s_0,a_0)$에 따른 보상 $r_1=r(s_0,a_0)$을 준다. 이때 환경은 $p(r\|s_0,a_0)$ 를 참고한다. (그리고 테이블 $p(r\|s_0,a_0)$ 의 값을 인간은 모른다.) <br/>
(4) **s**: (환경) $(s_0,a_0)$에 따라 다음상태 $s_1$을 준다. 이때 환경은 $p(s\|s_0,a_0)$ 를 참고한다. (그리고 테이블 $p(s\|s_0,a_0)$ 의 값을 인간은 모른다.) <br/>
(5) **a**: (인간) $s_1$에 맞는 적당한 액션 $a_1$을 선택한다. 이때 인간은 $q^{(0)}(s_1,a)$ 를 참조하며 항상 이 값이 최대가 되는 행동을 택한다. 즉 
\begin{align}
a_1= \underset{a \in {\cal A}(s_1) }{\operatorname{argmax} } q^{(0)}(s_1,a)
\end{align}
이다. <br/>
(6) 위의 결과로 샘플 $(s_0,a_0,r_1,s_1,a_1)$ 을 모으면 이것을 이용하여 아래와 같이 큐펑션을 업데이트 한다. 
\begin{align}
q(s_0,a_0) \leftarrow q(s_0,a_0) + \rho \left(r_1 + \gamma q(s_1,a_1)-q(s_0,a_0) \right)
\end{align}
여기에서 위의 식은 아래로 다시 바꿔쓸 수 있다. 
\begin{align}
q(s_0,a_0) \leftarrow q(s_0,a_0) + \rho \left(r_1 + \gamma \max_{a \in {\cal A}(s_1)} q(s_1,a)-q(s_0,a_0) \right)
\end{align}
(7) 에피소드가 끝날때까지 위의 과정을 반복한다. <br/>

- 왜 큐러닝이 강력한가? 이를 이해하기 위해서는 살사의 약점은 무엇인를 이해해야 한다. 살시의 약점은 $a_0$를 매우 적절하게 선택하였다고 하더라도, 탐험에 의해서 $a_1$가 잘못 선택되면 $q(s_0,a_0)$의 값이 낮아지는 쪽으로 업데이트 된다는 것이다. 따라서 $(s_0,a_0)$의 값이 낮은 원인이 1) $a_0$가 잘못되었는지 2) $a_1$이 잘못되었는지 알 수 없다는 것이다. 살사를 카운터치는 예제는 아래의 그림과 같이 만들수 있다. 아래의 그림에서 에이전트는 주황색에 있다고 하자. 즉 현재상태 $s_0=\mbox{C2}$ 이다. 터미널스테이트 $\mbox{F1}$으로 가기 위해서는 결국에는 주황색에서 오른쪽으로 가야함이 자명한 상황이다. 즉 $a_0=\mbox{right}$ 가 선택되어야 하고 $s_1=\mbox{D2}$이 되어야 한다. 그런데 $s_1$ 에서 탐험을 한답시고 혹시 $a_1=\mbox{up}$ 이라든가 $a_1=\mbox{down}$ 와 같은 것이 선택되면 그 이후로는 $q(s_0,\mbox{right})$ 에 대한 값이 점점 낮은값으로 업데이트 되게 된다. 
<br/>
<figure>	
<center>	
<img src="https://github.com/miruetoto/miruetoto.github.io/blob/master/fig/RL/sarsa.png?raw=true" height="70%" width="70%">
<figcaption> [살사의 약점을 나타내는 예제]  </figcaption>	
</center>	
</figure>

### 결론

- 개인적으로 강화학습은 딱 이정도까지만 공부해도 어느정도 기초가 쌓인것이라 보면 된다. 그뒤의 내용은 강화학습과 다른 분야를 섞어낸 것들이라 다른분야에 대한 이해가 충분하면 저절로 따라오는 것이다. 가령 예를 들어서 DQN은 딥뉴럴네트워크를 잘 알면 이해하기 쉽다. 

