#WAP to find prime factors of given number
n=int(input())
i=2
s=set()
while i<=n//2+1:
    if n%i==0:
        s.add(i)
        n=n//i
        i=1
    i+=1
else:
    s.add(n)
print(s)