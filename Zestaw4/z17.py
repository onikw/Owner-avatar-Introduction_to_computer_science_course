end=None

def zad(tab):
    N=len(tab)
    maks=0
    pam=(-1,-1)
    for y in range(N):
        for x in range(N):
            sum=0
            if x>0:
                sum+=tab[y][x-1]
            if x<N-1:
                sum+=tab[y][x+1]
            if y>0:
                sum+=tab[y-1][x]
            if y<N-1:
                sum+=tab[y+1][x]
            if sum>maks:
                maks=sum
                pam=(x,y)

    return pam



tab = [ [100, 1,4],
        [9,3,9],
        [19,13,63]]
print(zad(tab))