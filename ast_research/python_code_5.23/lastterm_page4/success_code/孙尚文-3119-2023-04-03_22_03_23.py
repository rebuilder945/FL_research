a=eval(input())
for x in range(len(a)-1,-1,-1):
    b=[]
    if a[x] not in b:
        b.append(a[x])
b.reverse()
print(b)
