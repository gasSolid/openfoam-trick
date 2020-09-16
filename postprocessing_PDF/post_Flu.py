#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math

def calc_PDF_Kn (data, n_interval):
    '''
    calc the PDF of data
    '''
    data.sort()
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
    accumu_PDF = 0.0
    for i in range(len(x_axi)):
        if PDF[i] == 0:
            continue
        x_ret.append(x_axi[i])
        y_ret.append(PDF[i])
	if (x_axi[i]<0.1):
            accumu_PDF += PDF[i]

    return x_ret, y_ret, accumu_PDF

def calc_PDF (data, n_interval):
    '''
    calc the PDF of data
    '''
    data.sort()
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
    accumu_PDF = 0.0;
    for i in range(len(x_axi)):
        if PDF[i] == 0:
            continue
        x_ret.append(x_axi[i])
        y_ret.append(PDF[i])
	if (x_axi[i]>1.0):
            accumu_PDF += PDF[i]

    return x_ret, y_ret, accumu_PDF

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
x_axi_Ma_S, PDF_Ma_S, accumu_PDF_Ma_s = calc_PDF(Ma_Savage,n_interval)
x_axi_Ma_dpm, PDF_Ma_dpm, accumu_PDF_Ma_d = calc_PDF(Ma_dpm,n_interval)
x_axi_Kn_f, PDF_Kn_f, accumu_PDF_Kn_f = calc_PDF_Kn(Kn_frac,n_interval)
x_axi_Kn_M, PDF_Kn_M, accumu_PDF_Kn_M = calc_PDF_Kn(Kn_Mag_us,n_interval)
x_axi_Kn_g, PDF_Kn_g, accumu_PDF_Kn_g = calc_PDF_Kn(Kn_gran,n_interval)
x_axi_Is, PDF_Is, accumu_PDF_Is = calc_PDF_Kn(Is,n_interval)

print "P(Knf<0.1) = ", accumu_PDF_Kn_f 
print "P(Knv<0.1) = ", accumu_PDF_Kn_M 
print "P(Kng<0.1) = ", accumu_PDF_Kn_g 
print "P(Is<0.1) = ", accumu_PDF_Is
print "P(Ma_Sa>1) = ", accumu_PDF_Ma_s
print "P(Ma_dpm>1) = ", accumu_PDF_Ma_d

#import csv
#with open("fw_htc.csv","w") as outfile:
#    writer = csv.writer(outfile,delimiter = '\t')
#    writer.writerows(zip(yData1))

fig = plt.figure(num=1, figsize=(16,14))
plt.rc('text',usetex=True)
mpl.rc('font', family='serif', weight = 'bold')

plt.title('FCCUg0.06', size=14)

#plt.xlabel("",size = 14)
#plt.ylabel('PDF', size=14)

#set tick size
#mpl.rcParams['xtick.major.size'] = 20

ax = plt.subplot(3,2,1)
plt.scatter(x_axi_Kn_f, PDF_Kn_f, color='g',  marker='>')
plt.xscale('log')
plt.yscale('log')
plt.xlim(5e-6, 1e1)
plt.ylim(1e-5, 1e-1)
plt.xlabel(r"$\textbf{Kn_{frac}}$",weight = 'bold', size = 14)
plt.ylabel(r"$\textbf{Probability distribution}$", size=14)
plt.text(1e-5,0.03 , r"$\textbf{P = 0.83}$", size = 14)
#tick line size
plt.setp(ax.yaxis.get_ticklines(), 'markeredgewidth', 2)
plt.setp(ax.yaxis.get_minorticklines(), 'markeredgewidth', 1)
plt.setp(ax.xaxis.get_ticklines(), 'markeredgewidth', 2)
plt.setp(ax.xaxis.get_minorticklines(), 'markeredgewidth', 1)
ax.xaxis.get_label().set_weight('black')
#plt.setp(ax.yaxis.get_label(), 'weight', 'bold')

