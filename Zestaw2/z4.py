def rozk(a):
    while a % 2 == 0:
        a = a / 2
    while a % 3 == 0:
        a = a / 3
    while a % 5 == 0:
        a = a / 5
    if a == 1:
        return True
    else:
        return False


n = int(input())

zlicz = 0
for i in range(1, n + 1):
    if rozk(i):
        zlicz += 1



print(zlicz)
