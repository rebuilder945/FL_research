ls = eval(input())
q =ls.count(0)
for x in range(q):
    ls.remove(0)
for x in range(q):
    ls.append(0)
print(ls)
