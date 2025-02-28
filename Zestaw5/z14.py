def hanoi(n,pocz,chwil,kon):
    if n>0:
        hanoi(n-1,pocz,kon,chwil)
        print("idze z",pocz,"na",kon)
        hanoi(n-1,chwil,pocz,kon)



hanoi(3,"A","B","C")