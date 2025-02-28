import math


def zad17(l1,l2):

    dl1=int(math.log10(l1))+1
    dl2=int(math.log10(l2))+1

    def prime(licz):
        if licz==2 or licz==3:
            return True
        i=2
        while i*i<=licz:
            if licz%i==0:
                return False
            i+=1

        return True


    def reku(ind1=0,ind2=0,licz=0):
        if ind1<dl1 and ind2<dl2:
            a=l1//(10**(dl1-ind1-1))%10
            reku(ind1+1,ind2,licz*10+a)
            a=l2//(10**(dl2-ind2-1))%10
            reku(ind1,ind2+1,licz*10+a)
        elif ind1<dl1:
            a=l1//(10**(dl1-ind1-1))%10
            reku(ind1+1,ind2,licz*10+a)
        elif ind2<dl2:
            a=l2//(10**(dl2-ind2-1))%10
            reku(ind1,ind2+1,licz*10+a)
        elif prime(licz):
            print(licz)


    reku()



l1,l2=123,75

zad17(l1,l2)