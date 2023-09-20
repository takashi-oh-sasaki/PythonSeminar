import numpy as np

A=np.array([1,2,3,4]) #1行4列
print(A) #配列の中身
print(np.ndim(A)) #次元
print(A.shape)  #形状
print(A.shape[0]) #行数

B=np.array([[1,2],[3,4],[5,6]]) #3行2列
print(B) #配列の中身
print(np.ndim(B)) #次元
print(B.shape)  #形状
print(B.shape[0]) #行数
