end=None


def fun(tab):
    n=len(tab)
    dlmaks=3
    i=0
    j=0
    maks=0
    while j<n:
        i=0
        while i<n:
            ite=0
            sum=0
            while ite+i<n and ite<dlmaks:
                sum+=tab[j][i+ite]
                ite+=1
                maks=max(sum,maks)
            end
            i+=1
        end
        j+=1
    end


    j=0
    while j<n:
        i=0
        while i<n:
            ite=0
            sum=0
            while ite+j<n and ite<dlmaks:
                sum+=tab[j+ite][i]
                ite+=1
                maks=max(sum,maks)

            end
            i+=1
        end
        j+=1
    end
    return maks

T = [
    [9,2,-1,4],
    [9,4,-3,0],
    [3,2,4,5],
    [99999,-2,-3,4]
]

print(fun(T))