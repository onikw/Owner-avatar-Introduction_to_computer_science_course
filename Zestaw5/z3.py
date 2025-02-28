end=None

def zad3(t,k):
    def reku(tab,kol,wier):
        if wier==7:
            return tab[wier][kol]



        mikoszt=2000




        if kol-1>=0:
            kosz=tab[wier][kol]+reku(tab,kol-1,wier+1)
            mikoszt=min(mikoszt,kosz)



        if kol+1<8:
            kosz=tab[wier][kol]+reku(tab,kol+1,wier+1)
            mikoszt=min(mikoszt,kosz)



        kosz=tab[wier][kol]+reku(tab,kol,wier+1)
        mikoszt=min(mikoszt,kosz)
        return mikoszt


    print(reku(t,k,0))


t= [
    [4, 9, 2, 7, 1, 1, 1, 8],
    [5, 1, 7, 3, 9, 1, 4, 6],
    [3, 8, 6, 5, 4, 1, 9, 7],
    [9, 2, 4, 8, 7, 1, 3, 1],
    [7, 6, 3, 2, 8, 1, 5, 4],
    [1, 5, 8, 6, 4, 1, 7, 9],
    [8, 4, 9, 1, 6, 1, 2, 3],
    [6, 7, 1, 4, 5, 1, 8, 2]
]
k=4
zad3(t,k)