#WAP to Find the Difference
s='aa'
t='aaa'
while True:
    if len(s)==0:
        break
    if s[0] in  t:
        t=t.replace(s[0],'',1)
        s=s.replace(s[0],'',1) 
    
print(t)