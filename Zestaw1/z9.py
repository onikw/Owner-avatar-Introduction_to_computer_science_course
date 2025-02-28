n=int(input())


s=[]
i=1
while(i*i<n):
    if(n%i==0):
        print(i)
        s.append(n//i)
    i+=1
if(i*i==n):
    print(i)

while(len(s)>0):
    print(s[len(s)-1])
    s.pop(len(s)-1)
