import random


def najdcr(tab):
    r=tab[1]-tab[0]
    dl=2
    maksdl=0
    for i in range(2,len(tab)):
        if tab[i]-tab[i-1]==r and r>0:
            dl+=1
            maksdl=max(maksdl,dl)

        else:
            dl=2
            r=tab[i]-tab[i-1]
    return maksdl


def najdcm(tab):
    r=tab[1]-tab[0]
    dl=2
    maksdl=0
    for i in range(2,len(tab)):
        if tab[i]-tab[i-1]==r and r<0:
            dl+=1
            maksdl=max(maksdl,dl)

        else:
            dl=2
            r=tab[i]-tab[i-1]
    return maksdl

N=int(input())
tab=[2*random.randint(1,50)-1 for i in range(N)]
print(tab)
print(najdcr(tab)-najdcm(tab))