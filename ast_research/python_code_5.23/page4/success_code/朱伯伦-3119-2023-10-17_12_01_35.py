list=eval(input())
list.reverse()
list2=[]
for x in list:
    if x not in list2:
        list2.append(x)
    else:
        continue
list2.reverse()
print(list2)
