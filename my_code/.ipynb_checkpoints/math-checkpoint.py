def cor(a,b):
    a=np.asmatrix(np.array(a)).T;b=np.asmatrix(np.array(b)).T; 
    rtn=a.T*b/np.sqrt(a.T*a)/np.sqrt(b.T*b)
    return rtn[0,0]

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

