import control.matlab as ml
import matplotlib.pyplot as plt
import numpy as np

dt = 0.1

s = ml.tf([1,0],[1])

# h1 = (s+1)/(2*s**4 + 10.4*s**3 +22.02 * s**2 + 42.5*s+ 48.12)
#
# h2 = (s+1)/(2*s**4 + 10*s**3 +20 * s**2 + 40*s+ 48)
#
# h3 = (s-2)/ ((s+1)*(s+3)*(s+2+2j)*(s+2-2j))
#
# h4 = (s-0.25)/ ((s+1)*(s)*(s+2+2j)*(s+2-2j))

t = np.arange(0,1000, dt)

#print(ml.poles(h1))
#print(ml.poles(h2))

# y1, t1 = ml.step(h1,t)
#
# y2, t2 = ml.step(h2,t)
#
# y3, t3 = ml.step(h3,t)
#
# y4, t4 = ml.step(h4,t)

#plt.plot(t1, y1)
#plt.plot(t2, y2)
# plt.plot(t3, -y3)
# plt.plot(t4, -y4)
# plt.show()

#question 3

# h = 3/ ((s+12.8)*(s-1.3))
# k = 1 #5.54
# feedback = ml.feedback(18*h, 1)
# #crit damped: 16.57
# # ml.rlocus(h*k)
# # plt.show()
#
# y1, t1 = ml.step(5*feedback, t)
#
# print(ml.stepinfo(y1, t1, SettlingTimeThreshold=0.05))
#
# plt.plot(t1,y1)
# plt.show()

#ex 4

# Ky = 0.2
# Kc = 4
# v = 11
# l=5
#
# h = (l*s*v)/(l*s**2+Kc*v*s + Kc*Ky*v**2)
#
# # print(ml.damp(h))
#
# t1, y1 = ml.step(h,t)
#
# plt.plot(y1,t1)
# plt.show()

#ex 5
#gain = 1/10**(37.8/20)
Kp = 0.01 #1
Kd = Kp*14 #0.14 #Kp*19
Ki = Kp*0.01 #0.0001
#D = Kp *(1+(Kd/Kp)*s)
# h = Kp *(1+(Kd/Kp)*s)*1.4/s**2 *2/(s+2)
#
# # print(ml.margin(h))
# # ml.bode(h)
# # plt.show()
D = (1+ (Kd/Kp)*s + (Ki/Kp)/s)

#h = 1.4 / (s**2 + (1.4*2)/(s+2)*D)
h = D * 1.4/s**2 * 2/(s+2)

#ml.damp(h)
#ml.rlocus(ml.minreal(h))
#plt.show()
print(ml.poles(h))
# print(ml.minreal(h))
# t1, y1 = ml.step(h, t)

# plt.plot(y1,t1)
# plt.show()

