sb = eval(input())
c = min(sb)
d = max(sb)
a = sb.count(c)
b = sb.count(d)
if a != 0:
    for i in range(a):
        sb.remove(c)
if b!=0:
    for i in range(b):
        sb.remove(d)
print(sb)
