a = list(input().split(" "))
b= list(input().split(" "))
n = int(b[0])
m = int(b[1])
c = a.copy()
a[n] = c[m]
a[m] = c[n]
print(a)

