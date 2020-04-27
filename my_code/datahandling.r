###########################################################################
###########################################################################
###########################################################################

pkgs<-c(
	"tidyverse",
	"lubridate",
	"stringr",
	"forcats",
	"ggplot2",
	"gridExtra",
	"latex2exp"
	)
not_installed_packages <- pkgs[ (  pkgs %in% installed.packages()[,1]  ) == 0]
install.packages(not_installed_packages,repos="https://cran.rstudio.com/")
for(i in pkgs) library(i,character.only = T)

###########################################################################
###########################################################################
###########################################################################

### funstions such that length of funtions names = 3
# clv is clean variable name 
clv<-function(dfdata){
  names(dfdata)<-str_replace_all(names(dfdata),"[(]","")
  names(dfdata)<-str_replace_all(names(dfdata),"[)]","")
  names(dfdata)<-str_replace_all(names(dfdata),"[|]","")
  names(dfdata)<-str_replace_all(names(dfdata),"[/]","")
  names(dfdata)<-str_replace_all(names(dfdata),"[<]","")
  names(dfdata)<-str_replace_all(names(dfdata),"[_]","")
  names(dfdata)<-str_replace_all(names(dfdata),"[\\[]","")
  names(dfdata)<-str_replace_all(names(dfdata),"[\\]]","")
  names(dfdata)<-str_replace_all(names(dfdata),"[-]","")
  names(dfdata)<-str_replace_all(names(dfdata),"[.]","")
  names(dfdata)<-str_replace_all(names(dfdata),"[ ]","")
  dfdata
}

# len is length
len<-function(data){
	length(data)
}

# print varialbe names
ids<-function(data){
	cat(str_c(str_c('[[',str_c(1:length(data)),']] ','\'',names(data),'\''),collapse='\n'))
}

# init tibble data 
itb<-function(n,p=1,vname=str_c('X',1:p)){
  tb<-rnorm(n*p)
  dim(tb)<-c(n,p)
  colnames(tb)<-vname
  tb<-as_tibble(tb)
  tb
}

# minmaxscaling
mms<-function(vector,range=c(0,1)){
	vectorshift<-vector-min(vector)+range[1]
	vectorshift/max(vectorshift)*range[2]
}

###########################################################################
###########################################################################
###########################################################################

### funstions such that length of funtions names = 5 
# make product space : sprod in python 
# sprod<-function(index){

# }

###########################################################################
###########################################################################
###########################################################################

### ggplots
myggplot<-function(...){
  ggplot(...)+theme(
         axis.title.x=element_blank(),
         axis.title.y=element_blank(),
         axis.text.y=element_text(family="Times",face="bold.italic",colour="blue"),
         axis.text.x=element_text(family="Times",face="bold.italic",colour="gray50"),
         plot.title=element_text(size=rel(1.5),lineheight=0.9,family="Times",face="bold.italic",colour="black"),
         legend.title=element_text(face="italic",family="Times",colour="blue",size=14),
         legend.text=element_text(face="italic",family="Times",colour="blue",size=10)
        )
}
