list=eval(input())
list2=[]
for i in list:
    if i!=0:
        list2.append(i)
    else:
        continue
n=list.count(0)
list3=[0]
list2=list2+list3*n
print(list2)
