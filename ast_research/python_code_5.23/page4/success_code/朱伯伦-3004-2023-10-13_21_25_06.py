list1=eval(input())
list2=[]
list4=[]
max=max(list1)
for x in range[2:max]:
    for i in range[2:max]:
        list3=[]
        if x%i==0:
            list3.append(i)
        else:
            continue
    if len(list3)>0:
        list2.append(x)
        
            
for i in list1:
    if i in list2:
        list4.append(i)
    else:
        continue
print(list4)

