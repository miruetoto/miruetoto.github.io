---
layout: post 
title: (내 맘대로) 선형대수학
---

선형대수학은 학부 1학년에 배우는 매우 쉬운 과목이지만 기본적인 개념이 헷갈릴때가 있다. 그럴때 마다 다시 선형대수학책을 꺼내들고 공부하게 되는데 이러한 무의미한 반복을 줄이고 싶어서 이 포스팅을 시작하였다. 본 문서에서 정리하는 선형대수학은 통계학과 연관성이 있는 내용위주로 정리하였음을 미리 밝힌다(난 통계학과니깐!). 본 문서를 만들때 참고한 문헌은 아래와 같다. 

- Petersen, K. B., & Pedersen, M. S. (2008). The matrix cookbook. Technical University of Denmark, 7(15), 510.
- Strang, G. (2006). Linear Algebra and Its Applications. Thomson, Brooks/Cole

참고로 본 문서에서는 나만 쓰는 notation이 있다. 예를들면 $rbind(c(1,2),c(2,4))$라든가 $X[,1]$과 같은 식의 기호이다. 이것은 R프로그래머라면 익숙한 기호이지만 그렇지 않은사람에게는 낯설 수 있다. 나는 이러한 notation이 익숙하여 내맘대로 쓰겠다. 그래서 포스팅 제목은 내맘대로 선형대수학이다. 

--- 

### (통계학과를 위한) 기본 매트릭스 연산

***매트릭스의 표현법***
- 보통 통계학과에서 사용하는 디자인매트릭스 ${\bf X}_ {n \times p}$를 아래와 같은 기호로 표현하면 편리하다. 
\begin{align}
{\bf X}=cbind({\bf X}_ 1,\dots,{\bf X}_ p)=rbind({\bf x}_ 1, \dots, {\bf x}_ n)
\end{align}
여기에서 ${\bf X}_ p ={\bf X}[,p]$이고, ${\bf x}_ n = {\bf X}[n,]$이 된다. 이때 ${\bf x}_ n$과 같은 경우는 row-vector임을 유의하자. 
- 이 챕터에서는 위와 유사한 방식으로 매트릭스를 ${\bf A}$와 같이 인덱스가 없는 대문자 볼드체로 종종 표시할 것이다. 
- 매트릭스 ${\bf A}$의 column은 ${\bf A}_ 1, {\bf A}_ 2, \dots$와 같이 인덱스가 있는 대문자 볼드체로 종종 표시할 것이다. 물론 일반적인 교재에서는 ${\bf A}_ 1$는 보통 매트릭스를 의미하기 때문에 헷갈릴 수 있다. 따라서 ${\bf A}=cbind({\bf A}_ 1, {\bf A}_ 2, \dots, {\bf A}_ p)$와 같이 될수 있는 한 명확하게 명시를 하겠다.   
- 매트릭스 ${\bf A}$의 row는 ${\bf a}_ 1, {\bf a}_ 2, \dots$와 같은 방식으로 종종 표시할 것이다. 이 역시 헷갈리는 표현인데 일반적인 교재에서 ${\bf a}_ 1$와 같은것은 col-vector를 의미하기 때문이다(여기서는 row-vector). 따라서 이 역시 ${\bf A}=rbind({\bf a}_ 1, {\bf a}_ 2, \dots, {\bf a}_ p)$와 같이 될 수 있는 한 명확하게 명시를 하겠다.    
- 일반적인 row-vector 혹은 col-vector는 ${\bf a}, {\bf b}, {\bf x}$와 같이 인덱스가 없는 소문자 볼드체로 표시할 것이다. 가급적이면 row-vector인지 col-vector인지 명확하게 명시할 예정이지만 만약에 언급이 없다면 col-vector로 생각해도 된다. 


***transpose*** 
- ${\bf X}'$는 아래와 같이 표현할 수 있다. 
\begin{align}
{\bf X}'=rbind({\bf X}_ 1',\dots,{\bf X}_ p') = cbind({\bf x}_ 1', \dots, {\bf x}_ n')
\end{align}
- 복소행렬의 경우는 transpose대신에 $H$를 사용한다. 
- 트랜스포즈는 보통 $L_2$-norm을 구할때 사용할 수 있다. 당연한 소리지만 col-vector일 경우와 row-vector일 경우 $L_2$-norm의 정의가 다르다. 즉 $\\| {\bf X}_ p \\|_ 2^2={\bf X}_ p'{\bf X}_ p$이고 $\\| {\bf x}_ n \\|_ 2^2={\bf x}_ n {\bf x}_ n'$이다. 

