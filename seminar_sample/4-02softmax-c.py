import numpy as np

a=np.array([1010,1000,990])
c=np.max(a)
exp_a=np.exp(a-c)
print(exp_a)

sum_exp_a=np.sum(exp_a)
print(sum_exp_a)

y=exp_a/sum_exp_a
print(y)