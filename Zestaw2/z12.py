def f(n):
    pam=len(str(n))
    print(pam)
    while(n>0):
        if(n%10==pam):
            return True
        n=n//10
    return False





n=int(input())
print(f(n))