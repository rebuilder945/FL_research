a=eval(input())
c=a.count(0)
b=[]
for i in range(len(a)):
    if a[i]==0:
        pass
    else:
        b.append(a[i])
for i in range(c):
    b.append(0)
print(b)

