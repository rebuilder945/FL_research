m=eval(input())
for x in m:
    m.remove(x)
    if x in m:
        pass
    else:
        m.append(x)
print(m)
