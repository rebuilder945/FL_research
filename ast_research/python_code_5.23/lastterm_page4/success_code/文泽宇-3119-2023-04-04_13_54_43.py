lst = eval(input())
for x in lst:
    if lst.count(x) == 1:
        None
    else:
        for i in range(1,lst.count(x)):
            lst.remove(x)
print(lst)
