#!/usr/bin/python
# coding=utf8

import numpy as np #import the library
import matplotlib.pyplot as plt

data0ml = np.loadtxt('data0ml.txt', usecols = [0]) #open the file and load data
plot0ml = data0ml[-10:] #take the 10 last values
mean0ml = np.mean(plot0ml) #calculation of the mean

datapg30ml = np.loadtxt('datapg30ml.txt', usecols = [0]) #open the file and load data
pg30ml = datapg30ml[-10]
meanpg30ml = np.mean(pg30ml)

datapg20ml = np.loadtxt('datapg20ml.txt', usecols = [0]) #open the file and load data
pg20ml = datapg20ml[-10]
meanpg20ml = np.mean(pg20ml)

datapg10ml = np.loadtxt('datapg10ml.txt', usecols = [0]) #open the file and load data
pg10ml = datapg10ml[-10]
meanpg10ml = np.mean(pg10ml)

datapg20ypd10ml = np.loadtxt('datapg20ypd10ml.txt', usecols = [0]) #open the file and load data
pg20ypd10ml = datapg20ypd10ml[-10]
meanpg20ypd10ml = np.mean(pg20ypd10ml)

datapg10ypd20ml = np.loadtxt('datapg10ypd20ml.txt', usecols = [0]) #open the file and load data
pg10ypd20ml = datapg10ypd20ml[-10]
meanpg10ypd20ml = np.mean(pg10ypd20ml)

datapg13ypd6ml = np.loadtxt('datapg13ypd6ml.txt', usecols = [0]) #open the file and load data
pg13ypd6ml = datapg13ypd6ml[-10]
meanpg13ypd6ml = np.mean(pg13ypd6ml)

datapg6ypd3ml = np.loadtxt('datapg6ypd3ml.txt', usecols = [0]) #open the file and load data
pg6ypd3ml = datapg6ypd3ml[-10]
meanpg6ypd3ml = np.mean(pg6ypd3ml)

datapg6ypd13ml = np.loadtxt('datapg6ypd13ml.txt', usecols = [0]) #open the file and load data
pg6ypd13ml = datapg6ypd13ml[-10]
meanpg6ypd13ml = np.mean(pg6ypd13ml)

datapg3ypd6ml = np.loadtxt('datapg3ypd6ml.txt', usecols = [0]) #open the file and load data
pg3ypd6ml = datapg3ypd6ml[-10]
meanpg3ypd6ml = np.mean(pg3ypd6ml)

datapg9030ml = np.loadtxt('90%30ml.txt', usecols = [0]) #open the file and load data
pg9030ml = datapg9030ml[-10]
meanpg9030ml = np.mean(pg9030ml)

datapg9020ml = np.loadtxt('90%20ml.txt', usecols = [0]) #open the file and load data
pg9020ml = datapg9020ml[-10]
meanpg9020ml = np.mean(pg9020ml)

datapg9010ml = np.loadtxt('90%10ml.txt', usecols = [0]) #open the file and load data
pg9010ml = datapg9010ml[-10]
meanpg9010ml = np.mean(pg9010ml)

datapg9530ml = np.loadtxt('95%30ml.txt', usecols = [0]) #open the file and load data
pg9530ml = datapg9530ml[-10]
meanpg9530ml = np.mean(pg9530ml)

datapg9520ml = np.loadtxt('95%20ml.txt', usecols = [0]) #open the file and load data
pg9520ml = datapg9520ml[-10]
meanpg9520ml = np.mean(pg9520ml)

datapg9510ml = np.loadtxt('95%10ml.txt', usecols = [0]) #open the file and load data
pg9510ml = datapg9510ml[-10]
meanpg9510ml = np.mean(pg9510ml)

datapg8030ml = np.loadtxt('80%30ml.txt', usecols = [0]) #open the file and load data
pg8030ml = datapg8030ml[-10]
meanpg8030ml = np.mean(pg8030ml)

