def zad15(rozm):
    tab=[-1]*rozm


    def czywp(tab,i,ind):
        for j in range (ind):
            if tab[j]==i:
                return False
        return True

    def czywuk(tab,i,ind):
        for j in range (ind):
            if tab[j]+ind-j==i:
                return False
            if tab[j]-ind+j==i:
                return False
        return True

    x=True
    def reku(tab,ind=0):

        nonlocal x

        if ind>rozm-1:
            x=False
            print(tab)
        elif x:
            for i in range(rozm):
                if czywp(tab,i,ind) and czywuk(tab,i,ind):
                    tab[ind]=i
                    reku(tab,ind+1)
                    tab[ind]=-1

    reku(tab)


rozm=8
zad15(rozm)