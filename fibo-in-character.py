def fibo(n):
    a=1
    b=2
    for i in range(1,n):
        a+=b
        a,b=b,a
    return a
s='MAN'
n=0
for i in range(len(s)):
    r=fibo(ord(s[i])-64)
    n+=r
print(n)