#!usr/bin/python3
# -*- coding: utf-8 -*-

#we import all needed libraries
import numpy as np  
import matplotlib.pyplot as plt
from scipy import stats
import pylab as pl

def lecture(fichier):#we open the file containing all data and we convert it into an array (matrix)
	l=np.loadtxt(fichier)
	return l
        fichier.close()

def nom(array): #we create one array for each tested conditions (containing data from 5 replicates)
	D=np.transpose(array)
	Z=D[0]
	nbRFPt1=D[1:6]
	szRFPt1=D[6:11]
	nbCRFPt1=D[11:16]
	szCRFPt1=D[16:21]
	nbRFPt2=D[21:26]
	szRFPt2=D[26:31]
	nbCRFPt2=D[31:36]
	szCRFPt2=D[36:41]
	nbRFPt3=D[41:46]
	szRFPt3=D[46:51]
	nbCRFPt3=D[51:56]
	szCRFPt3=D[56:61]
	return Z, nbRFPt1, szRFPt1, nbCRFPt1, szCRFPt1, nbRFPt2, szRFPt2, nbCRFPt2, szCRFPt2, nbRFPt3, szRFPt3, nbCRFPt3, szCRFPt3

def coeff(zone, nb, size): #we calulate the response coefficient 
	prod=zone**2*nb*size  #we first multiply area number (square) by number of colony and size of colonies for each replicates
	#print prod
	somme=np.sum(prod, axis=1) #then we sum the result of the multiplication from each area
	stddev = np.std(somme, axis=0) #we calcultate standard deviation on this value (value of 5 replicates)
	coeff=np.mean(somme) #we take the mean value to plot
	#print coeff
	return coeff, stddev

def graph(x,y,numfig,a, b, titre,labelx,labely,stddev): # this function will create the graphs: it takes as parameters the list to plot in the x axis, in the y axis, the number of the figure in which the graph has to be drawn, the name of the x axis, the name of the y axis, and the standard deviation on y to draw error bars
        plt.figure(numfig)
        plt.title(titre, fontsize=20)
        plt.xlabel(labelx, fontsize=16)
        #plt.axis([-10, 190,-20, 140])
        plt.ylabel(labely, fontsize=16)
	#plt.xscale("log", fontsize=16)
	#plt.yscale("log", fontsize=16)
        plt.plot(x,y,c=a, label=b)
        pl.errorbar(x,y,yerr=stddev, c=a)
	plt.legend()

def moyenne(array): #we calculate a mean and the standard deviation on the value from 5 replicates
	stddev = np.std(array, axis=0)
	somme=np.sum(array, axis=0)
	nomarray=somme/5
	#print nomarray
	return nomarray, stddev

def normalizesize(array): #this function can normalize coloniies' sizes but we do not use it here
	for i in range(len(array[1])):
		for k in range(len(array)):
			if array[k][i]<2.5:
				array[k][i]=1
			elif array[k][i]<5:
				array[k][i]=2
			else:
				array[k][i]=4
	return array


def main():
	l=lecture("RFPdata.tsv") #we upload data from the file
	Z, nbRFPt1, szRFPt1, nbCRFPt1, szCRFPt1, nbRFPt2, szRFPt2, nbCRFPt2, szCRFPt2, nbRFPt3, szRFPt3, nbCRFPt3, szCRFPt3=nom(l) #we create all needed matrix
#normalisation of size
	#NszRFPt1=normalizesize(szRFPt1)
	#NszRFPt2=normalizesize(szRFPt2)
	#NszRFPt3=normalizesize(szRFPt3)

#we calculate the response coefficient for the three times
	coeffRFPt1, stddevt1=coeff(Z, nbRFPt1, szRFPt1) 
	coeffRFPt2, stddevt2=coeff(Z, nbRFPt2, szRFPt2)
	coeffRFPt3, stddevt3=coeff(Z, nbRFPt3, szRFPt3)
#we create a matrix with this 3 value and 0 for the origin
	coeffRFP=np.array([0, coeffRFPt1, coeffRFPt2, coeffRFPt3])
	stddev=np.array([0, stddevt1, stddevt2, stddevt3])
#we create a matriw with the time values
	X=[0, 15, 23, 40]
#we plot response coefficient as a function of time 
	graph(X, coeffRFP, 1, 'r', 'RFP strain', "Gradient response of RFP as a function of time", "Time (h)", "Response coefficient (colony.zone.normalizedsize)", stddev)
        plt.axis([0, 45, 0, 2000])

#we do the same for control 
	coeffCRFPt1, stddevCt1=coeff(Z, nbCRFPt1, szCRFPt1)
	coeffCRFPt2, stddevCt2=coeff(Z, nbCRFPt2, szCRFPt2)
	coeffCRFPt3, stddevCt3=coeff(Z, nbCRFPt3, szCRFPt3)
	coeffCRFP=np.array([0,coeffCRFPt1, coeffCRFPt2, coeffCRFPt3])
	stddevC=np.array([0,stddevCt1, stddevCt2, stddevCt3])
	X=[0, 15, 23, 40]
	graph(X, coeffCRFP, 1, 'b', 'RFP strain, control', "Gradient response of RFP as a function of time", "Time (h)", "Response coefficient (colony.zone.normalizedsize)", stddevC)
        plt.axis([0, 45, 0, 2000])

