#WAP to increment the digit which is prime in mob number 
num=int(input())
d=str(num)
print(d)
for i in range(10):
    if int(d[i])>1:
        for j in range(2,int(d[i])//2+1):
            if int(d[i])%j==0:
                break
        else:
             d=d.replace(d[i],str(int(d[i])+1))
            
print(d)