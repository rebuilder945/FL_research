s=eval(input())
a=max(s)
a1=s.count(a)
for i in range(a1):
    s.remove(a)
b=min(s)
b1=s.count(b)
for x in range(b1):
    s.remove(b)
print(s)
