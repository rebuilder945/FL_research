a=eval(input())
m=max(a)
n=min(a)
for x in a:
    if x==m:
        a.remove(x)
    elif x==n:
        a.remove(x)
print(a)
