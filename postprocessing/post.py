#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

file = open("postprocessing.out","rb")
a = []
for line in file.readlines():
    point = line.split('\t')
    x = float(point[0])
    y = float(point[1])
    point_as_array = [x,y]
    a.append(point_as_array)
#print a

xData = [row[0] for row in a]
yData = [row[1] for row in a]

plt.figure(num=1, figsize=(8,6))
plt.rc('text',usetex=True)
plt.rc('font',family='serif')

plt.title('Solid fraction ', size=14)

plt.xlabel("Height, H",size = 14)

plt.ylabel(r"Solid fraction, $\varepsilon$", size=14)

plt.plot(xData, yData, color='r', linestyle='-', marker='o', label='Present study')
plt.legend(loc='upper left')
#plt.ylim(100,190)

plt.savefig('solidfraction.png', format='png', dpi=300)
