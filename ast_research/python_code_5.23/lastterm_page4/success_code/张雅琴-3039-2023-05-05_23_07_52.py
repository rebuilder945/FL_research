a=eval(input())
n=max(a)
m=min(a)
b=a.copy()
for i in a:
    if i==n or i==m:
        b.remove(i)
print(b)

