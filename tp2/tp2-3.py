#!/usr/bin/env python

from math import sqrt, cos, sin

nombre = float(input("Nombre: "))

print("Choisir le type d'opération: ")
print("1: carré")
print("2: racine carré")
print("3: cosinus")
print("4: sinus")

reponse = int(input("Choix: "))

if reponse == 1:
	print(nombre**2)
elif reponse == 2:
	print(sqrt(nombre))
elif reponse == 3:
	print(cos(nombre))
elif reponse == 4:
	print(sin(nombre))
else:
	print("Il faudra apprendre à lire les choix la prochaine fois...")