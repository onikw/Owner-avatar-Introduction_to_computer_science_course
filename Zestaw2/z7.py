
def wz(i):
    return(i*i+i+1)
n=int(input())

i=1
while(wz(i)<n and n%wz(i)!=0):
    i+=1

if(n%wz(i)==0):
    print("Li",i)