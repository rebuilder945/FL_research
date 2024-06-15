a=eval(input())
m=max(a)
print(m)
n=min(a)
print(n)
for x in a:
    if x==m or x==n:
        a.remove(x)
print(a)
