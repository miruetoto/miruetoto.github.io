## load pckg
# listofpackages <- c("ADMM")
# newpackages <- listofpackages[!(listofpackages %in% installed.packages()[,"Package"])]
# if(length(newpackages)) install.packages(newpackages,repos='http://cran.us.r-project.org')
# library(listofpackages)
library(ADMM)
library(ggplot2)
library(tidyverse)

plot_all<-function(rx,tx){
i0<-which(names(rx)=='datetime')
j0<-which(names(tx)=='datetime')
rx[[i0]]<-as.POSIXct(rx[[i0]])
tx[[j0]]<-as.POSIXct(tx[[j0]])
I0<-length(rx)
J0<-length(tx)
for(i in 1:I0){
    gplt<-ggplot(data=rx,mapping=aes(x=datetime,y=rx[[i]]))+
       ggtitle(paste("rx_",i,":",names(rx)[i]))+
       theme(
         axis.title.x=element_blank(),
         axis.title.y=element_blank(),
         axis.text.y=element_text(family="Times",face="bold.italic",colour="blue"),
         axis.text.x=element_text(family="Times",face="bold.italic",colour="gray50"),
         plot.title=element_text(size=rel(1.5),lineheight=0.9,family="Times",face="bold.italic",colour="red")
        )
    if(class(rx[[i]])=='factor'){
        gplt<-gplt+geom_point(mapping=aes(col=rx[[i]]),size=0.2)+theme(legend.position="none")
    }else{
        gplt<-gplt+geom_line(col="gray60",lwd=0.5)+geom_point(size=0.2)
    }
    show(gplt)
}

for(j in 1:J0){
    gplt<-ggplot(data=tx,mapping=aes(x=datetime,y=tx[[j]]))+
       ggtitle(paste("tx_",j,":",names(tx)[j]))+
       theme(
         axis.title.x=element_blank(),
         axis.title.y=element_blank(),
         axis.text.y=element_text(family="Times",face="bold.italic",colour="blue"),
         axis.text.x=element_text(family="Times",face="bold.italic",colour="gray50"),
         plot.title=element_text(size=rel(1.5),lineheight=0.9,family="Times",face="bold.italic",colour="red")
        )
    gplt<-gplt+geom_line(col="gray60",lwd=0.5)+geom_point(size=0.2)
    show(gplt)
}
}

