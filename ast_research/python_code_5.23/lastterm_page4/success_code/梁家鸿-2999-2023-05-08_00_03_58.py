a = input().split(" ")
c = input().split(" ")
n = eval(c[0])
m = eval(c[1])
b=a.copy()
a[n] = b[m]
a[m] = b[n]
print(a)
