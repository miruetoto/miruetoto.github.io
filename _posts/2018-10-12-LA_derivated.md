---
layout: post 
title: (정리) 선형대수학 - 미분
---

### About this post
- 이번에는 매트릭스 혹은 벡터로의 미분을 정리하겠다. 참고로 이 파트는 교재마다 노테이션이 다르다. 따라서 여러책을 참고하면서 공부했다가는 정신병걸리기 딱 좋다. 나도 수 많은 시행착오를 반복하고 이 포스팅에 사용된 노테이션들을 정의하였다. 주로 아래 교재들을 참고하였다. 
<br/><br/>
Petersen, K. B., & Pedersen, M. S. (2008). The matrix cookbook. Technical University of Denmark, 7(15), 510. 
<br/><br/>
Casella, G., Fienberg, S., & Olkin, I. (2007). Matrix Algebra: Theory, Computations, and Applications in Statistics. Springer New York.
<br/><br/>
첫 번째 교재는 이 교재는 임요한 교수님께 응용통계를 배울적에 알게 되었고 두번째 교재는 원중호교수님께 배운 수치선형대수의 교재였다. 매트릭스 쿡북은 상당히 흥미로운 교재이다. 쿡북주제에 엄청난 퀄리티를 자랑한다. 심지어 쿡북주제에 레퍼숫자가 1600을 넘어간다. 두번째 교재는 놀랍게도 저자가 카셀라이다. 그래서 그런지 통계학과에서 자주쓰는 매트릭스 연산들이 잘 정리되어 있다. 

- 사실 매트릭스(혹은 벡터)의 미분은 특별한 철학이 있는게 아니고 특별한 이론이 있는것도 아니다. 그냥 지겹게 계산하면 될 뿐이다. 노테이션이 헷갈려서 혹은 그리고 결과가 종종 직관적이지 않아 어려울 뿐이다. 매트릭스 연산은 통계에서 기본중의 기본이지만 사실 매트릭스 연산에 정통한 사람은 별로 없다. 임요한 교수님의 강의노트에 교수님조차 '요즘도 나는 매트릭스 쿡북을 참고한다'고 하셨는데 이해가 된다. 그냥 여기에 있는 내용은 성경처럼 달달 외우고 있는 것이 좋을것 같다. 

### 몇 가지 약속 

- 여기에서 ${\bf a}, {\bf b}, {\bf x}$와 같이 소문자로 표시된 기호들은 모두 vector이다. 이 벡터는 col-vector 일수도 있고 row-vector 일수도 있지만 **이 챕터에 한정하여 모든 벡터는 col-vector로 생각하겠다.** 그리고 ${\bf A}, {\bf B}, {\bf X}$와 같이 대문자로 표시된 기호는 모두 매트릭스이다. 

- 특별한 언급이 없다면 여기에서 나오는 모든 매트릭스는 스트럭처가 없다고 가정할 것이다. 여기에서 스트럭처가 있다는말은 *symm*-매트릭스라든가, *pd*-매트릭스라든가 하는 매트릭스 라는 것이다. 이렇게 스터럭처가 있는 매트릭스**를** 미분하거나 스트럭처가 있는 매트릭스**로** 미분하경우는 공식이 달라지게 된다. (진짜 괴롭다.) 

--- 

### 미분에 대한 간단한 정의 
- **($\star$)** 가장 중요한것은 차원이다. 미분의 결과는 항상 $\mbox{분모차원} \times \mbox{분자차원}$이 결과로 나온다. 예를들어서 분자의 차원이 
$1\times n$ 이고 분모의 차원이 $n\times 1$ 라면 결과는 $n\times n$ 

