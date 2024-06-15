m=eval(input())
a=max(m)
b=min(m)
for x in m:
    if x==a:
       m.remove(a)
    elif x==b:
       m.remove(b)
    else:
        pass
if m:
    pass
else:
    m.extend([a,b])
print(m)
