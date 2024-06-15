a = eval(input())
b = max(a)
d = min(a)
m = a.copy()
for c in a:
    if c == b or c == d:
        m.remove(c)
print(m)

