library(stringr)
formulatingprob_stackedwild_1to29<-function(data,presentindex){
    presentstate<-data[presentindex,1:3]
    paststate<-presentstate*0
    ## case 1 
    paststate$finishedspin<-presentstate$finishedspin-1
    paststate$remainedspin<-presentstate$remainedspin+1
    paststate$stackedwild<-presentstate$stackedwild
    action<-"DC39"
    pastindex<-which(data$finishedspin==paststate$finishedspin & data$remainedspin==paststate$remainedspin & data$stackedwild==paststate$stackedwild)
    if (length(pastindex)>0){
        if(paststate$remainedspin>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 2
    paststate$finishedspin<-presentstate$finishedspin-1
    paststate$remainedspin<-presentstate$remainedspin-2
    paststate$stackedwild<-presentstate$stackedwild
    action<-"DC40"
    pastindex<-which(data$finishedspin==paststate$finishedspin & data$remainedspin==paststate$remainedspin & data$stackedwild==paststate$stackedwild)
    if (length(pastindex)>0){
        if(paststate$remainedspin>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 3
    paststate$finishedspin<-presentstate$finishedspin-1
    paststate$remainedspin<-presentstate$remainedspin-4
    paststate$stackedwild<-presentstate$stackedwild
    action<-"DC41"
    pastindex<-which(data$finishedspin==paststate$finishedspin & data$remainedspin==paststate$remainedspin & data$stackedwild==paststate$stackedwild)
    if (length(pastindex)>0){
        if(paststate$remainedspin>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 4
    paststate$finishedspin<-presentstate$finishedspin-1
    paststate$remainedspin<-presentstate$remainedspin+1
    paststate$stackedwild<-presentstate$stackedwild-1
    action<-"DC42"
    pastindex<-which(data$finishedspin==paststate$finishedspin & data$remainedspin==paststate$remainedspin & data$stackedwild==paststate$stackedwild)
    if (length(pastindex)>0){
        if(paststate$remainedspin>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 5 
    paststate$finishedspin<-presentstate$finishedspin-1
    paststate$remainedspin<-presentstate$remainedspin-2
    paststate$stackedwild<-presentstate$stackedwild-1
    action<-"DC43"
    pastindex<-which(data$finishedspin==paststate$finishedspin & data$remainedspin==paststate$remainedspin & data$stackedwild==paststate$stackedwild)
    if (length(pastindex)>0){
        if(paststate$remainedspin>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 6
    paststate$finishedspin<-presentstate$finishedspin-1
    paststate$remainedspin<-presentstate$remainedspin+1
    paststate$stackedwild<-presentstate$stackedwild-2
    action<-"DC45"
    pastindex<-which(data$finishedspin==paststate$finishedspin & data$remainedspin==paststate$remainedspin & data$stackedwild==paststate$stackedwild)
    if (length(pastindex)>0){
        if(paststate$remainedspin>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 7 
    paststate$finishedspin<-presentstate$finishedspin-1
    paststate$remainedspin<-presentstate$remainedspin+1
    paststate$stackedwild<-presentstate$stackedwild-3
    action<-"DC48"
    pastindex<-which(data$finishedspin==paststate$finishedspin & data$remainedspin==paststate$remainedspin & data$stackedwild==paststate$stackedwild)
    if (length(pastindex)>0){
        if(paststate$remainedspin>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    str_c("=",data$prob[presentindex])
} 


formulatingprob_stackedwild30<-function(data,presentindex){
    presentstate<-data[presentindex,1:3]
    paststate<-presentstate*0
    ## case 1 
    paststate$finishedspin<-presentstate$finishedspin-1
    paststate$remainedspin<-presentstate$remainedspin+1
    paststate$stackedwild<-30
    action<-"DC39"
    pastindex<-which(data$finishedspin==paststate$finishedspin & data$remainedspin==paststate$remainedspin & data$stackedwild==paststate$stackedwild)
    if (length(pastindex)>0){
        if(paststate$remainedspin>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 2
    paststate$finishedspin<-presentstate$finishedspin-1
    paststate$remainedspin<-presentstate$remainedspin-2
    paststate$stackedwild<-30
    action<-"DC40"
    pastindex<-which(data$finishedspin==paststate$finishedspin & data$remainedspin==paststate$remainedspin & data$stackedwild==paststate$stackedwild)
    if (length(pastindex)>0){
        if(paststate$remainedspin>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 3
    paststate$finishedspin<-presentstate$finishedspin-1
    paststate$remainedspin<-presentstate$remainedspin-4
    paststate$stackedwild<-30
    action<-"DC41"
    pastindex<-which(data$finishedspin==paststate$finishedspin & data$remainedspin==paststate$remainedspin & data$stackedwild==paststate$stackedwild)
    if (length(pastindex)>0){
        if(paststate$remainedspin>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 4
    paststate$finishedspin<-presentstate$finishedspin-1
    paststate$remainedspin<-presentstate$remainedspin+1
    paststate$stackedwild<-30
    action<-"DC42"
    pastindex<-which(data$finishedspin==paststate$finishedspin & data$remainedspin==paststate$remainedspin & data$stackedwild==paststate$stackedwild)
    if (length(pastindex)>0){
        if(paststate$remainedspin>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 5 
    paststate$finishedspin<-presentstate$finishedspin-1
    paststate$remainedspin<-presentstate$remainedspin+1
    paststate$stackedwild<-29
    action<-"DC42"
    pastindex<-which(data$finishedspin==paststate$finishedspin & data$remainedspin==paststate$remainedspin & data$stackedwild==paststate$stackedwild)
    if (length(pastindex)>0){
        if(paststate$remainedspin>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 6
    paststate$finishedspin<-presentstate$finishedspin-1
    paststate$remainedspin<-presentstate$remainedspin-2
    paststate$stackedwild<-30
    action<-"DC43"
    pastindex<-which(data$finishedspin==paststate$finishedspin & data$remainedspin==paststate$remainedspin & data$stackedwild==paststate$stackedwild)
    if (length(pastindex)>0){
        if(paststate$remainedspin>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 7 
    paststate$finishedspin<-presentstate$finishedspin-1
    paststate$remainedspin<-presentstate$remainedspin-4
    paststate$stackedwild<-29
    action<-"DC43"
    pastindex<-which(data$finishedspin==paststate$finishedspin & data$remainedspin==paststate$remainedspin & data$stackedwild==paststate$stackedwild)
    if (length(pastindex)>0){
        if(paststate$remainedspin>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 8
    paststate$finishedspin<-presentstate$finishedspin-1
    paststate$remainedspin<-presentstate$remainedspin+1
    paststate$stackedwild<-30
    action<-"DC45"
    pastindex<-which(data$finishedspin==paststate$finishedspin & data$remainedspin==paststate$remainedspin & data$stackedwild==paststate$stackedwild)
    if (length(pastindex)>0){
        if(paststate$remainedspin>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 9
    paststate$finishedspin<-presentstate$finishedspin-1
    paststate$remainedspin<-presentstate$remainedspin+1
    paststate$stackedwild<-29
    action<-"DC45"
    pastindex<-which(data$finishedspin==paststate$finishedspin & data$remainedspin==paststate$remainedspin & data$stackedwild==paststate$stackedwild)
    if (length(pastindex)>0){
        if(paststate$remainedspin>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 10
    paststate$finishedspin<-presentstate$finishedspin-1
    paststate$remainedspin<-presentstate$remainedspin+1
    paststate$stackedwild<-28
    action<-"DC45"
    pastindex<-which(data$finishedspin==paststate$finishedspin & data$remainedspin==paststate$remainedspin & data$stackedwild==paststate$stackedwild)
    if (length(pastindex)>0){
        if(paststate$remainedspin>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 11 
    paststate$finishedspin<-presentstate$finishedspin-1
    paststate$remainedspin<-presentstate$remainedspin+1
    paststate$stackedwild<-30
    action<-"DC48"
    pastindex<-which(data$finishedspin==paststate$finishedspin & data$remainedspin==paststate$remainedspin & data$stackedwild==paststate$stackedwild)
    if (length(pastindex)>0){
        if(paststate$remainedspin>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 12 
    paststate$finishedspin<-presentstate$finishedspin-1
    paststate$remainedspin<-presentstate$remainedspin+1
    paststate$stackedwild<-29
    action<-"DC48"
    pastindex<-which(data$finishedspin==paststate$finishedspin & data$remainedspin==paststate$remainedspin & data$stackedwild==paststate$stackedwild)
    if (length(pastindex)>0){
        if(paststate$remainedspin>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 13 
    paststate$finishedspin<-presentstate$finishedspin-1
    paststate$remainedspin<-presentstate$remainedspin+1
    paststate$stackedwild<-28
    action<-"DC48"
    pastindex<-which(data$finishedspin==paststate$finishedspin & data$remainedspin==paststate$remainedspin & data$stackedwild==paststate$stackedwild)
    if (length(pastindex)>0){
        if(paststate$remainedspin>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 14 
    paststate$finishedspin<-presentstate$finishedspin-1
    paststate$remainedspin<-presentstate$remainedspin+1
    paststate$stackedwild<-27
    action<-"DC48"
    pastindex<-which(data$finishedspin==paststate$finishedspin & data$remainedspin==paststate$remainedspin & data$stackedwild==paststate$stackedwild)
    if (length(pastindex)>0){
        if(paststate$remainedspin>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    str_c("=",data$prob[presentindex])
}

formulatingprob<-function(data,presentindex){
    presentstate<-data[presentindex,1:3]
    if(presentstate$stackedwild == 30){
        rtn<-formulatingprob_stackedwild30(data,presentindex)
    }else{
        rtn<-formulatingprob_stackedwild_1to29(data,presentindex)
    }
    rtn
} 

# pasting<-function(present,action){
#     if (action=='DC39') {
#         spin_past<-present$finishedspin-1
#         remainedspin_past<-present$remainedspin+1
#         stackedwild_past<-present$stackedwild-0
#     }else if (action=='DC40') {
#         spin_past<-present$finishedspin-1
#         remainedspin_past<-present$remainedspin-2
#         stackedwild_past<-present$stackedwild-0
#     }else if (action=='DC41') {
#         spin_past<-present$finishedspin-1
#         remainedspin_past<-present$remainedspin-4
#         stackedwild_past<-present$stackedwild-0
#     }else if (action=='DC42') {
#         spin_past<-present$finishedspin-1
#         remainedspin_past<-present$remainedspin+1
#         stackedwild_past<-present$stackedwild-1
#     }else if (action=='DC43') {
#         spin_past<-present$finishedspin-1
#         remainedspin_past<-present$remainedspin-2
#         stackedwild_past<-present$stackedwild-1
#     }else if (action=='DC45') {
#         spin_past<-present$finishedspin-1
#         remainedspin_past<-present$remainedspin+1
#         stackedwild_past<-present$stackedwild-2
#     }else if (action=='DC48') {
#         spin_past<-present$finishedspin-1
#         remainedspin_past<-present$remainedspin+1
#         stackedwild_past<-present$stackedwild-3
#     }
#     data.frame(spin=spin_past,remainedspin=remainedspin_past,stackedwild=stackedwild_past)
# }

# formulatingprob_stackedwild_1to29<-function(data,presentindex){
#     presentstate<-data[presentindex,1:3]
#     actions<-c("DC39","DC40","DC41","DC42","DC43","DC45","DC48")
#     for(i in 1:length(actions)){
#         paststate<-pasting(presentstate,actions[i])
#         pastindex<-which(data$finishedspin==paststate$finishedspin & data$remainedspin==paststate$remainedspin & data$stackedwild==paststate$stackedwild)
#         if (length(pastindex)>0){
#             if(paststate$remainedspin>0){
#                 data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",actions[i])
#             }
#         }
#     }    
#     str_c("=",data$prob[presentindex])
# } 
