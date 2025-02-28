
suma=0

def sc(n):
    s=0
    while(n>0):
        s+=n%10
        n=n//10
    return s


def rozk(n):
    i=2
    global suma
    while(i*i<=n):
        if(n%i==0):
            suma+=sc(i)
            while(n%i==0):
                n=n//i
        i+=1

    if(n>1):
        suma+=sc(n)


n=int(input())
rozk(n)
if(suma==sc(n)):
    print("Smitha")
else:
    print("Nie Smitha")