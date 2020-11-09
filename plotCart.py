"""
Created on Sun Nov  1 22:15:18 2020

@author: JCHAPIN
"""
import csv
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fileName = 'fullcartdatar.csv'
print("fileName: ", fileName)
raw_data = open(fileName, 'rt')
#loadtxt defaults to floats
datarounded = np.loadtxt(raw_data, usecols = (0,1,2,3), delimiter=",")
data = np.around(datarounded, 3)
#find the number of points in the square grid
# I am assuming evenly spaced
points = (int)(math.sqrt(len(data)))
#points = 3032
#find the min and max of the x's and y's

xmax = np.max(data[:,0])
ymax = np.max(data[:,1])
xmin = np.min(data[:,0])
ymin = np.min(data[:,1])

#create a square grid of heights that will be plotted
z = np.zeros((points,points))

#find where the height is in the square grid
#this makes the upper left hand - min x = to the 0 index
#finds the percent that the number is between max and min
#multiplies it by the number of points to find the point on the grid
# if the min was 100 and max was 200 and the point was 150 then
# the indexs would be in the middle of the grid
for row in data:
    x_coordinate =(int)(((row[0]-xmin)/(xmax-xmin)) *(points-1))
    y_coordinate =(int)(((row[1]-ymin)/(ymax-ymin))* (points-1))
    z[x_coordinate][y_coordinate] = row[2]
    #if you want to plot slope
    #z[x_coordinate][y_coordinate] = row[3]
 
#
temp = z[:500,:]

#gets rid of plane of zeros
z[z==0] = np.nan

#plots in 3d
f1 = plt.figure(1)
ax = plt.axes(projection='3d')
X = np.linspace(xmin,xmax,points)
Y = np.linspace(ymin,ymax,points)
Z = z
X,Y = np.meshgrid(X,Y)
ax.plot_surface(X,Y,Z, cmap='viridis')

#plots in 2d
f2 = plt.figure(2)
ax = plt.axes()
X = np.linspace(xmin,xmax,points)
Y = np.linspace(ymin,ymax,points)
Z = z
X,Y = np.meshgrid(X,Y)
ax.contourf(X,Y,Z, cmap='viridis')

#saves the square matrix to a txt file
#np.savetxt('squarefulldata.txt', z, delimiter=',')



 


