list=eval(input())
list1=[]
for i in range(len(list)):
    if list[i]==2:
        list1.append(list[i])
    elif list[i]/range(2,i)!=0:
        list1.append(list[i])
print(list1)
