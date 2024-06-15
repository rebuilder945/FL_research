a = eval(input())
b = max(a)
c = min(a)
if len(a)==1 or 0:
    print("[]")
else:
    while max(a)==b:
        a.remove(b)
    while min(a)==c:
        a.remove(c)
    print(a)
