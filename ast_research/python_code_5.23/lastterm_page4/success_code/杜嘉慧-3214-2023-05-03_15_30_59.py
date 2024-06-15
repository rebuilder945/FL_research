lst = eval(input())
new = []
a = lst.count(0)
for x in lst:
    if x != 0:
        new.append(x)
new += [0] * a
print(new)




