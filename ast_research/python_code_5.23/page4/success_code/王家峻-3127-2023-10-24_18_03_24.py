n=eval(input())
b=[x for x in range(1,n)]
b[0],b[n-2]=b[n-2],b[0]
print(b)
