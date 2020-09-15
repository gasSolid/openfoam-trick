#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import math

def calc_PDF_Kn (data, n_interval):
    '''
    calc the PDF of data
    '''
    data.sort()
    count = 0
    for i in range(len(data)):
        if data[i] > 0:
            x_min = math.log10(data[i])
            break

    #x_max = data[-1]
    #x_min = data[0]
    x_max = math.log10(data[-1]);
    interval = (x_max - x_min) / n_interval 

    PF = [0]*(n_interval);
    for i in data:
        if i == 0 or i >= 10 :
            continue
        tmp_log = math.log10(i)
        #tmp_log = i
        index = int((tmp_log-x_min)/interval)
        PF[index] += 1

    sum_PF = sum(PF)

    # PDF
    PDF = [0.0]*(n_interval);
    for i in range(len(PF)):
        PDF[i] = PF[i]/float(sum_PF)

    x_axi = [0.0]*(n_interval);
    for i in range(len(PF)):
        x_axi[i] = math.pow(10.0,(interval*(i+0.5)+x_min))
	#print x_axi[i],' ', PDF[i], i

    x_ret = []
    y_ret = []
    for i in range(len(x_axi)):
        if PDF[i] == 0:
            continue
        x_ret.append(x_axi[i])
        y_ret.append(PDF[i])

    return x_ret, y_ret

def calc_PDF (data, n_interval):
    '''
    calc the PDF of data
    '''
    data.sort()
    count = 0
    for i in range(len(data)):
        if data[i] > 0:
            x_min = math.log10(data[i])
            break

    #x_max = data[-1]
    #x_min = data[0]
    x_max = math.log10(data[-1]);
    interval = (x_max - x_min) / n_interval 

    PF = [0]*(n_interval+1);
    for i in data:
        if i == 0 :
            continue
        tmp_log = math.log10(i)
        #tmp_log = i
        index = int((tmp_log-x_min)/interval)
        PF[index] += 1

    sum_PF = sum(PF)

    # PDF
    PDF = [0.0]*(n_interval+1);
    for i in range(len(PF)):
        PDF[i] = PF[i]/float(sum_PF)

    x_axi = [0.0]*(n_interval+1);
    for i in range(len(PF)):
        x_axi[i] = math.pow(10.0,(interval*(i+0.5)+x_min))

    x_ret = []
    y_ret = []
    for i in range(len(x_axi)):
        if PDF[i] == 0:
            continue
        x_ret.append(x_axi[i])
        y_ret.append(PDF[i])

    return x_ret, y_ret

#reading data
file = open("all.data","rb")
n_interval=300;
Ma_Savage = []
Ma_dpm = []
Kn_frac = []
Kn_Mag_us = []
Kn_gran = []
Is = []

for line in file.readlines():
    point = line.split('\t')
    x = float(point[0])
    x1 = float(point[1])
    x2 = float(point[2])
    x3 = float(point[3])
    x4 = float(point[4])
    x5 = float(point[5])
    Ma_Savage.append(x)
    Ma_dpm.append(x1)
    Kn_frac.append(x2)
    Kn_Mag_us.append(x3)
    Kn_gran.append(x4)
    Is.append(x5)

# calc PDF
x_axi_Ma_S, PDF_Ma_S = calc_PDF(Ma_Savage,n_interval)
x_axi_Ma_dpm, PDF_Ma_dpm = calc_PDF(Ma_dpm,n_interval)
x_axi_Kn_f, PDF_Kn_f = calc_PDF_Kn(Kn_frac,n_interval)
x_axi_Kn_M, PDF_Kn_M = calc_PDF_Kn(Kn_Mag_us,n_interval)
x_axi_Kn_g, PDF_Kn_g = calc_PDF_Kn(Kn_gran,n_interval)
x_axi_Is, PDF_Is = calc_PDF_Kn(Is,n_interval)

#import csv
#with open("fw_htc.csv","w") as outfile:
#    writer = csv.writer(outfile,delimiter = '\t')
#    writer.writerows(zip(yData1))

fig = plt.figure(num=1, figsize=(16,12))
plt.rc('text',usetex=True)
plt.rc('font',family='serif')

#plt.title('FCCUg0.06', size=14)
#plt.xlabel("",size = 14)
#plt.ylabel('PDF', size=14)
#laTex example
#plt.xlabel(r"$\theta^ \circ$",size = 14)


plt.subplot(3,2,1)
plt.scatter(x_axi_Kn_f, PDF_Kn_f, color='g',  marker='>')
plt.xscale('log')
plt.yscale('log')
plt.xlim(5e-6, 1e1)
plt.ylim(1e-5, 1e-1)
plt.xlabel("Kn_{frac}",size = 14)
plt.ylabel('Probability distribution', size=14)

plt.subplot(3,2,2)
plt.scatter(x_axi_Kn_M, PDF_Kn_M, color='c', marker='^')
plt.xscale('log')
plt.yscale('log')
plt.xlim(5e-6, 1e1)
plt.ylim(1e-5, 1e-1)
plt.xlabel("Kn_{vel}",size = 14)

plt.subplot(3,2,3)
plt.scatter(x_axi_Kn_g, PDF_Kn_g, color='m', marker='+')
plt.xscale('log')
plt.yscale('log')
plt.xlim(5e-5, 1e1)
plt.ylim(1e-5, 1e-1)
plt.xlabel("Kn_{gran}",size = 14)
plt.ylabel('Probability distribution', size=14)

plt.subplot(3,2,4)
plt.scatter(x_axi_Is, PDF_Is, color='navy', marker='x')
plt.xscale('log')
plt.yscale('log')
plt.xlim(6e-4, 1e1)
plt.ylim(1e-5, 1e-1)
plt.xlabel("I_{s}",size = 14)

plt.subplot(3,2,5)
plt.scatter(x_axi_Ma_S, PDF_Ma_S, color='r',  marker='o', label=None)
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e-2, 1e3)
plt.ylim(1e-5, 1e-1)
plt.ylabel('Probability distribution', size=14)
plt.xlabel("Ma",size = 14)
#I = plt.legend(loc='best')
#I.draw_frame(False)
plt.text(2,0.03 , "Ma (Marchisio and Fox, 2013)", size = 14)
#plt.legend(frameon = False)

plt.subplot(3,2,6)
plt.scatter(x_axi_Ma_dpm, PDF_Ma_dpm, color='b',  marker='<', label = None)
plt.xscale('log')
plt.yscale('log')
plt.xlim(5e-2, 1e4)
plt.ylim(1e-5, 1e-1)
plt.xlabel("Ma",size = 14)
#I = plt.legend(loc='best')
#I.draw_frame(False)
#plt.legend(frameon = False)
plt.text(200,0.03 , "Ma (Savage, 1988)", size = 14)

#fig.set_ylabel('Probability distribution', size=14)
plt.show()
plt.savefig('results.png', format='png')

