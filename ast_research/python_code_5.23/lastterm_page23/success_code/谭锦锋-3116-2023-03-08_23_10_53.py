a = input()
b = input()
a=a.split(",")
b=b.split(",")
x1 = float(a[0])
y1 = float(a[1])
x2 = float(b[0])
y2 = float(a[1])
d = ((x1-x2)**2+(y1-y2)**2)**1/2
f = "%.2f"%d
print(d)
