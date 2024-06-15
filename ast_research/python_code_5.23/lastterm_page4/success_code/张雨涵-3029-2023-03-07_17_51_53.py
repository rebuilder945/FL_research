list1=list(input().split(","))
list2=eval(input())
list3=[]
for i in range (len(list2)):
    m=[list1[i],list2[i]]
    list3.append(m)
print(list3)
