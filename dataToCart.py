# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 18:59:53 2020

@author: 834140
"""

import csv
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def plot(inData):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    
    # Plot the surface.
    surf = ax.plot_surface(inData[:, 0], inData[:, 1], inData[:, 2], cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    
    # Customize the z axis.
    #ax.set_zlim(-1.01, 1.01)
    #ax.zaxis.set_major_locator(LinearLocator(10))
    #ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    
    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    
    plt.show()

#make empty data matrix to store data
dataP = [[]]

with open('fulldata.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = csv.reader(read_obj)
    
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        
        #variable to store row of data that will be inserted into data matrix
        addRow = []
        #add moded lat & long, and the height & slope to addRow
        for num in range(len(row)):
            val = float(row[num])
            
            #change lat so radial angle???
            if (num == 0):
                val += 90
            #change long so azimuth angle (just but between 0 & 360 and then radians)
            elif (num == 1):
                if (val < 0):
                    val += 360
                elif (val > 360):
                    val -= 360
                val = math.radians(val)
            
            #add value into addRow
            addRow.append(val)
        
        #add lat, long, height as a row in data matrix
        dataP.append(addRow)

#delete empty matrix row
del dataP[0]

dataP = np.array(dataP)
theta = dataP[:, 1]
rad = dataP[:, 0]

dataC = np.hstack(((rad * np.cos(theta)).reshape(7223208,1), (rad * np.sin(theta)).reshape(7223208, 1), dataP[:,2:]))
dataCRound = np.around(dataC, 3)

#np.savetxt('fullcartdata.csv', dataCRound, delimiter=',')

plot(dataCRound[0:10000,:])

