list1=eval(input())
list1.reverse()
list2=[]
for x in list1:
    if x not in list2:
        list2.insert(0,x)
print(list2)
