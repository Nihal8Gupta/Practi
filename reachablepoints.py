#Reachable points (Medium)
Sx=1 #3,4,5 (3,5),(4,6),(5,7),(6,7),(7,7)
Sy=2 #6,7
Fx=1
Fy=2
t=2
def reachtime(Sx,Sy,Fx,Fy,t):
    x=abs(Sx-Fx)
    y=abs(Sy-Fy)
    if x==0 and y==0:
        return t>1
    else:
        return x<=t and y<=t
if reachtime(Sx,Sy,Fx,Fy,t):
    print(True)
else:
    print(False)
