import random


def najdc(tab):
    r=tab[1]-tab[0]
    dl=2
    maksdl=0
    for i in range(2,len(tab)):
        if tab[i]-tab[i-1]==r:
            dl+=1
            maksdl=max(maksdl,dl)

        else:
            dl=2
            r=tab[i]-tab[i-1]
    return maksdl


tab = [1, 2, 3, 4, 5, 6, 7, 0, 5, 10, 15, 20,25,30,35,40]
print(tab)
print(najdc(tab))