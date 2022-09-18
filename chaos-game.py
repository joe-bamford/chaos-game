# -*- coding: utf-8 -*-
"""
Created on Thu May  7 12:36:43 2020

@author: bamjoe

Customisable fractal generator based on a chaos game simulation inside an n-gon.
"""

from graphics import *
from random import randint
import numpy as np
import keyboard as kb
from contextlib import suppress as sp

#%% WELCOME AND INPUTS

print('Fractal generator by bamjoe. Press Q at any time to exit.')

# Choose border shape
n = 0
while not 3 <= n <= 50:
    try:
        n = int(input('Enter # of sides for border shape (integer, 3 <= n <= 50): '))
    except ValueError:
        continue
                  
# Choose distance to travel along each midpoint-vertex vector.
ratio = 0
while not 0 < ratio < 1:
    try:
        ratio = 1 - float(input('Enter ratio (0 < r < 1): '))
    except ValueError:
        continue
    
# Choose whether to disable the same-vertex rule.
vrule = ''
while not (vrule == 'y' or vrule == 'n' or vrule == 'Y' or vrule == 'N'):
    try:
        vrule = str(input('Enable vertex rule? (y/n): '))
    except ValueError:
        continue

#%% CALCULATIONS & SETUP

# Calculate positions of n points of shape from the nth roots of unity 
vertices = np.empty((n,2))
m = 1
r = 500
while m <= n:
    vt = np.rint(np.array([-r*np.cos(2*np.pi*m/n), r*np.sin(2*np.pi*m/n)]))
    vertices[m-1] = vt
    m += 1    

# Convert vertex vectors to points which the graphics library can understand, also store in a list for later
i = 0
points = []
plist = [] 
for i in range(n):
    point = vertices[i] + 500
    pvec = Point(point[0],point[1])
    points.append(pvec)
    plist.append(point.tolist())

# Select random initial point then check it lies inside shape
a = 0
tick = 1
while a == 0:
    initp = np.random.randint(1,999,size=(1,2))[0]
    initc = initp - 500
    initcmod = np.linalg.norm(initc)
    theta = np.arange(0, 2*np.pi, 0.001)
    rarr = np.abs(1/(np.cos(theta - (2*np.pi/n)*np.floor(n/(2*np.pi)*(theta + np.pi/n)))))
    rmax = np.max(rarr)
    
    phi = np.arctan2(initc[1],initc[0])
    # A gorgeous little polar function to draw any polygon, this is used for edge detection
    r1 = (500/rmax)*np.abs(1/(np.cos(phi - (2*np.pi/n)*np.floor(n/(2*np.pi)*(phi + np.pi/n)))))
    
    if initcmod <= r1:
        a = 1
        print('\nAttempt',tick,'successful, proceeding...')
    else:
        a = 0
        print('\nAttempt',tick,'failed, regenerating...')
        tick += 1

#%% SET UP DRAWING

# Draw window
win = GraphWin('chaosgame',1000,1000)
win.setBackground(color_rgb(0,0,0))

# Draw polygon
poly = Polygon(points)
poly.setOutline(color_rgb(255,255,0))
poly.setWidth(2)
poly.draw(win)

# Draw initial point.
pt = Point(initp[0],initp[1])
pt.setOutline(color_rgb(255,0,0))
# ln = Line(Point(500,500),pt)
# ln.setOutline(color_rgb(255,0,255))
pt.draw(win)
# ln.draw(win)

#%%

# Iterate through the chaos game and draw each new point as it gets calculated.
last = 0
while True:
    
    # Exit key
    if kb.is_pressed('q'):
        print('\nExiting')
        break
     
    if vrule == 'y' or vrule == 'Y':
        # Pick a random vertex to work with, and for n > 3 make sure the same
        # one can't be chosen twice in a row
        if n == 3:
            vtx = randint(1,n)
        else:
            vtx = randint(1,n)
            while vtx == last:
                vtx = randint(1,n)
            last = vtx
    else:
        # Allow any vertex to be chosen
        vtx = randint(1,n)
    vtxvec = plist[vtx-1]

    # Calculate point between previous point and vertex and draw it, ad nauseum
    mdptx,mdpty = vtxvec[0] + ratio*(initp[0] - vtxvec[0]), vtxvec[1] + ratio*(initp[1] - vtxvec[1])
    pouin = Point(mdptx,mdpty)
    mdpt = Rectangle(pouin, pouin)
    mdpt.setOutline(color_rgb(255,255,255))
    mdpt.draw(win)
    initp = np.array([mdptx,mdpty])
    
win.close()
    
# window()

