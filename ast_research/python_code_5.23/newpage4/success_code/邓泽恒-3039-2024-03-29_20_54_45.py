a=eval(input())
b=max(a)
c=min(a)
d=a.count(b)
for x in range(d):
    a.remove(b)
e=a.count(c)
for i in range(e):
    a.remove(c)
print(a)
