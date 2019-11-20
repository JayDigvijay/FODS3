# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 20:17:21 2019

@author: Digvijay Singh
"""
import numpy as np 
#import scipy as sp 
import matplotlib.pyplot as plt 
from scipy.special import gamma as G

## M = Number of Heads in Randomly Generated Sample. 
k = 0.5
a = 2 * k
b = 3 * k
u = 0
N = 160
M = 80
L = N - M
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
	Norm = G(a + b + N)/(G(a + M)*G(b + L))
	u1 = pow(u, (a - 1 + M))
	u2 = pow(1 - u, (b - 1  + L))
	P_Val = Norm * u1 * u2
	P.append(P_Val)
	U.append(u)
	u += 0.010000
	#print(Norm)
print('%0.2f' %U_ML)

fig = plt.figure()
plt.plot(U, P)
plt.ion()
plt.xlabel('μ')
plt.ylabel('P')
plt.show()
plt.pause(0.1)
plt.close()
fig.savefig('Final Graph.png')

