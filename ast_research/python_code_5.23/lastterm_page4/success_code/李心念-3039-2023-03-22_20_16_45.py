a = eval(input())
m = max(a)
n = min(a)
for i in range(a.count(m)):
    a.remove(m)
for i in range(a.count(n)):
    a.remove(n)
print(a)
