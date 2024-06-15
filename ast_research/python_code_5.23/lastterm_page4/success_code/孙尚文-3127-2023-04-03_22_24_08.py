a=input().split()
b=[x for x in range(len(a))]
c=b[0]
for y in range(0,len(b)-1):
    b[y+1]=b[y]
b[-1]=c
print(b)
