
end=None

a0=0
a1=1
b0=2
b1=2

f=0

i=int(input())
if(a0==i):
    print(b0)
else:
    f=1
    
i=int(input())
if(a1==i and f==0):
    a0,a1,b0,b1=a1,a1-(b1*b0),b1,b1+2*a1
    print(a0,a1,b0,b1)

    print(b0)
else:
    f=1


b0,b1=b1,b1+2*a1
     

while (f==0):
    i=int(input())       
    print(a0,a1,b0,b1)
    if(a0==i): 
        print(b0)
    else:
        f=1
    a0,a1,b0,b1=a1,a1-(b1*b0),b1,b1+2*a1



