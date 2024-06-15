lst = eval(input())
for i in lst:
    if lst.count(i) > 0:
        lst.remove(i)
print(lst)

