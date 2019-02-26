--- 
layout: post
title: 확률론 1 
--- 

### About this post
- 본 포스트는 작성중인 포스트이다. 

- 본 포스트는 대학원 교재인 듀렛책 4판을 바탕으로 작성하였다. 

- 본 포스팅에서는 확률론에 대한 기본적인 개념을 정리하고자 한다. 

### Measure Theory (1) 
- 여기서는 듀렛책 챕터 1.1~1.3 사이의 내용을 다룬다. 이 내용들은 Probability Spaces, Distributions, Random variable에 대한 내용인데 전반적으로 적분이전의 measure theory에 관한 내용이다. 개인적으로 책이 상당히 두서없이 정리되어 있다고 생각한다. 그래서 나도 두서없이 내맘대로 정리하였다. 

- 확률변수 $X$에 대한 정의를 생각하여 보자. 확률변수는 본질적으로 메저러블-맵핑이므로 메저러블-매핑의 정의에 대하여 알아보자. 어떠한 맵핑 $X$가 메저러블-스페이스 $(\Omega,{\cal F})$와 메저러블-스페이스 $(S,{\cal S})$를 이어주는 메저러블-맵핑이라는 의미는 1) $X$가 $\Omega$에서 $S$로 가는 함수이고 즉 $X:\Omega \rightarrow S$이고 2) $X^{-1}$가 
\begin{align}
\forall B \in {\cal S}: X^{-1}(B) \in {\cal F} 
\end{align} 
를 만족한다는 의미이다. 

- 확률변수 $X$라는 것을 정의하기 위해서는 반드시 두 메저러블-스페이스가 필요하다. 확률변수 $X$ 단독으로 정의될 수 없다. 이것은 비유하면 "남친"의 정의와 비슷하다. 남친은 혼자 될 수 있는 것이 아니다. 즉 남친은 단독으로 정의될 수 없고 "XXX의 남친"과 같은 식으로만 정의된다. 예를 들면 <br/><br/>
***"저는 남친이에요"***<br/><br/>
라고 말하는것은 올바른 정의가 아니며<br/><br/>
***"저는 XXX의 남친이에요"***<br/><br/>
라고 말하는 것이 올바른 정의이다. 이처럼<br/><br/> 
***"$X$는 확률변수에요"***<br/><br/>
라고 말하는 것은 올바른 정의가 아니며 (하지만 유감스럽게도 대부분 이렇게 말하고, 그래서 확률변수가 무엇인지 헷갈려한다. 그리고 내가 매년 이러고 있다..)<br/><br/> 
***"$X$는 두 메저러블-스페이스 $(\Omega,{\cal F})$와 $(S,{\cal S})$를 연결해주는 확률변수에요"***<br/><br/>
라고 말하는것이 올바른 정의라는 것이다. 요런 느낌의 정의를 확률론에서는 많이 가지고 있다. 가령 예를들면 시그마필드 ${\cal F}$는 홀로 정의될 수 없고 전체집합 $\Omega$가 존재해야지 정의된다. 그리고 임의의 메저러블셋 $A$은 시그마필드 $\cal F$가 있어야지 정의될 수 있다. 즉 아래와 같이 말한다.<br/><br/>
***"$\cal F$는 $\Omega$에 대한 시그마필드에요"***<br/><br/>
혹은<br/><br/>
***"집합 $A$는 시그마필드 $\cal F$에 대해서 메저러블해요"***<br/><br/>
와 같은 식으로 말이다. 

- 확률변수는 사실 메저러블-맵핑중에서 매우 특수한 경우이다. 왜냐하면 "이미지(=image)"에 해당하는 메저러블-스페이스 $(S,{\cal S})$가 $(\mathbb{R},{\cal R})$로 고정되어있기 때문이다. 여기에서 $\cal R$은 보렐클라스이다. 그러면 사실 확률변수 $X$를 정의하는데 $\Omega$, $\cal F$, $S$, $\cal S$를 일일히 정의할 필요는 없어진다. $(S,{\cal S})=(\mathbb{R},{\cal R})$은 이미 정해졌고 $\Omega$는 ${\cal F}$를 정의하면 사실 같이 정의된 셈이나 마찬가지다($\cal F$에서 가장 큰 원소가 $\Omega$일테니깐!). 종합하면 확률변수 $X$를 정의할때는 ${\cal F}$만 정의하면 된다. 따라서 <br/><br/> 
***"$X$는 두 메저러블-스페이스 $(\Omega,{\cal F})$와 $(S,{\cal S})$를 연결해주는 확률변수에요"***<br/><br/>
라고 말하는것이 정확하지만 <br/><br/>
***"$X$는 ${\cal F}$에서 정의된 확률변수에요"***<br/><br/>
라고 말해도 틀린말은 아니라는 것이다. 그리고 이렇게 말하는 것을 더 좋아하는 사람들이 많다(간단하니깐). 그리고 이것을 기호로는
\begin{align}
X \in {\cal F}
\end{align}
라고 쓴다. 

