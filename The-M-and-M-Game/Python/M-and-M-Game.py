# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 19:54:17 2022
@file-name: M-and-M-Game.py

@author: Charlie

@version: 1.0

@date: 03/01/2022

@description: Generates a visual of 56 randomly assigned colours within the M&M Colour Pallette
                Done as first stoic challenge.
"""

#Import Libraries
import matplotlib.pyplot as plt
import random
import pandas as pd

#Generate X & Y Axes
xaxis = [i for i in range(1,9)]
yaxis = [i for i in range(1,8)]

#Assign Hex Code Colour Palette
colours = {'red':'#b11224', 'yellow' : '#fff200', 'blue' : '#2f9fd7',\
           'green' : '#31ac55', 'orange' : '#f26f22', 'brown' : '#603a34'}

#Instantiates Empty Lists
valx = []
valy = []
sweets = []

#Populates X&Y Axis Values.
for x in xaxis:
      for y in yaxis:
          valx.append(x)
          valy.append(y)
          sweets.append(random.choice(['red', 'yellow', 'blue', 'green',\
                                       'orange', 'brown']))
#Create Pandas DataFrame to hold each value with corresponding colour key.              
df = pd.DataFrame({'X-Value': valx, 'Y-Value': valy, 'Sweet-Colour':sweets})

#Produces the Plot
fig, ax = plt.subplots()
ax.scatter(df['X-Value'], df['Y-Value'], c=df['Sweet-Colour'].map(colours))
plt.axis('off')
plt.title('Stoic Challenge: The M&M Game')
plt.show()