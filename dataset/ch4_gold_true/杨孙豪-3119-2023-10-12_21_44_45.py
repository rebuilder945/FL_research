lst=eval(input())
for i in lst:
    while lst.count(i)>1:
        lst.remove(i)
for i in lst:
    while lst.count(i)>1:
        lst.remove(i)
print(lst)

