list=eval(input())
list2=[]
for i in list:
    if list.count(i)==1:
        list2.append(i)
    else:
        continue
if len(list2)==0:
    print("False")
else:
    list2.sort(reverse=False)
    print(list2)