- 아마 나는 이 포스팅을 읽을때마다 보렐클라스가 무엇인지 다시 헷갈리기 시작할것이다(나 자신에 대한 끝없는 불신..). 그래서 보렐클라스에 대해서 다시 정의하고 넘어가겠다. 보렐클라스 $\cal R$이란 $\mathbb{R}$의 모든 오픈셋을 포함하는 시그마필드라는 것이다. 좀 더 엄밀하게 써보자. 집합 $O$를 $\mathbb{R}$에 속하는 임의의 오픈셋이라고 하자. 즉 
\begin{align}
O \subset \mathbb{R} ~~~ and ~~ O ~~ is ~~ open ~~ set
\end{align}
이라고 하자. 이러한 집합 $O$들을 모아놓은 클라스를 $\cal O$를 정의하자. 즉 
\begin{align}
{\cal O}=\\{O: O \subset \mathbb{R}, ~~~ O ~~ is ~~ open ~~ set \\}
\end{align}
이다. $\cal R$은 $\cal O$를 포함하는 가장 작은 시그마필드이다. 즉 1) ${\cal O} \subset {\cal R}$이고 2) "${\cal R}$ is $\sigma$-field." 이다. 이것을 기호로는 아래와 같이 쓴다. 
\begin{align}
{\cal R}=\sigma({\cal O})
\end{align}
그리고 ${\cal R}$을 $\cal O$에 의해서 제너레이트된 시그마필드라고도하며 $\cal O$가 $\cal R$을 생성했다고 말하기도 한다. 

- 보렐클라스는 우리가 상상할 수 있는 대부분의 "subset of $\mathbb{R}$"을 포함한다. 가령 예를들면 보렐클라스는 점집합, 인터벌, 레이와 같은 집합들을 포함하는데 이는 이러한 집합들이 $(a,b)$의 카운터블 유니온꼴로 표현될 수 있다는 것을 알면 쉽게 이해할 수 있다. 이러한 집합을 $\cal R$-메저러블한 집합이라고 표현한다. 간단히 줄여서 보렐셋이라고 표현하기도 한다. 하지만 "subset of $\mathbb{R}$"임에도 불구하고 가끔 가다가 보렐클라스의 원소가 아닌 이상한 집합이 있을 수 도 있다. 이런 집합을 보렐클라스의 원소가 아닌 집합 혹은 $\cal R$-메저러블하지 않은 집합 혹은 보렐셋이 아닌 집합이라고 한다. 대표적으로 칸토르집합이 있다. 

- 보렐셋 즉 $\cal R$-메저러블한 집합은 $\mathbb{R}$에서 길이를 잴 수 있는 집합이라고 이해해도 괜찮다. 가령 예를 들면 $[0,1]$의 길이는 1이고 $\emptyset$의 길이는 0이다. 또한 $\\{0\\}$와 같은 집합의 길이는 0, 유리수들의 집합의 길이는 0, 그리고 $[0,1]$사이에 포함된 무리수들의 집합을 길이로 재면 $1$과 같은식으로 정의할 수 있다. 따라서 위에서 언급한 집합들은 모두 잴 수 있는 집합이며, $\cal R$-메저러블한 집합이다. 

- 참고로 위와 같이 길이를 재는 함수를 **르벡메저**라고 한다. 르벡메저는 $\cal R$에 속한 임의의 집합에 대하여서도 이러식으로 **모순없이** 길이를 정의할 수 있다. 여기에서 모순없이 길이를 잴 수 있다는 말이 의미하는 것은 1) 공집합의 길이는 0이며 2) $\cal R$에 속하는 어떠한 집합의 길이도 양수이어야 하며 3) $\cal F$에 속하는 두 집합이 서로소라면(즉 $[0,1]$, $[3,4]$와 같은 집합) 두 집합의 합친집합의 길이는 각각의 길이의 합과 같아야 한다는 것이다(즉 $[0,1]\cup[3,4]$의 길이는 $[0,1]$의 길이와 $[3,4]$의 길이의 합과 같아야한다는것임). 어떠한 클라스 $\cal F$에서 이러한 위와 같은 조건을 만족하는 함수 $\mu$가 있다고 하면 이때 $\mu$는 $\cal F$의 모든 원소들의 크기(혹은 길이)를 **모순없이** 정의할 수 있다. 이러한 함수 $\mu :{\cal F} \rightarrow [0,\infty]$를 $\cal F$에서의 메저라고 한다. 참고로 **르벡메져** $\lambda$는 아래와 같이 정의되는 함수이다. 
\begin{align}
\lambda((a,b])=b-a
\end{align}
이러한 함수 $\lambda$는 보렐클래스 $\cal R$에 있는 모든집합에 대하여 **모순없이** 길이를 정의할 수 있다. 따라서 $\lambda$는 $\cal R$에 대한 메져이다. 

