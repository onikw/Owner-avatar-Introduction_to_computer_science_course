n=int(input())

i=pow(10,n-1)
while i<pow(10,n):
    l=i
    s=0
    while(l>0):
        s=s+pow(l%10,n)
        l=l//10
    if(s==i):
        print(i)
    i+=1
