import random

end=None


N=int(input())
tab=[[random.randint(1,30) for _ in range (N)] for _ in range(N)]
tab2=[0]*N*N
for i in range(N):
    tab[i].sort()
for w in tab:
    print(w)
for i in range(N):
    tab2[i]=tab[0][i]

kon=N
ite=0
for z in range(1,N):
    for i in range(N):
        ite=0
        while ite<kon and tab2[ite]<tab[z][i]:
            ite+=1
        for j in range(kon, ite,-1):
            tab2[j]=tab2[j-1]
        tab2[ite]=tab[z][i]

        kon+=1
        end
print(tab2)