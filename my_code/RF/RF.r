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
