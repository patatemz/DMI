# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
def mans_sinuss(x,n):
    k = 0
    a = (-1)**0*x**1/(1)
    S = a

    while k < n:
        k = k + 1
        R = (-1) * x**2 /(2*k*(2*k+1))
        a = a * R
        S = S + a
    return S

x = np.arange(0.0, 4, 0.01)
y = np.sin(x)

for i in range(0, 5, 1):
    yy = mans_sinuss(x,i)
    plt.plot(x,y)
    plt.plot(x,yy)

plt.show()


'''
#from math import sin
import numpy as np
import matplotlib.pyplot as plt
def mans_sinuss(x):
    k = 0
    a = (-1)**0*x**1/(1)
    S = a

    while k < 50:
        k = k + 1
        R = (-1) * x**2 /(2*k*(2*k+1))
        a = a * R
        S = S + a
    return S

x = np.arange(0.0, 6.28, 0.01)
y = np.sin(x)
yy = mans_sinuss(x)

plt.plot(x,y)
plt.plot(x,yy)
plt.show()

----
from math import sin

def mans_sinuss(x):
    k = 0
    a = (-1)**0*x**1/(1)
    S = a

    while k <= 3:
        k = k + 1
        R = (-1) * x**2 /(2*k*(2*k+1))
        a = a * R
        S = S + a
    return S

x = 0.89
y = sin(x)
yy = mans_sinuss(x)
print x, y, yy

x = 0.56
y = sin(x)
yy = mans_sinuss(x)
print x, y, yy
----------
from math import sin

x = 0.89
k = 0
a = (-1)**0*x**1/(1)
S = a

while k <= 3:
    k = k + 1
    R = (-1) * x**2 /(2*k*(2*k+1))
    a = a * R
    S = S + a

y = sin(x)
print x,y, S

x = 0.56
k = 0
a = (-1)**0*x**1/(1)
S = a

while k <= 3:
    k = k + 1
    R = (-1) * x**2 /(2*k*(2*k+1))
    a = a * R
    S = S + a

y = sin(x)
print x,y, S


from math import sin

x = 0.89
k = 0
a = (-1)**0*x**1/(1)
S = a

while k <= 3:
    k = k + 1
    R = (-1) * x**2 /(2*k*(2*k+1))
    a = a * R
    S = S + a

y = sin(x)
print x,y, S

x2 = 0.56
y2 = sin(x2)
'''
