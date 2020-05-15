---
layout : post 
title : (논문) EPT와 Vogt 방법을 활용한 변화점 탐지기법 
---

### About this doc

- Draft version. 

- Ref. <br/><br/>
[1] Kim, D., Choi, G., & Oh, H. S. (2019). Ensemble Patch Transformation: A New Tool for Signal Decomposition. arXiv preprint arXiv:1904.03643. <br/>
[2] Vogt, M., & Dette, H. (2015). Detecting gradual changes in locally stationary processes. The Annals of Statistics, 43(2), 713-740. 

### Method 

- consider Gaussian processes $\{X_i\}$ with time-varying dependent structure such that 
\begin{align}
X_i=\begin{cases}
0.1\epsilon_i \\\\ \\ i=1,2,\dots,50
5\epsilon_i \\\\ \\ i=51,52,\dots,150
(0.5i-25)\epsilon_i \\\\ \\ i=151,152,\dots,200
\end{cases}
\end{align}