ax = plt.subplot(3,2,2)
plt.scatter(x_axi_Kn_M, PDF_Kn_M, color='c', marker='^')
plt.xscale('log')
plt.yscale('log')
plt.xlim(5e-6, 1e1)
plt.ylim(1e-5, 1e-1)
plt.xlabel(r"$\textbf{Kn_{vel}}$",size = 14)
plt.text(1e-5,0.03 , r"$\textbf{P = 0.88}$", size = 14)
plt.setp(ax.yaxis.get_ticklines(), 'markeredgewidth', 2)
plt.setp(ax.yaxis.get_minorticklines(), 'markeredgewidth', 1)
plt.setp(ax.xaxis.get_ticklines(), 'markeredgewidth', 2)
plt.setp(ax.xaxis.get_minorticklines(), 'markeredgewidth', 1)

ax = plt.subplot(3,2,3)
plt.scatter(x_axi_Kn_g, PDF_Kn_g, color='m', marker='+')
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e-4, 1e1)
plt.ylim(1e-5, 1e-1)
plt.xlabel(r"$\textbf{Kn_{gran}}$",size = 14)
plt.ylabel(r"$\textbf{Probability distribution}$", size=14)
plt.text(2e-4,0.03 , r"$\textbf{P = 0.89}$", size = 14)
plt.setp(ax.yaxis.get_ticklines(), 'markeredgewidth', 2)
plt.setp(ax.yaxis.get_minorticklines(), 'markeredgewidth', 1)
plt.setp(ax.xaxis.get_ticklines(), 'markeredgewidth', 2)
plt.setp(ax.xaxis.get_minorticklines(), 'markeredgewidth', 1)

ax = plt.subplot(3,2,4)
plt.scatter(x_axi_Is, PDF_Is, color='navy', marker='x')
plt.xscale('log')
plt.yscale('log')
plt.xlim(6e-4, 1e1)
plt.ylim(1e-5, 1e-1)
plt.xlabel(r"$\textbf{I_{s}}$",size = 14)
plt.text(2e-3,0.03 , r"$\textbf{P = 0.94}$", size = 14)
plt.setp(ax.yaxis.get_ticklines(), 'markeredgewidth', 2)
plt.setp(ax.yaxis.get_minorticklines(), 'markeredgewidth', 1)
plt.setp(ax.xaxis.get_ticklines(), 'markeredgewidth', 2)
plt.setp(ax.xaxis.get_minorticklines(), 'markeredgewidth', 1)

ax = plt.subplot(3,2,5)
plt.scatter(x_axi_Ma_S, PDF_Ma_S, color='r',  marker='o', label=None)
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e-2, 1e3)
plt.ylim(1e-5, 1e-1)
plt.ylabel(r"$\textbf{Probability distribution}$", size=14)
plt.xlabel(r"$\textbf{Ma}$",size = 14)
plt.text(0.02,0.03 , r"$\textbf{P = 0.63}$", size = 14)
plt.text(10,0.03 , r"$\textbf{Ma (Savage, 1988)}$", size = 14)
plt.setp(ax.yaxis.get_ticklines(), 'markeredgewidth', 2)
plt.setp(ax.yaxis.get_minorticklines(), 'markeredgewidth', 1)
plt.setp(ax.xaxis.get_ticklines(), 'markeredgewidth', 2)
plt.setp(ax.xaxis.get_minorticklines(), 'markeredgewidth', 1)

ax = plt.subplot(3,2,6)
plt.scatter(x_axi_Ma_dpm, PDF_Ma_dpm, color='b',  marker='<', label = None)
plt.xscale('log')
plt.yscale('log')
plt.xlim(5e-2, 1e4)
plt.ylim(1e-5, 1.3e-1)
plt.xlabel(r"$\textbf{Ma}$",size = 14)
plt.text(0.1,0.035 , r"$\textbf{P = 0.99}$", size = 14)
plt.text(10,0.035 , r"$\textbf{Ma (Marchisio and Fox, 2013)}$", size = 14)
plt.setp(ax.yaxis.get_ticklines(), 'markeredgewidth', 2)
plt.setp(ax.yaxis.get_minorticklines(), 'markeredgewidth', 1)
plt.setp(ax.xaxis.get_ticklines(), 'markeredgewidth', 2)
plt.setp(ax.xaxis.get_minorticklines(), 'markeredgewidth', 1)
#I = plt.legend(loc='best')
#I.draw_frame(False)
#plt.legend(frameon = False)



#fig.set_ylabel('Probability distribution', size=14)
plt.show()
plt.savefig('results.png', format='png')

