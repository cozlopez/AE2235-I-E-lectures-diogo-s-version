import control.matlab as ml
import matplotlib.pyplot as plt
import numpy as np

dt = 0.01

t = np.arange(0,5, dt)

s = ml.tf([1,0],[1])
#
# h1 = ml.minreal((s)/((s+2j)*(s+1.75)*(s-1.75)))
#
# h2 = (s+1)/(s**3 + 4*s**2 + 5*s + 6)
#
# h3 = ml.minreal((s+9)/(2*s**3 + 2*s**2 + 11*s))
#
# #ml.bode(h2)
# #plt.show()
#
# #print(ml.poles(h1))
# #print(ml.poles(h2))
# print(ml.poles(h3))
#
# kp = 4
#
# h = 1/(1+h2)
#
# #y1, t1 = ml.step(h,t)
#
# #plt.plot(t1, y1)
# #plt.show()

h1 = (0.2*s-0.4)/(s**2)

h2 = 1/((s**2+0.4*s+1)*(s+5))

h3 = (-0.5*(s+1)**2)/(s+0.3)**2

#y1, t1 = ml.step(h1,t)#A
#y2, t2 = ml.step(h2,t)#C
#y3, t3 = ml.step(h3,t)#B

#plt.plot(t1, y1, color = "red")
#plt.plot(t2, y2, color = "green")
#plt.plot(t3, y3, color = "blue")

#ml.bode(h1)
#print(ml.poles(h1))
#plt.show()

V=1
l=1

#h1 = (0.18*V**2)/(s*(l*s+0.3*V)+0.18*V**2)

h = 7*(4*s**2+0.12*s+1)/((70*s+1)*(s**2+0.9*s+1))

#print(ml.damp(h))

ml.rlocus(h)
plt.show()