import random
end=None

def nwd(a,b,c):
    while(b>0):
        a,b=b,a%b
    while(c>0):
        a,c=c,a%c
    return a

def trojki(tab):
    licz=0
    for i in range(len(tab)):
        if(i+2<len(tab) and nwd(i,i+1,i+2)==1):
            licz+=1
        if(i+3<len(tab) and nwd(i,i+2,i+3)==1):
            licz+=1
        if(i+3<len(tab) and nwd(i,i+1,i+3)==1):            
            licz+=1
        if(i+4<len(tab) and nwd(i,i+2,i+4)==1):            
            licz+=1
    return licz


N=int(input())

tab=[random.randint(1,100) for _ in range (N)]

print(trojki(tab))