a = eval(input())
m = a.count(0)
for i in range(m):
    a.remove(0)
    a.append(0)
print(a)
