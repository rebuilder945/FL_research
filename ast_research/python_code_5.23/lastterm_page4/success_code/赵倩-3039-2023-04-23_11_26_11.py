a = eval(input())
b = max(a)
c = min(a)
while max(a)==b:
    a.remove(b)
while min(a)==c:
    a.remove(c)
print(a)
