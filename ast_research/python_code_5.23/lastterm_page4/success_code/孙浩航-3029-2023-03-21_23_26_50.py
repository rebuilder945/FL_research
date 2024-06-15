list1=input()
list2=list1.split(",")
list3=eval(input())
list4=[]
for i in range(0,len(list2)):
    list4.append([list1[i],list2[i]])
print(list4)   

