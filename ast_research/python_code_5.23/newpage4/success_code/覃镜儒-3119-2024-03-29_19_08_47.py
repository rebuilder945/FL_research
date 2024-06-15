i=eval(input())
b=i[:]
for a in range(len(b)):
    if b.count(a)>1:
        i.remove(a)
    else:
        pass
print(i)
