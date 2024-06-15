a=eval(input())
min=min(a)
max=max(a)
b=a.count(min)
c=a.count(max)
for i in range(b):
    a.remove(min)
for i in range(c):
    a.remove(max)
print(a)