***행렬곱***
- ${\bf X}'{\bf X}$는 아래와 같이 표현할 수 있다. <br/><br/>
  - $rbind({\bf X}_ 1',\dots,{\bf X}_ p') cbind({\bf X}_ 1,\dots,{\bf X}_ p)= \left( {\bf X}'_ i {\bf X}_ j \right)_ {ij}$ 
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
- 여기에서 ${\bf a}, {\bf b}, {\bf x}$와 같이 소문자로 표시된 기호들은 모두 col-vector이다. 그리고 ${\bf A}, {\bf B}, {\bf X}$와 같이 대문자로 표시된 기호는 모두 매트릭스이다. 
- 이 챕터에서는 벡터 ${\bf x}$혹은 매트릭스 ${\bf X}$로 주로 미분 할 것이다. 
- 이 챕터에서 ${\bf X}$는 특별한 스트럭처가 없다고 가정할 것이다. 만약에 ${\bf X}$가 스트럭쳐가 있다면 (예를들면 *symm*-매트릭스라든가, *pd*-매트릭스라든가) 미분결과가 달라지게 된다. 
- 이 챕터의 대부분의 내용은 matrix cookbook의 내용을 정리한 것이다. 따라서 참고하기 편하도록 매트릭스 쿡북에 해당하는 수식 인덱스를 달았다. 

--- 
- 아래식이 성립한다. (매트릭스 쿡북, 69) 
\begin{align}
\frac{\partial {\bf x}'{\bf a}}{\partial{\bf x}}=\frac{\partial {\bf a}'{\bf x}}{\partial{\bf x}}={\bf a}
\end{align}
눈 여겨 볼 사실은 아래와 같다. (1) 분자는 스칼라이다. (2) 분모는 벡터이다. (3) 스칼라를 벡터로 나누면 분모와 같은 차원의 벡터가 결과로 나온다. 

- 아래식이 성립한다. (매트릭스 쿡북, 70)
\begin{align}
\frac{\partial {\bf a}'{\bf X}{\bf b}}{\partial{\bf X}}={\bf a}{\bf b}'
\end{align}
편의상 ${\bf a}_ {n \times 1}, {\bf X}_ {n \times p}, {\bf b}_ {p \times 1}$이라고 하자. 이 역시 아래와 같은 사실을 관찰할 수 있다. (1) 분자는 스칼라이며 (2) 분모는 $n \times p$ 매트릭스이다. (3) 결과는 $n \times p$ 매트릭스이다. 

- 아래식이 성립한다. (매트릭스 쿡북, 71) 
\begin{align}
\frac{\partial {\bf a}'{\bf X}'{\bf b}}{\partial{\bf X}}={\bf b}{\bf a}' 
\end{align}
이다. 이 경우는 ${\bf a}_ {p \times 1}, {\bf X}_ {n \times p}, {\bf b}_ {n \times 1}$와 같이 생각할 수 있다. 이 경우 역시 (1) 스칼라 분자를 (2) 매트릭스로 미분할때 (3) 결과가 분모와 같은 차원의 매트릭스가 나옴을 확인할 수 있다. 


- 아래식이 성립한다. (매트릭스 쿡북, 77)
\begin{align}
\frac{\partial {\bf b}'{\bf X}'{\bf X}{\bf c}}{\partial {\bf X}}={\bf X}({\bf b}{\bf c}'+{\bf c}{\bf b}')
\end{align} 
간단하게 증명과정을 살펴보자. 여기에서는 편의상 ${\bf a}_ {p \times 1}, {\bf b}_ {p \times 1}, {\bf X}_ {n \times p}$라고 생각하자. 
\begin{align}
\frac{\partial {\bf b}'{\bf X}'{\bf X}{\bf c}}{\partial {\bf X}}=\frac{{\bf b}'{\partial \bf X}'{\bf X}{\bf c}}{\partial {\bf X}}+ \frac{{\bf b}'{\bf X}'{\partial \bf X}{\bf c}}{\partial {\bf X}}
\end{align} 
와 같이 쓸 수 있다. 왼쪽항과 오른쪽항을 각각 계산하여 보자. 먼저 왼쪽을 살펴보자. 
\begin{align}
\frac{{\bf b}'{\partial \bf X}'{\bf X}{\bf c}}{\partial {\bf X}}
\end{align}
여기에서 우리는 ${\bf X}{\bf c}$를 ${\bf X}$와 상관없는 어떤 임의의 상수벡터 ${\bf c}^* _ {n \times 1}$로 생각할 수 있다. (1) 분자는 스칼라이고 (2) 분모는 매트릭스이므로 (3) 미분한값은 $n \times p$의 차원을 가진 매트릭스가 나와야 한다. 따라서 ${\bf c}^* {\bf b}'={\bf X}{\bf c}{\bf b}' $가 왼쪽항을 미분한값이 된다. 마찬가지로 오른쪽 항을 미분한 값은 ${\bf X}{\bf b}{\bf c}'$가 된다. 

- 아래식이 성립한다. (매트릭스 쿡북, 78) 
\begin{align}
...asdf
\end{align} 

---

### Decomp - Eigenvalues and Eigenvectors.  
- 임의의 정사각행렬 ${\bf A}_ {n \times n}$에 대하여 어떠한 벡터 ${\bf v}_ {n \times 1} \neq {\bf 0}$가 적당한값 $\lambda$에 대하여 아래식을 만족하면 $\bf v$를 $\bf A$의 고유벡터라고 한다. 
\begin{align}
{\bf A v}= \lambda {\bf v}
\end{align}
주의할것은 $0$-벡터는 고유벡터로 취급하지 않는다는 것이다. 

- **고유값이 없는 정사각행렬은 없다.**
고유값이 없다는 말은 $det({\bf A}-\lambda {\bf I})=0$을 만족하는 $\lambda$가 없다는 말인데 임의의 $n$차 다항식의 해는 항상 존재하므로(정확하게는 모르겠지만 왠지 이런 정리가 있을것 같다) 어떠한 정사각행렬 ${\bf A}_ {n \times n}$도 $n$개의 고유값을 가진다. 다만 중복근이 존재할 수 있으므로  ${\bf A}_ {n \times n}$가 서로 다른 $n$개의 고유값을 가질 필요는 없다. 

- **하나의 고유값에 대응하는 고유벡터가 반드시 하나는 존재한다.**
일단 ${\bf A}_ {n \times n}$는 항상 $n$개의 고유값을 가진다. 그중에서 하나의 고유값 $\lambda^* $를 fix했다고 하자. 고유벡터가 없다는 말은 
\begin{align}
\left({\bf A}-\lambda^* {\bf I}\right){\bf v}=0
\end{align}
를 만족하는 벡터 $\bf v$는 오직 $\bf v=0$인 경우일 때 뿐이란 것을 의미한다. 그런데 고유값의 정의상 $det({\bf A}-\lambda^* {\bf I})=0$이 된다. 따라서 행렬 ${\bf A}-\lambda^* {\bf I}$은 *sing*-매트릭스가 된다. 따라서 ${\bf A}-\lambda^* {\bf I}$의 rows는 일차독립이 아니다. 따라서  $({\bf A}-\lambda^* {\bf I})\bf v=0$을 만족하는 $\bf v \neq 0$ 인 벡터가 적어도 하나는 존재한다. 

- 따라서 모든 정사각행렬은 고유벡터와 고유값을 반드시 가진다. 또한 하나의 고유값에 대응하는 고유벡터가 반드시 하나는 있다. 하지만 하나의 고유값에 반드시 하나의 고유벡터만 대응되는 것은 아니다. 예를들어서 $\bf A=I$일 경우와 $\bf A=O$일 경우가 그렇다. $\bf A=I$의 고유값은 $1$이고 고유벡터는 ***all non-zero vectors***다. 그리고 $\bf A=O$의 고유값은 $0$인데 고유벡터는 역시 ***all non-zero vectors***다. 이러한 사실들이 말해주는 것은 하나의 고유치에 대응하는 고유벡터가 무한개일 수도 있다는 것이다. 

- ${\bf A}_ {n \times n}$의 서로 다른 고유값에 대응하는 고유벡터는 선형적으로 독립이다. 요건 서로 다른 고유값 2개를 잡고 귀류법을 쓰면 엄청 쉽게 증명할 수 있다. 

- 지금까지 정리한 사항을 잘 추론하면 아래와 같은 사실들을 정리할 수 있다. 
  1. $n \times n$-행렬은 반드시 $n$개의 고유값을 가진다. <br/>
  2. 이 고유값들이 중복근일 경우가 있으므로 서로 다른 $n$개의 고유값을 가질 필요는 없다. <br/>
  3. 한개의 고유값에는 반드시 한개 이상의 고유벡터가 대응한다. (특정한 고유치를 고정하면 그에 대응하는 고유벡터는 항상 존재해야 하므로) <br/>
  4. 하지만 한개의 고유치에 반드시 한개의 고유벡터"만" 대응할 필요는 없다. 때에 따라서 한개의 고유치에 여러개의 고유벡터가 대응할수도 있다. <br/>
  5. 이러한 경우를 종합하면 $n \times n$-행렬의 아이겐벡터가 *span*하는 차원이 $n$보다 작을경우는 1) 고유값들이 중복근을 가지며 (즉 2의 케이스) 2) 그 중복근에 대응하는 고유벡터들이 *span*하는 공간의 차원이 중복근의 수보다 작은 경우이다. **그리고 바로 이 경우가 ${\bf A}_ {n \times n}$을 대각화할 수 없는 경우에 해당한다.** <br/>
  
