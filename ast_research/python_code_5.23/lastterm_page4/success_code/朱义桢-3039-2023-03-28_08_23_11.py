a=eval(input())
m=max(a)
n=min(a)
for i in a[:]:
    if i==m or i==n:
        a.remove(i)
print(a)


