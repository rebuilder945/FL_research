a = input()
b = input()
a=a.split(",")
b=b.split(",")
x1 = eval(a[0])
y1 = eval(a[1])
x2 = eval(b[0])
y2 = eval(a[1])
d = ((x1-x2)**2+(y1-y2)**2)**1/2
f = "%.2f"%d
print(f)
