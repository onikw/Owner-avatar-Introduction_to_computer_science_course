from math import sqrt

n=int(input())

f1=f2=g1=g2=1
while(f1<sqrt(n)+1):
    if(n%f1==0):
        g1,g2=f1,f2
        while g1*f1<n:
            g1,g2=g2,g1+g2

        if(g1*f1==n):
            print(g1,f1)
            break
    f1,f2=f2,f1+f2
else:
    print("nie")
