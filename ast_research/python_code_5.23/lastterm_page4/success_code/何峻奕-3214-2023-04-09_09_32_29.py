l=eval(input())
l1=l.copy()
for x in l1[0:]:
    if x==0:
        l.remove(x)
        l.append(0)
print(l)
