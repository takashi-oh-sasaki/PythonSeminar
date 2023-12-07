import numpy as np

y1=[0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0] #2がいちばん高い
y2=[0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0] #7がいちばん高い
t=[0,0,1,0,0,0,0,0,0,0] #2が正解

def mean_squared_error2(y1,t):
    return 0.5*np.sum((y1-t)**2)

print(mean_squared_error2(np.array(y1),np.array(t)))

def mean_squared_error7(y2,t):
    return 0.5*np.sum((y2-t)**2)

print(mean_squared_error7(np.array(y2),np.array(t)))
