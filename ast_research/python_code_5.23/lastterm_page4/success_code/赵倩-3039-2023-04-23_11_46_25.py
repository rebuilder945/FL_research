a = eval(input())
d = len(a)
if d<=2 and d>=0:
    print("[]")
else:
    b = max(a)
    c = min(a)
    for x in a:
        if x==c:
            a.remove(c)
        elif x==b:
            a.remove(b)
    print(a)
