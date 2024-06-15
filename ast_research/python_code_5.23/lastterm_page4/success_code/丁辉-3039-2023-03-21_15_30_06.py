a=eval(input())
b=max(a)
c=min(a)
for x in a:
    if x==b:
        d=a.remove(x)
for x in d:
    if x==c:
        e=a.remove(x)
print(e)
