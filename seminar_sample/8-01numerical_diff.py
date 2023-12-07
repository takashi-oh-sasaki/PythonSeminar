import numpy as np
import matplotlib.pylab as plt

def function_1(x):
    return 0.01*x**2 + 0.1*x

x=np.arange(0.0, 20.0, 0.1) #0から20まで、0.1刻みのｘ配列
y=function_1(x)

def numerical_diff(f,x):
    h=1e-4 #0.0001
    return (f(x+h) - f(x-h)) / (2*h)

print(numerical_diff(function_1,5))
print(numerical_diff(function_1,10))

plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.show()