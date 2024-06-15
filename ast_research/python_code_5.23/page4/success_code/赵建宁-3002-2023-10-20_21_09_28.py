a = eval(input())
s = 0
for i in range(a):
    s = s + i
l = len(a)
x = s / l
y = int(x)
if x - y == 0:
    print(x)
else:
    print("%.2f"%x)
