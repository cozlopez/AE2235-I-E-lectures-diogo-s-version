import control.matlab as c

# Laplace variable
s = c.tf([1, 0], [1])

h1 = 1/((1+2*s)*(1+3*s))
h2 = 1/(1+3*s)

#feedback function with H1 leading to H2:

print(h1.feedback(h2))

# this results in cancelling pole-zero pairs:
print(h1/(1+h1*h2))
# can be fixed with minreal:
print((h1/(1+h1*h2)).minreal())
# but using the feedback function is more robust
print(h1.feedback(h2))

