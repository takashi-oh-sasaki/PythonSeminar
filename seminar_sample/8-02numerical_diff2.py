import numpy as np
import matplotlib.pylab as plt

def function_1(x):
    return 0.01*x**2 + 0.1*x

x=np.arange(0.0, 20.0, 0.1) #0から20まで、0.1刻みのｘ配列
y=function_1(x)

def numerical_diff(f,x): #数値微分
    h=1e-4 #0.0001
    return (f(x+h) - f(x-h)) / (2*h)

def tangent_line(f, x): #数値微分の値を傾きとする接線のｙ
    d = numerical_diff(f, x)
    y = f(x) - d*x
    return lambda t: d*t + y

print(numerical_diff(function_1,5)) #傾き

tf = tangent_line(function_1, 5)
y2 = tf(x)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.plot(x, y2)
plt.show()