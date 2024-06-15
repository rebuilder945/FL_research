a = eval(input())
b = max(a)
c = min(a)
for x in a:
    if x == b or x == c:
        a.remove(x)
print(a)
