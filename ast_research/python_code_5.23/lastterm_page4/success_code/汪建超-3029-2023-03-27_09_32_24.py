list1 = input().split(',')
list2 = eval(input())
list3 = []
for x in list1:
    list3.append([x,list2[i]])
    i+=1
print(list3)

