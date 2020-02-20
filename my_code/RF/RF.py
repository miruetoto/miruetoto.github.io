def ginverseDiag(d,threshold=0.0005):
    d[d<threshold]=0
    d[d>0]=1/d[d>0]
    return np.asmatrix(np.diag(d))

def getbeta(X,Y):
    XX=X.T*X
    d,P=np.linalg.eig(XX)
    DI=ginverseDiag(d,threshold=0.05)
    betahat=(P*DI*P.I)*X.T*Y
    return betahat.real


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

def tidyrx(rxdata):
    push(rxdata,"rx")
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
    if rtn[3]=='pd': rtn[0:3]=[0,0,0]
    if rtn[3]=='OFF': rtn[0:3]=[0,0,0]
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
        walk=a2s(init('u',1)*5.5)
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


def slagging(npmat,lag=2,jump=60):
    npmat_ori=npmat.copy()
    rtn=lagg(npmat_ori,1*jump)
    for l in cc(2,lag):
        rtn=cbind(rtn,lagg(npmat_ori,l*jump))
    return rtn

def lagging(npmat,lag=2):
    npmat_ori=npmat.copy()
    rtn=lagg(npmat_ori,1)
    for l in cc(2,lag):
        rtn=cbind(rtn,lagg(npmat_ori,l))
    return rtn

def seperate_trtst(npmat,ratio=0.7):
    trindex=list(range(0,round(npmat.shape[0]*ratio)))
    testindex=list(range(round(npmat.shape[0]*ratio),npmat.shape[0]))
    return (npmat[trindex,:],npmat[testindex,:])

def smooth_spline(npmat):
    push(npmat,"npmat")
    ro.r('sy<-npmat*0; for(j in 1:dim(npmat)[2]) sy[,j]<-smooth.spline(npmat[,j])$y')
    return pull("sy")

def parse_data(nas_id, nas_pw, date, comm, place):
    import os
    from io import StringIO
    import getpass
    import subprocess
    template_column = ['datetime','rx_err','F step','R step','F ctrl. temp.','R ctrl. temp.','R-DIFF','F-DIFF','F temp.','R temp.','F dfr. temp.','R dfr. temp.',
              'RT temp.','humidity','F_state','R_state','(guc  exterior rt zone<<4)|(guc  humdity compensation value zone)','f fan power on','r fan power on',
              'c fan power on','hygiene fan power on','F FAN DUTY','R FAN DUTY','C FAN DUTY','F-FAN RPM','R-FAN RPM','C-FAN RPM','2eva ctrl. state<<4',
              '3W V/V STEP','R DOOR','F DOOR','R weak r load against flag','R weak r load against time','R weak r load against reload protection','R strong r load against flag',
              'R strong r load against time','R strong r load reload protection','F load against flag',
              'F load against time','heater filler power on','heater home bar power on','heater utill power on','heater drain power on','heater instaview power on',
              'heater F dfr. power on','heater R dfr. power on','F timer 1min accu.','F timer 1min changeable accu.','blackbox door r counter 5min','blackbox door r time 5min',
              'blackbox door f counter 5min','blackbox door f time 5min','2eva ctrl. 1sec lqc operation time','blackbox 60sec titmer',
              'compressor power on','compressor cooling power','COMP MODE','COMP FREQ','COMP SHIFT','compressor status','compressor power','compressor dc link',
              'C O M P S T R O K E','C O M P P H A S E','C O M P C U R R E N T','C O M P K G A S','C O M P P W M','C O M P X T D C','C O M P O B J E C T I V E',
              'blackbox f compressor continuity time min','(gun F titmer 1sec compressor force off/60)','gauc compressor tx data[0]','gauc compressor tx data[1]',
              'gauc compressor tx data[2]','(guc  F operation mode<<4)|(guc  R operation mode)','compressor leak high err','compressor leak low err',
              'comp_leak_low_state','comp_leak_high_state','f sensor error','r1 sensor error','rt sensor error','humidity sensor error','rpm f error','rpm r error',
              'rpm c error','F dfr. Error','R dfr. error','F dfr. sensor error','F dfr. sensor error','defrost']
    url = 'http://{nas_id}:{nas_pw}@10.178.134.156:/20-Project-Fridge/{place}/logs/{date}/log_{comm}Data_{date}.csv'.format(nas_id=nas_id, nas_pw=nas_pw, comm=comm, date=str(date), place=place)
    raw_data = requests.get(url, verify=False)
    pd_data = pd.read_csv(StringIO(raw_data.text))
    pd_data.columns = template_column
    push(pd_data, 'data_{}'.format(date))
    return pd_data

def estimatingtemp(X):
    import os
    from io import StringIO
    import getpass
    import subprocess
    
    nas_id = 'guebin'
    nas_pw = '123qwe'
    url ='http://{}:{}@10.178.134.156:/20-Project-Fridge/GuebinCoef/betahat.csv'.format(nas_id, nas_pw)
    raw_data = requests.get(url, verify=False)
    βhat=np.matrix(pd.read_csv(StringIO(raw_data.text)))
    #βhat=np.matrix(pd.read_csv("betahat.csv"))
    Xtilde=slagging(X,50,3)
    ΔY=Xtilde*βhat
    Yhat = np.cumsum(ΔY,axis=0)[:,:]
    return Yhat    