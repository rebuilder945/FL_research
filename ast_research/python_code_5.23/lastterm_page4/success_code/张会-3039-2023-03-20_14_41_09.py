lst = eval(input())
a = min(lst)
while a in lst:
    lst.remove(a)
b = max(lst)
while b in lst:
    lst.remove(b)
print(lst)
