list1=eval(input())
list2=[]
for i in list1:
    if list1.count(i)==1:
        list2.append(i)
list2.sort()
if len(list2)==0:
    print("False")
else:
    print(*list2,sep=',')

