n = eval(input())
a = [n for n in range(1,n)]
for i in range(a):
    if i >= 1:
        a[i] = a[i - 1]
    else:
        a[n] = a[0]
input(a)
