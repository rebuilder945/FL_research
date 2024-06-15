a=eval(input())
b=[x for x in range(len(a))]
for y in range(len(b)):
    b[y+1]=b[y]
b[-1]=b[1]
print(b)
