# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:56:12 2023

@author: ChrisZeThird
"""

# =============================================================================
# Simple code to create a rectangular box to visualize where the material is
# =============================================================================

import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def Cube(Lx,Ly,Lz,ax):
    
    """ Initialize cube """
    
    ## Define an array with dimensions 8 by 3
        # 8 for each vertex
        # 3 for each coordinate
    cube = np.zeros([8,3])
    
    # Define x values
    cube[:,0] = [-Lx/2, -Lx/2, -Lx/2, -Lx/2, Lx/2, Lx/2, Lx/2, Lx/2]
    # Define y values
    cube[:,1] = [-Ly/2, Ly/2, -Ly/2, Ly/2, -Ly/2, Ly/2, -Ly/2, Ly/2]
    # Define z values
    cube[:,2] = [-Lz/2, -Lz/2, Lz/2, Lz/2, -Lz/2, -Lz/2, Lz/2, Lz/2]
    
    """ Plotting the cube """
    
    # Initialize a list of vertex coordinates for each face
    faces = []
    faces.append(np.zeros([5,3]))
    faces.append(np.zeros([5,3]))
    faces.append(np.zeros([5,3]))
    faces.append(np.zeros([5,3]))
    faces.append(np.zeros([5,3]))
    faces.append(np.zeros([5,3]))
    
    # Bottom face
    faces[0][:,0] = [-Lx/2,-Lx/2,Lx/2,Lx/2,-Lx/2]
    faces[0][:,1] = [-Ly/2,Ly/2,Ly/2,-Ly/2,-Ly/2]
    faces[0][:,2] = [-Lz/2,-Lz/2,-Lz/2,-Lz/2,-Lz/2]
    # Top face
    faces[1][:,0] = [-Lx/2,-Lx/2,Lx/2,Lx/2,-Lx/2]
    faces[1][:,1] = [-Ly/2,Ly/2,Ly/2,-Ly/2,-Ly/2]
    faces[1][:,2] = [Lz/2,Lz/2,Lz/2,Lz/2,Lz/2]
    # Left Face
    faces[2][:,0] = [-Lx/2,-Lx/2,-Lx/2,-Lx/2,-Lx/2]
    faces[2][:,1] = [-Ly/2,Ly/2,Ly/2,-Ly/2,-Ly/2]
    faces[2][:,2] = [-Lz/2,-Lz/2,Lz/2,Lz/2,-Lz/2]
    # Left Face
    faces[3][:,0] = [Lx/2,Lx/2,Lx/2,Lx/2,Lx/2]
    faces[3][:,1] = [-Ly/2,Ly/2,Ly/2,-Ly/2,-Ly/2]
    faces[3][:,2] = [-Lz/2,-Lz/2,Lz/2,Lz/2,-Lz/2]
    # front face
    faces[4][:,0] = [-Lx/2,Lx/2,Lx/2,-Lx/2,-Lx/2]
    faces[4][:,1] = [-Ly/2,-Ly/2,-Ly/2,-Ly/2,-Ly/2]
    faces[4][:,2] = [-Lz/2,-Lz/2,Lz/2,Lz/2,-Lz/2]
    # front face
    faces[5][:,0] = [-Lx/2,Lx/2,Lx/2,-Lx/2,-Lx/2]
    faces[5][:,1] = [Ly/2,Ly/2,Ly/2,Ly/2,Ly/2]
    faces[5][:,2] = [-Lz/2,-Lz/2,Lz/2,Lz/2,-Lz/2]
    
    Poly = ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='k', alpha=.15))

    return Poly