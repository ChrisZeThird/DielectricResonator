# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 09:38:52 2023

@author: ChrisZeThird
"""

# =============================================================================
# Main file used to generate the plot of the fields. 
# At the bottom, slicing is done on the arrays. Otherwise matlplotlib would not 
# be able to render the figure
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D

from Cube3D import Cube
from electromagFields import electricField, magneticField

N = 200 # number of points for linspace array

""" Setting parameters of the cavity """

## Lengths are in millimeter
Lx = 0.7 #e-3
Ly = 0.55 #e-3
Lz = 0.3 #e-3

## Define wavevector for adapated mode (here TE110)
def waveVector(n,m,p,a,b,c):
    kx = n*np.pi/a
    ky = m*np.pi/b
    kz = p*np.pi/c
    return kx,ky,kz

n, m, p = 1, 1, 0
kx_110, ky_110, kz_110 = waveVector(n,m,p,Lx,Ly,Lz)

""" Setting figure """

## Create grid
limx = 0.5
limy = 0.5
limz = 0.5
x, y, z = np.meshgrid(np.linspace(start=-(Lx/2+limx), stop=(Lx/2+limx), num=N, endpoint=True),
                      np.linspace(start=-(Ly/2+limy), stop=(Ly/2+limy), num=N, endpoint=True),
                      np.linspace(start=-(Lz/2+limz), stop=(Lz/2+limz), num=N, endpoint=True))


## Make vector for Electric field and Magnetic field

    # Express condition outside the resonator for |i|<Li i in {x,y,z}
inside = ((abs(x)<=(Lx/2)) & (abs(y)<=(Ly/2)) & (abs(z)<=(Lz/2)))
outside = ~inside

Ex110,Ey110,Ez110 = electricField(x, y, z, kx_110, ky_110, kz_110, inside, outside)
Hx110,Hy110,Hz110 = magneticField(x, y, z, kx_110, ky_110, kz_110, inside, outside)

## Create figure
fig = plt.figure(figsize=(12,12))
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# ax = Axes3D(fig)

## Slicing of arrays
def skip(s):
    slicing = (slice(None, None, s), slice(None, None, s), slice(None, None, s))
    return slicing

slicingE = skip(12) #12
slicingH = skip(25) #30

ax.quiver(x[slicingE], y[slicingE], z[slicingE], Ex110[slicingE], Ey110[slicingE], Ez110[slicingE], length=0.08, pivot='middle', normalize=True)
# ax.quiver(x[slicingH], y[slicingH], z[slicingH], Hx110[slicingH], Hy110[slicingH], Hz110[slicingH], length=0.1, pivot='middle', normalize=True, color='r')

Cube(Lx,Ly,Lz,ax) # create a box on the figure, independent from the rest

ax.set_xlim3d(-(Lx/2+limx),Lx/2+limx)
ax.set_ylim3d(-(Ly/2+limy),Ly/2+limy)
ax.set_zlim3d(-(Lz/2+limz),Lz/2+limz)
plt.show()