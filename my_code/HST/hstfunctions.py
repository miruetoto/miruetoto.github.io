### 1. hst: calculation 
def hst1walk(f,W,u,b,binit,γ,p0): #supporting hst
    d=m2a(apply(W,'np.sum'))
    rtn=f.copy()
    n=len(rtn)
    # 1. f(u) <- f(u)+b : update current node 
    rtn[u]=rtn[u]+b
    # 2. check that: are there any nodes to which snow can flow from u. 
    Nu=np.where(W[u,:]>0)[1] ## Nu is np.array
    if len(Nu)==0: Uu=np.array([])
    else: Uu=Nu[list((np.where(rtn[Nu]<=rtn[u]))[0])]
    # 3. check Uu=emptyset 
    if len(Uu)==0: 
        v=a2s(np.random.choice(n, 1, p=p0))
        b=binit
    else:
        v=a2s(np.random.choice(list(Uu),1))
        b=b*γ
    return [rtn,b,v]

def hst(gdata,τ,b,γ=1): #samefunction with hst1realization except print
    from random import sample     
    vname=gdata[0]
    E=gdata[1]
    W=gdata[2]    
    f=gdata[3]
    n=len(f)
    binit=b
    d=m2a(apply(W,'np.sum'))
    p0=d/sum(d)
    u=a2s(np.random.choice(n, 1, p=p0))
    rtn=initpd("0",n=n,p=2,vname=['Nodename(=v)','h0'])
    rtn['Nodename(=v)']=vname
    rtn['h0']=f
    print('hst start (' +'τ='+str(τ)+', b='+str(b)+')')
    for ℓ in cc(1,τ): 
        print('\r'+str(ℓ)+'/'+str(τ),sep='',end='')
        Wtemp=W>init('u',(n,n))
        hstwalkrslt=hst1walk(f=rtn['h'+str(ℓ-1)],W=Wtemp,u=u,b=b,binit=binit,γ=γ,p0=p0)
        rtn['h'+str(ℓ)]=hstwalkrslt[0]
        b=hstwalkrslt[1]
        u=hstwalkrslt[2]
    print('\n'+'hst end')
    return rtn

# def ϵfallmat(hstresult): 
#     τ=int((hstresult.shape[1]-2)/3)
#     rtn=np.asmatrix(hstresult[sprod('ϵ fall',cc(0,τ-1))])
#     return rtn 
    
# def ϵstackmat(hstresult): 
#     τ=int((hstresult.shape[1]-2)/3)
#     rtn=np.asmatrix(hstresult[sprod('ϵ stack',cc(0,τ-1))])
#     return rtn 

def hhmat(hstresult):
    τ=int((hstresult.shape[1]-2))
    rtn=np.asmatrix(hstresult[sprod('h',cc(0,τ))])
    return rtn 

def L2dist(hhlike,prnt=False): #supporting snowdist, #hh:=n*p 
    hhlike=np.array(hhlike)
    n=len(hhlike)
    rtn=np.array(init('0',(n,n)))
    try: 
        rtn=np.sum((hhlike[:,np.newaxis,:]-hhlike[np.newaxis,:,:])**2,axis=-1)
    except MemoryError:
        if prnt==True: print('calculating snowdistance serially(due to lack of memory)')
        for i in co(0,n):
            rtn[i,:]=np.sum((hhlike[i,:]-hhlike[:,:])**2,axis=1)
            if prnt==True: print('\r'+str(i),'/'+str(n),sep='',end='')
        if prnt==True: print('\n'+'end')
    return np.asmatrix(rtn)

# def snowdist(hh,τmax=None,prnt=False): 
#     #hh=hhmat(hstresult)
#     if τmax==None: rtn=L2dist(hh,prnt=prnt)
#     else: rtn=L2dist(hh[:,0:(τmax+1)],prnt=prnt)
#     return rtn

def Sigma(hh,τmax=None,prnt=False): 
    #hh=hhmat(hstresult)
    if τmax==None: rtn=L2dist(hh,prnt=prnt)
    else: rtn=L2dist(hh[:,0:(τmax+1)],prnt=prnt)
    return rtn

