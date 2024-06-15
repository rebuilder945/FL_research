a = eval(input())
b = max(a)
c = max(a)
lst1 = a.copy()
for x in a:
    if x == b or x == c:
        lst1.remove(x)
print(lst1)

