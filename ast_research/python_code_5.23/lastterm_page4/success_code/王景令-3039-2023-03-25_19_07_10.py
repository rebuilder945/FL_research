a = eval(input())
b = a.copy()
for i in a:
    if i == min(a) or i == max(a):
        b.remove(i)
print(b)
