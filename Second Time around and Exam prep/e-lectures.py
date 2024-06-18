import control.matlab as ml
import matplotlib.pyplot as plt
import scipy as np
import math
import numpy

s = ml.tf([1,0], [1])

# k1 = 1
#
# h1 = 5/(s**2 + 3*s + 5)
#
# g = k1 * (1 + 0.2/s)
#
# one = 1
#
# print((h1*g).feedback(1))
# print('-------------------')
# print((g).feedback(h1))
# print('-------------------')
# print((h1).feedback(g))
# print('-------------------')
# print(ml.feedback(1, g*h1))

# K = 1
#
# V = 1
#
# s_sp = 2 / math.sqrt(13)
# w_sp = math.sqrt(13)
#
# H = ml.minreal((K * V)/(s**2*(s**2 + 2 * s_sp * w_sp * s + w_sp**2)))
# print(H.poles())



ssp = 2 / math.sqrt(13)
wsp = math.sqrt(13)
Kq = -24
#T02 = 1.4
#new
T02 = 1.4
#Kt = -0.4379
Kr = -0.08944
Vtas = 160

#Ht = ml.minreal(Kt * H)
#Ht = ml.minreal((H).feedback(Kr))
#Ht = ml.minreal(H*Kr)
#print(ml.damp(Ht))
#ml.rlocus(Ht)
#plt.show()
#print(ml.poles(Ht))

Hq = ml.minreal(Kq*(1 + T02 * s)/(s**2 + 2*ssp * wsp *s + wsp**2))
Htheta = Hq / s
Hgamma = Hq / (s*(1+T02*s))
Hh = Vtas * Hq / (s**2*(1+T02 * s))

Hall = ml.tf([[Hq.num[0][0]],
           [Htheta.num[0][0]],
           [Hgamma.num[0][0]],
           [Hh.num[0][0]]],
          [[Hq.den[0][0]],
            [Htheta.den[0][0]],
            [Hgamma.den[0][0]],
            [Hh.den[0][0]]])

sys1 = ml.ss(Hall)

gain = numpy.matrix([Kr,0,0,0])

sys2 = ml.feedback(sys1, gain, -1)

dt = 0.01

t = numpy.arange(0, 20,dt)

#y1, t1 = ml.step(numpy.matrix([1,0,0,0])*sys1, t)

#y2, t2 = ml.step(numpy.matrix([1,0,0,0])*sys2, t)

#print(ml.ss(sys2))

# plt.plot(t1,y1)
#
# plt.plot(t2,y2)
#
# plt.show()

Ktheta = -0.4737

Hth = ml.tf(numpy.array([0, 1, 0, 0]) * sys2)

#ml.rlocus(Ktheta * Hth)

#plt.show()
feederino = ml.feedback(Ktheta*Hth, 1, -1)
#print(ml.damp(feederino))

sys3 = ml.feedback(sys2 * Ktheta , numpy.array([0,1,0,0]))

#print(ml.ss(sys3))

y3, t3 = ml.step(numpy.matrix([0,0,1,0])*sys3, t)
#y4, t4 = ml.step(1/(1+2.5*s), t)
# plt.plot(t3, y3)
# plt.plot(t3, 0.95*numpy.ones(int(20/dt)))
# plt.show()

print(ml.stepinfo(y3, t3, SettlingTimeThreshold=0.05))