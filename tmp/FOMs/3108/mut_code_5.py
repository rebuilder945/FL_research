a = eval(input())
b = {}
c = list("".join(a))
c.sort()
for i not in c:
    b[i] = c.count(i)
for m,n in b.items():
    print("{},{} ".format(m,n))

