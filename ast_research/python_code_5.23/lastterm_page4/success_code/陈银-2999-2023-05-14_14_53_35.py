a = input().split(" ")
n,m = eval(input())
b = a.copy()
a[n]=b[m]
a[m]=b[n]
print(a)
