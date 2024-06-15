list=eval(input())
list2=list.copy()
for x in list:
    if list2.count(x)>1:
        list2.remove(x)
    else:
        continue
print(list2)
    
