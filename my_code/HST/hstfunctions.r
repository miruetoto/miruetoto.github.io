library(kohonen)
library(dplyr)
library(ggplot2)
library(ggforce)
library(ggrepel)

somplot<-function(V,hh,maxtau=dim(hh)[2]-1,gridxdim,gridydim,somsd=0.1,label=1:dim(hh)[1]){
set.seed(777)
#library(kohonen)
hh<-hh[,1:(maxtau+1)]
somrslt <- som(hh, somgrid(gridxdim,gridydim,"hexagonal"))
#library(dplyr)
somgrd <- somrslt[[4]]$pts %>%
  as_tibble %>% 
  mutate(id=row_number())

sompts <- tibble(id = somrslt[[2]],
                  dist = somrslt[[3]])
sompts <- sompts %>% left_join(somgrd,by="id")
sompts$x<-sompts$x+rnorm(dim(hh)[1])*somsd
sompts$y<-sompts$y+rnorm(dim(hh)[1])*somsd
ndist <- unit.distances(somrslt$grid)
cddist <- as.matrix(object.distances(somrslt, type = "codes"))
cddist[abs(ndist - 1) > .001] <- NA
neigh.dists <- colMeans(cddist, na.rm = TRUE)
somgrd <- somgrd %>% mutate(dist=neigh.dists)
#library(ggplot2)
#library(ggforce) # for geom_circle function
#library(ggrepel) # for geom_text_repel
p <- somgrd %>% 
     ggplot(aes(x0=x,y0=y))+ggforce::geom_circle(aes(r=0.5,fill=dist))+
     scale_fill_gradient(low="white",high="gray25",name="Distance")+
     theme(panel.background = element_blank(),
           axis.ticks = element_blank(),
           panel.grid = element_blank(),
           axis.text = element_blank(),
           axis.title = element_blank(),
           legend.position = "right")+
           geom_point(data = sompts,aes(x,y),alpha = 0.8,cex=3)+
           geom_text_repel(data=sompts,aes(x,y,label=V),cex=3)
p
}

friendship<-function(W){
    frnd_ship<-c()
    for(i in 1:n){
        for(j in 1:n){
            frnd_ship[(i-1)*n+j]<-W[i,j]
        }
    }
    frnd_ship
}

vis4igraph<-function(V,W,
                     Vsize=1,Vcol="#FFB3FFFF",Vfontsize=1,Vfontcol="gray40",Vfontype=4,
                     Elwd=1,Elty=1,Ecol="gray80",Ecurved=0.3,Earrowsize=1){
    library(igraph)
    
    ## 1. define friendship 
    frnd_ship<-friendship(W)
    
    ## 2. define relations
    relations<-expand.grid(from=V, to=V)
    relations<-cbind(relations,frnd_ship)
    
    ## 3. make gdf and weight
    gdf<-graph_from_data_frame(relations[frnd_ship>0,],directed=TRUE,vertices=V)
    wght<-frnd_ship[frnd_ship>0]
    
    ## 4. set param 4 gdf visualization 
    V(gdf)$label.cex<-Vfontsize*0.7 # 글씨크기
    V(gdf)$label.font=Vfontype # 글꼴 
    V(gdf)$label.color<-Vfontcol # 글씨색 
    E(gdf)$arrow.size<-wght*Earrowsize*0.2 # 화살표의 끝모양(세모) 크기 
    E(gdf)$width=wght*Elwd # 화살표선굵기 
    set.seed(7777)
    ## 5. plot result 
    #png(paste("ntwksinit.png",sep=""),res=rs, width=wdth, height=hght)
    #plot(wc,gdf,edge.color="gray80",edge.lty=1,vertex.color=log(f),vertex.shape="none",edge.curved=0.1,edge.alpha=0.2)
    plot(gdf,
         vertex.size=Vsize*10, vertex.frame.color="NA",vertex.color=Vcol,
         vertex.shape="circle",vertex.label.degree=-pi/2,
         edge.color=Ecol,edge.lty=Elty,edge.curved=Ecurved)
    #dev.off()
}

vis4wc<-function(V,W,step=30,
                 Vfontsize=1,Vfontcol="gray40",Vfontype=4,
                 Elwd=1,Elty=1,Ecol="gray80",Ecurved=0.3,Earrowsize=1){
    library(igraph)
    
    ## 1. define friendship 
    frnd_ship<-friendship(W)
    
    ## 2. define relations
    relations<-expand.grid(from=V, to=V)
    relations<-cbind(relations,frnd_ship)
    
    ## 3. make gdf and weight
    gdf<-graph_from_data_frame(relations[frnd_ship>0,],directed=TRUE,vertices=V)
    wght<-frnd_ship[frnd_ship>0]
    
    ## 4. set param 4 gdf visualization 
    V(gdf)$label.cex<-Vfontsize*0.7 # 글씨크기
    V(gdf)$label.font=Vfontype # 글꼴 
    V(gdf)$label.color<-Vfontcol # 글씨색 
    E(gdf)$arrow.size<-wght*Earrowsize*0.2 # 화살표의 끝모양(세모) 크기 
    E(gdf)$width=wght*Elwd # 화살표선굵기 
    set.seed(7777)
    wc<-walktrap.community(gdf,weights=wght,step=step)
    ## 5. plot result 
    #png(paste("ntwksinit.png",sep=""),res=rs, width=wdth, height=hght)
    #plot(wc,gdf,edge.color="gray80",edge.lty=1,vertex.color=log(f),vertex.shape="none",edge.curved=0.1,edge.alpha=0.2)
    plot(wc,gdf,
         vertex.frame.color="NA",
         vertex.shape="none",vertex.label.degree=-pi/2,
         edge.color=Ecol,edge.lty=Elty,edge.curved=Ecurved)
    #dev.off()
}

