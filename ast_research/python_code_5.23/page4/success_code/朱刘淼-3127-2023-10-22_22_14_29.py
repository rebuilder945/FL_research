n=int(input())
a=[i+1 for i in range(n)]
b=a
for m in range(n-1):
    b[m]=b[m+1]
b[n-1]=1
print(b)
    

