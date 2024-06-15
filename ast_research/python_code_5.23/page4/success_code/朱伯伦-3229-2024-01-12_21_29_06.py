list=eval(input())
list2=[]
for i in list:
    if list.count(i)==1:
        list2.append(i)
if len(list2)==0:
    print("False")
else:
    list2.sort()
    m=""
    for i in list2:
        print(i,end=',')
