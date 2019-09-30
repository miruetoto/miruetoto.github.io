### 1. hst: calculation 

def hst1(f,Edg,b,γ):
# 1. choose u from {1,2,...,n}
# 2. generate ϵ form U(0,1)
# 3. f(u) <- f(u)+ϵ
# 4. choose v \in N_i such that f(v) \leq f(u)
# 5. u <- v and repeat 3-4 until {v: v \in N_i & f(v) \leq f(u)}=\emptyset 
    # 1. choose u from {1,2,...,n}
    n=len(f)
    from random import sample 
    u=sample(list(co(0,n)),1)[0]
    # 2. generate ϵ form U(0,1)
    ϵ=init('u',1)[0]*b
    rtn=f.copy()
    ##i=1
    iter=0
    while True:
        iter=iter+1
        ##print(i)
        # 3. f(u) <- f(u)+ϵ*0.9
        rtn[u]=rtn[u]+ϵ*(γ**iter)
        # 4. choose v \in N_u such that f(v) \leq f(u)
        N_u=list(np.where(Edg[u,:]==1)[1])
        stop_criterion=sum(rtn[N_u]<=rtn[u]) # if stop_criterion=0, then we should stop. 
        if stop_criterion==0: break;
        if iter>500: break;
        else: 
            v=N_u[sample(list(np.where(rtn[N_u]<=rtn[u])[0]),1)[0]]
            rtn[v]=rtn[v]+ϵ*Edg[u,v]
        u=v
        ##i=i+1
    # 5. u <- v and repeat 3-4 until {v: v \in N_i & f(v) \leq f(u)}=\emptyset 
    return rtn

def hst(f,Edg,τ,b,γ):
    n=len(f)
    rtn=initpd("0",n=n,p=2,vname=['Node(=v)','h0'])
    rtn['Node(=v)']=cc(1,n); rtn['Node(=v)'].astype(int)
    rtn['h0']=f
    print('hst start (' +'τ='+str(τ)+', b='+str(b)+' ,γ='+str(γ)+')')
    for ℓ in cc(1,τ): 
        print('\r'+str(ℓ),'/'+str(τ),sep='',end='')
        Edgtemp=init('0',(n,n))
        while np.sum(Edgtemp)==0: 
            Edgtemp=(init('u',(n,n))<Edg)*1
        rtn['h'+str(ℓ)]=hst1(rtn['h'+str(ℓ-1)],Edg=Edgtemp,b=b,γ=γ)
    print('\n'+'hst end')
    return rtn

def hmat(hstresult):
    τ=int((hstresult.shape[1]-2))
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

def snowdist(hh,τmax=None,prnt=False): 
    #hh=hmat(hstresult)
    if τmax==None: rtn=L2dist(hh,prnt=prnt)
    else: rtn=L2dist(hh[:,0:(τmax+1)],prnt=prnt)
    return rtn

def dist2Edg(dist,θ=1):
    n=len(dist)
    rtn=init('0',(n,n))
    for i in co(0,n):
        for j in co(0,n):
            if i==j: rtn[i,j]=0
            else: rtn[i,j]=np.exp(-dist[i,j]**2/θ)
    return rtn

def Glaplacian(Edg):
    D=np.asmatrix(np.diag(m2a(apply(Edg,'sum'))))
    rtn=D-Edg
    return rtn

def L2dist(hhlike,prnt=False): #hh:=n*p 
    hhlike=np.array(hhlike)
    n=len(hhlike)
    rtn=np.array(init('0',(n,n)))
    try: 
        rtn=np.sqrt(np.sum((hhlike[:,np.newaxis,:]-hhlike[np.newaxis,:,:])**2,axis=-1))
    except MemoryError:
        if prnt==True: print('calculating snowdistance serially(due to lack of memory)')
        for i in co(0,n):
            rtn[i,:]=np.sqrt(np.sum((hhlike[i,:]-hhlike[:,:])**2,axis=1))
            if prnt==True: print('\r'+str(i),'/'+str(n),sep='',end='')
        if prnt==True: print('\n'+'end')
    return np.asmatrix(rtn)


### 2. hst: visualization 
def datavis4ts(f,nodename=None,groupindex=None,
           figname='temp',figsize=(1,1),dpi=1,cex=1,text=1,fade=1):
    n=len(f)
    
    if groupindex==None: colors=[0]*n
    elif groupindex=='continuous': colors=cm.rainbow(np.linspace(1, 0, n))
    else: colors=np.array(groupindex)
    
    f=np.array(f)
    figsize=(15*figsize[0],10*figsize[1])
    dpi=200*dpi
    cex=20*cex
    text=15*text
    fade=fade
    
    Fig=plt.figure(figsize=figsize, dpi=dpi) # Make figure object 
    ax=plt.axes()
    plt.scatter(cc(1,n),f,c=colors,s=cex,alpha=fade)
    style=dict(size=text,color='k')
    
    if nodename==None:
        for i in cc(1,n): 
            ax.text(i,f[i-1],'%s'% str(i), **style) # numbering index of nodes 
        rtn=Fig 
    else: 
        for i in cc(1,n): 
            ax.text(i,f[i-1],'%s'% nodename[i-1], **style) # numbering index of nodes 
        rtn=Fig 
    rtn.savefig(figname+'.png')

