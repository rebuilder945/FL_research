a=int(input())
b=[x for x in range(1,a+1)]
for i in b:
    b.remove(i)
    b.append(i)
print(b)
