lst =[]
lst2=[]
list1 = input().split(",")
list2 = input().split(",")
for i in range(len(list1)):
    lst.append(list1[i])
    lst.append(list2[i])
    lst2.append(lst)
    lst=[]
lst2 
print(sorted(lst2,key=lambda x:(x[1],x[0])))


