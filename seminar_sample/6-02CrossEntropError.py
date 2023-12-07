import numpy as np

y1=[0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0] #2がいちばん高い
y2=[0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0] #7がいちばん高い
t=[0,0,1,0,0,0,0,0,0,0] #2が正解
delta=1e-7
def cross_entropy_error2(y1,t):
    return -np.sum(t*np.log(y1+delta))

print(cross_entropy_error2(np.array(y1),np.array(t)))

def cross_entropy_error7(y2,t):
    return -np.sum(t*np.log(y2+delta))

print(cross_entropy_error7(np.array(y2),np.array(t)))