def f(n):
    i=0
    while(i<len(n)-1):
        if(n[i]==n[len(n)-1]):
            return False
        i+=1
    return True






n=input()
print(f(n))