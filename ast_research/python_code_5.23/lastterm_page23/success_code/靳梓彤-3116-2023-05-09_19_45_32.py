import math
xA,yA=eval(input().split(","))
xB,yB=eval(input().split(","))
dir=(xA-xB)**2+(yA-yB)**2
dir2=math.sqrt(dir)
print(dir2)
