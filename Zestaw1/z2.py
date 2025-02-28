

minn=100000
pami=pamj=0

for i in range(1,100):
    for j in range(i,100):
        fib=1
        fibs=j
        fibss=i
        while(fib<2023):
            fib=fibs+fibss
            fibss=fibs
            fibs=fib
        if fib==2023:
            print(i," ",j," ",fib)
            if i+j<minn:
                minn=i+j
                pami=i
                pamj=j

print(minn," ",pami," ",pamj)