def datavis4sct(v1,v2,nodename=None,groupindex=None,
           figname='temp',figsize=(1,1),dpi=1,cex=1,text=1,fade=1):
    n=len(v1)
    
    if groupindex==None: colors=[0]*n
    elif groupindex=='continuous': colors=cm.rainbow(np.linspace(1, 0, n))
    else: colors=np.array(groupindex)
    
    v1=np.array(v1)
    v2=np.array(v2)
    figsize=(15*figsize[0],10*figsize[1])
    dpi=200*dpi
    cex=20*cex
    text=15*text
    fade=fade
    
    Fig=plt.figure(figsize=figsize, dpi=dpi) # Make figure object 
    ax=plt.axes()
    plt.scatter(v1,v2,c=colors,s=cex,alpha=fade)
    style=dict(size=text,color='k')
    
    if nodename==None:
        for i in cc(1,n): 
            ax.text(v1[i-1],v2[i-1],'%s'% str(i), **style) # numbering index of nodes 
        rtn=Fig 
    else: 
        for i in cc(1,n): 
            ax.text(v1[i-1],v2[i-1],'%s'% nodename[i-1], **style) # numbering index of nodes 
        rtn=Fig 
    rtn.savefig(figname+'.png')
    
    
def pca4vis(sdistresult,nodename=None,groupindex=None,
           figname='temp',figsize=(1, 1),dpi=1,cex=1,text=1,fade=1,
           prnt=False,logscale=(False,False,False)): # size=(size of obs representation, size of text which represent obs index)

    from sklearn.decomposition import PCA 
    from mpl_toolkits import mplot3d
    if prnt==True: print('PCA start')
    pca=PCA(n_components=3) # PCA start 
    pca.fit(sdistresult) 
    pcarslt=pca.transform(sdistresult) # PCA end 
    if prnt==True: print('end')

    n=len(sdistresult)
    if groupindex==None: colors=['gray']*n
    elif groupindex=='continuous': colors=cm.rainbow(np.linspace(1, 0, n))
    else: colors=np.array(groupindex)

    figsize=(15*figsize[0],10*figsize[1])
    dpi=200*dpi
    cex=200*cex
    text=15*text
    fade=fade
    
    Fig=plt.figure(figsize=figsize, dpi=dpi) # Make figure object 
    ax=plt.axes(projection='3d') # define type of axes: 3d plot 
    
    ax.scatter3D(pcarslt[:,0],pcarslt[:,1],pcarslt[:,2],s=cex,c=colors,alpha=fade) # drawing each obs by scatter in 3d axes   
    if logscale[0]==True: ax.set_xscale('log')
    if logscale[1]==True: ax.set_yscale('log')
    if logscale[2]==True: ax.set_zscale('log')
        
    if prnt==True: print('labeling (observation-wise)')
    if nodename==None:
        for i in cc(1,n): 
            if prnt==True: print('\r'+str(i),'/'+str(n),sep='',end='')
            ax.text(pcarslt[i-1,0],pcarslt[i-1,1],pcarslt[i-1,2],'%s'% (str(i)), size=text, zorder=1,color='k') # numbering index of nodes 
        if prnt==True: print('\n'+'end')
    else: 
        for i in cc(1,n): 
            if prnt==True: print('\r'+str(i),'/'+str(n),sep='',end='')
            ax.text(pcarslt[i-1,0],pcarslt[i-1,1],pcarslt[i-1,2],'%s'% (nodename[i-1]), size=text, zorder=1,color='k') # numbering index of nodes 
        if prnt==True: print('\n'+'end')
    Fig.savefig(figname+'.png')

def pca4msvis(hstresult,τlist,
              nodename=None,groupindex=None,
              figname='temp',figsize=(1, 1),dpi=1,cex=1,text=1,fade=1,
              prnt=False,logscale=(False,False,False)): # size=(size of obs representation, size of text which represent obs index)
    dhhlist=τlist.copy()
    sdistrslt=τlist.copy()
    M=len(τlist)
    dhh0=np.asmatrix(hstresult[sprod('h',cc(0,τlist[0]))])
    sdistrslt0=snowdist(dhh0)
    pca4vis(sdistrslt0,nodename=nodename,groupindex=groupindex,figname=figname+str(1),figsize=figsize,dpi=dpi,cex=cex,text=text,fade=fade,logscale=logscale)
    if prnt==True: print('obtain snowdist')
    for m in co(1,M):
        if prnt==True: print('\r'+str(m),'/'+str(M),sep='',end='')
        dhh1=np.asmatrix(hstresult[sprod('h',cc(τlist[m-1]+1,τlist[m]))])
        sdistrslt1=np.asmatrix(np.sqrt(np.array(snowdist(dhh0))**2+np.array(snowdist(dhh1))**2))
        pca4vis(sdistrslt1,nodename=nodename,groupindex=groupindex,figname=figname+str(m+1),figsize=figsize,dpi=dpi,cex=cex,text=text,fade=fade,logscale=logscale)
        dhh0=dhh1.copy()
        sdistrslt0=sdistrslt1.copy()
    if prnt==True: print('\n'+'end')    

        
