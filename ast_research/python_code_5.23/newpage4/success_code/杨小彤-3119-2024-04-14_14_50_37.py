ls1 = eval(input())
ls = ls1.copy()
for x in ls1:
    a = ls.count(x)
    if a > 1:
        while a > 1:
            ls.remove(x)
            a-=1
print(ls)
