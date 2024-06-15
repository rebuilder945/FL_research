list=eval(input())
list2=[]
for x in list:
    if x not in list2:
        list2.append(x)
    else:
        continue
print(list2)
