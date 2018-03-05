import numpy as np

a = np.array([1010, 1000, 990])
print(np.exp(a) / np.sum(np.exp(a))) 
c = np.max(a)
print(a - c)
print(np.exp(a - c) / np.sum(np.exp(a - c)))

def softmax(a):
	x = np.max(a)
	exp_a = np.max(a - c)
	sum_exp_a = np.sum(exp_a)
	y = exp_a / sum_exp_a
	return y
