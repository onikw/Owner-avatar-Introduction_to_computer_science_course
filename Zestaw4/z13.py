import random
end=None

def sito(tab,N):
    i=2
    tab[0]=tab[1]=0
    while i*i<=N:
        if tab[i]==1:
            for j in range(i+i,N+1,i):
                tab[j]=0
        i+=1

    end
def fun(tab,N,czyp):
    liczba=1
    flag=0
    for i in range(N):
        for j in range(N):
            liczba=tab[i][j]
            flag=0
            for x in range(N):
                for y in range(N):
                    if czyp[liczba+tab[x][y]]:
                        flag=1
            if flag==0:
                tab[i][j]=0







N=int(input())
tab=[[random.randint(1,500) for _ in range(N)] for _ in range(N)]
czyp=[1]*1001

for w in tab:
    print(w)
sito(czyp,1000)
fun(tab,N,czyp)
for w in tab:
    print(w)