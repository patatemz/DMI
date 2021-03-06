# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
def mans_asinuss(x):
    k = 0
    a = 1*x**1/1
    S = a

    while k < 10:
        k = k + 1
        R = x**2*((2*k-1)**2)/(2*(2*k+1)*k)
        a = a * R
        S = S + a
    return S
#zimesana
a=0
b=7
x=np.arange(a,b,0.01)
y=mans_asinuss(x)
plt.plot(x,y)
plt.grid()
plt.show()
#saknes meklesana
delta_x=1.e-3
funa=mans_asinuss(a)
funb=mans_asinuss(b)
if funa*funb>0:
    print("Starp [%.2f,%.2f] funkcijai nav saknes"%(a,b))
    print("vai funkcijai saja intervala ir paru saknu skaits, ko ar so funkciju nemekle")
    exit()
print("uz robezam f(%.2f)=%.2f f(%.2f)=%.2f"%(a,funa,b,funb))
k=0
while b-a>delta_x:
    x=(a+b)/2
    k=k+1
    funx=mans_asinuss(x)
    print("%3d. a=%.4f f(%.4f)=%7.4f b=(%.4f)"%(k,a,x,funx,b,))
    if funa*funx>0:
        a=x
    else:
        b=x
print("a=%.4f f(%.4f)=%7.4f b=(%.4f)"%(a,x,funx,b,))
print("iteraciju skaits ir %d"%(k))
