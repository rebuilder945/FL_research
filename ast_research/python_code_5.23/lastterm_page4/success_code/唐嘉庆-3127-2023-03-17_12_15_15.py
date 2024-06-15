n=eval(input())
b=[x+1 for x in range(n)]
for i in range(n-1):
    b[i]=b[i+1]
b[-1]=1
print(b)
