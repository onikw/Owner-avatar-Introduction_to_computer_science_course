end=None

def f(T,k):
    N=len(T)
    wy=0
    for py in range(0,N-2,1):
        for px in range(0,N-2,1):
            roz=2
            while py+roz<N and px+roz<N:
                wy=T[py][px]*T[roz+py][px]*T[py][px+roz]*T[py+roz][px+roz]
                if wy==k:
                    return ((px+px+roz)//2,(py+py+roz)//2)
                roz+=2
            end






T = [ [1,2,3,4,5],
      [5,6,7,8,3],
      [9,10,11,12,4],
      [13,14,15,16,1],
      [4, 3, 5, 3, 1] ]

print( f(T, 297 ))