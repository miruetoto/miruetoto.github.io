---
layout: post
title: (논문) 태양광
---

### About this doc

- 태양광 자료 분석에 대한 draft 

- 논문 
  
### Method 
- 아래와 같은 자료를 고려하자. 
\begin{align}
Z_i=W_i y_i + (1-W_i){\tilde y}_ i, \quad i=1,\dots,n 
\end{align}
아래를 가정하자. <br/><br/>
**(1)** 모든 관측치는 서로 독립이다. <br/>
**(2)** $W_i$ 는 확률이 $p_i$인 베르누이 분포에서 생성되었다. 여기에서 $p_i=\frac{\exp(\gamma+{\bf x_i}{\boldsymbol\beta})}{\exp(\gamma+{\bf x_i}{\boldsymbol\beta})+1}$. <br/>
**(3)** ${\bf y}={\bf X}{\boldsymbol \beta} +{\boldsymbol \epsilon}$ 이다. <br/>
**(4)** ${\bf \tilde y}=0$ 이다. 

- 관측한 자료는 $\bf z$이고, 완전한 자료는 $\bf (w,z)$이다. 그리고 ${\boldsymbol\theta}=(\gamma,\boldsymbol{\beta})$이다. 완전한 자료를 모두 관측하였다고 가정하였을 경우 우도함수는 아래와 같이 표현가능하다. 
\begin{align}
L({\boldsymbol\theta})=\prod_{i=1}^{n} f(z_i|w_i)f(w_i)  
\end{align}
여기에서 $f(w_i)$와 $f(z_i|w_i)$는 각각 아래와 같이 표현된다. 
\begin{align}
f(w_i)=\Bigg[\frac{\exp(\gamma+{\bf x}_ i {\boldsymbol\beta})}{\exp(\gamma+{\bf x}_ i{\boldsymbol\beta})+1}\Bigg]^{w_i}\Bigg[1-\frac{\exp(\gamma+{\bf x}_ i{\boldsymbol\beta})}{\exp(\gamma+{\bf x}_ i{\boldsymbol\beta})+1}\Bigg]^{1-w_i}
\end{align}
\begin{align}
f(z_i|w_i)=
\Bigg[ \frac{1}{\sigma\sqrt{2\pi}}\exp\big(-(z_i-{\bf x}_ i {\boldsymbol\beta})^2 \big) \Bigg]^{w_i} \Bigg[\delta(z_i)  \Bigg]^{1-w_i}
\end{align}
그리고 이때 $E(W_i \| z_i)=I(z_i>0)$와 같이 구할 수 있다. 이제부터 아래와 같이 놓고 생각없이 쭉쭉 풀면(=미분하면) 된다. 
\begin{align}
E\big[\log L({\boldsymbol\theta}) \| {\bf z} \big]
=\sum_{i=1}^{n}\Bigg(E\big[\log f(z_i|w_i) \| z_i \big]+ E\big[\log f(w_i) \| z_i \big]\Bigg)
\end{align}

- $\gamma$로 미분해보자. 
\begin{align}
\frac{\partial}{\partial\gamma}E\big[\log f(z_i|w_i) \| z_i \big]=0 
\end{align}
\begin{align}
\frac{\partial}{\partial\gamma}E\big[\log f(w_i) \| z_i \big] 
=I(z_i>0)\frac{1}{e^{\gamma+{\bf x}_ i {\boldsymbol\beta}}+1}+ I(z_i=0)\frac{-e^{\gamma+{\bf x}_ i {\boldsymbol \beta}}}{e^{\gamma+{\bf x}_ i {\boldsymbol\beta}}+1}
\end{align}
따라서
\begin{align}
\frac{\partial}{\partial\gamma}E\big[\log L({\boldsymbol\theta}) \| {\bf z} \big]=0 
\end{align}
을 만족하는 방정식을 풀면 
\begin{align}
m = \sum_{i=1}^{n} p_i = \bf 1'p 
\end{align}
가 된다. 여기에서 $m=\sum_{i=1}^{n} I(z_i>0)$ 이고 ${\bf p}=(p_1,\dots,p_n)'$ 이다. 

