a = eval(input())
d = len(a)
if d<=2 and d>=0:
    print("[]")
else:
    b = max(a)
    c = min(a)
    while b in a and c in a:
        a.remove(b)
        a.remove(c)
    print(a)
