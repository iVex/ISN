#!/usr/bin/env python

from math import exp, log

"""
Ef = Eo*exp(-ti/constT)
print(Ef)
"""

Eo = float(input("E0: "))
Eu = float(input("E1 (E1>E0): "))
constT = 10**-6

ti = 0.37*Eo
tf = 0.37*Eu

t = tf - ti
print(t)