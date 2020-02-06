def ginverseDiag(d,threshold=0.0005):
    d[d<threshold]=0
    d[d>0]=1/d[d>0]
    return np.asmatrix(np.diag(d))

def getbeta(Y,X):
    XX=X.T*X
    d,P=np.linalg.eig(XX)
    DI=ginverseDiag(d,threshold=0.05)
    betahat=(P*DI*P.I)*X.T*Y
    return betahat


# site: 1=Gasan, 2=Yangjae 
# type: 1=rx, 2=tx, 3=all 
# mmddhhmm: "01-02,14:24"

# def pull_gasan(filename): 
#     from io import StringIO
#     u='http://guebin:123qwe@10.178.134.156:/20-Project-Fridge/gasan/logs/'+filename
#     r = requests.get(u, verify=False)
#     rtn=pd.read_csv(StringIO(r.text))
#     return rtn

# def pull_yangjae(filename): 
#     from io import StringIO
#     u='http://guebin:123qwe@10.178.134.156:/20-Project-Fridge/yangjae/logs/'+filename
#     r = requests.get(u, verify=False)
#     rtn=pd.read_csv(StringIO(r.text))
#     return rtn

def tidyrx(rx):
    push(rx)
    ro.r('names(rx)<-str_replace_all(names(rx),"[.]","_")')
    ro.r('lovevname<-c("F_temp_", "R_temp_", "RT_temp_", "f_fan_power_on","r_fan_power_on", "F_FAN_DUTY", "R_FAN_DUTY","X2eva_ctrl__state__4", "R_DOOR", "F_DOOR","compressor_cooling_power")')
    ro.r('data_rx<-select(rx,lovevname)')  
    ro.r('data_rx<-mutate(data_rx,mtt_f_fan_duty_plus=F_FAN_DUTY*(X2eva_ctrl__state__4=="F"),mtt_r_fan_duty_plus=R_FAN_DUTY*(X2eva_ctrl__state__4=="R"),mtt_f_fan_duty_minus=F_FAN_DUTY-F_FAN_DUTY*(X2eva_ctrl__state__4=="F"),mtt_r_fan_duty_minus=R_FAN_DUTY-R_FAN_DUTY*(X2eva_ctrl__state__4=="R"),mtt_f_comp=compressor_cooling_power*(X2eva_ctrl__state__4=="F"),mtt_r_comp=compressor_cooling_power*(X2eva_ctrl__state__4=="R"),mtt_rt_fopen=RT_temp_*(F_DOOR=="open"),mtt_rt_ropen=RT_temp_*(R_DOOR=="open"))')
    ro.r('tidy<-select(data_rx,F_temp_,R_temp_,RT_temp_,starts_with("mtt_"))')
    return pull("tidy")

def pid_init(tidy,tintrvl=100):
    RTindex=[2] 
    Y1index=[0] 
    Y2index=[1] 
    U1index=[7] 
    U2index=[8] 
    RT=np.asmatrix(tidy.iloc[:,RTindex])
    Y1=np.asmatrix(tidy.iloc[:,Y1index])
    Y2=np.asmatrix(tidy.iloc[:,Y2index])
    U1=np.asmatrix(tidy.iloc[:,U1index])
    U2=np.asmatrix(tidy.iloc[:,U2index])
    tintrvl=tintrvl
    
    ΔY1=Y1-lagg(Y1,1*tintrvl)
    ΔY2=Y2-lagg(Y2,1*tintrvl)

    U1_lag1=lagg(U1,1*tintrvl)
#     U1_lag2=lagg(U1,2*tintrvl)
#     U1_lag3=lagg(U1,3*tintrvl)
#     U1_lag4=lagg(U1,4*tintrvl)

    U2_lag1=lagg(U2,1*tintrvl)
#     U2_lag2=lagg(U2,2*tintrvl)
#     U2_lag3=lagg(U2,3*tintrvl)
#     U2_lag4=lagg(U2,4*tintrvl)

    U1tilde=U1_lag1
    U2tilde=U2_lag1
#     U1tilde=cbind(U1_lag1,U1_lag2,U1_lag3,U1_lag4)
#     U2tilde=cbind(U2_lag1,U2_lag2,U2_lag3,U2_lag4)
    
    X1=cbind(U1tilde,RT)
    X2=cbind(U2tilde,RT)
    
    (U1,d1,V1t)=np.linalg.svd(X1)
    V1=V1t.T[:,0:2] # major 2 pc
    Z1=X1*V1
    ΔY1hat=Z1*(Z1.T*Z1).I*Z1.T*ΔY1
    (U2,d2,V2t)=np.linalg.svd(X2)
    V2=V2t.T[:,0:2] # major 2 pc
    Z2=X2*V2
    ΔY2hat=Z2*(Z2.T*Z2).I*Z2.T*ΔY2
    β1=(V1*V1.T).I*V1*((Z1.T*Z1).I*Z1.T*ΔY1)
    β2=(V2*V2.T).I*V2*((Z2.T*Z2).I*Z2.T*ΔY2)
#     Fcomp_Kp_inv=np.sum(β1[0:4])
#     Rcomp_Kp_inv=np.sum(β2[0:4])
    Fcomp_Kp_inv=np.sum(β1[0])
    Rcomp_Kp_inv=np.sum(β2[0])

    print("Fcomp_Kp:",-1/Fcomp_Kp_inv)
    print("Ffan_Kp:",-1/Fcomp_Kp_inv*2.73296)
    print("Rcomp_Kp:",-1/Rcomp_Kp_inv)
    print("Rfan_Kp:",-1/Rcomp_Kp_inv*4.060935)
    return (-1/Fcomp_Kp_inv,-1/Fcomp_Kp_inv*2.73296,-1/Rcomp_Kp_inv,-1/Rcomp_Kp_inv*4.060935)    
 
def nextaction(previous):
    daction=init('u',3)*10-5
    rtn=previous.copy()
    rtn[0:3]=previous[0:3]+daction
    ## adjusting comp power 
    if rtn[0]<15: rtn[0]=15
    elif rtn[0]>90: rtn[0]=90
    else: rtn=rtn 
    ## adjusting r-fan 
    if rtn[1]<0: rtn[1]=0
    elif rtn[1]>178: rtn[1]=178
    else: rtn=rtn 
    ## adjusting f-fan 
    if rtn[2]<0: rtn[2]=0
    elif rtn[2]>178: rtn[2]=178
    else: rtn=rtn 
    ## next2eva 
    rtn[3:5]=next2eva(previous[3],previous[4])
    if rtn[3]=='pd': rtn[0:3]=0
    if rtn[3]=='OFF': rtn[0:3]=0
    return rtn

def next2eva(eva,walksum): 
    ## 0: 'sim'
    ## 1: 'R'
    ## 2: 'F'
    ## 3: 'OFF'
    ## 4: 'pd'
    ## 5: 'fixtemp'
    nexteva=eva
    if eva=='pd':
        walk=150
    else:
        walk=a2s(init('u',1)*5.5-2.5)
    walksum=walk+walksum
    if walksum>3000: 
        walksum=0
        if eva=='F':
            nexteva='pd'
        else:
            from random import sample 
            nexteva=a2s(sample(['F','R','OFF'],1))
    rtn=[nexteva,walksum]
    return rtn