#we calcultae the mean number of colony per area at three times
	moynbRFPt1, stddevnbt1=moyenne(nbRFPt1)
	print moynbRFPt1
	moynbRFPt2, stddevnbt2=moyenne(nbRFPt2)
	print moynbRFPt2
	moynbRFPt3, stddevnbt3=moyenne(nbRFPt3)
	print moynbRFPt3
	moynbRFP=np.array([moynbRFPt1, moynbRFPt2, moynbRFPt3])
	#x=np.argmax(moynbRFP, axis=0)
	#maxi=np.max(moynbRFP, axis=1)
	#print maxi
	#print x
	#slope, intercept, r_value, p_value, std_err=stats.linregress(x,maxi)
	#print r_value
#we plot the graph of the number of colony depending on area number at three different times on the same graph
	graph(Z, moynbRFPt1, 2, 'g', 't=15h', "Number of colonies depending on nutrient gradient at three distinct times", "Zone number", "Number of colonies", stddevnbt1)
	graph(Z, moynbRFPt2, 2, 'b', 't=23h', "Number of colonies depending on nutrient gradient at three distinct times", "Zone number", "Number of colonies", stddevnbt2)
	graph(Z, moynbRFPt3, 2, 'y', 't=40h', "Number of colonies depending on nutrient gradient at three distinct times", "Zone number", "Number of colonies", stddevnbt3)

#we do the same for number control
	moynbCRFPt1, stddevnbCt1=moyenne(nbCRFPt1)
	moynbCRFPt2, stddevnbCt2=moyenne(nbCRFPt2)
	moynbCRFPt3, stddevnbCt3=moyenne(nbCRFPt3)
	moynbCRFP=np.array([moynbCRFPt1, moynbCRFPt2, moynbCRFPt3])
	x=np.argmax(moynbCRFP, axis=0)
	maxi=np.max(moynbCRFP, axis=1)
	#print maxi
	#print x
	#slope, intercept, r_value, p_value, std_err=stats.linregress(x,maxi)
	#print r_value
	graph(Z, moynbCRFPt1, 3, 'g', 't=15h', "Number of colonies depending on nutrient gradient at three distinct times, controls", "Zone number", "Number of colonies", stddevnbCt1)
	graph(Z, moynbCRFPt2, 3, 'b', 't=23h', "Number of colonies depending on nutrient gradient at three distinct times, controls", "Zone number", "Number of colonies", stddevnbCt2)
	graph(Z, moynbCRFPt3, 3, 'y', 't=40h', "Number of colonies depending on nutrient gradient at three distinct times, controls", "Zone number", "Number of colonies", stddevnbCt3)
        plt.axis([1, 5, -5, 30])
	#graph(x, maxi, 2, 'r', "Gradient response of RFP versus time", "time(h)", "Response coefficient (colony.zone.size)", stddevnbt3)
	plt.show()

#we do the same for size of colony
	moyszRFPt1, stddevszt1=moyenne(szRFPt1)
	print moyszRFPt1
	moyszRFPt2, stddevszt2=moyenne(szRFPt2)
	print moyszRFPt2
	moyszRFPt3, stddevszt3=moyenne(szRFPt3)
	print moyszRFPt3
	moyszRFP=np.array([moyszRFPt1, moyszRFPt2, moyszRFPt3])
	q=np.argmax(moyszRFP, axis=0)
	maxi=np.max(moyszRFP, axis=1)
	#print maxi
	#print q
	#slope, intercept, r_value, p_value, std_err=stats.linregress(x,maxi)
	#print r_value
	graph(Z, moyszRFPt1, 4, 'g', 't=15h', "Size of colonies depending on nutrient gradient at three distinct times", "Zone number", "Normalized size of colonies (arbitrary units)", stddevszt1)
	graph(Z, moyszRFPt2, 4, 'b', 't=23h', "Size of colonies depending on nutrient gradient at three distinct times", "Zone number", "Normalized size of colonies (arbitrary units)", stddevszt2)
	graph(Z, moyszRFPt3, 4, 'y', 't=40h', "Size of colonies depending on nutrient gradient at three distinct times", "Zone number", "Normalized size of colonies (arbitrary units)", stddevszt3)
	#graph(q, maxi, 2, 'r', "Gradient response of RFP versus time", "time(h)", "Response coefficient (colony.zone.size)", stddevnbt3)

#we do the same for size control
	moyszCRFPt1, stddevszCt1=moyenne(szCRFPt1)
	moyszCRFPt2, stddevszCt2=moyenne(szCRFPt2)
	moyszCRFPt3, stddevszCt3=moyenne(szCRFPt3)
	moyszCRFP=np.array([moyszCRFPt1, moyszCRFPt2, moyszCRFPt3])
	q=np.argmax(moyszRFP, axis=0)
	maxi=np.max(moyszRFP, axis=1)
	#print maxi
	#print q
	#slope, intercept, r_value, p_value, std_err=stats.linregress(x,maxi)
	#print r_value
	graph(Z, moyszCRFPt1, 5, 'g', 't=15h', "Size of colonies depending on nutrient gradient at three distinct times, controls", "Zone number", "Normalized size of colonies (arbitrary units)", stddevszCt1)
	graph(Z, moyszCRFPt2, 5, 'b', 't=23h', "Size of colonies depending on nutrient gradient at three distinct times, controls", "Zone number", "Normalized size of colonies (arbitrary units)", stddevszCt2)
	graph(Z, moyszCRFPt3, 5, 'y', 't=40h', "Size of colonies depending on nutrient gradient at three distinct times, controls", "Zone number", "Normalized size of colonies (arbitrary units)", stddevszCt3)
        plt.axis([1, 5, -2, 10])
	plt.show()
main()
	
