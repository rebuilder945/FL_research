a=eval(input())
m=max(a)
n=min(a)
while a.count(m)>0:
    a.remove(m)
while a.count(n)>0:
    a.remove(n)
print(a)
