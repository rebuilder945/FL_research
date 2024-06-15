a = input()
n,m = eval(input())
k = a[m]
a[m] = a[n]
a[n] = k
print(a)
