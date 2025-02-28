def f(n):
    if(n==1):
        return 2
    else:
        return (f(n-1)*3+1)



n=int(input())


i=1
while(f(i)<n and n%f(i)!=0):
    i+=1

if(n%f(i)==0):
    print("git")