import math
a,b=eval(input())
c,d=eval(input())
r=math.sqrt((a-c)**2+(b-d)**2)
sText="%.2f" % (r)
print(sText)
