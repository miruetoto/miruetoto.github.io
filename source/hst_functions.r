pkgs<-c(
    "kohonen",
    "dplyr",
    "ggplot2",
    "ggforce",
    "ggrepel",
    "igraph",
    "plot3D",
    "MBA"
    )
not_installed_packages <- pkgs[ (  pkgs %in% installed.packages()[,1]  ) == 0]
install.packages(not_installed_packages,repos="https://cran.rstudio.com/")
for(i in pkgs) library(i,character.only = T)

library(kohonen)
library(dplyr)
library(ggplot2)
library(ggforce)
library(ggrepel)

###

somplot<-function(V,hh,maxtau=dim(hh)[2]-1,gridxdim,gridydim,
  somsd=0.1,label=1:dim(hh)[1],col=1,
  legendposition="right",textsize=3){
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
           legend.position = legendposition)+
           geom_point(data = sompts,aes(x,y),alpha = 0.8,cex=5,col=col)+
           geom_text_repel(data=sompts,aes(x,y,label=V),cex=textsize,fontface=4)
p
}

friendship<-function(W){
    n<-dim(W)[1]
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
    par(mar=c(0.1,0.1,0.1,0.1))
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
    par(mar=c(0.1,0.1,0.1,0.1))
    plot(wc,gdf,
         vertex.frame.color="NA",
         vertex.shape="none",vertex.label.degree=-pi/2,
         edge.color=Ecol,edge.lty=Elty,edge.curved=Ecurved)
    #dev.off()
    wc
}

