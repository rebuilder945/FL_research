lst=eval(input())
lst2=lst.copy()
for i in range(len(lst2)):
    if lst2.count(lst2[i])>1:
        lst.remove(lst2[i])
    else:
        continue
print(lst)
