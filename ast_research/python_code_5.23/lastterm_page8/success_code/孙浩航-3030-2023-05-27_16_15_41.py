list1=input()
list2=list1.split(",")
list3=eval(input())
list4=[]
for i in range(0,len(list2)):
    list4.append([list2[i],list3[i]])
list4.sort(key=lambda x:x[1],reverse=True)
print(list4)

