a=eval(input())
b=[]
c=[]
for i in range(len(a)):
    
    if a[i] in b:
        pass
    else:
        b.append(a[i])

    if a[i] in b:
        pass
    else:
        c.append(a[i])
c.sort()
c=str(c)
print(c)
