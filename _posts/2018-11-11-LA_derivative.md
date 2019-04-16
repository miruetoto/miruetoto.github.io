---
layout: post 
title: (정리) 선형대수학 - 미분
---

### About this post
- 이번에는 행렬의 미분에 대하여 다룬다. 참고로 행렬의 미분은 책마다 정의하는 노테이션이 다르다. 심오한 철학이 있는것 같지는 않고 그냥 푸는사람이 자기 마음대로 정리한것으로 생각된다. 이것저것 참고하면 정신병 걸리기 딱 좋다. 내 경험상 아래의 참고문헌을 보고 외우는 것이 제일 정신건강에 좋다. <br/>
Petersen, K. B., \& Pedersen, M. S. (2008). The matrix cookbook. Technical University of Denmark, 7(15), 510.

- 본 포스트에서는 나만 쓰는 notation이 있다. 예를들면 $rbind(c(1,2),c(2,4))$라든가 $X[,1]$과 같은 식의 기호이다. 이것은 R프로그래머라면 익숙한 기호이지만 그렇지 않은사람에게는 낯설 수 있다. 나는 이러한 notation이 익숙하여 내맘대로 쓰겠다.

### 매트릭스 표현법

- 보통 통계학과에서 사용하는 디자인매트릭스 ${\bf X}_ {n \times p}$를 아래와 같은 기호로 표현하면 편리하다. 
\begin{align}
{\bf X}=cbind({\bf X}_ 1,\dots,{\bf X}_ p)=rbind({\bf x}_ 1, \dots, {\bf x}_ n)
\end{align}
여기에서 ${\bf X}_ p ={\bf X}[,p]$이고, ${\bf x}_ n = {\bf X}[n,]$이 된다. 이때 ${\bf x}_ n$과 같은 경우는 row-vector임을 유의하자. 

- 이 챕터에서는 일반적인 매트릭스를 ${\bf X}$와 같이 인덱스가 없는 대문자 볼드체로 종종 표시할 것이다. 

- 매트릭스 ${\bf X}$의 column은 ${\bf X}_ 1, {\bf X}_ 2, \dots$와 같이 인덱스가 있는 대문자 볼드체로 종종 표시할 것이다. 따라서 매트릭스 ${\bf A}$의 첫번째 column은 ${\bf A}_ 1$이 된다. 물론 일반적인 교재에서는 ${\bf A}_ 1$와 같이 대문자로 표시된 기호는 보통 매트릭스를 의미하기 때문에 헷갈릴 수 있다. 따라서 ${\bf A}=cbind({\bf A}_ 1, {\bf A}_ 2, \dots, {\bf A}_ p)$와 같이 될수 있는 한 명확하게 명시를 하겠다.   

- 매트릭스 ${\bf X}$의 row는 ${\bf x}_ 1, {\bf x}_ 2, \dots$와 같은 방식으로 종종 표시할 것이다. 따라서 매트릭스 ${\bf a}_ 1$은 매트릭스 ${\bf A}$의 첫번째 row가 된다. 이 역시 헷갈리는 표현인데 일반적인 교재에서 ${\bf a}_ 1$와 같은것은 col-vector를 의미하기 때문이다(여기서는 row-vector). 따라서 이 역시 ${\bf A}=rbind({\bf a}_ 1, {\bf a}_ 2, \dots, {\bf a}_ p)$와 같이 될 수 있는 한 명확하게 명시를 하겠다.    

- 일반적인 row-vector 혹은 col-vector는 ${\bf a}, {\bf b}, {\bf x}$와 같이 인덱스가 없는 소문자 볼드체로 표시할 것이다. 가급적이면 row-vector인지 col-vector인지 명확하게 명시할 예정이지만 만약에 언급이 없다면 col-vector로 생각해도 된다. 

### 매트릭스 연산

***transpose*** 
- ${\bf X}'$는 아래와 같이 표현할 수 있다. 
\begin{align}
{\bf X}'=rbind({\bf X}_ 1',\dots,{\bf X}_ p') = cbind({\bf x}_ 1', \dots, {\bf x}_ n')
\end{align}

- 복소행렬의 경우는 transpose대신에 $H$를 사용한다. 

- 트랜스포즈는 보통 $L_2$-norm을 구할때 사용할 수 있다. 당연한 소리지만 col-vector일 경우와 row-vector일 경우 $L_2$-norm의 정의가 다르다. 즉 $\\| {\bf X}_ p \\|_ 2^2={\bf X}_ p'{\bf X}_ p$이고 $\\| {\bf x}_ n \\|_ 2^2={\bf x}_ n {\bf x}_ n'$이다. 

