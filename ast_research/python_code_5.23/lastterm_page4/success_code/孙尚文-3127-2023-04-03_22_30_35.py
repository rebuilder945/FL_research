a=eval(input())
b=[x for x in range(a)]
c=b[0]
for y in range(0,len(b)-1):
    b[y]=b[y+1]
b[-1]=c
print(b)
