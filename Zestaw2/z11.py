def czyr(n):
    i=0
    while(i<len(n)-1):
        if(n[i]>=n[i+1]):
            return False
        i+=1
    return True





a=input()
print(czyr(a))
