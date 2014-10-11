#!/usr/bin/env python

import sys

i=1
x=0
n=1
while i<10:
    if i<5:
        while x<(5-i):
            sys.stdout.write(' ')
            x+=1
    else:
        while x<(i-5):
            sys.stdout.write(' ')
            x+=1
    x=0
    while x<n:
        sys.stdout.write('*')
        x+=1
    print('')
    x=0
    if i<5:
        n=n+2
    else:
        n=n-2
    i+=1
