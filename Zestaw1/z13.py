def nww(a,b):
    return (a*b)//nwd(a,b)

def nwd(a,b):
    while(b>0):
        return nwd(b,a%b)
    return a

a=int(input())
b=int(input())
c=int(input())

print(nww(nww(a,b),c))
