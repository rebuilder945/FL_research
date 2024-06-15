list1=input().split(',')
list2=eval(input())
list3=[]
for x in range(len(list1)):
    list4=[list1[x],list2[x]]
    list3.append(list4)
print(list3)
