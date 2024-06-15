import math
xA,yA=input().split(",")
xB,yB=input().split(",")
dir=(xA-xB)**2+(yA-yB)**2
dir2=math.sqrt(dir)
print(dir2)