- ${\bf A}_ {n\times n}$이 대각화가능할 필요충분조건은 $\bf A$의 고유벡터들이 *span*하는 공간이 $n$차원일 경우이다. 가끔 가다가 ${\bf A}_ {n\times n}$이 대각화가능할 필요충분조건이 $\bf A$의 랭크가 $n$이라고 착각하는 사람들이 있는데 이것은 사실이 아니다. $\bf A$의 랭크가 $n$이 아니어도 대각화 가능한 행렬은 얼마든지 있다. 바로 위에서 예를 든것처럼 ${\bf A}=0$도 대각화 가능하고 ${\bf A}=rbind(c(1,2),c(2,4))$와 같은 행렬도 (*real-symm*-매트릭스이므로) 대각화 가능하다. 

- **모든 *Hermitian*-매트릭스는 1) 실수의 고유값을 가지며 2) 아이겐벡터들이 서로 직교한다.** 행렬 $\bf A$의 성분들이 모두 실수이면 *symm*-매트릭스가 곧 *에르미트*-매트릭스가 된다. 따라서 **"모든 *real-symm*-매트릭스는 1) 실수의 고유값을 가지며 2) 고유벡터들이 서로 직교한다."** 라고 생각할 수 있다. 

- *real-symm*-매트릭스 ${\bf A}_ {n \times n}$는 아래와 같이 표현할 수 있다. 특별히 수학적인 의미가 있는건 아니고 단순히 전개한것 뿐이지만 매트릭스 표현법에 익숙해지기 위해서 한번 읽어보자. 
\begin{align}
{\bf A} & cbind({\bf v}_ 1, \dots, {\bf v}_ n)=cbind({\bf A}{\bf v}_ 1, \dots, {\bf A}{\bf v}_ n)=cbind(\lambda_1 {\bf v}_ 1, \dots, \lambda_n {\bf v}_ n) \\\\ 
&=cbind({\bf v}_ 1, \dots, {\bf v}_ n)diag(\lambda_1,\dots,\lambda_n)
\end{align}
따라서 *real-symm*-매트릭스 ${\bf A}_ {n \times n}$는 아래와 같이 표현 가능하다. 
\begin{align}
{\bf A}{\bf P}={\bf P}{\bf D} ~~ or ~~ {\bf A}={\bf P}{\bf D}{\bf P}'
\end{align}
여기에서 ${\bf P}=cbind({\bf v}_ 1, \dots, {\bf v}_ n)$이고 ${\bf D}=diag(\lambda_1,\dots,\lambda_n)$이다. 그리고 ${\bf A}={\bf P}{\bf D}{\bf P}'$를 그대로 풀면 아래와 같이 쓸 수 있다. 
\begin{align}
{\bf A}&=cbind({\bf v}_ 1, \dots, {\bf v}_ n) diag(\lambda_1, \dots, \lambda_n) rbind({\bf v}'_ 1, \dots, {\bf v}'_ n) \\\\ \\\\
&=cbind(\lambda_1{\bf v}_ 1, \dots, \lambda_n {\bf v}_ n) rbind({\bf v}'_ 1, \dots, {\bf v}'_ n) \\\\ \\
&=\sum_{i=1}^{n} \lambda_i {\bf v}_ i {\bf v}'_ i
\end{align}
특히 
\begin{align}
{\bf A}={\bf P}{\bf D}{\bf P}'=\sum_{i=1}^{n} \lambda_i {\bf v}_ i {\bf v}'_ i
\end{align}
와 같은 표현이나 
\begin{align}
{\bf A}{\bf P}={\bf P}{\bf D}
\end{align}
와 같은 표현은 자주나오므로 익숙해지는 것이 좋다. 또한 위의 과정에서 아래와 같이 매트릭스 계산하는 방식도 눈여겨볼만 하다. 

  1. $cbind(\lambda_1 {\bf v}_ 1, \dots, \lambda_n {\bf v}_ n) = cbind({\bf v}_ 1, \dots, {\bf v}_ n)diag(\lambda_1,\dots,\lambda_n)$. <br/>
  2. $cbind(\lambda_1{\bf v}_ 1, \dots, \lambda_n {\bf v}_ n) rbind({\bf v}'_ 1, \dots, {\bf v}'_ n)=\sum_{i=1}^{n} \lambda_i {\bf v}_ i {\bf v}'_ i$. <br/><br/>