- 다시 $X$로 관심을 돌려보자. $X$는 기본적으로 $\Omega$와 $\mathbb{R}$을 연결하는 맵핑이다. 이것이 $(\Omega,{\cal F})$와 $(\mathbb{R},{\cal R})$을 연결하는 맵핑, 즉 메저러블 맵핑이 되려면 어떻게 되어야 할까? 해답은 매우 간단하다. **$\Omega$를 보고 근원사건을 해석하여 맵핑하지말고 $\cal F$를 보고 근원사건을 해석하여 맵핑시키면 된다.** 이게 무슨말인지 찬찬히 살펴보자. 예를들어 $\Omega=\\{1,2,3,4,5,6\\}$이라고 하자. 즉 주사위를 던져서 나오는 눈들의 집합이 $\Omega$이다. $\Omega$를 보고 이해한 근원사건은 다음과 같다. <br/><br/>
***"주사위를 던져서 눈이 1이 나올 경우, ... , 주사위를 던져서 눈이 6이 나올 경우"***<br/><br/>
이제 $\Omega$에 대한 시그마필드를 아래와 같이 정의하자. 
\begin{align}
{\cal F}=\\{\emptyset, \\{1,3,5\\}, \\{2,4,6\\},\Omega \\}.
\end{align}
즉 $\cal F$의 원소는 1) 공집합 2) 전체집합 그리고 3) 주사위를 던져서 짝수가 나오는 경우를 모은 집합 4) 주사위를 던져서 홀수가 나오는 경우를 모은 집합이다. 이 경우 $\cal F$의 관점에서 이해한 근원사건은 다음과 같다. <br/><br/>
***"주사위를 던져서 짝수가 나올 경우, 주사위를 던져서 홀수가 나올 경우"*** <br/><br/>
$X$가 단지 $\Omega$에서 $\mathbb{R}$의 맵핑이 아니라 $(\Omega,{\cal F})$에서 $(\mathbb{R},{\cal R})$로 메저러블맵핑이 되려면 **$\cal F$가 이해하는 사건의 구성으로 맵핑을 해야한다.** 즉 
\begin{align}
X(\\{1\\})=1, \dots, X(\\{6\\})=6
\end{align}
과 같이 맵핑을 하면 안되고 
\begin{align}
X(\\{1\\})=X(\\{3\\})=X(\\{5\\})=1 
\end{align}
\begin{align}
X(\\{2\\})=X(\\{4\\})=X(\\{6\\})=0
\end{align}
과 같은 식으로 맵핑을 해야한다는 것이다. 참고로 전자의 맵핑은 **"$X$: 주사위를 던져서 나오는 눈의 수"**와 같은 식으로 확률변수를 구성한 것이고 후자의 경우는 **"$X$: 주사위를 던져 홀수면 1 짝수면 0"**과 같은 방식으로 확률변수를 구성한 것이다. 전자의 근원사건은 주사위를 던져서 나온 눈의 수이며 후자의 근원사건은 주사위를 던져서 짝수가 나왔는지 홀수가 나왔는지다. 참고로 후자의 방식이 $\cal F$가 근원사건을 이해하는 방식이므로 후자의 처럼 $X$를 맵핑해야 $X$가 $\cal F$에서 정의된 랜덤변수 즉 $X \in {\cal F}$라고 할 수 있는 것이다. 

- $X \in {\cal F}$가 되도록 $X$를 정의하기 위해서는 위에서 처럼 ${\cal F}$가 근원사건을 이해하는 방식으로 맵핑 $X$를 정의해도 되지만 ${\cal F}$보다 작은 어떤 시그마필드 ${\cal F}^* $가 근원사건을 이해하는 방식으로 맵핑 $X$를 정의해도 된다. 예를들면 위의 예제처럼 
\begin{align}
{\cal F}=\\{\emptyset, \\{1,3,5\\}, \\{2,4,6\\},\Omega \\}.
\end{align}
라고 하고 우리는 $X \in {\cal F}$가 되도록 맵핑 $X$를 잘 정의하고 싶다고 하자. $X$를 위의 예제처럼 ${\cal F}$가 근원사건을 이해하는 방식으로
\begin{align}
X(\\{1\\})=X(\\{3\\})=X(\\{5\\})=1 
\end{align}
\begin{align}
X(\\{2\\})=X(\\{4\\})=X(\\{6\\})=0
\end{align}
와 같이 구성하면 당연히 $X \in {\cal F}$가 성립하지만 ${\cal F}$보다 작은 집합 ${\cal F}^* $, 예를들면 ${\cal F}^* = \\{\emptyset, \Omega\\}$와 같은 시그마필드가 근원사건을 이해하는 방식으로(여기서는 근원사건이 $\Omega$이다) 맵핑 $X$를 정의해도 된다. 예컨데 아래와 같은식으로 말이다.
\begin{align}
X(\\{1\\})=X(\\{2\\})=X(\\{3\\})=X(\\{4\\})=X(\\{5\\})=X(\\{6\\})=1.
\end{align}
이렇게 정의하여도 $X \in {\cal F}$가 성립한다. 단지 이러한 경우 ${\cal F}$는 $X$를 정의하기 위해서 필요한 최소한의(=가장작은) 시그마필드는 아니게 된다. 이 경우 $X$를 정의하는데 필요한 최소한의 시그마필드는 ${\cal F}^* $가 된다. 이처럼 맵핑 $X$를 ${\cal F}$ 메저러블하도록 만드는데 필요한 최소한의 시그마필드를 기호로 $\sigma(X)$라고 한다. 그리고 이 예제에서는 $\sigma(X)={\cal F}^* $가 된다. 

