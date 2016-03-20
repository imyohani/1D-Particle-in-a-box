# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 14:41:26 2016

@author: Administrator
"""
import numpy as np
import matplotlib.pyplot as plt



#input parameters
target = int(raw_input("Number of states = "))
N = int(raw_input("Steps = "))
h_bar = float(1)
m = float(1)
L = float(2 * 3.141592)
t0 = h_bar**2/(2*m)

#internal parameters
dx = L / float(N)
a = 1 / float(dx*dx)

#prepare hamiltonian matrix
H = np.zeros((N,N))

for i in range(N):
    for j in range(N):
        if i == j:
            H[i,j] = t0*2*a
        elif i == j+1 or j == i+1:
            H[i,j] = t0*(-a)
            
#boundary condition
H[0,0] = 0
H[0,1] = 0
H[1,0] = 0
H[N-1,N-1] = 0
H[N-1,N-2] = 0
H[N-2,N-1] = 0

values, vectors = np.linalg.eig(H)

#sort and plot
vectors_new = np.zeros((N,N))
for i in range(N):
    for j in range(N):
        vectors_new[i][j] = vectors[j][i]
a = []
for i in range(N):
    a.append(values[i])
a.sort()
count = 0;
x = np.zeros((N,1))
for i in range(N):
    x[i] = L / float(N) * float(i)
    
for i in range(N):
    if a[i] == 0:
        continue
    else:
        count = count + 1    
    for j in range(N):
        if count == target and a[i] == values[j]:
            print "# of state : ",count
            print "Eigenvalue : ",a[i]
            plt.plot(x,vectors_new[j])