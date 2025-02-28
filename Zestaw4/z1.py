end=None
def spirala(n):
    tt=[[0 for _ in range (n)] for _ in range (n)]
    poczatek=0
    koniec=n-1
    ite=0
    indeks=0
    while(poczatek<=koniec):
        for i in range (poczatek,koniec+1):
            tt[poczatek][i]=ite
            ite+=1
        for i in range (poczatek+1,koniec+1):
            tt[i][koniec]=ite
            ite+=1

        for i in range (koniec-1,poczatek-1,-1):
            tt[koniec][i]=ite
            ite+=1
        for i in range (koniec-1,poczatek,-1):
            tt[i][poczatek]=ite
            ite+=1
        poczatek+=1
        koniec-=1
    end


    for w in tt:
        print(w)

n=int(input())
spirala(n)