- $\boldsymbol\beta$로 미분해보자. (*벡터미분이 생소하다고 $\beta_j$로 미분할생각하면 진짜 엄청난 계산이 기다린다. 개고생만 하다가 결국에는 반드시 공책을 찢게 될 것이다. 방금 공책 찢고와서 너무 한이 맺혀서 쓰는 글이다. 벡터나 행렬에서 **엘리먼트-와이즈 연산** 은 남들이 해놓은거 이해하기는 쉽지만 본인이 하려면 엄청 힘들고 특히 머리가 겁나 좋아야 한다는걸 깨달았다. 이인석 교수님 급으로 머리 돌아가는거 아니면 그냥 포기하는게 낫다. 잘 생각해보면 애초에 **엘리먼트-와이즈** 연산을 잘한다는 것은 벡터미분의 다양한 공식(?)들을 다 바로바로 유도하면서 쓴다는 소리이니 이것이 쉬울리가 없다. 다시는 이렇게 풀 생각하지 말자. 머리 나쁘면 그냥 미리 정리해둔 공식 떠올리면서 벡터미분하는게 정신건강에 좋다.*)
\begin{align}
\frac{\partial}{\partial\boldsymbol\beta}E\big[\log f(z_i|w_i) \| z_i \big]=I(z_i>0)\frac{(z_i-{\bf x}_ i \boldsymbol\beta){\bf x}_ i'}{\sigma^2} = I(z_i>0) {\bf x}_ i' z_i - {\bf x}_ i' {\bf x}_ i \boldsymbol\beta
\end{align}
여기에서 
\begin{align}
\sum_{i=1}^{n} {\bf x}_ i' {\bf x}_ i = {\bf X}'{\bf X}, \quad \sum_{i=1}^{n} {\bf x}_ i' z_ i = {\bf X}'{\bf z}
\end{align}
임을 이용하면 아래와 같이 정리할 수 있다. 
\begin{align}
\sum_{i=1}^{n}\left( \frac{\partial}{\partial\boldsymbol\beta}E\big[\log f(z_i|w_i) \| z_i \big]\right)
=\bf \tilde X' z -\tilde X'\tilde X {\boldsymbol\beta} 
\end{align}
여기에서 ${\bf \tilde X}$는 $z_i$의 값이 $0$인 인덱스를 제외한 값들로만 구성한 디자인매트릭스 이다. 
한편 
\begin{align}
\frac{\partial}{\partial\boldsymbol \beta}E\big[\log f(w_i) \| z_i \big] 
=I(z_i>0)\frac{\bf x_i}{e^{\gamma+{\bf x}_ i {\boldsymbol\beta}}+1}+ I(z_i=0)\frac{-e^{\gamma+{\bf x}_ i {\boldsymbol \beta}}{\bf x_i}}{e^{\gamma+{\bf x}_ i {\boldsymbol\beta}}+1}
\end{align}
이다. 따라서 
\begin{align}
\sum_{i=1}^{n} \left( \frac{\partial}{\partial\boldsymbol \beta}E\big[\log f(w_i) \| z_i \big]  \right) = - \bf X'p + \tilde X' 1 
\end{align}
가 된다. 둘을 종합해서 $\frac{\partial}{\partial\boldsymbol\beta}E\big[\log L({\boldsymbol\theta}) \| {\bf z} \big]=0$를 계산하면
\begin{align}
\bf \tilde X' z -\tilde X'\tilde X {\boldsymbol\beta}  - \bf X'p + \tilde X' 1 = 0
\end{align}
와 같이 된다. 


- 결국 EM 알고리즘은 아래와 같이 된다.
1. $m$과 $\bf \tilde X$를 구한다. <br/> 
2. $\bf p$와 $\boldsymbol\beta$를 각각의 ${\bf p}^{(0)}$와 $\boldsymbol\beta^{(0)}$로 초기화 한다. <br/>
3. ${\boldsymbol \beta}^{(n)} \leftarrow \big({\bf\tilde X'\tilde X }\big)^{-1}{\bf \tilde X' z} +\big({\bf\tilde X'\tilde X }\big)^{-1}\big({\bf \tilde X' 1 - X'p^{(n-1)}   \big)}$<br/>
4. ${\bf p}^{(n)} \leftarrow \frac{e^{\bf X \boldsymbol\beta^{(n-1)}   } }{1+e^{\bf X \boldsymbol\beta^{(n-1)}   } }$ <br/>
5. ${\bf p}^{(n)} \leftarrow {\bf p}^{(n)} \frac{m}{ {\bf 1}'{\bf p}^{(n)}  }$ <br/>
6. 수렴할때까지 3-5 를 반복한다. 
