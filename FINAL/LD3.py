# -*- coding: utf-8 -*-

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
