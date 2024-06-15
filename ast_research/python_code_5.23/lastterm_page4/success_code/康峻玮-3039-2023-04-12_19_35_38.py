ls=eval(input())
x=max(ls)
y=min(ls)
for x in range(ls):
    ls.remove(x)
for y in range(ls):
    ls.remove(y)
print(ls)
