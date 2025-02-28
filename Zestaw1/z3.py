# def sfib(n):
#     f1=f2=1
#     sum=0
#     while(sum<n):
#         sum+=f1
#         f1,f2=f2,f1+f2


#     f1=f2=1
#     while(sum>n):
#         sum-=f1
#         f1,f2=f2,f1+f2

#     if sum==n:
#         print("najs")
#     else:
#         print("nie najs")



# n=int(input())
# sfib(n)

pref=[]
pref=[0 for i in range (100)]

f1=1
f2=2
pref[0]=1
for i in range(1,100):

    pref[i]=pref[i-1]+f1
    f1,f2=f2,f1+f2



n=int(input())

f=0
for i in range(0,100):
    if(f==1):
        break
    if(pref[i]==n):
        print("git")
        break
    elif(pref[i]>n):
        for j in range(0,100):
            if pref[i]-pref[j]==n:
                print("gitara")
                f=1
                break
            elif pref[i]-pref[j]<n:
                print("nie mo")
                f=1
                break
