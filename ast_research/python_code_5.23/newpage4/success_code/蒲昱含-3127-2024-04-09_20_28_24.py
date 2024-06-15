a=int(input())
b=[i for i in range(1,a+1)]
d=b[0]
for i in range(a-1):
    b[i]=b[i+1]
b[a-1]=d
print(b)
