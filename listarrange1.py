#By recursion approach
def insert(l,nl=[]):
    for i in range(len(l)):
        if type(l[i])==type([]):
            insert(l[i])
        else:
            nl.append(l[i])
    return nl
l=[1,2,[3,4],[5,[6,7],8],9,10]
print(l)
print(insert(l))