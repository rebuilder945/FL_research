a=eval(input())
b=[]
for i in range(len(a)):
    if a[i]==0:
        b.append(0)
    else:
        b.append(a[i])
print(b)
