#WAP to arrange a character with LRU algorithim
s='j5p4lqta0d'
l=['A','B','A','C','A','B']
nl=[]
for i in range(len(l)):
    if l[i] not in nl and len(nl)<=5:
        nl.append(l[i])
        
    elif l[i] not in nl:
        
        nl.pop(0)
        
        nl.append(l[i])
        
    else:
        ind=nl.index(l[i])
        nl.append(nl.pop(ind))
        
    if len(nl)>5:
        nl.pop(0)
print(nl)
nl=list(map(lambda i:i if i.lower() not in s else '',nl))
print('-'.join(nl))
