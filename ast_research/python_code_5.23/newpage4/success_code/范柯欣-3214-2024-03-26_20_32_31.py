m=list(eval(input()))
i=m.count(0)

for b in range(i+1):
    if b>0:
        m.append(0)
        m.remove(0)
        i=i-1
print(m)
