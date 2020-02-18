library(tidyverse)
library(lubridate)

cleaningvname<-function(dfdata){
    names(dfdata)<-str_replace_all(names(dfdata),"[.]","_")
    dfdata
}
