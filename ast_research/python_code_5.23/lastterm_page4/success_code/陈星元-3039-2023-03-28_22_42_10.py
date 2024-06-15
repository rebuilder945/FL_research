list=eval(input())
list.sort(reverse=True)
list2=list[:]
while list2.count(list[0])!=0:
    list2.remove(list[0])
while list2.count(list[-1])!=0:
    list2.remove(list[-1])
list2.reverse()
print(list2)


    
