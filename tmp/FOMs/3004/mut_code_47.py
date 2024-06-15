list1=eval(input())
list2=[]
list3=[]
list4=[]
m=max(list1)
for x in range(2,m+1):
    for i in range(2,x):
        if x%i==0:
            list3.append(i)
        else:
            continue
    if len(list3)==0:
        list2.append(x)
    else:
        list3.clear
        
            
for a in list1:
    if a not in list2:
        list4.append(a)
    else:
        continue
print(list4)
