import numpy as np
#Feng & BJ (2013) potential
#Units = Distance(pc) - Time (Myrs) - Mass (M_sun) -> G = 0.00449, pc/Myr = km/s
G = 0.00449
#Symmetric parameters
mass_d = 7.9080e10
mass_b = 1.3955e10
mass_h = 6.9766e11
a_d = 3550
b_d = 250
b_b = 350
b_h = 24000


def pot(rpos):
    rad = rpos[0]
    z = rpos[2]
    r = np.sqrt(rpos[0]**2+rpos[2]**2)
 
   
    #Contribution from disk
    phi_d = -G*mass_d / np.sqrt(rad**2+(a_d+np.sqrt(z**2+b_d**2))**2)
    
    #Contribution from bulge
    phi_b = -G*mass_b / np.sqrt(rad**2+z**2+b_b**2)
    
    #Contribution from Halo
    phi_h = -G*mass_h / np.sqrt(rad**2+z**2+b_h**2)
    
    phi_symm = phi_d + phi_b + phi_h

    
    return phi_symm


def dpot(rpos):
    r = np.sqrt(rpos[0]**2+rpos[2]**2)
    rad = rpos[0]
    z = rpos[2]


    #Contribution from disk
    rphi_d = -G*mass_d*rad/np.sqrt(((a_d+np.sqrt(b_d**2+z**2))**2+rad**2)**3)
    pphi_d = 0
    zphi_d = -G*mass_d*z*(a_d+np.sqrt(b_d**2+z**2))/((np.sqrt(b_d**2+z**2))*np.sqrt((a_d+np.sqrt(b_d**2+z**2))**2+rad**2)**3)
    
    #Contribution from bulge
    rphi_b = -rad*G*mass_b / np.sqrt((rad**2+z**2+b_b**2)**3)
    pphi_b = 0
    zphi_b = -z*G*mass_b / np.sqrt((rad**2+z**2+b_b**2)**3)
    
    #Contribution from halo
    rphi_h = -rad*G*mass_h / np.sqrt((rad**2+z**2+b_h**2)**3)
    pphi_h = 0
    zphi_h = -z*G*mass_h / np.sqrt((rad**2+z**2+b_h**2)**3)
    


    f = np.zeros(3)
    f[0] = rphi_d+rphi_b+rphi_h
    f[1] = 0
    f[2] = zphi_d+zphi_b+zphi_h
    return f
