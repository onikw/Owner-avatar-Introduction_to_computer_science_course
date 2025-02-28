end = None


def zad5(tab):
    def czyp(n):

        if n<2:
            return False
        j = 2
        while j * j<= n:
            if n % j == 0:
                return False
            j+=1
        end
        return True

    end

    def konw(tab):
        wyn = 0
        n = len(tab)
        for i in range(n):
            wyn += tab[i] * (2 ** (n - i - 1))

        return wyn


    end

    def rek(i, j, tab):
        if j > len(tab) - 1:
            return False
        if j == len(tab) - 1:
            print (i,j,konw(tab[i : j + 1]))
            return czyp(konw(tab[i : j + 1]))
        if czyp(konw(tab[i : j + 1])):
            print (i,j,konw(tab[i : j + 1]))
            return rek(j + 1, j + 2, tab) or rek(i, j + 1, tab)
        return rek(i, j + 1, tab)

    return rek(0, 1, tab)


tab = [1, 1, 1, 0, 1, 1]
print(zad5(tab))
print(tab[0:3])