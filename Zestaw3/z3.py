def sito(N):
    l[0]=0
    l[1]=0
    i=2
    while(i*i<=N):
        if(l[i]==1):
            for j in range(i+i,N+1,i):
                l[j]=0
        i+=1


n=int(input())
l=[1]*(n+1)

sito(n)
for i in range(0,n+1):
    print(i,":",l[i])