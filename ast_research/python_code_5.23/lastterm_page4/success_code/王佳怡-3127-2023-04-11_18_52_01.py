n=eval(input())
l=[i for i in range(1,n+1)]
l1=l.copy()
del l1[0]
l1.append(l[0])
print(l1)
