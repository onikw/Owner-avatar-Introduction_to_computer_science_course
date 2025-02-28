end=None 

def czybit(maska,ilebit):
    licz=0
    while(maska):
        licz+=maska%2
        maska//=2
    end
    if(licz==ilebit):
        return True
    return False

def scal(maska,s1,s2):
    wyn=''
    ite1=0
    ite2=0
    while(ite1+ite2<len(s1)+len(s2)):
        if(maska%2==1):
            wyn=wyn+s1[ite1]
            ite1+=1
        else:
            wyn=wyn+s2[ite2]
            ite2+=1

        maska//=2
    end
    return wyn


def czyp(a):
    if(a==2 or a==3): return True
    if(a%2==0 or a%3==0 or a<=1): return False

    i=5
    while(i*i<=a):
        if(a%i==0):
            return False
        i+=2
        if(a%i==0):
            return False
        i+=4
    end
    return True    

a=input()
b=input()
dl=len(a)+len(b)

for i in range(1,2**dl):
    if(czybit(i,len(a)) and czyp(int(scal(i,a,b))) and scal(i,a,b)[0]!='0'):
        print(scal(i,a,b))
