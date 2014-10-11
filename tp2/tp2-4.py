#!/usr/bin/env python

a = float(input("Entrez nombre a: "))
b = float(input("Entrez nombre b: "))
c = float(input("Entrez nombre c: "))

if a>b:
	a, b = b, a
if b>c:
	b, c = c, b

print(a, b, c)
