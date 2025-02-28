end = None


def zad(tab, il):
    ruchy = [(2, -1), (-2, -1), (1, -2), (-1, -2)]
    n = len(tab)
    licz = 0
    for j in range(n):
        for i in range(n):
            for ruch in ruchy:
                if (
                    i + ruch[0] >= 0
                    and i + ruch[0] < n
                    and j + ruch[1] >= 0
                    and j + ruch[1] < n
                    and il == tab[j][i] * tab[j + ruch[1]][i + ruch[0]]
                ):
                    licz += 1
            end
        end
    end
    return licz


tab = [[1, 0, 0, 0], [1, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 0]]
print(zad(tab, 1))
