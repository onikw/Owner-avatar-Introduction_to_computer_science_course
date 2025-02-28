
pam=0
def pierw(a):
    i=1
    global pam
    while True:
        if(a-i>=0):
            a=a-i
            i=i+2
            pam=i

        else:
            return a


n=int(input())

if(pierw(n)>0):
    print(-1)
else:
    print((pam-1)//2)