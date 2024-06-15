lst=eval(input())
for i in lst:
    while lst.count(i)>=2:
        lst.remove(i)
print (lst)
