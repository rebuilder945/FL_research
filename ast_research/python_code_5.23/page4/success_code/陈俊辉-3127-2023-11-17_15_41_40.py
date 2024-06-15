n=int(input())
a=[]
for i in range(1,n+1):
    if i not in a:
        a.append(i)
b=a.copy()
b[n-1]=a[0]
b[0]=a[n-1]
print(b)
