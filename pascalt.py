from math import perm,factorial
i=0
l=[[]]*3
while i<3:
    l[i]=list(map(lambda j:perm(i,j)//factorial(j),list(range(0,i+1))))
    i+=1
print(l)