import numpy as np 
import scipy as sp 
import matplotlib.pyplot as plt 
from scipy.special import gamma as G

## M = Number of Heads in Randomly Generated Sample. 
k = 1.1
a = 4 * k
b = 6 * k
u = 0
N = 160
M = np.random.randint(1,161)
while(M >= 0.4*160 and M <= 0.6*160):
	M = np.random.randint(1,161)
arr = np.array([0]*(N-M) + [1]*(M))	
np.random.shuffle(arr)
#print(G(2.5))
#print(arr) 
U_ML = M/160.00

P = []
U = []
for i in range (101):
	if u > 1:
		u = 1
	Norm = G(a + b + N)/(G(a + M)*G(b + N - M))
	u1 = pow(u, (a - 1 + M))
	u2 = pow(1 - u, (b - 1  + N - M))
	P_Val = Norm * u1 * u2
	P.append(P_Val)
	U.append(u)
	u += 0.010000
	#print(P_Val)

print('%0.2f' %U_ML)
plt.plot(U, P)
plt.xlabel('u')
plt.ylabel('P')

plt.show()
