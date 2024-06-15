m=eval(input())
for x in m:
    if x==0:
        m.remove(x)
        m.append(x)
    else:
        pass
print(m)
