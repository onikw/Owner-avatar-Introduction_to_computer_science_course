def licz(n, m):
    l = 0
    dl = len(str(n))
    ite = 0
    for i in range(dl):
        l = l + n % 10 * (m % 2) * pow(10, ite)
        if m % 2 == 1:
            ite += 1

        m = m // 2
        n = n // 10

    return l


n = int(input())
for m in range(1, 2 ** len(str(n))):
    if licz(n, m) % 7 == 0:
        print(licz(n, m))
        
