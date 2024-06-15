list1=eval(input())
list2=list1.copy()
i=0
for x in list1:
    if x==0:
        i+=1
        list2.remove(x)
for x in range(i):
    list2.append(0)
print(list2)
