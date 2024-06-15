a = input().split(",")
b = input().split(",")
x1,x2=float(a[0]),float(a[1])
y1,y2=float(b[0]),float(b[1])
s = ((x1-x2)**2+(y1-y2)**2)**0.5
print(f"{s:.2f}")
