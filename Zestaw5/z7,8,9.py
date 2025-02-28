end=None


def zad7(tab,m):
    def rek(tab,m,i=0):
        if m==0:
            return True
        elif m<0 or i>=len(tab):
            return False
        return rek(tab,m-tab[i],i+1) or rek(tab,m,i+1)
    return rek(tab,m)



def zad8(tab,m):
    def rek(tab,m,i=0):
        if m==0:
            return True
        elif i>=len(tab):
            return False
        return rek(tab,m-tab[i],i+1) or rek(tab,m,i+1) or rek(tab,m+tab[i],i+1)
    return rek(tab,m)



def zad9(tab,m):
    def rek(tab,m,i=0,wag=[]):
        if m==0:
            print(wag)
            return True
        elif i>=len(tab):
            return False
        return rek(tab,m-tab[i],i+1,wag+[tab[i]]) or rek(tab,m,i+1,wag) or rek(tab,m+tab[i],i+1,wag+[tab[i]])
    return rek(tab,m)





tab=[2,2,7,3]
print(zad9(tab,6))