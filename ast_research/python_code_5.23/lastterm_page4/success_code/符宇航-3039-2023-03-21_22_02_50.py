lst = eval(input())
lst.sort()
x = lst[-1]
y = lst[0]
a = lst.count(x)
b = lst.count(y)
for i in range(a):
    del lst[-1]
for i in range(b):
    del lst[0]
print(lst)

