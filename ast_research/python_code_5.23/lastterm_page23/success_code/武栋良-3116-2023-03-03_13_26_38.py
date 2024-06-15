a = input().split()
x1,y1 = a[0:1],a[1:2]
b = input().split()
x2,y2 = b[0:1],b[1:2]
e = ((x1-x2)**2+(y1-y2)**2)**0.5
print("%.2f"%(e))


