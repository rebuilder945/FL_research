a=eval(input())
b=[]
c=[]
for i in range(len(a)):
    if a[i]==0:
        b.append(a[i])
    else:
        c.append(a[i])
print(c+b)

