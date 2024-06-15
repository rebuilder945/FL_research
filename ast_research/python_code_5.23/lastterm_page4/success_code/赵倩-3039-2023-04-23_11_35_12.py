a = eval(input())
if len(a)==1 or 0 or 2:
    print("[]")
else:
    b = max(a)
    c = min(a)
    while max(a)==b:
        a.remove(b)
    while min(a)==c:
        a.remove(c)
    print(a)
