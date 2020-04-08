from math import *
def sumaciagu(a1=1,r=1,ile=10):
    suma=0
    a=a1
    for i in range(ile):
        suma+=a
        a+=r
    print(suma)
sumaciagu()