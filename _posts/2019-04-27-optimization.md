--- 
layout: post 
title: (정리) 최적화 
---

### About this doc

- 이 포스트는 최적화 이론에 대한 내용을 정리한 것이다. 아래의 교재를 정리하였다. 이 교재는 약 25400번 정도 레퍼된 엄청난 교재이다. <br/>
Nocedal, J., \& Wright, S. (2006). Numerical optimization. Springer Science & Business Media.

### Ch 12. Theory of Constrained Optimization

- 이 챕터에서는 아래와 같은 형태의 함수에 대한 최적화 문제를 다룬다.
\begin{align}
\underset{ {\bf x} \in \mathbb{R}^p }{ \operatorname{min} } f({\bf x}) \quad \mbox{ subject to } \quad
\begin{cases} {\bf c}_ i({\bf x})=0,~ i \in {\cal E} \\\\ 
{\bf c}_ i({\bf x})\geq 0, ~i \in {\cal I} 
\end{cases}
\end{align}

- 일반적으로 $f$와 $c_i$는 ${\bf x}$의 모든 원소들에 대하여 편미분가능하다고 가정한다. 이것을 단순히 줄여서 $f$와 $c_i$는 ${\bf x}$에 대하여 미분가능하다고 하자. 여기에서 몇몇 사람들은 $c_i({\bf x})$가 ${\bf x}$로 미분가능해야 한다는것이 너무 강한 조건이라고 생각할 수 있다. 예를들어 
\begin{align}
c({\bf x})=\| {\bf x} \|_ 1 \leq 1
\end{align}
와 같은 다이아몬드 형태의 제약조건은 미분가능하지 않기 때문에 우리가 풀수 없는 문제라 생각할 수 있다. 하지만  제약은 미분가능한 제약조건들의 합으로 표현될 수 있다. 이 뿐만 아니라 많은 경우에서 미분불가능해보이는 많은 제약조건들이 미분가능한 제약조건들의 합으로 표현가능하다. 따라서 $c_i({\bf x})$가 ${\bf x}$로 미분가능해야 한다는 제약이 그렇게 강한 조건은 아니다. 

