ls = eval(input())
lss = []
a = max(ls)
b = min(ls)
for x in ls:
    if x == a or x == b:
        lss = lss[0:]
    else:
        lss.append(x)
print(lss)
