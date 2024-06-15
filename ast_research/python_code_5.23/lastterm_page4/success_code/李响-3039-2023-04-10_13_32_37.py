a = eval(input())
b = max(a)
c = min(a)
a.sort()
if b in a:
    a.remove(b)
if c in a:
    a.remove(c)
else :
    print(a)
