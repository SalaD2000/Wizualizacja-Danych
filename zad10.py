def lista(** rzeczy):
    ilosc=0
    for cos in rzeczy:
        print(cos," x ",rzeczy[cos])
        ilosc+=int(rzeczy[cos])
    return ilosc
a=lista(cebula=10,burak=22)
print(a)