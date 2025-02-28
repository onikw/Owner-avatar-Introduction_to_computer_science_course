import random

end = None


def nwd(a, b):
    while b > 0:
        return nwd(b, a % b)
    return a


def f(tab, N):
    ite = 0
    q = (0, 0)
    nq = (0, 0)
    d = 0
    maks=0
    for i in range(N):
        wyn = 0
        while ite + i < N - 1:
            d = nwd(tab[ite][ite + i], tab[ite + 1][ite + i + 1])
            nq = (tab[ite + 1][ite + i + 1] // d, tab[ite][ite + i] // d)
            if q == nq:
                wyn += 1
            else:
                q=nq
                maks=max(maks,wyn)
                wyn=0

            ite += 1
        ite = 0
        maks=max(maks,wyn)

        end


    for i in range(1,N):
        wyn = 0
        ite=0
        while ite + i < N - 1:
            d = nwd(tab[i+ite][ite], tab[ite+i + 1][ite  + 1])
            nq = (tab[ite + i+1][ite  + 1] // d, tab[ite+i][ite ] // d)
            if q == nq:

                wyn += 1
            else:
                q=nq
                maks=max(maks,wyn)
                wyn=0

            ite += 1
        ite = 0
        maks=max(maks,wyn)

        end
    return (maks+1)


N = int(input())
tab = [[random.randint(1, 5) for _ in range(N)] for _ in range(N)]
for w in tab:
    print(w)

T= [ [1,2,3,4],
     [5,7,7,8],
     [9,10,36,12],
     [13,14,20,216]]

print(f(tab,N))