- **(1)** col-vector을 스칼라로 미분하는 경우는 아래와 같다. 
\begin{align}
\frac{\partial {\bf z}}{\partial y}=\frac{\partial rbind(z_1,\dots,z_n)}{\partial y}= rbind\left(\frac{\partial z_1}{\partial y},\dots,\frac{\partial z_n}{\partial y}\right). 
\end{align}
이와 유사하게 row-vector을 스칼라로 미분하는 경우도 아래와 같다. 
\begin{align}
\frac{\partial {\bf z}'}{\partial y}=\frac{\partial cbind(z_1,\dots,z_n)}{\partial y}= cbind\left(\frac{\partial z_1}{\partial y},\dots,\frac{\partial z_n}{\partial y}\right). 
\end{align}

- **(2)** 스칼라를 col-vector으로 미분하는 경우는 아래와 같다. 
\begin{align}
\frac{\partial z}{\partial {\bf y}}=\frac{\partial z}{\partial rbind(y_1,\dots,y_n)}= rbind\left(\frac{\partial z}{\partial y_1},\dots,\frac{\partial z}{\partial y_n}\right). 
\end{align}
이와 유사하게 스칼라를 row-vector으로 미분하는 경우도 아래와 같다. 
\begin{align}
\frac{\partial z}{\partial {\bf y}}=\frac{\partial z}{\partial cbind(y_1,\dots,y_n)}= cbind\left(\frac{\partial z}{\partial y_1},\dots,\frac{\partial z}{\partial y_n}\right). 
\end{align}

- **(3)** 벡터를 벡터로 미분하는 경우는 1) row-vector를 col-vector로 미분하거나 2) col-vector를 row-vector로 미분할 경우에만 벡터간의 미분이 정의된다는 것을 유의하자. 이와 같은 이유로 헤시안(Hessian)을 $\frac{\partial^2}{\partial \beta \partial \beta'}$로 정의한다. 가끔 가다가 col-vector를 col-vector로 미분한 것처럼 정의하는 notation이 있는데 **이런건 무시하는것이 정신건강에 좋다.** 사실 매트릭스 쿡북에도 (32) 공식 밑에 
\begin{align}
\left[ \frac{\partial {\bf z}}{\partial {\bf y}} \right]_ {ij}=\frac{\partial z_i}{\partial y_j}
\end{align}
와 같이 표현되어 있는데 이것은 엄밀하게 말하면 잘못된 표현이다. **바로 이부분이 짜증나는 부분이다.** 교재 <br/><br/>
Casella, G., Fienberg, S., & Olkin, I. (2007). Matrix Algebra: Theory, Computations, and Applications in Statistics. Springer New York.<br/><br/>
의 (4.11)을 참고하면 임의의 col-vector ${\bf z}_ {m \times 1}$ 와 ${\bf y}_ {n \times 1}$ 에 대하여 아래가 성립한다고 약속하였다. 
\begin{align}
\frac{\partial {\bf z}'}{\partial {\bf y}}=cbind\left(\frac{\partial z_1}{\partial {\bf y}}, \dots, \frac{\partial z_m}{\partial {\bf y}} \right)
\end{align}
즉 카셀라 교재에서는 엄밀하게 col-vector, row-vector 를 구분하면서 미분하고 있다. 다만 편의상 
\begin{align}
\frac{\partial {\bf z}'}{\partial {\bf y}}=\frac{\partial {\bf z}}{\partial {\bf y}}
\end{align}
와 같이 쓰기도 한다고 덧붙이긴 했다. **그렇지만 나는 이런 헷갈리는 표현을 쓰지 않겠다.** 

- 연습삼아 아래를 증명하여 보자. 
\begin{align}
\frac{\partial {\bf X}\beta}{\partial \beta'}={\bf X}
\end{align}
여기에서 ${\bf X}_ {n \times p}$ 이고 ${\beta}_ {p \times 1}$ 이다. 
\begin{align}
\frac{\partial {\bf X}\beta}{\partial {\beta}'}=\frac{\partial {\bf X}\beta }{\partial cbind(\beta_1,\dots,\beta_p)}=cbind\left( \frac{\partial {\bf X}\beta}{\partial \beta_1}, \dots, \frac{\partial {\bf X}\beta}{\partial \beta_p} \right) 
\end{align}
여기에서 ${\bf X}\beta= cbind(X_1,\dots,X_p) rbind(\beta_1,\dots,\beta_p)=\sum_{k=1}^{p} X_k\beta_k$가 성립하므로, 위의 식은 아래와 같이 계산할 수 있다. 
\begin{align}
\frac{\partial {\bf X}\beta}{\partial \beta'}=cbind(X_1,\dots,X_p)={\bf X}
\end{align}
또한 비슷한 논리로 아래가 성립함을 쉽게 보일 수 있다. 
\begin{align}
\frac{\partial \beta'{\bf X}' }{\partial \beta} = {\bf X}'
\end{align}
간단하게 계산해보면 $\beta'{\bf X}'=cbind(\beta_1,\dots,\beta_p)rbind(X_1',\dots,X_p')=\sum_{k=1}^{k} \beta_k X_k' $가 성립하고 따라서 
\begin{align}
\frac{\partial \beta'{\bf X}' }{\partial \beta} = rbind(X_1',\dots,X_p')= (cbind(X_1,\dots, X_p))'={\bf X}'
\end{align}
이다. <br/>

- 물론 아래와 같이 계산하는 것이 더 쉽다. 
\begin{align}
\frac{\partial {\bf X}\beta}{\partial \beta'}= {\bf X} \frac{\partial{\beta}}{\partial \beta'}={\bf X}
\end{align}
\begin{align}
\frac{\partial \beta'{\bf X}' }{\partial \beta} =\frac{\partial \beta' }{\partial \beta} {\bf X}' = {\bf X}'
\end{align}

--- 

### 공식

- 여기에서는 외워두면 유용한 공식들을 나열한다. 

- 아래식이 성립한다. 
\begin{align}
\frac{\partial {\bf X}\beta}{\partial \beta'}={\bf X}
\end{align}
\begin{align}
\frac{\partial \beta'{\bf X}' }{\partial \beta} = {\bf X}'
\end{align}

- 아래식이 성립한다. 
\begin{align}
\frac{\partial {\bf y}'{\bf X}\beta}{\partial\beta}={\bf X}'{\bf y} 
\end{align}
\begin{align}
\frac{\partial \beta'{\bf X}'{\bf y} }{\partial\beta}={\bf X}'{\bf y} 
\end{align}
아래식이 성립함은 당연하고 위의 식은 ${\bf y}'{\bf X}\beta=\beta'{\bf X}'{\bf y}$임을 이용하면 식이 성립함을 쉽게 이해할 수 있다. 

- 위의 식은 ${\bf Y}$가 multivariate 일 경우도 성립한다. 즉 아래식이 성립한다. 
\begin{align}
\frac{\partial {\bf Y}'{\bf X}{\boldsymbol\beta} } {\partial{\boldsymbol\beta} } ={\bf X}'{\bf Y} 
\end{align}
\begin{align}
\frac{\partial {\boldsymbol\beta}'{\bf X}'{\bf Y} }{\partial{\boldsymbol\beta} }={\bf X}'{\bf Y} 
\end{align}
아래식이 성립함은 당연하다. 위의식이 성립함을 증명하여보자. 편의상 ${\bf Y}_ {n \times 2}$, ${\bf X}_ {n\times p}$, ${\boldsymbol\beta}_ {p \times 2}$ 라고 하자. 아래가 성립한다. 
\begin{align}
{\bf Y}'{\bf X}{\boldsymbol\beta}=\bigl(\begin{smallmatrix}	{\bf Y}'{\bf X}{\boldsymbol\beta}=\begin{pmatrix}
{\bf y}_ 1 \\ 	{\bf y}_ 1' \\\\ \\  
{\bf y}_ 2	{\bf y}_ 2'
\end{smallmatrix}\bigr){\bf X}(\beta_1,\beta_2)	\end{pmatrix}{\bf X}(\beta_1,\beta_2)
=\bigl(\begin{smallmatrix}	=\begin{pmatrix}
{\bf y}_ 1{\bf X}\beta_1 \\ {\bf y}_ 1{\bf X}\beta_2	{\bf y}_ 1'{\bf X}\beta_1 & {\bf y}_ 1{\bf X}\beta_2 \\\\ \\
{\bf y}_ 2{\bf X}\beta_1 \\ {\bf y}_ 2{\bf X}\beta_2	{\bf y}_ 2'{\bf X}\beta_1 & {\bf y}_ 2{\bf X}\beta_2 
\end{smallmatrix}\bigr)	\end{pmatrix}
\end{align} 



- 아래식이 성립한다.
\begin{align}
\frac{\partial \beta'\beta}{\partial\beta}=2\beta
\end{align}
증명은 다음과 같이 한다. 
\begin{align}
\frac{\partial \beta'\beta}{\partial\beta}
=\frac{\partial \sum_{k=1}^{p}\beta_k^2}{\partial rbind(\beta_1,\dots,\beta_p)}
=rbind\left(2\beta_1,\dots,2\beta_p\right)
=2\beta
\end{align}



---

- 아래식이 성립한다. (카셀라책 p.154, table 4.1) 
\begin{align}
\frac{\partial {\bf x}'{\bf A}{\bf b}}{\partial{\bf x}}={\bf b}'{\bf A}
\end{align}
증명은 위와 유사하다. 

- 아래식이 성립한다. (카셀라책 p.154, table 4.1 / 매트릭스 쿡북 (81))
\begin{align}
\frac{ \partial {\bf x}'{\bf B}{\bf x}}{\partial {\bf x}} = ({\bf B} +{\bf B}') {\bf x}
\end{align}
이거 증명이 생각보다 어렵다. 

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
