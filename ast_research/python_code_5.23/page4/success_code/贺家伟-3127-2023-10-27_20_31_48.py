n=eval(input())
a=[]
for i in range(1,n+1):
    a.append(i)
for i in range(0,n):
    a[i]=a[i+1]
print(a)
