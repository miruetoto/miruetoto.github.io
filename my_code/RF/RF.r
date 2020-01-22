## load pckg
# listofpackages <- c("ADMM")
# newpackages <- listofpackages[!(listofpackages %in% installed.packages()[,"Package"])]
# if(length(newpackages)) install.packages(newpackages,repos='http://cran.us.r-project.org')
# library(listofpackages)
library(ADMM)
library(ggplot2)
library(tidyverse)
library(plotly)

plot_all<-function(rx,tx=NULL){
if(is.null(tx)-1){
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
    show(gplt); suppressMessages(ggsave(paste("Figtemp/plotall/plotall_rx",i,"_",names(rx)[i],".png",sep=""),gplt))
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
    show(gplt); suppressMessages(ggsave(paste("Figtemp/plotall/plotall_tx",j,"_",names(tx)[j],".png",sep=""),gplt))
  }
}else{
  i0<-which(names(rx)=='datetime')
  rx[[i0]]<-as.POSIXct(rx[[i0]])
  I0<-length(rx)
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
    show(gplt); suppressMessages(ggsave(paste("Figtemp/plotall/plotall_rx",i,"_",names(rx)[i],".png",sep=""),gplt))
  }
}
}

plot_pretty<-function(rx,tx=NULL,time=c(0,1),rxindex=NULL,txindex=NULL){
if(is.null(tx)) tx=rx
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
show(gplt); suppressMessages(ggsave("Figtemp/plotpretty/plotpretty_F.temp.png",gplt))

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
show(gplt); suppressMessages(ggsave("Figtemp/plotpretty/plotpretty_F.fan.rpm.png",gplt))

i=54 ## compressor.cooling.power
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
show(gplt); suppressMessages(ggsave("Figtemp/plotpretty/plotpretty_compressor.cooling.power.png",gplt))


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
show(gplt); suppressMessages(ggsave("Figtemp/plotpretty/plotpretty_compressor.power.png",gplt))


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
show(gplt); suppressMessages(ggsave("Figtemp/plotpretty/plotpretty_R.temp.png",gplt))

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
show(gplt); suppressMessages(ggsave("Figtemp/plotpretty/plotpretty_R.fan.rpm.png",gplt))

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

plotj<-function(data,j,time=c(0,1)){
j0<-which(names(data)=='datetime')
data[[j0]]<-as.POSIXct(data[[j0]])
N<-dim(data)[1] # N is # of obs in data
t1<-time[1]
t2<-time[2]
data<-data[(floor(N*t1)+1):floor(N*t2),]

gplt<-ggplot(data=data,mapping=aes(x=datetime,y=data[[j]]))+
       ggtitle(paste("var_",j,":",names(data)[j]))+
       theme(
         axis.title.x=element_blank(),
         axis.title.y=element_blank(),
         axis.text.y=element_text(family="Times",face="bold.italic",colour="blue"),
         axis.text.x=element_text(family="Times",face="bold.italic",colour="gray50"),
         plot.title=element_text(size=rel(1.5),lineheight=0.9,family="Times",face="bold.italic",colour="red")
        )
if(class(data[[j]])=='factor'){
        gplt<-gplt+geom_point(mapping=aes(col=data[[j]]),size=0.2)+theme(legend.position="none")
  }else{
        gplt<-gplt+geom_line(col="gray60",lwd=0.5)+geom_point(size=0.2)
  }
suppressMessages(ggsave(paste("Figtemp/plotj/",names(data)[j],".png",sep=""),gplt))
gplt
}
