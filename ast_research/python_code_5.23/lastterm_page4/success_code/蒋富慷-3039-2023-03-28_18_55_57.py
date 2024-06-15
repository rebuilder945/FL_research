a = eval(input())
n = min(a)
m = max(a)
while n in a:
    a.remove(n)
while m in a:
    a.remove(m)
print(a)
