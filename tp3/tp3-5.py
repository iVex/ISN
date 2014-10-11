#!/usr/bin/env python
from random import uniform

i=0
Nc=0

N = input('N value: ')
N = int(N)

while i<N:
    x = uniform(-1,1)
    y = uniform(-1,1)
    if x**2 + y**2 < 1:
        Nc+=1
    print((Nc * 4 /N))
    i+=1

pi= (Nc * 4 /N)
print(pi)
