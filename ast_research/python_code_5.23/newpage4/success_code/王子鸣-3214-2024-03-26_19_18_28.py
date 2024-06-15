list1=eval(input())
list2=[x for x in list1 if x!=0]
a=list1.count(0)
list3=[x*0 for x in range(0,a)]
list2.extend(list3)
print(list2)
