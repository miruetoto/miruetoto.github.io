### 1. hst: calculation 
def Smat(f,ϵ,Edg,W=None):
    n=len(f)
    calU=init("0",(n,n)) # i 보다 높은 지형
    calL=init("0",(n,n)) # i 보다 낮은 지형
    for i in co(0,n):
        calU[i,:]=(f>=f[i,:]).T&(Edg[i,:]>0) #nbhood1[i,:]=(f>f[i,:]+ϵ[i]).T&(Edg[i,:]>0)
        calL[i,:]=(f<f[i,:]).T&(Edg[i,:]>0) #nbhood2[i,:]=(f+ϵ[i]<f[i,:]).T&(Edg[i,:]>0)
    Stemp=calU-calL
    S=init("0",(n,n))
    rowsumE=m2a(apply(Edg,1,'np.sum'))
    rowsumN=m2a(apply(Stemp,1,'np.sum'))
    for i in co(0,n):
        for j in co(0,n):
            if i==j: S[i,j]=1-rowsumN[i]/rowsumE[i]
            else: S[i,j]=Stemp[i,j]/rowsumE[i]
    return S-np.diag(np.diag(S)*1)

def Smat2(f,ϵ,Edg,W=None):
    n=len(f)
    calU=init("0",(n,n)) # i 보다 높은 지형
    for i in co(0,n):
        calU[i,:]=(f>f[i,:]).T&(Edg[i,:]>0) #nbhood1[i,:]=(f>f[i,:]+ϵ[i]).T&(Edg[i,:]>0)
    S=init("0",(n,n))
    for i in co(0,n):
        for j in co(0,n):
            if i==j: S[i,j]=0
            else: S[i,j]=calU[i,j]
    return S

def hst(f,Edg,τ,γ,rvsnow=False):
    n=len(f)
    rtn=initpd("0",n=n,p=2,vname=['Node(=v)','h0'])
    rtn['Node(=v)']=cc(1,n); rtn['Node(=v)'].astype(int)
    rtn['h0']=f
    print('hst start')
    for ℓ in cc(1,τ): 
        if rvsnow==False: ϵ=(init("0",(n,1))+1)*γ 
        else: ϵ=init("u",(n,1))*γ 
        S=Smat(np.asmatrix(rtn.eval('h'+str(ℓ-1))).T,ϵ,Edg)
        rtn['ϵ fall'+str(ℓ-1)]=ϵ
        rtn['ϵ stack'+str(ℓ-1)]=S*ϵ
        rtn['h'+str(ℓ)]=np.asmatrix(rtn.eval('h'+str(ℓ-1))).T+S*ϵ
        print('\r'+str(ℓ),'/'+str(τ),sep='',end='')
    print('\n'+'hst end')
    return rtn

def hst2(f,Edg,τ,γ,rvsnow=False):
    n=len(f)
    rtn=initpd("0",n=n,p=2,vname=['Node(=v)','h0'])
    rtn['Node(=v)']=cc(1,n); rtn['Node(=v)'].astype(int)
    rtn['h0']=f
    print('hst start')
    for ℓ in cc(1,τ): 
        print('\r'+str(ℓ),'/'+str(τ),sep='',end='')
        if rvsnow==False: ϵ=(init("0",(n,1))+1)*γ 
        else: ϵ=init("u",(n,1))*γ 
        S=Smat2(np.asmatrix(rtn.eval('h'+str(ℓ-1))).T,ϵ,Edg) ## hst1과 hst2는 이부분만 다르다 
        rtn['ϵ fall'+str(ℓ-1)]=ϵ
        rtn['ϵ stack'+str(ℓ-1)]=S*ϵ
        rtn['h'+str(ℓ)]=np.asmatrix(rtn.eval('h'+str(ℓ-1))).T+S*ϵ        
    print('\n'+'hst end')
    return rtn

def hmat(hstresult):
    τ=int((hstresult.shape[1]-2)/3)
    rtn=np.asmatrix(hstresult[sprod('h',cc(0,τ))])
    return rtn 

def ϵfallmat(hstresult):
    τ=int((hstresult.shape[1]-2)/3)
    rtn=np.asmatrix(hstresult[sprod('ϵ fall',cc(0,τ-1))])
    return rtn 
    
def ϵstackmat(hstresult):
    τ=int((hstresult.shape[1]-2)/3)
    rtn=np.asmatrix(hstresult[sprod('ϵ stack',cc(0,τ-1))])
    return rtn 

def cor(a,b):
    a=np.asmatrix(np.array(a)).T;b=np.asmatrix(np.array(b)).T; 
    rtn=a.T*b/np.sqrt(a.T*a)/np.sqrt(b.T*b)
    return rtn[0,0]

def snowdist(hstresult): 
    hh=hmat(hstresult)
    n=len(hh)
    rtn=init("0",(n,n))
    print('snowdist')
    for i in co(0,n):
        print('\r'+str(i+1),'/'+str(n),sep='',end='')
        for j in co(0,n):
            rtn[i,j]=np.sqrt((hh[i,:]-hh[j,:])*(hh[i,:]-hh[j,:]).T)[0,0]
    print('\n'+'end')
    return rtn

def snowdist2(hstresult): 
    hhdot=ϵstackmat(hstresult)
    n=len(hhdot)
    rtn=init("0",(n,n))
    print('snowdist')
    for i in co(0,n):
        print('\r'+str(i+1),'/'+str(n),sep='',end='')
        for j in co(0,n):
            rtn[i,j]=cor(hh[i,:],hh[j,:])
    print('\n'+'end')
    return rtn

### 2. hst: visualization 
def pcavis(hstresult,figsize=(15, 10),dpi=600,size=(200,15),fade=0.5): # size=(size of obs representation, size of text which represent obs index)
    sdist=snowdist(hstresult) # get snow dist 
    from sklearn.decomposition import PCA 
    from mpl_toolkits import mplot3d
    print('PCA start')
    pca=PCA(n_components=3) # PCA start 
    pca.fit(sdist) 
    pcarslt=pca.transform(sdist) # PCA end 
    print('end')
    Fig=plt.figure(figsize=figsize, dpi=dpi) # Make figure object 
    ax=plt.axes(projection='3d') # define type of axes: 3d plot 
    ax.scatter3D(pcarslt[:,0],pcarslt[:,1],pcarslt[:,2],s=size[0],alpha=fade) # drawing each obs by scatter in 3d axes
    print('labeling')
    for i in cc(1,n): 
        print('\r'+str(i),'/'+str(n),sep='',end='')
        ax.text(pcarslt[i-1,0],pcarslt[i-1,1],pcarslt[i-1,2],'%s'% (str(i)), size=size[1], zorder=1,color='k') # numbering index of nodes 
    print('\n'+'end')
    rtn=Fig 
