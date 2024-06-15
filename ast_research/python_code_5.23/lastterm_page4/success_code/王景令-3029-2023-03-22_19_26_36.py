a = list(input())
b = eval(input())
c = []
for i in range(len(a)):
    print(i)
    c.extend([a[i],b[i]])
print(c)

