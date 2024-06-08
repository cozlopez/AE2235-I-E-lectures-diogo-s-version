#random 2
import numpy as np
import numpy.random as rnd
import scipy.linalg as la
#xr = rnd.get_state()

#print(xr)

# get the current random generator state and save it
#a = rnd.get_state()

# restore to the previously saved state
#rnd.set_state(a)

#variables 1
#rnd.seed(4)

#a = rnd.rand(15,7)
#c=a[:,5]
#b = np.sum(a[:,5])

#print(a)
#print(c)
#print(b)

#variables 2

#a = np.identity(17)
#print(a)
#print(np.trace(a))

#variables 3

#rnd.seed(3)
#a = rnd.rand(6,6)
#a[4] = [2,3,4,5,6,7]
#print(a)
#print(np.sum(a))

#variables 4 (randn)

#rnd.seed(7)

#rowvector = np.arange(-2,3).reshape((1,5))
#columnvector = np.arange(0,6).reshape((6, 1))

#a= np.round(rnd.randn(5,5),0)
#print(a)
#a= np.append(a,rowvector,axis=0)
#print(a)
#a=np.append(a,columnvector,axis=1)
#print('------------------------------')
#print(a)
#counter = np.count_nonzero(a)
#print(counter)

#variables 5

#rnd.seed(4)

#a = np.transpose(rnd.rand(5,5))

#t = np.transpose(la.toeplitz(np.arange(1, 6)))

#b = np.append(a,t,axis=0)

#soma = np.sum(b[:,0])

#print(soma)

#operations 1

