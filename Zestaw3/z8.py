import random

end=None

def sito(n):
    i=2
    l=[True for i in range(n+1)]
    l[0]=l[1]=False
    while i*i<=n:
        if l[i]:
            for j in range(i+i,n+1,i):
                l[j]=False
        i+=1
    end
    return l

def skok(tab,l):
    rozm=len(tab)
    czydosk=[False for i in range(rozm)]
    czydosk[0]=True
    i=0
    while i<rozm:
        if czydosk[i]:
            for j in range(i+1,rozm):
                if l[j-i] and tab[j]%(j-i)==0:
                    czydosk[j]=True
        i+=1
    print(tab)
    print(czydosk)



n=int(input())
tab=[random.randint(1,20) for i in range(n)]
skok(tab,sito(n))