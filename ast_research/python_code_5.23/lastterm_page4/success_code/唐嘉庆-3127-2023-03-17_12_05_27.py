n=eval(input())
b=[b for b in range(1,n+1)]
for i in range(n-1):
    b[i],b[i+1]=b[i+1],b[i]
print(b)
