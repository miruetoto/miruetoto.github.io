---
layout: post 
title: (창피한) 선형대수학
---

### Eigendecomposition
- 임의의 정사각행렬 ${\bf A}_ {n \times n}$에 대하여 어떠한 벡터 ${\bf v}_ {n \times 1} \neq {\bf 0}$가 적당한값 $\lambda$에 대하여 아래식을 만족하면 $\bf v$를 $\bf A$의 고유벡터라고 한다. 
\begin{align}
{\bf A v}= \lambda {\bf v}
\end{align}
주의할것은 $0$-벡터는 고유벡터로 취급하지 않는다는 것이다. 

- 행렬 $\bf A=I$를 생각하여 보자. 어떠한 벡터 ${\bf v}$를 가져와도 ${\bf Av}={\bf v}$가 되므로 고유값은 $1$이고 고유벡터는 ***all non-zero vectors***다. $0$-벡터는 고유벡터라고 안친다고 했으므로 제외한다. 또한 마찬가지 논리로 $\bf A=O$의 고유값은 $0$이고 고유벡터는 ***all non-zero vectors***다. 

- 임의의 ${\bf A}_ {n \times n}$에 대하여 고유값은 항상 $n$개가 나온다. 단지 고유값을 구하기 위해서는 $det({\bf A}-\lambda{\bf I})=0$을 풀어야 하는데 위의 식을 만족하는 해 $\lambda$가 중근일수가 있으므로 서로 구별되는 고유치의 수는 $n$보다는 작다. 

- 아래와 같은 매트릭스를 $\bf A$를 생각하여 보자. <br/><br/>
```
A<-c(1,1,1,1)
dim(A)<-c(2,2)
```
고유값은 $(1-\lambda)^2-1=0$을 풀어서 나오니까 $\lambda=0$ 이 된다. 고유벡터 ${\bf v}=c(v1,v2)$는 아래 식을 풀면 구할 수 있다. 
\begin{align}
v1 + v2 = 0  \\\\ 
v1 + v2 = 0 
\end{align}
위와 아래의 식이 똑같은게 나왔지만 상관없다. 이걸 풀면 ${\bf v}=c(-1,1)$이 된다. 

- https://kevinbinz.com/2017/03/07/svd/
