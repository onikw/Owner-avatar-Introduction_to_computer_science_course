def f(n):
    return ((n%2)*(3*n+1)+(1-n%2)*n//2)

maks=0
pam=0
ite=0
war=0
for i in range(2,10001):
    ite=1
    war=f(i)
    while(war>1):
        war=f(war)
        ite+=1
    if(maks<ite):
        maks=ite
        pam=i

print(maks)
