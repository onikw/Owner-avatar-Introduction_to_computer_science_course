def czyp(n):
    if n == 1:
        return "panie to jeden jest"
    i = 2
    while i * i <= n:
        if n % i == 0:
            return "złożona"
        i += 1
    return "pierwsza"


n = int(input())
print(czyp(n))
