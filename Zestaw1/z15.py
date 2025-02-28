from math import sqrt
a=sqrt(0.5)
pom=a
for i in range(100):

    pom=sqrt(0.5+0.5*pom)
    a=a*pom
print(2/a)