a = eval(input())
n = min(a)
m = max(a)
while n in a or m in a:
    a.remove(n) or a.remove(m)
print(a)
