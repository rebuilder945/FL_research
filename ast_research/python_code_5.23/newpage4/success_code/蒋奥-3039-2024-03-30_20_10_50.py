a=eval(input())
m=max(a)
n=min(a)
while a.count(m)>0 or a.count(n)>0:
    a.remove(m)
    a.remove(n)
print(a)
