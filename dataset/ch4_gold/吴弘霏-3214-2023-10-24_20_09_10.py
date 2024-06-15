a=eval(input())
a.reverse()
b=[]
for i in range(len(a)):
    if a[i]!=0:
        b.insert(0,a[i])
    else:
        b.append(a[i])
b.reverse()
print(b)
