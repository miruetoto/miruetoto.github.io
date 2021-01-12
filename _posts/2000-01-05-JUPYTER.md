---
title: (정리) jupyter setting 
layout: post
---

### About this doc 

- 이번장에서는 주피터와 관련된 셋팅을 다룬다. 

- 쿡북형태 

--- 

### R kernel in jupyter 

***resize the figure***
```python
options(repr.plot.width=10, repr.plot.height=3,repr.plot.res=300)
```

---


### initial settings 

***remove the file in trash***
```python
!rm -rf ~/.local/share/Trash/files/* 
```

***load *.py from github*** 
```python
import requests
exec(requests.get('http://miruetoto.github.io/my_code/datahandling.py').text)
```

***rpy2 setting in Jupyter*** 
```python
%load_ext rpy2.ipython
```

***load *.R from github***
```python
%R library(devtools)
%R source_url("http://miruetoto.github.io/my_code/datahandling.r")
```

***show large figure***
```python
import matplotlib as mpl 
import matplotlib.pyplot as plt 
Ipython_default=plt.rcParams.copy() # save initial value 
from matplotlib import cycler
plt.rc('figure',dpi=150) # default value 4 figure.dpi is 72.0 
# plt.rcParams.update(Ipython_default) # load initial value 
```

***check gpu***
```python
from keras import backend as K
print('GPU check 4 Keras: '+ str(K.tensorflow_backend._get_available_gpus()))
import torch
print('GPU check 4 Pytorch: '+ str(torch.cuda.get_device_name(0)))
```

---


***load *.py from gitlab*** 
```python
import gitlab
gl = gitlab.Gitlab('http://10.178.145.54:9000', private_token='RkZz465zdyyEChamLKy8')
gl.auth()
project = gl.projects.get(2)

# (1) load RF.py, RF_withGIT.py, RF_withR.py
RF_py = project.files.get(file_path='modeling/RF.py', ref='fridge').decode()
RF_GIT_py = project.files.get(file_path='utils/RF_withGIT.py', ref='fridge').decode()
RF_R_py = project.files.get(file_path='utils/RF_withR.py', ref='fridge').decode()
exec(str(RF_py, 'utf-8'))
exec(str(RF_GIT_py, 'utf-8'))
exec(str(RF_R_py, 'utf-8'))
```

***load *.R in gitlab***
```python
import gitlab
gl = gitlab.Gitlab('http://10.178.145.54:9000', private_token='RkZz465zdyyEChamLKy8')
gl.auth()
project = gl.projects.get(2)
RF_R_rcode = project.files.get(file_path='utils/RF_Rfunctions.r', ref='fridge').decode()
# tricks for source('Rfunctions.r')
file1 = open("RF_Rfunctions.r","w") 
file1.write(str(RF_R_rcode, 'utf-8'))
file1.close() 
ro.r("source('RF_Rfunctions.r')")
import os
os.remove('RF_Rfunctions.r')
```

