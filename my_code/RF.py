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

def nextaction(sp1,sp2,laststatus,βhat,Ubounds,Lbounds,λ1=10e-6,λ2=10e-6): 
    Ysp1=sp1
    Ysp2=sp2
    ## Estimate next
    Xtmp=laststatus
    Ywillbe = Xtmp*betahat
    Errwillbe = np.array([Ysp1,Ysp2])- Ywillbe
    ### we want to solve minimize 
    ### min_x Lx, where Lx:=1/2|Ax-b|^2 + λ1|x|+λ2|x|^2
    ### In our cases, U1*betahat[0,:] should be -Errwillbe, thus let
    ### A'=betahat[0,:], x'=U1, b'=-Errwillbe.  
    ### then the equation U1*betahat[0,:]=-Errwillbe is x'A'-b'=0
    ### Now we can use admm algorithm.
    lamb1= λ1
    lamb2= λ2
    A = np.array(betahat[0:2]).T
    b = np.array(Errwillbe.T)
    ## determind next action 
    %R -i A,b,lamb1,lamb2
    %R dU<-admm.enet(A, b,lambda1=lamb1,lambda2=lamb2)[[1]]
    %R -o dU
    #print(dU)
    nextU=Xtmp[:,0:2]+np.asmatrix(dU).T #8 is lag*numberofU
    if(np.sum(nextU>Ubounds)>0): nextU[np.where(nextU>Ubounds)]=np.asmatrix(Ubounds)[np.where(nextU>Ubounds)]
    if(np.sum(nextU<Lbounds)>0): nextU[np.where(nextU<Lbounds)]=np.asmatrix(Lbounds)[np.where(nextU<Lbounds)]

    return m2a(nextU)
