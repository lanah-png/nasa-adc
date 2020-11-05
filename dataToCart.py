# -*- coding: utf-8 -*-
"""
convert full data to cartesian and put in a txt file
"""

import csv
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

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

#puts cart data together w/ height and slope
dataC = np.hstack(((rad * np.cos(theta)).reshape(len(dataP),1), (rad * np.sin(theta)).reshape(len(dataP), 1), dataP[:,2:]))

#rounds data
#dataCRound = np.around(dataC, 3)

#saves unrounded data
np.savetxt('fullcartdata.txt', dataC, delimiter=',')
#saves rounded data
#np.savetxt('fullcartdatar.txt', dataCRound, delimiter=',')
