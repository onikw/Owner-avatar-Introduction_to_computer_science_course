end=None

def czyp(N):
    if N==2 or N==3 or N==5 or N==7:
        return True
    return False

def rozk(N):
    while N>0:
        if  czyp(N%10):
            return True
        N//=10
    return False


def zad(tab):
    N=len(tab)
    for w in tab:
        f=1
        for i in w:
            if  not rozk(i):
                f=0

        if f==1:
            return True
    return False








tab = [ [14,12,23,962],
        [960,846,211,7],
        [333, 991, 484, 884],
        [6455, 557, 6566, 992] ]
print(zad(tab))
