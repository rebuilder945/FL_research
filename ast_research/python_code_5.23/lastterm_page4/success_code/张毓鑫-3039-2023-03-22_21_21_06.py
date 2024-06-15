a=eval(input())
b=max(a)
c=min(a)
d=a.count(b)
e=a.count(c)
for i in range(d):
    a.remove(b)
if len(a)>0:
    for i in range(e):
        a.remove(c)
        print(a)
else:
    print(a)
