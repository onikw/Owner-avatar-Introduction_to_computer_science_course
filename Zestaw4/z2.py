import random

end = None


def rozk(n):
    while(n>0):
        if n%2==1:
            return True
        n=n//10
    end
    return False

N = int(input())
tt = [[random.randint(1, 100) for _ in range(N)] for _ in range(N)]
for r in tt:
    print(r)

f = True
fw = False
for i in range(N):
    fw = False
    for j in range(N):
        if rozk(tt[i][j]):
            fw = True
            break
    if fw == False:
        f = False
        break
print(f)
