xa,ya=map(int,input().split(","))
xb,yb=map(int,input().split(","))
# print(xa,ya,xb,yb)
c=xa-ya
d=xb-yb
e=c**2+d**2
h=e**(0.5)
print("%.2f"%(h))


