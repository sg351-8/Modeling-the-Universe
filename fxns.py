#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
import numpy as np


# In[1]:


# Flux ratio code from the first pset
def Flux(p,z):
    
    # first make sure z is taken as the absolute value
    z=abs(z)
    
    # lambda partial function; different function for different values of z
    if (1+p)<z:
        lamda=0    #misspelled lambda bc the correct spelling is some native python function
    elif abs(1.-p)<z and z<=(1.+p):
        # define kappa 0 and 1 wrt p,z
        kap1 = math.acos( (1 - p**2 + z**2) / (2 * z) )
        kap0 = math.acos((p**2+z**2-1)/(2*p*z))
        lamda=(1/math.pi)*(p**2 * kap0 + kap1 - math.sqrt((4*z**2 - (1+z**2 -p**2)**2)/4))
    elif z<=(1.-p):
        lamda=p**2
    elif z<= (p-1):
        lamda=1
        
    #final observed flux wrt unobscured flux
    return(1 - lamda)


# In[3]:


# integral code from second pset
def integraltr(func, lowbound, upbound, N):
    """gives the integral of sin(x) with givens: lower bound, upper bound, number of rectangles"""
   
    # steps through the given bounds in N steps, finds the area of each rectangle + each trapezoid, sums them
    sum=0
    for x in np.linspace(lowbound, upbound, N, endpoint=False):
        width = ((upbound-lowbound)/N)
        height_rectangle = func(x)
        height_trapezoid = func(x+width)
        rectangle_trapezoid = (height_rectangle*width) + (((height_trapezoid - height_rectangle) * width) / 2)
        sum = sum + rectangle_trapezoid
    return sum


# In[ ]:




