list0=eval(input())
list0=list(list0)
list1=[]
for i in list0:
    if list0.count(i) == 1:
        if list1.count(i) != 1:
            list1.append(i)
list1.sort(reverse=False)
if len(list1)==0:
    print('False')
else:
    print(list1)
