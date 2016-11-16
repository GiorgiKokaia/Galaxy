#from __future__ import division - uncomment if you are using Python 2.7
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def oc(rt, vt, et, n):

	l = np.arange(n)
	etot = et[0, :]+et[1, :]
	eerr = (np.amax(etot)-np.amin(etot))/np.mean(etot)
	print ("Energy error is " + str(eerr))

	amc = rt[0, :]**2*vt[1, :]
	amcerr = (np.amax(amc)-np.amin(amc))/np.mean(amc)
	am = np.sqrt(rt[0,:]**2+rt[2, :]**2)*np.sqrt((rt[0,:]*vt[1,:])**2+vt[2, :]**2)
	amerr = (np.amax(am)-np.amin(am))/np.mean(am)

	print ("(R)Angular Momentum error is " + str(amcerr))
	print ("(RZ)Angular Momentum error is " + str(amerr))
	
	plt.figure(1)
	e = plt.plot(l, etot, c='r', label='total energy')
	ek = plt.plot(l, et[0, :], c='blue', label='kinetic energy')
	ep = plt.plot(l, et[1, :], c='black', label='potential energy')
	plt.legend()
	plt.xlabel('Timestep')
	plt.ylabel('Energy')
	plt.title('Energy conservation')
	plt.show()

	plt.figure(6)
	plt.semilogy(l, amc)
	plt.xlabel('Timestep')
	plt.ylabel('Angular Momentum')
	plt.title('Angular Momentum Conservation')
	plt.show()

	plt.figure(3)
	plt.plot(-vt[0, :]*np.cos(vt[1, :]), vt[0, :]*np.sin(vt[1, :]), marker='.')
	plt.xlabel(r'$v_x$ (km/s$\sim$pc/Myr)')
	plt.ylabel(r'$v_y$ (km/s$\sim$pc/Myr)')
	plt.axes().set_aspect('equal', 'datalim')
	plt.show()


	plt.figure(4)
	plt.plot(l, rt[2,:])
	plt.xlabel('Timestep')
	plt.ylabel('z(pc)')
	plt.show()

	plt.figure(5)
	plt.plot(l, np.sqrt(rt[0,:]**2+rt[1, :]**2), marker='.')
	plt.xlabel('timestep')
	plt.ylabel(r'r(pc)')
	plt.show()

	return None
