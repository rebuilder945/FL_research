a = eval(input())
d = len(a)
if d<=2 and d>=0:
    print("[]")
else:
    b = max(a)
    c = min(a)
    for x in a:
        if x==c or x==b:
            a.remove(c) or a.remove(b)
    print(a)
