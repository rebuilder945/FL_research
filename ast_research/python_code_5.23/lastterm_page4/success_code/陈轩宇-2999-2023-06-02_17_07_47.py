a = (input()).split()
a = list(a)
n,m = eval(input())
b = a[n]
c = a[m]
a[n] = c
a[m] = b
print(a)

