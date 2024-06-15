a=list(eval(input()))
n=max(a)
m=min(a)
b=a.copy()
for x in b:
    if x==n or x==m:
        a.remove(x)
print(a)
