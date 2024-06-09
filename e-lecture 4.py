import control.matlab as c
import matplotlib.pyplot as plt
import numpy as np
# Laplace variable
# s = c.tf([1, 0], [1])
#
# h1 = 1/((1+2*s)*(1+3*s))
# h2 = 1/(1+3*s)
#
# #feedback function with H1 leading to H2:
#
# print(h1.feedback(h2))
#
# # this results in cancelling pole-zero pairs:
# print(h1/(1+h1*h2))
# # can be fixed with minreal:
# print((h1/(1+h1*h2)).minreal())
# # but using the feedback function is more robust
# print(h1.feedback(h2))
#
# s = c.tf([1,0],[1])
#
# h1 = (1+0.4*s)/(s*(s**2+3*s+6))
#
# h2 = 1/(1+0.1*s)
#
# print(h1.feedback(h2))

#transfer Function 2

# s = c.tf([1,0],[1])
#
# k1=6
#
# k2 = 2.6
#
# h1 = k1/(2+s)
#
# h2 = (1 + 0.4*s)/(s**2+3*s+6)
#
# h3 = k2/(9+s)
#
# h = (h1 + h3).minreal()
#
# print((h*h2).num)
# print((h*h2).den)

#tf3

#I got 1 and 4, 1 is just equivalent, but with the signs swapped and 4's expression is equivalent (check ig your figures are differently laid out, YMMV)


#transfer functions, disturbance as input 2

# s = c.tf([1,0],[1])
#
# h1 = 5/(s**2 + 3*s + 5)
#
# k1 = 1
#
# g = k1*(1+0.2/s)
# print("--First Transfer Function--")
# print(((g*h1).feedback(1)).num)
# print(((g*h1).feedback(1)).den)
#
# print("--Second Transfer Function--")
# print(((g).feedback(h1)).num)
# print(((g).feedback(h1)).den)
#
# print("--Third Transfer Function--")
# print(((h1).feedback(g)).num)
# print(((h1).feedback(g)).den)
#
# print("--Fourth Transfer Function--")
# print((1/(1+h1*g)).num)
# print((1/(1+h1*g)).den)

#4.2 time domain signals

#representiong a certain function:

# t = np.arange(0, 10.01, 0.01)
# x = np.sin(t)
# plt.plot(t, x)
# plt.show()

#a ramp and hold input signal, of size 1, with a ramp starting at 1 second and completing at 5 seconds

# dt = 0.04
# t = np.arange(0.0, 30+dt, dt)
# u = np.hstack( (np.zeros( (1.0/dt) ), np.arange(0, 1+dt/4, dt/4), np.ones( (25/dt) ) ) )
# plt.plot(t, u)
# plt.show()

#4.2 signal

# dt = 0.2
# l = 20.
# freq = 4.8
# t = np.arange(0.0,l+dt,dt)
#
# sin = np.sin(t*(2*np.pi)*freq)
#
# plt.plot(t,sin)
# plt.plot(t,np.zeros(int(l/dt)+1))
# plt.show()

#creating a ramp

# dt = 0.15
# l = 30.
# t = np.arange(0.0,l+dt,dt)
# l_ramp = 9.
# size = 3.8
# u = np.hstack((np.arange(0,size*(1+dt/l_ramp), size*dt/l_ramp), size*np.ones(int((l-l_ramp)/dt))))
# s = sum(u)
# print(s)
# plt.plot(t,u)
# plt.show()

