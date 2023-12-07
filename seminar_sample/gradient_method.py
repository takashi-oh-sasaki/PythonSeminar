# coding: utf-8
import numpy as np
import matplotlib.pylab as plt
from gradient_2d import numerical_gradient #ファイルgradient_2d.pyが必要


def gradient_descent(f, init_x, lr, step_num):
    x = init_x
    x_history = []

    for i in range(step_num):
        x_history.append( x.copy() )

        grad = numerical_gradient(f, x)
        x -= lr * grad #勾配降下法のパラメータ更新

    return x, np.array(x_history)


def function_2(x): #f(x0,x1)=x0^2+x1^2の最小値を勾配法で計算
    return x[0]**2 + x[1]**2

init_x = np.array([-3.0, 4.0])    

lr = 0.1 #学習率
step_num = 101 #勾配法の繰り返し数
x, x_history = gradient_descent(function_2, init_x, lr, step_num)

#print(gradient_descent(function_2, np.array([-3.0, 4.0]), lr=0.1, step_num=100)) #計算テスト：グラフとは別
print(x_history)

plt.plot( [-5, 5], [0,0], '--b')
plt.plot( [0,0], [-5, 5], '--b')
plt.plot(x_history[:,0], x_history[:,1], 'o')

plt.xlim(-3.5, 3.5)
plt.ylim(-4.5, 4.5)
plt.xlabel("X0")
plt.ylabel("X1")
plt.show()