- *에르미트*-매트릭스 ${\bf A}_ {n \times n}$의 모든 고유값이 양수일때 이러한 행렬 $\bf A$를 *(에르미트)-pd*-매트릭스라고 부른다. *pd*-매트릭스는 기본적으로 *에르미트*-매트릭스이어야 하므로 이를 앞으로 *(에르미트)-pd*-매트릭스라 표현하겠다. *(에르미트)-pd*-매트릭스는 말그대로 1) 에르미트행렬이며 2) 모든 고유치가 양수라는 조건을 만족해야하는데 이러한 2가지 조건이 만족되면 모든 *non-zero vector* ${\bf x}$에 대하여 아래식을 만족한다. 
\begin{align}
{\bf x}^{H}{\bf A}{\bf x}>0
\end{align}
이는 ${\bf A}=PDP^{H}$꼴로 변형하고 위의 식의 대입하면 쉽게 증명할 수 있다. 반대로 어떠한 정사각행렬 ${\bf A}$가 모든 *non-zero vector* ${\bf x}$에 대하여 위의 식을 만족하면 이 행렬 ${\bf A}$는 1) *에르미트*-매트릭스이며 2) 모든 고유치가 양수인 행렬이 된다(이것도 쉽게 증명된다). 즉 아래조건은 *(에르미트)-pd*-매트릭스의 정의처럼 사용가능하다. 
\begin{align}
\forall {\bf x}\neq {\bf 0}: ~~ {\bf x}^{H}{\bf A}{\bf x}>0
\end{align}

