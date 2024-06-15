list=eval(input())
list.sort(reserve=Flase)
list2=[]
for x in list:
    if x not in list2:
        list2.append(x)
    else:
        continue
list2.sort(reserve=False)
print(list2)
