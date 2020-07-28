# 기울기 
# obj_ftemp는 사용자가 정의하는 함수이다. 
# 예를들어 아래와 같이 정의한다. 
# x는 넘파이다. 

def grd(obj_ftemp,x): 
    h=1e-4
    grad=np.zeros_like(x)
    
    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx]=tmp_val +h 
        fxh1=obj_ftemp(x)
        x[idx]=tmp_val -h
        fxh2=obj_ftemp(x)
        grad[idx]=(fxh1-fxh2)/(2*h)
        x[idx]=tmp_val 
    return grad   

def grd_descent(obj_ftemp,init_x,lr=0.01,step_num=100): #lr: learning rate 
    x=init_x
    for i in range(step_num):
        grad=grd(obj_ftemp,x)
        x -= lr*grad
    return x
