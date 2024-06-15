sb = eval(input())
c = min(sb)
d = max(sb)
a = sb.count(c)
b = sb.count(d)
if (a > 0 or b >0)and c!=d:
    for i in range(a):
        sb.remove(c)
    for i in range(b):
        sb.remove(d)
else:
    for i in range(a):
        sb.remove(c)
print(sb)
