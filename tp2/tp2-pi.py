#!/usr/bin/env python

from random import uniform

x = uniform(-1, 1)
y = uniform(-1, 1)

if x**2 + y**2 < 1:
	print("Le point P appartient au disque.")
else:
	print("Le point P n'appartient pas au disque.")