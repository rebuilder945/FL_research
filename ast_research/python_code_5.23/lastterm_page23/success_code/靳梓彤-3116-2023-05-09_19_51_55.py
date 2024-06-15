import math
xA,yA=map(int,input().split(","))
xB,yB=map(int,input().split(","))
dir=(xA-xB)**2+(yA-yB)**2
dir2=math.sqrt(dir)
print("%.2f"%dir2)
