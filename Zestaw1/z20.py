
from math import sqrt
a=int(input())
b=int(input())

for i in range (50):
    a,b=sqrt(a*b),(a+b)/2

print(a," ",b)