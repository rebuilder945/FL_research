x1,y1=map(int,input().split(","))
x2,y2=map(int,input().split(","))
d1=x1-x2
d2=y1-y2
d3=d1**2+d2**2
d=d3**0.5
stext="%.2f"%(d)
print(stext)
