ls=eval(input())
a=max(ls)
b=min(ls)
c=ls.copy()
for d in c:
    if d==a or d==b:
        ls.remove(d)
print(ls)

