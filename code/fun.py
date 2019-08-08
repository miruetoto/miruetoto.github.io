import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import math  

def cc(start=0,end=1,samplingFreq=1):
    return c2a(cbind(np.arange(start,end,1/samplingFreq),end).T)

def co(start=0,end=1,samplingFreq=1):
    return c2a(np.asmatrix(np.arange(start,end,1/samplingFreq)).T)

def oc(start=0,end=1,samplingFreq=1):
    return c2a(np.asmatrix(np.arange(start,end,1/samplingFreq)).T+1/samplingFreq)

def oo(start=0,end=1,samplingFreq=1):
    rtn=np.asmatrix(np.arange(start,end,1/samplingFreq)).T
    return c2a(rtn[1:len(rtn)])

def cc(start=0,end=1,samplingPeriod=1):
    return c2a(cbind(np.arange(start,end,samplingPeriod),end).T)

def co(start=0,end=1,samplingPeriod=1):
    return c2a(np.asmatrix(np.arange(start,end,samplingPeriod)).T)

def oc(start=0,end=1,samplingPeriod=1):
    return c2a(np.asmatrix(np.arange(start,end,samplingPeriod)).T+samplingPeriod)

def oo(start=0,end=1,samplingPeriod=1):
    rtn=np.asmatrix(np.arange(start,end,samplingPeriod)).T
    return c2a(rtn[1:len(rtn)])

### 입력은 n×p np.matrix 이고 출력도 n×p np.matrix 임. 이때 첫번째 row가 0임. 
def lagg(inputMatrix,lag):
    inputdf=pd.DataFrame(inputMatrix)
    shifted=np.asmatrix(inputdf.shift(lag))
    shifted[range(lag),:]=0
    return shifted

def cbind(A,B):
    A=np.asmatrix(A)
    B=np.asmatrix(B)
    if np.asmatrix(A).shape==(1,1):
        A=np.full((B.shape[0],1),A[0,0])
    if np.asmatrix(B).shape==(1,1):
        B=np.full((A.shape[0],1),B[0,0])
    return np.hstack([A,B])
    
def rbind(A,B):
    A=np.asmatrix(A)
    B=np.asmatrix(B)
    if np.asmatrix(A).shape==(1,1):
        A=np.full((1,B.shape[1]),A[0,0])
    if np.asmatrix(B).shape==(1,1):
        B=np.full((1,A.shape[1]),B[0,0])
    return np.vstack([A,B])

def info(A):
    print("type of data         :   ",type(A))
    if type(A) is int       :  print("len or shape of data :   ",1); 
    elif type(A) is float   :  print("len or shape of data :   ",1)
    elif type(A) is bool    :  print("len or shape of data :   ",1)    
    elif type(A) is str     :  print("len or shape of data :   ",len(A))
    elif type(A) is list    :  print("len or shape of data :   ",len(A))
    elif type(A) is tuple   :  print("len or shape of data :   ",len(A))
    elif type(A) is dict    :  print("len or shape of data :   ",len(A))
    elif type(A) is set     :  print("len or shape of data :   ",len(A))       
    elif type(A) is range   :  print("len or shape of data :   ",len(A))
    else                    :  print("len or shape of data :   ",A.shape)
    
### n×1 matrix를 길이가 n인 np.array로 변환 
def c2a(a):
    return np.array(a.T)[0,:]

### 1×p matrix를 길이가 p인 np.array로 변환 
def r2a(a):
    return np.array(a)[0,:]

def grd(f,x):
    h=1e-4
    grad=np.zeros_like(x)
    
    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx]=tmp_val +h 
        fxh1=f(x)
        x[idx]=tmp_val -h
        fxh2=f(x)
        grad[idx]=(fxh1-fxh2)/(2*h)
        x[idx]=tmp_val 
    return grad   