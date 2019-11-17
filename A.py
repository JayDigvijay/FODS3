import numpy as np 
import scipy as sp 
import matplotlib.pyplot as plt 
from scipy.special import gamma as G

## M = Number of Heads in Randomly Generated Sample. 
k = 1
a = 4 * k
b = 6 * k
u = 0
N = 160
M = np.random.randint(1,161)
while(M >= 0.4*160 and M <= 0.6*160):
	M = np.random.randint(1,161)
L = N - M
arr = np.array([0]*(N-M) + [1]*(M))	
np.random.shuffle(arr)
#print(G(2.5))
#print(arr) 
U_ML = M/160.00
print('%0.2f' %U_ML)
P = []
U = []
m = 0
l = 0

for j in range(len(arr)):
	P = []
	U = []
	u = 0
	if arr[j] == 1:
		m += 1
	else:
		l += 1
	for i in range (101):
		if u > 1:
			u = 1
		Norm = G(a + b + l + m)/(G(a + m)*G(b + l))
		u1 = pow(u, (a - 1 + m))
		u2 = pow(1 - u, (b - 1  + l))
		P_Val = Norm * u1 * u2
		P.append(P_Val)
		U.append(u)
		u += 0.010000
		#print(Norm)
	if (j + 1)%2 == 0:
		##print(m/160.0)
		plt.plot(U, P)
		plt.ion()
		plt.xlabel('u')
		plt.ylabel('P')
		plt.show()
		plt.pause(0.1)
		plt.clf()
