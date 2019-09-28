import requests
exec(requests.get('http://miruetoto.github.io/code/dataHandling.py').text)
exec(requests.get('http://miruetoto.github.io/code/HST/hstfunctions.py').text)

## load data
url='https://raw.githubusercontent.com/miruetoto/miruetoto.github.io/master/data/CollegeMsg.csv'
#data=pd.read_csv("CollegeMsg.csv")
data = pd.read_csv(url, error_bad_lines=False)
from datetime import datetime

transformReadabletime= lambda inpt: datetime.utcfromtimestamp(inpt).strftime('%Y-%m-%d %H:%M:%S')

data['time']=data.time.transform(transformReadabletime)
data['time']=pd.to_datetime(data.time)
data['month']=data.time.transform(lambda inpt: inpt.month)

n=max(max(data.v),max(data.u))
mon=["Apr","Mar","Jun","Jul","Aug","Sep","Nov"]
obs=cc(1,1899)
vname=sprod(mon,'-',obs)

data4=data[data['month']==4].iloc[:,0:2] 
data5=data[data['month']==5].iloc[:,0:2]
data6=data[data['month']==6].iloc[:,0:2]
data7=data[data['month']==7].iloc[:,0:2]
data8=data[data['month']==8].iloc[:,0:2]
data9=data[data['month']==9].iloc[:,0:2]
data10=data[data['month']==10].iloc[:,0:2]

Edg4=init('0',(n,n))
for i in co(0,len(data4)):
    Edg4[data4.iloc[i,0]-1,data4.iloc[i,1]-1] =Edg4[data4.iloc[i,0]-1,data4.iloc[i,1]-1] + 1 
    Edg4[data4.iloc[i,1]-1,data4.iloc[i,0]-1] =Edg4[data4.iloc[i,1]-1,data4.iloc[i,0]-1] + 1 
Edg5=init('0',(n,n))
for i in co(0,len(data5)):
    Edg5[data5.iloc[i,0]-1,data5.iloc[i,1]-1] =Edg5[data5.iloc[i,0]-1,data5.iloc[i,1]-1] + 1 
    Edg5[data5.iloc[i,1]-1,data5.iloc[i,0]-1] =Edg5[data5.iloc[i,1]-1,data5.iloc[i,0]-1] + 1 
Edg6=init('0',(n,n))
for i in co(0,len(data6)):
    Edg6[data6.iloc[i,0]-1,data6.iloc[i,1]-1] =Edg6[data6.iloc[i,0]-1,data6.iloc[i,1]-1] + 1 
    Edg6[data6.iloc[i,1]-1,data6.iloc[i,0]-1] =Edg6[data6.iloc[i,1]-1,data6.iloc[i,0]-1] + 1 
Edg7=init('0',(n,n))
for i in co(0,len(data7)):
    Edg7[data7.iloc[i,0]-1,data7.iloc[i,1]-1] =Edg7[data7.iloc[i,0]-1,data7.iloc[i,1]-1] + 1 
    Edg7[data7.iloc[i,1]-1,data7.iloc[i,0]-1] =Edg7[data7.iloc[i,1]-1,data7.iloc[i,0]-1] + 1 
Edg8=init('0',(n,n))
for i in co(0,len(data8)):
    Edg8[data8.iloc[i,0]-1,data8.iloc[i,1]-1] =Edg8[data8.iloc[i,0]-1,data8.iloc[i,1]-1] + 1 
    Edg8[data8.iloc[i,1]-1,data8.iloc[i,0]-1] =Edg8[data8.iloc[i,1]-1,data8.iloc[i,0]-1] + 1 
Edg9=init('0',(n,n))
for i in co(0,len(data9)):
    Edg9[data9.iloc[i,0]-1,data9.iloc[i,1]-1] =Edg9[data9.iloc[i,0]-1,data9.iloc[i,1]-1] + 1 
    Edg9[data9.iloc[i,1]-1,data9.iloc[i,0]-1] =Edg9[data9.iloc[i,1]-1,data9.iloc[i,0]-1] + 1 
Edg10=init('0',(n,n))
for i in co(0,len(data10)):
    Edg10[data10.iloc[i,0]-1,data10.iloc[i,1]-1] =Edg10[data10.iloc[i,0]-1,data10.iloc[i,1]-1] + 1 
    Edg10[data10.iloc[i,1]-1,data10.iloc[i,0]-1] =Edg10[data10.iloc[i,1]-1,data10.iloc[i,0]-1] + 1 

Iden=1*init('I',(n,n));Zeros=init('0',(n,n)) # n=1899 
R4=cbind(Edg4,Iden,Zeros,Zeros,Zeros,Zeros,Zeros)
R5=cbind(Iden,Edg5,Iden,Zeros,Zeros,Zeros,Zeros)
R6=cbind(Zeros,Iden,Edg6,Iden,Zeros,Zeros,Zeros)
R7=cbind(Zeros,Zeros,Iden,Edg7,Iden,Zeros,Zeros)
R8=cbind(Zeros,Zeros,Zeros,Iden,Edg8,Iden,Zeros)
R9=cbind(Zeros,Zeros,Zeros,Zeros,Iden,Edg9,Iden)
R10=cbind(Zeros,Zeros,Zeros,Zeros,Zeros,Iden,Edg10)

Edgtemp=rbind(R4,R5,R6,R7,R8,R9,R10)
Edg=Edgtemp/np.max(Edgtemp)
f=init('0',len(nodename))
hstrslt=hst(f,Edg,τ=20000,γ=0.5,b=0.1)
