v=eval(input())
d=max(v)
x=min(v)
if d or x in v:
    v.remove(d or x)
print(v)
