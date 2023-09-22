#WAP to check it Is subsquence
s='abc'
t='abhgyc'
x,y=len(s),len(t)
i=0
j=0
while i<x and j<y:
    if s[i]==t[j]:
        print(s[i])
        i+=1
    j+=1
if i==x:
    print(True)
else:
    print(False)