l=eval(input())
for i in l:
    if i==0:
        l.remove(i)
        l.append(i)
    else:
        pass
print(l)