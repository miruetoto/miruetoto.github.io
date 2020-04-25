library(tidyverse)
library(lubridate)
library(stringr)
library(forcats)

### 3 
# clv is clean variable name 
clv<-function(dfdata){
    names(dfdata)<-str_replace_all(names(dfdata),"[.]","_")
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
itb<-function(typ,n,p=1,vname=None){
    if vname==None: vname=sprod('X',cc(1,p))
    val=init(typ,(n,p))
    rtn=pd.DataFrame(val)
    rtn.columns=vname
    return rtn   	
}

# minmaxscaling
mms<-function(vector,range=c(0,1)){
	vectorshift<-vector-min(vector)+range[1]
	vectorshift/max(vectorshift)*range[2]
}

### 5
# make product space : sprod in python 
sprod<-function(index){

}