list1=list(input())
list2=[]
for i in list1:
    if list1.count(i)==1:
       list2.append(i)
print(list2[0]) 
