ls=eval(input())
a=max(ls)
b=min(ls)
while ls.count(a)>0:
    ls.remove(a)
while ls.count(b)>0:
    ls.remove(b)
print(b)
