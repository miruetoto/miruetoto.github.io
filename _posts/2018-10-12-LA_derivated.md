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

- 여기에서 ${\bf a}, {\bf b}, {\bf x}$와 같이 소문자로 표시된 기호들은 모두 vector이다. 이 벡터는 col-vector 일수도 있고 row-vector 일수도 있지만 **이 챕터에 한정하여 모든 벡터는 col-vector로 생각하겠다.** 그리고 ${\bf A}, {\bf B}, {\bf X}$와 같이 대문자로 표시된 기호는 모두 매트릭스이다. 보통 매트릭스의 차원은 $n\times p$로 정의한다. 

- 이 챕터에서 ${\bf X}$는 특별한 스트럭처가 없다고 가정할 것이다. 만약에 ${\bf X}$가 스트럭쳐가 있다면 (예를들면 *symm*-매트릭스라든가, *pd*-매트릭스라든가) 미분결과가 달라지게 된다. (진짜 괴롭다.) 

--- 

### 미분에 대한 간단한 정의 
- **(1)** col-vector을 스칼라로 미분하는 경우는 아래와 같다. 
\begin{align}
\frac{\partial {\bf x}}{\partial y}=\frac{\partial rbind(x_1,\dots,x_n)}{\partial y}= rbind\left(\frac{\partial x_1}{\partial y},\dots,\frac{\partial x_n}{\partial y}\right). 
\end{align}
이와 유사하게 row-vector을 스칼라로 미분하는 경우도 아래와 같다. 
\begin{align}
\frac{\partial {\bf x}'}{\partial y}=\frac{\partial cbind(x_1,\dots,x_n)}{\partial y}= cbind\left(\frac{\partial x_1}{\partial y},\dots,\frac{\partial x_n}{\partial y}\right). 
\end{align}

- **(2)** 스칼라를 col-vector으로 미분하는 경우는 아래와 같다. 
\begin{align}
\frac{\partial x}{\partial {\bf y}}=\frac{\partial x}{\partial rbind(y_1,\dots,y_n)}= rbind\left(\frac{\partial x}{\partial y_1},\dots,\frac{\partial x}{\partial y_n}\right). 
\end{align}
이와 유사하게 스칼라를 row-vector으로 미분하는 경우도 아래와 같다. 
\begin{align}
\frac{\partial x}{\partial {\bf y}}=\frac{\partial x}{\partial cbind(y_1,\dots,y_n)}= cbind\left(\frac{\partial x}{\partial y_1},\dots,\frac{\partial x}{\partial y_n}\right). 
\end{align}

- **(3)** 벡터를 벡터로 미분하는 경우는 1) row-vector를 col-vector로 미분하거나 2) col-vector를 row-vector로 미분할 경우에만 벡터간의 미분이 정의된다는 것이다. 이와 같은 이유로 헤시안(Hessian)을 $\frac{\partial}{\partial {\bf x} \partial {\bf x}'}$로 정의한다. 가끔 가다가 col-vector를 col-vector로 미분한 것처럼 정의하는 notation이 있는데 이런건 무시하는것이 정신건강에 좋다. 사실 매트릭스 쿡북에도 (32) 공식 밑에 
\begin{align}
\left[ \frac{\partial {\bf x}}{\partial {\bf y}} \right]_ {ij}=\frac{\partial x_i}{\partial y_j}
\end{align}
와 같이 표현되어 있는데 이것은 엄밀하게 말하면 잘못된 표현이다. **바로 이부분이 짜증나는 부분이다.** 교재 <br/><br/>
Casella, G., Fienberg, S., & Olkin, I. (2007). Matrix Algebra: Theory, Computations, and Applications in Statistics. Springer New York.<br/><br/>
의 (4.11)을 참고하면 임의의 col-vector ${\bf x}_ {m \times 1}$ 와 ${\bf y}_ {n \times 1}$ 에 대하여 아래가 성립한다고 약속하였다. 
\begin{align}
\frac{\partial {\bf x}'}{\partial {\bf y}}=cbind\left(\frac{\partial x_1}{\partial {\bf y}}, \dots, \frac{\partial x_m}{\partial {\bf y}} \right)
\end{align}
다만 편의상 
\begin{align}
\frac{\partial {\bf x}'}{\partial {\bf y}}=\frac{\partial {\bf x}}{\partial {\bf y}}
\end{align}
와 같이 쓰기도 한다고 덧붙이긴 했다. **그렇지만 나는 이런 헷갈리는 표현을 쓰지 않겠다.** 이제 예제로 아래를 증명하여 보자. 이거는 매트릭스 쿡북에는 없는 공식이지만 너무 중요해보이는 공식이라 연습삼아서 풀어보겠다. 
\begin{align}
\frac{\partial {\bf B}{\bf x}}{\partial {\bf x}'}={\bf B}
\end{align}
편의상 ${\bf B}_ {n \times p}, ~~ {\bf x}_ {p \times 1}$라고 가정하겠다. 
\begin{align}
\frac{\partial {\bf B}{\bf x}}{\partial {\bf x}'}=\frac{\partial {\bf B}{\bf x}}{\partial cbind(x_1,\dots,x_p)}=cbind\left( \frac{\partial {\bf B}{\bf x}}{\partial x_1}, \dots, \frac{\partial {\bf B}{\bf x}}{\partial x_n} \right) 
\end{align}
여기에서 ${\bf B}{\bf x}= cbind(B_1,\dots,B_p) rbind(x_1,\dots,x_p)=\sum_{i=1}^{p} B_i x_i$가 성립하므로, 위의 식은 아래와 같이 계산할 수 있다. 
\begin{align}
\frac{\partial {\bf B}{\bf x}}{\partial {\bf x}'}=cbind(B_1,\dots,B_p)={\bf B}
\end{align}
또한 비슷한 논리로 아래가 성립함을 쉽게 보일 수 있다. 
\begin{align}
\frac{\partial {\bf x}'{\bf B}' }{\partial {\bf x}} = {\bf B}'
\end{align}
간단하게 계산해보면 ${\bf x}'{\bf B}'=cbind(x_1,\dots,x_p)rbind(B_1',\dots,B_p')=\sum_{i=1}^{p} x_i B_i' $가 성립하고 따라서 
\begin{align}
\frac{\partial {\bf x}'{\bf B}' }{\partial {\bf x}} = rbind(B_1',\dots,B_p')= (cbind(B_1,\dots, B_p))'={\bf B}'
\end{align}
이다. <br/>

- **(4)** 스칼라를 매트릭스로 미분하는 경우를 살펴보자. 임의의 스칼라를 ${\bf X}_ {n \times p}$로 미분하는것에 대한 기호를 약속하여 보자. 별로 특별할건 없다. 
\begin{align}
\frac{\partial a}{\partial {\bf X}}=cbind\left( \frac{\partial a}{\partial X_1},\dots,\frac{\partial a}{\partial X_p} \right)
\end{align}
혹은 
\begin{align}
\frac{\partial a}{\partial {\bf X}}=rbind\left( \frac{\partial a}{\partial {\bf x}_ 1},\dots,\frac{\partial a}{\partial {\bf x}_ n} \right)
\end{align}
와 같이 약속한다. 

--- 

### 공식

- 아래식이 성립한다. (카셀라책 p.154, Table 4.1 / 매트릭스 쿡북 (69)) 
\begin{align}
\frac{\partial {\bf x}'{\bf a}}{\partial{\bf x}}=\frac{\partial {\bf a}'{\bf x}}{\partial{\bf x}}={\bf a}
\end{align}
증명은 다음과 같이 한다. 
\begin{align}
\frac{\partial {\bf x}'{\bf a}}{\partial{\bf x}}
=\frac{\partial \sum_{i=1}^{n}x_i a_i}{\partial rbind(x_1,\dots,x_n)}
=rbind\left(a_1,\dots,a_n\right)
={\bf a}
\end{align}
반대측도 비슷한논리로 증명하면 된다.

- 아래식이 성립한다. (카셀라책 p.154, Table 4.1) 
\begin{align}
\frac{\partial {\bf x}'{\bf x}}{\partial{\bf x}}=2{\bf x}
\end{align}
증명은 다음과 같이 한다. 
\begin{align}
\frac{\partial {\bf x}'{\bf x}}{\partial{\bf x}}
=\frac{\partial \sum_{i=1}^{n}x_i^2}{\partial rbind(x_1,\dots,x_n)}
=rbind\left(2x_1,\dots,2x_n\right)
=2{\bf x}
\end{align}

- 아래식이 성립한다. (카셀라책 p.154, Table 4.1) 
\begin{align}
\frac{\partial {\bf b}'{\bf A}{\bf x}}{\partial{\bf x}}={\bf A}'{\bf b}
\end{align}
증명은 다음과 같이 한다. 편의상 ${\bf b}_ {n \times 1}$, ${\bf A}_ {n\times p}$, ${\bf x}_ {p \times 1}$이라고 하자. 피미분함수를 풀어보면 아래와 같이 된다. 
\begin{align}
cbind(b_1,\dots,b_n)rbind({\bf a}_ 1, \dots, {\bf a}_ n ) {\bf x} 
= \sum_{i=1}^{n} b_i {\bf a}_ i {\bf x}
= \sum_{i=1}^{n}\sum_{j=1}^{p} b_i a_{ij} x_j
\end{align}
이것을 ${\bf x}=rbind(x_1,\dots,x_p)$로 미분하면 
\begin{align}
rbind\left(\sum_{i=1}^{n} b_i a_{i1},\dots, \sum_{i=1}^{n} b_i a_{ip} \right) = rbind({\bf b}'A_1,\dots,{\bf b}'A_p)
={\bf b}'{\bf A}
\end{align}
와 같이 된다. 

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

- 아래식이 성립한다. (매트릭스 쿡북 (81))
\begin{align}
\frac{ \partial {\bf x}'{\bf B}{\bf x}}{\partial {\bf x}} = ({\bf B} +{\bf B}') {\bf x}
\end{align}
편의상 ${\bf B}_ {n \times n}$, ${\bf x}_ {n \times 1}$으로 가정하자. 
