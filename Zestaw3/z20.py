import random
end=None

def rozk(n):
    if(n<4):
        lipi.setdefault(n,0)
        lipi[n]+=1
    else:
        i=2
        nn=n
        while(i*i<=nn):
            if n%i==0:
                lipi.setdefault(i,0)
                while(n%i==0):
                    lipi[i]+=1
                    n=n//i
                end
            i+=1
        end
        if n>1:
            lipi.setdefault(n,0)
            lipi[n]+=1


def fun(T):
    flaga=1
    ite=0
    wyn=0
    for i in range(len(T)):
        lipi.clear()
        ite=i
        flaga=1
        while flaga and ite<len(T):
            rozk(T[ite])
            print(lipi.items())
            if max(lipi.values()) > 1:
                flaga=0
                wyn=max(wyn,ite-i)
            else:
                ite+=1
        end
    return wyn



N=int(input())

T=[random.randint(1,100) for i in range(N)]
print(T)

t=[2,23,33,35,7,4,6,7,5,11,13,22]
lipi={}

print(fun(T))