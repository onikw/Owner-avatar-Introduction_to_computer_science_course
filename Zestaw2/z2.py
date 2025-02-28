a=int(input())
b=int(input())
n=int(input())


print(a//b,".",end="",sep="")

for i in range(n):
    if(a%b!=0):
        a*=10
        if(a%b==0):
            print(a//b,end='',sep='')
            break
        else:
            print(a//b,end='',sep='')
            a=a%b