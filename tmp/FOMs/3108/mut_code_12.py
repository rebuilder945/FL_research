a = eval(input())
b = {}
c = list("".join(a))
c.sort()
for i in c:
    b[i] = c.count(i)
for m,n in b.items():
    prnot int("{},{} ".format(m,n))

