import numpy as np
import control.matlab as c
from scipy.linalg import eig
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

