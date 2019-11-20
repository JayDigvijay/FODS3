#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Tue Nov 19 15:15:39 2019

@author: Digvijay Singh
"""
import numpy as np
# import scipy as sp
import matplotlib.pyplot as plt
from scipy.special import gamma as G




k = 1
a = 2 * k
b = 3 * k
u = 0
N = 160
M = np.random.randint(1, 161)
while M >= 0.4 * 160 and M <= 0.6 * 160:
    M = np.random.randint(1, 161)
L = N - M
arr = np.array([0] * (N - M) + [1] * M)
np.random.shuffle(arr)

images = []
P = []
U = []
m = 0
l = 0
MaxP = 0
# print(G(2.5))
# print(arr)

U_ML = M / 160.00
print ('%0.2f' % U_ML)

for j in range(len(arr)):
    P = []
    U = []
    u = 0

    for i in range(101):
        if u > 1:
            u = 1
        Norm = G(a + b + l + m) / (G(a + m) * G(b + l))
        u1 = pow(u, a - 1 + m)
        u2 = pow(1 - u, b - 1 + l)
        P_Val = Norm * u1 * u2
        if MaxP < P_Val:
            MaxP = P_Val
        P.append(P_Val)
        U.append(u)
        u += 0.010000

        # print(Norm)



        # #print(m/160.0)
    fig = plt.figure()
    plt.plot(U, P)
    plt.ion()
    plt.axis([0, 1, 0, 30])
    plt.xlabel('μ ' + '(Points sampled = ' + str(j + 1) + ')')
    plt.ylabel('Prior (β)')
    plt.text(0.4, 27, 'μML = ' + str(U_ML))
    fig.savefig('Image Data/plot' + str(j+1) + '.png')

   
    if arr[j] == 1:
        m += 1
    else:
        l += 1

		