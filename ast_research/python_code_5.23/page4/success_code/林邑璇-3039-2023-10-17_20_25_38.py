a=eval(input())
b=max(a)
c=min(a)
d=a.count(b)
e=a.count(c)
for i in range(d):
    a.remove(b)
for i in range(e):
    a.remove(c)
print(a)

