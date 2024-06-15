lst=eval(input())
lst1=lst.copy()
for i in lst1:
    if i==0:
        lst.remove(i)
        lst.append(0)
print(lst)




