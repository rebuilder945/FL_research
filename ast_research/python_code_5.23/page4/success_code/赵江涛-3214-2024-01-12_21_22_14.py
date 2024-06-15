a = eval(input())
n = a.count(0)
for i in range(n):
    a.remove(0)
    a.append(0)
print(a)
