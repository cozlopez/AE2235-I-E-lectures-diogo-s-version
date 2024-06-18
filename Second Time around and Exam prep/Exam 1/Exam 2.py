import control.matlab as ml
import matplotlib.pyplot as plt
import numpy as np

dt = 0.001

s = ml.tf([1,0],[1])

# h1 = (21*s**2 + 4.4 * s + 480.2)/(s**4 + 0.6*s**3 + 404.1*s**2 + 81.61*s + 1604)
#
# h2 = (30*s**2 + 40 * s + 4040)/(s**4 + 2*s**3 + 402*s**2 + 800*s + 800)
#
# h3 = ((s+ 0.1 + 5j)*(s+ 0.1 - 5j))/((s - 0 - 20j)*(s- 0 + 20j)*(s + 0.1 - 2j)*(s+ 0.1 + 2j))
#
# h4 = ((s- 0.1 + 5j)*(s- 0.1 - 5j))/((s +0.2 - 20j)*(s + 0.2 + 20j)*(s - 0.1 - 2j)*(s- 0.1 + 2j))
#
# h5 = ((s- 5j)*(s+5j))/((s +2j)*(s -2j)*(s - 20j)*(s+20j))
#
# h6 = ((s+ 0.7 + 11j)*(s+ 0.7 - 12j))/((s +1 + 0.1j)*(s +1 - 0.1j)*(s - 20j)*(s+ 20j))

t = np.arange(0,1000,dt)

# y1, t1 = ml.step(h1,t)
#
# y2, t2 = ml.step(h2,t)
#
# y3, t3 = ml.step(h3,t)
#
# y4, t4= ml.step(h4,t)
#
# y5, t5 = ml.step(h5,t)
#
# y6, t6 = ml.step(h6,t)
#
#
# #plt.plot(t1, y1, color = "red")
#
# #plt.plot(t2, y2, color = "brown")
# plt.plot(t3, y3, color = "blue")
# plt.plot(t4, y4, color = "green")
# plt.plot(t5, y5, color = "magenta")
# #plt.plot(t6, y6, color = "orange")
#
# plt.show()

# A = np.matrix("""-0.9, -3.0, 0; -0.5, -2.5, 0; 0 , 1 , 0""")
#
# B = np.matrix("""0.2; -0.1; 0""")
#
# C = np.matrix([[1,0,0],
#                [0,1,0],
#                [0,0,1]])
#
# D = np.matrix([[0],[0],[0]])
#
# sys1 = ml.ss(A,B,C,D)
#
# print(ml.tf(sys1))
#
# hnew = -0.2*(-0.1*s -0.0198)/(s**3 + 0.46*s**2 + 0.0401*s)
#
# #ml.rlocus(hnew)
# #plt.show()
#
# y1, t1 = ml.step(ml.minreal(ml.feedback(hnew,1)),t)
# print(ml.stepinfo(y1,t1, SettlingTimeThreshold=0.05))
# plt.plot(t1,y1)
# plt.plot(t1, np.ones(int(100/dt))*0.95)
# plt.plot(t1, np.ones(int(100/dt))*1.05)
# plt.show()

# Ky = 0.6
# Kpsi = 0.6
# V = 9
# l = 3
#
# sys1 = Ky *s/s
# sys2 = Kpsi
# sys3 = V/(l*s)
# sys4 = V/s
#
# sys = ml.append(sys1, sys2, sys3, sys4)
#
# Q = np.matrix([[1,-4,0],
#                [2,1,-3],
#                [3,2,0],
#                [4,3,0]])
#
# inputs = [1,2]
# outputs = [4,3,2]
#
# syscon = ml.connect(sys,Q,inputs, outputs)
# print(syscon)

Kap = 0.1912#1 #0.3351 #1
Kr = 1.2
taua = 0.5
taufi = 0.8

H = 9/(s**2+5*s+9)
G = Kr/(taua*s**2+s)
a = 1/(taufi*s+1)

h1 = ml.feedback(H*G,a)

h2 = ml.feedback(1, H*G*a)

h = H*G*a

print(h2)

#ml.rlocus(ml.minreal(h))

y1, t1 = ml.step(1.6*h, t)

plt.plot(t1,y1)

plt.show()
