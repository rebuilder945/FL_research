n = eval(input())
b = [x+1 for x in range(n)]
c = b.copy()
for i in range(n-1):
    b[i] = b[i+1]
b[n-1] = c[0]
print(b)