***행렬곱***
- 임의의 행렬 ${\bf X}_ {n \times p}$, ${\bf T}_ {p \times p'}$에 대하여 행렬곱 ${\bf X}{\bf T}$의 각 원소를 아래와 같이 정의한다. 
\begin{align}
({\bf X}{\bf T})_ {ij}=\sum_{k=1}^{p} x_{ik}t_{kj}
\end{align}

- ${\bf X}'{\bf X}$는 아래와 같이 표현할 수 있다. <br/><br/>
  - $rbind({\bf X}_ 1',\dots,{\bf X}_ p') cbind({\bf X}_ 1,\dots,{\bf X}_ p)= ({\bf X}'_ i {\bf X}_ j) $ 
  - $cbind({\bf x}_ 1',\dots, {\bf x}_ n') rbind({\bf x}_ 1,\dots, {\bf x}_ n) = \sum_{i=1}^{n} {\bf x}_ i' {\bf x}_ i$
  - $rbind({\bf X}_ 1',\dots,{\bf X}_ p') {\bf X} = rbind({\bf X}_ 1'{\bf X},\dots,{\bf X}_ p' {\bf X})$ 
  - ${\bf X}' cbind({\bf X}_ 1,\dots,{\bf X}_ p)=  cbind({\bf X}'{\bf X}_ 1,\dots,{\bf X}'{\bf X}_ p)$<br/><br/>

- ${\bf D}=diag(\lambda_1,\dots,\lambda_p)$이라고 하자. ${\bf A}$에 대하여 아래처럼 쓸 수 있다. <br/><br/>
  - ${\bf A}{\bf D}=cbind({\bf A}_ 1, \dots, {\bf A}_ p)diag(\lambda_1,\dots,\lambda_p)=cbind(\lambda_1{\bf A}_ 1,\dots,\lambda_p {\bf A}_ p)$.  
  - ${\bf D}{\bf A}=diag(\lambda_1,\dots,\lambda_p)rbind({\bf a}_ 1, \dots, {\bf a}_ p)=rbind(\lambda_1{\bf a}_ 1, \dots, \lambda_n{\bf a}_ p)$. <br/><br/>

- 따라서 ${\bf U}_ {n \times p}$, ${\bf D}=diag(\lambda_1,\dots,\lambda_p)$, ${\bf V}'_ {p \times p}$에 대하여 아래와 같이 쓸 수 있다.<br/><br/> 
  - ${\bf U} {\bf D}=cbind({\bf U}_ 1,\dots, {\bf U}_ p)diag(\lambda_1,\dots,\lambda_p)=cbind(\lambda_1{\bf U}_ 1,\dots, \lambda_p{\bf U}_ p)$
  - ${\bf D}{\bf V}'=diag(\lambda_1,\dots,\lambda_p)rbind({\bf V}_ 1', \dots, {\bf V}_ p')=rbind(\lambda_1{\bf V}_ 1', \dots, \lambda_p{\bf U}_ p')$
  - ${\bf U}{\bf D}{\bf V}'= \sum_{i =1}^{p} \lambda_i {\bf U}_ i {\bf V}_ i'$. <br/><br/>
  
- 가끔씩 ${\bf D}$를 정사각행렬이 아니라 사각행렬로 ${\bf D}_ {n \times m}$로 정의할때도 있다. 가령 예를 들어 ${\bf D}_ {2 \times 3}=rbind(c(\lambda_1,0,0),c(0,\lambda_2,0))$ 혹은 ${\bf D}_ {3\times 2}=rbind(c(\lambda_1,0),c(0,\lambda_2),c(0,0))$과 같이 정의하는 식이다. 위의 두 경우 모두 편의상 $diag(\lambda_1,\lambda_2)$로 표현가능하다. 그리고 이 경우에는 행렬곱을 $min(n,m)$까지만 전개하면된다. 예를들면 아래와 같은 식으로 말이다. 
\begin{align}
cbind({\bf U}_ 1,{\bf U}_ 2,{\bf U}_ 3){\bf D}_ {3 \times 2}=cbind({\bf U}_ 1,{\bf U}_ 2,{\bf U}_ 3)diag(\lambda_1,\lambda_2)=cbind(\lambda_1{\bf U}_ 1,\lambda_2{\bf U}_ 2)
\end{align}

***trace***
- $tr({\bf A})=tr({\bf A}')$

- $tr({\bf A}{\bf B}{\bf C})=tr({\bf B}{\bf C}{\bf A})=tr({\bf C}{\bf A}{\bf B})$

- ${\bf a}$가 col-vector일 경우 아래식이 성립한다. 
\begin{align}
{\bf a}'{\bf a}=tr({\bf a}{\bf a}')
\end{align}
당연한 소리지만 ${\bf a}$가 row-vector일 경우는 아래와 같이 된다. 
\begin{align}
{\bf a}{\bf a}'=tr({\bf a}'{\bf a})
\end{align}

--- 
### 미분 (Derivatives) 
- 여기에서 ${\bf a}, {\bf b}, {\bf x}$와 같이 소문자로 표시된 기호들은 모두 col-vector이다. 그리고 ${\bf A}, {\bf B}, {\bf X}$와 같이 대문자로 표시된 기호는 모두 매트릭스이다. 특별한 언급이 없으면 col-vector는 $n\times 1$ 차원을 가진다고 생각하고 매트릭스는 $n \times p$의 차원을 가진다고 가정하였다. 

- 이 챕터에서 ${\bf X}$는 특별한 스트럭처가 없다고 가정할 것이다. 만약에 ${\bf X}$가 스트럭쳐가 있다면 (예를들면 *symm*-매트릭스라든가, *pd*-매트릭스라든가) 미분결과가 달라지게 된다. 

- 이 챕터의 대부분의 내용은 matrix cookbook의 내용을 정리한 것이다. 따라서 참고하기 편하도록 매트릭스 쿡북에 해당하는 수식 인덱스를 달았다. 

--- 

- 이제 아래식부터는 공식의 나열 그리고 증명의 나열이다. 

- 아래식이 성립한다. (매트릭스 쿡북 (69)) 
\begin{align}
\frac{\partial {\bf x}'{\bf a}}{\partial{\bf x}}=\frac{\partial {\bf a}'{\bf x}}{\partial{\bf x}}={\bf a}
\end{align}
증명은 다음과 같이 한다. 
\begin{align}
\frac{\partial {\bf x}'{\bf a}}{\partial{\bf x}}
=\frac{\partial \sum_{i=1}^{n}x_i a_i}{\partial c(x_1,\dots,x_n)}
=c\left(\frac{\partial}{\partial x_1}\sum_{i=1}^{n}x_i a_i}, \dots,  \frac{\partial}{\partial x_n}\sum_{i=1}^{n}x_i a_i} \right)
\end{align}
눈 여겨 볼 사실은 아래와 같다. (1) 분자는 스칼라이다. (2) 분모는 벡터이다. (3) 스칼라를 벡터로 나누면 분모와 같은 차원의 벡터가 결과로 나온다. 

