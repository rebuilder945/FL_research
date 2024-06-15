ls = eval(input())
ls2 = ls.copy()
for x in ls:
    js = ls2.count(x)
    while js>1:
        ls2.remove(x)
        js-= 1
print(ls2)
    
