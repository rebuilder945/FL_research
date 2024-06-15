n = eval(input())
a = [n for n in range(1,n)]
b = [n for n in range(1,n)]
for i in range(n):
    if i >= 2:
        b[i - 2] = a[i - 1]
    elif i == 1:
        b[-1] = a[0]
    else:
        continue
input(b)