# def Sigma(hstrslt,τmax=None):
#     hh=hhmat(hstrslt)
#     if τmax==None: 
#         Σtemp=hh*hh.T
#         rtn=Σtemp
#     else: 
#         Σtemp=hh[:,0:(τmax+1)]*hh[:,0:(τmax+1)].T
#         rtn=Σtemp
#     return rtn

def dist2W(dist,θ=1): 
    n=len(dist)
    rtn=init('0',(n,n))
    for i in co(0,n):
        for j in co(0,n):
            if i==j: rtn[i,j]=0
            else: rtn[i,j]=np.exp(-dist[i,j]**2/(2*θ**2))
    return rtn

# def degree(W):
#     return np.matrix(np.diag(m2a(apply(W,'np.sum'))))

def total_degree(W):
    return np.sum(m2a(apply(W,'np.sum')))

# def degree_rootinv(W):
#     return np.matrix(np.diag(np.sqrt(1/m2a(apply(W,'np.sum')))))

# # def Wtau(Σ,θ): 
# #     a=(θ**2)*2
# #     return transform(Σ,'dist2W')

# def decomp(gdataτ):
#     Wτ=gdataτ[2]
#     f=gdataτ[3]
#     n=Wτ.shape[0]
#     Dτ=degree(Wτ)
#     Dτ_rootinv=degree_rootinv(Wτ)
#     Lτ=Dτ-Wτ
#     Lτ_tilde=Dτ_rootinv*Lτ*Dτ_rootinv
    
#     (λ,Ψ)=np.linalg.eig(Lτ_tilde)
#     fdecomprlst=init('0',(n,n))
#     for i in co(0,n):
#         fdecomprlst[:,i]=Ψ[:,i]*Ψ[:,i].T*f
#     return [λ,fdecomprlst]


### 2. hst: visualization 
def datavis4ts(f,nodename=None,groupindex=None,
           figname='temp',figsize=(1,1),dpi=1,cex=1,
           text=None,fade=0.5):
    n=len(f)
    
    if groupindex==None: colors=[0]*n
    elif groupindex=='continuous': colors=cm.rainbow(np.linspace(1, 0, n))
    else: colors=np.array(groupindex)
    
    f=np.array(f)
    figsize=(10*figsize[0],6*figsize[1])
    dpi=150*dpi
    cex=50*cex
    if text!=None: text=10*text
    fade=fade
    
    Fig=plt.figure(figsize=figsize, dpi=dpi) # Make figure object 
    ax=plt.axes()
    plt.scatter(cc(1,n),f,c=colors,s=cex,alpha=fade)
    style=dict(size=text,color='k')
    
    if nodename==None:
        for i in cc(1,n): 
            if text!=None: ax.text(i,f[i-1],'%s'% str(i), **style) # numbering index of nodes 
        rtn=Fig 
    else: 
        for i in cc(1,n): 
            if text!=None: ax.text(i,f[i-1],'%s'% nodename[i-1], **style) # numbering index of nodes 
        rtn=Fig 
    rtn.savefig(figname+'.pdf')

def datavis4sct(v1,v2,nodename=None,groupindex=None,
           figname='temp',figsize=(1,1),dpi=1,cex=1,
           text=None,fade=0.5):
    n=len(v1)
    
    if groupindex==None: colors=[0]*n
    elif groupindex=='continuous': colors=cm.rainbow(np.linspace(1, 0, n))
    else: colors=np.array(groupindex)
    
    v1=np.array(v1)
    v2=np.array(v2)
    figsize=(10*figsize[0],6*figsize[1])
    dpi=150*dpi
    cex=50*cex
    if text!=None: text=10*text
    fade=fade
    
    Fig=plt.figure(figsize=figsize, dpi=dpi) # Make figure object 
    ax=plt.axes()
    plt.scatter(v1,v2,c=colors,s=cex,alpha=fade)
    style=dict(size=text,color='k')
    
    if nodename==None:
        for i in cc(1,n): 
            if text!=None: ax.text(v1[i-1],v2[i-1],'%s'% str(i), **style) # numbering index of nodes 
        rtn=Fig 
    else: 
        for i in cc(1,n): 
            if text!=None: ax.text(v1[i-1],v2[i-1],'%s'% nodename[i-1], **style) # numbering index of nodes 
        rtn=Fig 
    rtn.savefig(figname+'.pdf')
 
