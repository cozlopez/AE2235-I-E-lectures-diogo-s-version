import numpy as np
import control.matlab as c
from control.matlab import poles
from scipy.linalg import eig
import matplotlib.pyplot as plt
import scipy
#first description
# a = np.matrix(""" 0       1      0   ;
#                  -0.0071 -0.111  0.12;
#                   0       0.07  -0.3""")
# b = np.matrix(""" 0 ;    -0.095; 0.072""")
# c = np.matrix(""" 1       0     0    """)
# d = np.matrix(""" 0     """)
#
# #creating state space
#
# sys = c.ss(a, b, c, d) #As long as you do not specify a time step as 5th parameter, Matlab will assume that you are creating a continuous-time system. If you enter a time step as 5th parameter, Matlab assumes you are entering a discrete-time system.
#
# #Of course, the dimensions of the matrices you enter must fit; B must have as many rows as A, A must be a square matrix, C must have as many columns as A, and the D matrix must have as many columns as B and as many rows as C.
#
# #add new climb or descent angle
#
# newc = np.matrix("1.0 0  0;"  # theta
#                  "0   1  0;"  # q
#                  "0   0  1;"  # aplha
#                  "1   0 -1")  # gamma = theta - alpha
# newd = np.zeros((4,1))
# sys2 = ss(a, b, newc, newd)

#system 1

# m = 3.5
# b = 9
# k= 60
#
# A = np.matrix([[-b/m,-k/m],
#                [1,0]])
# B = np.matrix([[1/m],
#                [0]])
# C = np.matrix([[0,1],
#                [1,0],
#                [-b/m,-k/m]])
# D = np.matrix([[0],
#                [0],
#                [1/m]])
#
# print("--Matrix A--")
# print(A)
# print("--Matrix B--")
# print(B)
# print("--Matrix C--")
# print(C)
# print("--Matrix D--")
# print(D)

#state space 2

# # parameter values
# m = 3.5
# b = 9
# k = 60
# # matrices
# A = np.matrix([[ -b/m, -k/m], [ 1, 0]])
# B = np.matrix([[ 1/m], [ 0]])
# C = np.matrix([[ 0, 1]])
# D = np.matrix([[ 0]])
# # system
# dt = 0.01
# t_length = 20
# sys = c.ss(A, B, C, D)
# t= np.arange(0,t_length,dt)
# f1 = 3.9357078 #0.027858371518604926
# f2 = 3.7197762 #0.02822810631125589
# U = np.sin(f1*t)
# output = c.lsim(sys, U, t, X0= [1,0])
#
# plt.plot(t, output[2][:,1])
# plt.plot(t,np.zeros(int(t_length/dt))) #helps find point of intersection
# plt.show()
# # help(c.lsim)
# print(output[2][int(10/dt):,1].max())

#state space to transfer function


#help(c.rss)
# A = [ [ -1.4,    0,    0  ],
#       [ 0.4, -1.2, -5.0],
#       [ 0,    1,    0  ] ]
# B = [ [0.3 ], [0 ], [0 ] ]
# C = [ [0,   1, 0 ],
#       [0.1, 0, 1 ]]
# D= [ [0],
#      [0] ]
# sys = c.ss(A,B,C,D)
# H = c.tf(sys)
# roots = np.roots(H.den[0][0])
# print(H)
# print(roots)

#converting from transfer function to state space

# s = c.tf([1,0],[1])
# b0 = 0.4
# b1 = 0.1
# b2 = 0.5
# a0 = 2.3
# a1 = 6.3
# a2 = 3.6
# a3 = 1.0
#
# h = (b0 + b1*s + b2*s**2)/( a0 + a1*s + a2*s**2 + a3*s**3 )
#
# H = c.tf([[h.num[0][0]],[(h*s).num[0][0]]],
#         [[h.den[0][0]],[(h*s).den[0][0]]])
#
# print(c.ss(H))
# print(eig(c.ss(H).A))
# print(h.poles())

#State-Space Systems Diagram

K1 = 0.6
K2 = 2.8
K3 = 2.5
K4 = 0.6

A = np.matrix([[0, -K4*K2, -K4*K3],
               [1, -1, 0],
               [0,1,0]])

B = np.matrix([[K4, 1],
               [0,0],
               [0,0]])

C = np.matrix([[K1, 0, 1]])

D = np.matrix([[0,0]])

print(c.ss(A, B, C, D))