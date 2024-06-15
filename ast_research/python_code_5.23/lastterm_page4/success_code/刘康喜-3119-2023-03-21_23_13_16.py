a=eval(input())
c=a.copy()
d=[]
for i in range(0,len(a)):
    b=a.count(a[i])
    if b>1 and a[i] not in d:
        for j in range(1,b):
            c.remove(a[i])
            d.append(a[i])
print(c)
