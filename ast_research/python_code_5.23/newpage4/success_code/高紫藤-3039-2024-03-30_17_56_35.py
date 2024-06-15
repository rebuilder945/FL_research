a = eval(input())
max_a = max(a)
min_a = min(a)
c = a.copy()
for d in a:
    if d ==max_a or d == min_a:
        c.remove(d)
print(c)