- 이제 $\cal F$에서 정의된 어떠한 확률변수 $X$가 $\cal F$에 포함된 모든 근원사건들을 **잘** 연결하는 어떠한 맵핑이라는건 알겠다. 그런데 확률변수 $X$가 어떤 **랜덤**한 출력을 주는 함수라는 느낌은 없다. 왜냐하면 말그대로 확률변수 $X$는 두 메저러블 스페이스 $(\Omega, {\cal F})$, $(\mathbb{R},{\cal R})$을 잘 연결하는 어떠한 맵핑일 뿐이기 때문이다. 즉 $X$는 단순히 함수(혹은 맵핑)이기 때문에 $\omega \in \Omega$가 고정되면 $X(\omega)$의 값도 고정된다. 따라서 $X$가 어떤 **랜덤**한 출력을 가지도록 하기 위해서는 $\omega$를 랜덤하게 선택하는 수밖에 없다. 이렇게 $\omega$를 랜덤하게 선택할 수 있게 만들어주는 장치가 바로 확률척도 $P:{\cal F} \rightarrow \mathbb{R}$이다. $P(\\{\omega\\})$는 $\Omega$에서 $\\{\omega\\}$가 선택될 확률을 의미한다. 따라서 $P$는 $\omega$를 **랜덤**하게 선택할수 있게 해주고 그 결과 $X(\omega)$의 출력역시 **랜덤**하게 나올 수 있도록 해준다. 따라서 우리가 일반적으로 생각하는 확률변수 $X$를 정의하기 위해서는 $(\Omega, {\cal F}), ~ (\mathbb{R},{\cal R})$과 더불어서 $P$가 추가적으로 필요하다. 즉 확률변수 $X$를 정의하기 위해서는 $(\Omega,{\cal F},P), ~ (\mathbb{R},{\cal R})$이 필요하다. 여기에서 $(\Omega, {\cal F}, P)$를 묶어서 확률공간이라고 한다. 

- 엄밀하게 말하면 $X$를 정의하기 위해서는 $(\Omega, {\cal F},P), ~ (\mathbb{R},{\cal R})$가 모두 필요하지만 앞에서 언급하였듯이 ${\cal F}$를 알면 $\Omega$를 아는 셈이고 (${\cal F}$에서 젤 큰 집합이 $\Omega$임) $(\mathbb{R},{\cal R})$는 이미 정해진 것이므로 $X$를 정의하는데 최소한으로 필요한 정보는 ${\cal F}$와 $P$이다. 그런데 이 사실은 $X \in {\cal F}$라는 기호를 이상하게 느껴지게 만들 수 있다. 즉 ''$X$를 **well-define** 하는데 ${\cal F}$만 필요하다고 하면 된다고 했는데 사실 그게 아니고 $P$도 필요한것 아니야?" 라고 생각할 수 있다. 하지만 $P$는 사실 $X$가 가지는 **랜덤**성을 주기 위한 장치이고 **따라서 $P$를 잘 못 정의한다고 하여서 $X$가 랜덤변수가 아니게 되는 경우는 없다**($P$가 probability measure가 되도록만 정의하면 됨)는 사실을 유의하면 $X$를 **well-define**하기 위해서는 $P$가 필요하지 않음을 알 수 있다. 즉 아래의 기호는 여전히 유용하다. 
\begin{align}
X \in {\cal F}
\end{align}

- 그럼 $P$가 가지는 역할은 무엇일까? $P$는 $X$는 가지는 분포를 결정하여 준다. 따라서 $P$는 맵핑 $X$가 확률변수인지 아닌지를 결정하지는 않지만 (이것은 ${\cal F}$가 결정함) $X$가 ***어떠한*** 확률변수인지는 결정한다. 즉 $P$가 정의되면 부수적으로 $X$가 가지는 여러가지 성질들을 추가적으로 **assume**할 수 있다. 예를들어 $P$는 확률변수의 모멘트가 유한한지 그렇지 않은지를 결정할 수 있으며 확률변수들이 독립인지 아닌지도 결정할 수 있다. (예컨데 $P:=P_1 \times P_2$를 확률벡터 $(X_1,X_2)$의 확률측도라고 하자. 여기에서 $P_1, P_2$는 각각 $X_1, X_2$의 probability measure이다. 이떄 $P$를 알고있다면 두 확률변수 $X_1$, $X_2$ 가 독립인지 독립이 아닌지도 알 수 있다.)

