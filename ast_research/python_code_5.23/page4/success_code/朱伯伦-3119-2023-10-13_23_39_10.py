list=eval(input())
list.sort(key=False)
list2=[]
for x in list:
    if x not in list2:
        list2.append(x)
    else:
        continue
list2.sort(key=False)
print(list2)
