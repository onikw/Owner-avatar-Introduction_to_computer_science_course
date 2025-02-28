t=[2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]

dl=0
maks=0
for i in range (len(t)):
    for j in range (len(t)-1,-1,-1):
        while(i+dl<len(t) and j-dl>=0 and t[i+dl]==t[j-dl]):
            dl+=1
        maks=max(dl,maks)
        dl=0

print(maks)