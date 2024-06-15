n=eval(input())
a=[x for x in range(1,n+1)]
b=[]
for i in range(len(a)-1):
    b.append(a[i+1])
b.append(1)
print(b)
