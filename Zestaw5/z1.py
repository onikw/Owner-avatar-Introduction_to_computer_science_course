import math

end=None

def zad1(N):
    def czyp(l):
        i=2
        while i*i<=l:
            if l%i==0:
                return False
            i+=1
        end


        return True
    def rek(N,liczba=0,ite=0,dl=N):
        if N==0 and liczba>9 and czyp(liczba) and dl!=liczba:
            print(liczba)
            return


        elif N==0:
            return


        dziel=N//10
        dod=N%10
        rek(dziel,liczba+dod*pow(10,ite),ite+1,dl)
        rek(dziel,liczba,ite,dl)





    rek(N)






N=2137
zad1(N)