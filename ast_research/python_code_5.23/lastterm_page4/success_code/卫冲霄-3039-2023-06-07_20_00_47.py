ls=eval(input())
m=max(ls)
n=min(ls)
for i in ls[:]:
    if i==m or i==n:
        ls.remove(i)
print(ls)

