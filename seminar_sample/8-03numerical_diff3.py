import numpy as np
import matplotlib.pylab as plt

#x0=3,x1=4のときの偏微分 f(x)=x0^2+x1^2 

def function_tmp0(x0): #x0に対する偏微分ならtmp0
    plt.xlabel("x0")
    plt.ylabel("f(x0)")
    return x0*x0 + 4.0 ** 2.0 

def function_tmp1(x1): #x1に対する偏微分ならtmp1
    plt.xlabel("x1")
    plt.ylabel("f(x1)")
    return 3.0 ** 2.0 + x1*x1 

x=np.arange(0.0, 20.0, 0.1) #0から20まで、0.1刻みのｘ配列

def numerical_diff(f,x):
    h=1e-4 #0.0001
    return (f(x+h) - f(x-h)) / (2*h)

print(numerical_diff(function_tmp0,3.0)) #x0に対する偏微分ならtmp1と3.0、x1ならtmp2と4.0

plt.plot(x, function_tmp0(x)) #tmp0 or tmp1　書き換え
plt.show()