- 아래식이 성립한다. (매트릭스 쿡북 (70))
\begin{align}
\frac{\partial {\bf a}'{\bf X}{\bf b}}{\partial{\bf X}}={\bf a}{\bf b}'
\end{align}
편의상 ${\bf a}_ {n \times 1}, {\bf X}_ {n \times p}, {\bf b}_ {p \times 1}$이라고 하자. 이 역시 아래와 같은 사실을 관찰할 수 있다. (1) 분자는 스칼라이며 (2) 분모는 $n \times p$ 매트릭스이다. (3) 결과는 $n \times p$ 매트릭스이다. 

- 아래식이 성립한다. (매트릭스 쿡북 (71)) 
\begin{align}
\frac{\partial {\bf a}'{\bf X}'{\bf b}}{\partial{\bf X}}={\bf b}{\bf a}' 
\end{align}
이다. 이 경우는 ${\bf a}_ {p \times 1}, {\bf X}_ {n \times p}, {\bf b}_ {n \times 1}$와 같이 생각할 수 있다. 이 경우 역시 (1) 스칼라 분자를 (2) 매트릭스로 미분할때 (3) 결과가 분모와 같은 차원의 매트릭스가 나옴을 확인할 수 있다. 

- 아래식이 성립한다. (매트릭스 쿡북 (77))
\begin{align}
\frac{\partial {\bf b}'{\bf X}'{\bf X}{\bf c}}{\partial {\bf X}}={\bf X}({\bf b}{\bf c}'+{\bf c}{\bf b}')
\end{align} 
간단하게 증명과정을 살펴보자. 여기에서는 편의상 ${\bf a}_ {p \times 1}, {\bf b}_ {p \times 1}, {\bf X}_ {n \times p}$라고 생각하자. 
\begin{align}
\frac{\partial {\bf b}'{\bf X}'{\bf X}{\bf c}}{\partial {\bf X}}
=\frac{ {\bf b}'\partial {\bf X}'{\bf X}{\bf c}}{\partial {\bf X}}+ \frac{ {\bf b}'{\bf X}'\partial {\bf X}{\bf c}}{\partial {\bf X}}
\end{align} 
와 같이 쓸 수 있다. 왼쪽항과 오른쪽항을 각각 계산하여 보자. 먼저 왼쪽항 $\frac{ {\bf b}'{\partial \bf X}'{\bf X}{\bf c}}{\partial {\bf X}}$를 살펴보자. 여기에서 우리는 ${\bf X}{\bf c}$를 ${\bf X}$와 상관없는 어떤 임의의 상수벡터 ${\bf c}_ {n \times 1}^* $로 생각할 수 있다. (1) 분자는 스칼라이고 (2) 분모는 매트릭스이므로 (3) 미분한값은 $n \times p$의 차원을 가진 매트릭스가 나와야 한다. 따라서 ${\bf c}^* {\bf b}'={\bf X}{\bf c}{\bf b}' $가 왼쪽항을 미분한값이 된다. 마찬가지로 오른쪽 항을 미분한 값은 ${\bf X}{\bf b}{\bf c}'$가 된다. 따라서 왼쪽항과 오른쪽 항을 더하면 ${\bf X}({\bf b}{\bf c}'+{\bf c}{\bf b}')$가 된다. 

- 아래식이 성립한다. (매트릭스 쿡북 (78)) 
\begin{align}
\frac{\partial ({\bf B}{\bf x}+{\bf b})' {\bf C} ({\bf D}{\bf x}+{\bf d})}{\partial {\bf x}} = {\bf B}'{\bf C}({\bf D}{\bf x}+{\bf d})+{\bf D}'{\bf C}'({\bf B}{\bf x}+{\bf b})
\end{align} 
증명은 분자를 쭉 풀어서 비슷한 논리로 하면 된다. 별로 특별할게 없는듯. 

- 지금까지는 (1) 분자가 스칼라이고 (2) 분모가 벡터 혹은 매트릭스인 경우를 다루었다. 이 경우 (3) 결과는 항상 분모의 차원과 같은 특징이 있었다. 그래서 보통 (3)의 특징을 이용하여 결과의 차원을 어거지로 짜맞추는 식으로 증명을 하였다. 하지만 벡터를 벡터로 미분한다든지 하는 상황이 존재할 수 있다. 이러한 경우에도 자유롭게 미분을 사용할 수 있어야 한다. 예제로 아래를 증명하여 보자. 
\begin{align}
\frac{\partial {\bf B}{\bf x}}{\partial {\bf x}'}={\bf B}
\end{align}
편의상 ${\bf B}_ {n \times p}, ~~ {\bf x}_ {p \times 1}$라고 가정하겠다. 아래와 같은 표기법을 도입하자. 
\begin{align}
\frac{\partial {\bf B}{\bf x}}{\partial {\bf x}'}=\frac{\partial {\bf B}{\bf x}}{\partial cbind(x_1,\dots,x_p)}=cbind\left( \frac{\partial {\bf B}{\bf x}}{\partial x_1}, \dots, \frac{\partial {\bf B}{\bf x}}{\partial x_n} \right) 
\end{align}
여기에서 ${\bf B}{\bf x}= cbind({\bf B}_ 1, \dots, {\bf B}_ p) rbind(x_1,\dots,x_p)=\sum_{i=1}^{p} {\bf B}_ i x_i$가 성립하므로, 위의 식은 아래와 같이 계산할 수 있다. 
\begin{align}
\frac{\partial {\bf B}{\bf x}}{\partial {\bf x}}=cbind( {\bf B}_ 1, \dots, {\bf B}_ p )={\bf B}
\end{align}
또한 비슷한 논리로 아래가 성립함을 쉽게 보일 수 있다. 
\begin{align}
\frac{\partial {\bf x}'{\bf B}' }{\partial {\bf x}} = {\bf B}'
\end{align}
간단하게 계산해보면 ${\bf x}'{\bf B}'=cbind(x_1,\dots,x_p)rbind({\bf B}'_ 1,\dots, {\bf B}'_ p)=\sum_{i=1}^{p} x_i {\bf B}_ i $가 성립하고 따라서 
\begin{align}
\frac{\partial {\bf x}'{\bf B}' }{\partial {\bf x}} = rbind({\bf B}_ 1, \dots, {\bf B}_ p)= (cbind({\bf B}_ 1,\dots, {\bf B}_ p ))'={\bf B}'
\end{align}
이다. 위의 두가지를 보면서 알수 있는것은 1) row-vector를 col-vector로 미분하거나 2) col-vector를 row-vector로 미분할 경우에만 벡터간의 미분이 정의된다는 것이다. 이와 같은 이유로 헤시안(Hessian)을 $\frac{\partial}{\partial {\bf x} \partial {\bf x}'}$로 정의한다. 가끔 가다가 col-vector를 col-vector로 미분한 것처럼 정의하는 notation이 있는데 이런건 무시하는것이 정신건강에 좋다. 

- 아래식이 성립한다. (매트릭스 쿡북 (81))
\begin{align}
\frac{ \partial {\bf x}'{\bf B}{\bf x}}{\partial {\bf x}} = ({\bf B} +{\bf B}') {\bf x}
\end{align}
편의상 ${\bf B}_ {n \times n}$, ${\bf x}_ {n \times 1}$으로 가정하자. 
