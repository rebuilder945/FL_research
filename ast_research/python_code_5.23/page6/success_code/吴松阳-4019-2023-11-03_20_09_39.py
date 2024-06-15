a = list(eval(input()))
for x in a:
    a[x] = (a[x]+5)%10
b = a.copy()
a[0] = b[-1]
a[-1] = b[0]
a[1] = b[-2]
a[-2] = b[1]
print(a)