vis4mcu3d<-function(V,W,f,hh,maxtau){
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
    par(mar=c(0.1,0.1,0.1,0.1))
    ## scatter3d 
    scatter3D(gx,gy,gz,colvar=gz/max(gz),
              type='h',pch=19,bty='g',ticktype="detailed",
              xlab="",ylab="",zlab="",
              xlim=c(min(gx)*1.5,max(gx)*1.5),ylim=c(min(gy)*1.5,max(gy)*1.5),zlim=c(0,max(gz)*1.5),
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
    text3D(gx,gy,gz+100,label=V,add=TRUE,cex=0.8,font=3,adj=0.5,alpha=0.6,phi=40,theta=40)
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
    λ<-svdrslt$d
    Λ<-diag(λ)
    U<-svdrslt$u; 
    V<-svdrslt$v; 
    Ψ<-U
    ## reconstruction: L_tilde <- U%*%Lamb*t(V) or L_tilde <- Psi%*%Lamb*t(Psi)
    fbar<-as.vector(t(Ψ)%*%f) ## fhat is Fourier Transform of f. 
    list(λ=λ,Ψ=Ψ,fbar=fbar)
}

eigenplot<-function(gfftresult,title=""){
    library(latex2exp)
    λ<-gfftresult$λ
    egntb <- tibble(y=λ,x=(length(λ)):1)
    library(ggplot2)
    egnplt <- ggplot(aes(x,y), data=egntb) + theme_classic()+
            geom_point(aes(x,y),size=1) + geom_line(lty=3,col="gray60") +
            xlab("")+ylab(TeX("$\\lambda$"))+ggtitle(TeX(title))
    egnplt
}

specplot<-function(gfftresult,title=""){
    library(latex2exp)
    λ<-gfftresult$λ
    fhatabs<-abs(gfftresult$fbar)
    spectb <- tibble(y=fhatabs,x=λ)
    spcplt <- ggplot(aes(x,y), data=spectb) + theme_classic()+
            geom_segment(aes(x,y,xend=x,yend=y-y)) + 
            geom_point(size=1) + xlim(0,2.1)+
            xlab(TeX("$\\lambda$"))+ylab(TeX("$|\\bar{f}(\\lambda)|$"))+ggtitle(TeX(title))
    spcplt
}
decompose<-function(f,W,V=1:length(f),showingeigenvector=F){
    n<-length(f)
    gfftrslt<-gfft(f,W)
    eigenplt<-eigenplot(gfftrslt)+ylim(0,2)
    show(eigenplt)
    specplt<-specplot(gfftrslt)
    show(specplt)
    components<-rep(0,n*n);dim(components)<-c(n,n); components<-as_tibble(components)
    λinverse<-gfftrslt$λ[n:1]
    Ψ<-gfftrslt$Ψ
    n<-length(f)
    for(k in 1:n){
        components[[n-k+1]]<-as.vector(Ψ[,k]%*%t(Ψ[,k])%*%f)
    }
#     regcoef<-rep(0,n*n);dim(regcoef)<-c(n,n); regcoef<-data.frame(regcoef)
#     for(k in 1:n){
#         regcoef[[n-k+1]]<-as.vector(Ψ[,k]%*%t(Ψ[,k])%*%(f*0+1))
#     }
    componentsplt<-list()
    if(showingeigenvector==T){
        for(k in 1:n){
            fhat<-components[[k]]
            textalpha<-abs(fhat)/max(abs(fhat))
            textsize<-(textalpha/sd(textalpha)>1 & abs(fhat)>30)*2.0
            componentsplt[[k]]<-ggplot(data.frame(V=V,fhat=fhat),aes(1:n,fhat))+theme_classic()+
                            ylab("")+xlab("")+theme(axis.text.x = element_text(angle = 45, hjust = 1))+
                            geom_line(lty=2)+geom_point()+geom_hline(aes(yintercept=0),col=2,lty=3,lwd=0.5)+
                            #geom_label_repel(aes(label=1:n),fontface=4)+
                            geom_text_repel(aes(label=V),fontface=4,size=textsize,alpha=1)+
                            theme(axis.ticks.x=element_blank(),axis.text.x=element_blank())+
                            ggtitle(str_c("component ",k))
            show(componentsplt[[k]])
        }
    }
    names(components)<-1:n
    components$V<-factor(V,levels=V)
    rtn<-components %>% gather(1:n,key="eigenvectorindex",value="fhat")
    rtn$eigenvectorindex <-parse_number(rtn$eigenvectorindex)
    rtn$eigenvalue<-λinverse[rtn$eigenvectorindex]
    rtn
}

savedecomposeplots<-function(f,W,V=1:length(f),textsizethresh=30){
    n<-length(f)
    gfftrslt<-gfft(f,W)
    components<-rep(0,n*n);dim(components)<-c(n,n); components<-as_tibble(components)
    λinverse<-gfftrslt$λ[n:1]
    Ψ<-gfftrslt$Ψ
    n<-length(f)
    for(k in 1:n){
        components[[n-k+1]]<-as.vector(Ψ[,k]%*%t(Ψ[,k])%*%f)
    }
    componentsplt<-list()
    for(k in 1:n){
        fhat<-components[[k]]
        textalpha<-abs(fhat)/max(abs(fhat))
        textsize<-(textalpha/sd(textalpha)>1 & abs(fhat)>textsizethresh)*3
        componentsplt[[k]]<-ggplot(data.frame(V=V,fhat=fhat),aes(1:n,fhat))+
                            ylab("")+xlab("")+theme(axis.text.x = element_text(angle = 45, hjust = 1))+
                            geom_line(lty=2)+geom_point()+geom_hline(aes(yintercept=0),col=2,lty=3,lwd=0.5)+
                            geom_text_repel(aes(label=V),fontface=4,size=textsize,alpha=1)+
                            theme(axis.ticks.x=element_blank(),axis.text.x=element_blank())+ggtitle(str_c("component ",k))+theme_classic()
    }
    componentsplt
}

shumanplot<-function(f,W){
    library(plot3D)
    n<-length(f)
    z<-f
    xpred<-seq(min(x)-0.5,max(x)+0.5,length.out=50)
    ypred<-seq(min(y)-0.5,max(y)+0.5,length.out=50)
    xy<-expand.grid(x=xpred,y=ypred)
    fit<-lm(z~x+y)
    zpred <- matrix(predict(fit, newdata = xy),nrow = 50, ncol =50)*0
    fitpoints<-predict(fit)*0
    par(mar=c(0,0,0,0))
    scatter3D(x=x,y=y,z=z,xlim=c(min(x)-0.5,max(x)+0.5),ylim=c(min(y)-0.5,max(y)+0.5),col="black",
          pch=19,ticktype="detailed",
          xlab="",ylab="",zlab="",
          theta=60,phi=10,adj=0.1,d=3,
          lwd=2,lty=1,cex=0,
          surf = list(x = xpred, y = ypred, z = zpred,alpha=0.001,lwd=0.001,facets=NA,fit=fitpoints),
          colkey=FALSE,grid=TRUE,axes=FALSE,box=FALSE)
    scatter3D(x=x,y=y,z=z*0,add=TRUE,colkey=FALSE,cex=2,pch=20,col="black")
    expgx<-expand.grid(x,x)
    expgy<-expand.grid(y,y)
    expgz<-expgx[,1]*0
    Wvec<-as.vector(W)
    arrowindex<-which(Wvec>0)
    arrows3D(expgx[,1][arrowindex],expgy[,1][arrowindex],expgz[arrowindex],
         expgx[,2][arrowindex],expgy[,2][arrowindex],expgz[arrowindex],
         add=TRUE,
         lwd=1,lty=3,code=1,angle=0,alpha=0.5,col=1)
    text3D(x,y,z+sign(z+0.00001)*0.5,label=1:n,add=TRUE,font=4,col=1)
}
