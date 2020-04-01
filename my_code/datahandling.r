library(tidyverse)
library(lubridate)
library(stringr)
library(forcats)

# clv is clean variable name 
clv<-function(dfdata){
    names(dfdata)<-str_replace_all(names(dfdata),"[.]","_")
    dfdata
}

# mms is minmaxsacling
mms<-function(vector,range=c(0,1)){
	vectorshift<-vector-min(vector)+range[1]
	vectorshift/max(vectorshift)*range[2]
}

# len is length
len<-function(data){
	length(data)
}

ids<-function(data){
	print(str_c(str_c(' [[',str_c(1:length(data)),']]',names(data)),collapse=', '))
}

