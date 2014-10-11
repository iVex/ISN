#!/usr/bin/env python

x = float(input("Entrez x entre -1 et 1: "))
y = float(input("Entrez y entre -1 et 1: "))

if x>0 and y>0:
	print("Quadrant n°1")
if x<0 and y>0:
	print("Quadrant n°2")
if x<0 and y<0:
	print("Quadrant n°3")
if x>0 and y<0:
	print("Quadrant n°4")