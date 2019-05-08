--- 
layout: post 
title: (정리) 최적화 
---

### About this doc

- 이 포스트는 최적화 이론에 대한 내용을 정리한 것이다. 아래의 교재를 정리하였다. 이 교재는 약 25400번 정도 레퍼된 엄청난 교재이다. <br/>
Nocedal, J., \& Wright, S. (2006). Numerical optimization. Springer Science & Business Media.

### Ch 12. Theory of Constrained Optimization

- 이 챕터에서는 아래와 같은 형태의 함수에 대한 최적화 문제를 다룬다.
\begin{align}
\underset{ {\bf x} \in \mathbb{R}^p }{ \operatorname{min} } f({\bf x}) \quad \mbox{ subject to } \quad
\begin{cases} {\bf c}_ i({\bf x})=0,~ i \in {\cal E} \\\\ 
{\bf c}_ i({\bf x})\geq 0, ~i \in {\cal I} 
\end{cases}
\end{align}

- 일반적으로 $f$와 $c_i$는 ${\bf x}$의 모든 원소들에 대하여 편미분가능하다고 가정한다. 이것을 단순히 줄여서 $f$와 $c_i$는 ${\bf x}$에 대하여 미분가능하다고 하자. 여기에서 몇몇 사람들은 $c_i({\bf x})$가 ${\bf x}$로 미분가능해야 한다는것이 너무 강한 조건이라고 생각할 수 있다. 예를들어 
\begin{align}
c({\bf x})=\| {\bf x} \|_ 1 \leq 1
\end{align}
와 같은 다이아몬드 형태의 제약조건은 미분가능하지 않기 때문에 우리가 풀수 없는 문제라 생각할 수 있다. 하지만  제약은 미분가능한 제약조건들의 합으로 표현될 수 있다. 이 뿐만 아니라 많은 경우에서 미분불가능해보이는 많은 제약조건들이 미분가능한 제약조건들의 합으로 표현가능하다. 따라서 $c_i({\bf x})$가 ${\bf x}$로 미분가능해야 한다는 제약이 그렇게 강한 조건은 아니다. 

#### A Single Equality constraint 

- 아래와 같이 하나의 **등호** 로 이루어진 제약조건을 가지는 경우를 상상하여 보자. 
\begin{align}
\underset{ {\bf x} \in \mathbb{R}^p }{ \operatorname{min} } f({\bf x}) \quad \mbox{ subject to } \quad c({\bf x})=0
\end{align}
지점 ${\bf x}$에서 출발하여 
