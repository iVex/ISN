#!/usr/bin/env python

nb = int(input("4 chiffres à décrypter: "))

nb1, nb2, nb3, nb4 = int(nb/1000), int((nb%1000)/100), int((nb%100)/10), int((nb%10))

nb1, nb3, nb2, nb4 = nb3, nb1, nb4, nb2

nb1 = (nb1+3)%10
nb2 = (nb2+3)%10
nb3 = (nb3+3)%10
nb4 = (nb4+3)%10

nb = str(nb1)+str(nb2)+str(nb3)+str(nb4)
print(nb)