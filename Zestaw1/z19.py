
def sil(s):
    licz=1
    for i in range(1,s+1):
        licz*=i
    return 1/licz


def num_e(d):
    e=0
    kon=0
    ite=0
    while True:
        if(sil(ite)<d):
            return e
        else:
            e+=sil(ite)
            ite+=1









a=float(input())
print(num_e(a))