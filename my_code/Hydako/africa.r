library(stringr)
# formulatingprob_wildstack_1to29<-function(data,presentindex){
#     presentstate<-data[presentindex,2:4]
#     actions<-c("DC39","DC40","DC41","DC42","DC43","DC45","DC48")
#     for(i in 1:length(actions)){
#         paststate<-pasting(presentstate,actions[i])
#         pastindex<-which(data$spin==paststate$spin & data$spinremain==paststate$spinremain & data$wildstack==paststate$wildstack)
#         if (length(pastindex)>0){
#             if(paststate$spinremain>0){
#                 data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",actions[i])
#             }
#         }
#     }    
#     str_c("=",data$prob[presentindex])
# } 

formulatingprob_wildstack_1to29<-function(data,presentindex){
    presentstate<-data[presentindex,2:4]
    paststate<-presentstate*0
    ## case 1 
    paststate$spin<-presentstate$spin-1
    paststate$spinremain<-presentstate$spinremain+1
    paststate$wildstack<-presentstate$wildstack
    action<-"DC39"
    pastindex<-which(data$spin==paststate$spin & data$spinremain==paststate$spinremain & data$wildstack==paststate$wildstack)
    if (length(pastindex)>0){
        if(paststate$spinremain>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 2
    paststate$spin<-presentstate$spin-1
    paststate$spinremain<-presentstate$spinremain-3
    paststate$wildstack<-presentstate$wildstack
    action<-"DC40"
    pastindex<-which(data$spin==paststate$spin & data$spinremain==paststate$spinremain & data$wildstack==paststate$wildstack)
    if (length(pastindex)>0){
        if(paststate$spinremain>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 3
    paststate$spin<-presentstate$spin-1
    paststate$spinremain<-presentstate$spinremain-5
    paststate$wildstack<-presentstate$wildstack
    action<-"DC41"
    pastindex<-which(data$spin==paststate$spin & data$spinremain==paststate$spinremain & data$wildstack==paststate$wildstack)
    if (length(pastindex)>0){
        if(paststate$spinremain>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 4
    paststate$spin<-presentstate$spin-1
    paststate$spinremain<-presentstate$spinremain+1
    paststate$wildstack<-presentstate$wildstack-1
    action<-"DC42"
    pastindex<-which(data$spin==paststate$spin & data$spinremain==paststate$spinremain & data$wildstack==paststate$wildstack)
    if (length(pastindex)>0){
        if(paststate$spinremain>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 5 
    paststate$spin<-presentstate$spin-1
    paststate$spinremain<-presentstate$spinremain-3
    paststate$wildstack<-presentstate$wildstack-1
    action<-"DC43"
    pastindex<-which(data$spin==paststate$spin & data$spinremain==paststate$spinremain & data$wildstack==paststate$wildstack)
    if (length(pastindex)>0){
        if(paststate$spinremain>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 6
    paststate$spin<-presentstate$spin-1
    paststate$spinremain<-presentstate$spinremain+1
    paststate$wildstack<-presentstate$wildstack-2
    action<-"DC45"
    pastindex<-which(data$spin==paststate$spin & data$spinremain==paststate$spinremain & data$wildstack==paststate$wildstack)
    if (length(pastindex)>0){
        if(paststate$spinremain>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 7 
    paststate$spin<-presentstate$spin-1
    paststate$spinremain<-presentstate$spinremain+1
    paststate$wildstack<-presentstate$wildstack-3
    action<-"DC48"
    pastindex<-which(data$spin==paststate$spin & data$spinremain==paststate$spinremain & data$wildstack==paststate$wildstack)
    if (length(pastindex)>0){
        if(paststate$spinremain>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    str_c("=",data$prob[presentindex])
} 


formulatingprob_wildstack30<-function(data,presentindex){
    presentstate<-data[presentindex,2:4]
    paststate<-presentstate*0
    ## case 1 
    paststate$spin<-presentstate$spin-1
    paststate$spinremain<-presentstate$spinremain+1
    paststate$wildstack<-30
    action<-"DC39"
    pastindex<-which(data$spin==paststate$spin & data$spinremain==paststate$spinremain & data$wildstack==paststate$wildstack)
    if (length(pastindex)>0){
        if(paststate$spinremain>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 2
    paststate$spin<-presentstate$spin-1
    paststate$spinremain<-presentstate$spinremain-3
    paststate$wildstack<-30
    action<-"DC40"
    pastindex<-which(data$spin==paststate$spin & data$spinremain==paststate$spinremain & data$wildstack==paststate$wildstack)
    if (length(pastindex)>0){
        if(paststate$spinremain>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 3
    paststate$spin<-presentstate$spin-1
    paststate$spinremain<-presentstate$spinremain-5
    paststate$wildstack<-30
    action<-"DC41"
    pastindex<-which(data$spin==paststate$spin & data$spinremain==paststate$spinremain & data$wildstack==paststate$wildstack)
    if (length(pastindex)>0){
        if(paststate$spinremain>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 4
    paststate$spin<-presentstate$spin-1
    paststate$spinremain<-presentstate$spinremain+1
    paststate$wildstack<-30
    action<-"DC42"
    pastindex<-which(data$spin==paststate$spin & data$spinremain==paststate$spinremain & data$wildstack==paststate$wildstack)
    if (length(pastindex)>0){
        if(paststate$spinremain>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 5 
    paststate$spin<-presentstate$spin-1
    paststate$spinremain<-presentstate$spinremain+1
    paststate$wildstack<-29
    action<-"DC42"
    pastindex<-which(data$spin==paststate$spin & data$spinremain==paststate$spinremain & data$wildstack==paststate$wildstack)
    if (length(pastindex)>0){
        if(paststate$spinremain>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 6
    paststate$spin<-presentstate$spin-1
    paststate$spinremain<-presentstate$spinremain-3
    paststate$wildstack<-30
    action<-"DC43"
    pastindex<-which(data$spin==paststate$spin & data$spinremain==paststate$spinremain & data$wildstack==paststate$wildstack)
    if (length(pastindex)>0){
        if(paststate$spinremain>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 7 
    paststate$spin<-presentstate$spin-1
    paststate$spinremain<-presentstate$spinremain-3
    paststate$wildstack<-29
    action<-"DC43"
    pastindex<-which(data$spin==paststate$spin & data$spinremain==paststate$spinremain & data$wildstack==paststate$wildstack)
    if (length(pastindex)>0){
        if(paststate$spinremain>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 8
    paststate$spin<-presentstate$spin-1
    paststate$spinremain<-presentstate$spinremain+1
    paststate$wildstack<-30
    action<-"DC45"
    pastindex<-which(data$spin==paststate$spin & data$spinremain==paststate$spinremain & data$wildstack==paststate$wildstack)
    if (length(pastindex)>0){
        if(paststate$spinremain>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 9
    paststate$spin<-presentstate$spin-1
    paststate$spinremain<-presentstate$spinremain+1
    paststate$wildstack<-29
    action<-"DC45"
    pastindex<-which(data$spin==paststate$spin & data$spinremain==paststate$spinremain & data$wildstack==paststate$wildstack)
    if (length(pastindex)>0){
        if(paststate$spinremain>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 10
    paststate$spin<-presentstate$spin-1
    paststate$spinremain<-presentstate$spinremain+1
    paststate$wildstack<-28
    action<-"DC45"
    pastindex<-which(data$spin==paststate$spin & data$spinremain==paststate$spinremain & data$wildstack==paststate$wildstack)
    if (length(pastindex)>0){
        if(paststate$spinremain>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 11 
    paststate$spin<-presentstate$spin-1
    paststate$spinremain<-presentstate$spinremain+1
    paststate$wildstack<-30
    action<-"DC48"
    pastindex<-which(data$spin==paststate$spin & data$spinremain==paststate$spinremain & data$wildstack==paststate$wildstack)
    if (length(pastindex)>0){
        if(paststate$spinremain>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 12 
    paststate$spin<-presentstate$spin-1
    paststate$spinremain<-presentstate$spinremain+1
    paststate$wildstack<-29
    action<-"DC48"
    pastindex<-which(data$spin==paststate$spin & data$spinremain==paststate$spinremain & data$wildstack==paststate$wildstack)
    if (length(pastindex)>0){
        if(paststate$spinremain>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 13 
    paststate$spin<-presentstate$spin-1
    paststate$spinremain<-presentstate$spinremain+1
    paststate$wildstack<-28
    action<-"DC48"
    pastindex<-which(data$spin==paststate$spin & data$spinremain==paststate$spinremain & data$wildstack==paststate$wildstack)
    if (length(pastindex)>0){
        if(paststate$spinremain>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    ## case 14 
    paststate$spin<-presentstate$spin-1
    paststate$spinremain<-presentstate$spinremain+1
    paststate$wildstack<-27
    action<-"DC48"
    pastindex<-which(data$spin==paststate$spin & data$spinremain==paststate$spinremain & data$wildstack==paststate$wildstack)
    if (length(pastindex)>0){
        if(paststate$spinremain>0){
            data$prob[presentindex]<-str_c(data$prob[presentindex],"+",data$stateindex[pastindex],"*",action)
        }
    }
    str_c("=",data$prob[presentindex])
}

formulatingprob<-function(data,presentindex){
    presentstate<-data[presentindex,2:4]
    if(presentstate$wildstack == 30){
        rtn<-formulatingprob_wildstack30(data,presentindex)
    }else{
        rtn<-formulatingprob_wildstack_1to29(data,presentindex)
    }
} 

# pasting<-function(present,action){
#     if (action=='DC39') {
#         spin_past<-present$spin-1
#         spinremain_past<-present$spinremain+1
#         wildstack_past<-present$wildstack-0
#     }else if (action=='DC40') {
#         spin_past<-present$spin-1
#         spinremain_past<-present$spinremain-2
#         wildstack_past<-present$wildstack-0
#     }else if (action=='DC41') {
#         spin_past<-present$spin-1
#         spinremain_past<-present$spinremain-4
#         wildstack_past<-present$wildstack-0
#     }else if (action=='DC42') {
#         spin_past<-present$spin-1
#         spinremain_past<-present$spinremain+1
#         wildstack_past<-present$wildstack-1
#     }else if (action=='DC43') {
#         spin_past<-present$spin-1
#         spinremain_past<-present$spinremain-2
#         wildstack_past<-present$wildstack-1
#     }else if (action=='DC45') {
#         spin_past<-present$spin-1
#         spinremain_past<-present$spinremain+1
#         wildstack_past<-present$wildstack-2
#     }else if (action=='DC48') {
#         spin_past<-present$spin-1
#         spinremain_past<-present$spinremain+1
#         wildstack_past<-present$wildstack-3
#     }
#     data.frame(spin=spin_past,spinremain=spinremain_past,wildstack=wildstack_past)
# }