plot_pretty<-function(rx,tx,time=c(0,1),rxindex=NULL,txindex=NULL){

i0<-which(names(rx)=='datetime')
j0<-which(names(tx)=='datetime')
rx[[i0]]<-as.POSIXct(rx[[i0]])
tx[[j0]]<-as.POSIXct(tx[[j0]])
rxN<-dim(rx)[1] # rxN is # of obs in rx
txN<-dim(tx)[1] # txN is # of obs in tx
t1<-time[1]
t2<-time[2]
rx<-rx[(floor(rxN*t1)+1):floor(rxN*t2),]
tx<-tx[(floor(txN*t1)+1):floor(txN*t2),]

i=7 ## F.temp
gplt<-ggplot(data=rx,mapping=aes(x=datetime,y=rx[[i]]))+
       ggtitle(paste("rx_",i,":",names(rx)[i]))+
       theme(
         axis.title.x=element_blank(),
         axis.title.y=element_blank(),
         axis.text.y=element_text(family="Times",face="bold.italic",colour="blue"),
         axis.text.x=element_text(family="Times",face="bold.italic",colour="gray50"),
         plot.title=element_text(size=rel(1.5),lineheight=0.9,family="Times",face="bold.italic",colour="red")
        )
gplt<-gplt+ geom_line(col="gray60",lwd=0.5)+
            geom_point(mapping=aes(col=rx[[26]]),size=0.2)+guides(col=FALSE)+
            geom_rect(mapping=aes(x=NULL,y=NULL,
                                  xmin=datetime[1],xmax=datetime[length(datetime)],
                                  ymin=rx[[3]],ymax=rx[[3]],fill=rx[[26]]),alpha=1)+   
            geom_line(mapping=aes(x=datetime,y=rx[[3]]),col='gray60',lty=2)+
            theme(legend.title=element_text(face="italic",family="Times",colour="blue",size=14),
                  legend.text=element_text(face="italic",family="Times",colour="blue",size=10))+
            labs(fill="2 eva state")       
show(gplt)

i=23 ## F.fan.rpm
gplt<-ggplot(data=rx,mapping=aes(x=datetime,y=rx[[i]]))+
       ggtitle(paste("rx_",i,":",names(rx)[i]))+
       theme(
         axis.title.x=element_blank(),
         axis.title.y=element_blank(),
         axis.text.y=element_text(family="Times",face="bold.italic",colour="blue"),
         axis.text.x=element_text(family="Times",face="bold.italic",colour="gray50"),
         plot.title=element_text(size=rel(1.5),lineheight=0.9,family="Times",face="bold.italic",colour="red")
        )
gplt<-gplt+ geom_line(col="gray60",lwd=0.5)+
            geom_point(mapping=aes(col=rx[[26]]),size=0.2)+guides(col=FALSE)+
            geom_rect(mapping=aes(x=NULL,y=NULL,
                                  xmin=datetime[1],xmax=datetime[length(datetime)],
                                  ymin=0,ymax=0,fill=rx[[26]]),alpha=1)+   
            theme(legend.title=element_text(face="italic",family="Times",colour="blue",size=14),
                  legend.text=element_text(face="italic",family="Times",colour="blue",size=10))+
            labs(fill="2 eva state")         
show(gplt)

i=59 ## compressor.power
gplt<-ggplot(data=rx,mapping=aes(x=datetime,y=rx[[i]]))+
       ggtitle(paste("rx_",i,":",names(rx)[i]))+
       theme(
         axis.title.x=element_blank(),
         axis.title.y=element_blank(),
         axis.text.y=element_text(family="Times",face="bold.italic",colour="blue"),
         axis.text.x=element_text(family="Times",face="bold.italic",colour="gray50"),
         plot.title=element_text(size=rel(1.5),lineheight=0.9,family="Times",face="bold.italic",colour="red")
        )
gplt<-gplt+ geom_line(col="gray60",lwd=0.5)+
            geom_point(mapping=aes(col=rx[[26]]),size=0.2)+guides(col=FALSE)+
            geom_rect(mapping=aes(x=NULL,y=NULL,
                                  xmin=datetime[1],xmax=datetime[length(datetime)],
                                  ymin=0,ymax=0,fill=rx[[26]]),alpha=1)+   
            theme(legend.title=element_text(face="italic",family="Times",colour="blue",size=14),
                  legend.text=element_text(face="italic",family="Times",colour="blue",size=10))+
            labs(fill="2 eva state")          
show(gplt)


i=8 ## R.temp
gplt<-ggplot(data=rx,mapping=aes(x=datetime,y=rx[[i]]))+
       ggtitle(paste("rx_",i,":",names(rx)[i]))+
       theme(
         axis.title.x=element_blank(),
         axis.title.y=element_blank(),
         axis.text.y=element_text(family="Times",face="bold.italic",colour="blue"),
         axis.text.x=element_text(family="Times",face="bold.italic",colour="gray50"),
         plot.title=element_text(size=rel(1.5),lineheight=0.9,family="Times",face="bold.italic",colour="red")
        )
gplt<-gplt+ geom_line(col="gray60",lwd=0.5)+
            geom_point(mapping=aes(col=rx[[26]]),size=0.2)+guides(col=FALSE)+
            geom_rect(mapping=aes(x=NULL,y=NULL,
                                  xmin=datetime[1],xmax=datetime[length(datetime)],
                                  ymin=rx[[4]],ymax=rx[[4]],fill=rx[[26]]),alpha=1)+   
            geom_line(mapping=aes(x=datetime,y=rx[[4]]),col='gray60',lty=2)+
            theme(legend.title=element_text(face="italic",family="Times",colour="blue",size=14),
                  legend.text=element_text(face="italic",family="Times",colour="blue",size=10))+
            labs(fill="2 eva state")       
show(gplt)

i=24 ## R.fan.rpm
gplt<-ggplot(data=rx,mapping=aes(x=datetime,y=rx[[i]]))+
       ggtitle(paste("rx_",i,":",names(rx)[i]))+
       theme(
         axis.title.x=element_blank(),
         axis.title.y=element_blank(),
         axis.text.y=element_text(family="Times",face="bold.italic",colour="blue"),
         axis.text.x=element_text(family="Times",face="bold.italic",colour="gray50"),
         plot.title=element_text(size=rel(1.5),lineheight=0.9,family="Times",face="bold.italic",colour="red")
        )
gplt<-gplt+ geom_line(col="gray60",lwd=0.5)+
            geom_point(mapping=aes(col=rx[[26]]),size=0.2)+guides(col=FALSE)+
            geom_rect(mapping=aes(x=NULL,y=NULL,
                                  xmin=datetime[1],xmax=datetime[length(datetime)],
                                  ymin=0,ymax=0,fill=rx[[26]]),alpha=1)+   
            theme(legend.title=element_text(face="italic",family="Times",colour="blue",size=14),
                  legend.text=element_text(face="italic",family="Times",colour="blue",size=10))+
            labs(fill="2 eva state")         
show(gplt)

if(is.null(rxindex)-1){
for(i in 1:length(rxindex)){
    gplt<-ggplot(data=rx,mapping=aes(x=datetime,y=rx[[rxindex[i]]]))+
       ggtitle(paste("rx_",rxindex[i],":",names(rx)[rxindex[i]]))+
       theme(
         axis.title.x=element_blank(),
         axis.title.y=element_blank(),
         axis.text.y=element_text(family="Times",face="bold.italic",colour="blue"),
         axis.text.x=element_text(family="Times",face="bold.italic",colour="gray50"),
         plot.title=element_text(size=rel(1.5),lineheight=0.9,family="Times",face="bold.italic",colour="red")
        )
    if(class(rx[[rxindex[i]]])=='factor'){
        gplt<-gplt+geom_point(mapping=aes(col=rx[[rxindex[i]]]),size=0.2)+theme(legend.position="none")
    }else{
        gplt<-gplt+geom_line(col="gray60",lwd=0.5)+geom_point(size=0.2)
    }
    show(gplt)
}    
}

if(is.null(txindex)-1){
for(j in 1:length(txindex)){
    gplt<-ggplot(data=tx,mapping=aes(x=datetime,y=tx[[txindex[j]]]))+
       ggtitle(paste("tx_",txindex[j],":",names(tx)[txindex[j]]))+
       theme(
         axis.title.x=element_blank(),
         axis.title.y=element_blank(),
         axis.text.y=element_text(family="Times",face="bold.italic",colour="blue"),
         axis.text.x=element_text(family="Times",face="bold.italic",colour="gray50"),
         plot.title=element_text(size=rel(1.5),lineheight=0.9,family="Times",face="bold.italic",colour="red")
        )
    if(class(tx[[txindex[j]]])=='factor'){
        gplt<-gplt+geom_point(mapping=aes(col=tx[[txindex[j]]]),size=0.2)+theme(legend.position="none")
    }else{
        gplt<-gplt+geom_line(col="gray60",lwd=0.5)+geom_point(size=0.2)
    }
    show(gplt)
}    
}
}