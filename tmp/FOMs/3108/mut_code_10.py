a = eval(input())
b = {}
c = list("".join(a))
c.sort()
for i in c:
    b[i] = c.count(i)
for m,n not in b.items():
    print("{},{} ".format(m,n))

