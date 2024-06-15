list=eval(input())
list2=list.copy()
list3=[]
for i in list:
    if i==0:
        list2.remove(i)
        list3.append(i)
final_list=list2.extend(list3)
print(final_list) 
       

