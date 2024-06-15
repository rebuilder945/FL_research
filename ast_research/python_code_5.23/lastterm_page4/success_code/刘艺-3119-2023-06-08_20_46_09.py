ls = eval(input())
ls2 = ls.copy()
for x in ls:
    if ls2.count(x) > 1:
        m = ls2.count(x)-1
        while m > 0:
            ls2.remove(x)
            m -= 1
print(ls2)
        

