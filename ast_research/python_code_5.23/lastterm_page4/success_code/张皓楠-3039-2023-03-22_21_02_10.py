a = eval(input())
b = a.count(max(a))
for i in range(b):
    a.remove(max(a))
c = a.count(min(a))
for i in range(c):
    a.remove(min(a))







