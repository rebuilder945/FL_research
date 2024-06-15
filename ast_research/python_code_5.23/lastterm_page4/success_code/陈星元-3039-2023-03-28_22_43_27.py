list=eval(input())
list2=list[:]
list.sort(reverse=True)
while list2.count(list[0])!=0:
    list2.remove(list[0])
while list2.count(list[-1])!=0:
    list2.remove(list[-1])
print(list2)


    
