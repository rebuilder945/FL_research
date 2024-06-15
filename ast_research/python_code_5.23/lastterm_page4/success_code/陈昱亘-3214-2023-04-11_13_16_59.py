lst=eval(input())
lst2=[x for x in lst]
for i in lst2:
    if i==0:
        lst.remove(i)
        lst.append(i)
print(lst)
