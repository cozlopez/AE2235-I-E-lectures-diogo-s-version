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


# A = np.matrix([[-0.2, 0.06, 0, -1],
#                [0,0,1,0],
#                [-17,0,-3.8,1],
#                [9.4,0,-0.4,-0.6]])
# B = np.matrix([[-0.01, 0.06],
#                [0,0],
#                [-32,5.4],
#                [2.6, -7]])
#
# C = np.matrix([0,0,0,1])
#
# D = np.zeros((1,2))
#
# sys = c.ss(A,B,C,D)
#
# Kr = -0.55
#
# K_pain = np.matrix([[0],[Kr]])
#
# sys_plain = sys.feedback(K_pain)
#
# # feedback system for washout yaw damper
# A_fb = np.mat([[-0.5]])
# B_fb = np.mat([[0.5]])
# C_fb = np.mat([[0], [-Kr]])
# D_fb = np.mat([[0], [Kr]])
# K_wash = c.ss(A_fb, B_fb, C_fb, D_fb)
# sys_wash = sys.feedback(K_wash)
#
# t = np.arange(0.1,20.1,0.1)
#
# u = np.zeros((t.size, 2))
# u[:10,0] = 1.
#
# for i, (name,system) in enumerate([('no damper', sys),('plain damper', sys_plain),('washout damper', sys_wash)]):
#     print(name)
#     c.damp(system,True)
#     y,t, _x = c.lsim(system, u, t)
#     print("value at 20s", y[-1])
#     plt.subplot(3,1,i+1)
#     plt.plot(t,y)
#     plt.title(name)
#
# plt.show()

#roll control of an aircraft

#Ka = 4

#tau_a = 1.2


#Kap = 0.4

#s = c.tf([1,0], [1])

#Hact = c.ss(8/(s**2 + 5*s + 9))

#Hac = c.ss(Ka/((1+tau_a*s)*s))

#sys = c.append(Hact, Hac, Kap)

#Q = np.matrix([[1,3],[2,1],[3, -2]])

#inputs =[3]

#outputs = [3,1,2]

#sysc = c.connect(sys, Q, inputs, outputs)

#print(sysc)

#control of Moller SkyCarTM4kUHD brought to you by CarlsJunior Nascar Cup Series Visa Cash App Superslam

# s = c.tf([1,0],[1])
#
# K = 0.75
#
# G = K* (4*s**2 + 2*s +1)/(s*(1+ 0.1*s))
#
# H = 1/(s**2 * (s**2 + s + 4))
#
# sys = c.append(c.ss(H), c.ss(G))
# Q = [[1,2],[2,-1]]
#
# inputs = [2]
#
# outputs = [ 1,2]
#
# sys = c.connect(sys, Q, inputs, outputs)
#
# print(sys)