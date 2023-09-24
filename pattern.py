n=int(input())
star=1
space=n//2
for i in range(1,n+1):
    if i%2==0:
        d=2
    else:
        d=1
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(d,end=' ')
        if i%2==0:
            if st<star//2+1:
                d+=2
            else:
                d-=2
        else:
            if st<star//2+1:
                d+=1
            else:
                d-=1
                
    print()
    if i<n//2+1:
        star+=2
        space-=1
    else:
        star-=2
        space+=1