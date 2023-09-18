#WAP to evalute median of given list
L1=eval(input("Enter the first list="))
L2=eval(input("Enter the second list="))
L3=(L1+L2)
l=len(L3)
if l%2==0:
    print(f"Median of {L3}=",(L3[l//2-1]+L3[l//2])/2)
else:
    print(f"Median of {L3}=",L3[l//2])