- 확률척도 $P$는 $X$의 분포에 대한 정보를 담고 있지만 $P$의 정의역은 ${\cal F}$이다. $P$의 정의역이 보렐셋 ${\cal R}$이 아니기 때문에 종종 $P$를 쓰기 불편할 때가 있다. 그래서 $P$와 동등한 역할을 하는 또 다른 함수 $\mu: {\cal R} \rightarrow [0,1]$를 아래와 같이 만든다. 
\begin{align}
\mu := P \circ X^{-1}. 
\end{align}
이때 $\mu$를 확률변수 $X$의 ***distribution***이라고 정의한다. 이렇게 정의하면 임의의 집합 $B \in {\cal R}$에 대하여 아래식이 성립한다. 
\begin{align}
\mu(B)=P(\\{\omega: X(\omega) \in B\\})
\end{align}
참고로 이때 $\mu$는 확률측도가 된다(증명은 알아서 하든가 아니면 그냥 믿든가). 따라서 $(\mathbb{R},{\cal R},\mu)$는 확률공간이 된다. 여기에서 $\mu$가 $X$에 의해서 정의되므로 확률공간 $(\mathbb{R},{\cal R},\mu)$ 역시 $X$에 의해서 정의되는데 이러한 이유로 **확률공간 $(\mathbb{R},{\cal R},\mu)$를 $X$에 의해서 유도된 확률공간이라고 표현하기도 한다.** 

- 확률변수 $X$에 대한 ***distribution*** $\mu$까지 잘 정의하였다면 확률변수 $X$에 대한 ***distribution function***을 정의할 수 있다. 확률변수 $X$의 ***distribution function*** $F:\mathbb{R} \rightarrow [0,1]$는 아래와 같이 정의한다. 
\begin{align}
F(x)=\mu((-\infty,x])=P(\\{\omega: X(\omega) \leq x\\})
\end{align}
$F(x)$는 $X$의 ***cdf*** 라고 표현하기도 한다. 참고로 $F(x)$는 (1) $F(-\infty)=0, F(\infty)=1$을 만족하고 (2) 비감소이며 (3) 오른쪽 연속인 함수가 된다. 그리고 임의의 함수 $F(x)$가 위의 3가지 조건을 만족하면 $F(x)$는 어떠한 확률변수 $X$의 ***distribution function***이 된다.

- 여기에서 어떠한 확률변수 $X$인지 구체적으로 알아보도록 하자. 결론적으로 $X(\omega):= \sup \\{ y : F(y)<\omega \\}$와 같이 하면 이 확률변수는 $F(x)$를 **distribution function**으로 가지는 하나의 확률변수가 된다. 

- 만약에 $F(x)$가 $x$에 대하여 미분가능하다면 
\begin{align}
f(x):=\frac{\partial}{\partial x}F(x) 
\end{align}
를 정의할수 있는데 이때 $f(x)$를 $X$의 ***pdf*** 라고 한다. 참고로 $\mu$가 $F$에 대응하듯이 (recall $F(x)=\mu((-\infty,x])$) $f$에 대응하는 어떠한 메져 $\nu$를 생각할 수 있다. 즉 임의의 $B \in {\cal B}$에 대하여 아래와 같은 성질을 만족하는 $\nu$를 생각할 수 있다.
\begin{align}
\mu(B)=\int_B \nu d\lambda 
\end{align}
여기에서 $\lambda$는 르벡메져이다. 참고로 $\mu \ll \lambda$이기만 하면 위의 식을 만족하는 메져 $\nu$가 반드시 존재함이 ***라돈-니코딤*** 정리에 의하여 알려져 있다. 여기에서 $\mu \ll \lambda$는 메져 $\mu$가 메져 $\lambda$에 대하여 ***absolutely continuous*** 하다는 의미이다(제발 매우작다라고 해석하지 말자). 참고로 원래 ***라돈-니코딤***정리를 쓰려면 $\mu$, $\lambda$가 $\sigma$-finite 메져라는 조건이 추가적으로 필요한데 이 경우에는 $\mu$는 확률측도이고 $\lambda$는 르벡측도이므로 이 조건이 그냥 만족된다. 

--- 
### Measure Theory (2) : Integration 
- 여기에서는 듀렛책 챕터 1.4~1.7의 내용을 다룬다. 이곳에서는 메저러블 맵핑 $f$의 적분을 다룬다. 

- $f:\Omega \rightarrow \mathbb{R}$가 두 가측공간 $(\Omega,{\cal F})$와 $(\mathbb{R},{\cal R})$를 이어주는 매저러블-맵핑이라고 하자. 그리고 $\mu:{\cal F} \rightarrow \mathbb{R}$는 ${\cal F}$에서의 메저라고 하자. 여기에서 특별히 $\mu$는 **$\sigma$-finite measure** 라고 정의한다(사실 우리가 관심 있는것은 $f=X$이며 $\mu=P$인 경우이지만 일단 일반적은 측도론에서 이야기 하도록 하자). 이 챕터에서 우리의 관심은 (1) $f$를 $\mu$로 적분한것 즉 
\begin{align}
\int f d \mu
\end{align}
를 ***잘*** 정의하고 (2) 적분관련 성질들을 자유자재로 계산할 수 있는 ***적당한 조건***을 알아보는 것이다. 여기에서 적분관련 성질들은 예를들어 
\begin{align}
\int af d\mu = a \int f d \mu 
\end{align} 
\begin{align}
\int f+g d\mu = \int f d \mu + \int g d \mu 
\end{align} 
와 같은 것들을 의미한다. 

