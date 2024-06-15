a = eval(input())
b = max(a)
c = min(a)
list1 = a.copy()
for i in a:
    if i == b or i ==c:
        a.remove(i)
print(a)
