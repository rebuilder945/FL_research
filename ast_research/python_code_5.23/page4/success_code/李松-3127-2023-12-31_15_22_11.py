n = int(input())
b = []
a = [x for x in range (1,n+1)]
for i in a[1:n+1]:
    b.append(i)
b.append(a[0])
print(b)


