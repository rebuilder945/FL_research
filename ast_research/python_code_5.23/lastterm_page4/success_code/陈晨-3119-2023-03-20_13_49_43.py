lst=eval(input())
for x in lst:
    while lst.count(x)!=1:
        lst.remove(x)
print(lst)


