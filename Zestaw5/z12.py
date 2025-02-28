end=None

def zad11(tab,k):

    def reku(tab,k,ite=0):

        if ite==len(tab):
            return 0

        wyn=0
        for i in range(ite+1,len(tab)):
            if tab[ite]*tab[i]==k:
                print(ite,i)
                wyn+=1


        return wyn + reku(tab,k,ite+1)


    print(reku(tab,k))


tab = [2, 4, 5, 3, 8, 6, 10]
k= 20
zad11(tab,k)