import math

end = None


def zad18(tab, w, k):
    def spr(l1, l2):
        return True

    wierz = [(0, 0), (7, 0), (7, 7), (0, 7)]
    ruchy = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    flag=False

    def reku(kx, ky, wx, wy,tabr,ind=0):
        nonlocal flag
        if kx == wx and ky == wy:

            flag=True
            print(tabr)

        if not flag:
            for rx, ry in ruchy:
                if 0 <= kx + rx and 0 <= ky + ry and 8 > kx + rx and 8 > ky + ry:

                    if (abs(wx - kx) >= abs(wx - (rx + kx))) and (abs(wy - ky) >= abs(wy - (ry + ky))):
                        if tab[ky][kx] % 10 < (tab[ky + ry][kx + rx]// (10 ** int(math.log10(tab[ky + ry][kx + rx])))):
                            tabr[ind]=(rx,ry)
                            reku(kx + rx, ky + ry, wx, wy,tabr,ind+1)



    for wx, wy in wierz:
        flag=False
        tabr=[(0,0)]*17
        reku(k, w, wx, wy,tabr)
        if(flag):
            print("gitara")
        else:
            print("niegit")





tab = [
    [9, 8, 7, 6, 1, 6, 7, 8],
    [1, 2, 3, 4, 2, 6, 7, 8],
    [2, 3, 4, 5, 5, 3, 8, 9],
    [3, 4, 5, 6, 5, 4, 9, 1],
    [4, 5, 6, 7, 8, 5, 1, 2],
    [5, 6, 7, 8, 9, 6, 2, 3],
    [6, 7, 8, 9, 1, 7, 9, 4],
    [7, 8, 9, 1, 2, 3, 8, 9],
]
w, k = 0, 4
zad18(tab, w, k)
