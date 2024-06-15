ls1 = eval(input())
a = max(ls1)
b = min(ls1)
jishu = ls1.count(a)
cnt = ls1.count(b)
if jishu>=2:
    for i in range(jishu):
        ls1.remove(a)
if cnt>=2:
    for i in range(cnt):
        ls1.remove(b)
print(ls1)
