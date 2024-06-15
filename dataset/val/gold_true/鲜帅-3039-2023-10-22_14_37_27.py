ls1 = eval(input())
ls2 = ls1.copy()
a = max(ls2)
b = min(ls2)
jishu = ls2.count(a)
cnt = ls2.count(b)
if jishu>=2:
    for i in range(jishu):
        ls1.remove(a)
else:
    ls1.remove(a)
if a!=b:
    if cnt>=2:
        for i in range(cnt):
            ls1.remove(b)
    else:
        ls1.remove(b)
print(ls1)
