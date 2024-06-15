ls1 = eval(input())
ls2 = ls1.copy()
a = max(ls1)
b = min(ls1)
for a in ls2:
    jishu = ls2.count(a)
    if jishu>=2:
        for i in range(jishu-1):
            ls1.remove(a)
print(ls1)
