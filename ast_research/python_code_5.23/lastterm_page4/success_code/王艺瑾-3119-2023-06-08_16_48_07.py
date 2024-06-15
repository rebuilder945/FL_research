a=eval(input())
b=[]
c=len(a)
for i in range(-1,-c-1,-1):
    if a[i] not in b:
        b.append(a[i])
b.reverse()
print(b)


