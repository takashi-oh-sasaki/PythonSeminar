import numpy as np

def sigmoid(x):
    return 1 / (1+np.exp(-x))

def identify_function(x):
    return x

#1層目
X=np.array([1.0,0.5]) #1x2
W1=np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]]) #2x3
B1=np.array([0.1,0.2,0.3]) #1x3

A1=np.dot(X,W1)+B1
Z1=sigmoid(A1) #1x3

#2層目
W2=np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]]) #3x2
B2=np.array([0.1,0.2]) #1x2

A2=np.dot(Z1,W2)+B2
Z2=sigmoid(A2) #1x2

#3層目
W3=np.array([[0.1,0.3],[0.2,0.4]]) #2x2
B3=np.array([0.1,0.2]) #1x2

A3=np.dot(Z2,W3)+B3
Y=identify_function(A3) #1x2

print(Y)