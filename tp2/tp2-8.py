#!/usr/bin/env python

nb = int(input("4 chiffres à crypter: "))

nb1, nb2, nb3, nb4 = int(nb/1000), int((nb%1000)/100), int((nb%100)/10), int((nb%10))

nb1 = (nb1+7)%10
nb2 = (nb2+7)%10
nb3 = (nb3+7)%10
nb4 = (nb4+7)%10

nb1, nb3, nb2, nb4 = nb3, nb1, nb4, nb2

nb = str(nb1)+str(nb2)+str(nb3)+str(nb4)
print(nb)