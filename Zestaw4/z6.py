import random

end=None


N=int(input())
tab=[[random.randint(1,20) for _ in range (N)] for _ in range(N)]
tab2=[-1 for _ in range(N*N)]
t={}

for w in tab:
    print(w)
for w in tab:
    for e in w:
        t.setdefault(e,0)
        t[e]+=1
ind=0
for ite in t:
    if t[ite]==1:
        tab2[ind]=ite
        ind+=1

tab2.sort()
for i in tab2:
    if i>=0:
        print(i)
