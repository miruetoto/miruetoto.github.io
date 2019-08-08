import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import math  

def ccfrq(start=0,end=1,samplingFreq=10):
    return cbind(np.arange(start,end,1/samplingFreq),end).T

def cofrq(start=0,end=1,samplingFreq=10):
    return np.asmatrix(np.arange(start,end,1/samplingFreq)).T

def ocfrq(start=0,end=1,samplingFreq=10):
    return np.asmatrix(np.arange(start,end,1/samplingFreq)).T+1/samplingFreq

def oofrq(start=0,end=1,samplingFreq=10):
    rtn=np.asmatrix(np.arange(start,end,1/samplingFreq)).T
    return rtn[1:len(rtn)]

def ccprd(start=0,end=1,samplingPeriod=1):
    return cbind(np.arange(start,end,samplingPeriod),end).T

def coprd(start=0,end=1,samplingPeriod=1):
    return np.asmatrix(np.arange(start,end,samplingPeriod)).T

def ocprd(start=0,end=1,samplingPeriod=1):
    return np.asmatrix(np.arange(start,end,samplingPeriod)).T+samplingPeriod

def ooprd(start=0,end=1,samplingPeriod=1):
    rtn=np.asmatrix(np.arange(start,end,samplingPeriod)).T
    return rtn[1:len(rtn)]

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
    print("type of data        :   ",type(A))
    if type(A) is int or float or bool :  print("len or shape of data: ",1)
    elif type(A) is str or list or tuple or dict or set :  print("len or shape of data: ",len(A))
    else : print("len or shape of data: ",A.shape)

def colvec2array(a):
    return np.array(a.T)[0,:]
    
def rowvec2array(a):
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
