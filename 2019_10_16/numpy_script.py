# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

cvalues = [20.1, 20.8, 21.9,22.5, 22.7, 21.8, 21.3, 20.9, 20.1]

C_Liste = np.array(cvalues)
F_Liste = C_Liste * 9 / 5 + 32

print(C_Liste)
print(F_Liste)

plt.plot(C_Liste)
plt.plot(F_Liste)
#plt.show()

#plt.savefig("Bla.png")

A = np.array([ [1, 2, 3], 
               [4, 5, 6],
               [7, 8, 9]  ])


#B = np.ones((3,3))
B = np.array([ [2], 
               [1],
               [2] ])


C = A*B

print(A)
print(np.shape(A))
print()

print(B)
print(np.shape(B))
print()
print(C)
print(np.shape(C))
