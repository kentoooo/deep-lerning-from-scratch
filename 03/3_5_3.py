import numpy as np

def softmax(a):
	print('------a=--------')
	print(a)
	c = np.max(a)
	print('------c=--------')
	print(c)
	exp_a = np.exp(a - c)
	print('------a - c = -----')
	print(exp_a)
	sum_exp_a = np.sum(exp_a)
	print('------sum_exp_a = -------')
	print(sum_exp_a)
	y = exp_a / sum_exp_a
	return y

a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y)
print(np.sum(y))
