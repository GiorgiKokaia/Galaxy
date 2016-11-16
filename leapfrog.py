import numpy as np
import potential as pt


def integrate3d(r, v, h):
    
    #Get the acceleration
    f = pt.dpot(r)
    #Changing the R and Phi-components of Gradient to cylindrical. Z is the same
    f[0] = f[0] + r[0]*v[1]**2
    f[1] = (f[1]-2*v[0]*v[1])/r[0]
    
    #Update velocity
    v = v + h/2 * f
    
    #Update position
    r = r + h * v
    
    #Get updated acceleration
    f = pt.dpot(r)
    #Changing the R and Phi-components of Gradient to cylindrical. Z is the same
    f[0] = f[0] + r[0]*v[1]**2
    f[1] = (f[1]-2*v[0]*v[1])/r[0]
    
    #Update velocity again
    v = v + h/2 * f
        
    return r, v
