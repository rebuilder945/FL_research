list1=input().split(',')
list2=eval(input())
list3=[]
for x in list1:
    for y in list2:
        list3.append([x,str(y)])
print(list3)
