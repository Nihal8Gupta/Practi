
#WAP to counting minimum candy according to their ratings and highest ratings got maximum candy than its neighbours
#and each member holds atleast one candy Ratings =[1,2,87,87,87,2,1]
l=[[1,1],[2,1],[87,1],[87,1],[87,1],[2,1],[1,1]] #here i am giving one candy to all the members
add=0 
for i in range(len(l)):
    if i==0 and l[i]>l[i+1]:
        l[i][1]+=1
        
    elif i==len(l)-1:
        if l[i-1]<l[i]:
            l[i][1]+=l[i-1][1]
            
    elif (l[i-1]<l[i]<l[i+1]) or (l[i-1]<l[i] and l[i]==l[i+1]):
        l[i][1]+=l[i-1][1]
        
    elif l[i-1]==l[i] and l[i]>l[i+1] :
        l[i][1]+=l[i-1][1]
        
    elif l[i-1]>l[i]>l[i+1]:
        l[i-1][1]+=l[i][1]
        l[i][1]+=l[i+1][1]
for i in range(len(l)):
    add+=l[i][1]
print('Candy:',add)