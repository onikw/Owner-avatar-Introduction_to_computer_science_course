def czyzl(n):
    i=2
    while(i*i<=n):
        if n%i==0:
            return True
        i+=1
    return False

def czyp(n):
    i=2
    while(i*i<=n):
        if n%i==0:
            return False
        i+=1
    return True

def fib(tab):
    f1=1
    f2=2
    flaga=0
    if czyp(tab[0]):
        flaga=1

    while(f2<len(tab)):
        for i in range(f1+1,f2):
            if(czyp(tab[i])):
                flaga=1
        if czyzl(tab[f1])==False or czyzl(tab[f2])==False:
            return False
        f1,f2=f2,f1+f2
    
    if flaga:
        return True
    return False
        



tab=[12, 4, 8, 15, 7, 6]
print(fib(tab))

