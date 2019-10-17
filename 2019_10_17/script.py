# -*- coding: utf-8 -*-

import time
import numpy as np
import pandas as pd

#from timeit import default_timer as timer
#
#start1 = timer()
#
#a = 2.7
#b = 3.14
#c = a**b
##print(c)
#end1 = timer()
#gesamt1 = end1 - start1
#
#
#
#start2 = timer()
#
#a = 2.7
#b = 3.14
#c = np.power(a,b)
##print(c)
#
#end2 = timer()
#gesamt2 = end2 - start2
#
#
#if gesamt1 < gesamt2:
#    print("python ist schneller als numpy")
#else:
#    print("numpy ist schneller als python")



data = pd.read_csv('president_heights.csv')
#print(data)
heights = np.array(data['height(cm)'])

x = data.sort_values(by=['height(cm)'])
print(type(x))
print(x)

#print(heights)

#print("Durchschnittsgröße:", heights.mean())
#print("Standardabweichung:", heights.std())
#print("Minimale Größe :", heights.min())
#print("Maximale Größe :", heights.max())
#print("Unteres Quartil:", np.percentile(heights, 25))
#print("Median: ", np.percentile(heights, 50))
#print("Oberes Quartil: ", np.percentile(heights, 75))

import matplotlib.pyplot as plt
plt.hist(heights)
plt.show()
