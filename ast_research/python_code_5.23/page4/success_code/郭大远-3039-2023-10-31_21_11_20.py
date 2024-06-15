list1=eval(input())
h=max(list1)
a=min(list1)
list2=[h,a]
list3=[]
for x in  list1:
    if x not in list2:
        list3.append(x)
print(list3)
