def zad13(n):
    tab = [0] * n

    def rek(n, i , tab):

        if n==0:
            print(tab)
        if i==0:
            minn=1
        else:
            minn=tab[i-1]
        for j in range(minn,n+1):
            tab[i]=j
            rek(n-j,i+1,tab)
            tab[i]=0

    rek(n, 0, tab)





zad13(4)
