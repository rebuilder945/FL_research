a=int(input())
b=[x+1 for x in range(a)]
for x in range (a-1):
    b[x]=b[x+1]
b[a-1]=1
print(b)
