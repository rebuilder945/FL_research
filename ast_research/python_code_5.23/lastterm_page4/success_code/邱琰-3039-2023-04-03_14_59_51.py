ls=eval(input())
a=max(ls)
b=min(ls)
for i in range(ls.count(a)+1):
    ls().remove(a)
for i in range(ls.count(b)+1):
    ls().remove(b)
print(ls)
