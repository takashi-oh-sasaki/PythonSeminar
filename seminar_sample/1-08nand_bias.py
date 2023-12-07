import numpy as np

def NAND(x1, x2):
    w1, w2, theta = -1.1, -2.1, -2.2
    y = x1*w1 + x2*w2
    if y <= theta:
        return 0
    elif y > theta:
        return 1

print(NAND(0,0))
print(NAND(1,0))
print(NAND(0,1))
print(NAND(1,1))