- 아래와 같이 하나의 **등호** 로 이루어진 제약조건을 가지는 경우를 상상하여 보자. 
\begin{align}
\underset{ {\bf x} \in \mathbb{R}^p }{ \operatorname{min} } f({\bf x}) \quad \mbox{ subject to } \quad c({\bf x})=0
\end{align}
제약조건 $c({\bf x})$위에서 점들이 움직이려면 임의의 점 ${\bf x}$에 대하여 $c({\bf x})={\bf 0} \mbox{ and } c({\bf x}+{\bf d})={\bf 0}$를 만족하는 ${\bf d}$를 찾아야 한다. 테일러 정리에 의하여 아래식이 성립한다. 
\begin{align}
{\bf 0}=c({\bf x}+{\bf d}) \approx c({\bf x})+ \left(\frac{d}{d{\bf x}} c({\bf x})\right)^T {\bf d}
\end{align}
그런데 $c({\bf x})={\bf 0} \mbox{ and } c({\bf x}+{\bf d})={\bf 0}$ 이 만족해야 하므로, $\left(\frac{d}{d{\bf x}} c({\bf x}) \right)^T {\bf d}={\bf 0}$ 이어야 한다. 즉 ${\bf d}$는 $c({\bf x})$의 그래디언트와 수직인 방향으로 움직이면 된다는 것을 알 수 있다. 한편 ${\bf d}$는 아래를 만족하도록 선택되어야 한다. 
\begin{align}
f({\bf x} )> f({\bf x}+{\bf d})
\end{align}
여기에서 $f({\bf x}+{\bf d}) \approx f({\bf x})+ \left(\frac{d}{d{\bf x}} f({\bf x})\right)^T {\bf d}$ 이므로 결국아래 2식이 동시에 만족될때까지 ${\bf d}$를 찾는다. 
\begin{align}
\begin{cases}
\left(\frac{d}{d{\bf x}} f({\bf x})\right)^T {\bf d} < {\bf 0} \\\\ \\\\
\left(\frac{d}{d{\bf x}} c({\bf x})\right)^T {\bf d} = {\bf 0} 
\end{cases}
\end{align}
위의 수식을 동시에 만족하는 ${\bf d}$를 찾지 못하면 업데이트를 멈춘다. 잘 생각해보면 특정한 ${\bf d}={\bf d}^* $가 $\left(\frac{d}{d{\bf x}} c({\bf x})\right)^T {\bf d} = {\bf 0}$를 만족한다면 ${\bf d}=-{\bf d}^* $ 역시 $\left(\frac{d}{d{\bf x}} c({\bf x})\right)^T {\bf d} = {\bf 0}$ 를 만족한다. ${\bf d}={\bf d}^* $ 혹은 ${\bf d}=-{\bf d}^* $ 둘중하나는 $\left(\frac{d}{d{\bf x}} f({\bf x})\right)^T {\bf d} < {\bf 0}$ 를 만족하므로 위의 부등식을 만족하는 ${\bf d}$는 $\left(\frac{d}{d{\bf x}} f({\bf x})\right)^T {\bf d} = {\bf 0}$인 경우를 제외하고 항상 찾을 수 있다. 결론적으로 ${\bf d}$는 $\left(\frac{d}{d{\bf x}} f({\bf x})\right)^T$와 $\left(\frac{1}{d{\bf x}} c({\bf x})\right)^T$ 이 평행이 될대까지 업데이트 해야함을 알 수 있는데 이를 수식으로 쓰면 아래와 같다. 
\begin{align}
\frac{d}{d{\bf x}} f({\bf x}) = \lambda \frac{d}{d{\bf x}} c({\bf x})
\end{align}
결국 우리는 아래 2가지의 식을 동시에 만족하는 ${\bf x}$를 찾으면 된다. 
\begin{align}
\begin{cases}
\frac{d}{d{\bf x}} f({\bf x}) - \lambda \frac{d}{d{\bf x}} c({\bf x}) = {\bf 0} \\\\ \\\\
c({\bf x}) ={\bf 0}
\end{cases}
\end{align}
이는 ${\cal L}({\bf x},\lambda)=f({\bf x}) - \lambda  c({\bf x})$ 에 대하여 아래식을 푸는것과 동치이다. 
\begin{align}
\begin{cases}
\frac{\partial}{\partial{\bf x}} {\cal L}({\bf x},\lambda) = {\bf 0} \\\\ \\\\
\frac{\partial}{\partial\lambda} {\cal L}({\bf x},\lambda) ={\bf 0}
\end{cases}
\end{align}

