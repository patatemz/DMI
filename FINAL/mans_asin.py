#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import asin
x = 1. * input("Lietotāj, lūdzu, ievadi argumentu (x): ")
print type (x)
y = asin(x)
print "asin(%.2f)=%.2f"%(x,y)

k = 0
a = 1*x**1/1
S = a
print "a0 = %6.2f S0 = %6.2f"%(a,S)

while k <= 10:
    k = k + 1
    R = x**2*((2*k-1)**2)/(2*(2*k+1)*k)
    a = a * R
    S = S + a
    print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)
print asin(x)
