# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 16:52:59 2022

@author: CFitz

@filename: PostureChallenge.py

@description: Graphical representation of deteriorating posture.

@version-history:
|    ver        |    date    |   author    |     comment       |
|   v1.0        | 07/01/2022 |    CMF      |  Initial Version  |
"""

import matplotlib.pyplot as plt
import math

height = (6.1,0.0)
stand = (1,1)

x = [-1,-1,-1, -1, -0.9]
y = [6.1, 3.05, 1.525 ,0.0, 0.0]
graphs = []

count = 0

labels = {1 : "Now", 2 : "+5 Years", 3 : "+10 Years", 4 : "+15 Years", 5 : "+20 Years"}

for i in range(5):
    plt.scatter(x,y)
    plt.plot(x,y)
    x[0] = x[0] + math.sqrt(0.04)
    y[0] = y[0] - 0.04    