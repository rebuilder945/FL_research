lst = eval(input())
for i in lst:
    n = lst.count(i)
    for x in range(n-1):
        for x in range(n-1):
            lst.remove(i)
print(lst)

