## HST 
def Smat(f,Edg,W=None):
    n=len(f)
    nbhood=init("0",(n,n)) # the node who can flow the snow to i. 
    for i in co(0,n):
        nbhood[i,:]=(f>f[i,:]).T&(Edg[i,:]==1)
    S=init("0",(n,n))
    rowsumE=m2a(apply(Edg,1,'np.sum'))
    rowsumN=m2a(apply(nbhood,1,'np.sum'))
    for i in co(0,n):
        for j in co(0,n):
            if i==j: S[i,j]=rowsumN[i]/rowsumE[i]
            else: S[i,j]=nbhood[i,j]/rowsumE[i]
    return S

def hst(f,Edg,τ):
    n=len(f)
    rtn=initpd("0",n=n,p=2,vname=['Node(=v)','h0'])
    rtn['Node(=v)']=cc(1,n); rtn['Node(=v)'].astype(int)
    rtn['h0']=f
    for ℓ in cc(1,τ): 
        S=Smat(np.asmatrix(rtn.eval('h'+str(ℓ-1))).T,Edg)
        ϵ=init("u",(n,1))*0.2
        rtn['ϵ fall'+str(ℓ-1)]=ϵ
        rtn['ϵ stack'+str(ℓ-1)]=S*ϵ
        rtn['h'+str(ℓ)]=np.asmatrix(rtn.eval('h'+str(ℓ-1))).T+S*ϵ
    return rtn

## regularity 
def regularity(hstresult):
    n=hstresult.shape[0]
    τ=int((hstresult.shape[1]-2)/3)
    ϵmat=np.asmatrix(hstresult[sprod('ϵ fall',cc(0,τ-1))])
    dothpd=np.asmatrix(hstresult[sprod('ϵ stack',cc(0,τ-1))])
    rtn=init("0",τ)
    for ℓ in co(0,τ):
        a=ϵmat[:,ℓ]
        b=dothmat[:,ℓ]
        rtn[ℓ]=a.T*b/np.sqrt((a.T*a)*(b.T*b))
        
    return rtn
