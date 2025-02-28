def f(tab):
    maks=0
    dl=0
    for i in range(len(tab)):
        while i-dl>=0 and i+dl<len(tab) and tab[i-dl]==tab[i+dl] and tab[i-dl]%2==1:
            dl+=1
            maks=max(maks,dl*2-1)
        dl=0


    dl=0
    for i in range(len(tab)):
        while i-dl>=0 and i+dl+1<len(tab) and tab[i-dl]==tab[i+dl+1] and tab[i-dl]%2==1:
            dl+=1
            maks=max(maks,dl*2)
            print(i,dl)
        dl=0
    return maks


tab=[3,3,5,5,3,3,8]
print(f(tab))
        
    

