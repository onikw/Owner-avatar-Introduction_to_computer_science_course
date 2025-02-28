end = None


def zad4(tab, n):
    ruchy = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    def czygit(x, y, n):
        return x >= 0 and y >= 0 and x < n and y < n

    def rek(tab, x, y, ruch):

        if n * n == ruch:
            return True


        for nx, ny in ruchy:
            if czygit(x + nx, y + ny, n) and tab[y + ny][x + nx] == 0:
                tab[y+ny][x+nx]=ruch+1
                if rek(tab, x + nx, y + ny, ruch + 1):
                    return True
                tab[y + ny][x + nx] = 0

        return False


    tab[0][0]=1
    rek(tab, 0, 0, 1)


n = 5
tab = [[0 for i in range(n)] for i in range(n)]
zad4(tab, n)
for w in tab:
    print(w)
