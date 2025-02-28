def goldratio(a,b):
    while abs( (b/a) - (a+b)/b ) > 0.00001:
        a, b = b, a+b

    return b/a

print(goldratio(1,1))
