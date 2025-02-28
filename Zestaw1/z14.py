def sil(n): return n*sil(n-1) if n > 1 else 1

a=int(input())
c=0
for n in range(5):
    c=c+(pow(-1,n)*pow(c,2*n))/sil(n*2)
print(c)