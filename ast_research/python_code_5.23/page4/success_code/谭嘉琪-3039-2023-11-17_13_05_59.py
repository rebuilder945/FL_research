ls=eval(input())
a=max(ls)
b=min(ls)
c=ls.count(a)
d=ls.count(b)
for i in range(c):
    ls.remove(a)
if a!=b:
    for i in range(d):
        ls.remove(b)
print(ls)
