lst=eval(input())
list1=lst.copy()
for i in list1:
    if i == 0:
        lst.remove(i)
        lst.append(0)
print(lst)
