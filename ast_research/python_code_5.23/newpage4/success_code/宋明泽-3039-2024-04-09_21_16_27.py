a = eval(input())
b = max(a)
c = min(a)
f = a.copy()
for x in a:
    if x == b or x == c:
        f.remove(x)
print(f)
