x1, y1 = input()
x2, y2 = input()
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
s1 = x1 - x2
s2 = y1 - y2
s3 = s1 ** 2 + s2 ** 2
s = s3 ** 0.5
print("%.2f"%s)
