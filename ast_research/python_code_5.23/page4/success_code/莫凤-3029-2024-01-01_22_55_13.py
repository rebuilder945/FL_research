list1=input().split(",")
list2=eval(input())
list3=[]
for x in range(len(list1)):
    a=[]
    a.append(list1[x])
    a.append(list2[x])
    list3.append(a)
print(list3)
