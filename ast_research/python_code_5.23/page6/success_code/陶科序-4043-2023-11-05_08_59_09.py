a = eval(input())
b = ""
c = []
d = []
for i in a:
    b += i
for i in b:
    d.append(i)
    if i not in c:
        c.append(i)
        c . sort()
for i in c:
    e=b.count(i)
    print(f"{i},{d}")








