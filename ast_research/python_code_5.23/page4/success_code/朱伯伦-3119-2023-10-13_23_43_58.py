list=eval(input())
list=reserse(list)
list2=[]
for x in list:
    if x not in list2:
        list2.append(x)
    else:
        continue
list2=reserse(list2)
print(list2)
