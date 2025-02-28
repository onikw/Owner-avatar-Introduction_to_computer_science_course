import random

end = None


def naj(tab, N):
    maks = 0
    wyn=()
    for i in range(N):
        for j in range(N):
            if maks<licz(tab, N, i, j):
                maks = licz(tab, N, i, j)
                wyn=(i,j,licz(tab, N, i, j))

    return wyn


def licz(tab, N, i, j):
    wierzs = 0
    kols = 0
    for x in range(N):
        wierzs += tab[i][x]
        kols += tab[x][j]
        if wierzs==0:
            return 0
    return kols / wierzs


N = int(input())
tab = [[random.randint(-10, 10) for _ in range(N)] for _ in range(N)]
for w in tab:
    print(w)
print(naj(tab, N))
