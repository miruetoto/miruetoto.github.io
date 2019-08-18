pplot<-function(x,y,size=1,col=1,main="",mainsize=1,xlim=range(x),ylim=range(y),text.location=c(mean(x),quantile(y,0.1)),text.size=1,text="",type="l")
{
  library(ggplot2)
  data<-data.frame(x,y)
  if(type=="p"){
    result<-ggplot(data,aes(x=x,y=y))+
      geom_point(size=size,col=col,shape=21)+  
      ggtitle(main)+
      xlab("")+ylab("")+
      scale_x_continuous(limits = xlim)+    
      scale_y_continuous(limits = ylim)+
      theme_bw()+theme(panel.border=element_blank(),axis.line=element_line(colour="black"))+
      theme(axis.title.x=element_text(size=rel(1),lineheight=0.9,face="bold.italic"))+
      theme(axis.title.y=element_text(size=rel(1),lineheight=0.9,face="bold.italic"))+
      theme(plot.title=element_text(size=rel(mainsize),lineheight=0.9,face="bold.italic"))+
      theme(plot.margin = unit(c(0,3,0,0), "mm"))+
      annotate("text",x=text.location[1],y=text.location[2],size=2.5*text.size,fontface="bold.italic",label=text)
  }
  if (type=="l"){
    result<-ggplot(data,aes(x=x,y=y))+
      geom_line(size=size,col=col)+  
      ggtitle(main)+
      xlab("")+ylab("")+
      scale_x_continuous(limits = xlim)+    
      scale_y_continuous(limits = ylim)+
      theme_bw()+theme(panel.border=element_blank(),axis.line=element_line(colour="black"))+
      theme(axis.title.x=element_text(size=rel(1),lineheight=0.9,face="bold.italic"))+
      theme(axis.title.y=element_text(size=rel(1),lineheight=0.9,face="bold.italic"))+
      theme(plot.title=element_text(size=rel(mainsize),lineheight=0.9,face="bold.italic"))+
v
      annotate("text",x=text.location[1],y=text.location[2],size=2.5*text.size,fontface="bold.italic",label=text)
  }
  result
}

blank<-function(xlim=c(0,1),ylim=c(0,1),text.location=c(mean(xlim),mean(ylim)),text.size=1,text="")
{
  result<-ggplot(data.frame())+
    geom_point()+  
    xlab("")+ylab("")+
    scale_x_continuous(limits = xlim)+
    scale_y_continuous(limits = ylim)+
    theme_bw()+theme(panel.border=element_blank(),axis.line=element_line(colour="White"))+
    theme(axis.ticks=element_blank(),axis.text.y=element_blank())+
    theme(axis.ticks=element_blank(),axis.text.x=element_blank())+
    theme(panel.grid.major=element_blank(),panel.grid.minor=element_blank())+
    theme(plot.margin = unit(c(0,3,0,0), "mm"))+    
    annotate("text",x=text.location[1],y=text.location[2],size=4.5*text.size,fontface="bold.italic",label=text)
  result
}

bplot<-function(x,y,main="",mainsize=1,ylim=range(y))
{
  library(ggplot2)
  data<-data.frame(x,y)
  result<-ggplot(data,aes(x=x,y=y))+
    geom_boxplot()+  
    ggtitle(main)+
    xlab("")+ylab("")+
    scale_y_continuous(limits = ylim)+
    theme_bw()+theme(panel.border=element_blank(),axis.line=element_line(colour="black"))+
    theme(axis.title.x=element_text(size=rel(1),lineheight=0.9,face="bold.italic"))+
    theme(axis.title.y=element_text(size=rel(1),lineheight=0.9,face="bold.italic"))+
    theme(plot.margin = unit(c(0,3,0,0), "mm"))+    
    theme(plot.title=element_text(size=rel(mainsize),lineheight=0.9,face="bold.italic"))
  result
}
