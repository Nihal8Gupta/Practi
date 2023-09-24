#WAP to get the info of glass of Champagne Tower
l=[[0]]
l[0][0]=100000009
for i in range(100):
    l.append([0]*(i+2))
    for j in range(i+1):
        if l[i][j]>=1:
            l[i+1][j]+=(l[i][j]-1)/2
            l[i+1][j+1]+=(l[i][j]-1)/2
            l[i][j]=1
    
print(l[33][17])