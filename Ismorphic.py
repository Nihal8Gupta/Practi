#WAP to check given strings are Isomorphic Strings or not
s='egg'
t='add'
d={}
if len(s)==len(t):
    for i in range(len(s)):
        if s[i] not in d:
            if t[i] not in d.values():
                d[s[i]]=t[i]
            else:
                print(False)
        else:
            if d[s[i]]!=t[i]:
                print(False)
    else:
        print(True)
else:
    print(False)