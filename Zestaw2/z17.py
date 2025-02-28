from math import *


a1=1
for i in range(500):
    a1=a1-(pow(a1,a1)-20)/(pow(a1,a1)*( log(a1)+1 ))
    print(a1)