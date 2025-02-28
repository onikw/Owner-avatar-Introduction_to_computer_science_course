def spr(a,b):
    l1=[0]*10
    l2=[0]*10


    if(len(a)!=len(b)):
        return False
    else:
        for i in range (0,len(a)):
            l1[ord(a[i])-ord('0')]+=1
            l2[ord(b[i])-ord('0')]+=1


    for i in range(0,10):
        if(l1[i]!=l2[i]):
            return False
    return True


a=input()
b=input()

print(spr(a,b))
