a=input().split()
b=[x for x in range(len(a))]
for y in range(0,len(b)):
    b[y+1]=b[y]
b[-1]=b[1]
print(b)
