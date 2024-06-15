list=eval(input())
list3=list.copy()
list3.reverse()
list2=[]
for x in list3:
    if x not in list2:
        list2.append(x)
    else:
        continue
list4=list2.reverse()
print(list2)
