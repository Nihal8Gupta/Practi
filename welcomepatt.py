#WAP to print welcome
n=int(input())
star=1
space=n-1
for i in range(1,n+1):
    if i==n//2+1:
        print('- '*(2*n-7),'WELCOME','- '*(2*n-7),end=' ')
    else:
        for sp in range(1,space+1):
            print('-',end=' ')
        
        for st in range(1,star+1):
            print('.|.',end=' ')
        
        for sp in range(1,space+1):
            print('-',end=' ')
    print()
    if i<n//2+1:     
        star+=2
        space-=2
    else:
        star-=2
        space+=2