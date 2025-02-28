def zam(n, s):
    l = ""
    print("system:", s, "liczba to")
    while n > 0:
        if n % s >= 10:
            l = (chr(ord("A") + (n % s) - 10)) + l
            n = n // s
        else:
            l = str(n % s) + l
            n = n // s

    print(l)


n = int(input())
for i in range(2, 17):
    zam(n, i)
