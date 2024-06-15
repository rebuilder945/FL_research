a=eval(input())
a.sort()
b=max(a)
c=min(a)
for i in range(a.count(b)):
    a.remove(b)
for x in range(a.count(c)):
    a.remove(c)
print(a)
