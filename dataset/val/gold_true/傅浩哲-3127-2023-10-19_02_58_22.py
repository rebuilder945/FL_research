n=eval(input())
a=[x for x in range(1,n+1)]
b=[]
for i in range(1,n):
    b.append(a[i])
b.append(a[0])
print(b)
