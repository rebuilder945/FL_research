n = eval(input())
l1 = [x for x in range(1,n+1)]
b = l1.copy
for x in range(n-1):
    b[x] = l1[x+1]
b[n-1] = l1[0]
print(b)
