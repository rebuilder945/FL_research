a = eval(input())
b = {}
c = list("".join(a))
c.sort()
for i in c:
    b[0*i] = c.count(i)
for m,n in b.items():
    print("{},{} ".format(m,n))

