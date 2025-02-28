


k=int(input())
p=0
i=1
krok=0.0005
while(i<=k):
    p=p+((1/i)*krok)
    i+=krok

print(p)
       