vis4graph3d<-function(V,W,f,hh,maxtau){
    library(fields)
    library(fields)
    sdist<-rdist(hh[,1:(maxtau+1)])
    ## pca
    pcarslt<-princomp(sdist)
    gx<-pcarslt$scores[,1]
    gy<-pcarslt$scores[,2]
    gz<-f
    ## load graph lib
    library(plot3D)
    library(MBA)
    #png("verytemp.png",res=300, width=2000, height=2000)
    par(mar=c(1,1,1,1))
    ## scatter3d 
    scatter3D(gx,gy,gz,colvar=gz/max(gz),
              type='h',pch=19,bty='g',ticktype="detailed",
              xlab="",ylab="",zlab="",
              xlim=c(min(gx)*1.5,max(gx)*1.5),ylim=c(min(gy)*1.5,max(gy)*1.5),zlim=c(0,3000),
              theta=15,phi=30,adj=0.1,d=3,
              lwd=2,lty=3,cex=1,
              colkey=FALSE,grid=TRUE)
    ## draw Edg 
    expgx<-expand.grid(gx,gx)
    expgy<-expand.grid(gy,gy)
    expgz<-expgx[,1]*0
    Wvec<-as.vector(W)
    arrowcol<-gray(Wvec*0.01)
    arrowindex<-which(Wvec>0)
    lines3D(expgx[,1][arrowindex],expgy[,1][arrowindex],expgz[arrowindex]
         ,expgx[,2][arrowindex],expgy[,2][arrowindex],expgz[arrowindex],add=TRUE,
         col="gray60",lwd=exp(1+Wvec[arrowindex])*3,lty=1,alpha=0.1)
    ## labeling
    text3D(gx,gy,gz+100,label=V,add=TRUE,cex=0.8,font=3,adj=0.5,alpha=0.6)
    #dev.off()   
}


degree<-function(W){
    diag(apply(W,1,sum))
}

degree_rootinv<-function(W){
    d<-apply(W,1,sum)
    drootinv<-d
    drootinv[d>0.01]<-sqrt(1/d[d>0.01])
    diag(drootinv)
}
gfft<-function(f,W){
    n<-length(f)
    D<-degree(W)
    D_rootinv<-degree_rootinv(W)
    L<-D-W
    L_tilde<-D_rootinv%*%L%*%D_rootinv
    svdrslt<-svd(L_tilde)
    lamb<-svdrslt$d
    Lamb<-diag(lamb)
    U<-svdrslt$u; 
    V<-svdrslt$v; 
    Psi<-V
    ## reconstruction: L_tilde <- U%*%Lamb*t(V) or L_tilde <- Psi%*%Lamb*t(Psi)
    fhat<-as.vector(Psi%*%f) ## fhat is Fourier Transform of f. 
    list(lamb=lamb,fhat=fhat)
}

specplot<-function(gfftresult,filename="temp.pdf",title=""){
    library(latex2exp)
    lamb=gfftresult[[1]]
    fhatabs=abs(gfftresult[[2]])
    specdf <- data.frame(y=fhatabs,x=lamb)
    library(ggplot2)
    specplot <- ggplot(aes(x,y), data=specdf) + 
            geom_hline(aes(yintercept=0)) +
            geom_segment(aes(x,y,xend=x,yend=y-y)) + 
            geom_point(aes(x,y),size=1.5) + xlim(0,2)+
            xlab(TeX("$\\lambda$"))+ylab(TeX("$\\hat{f}(\\lambda)$"))+ggtitle(title)
    ggsave(filename,plot=specplot,dpi=300, width=5, height=2.5)
    show(specplot)
    specplot
}



decompose<-function(f,W){
    n<-length(f)
    D<-degree(W)
    D_rootinv<-degree_rootinv(W)
    L<-D-W
    L_tilde<-D_rootinv%*%L%*%D_rootinv
    svdrslt<-svd(L_tilde)
    lamb<-svdrslt$d
    
    U<-svdrslt$u; 
    V<-svdrslt$v; 
    Psi<-V
    ## reconstruction: L_tilde <- U%*%Lamb*t(V) or L_tilde <- Psi%*%Lamb*t(Psi)
    dcmp<-rep(0,n*n);dim(dcmp)<-c(n,n)
    for(k in 1:n) dcmp[,k]<-as.vector(Psi[,k]%*%t(Psi[,k])%*%f)
    list(lamb=lamb,decomp=dcmp)
}