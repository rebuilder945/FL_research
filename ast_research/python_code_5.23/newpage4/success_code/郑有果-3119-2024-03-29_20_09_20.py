m=eval(input())
for x in m:
    m.remove(x)
    if m.count(x)==1:
        pass
    else:
        m.remove(x)
print(m)
