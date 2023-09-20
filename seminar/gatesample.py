# coding: utf-8

# ANDゲート
def AND(x1, x2):
    w1, w2, theta = 1.1, 2.1, 2.2  # 数値のパラメータは自分で決めている
    y = x1*w1 + x2*w2
    if y <= theta:
        return 0
    elif y > theta:
        return 1

# NANDゲート

def NAND(x1, x2):
    w1, w2, theta = -1.1, -2.1, -2.2  # 数値のパラメータは自分で決めている
    y = x1*w1 + x2*w2
    if y <= theta:
        return 0
    elif y > theta:
        return 1

# ORゲート

def OR(x1, x2):
    w1, w2, theta = 0.5, 0.2, 0  # 数値のパラメータは自分で決めている
    y = x1*w1 + x2*w2
    if y <= theta:
        return 0
    elif y > theta:
        return 1

print(AND(0, 0))
print(AND(1, 0))
print(AND(0, 1))
print(AND(1, 1))
print("--------")
print(NAND(0, 0))
print(NAND(1, 0))
print(NAND(0, 1))
print(NAND(1, 1))
print("--------")
print(OR(0, 0))
print(OR(1, 0))
print(OR(0, 1))
print(OR(1, 1))
print("--------")

