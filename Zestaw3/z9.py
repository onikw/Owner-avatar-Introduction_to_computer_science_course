import random

N=int(input())

tab=[random.randint(1,100) for i in range(N)]
dl=1
maks=0
print(tab)
for i in range (N):
    for j in range(i+1,N):
        if tab[j-1]<tab[j]:
            dl+=1
        else:
            break
    maks=max(maks,dl)
    dl=1
        
print(maks)
    
