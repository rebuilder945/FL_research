a = eval(input())
b = max(a)
c = min(a)
for i in a:
    if i == b or i == c:
        d = a.index(i)
        a.pop(d)
print(a)
