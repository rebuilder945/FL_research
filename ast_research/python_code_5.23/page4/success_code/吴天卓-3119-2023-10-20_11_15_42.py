l=eval(input())
l1=l.copy()
for i in l:
    if l.count(i)>1:
        for a in range(l.count(i)-1):
            l1.remove(i)
        break
print(l1)
