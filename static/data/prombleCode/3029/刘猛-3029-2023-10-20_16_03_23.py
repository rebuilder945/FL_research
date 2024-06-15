a = input().split(",")
b = eval(input())
c = []
d = ()
for i in range(len(a)):
    d = (a[i],b[i])
    c.append(list(d))


print(c)
