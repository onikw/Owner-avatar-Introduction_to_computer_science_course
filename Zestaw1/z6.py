
p=1
k=5
s=(p+k)/2
for i in range(50):
    print(s)
    if(pow(s,s)>2020):
        k=s
    else:
        p=s
    s=(p+k)/2