- 여기서 잠깐 정리해둘 노테이션이 있는데 
\begin{align}
\int f d \mu
\end{align}
와 
\begin{align}
\int f(x) \mu(dx)
\end{align}
는 같은 기호이다. (Chung 책 p.42를 참고하면 알 수 있음) 

- 다시 본론으로 돌아오자. $\int f d \mu$를 정의하기 위해 필요한 기본가정을 살펴보자. 당연히 $\int f d \mu$를 계산하기 위해서는 보는것처럼 매저러블 맵핑 $f$가 정의되어야 하며, 메져 $\mu$가 정의되어야 한다. 그리고 $f$와 $\mu$를 정의하기 위한 시그마필드 $\cal F$가 정의되어야 한다. 참고로 메저러블 맵핑 $f$를 정의하기 위해서는 기본적으로 $(\Omega,{\cal F}),~ (\mathbb{R},{\cal R})$이 모두 필요하지만 편의상 ${\cal F}$만 필요하다고 생각해도 무방하다는 것을 앞에서 설명하였다. 그리고 주목할만한 점이 하나 있는데 $f$와 $\mu$는 같은 시그마필드 ${\cal F}$에서 정의되고 있다는 것이다. 이것은 우리가 지금 정의하고 싶은 적분이 고등학교때 배운 적분처럼 실수축위에서 이루어지고 있는 것이 아니라 $(\Omega,{\cal F})$에서 이루어 지고 있다는 것을 생각하면 쉽게 이해할 수 있다. 그리고 또 하나 필요한 가정은 $\mu$가 **$\sigma$-finite measure** 라는 것이다. 이걸 이용하면 임의의 $A \in {\cal F}$에 대하여서도 $\mu(A)<\infty$가 성립하게 되어서 $d \mu$부분을 상당히 안정적으로 정의할 수 있다. 요약하면 
\begin{align}
\int f d \mu
\end{align}
를 정의하기 위해서는 1) $f$가 ${\cal F}$에 대한 메저러블펑션이며 2) $\mu$가 ${\cal F}$에 대한 **$\sigma$-finite measure**이어야 한다(그리고 $f$와 $\mu$는 같은 시그마필드 ${\cal F}$를 공유해야함). 

- 왜 적분을 **measure theory** 를 이용하여 정의할까? 고등학교때 정의하던대로 하면 안되나? 다 이유가 있어서 이렇게 정의하는 것이다. **measure theory** 를 이용하여 적분을 정의하면 고등학교때 배운 논리로 정의하기 애매하 적분들을 매우 깔끔하게 정의할 수 있다는 장점이 있다. 가령 예를들면 모든 유리수에서 $1$의 값을 가지고 나머지는 $0$을 가지는 함수 $f$를 생각하여 보자. 즉 $f$는 아래와 같다. 
\begin{align}
f(x)=\begin{cases} 1 & x \in \mathbb{Q} \\\\ 0 & x \notin \mathbb{Q} \end{cases}
\end{align}
이 함수 $f$에 대한 적분은 고등학교때 배운 **구분구적법** 혹은 **리만적분** 과 같은 방식으로는 정의할 수 없다(얼핏 생각하면 **리만적분**으로는 가능할것 같은데 불가능하다고 한다 $f$를 리만적분하면 0과 1사이의 임의의 값이 랜덤으로 정의된다고 한다). 하지만 **measure theory**를 이용하면 이 적분값은 0으로 깔끔하게 정의된다. 즉 
\begin{align}
\int f d\lambda=0
\end{align}
으로 깔끔하게 정의된다. 여기에서 $\lambda$는 르벡메져이며 이러한 적분을 **르벡적분**이라고 한다. 기본적으로 **구분구적법** 이나 **리만적분** 은 $f$가 연속이거나 부분적으로 연속이어야 할 것 같은 느낌인데 **measure theory**를 이용한 **르벡적분** 은 $f$가 매저러블 맵핑이기만 하면 되므로 좀 더 적분을 정의할 수 있는 함수의 선택폭이 넓다. 일단 ${\cal R}$자체가 거의 대부분의 ''subset of $\mathbb{R}$''을 커버하고 있기 때문에 ${\cal R}$-메저러블하지 않는 함수 $f:\mathbb{R} \rightarrow \mathbb{R}$는 거의 없다고 보는 편이 좋다. 즉 **르벡적분** 불가능한 함수 $f:\mathbb{R} \rightarrow \mathbb{R}$는 거의 없다고 보는것이 맞다(뭐 칸토르집합에서만 1의 값을 가지고 그렇지 않은 경우에서는 0의 값을 가지는 이상한 함수 $f$만 아니라며 말이다).

