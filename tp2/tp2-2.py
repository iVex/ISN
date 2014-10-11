#!/usr/bin/env python

from math import sqrt

print("Equation de second degre: ax²+bx+c.")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

d = (b**2)-4*a*c

if d>0:
	print("x1: ", (-b-sqrt(d))/2*a)
	print("x2: ", (-b+sqrt(d))/2*a)
elif d==0:
	print("x: ", -b/(2*a))
else:
	print("Pas de solutions.")