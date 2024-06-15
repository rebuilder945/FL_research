n = eval(input())
a = [n for n in range(1,n)]
b = [n for n in range(1,n)]
for i in range(a):
    if i >= 1:
        b[i] = a[i - 1]
    else:
        b[n] = a[0]
input(b)
