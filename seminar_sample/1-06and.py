def AND(x1,x2):
    w1,w2,theta=1,1,1

    if x1*w1+x2*w2 <= theta:
        return 0
    elif x1*w1+x2*w2 > theta:
        return 1

print(AND(0,0))
print(AND(1,0))
print(AND(0,1))
print(AND(1,1))

    