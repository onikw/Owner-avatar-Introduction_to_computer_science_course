end=None

def zad2(tab):
    def wag(n):
        i=2
        wyn=0
        while n>1:
            if n%i==0:
                wyn+=1
            while n%i==0:
                n//=i
            i+=1

        return wyn



    n=len(tab)
    def rek(i,a,b,c):
        if i==n:
            return a==b and b==c

        return rek(i+1,a+wag(tab[i]),b,c) or rek(i+1,a,b+wag(tab[i]),c) or rek(i+1,a,b,c+wag(tab[i]))



    print(rek(0,0,0,0))




tab=[2,17,6,5,10,6]
zad2(tab)