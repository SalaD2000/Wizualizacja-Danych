from math import *
def iloczynciagu(a1=1,r=2,ile=3):
    suma=1
    a=a1
    for i in range(ile):
        suma*=a
        a+=r
    print(suma)
iloczynciagu(5,2,2)