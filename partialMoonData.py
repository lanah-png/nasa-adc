"""
Code to just get latitude, longitude, and height into a txt file
"""

import csv
import numpy as np

#create/overwrite txt file to store data
f = open("smallermoondata.txt", "w")

with open('moondata.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = csv.reader(read_obj)
    
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        
        #variable to store string that will be inserted into the txt file
        addRow = ''
        #add latitude and longitude in this row of csv to addRow variable, separated by commas
        for num in range(len(row)-2):
            addRow += str(row[num]) + ','
        #add height to addRow variable and create new line after
        addRow += str(row[len(row)-2]) + '\n'
        
        #add lat, long, height to txt file in one line
        f.write(addRow)

#close txt file to save changes
f.close()
        
