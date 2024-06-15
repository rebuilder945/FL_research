ls=eval(input())
a=max(ls)
for a in ls:
    ls.remove(a)
b=min(ls)
for b in ls:
    ls.remove(b)
print(ls)
