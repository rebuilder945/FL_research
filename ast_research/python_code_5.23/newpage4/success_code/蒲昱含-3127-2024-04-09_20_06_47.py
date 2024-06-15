a=int(input())
b=[c for c in range(1,a+1)]
for i in b:
    i=b[0]
    b.pop(0)
    b.append(i)
print(b)
