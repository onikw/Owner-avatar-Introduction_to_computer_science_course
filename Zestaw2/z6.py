from math import sqrt


a=int(input())


i=int(sqrt(a))
while True:
    if(a%i==0):
        print(i,a//i)
        break
    else:
        i=i+1
