#WAP to print alphabate Rangoli
print('-: Alphabate Rangoli :-')
s=int(input())
n=s*2-1
star=1
space=n-1
for i in range(1,n+1):
    d=96+s
    for sp in range(1,space+1):
        print('-',end='')
    for st in range(1,star+1):
        if st<star//2+1:
            print(chr(d),end='-')
            d-=1
        else:
            if st==star:
                print(chr(d),end='')
                d+=1
            else:
                print(chr(d),end='-')
                d+=1
    for sp in range(1,space+1):
        print('-',end='')
    print()
    if i<n//2+1:
        star+=2
        space-=2
    else:
        star-=2
        space+=2