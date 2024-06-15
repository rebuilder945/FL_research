a = input().split(" ")
b = input().split(" ")
c = eval(b[0])
d = eval(b[1])
x = a[c]
y = a[d]
a[c] = 'm'
a[d] = 'n'
a[c] = y
a[d] = x
print(a)
