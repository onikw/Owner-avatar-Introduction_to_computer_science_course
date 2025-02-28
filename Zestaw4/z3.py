import random

end=None
def f(tab,N):
    f=0

    for i in range (N):
        f=0
        for j in range(N):
            if not czyp(tab[i][j]):
                f=1
                break
        if f==0:
            return True
    return False



def czyp(n):
    while n>0:
        if n%2==0:
            return True
        n//=10
    end
    return False




N=int(input())
tab=[[random.randint(0,100) for _ in range(N)] for _ in range(N)]
for w in tab:
    print(w)
print(f(tab,N))