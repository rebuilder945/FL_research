lst = eval(input())
x = max(lst)
y = min(lst)
a = lst.count(x)
b = lst.count(y)
for i in range(a):
    lst.remove(x)
if not lst == 0:
    for i in range(b):
        lst.remove(y)
print(lst)

