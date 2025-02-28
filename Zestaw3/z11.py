


def najdc(tab):
    r=tab[1]/tab[0]
    dl=2
    maksdl=0
    for i in range(2,len(tab)):
        if tab[i]/tab[i-1]==r:
            dl+=1
            maksdl=max(maksdl,dl)

        else:
            dl=2
            r=tab[i]/tab[i-1]
    return maksdl


tab = [2,4,6,8,10,20,40,80,160,2,4,8,16,32]
print(tab)
print(najdc(tab))


