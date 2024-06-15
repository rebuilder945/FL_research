lst=eval(input())
lst1=lst.copy()
for i in lst1:
    while lst.count(i)>1:
        lst.remove(i)
print(lst)


    





