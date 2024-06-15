a = eval(input())
b,c = eval(input())
a = a.split(",")
d = a[b]
for i in range(c):
    a.append(d)
print(a)
