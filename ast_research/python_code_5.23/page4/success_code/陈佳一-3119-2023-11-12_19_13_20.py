a=eval(input())
c=[]
for b in range(len(a)-1,-1,-1):
    if a[b] in c:
        continue
    else:
        c.append(a[b])
print(c)
