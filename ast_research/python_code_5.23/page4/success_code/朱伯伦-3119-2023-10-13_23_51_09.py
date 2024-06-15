list=eval(input())
list3=list.sort(reserse=True)
list2=[]
for x in list3:
    if x not in list2:
        list2.append(x)
    else:
        continue
list4=list2.sort(reserse=True)
print(list2)
