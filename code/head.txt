## 1. remove trash
!rm -rf ~/.local/share/Trash/files/*

## 2. load useful functions
import requests
exec(requests.get('http://miruetoto.github.io/code/dataHandling.py').text)
#exec(requests.get('http://miruetoto.github.io/code/HST/hstfunctions.py').text)

## 3. for R user
%load_ext rpy2.ipython
%R library(devtools)
#%R source_url('http://miruetoto.github.io/code/HST/hstfunctions.r')

## 4. plt
import matplotlib as mpl 
import matplotlib.pyplot as plt 
Ipython_default=plt.rcParams.copy() # save initial value 
from matplotlib import cycler
plt.rc('figure',dpi=150) # default value 4 figure.dpi is 72.0 
# plt.rcParams.update(Ipython_default) # load initial value 

## 5. Check GPU
from keras import backend as K
print('GPU check 4 Keras: '+ str(K.tensorflow_backend._get_available_gpus()))
import torch
print('GPU check 4 Pytorch: '+ str(torch.cuda.get_device_name(0)))
