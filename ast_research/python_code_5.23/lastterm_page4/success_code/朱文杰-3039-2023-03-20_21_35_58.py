v=eval(input())
d=max(v)
x=min(v)
while d in v:
    v.remove(d)
while x in v:
    v.remove(x)
print(v)
