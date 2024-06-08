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
#---------------------------------------------------------------------
#Operations:


# difference between matrix and array
# note that the shape is given here as a tuple: (3, 3)
#a = np.arange(9.0).reshape((3, 3))
#m = np.matrix(a)

# for example, multiplying 2 arrays
#print(a * a)

# or two matrices
#print(m * m)

# or mix them; they become matrices
#print(a * m)

# but if you need array behaviour, simply do
#print np.array(m) * np.array(m)

#eye-> identity matrices

#operations 1

#rnd.seed(3)

#a = np.matrix(rnd.randn(5,5))

#b = np.linalg.eigvals(a)
#maxeig_arg = np.argmax(np.absolute(b))
#maxeig = b[maxeig_arg]
#mineig_arg = np.argmin(np.absolute(b))
#mineig = b[mineig_arg]
#print(maxeig)
#print(mineig)

#operations 2

# ang_d = np.angle(3+4j)*180/np.pi
#
# ang_e = np.angle(-1-3j)*180/np.pi
#
# absolute_f = np.absolute(-8-1j)
#
# print(ang_d)
# print(ang_e)
# print(absolute_f)

#operations 3

# a = np.matrix(np.arange(0,5,0.1))
# print(np.sum(np.sin(a)))

#operations 4

# rnd.seed(4)
#
# a = np.matrix(rnd.randn(20, 70))
# print(a)
# for i in range(20):
#     for j in range(70):
#         if not a[i,j] > 2:
#             a[i,j] = 0
# print("-----------------------")
# print(a)
# b=np.sum(a)
# print(b)

#operations 5

rnd.seed(8)
a = rnd.randn(5000)
b = a[np.where(abs(a) <= 2)]
c = len(b) / len(a) * 100

print(c)

