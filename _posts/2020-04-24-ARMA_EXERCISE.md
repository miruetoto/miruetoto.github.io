---
layout : post 
title : (강의) ARMA 문제풀이 
---

이제 6장의 연습문제를 풀어보자. 

### 6.1 

***model 1: $Z_t-0.8Z_{t-1}=\epsilon_t$***

(1) 모형: AR(1)

(2) 평균: $\mu=0$

(3) 표현: $(1-0.8B)Z_t=\epsilon_t$

(4) ACF 
- corr: $\rho_0=1, \rho_1=0.8, \rho_2=0.8^2, \rho_3=0.8^3, \rho_4=0.8^4 $ 
- cov: $\gamma_0=\frac{1}{1-0.8^2}, \gamma_1=\frac{0.8}{1-0.8^2},\gamma_2=\frac{0.8^2}{1-0.8^2}, \gamma_3=\frac{0.8^3}{1-0.8^2}, \gamma_4=\frac{0.8^4}{1-0.8^2}.$

(5) PACF
- $\phi_{11}=0.8, \phi_{22}=0, \phi_{33}=0, \phi_{44}=0.$

(6) correlogram: 
- ACF는 지수적으로 감소하는 모양. 
- PACF는 lag=1에서만 값이 존재하는 모양.  

---

***model 2: $Z_t-0.5Z_{t-1}=100+\epsilon_t$***

(1) 모형: AR(1) with drift 

(2) 평균: $\mu=200$

(3) 표현: $(1-0.5B)(Z_t-200)=\epsilon_t$

(4) ACF 
- corr: $\rho_0=1, \rho_1=0.5, \rho_2=0.5^2, \rho_3=0.5^3, \rho_4=0.5^4 $ 
- cov: $\gamma_0=\frac{1}{1-0.5^2}, \gamma_1=\frac{0.5}{1-0.5^2},\gamma_2=\frac{0.5^2}{1-0.5^2}, \gamma_3=\frac{0.5^3}{1-0.5^2}, \gamma_4=\frac{0.5^4}{1-0.5^2}.$

(5) PACF
- $\phi_{11}=0.5, \phi_{22}=0, \phi_{33}=0, \phi_{44}=0.$

(6) correlogram:
- ACF는 지수적으로 감소하는 모양
- PACF는 lag=1에서만 값이 존재하는 모양. 

---

***model 3: $Z_t=\epsilon_t+0.7\epsilon_{t-1}$***

(1) 모형: MA(1)

(2) 평균: $\mu=0$

(3) 표현: $Z_t=(1+0.7B)\epsilon_t$

(4) ACF 
- corr: $\rho_0=1, \rho_1=0.7, \rho_2=0, \rho_3=0, \rho_4=0 $ 
- cov: $\gamma_0=\frac{1}{1+0.49}, \gamma_1=\frac{0.7}{1+0.49},\gamma_2=0, \gamma_3=0, \gamma_4=0.$

(5) PACF
- $\phi_{11}=-0.7, \phi_{22}=(-0.7)^2, \phi_{33}=(-0.7)^3, \phi_{44}=(-0.7)^4.$

(6) correlogram
- ACF는 lag=1에서만 존재하는 모양. 
- PACF는 (부호가 교차하면서) 지수적으로 감소하는 모양. 

---

***model 4: $Z_t-9.5=\epsilon_t-1.3\epsilon_{t-1}+0.6\epsilon_{t-2}$***

(1) 모형: MA(2)

(2) 평균: $\mu=9.5$

(3) 표현: $Z_t-9.5=(1-1.3B+0.6B^2)\epsilon_t$

(4) ACF 
- corr: $\rho_0=, \rho_1=, \rho_2=, \rho_3=, \rho_4=.$ 
- cov: $\gamma_0=, \gamma_1=,\gamma_2=, \gamma_3=, \gamma_4=.$

(5) PACF
- $\phi_{11}=, \phi_{22}=?, \phi_{33}=??, \phi_{44}=??.$

(6) correlogram
- ACF는 lag=1에서만 존재하는 모양. 
- PACF는 (부호가 교차하면서) 지수적으로 감소하는 모양. 
