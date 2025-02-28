import random
end=None

def czyp(n):
    while(n>0):
        if(n%2==1):
            return True
        n=n//10
    return False

N=int(input())

l=[random.randint(1,1000) for i in range(N)]

for i in l:
    if czyp(i):
        print(i,": zawiera cyfrę nieparzystą.",sep='')
    else:
        print(i,": nie zawiera cyfry nieparzystej.",sep='')