- 이제 적분을 **모순없이** 정의하는 방법을 살펴보자. 적분은 기본적으로 넓이를 구하는 개념이므로 $f:\Omega \rightarrow \mathbb{R}$가 **simple function** 일때  $\mu:{\cal F} \rightarrow \mathbb{R}$에 대한 적분은 사각형넓이의 유한합으로 매우 명확히 정의할 수 있다. 여기까지는 당연한거라서 우리의 관심은 <br/><br/>
''$f$가 simple function이 아닐 경우에도 $\mu$에 대한 적분을 모순없이 잘 정의할 수 있을까?''
<br/><br/>
가 된다. 결론적으로 (1) $f$가 **bounded function** 인 경우 (2) $f$가 **non-negative function**인 경우 (3) $\int |f| d\mu < \infty$인 경우에서는 적분값 
\begin{align}
\int f d \mu 
\end{align}
가 (마치 $f$가 **simple function**인것마냥) **모순없이** 잘 정의되며 $\int af d\mu = a \int f d \mu$, $\int f+g d\mu = \int f d \mu + \int g d \mu$ 따위의 성질들도 **모순없이** 잘 성립한다. 

- 먼저 (1) $f$가 **bounded function** 인 경우를 살펴보자. $f$를 두 **simple function** $\phi$, $\psi$ 사이에 끼워넣고, 즉 $\phi \leq f \leq \psi$ 와 같이 만든 다음 $\int f d\mu $를 아래와 같이 정의하면 $f$가 **simple function** 일때마냥 $\mu$에 대한 적분값을 잘 정의할 수 있다. 
\begin{align}
\int f d\mu = \sup_{\phi \leq f} \int \phi d\mu = \inf_{\psi \geq f} \int \psi d\mu. 
\end{align}
참고로 위의 정의가 말이 되려면 즉 **모순이 되지 않으려면** $\sup_{\phi \leq f} \int \phi d\mu = \inf_{\psi \geq f} \int \psi d\mu$가 성립해야 하는데 이것이 성립하는 것은 듀렛책에 증명이 되어있다. 

- 위의 결과를 이용하면 (2) $f$가 **non-negative function**인 경우에도 $\mu$에 대한 적분을 쉽게 정의할 수 있다. 먼저 $h$를 $0\leq h \leq f$를 만족하는 **bounded function**이라고 하자. $\int f d\mu$는 아래와 같이 $\int h d \mu$의 sup으로 정의할 수 있다. 
\begin{align}
\int f d\mu = \sup_{0\leq h \leq f} \int h d \mu
\end{align}

- 이제 (3)의 경우를 살펴보자. 일반적인 $f$는 아래와 같이 표현가능하다. 
\begin{align}
f=f^+ -f^-
\end{align}
따라서 $\int f d\mu$는 아래와 같이 정의할 수 있다. 
\begin{align}
\int f d\mu = \int f^+ d\mu - \int f^- d\mu
\end{align}
단지 위의 식이 **모순없이** 정의되려면 $\int f^+ d\mu$와 $\int f^- d\mu$이 모두 무한대이면 안되는데 이런 경우는 $\int |f| d\mu < \infty$라는 조건에 의해서 방지된다. 참고로 $\int |f| d\mu < \infty$를 만족하는 $f$를 우리는 **integrable하다**고 한다. 

- $(\Omega, {\cal F},\mu)=(\mathbb{R}, {\cal R}, \mu)$이고 적분을 하는 메져 $\mu$가 $\mu((a,b])=F(b)-F(a)$와 같은 꼴로 표현가능하다면 우리는 $\int f d\lambda$를 아래와 같이 쓸 수 있다. 
\begin{align}
\int f d\mu = \int f(x) dF(x)
\end{align}
예를들어 $(\Omega, {\cal F},\mu)=(\mathbb{R}, {\cal R}, \lambda)$와 같은 상황을 생각해보자. 여기에서는 적분을 수행하는 메져가 르벡메져이고 르벡메져 $\lambda$는 $\lambda((a,b])=b-a$꼴로 쓸 수 있으므로 
\begin{align}
\int f d\lambda = \int f(x) dx
\end{align}
와 같이 나타낼 수 있다. 

- $\Omega$가 countable set이고 ${\cal F}$는 ''all subset of $\Omega$'' 라고 하자. $\mu$는 counting measure라고 하자. 이때는 $\int f d\mu$는 아래와 같이 나타낼 수 있다. 
\begin{align}
\int f d \mu = \sum_{i \in \Omega} f(i).
\end{align}

- 이제 극한이 적분안으로 들어오는 조건 즉 아래의 식이 만족하는 조건을 찾는 것에 관심을 가져보자. 
\begin{align}
\lim_{n \rightarrow \infty} \int f_n d\mu = \int \left( \lim_{n \rightarrow \infty} f_n \right) d\mu
\end{align}
결론적으로 말해서 (1) $f_n$이 모두 bounded function이거나 (2) $f_n$이 모두 non-negative function이거나 (3) $f_n$이 모두 integrable하면 된다. 신기하게도 모든 $n$에 대하여 $\int f_n d \mu$를 **모순없이** 정의할 수 있기만 하면 되는 느낌이다. 심지어 (3)의 조건은 (1)의 조건을 포함하므로 결론적으로 극한이 적분안으로 들어오기 위해서는 1) $f_n$이 모두 non-negative function이거나 2) $f_n$이 모두 integrable 하면 된다는 것을 알 수 있다.

