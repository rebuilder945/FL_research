a = eval(input())
d = len(a)
if d<=2 and d>=0:
    print("[]")
else:
    b = max(a)
    c = min(a)
    while max(a)==b:
        a.remove(b)
    while min(a)==c:
        a.remove(c)
    print(a)