def pca4vis4msg(sdistresult,nodename=None,groupindex=None,
           figname='temp',figsize=(1, 1),dpi=1,cex=1,text=1,fade=1,
           prnt=False): # size=(size of obs representation, size of text which represent obs index)

    from sklearn.decomposition import PCA 
    from mpl_toolkits import mplot3d
    if prnt==True: print('PCA start')
    pca=PCA(n_components=3) # PCA start 
    pca.fit(sdistresult) 
    pcarslt=pca.transform(sdistresult) # PCA end 
    if prnt==True: print('end')

    n=len(sdistresult)
    if groupindex==None: colors=[0]*n
    elif groupindex=='continuous': colors=cm.rainbow(np.linspace(1, 0, n))
    else: colors=np.array(groupindex)

    figsize=(15*figsize[0],10*figsize[1])
    dpi=200*dpi
    cex=200*cex
    text=15*text
    fade=fade
    
    Fig=plt.figure(figsize=figsize, dpi=dpi) # Make figure object 
    ax=plt.axes(projection='3d') # define type of axes: 3d plot 
    ax.scatter3D(pcarslt[:,0],pcarslt[:,1],pcarslt[:,2],s=cex,c=colors,alpha=fade) # drawing each obs by scatter in 3d axes   
    if prnt==True: print('labeling (observation-wise)')
    if nodename==None:
        for i in cc(1,n): 
            if prnt==True: print('\r'+str(i),'/'+str(n),sep='',end='')
            ax.text(pcarslt[i-1,0],pcarslt[i-1,1],pcarslt[i-1,2],'%s'% (str(i)), size=text, zorder=1,color='k') # numbering index of nodes 
        if prnt==True: print('\n'+'end')
    else: 
        for i in cc(1,n): 
            if prnt==True: print('\r'+str(i),'/'+str(n),sep='',end='')
            ax.text(pcarslt[i-1,0],pcarslt[i-1,1],pcarslt[i-1,2],'%s'% (nodename[i-1]), size=text, zorder=1,color='k') # numbering index of nodes 
        if prnt==True: print('\n'+'end')
            
    #####################################################
    lgndname=['Apr','Mar','Jun','Jul','Aug','Sep','Nov']
    lgndcol=['greenyellow','lime','green','darkgreen','darkolivegreen','olive','goldenrod']
    
    for g in co(0,len(lgndname)):
        ax.scatter3D([],[],c=lgndcol[g],s=150,alpha=fade,label=lgndname[g])
    ax.legend(loc="upper right", title="Month")
    Fig.savefig(figname+'.png')
    plt.close(Fig)

def pca4msvis4msg(hstresult,τlist,
              nodename=None,groupindex=None,
              figname='temp',figsize=(1, 1),dpi=1,cex=1,text=1,fade=1,
              prnt=False): # size=(size of obs representation, size of text which represent obs index)
    dhhlist=τlist.copy()
    sdistrslt=τlist.copy()
    M=len(τlist)
    dhh0=np.asmatrix(hstresult[sprod('h',cc(0,τlist[0]))])
    sdistrslt0=snowdist(dhh0)
    pca4vis(sdistrslt0,nodename=nodename,groupindex=groupindex,figname=figname+str(1),figsize=figsize,dpi=dpi,cex=cex,text=text,fade=fade)
    if prnt==True: print('obtain snowdist')
    for m in co(1,M):
        if prnt==True: print('\r'+str(m),'/'+str(M),sep='',end='')
        dhh1=np.asmatrix(hstresult[sprod('h',cc(τlist[m-1]+1,τlist[m]))])
        sdistrslt1=np.asmatrix(np.sqrt(np.array(snowdist(dhh0))**2+np.array(snowdist(dhh1))**2))
        pca4vis4msg(sdistrslt1,nodename=nodename,groupindex=groupindex,figname=figname+str(m+1),figsize=figsize,dpi=dpi,cex=cex,text=text,fade=fade)
        dhh0=dhh1.copy()
        sdistrslt0=sdistrslt1.copy()
    if prnt==True: print('\n'+'end')        
 
### 3. old functions

def Smat_old(f,ϵ,Edg,W=None):
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

def Smat2_old(f,ϵ,Edg,W=None):
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

def hst_old(f,Edg,τ,γ,rvsnow=False):
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

def hst2_old(f,Edg,τ,γ,rvsnow=False):
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

