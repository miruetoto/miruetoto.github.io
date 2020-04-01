library(tidyverse)
library(lubridate)
library(stringr)
library(forcats)

cleanvname<-function(dfdata){
    names(dfdata)<-str_replace_all(names(dfdata),"[.]","_")
    dfdata
}

minmaxsacling<-function(vector,range=c(0,1)){
	vectorshift<-vector-min(vector)+range[1]
	vectorshift/max(vectorshift)*range[2]
}

ln<-function(data){
	length(data)
}