def pca4vis3d(Σ,nodename=None,groupindex=None,
           figname='temp',title=None,figsize=(1,1),dpi=1,cex=1,
           xlim=None,ylim=None,zlim=None,text=None,fade=0.5,
           prnt=False): # size=(size of obs representation, size of text which represent obs index)

    from sklearn.decomposition import PCA 
    from mpl_toolkits import mplot3d
    if prnt==True: print('PCA start')
    pca=PCA(n_components=3) # PCA start 
    n=Σ.shape[0]
    pca.fit(Σ) 
    pcarslt=pca.transform(Σ) # PCA end 
    if prnt==True: print('end')

    if groupindex==None: colors=['gray']*n
    elif groupindex=='continuous': colors=cm.rainbow(np.linspace(1, 0, n))
    else: colors=np.array(groupindex)
    
    figsize=(20*figsize[0],6*figsize[1])
    dpi=200*dpi
    cex=50*cex
    if text!=None: text=10*text
    fade=fade
    
    Fig=plt.figure(figsize=figsize, dpi=dpi)  # Make figure object 
    ax=plt.axes(projection='3d') # define type of axes: 3d plot 
    if title!=None: ax.text(0,0,zlim[1],title,fontsize=30)
    if xlim!=None: ax.set_xlim(xlim[0],xlim[1])
    if ylim!=None: ax.set_ylim(ylim[0],ylim[1])
    if zlim!=None: ax.set_zlim(zlim[0],zlim[1])
    ax.scatter3D(pcarslt[:,0],pcarslt[:,1],pcarslt[:,2],s=cex,c=colors,alpha=fade) # drawing each obs by scatter in 3d axes   
    ax.ticklabel_format(style='sci', axis='x',scilimits=(0,0))
    ax.ticklabel_format(style='sci', axis='y',scilimits=(0,0))
    ax.ticklabel_format(style='sci', axis='z',scilimits=(0,0))
    ax.xaxis.set_major_locator(plt.MaxNLocator(9))
    ax.yaxis.set_major_locator(plt.MaxNLocator(5))
    ax.zaxis.set_major_locator(plt.MaxNLocator(3))
    ax.w_xaxis.pane.fill = False
    ax.w_yaxis.pane.fill = False
    ax.w_zaxis.pane.fill = False
    if prnt==True: print('labeling (observation-wise)')
    if nodename==None:
        for i in cc(1,n): 
            if prnt==True: print('\r'+str(i),'/'+str(n),sep='',end='')
            if text!=None: ax.text(pcarslt[i-1,0],pcarslt[i-1,1],pcarslt[i-1,2],'%s'% (str(i)), size=text, zorder=1,color='k') # numbering index of nodes 
        if prnt==True: print('\n'+'end')
    else: 
        for i in cc(1,n): 
            if prnt==True: print('\r'+str(i),'/'+str(n),sep='',end='')
            if text!=None: ax.text(pcarslt[i-1,0],pcarslt[i-1,1],pcarslt[i-1,2],'%s'% (nodename[i-1]), size=text, zorder=1,color='k') # numbering index of nodes 
        if prnt==True: print('\n'+'end')
    Fig.savefig(figname+'.pdf')
    rtn=Fig
    
def pca4msvis3d(hstresult,τlist,
              nodename=None,groupindex=None,
              figname='temp',figsize=(1,1),dpi=1,cex=1,text=None,fade=1,
              prnt=False,logscale=(False,False,False)): # size=(size of obs representation, size of text which represent obs index)
    Σresult=τlist.copy()
    hh=hhmat(hstresult)
    M=len(τlist)
    from sklearn.decomposition import PCA 
    pca=PCA(n_components=3) # PCA start 
    pca.fit(Sigma(hh)) 
    pcarslt=pca.transform(Sigma(hh))
    x0=min(pcarslt[:,0]);x1=max(pcarslt[:,0])
    y0=min(pcarslt[:,1]);y1=max(pcarslt[:,1])
    z0=min(pcarslt[:,2]);z1=max(pcarslt[:,2])
    if prnt==True: print('obtain snowdist')
    for m in co(0,M):
        if prnt==True: print('\r'+str(m),'/'+str(M),sep='',end='')
        Σresult[m]=Sigma(hh,τmax=τlist[m])
        pca4vis3d(Σresult[m],nodename=nodename,groupindex=groupindex,
            title='τ='+str(τlist[m]),
            figname=figname+str(m+1),figsize=figsize,dpi=dpi,
            cex=cex,text=text,fade=fade,
            xlim=(x0,x1),ylim=(y0,y1),zlim=(z0,z1))      
    if prnt==True: print('\n'+'end')    

