lst = eval(input())
for i in  lst[:-1]:
    for x in  lst[1:]:
        if i == x:
            lst.remove(i)
print(lst)
