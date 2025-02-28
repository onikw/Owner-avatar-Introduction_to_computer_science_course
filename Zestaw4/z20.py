end = None


def suma(tab):
    n = len(tab)
    wiersze = [0] * n
    kolumny = [0] * n

    for i in range(n):
        for j in range(n):
            wiersze[i] += tab[j][i]
            kolumny[i] += tab[i][j]
        end
    end
    return (wiersze, kolumny)


def zad(tab):
    n = len(tab)
    wiersze, kolumny = suma(tab)
    maks = 0
    pampos = (-1, -1, -1, -1, -1)
    zm = 0

    for j in range(n - 1):
        for i in range(n - 1):
            for y in range(j + 1, n):
                for x in range(i + 1, n):
                    zm = (
                        wiersze[i]
                        + wiersze[x]
                        + kolumny[j]
                        + kolumny[y]
                        - tab[y][i]
                        - tab[j][x]
                        - 2 * tab[j][i]
                        - 2 * tab[y][x]
                    )
                    if zm > maks:
                        maks = zm
                        pampos = (i, j, x, y, maks)
    return pampos


tab = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(zad(tab))