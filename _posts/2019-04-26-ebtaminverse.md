---
layout: post 
title: (논문) 고무줄변환, inverse AM
--- 

### inverse AM
- 아래와 같은 주기신호가 있다고 하자. 
\begin{align}
{\bf p}=\\{\dots,1,2,3,4,5,1,2,3,4,5,\dots\\}
\end{align}
그리고 또 다른 신호 ${\bf q}$가 있다고 하자. 두 신호의 곱은 아래와 같이 표현된다. 
\begin{align}
{\bf x}={\bf pq}=\\{\dots,1 q_1,2q_2,3q_3,4q_4,5q_5,1q_6,2q_7,3q_8,4q_9,5q_{10},\dots\\}
\end{align}
$\tau=5$일 경우에 ${\bf x}$의 고무줄 변환을 생각하여 보자. 각 고무줄들은 아래와 같이 표현된다. 
\begin{align}
{\bf x}^{1,5}=p_1 \times {\bf q}^{1,5}, \dots, {\bf x}^{5,5}=p_5 \times {\bf q}^{5,5}.
\end{align}
이제 $p_1,\dots,p_5$를 추정하기 위해서 아래의 식을 풀것을 제안하자. 
\begin{align}
\underset{\\{p_1,\dots,p_{\xi}\\}}{\operatorname{argmin}} \sum_{i=1}^{\xi} \frac{1}{\xi-1} \sum_{\ell=1}^{\xi}\left( \frac{x_i^{\ell,\xi}}{p_{\ell}}-\frac{1}{\xi} \sum_{\ell=1}^{\xi}\frac{x_{i}^{\ell,\xi}}{p_{\ell}} \right)^2 
~~ s.t. ~~ \sum_{\ell=1}^{\xi}p_{\ell}^2=1
\end{align}
