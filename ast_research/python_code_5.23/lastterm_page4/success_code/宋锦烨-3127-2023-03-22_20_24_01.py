a=int(input())
b=[x for x in range(1,a)]
for i in b:
    b[i]=b[i-1]
print(b)
