import numpy as np

def OR(x1, x2):
    w1, w2, theta = 0.5, 0.2, 0
    y = x1*w1 + x2*w2
    if y <= theta:
        return 0
    elif y > theta:
        return 1

print(OR(0,0))
print(OR(1,0))
print(OR(0,1))
print(OR(1,1))
