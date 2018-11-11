---
layout: post 
title: (창피한) 선형대수학
---

### Eigendecomposition
- 임의의 정사각행렬 ${\bf A}_ {n \times n}$에 대하여 어떠한 벡터 ${\bf v}_ {n \times 1} \neq {\bf 0}$가 적당한값 $\lambda$에 대하여 아래식을 만족하면 $\bf v$를 $\bf A$의 고유벡터라고 한다. 
\begin{align}
{\bf A v}= \lambda {\bf v}
\end{align}
주의할것은 $0$벡터는 고유벡터로 취급하지 않는다는 것이다. 

- 다음과 같은 행렬 $A$를 생각하여 보자. <br/><br/>
```
A<-c(k,0,0,k)
dim(A)<-c(2,2)
```
이 행렬은 $k$배만큼 스케일링하는 행렬이다. 어떠한 벡터 ${\bf v}$를 가져와도 ${\bf Av}=k{\bf v}$가 되므로 고유값은 $k$이고 고유벡터는 $0$벡터가 아닌 임의의 모든 벡터이다. ($0$벡터는 고유벡터라고 안친다고 했음) 

- 
