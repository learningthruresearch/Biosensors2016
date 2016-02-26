#!/usr/bin/python
# coding=utf8

import numpy as np #import the library
import matplotlib.pyplot as plt

time = np.loadtxt('Ethanol_average.txt', usecols= [0]) #open the file and load the columns [0] which is the first

#import of the mean of each concentration of alcohol
E0 = np.loadtxt('Ethanol_average.txt', usecols= [1])
E1 = np.loadtxt('Ethanol_average.txt', usecols= [2])
E2 = np.loadtxt('Ethanol_average.txt', usecols= [3])
E3 = np.loadtxt('Ethanol_average.txt', usecols= [4])
E4 = np.loadtxt('Ethanol_average.txt', usecols= [5])
E5 = np.loadtxt('Ethanol_average.txt', usecols= [6])
N = np.loadtxt('LB_average.txt', usecols= [1])

#standard deviation's import 
sd0 = np.loadtxt('Ethanol_STDEV.txt', usecols= [1])
sd1 = np.loadtxt('Ethanol_STDEV.txt', usecols= [2])
sd2 = np.loadtxt('Ethanol_STDEV.txt', usecols= [3])
sd3 = np.loadtxt('Ethanol_STDEV.txt', usecols= [4])
sd4 = np.loadtxt('Ethanol_STDEV.txt', usecols= [5])
sd5 = np.loadtxt('Ethanol_STDEV.txt', usecols= [6])
sdn = np.loadtxt('LB_STDV.txt', usecols= [1])


plt.xlabel('Time [s]', fontsize = 20) #name of x axis
plt.ylabel('Optic Density [no unit]', fontsize = 20) #name of y axis
plt.title("E.coli's optic density in function of time after a 10 min ethanol shock", fontsize = 26) #title of the graph

plt.errorbar(time,E0, yerr=sd0, color='b', linewidth=1.5) #draw of the error#
plt.errorbar(time,E1, yerr=sd1, color='r', linewidth=1.5)
plt.errorbar(time,E2, yerr=sd2, color='m', linewidth=1.5)
plt.errorbar(time,E3, yerr=sd3, color='g', linewidth=1.5)
plt.errorbar(time,E4, yerr=sd4, color='k', linewidth=1.5)
plt.errorbar(time,E5, yerr=sd5, color='c', linewidth=1.5) 
plt.errorbar(time,N, yerr=sdn, color='maroon', linewidth=1.5)

plt.plot(time,E0, label='100%', color='b', linewidth=2.5) #draw the curve
plt.plot(time,E1, label='70%', color='r', linewidth=2.5)
plt.plot(time,E2, label='60%', color='m', linewidth=2.5)
plt.plot(time,E3, label='50%', color='g', linewidth=2.5)
plt.plot(time,E4, label='40%', color='k', linewidth=2.5)
plt.plot(time,E5, label='30%', color='c', linewidth=2.5)
plt.plot(time, N, label='LB', color='maroon', linewidth=2.5)
plt.legend(loc="upper left") #location of the legend
plt.show()


