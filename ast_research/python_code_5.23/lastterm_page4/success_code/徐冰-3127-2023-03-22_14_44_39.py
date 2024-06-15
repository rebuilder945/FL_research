n=eval(input())
a=[x for x in range(1,n+1,1)]
b=[]
for i in range(0,n-1):
    b.append(a[i+1])
b.append(a[0])
print(b)


