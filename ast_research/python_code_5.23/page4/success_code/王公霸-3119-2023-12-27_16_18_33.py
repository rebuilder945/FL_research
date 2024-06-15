lst = eval(input())
for i in lst:
    for x in lst[1:]:
        if i==x:
            lst.remove(i)
            break
print(lst)

