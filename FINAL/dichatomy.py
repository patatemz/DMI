#!/usr/bin/python
#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def mans_sinuss(x):
    a=(-1)**0*x**1/(1)
    S=a
    f=500
    k=0
    n=1
    while k<=f:
        R=(-1)*x**2/((n*2)*(n*2+1))
        a=a*R
        S=S+a
        n=n+1
        k=k+1
    return S
#zimesana
a=1.57
b=4.71
x=np.arange(a,b,0.01)
y=mans_sinuss(x)
plt.plot(x,y)
plt.grid()
plt.show()
#saknes meklesana
delta_x=1.e-3
funa=mans_sinuss(a)
funb=mans_sinuss(b)
if funa*funb>0:
    print("Starp [%.2f,%.2f] funkcijai nav saknes"%(a,b))
    print("vai funkcijai saja intervala ir paru saknu skaits, ko ar so funkciju nemekle")
    exit()
print("uz robezam f(%.2f)=%.2f f(%.2f)=%.2f"%(a,funa,b,funb))
k=0
while b-a>delta_x:
    x=(a+b)/2
    k=k+1
    funx=mans_sinuss(x)
    print("%3d. a=%.4f f(%.4f)=%7.4f b=(%.4f)"%(k,a,x,funx,b,))
    if funa*funx>0:
        a=x
    else:
        b=x
print("a=%.4f f(%.4f)=%7.4f b=(%.4f)"%(a,x,funx,b,))
print("iteraciju skaits ir %d"%(k))
