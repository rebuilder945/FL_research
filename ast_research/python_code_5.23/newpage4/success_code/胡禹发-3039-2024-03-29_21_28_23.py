a=list(eval(input()))
b=max(a)
c=min(a)
for i in range(1,a.count(b)):
    a.remove(b)
for i in range(1,a.count(c)):
    a.remove(c)
print(a)

