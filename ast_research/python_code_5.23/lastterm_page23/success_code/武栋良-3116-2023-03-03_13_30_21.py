a = input().split()
x1,y1 = float(a[0:1]),float(a[1:2])
b = input().split()
x2,y2 = float(b[0:1]),float(b[1:2])
e = ((x1-x2)**2+(y1-y2)**2)**0.5
print("%.2f"%(e))


