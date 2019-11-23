### 1. hst: calculation 
def Ehst(gdata,τ,b,esb=5):
    print('Ehst start (' +'τ='+str(τ)+', b='+str(b)+')')
    rtn=hst1realization(gdata,τ=τ,b=b)
    hstrslt4hh=np.apply_along_axis(
        lambda inpt: np.array(hhmat(hst1realization(gdata,τ=τ,b=b))),
        -1,np.asmatrix(cc(2,esb)).T)
    hstTemp=np.apply_along_axis(np.sum,0,hstrslt4hh)
    print('\n'+'Ehst end')
    rtn.iloc[:,1:(τ+2)]=(hstTemp+rtn.iloc[:,1:(τ+2)])/esb
    return rtn

def hst1walk(f,Edg,b,u): #supporting hst
    n=len(f)
    nextf=f.copy()
    nextu=u
    N_u=list(np.where(Edg[u,:]==1)[1])
    from random import sample
    if len(N_u)==0: 
        nextu=sample(list(co(0,n)),1)[0]
    else: 
        v=N_u[sample(list(co(0,len(N_u))),1)[0]]
        if nextf[u]<nextf[v]: 
            nextf[u]=nextf[u]+2*b 
            nextu=u #sample(list(co(0,n)),1)[0]
        else: 
            nextf[v]=nextf[v]+b 
            nextu=v
    return [nextf,nextu]

def hst1realization(gdata,τ,b): 
    vname=gdata[0]
    f=gdata[1]
    Edg=gdata[2]    
    n=len(f)
    rtn=initpd("0",n=n,p=2,vname=['Nodename(=v)','h0'])
    rtn['Nodename(=v)']=vname
    rtn['h0']=f
    from random import sample 
    u=sample(list(co(0,n)),1)[0]
    for ℓ in cc(1,τ): 
        #print('\r'+str(ℓ)+'/'+str(τ),sep='',end='')
        Edgtemp=init('0',(n,n))
        while np.sum(Edgtemp)==0: 
            Edgtemp=(init('u',(n,n))<Edg)*1
        hst1walkrslt=hst1walk(rtn['h'+str(ℓ-1)],Edg=Edgtemp,b=b,u=u)
        rtn['h'+str(ℓ)]=hst1walkrslt[0]
        u=hst1walkrslt[1]
    print("■",sep='',end='')
    return rtn

def hst(gdata,τ,b): #samefunction with hst1realization except print
    vname=gdata[0]
    f=gdata[1]
    Edg=gdata[2]    
    n=len(f)
    rtn=initpd("0",n=n,p=2,vname=['Nodename(=v)','h0'])
    rtn['Nodename(=v)']=vname
    rtn['h0']=f
    from random import sample 
    u=sample(list(co(0,n)),1)[0]
    print('hst start (' +'τ='+str(τ)+', b='+str(b)+')')
    for ℓ in cc(1,τ): 
        print('\r'+str(ℓ)+'/'+str(τ),sep='',end='')
        Edgtemp=init('0',(n,n))
        while np.sum(Edgtemp)==0: 
            Edgtemp=(init('u',(n,n))<Edg)*1
        hst1walkrslt=hst1walk(rtn['h'+str(ℓ-1)],Edg=Edgtemp,b=b,u=u)
        rtn['h'+str(ℓ)]=hst1walkrslt[0]
        u=hst1walkrslt[1]
    print('\n'+'hst end')
    return rtn

def hhmat(hstresult):
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
    #hh=hhmat(hstresult)
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

def L2dist(hhlike,prnt=False): #supporting snowdist, #hh:=n*p 
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
           prnt=False): # size=(size of obs representation, size of text which represent obs index)

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
    dhh=np.asmatrix(hstresult[sprod('h',cc(0,τlist[0]))])
    sdistrslt0=snowdist(dhh)
    pca4vis(sdistrslt0,nodename=nodename,groupindex=groupindex,figname=figname+str(1),figsize=figsize,dpi=dpi,cex=cex,text=text,fade=fade)
    if prnt==True: print('obtain snowdist')
    for m in co(1,M):
        if prnt==True: print('\r'+str(m),'/'+str(M),sep='',end='')
        dhh=np.asmatrix(hstresult[sprod('h',cc(τlist[m-1]+1,τlist[m]))])
        sdistrslt1=np.asmatrix(np.sqrt(np.array(sdistrslt0)**2+np.array(snowdist(dhh))**2))
        pca4vis(sdistrslt1,nodename=nodename,groupindex=groupindex,figname=figname+str(m+1),figsize=figsize,dpi=dpi,cex=cex,text=text,fade=fade)
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


def hst1old(f,Edg,b,γ): #supporting hst
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
    rtn=f.copy()
    ##i=1
    ϵ=init('u',1)[0]*b
    iter=1
    while True:
        # 3. f(u) <- f(u)+ϵ
        rtn[u]=rtn[u]+ϵ*(γ**iter)
        # 4. choose v \in N_u such that f(v) \leq f(u)
        N_u=list(np.where(Edg[u,:]==1)[1])
        stop_criterion=sum(rtn[N_u]<=rtn[u]) # if stop_criterion=0, then we should stop. 
        if stop_criterion==0: break;
        if iter>500: break;
        else: u=N_u[sample(list(np.where(rtn[N_u]<=rtn[u])[0]),1)[0]]
        iter=iter+1
    # 5. u <- v and repeat 3-4 until {v: v \in N_i & f(v) \leq f(u)}=\emptyset 
    return rtn

