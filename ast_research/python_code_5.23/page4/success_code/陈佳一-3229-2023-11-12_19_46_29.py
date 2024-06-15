a=eval(input())
b=[]
for x in range(len(a)):
    if a.count(a[x])==1:
        b.append(a[x])
b.sort()
print(",".join(str(i)for i in b))

