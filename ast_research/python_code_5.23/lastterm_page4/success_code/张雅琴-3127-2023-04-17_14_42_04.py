n=eval(input())
a=[]
for i in range(1,n+1):
    a.append(i)
    del a[0]
    a.append(1)
print(a)

