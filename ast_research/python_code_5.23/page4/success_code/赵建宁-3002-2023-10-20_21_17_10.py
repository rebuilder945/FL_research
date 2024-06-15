a = eval(input())
s = sum(a)
l = len(a)
x = s / l
y = int(x)
if x - y == 0:
    print(y)
else:
    print("%.2f"%x)