datapg8020ml = np.loadtxt('80%20ml.txt', usecols = [0]) #open the file and load data
pg8020ml = datapg8020ml[-10]
meanpg8020ml = np.mean(pg8020ml)

datapg8010ml = np.loadtxt('80%10ml.txt', usecols = [0]) #open the file and load data
pg8010ml = datapg8010ml[-10]
meanpg8010ml = np.mean(pg8010ml)

datapg7030ml = np.loadtxt('70%30ml.txt', usecols = [0]) #open the file and load data
pg7030ml = datapg7030ml[-10]
meanpg7030ml = np.mean(pg7030ml)

datapg7020ml = np.loadtxt('70%20ml.txt', usecols = [0]) #open the file and load data
pg7020ml = datapg7020ml[-10]
meanpg7020ml = np.mean(pg7020ml)

datapg7010ml = np.loadtxt('70%10ml.txt', usecols = [0]) #open the file and load data
pg7010ml = datapg7010ml[-10]
meanpg7010ml = np.mean(pg7010ml)

time = range(0,720,2) #values for x axis

x = [33, 66, 70, 80, 90, 95, 100] #propylene glycol concentration
y = [meanpg10ypd20ml, meanpg20ypd10ml, meanpg7030ml, meanpg8030ml, meanpg9030ml, meanpg9530ml, meanpg30ml] #% of humidity
z = [meanpg6ypd13ml, meanpg13ypd6ml, meanpg7020ml, meanpg8020ml, meanpg9020ml, meanpg9520ml, meanpg20ml] #% of humidity
w = [meanpg3ypd6ml, meanpg6ypd3ml, meanpg7010ml, meanpg8010ml, meanpg9010ml, meanpg9510ml, meanpg10ml] #% of humidity

error30ml = [np.std(datapg10ypd20ml[-10:]), np.std(datapg20ypd10ml[-10:]), np.std(datapg7030ml[-10:]), np.std(datapg8030ml[-10:]), np.std(datapg9030ml[-10:]), np.std(datapg9530ml[-10:]), np.std(datapg30ml[-10:])] #caculcalion of the error

error20ml = [np.std(datapg6ypd13ml[-10:]), np.std(datapg13ypd6ml[-10:]), np.std(datapg7020ml[-10:]), np.std(datapg8020ml[-10:]), np.std(datapg9020ml[-10:]), np.std(datapg9520ml[-10:]), np.std(datapg20ml[-10:])] #caculcalion of the error

error10ml = [np.std(datapg3ypd6ml[-10:]), np.std(datapg6ypd3ml[-10:]), np.std(datapg7010ml[-10:]), np.std(datapg8010ml[-10:]), np.std(datapg9010ml[-10:]), np.std(datapg9510ml[-10:]), np.std(datapg10ml[-10:])] #caculcalion of the error

plt.errorbar(x,y, yerr=error30ml, ecolor='k') #draw of the error
plt.errorbar(x,z, yerr=error20ml, ecolor='k') #draw of the error
plt.errorbar(x,w, yerr=error10ml, ecolor='k') #draw of the error

plt.xlabel('Concentration of propylene glycol [%]', fontsize=22) #name of x axis
plt.ylabel('Humidity [%]', fontsize=22) #name of y axis
plt.title('Humidity in function of the propylene glycol concentration', fontsize=22) #title of the graph

'''plt.plot(time, datapg30ml, color='r') #draw the graph
plt.plot(time, datapg20ml, color='g')
plt.plot(time, datapg10ml, color='b')
plt.plot(time, datapg10ml, color='r')
plt.plot(time, datapg6ypd3ml, color='g')
plt.plot(time, datapg3ypd6ml, color= 'b')'''

plt.plot(x,y, color='r', label='30mL') #draw th graph
plt.plot(x,z, color='b', label='20mL')
plt.plot(x,w, color='g', label='10mL')
plt.legend(fontsize=22)
plt.show() #show the graph'''
