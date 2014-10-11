#!/usr/bin/env python3.2

notes = [0]
i=0

while notes[i]>=0 and notes[i]<=20:
    i+=1
    note = input("Note: ")
    note = int(note)
    notes.append(note)

del notes[0]

moy = 0
for x, item in enumerate(notes):
    moy += notes[x]

moy = moy/x
print(moy)