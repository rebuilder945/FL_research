import math
a,b=map(int,input().split(","))
c,d=map(int,input().split(","))
D=math.sqrt((a-c)**2+(b-d)**2)
print("%.2f"%D)
