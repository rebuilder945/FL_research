lst = eval(input())
a = min(lst)
b = max(lst)
for i in lst:
    if i==a or i==b:
        lst.remove(i)
print(lst)
