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

def tidyrx(rx):
    push(rx)
    ro.r('names(rx)<-str_replace_all(names(rx),"[.]","_")')
    ro.r('data_rx<-rx[,c(7,8,11,16,17,20,21,26,28,29,54)]')
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
    print("Rcomp_Kp:",-1/Rcomp_Kp_inv)
    return (-1/Fcomp_Kp_inv,-1/Rcomp_Kp_inv)    