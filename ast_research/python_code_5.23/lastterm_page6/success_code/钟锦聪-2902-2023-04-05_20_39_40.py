a=2
b=1
s=0
a1 = a/b
sun =[a1]
n = int(input())
for i in range(n-1):
    a=a+b
    b=a-b
    t = a/b
    sun.append(t)
for x in sun:
    s += x
print("%.4f"%s)

