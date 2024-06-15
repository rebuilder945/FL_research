a=int(input())
b=[c for c in range(1,a+1)]
d=b[0]
for i in b:
    b[i]=b[i+1]
    b[a-1]=d
print(b)
