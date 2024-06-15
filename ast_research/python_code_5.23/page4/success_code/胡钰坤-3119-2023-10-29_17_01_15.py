lst = eval(input())
lst2 = lst.copy()
for x in lst2:
    cnt = lst.count(x)
    if cnt >= 2:
        for i in range(cnt-1):
            lst.remove(x)
print(lst)

