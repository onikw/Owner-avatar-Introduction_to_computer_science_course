n = 0


for j in range(1, 1000001):
    n = j
    s = 1
    i = 2
    while i * i < n:
        if n % i == 0:
            s = s + i + n // i
        i += 1
    if i * i == n:
        s += i

    n=s
    ss=s
    i=2
    s=1

    while i * i < n:
        if n % i == 0:
            s = s + i + n // i
        i += 1
    if i * i == n:
        s += i

    if(s==j and j>n):
        print(j," ",n)
