a=eval(input())
b=[]
for x in range(-1,-len(a)-1,-1):
    if a[x] not in b:
        b.append(a[x])
b.reverse()
print(b)
