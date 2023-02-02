# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 14:41:28 2023

@author: ChrisZeThird
"""

# =============================================================================
# The electric field is considered completely confined in this approximation. 
# The material is approxiamated by a dipole in order to approach the expression 
# of the external magnetic field
# =============================================================================

import numpy as np
from dipoleField import magneticDipole

## Lengths are in millimeter
Lx = 0.7 #e-3
Ly = 0.55 #e-3
Lz = 0.3 #e-3

def electricField(x,y,z,kx,ky,kz,inside,outside):
    ## x,y and z are the entire space not the restriction to the dielectric cube
    
    Ex = np.empty_like(x)
    Ey = np.empty_like(x)
    Ez = np.empty_like(x)
    
    Ex_inside = np.cos(kx*x)*np.sin(ky*y)*np.cos(kz*z)
    Ey_inside = -np.sin(kx*x)*np.cos(ky*y)*np.cos(kz*z)
    Ez_inside = np.sin(kx*x)*np.sin(ky*y)*np.sin(kz*z)
    
    Ex_outside = 0 #np.cos(kx*x)*np.sin(ky*y)*np.cos(kz*z)
    Ey_outside = 0 #np.sin(kx*x)*np.cos(ky*y)*np.cos(kz*Lz)*np.exp(Lz - z)
    Ez_outside = 0 #np.sin(kx*x)*np.sin(ky*y)*np.sin(kz*Lz)*np.exp(Lz - z)
    
    np.putmask(Ex,inside,Ex_inside)
    np.putmask(Ey,inside,Ey_inside)
    np.putmask(Ez,inside,Ez_inside)
    
    np.putmask(Ex,outside,Ex_outside)
    np.putmask(Ey,outside,Ey_outside)
    np.putmask(Ez,outside,Ez_outside)
    return Ex,Ey,Ez

def magneticField(x,y,z,kx,ky,kz,inside,outside):
    ## x,y and z are the entire space not the restriction to the dielectric cube
    Hx = np.empty_like(x)
    Hy = np.empty_like(x)
    Hz = np.empty_like(x)
    
    Hx_inside = -np.sin(kx*x)*np.cos(ky*y)*np.sin(kz*z)
    Hy_inside = -np.cos(kx*x)*np.sin(ky*y)*np.sin(kz*z)
    Hz_inside = np.cos(kx*x)*np.cos(ky*y)*np.cos(kz*z)
    
    Hx_outside, Hy_outside, Hz_outside = magneticDipole(x,y,z)
    
    np.putmask(Hx,inside,Hx_inside)
    np.putmask(Hy,inside,Hy_inside)
    np.putmask(Hz,inside,Hz_inside)
    
    np.putmask(Hx,outside,Hx_outside)
    np.putmask(Hy,outside,Hy_outside)
    np.putmask(Hz,outside,Hz_outside)
    
    # Hx = -np.sin(kx*x)*np.cos(ky*y)*np.sin(kz*z)
    # Hy = -np.cos(kx*x)*np.sin(ky*y)*np.sin(kz*z)
    # Hz = np.cos(kx*x)*np.cos(ky*y)*np.cos(kz*z)
    
    return Hx,Hy,Hz
