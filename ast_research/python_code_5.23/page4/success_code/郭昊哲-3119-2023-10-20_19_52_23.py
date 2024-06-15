a=eval(input())
b=[]
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
    else:
        pass
for i in range(len(b)):
    if a.count(b[i])>1:
        for m in range(a.count(b[i])-1):
            a.remove(b[i])
    else:
        pass
print(a)