- 아래와 같이 하나의 **부등호** 로 이루어진 제약조건을 가지는 경우를 상상하여 보자. 
\begin{align}
\underset{ {\bf x} \in \mathbb{R}^p }{ \operatorname{min} } f({\bf x}) \quad \mbox{ subject to } \quad c({\bf x}) \geq 0
\end{align}
이 경우는 아래의 제약을 만족하는 ${\bf d}$를 계속 찾으면 된다. 
\begin{align}
\begin{cases}
\left(\frac{d}{d{\bf x}} f({\bf x})\right)^T {\bf d} < {\bf 0} \\\\ \\\\
c({\bf x}) \geq 0 \\\\ 
c({\bf x})+\left(\frac{d}{d{\bf x}} c({\bf x})\right)^T {\bf d} \geq {\bf 0} \\\\ 
\end{cases}
\end{align}
<br/>
**CASE 1** : 먼저 $c({\bf x}) > 0$ 라고 가정하자. 그럼 아래를 풀면 된다. 
\begin{align}
\begin{cases}
\left(\frac{d}{d{\bf x}} f({\bf x})\right)^T {\bf d} < {\bf 0} \\\\ \\\\
c({\bf x})+\left(\frac{d}{d{\bf x}} c({\bf x})\right)^T {\bf d} \geq {\bf 0} \\\\ 
\end{cases}
\end{align}
이때 $\left(\frac{d}{d{\bf x}} f({\bf x})\right)^T {\bf d} < {\bf 0} $ 을 만족하는 ${\bf d}$가 존재한다고 하자. 이러한 ${\bf d}$를 ${\bf d}^* $ 라고 정의하자. 이제 $c({\bf x})+\left(\frac{d}{d{\bf x}} c({\bf x})\right)^T {\bf d} \geq {\bf 0}$ 가 성립하는지 살펴보자. ${\bf d}={\bf d}^* $ 를 대입하면 
\begin{align}
c({\bf x})+\left(\frac{d}{d{\bf x}} c({\bf x})\right)^T {\bf d}^* \geq {\bf 0}
\end{align}
가 되는데, $c({\bf x})>{\bf 0}$이므로 아래식을 만족하는 적당히 작은 $\delta$가 존재할 것이다. 
\begin{align}
c({\bf x})+\left(\frac{d}{d{\bf x}} c({\bf x})\right)^T \left(\frac{1}{\delta}{\bf d}^* \right)   \geq {\bf 0}
\end{align}
${\bf d}={\bf d}^* $ 가 $\left(\frac{d}{d{\bf x}} f({\bf x})\right)^T {\bf d} < {\bf 0} $ 를 만족하면 ${\bf d}=\frac{1}{\delta}{\bf d}^* $ 도 만족하므로  $\left(\frac{d}{d{\bf x}} f({\bf x})\right)^T {\bf d} < {\bf 0} $ 를 만족하는 ${\bf d}$가 존재하면 아래의 세 부등식을 만족하는 ${\bf d}$는 항상 잡을 수 있다. 
\begin{align}
\begin{cases}
\left(\frac{d}{d{\bf x}} f({\bf x})\right)^T {\bf d} < {\bf 0} \\\\ \\\\
c({\bf x}) \geq 0 \\\\ 
c({\bf x})+\left(\frac{d}{d{\bf x}} c({\bf x})\right)^T {\bf d} \geq {\bf 0} \\\\ 
\end{cases}
\end{align}
따라서 이러한 ${\bf d}$를 못찾는 경우는 $\frac{d}{d{\bf x}} f({\bf x})= {\bf 0} $ 인 경우뿐이다. 
<br/><br/>
**CASE 2** : $c({\bf x}) = 0$ 이라고 하자. 그럼 아래를 풀면 된다. 
\begin{align}
\begin{cases}
\left(\frac{d}{d{\bf x}} f({\bf x})\right)^T {\bf d} < {\bf 0} \\\\ \\\\
\left(\frac{d}{d{\bf x}} c({\bf x})\right)^T {\bf d} \geq {\bf 0} \\\\ 
\end{cases}
\end{align}

\begin{align}
\frac{d}{d{\bf x}} f({\bf x}) = \lambda \frac{d}{d{\bf x}} c({\bf x})
\end{align}
인 경우를 제외하고는 항상 아래 세 부등식을 만족하는 ${\bf d}$를 구할 수 있다. 
\begin{align}
\begin{cases}
\left(\frac{d}{d{\bf x}} f({\bf x})\right)^T {\bf d} < {\bf 0} \\\\ \\\\
c({\bf x}) \geq 0 \\\\ 
c({\bf x})+\left(\frac{d}{d{\bf x}} c({\bf x})\right)^T {\bf d} \geq {\bf 0} \\\\ 
\end{cases}
\end{align}
<br/><br/>

종합하면 아래를 풀면 된다. 
\begin{align}
\begin{cases}
c({\bf x}) > 0 \\\\ \\\\
\frac{d}{d{\bf x}} f({\bf x})= {\bf 0} 
\end{cases}
\end{align}
\begin{align}
\begin{cases}
c({\bf x}) = 0 \\\\ \\\\
\frac{d}{d{\bf x}} f({\bf x}) - \lambda \frac{d}{d{\bf x}} c({\bf x}) = {\bf 0} 
\end{cases}
\end{align}


