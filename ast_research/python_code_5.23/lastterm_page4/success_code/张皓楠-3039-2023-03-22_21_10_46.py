a = eval(input())
b = max(a)
b2 = a.count(b)
for i in range(b2):
    a.remove(b)
c = min(a)
c2 = a.count(c)
for i in range(c2):
    a.remove(c)
print(a)








