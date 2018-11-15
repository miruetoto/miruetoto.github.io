--- 
layout: post
title: (듀렛) 확률론
--- 

본 포스팅은 대학원 교재인 듀렛책을 바탕으로 작성하였다. 

### 기본정의 
- 확률변수 $X$에 대한 정의를 생각하여 보자. 일단 확률변수는 본질적으로 메저러블-맵핑이므로 메저러블-매핑의 정의에 대하여 알아보자. 어떠한 맵핑 $X$가 두 공간 $(\Omega,{\cal F})$, $(S,{\cal S})$을 이어주는 메저러블-맵핑이라는 의미는 확률변수 $X$가 아래를 만족한다는 것이다. 
\begin{align}
\forall S \in {\cal S}: X^{-1}(S) \in {\cal F}
\end{align}

***"매핑 $X$는 두 메저러블-스페이스 $(\Omega,{\cal F})$, $(S,{\cal S})$ 에 대한 메저러블-맵핑이에요"*** 

라고 해야지 말이 된다는 것이다. 


### 대수의법칙 

### 중심극한정리 

### 마틴게일 
- Durret책을 보면 Conditional Expectation $E(X \vert {\cal F})$를 확률변수 $Y$라고 생각한다. 우선 Conditional Expectation이 왜 확률변수인지부터 설명하는것이 좋을 것 같다. 우선 적당한 확률변수 $X$를 정의하여 보자. 확률변수 즉 메저러블맵핑을 $X$를 정의하기 위해서 적당한 두 메저러블-스페이스를 $(\Omega,\{\cal F})$, $(S,{\cal S})$를 정의한다. 일반적으로 $\Omega=[0,1]$, ${\cal F}_ 0 = \sigma({\cal O})$, $S=\mathbb{R}$, ${\cal S}=\{\cal B}$이다. 즉 $X:([0,1],\sigma([0,1])) \rightarrow (\mathbb{R},{\cal R})$이다. 
