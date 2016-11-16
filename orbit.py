import numpy as np
import leapfrog as lf
import potential as pot

def orbit(r, v, h, n):
	rt = np.zeros((3, n))
	vt = np.zeros((3, n))
	et = np.zeros((2, n))
	for i in range(0, n):
		r, v = lf.integrate3d(r, v, h)
		rt[:,i] = r
		vt[:,i] = v


		et[0, i] = (v[0]**2+(r[0]*v[1])**2+v[2]**2)*0.5	
		et[1, i] = pot.pot(r)

	return rt, vt, et
