end=None
def czyp(n):
    i=2
    while i*i<=n :
        if n%i==0:
            return False
        i+=1
    return True

def suma(t1,t2,mask):
    sum=0
    ite=0
    while ite<len(t1):
    
        if mask%3==0:
            sum+=t1[ite]+t2[ite]
        elif mask%3==1:
            sum+=t1[ite]
        else:
            sum+=t2[ite]
        mask//=3
        ite+=1
    end
    return sum



def f(t1,t2):
    licz=0
    for i in range(3**len(t1)):
        if czyp(suma(t1,t2,i)):
            licz+=1
    return licz

t1 = [1, 4, 52, 3, 5, 2, 35]
t2 = [33, 0, 93, 5, 12, 2, 5]
print(f(t1,t2))
