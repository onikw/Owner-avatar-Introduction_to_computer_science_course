def nwd(a,b):
    if(b>1):
        return nwd(b,a%b)

    return a


a=int(input())
b=int(input())
c=int(input())

print(nwd(nwd(a,b),c))
