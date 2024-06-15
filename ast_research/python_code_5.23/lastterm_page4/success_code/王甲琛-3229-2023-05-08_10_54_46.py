l1=eval(input())
l2=[]
for x in l1:
    if x not in l2:
        l2.append(x)
for i in l2:
    if i in l1:
        l1.remove(i)
for b in l1:
    if b in l2:
        l2.remove(b)
l2.sort()
print(l2)
