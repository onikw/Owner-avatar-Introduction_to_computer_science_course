import random

end=None

def zad(tab,N):
    flaga1=flaga2=0
    for i in range(N):
        for j in range(N):
            if tab[i][j]==0:
                flaga1=1

            if tab[j][i]==0:
                flaga2=1
                
        if flaga2==0 or flaga1==0:
            print(i,j)
            return False
        flaga1=flaga2=0
    return True


N=int(input())
tab=[[random.randint(0,1) for _ in range(N)] for _ in range(N)]

for w in tab:
    print(w)
print(zad(tab,N))
