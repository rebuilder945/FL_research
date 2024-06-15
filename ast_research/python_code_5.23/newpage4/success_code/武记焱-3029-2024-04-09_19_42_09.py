list1=eval(input())
list2=eval(input())
list3=[]
for x in list1:
    for y in list2:
        list3.append([x+y])
print(list3)