--- 
***Eigenvalue, Eigenvector에 대한 미세먼지 팁***
- **모든 고유값들의 합은 원래 행렬의 trace와 같고 모든 고유값들의 곱은 원래 행렬의 determinent와 같다. 이 사실은 임의의 정사각행렬에서 성립한다.** 즉 임의의 정사각행렬에서 $tr({\bf A}_ {n \times n})=\sum_{i=1}^{n} \lambda_i$이고 $det({\bf A}_ {n \times n})=\prod_{i=1}^{n}\lambda_i$이다. 이 사실은 그냥 증명없이 외우자. 

- ***sing*-매트릭스의 고유값에는 0이 적어도 하나는 포함되어 있다.** 이 사실은 **모든 고유값들의 곱은 원래 행렬의 determinent와 같다**는 사실을 떠올리면 쉽게 이해할 수 있다. 

- $A_{n \times n}$모든 col의 합이 1인 행렬을 *markov*-매트릭스라고 한다. **markov-매트릭스의 고유값들중 최소한 하나는 1이고 나머지 고유값은 모두 1보다 작다.** 이 사실은 그냥 증명없이 외우자. 

- **임의의 $2\times 2$-행렬 ${\bf A}=rbind(c(a,b),c(c,d))$에서 고정된 고유값 $\lambda^* $에 대한 고유벡터는 $c(-b,a-\lambda^* )$이다.** 이건 그냥 혼자 유추한것인데 상당히 유용하다. 증명은 그렇게 어렵지 않다. 우선 임의의 $2 \times 2$-행렬의 고유값과 고유벡터는 항상 존재한다. 고정된 고유값 $\lambda^* $에 대한 *characteristic polynomial*은 아래와 같이 쓸 수 있다. 
\begin{align}
det\left({\bf A}-\lambda^* {\bf I}\right)=0
\end{align}
앞에서 언급하였듯이 고유치 $\lambda^* $의 정의에 의해서 위의 식은 항상 성립한다. 따라서 행렬 ${\bf A}-\lambda^* {\bf I}$는 *sing*-매트릭스이다. 따라서 0을 고유값으로 가지며 0에 해당하는 고유벡터는 ${\bf v}=(-b,a-\lambda^* )$이다. 그런데 ${\bf v}$는 행렬 ${\bf A}-\lambda^* {\bf I}$에서 고유값 0에 대한 고유벡터이기도 하지만 행렬 ${\bf A}$에서 고유값 $\lambda^* $에 대한 고유벡터이기도 하다. 왜냐하면 
\begin{align}
\left({\bf A}-\lambda^* {\bf I}\right){\bf v}=0
\end{align}
이므로, 
\begin{align}
{\bf Av}=\lambda^* {\bf v}
\end{align}
이기 때문이다. 

