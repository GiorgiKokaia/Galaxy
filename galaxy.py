#from __future__ import division - uncomment if you are using Python 2.7
import numpy as np
import matplotlib.pyplot as plt
import leapfrog as lf
import orbit as orb
import time
import os
import numpy.ma as M
import matplotlib
import orbcheck as oc
import potential as p
np.set_printoptions(threshold=np.nan)
start_time = time.time()
#Units = Distance(pc) - Time (Myrs) - Mass (M_sun) -> G = 0.00449, pc/Myr = km/s
#For single particle set initial values (These are solar)					 
r = np.zeros(3)					#Used for the integration
r[0] = 8300 					#set to be at solar circle
v = np.zeros(3) 				#Used for integration
h = 0.1 					#Stepsize
n = 10000					#Number of timesteps
m = 1 						#Number of trajectories to integrate
rt = np.zeros((m, 3, n)) 			#x, y, z
vt = np.zeros((m, 3, n)) 			#v_x, v_y, v_z
et = np.zeros((m, 2, n)) 			#0 = E_k, 1 = E_p
#path = "/home/giorgi/my/folder/" 		Path to folder in which you want to save data
#os.mkdir(path) 				#If folder you want to save data in doesn't exist, if you want to save at all uncomment this
for q in range(0, m):
	r[1] = 2*np.pi*np.random.random()
	v[0] = -5 + 10*np.random.random()
	v[1] = np.sqrt(r[0]*np.abs(p.dpot(r)[0]))/r[0]+(-5+10*np.random.random())/r[0]
	v[2] = 40*np.random.random()-20
	rt[q, :, :], vt[q, :, :], et[q, :, :] = orb.orbit(r, v, h, n)
	#data = [rt[q, :, :], vt[q, :, :], et[q, :, :]] Putting all the data in one tuple
	#np.save(path+str(q).zfill(4), data) Saving the data in a ".npy" file
	print( "completed orbit nr " + str(q))

print( "orbits completed" )
print("Integration time is %s seconds " % (time.time() - start_time))
#If plotting, ind is the index of the run you want to check
ind = 0
#Number of orbits completed
orbs = str(np.round(np.abs(rt[ind, 1, n-1]-rt[ind, 1, 0])/(2*np.pi), decimals=1))
print( orbs )

oc.oc(rt[ind,:,:], vt[ind,:,:], et[ind,:,:], n)