# def pca4vis2d(Σ,nodename=None,groupindex=None,
#             figname='temp',figsize=(1,1),dpi=1,cex=1,
#             text=None,fade=0.5,
#            prnt=False): # size=(size of obs representation, size of text which represent obs index)

#     from sklearn.decomposition import PCA 
#     from mpl_toolkits import mplot3d
#     if prnt==True: print('PCA start')
#     pca=PCA(n_components=2) # PCA start
#     # # start Get Lτ_tilde
#     # n=Wτ.shape[0]
#     # Dτ=degree(Wτ)
#     # Dτ_rootinv=degree_rootinv(Wτ)
#     # Lτ=Dτ-Wτ
#     # I=np.matrix(np.diag([1]*n))
#     # Lτ_tilde=Dτ_rootinv*Lτ*Dτ_rootinv
#     # # end
#     pca.fit(Σ) 
#     pcarslt=pca.transform(Σ) # PCA end 
#     if prnt==True: print('end')

#     if groupindex==None: colors=['gray']*n
#     elif groupindex=='continuous': colors=cm.rainbow(np.linspace(1, 0, n))
#     else: colors=np.array(groupindex)

#     figsize=(10*figsize[0],6*figsize[1])
#     Fig=plt.figure(figsize=figsize, dpi=dpi) # Make figure object 
#     dpi=150*dpi
#     cex=50*cex
#     if text!=None: text=10*text
#     fade=fade
    
#     Fig=plt.figure(figsize=figsize, dpi=dpi)  # Make figure object 
#     ax=plt.axes() # define type of axes: 3d plot 
    
#     ax.scatter(pcarslt[:,0],pcarslt[:,1],s=cex,c=colors,alpha=fade) # drawing each obs by scatter in 3d axes   

#     if prnt==True: print('labeling (observation-wise)')
#     if nodename==None:
#         for i in cc(1,n): 
#             if prnt==True: print('\r'+str(i),'/'+str(n),sep='',end='')
#             if text!=None: ax.text(pcarslt[i-1,0],pcarslt[i-1,1],'%s'% (str(i)), size=text, zorder=1,color='k') # numbering index of nodes 
#         if prnt==True: print('\n'+'end')
#     else: 
#         for i in cc(1,n): 
#             if prnt==True: print('\r'+str(i),'/'+str(n),sep='',end='')
#             if text!=None: ax.text(pcarslt[i-1,0],pcarslt[i-1,1],'%s'% (nodename[i-1]), size=text, zorder=1,color='k') # numbering index of nodes 
#         if prnt==True: print('\n'+'end')
#     Fig.savefig(figname+'.pdf')

# def pca4msvis2d(hstresult,τlist,
#               nodename=None,groupindex=None,
#               figname='temp',dpi=1,cex=1,text=1,fade=1,
#               prnt=False,logscale=(False,False,False)): # size=(size of obs representation, size of text which represent obs index)
#     dhhlist=τlist.copy()
#     sdistrslt=τlist.copy()
#     M=len(τlist)
#     dhh=np.asmatrix(hstresult[sprod('h',cc(0,τlist[0]))])
#     sdistrslt0=snowsim(norm_hh(dhh))
#     pca4vis2d(sdistrslt0,nodename=nodename,groupindex=groupindex,figname=figname+str(1),dpi=dpi,cex=cex,text=text,fade=fade)
#     if prnt==True: print('obtain snowdist')
#     for m in co(1,M):
#         if prnt==True: print('\r'+str(m),'/'+str(M),sep='',end='')
#         dhh=np.asmatrix(hstresult[sprod('h',cc(τlist[m-1]+1,τlist[m]))])
#         sdistrslt1=np.asmatrix(np.sqrt(np.array(sdistrslt0)**2+np.array(snowdist(dhh))**2))
#         pca4vis2d(sdistrslt1,nodename=nodename,groupindex=groupindex,figname=figname+str(m+1),dpi=dpi,cex=cex,text=text,fade=fade)
#         sdistrslt0=sdistrslt1.copy()
#     if prnt==True: print('\n'+'end')            
        
