ls = input() or "None"
lb =[]
lc = []
for a in ls:
    b = ls.count(a)
    if b == 1:
        lb.append(a)
for x in lb:
    c = ls.index(x)
    lc.append(c)
print(lb[lc.index(min(lc))])
