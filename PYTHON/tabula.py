#!/usr/bin/python
# -*- coding: utf-8 -*-
x = int(input("ievadiet skaitli: "))
print "\t\tDalijumu atlikumu vērtibas tabula"

for x in range(x, x+11, 1):
	print "%d \t"%(x),
	for i in range(1, 9, 1):
		sk_mod = x%i
		print "%d \t"%(sk_mod),
	print "\n"

