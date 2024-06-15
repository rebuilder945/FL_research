list=eval(input())
list3=list.sort(reverse=True)
list2=[]
for x in list3:
    if x not in list2:
        list2.append(x)
    else:
        continue
list4=list2.sort(reverse=True)
print(list2)
