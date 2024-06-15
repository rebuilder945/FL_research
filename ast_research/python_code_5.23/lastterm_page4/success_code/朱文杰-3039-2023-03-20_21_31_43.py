v=eval(input())
d=max(v)
x=min(v)
while d or x in v:
    v.remove(d or x)
print(v)