- 위의 과정에서 (1)의 경우를 정리한 것이 BCT이며 (2)의 경우을 정리한것이 MCT이고 (3)의 경우를 정리한것이 DCT이다. 
증명은 당연히 BCT $\rightarrow$ MCT $\rightarrow$ DCT 순서로 하며 MCT는 BCT로부터 바로 증명할 수 없어서 Fatou lemma를 추가적으로 증명한다. 참고로 파토우 레마는 아래와 같다. 
\begin{align}
\liminf_{n \rightarrow \infty} \int f_n d\mu \leq \int \left(\liminf_{n\rightarrow \infty} f_n \right) d\mu 
\end{align}
여기에서 $f_n \geq 0$이다. 

- 이제 
\begin{align}
\int \left( \lim_{n \rightarrow \infty} f_n \right) d\mu = \int f d \mu 
\end{align}
라고 쓸 수 있는 조건을 알아보자. 당연히 모든 $x$에 대하여 $\lim_{n \rightarrow \infty} f_n(x)= f(x)$ 이면 되겠지만(**pointwise convergence**라고 함) 현실적으로 이런 조건은 너무 강해서 좀더 약한 조건이면 좋겠다. 일반적으로 $f_n \rightarrow f$ **a.s**이면 무리가 없이
\begin{align}
\int \left( \lim_{n \rightarrow \infty} f_n \right) d\mu = \int f d \mu 
\end{align}
임을 주장할 수 있다. 사실 $f_n \rightarrow f$ **in measure $\mu$** 이어도 되는 것으로 알고 있다. 왜냐하면  $f_n \rightarrow f$ **in measure $\mu$** 의 의미는 임의의 $\epsilon>0$에 대하여 $\mu(\\{x: \\| f(x)-f_n(x) \\|> \epsilon \\}) \rightarrow 0$이라는 의미인데 


그래서 그냥 $f_n \rightarrow f$ **a.s**라고 기억하는 것이 정신건강에 좋다. 

- $X_n$이  $h$가 적당한 조건을 만족하는 연속함수일경우 $Eh(X_n) \rightarrow Eh(X)$가 됨을 보였다. 

- 듀렛책 P.27. Thm 1.6.9에서 $Ef(X)=\int_{\Omega} f(y)\mu(dy)$임을 보였다. 이게 무슨기호인지도 몰겠음. 

- 두개의 메저러블 맵핑 $X_1$과 $X_2$를 각각 $(\Omega_1,{\cal F}_ 1, P_1)$와 $(\Omega_2,{\cal F}_ 2, P_2)$에서 정의하자. 확률벡터 $(X_1,X_2)$를 정의하기 위한 공간을 construct하자. 먼저 
\begin{align}
\Omega=\Omega_1 \times \Omega_2= \\{(x_1,x_2):x_1 \in \Omega_1, x_2 \in \Omega_2\\}
\end{align}
와 같이 설정하자. 그리고 ${\cal S}$를 아래와 같이 정의하자. 
\begin{align}
{\cal S}=\\{A\times B: A \in {\cal F}_ 1, B \in {\cal F}_ 2\\}
\end{align}
이때 ${\cal S}$는 semi-algebra가 된다고 한다. ${\cal F}$를 아래와 같이 정의한다. 
\begin{align}
{\cal F}=\sigma({\cal S})
\end{align}
이제 공간 $(\Omega,{\cal F})$는 확률벡터 $(X_1,X_2)$가 정의 될 수 있는 공간이 되었다. 즉 확률벡터 $(X_1,X_2)$는 $(\Omega,{\cal F})$에서의 메저러블-맵핑이 된다. 이제 확률벡터 $(X_1,X_2)$의 분포를 결정할 수 있는 메져 $P$만 정의하면 된다. 일반적인 길이의 개념을 넓이로 확장시키면 메져 $P$가 아래의 성질을 만족하는 것이 합리적이라고 생각된다. 
\begin{align}
P(A \times B)=P_1(A) \times P_2(B)
\end{align}
듀렛책의 thm 1.7.1에 의하면 이러한 메져 $P$가 유니크하게 존재한다고 한다. 

- LGE에서 

***useful inequalities***
- 여기에서는 적분 혹은 평균과 관련된 유용한 부등식들을 정리하였다. 
- Jensen's inequality: 젠센스-인이퀄리티는 임의의 convex 함수 $\phi$에 대하여 아래가 성립한다는 것인데 
\begin{align}
\phi \left( \int f d\mu \right) \leq \int \phi (f) d \mu
\end{align}
이것을 적용한 대표적인 예제는 확률변수 $X$에 대하여 $E^2(X) \leq E(X^2)$이 성립하는 것이다. 

- Holder's inequality: 횔더스-인이퀼리티를 정의하기 위해서는 $$\\| f \\|_p$를 정의해야 한다.  

- Minkowski's inequality: 민코우스키-인이퀄리티는 

- Chebyshev's inequality: 쳬비쉐프-인이퀄리티는 

- Markov's inequality: 마코브-인이퀄리티는 

--- 
### Independence 

--- 
### Weak Laws of Large Numbers

--- 
### Strong Law of Large Numbers

--- 
### Convergence of Random Series

