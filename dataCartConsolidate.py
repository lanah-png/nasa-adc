# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 00:12:17 2020

@author: 834140
"""
import csv
import numpy as np
import math
import matplotlib.pyplot as plt

def consolidate_points(data):
    x_d = {}
    y_d = {}
    for row in data:
        x = row[0]
        y = row[1]
        h = row[2]
        s = row[3]
        if x in x_d:
            temp_d = {x_d[x]}
            if y in temp_d:
                temp_d[y][0].append(h)
                temp_d[y][1].append(s)
            else:
                temp_d[y] = [[h], [s]]
        else:
            x_d[x] = {y: [[h], [s]]}
    return x_d

#make empty data matrix to store data
dataP = [[]]

fileName = 'fullcartdata.csv'
print("fileName: ", fileName)
raw_data = open(fileName, 'rt')
#loadtxt defaults to floats
dataRounded = np.loadtxt(raw_data, usecols = (0,1,2,3), delimiter=",")
                
dataCShort = consolidate_points(dataRounded)

# def down_sample(x, f=2400):
#     # pad to a multiple of f, so we can reshape
#     # use nan for padding, so we needn't worry about denominator in
#     # last chunk
#     xp = np.r_[x, math.nan + np.zeros((-len(x) % f,))]
#     # reshape, so each chunk gets its own row, and then take mean
#     return np.nanmean(xp.reshape(-1, f), axis=-1)

# dataCShortX = down_sample(dataCRound[:, 0])
# dataCShortY = down_sample(dataCRound[:, 1])
# dataCShortH = down_sample(dataCRound[:, 2])
# dataCShortS = down_sample(dataCRound[:, 3])

# dataCShort = np.hstack((dataCShortX.reshape(3010,1), dataCShortY.reshape(3010,1),dataCShortH.reshape(3010,1),dataCShortS.reshape(3010,1)))

