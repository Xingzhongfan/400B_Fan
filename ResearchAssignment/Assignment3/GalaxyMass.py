
# coding: utf-8

# In[1]:

# Homework 3 Solutions
# Computing the Mass of the Local Group
# G. Besla


# In[2]:

# import necessary modules
# numpy provides powerful multi-dimensional arrays to hold and manipulate data
import numpy as np
# astropy provides unit system for astronomical calculations
import astropy.units as u
# import previous HW functions
from ReadFile import Read


# # Galaxy Mass

# In[3]:


def ComponentMass(filename):
# function to compute the mass of all particles of a given type for a given galaxy 
# input:  filename (str) ,  Particle type (1,2,3)
# output: Mass in units of Msun. 
    
     # read in the file 
    time, total, data = Read(filename)
    
      # gather particles with the same type and sum up the mass
    # we can directly round the result and adjust the units
    mass = np.round(data['m'].sum() * 1e10, 3)
    
    # return the mass 
    return mass


