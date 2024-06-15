a = list(input().split(" "))
b,c = input().split()
m = eval(b)
n = eval(c)
a[m],a[n] = a[n],a[m]
print(a)
