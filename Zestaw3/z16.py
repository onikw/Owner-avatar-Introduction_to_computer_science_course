def f(tab):
    tab.sort()
    dl=len(tab)
    if(dl==1):
        return False
    if(tab[0]==tab[1] or tab[dl-1]==tab[dl-2]):
        return False
    return True



tab=[1,2,5,5,4]
print(f(tab))