a = input()
n,m = eval(input())
k = a[m]
p = a[n]
a[m] = p
a[n] = k
print(a)
