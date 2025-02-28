end=None
def sil(n):
    wyn=1
    while n > 0:
        wyn=wyn*n
        n-=1
    end
    return 1/wyn


n=int(input())

i=0
e=0

dok=1
while n>0:
    dok/=10
    n-=1

print(dok)
while dok<sil(i):
    e+=sil(i)
    i+=1
end
print(e)    
    