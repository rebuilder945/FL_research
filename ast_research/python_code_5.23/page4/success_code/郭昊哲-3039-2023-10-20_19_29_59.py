a=eval(input())
a.sort()
x=a.count(a[0])
d=a.count(a[-1])
for i in range(x):
    a.remove(a[0])
for i in range(d):
    a.remove(a[-1])
print(a)

