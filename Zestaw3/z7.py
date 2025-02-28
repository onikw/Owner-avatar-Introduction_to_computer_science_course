import random
end=None

def czyn(n):
    while n>0:
        if n%2==0:
            return False
        n//=10
    end
    return True

N=int(input())

l=[random.randint(1,1000) for i in range(N)]

for i in l:
    if czyn(i):
        print(i,': zawiera wyłącznie cyfry nieparzyste',sep='')
    else:
        print(i,': zawiera cyfry parzyste',sep='')
