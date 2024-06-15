lst=eval(input())
for i in lst[0:]:
    while lst.count(i)>=2:
        lst.remove(i)
print (lst)
