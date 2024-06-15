a = input().split()
x1,y1 = float(print(a[0:1])),float(print(a[1:2]))
b = input().split()
x2,y2 = float(print(b[0:1])),float(print(b[1:2]))
e = ((x1-x2)**2+(y1-y2)**2)**0.5
print("%.2f"%(e))


