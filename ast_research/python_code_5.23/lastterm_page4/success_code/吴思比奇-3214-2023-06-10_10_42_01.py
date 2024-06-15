a=list(input())
le=len(a)
b=a.count(0)
for i in range(1,b+1):
    a.remove(0)
for i in range(1,b+1):
    a.append(0)
print(a)


