a=eval(input())
b=max(a)
c=min(a)
print(b)
d=a.count(b)
e=a.count(c)
for i in range(d):
    a=a.remove("b")
for i in range(e):
    a=a.remove("c")
print(a)

