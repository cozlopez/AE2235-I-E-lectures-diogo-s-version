import numpy as np
import control.matlab as c
from control.matlab import poles
from scipy.linalg import eig
import matplotlib.pyplot as plt
import scipy as sp

#dominant poles/step response 1

# s = c.tf([1,0],[1])
#
# G = 6205 / (s*(s**2+13*s+1281))
#
# Heq = G.feedback(1)
#
# p = c.pole(Heq)
#
# H1 = 5/(s+5)
#
# H2 = (Heq/H1).minreal()
#
# tend = 1
#
# dt = 0.01
#
# t = np.arange(0, tend+dt, dt)
#
# y, t2 = c.step(Heq, t)
#
# y1, t2 = c.step(H1, t)
#
# y2, t2 = c.step(H2, t)
#
# print('--D1--')
# print(sp.integrate.trapz(abs(y-y1),t))
# print('--D2--')
# print(sp.integrate.trapz(abs(y-y2),t))
# plt.plot(t,y,t,y1,t,y2)
# plt.show()

#yaw response of aircraft

A = np.matrix([[-0.2, 0.06, 0, -1],
               [0,0,1,0],
               [-17,0,-3.8,1],
               [9.4,0,-0.4,-0.6]])
B = np.matrix([[-0.01, 0.06],
               [0,0],
               [-32,5.4],
               [2.6, -7]])
#
# B = B[:,[1]]
#
# C = np.matrix([0,0,0,1])
#
# D = np.matrix([[0]])
#
# sys = c.ss(A,B,C,D)
#
# T = np.arange(0,20,0.01)
#
# y,t = c.step(sys,T)
#
# plt.plot(t,y)
#
# plt.show()
#
# print(np.min(y[t<2]))

#control with state space systems

# Kd = -0.55
#
# C = np.eye(4)
#
# D = np.zeros((4,2))
#
# sys = c.ss(A,B,C,D)
#
# K = np.matrix([[0,0,0,0],[0,0,0,Kd]])
#
# sys_new = sys.feedback(K)
#
# print(sys_new)

#control with state space systems 2

