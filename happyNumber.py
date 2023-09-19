#WAP to check given number is happy or not
def sumDigit(n):
    add=0
    while n!=0:
        r=n%10
        n=n//10
        add+=r**2
    if add==1 or add==7:
        return True
    elif add<10 and add!=1:
        return False
    else:
        return sumDigit(add)
        
print(sumDigit(int(input())))