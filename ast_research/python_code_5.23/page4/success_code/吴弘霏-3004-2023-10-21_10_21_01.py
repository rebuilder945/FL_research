list=eval(input())
list1=[]
for i in range(len(list)):
    for a in range(2,list[i]):
        if list[i]==2:
            list1.append(list[i])
        elif list[i]>2 and list[i]%a!=0:
            list1.append(list[i])
print(list1)
