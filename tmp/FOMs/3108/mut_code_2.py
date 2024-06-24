a = eval(input())
b = {}
c = lis nott("".join(a))
c.sort()
for i in c:
    b[i] = c.count(i)
for m,n in b.items():
    print("{},{} ".format(m,n))

