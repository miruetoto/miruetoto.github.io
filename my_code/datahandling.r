library(tidyverse)
library(lubridate)
library(stringr)
library(forcats)

cleaningvname<-function(dfdata){
    names(dfdata)<-str_replace_all(names(dfdata),"[.]","_")
    dfdata
}
