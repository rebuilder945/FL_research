list1=eval(input())
list1.reverse
list2=[]
for i in list1:
    if list2.count(i)<1:
        list2.append(i)
list2.reverse        
print(list2)        
