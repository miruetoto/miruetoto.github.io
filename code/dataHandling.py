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

### 입력은 n×p matrix , 혹은 n×p DataFrame 으로 바꿀 수 있는 어떤자료 / 출력 n×p np.matrix 임. 이때 첫번째 row가 0임. 
def lagg(inputMatrix,lag):
    inputdf=pd.DataFrame(inputMatrix)
    shifted=np.asmatrix(inputdf.shift(lag))
    shifted[range(lag),:]=0
    return shifted

def cbind(A,B):
    typ=['matrix','matrix']
    
    A=np.asmatrix(A)
    B=np.asmatrix(B)

    # row-vector에 대한 처리 
    if A.shape[0]==1: typ[0]='rowvec'
    if B.shape[0]==1: typ[1]='rowvec'

    # col-vector에 대한 처리 
    if A.shape[1]==1: typ[0]='colvec'
    if B.shape[1]==1: typ[1]='colvec'    
    
    # 스칼라에 대한 처리 
    if A.shape==(1,1): typ[0]='scala'
    if B.shape==(1,1): typ[1]='scala'
        
    if typ==['scala','scala']:  A=np.array(A); B=np.array(B)
    if typ==['scala','rowvec']: A=np.array(A); 
    if typ==['scala','colvec']: A=np.full(B.shape,A[0,0]); 
    if typ==['scala','matrix']: A=np.full((B.shape[0],1),A[0,0]); 
    	
    if typ==['rowvec','scala']: B=np.array(B)
    #if typ==['rowvec','rowvec']:
    if typ==['rowvec','colvec']: A=A.T
    if typ==['rowvec','matrix']: A=A.T
        
    if typ==['colvec','scala']:  B=np.full(A.shape,B[0,0])
    if typ==['colvec','rowvec']: B=B.T
    #if typ==['colvec','colvec']: 
    #if typ==['colvec','matrix']: 
    
    if typ==['matrix','scala']:  B=np.full((A.shape[0],1),B[0,0])
    if typ==['matrix','rowvec']: B=B.T
    #if typ==['matrix','colvec']: 
    #if typ==['matrix','matrix']:
    
    return np.hstack([A,B])
    
def rbind(A,B):
    typ=['matrix','matrix']
    
    A=np.asmatrix(A)
    B=np.asmatrix(B)

    # row-vector에 대한 처리 
    if A.shape[0]==1: typ[0]='rowvec'
    if B.shape[0]==1: typ[1]='rowvec'

    # col-vector에 대한 처리 
    if A.shape[1]==1: typ[0]='colvec'
    if B.shape[1]==1: typ[1]='colvec'    
    
    # 스칼라에 대한 처리 
    if A.shape==(1,1): typ[0]='scala'
    if B.shape==(1,1): typ[1]='scala'
        
    if typ==['scala','scala']:  A=np.array(A); B=np.array(B)
    if typ==['scala','rowvec']: A=np.full(B.shape,A[0,0]); 
    if typ==['scala','colvec']: A=np.array(A);
    if typ==['scala','matrix']: A=np.full((1,B.shape[1]),A[0,0]); 
    	
    if typ==['rowvec','scala']: B=np.full((1,A.shape[1]),B[0,0]); 
    #if typ==['rowvec','rowvec']:
    if typ==['rowvec','colvec']: B=B.T
    #if typ==['rowvec','matrix']: 
        
    #if typ==['colvec','scala']:  
    if typ==['colvec','rowvec']: A=A.T
    #if typ==['colvec','colvec']: 
    if typ==['colvec','matrix']: A=A.T
    
    if typ==['matrix','scala']:  B=np.full((1,A.shape[1]),B[0,0])
    #if typ==['matrix','rowvec']: 
    if typ==['matrix','colvec']: B=B.T
    if typ==['matrix','matrix']:
    
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
