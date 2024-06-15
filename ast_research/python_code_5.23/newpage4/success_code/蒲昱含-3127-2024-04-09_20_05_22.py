a=int(input())
b=[c for c in range(1,a+1)]
i=b(0)
for i in b:
    b.pop(0)
    b.append(i)
print(b)
