library(ggplot2)
library(gridExtra)
library(latex2exp)

myggplot<-function(data){
  ggplot(data)+theme(
         axis.title.x=element_blank(),
         axis.title.y=element_blank(),
         axis.text.y=element_text(family="Times",face="bold.italic",colour="blue"),
         axis.text.x=element_text(family="Times",face="bold.italic",colour="gray50"),
         plot.title=element_text(size=rel(1.5),lineheight=0.9,family="Times",face="bold.italic",colour="red"),
         legend.title=element_text(face="italic",family="Times",colour="blue",size=14),
         legend.text=element_text(face="italic",family="Times",colour="blue",size=10)
        )
}
