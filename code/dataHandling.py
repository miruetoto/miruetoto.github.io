import numpy as np
import pandas as pd

def cc(start=0,end=1,samplingFreq=1):
    return m2a(cbind(np.arange(start,end,1/samplingFreq),end).T)

def co(start=0,end=1,samplingFreq=1):
    return m2a(np.asmatrix(np.arange(start,end,1/samplingFreq)).T)

def oc(start=0,end=1,samplingFreq=1):
    return m2a(np.asmatrix(np.arange(start,end,1/samplingFreq)).T+1/samplingFreq)

def oo(start=0,end=1,samplingFreq=1):
    rtn=np.asmatrix(np.arange(start,end,1/samplingFreq)).T
    return m2a(rtn[1:len(rtn)])

### 입력은 n×p np.matrix 이고 출력도 n×p np.matrix 임. 이때 첫번째 row가 0임. 
def lagg(inputMatrix,lag):
    inputdf=pd.DataFrame(inputMatrix)
    shifted=np.asmatrix(inputdf.shift(lag))
    shifted[range(lag),:]=0
    return shifted

def cbind(A,B):
    try: A.shape 
    except AttributeError: 
        A=np.asmatrix(A).T
        B=np.asmatrix(B)
        if np.asmatrix(A).shape==(1,1): A=np.full((B.shape[0],1),A[0,0])
        if np.asmatrix(B).shape==(1,1): B=np.full((A.shape[0],1),B[0,0])
    else:
        try: B.shape 
        except AttributeError: 
            A=np.asmatrix(A)
            B=np.asmatrix(B).T
            if np.asmatrix(A).shape==(1,1): A=np.full((B.shape[0],1),A[0,0])
            if np.asmatrix(B).shape==(1,1): B=np.full((A.shape[0],1),B[0,0])
        else:
            A=np.asmatrix(A)
            B=np.asmatrix(B)
            if np.asmatrix(A).shape==(1,1): A=np.full((B.shape[0],1),A[0,0])
            if np.asmatrix(B).shape==(1,1): B=np.full((A.shape[0],1),B[0,0])
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
    
### n×1 이거나 1×n matrix를 길이가 n인 np.array로 변환 
def m2a(A):
    if A.shape[0]==1: rtn=np.array(A)[0,:]
    elif A.shape[1]==1: rtn=np.array(A.T)[0,:]
    else :
        print("The input matrix is neither a row-vector nor a col-vector. So we will not do any conversion.")
        rtn=A
    return rtn

### 초기화 (1) 0 (2) 유니폼 (3) 정규분포
def init(typ,dim):
    if dim*0==0: 
        if typ=="0": rtn=np.zeros(dim)
        elif typ=="u": rtn=np.random.random(dim)
        elif typ=="n": rtn=np.random.normal(0,1,dim)
    else:
        if typ=="0": rtn=np.asmatrix(np.zeros(dim))
        elif typ=="u": rtn=np.asmatrix(np.random.random(dim))
        elif typ=="n": rtn=np.asmatrix(np.random.normal(0,1,dim))
    return rtn