- 매트릭스 ${\bf A}=rbind(c(0.5,0.5),c(0.5,0.5))$를 생각하여 보자. $\bf A$는 *sing*-매트릭스이므로 0을 고유값으로 가진다. 또한 $\bf A$는 *markov*-매트릭스 이므로 1을 고유값으로 가진다(그리고 다른 고유값은 모두 1보다 작음). 종합하면 $\bf A$의 고유값은 0과 1이다. 따라서 고유벡터는 $c(-0.5,0.5)$, $c(-0.5,-0.5)$이다. 

- **모든 고유값들의 합은 원래 행렬의 trace와 같고 모든 고유값들의 곱은 원래 행렬의 determinent와 같다.** 이 2개의 사실을 연립하여 풀면 모든 $2 \times 2$-매트릭스의 고유값을 쉽게 구할 수 있다. 가령 예를 들면 ${\bf A}=rbind(c(1,2),c(2,4))$인 행렬을 생각하자. $\lambda_1+\lambda_2=5$ 이고 $\lambda_1 \lambda_2=0$ 이다. 따라서 고유값은 0과 5임을 쉽게 유추할 수 있다. 그리고 고유값만 알면 고유벡터는 $c(-b,\lambda-a)$로 바로 찾아질 수 있다. 예를 들어서 이 행렬에서 $0$에 대응하는 고유벡터는 $c(-2,1)$이고 $5$에 대응하는 고유벡터는 $c(-2,-4)$이다. 

- 임의의 정사각행렬 ${\bf A}$의 값이 모두 실수여도 그 고유값이 반드시 실수인것은 아니다. ${\bf A}=rbind(c(0,-1),c(1,0))$을 생각하여 보자. $\lambda_1+\lambda_2=0$ 이고 $\lambda_1 \lambda_2=1$이다. $i$와 $-i$가 해당조건을 만족하므로 ${\bf A}$의 고유값은 $i$와 $-i$이다. 이때 고유값 $i$에 대응하는 고유벡터는 $c(1,-i)$이고 고유값 $-i$에 대응하는 고유벡터는 $c(1,i)$이다. 

- ${\bf A}$가 *orthogonal*-매트릭스이면 모든 고유값들의 절대값이 1이다. 즉 $\|\lambda\|=1$이다. 이것은 귀류법을 쓰면 쉽게 증명가능하다.


--- 
### Decomp - Singular Value Decomposition
- ㅇㅇ

