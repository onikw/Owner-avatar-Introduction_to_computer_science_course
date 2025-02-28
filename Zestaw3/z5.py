end=None
l=[0 for i in range(10)]

a=int(input())

i=0
while a!=0:
    i=0
    while True:
        if l[i]<a:
            for j in range(9,i,-1):
                l[j]=l[j-1]
            l[i]=a    
            break
        elif l[i]==a:
            break
        elif i<10:
            i+=1
        else:
            break
    end
    a=int(input())
end
print(l[9])
