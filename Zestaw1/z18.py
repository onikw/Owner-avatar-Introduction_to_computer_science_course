
n=float(input())
s=n/3
while(abs(s-(n/s/s))>0.00000000001):
    s=(n/s/s+s+s)/3
    print(s)