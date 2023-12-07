import numpy as np

A=np.array([[1,2,3],[4,5,6]]) #2x3
print(A.shape)

B=np.array([[1,2],[3,4],[5,6]]) #3x2
print(B.shape)

print(np.dot(A,B)) #2x2

C=np.array([[1,2],[3,4],[5,6]]) #3x2
print(C.shape)

D=np.array([7,8]) #2x1
print(D.shape)

print(np.dot(C,D)) #3x1