end=None

def czyp(N):
    if N==2 or N==3 or N==5 or N==7:
        return True
    return False

def rozk(N):
    while N>0:
        if not czyp(N%10):
            return False
        N//=10
    return True


def zad(tab):
    N=len(tab)
    for w in tab:
        f=0
        for i in w:
            if  rozk(i):
                f=1
                print(i)

        if f==0:
            return False
    return True








tab = [ [14,12,23,962],
        [960,846,211,7],
        [333, 991, 484, 884],
        [645, 557, 666, 992] ]
print(zad(tab))
