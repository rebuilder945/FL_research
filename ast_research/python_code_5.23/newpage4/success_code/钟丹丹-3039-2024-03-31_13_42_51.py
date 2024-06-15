n = eval(input())
a=max(n)
b=min(n)
if a!=b:
    for x in n:
        if n.count(a)>0:
            n.remove(a)
    for x in n:
        if n.count(b)>0:
            n.remove(b)
    print(n)
if a==b:
    print("[]")

