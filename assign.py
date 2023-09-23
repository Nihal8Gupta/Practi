s='hello*3'
ns=''
for i in range(len(s)):
    if s[i].isalpha():
        ns+=chr(ord(s[i])+1)
    else:
        ns+=s[i]
print(ns)
for i in range(len(ns)-1):
    if s[i].isalpha():
        if s[i]==s[i+1]:
            ns=ns.replace(ns[i:i+2:],'')
    if s[i].isdigit():
        ns=ns.replace(ns[i],'')
if s[-1].isdigit():
    ns=ns.replace(ns[-1],'')
print(ns)