#By normal approach
l=[1,2,[3,4],[5,[6,7],8],9,10]
print(l)
nl=[]
while True:
    if len(l)==0:
       break
    t=0
    if type(l[0])==type([]):
         t=l.pop(0)
         for j in range(len(t)):
             if type(t[j])==type([]):
                 l.insert(0,t[j])
             else:
                 nl.append(t[j])   
    else:
        nl.append(l.pop(0))
print(nl)