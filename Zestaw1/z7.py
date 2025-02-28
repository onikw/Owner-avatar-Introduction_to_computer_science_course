
n=int(input())
f1=f2=1
while(True):
    if(f1*f2>n):
        print("nie da się")
        break
    if(f1*f2==n):
        print(f1," ",f2)
        break
    f1,f2=f2,f1+f2


