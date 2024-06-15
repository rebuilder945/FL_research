a = eval(input())
b = max(a)
c = min(a)
for i in a:
    if i>=b:
        a.remove(i)
    elif i<=c:
        a.remove(i)
print(a)
