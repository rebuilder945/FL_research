a=eval(input())
b=max(a)
c=min(a)
for x in a:
    if x==b:
        a=a.remove(x)
    if x==c:
        a=a.remove(x)
print(a)