# def pca4vis4msg(sdistresult,nodename=None,groupindex=None,
#            figname='temp',figsize=(1, 1),dpi=1,cex=1,text=1,fade=1,
#            prnt=False): # size=(size of obs representation, size of text which represent obs index)

#     from sklearn.decomposition import PCA 
#     from mpl_toolkits import mplot3d
#     if prnt==True: print('PCA start')
#     pca=PCA(n_components=3) # PCA start 
#     pca.fit(sdistresult) 
#     pcarslt=pca.transform(sdistresult) # PCA end 
#     if prnt==True: print('end')

#     n=len(sdistresult)
#     if groupindex==None: colors=[0]*n
#     elif groupindex=='continuous': colors=cm.rainbow(np.linspace(1, 0, n))
#     else: colors=np.array(groupindex)

#     figsize=(15*figsize[0],10*figsize[1])
#     dpi=200*dpi
#     cex=200*cex
#     text=15*text
#     fade=fade
    
#     Fig=plt.figure(figsize=figsize, dpi=dpi) # Make figure object 
#     ax=plt.axes(projection='3d') # define type of axes: 3d plot 
#     ax.scatter3D(pcarslt[:,0],pcarslt[:,1],pcarslt[:,2],s=cex,c=colors,alpha=fade) # drawing each obs by scatter in 3d axes   
#     if prnt==True: print('labeling (observation-wise)')
#     if nodename==None:
#         for i in cc(1,n): 
#             if prnt==True: print('\r'+str(i),'/'+str(n),sep='',end='')
#             ax.text(pcarslt[i-1,0],pcarslt[i-1,1],pcarslt[i-1,2],'%s'% (str(i)), size=text, zorder=1,color='k') # numbering index of nodes 
#         if prnt==True: print('\n'+'end')
#     else: 
#         for i in cc(1,n): 
#             if prnt==True: print('\r'+str(i),'/'+str(n),sep='',end='')
#             ax.text(pcarslt[i-1,0],pcarslt[i-1,1],pcarslt[i-1,2],'%s'% (nodename[i-1]), size=text, zorder=1,color='k') # numbering index of nodes 
#         if prnt==True: print('\n'+'end')
            
#     #####################################################
#     lgndname=['Apr','Mar','Jun','Jul','Aug','Sep','Nov']
#     lgndcol=['greenyellow','lime','green','darkgreen','darkolivegreen','olive','goldenrod']
    
#     for g in co(0,len(lgndname)):
#         ax.scatter3D([],[],c=lgndcol[g],s=150,alpha=fade,label=lgndname[g])
#     ax.legend(loc="upper right", title="Month")
#     Fig.savefig(figname+'.png')
#     plt.close(Fig)

# def pca4msvis4msg(hstresult,τlist,
#               nodename=None,groupindex=None,
#               figname='temp',figsize=(1, 1),dpi=1,cex=1,text=1,fade=1,
#               prnt=False): # size=(size of obs representation, size of text which represent obs index)
#     dhhlist=τlist.copy()
#     sdistrslt=τlist.copy()
#     M=len(τlist)
#     dhh0=np.asmatrix(hstresult[sprod('h',cc(0,τlist[0]))])
#     sdistrslt0=snowdist(dhh0)
#     pca4vis(sdistrslt0,nodename=nodename,groupindex=groupindex,figname=figname+str(1),figsize=figsize,dpi=dpi,cex=cex,text=text,fade=fade)
#     if prnt==True: print('obtain snowdist')
#     for m in co(1,M):
#         if prnt==True: print('\r'+str(m),'/'+str(M),sep='',end='')
#         dhh1=np.asmatrix(hstresult[sprod('h',cc(τlist[m-1]+1,τlist[m]))])
#         sdistrslt1=np.asmatrix(np.sqrt(np.array(snowdist(dhh0))**2+np.array(snowdist(dhh1))**2))
#         pca4vis4msg(sdistrslt1,nodename=nodename,groupindex=groupindex,figname=figname+str(m+1),figsize=figsize,dpi=dpi,cex=cex,text=text,fade=fade)
#         dhh0=dhh1.copy()
#         sdistrslt0=sdistrslt1.copy()
#     if prnt==True: print('\n'+'end')        
 

