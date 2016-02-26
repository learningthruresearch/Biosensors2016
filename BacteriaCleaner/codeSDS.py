#!/usr/bin/python
# coding=utf8

import numpy as np #import the library
import matplotlib.pyplot as plt

time = np.loadtxt('Ethanol_average.txt', usecols= [0]) #open the file and load the columns [0] which is the first

S0 = np.loadtxt('SDS_average.txt', usecols= [1])
S1 = np.loadtxt('SDS_average.txt', usecols= [2])
S2 = np.loadtxt('SDS_average.txt', usecols= [3])
S3 = np.loadtxt('SDS_average.txt', usecols= [4])
S4 = np.loadtxt('SDS_average.txt', usecols= [5])
S5 = np.loadtxt('SDS_average.txt', usecols= [6])
N = np.loadtxt('LB_average.txt', usecols= [1])


sd0 = np.loadtxt('SDS_STDEV.txt', usecols= [1])
sd1 = np.loadtxt('SDS_STDEV.txt', usecols= [2])
sd2 = np.loadtxt('SDS_STDEV.txt', usecols= [3])
sd3 = np.loadtxt('SDS_STDEV.txt', usecols= [4])
sd4 = np.loadtxt('SDS_STDEV.txt', usecols= [5])
sd5 = np.loadtxt('SDS_STDEV.txt', usecols= [6])
sdn = np.loadtxt('LB_STDV.txt', usecols= [1])

plt.xlabel('Time [s]', fontsize = 20) #name of x axis
plt.ylabel('Optic Density [no unit]', fontsize = 20) #name of y axis
plt.title("E.coli's optic density in function of time after a 10 min SDS shock", fontsize = 26) #title of the graph

#plt.errorbar(time,S0, yerr=sd0, color='b', linewidth=1.5) #draw of the error#
#plt.errorbar(time,S1, yerr=sd1, color='r', linewidth=1.5)
#plt.errorbar(time,S2, yerr=sd2, color='m', linewidth=1.5)
#plt.errorbar(time,S3, yerr=sd3, color='g', linewidth=1.5)
#plt.errorbar(time,S4, yerr=sd4, color='k', linewidth=1.5)
#plt.errorbar(time,S5, yerr=sd5, color='c', linewidth=1.5)
#plt.errorbar(time,N, yerr=sdn, color='maroon', linewidth=1.5) 

plt.plot(time,S0, label='1%', color='b', linewidth=2.5) #draw the curve
plt.plot(time,S1, label='0,1%', color='r', linewidth=2.5)
plt.plot(time,S2, label='0,01%', color='m', linewidth=2.5)
plt.plot(time,S3, label='0,001%', color='g', linewidth=2.5)
plt.plot(time,S4, label='0,0001%', color='k', linewidth=2.5)
plt.plot(time,S5, label='0,00001%', color='c', linewidth=2.5)
plt.plot(time,N, label='LB', color='maroon', linewidth=2.5)
plt.legend(loc="lower left") #location of the legend
plt.show()


