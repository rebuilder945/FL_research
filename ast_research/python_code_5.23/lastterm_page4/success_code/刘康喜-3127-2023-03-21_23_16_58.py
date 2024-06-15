n=int(input())
b=[x for x in range(1,n+1)]
c=b[0]
del b[0]
b.append(c)
print(b)

