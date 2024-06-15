a = eval(input())
b = max(a)
c = min(a)
while b in a or c in a:
    a.remove(c)
    a.remove(b)
print(a)
