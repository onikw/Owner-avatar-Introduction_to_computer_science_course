def zad10(mac):
    def utnij(mac,x,y):
        return [wier[:x] + wier[x + 1:] for wier in (mac[:y] + mac[y + 1:])]
    def wyz(mac):


        wyn=0

        if len(mac)==1:
            return mac[0][0]

        for y in range(len(mac)):
            wyn+=mac[y][0]*((-1)**y)*wyz(utnij(mac,0,y))


        return wyn

    return wyz(mac)






mac = [
    [3, 1, -2],
    [4, 2, 1],
    [5, 6, 3]
]
print(zad10(mac))
