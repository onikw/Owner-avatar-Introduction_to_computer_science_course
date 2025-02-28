end=None

def przyj(tab,N):
    flag=0
    licz=0
    for i in range(N):
        for j in range(N):
            flag=1

            if i>0 and not samecy(tab[j][i],tab[j][i-1]):
                flag=0
            if i<N-1 and not samecy(tab[j][i],tab[j][i+1]):
                flag=0
            if j>0 and not samecy(tab[j][i],tab[j-1][i]):
                flag=0
            if j<N-1 and not samecy(tab[j][i],tab[j+1][i]):
                flag=0
            if flag==1:
                licz+=1
                print(i,j)
    return licz








def samecy(a,b):
    tab1=[0]*10
    tab2=[0]*10
    while a>0:
        tab1[a%10]+=1
        a//=10
    end
    while b>0:
        tab2[b%10]+=1
        b//=10
    end

    for i in range (10):
        if not ((tab1[i]>0 and tab2[i]>0) or (tab1[i]==0 and tab2[i]==0)):
            return False
    return True










T = [ [321,132,1312,0],
      [3333221,1223,7,0],
      [9,10,0,12],
      [13,14,0,16] ]

print(przyj(T,4))
print(samecy(12,0))