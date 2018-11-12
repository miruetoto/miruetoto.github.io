---
layout: post 
title: (믿거나 말거나) 딥러닝 
---

딥러닝에 대해서 잘 모른다. 그래서 공부한다. 공부한 내용을 정리하는데 틀린내용이 있을 수 있다. 그래서 제목은 믿거나 말거나 딥러닝이다. 

### GAN 
- 우리가 관측한 자료 $\\{x_i\\}_ {i=1}^{n}$가 평균이 $500$이고 분산이 $5^2$인 정규분포 생성된다고 가정하자. 

- $G$는 주어진 자료 $\\{x_i\\}_ {i=1}^{n}$로부터 generator's distribution $p_g(x)$를 알고 싶다. 즉 $G$의 목적은 
\begin{align}
p_g(x)=\frac{1}{\sqrt{10\pi}}\exp^{\frac{-1}{2}\left(\frac{x-500}{25}\right)^2}
\end{align}

- $\\{z_i\\}_ {i=1}^{n}$를 평균이 0이고 분산이 1인 정규분포 $p_z(z)$에서 발생시킨다. 그리고
\begin{align}
x_i \approx G(z_i; \theta_g)
\end{align}
가 되도록 MLP를 쌓는다. 당연히 $G(z_i)=5\times z_i + 500$이 되도록 학습이 될 것이고 이때 $\theta_g=(500,5)$가 된다. 

- 
