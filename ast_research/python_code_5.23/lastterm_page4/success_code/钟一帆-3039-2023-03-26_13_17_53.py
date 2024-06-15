a=eval(input())
m=max(a)
n=min(a)
b=a.copy()
for x in a:
    if x==m or x==n:
        b.remove(x)
print(b)

