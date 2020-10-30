"""
Code that takes data, constrains it, converts to polar, and then plots it (hopefully correctly?)
Also kinda slow - all the code is, honestly, but just an extra warning
"""

import csv
import numpy as np
import math
import matplotlib.pyplot as plt

#make empty data matrix to store data
data = [[]]

with open('fulldata.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = csv.reader(read_obj)
    
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        
        #skip this row if the "radial angle" (modified lat) is too big
        checkRow = (float(row[0]) + 89)
        if checkRow > 0.001 or checkRow < -0.001:
            continue
        
        #variable to store row of data that will be inserted into data matrix
        addRow = []
        #add moded lat & long, and the height to addRow
        for num in range(len(row)-1):
            val = float(row[num])
            
            #change lat so radial angle???
            if (num == 0):
                val += 89
                if val < 0:
                    val *= -1
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
        data.append(addRow)

del data[0]

data = np.array(data)
theta = data[:, 1]
rad = data[:, 0]

for i in range(len(rad)):
    plt.polar(data[i, 1], data[i, 0], '.', markersize=1, color='black')
    