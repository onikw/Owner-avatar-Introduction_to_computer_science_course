end=None
def f(tab):
    ind=0
    suma=0
    sumaind=0
    maks=0

    for i in range(len(tab)-1):
        suma=tab[i]
        sumaind=i
        ind=0
        while  i+ind+1<len(tab) and tab[i+ind]<tab[i+ind+1]:
            suma+=tab[i+ind+1]
            sumaind+=i+ind+1
            ind+=1
        if(sumaind==suma):
            maks=max(maks,suma)
        
    return maks

        
        
        


tab=[0,3,5,3,4,5]
print(f(tab))
        
    

