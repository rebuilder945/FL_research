a=eval(input())
b=[]
for i in range(len(a)):
    if a[i]==0:
        b.append(0)
    else:
        b.append(a[i])
for i in range(len(b)):
    if b[i]==0:
        b.pop(i)
        b.append(0)
print(b)

