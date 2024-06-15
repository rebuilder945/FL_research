a = eval(input())
b = max(a)
c = min(a)
a.sort()
for i in range(len(a)):
    if b in a:
        a.remove(b)
    if c in a:
        a.remove(c)
print(a)
