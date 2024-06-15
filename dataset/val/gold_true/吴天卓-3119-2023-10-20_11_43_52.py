l=eval(input())
l1=l.copy()
for i in range(len(l)):
    b=l.count(l[i])
    if b>=2:
        l1.remove(l[i])
    l[i]=[]
print(l1)
