import random

end=None
def fun(T1,T2):
    liczz=0
    n, m = len(T1), len(T2)
    for i in range(m-n+1):
        for j in range(m-n+1):
            liczz=0
            for x in range(i,i+n):
                for y in range(j,j+n):
                    if licz(T2[x][y],T1[x-i][y-j]):
                        liczz+=1
            if(liczz/(n*n)>1/3):
                return (i,j)




def licz(a,b):
    licza=0
    liczb=0
    while a>0:
        licza+=a%2
        a//=2
    end
    while b>0:
        liczb+=b%2
        b//=2
    end
    if licza==liczb:
        return True
    return False


T2 = [
    [22, 52, 7, 8],
    [24, 109, 6, 7],
    [12, 14, 17, 18],
    [9, 9, 4, 4]]

T1 = [
    [2, 2],
    [2, 2]
]
print( fun(T1, T2) )