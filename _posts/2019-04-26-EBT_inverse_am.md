---
layout: post 
title: (논문) 고무줄변환, inverse AM
--- 

### inverse AM
- 아래와 같은 주기신호가 있다고 하자. 
\begin{align}
{\bf p}=\\{\dots,2,3,2,3,2,3,\dots\\}
\end{align}
그리고 또 다른 신호 ${\bf q}$가 있다고 하자. 두 신호의 곱은 아래와 같이 표현된다. 
\begin{align}
{\bf x}={\bf pq}=\\{\dots,2 q_1,3q_2,2q_3,3q_4,2q_5,3q_6,\dots\\}
\end{align}
$\tau=2$일 경우에 ${\bf x}$의 고무줄 변환을 생각하여 보자. 각 고무줄들은 아래와 같이 표현된다. 
\begin{align}
{\bf x}^{1,2}=p_1 \times {\bf q}^{1,2}, {\bf x}^{2,2}=p_2 \times {\bf q}^{2,2}.
\end{align}
이제 $p_1,p_2$를 추정하기 위해서 아래의 식을 풀것을 제안하자. 
\begin{align}
\underset{\\{p_1,\dots,p_{\xi}\\}}{\operatorname{argmin}} \sum_{i=1}^{\xi} \frac{1}{\xi-1} \sum_{\ell=1}^{\xi}\left( \frac{x_i^{\ell,\xi}}{p_{\ell}}-\frac{1}{\xi} \sum_{\ell=1}^{\xi}\frac{x_{i}^{\ell,\xi}}{p_{\ell}} \right)^2 
~~ s.t. ~~ \sum_{\ell=1}^{\xi}p_{\ell}^2=1
\end{align}
우리의 경우에는 $p_1=2$, $p_2=3$ 이므로 아래와 같이 쓸 수 있다. 

