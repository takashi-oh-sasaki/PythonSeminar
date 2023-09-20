import numpy as np

#バイアスと活性化関数は省略
X=np.array([1,2]) #1x2
W=np.array([[1,3,5],[2,4,6]]) #2x3

Y=np.dot(X,W)
print(Y)

