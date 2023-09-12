#WAP to print Flag in pattern
n=7
for i in range(1,n+1):
    for j in range(1,n+n):
        if i==1 or i==n:        #first line of star
            print('*',end=' ')
        elif j==n+n-1 and i!=1 and i!=n:
            print('*',end=' ')
        elif j==1 and i!=1 and i!=n:
            print('*',end=' ')
        elif i==n//2 or i==n//2+2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(1,n+n):
    if i==n+n-1:
        print('***')
    else:
        print('* *')

