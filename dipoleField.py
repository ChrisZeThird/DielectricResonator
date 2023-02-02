# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 21:21:49 2023

@author: ChrisZeThird
"""

# =============================================================================
# Short program that gives the expression of the magnetic field for a magnetic 
# dipole
# =============================================================================

import numpy as np

def magneticDipole(x,y,z):
    r = np.sqrt(x**2 + y**2 + z**2)
    c = (1/(4*np.pi))
    
    Hx = c*(3*z*x/r**5 - x/r**3)
    Hy = c*(3*z*y/r**5 - y/r**3)
    Hz = c*(3*(z**2)/r**5 - 1/r**3 - 1) # Mz = 1
    
    return Hx,Hy,Hz