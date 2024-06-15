ls = eval(input())
m = ls.copy()
a = max(ls)
b = min(ls)
for i in ls:
    if i == a or i == b :
        m.remove(i)
print(m)
