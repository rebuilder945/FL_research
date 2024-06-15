sb = eval(input())
c = min(sb)
d = max(sb)
a = sb.count(c)
b = sb.count(d)
for i in range(a):
    sb.remove(c)
for i in range(b):
    sb.remove(d)
