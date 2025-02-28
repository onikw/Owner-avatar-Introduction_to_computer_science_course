import random

N=int(input())
licz=0
lp=1000
for _ in range (lp):
    dni=[0 for i in range(365)]
    for i in range (N):
        dni[random.randint(0,364)]+=1
    for i in range (365):
        if dni[i]>1:
            licz+=1
            break

print(licz/lp)