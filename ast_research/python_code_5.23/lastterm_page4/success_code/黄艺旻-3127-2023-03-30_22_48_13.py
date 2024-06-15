n = InterruptedError(input())
b = list(range(1,n+1))
for i in range(1,n+1):
    if i != n and i != 1:
        b[i] = b[i+1]
    elif i == 1:
        b[i] = b[n]
    else:
        b[i] = b[1]
print(b)

