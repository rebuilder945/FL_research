n = eval(input())
a = [n for n in range(1,n)]
b = [n for n in range(1,n)]
for i in range(n-1):
    if i >= 1:
        b[i] = a[i - 1]
    else:
        b[n-1] = a[0]
input(b)
