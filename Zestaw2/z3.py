def pal(n):

    i=0

    while(i<len(n)//2):
        if(n[i]!=n[len(n)-i-1]):
            return False
        i+=1
    return True


n=input()
if(pal(n)):
    print("PAL DEC")
else:
    print("NIE PAL DEC")


n=int(n)

n=bin(n)
n=str(n)

n=n[2:]
print(n)

if(pal(n)):
    print("PAL BIN")
else:
    print("NIE PAL BIN")
