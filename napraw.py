end = None


def napraw(ogrod):
    policz = 0
    n = len(ogrod)
    lustra = [(0, 0)] * n * n
    for i in range(n):
        for j in range(n):
            if ogrod[j][i] != " ":
                lustra[policz] = (i, j)
                policz += 1
    for L1 in range(policz - 1):
        for L2 in range(L1 + 1, policz):
            if ogrod[lustra[L1][1]][lustra[L1][0]] == "\\":
                ogrod[lustra[L1][1]][lustra[L1][0]] = "/"
            else:
                ogrod[lustra[L1][1]][lustra[L1][0]] = "\\"

            if ogrod[lustra[L2][1]][lustra[L2][0]] == "\\":
                ogrod[lustra[L2][1]][lustra[L2][0]] = "/"
            else:
                ogrod[lustra[L2][1]][lustra[L2][0]] = "\\"
            x = y = 0
            kier = (0, 1)
            while x >= 0 and y >= 0 and x < n and y < n:
                if ogrod[y][x] == " ":
                    x = x + kier[0]
                    y = y + kier[1]
                elif ogrod[y][x] == "\\":
                    if kier == (0, -1):
                        kier = (-1, 0)
                    elif kier == (1, 0):
                        kier = (0, 1)
                    elif kier == (0, 1):
                        kier = (1, 0)
                    elif kier == (-1, 0):
                        kier = (0, -1)
                    x = x + kier[0]
                    y = y + kier[1]
                elif ogrod[y][x] == "/":
                    if kier == (0, -1):
                        kier = (1, 0)
                    elif kier == (1, 0):
                        kier = (0, -1)
                    elif kier == (0, 1):
                        kier = (-1, 0)
                    elif kier == (-1, 0):
                        kier = (0, 1)
                    x = x + kier[0]
                    y = y + kier[1]

            if x - kier[0] == n - 1 and y - kier[1] == n - 1:
                return ogrod

            if ogrod[lustra[L1][1]][lustra[L1][0]] == "\\":
                ogrod[lustra[L1][1]][lustra[L1][0]] = "/"
            else:
                ogrod[lustra[L1][1]][lustra[L1][0]] = "\\"

            if ogrod[lustra[L2][1]][lustra[L2][0]] == "\\":
                ogrod[lustra[L2][1]][lustra[L2][0]] = "/"
            else:
                ogrod[lustra[L2][1]][lustra[L2][0]] = "\\"


ogrod = [
    [" ", " ", " ", " ", " "],
    [" ", "/", " ", "\\", " "],
    [" ", " ", " ", " ", " "],
    ["/", " ", " ", "/", " "],
    [" ", "/", " ", " ", "\\"],
]

print(napraw(ogrod))
