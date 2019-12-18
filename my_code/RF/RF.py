def ginverseDiag(d,threshold=0.0005):
    d[d<threshold]=0
    d[d>0]=1/d[d>0]
    return np.asmatrix(np.diag(d))

def getβ(X,Y):
    XX=X.T*X
    d,P=np.linalg.eig(XX)
    DI=ginverseDiag(d,threshold=0.05)
    betahat=(P*DI*P.I)*X.T*Y
    return betahat
