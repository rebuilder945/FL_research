import math
# xa,ya=map(int,input().split(","))
# xb,yb=map(int,input().split(","))
xa,ya=eval(input())
xb,yb=eval(input())
# print(xa,ya,xb,yb)
# c=xa-ya
# d=xb-yb
c = xb-xa
d = yb-ya
e=c**2+d**2
# h=e**(1/2)
h = math.sqrt(e)
print("%.2f"%(h))


