a = input().split()
a1 = print(a[0])
a2 = print(a[1])
x1,y1 = a1,a2
b = input().split()
b1 = print(b[0])
b2 = print(b[1])
x2,y2 = b1,b2
e = ((x1-x2)**2+(y1-y2)**2)**0.5
print("%.2f"%(e))


