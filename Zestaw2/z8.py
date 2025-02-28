pref = []
pref = [0 for i in range(100)]

f1 = 1
f2 = 1
pref[0] = 0
for i in range(1, 100):
    pref[i] = pref[i - 1] + f1
    f1, f2 = f2, f1 + f2


f = 1
n = int(input())
war = 0
while f:
    n += 1
    war = 0
    for i in range(0, 10):
        for j in range(i, 10):
            if pref[j] - pref[i] == n:
                war = 1
    if war == 0:
        print(n)
        f = 0
