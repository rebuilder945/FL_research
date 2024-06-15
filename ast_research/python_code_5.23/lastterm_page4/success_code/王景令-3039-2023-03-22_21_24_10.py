a = eval(input())
b = max(a)
while b in a:
    a.remove(b)
print(a)
