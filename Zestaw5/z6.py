end=None

def zad6(tab):

    def reku(tab,dl,w1,w2,odp=0):

        nonlocal minn,pam


        if dl>=0:
            reku(tab,dl-1,w1+tab[dl],w2+dl,odp+1)
            reku(tab,dl-1,w1,w2,odp)
        elif w1==w2 and w1>0:
            if odp<minn:
                minn=odp
                pam=w1

    minn=10**6
    pam=0



    reku(tab,len(tab)-1,0,0)
    print(pam)



tab=[1,7,3,5,11,2]
zad6(tab)